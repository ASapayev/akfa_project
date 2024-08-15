from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from aluminiy.models import AluProfilesData,AluFile,AluminiyProduct,LengthOfProfile,BrendKraska
from pvc.models import ArtikulKomponentPVC ,NakleykaPvc,PVCFile,PVCProduct
from radiator.models import RadiatorFile,OrderRadiator as BaseOrderRadiator,ProchiyeFile,AkpFile
from .models import Anod,Order,OrderDetail
from accessuar_import.models import Category,GroupProduct
from accessuar.models import OrderACS,OrderAKP,OrderProchiye,AccessuarDownloadFile,ArtikulAccessuar
from radiator.models import ArtikulRadiator
from django.contrib.auth.decorators import login_required
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from accounts.decorators import customer_only,moderator_only,allowed_users
from django.core.paginator import Paginator
import json
import requests as rq
import base64
from .forms import OrderFileForm
from django.db.models import Q
from accounts.models import User
from django.views.decorators.csrf import csrf_exempt
import websocket
from django_eventstream import send_event
import pandas as pd
from aluminiytermo.models import ArtikulComponent,AluFileTermo,NakleykaCode,AluminiyProductTermo
import os
from config.settings import MEDIA_ROOT
from datetime import datetime
from order.models import Order as BaseOrder
from order.models import OrderPVX as BaseOrderPvc
import string
import random
from django.core.files import File
from decouple import config


# API_KEY = os.environ.get("JIRA_CREDENTIALS")
API_KEY = config('JIRA_CREDENTIALS')

credentials = "Basic " + base64.b64encode(f"{API_KEY}".encode("ascii")).decode("ascii")



headers_jira = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": credentials
}


def test(request):
    send_event("test", "message", {"text": "hello world"})
    return JsonResponse({'a':'b'})

@csrf_exempt
def user_message_receive(request):
    websocket_url ='ws://54.210.252.107:8001/ws/messages/'
    if request.method =='POST':
        data = dict(request.POST)
        chat_id = 0
        message_id =0
        user_id =1
        text =''
        owner =3
       
        

        if 'chat_id' in data:
            chat_id = data['chat_id'][0]
        if 'message_id' in data:
            message_id = data['message_id'][0]
        if 'user_id' in data:
            user_id = data['user_id'][0]
            user=''
            user.save()
        if 'text' in data:
            text = data['text'][0]
        
        data ={
            'chat_id':chat_id,
            'message_id':message_id,
            'user_id':user_id,
            'text':text,
            'msg_type':data['msg_type'][0],
            'owner':owner,
            'image':str(user.image),
            'username':user.first_name,
        }
        print(data,'<<<<<<'*10)
        websocket_url +=str(user.operator.id)+'/'
        print(websocket_url)
        send_message_to_websocket(websocket_url,data=data)
        
        return JsonResponse({'message':'Successfully saved!'})

    else:
        return JsonResponse({'msg':'GET method not allowed!'})


def send_message_to_websocket(websocket_url,data):
    print(websocket_url)
    ws = websocket.WebSocket()
    ws.connect(websocket_url)
    ws.send(json.dumps(data))
    response = ws.recv()
    # print(response)
    ws.close()

class OrderSaveView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print('come to get')
        return Response(['hello',])    
    
    def post(self, request):
        data = request.data.get('data',None)
        name = request.data.get('name',None)
        order_name = request.data.get('order_name',None)

        order_type = request.data.get('order_type',None)
        response = json.loads(data)
        artikules = []
        for key,val in response.items():
            if 'acs' not in order_type and 'akp' not in order_type and 'prochiye' not in order_type:
                artikules.append(val['base_artikul'])
            if 'segment' in val:
                if val['segment'] =='no' and 'alu_savdo' == order_type:
                    response[key]['segment'] =''
                    baza_profiley = AluProfilesData.objects.filter(data__Артикул= val['base_artikul'])[:1].get()

                    if baza_profiley.data['Сегмент'] =='Нет сегмента' and str(response[key]['is_active'])=='false':
                        baza_profiley.data['Сегмент'] = response[key]['segment']
                        baza_profiley.save()

        try:
            # issueKey = order_create_jira(order_name)
            issueKey = 'MDMtest'
            order = Order(data = {'name':name,'data':response,'artikul':artikules},owner=request.user,order_type = order_type,theme =order_name,id_for_jira=issueKey)
            order.save()
            order_detail = OrderDetail(order=order,owner=request.user)
            order_detail.save()
            print(order.created_at,'$'*250)
            ##### create jira ######
            send_event("orders", "message_new", {
                                        "id":order.id,
                                        "order_type" : name,
                                        "order_id" : issueKey,
                                        "order_name" : order.theme,
                                        "owner" : str(request.user),
                                        "checker":None,
                                        "status":"1",
                                        "created_at":order.created_at
                                        })
            return Response({'msg':'Ordered successfully!','status':201,'order_id':order.id})    
        except:
            return Response({'msg':'Something went wrong.','status':300,'order_id':None}) 





   


def jira_status_change(id,status):
    payload_jira = json.dumps({
            "transition": {
                "id": status
            }
        })
    url_jira = f"https://akfa-group.atlassian.net/rest/api/3/issue/{id}/transitions"

    response = rq.request(
        "POST",
        url_jira,
        data=payload_jira,
        headers=headers_jira
    )
    return JsonResponse({'status':'changed'})



def order_create_jira(name):
    payload_jira = json.dumps({
        "requestFieldValues": {
            "summary":name
        },
        "serviceDeskId": "11",
        "requestTypeId": "78",
        "raiseOnBehalfOf": "712020:81c47857-d7c3-4478-86af-60456c2ed63f"
    })
    url_jira = "https://akfa-group.atlassian.net/rest/servicedeskapi/request"

    response = rq.request(
        "POST",
        url_jira,
        data=payload_jira,
        headers=headers_jira
    )
    issueKey = json.loads(response.text)['issueKey']
    # print(res)
    # print(json.dumps(json.loads(response.text),
    #     sort_keys=True, indent=4, separators=(",", ": ")))
    return issueKey

@login_required(login_url='/accounts/login/')
@moderator_only
def order_list_for_zavod(request):
    orders = Order.objects.filter(Q(checker = request.user)|(Q(partner = request.user)&Q(status=10083))).order_by('-created_at')

    paginator = Paginator(orders, 15)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)

    context ={
        'orders':page_obj
    }
    return render(request,'client/moderator/order_list.html',context)
@login_required(login_url='/accounts/login/')

@allowed_users(allowed_roles=['moderator','user1'])
def order_list_for_moderator(request):
    orders = Order.objects.filter(~Q(status=10023)).order_by('-created_at')

    paginator = Paginator(orders, 15)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)


    context ={
        'orders':page_obj
    }
    return render(request,'client/moderator/order_list.html',context)

def create_folder(parent_dir,directory):
    path =os.path.join(parent_dir,directory)
    if not os.path.isdir(path):
        os.mkdir(path)

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def save_file_to_model(file_path,model):
    with open(file_path, 'rb') as file:
        my_model_instance = model
        my_model_instance.file.save(os.path.basename(file_path), File(file))
        my_model_instance.save()
        return my_model_instance.id

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['moderator','user1'])
def save_ves_of_profile(request):
    data_json = request.POST.get('data',None)
    
    data = json.loads(data_json)
    print(data)
    if data_json:
        for dat in data:
            ves_za_shtuk = float(str(dat['ves']).replace(',','.'))
            dlina = float(dat['dlina'])/1000 # metr
            ves_za_metr ='%.3f' % (float(ves_za_shtuk)/dlina)
            if not LengthOfProfile.objects.filter(artikul = dat['base_artikul'],length=dat['dlina']).exists():
                profile = LengthOfProfile(artikul = dat['base_artikul'],length=dat['dlina'],ves_za_shtuk=ves_za_shtuk,ves_za_metr=ves_za_metr)
                profile.save()
            # else:
            #     profile =  LengthOfProfile.objects.filter(artikul = dat['base_artikul'],length=dat['dlina'])[:1].get() 
          
        return JsonResponse({'status':201,'msg':'saved'})
    else:
        return JsonResponse({'status':400,'msg':'something went wrong'})
    

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['moderator','user1'])
def save_ves_of_profile_single(request):
    data_json = request.POST.get('data',None)
    
    data = json.loads(data_json)
    if data_json:
        if LengthOfProfile.objects.filter(artikul = data['artikul'],length=data['dlina']).exists():
            profile = LengthOfProfile.objects.filter(artikul = data['artikul'],length=data['dlina'])[:1].get()
            return JsonResponse({'status':201,'msg':profile.ves_za_shtuk})
        else:
            return JsonResponse({'status':400,'msg':'not exist'})
          
    else:
        return JsonResponse({'status':400,'msg':'something went wrong'})

def create_folder(parent_dir,directory):
    path =os.path.join(parent_dir,directory)
    if not os.path.isdir(path):
        os.mkdir(path)


