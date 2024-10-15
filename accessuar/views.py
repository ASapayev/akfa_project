from django.shortcuts import render,redirect
from config.settings import MEDIA_ROOT
from .forms import AccessuarFileForm
from .models import Norma,Siryo,TexcartaBase,DataForText,OrderACS,AccessuarFiles
import modin.pandas as pd
from .utils import get_norma_df,get_norma_price,create_folder,lenght_generate_texcarta,get_sapcodes
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.http import JsonResponse
import json
from django.db.models import Q
from django.core.paginator import Paginator
import numpy as np
from .serializers import NormaSerializers
from datetime import datetime


class File:
    def __init__(self,file):
        self.file = file

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def texcarta_delete(request):
    
    if request.method =='POST':
        ozmk = request.POST.get('ozmk',None)
          
        if ozmk:
            ozmks =ozmk.split()
            for ozm in ozmks:
                if TexcartaBase.objects.filter(material = ozm).exists():
                    texcarta = TexcartaBase.objects.filter(material = ozm)[:1].get()
                    texcarta.delete()
            return render(request,'norma/accessuar/norma_sapcode.html')
    else:
        return render(request,'norma/accessuar/norma_sapcode.html')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def check_sapcode(request):
    if request.method =='POST':
        ozmk = request.POST.get('ozmk',None)
          
        if ozmk:
            ozmks =ozmk.split()
            norma_exists = []
            example_exists = []
            new = []
            for ozm in ozmks:
                if Norma.objects.filter(data__sap_code__icontains = ozm).exists():
                    norma_exists.append(ozm)
                else:
                    new.append(ozm)

                if Norma.objects.filter(data__sap_code__icontains = ozm.split('-')[0]).exists():
                    norm = Norma.objects.filter(data__sap_code__icontains = ozm.split('-')[0])[:1].get()
                    example_exists.append([ozm,norm.data['sap_code'],norm.id])

            context ={
                'norma_exists':norma_exists,
                'example_exists':example_exists,
                'new':new
            }
            return render(request,'norma/accessuar/check.html',context)
    else:
        return render(request,'norma/accessuar/norma_sapcode.html')
    
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def get_accessuar_sapcode(request):
    if request.method =='POST':
        ozmk = request.POST.get('ozmk',None)
          
        if ozmk:
            ozmks =ozmk.split()
            path = get_norma_df(ozmks)
            files = [File(file=p) for p in path]
            context ={
                'files':files,
                'section':'SAP code'
            }
            return render(request,'norma/accessuar/generated_files.html',context)
    else:
        return render(request,'norma/accessuar/norma_sapcode.html')
    
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def get_accessuar_sapcode_narx(request):
    if request.method =='POST':
        ozmk = request.POST.get('ozmk',None)
          
        if ozmk:
            ozmks =ozmk.split()
            path = get_norma_price(ozmks)
            files = [File(file=p) for p in path]
            context ={
                'files':files,
                'section':'SAP code'
            }
            return render(request,'norma/accessuar/generated_files.html',context)
    else:
        return render(request,'norma/accessuar/norma_sapcode.html')
    
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def get_accessuar_sapcode_texcarta(request):
    if request.method =='POST':
        ozmk = request.POST.get('ozmk',None)
          
        if ozmk:
            ozmks =ozmk.split()
            path = lenght_generate_texcarta(ozmks)
            files = [File(file=p) for p in path]
            context ={
                'files':files,
                'section':'SAP code'
            }
            return render(request,'norma/accessuar/generated_files.html',context)
    else:
        return render(request,'norma/accessuar/norma_sapcode.html')
    

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def delete_texcarta(request,id):
    norm = Norma.objects.get(id = id)
    data = norm.data
    # print(data,'++'*20)
    if 'ARBPL' in data:
        del data['ARBPL']
    if 'LGORD' in data:
        del data['LGORD']
    norm.data = data
    norm.save()
    return JsonResponse({'status':201})


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def delete_siryo(request,id):
    norm = Siryo.objects.get(id = id)
    norm.delete()
    return JsonResponse({'status':201})

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def delete_sapcode(request,id):
    norm = Norma.objects.get(id = id)
    norm.delete()
    return JsonResponse({'status':201})

