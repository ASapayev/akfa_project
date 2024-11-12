from django.shortcuts import render,redirect
from django.http import JsonResponse
import pandas as pd
from config.settings import MEDIA_ROOT
from aluminiy.models import LengthOfProfile,ExchangeValues
from functools import partial
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import FileForm,FileForm2
from accounts.models import User
from .models import OnlineSavdoOrder,OnlineSavdoFile
import os
from .utils import create_folder,zip,format_to_online,get_id,create_session,upload_file_online,sozdaniye_sena_sap,sozdaniye_sap_format_sena_create,check_sena
from accounts.decorators import allowed_users
from order.models import Order
from django.db.models import Q
import requests as rq

base_url = 'http://test.app.akfa.onlinesavdo.com'




class File:
    def __init__(self,id,file,filetype,created_at):
        self.id =id
        self.file =file
        self.filetype =filetype
        self.created_at = created_at

class FileG:
    def __init__(self,file,filetype):
        self.file =file
        self.filetype =filetype

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def online_savdo_list(request):
    orders = OnlineSavdoOrder.objects.all().order_by('-created_at')
    context ={
        'orders':orders
    }
    
    return render(request,'online_savdo/file_list.html',context)







@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def upload_product_org(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
                new_order = form.save()
                order = OnlineSavdoOrder()
                order.paths['first_file_id'] =new_order.id
                order.paths['first_file_path'] =str(new_order.file)
                order.paths['created_at'] =order.created_at
                order.save()
                order.paths['link'] ='generate-online-file/'+str(order.id)
                order.save()
                return redirect('online_savdo_zayavki')
                # context ={
                #     'first_file_id':new_order.id,
                #     'first_file_path':new_order.file,
                #     'created_at':order.created_at,
                #     'link':'generate-online-file/'+str(order.id),
                #     'status':'1'
                # }
                # return render(request,'online_savdo/order_detail.html',context)
    else:
        form =FileForm()
        context ={
        'form':form,
        'section':'Формирование сапкода обычный'
        }
    return render(request,'online_savdo/main.html',context)






@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def merging_files(request,id):
    file = OnlineSavdoFile.objects.get(id=id).file
    df = pd.read_excel(f'{MEDIA_ROOT}/{file}')
   
    df =df.astype(str)
    df = df.replace('nan','')
    df['SAP CODE']= ''
    df['KRATKIY TEXT']= ''

    for key,row in df.iterrows():
        if key ==1:
            df.at[0,'SAP CODE'] ='12345566'
            df.at[0,'KRATKIY TEXT'] ='MAXIMUM-GOODS'
        
        if (row[df.columns[0]]=='Id'):
            df.at[key,'SAP CODE'] = 'SAP CODE'
            df.at[key,'KRATKIY TEXT'] = 'KRATKIY TEXT'

        if (row[df.columns[0]]!='Id') and (row[df.columns[0]]!=''):
            df.at[key,'SAP CODE'] = key
            df.at[key,'KRATKIY TEXT'] = key
           
    zagolovok = list(df.columns)
    desired_order = zagolovok[:2] + zagolovok[-2:] +zagolovok[2:-2]
    
    df = df[desired_order]

    for i, col in enumerate(df.columns):
        if 'Unnamed: ' in col or 'SAP CODE' in col or 'KRATKIY TEXT' in col:
            df = df.rename(columns={col: ''})
    
   
    now =datetime.now()
    minut =now.strftime('%M-%S')
    pathtext1=f'{MEDIA_ROOT}/uploads/online_savdo/downloads/savdo_{minut}.xlsx'
    df.to_excel(pathtext1,index=False,engine='openpyxl')
    files = [FileG(file=pathtext1,filetype='obichniy')]
    context = {
        'files':files
    }
    return render(request,'universal/generated_files.html',context)



@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def upload_file_for_preparing(request):
    if request.method == 'POST':
        form1 = FileForm(request.POST, request.FILES)
        if form1.is_valid():
            new_order1 = form1.save()
            online_savdo_order = OnlineSavdoOrder()
            online_savdo_order.paths = { 
                        'path_1' : str(new_order1.file)
                    }
            online_savdo_order.save()

            files = [File(id=new_order1.id,file = 'EXCELL FILES',filetype = 'savdo',created_at=datetime.now())]
            context ={
                'files':files,
                'link':'generate-merging-files/'
            }
            return render(request,'online_savdo/file_list.html',context)
    else:
        form1 = FileForm()
        context ={
            'form1':form1,
            'section':'Формирование'
        }
    return render(request,'online_savdo/sena_format.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def upload_for_proverka(request):
    if request.method == 'POST':
        form1 = FileForm(request.POST, request.FILES)
        if form1.is_valid():
                paths = {}
                for f in request.FILES.getlist('file'):
                    file_instance = OnlineSavdoFile(file=f)
                    file_instance.save()
                    file_name = str(file_instance.file)
                    if ('VK' in file_name and 'ZORN' in file_name):
                        paths['1'] = file_name
                    elif ('CHECK' in file_name and 'ZORN' in file_name):
                        paths['2'] = file_name

                    

                    elif ('VK' in file_name and 'ZUU' in file_name):
                        paths['5'] = file_name
                    elif ('CHECK' in file_name and 'ZUU' in file_name):
                        paths['6'] = file_name

                    

                    elif ('VK' in file_name and 'ZREN' in file_name):
                        paths['11'] = file_name
                    elif ('CHECK' in file_name and 'ZREN' in file_name):
                        paths['12'] = file_name
                

                online_savdo_order = OnlineSavdoOrder()
                online_savdo_order.paths = { 
                    'path_1' : str(paths['1']),
                    'path_2' : str(paths['2']),
                    'path_3' : '',
                    'path_4' : '',
                    'path_5' : str(paths['5']),
                    'path_6' : str(paths['6']),
                    'path_7' : '',
                    'path_8' : '',
                    'path_9' : '',
                    'path_10' : '',
                    'path_11' : str(paths['11']),
                    'path_12' : str(paths['12'])
                      }
                online_savdo_order.save()

                files = [File(id=online_savdo_order.id,file = 'EXCELL FILES',filetype = 'savdo',created_at=datetime.now())]
                context ={
                    'files':files,
                    'link':'generate-proverka-files/'
                }
                return render(request,'online_savdo/file_list.html',context)
    else:
        form1 = FileForm2()
        context ={
        'form1':form1,
        'section':'Формирование'
        }
    return render(request,'online_savdo/proverka.html',context)



def round50(n):
    return round(n/0.01)*0.01

def round502(n):
    if str(n)=='':
        return ''
    return round(float(str(n).replace(',','.')), -2)

def round503(n):
    return round(n * 2, -2) // 2




@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def create_online(request,id):
    order = OnlineSavdoOrder.objects.get(id = id)
    paths = order.paths
    cliked_btn = request.GET.get('cliked_btn',None)

    if str(order.status) == '1':
        first_file_path = paths['first_file_path']
        
        session,status_code =create_session(f'{base_url}/auth/login')

        url ='http://test.app.akfa.onlinesavdo.com/ajax-goods-datagrid'
        
        path,condition = format_to_online(url,session,first_file_path)
       
        if condition =='success':
            order.paths['file_formated'] = path
            order.status ='2'
        else:
            order.paths['error_file'] = path        
        order.save()
       

        
       
    elif str(order.status) == '2' and cliked_btn and cliked_btn =='2':
        file_formated = paths['file_formated']
        session,status_code =create_session(f'{base_url}/auth/login')
        url ='http://test.app.akfa.onlinesavdo.com/ajax-goods-excelUpload'
        status = upload_file_online(file_formated,session,status_code,url,'Goods')

        # print(status,'stats'*52)
        if status == 200:
            first_file_path = paths['first_file_path']
            # path = OnlineSavdoFile.objects.get(id=int(first_file_id)).file
            status_code2,path_id = get_id(first_file_path,status_code)

            if status_code2 == 200:
                order.status ='4'
                order.paths['created_sena_file'] = path_id
            else:
                order.status ='3'
                order.paths['created_id_error_file'] = path_id
            order.save()
        else:
            return JsonResponse({'Something went wrong in savdo request!'})
        
    elif str(order.status) == '3' and cliked_btn and cliked_btn =='3':
        # session,status_code =create_session(f'{base_url}/auth/login')
        first_file_path = paths['first_file_path']
        # path = OnlineSavdoFile.objects.get(id=int(first_file_id)).file
        status_code2,path_id = get_id(first_file_path)
        if status_code2 == 200:
            order.status ='4'
            order.paths['created_sena_file'] = path_id
        else:
            order.status ='3'
            order.paths['created_id_error_file'] = path_id
        order.save()
    elif str(order.status) == '4' and cliked_btn and cliked_btn =='4':
        created_sena_file = paths['created_sena_file']
        session,status_code =create_session(f'{base_url}/auth/login')
        url ='http://test.app.akfa.onlinesavdo.com/ajax-goods-rate-excelUpload'
        status = upload_file_online(created_sena_file,session,status_code,url,'SENA')

        if status ==200:
            order.status =5
            order.save()
        else:
            return JsonResponse({'msg':'Something went wrong in sena request!'})
        
    ############# done done done #######
    elif str(order.status) == '5' and cliked_btn and cliked_btn =='5':
        created_sena_file = paths['created_sena_file']
        session,status_code =create_session(f'{base_url}/auth/login')
        if status_code ==200:
            path_sena_file = check_sena(created_sena_file)
            # order.paths['path_sena_file'] = path_sena_file
            order.paths['path_sena_file_checker'] = path_sena_file
            order.status = 6
            order.save()
        else:
            return JsonResponse({'msg':'Something went wrong!'})
        
    elif str(order.status) == '6' and cliked_btn and cliked_btn =='6':
        first_file_path = paths['first_file_path']
        session,status_code =create_session(f'{base_url}/auth/login')
        if status_code ==200:
            path_sena_file =sozdaniye_sena_sap(first_file_path,session)
            order.paths['path_sena_file'] = path_sena_file
            order.status = 7
            order.save()
        else:
            return JsonResponse({'msg':'Something went wrong!'})
        
    elif str(order.status) == '7' and cliked_btn and cliked_btn =='7':
        path_sena_file = paths['path_sena_file']
        session,status_code =create_session(f'{base_url}/auth/login')
        if status_code ==200:
            zip_file_for_sap =sozdaniye_sap_format_sena_create(path_sena_file)
            order.paths['zip_file_for_sap'] = zip_file_for_sap
            order.status = 8
            order.save()
        else:
            return JsonResponse({'msg':'Something went wrong!'})





    
    context ={'status':str(order.status)}
    for key,val in paths.items():
        context[key]=val

    return render(request,'online_savdo/order_detail.html',context)


   
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def proverka(request,id):
    order = OnlineSavdoOrder.objects.get(id = id)
    path1 = order.paths['path_1']
    path2 = order.paths['path_2']
    path3 = order.paths['path_3']
    path4 = order.paths['path_4']
    path5 = order.paths['path_5']
    path6 = order.paths['path_6']
    path7 = order.paths['path_7']
    path8 = order.paths['path_8']
    path9 = order.paths['path_9']
    path10 = order.paths['path_10']
    path11 = order.paths['path_11']
    path12 = order.paths['path_12']

    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M%S%S")

    parent_dir =f'{MEDIA_ROOT}\\uploads\\online_savdo\\'
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads\\','online_savdo')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\',hour)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\','ONLINE')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\',minut)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}','PROVERKA')

    pathtext1 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\ZORN ERROR.xlsx'
    pathtext2 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\БЕЗНАЛ ERROR.xlsx'
    pathtext3 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\ZUU ERROR.xlsx'
    pathtext4 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\ZFKN ERROR.xlsx'
    pathtext5 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\ZFDN ERROR.xlsx'
    pathtext6 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\ZREN ERROR.xlsx'
    pathzip =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA'

    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)

    to_datetime_fmt = partial(pd.to_datetime, format='%d.%m.%Y')

    df1['DATAB'] = df1['DATAB'].apply(to_datetime_fmt)

    df1 = df1.astype(str)
    df1['joined_data']= df1['VKORG'] + df1['KONDA'] + df1['MATNR'] +df1['DATAB']

    # print(df1['joined_data'])

    df2 = pd.read_excel(f'{MEDIA_ROOT}/{path2}',sheet_name='Sheet1',header=0)

    df2 = df2.astype(str)
    df2['joined_data']= df2['Сбытовая организация'] + df2['Группа цен клиента'] + df2['Материал'] +df2['Действ. с']

    # print(df2['joined_data'])
    nesovpaden_datas =[[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[],[],[],[]]

    for key1,row1 in df1.iterrows():
        result = df2[df2['joined_data'] == row1['joined_data'] ]
        result['Сумма']=result['Сумма'].astype(float)
        row1['KBETR']= float(row1['KBETR'])
        
        result2 =result[result['Сумма'] == row1['KBETR']]
        if result2.empty:
            nesovpaden_datas[0].append(row1['KSCHL'])
            nesovpaden_datas[1].append(row1['VKORG'])
            nesovpaden_datas[2].append(row1['WERKS'])
            nesovpaden_datas[3].append(row1['VTWEG'])
            nesovpaden_datas[4].append(row1['KONDA'])
            nesovpaden_datas[5].append(row1['MATNR'])
            nesovpaden_datas[6].append(row1['KBETR'])
            nesovpaden_datas[7].append(row1['KONWA'])
            nesovpaden_datas[8].append(row1['KPEIN'])
            nesovpaden_datas[9].append(row1['KMEIN'])
            nesovpaden_datas[10].append(row1['DATAB'])
            nesovpaden_datas[11].append(row1['DATBI'])
            nesovpaden_datas[12].append(row1['KUNNR'])
            nesovpaden_datas[13].append(row1['FKART'])
            nesovpaden_datas[14].append(row1['AUART'])
            nesovpaden_datas[15].append(row1['AUGRU'])
            # nesovpaden_datas[16].append(result.iloc[0]['Сумма'])
        else:
            pass

    df_nesovpa =pd.DataFrame({
    'KSCHL':nesovpaden_datas[0],
    'VKORG':nesovpaden_datas[1],
    'WERKS':nesovpaden_datas[2],
    'VTWEG':nesovpaden_datas[3],
    'KONDA':nesovpaden_datas[4],
    'MATNR':nesovpaden_datas[5],
    'KBETR':nesovpaden_datas[6],
    'KONWA':nesovpaden_datas[7],
    'KPEIN':nesovpaden_datas[8],
    'KMEIN':nesovpaden_datas[9],
    'DATAB':nesovpaden_datas[10],
    'DATBI':nesovpaden_datas[11],
    'KUNNR':nesovpaden_datas[12],
    'FKART':nesovpaden_datas[13],
    'AUART':nesovpaden_datas[14],
    'AUGRU':nesovpaden_datas[15],
    # 'ERROR':nesovpaden_datas[16]

    })
    df_nesovpa =df_nesovpa.replace('nan','')

    if not df_nesovpa.empty:
        df_nesovpa.to_excel(pathtext1)
    try:
        df1 = pd.read_excel(f'{MEDIA_ROOT}/{path3}',sheet_name='Sheet1',header=0)

        to_datetime_fmt = partial(pd.to_datetime, format='%d.%m.%Y')

        df1['DATAB'] = df1['DATAB'].apply(to_datetime_fmt)
        df1 = df1.astype(str)
        df1['joined_data']= df1['VKORG'] + df1['KONDA'] + df1['MATNR'] +df1['DATAB']

        # print(df1['joined_data'])

        df2 = pd.read_excel(f'{MEDIA_ROOT}/{path4}',sheet_name='Sheet1',header=0)

        df2 = df2.astype(str)
        df2['joined_data']= df2['Сбытовая организация'] + df2['Группа цен клиента'] + df2['Материал'] +df2['Действ. с']

        # print(df2['joined_data'])
        nesovpaden_datas =[[],[],[],[],
                        [],[],[],[],[],[],[],[],[],[],[],[],[]]

        for key1,row1 in df1.iterrows():
            result = df2[df2['joined_data'] == row1['joined_data'] ]
            result['Сумма'] = result['Сумма'].astype(float)
            row1['KBETR'] = float(row1['KBETR'])
            
            result2 =result[result['Сумма'] == row1['KBETR']]
            if result2.empty:
                nesovpaden_datas[0].append(row1['KSCHL'])
                nesovpaden_datas[1].append(row1['VKORG'])
                nesovpaden_datas[2].append(row1['WERKS'])
                nesovpaden_datas[3].append(row1['VTWEG'])
                nesovpaden_datas[4].append(row1['KONDA'])
                nesovpaden_datas[5].append(row1['MATNR'])
                nesovpaden_datas[6].append(row1['KBETR'])
                nesovpaden_datas[7].append(row1['KONWA'])
                nesovpaden_datas[8].append(row1['KPEIN'])
                nesovpaden_datas[9].append(row1['KMEIN'])
                nesovpaden_datas[10].append(row1['DATAB'])
                nesovpaden_datas[11].append(row1['DATBI'])
                nesovpaden_datas[12].append(row1['KUNNR'])
                nesovpaden_datas[13].append(row1['FKART'])
                nesovpaden_datas[14].append(row1['AUART'])
                nesovpaden_datas[15].append(row1['AUGRU'])
                nesovpaden_datas[16].append(result.iloc[0]['Сумма'])
                # print(result,'nesovpaden')
            else:
                pass
                # print(result2,'sovpaden')

        df_nesovpa =pd.DataFrame({
        'KSCHL':nesovpaden_datas[0],
        'VKORG':nesovpaden_datas[1],
        'WERKS':nesovpaden_datas[2],
        'VTWEG':nesovpaden_datas[3],
        'KONDA':nesovpaden_datas[4],
        'MATNR':nesovpaden_datas[5],
        'KBETR':nesovpaden_datas[6],
        'KONWA':nesovpaden_datas[7],
        'KPEIN':nesovpaden_datas[8],
        'KMEIN':nesovpaden_datas[9],
        'DATAB':nesovpaden_datas[10],
        'DATBI':nesovpaden_datas[11],
        'KUNNR':nesovpaden_datas[12],
        'FKART':nesovpaden_datas[13],
        'AUART':nesovpaden_datas[14],
        'AUGRU':nesovpaden_datas[15],
        'ERROR':nesovpaden_datas[16]

        })
        df_nesovpa =df_nesovpa.replace('nan','')
        
        if not df_nesovpa.empty:
            df_nesovpa.to_excel(pathtext2)
    except:
        pass

    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path5}',sheet_name='Sheet1',header=0)

    # to_datetime_fmt = partial(pd.to_datetime, format='%d.%m.%Y')

    # df1['DATAB'] = df1['DATAB'].apply(to_datetime_fmt)
    df1 = df1.astype(str)
    df1['joined_data']= df1['VKORG'] + df1['KONDA'] + df1['MATNR'] +df1['DATAB']

    # print(df1['joined_data'])

    df2 = pd.read_excel(f'{MEDIA_ROOT}/{path6}',sheet_name='Sheet1',header=0)

    df2 = df2.astype(str)
    df2['joined_data']= df2['Сбытовая организация'] + df2['Группа цен клиента'] + df2['Материал'] +df2['Действ. с']

    # print(df2['joined_data'])
    nesovpaden_datas =[[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[],[],[],[]]
    
    # print(df1['joined_data'],'df1')
    # print(df2['joined_data'],'df2')

    for key1,row1 in df1.iterrows():
        result = df2[df2['joined_data'] == row1['joined_data'] ]
        # print(result,'result')
        result['Сумма']=result['Сумма'].astype(float)
        row1['KBETR']= float(row1['KBETR'])
        
        result2 =result[result['Сумма'] == row1['KBETR']]
        if result2.empty:
            nesovpaden_datas[0].append(row1['KSCHL'])
            nesovpaden_datas[1].append(row1['VKORG'])
            nesovpaden_datas[2].append(row1['WERKS'])
            nesovpaden_datas[3].append(row1['VTWEG'])
            nesovpaden_datas[4].append(row1['KONDA'])
            nesovpaden_datas[5].append(row1['MATNR'])
            nesovpaden_datas[6].append(row1['KBETR'])
            nesovpaden_datas[7].append(row1['KONWA'])
            nesovpaden_datas[8].append(row1['KPEIN'])
            nesovpaden_datas[9].append(row1['KMEIN'])
            nesovpaden_datas[10].append(row1['DATAB'])
            nesovpaden_datas[11].append(row1['DATBI'])
            nesovpaden_datas[12].append(row1['KUNNR'])
            nesovpaden_datas[13].append(row1['FKART'])
            nesovpaden_datas[14].append(row1['AUART'])
            nesovpaden_datas[15].append(row1['AUGRU'])
            nesovpaden_datas[16].append(result.iloc[0]['Сумма'])
            # print(result,'nesovpaden')
        else:
            pass
            # print(result2,'sovpaden')

    df_nesovpa =pd.DataFrame({
    'KSCHL':nesovpaden_datas[0],
    'VKORG':nesovpaden_datas[1],
    'WERKS':nesovpaden_datas[2],
    'VTWEG':nesovpaden_datas[3],
    'KONDA':nesovpaden_datas[4],
    'MATNR':nesovpaden_datas[5],
    'KBETR':nesovpaden_datas[6],
    'KONWA':nesovpaden_datas[7],
    'KPEIN':nesovpaden_datas[8],
    'KMEIN':nesovpaden_datas[9],
    'DATAB':nesovpaden_datas[10],
    'DATBI':nesovpaden_datas[11],
    'KUNNR':nesovpaden_datas[12],
    'FKART':nesovpaden_datas[13],
    'AUART':nesovpaden_datas[14],
    'AUGRU':nesovpaden_datas[15],
    'ERROR':nesovpaden_datas[16]

    })
    df_nesovpa =df_nesovpa.replace('nan','')
    if not df_nesovpa.empty:
        df_nesovpa.to_excel(pathtext3)
    
    try:
        df1 = pd.read_excel(f'{MEDIA_ROOT}/{path7}',sheet_name='Sheet1',header=0)

        to_datetime_fmt = partial(pd.to_datetime, format='%d.%m.%Y')

        df1['DATAB'] = df1['DATAB'].apply(to_datetime_fmt)
        df1 = df1.astype(str)
        df1['joined_data']= df1['VKORG'] + df1['KONDA'] + df1['MATNR'] +df1['DATAB']

        # print(df1['joined_data'])

        df2 = pd.read_excel(f'{MEDIA_ROOT}/{path8}',sheet_name='Sheet1',header=0)

        df2 = df2.astype(str)
        df2['joined_data']= df2['Сбытовая организация'] + df2['Группа цен клиента'] + df2['Материал'] +df2['Действ. с']

        # print(df2['joined_data'])
        nesovpaden_datas =[[],[],[],[],
                        [],[],[],[],[],[],[],[],[],[],[],[],[]]

        for key1,row1 in df1.iterrows():
            result = df2[df2['joined_data'] == row1['joined_data'] ]
            # print(row1['joined_data'],result)
            result['Сумма']=result['Сумма'].astype(float)
            result['Сумма']=result['Сумма'].round(decimals = 1)
        
            row1['KBETR']= round(float(row1['KBETR']),1)
            
            result2 =result[result['Сумма'] == row1['KBETR']]
            # print(result['Сумма'])
        
            if result2.empty:
                nesovpaden_datas[0].append(row1['KSCHL'])
                nesovpaden_datas[1].append(row1['VKORG'])
                nesovpaden_datas[2].append(row1['WERKS'])
                nesovpaden_datas[3].append(row1['VTWEG'])
                nesovpaden_datas[4].append(row1['KONDA'])
                nesovpaden_datas[5].append(row1['MATNR'])
                nesovpaden_datas[6].append(row1['KBETR'])
                nesovpaden_datas[7].append(row1['KONWA'])
                nesovpaden_datas[8].append(row1['KPEIN'])
                nesovpaden_datas[9].append(row1['KMEIN'])
                nesovpaden_datas[10].append(row1['DATAB'])
                nesovpaden_datas[11].append(row1['DATBI'])
                nesovpaden_datas[12].append(row1['KUNNR'])
                nesovpaden_datas[13].append(row1['FKART'])
                nesovpaden_datas[14].append(row1['AUART'])
                nesovpaden_datas[15].append(row1['AUGRU'])
                nesovpaden_datas[16].append(result.iloc[0]['Сумма'])
                # print(result,'nesovpaden')
                break
            else:
                pass
                # print(result2,'sovpaden')

        df_nesovpa =pd.DataFrame({
        'KSCHL':nesovpaden_datas[0],
        'VKORG':nesovpaden_datas[1],
        'WERKS':nesovpaden_datas[2],
        'VTWEG':nesovpaden_datas[3],
        'KONDA':nesovpaden_datas[4],
        'MATNR':nesovpaden_datas[5],
        'KBETR':nesovpaden_datas[6],
        'KONWA':nesovpaden_datas[7],
        'KPEIN':nesovpaden_datas[8],
        'KMEIN':nesovpaden_datas[9],
        'DATAB':nesovpaden_datas[10],
        'DATBI':nesovpaden_datas[11],
        'KUNNR':nesovpaden_datas[12],
        'FKART':nesovpaden_datas[13],
        'AUART':nesovpaden_datas[14],
        'AUGRU':nesovpaden_datas[15],
        'ERROR':nesovpaden_datas[16]

        })

        df_nesovpa =df_nesovpa.replace('nan','')
        if not df_nesovpa.empty:
            df_nesovpa.to_excel(pathtext4)
    except:
        pass
    

    try:
        df1 = pd.read_excel(f'{MEDIA_ROOT}/{path9}',sheet_name='Sheet1',header=0)

        to_datetime_fmt = partial(pd.to_datetime, format='%d.%m.%Y')

        df1['DATAB'] = df1['DATAB'].apply(to_datetime_fmt)
        df1 = df1.astype(str)
        df1['joined_data']= df1['VKORG'] + df1['KONDA'] + df1['MATNR'] +df1['DATAB']

        df2 = pd.read_excel(f'{MEDIA_ROOT}/{path10}',sheet_name='Sheet1',header=0)

        df2 = df2.astype(str)
        df2['joined_data']= df2['Сбытовая организация'] + df2['Группа цен клиента'] + df2['Материал'] +df2['Действ. с']

        nesovpaden_datas =[[],[],[],[],
                        [],[],[],[],[],[],[],[],[],[],[],[],[]]

        for key1,row1 in df1.iterrows():
            result = df2[df2['joined_data'] == row1['joined_data'] ]
            result['Сумма']=result['Сумма'].astype(float)
            result['Сумма']=result['Сумма'].round(decimals = 1)
        
            row1['KBETR']= round(float(row1['KBETR']),1)
            
            result2 =result[result['Сумма'] == row1['KBETR']]
        
        
            if result2.empty:
                nesovpaden_datas[0].append(row1['KSCHL'])
                nesovpaden_datas[1].append(row1['VKORG'])
                nesovpaden_datas[2].append(row1['WERKS'])
                nesovpaden_datas[3].append(row1['VTWEG'])
                nesovpaden_datas[4].append(row1['KONDA'])
                nesovpaden_datas[5].append(row1['MATNR'])
                nesovpaden_datas[6].append(row1['KBETR'])
                nesovpaden_datas[7].append(row1['KONWA'])
                nesovpaden_datas[8].append(row1['KPEIN'])
                nesovpaden_datas[9].append(row1['KMEIN'])
                nesovpaden_datas[10].append(row1['DATAB'])
                nesovpaden_datas[11].append(row1['DATBI'])
                nesovpaden_datas[12].append(row1['KUNNR'])
                nesovpaden_datas[13].append(row1['FKART'])
                nesovpaden_datas[14].append(row1['AUART'])
                nesovpaden_datas[15].append(row1['AUGRU'])
                nesovpaden_datas[16].append(result.iloc[0]['Сумма'])
                break
            else:
                pass

        df_nesovpa =pd.DataFrame({
        'KSCHL':nesovpaden_datas[0],
        'VKORG':nesovpaden_datas[1],
        'WERKS':nesovpaden_datas[2],
        'VTWEG':nesovpaden_datas[3],
        'KONDA':nesovpaden_datas[4],
        'MATNR':nesovpaden_datas[5],
        'KBETR':nesovpaden_datas[6],
        'KONWA':nesovpaden_datas[7],
        'KPEIN':nesovpaden_datas[8],
        'KMEIN':nesovpaden_datas[9],
        'DATAB':nesovpaden_datas[10],
        'DATBI':nesovpaden_datas[11],
        'KUNNR':nesovpaden_datas[12],
        'FKART':nesovpaden_datas[13],
        'AUART':nesovpaden_datas[14],
        'AUGRU':nesovpaden_datas[15],
        'ERROR':nesovpaden_datas[16]

        })

        df_nesovpa =df_nesovpa.replace('nan','')
        if not df_nesovpa.empty:
            df_nesovpa.to_excel(pathtext5)
    except:
        pass
    


    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path11}',sheet_name='Sheet1',header=0)

    to_datetime_fmt = partial(pd.to_datetime, format='%d.%m.%Y')

    df1['DATAB'] = df1['DATAB'].apply(to_datetime_fmt)
    df1 = df1.astype(str)
    df1['joined_data']= df1['VKORG'] + df1['KONDA'] + df1['MATNR'] +df1['DATAB']

    df2 = pd.read_excel(f'{MEDIA_ROOT}/{path12}',sheet_name='Sheet1',header=0)

    df2 = df2.astype(str)
    df2['joined_data']= df2['Сбытовая организация'] + df2['Группа цен клиента'] + df2['Материал'] +df2['Действ. с']

    nesovpaden_datas =[[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[],[],[],[]]
    
    # print(df1['joined_data'],'df1')
    # print(df2['joined_data'],'df2')

    for key1,row1 in df1.iterrows():
        result = df2[df2['joined_data'] == row1['joined_data']]
        # print(result)
        result['Сумма']=result['Сумма'].astype(float)
        result['Сумма']=result['Сумма'].round(decimals = 1)
    
        row1['KBETR']= round(float(row1['KBETR']),1)
        
        result2 =result[result['Сумма'] == row1['KBETR']]
    
        if result2.empty:
            nesovpaden_datas[0].append(row1['KSCHL'])
            nesovpaden_datas[1].append(row1['VKORG'])
            nesovpaden_datas[2].append(row1['WERKS'])
            nesovpaden_datas[3].append(row1['VTWEG'])
            nesovpaden_datas[4].append(row1['KONDA'])
            nesovpaden_datas[5].append(row1['MATNR'])
            nesovpaden_datas[6].append(row1['KBETR'])
            nesovpaden_datas[7].append(row1['KONWA'])
            nesovpaden_datas[8].append(row1['KPEIN'])
            nesovpaden_datas[9].append(row1['KMEIN'])
            nesovpaden_datas[10].append(row1['DATAB'])
            nesovpaden_datas[11].append(row1['DATBI'])
            nesovpaden_datas[12].append(row1['KUNNR'])
            nesovpaden_datas[13].append(row1['FKART'])
            nesovpaden_datas[14].append(row1['AUART'])
            nesovpaden_datas[15].append(row1['AUGRU'])
            nesovpaden_datas[16].append(result.iloc[0]['Сумма'])
            break
        else:
            pass

    df_nesovpa =pd.DataFrame({
    'KSCHL':nesovpaden_datas[0],
    'VKORG':nesovpaden_datas[1],
    'WERKS':nesovpaden_datas[2],
    'VTWEG':nesovpaden_datas[3],
    'KONDA':nesovpaden_datas[4],
    'MATNR':nesovpaden_datas[5],
    'KBETR':nesovpaden_datas[6],
    'KONWA':nesovpaden_datas[7],
    'KPEIN':nesovpaden_datas[8],
    'KMEIN':nesovpaden_datas[9],
    'DATAB':nesovpaden_datas[10],
    'DATBI':nesovpaden_datas[11],
    'KUNNR':nesovpaden_datas[12],
    'FKART':nesovpaden_datas[13],
    'AUART':nesovpaden_datas[14],
    'AUGRU':nesovpaden_datas[15],
    'ERROR':nesovpaden_datas[16]

    })

    df_nesovpa =df_nesovpa.replace('nan','')
    if not df_nesovpa.empty:
        df_nesovpa.to_excel(pathtext6)
    



    file_path =f'{pathzip}.zip'

    zip(pathzip, pathzip)
    

    files = [FileG(file=file_path,filetype='obichniy')]
    context ={
        'files':files
    }
    return render(request,'online_savdo/zip_file_download.html',context)

 