@login_required(login_url='/accounts/login/')
@moderator_only
def moderator_convert(request,id):
    order = Order.objects.get(id=id)
    datas = order.data['data']
    name = order.data['name']
    rand_string = id_generator()
    create_folder(f'{MEDIA_ROOT}\\uploads','radiator')
    create_folder(f'{MEDIA_ROOT}\\uploads\\radiator','downloads')
    create_folder(f'{MEDIA_ROOT}\\uploads','accessuar')
    create_folder(f'{MEDIA_ROOT}\\uploads\\accessuar','downloads')
    create_folder(f'{MEDIA_ROOT}\\uploads','akp')
    create_folder(f'{MEDIA_ROOT}\\uploads\\akp','downloads')
    create_folder(f'{MEDIA_ROOT}\\uploads','prochiye')
    create_folder(f'{MEDIA_ROOT}\\uploads\\prochiye','downloads')

    print(name,'<<<'*7)

    if name in ['ALUMINIY SAVDO','ALUMINIY EXPORT','ALUMINIY IMZO'] :
        df_simple, df_termo , correct, artikul_list = json_to_excel_alumin(datas,name)

        if not correct:
            context ={
                'artikules':artikul_list
            }
            return render(request,'client/moderator/artikul_component.html',context)

        path_alu_termo = f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\downloads\\SHABLON_ALUMINIY_{rand_string}.xlsx'
        path_alu_simple = f'{MEDIA_ROOT}\\uploads\\aluminiy\\downloads\\SHABLON_{rand_string}.xlsx'
        
        is_column_empty_simple = (df_simple['Краткий текст товара'] == "").all()
        is_column_empty_termo = (df_termo['Краткий текст товара'] == "").all()

       
        if not is_column_empty_simple:
            df_simple.to_excel(path_alu_simple, index = False)
            oid = save_file_to_model(path_alu_simple,AluFile())
            is_1101 = request.GET.get('for1101','off')
            is_1201 = request.GET.get('for1201','off')
            is_1112 = request.GET.get('for1112','off')
            print(is_1101,is_1201,is_1112,'sstttatus')
            o_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                        
            paths ={
                        'obichniy_file':path_alu_simple,
                        'oid':oid,
                        'obichniy_date':o_created_at,
                        'is_obichniy':'yes',
                        'type':'Обычный',
                        'status_l':'on hold',
                        'status_raz':'on hold',
                        'status_zip':'on hold',
                        'status_norma':'on hold',
                        'status_text_l':'on hold',
                        'status_norma_lack':'on hold',
                        'status_texcarta':'on hold',
                        'is_1101':is_1101,
                        'is_1201':is_1201,
                        'is_1112':is_1112,

                    }
                
            order = BaseOrder(title = name,owner=request.user,current_worker_id= request.user.id,aluminiy_worker_id =request.user.id,paths=paths,order_type =1)
            order.save()

        if not is_column_empty_termo:
            df_termo.to_excel(path_alu_termo, index = False)
            oid = save_file_to_model(path_alu_termo,AluFileTermo())
            is_1101 = request.GET.get('for1101','off')
            is_1201 = request.GET.get('for1201','off')
            is_1112 = request.GET.get('for1112','off')
            print(is_1101,is_1201,is_1112,'sstttatus')
            o_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                        
            paths ={
                    'termo_file':path_alu_termo,
                    'oid':oid,
                    'obichniy_date':o_created_at,
                    'is_obichniy':'no',
                    'type':'ТЕРМО',
                    'status_l':'on hold',
                    'status_raz':'on hold',
                    'status_zip':'on hold',
                    'status_norma':'on hold',
                    'status_text_l':'on hold',
                    'status_norma_lack':'on hold',
                    'status_texcarta':'on hold',
                    'is_1101':is_1101,
                    'is_1201':is_1201,
                    'is_1112':is_1112,
                }
            
            order = BaseOrder(title = name,owner=request.user,current_worker_id= request.user.id,aluminiy_worker_id =request.user.id,paths=paths,order_type =2)
            order.save()
        return redirect('order')   
    elif name in ['PVC SAVDO','PVC EXPORT','PVC IMZO']:
        df_pvc = json_to_excel_pvc(datas)
        path_pvc = f'{MEDIA_ROOT}\\uploads\\pvc\\downloads\\SHABLON_PVC_{rand_string}.xlsx'
        df_pvc.to_excel(path_pvc, index = False)
       
        oid = save_file_to_model(path_pvc,PVCFile())
        o_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                        
        paths ={
                    'pvc_file':path_pvc,
                    'oid':oid,
                    'obichniy_date':o_created_at,
                    'is_obichniy':'yes',
                    'type':'PVC',
                    'status_l':'on hold',
                    'status_raz':'on hold',
                    'status_zip':'on hold',
                    'status_norma':'on hold',
                    'status_text_l':'on hold',
                    'status_norma_lack':'on hold',
                    'status_texcarta':'on hold',
                }
            
        order = BaseOrderPvc(title = name,owner=request.user,current_worker_id= request.user.id,pvc_worker_id =request.user.id,paths=paths,order_type =2)
        order.save()
        return redirect('order_detail_pvc',id=order.id)
    elif name in ['RADIATOR']:
        df_radiator = json_to_excel_radiator(datas)
        path_radiator = f'{MEDIA_ROOT}\\uploads\\radiator\\downloads\\SHABLON_RADIATOR_{rand_string}.xlsx'
        df_radiator.to_excel(path_radiator, index = False)
        
        oid = save_file_to_model(path_radiator,RadiatorFile(file_type='radiator'))
        o_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                        
        paths ={
                    'radiator_file':path_radiator,
                    'oid':oid,
                    'obichniy_date':o_created_at,
                    'is_obichniy':'yes',
                    'type':'RADIATOR',
                    'status_l':'on hold',
                    'status_raz':'on hold',
                    'status_zip':'on hold',
                    'status_norma':'on hold',
                    'status_text_l':'on hold',
                    'status_norma_lack':'on hold',
                    'status_texcarta':'on hold',
                }
            
        order = BaseOrderRadiator(title = name,owner=request.user,current_worker_id= request.user.id,radiator_worker_id =request.user.id,paths=paths,order_type =2)
        order.save()
        return redirect('order_detail_radiator',id=order.id)  
    elif name in ['RADIATOR EXPORT']:
        df_radiator = json_to_excel_radiator_export(datas)
        path_radiator = f'{MEDIA_ROOT}\\uploads\\radiator\\downloads\\SHABLON_RADIATOR_EXPORT_{rand_string}.xlsx'
        df_radiator.to_excel(path_radiator, index = False)
      
        oid = save_file_to_model(path_radiator,RadiatorFile(file_type='radiator_export'))
        o_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                        
        paths ={
                    'radiator_file':path_radiator,
                    'oid':oid,
                    'obichniy_date':o_created_at,
                    'is_obichniy':'yes',
                    'type':'RADIATOR EXPORT',
                    'status_l':'on hold',
                    'status_raz':'on hold',
                    'status_zip':'on hold',
                    'status_norma':'on hold',
                    'status_text_l':'on hold',
                    'status_norma_lack':'on hold',
                    'status_texcarta':'on hold',
                }
            
        order = BaseOrderRadiator(title = name,owner=request.user,current_worker_id= request.user.id,radiator_worker_id =request.user.id,paths=paths,order_type =2)
        order.save()
        return redirect('order_detail_radiator',id=order.id)
    elif name in ['ACCESSUAR SAVDO','ACCESSUAR IMZO','ACCESSUAR EXPORT','ACCESSUAR IMPORT']:
        df_accessuar = json_to_excel_accessuar(datas,order_name=name)
        path_accessuar = f'{MEDIA_ROOT}\\uploads\\accessuar\\downloads\\SHABLON_ACCESSUAR_{rand_string}.xlsx'
        df_accessuar.to_excel(path_accessuar, index = False)
      
        oid = save_file_to_model(path_accessuar,AccessuarDownloadFile())
        o_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                        
        paths ={
                    'accessuar_file':path_accessuar,
                    'oid':oid,
                    'obichniy_date':o_created_at,
                    'is_obichniy':'yes',
                    'type':'ACCESSUAR',
                    'status_l':'on hold',
                    'status_raz':'on hold',
                    'status_zip':'on hold',
                    'status_norma':'on hold',
                    'status_text_l':'on hold',
                    'status_norma_lack':'on hold',
                    'status_texcarta':'on hold',
                }
            
        order = OrderACS(title = name,owner=request.user,current_worker_id= request.user.id,worker_id =request.user.id,paths=paths,order_type =1)
        order.save()
        return redirect('order_detail_accessuar',id=order.id)
    elif name in ['AKP SAVDO']:
        df_akp = json_to_excel_akp(datas)
        path_akp = f'{MEDIA_ROOT}\\uploads\\akp\\downloads\\SHABLON_AKP_{rand_string}.xlsx'
        df_akp.to_excel(path_akp, index = False)
      
        oid = save_file_to_model(path_akp,AkpFile(file_type='akp'))
        o_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                        
        paths ={
                    'akp_file':path_akp,
                    'oid':oid,
                    'obichniy_date':o_created_at,
                    'is_obichniy':'yes',
                    'type':'AKP EXPORT',
                    'status_l':'on hold',
                    'status_raz':'on hold',
                    'status_zip':'on hold',
                    'status_norma':'on hold',
                    'status_text_l':'on hold',
                    'status_norma_lack':'on hold',
                    'status_texcarta':'on hold',
                }
            
        order = OrderAKP(title = name,owner=request.user,current_worker_id= request.user.id,worker_id =request.user.id,paths=paths,order_type =1)
        order.save()
        return redirect('order_detail_akp',id=order.id)
    elif name in ['PROCHIYE']:
        df_prochiye = json_to_excel_prochiye(datas)
        path_prochiye = f'{MEDIA_ROOT}\\uploads\\prochiye\\downloads\\SHABLON_PROCHIYE_{rand_string}.xlsx'
        df_prochiye.to_excel(path_prochiye, index = False)
      
        oid = save_file_to_model(path_prochiye,ProchiyeFile(file_type='prochiye'))
        o_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                        
        paths ={
                    'prochiye_file':path_prochiye,
                    'oid':oid,
                    'obichniy_date':o_created_at,
                    'is_obichniy':'yes',
                    'type':'AKP EXPORT',
                    'status_l':'on hold',
                    'status_raz':'on hold',
                    'status_zip':'on hold',
                    'status_norma':'on hold',
                    'status_text_l':'on hold',
                    'status_norma_lack':'on hold',
                    'status_texcarta':'on hold',
                }
            
        order = OrderProchiye(title = name,owner=request.user,current_worker_id= request.user.id,worker_id =request.user.id,paths=paths,order_type =1)
        order.save()
        return redirect('order_detail_prochiye',id=order.id)


