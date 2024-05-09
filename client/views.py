from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from aluminiy.models import AluProfilesData
from pvc.models import ArtikulKomponentPVC ,NakleykaPvc
from norma.models import Nakleyka
from .models import Anod,Order,OrderDetail
from django.contrib.auth.decorators import login_required
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from accounts.decorators import customer_only,moderator_only,allowed_users
from django.core.paginator import Paginator
import json
from .forms import OrderFileForm
from django.db.models import Q
from accounts.models import User
from django.views.decorators.csrf import csrf_exempt
import websocket
from django_eventstream import send_event



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
        order_type = request.data.get('order_type',None)
        res = json.loads(data)
        try:
            order = Order(data = {'name':name,'data':res},owner=request.user,order_type = order_type)
            order.save()
            order_detail = OrderDetail(order=order,owner=request.user)
            order_detail.save()
            send_event("test", "message", {
                                        "id":order.id,
                                        "order_name" : name,
                                        "owner" : str(request.user),
                                        "checker":None,
                                        "status":"1",
                                        "created_at":order.created_at
                                        })
            return Response({'msg':'Ordered successfully!','status':201,'order_id':order.id})    
        except:
            return Response({'msg':'Something went wrong.','status':300,'order_id':None})    


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

@moderator_only
def order_list_for_moderator(request):
    orders = Order.objects.all().order_by('-created_at')

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
@moderator_only
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
        order.status = data.get('status',1)
        order.checker = request.user
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
                                        "owner" : str(owner),
                                        "checker":None,
                                        "status":str(order.status),
                                        "created_at":order.created_at
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
STATUSES =  {
    '1':'Открыто',
    '4':'Пере-открыто',
    '10023':'Выполнено',
    '10063':'Работа ведется',
    '10081':'На паузе',
    '10083':'Согласование',
    '10084':'Доработка',
    '10082':'Отменено',
    '10063':'Работа ведется',
    '10085':'Исправлено'

}

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
def detail_order_update(request,id):
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
                'order_details':order_details
            }
            return render(request,'client/customer/order_detail.html',context)
        else:
            return JsonResponse({'form':form.errors})
    else:
        order = Order.objects.get(id = id)
        order_details = OrderDetail.objects.filter(order = order)
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
def order_list(request):
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
    return render(request,'client/index.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_imzo_detail(request):
    if request.method =='POST':
        context ={
            'link':'https://mdm.akfagroup.com/'
        }
        return render(request,'client/created_link.html',context)
    else:
        return render(request,'client/shablonlar/aluminiy_imzo.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_savdo_detail(request):
    return render(request,'client/shablonlar/aluminiy_savdo.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_export_detail(request):
    return render(request,'client/shablonlar/aluminiy_export.html')


@login_required(login_url='/accounts/login/')
@customer_only
def shablon_acs_export_detail(request):
    return render(request,'client/shablonlar/accessuar_imzo.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_acs_savdo_detail(request):
    return render(request,'client/shablonlar/accessuar_savdo.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_acs_export_savdo_detail(request):
    return render(request,'client/shablonlar/accessuar_export.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_pvc_export_detail(request):
    return render(request,'client/shablonlar/pvc_imzo.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_akp_savdo_detail(request):
    return render(request,'client/shablonlar/akp_savdo.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_pvc_savdo_detail(request):
    return render(request,'client/shablonlar/pvc_savdo.html')

@login_required(login_url='/accounts/login/')
@customer_only
def shablon_pvc_export_savdo_detail(request):
    return render(request,'client/shablonlar/pvc_export.html')

@login_required(login_url='/accounts/login/')
@customer_only
def imzo_artikul_list(request):
    
    term = request.GET.get('term',None)
    if term:
        artikules = AluProfilesData.objects.filter(artikul__icontains = term).values('id','data')
    else:
        artikules = AluProfilesData.objects.all()[:50].values('id','data')
    return JsonResponse(list(artikules),safe=False)


@login_required(login_url='/accounts/login/')
@customer_only
def pvc_artikul_list(request):
    
    term = request.GET.get('term',None)
    if term:
        artikules = ArtikulKomponentPVC.objects.filter(artikul__icontains = term).values('id','artikul','component','component2','category','nazvaniye_sistem','camera','kod_k_component','iskyucheniye')
    else:
        artikules = ArtikulKomponentPVC.objects.all()[:50].values('id','artikul','component','component2','category','nazvaniye_sistem','camera','kod_k_component','iskyucheniye')
    return JsonResponse(list(artikules),safe=False)


    
    
    
@login_required(login_url='/accounts/login/')
@customer_only
def nakleyka_list(request):
    
    term = request.GET.get('term',None)
    if term:
        nakleyka_l = Nakleyka.objects.filter(код_наклейки__icontains = term).distinct("код_наклейки").values('id','код_наклейки')
    else:
        nakleyka_l = Nakleyka.objects.all().distinct("код_наклейки").values('id','код_наклейки')
        
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