profile_type ={
      '-LA/LC':0,
      '-PA':1,
      '-PC':2,
      '-MO':3,
      '-GZ':4,
      '-AN':5,
      '-TP':6,
      '-RU':7,
      '-SN':8,
      '-VS':9,
      '-KL':10,
      '-SK':11,
      '-TP':12,
      '-ZG':13,
      '-7':14,
    }

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def copy_sapcode(request,id):
    if request.method =='POST':
        data = list(request.POST.keys())[0]
        items = json.loads(data)
        name_of_type =''
        all_data =[]
        new_data = []
        for item in items:
            for val in item:
                if isinstance(val,str):
                    if len(new_data) > 0 and name_of_type !='':
                        df = pd.DataFrame(np.array(new_data),columns=['SAP CODE','KRATKIY TEXT','BEI','COUNT','FACT','PLAN'])
                        data_gp = generate_datas(df,['SAP CODE','KRATKIY TEXT','BEI','PLAN','FACT'],name_of_type)
                        data_gp = generate_sap_code_price(data_gp)
                        
                        all_data +=data_gp
                        new_data = []
                    name_of_type = val
                else:
                    if val[0] != '':
                        new_data.append(val)
            if len(new_data) > 0 and name_of_type !='':
                df = pd.DataFrame(np.array(new_data),columns=['SAP CODE','KRATKIY TEXT','BEI','COUNT','FACT','PLAN'])
                
                data_gp = generate_datas(df,['SAP CODE','KRATKIY TEXT','BEI','PLAN','FACT'],name_of_type)
                data_gp = generate_sap_code_price(data_gp)
                all_data +=data_gp
                new_data = []
        data_list = [dat for dat in all_data if not Norma.objects.filter(data__sap_code=dat['sap_code']).exists()] 
    
        if len(data_list)>0:
            instances_to_create = [Norma(data=data) for data in data_list]
            Norma.objects.bulk_create(instances_to_create)
            return JsonResponse({'saved':True,'status':201})
        else:
            return JsonResponse({'saved':False,'status':301})
    else:
        norm = Norma.objects.get(id = id)
        normalar = get_sapcodes([norm.data['sap_code'],])
        checker =[False for i in range(0 , 15)]
        datas = {
            '-LA/LC':[],
            '-PA':[],
            '-PC':[],
            '-MO':[],
            '-GZ':[],
            '-AN':[],
            '-TP':[],
            '-RU':[],
            '-SN':[],
            '-VS':[],
            '-KL':[],
            '-SK':[],
            '-TP':[],
            '-ZG':[],
            '-7':[],
        }
        for norma in normalar:
            index =norma.data['sap_code'].find('-')
            profile_t =''
            if '-7' in norma.data['sap_code'][index:index+3]:
                profile_t ='-7'
            else:
                if '-LA' in norma.data['sap_code'][index:index+3] or '-LC' in norma.data['sap_code'][index:index+3]:
                    profile_t = '-LA/LC'
                else:
                    profile_t = norma.data['sap_code'][index:index+3]

            checker[profile_type[profile_t]] = True
            dat = NormaSerializers(norma , many=False).data
            datas[profile_t].append(dat)

        context ={
            'checker':json.dumps(checker),
            'data':json.dumps(datas),
            'id':id
        }

    return render(request,'norma/accessuar/copy.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def edit_sapcode(request,id):
    if request.method =='POST':
        data = list(request.POST.keys())[0]
        items = json.loads(data)
        name_of_type =''
        all_data =[]
        new_data = []
        for item in items:
            for val in item:
                if isinstance(val,str):
                    if len(new_data) > 0 and name_of_type !='':
                        df = pd.DataFrame(np.array(new_data),columns=['SAP CODE','KRATKIY TEXT','BEI','COUNT','FACT','PLAN'])
                        data_gp = generate_datas(df,['SAP CODE','KRATKIY TEXT','BEI','PLAN','FACT'],name_of_type)
                        data_gp = generate_sap_code_price(data_gp)
                        
                        all_data +=data_gp
                        new_data = []
                    name_of_type = val
                else:
                    if val[0] != '':
                        new_data.append(val)
            if len(new_data) > 0 and name_of_type !='':
                df = pd.DataFrame(np.array(new_data),columns=['SAP CODE','KRATKIY TEXT','BEI','COUNT','FACT','PLAN'])
                
                data_gp = generate_datas(df,['SAP CODE','KRATKIY TEXT','BEI','PLAN','FACT'],name_of_type)
                data_gp = generate_sap_code_price(data_gp)
                all_data +=data_gp
                new_data = []
        data_list = all_data
        if len(data_list) > 0:
            for dat in data_list:
                norma = Norma.objects.get(data__sap_code = dat['sap_code'])
                norma.data =dat
                norma.save()
            return JsonResponse({'saved':True,'status':201})
        else:
            return JsonResponse({'saved':False,'status':301})
    else:
        norm = Norma.objects.get(id = id)
        normalar = get_sapcodes([norm.data['sap_code'],])
        checker =[False for i in range(0 , 15)]
        datas = {
            '-LA/LC':[],
            '-PA':[],
            '-PC':[],
            '-MO':[],
            '-GZ':[],
            '-AN':[],
            '-TP':[],
            '-RU':[],
            '-SN':[],
            '-VS':[],
            '-KL':[],
            '-SK':[],
            '-TP':[],
            '-ZG':[],
            '-7':[],
        }
        for norma in normalar:
            index =norma.data['sap_code'].find('-')
            profile_t =''
            if '-7' in norma.data['sap_code'][index:index+3]:
                profile_t ='-7'
            else:
                if '-LA' in norma.data['sap_code'][index:index+3] or '-LC' in norma.data['sap_code'][index:index+3]:
                    profile_t = '-LA/LC'
                else:
                    profile_t = norma.data['sap_code'][index:index+3]

            checker[profile_type[profile_t]] = True
            dat = NormaSerializers(norma , many=False).data
            datas[profile_t].append(dat)

        context ={
            'checker':json.dumps(checker),
            'data':json.dumps(datas),
            'id':id
        }

    return render(request,'norma/accessuar/edit.html',context)



@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def texcarta_list(request):
    search = request.GET.get('search',None)
    if search:
        norma = Norma.objects.filter(Q(data__sap_code__icontains =search)&Q(data__has_key='ARBPL')&Q(data__has_key='LGORD')).order_by('-updated_at')
    else:
        norma = Norma.objects.filter(Q(data__has_key='ARBPL')&Q(data__has_key='LGORD')).order_by('-updated_at')
        

    paginator = Paginator(norma, 25)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)
    context ={
        'products':page_obj
    }
    return render(request,'norma/accessuar/texcarta_list.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def siryo_list(request):
    search = request.GET.get('search',None)
    if search:
        norma = Siryo.objects.filter(data__sap_code__icontains =search).order_by('-updated_at')
    else:
        norma = Siryo.objects.filter(Q(data__sap_code__startswith ='ASM')|Q(data__sap_code__startswith ='1')).order_by('-updated_at')

    paginator = Paginator(norma, 25)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)
    context ={
        'products':page_obj
    }
    return render(request,'norma/accessuar/siryo_list.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def update_texcarta(request,id):
    norma = Norma.objects.get(id = id)
    if request.method == 'POST':
        data = list(request.POST.keys())[0]
        items = json.loads(data)
        json_data = norma.data
        json_data['ARBPL'] = [items['arbpl1'],items['arbpl2'],items['arbpl3']]
        json_data['LGORD'] = items['lgord']
        norma.data =json_data
        norma.save()
        return JsonResponse({'saved':True,'status':201})
    context ={
        'norma':norma
    }
    return render(request,'norma/accessuar/update_texcarta.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def update_siryo(request,id):
    siryo = Siryo.objects.get(id = id)
    if request.method == 'POST':
        data = list(request.POST.keys())[0]
        items = json.loads(data)
        siryo.data ={'sap_code':items['artikul'],'kratkiy_text':items['kratkiy_text'],'menge':items['menge'],'price':'0'}
        siryo.save()
        return JsonResponse({'saved':True,'status':201})
    context ={
        'siryo':siryo
    }
    return render(request,'norma/accessuar/update_siryo.html',context)
        

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def new_texcarta(request):
    if request.method == 'POST':
        data = list(request.POST.keys())[0]
        items = json.loads(data)
        print(items)
        try:
            for item in items:
                print(item['artikul'],item['arbpl1'],item['arbpl2'],item['arbpl3'],item['lgord'])
                if not Norma.objects.filter(Q(data__sap_code__icontains =item['artikul'])&Q(data__has_key ='ARBPL')&Q(data__has_key ='LGORD')).exists():
                    if Norma.objects.filter(data__sap_code__icontains =item['artikul']).exists():
                        norma = Norma.objects.get(data__sap_code__icontains =item['artikul'])
                        json_data = norma.data
                        json_data['ARBPL'] = [item['arbpl1'],item['arbpl2'],item['arbpl3']]
                        json_data['LGORD'] = item['lgord']
                        norma.data =json_data
                        norma.save()
            return JsonResponse({'saved':True,'status':201})        
        except:
            return JsonResponse({'saved':False,'status':301})

    return render(request,'norma/accessuar/new_texcarta.html')
        
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def new_siryo(request):
    if request.method == 'POST':
        data = list(request.POST.keys())[0]
        items = json.loads(data)
        if not Siryo.objects.filter(data__sap_code__icontains =items['artikul']).exists():
            siryo =Siryo(
                data ={'sap_code':items['artikul'],'kratkiy_text':items['kratkiy_text'],'menge':items['menge'],'price':'0'}
                    )
            siryo.save()
            return JsonResponse({'saved':True,'status':201})
        else:
            return JsonResponse({'saved':False,'status':301})

       
        

    return render(request,'norma/accessuar/new_siryo.html')





@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def show_sapcodes(request):
    search = request.GET.get('search',None)
    if search:
        norma = Norma.objects.filter(data__sap_code__icontains =search).order_by('-updated_at')
    else:
        norma = Norma.objects.filter(data__sap_code__icontains ='-7').order_by('-updated_at')

    paginator = Paginator(norma, 25)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)
    context ={
        'products':page_obj
    }
    return render(request,'norma/accessuar/list_sapcodes.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def full_update_siryo(request):
    if request.method == 'POST':
        data = request.POST.copy()
        form = AccessuarFileForm(data, request.FILES)
        if form.is_valid():
            siryo = Siryo.objects.all()
            siryo.delete()
            form_file = form.save()
            file = form_file.file
            path =f'{MEDIA_ROOT}/{file}'
            
            df = pd.read_excel(path,header=0,sheet_name='Сырьё')
            for key,row in df.iterrows():
                Siryo(
                    data ={'sap_code':row['SAPCODE'],'kratkiy_text':row['KRATKIY TEXT'],'menge':row['NARX'],'price':'0'}
                ).save()

    return render(request,'norma/benkam/main.html')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def update_text_base(request):
    if request.method == 'POST':
        data = request.POST.copy()
        form = AccessuarFileForm(data, request.FILES)
        if form.is_valid():
            form_file = form.save()
            file = form_file.file
            path =f'{MEDIA_ROOT}/{file}'
            df = pd.read_excel(path,header=0)
            DataForText.objects.all().delete()
            df = df.astype(str)
            df = df.replace('nan','')
            colums_name = list(df.columns)
            data =[]
            for key,row in df.iterrows():
                dat ={}
                for col in colums_name:
                    dat[col] = row[col]
                data.append(dat)
            
            items =[DataForText(data=dat) for dat in data]
            DataForText.objects.bulk_create(items)

    return render(request,'norma/benkam/main.html')


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def full_update_texcarta(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['type']='termo'
        form = AccessuarFileForm(data, request.FILES)
        if form.is_valid():
            form_file = form.save()
            file = form_file.file
            path =f'{MEDIA_ROOT}/{file}'
            
            df = pd.read_excel(path,header=0)
            
            df = df.astype(str)
            df = df.replace('nan','0')
            df = df.replace('0.0','0')
            for key,row in df.iterrows():
                norma_exists = Norma.objects.filter(data__sap_code__icontains =row['SAPCODE']).exists()
                if norma_exists:
                    norma = Norma.objects.filter(data__sap_code__icontains =row['SAPCODE'])[:1].get()
                    arbpl = []
                    if row['ARBPL1'] !='0':
                        arbpl.append(row['ARBPL1'])
                    if row['ARBPL2'] !='0':
                        arbpl.append(row['ARBPL2'])
                    if row['ARBPL3'] !='0':
                        arbpl.append(row['ARBPL3'])
                    norma.data['ARBPL'] = arbpl
                    norma.data['LGORD'] = row['LGORD']
                    norma.save()
    return render(request,'norma/benkam/main.html')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def create_norma_post(request):

    data = list(request.POST.keys())[0]
    items = json.loads(data)
    
    name_of_type =''
    all_data =[]
    new_data = []
    for item in items:
        for val in item:
            if isinstance(val,str):
                if len(new_data) > 0 and name_of_type !='':
                    df = pd.DataFrame(np.array(new_data),columns=['SAP CODE','KRATKIY TEXT','BEI','COUNT','FACT','PLAN'])
                    data_gp = generate_datas(df,['SAP CODE','KRATKIY TEXT','BEI','PLAN','FACT'],name_of_type)
                    data_gp = generate_sap_code_price(data_gp)
                    
                    all_data +=data_gp
                    new_data = []
                name_of_type = val
            else:
                if val[0] != '':
                    val[4] = val[4].replace(',','.')
                    val[5]= val[5].replace(',','.')
                    new_data.append(val)
        if len(new_data) > 0 and name_of_type !='':
            df = pd.DataFrame(np.array(new_data),columns=['SAP CODE','KRATKIY TEXT','BEI','COUNT','FACT','PLAN'])
            
            data_gp = generate_datas(df,['SAP CODE','KRATKIY TEXT','BEI','PLAN','FACT'],name_of_type)
            data_gp = generate_sap_code_price(data_gp)
            all_data +=data_gp
            new_data = []
        # print(new_data)
        
        
    data_list = [dat for dat in all_data if not Norma.objects.filter(data__sap_code=dat['sap_code']).exists()] 
    
    if len(data_list)>0:
        instances_to_create = [Norma(data=data) for data in data_list]
        Norma.objects.bulk_create(instances_to_create)
        return JsonResponse({'saved':True,'status':201})
    else:
        return JsonResponse({'saved':False,'status':301})

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def update_norma_post(request,id):

    data = list(request.POST.keys())[0]
    items = json.loads(data)
    name_of_type =''
    all_data =[]
    new_data = []
    for item in items:
        for val in item:
            if isinstance(val,str):
                if len(new_data) > 0 and name_of_type !='':
                    df = pd.DataFrame(np.array(new_data),columns=['SAP CODE','KRATKIY TEXT','BEI','COUNT','FACT','PLAN'])
                    data_gp = generate_datas(df,['SAP CODE','KRATKIY TEXT','BEI','PLAN','FACT'],name_of_type)
                    data_gp = generate_sap_code_price(data_gp)
                    
                    all_data +=data_gp
                    new_data = []
                name_of_type = val
            else:
                if val[0] != '':
                    new_data.append(val)
        if len(new_data) > 0 and name_of_type !='':
            df = pd.DataFrame(np.array(new_data),columns=['SAP CODE','KRATKIY TEXT','BEI','COUNT','FACT','PLAN'])
            
            data_gp = generate_datas(df,['SAP CODE','KRATKIY TEXT','BEI','PLAN','FACT'],name_of_type)
            data_gp = generate_sap_code_price(data_gp)
            all_data +=data_gp
            new_data = []
        # print(new_data)
        
        
    data_list = [dat for dat in all_data if not Norma.objects.filter(data__sap_code=dat['sap_code']).exists()] 
  
    if len(data_list)>0:
        instances_to_create = [Norma(data=data) for data in data_list]
        Norma.objects.bulk_create(instances_to_create)
        return JsonResponse({'saved':True,'status':201})
    else:
        return JsonResponse({'saved':False,'status':301})


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def create_new_norma(request):
    return render(request,'norma/accessuar/create.html')



@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user_accessuar'])
def full_update_norm(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['type']='termo'
        form = AccessuarFileForm(data, request.FILES)
        if form.is_valid():
            normaa = Norma.objects.all()
            normaa.delete()
            form_file = form.save()
            file = form_file.file
            path =f'{MEDIA_ROOT}/{file}'
            
            df = pd.read_excel(path,sheet_name='ГП ПЕРЕДЕЛИ',header=0)
            
            df = df.astype(str)
            df = df.replace('nan','0')
            df = df.replace('0.0','0')

            df_new_la_lc = pd.DataFrame()
            df_new_la_lc['Нумерация до Цинк 1 шт'] = df['Нумерация до Цинк 1 шт']
            df_new_la_lc['Литё Алюмин.2 шт / Литё Цинк 1 шт'] = df['Литё Алюмин.2 шт / Литё Цинк 1 шт']
            df_new_la_lc['БЕИЛитё Алюмин.2 шт / Литё Цинк 1 шт'] = df['БЕИЛитё Алюмин.2 шт / Литё Цинк 1 шт']
            df_new_la_lc['Вес плановыйЛитё Алюмин.2 шт / Литё Цинк 1 шт'] = df['Вес плановыйЛитё Алюмин.2 шт / Литё Цинк 1 шт']
            df_new_la_lc['Вес фактическийЛитё Алюмин.2 шт / Литё Цинк 1 шт'] = df['Вес фактическийЛитё Алюмин.2 шт / Литё Цинк 1 шт']

            data_la_lc = generate_datas(df_new_la_lc,['Нумерация до Цинк 1 шт','Литё Алюмин.2 шт / Литё Цинк 1 шт','БЕИЛитё Алюмин.2 шт / Литё Цинк 1 шт','Вес плановыйЛитё Алюмин.2 шт / Литё Цинк 1 шт','Вес фактическийЛитё Алюмин.2 шт / Литё Цинк 1 шт'],'-LA/LC')
            data_la_lc = generate_sap_code_price(data_la_lc)
            
            df_new_pa = pd.DataFrame()
            df_new_pa['Нумерация до SAPЛитейный пресс машины мини Ал. 9 шт'] = df['Нумерация до SAPЛитейный пресс машины мини Ал. 9 шт']
            df_new_pa['Литейный пресс машины мини Ал. 9 шт'] = df['Литейный пресс машины мини Ал. 9 шт']
            df_new_pa['БЕИЛитейный пресс машины мини Ал. 9 шт'] = df['БЕИЛитейный пресс машины мини Ал. 9 шт']
            df_new_pa['Вес плановыйЛитейный пресс машины мини Ал. 9 шт'] = df['Вес плановыйЛитейный пресс машины мини Ал. 9 шт']
            df_new_pa['Вес фактическийЛитейный пресс машины мини Ал. 9 шт'] = df['Вес фактическийЛитейный пресс машины мини Ал. 9 шт']

            data_pa = generate_datas(df_new_pa,['Нумерация до SAPЛитейный пресс машины мини Ал. 9 шт','Литейный пресс машины мини Ал. 9 шт','БЕИЛитейный пресс машины мини Ал. 9 шт','Вес плановыйЛитейный пресс машины мини Ал. 9 шт','Вес фактическийЛитейный пресс машины мини Ал. 9 шт'],'-PA')
            data_pa = generate_sap_code_price(data_pa)

            df_new_pc = pd.DataFrame()
            df_new_pc['Нумерация до SAPЛитейный пресс машины мини Цинк 6 шт'] = df['Нумерация до SAPЛитейный пресс машины мини Цинк 6 шт']
            df_new_pc['Литейный пресс машины мини Цинк 6 шт'] = df['Литейный пресс машины мини Цинк 6 шт']
            df_new_pc['БЕИЛитейный пресс машины мини Цинк 6 шт'] = df['БЕИЛитейный пресс машины мини Цинк 6 шт']
            df_new_pc['Вес плановыйЛитейный пресс машины мини Цинк 6 шт'] = df['Вес плановыйЛитейный пресс машины мини Цинк 6 шт']
            df_new_pc['Вес фактическийЛитейный пресс машины мини Цинк 6 шт'] = df['Вес фактическийЛитейный пресс машины мини Цинк 6 шт']

            data_pc = generate_datas(df_new_pc,['Нумерация до SAPЛитейный пресс машины мини Цинк 6 шт','Литейный пресс машины мини Цинк 6 шт','БЕИЛитейный пресс машины мини Цинк 6 шт','Вес плановыйЛитейный пресс машины мини Цинк 6 шт','Вес фактическийЛитейный пресс машины мини Цинк 6 шт'],'-PC')
            data_pc = generate_sap_code_price(data_pc)

            df_new_mo = pd.DataFrame()
            df_new_mo['Нумерация до SAPМех. Обработка 20 шт'] = df['Нумерация до SAPМех. Обработка 20 шт']
            df_new_mo['Мех. Обработка 20 шт'] = df['Мех. Обработка 20 шт']
            df_new_mo['БЕИМех. Обработка 20 шт'] = df['БЕИМех. Обработка 20 шт']
            df_new_mo['Вес плановыйМех. Обработка 20 шт'] = df['Вес плановыйМех. Обработка 20 шт']
            df_new_mo['Вес фактическийМех. Обработка 20 шт'] = df['Вес фактическийМех. Обработка 20 шт']

            data_mo = generate_datas(df_new_mo,['Нумерация до SAPМех. Обработка 20 шт','Мех. Обработка 20 шт','БЕИМех. Обработка 20 шт','Вес плановыйМех. Обработка 20 шт','Вес фактическийМех. Обработка 20 шт'],'-MO')
            data_mo = generate_sap_code_price(data_mo)


            df_new_gz = pd.DataFrame()
            df_new_gz['Нумерация до SAPГальванизация'] = df['Нумерация до SAPГальванизация']
            df_new_gz['Гальванизация'] = df['Гальванизация']
            df_new_gz['БЕИГальванизация'] = df['БЕИГальванизация']
            df_new_gz['Вес плановыйГальванизация'] = df['Вес плановыйГальванизация']
            df_new_gz['Вес фактическийГальванизация'] = df['Вес фактическийГальванизация']

            data_gz = generate_datas(df_new_gz,['Нумерация до SAPГальванизация','Гальванизация','БЕИГальванизация','Вес плановыйГальванизация','Вес фактическийГальванизация'],'-GZ')
            data_gz = generate_sap_code_price(data_gz)



            
            df_new_ru = pd.DataFrame()
            df_new_ru['Нумерация до SAPРезка + Упк'] = df['Нумерация до SAPРезка + Упк']
            df_new_ru['Резка + Упк'] = df['Резка + Упк']
            df_new_ru['БЕИРезка + Упк'] = df['БЕИРезка + Упк']
            df_new_ru['Вес плановыйРезка + Упк'] = df['Вес плановыйРезка + Упк']
            df_new_ru['Вес фактическийРезка + Упк'] = df['Вес фактическийРезка + Упк']

            data_ru = generate_datas(df_new_ru,['Нумерация до SAPРезка + Упк','Резка + Упк','БЕИРезка + Упк','Вес плановыйРезка + Упк','Вес фактическийРезка + Упк'],'-RU')
            data_ru = generate_sap_code_price(data_ru)

            df_new_sn = pd.DataFrame()
            df_new_sn['Нумерация до SAPШтамповка'] = df['Нумерация до SAPШтамповка']
            df_new_sn['Штамповка'] = df['Штамповка']
            df_new_sn['БЕИШтамповка'] = df['БЕИШтамповка']
            df_new_sn['Вес плановыйШтамповка'] = df['Вес плановыйШтамповка']
            df_new_sn['Вес фактическийШтамповка'] = df['Вес фактическийШтамповка']

            data_sn = generate_datas(df_new_sn,['Нумерация до SAPШтамповка','Штамповка','БЕИШтамповка','Вес плановыйШтамповка','Вес фактическийШтамповка'],'-SN')
            data_sn = generate_sap_code_price(data_sn)


            df_new_vs = pd.DataFrame()
            df_new_vs['Нумерация до SAPВибро.Голтовка 8 шт и Сушка'] = df['Нумерация до SAPВибро.Голтовка 8 шт и Сушка']
            df_new_vs['Вибро.Голтовка 8 шт и Сушка'] = df['Вибро.Голтовка 8 шт и Сушка']
            df_new_vs['БЕИВибро.Голтовка 8 шт и Сушка'] = df['БЕИВибро.Голтовка 8 шт и Сушка']
            df_new_vs['Вес плановыйВибро.Голтовка 8 шт и Сушка'] = df['Вес плановыйВибро.Голтовка 8 шт и Сушка']
            df_new_vs['Вес фактическийВибро.Голтовка 8 шт и Сушка'] = df['Вес фактическийВибро.Голтовка 8 шт и Сушка']

            data_vs = generate_datas(df_new_vs,['Нумерация до SAPВибро.Голтовка 8 шт и Сушка','Вибро.Голтовка 8 шт и Сушка','БЕИВибро.Голтовка 8 шт и Сушка','Вес плановыйВибро.Голтовка 8 шт и Сушка','Вес фактическийВибро.Голтовка 8 шт и Сушка'],'-VS')
            data_vs = generate_sap_code_price(data_vs)


            df_new_kl = pd.DataFrame()
            df_new_kl['Нумерация до SAPПокраска + Нанесение логотипа (гравировка)'] = df['Нумерация до SAPПокраска + Нанесение логотипа (гравировка)']
            df_new_kl['Покраска + Нанесение логотипа (гравировка)'] = df['Покраска + Нанесение логотипа (гравировка)']
            df_new_kl['БЕИПокраска + Нанесение логотипа (гравировка)'] = df['БЕИПокраска + Нанесение логотипа (гравировка)']
            df_new_kl['Вес плановыйПокраска + Нанесение логотипа (гравировка)'] = df['Вес плановыйПокраска + Нанесение логотипа (гравировка)']
            df_new_kl['Вес фактическийПокраска + Нанесение логотипа (гравировка)'] = df['Вес фактическийПокраска + Нанесение логотипа (гравировка)']

            data_kl = generate_datas(df_new_kl,['Нумерация до SAPПокраска + Нанесение логотипа (гравировка)','Покраска + Нанесение логотипа (гравировка)','БЕИПокраска + Нанесение логотипа (гравировка)','Вес плановыйПокраска + Нанесение логотипа (гравировка)','Вес фактическийПокраска + Нанесение логотипа (гравировка)'],'-K')
            data_kl = generate_sap_code_price(data_kl)

            df_new_an = pd.DataFrame()
            df_new_an['Нумерация до SAPПокраска + Нанесение логотипа (гравировка)'] = df['Нумерация до SAPПокраска + Нанесение логотипа (гравировка)']
            df_new_an['Покраска + Нанесение логотипа (гравировка)'] = df['Покраска + Нанесение логотипа (гравировка)']
            df_new_an['БЕИПокраска + Нанесение логотипа (гравировка)'] = df['БЕИПокраска + Нанесение логотипа (гравировка)']
            df_new_an['Вес плановыйПокраска + Нанесение логотипа (гравировка)'] = df['Вес плановыйПокраска + Нанесение логотипа (гравировка)']
            df_new_an['Вес фактическийПокраска + Нанесение логотипа (гравировка)'] = df['Вес фактическийПокраска + Нанесение логотипа (гравировка)']

            data_an = generate_datas(df_new_an,['Нумерация до SAPПокраска + Нанесение логотипа (гравировка)','Покраска + Нанесение логотипа (гравировка)','БЕИПокраска + Нанесение логотипа (гравировка)','Вес плановыйПокраска + Нанесение логотипа (гравировка)','Вес фактическийПокраска + Нанесение логотипа (гравировка)'],'-AN')
            data_an = generate_sap_code_price(data_an)


            df_new_sk = pd.DataFrame()
            df_new_sk['Нумерация до SAPШтамповка + Заготовка +Упк'] = df['Нумерация до SAPШтамповка + Заготовка +Упк']
            df_new_sk['Штамповка + Заготовка +Упк'] = df['Штамповка + Заготовка +Упк']
            df_new_sk['БЕИШтамповка + Заготовка +Упк'] = df['БЕИШтамповка + Заготовка +Упк']
            df_new_sk['Вес плановыйШтамповка + Заготовка +Упк'] = df['Вес плановыйШтамповка + Заготовка +Упк']
            df_new_sk['Вес фактическийШтамповка + Заготовка +Упк'] = df['Вес фактическийШтамповка + Заготовка +Упк']

            data_sk = generate_datas(df_new_sk,['Нумерация до SAPШтамповка + Заготовка +Упк','Штамповка + Заготовка +Упк','БЕИШтамповка + Заготовка +Упк','Вес плановыйШтамповка + Заготовка +Упк','Вес фактическийШтамповка + Заготовка +Упк'],'-SK')
            data_sk = generate_sap_code_price(data_sk)

            df_new_tp = pd.DataFrame()
            df_new_tp['Нумерация до SAPТермопласт автомат 7 шт + Упк'] = df['Нумерация до SAPТермопласт автомат 7 шт + Упк']
            df_new_tp['Термопласт автомат 7 шт + Упк'] = df['Термопласт автомат 7 шт + Упк']
            df_new_tp['БЕИТермопласт автомат 7 шт + Упк'] = df['БЕИТермопласт автомат 7 шт + Упк']
            df_new_tp['Вес плановыйТермопласт автомат 7 шт + Упк'] = df['Вес плановыйТермопласт автомат 7 шт + Упк']
            df_new_tp['Вес фактическийТермопласт автомат 7 шт + Упк'] = df['Вес фактическийТермопласт автомат 7 шт + Упк']

            data_tp = generate_datas(df_new_tp,['Нумерация до SAPТермопласт автомат 7 шт + Упк','Термопласт автомат 7 шт + Упк','БЕИТермопласт автомат 7 шт + Упк','Вес плановыйТермопласт автомат 7 шт + Упк','Вес фактическийТермопласт автомат 7 шт + Упк'],'-TP')
            data_tp = generate_sap_code_price(data_tp)


            df_new_zg = pd.DataFrame()
            df_new_zg['Нумерация до SAPЗаготовка и Упковка'] = df['Нумерация до SAPЗаготовка и Упковка']
            df_new_zg['Заготовка и Упковка'] = df['Заготовка и Упковка']
            df_new_zg['БЕИЗаготовка и Упковка'] = df['БЕИЗаготовка и Упковка']
            df_new_zg['Вес плановыйЗаготовка и Упковка'] = df['Вес плановыйЗаготовка и Упковка']
            df_new_zg['Вес фактическийЗаготовка и Упковка'] = df['Вес фактическийЗаготовка и Упковка']

            data_zg = generate_datas(df_new_zg,['Нумерация до SAPЗаготовка и Упковка','Заготовка и Упковка','БЕИЗаготовка и Упковка','Вес плановыйЗаготовка и Упковка','Вес фактическийЗаготовка и Упковка'],'-ZG')
            data_zg = generate_sap_code_price(data_zg)

            
            df_new_gp = pd.DataFrame()
            df_new_gp['Нумерация до SAPСборка + Упк'] = df['Нумерация до SAPСборка + Упк']
            df_new_gp['Сборка + Упк'] = df['Сборка + Упк']
            df_new_gp['БЕИСборка + Упк'] = df['БЕИСборка + Упк']
            df_new_gp['Вес плановыйСборка + Упк'] = df['Вес плановыйСборка + Упк']
            df_new_gp['Вес фактическийСборка + Упк'] = df['Вес фактическийСборка + Упк']

            data_gp = generate_datas(df_new_gp,['Нумерация до SAPСборка + Упк','Сборка + Упк','БЕИСборка + Упк','Вес плановыйСборка + Упк','Вес фактическийСборка + Упк'],'-7')
            data_gp = generate_sap_code_price(data_gp)
            
            data_list =data_gp + data_zg + data_tp + data_sk + data_kl + data_an + data_vs + data_sn + data_ru + data_gz + data_mo + data_pc +data_pa + data_la_lc
            instances_to_create = [Norma(data=data) for data in data_list]
            Norma.objects.bulk_create(instances_to_create)

    return render(request,'norma/benkam/main.html')



def generate_datas(df,names,type_profile) -> list:
    all_data = []
    sap_codesss = []
    # print(df)
    for key,row in df.iterrows():
        if type_profile =='-LA/LC':
            conditon = ('-LA' in row[names[0]] or '-LC' in row[names[0]] or '-7' in row[names[0]]) and row[names[0]] not in sap_codesss
        else:
            # print( row[names[0]],names[0])
            conditon = (type_profile in row[names[0]]  or '-7' in row[names[0]])and('-75' not in row[names[0]]) and row[names[0]] not in sap_codesss
        
        if conditon:
            sap_codesss.append(row[names[0]])
            components = []
            collected_data ={}
            collected_data['sap_code'] =row[names[0]]
            collected_data['ves_corredted'] = False
            collected_data['kratkiy_tekst'] =row[names[1]]
            collected_data['price'] ='0'
            collected_data['bei'] =row[names[2]]
            collected_data['kolichestvo'] ='1'
            collected_data['planoviy'] =row[names[3]]
            collected_data['fact'] =row[names[4]]

            component_sap_codes = []

            for i in range(1,25):
                if type_profile =='-LA/LC':
                    try:
                        if df.iloc[key + i][names[0]] != '0' and '-LA' not in df.iloc[key + i][names[0]] and '-LC' not in df.iloc[key + i][names[0]] and '-7' not in df.iloc[key + i][names[0]] and df.iloc[key + i][names[1]] != '0':
                            component_name =df.iloc[key + i][names[0]]
                            component_value =df.iloc[key + i][names[1]]
                            component_menge =df.iloc[key + i][names[2]]
                            component_ves =df.iloc[key + i][names[3]]   
                            component_fakt =df.iloc[key + i][names[4]]   
                            components.append([component_name,component_value,component_menge,'0',component_ves,'0',component_fakt,'0','0'])
                            component_sap_codes.append(df.iloc[key + i][names[0]])
                        else:
                            break
                    except IndexError:
                        break
                    
                else:
                    try:
                        if df.iloc[key + i][names[0]] != '0' and type_profile not in df.iloc[key + i][names[0]] and '-7' not in df.iloc[key + i][names[0]] and df.iloc[key + i][names[1]] != '0':
                            component_name =df.iloc[key + i][names[0]]
                            component_value =df.iloc[key + i][names[1]]
                            component_menge =df.iloc[key + i][names[2]]
                            component_ves =df.iloc[key + i][names[3]]  
                            component_fakt =df.iloc[key + i][names[4]]  
                            components.append([component_name,component_value,component_menge,'0',component_ves,'0',component_fakt,'0','0'])
                            
                            component_sap_codes.append(df.iloc[key + i][names[0]])
                        else:
                            break
                    except IndexError:
                        break
                    
            collected_data['component_sapcodes'] = component_sap_codes
            collected_data['components'] = components
            all_data.append(collected_data)
    # if type_profile =='-PA':
    #     print(all_data,df)
    return all_data



def generate_sap_code_price(sapcodes):
    siryolar = Siryo.objects.all()
    
    sapcodes_copy = sapcodes.copy()
    siryo_menge ={}
    siryo_price ={}
    for siryo in siryolar:
        siryo_menge[f'{siryo.data["sap_code"]}']=str(siryo.data["menge"]).replace("\xa0", "")
        siryo_price[f'{siryo.data["sap_code"]}']=str(siryo.data["price"]).replace("\xa0", "")



    for i in range(0,len(sapcodes)):
        component_count = 0
        value = 0
        price = 0
        for j in range(0,len(sapcodes[i]['components'])):
            if sapcodes[i]['components'][j][0] in siryo_menge:
                sapcodes_copy[i]['components'][j][3] = (float(siryo_menge[sapcodes[i]['components'][j][0]]) )
                # if 'APF.001.STK-KL06' ==sapcodes[i]['components'][j][0]:
                #     print('*'*25,sapcodes[i]['components'][j][0],sapcodes_copy[i]['components'][j])
                #     print('*'*25,siryo_menge[sapcodes[i]['components'][j][0]],sapcodes_copy[i]['components'][j][4])
                sapcodes_copy[i]['components'][j][5] =(float(siryo_menge[sapcodes[i]['components'][j][0]]) * float(sapcodes_copy[i]['components'][j][4]))
                value += float(siryo_menge[sapcodes[i]['components'][j][0]])
                component_count += 1
                
                if '-LA' in sapcodes[i]['sap_code'] or '-LC' in sapcodes[i]['sap_code']:
                    # print(sapcodes[i]['sap_code'],'>>>>>>>>>>>>>')
                    sapcodes_copy[i]['components'][j][8] = sapcodes_copy[i]['components'][j][3]
                    sapcodes_copy[i]['components'][j][7] = float(sapcodes_copy[i]['components'][j][3]) * float(sapcodes_copy[i]['components'][j][4])/1000
                    price += float(sapcodes_copy[i]['components'][j][3]) * float(sapcodes_copy[i]['components'][j][4])/1000
                else:
                    # print(sapcodes[i]['sap_code'],'Gp- 7777 >>>>>> ',siryo_price[sapcodes[i]['components'][j][0]])
                    sapcodes_copy[i]['components'][j][8] = float(siryo_price[sapcodes[i]['components'][j][0]])
                    if '-7' in sapcodes[i]['sap_code']:
                        if siryo_price[sapcodes[i]['components'][j][0]] !='0' and siryo_price[sapcodes[i]['components'][j][0]] !='0.0':
                            # if  sapcodes_copy[i]['components'][j][0] =='APF.091.MSK-TP01':
                            #     print(sapcodes_copy[i]['components'][j][0],'&'*25)
                            sapcodes_copy[i]['components'][j][7] =(float(siryo_price[sapcodes[i]['components'][j][0]]) * float(sapcodes_copy[i]['components'][j][6]))
                            price += (float(siryo_price[sapcodes[i]['components'][j][0]].replace(',','.')) * float(sapcodes_copy[i]['components'][j][6].replace(',','.')))
                            # if  sapcodes_copy[i]['sap_code'] =='ACS.091.MSK-7002':
                            #     print('price>>>>>',sapcodes[i]['components'][j][0],price,float(siryo_price[sapcodes[i]['components'][j][0]]),float(sapcodes_copy[i]['components'][j][6]))
                        else:
                            # if  sapcodes_copy[i]['components'][j][0] =='APF.091.MSK-TP01':
                            #     print(sapcodes_copy[i]['components'][j][0],'@'*25)
                            sapcodes_copy[i]['components'][j][8] = sapcodes_copy[i]['components'][j][3]
                            sapcodes_copy[i]['components'][j][7] = float(siryo_menge[sapcodes_copy[i]['components'][j][0]].replace(',','.')) * float(sapcodes_copy[i]['components'][j][6].replace(',','.'))
                            price += float(siryo_menge[sapcodes_copy[i]['components'][j][0]].replace(',','.')) * float(sapcodes_copy[i]['components'][j][6].replace(',','.'))
                            # if  sapcodes_copy[i]['sap_code'] =='ACS.091.MSK-7002':
                            #     print('price>>>>>',sapcodes[i]['components'][j][0],price,float(siryo_price[sapcodes[i]['components'][j][0]]),float(sapcodes_copy[i]['components'][j][6]))
                    else:
                        # if sapcodes[i]['sap_code']=='APF.091.MSK-TP01':
                        #     print(sapcodes[i]['components'][j][0],'^^^^^^^1111111111111111111')
                        if siryo_price[sapcodes[i]['components'][j][0]] !='0' and siryo_price[sapcodes[i]['components'][j][0]] !='0.0':
                            # if  sapcodes_copy[i]['sap_code'] =='APF.091.MSK-TP01':
                            #     print(sapcodes_copy[i]['components'][j][0],'@'*25)
                            sapcodes_copy[i]['components'][j][7] =(float(siryo_price[sapcodes[i]['components'][j][0]]) * float(sapcodes_copy[i]['components'][j][4]))/1000
                            price += (float(siryo_price[sapcodes[i]['components'][j][0]]) * float(sapcodes_copy[i]['components'][j][4]))/1000
                            # if  sapcodes_copy[i]['sap_code'] =='APF.091.MSK-TP01':
                            #     print('price>>>>>',sapcodes[i]['components'][j][0],price,float(siryo_price[sapcodes[i]['components'][j][0]]),float(sapcodes_copy[i]['components'][j][4]))
                        else:
                            # if  sapcodes_copy[i]['components'][j][0] =='APF.091.MSK-TP01':
                            #     print(sapcodes_copy[i]['components'][j][0],'&'*25)
                            sapcodes_copy[i]['components'][j][8] = sapcodes_copy[i]['components'][j][3]
                            sapcodes_copy[i]['components'][j][7] = float(siryo_menge[sapcodes_copy[i]['components'][j][0]]) * float(sapcodes_copy[i]['components'][j][4])/1000
                            price += float(siryo_menge[sapcodes_copy[i]['components'][j][0]]) * float(sapcodes_copy[i]['components'][j][4])/1000
                            # if  sapcodes_copy[i]['sap_code'] =='APF.091.MSK-TP01':
                            #     print('price>>>>>',sapcodes[i]['components'][j][0],price,float(siryo_price[sapcodes[i]['components'][j][0]]),float(sapcodes_copy[i]['components'][j][4]))
        
        # if sapcodes[i]['sap_code']=='ACS.091.MSK-7002':
        #     print(sapcodes[i]['components'],'<<<<<<<<',component_count,price)

        if component_count == len(sapcodes[i]['components']):
            # if sapcodes[i]['sap_code']=='APF.091.MSK-TP01':
            #     print(sapcodes[i]['components'],'yyy<<<<<<<<',component_count,price)
            sapcodes_copy[i]['ves_corredted'] = True
            sapcodes_copy[i]['price'] = price
            if Siryo.objects.filter(data__sap_code =sapcodes[i]['sap_code']).exists():
                # if sapcodes[i]['sap_code']=='APF.091.MSK-TP01':
                #     print(sapcodes[i]['components'],'existsss<<<<<<<<',component_count,price)
                siryo = Siryo.objects.filter(data__sap_code =sapcodes[i]['sap_code'])[:1].get()
                siryo.data['price'] = price
                siryo.save()
                
            else:
                # if sapcodes[i]['sap_code']=='APF.091.MSK-TP01':
                #     print(sapcodes[i]['components'],'newwwyyy<<<<<<<<',component_count,price)
                Siryo(
                    data ={'sap_code':sapcodes[i]['sap_code'],'menge':value,'price':price}
                ).save()
        
    return sapcodes_copy
    





# @login_required(login_url='/accounts/login/')
# @allowed_users(allowed_roles=['admin','moderator'])    
# def product_add_second_org_accessuar_uz(request,id):
#     file = AccessuarFiles.objects.get(id=id).file
#     if 'SHABLON' in str(file):
#         df = pd.read_excel(f'{MEDIA_ROOT}/{file}')
#     else:
#         df = pd.read_excel(f'{MEDIA_ROOT}/{file}',header=4)
    
#     df = df.astype(str)
    
#     now = datetime.now()
#     year =now.strftime("%Y")
#     month =now.strftime("%B")
#     day =now.strftime("%a%d")
#     hour =now.strftime("%H HOUR")
#     minut =now.strftime("%M")
      
#     order_id = request.GET.get('order_id',None)
      


      
#     aluminiy_group = RadiatorSapCode.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
#     umumiy_counter={}
#     for al in aluminiy_group:
#         umumiy_counter[ al['artikul'] + '-' + al['section'] ] = al['total_max']
    
#     aluminiy_group_termo = RadiatorSapCode.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
#     umumiy_counter_termo = {}
#     for al in aluminiy_group_termo:
#         umumiy_counter_termo[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      
      
      
    
#     for key,row in df.iterrows():
#         if row['Модель'] == 'nan':
#                 df = df.drop(key)
    
        
    
    
#     df_new = pd.DataFrame()

#     df_new['counter'] =df['Артикул']
    
#     df_new['SAP CODE 7']=''
#     df_new['7 - Upakovka']=''
    
    
    
#     cache_for_cratkiy_text =[]
#     duplicat_list =[]
    
    
#     for key,row in df.iterrows():  
#         df_new['7 - Upakovka'][key] = df['Краткий текст'][key]
        
        
#         if ((row['Название'] == 'nan') or (row['Название'] == '')):
#             online_savdo_name = ''
#         else:
#             online_savdo_name = row['Название']
            
            
#         if ((row['Online savdo ID'] == 'nan') or (row['Online savdo ID'] == '')):
#             id_savdo = 'XXXXX'
#         else:
#             id_savdo = str(row['Online savdo ID']).replace('.0','')

        
#         if RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala= df_new['7 - Upakovka'][key]).exists():
#             df_new['SAP CODE 7'][key] = RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['7 - Upakovka'][key])[:1].get().material
#             duplicat_list.append([df_new['SAP CODE 7'][key],df_new['7 - Upakovka'][key],'7'])
#         else: 
#             if RadiatorSapCode.objects.filter(artikul=df['Артикул'][key],section ='7').exists():
#                     umumiy_counter[df['Артикул'][key]+'-7'] += 1
#                     max_values7 = umumiy_counter[df['Артикул'][key]+'-7']
#                     materiale = df['Артикул'][key]+"-7{:03d}".format(max_values7)
#                     RadiatorSapCode(artikul = df['Артикул'][key],section ='7',counter=max_values7,kratkiy_tekst_materiala=df_new['7 - Upakovka'][key],material=materiale).save()
#                     df_new['SAP CODE 7'][key] = materiale
                    
#                     cache_for_cratkiy_text.append({
#                                         'kratkiy':df_new['7 - Upakovka'][key],
#                                         'sap_code':  materiale,
                                        
#                                         # 'system' : row['Название системы'],
#                                         # 'number_of_chambers' : row['Количество камер'],
#                                         # 'article' : row['Артикул'],
#                                         # '7ofile_type_id' : row['Код к компоненту системы'],
                                        
#                                     })
            
#             else:
#                     materiale = df['Артикул'][key]+"-7{:03d}".format(1)
#                     RadiatorSapCode(artikul = df['Артикул'][key],section ='7',counter=1,kratkiy_tekst_materiala=df_new['7 - Upakovka'][key],material=materiale).save()
#                     df_new['SAP CODE 7'][key] = materiale
#                     umumiy_counter[df['Артикул'][key]+'-7'] = 1
            
#                     cache_for_cratkiy_text.append(
#                                     {
#                                         'kratkiy':df_new['7 - Upakovka'][key],
#                                         'sap_code':  materiale,
#                                     }
#                                 )
            
    
            
           
        
      
#     parent_dir ='{MEDIA_ROOT}\\uploads\\radiator\\'
    
#     if not os.path.isdir(parent_dir):
#         create_folder(f'{MEDIA_ROOT}\\uploads\\','radiator')
        
#     create_folder(f'{MEDIA_ROOT}\\uploads\\radiator\\',f'{year}')
#     create_folder(f'{MEDIA_ROOT}\\uploads\\radiator\\{year}\\',f'{month}')
#     create_folder(f'{MEDIA_ROOT}\\uploads\\radiator\\{year}\\{month}\\',day)
#     create_folder(f'{MEDIA_ROOT}\\uploads\\radiator\\{year}\\{month}\\{day}\\',hour)
      
      
#     df_char = create_characteristika(cache_for_cratkiy_text) 
    
#     df_char_title = create_characteristika_utils(cache_for_cratkiy_text)
                 
      
            
#     if not os.path.isfile(f'{MEDIA_ROOT}\\uploads\\radiator\\{year}\\{month}\\{day}\\{hour}\\radiator-{minut}.xlsx'):
#         path_radiator =  f'{MEDIA_ROOT}\\uploads\\radiator\\{year}\\{month}\\{day}\\{hour}\\radiator-{minut}.xlsx'
#     else:
#         st = randint(0,1000)
#         path_radiator =  f'{MEDIA_ROOT}\\uploads\\radiator\\{year}\\{month}\\{day}\\{hour}\\radiator-{minut}-{st}.xlsx'
      



#     for key,razlov in df_new.iterrows():
#         if razlov['SAP CODE 7']!="":
#                 if not RazlovkaRadiator.objects.filter(sap_code7=razlov['SAP CODE 7'],kratkiy7=razlov['7 - Upakovka']).exists():
#                     RazlovkaRadiator(
#                             pr_sap_code =razlov['SAP CODE P'],
#                             pr_kratkiy =razlov['PR - Press'],
#                             mo_sap_code =razlov['SAP CODE M'],
#                             mo_kratkiy =razlov['MO - Mex obrabotka'], 
#                             pm_sap_code =razlov['SAP CODE PM'],
#                             pm_kratkiy =razlov['PM - Puma'], 
#                             pk_sap_code =razlov['SAP CODE PK'],
#                             pk_kratkiy =razlov['PK - Pokraska'], 
#                             sap_code7 =razlov['SAP CODE 7'],
#                             kratkiy7 =razlov['7 - Upakovka']
#                         ).save()
        
    
#     price_all_correct = False
      
    


#     del df_new['counter']

#     writer = pd.ExcelWriter(path_radiator, engine='openpyxl')
#     df_new.to_excel(writer,index=False,sheet_name='Schotchik')
#     df_char.to_excel(writer,index=False,sheet_name='Characteristika')
#     df_char_title.to_excel(writer,index=False,sheet_name='title')
#     writer.close()


#     order_id = request.GET.get('order_id',None)

#     work_type = 1
#     if order_id:
#         work_type = OrderRadiator.objects.get(id = order_id).work_type
#         if price_all_correct and  work_type != 5 :
#             # path = update_char_title_function(df_char_title,order_id)
#             # files =[File(file=p,filetype='radiator') for p in path]
#             files = []
#             files.append(File(file=path_radiator,filetype='radiator'))
#             context ={
#                   'files':files,
#                   'section':'Формированый радиатор файл'
#             }

#             if order_id:
#                 file_paths =[ file.file for file in files]
#                 order = OrderRadiator.objects.get(id = order_id)
#                 paths = order.paths
#                 raz_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
#                 zip_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
#                 paths['radiator_razlovka_file']= file_paths
#                 paths['raz_created_at']= raz_created_at
#                 paths['zip_created_at']= zip_created_at
#                 paths['status_l']= 'done'
#                 paths['status_raz']= 'done'
#                 paths['status_zip']= 'done'
#                 paths['status_text_l']= 'done'
                
#                 order.paths = paths
#                 order.radiator_worker = request.user
#                 order.current_worker = request.user
#                 order.work_type = 6
#                 order.save()
#                 context['order'] = order
#                 paths =  order.paths
#                 for key,val in paths.items():
#                     context[key] = val
#                 return render(request,'order/order_detail_radiator.html',context)  
#         else:
            
#             file =[File(file = path_radiator,filetype='radiator',id=1)]
#             context = {
#                   'files':file,
#                   'section':'Формированый radiator файл'
#             }
            
#             if order_id:
#                 order = OrderRadiator.objects.get( id = order_id)
#                 paths = order.paths 
#                 if work_type != 5:
#                     context2 ={
#                             'radiator_razlovka_file':[path_radiator,path_radiator]
#                     }
#                     paths['radiator_razlovka_file'] = [path_radiator,path_radiator]
#                 else:
#                     path_radiator = order.paths['radiator_razlovka_file']
#                     context2 ={
#                             'radiator_razlovka_file':[path_radiator,path_radiator]
#                     }

                
#                 raz_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                 paths['raz_created_at']= raz_created_at
                
#                 paths['status_l']= 'done'
#                 paths['status_raz']= 'done'
#                 paths['status_zip']= 'on process'
#                 paths['status_text_l']= 'on process'
                

#                 order.paths = paths
#                 order.current_worker = request.user
#                 order.work_type = 5
#                 order.save()
#                 context2['order'] = order
#                 paths =  order.paths
#                 for key,val in paths.items():
#                     context2[key] = val

#                 workers = User.objects.filter(role =  'moderator',is_active =True)
#                 context2['workers'] = workers

#                 return render(request,'order/order_detail_radiator.html',context2)

    
#     return render(request,'universal/generated_files.html',{'a':'b'})