def json_to_excel_prochiye(datas):
    df_prochiye  = pd.DataFrame()

    df_prochiye['counter'] =['' for x in range(0,len(datas))]

    df_prochiye['Дата добавления цены'] = ''
    df_prochiye['Цена за БЕИ с ндс'] = ''
    df_prochiye['Цена за БЕИ без ндс'] = ''
    df_prochiye['Online savdo ID'] = ''
    df_prochiye['Название'] = ''
    df_prochiye['Цвет продукта'] = ''
    df_prochiye['Группа закупок'] = ''
    df_prochiye['Группа'] = ''
    df_prochiye['Тип'] = ''
    df_prochiye['Сегмент'] = ''
    df_prochiye['Бухгал товары'] = ''
    df_prochiye['Бухгалтерская цена'] = ''
    df_prochiye['Бухгалтерский учет'] = ''
    df_prochiye['Базовый единица'] = ''
    df_prochiye['Альтер единица'] = ''
    df_prochiye['Стмость баз едн'] = ''
    df_prochiye['Альтер. стоимость единицы'] = ''
    df_prochiye['Статус'] = ''
    df_prochiye['Завод'] = ''
    df_prochiye['Тип клиента'] = ''
    df_prochiye['Комментария'] = ''
    
    k = 0
    for key1,data in datas.items():
        df_prochiye['Дата добавления цены'][k] = data['pickupdate']
        df_prochiye['Цена за БЕИ с ндс'][k] = data['sena_c_nds']
        df_prochiye['Цена за БЕИ без ндс'][k] = data['sena_bez_nds']
        df_prochiye['Online savdo ID'][k] = data['online_id']
        df_prochiye['Название'][k] = data['nazvaniye_ruchnoy']
        df_prochiye['Цвет продукта'][k] = data['svet_product']
        df_prochiye['Группа закупок'][k] = data['group_zakup']
        df_prochiye['Группа'][k] = data['group']
        df_prochiye['Тип'][k] = data['tip']
        df_prochiye['Сегмент'][k] = data['segment']
        df_prochiye['Бухгал товары'][k] = data['buxgalter_tovar']
        df_prochiye['Бухгалтерская цена'][k] = data['buxgalter_sena']
        df_prochiye['Бухгалтерский учет'][k] = data['buxgalter_uchot']
        df_prochiye['Базовый единица'][k] = data['bazoviy_edin']
        df_prochiye['Альтер единица'][k] = data['alter_edin']
        df_prochiye['Стмость баз едн'][k] = data['stoimost_baza']
        df_prochiye['Альтер. стоимость единицы'][k] = data['stoimost_alter']
        df_prochiye['Статус'][k] = data['status_online']
        df_prochiye['Завод'][k] = data['zavod']
        df_prochiye['Тип клиента'][k] = data['tip_clenta']
        df_prochiye['Комментария'][k] = data['comment']
        
        k+=1

    del df_prochiye['counter']
    return df_prochiye



def json_to_excel_akp(datas):
    df_akp  = pd.DataFrame()

    df_akp['counter'] =['' for x in range(0,len(datas))]

    df_akp['Бренд'] = ''
    df_akp['Микрон'] = ''
    df_akp['Сторонность'] = ''
    df_akp['Код цвета'] = ''
    df_akp['Название цвета'] = ''
    df_akp['Тип панели'] = ''
    df_akp['Длина (мм)'] = ''
    df_akp['Ширина'] = ''
    df_akp['Группа материалов'] = ''
    df_akp['Краткий текст товара'] = ''
    df_akp['SAP Код вручную (вставляется вручную)'] = ''
    df_akp['Краткий текст товара (вставляется вручную)'] = ''
    df_akp['Место для комментариев'] = ''
    df_akp['Дата добавление цены'] = ''
    df_akp['Цена с НДС'] = ''
    df_akp['Цена без НДС'] = ''
    df_akp['Online savdo ID'] = ''
    df_akp['Название'] = ''
    df_akp['Цвет продукта'] = ''
    df_akp['Группа закупок'] = ''
    df_akp['Группа'] = ''
    df_akp['Тип'] = ''
    df_akp['Сегмент'] = ''
    df_akp['Бухгал товары'] = ''
    df_akp['Бухгалтерский учет'] = ''
    df_akp['Базовый единица'] = ''
    df_akp['Альтер единица'] = ''
    df_akp['Статус'] = ''
    df_akp['Завод'] = ''
    df_akp['Акфа дилерда очиш керак'] = ''
    df_akp['Тип клиента'] = ''
    
    
    k = 0
    for key1,data in datas.items():
        df_akp['Бренд'][k] = data['brend']
        df_akp['Микрон'][k] = data['mikron']
        df_akp['Сторонность'][k] = data['storonnost']
        df_akp['Код цвета'][k] = data['kod_sveta']
        df_akp['Название цвета'][k] = data['naz_sveta']
        df_akp['Тип панели'][k] = data['tip_paneli']
        df_akp['Длина (мм)'][k] = data['dlina']
        df_akp['Ширина'][k] = data['shirina']
        df_akp['Группа материалов'][k] = data['gruppa_materialov']
        df_akp['Краткий текст товара'][k] = data['kratkiy_tekst']
        df_akp['SAP Код вручную (вставляется вручную)'][k] = data['sap_code']
        df_akp['Краткий текст товара (вставляется вручную)'][k] = data['krat']
        df_akp['Место для комментариев'][k] = data['comment']
        df_akp['Дата добавление цены'][k] = data['pickupdate']
        df_akp['Цена с НДС'][k] = data['sena_c_nds']
        df_akp['Цена без НДС'][k] = data['sena_bez_nds']
        df_akp['Online savdo ID'][k] = data['online_id']
        df_akp['Название'][k] = data['nazvaniye_ruchnoy']
        df_akp['Цвет продукта'][k] = data['svet_product']
        df_akp['Группа закупок'][k] = data['group_zakup']
        df_akp['Группа'][k] = data['group']
        df_akp['Тип'][k] = data['tip']
        df_akp['Сегмент'][k] = data['segment']
        df_akp['Бухгал товары'][k] = data['buxgalter_tovar']
        df_akp['Бухгалтерский учет'][k] = data['buxgalter_uchot']
        df_akp['Базовый единица'][k] = data['bazoviy_edin']
        df_akp['Альтер единица'][k] = data['alter_edin']
        df_akp['Статус'][k] = data['status_online']
        df_akp['Завод'][k] = data['zavod_name']
        df_akp['Акфа дилерда очиш керак'][k] = data['diller']
        df_akp['Тип клиента'][k] = data['tip_clenta']
        
        k+=1

    del df_akp['counter']
    return df_akp




def json_to_excel_accessuar(datas,order_name):
    df_accessuar  = pd.DataFrame()

    df_accessuar['counter'] =['' for x in range(0,len(datas))]

    if order_name =='ACCESSUAR SAVDO':

        df_accessuar['Дата добавления цены'] = ''
        df_accessuar['Цена за БЕИ'] = ''
        df_accessuar['Online savdo ID'] = ''
        df_accessuar['Название'] = ''
        df_accessuar['Цвет продукта'] = ''
        df_accessuar['Группа закупок'] = ''
        df_accessuar['Группа'] = ''
        df_accessuar['Тип'] = ''
        df_accessuar['Сегмент'] = ''
        df_accessuar['Бухгал товары'] = ''
        df_accessuar['Бухгалтерский учет'] = ''
        df_accessuar['Базовый единица'] = ''
        df_accessuar['Альтер единица'] = ''
        df_accessuar['Стмость баз едн'] = ''
        df_accessuar['Альтер. стоимость единицы'] = ''
        df_accessuar['Статус'] = ''
        df_accessuar['Завод'] = ''
        df_accessuar['Тип клиента'] = ''
    
    
        k = 0
        for key1,data in datas.items():
            df_accessuar['Дата добавления цены'][k] = data['pickupdate']
            df_accessuar['Цена за БЕИ'][k] = data['sena_za_bei']
            df_accessuar['Online savdo ID'][k] = data['online_id']
            df_accessuar['Название'][k] = data['nazvaniye_ruchnoy']
            df_accessuar['Цвет продукта'][k] = data['svet_product']
            df_accessuar['Группа закупок'][k] = data['group_zakup']
            df_accessuar['Группа'][k] = data['group']
            df_accessuar['Тип'][k] = data['tip']
            df_accessuar['Сегмент'][k] = data['segment']
            df_accessuar['Бухгал товары'][k] = data['buxgalter_tovar']
            df_accessuar['Бухгалтерский учет'][k] = data['buxgalter_uchot']
            df_accessuar['Базовый единица'][k] = data['bazoviy_edin']
            df_accessuar['Альтер единица'][k] = data['alter_edin']
            df_accessuar['Стмость баз едн'][k] = data['stoimost_baza']
            df_accessuar['Альтер. стоимость единицы'][k] = data['stoimost_alter']
            df_accessuar['Статус'][k] = data['status_online']
            df_accessuar['Завод'][k] = data['zavod']
            df_accessuar['Тип клиента'][k] = data['tip_clenta']
    
            
            k+=1

   
    
    if order_name =='ACCESSUAR IMZO':

        df_accessuar['SAP код'] = ''
        df_accessuar['Название товаров (40 симвлов)'] = ''
        df_accessuar['Полное название товара'] = ''
        df_accessuar['Цена материала (СУМ)'] = ''
        df_accessuar['Базовая единица измерения'] = ''
        df_accessuar['GOODS_GROUP'] = ''
        df_accessuar['TEX_NAME'] = ''
        df_accessuar['Коеффициент пересчета'] = ''
        df_accessuar['Альтернативная единица измерения'] = ''
        df_accessuar['ID KLAES'] = ''
        df_accessuar['Группма Материалов'] = ''
        df_accessuar['Комментария'] = ''
        
    
    
        k = 0
        for key1,data in datas.items():
            df_accessuar['SAP код'][k] = data['sapcode']
            df_accessuar['Название товаров (40 симвлов)'][k] = data['nazvaniye_tovarov']
            df_accessuar['Полное название товара'][k] = data['polnoye_nazvaniye']
            df_accessuar['Цена материала (СУМ)'][k] = data['sena_materiala']
            df_accessuar['Базовая единица измерения'][k] = data['bazoviy_edinitsa']
            df_accessuar['GOODS_GROUP'][k] = data['goods_group']
            df_accessuar['TEX_NAME'][k] = data['tex_name']
            df_accessuar['Коеффициент пересчета'][k] = data['koefitsiyent']
            df_accessuar['Альтернативная единица измерения'][k] = data['alternativ_edin']
            df_accessuar['ID KLAES'][k] = data['id_klaes']
            df_accessuar['Группма Материалов'][k] = data['gruppa_materialov']
            df_accessuar['Комментария'][k] = data['comment']
            
    
            
            k+=1

   
    
    if order_name =='ACCESSUAR EXPORT':

        df_accessuar['SAP код'] = ''
        df_accessuar['Название товаров (40 симвлов)'] = ''
        df_accessuar['Полное название товара'] = ''
        df_accessuar['Цена материала (СУМ)'] = ''
        df_accessuar['Базовая единица измерения'] = ''
        df_accessuar['Коеффициент пересчета'] = ''
        df_accessuar['Альтернативная единица измерения'] = ''
        df_accessuar['Группма Материалов'] = ''
        df_accessuar['Комментария'] = ''
        
    
    
        k = 0
        for key1,data in datas.items():
            df_accessuar['SAP код'][k] = data['sapcode']
            df_accessuar['Название товаров (40 симвлов)'][k] = data['nazvaniye_tovarov']
            df_accessuar['Полное название товара'][k] = data['polnoye_nazvaniye']
            df_accessuar['Цена материала (СУМ)'][k] = data['sena_materiala']
            df_accessuar['Базовая единица измерения'][k] = data['bazoviy_edinitsa']
            df_accessuar['Коеффициент пересчета'][k] = data['koefitsiyent']
            df_accessuar['Альтернативная единица измерения'][k] = data['alternativ_edin']
            df_accessuar['Группма Материалов'][k] = data['gruppa_materialov']
            df_accessuar['Комментария'][k] = data['comment']
            
    
            
            k+=1

   
    if order_name =='ACCESSUAR IMPORT':

        df_accessuar['Артикул'] = ''
        df_accessuar['Группа товар'] = ''
        df_accessuar['Категория'] = ''
        df_accessuar['Названия материала'] = ''
        df_accessuar['Цвет'] = ''
        df_accessuar['БЕИ'] = ''
        df_accessuar['АЕИ'] = ''
        df_accessuar['Коэффициент пересчета'] = ''
        df_accessuar['SAP CODE'] = ''
        df_accessuar['Дата добавление цены'] = ''
        df_accessuar['Цена с ндс'] = ''
        df_accessuar['Цена без ндс'] = ''
        df_accessuar['Ед.изм цены'] = ''
        df_accessuar['Online savdo ID'] = ''
        df_accessuar['Название'] = ''
        df_accessuar['Цвет продукта'] = ''
        df_accessuar['Группа закупок'] = ''
        df_accessuar['Группа'] = ''
        df_accessuar['Тип'] = ''
        df_accessuar['Сегмент'] = ''
        df_accessuar['Базовый единица'] = ''
        df_accessuar['Альтер единица'] = ''
        df_accessuar['Стмость баз едн'] = ''
        df_accessuar['Альтер. стоимость единицы'] = ''
        df_accessuar['Статус'] = ''
        df_accessuar['Завод'] = ''
        df_accessuar['Тип клиента'] = ''
        df_accessuar['Комментария'] = ''
        
        
    
    
        k = 0
        for key1,data in datas.items():
            df_accessuar['Артикул'][k] = data['artikul']
            df_accessuar['Группа товар'][k] = data['group_tovarov']
            df_accessuar['Категория'][k] = data['categoriya']
            df_accessuar['Названия материала'][k] = data['nazvaniye_materiala']
            df_accessuar['Цвет'][k] = data['svet']
            df_accessuar['БЕИ'][k] = data['bei']
            df_accessuar['АЕИ'][k] = data['aei']
            df_accessuar['Коэффициент пересчета'][k] = data['koefitsiyent']
            df_accessuar['SAP CODE'][k] = data['sap_code']
            df_accessuar['Дата добавление цены'][k] = data['pickupdate']
            df_accessuar['Цена с ндс'][k] = data['sena_c_nds']
            df_accessuar['Цена без ндс'][k] = data['sena_bez_nds']
            df_accessuar['Ед.изм цены'][k] = data['edizm']
            df_accessuar['Online savdo ID'][k] = data['online_id']
            df_accessuar['Название'][k] = data['nazvaniye_ruchnoy']
            df_accessuar['Цвет продукта'][k] = data['svet_product']
            df_accessuar['Группа закупок'][k] = data['group_zakup']
            df_accessuar['Группа'][k] = data['group']
            df_accessuar['Тип'][k] = data['tip']
            df_accessuar['Сегмент'][k] = data['segment']
            df_accessuar['Базовый единица'][k] = data['bazoviy_edin']
            df_accessuar['Альтер единица'][k] = data['alter_edin']
            df_accessuar['Стмость баз едн'][k] = data['stoimost_baza']
            df_accessuar['Альтер. стоимость единицы'][k] = data['stoimost_alter']
            df_accessuar['Статус'][k] = data['status_online']
            df_accessuar['Завод'][k] = data['zavod']
            df_accessuar['Тип клиента'][k] = data['tip_clenta']
            df_accessuar['Комментария'][k] = data['comment']
            
            k+=1

   
    del df_accessuar['counter']
   
    return df_accessuar

def json_to_excel_radiator_export(datas):
    df_radiator  = pd.DataFrame()

    df_radiator['counter'] =['' for x in range(0,len(datas))]

    df_radiator['Модель'] = ''
    df_radiator['Артикул'] = ''
    df_radiator['Количество секций'] = ''
    df_radiator['Цвет'] = ''
    df_radiator['Бренд'] = ''
    df_radiator['Краткий текст'] = ''
    df_radiator['Комментарий'] = ''
    
    
    k = 0
    for key1,data in datas.items():
        df_radiator['Модель'][k] = data['model']
        df_radiator['Артикул'][k] = data['base_artikul']
        df_radiator['Количество секций'][k] = data['kol_section']
        df_radiator['Цвет'][k] = data['svet']
        df_radiator['Бренд'][k] = data['brend']
        df_radiator['Краткий текст'][k] = data['kratkiy_tekst']
        df_radiator['Комментарий'][k] = data['comment']
        
        k+=1
    del df_radiator['counter']
   
    return df_radiator






def json_to_excel_radiator(datas):
    df_radiator  = pd.DataFrame()

    df_radiator['counter'] =['' for x in range(0,len(datas))]

    df_radiator['Модель'] = ''
    df_radiator['Артикул'] = ''
    df_radiator['Количество секций'] = ''
    df_radiator['Цвет'] = ''
    df_radiator['Бренд'] = ''
    df_radiator['Краткий текст'] = ''
    df_radiator['Комментарий'] = ''
    df_radiator['Дата добавление цены'] = ''
    df_radiator['Цена с НДС'] = ''
    df_radiator['Цена без НДС'] = ''
    df_radiator['Online savdo ID'] = ''
    df_radiator['Название'] = ''
    df_radiator['Цвет продукта'] = ''
    df_radiator['Группа закупок'] = ''
    df_radiator['Группа'] = ''
    df_radiator['Тип'] = ''
    df_radiator['Сегмент'] = ''
    df_radiator['Бухгал товары'] = ''
    df_radiator['Бухгалтерская цена'] = ''
    df_radiator['Бухгалтерский учет'] = ''
    df_radiator['Базовый единица'] = ''
    df_radiator['Альтер единица'] = ''
    df_radiator['Стоимость базовой единицы'] = ''
    df_radiator['Альтер. стоимость единицы'] = ''
    df_radiator['Статус'] = ''
    df_radiator['Завод'] = ''
    df_radiator['Тип клиента'] = ''
    
    
    
    k = 0
    for key1,data in datas.items():
        df_radiator['Модель'][k] = data['model']
        df_radiator['Артикул'][k] = data['base_artikul']
        df_radiator['Количество секций'][k] = data['kol_section']
        df_radiator['Цвет'][k] = data['svet']
        df_radiator['Бренд'][k] = data['brend']
        df_radiator['Краткий текст'][k] = data['kratkiy_tekst']
        df_radiator['Комментарий'][k] = data['comment']
        df_radiator['Дата добавление цены'][k] = data['pickupdate']
        df_radiator['Цена с НДС'][k] = data['sena_c_nds']
        df_radiator['Цена без НДС'][k] = data['sena_bez_nds']
        df_radiator['Online savdo ID'][k] = data['online_id']
        df_radiator['Название'][k] = data['nazvaniye_ruchnoy']
        df_radiator['Цвет продукта'][k] = data['svet_product']
        df_radiator['Группа закупок'][k] = data['group_zakup']
        df_radiator['Группа'][k] = data['group']
        df_radiator['Тип'][k] = data['tip']
        df_radiator['Сегмент'][k] = data['segment']
        df_radiator['Бухгал товары'][k] = data['buxgalter_tovar']
        df_radiator['Бухгалтерский учет'][k] = data['buxgalter_uchot']
        df_radiator['Базовый единица'][k] = data['bazoviy_edin']
        df_radiator['Альтер единица'][k] = data['alter_edin']
        df_radiator['Стоимость базовой единицы'][k] = data['stoimost_baza']
        df_radiator['Альтер. стоимость единицы'][k] = data['stoimost_alter']
        df_radiator['Статус'][k] = data['status_online']
        df_radiator['Завод'][k] = data['zavod_name']
        df_radiator['Тип клиента'][k] = data['tip_clenta']
        k+=1

    del df_radiator['counter']
    return df_radiator

def json_to_excel_pvc(datas):
    df_pvc  = pd.DataFrame()

    df_pvc['counter'] =['' for x in range(0,len(datas)+4)]

    df_pvc['Название системы'] = ''
    df_pvc['Количество камер'] = ''
    df_pvc['Артикул'] = ''
    df_pvc['Код к компоненту системы'] = ''
    df_pvc['Тип покрытия'] = ''
    df_pvc['Код цвета основы/Замес'] = ''
    df_pvc['Длина (мм)'] = ''
    df_pvc['Цвет лам пленки снаружи'] = ''
    df_pvc['Код лам пленки снаружи'] = ''
    df_pvc['Цвет лам пленки внутри'] = ''
    df_pvc['Код лам пленки внутри'] = ''
    df_pvc['Код резины'] = ''
    df_pvc['Цвет резины'] = ''
    df_pvc['Код наклейки'] = ''
    df_pvc['Надпись наклейки'] = ''
    df_pvc['Группа материалов'] = ''
    df_pvc['Краткий текст'] = ''
    df_pvc['SAP Код вручную (вставится вручную)'] = ''
    df_pvc['Краткий текст товара (вставится вручную)'] = ''
    df_pvc['Online savdo ID'] = ''
    df_pvc['Название'] = ''
    
    k = 0
    for key1,data in datas.items():
        df_pvc['Название системы'][k] = data['nazvaniye_system']
        df_pvc['Количество камер'][k] = data['camera']
        df_pvc['Артикул'][k] = data['base_artikul']
        df_pvc['Код к компоненту системы'][k] = data['kod_k_component']
        df_pvc['Тип покрытия'][k] = data['tip_pokritiya']
        df_pvc['Код цвета основы/Замес'][k] = data['kod_svet_zames']
        df_pvc['Длина (мм)'][k] = data['dlina']
        df_pvc['Цвет лам пленки снаружи'][k] = data['svet_lamplonka_snaruji']
        df_pvc['Код лам пленки снаружи'][k] = data['kod_lam_sn']
        df_pvc['Цвет лам пленки внутри'][k] = data['svet_lamplonka_vnutri']
        df_pvc['Код лам пленки внутри'][k] = data['kod_lam_vn']
        df_pvc['Код резины'][k] = data['kod_svet_rezini']
        df_pvc['Цвет резины'][k] = data['svet_rezin']
        df_pvc['Код наклейки'][k] = data['kod_nakleyki']
        df_pvc['Надпись наклейки'][k] = data['nadpis_nakleyki']
        df_pvc['Группа материалов'][k] = 'PVCGP'
        df_pvc['Краткий текст'][k] = data['kratkiy_tekst']
        df_pvc['SAP Код вручную (вставится вручную)'][k] = data['sap_code']
        df_pvc['Краткий текст товара (вставится вручную)'][k] = data['krat']
        if 'online_id' in data:
            df_pvc['Online savdo ID'][k] = data['online_id']
            df_pvc['Название'][k] = data['nazvaniye_ruchnoy']
        k+=1
        
    del df_pvc['counter']
   
    return df_pvc


def json_to_excel_alumin(datas,name):
    df_termo  = pd.DataFrame()
    df_termo['counter'] =['' for x in range(0,len(datas)*4)]
    df_termo['Название системы'] =''
    df_termo['Артикул'] =''
    df_termo['Компонент'] =''
    df_termo['Длина (мм)'] =''
    df_termo['Тип покрытия'] =''
    df_termo['Сплав'] =''
    df_termo['тип закаленности'] =''
    df_termo['Комбинация'] =''
    df_termo['Бренд краски снаружи'] =''
    df_termo['Код краски снаружи'] =''
    df_termo['Бренд краски внутри'] =''
    df_termo['Код краски внутри'] =''
    df_termo['Код декор пленки снаружи'] =''
    df_termo['Цвет декор пленки снаружи'] =''
    df_termo['Код декор пленки внутри'] =''
    df_termo['Цвет декор пленки внутри'] =''
    df_termo['Код лам пленки снаружи'] =''
    df_termo['Цвет лам пленки снаружи'] =''
    df_termo['Код лам пленки внутри'] =''
    df_termo['Цвет лам пленки внутри'] =''
    df_termo['Код цвета анодировки снаружи'] =''
    df_termo['Код цвета анодировки внутри'] =''
    df_termo['Контактность анодировки'] =''
    df_termo['Тип анодировки'] =''
    df_termo['Способ анодировки'] =''
    df_termo['Код наклейки'] =''
    df_termo['Надпись наклейки'] =''
    df_termo['База профилей'] =''
    df_termo['Группа материалов'] =''
    df_termo['Краткий текст товара'] =''
    df_termo['SAP Код вручную (вставится вручную)'] =''
    df_termo['Краткий текст товара (вставится вручную)'] =''
    df_termo['Место для комментариев'] =''
    df_termo['Длина при выходе из пресса'] =''

    

    df_simple  = pd.DataFrame()
    df_simple['counter'] =['' for x in range(0,len(datas))]
    df_simple['Название системы'] =''
    df_simple['Артикул'] =''
    df_simple['Длина (мм)'] =''
    df_simple['Тип покрытия'] =''
    df_simple['Сплав'] =''
    df_simple['тип закаленности'] =''
    df_simple['Комбинация'] =''
    df_simple['Бренд краски снаружи'] =''
    df_simple['Код краски снаружи'] =''
    df_simple['Бренд краски внутри'] =''
    df_simple['Код краски внутри'] =''
    df_simple['Код декор пленки снаружи'] =''
    df_simple['Цвет декор пленки снаружи'] =''
    df_simple['Код декор пленки внутри'] =''
    df_simple['Цвет декор пленки внутри'] =''
    df_simple['Код лам пленки снаружи'] =''
    df_simple['Цвет лам пленки снаружи'] =''
    df_simple['Код лам пленки внутри'] =''
    df_simple['Цвет лам пленки внутри'] =''
    df_simple['Код цвета анодировки снаружи'] =''
    df_simple['Код цвета анодировки внутри'] =''
    df_simple['Контактность анодировки'] =''
    df_simple['Тип анодировки'] =''
    df_simple['Способ анодировки'] =''
    df_simple['Код наклейки'] =''
    df_simple['Надпись наклейки'] =''
    df_simple['База профилей'] =''
    df_simple['Группа материалов'] =''
    df_simple['Краткий текст товара'] =''
    df_simple['SAP Код вручную (вставится вручную)'] =''
    df_simple['Краткий текст товара (вставится вручную)'] =''
    if name =='ALUMINIY EXPORT':
        df_simple['Длина при выходе из пресса'] =''
    df_simple['Код заказчика экспорт если експорт'] =''
    correct = True
    artikul_list = []
    for key1,data in datas.items():
        if data['is_termo']:
            lenth_of_component = ArtikulComponent.objects.filter(data__artikul =data['base_artikul']).count()
            if lenth_of_component <2:
                if data['base_artikul'] not in artikul_list :
                    artikul_list.append(data['base_artikul'])
                correct = False
    if not correct:
        return df_simple,df_termo,correct,artikul_list 
    

    k_termo = 0
    k_simple = 0
    for key1,data in datas.items():
            if data['is_termo']:
                df_termo['Название системы'][k_termo] = data['nazvaniye_system']
                df_termo['Артикул'][k_termo] = data['base_artikul']
                df_termo['Компонент'][k_termo] = ''
                df_termo['Длина (мм)'][k_termo] = data['dlina']
                df_termo['Тип покрытия'][k_termo] = data['tip_pokritiya']
                df_termo['Сплав'][k_termo] = data['splav']
                df_termo['тип закаленности'][k_termo] = data['tip_zak']
                df_termo['Комбинация'][k_termo] = data['combination']
                df_termo['Бренд краски снаружи'][k_termo] = data['brend_kraska_sn']
                df_termo['Код краски снаружи'][k_termo] = data['kod_kraska_sn']
                df_termo['Бренд краски внутри'][k_termo] = data['brend_kraska_vn']
                df_termo['Код краски внутри'][k_termo] = data['kod_kraska_vn']
                df_termo['Код декор пленки снаружи'][k_termo] = data['kod_dekor_sn']
                df_termo['Цвет декор пленки снаружи'][k_termo] = data['svet_dekplonka_snaruji']
                df_termo['Код декор пленки внутри'][k_termo] = data['kod_dekor_vn']
                df_termo['Цвет декор пленки внутри'][k_termo] = data['svet_dekplonka_vnutri']
                df_termo['Код лам пленки снаружи'][k_termo] = data['kod_lam_sn']
                df_termo['Цвет лам пленки снаружи'][k_termo] = data['svet_lamplonka_snaruji']
                df_termo['Код лам пленки внутри'][k_termo] = data['kod_lam_vn']
                df_termo['Цвет лам пленки внутри'][k_termo] = data['svet_lamplonka_vnutri']
                df_termo['Код цвета анодировки снаружи'][k_termo] = data['kod_anod_sn']
                df_termo['Код цвета анодировки внутри'][k_termo] = data['kod_anod_vn']
                df_termo['Контактность анодировки'][k_termo] = data['contactnost_anod']
                df_termo['Тип анодировки'][k_termo] = data['tip_anod']
                df_termo['Способ анодировки'][k_termo] = data['sposob_anod']
                df_termo['Код наклейки'][k_termo] = data['kod_nakleyki']
                df_termo['Надпись наклейки'][k_termo] = data['nadpis_nakleyki']
                df_termo['База профилей'][k_termo] = data['baza_profiley']
                df_termo['Группа материалов'][k_termo] = data['gruppa_materialov']
                df_termo['Краткий текст товара'][k_termo] = data['kratkiy_tekst']
                df_termo['SAP Код вручную (вставится вручную)'][k_termo] = ''
                df_termo['Краткий текст товара (вставится вручную)'][k_termo] = ''
                if name =='ALUMINIY EXPORT':
                    df_termo['Длина при выходе из пресса'][k_termo] = data['dilina_pressa']
                k_termo += 1
                lenth_of_component = ArtikulComponent.objects.filter(data__artikul =data['base_artikul']).count()

                
            
           
               
           
                 

                for i in range(1,lenth_of_component+1):
                    if i == 1:
                        if data['id'] ==1:
                            kratkiy_text_component = data['splav'] + data['tip_zak'] + ' L' + data['dlina'] + ' ' + data['kod_kraska_sn'] + ' ' + data['kod_nakleyki']
                                
                        elif data['id'] ==2:    
                            kratkiy_text_component = data['splav'] + data['tip_zak'] + ' L' + data['dlina'] + ' ' +data['brend_kraska_sn'] + data['kod_kraska_sn'] + ' ' + data['kod_nakleyki']
                        
                        elif data['id'] ==3:    
                            kratkiy_text_component = data['splav'] + data['tip_zak'] + ' L' + data['dlina'] + ' ' +data['brend_kraska_sn'] + data['kod_kraska_sn'] + ' ' + data['kod_nakleyki']
                    
                        elif data['id'] ==4:    
                            kratkiy_text_component = data['splav'] + data['tip_zak'] + ' L' + data['dlina'] + ' ' +data['brend_kraska_sn'] + data['kod_kraska_sn'] + '_' +data['kod_lam_sn']+ ' ' + data['kod_nakleyki']
                        
                        elif data['id'] ==5:    
                            kratkiy_text_component = data['splav'] + data['tip_zak'] + ' L' + data['dlina'] + ' ' +data['brend_kraska_sn'] + data['kod_kraska_sn'] + '_' +data['kod_dekor_sn']+ ' ' + data['kod_nakleyki']
                        
                        elif data['id'] ==6:    
                            kratkiy_text_component = data['splav'] + data['tip_zak'] + ' L' + data['dlina'] + ' ' +data['kod_anod_sn'] +' ' +data['contactnost_anod']+ ' ' + data['kod_nakleyki']
            
                        component = ArtikulComponent.objects.get(data__artikul =data['base_artikul'],data__counter = '1')
                        df_termo['Название системы'][k_termo] = data['nazvaniye_system']
                        df_termo['Артикул'][k_termo] = ''
                        df_termo['Компонент'][k_termo] =component.data['component']
                        df_termo['Длина (мм)'][k_termo] = data['dlina']
                        df_termo['Тип покрытия'][k_termo] = data['tip_pokritiya']
                        df_termo['Сплав'][k_termo] = data['splav']
                        df_termo['тип закаленности'][k_termo] = data['tip_zak']
                        df_termo['Комбинация'][k_termo] = 'Без термомоста'
                        df_termo['Бренд краски снаружи'][k_termo] = data['brend_kraska_sn']
                        df_termo['Код краски снаружи'][k_termo] = data['kod_kraska_sn']
                        df_termo['Бренд краски внутри'][k_termo] = ''
                        df_termo['Код краски внутри'][k_termo] = ''
                        df_termo['Код декор пленки снаружи'][k_termo] = data['kod_dekor_sn']
                        df_termo['Цвет декор пленки снаружи'][k_termo] = data['svet_dekplonka_snaruji']
                        df_termo['Код декор пленки внутри'][k_termo] = ''
                        df_termo['Цвет декор пленки внутри'][k_termo] = ''
                        df_termo['Код лам пленки снаружи'][k_termo] = data['kod_lam_sn']
                        df_termo['Цвет лам пленки снаружи'][k_termo] = data['svet_lamplonka_snaruji']
                        df_termo['Код лам пленки внутри'][k_termo] = ''
                        df_termo['Цвет лам пленки внутри'][k_termo] = ''
                        df_termo['Код цвета анодировки снаружи'][k_termo] = data['kod_anod_sn']
                        df_termo['Код цвета анодировки внутри'][k_termo] = ''
                        df_termo['Контактность анодировки'][k_termo] =''
                        df_termo['Тип анодировки'][k_termo] = ''
                        df_termo['Способ анодировки'][k_termo] = ''
                        df_termo['Код наклейки'][k_termo] = data['kod_nakleyki']
                        df_termo['Надпись наклейки'][k_termo] = data['nadpis_nakleyki']
                        df_termo['База профилей'][k_termo] = data['baza_profiley']
                        df_termo['Группа материалов'][k_termo] = data['gruppa_materialov']
                        df_termo['Краткий текст товара'][k_termo] = kratkiy_text_component
                        df_termo['SAP Код вручную (вставится вручную)'][k_termo] = ''
                        df_termo['Краткий текст товара (вставится вручную)'][k_termo] = ''
                        if name =='ALUMINIY EXPORT':
                            df_termo['Длина при выходе из пресса'][k_termo] = data['dilina_pressa']
                        k_termo += 1
                    if i == 2:
                        if data['id'] ==1:
                            kratkiy_text_component = data['splav'] + data['tip_zak'] + ' L' + data['dlina'] + ' ' + data['kod_kraska_vn'] + ' ' + data['kod_nakleyki']
                                
                        elif data['id'] ==2:    
                            kratkiy_text_component = data['splav'] + data['tip_zak'] + ' L' + data['dlina'] + ' ' +data['brend_kraska_vn']+ data['kod_kraska_vn'] + ' ' + data['kod_nakleyki']
                        
                        elif data['id'] ==3:    
                            kratkiy_text_component = data['splav'] + data['tip_zak'] + ' L' + data['dlina'] + ' ' + data['brend_kraska_vn']+ data['kod_kraska_vn'] + ' ' + data['kod_nakleyki']
                    
                        elif data['id'] ==4:    
                            kratkiy_text_component = data['splav'] + data['tip_zak'] + ' L' + data['dlina'] + ' ' +data['brend_kraska_vn']+ data['kod_kraska_vn'] +'_' +data['kod_lam_vn']+ ' ' + data['kod_nakleyki']
                        
                        elif data['id'] ==5:    
                            kratkiy_text_component = data['splav'] + data['tip_zak'] + ' L' + data['dlina'] + ' ' +data['brend_kraska_vn']+ data['kod_kraska_vn'] +'_' +data['kod_dekor_vn']+ ' ' + data['kod_nakleyki']
                        
                        elif data['id'] ==6:    
                            kratkiy_text_component = data['splav'] + data['tip_zak'] + ' L' + data['dlina'] + ' ' +data['kod_anod_vn'] + ' ' +data['contactnost_anod']+ ' ' + data['kod_nakleyki']
            
                        component = ArtikulComponent.objects.get(data__artikul =data['base_artikul'],data__counter = '2')
                        df_termo['Название системы'][k_termo] = data['nazvaniye_system']
                        df_termo['Артикул'][k_termo] = ''
                        df_termo['Компонент'][k_termo] =component.data['component']
                        df_termo['Длина (мм)'][k_termo] = data['dlina']
                        df_termo['Тип покрытия'][k_termo] = data['tip_pokritiya']
                        df_termo['Сплав'][k_termo] = data['splav']
                        df_termo['тип закаленности'][k_termo] = data['tip_zak']
                        df_termo['Комбинация'][k_termo] = 'Без термомоста'
                        df_termo['Бренд краски снаружи'][k_termo] = data['brend_kraska_vn']
                        df_termo['Код краски снаружи'][k_termo] = data['kod_kraska_vn']
                        df_termo['Бренд краски внутри'][k_termo] = ''
                        df_termo['Код краски внутри'][k_termo] = ''
                        df_termo['Код декор пленки снаружи'][k_termo] = data['kod_dekor_vn']
                        df_termo['Цвет декор пленки снаружи'][k_termo] = data['svet_dekplonka_vnutri']
                        df_termo['Код декор пленки внутри'][k_termo] = ''
                        df_termo['Цвет декор пленки внутри'][k_termo] = ''
                        df_termo['Код лам пленки снаружи'][k_termo] = data['kod_lam_vn']
                        df_termo['Цвет лам пленки снаружи'][k_termo] = data['svet_lamplonka_vnutri']
                        df_termo['Код лам пленки внутри'][k_termo] = ''
                        df_termo['Цвет лам пленки внутри'][k_termo] = ''
                        df_termo['Код цвета анодировки снаружи'][k_termo] = data['kod_anod_vn']
                        df_termo['Код цвета анодировки внутри'][k_termo] = ''
                        df_termo['Контактность анодировки'][k_termo] =''
                        df_termo['Тип анодировки'][k_termo] = ''
                        df_termo['Способ анодировки'][k_termo] = ''
                        df_termo['Код наклейки'][k_termo] = data['kod_nakleyki']
                        df_termo['Надпись наклейки'][k_termo] = data['nadpis_nakleyki']
                        df_termo['База профилей'][k_termo] = data['baza_profiley']
                        df_termo['Группа материалов'][k_termo] = data['gruppa_materialov']
                        df_termo['Краткий текст товара'][k_termo] = kratkiy_text_component
                        df_termo['SAP Код вручную (вставится вручную)'][k_termo] = ''
                        df_termo['Краткий текст товара (вставится вручную)'][k_termo] = ''
                        if name =='ALUMINIY EXPORT':
                            df_termo['Длина при выходе из пресса'][k_termo] = data['dilina_pressa']
                        k_termo += 1
            else:
                df_simple['Название системы'][k_simple] = data['nazvaniye_system']
                df_simple['Артикул'][k_simple] = data['base_artikul']
                df_simple['Длина (мм)'][k_simple] = data['dlina']
                df_simple['Тип покрытия'][k_simple] = data['tip_pokritiya']
                df_simple['Сплав'][k_simple] = data['splav']
                df_simple['тип закаленности'][k_simple] = data['tip_zak']
                df_simple['Комбинация'][k_simple] = data['combination']
                df_simple['Бренд краски снаружи'][k_simple] = data['brend_kraska_sn']
                df_simple['Код краски снаружи'][k_simple] = data['kod_kraska_sn']
                df_simple['Бренд краски внутри'][k_simple] = data['brend_kraska_vn']
                df_simple['Код краски внутри'][k_simple] = data['kod_kraska_vn']
                df_simple['Код декор пленки снаружи'][k_simple] = data['kod_dekor_sn']
                df_simple['Цвет декор пленки снаружи'][k_simple] = data['svet_dekplonka_snaruji']
                df_simple['Код декор пленки внутри'][k_simple] = data['kod_dekor_vn']
                df_simple['Цвет декор пленки внутри'][k_simple] = data['svet_dekplonka_vnutri']
                df_simple['Код лам пленки снаружи'][k_simple] = data['kod_lam_sn']
                df_simple['Цвет лам пленки снаружи'][k_simple] = data['svet_lamplonka_snaruji']
                df_simple['Код лам пленки внутри'][k_simple] = data['kod_lam_vn']
                df_simple['Цвет лам пленки внутри'][k_simple] = data['svet_lamplonka_vnutri']
                df_simple['Код цвета анодировки снаружи'][k_simple] = data['kod_anod_sn']
                df_simple['Код цвета анодировки внутри'][k_simple] = data['kod_anod_vn']
                df_simple['Контактность анодировки'][k_simple] = data['contactnost_anod']
                df_simple['Тип анодировки'][k_simple] = data['tip_anod']
                df_simple['Способ анодировки'][k_simple] = data['sposob_anod']
                df_simple['Код наклейки'][k_simple] = data['kod_nakleyki']
                df_simple['Надпись наклейки'][k_simple] = data['nadpis_nakleyki']
                df_simple['База профилей'][k_simple] = data['baza_profiley']
                df_simple['Группа материалов'][k_simple] = data['gruppa_materialov']
                df_simple['Краткий текст товара'][k_simple] = data['kratkiy_tekst']
                df_simple['SAP Код вручную (вставится вручную)'][k_simple] = ''
                df_simple['Краткий текст товара (вставится вручную)'][k_simple] =''
                if name =='ALUMINIY EXPORT':
                    df_simple['Длина при выходе из пресса'][k_simple] = data['dilina_pressa']
                k_simple+=1
    del df_simple['counter']
    del df_termo['counter']
    return df_simple,df_termo,correct,artikul_list






STATUSES =  {
    '1':'Открыто',
    '4':'Пере-открыто',
    '10023':'Выполнено',
    '10081':'На паузе',
    '10083':'Согласование',
    '10084':'Доработка заявителем',
    '10082':'Отменено',
    '10063':'Работа ведется',
    '10085':'Исправлено'

}
STATUS_JIRA ={
                    '1':{"id": "161",
                        "name": "Open"},
                
                    '10023':{"id": "61",
                            "name": "Отметить как выполненное"},
               
                    '10082':{"id": "171",
                            "name": "Отозвать заявку"},
               
                    '10083':{"id": "181",
                            "name": "Согласование",},
                
                    '10081':{"id": "41",
                        "name": "В ожидании",},
                
                    '10085':{"id": "151",
                        "name": "Доработан"},
                    
                    '10084':{"id": "121",
                        "name": "Отправить на доработку",},

                    '10063':{"id": "11",
                        "name": "Ход запуска",}

                }
                

              

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['moderator','user1'])
def moderator_check_zavod(request,id):
    users = User.objects.all()
    if request.method =='POST':
        data =request.POST.copy()
        order = Order.objects.get(id=id)
        order.status = data.get('status',1)
        order.save()

        # status_id_for_jira =STATUS_JIRA[order.status]['id']
        # jira_status_change(order.id_for_jira,status=status_id_for_jira)
        
        order_details = OrderDetail.objects.filter(order = order)
        send_event("test", "message", {
                                    "id":order.id,
                                    "order_name" : order.data['name'],
                                    "owner":str(order.owner),
                                    "checker":str(order.checker),
                                    "status":str(order.status),
                                    "created_at":order.created_at
                                    })
        return redirect('order_list_for_moderator')
        
    else:
        order = Order.objects.get(id = id)
        order_details = OrderDetail.objects.filter(order = order)
        context ={
            'status_name':STATUSES[str(order.status)],
            'status':str(order.status),
            'order_type':order.order_type,
            'data':json.dumps(order.data),
            'order_details':order_details,
            'users':users,
            'partner':order.partner
        }
        return render(request,'client/moderator/order_detail_zavod.html',context)
    
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['moderator','user1'])
def moderator_check(request,id):
    users = User.objects.all()
    if request.method =='POST':
        data =request.POST.copy()
        owner =request.user
        partner_id = data.get('user_id',None)
        order = Order.objects.get(id=id)
        if partner_id and partner_id !='':
            partner = User.objects.get(id = int(partner_id))
            order.partner =partner
        order_status = data.get('status',1)
        order.status = order_status

        status_id_for_jira =STATUS_JIRA[order.status]['id']
        # jira_status_change(order.id_for_jira,status=status_id_for_jira)
        # checker_send_to_jira(order.id_for_jira)


        order.checker = request.user
        order.save()
        data['owner'] = owner
        data['order'] = order
        form = OrderFileForm(data,request.FILES)
        if form.is_valid():
            form.save()
            order_details = OrderDetail.objects.filter(order = order)
            send_event("orders", "message_update", {
                                        "id":order.id,
                                        "owner":str(order.owner),
                                        "checker":order.checker.username +' ' +order.checker.last_name,
                                        "status":STATUSES[order_status],
                                        "is_alu":True if 'alu' in order.order_type else False,
                                        })
            return redirect('order_list_for_moderator')
        else:
            return JsonResponse({'form':form.errors})
    else:
        order = Order.objects.get(id = id)
        order_details = OrderDetail.objects.filter(order = order)
        context ={
            'status_name':STATUSES[str(order.status)],
            'status':str(order.status),
            'order_type':order.order_type,
            'data':json.dumps(order.data),
            'order_details':order_details,
            'users':users,
            'partner':order.partner
        }
        return render(request,'client/moderator/order_detail.html',context)
    
def checker_send_to_jira(id):
    
    payload_jira = json.dumps( 
        {
        "accountId": "712020:81c47857-d7c3-4478-86af-60456c2ed63f"
        })

    url_jira = f"https://akfa-group.atlassian.net/rest/api/3/issue/{id}/assignee"
    print(url_jira)
    response = rq.request(
        "PUT",
        url_jira,
        data=payload_jira,
        headers=headers_jira
    )
    print(response.text)
    return JsonResponse({'status':'changed'})


@login_required(login_url='/accounts/login/')
@customer_only
def order_update_all(request,id):
   
    if request.method =='POST':
        data =request.POST.copy()
        owner =request.user
        order = Order.objects.get(id=id)
        order.status = data.get('status',1)
        order.save()
        data['owner'] = owner
        data['order'] = order
        form = OrderFileForm(data,request.FILES)
        if form.is_valid():
            form.save()
            order_details = OrderDetail.objects.filter(order = order)
            send_event("test", "message", {
                                        "id":order.id,
                                        "order_name" : order.data['name'],
                                        "owner" : None,
                                        "checker":None,
                                        "status":str(order.status),
                                        "created_at":order.created_at
                                        })
            return redirect('client_order_list')
    else:
        nakleyka_list = NakleykaCode.objects.all()
        order = Order.objects.get(id = id)
        order_details = OrderDetail.objects.filter(order = order)
        context ={
            'status_name':STATUSES[str(order.status)],
            'status':str(order.status),
            'order_type':order.order_type,
            'data':json.dumps(order.data),
            'order_details':order_details,
            'id':order.id,
            'nakleyka_list': nakleyka_list    
        }
    return render(request,f'client/customer/update/{order.order_type}.html',context)

@login_required(login_url='/accounts/login/')
@customer_only
def order_update(request,id):
    
    if request.method =='POST':
        order = Order.objects.get(id=id)
        data = request.POST.get('data',None)
        name = request.POST.get('name',None)
        res = json.loads(data)
        
        try:
            # order.data = Order(data = {'name':name,'data':res})
            order.data ={'name':name,'data':res}
            order.save()
            return JsonResponse({'status':201})
        except:
            return JsonResponse({'status':405})
       
    else:
        nakleyka_list = NakleykaCode.objects.all()
        order = Order.objects.get(id = id)
        order_details = OrderDetail.objects.filter(order = order)
        context ={
            'status_name':STATUSES[str(order.status)],
            'status':str(order.status),
            'order_type':order.order_type,
            'data':json.dumps(order.data),
            'order_details':order_details,
            'id':order.id,
            'nakleyka_list': nakleyka_list   
        }
    return render(request,f'client/customer/update/{order.order_type}.html',context)

@login_required(login_url='/accounts/login/')
@customer_only
def detail_order_update(request,id):
    if request.method =='POST':
        data =request.POST.copy()
        owner =request.user
        order = Order.objects.get(id=id)
        order.status = data.get('status',1)
        # status_id_for_jira =STATUS_JIRA[order.status]['id']
        # jira_status_change(order.id_for_jira,status=status_id_for_jira)
        order.save()
        data['owner'] = owner
        data['order'] = order
        form = OrderFileForm(data,request.FILES)
        if form.is_valid():
            form.save()
            order_details = OrderDetail.objects.filter(order = order)
            context ={
                'status_name':STATUSES[str(order.status)],
                'status':str(order.status),
                'order_type':order.order_type,
                'data':json.dumps(order.data),
                'order_details':order_details,
                'id':order.id            
                }
            send_event("test", "message", {
                                        "id":order.id,
                                        "order_name" : order.data['name'],
                                        "owner" : None,
                                        "checker":None,
                                        "status":str(order.status),
                                        "created_at":order.created_at
                                        })
            return render(request,f'client/customer/update/{order.order_type}.html',context)
        else:
            return JsonResponse({'form':form.errors})
    else:
        order = Order.objects.get(id = id)
        order_details = OrderDetail.objects.filter(order = order)
        context ={
            'status_name':STATUSES[str(order.status)],
            'status':str(order.status),
            'order_type':order.order_type,
            'data':json.dumps(order.data),
            'order_details':order_details,
            'id':order.id   
        }
    return render(request,f'client/customer/update/{order.order_type}.html',context)



@login_required(login_url='/accounts/login/')
@customer_only
def order_detail(request,id):
    if request.method =='POST':
        data =request.POST.copy()
        owner =request.user
        order = Order.objects.get(id=id)
        order.status = data.get('status',1)
        # status_id_for_jira =STATUS_JIRA[order.status]['id']
        # jira_status_change(order.id_for_jira,status=status_id_for_jira)
        order.save()
        data['owner'] = owner
        data['order'] = order
        form = OrderFileForm(data,request.FILES)
        if form.is_valid():
            form.save()
            order_details = OrderDetail.objects.filter(order = order)
            context = {
                'status_name':STATUSES[str(order.status)],
                'status':str(order.status),
                'order_type':order.order_type,
                'data':json.dumps(order.data),
                'order_details':order_details
            }
            return render(request,'client/customer/order_detail.html',context)
        else:
            return JsonResponse({'form':form.errors})
    else:
        order = Order.objects.get(id = id)
        order_details = OrderDetail.objects.filter(order = order)
        
        if order.status == 10023 and order.order_type in ['pvc_export','pvc_savdo','pvc_imzo','alu_export','alu_savdo','alu_imzo']:
            datas = order.data['data']
            for key,val in datas.items():
                artikul = val['base_artikul']
                kratkiy = val['kratkiy_tekst']
                if not val['krat'] or not val['sap_code']:
                    if 'pvc' in order.order_type:
                        if PVCProduct.objects.filter(artikul=artikul,kratkiy_tekst_materiala=kratkiy,section='7').exists():
                            profil = PVCProduct.objects.filter(artikul=artikul,kratkiy_tekst_materiala=kratkiy,section='7')[:1].get()
                            datas[key]['sap_code'] =profil.material
                            datas[key]['krat'] =profil.kratkiy_tekst_materiala
                        
                    if 'alu' in order.order_type:
                        if val['is_termo']:
                            if AluminiyProductTermo.objects.filter(artikul=artikul,kratkiy_tekst_materiala=kratkiy,section='7').exists():
                                profil = AluminiyProductTermo.objects.filter(artikul=artikul,kratkiy_tekst_materiala=kratkiy,section='7')[:1].get()
                                datas[key]['sap_code'] =profil.material
                                datas[key]['krat'] =profil.kratkiy_tekst_materiala
                        else:
                            if AluminiyProduct.objects.filter(artikul=artikul,kratkiy_tekst_materiala=kratkiy,section='7').exists():
                                profil = AluminiyProduct.objects.filter(artikul=artikul,kratkiy_tekst_materiala=kratkiy,section='7')[:1].get()
                                datas[key]['sap_code'] =profil.material
                                datas[key]['krat'] =profil.kratkiy_tekst_materiala
            order.data['data'] = datas
            order.save()
                        
        context = {
            'status_name':STATUSES[str(order.status)],
            'status':str(order.status),
            'order_type':order.order_type,
            'data':json.dumps(order.data),
            'order_details':order_details
            }
        return render(request,'client/customer/order_detail.html',context)

   


@login_required(login_url='/accounts/login/')
@customer_only
def get_sapcodes(request):
    artikul = request.GET.get('artikul')
    kratkiy_tekst = request.GET.get('kratkiy_tekst')
    is_termo = request.GET.get('is_termo')
    if is_termo =='false':
        if AluminiyProduct.objects.filter(artikul=artikul,kratkiy_tekst_materiala=kratkiy_tekst).exists():
            sapcode = AluminiyProduct.objects.filter(artikul=artikul,kratkiy_tekst_materiala=kratkiy_tekst)[:1].get()
        else:
            return  JsonResponse({'status':400,'artikul':None,'kratkiy_tekst':None})
    else:
        if AluminiyProductTermo.objects.filter(artikul=artikul,kratkiy_tekst_materiala=kratkiy_tekst).exists():
            sapcode = AluminiyProductTermo.objects.filter(artikul=artikul,kratkiy_tekst_materiala=kratkiy_tekst)[:1].get()
        else:
            return  JsonResponse({'status':400,'artikul':None,'kratkiy_tekst':None})

    return JsonResponse({'status':201,'artikul':sapcode.material,'kratkiy_tekst':sapcode.kratkiy_tekst_materiala})

@login_required(login_url='/accounts/login/')
@customer_only
def get_sapcodes_pvc(request):
    artikul = request.GET.get('artikul')
    kratkiy_tekst = request.GET.get('kratkiy_tekst')
   
    
    if PVCProduct.objects.filter(artikul=artikul,kratkiy_tekst_materiala=kratkiy_tekst).exists():
        sapcode = PVCProduct.objects.filter(artikul=artikul,kratkiy_tekst_materiala=kratkiy_tekst)[:1].get()
    else:
        return  JsonResponse({'status':400,'artikul':None,'kratkiy_tekst':None})
   
    return JsonResponse({'status':201,'artikul':sapcode.material,'kratkiy_tekst':sapcode.kratkiy_tekst_materiala})



      
      




@login_required(login_url='/accounts/login/')
@customer_only
def order_list_test(request):
    search = request.GET.get('search',None)

    if search:
        orders = Order.objects.filter(Q(owner = request.user)&(Q(id_for_jira__icontains=search)|Q(theme__icontains=search)|Q(data__artikul__icontains=search))).order_by('-created_at')
    else:
        orders = Order.objects.filter(Q(owner = request.user)|(Q(partner = request.user)&Q(status=10083))).order_by('-created_at')

    paginator = Paginator(orders, 15)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)
    context ={
        'orders':page_obj
    }
    return render(request,'client/customer/test_list.html',context)



@login_required(login_url='/accounts/login/')
@customer_only
def order_list(request):
    search = request.GET.get('search',None)

    if search:
        orders = Order.objects.filter(Q(owner = request.user)&(Q(id_for_jira__icontains=search)|Q(theme__icontains=search)|Q(data__artikul__icontains=search))).order_by('-created_at')
    else:
        orders = Order.objects.filter(Q(owner = request.user)|(Q(partner = request.user)&Q(status=10083))).order_by('-created_at')

    paginator = Paginator(orders, 15)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)
    context ={
        'orders':page_obj
    }
    return render(request,'client/customer/order_list.html',context)





#################
@login_required(login_url='/accounts/login/')
@customer_only
def index(request):
    current_date = datetime.now()
    return render(request,'client/index.html',{'current_date': current_date})

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_imzo_detail(request):
    if request.method =='POST':
        
        return render(request,'client/created_link.html')
    else:
        nakleyka_list = NakleykaCode.objects.all()
        brend_kraska = BrendKraska.objects.all().values('brend','kraska')
        context ={
            'nakleyka_list': nakleyka_list,
            'brend_kaska':json.dumps(list(brend_kraska))
        }
        # return render(request,'client/shablonlar/example.html',context)
        return render(request,'client/shablonlar/aluminiy_imzo.html',context)

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_savdo_detail(request):
    nakleyka_list = NakleykaCode.objects.all()
    brend_kraska = BrendKraska.objects.all().values('brend','kraska')
    context ={
        'nakleyka_list': nakleyka_list,
        'brend_kaska':json.dumps(list(brend_kraska))
    }
    return render(request,'client/shablonlar/aluminiy_savdo.html',context)

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_export_detail(request):
    nakleyka_list = NakleykaCode.objects.all()
    brend_kraska = BrendKraska.objects.all().values('brend','kraska')
    context ={
        'nakleyka_list': nakleyka_list,
        'brend_kaska':json.dumps(list(brend_kraska))
    }
    return render(request,'client/shablonlar/aluminiy_export.html',context)


@login_required(login_url='/accounts/login/')
@customer_only
def shablon_acs_export_detail(request):
    return render(request,'client/shablonlar/accessuar_imzo.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_acs_savdo_detail(request):
    artikul_list = ArtikulAccessuar.objects.all().values_list('artikul')
    context ={
        'artikul_list':json.dumps(list(artikul_list))
    }
    return render(request,'client/shablonlar/accessuar_savdo.html',context)

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_acs_export_savdo_detail(request):
    return render(request,'client/shablonlar/accessuar_export.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_acs_zavod_savdo_detail(request):
    artikul_list = ArtikulAccessuar.objects.all().values_list('artikul')
    context ={
        'artikul_list':json.dumps(list(artikul_list))
    }
    return render(request,'client/shablonlar/accessuar_zavod.html',context)

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_pvc_export_detail(request):
    nakleyka_list = NakleykaPvc.objects.all().values_list('name','nadpis')
    context ={
        'nakleyka_list':json.dumps(list(nakleyka_list))
    }
    return render(request,'client/shablonlar/pvc_imzo.html',context)

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_akp_savdo_detail(request):
    return render(request,'client/shablonlar/akp_savdo.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_pvc_savdo_detail(request):
    nakleyka_list = NakleykaPvc.objects.all().values_list('name','nadpis')
    context ={
        'nakleyka_list':json.dumps(list(nakleyka_list))
    }
    return render(request,'client/shablonlar/pvc_savdo.html',context)

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_radiator_detail(request):
    return render(request,'client/shablonlar/radiator.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_radiator_export_detail(request):
    return render(request,'client/shablonlar/radiator_export.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_prochiye_detail(request):
    return render(request,'client/shablonlar/prochiye.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_accessuar_import_detail(request):
    category = Category.objects.all().values_list('name','code')
    group_product = GroupProduct.objects.all().values_list('name','code')

    context ={
        'category':json.dumps(list(category)),
        'group_product':json.dumps(list(group_product))
    }
    return render(request,'client/shablonlar/accessuar_import.html',context)

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_pvc_export_savdo_detail(request):
    nakleyka_list = NakleykaCode.objects.all().values_list('name','nadpis')
    context ={
        'nakleyka_list':json.dumps(list(nakleyka_list))
    }
    return render(request,'client/shablonlar/pvc_export.html',context)

@login_required(login_url='/accounts/login/')
@customer_only
def imzo_artikul_list(request):
    
    term = request.GET.get('term',None)
    if term:
        artikules = AluProfilesData.objects.filter(Q(data__Артикул__icontains = term)|Q(data__Компонент__icontains=term)).values('id','data')
    else:
        artikules = AluProfilesData.objects.all()[:50].values('id','data')
    return JsonResponse(list(artikules),safe=False)


@login_required(login_url='/accounts/login/')
@customer_only
def pvc_artikul_list(request):
    
    term = request.GET.get('term',None)
    if term:
        artikules = ArtikulKomponentPVC.objects.filter(artikul__icontains = term).values('id','artikul','component','component2','category','nazvaniye_sistem','camera','kod_k_component','iskyucheniye','is_special','nakleyka_nt1')
    else:
        artikules = ArtikulKomponentPVC.objects.all()[:50].values('id','artikul','component','component2','category','nazvaniye_sistem','camera','kod_k_component','iskyucheniye','is_special','nakleyka_nt1')
    return JsonResponse(list(artikules),safe=False)


@login_required(login_url='/accounts/login/')
@customer_only
def radiator_artikul_list(request):
    term = request.GET.get('term',None)
    if term:
        artikules = ArtikulRadiator.objects.filter(model_radiator__icontains = term).values('id','model_radiator','artikul')
    else:
        artikules = ArtikulRadiator.objects.all()[:50].values('id','model_radiator','artikul')
    return JsonResponse(list(artikules),safe=False)

# @login_required(login_url='/accounts/login/')
# @customer_only
# def accessuar_uz_artikul_list(request):
#     term = request.GET.get('term',None)
#     if term:
#         artikules = ArtikulAccessuar.objects.filter(model_radiator__icontains = term).values('id','model_radiator','artikul')
#     else:
#         artikules = ArtikulAccessuar.objects.all()[:50].values('id','model_radiator','artikul')
#     return JsonResponse(list(artikules),safe=False)


    
    
    
@login_required(login_url='/accounts/login/')
@customer_only
def nakleyka_list(request):
    
    term = request.GET.get('term',None)
    if term:
        nakleyka_l = NakleykaCode.objects.filter(name__icontains = term).distinct("name").values('id','name','nadpis')
    else:
        nakleyka_l = NakleykaCode.objects.all().distinct("name").values('id','name','nadpis')
        
    return JsonResponse(list(nakleyka_l),safe=False)





@login_required(login_url='/accounts/login/')
@customer_only
def nakleyka_list_pvc(request):
    
    term = request.GET.get('term',None)
    if term:
        nakleyka_l = NakleykaPvc.objects.filter(name__icontains = term).distinct("name").values('id','name','nadpis')
    else:
        nakleyka_l = NakleykaPvc.objects.all().distinct("name").values('id','name','nadpis')
        
    return JsonResponse(list(nakleyka_l),safe=False)

@login_required(login_url='/accounts/login/')
@customer_only
def anod_list(request):
    term = request.GET.get('term',None)
    if term:
        anod_l = Anod.objects.filter(code_sveta__icontains = term).distinct("code_sveta").values('id','code_sveta','tip_anod','sposob_anod')
    else:
        anod_l = Anod.objects.all().distinct("code_sveta").values('id','code_sveta','tip_anod','sposob_anod')
        
    return JsonResponse(list(anod_l),safe=False)
