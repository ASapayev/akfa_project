from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from .forms import NormaKraskaFileForm,TexcartaKraskaFileForm
from .models import Norma7,SiroKraska,TexcartaFile,KarkaCode,KraskaFileClient,KraskaSapCode,OrderKraska
from config.settings import MEDIA_ROOT
import pandas as pd
from django.http import JsonResponse
from django.db.models import Q,Max
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json
import random
import string
import os 
from datetime import datetime
from random import randint
from aluminiy.views import create_folder
from accounts.models import User
from .utils import characteristika_created_txt_create
# Create your views here.


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','customer','universal_user']) 
def get_or_add_option(request):
    # print(request.method)
    if request.method == 'GET':
        # Fetch data for the Select2 dropdown
        search_term = request.GET.get('term', '')  # Search term from the Select2 input
        
        
        if search_term:
            # Query your model for matching options
            queryset = KarkaCode.objects.filter(name__icontains=search_term).values('id','name')
        else:
            queryset = KarkaCode.objects.all().values('id','name')
           
       
        # Return the data in the format Select2 expects
        return JsonResponse({"results": list(queryset)})
    
    elif request.method == 'POST':
        # This part handles adding a new option if it doesn't exist
        new_option = request.POST.get('new_option', '')
        print(request.POST,'request option')
        print(new_option,'new option')
        
        if new_option:
            # Save the new option in your model
            obj, created = KarkaCode.objects.get_or_create(name=new_option)
            return JsonResponse({"id": obj.id, "text": obj.name})

        return JsonResponse({"error": "Invalid input"}, status=400)



@csrf_exempt
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','kraska','universal_user']) 
def edit_siryo(request,id):
      sapcode_org = SiroKraska.objects.get(id=id)
      if request.method =='POST':
            data_json = request.POST.get('data',None)
        
            datas = json.loads(data_json)

            sapcode_org.code = datas['code'].replace(',','.')
            sapcode_org.kratkiy = datas['kratkiy']
            sapcode_org.save()
            
            return JsonResponse({'status':201})
      else:
            context ={
                  'sapcode':sapcode_org,
                  'section':'Краска сапкод'
            }
            return render(request,'kraska/edit.html',context)




@login_required(login_url='/accounts/login/') 
@allowed_users(allowed_roles=['admin','moderator','kraska','universal_user']) 
def find_norma(request):
    all_data = [ [] for i in range(3)]
    does_not_exists = []

    if request.method =='POST':
        ozmk =request.POST.get('ozmk',None)
        if ozmk:
            ozmks = ozmk.split()
            for ozm in ozmks:
                if SiroKraska.objects.filter(sapcode=ozm).exists():
                    siryo = SiroKraska.objects.filter(sapcode=ozm)[:1].get()
                    all_data[0].append(siryo.code)
                    all_data[1].append(siryo.sapcode)
                    all_data[2].append(siryo.kratkiy)
                else:
                    does_not_exists.append(ozm)
            data_df =pd.DataFrame({'MATNR':all_data[1],'TEXT1':all_data[2],'CODE':all_data[0]})
            df_not = pd.DataFrame({'SAP CODE':does_not_exists})
            path = generate_norma_kraska(data_df,df_not)
            
            files =[File(file=path,filetype='obichniy',id=1)]
            context ={
                'files':files,
                'section':'Норма лист'
            }
        return render(request,'universal/generated_files.html',context)
    else:
        
        return render(request,'norma/character_find.html',{'section':'Норма','section2':'Генерация нормы'})


@csrf_exempt
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','kraska','universal_user']) 
def siryo_bulk_delete(request):
    if request.method =='POST':
        ids = request.POST.get('ids',None)
        if ids:
            ids = ids.split(',')
            
            for id in ids:
                sapcode = SiroKraska.objects.get(id=id)
                sapcode.delete()

        return JsonResponse({'msg':True})
    else:
        return JsonResponse({'msg':False})

@csrf_exempt
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','kraska','universal_user']) 
def delete_siryo(request,id):
      if request.method =='POST':
            if SiroKraska.objects.filter(id=id).exists():
                SiroKraska.objects.get(id=id).delete()
                return JsonResponse({'msg':True})
            else:
                return JsonResponse({'msg':False})

      else:
            return JsonResponse({'msg':False})


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','kraska','universal_user']) 
def create_siryo_from_file(request):
    file =f'D:\\Users\\Muzaffar.Tursunov\\Desktop\\NORMA\\NORMA\\SAPCODE_BAZA.xlsx'
    # file =f'c:\\OpenServer\\domains\\SAPCODE_BAZA.xlsx'

    df = pd.read_excel(file)
    df = df.astype(str)
    # print(df)

    for key,row in df.iterrows():   
            # # data =data[key]
        artikul =row['MATNR'].split('-')[0]
        artikul_component = SiroKraska(
            code = row['KOD'],
            artikul =artikul,
            sapcode = row['MATNR'],
            kratkiy = row['TEXT1'],
            )
        artikul_component.save()

    return JsonResponse({'a':'b'})

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','kraska','universal_user']) 
def create_siryo(request):
    if request.method =='POST':
        # data_j = dict(request.POST)
        data_json = request.POST.get('data',None)
        
        datas = json.loads(data_json)
       
           
            # # data =data[key]
        artikul = datas['sapcode'].split('-')[0]
        artikul_component = SiroKraska(
            code = datas['code'],
            artikul =artikul,
            sapcode = datas['sapcode'],
            kratkiy = datas['kratkiy'],
            )
        artikul_component.save()

        return JsonResponse({'status':201})
    return render(request,'kraska/add.html')

class File:
    def __init__(self,file,filetype,id):
        self.file =file
        self.filetype =filetype
        self.id = id
        

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','kraska','universal_user'])
def file_upload_kraska_tex(request): 
  if request.method == 'POST':
    data = request.POST.copy()
    data['type']='simple'
    form = TexcartaKraskaFileForm(data, request.FILES)
    if form.is_valid():
        file = form.save()
        context ={'files':[File(file=str(file.file),id=file.id,filetype='texcarta'),],
              'link':'/kraska/generate-kraska-texcarta/',
              'section':'Генерация техкарта файла',
              'type':'Kraska',
              'file_type':'simple'
              }
    return render(request,'universal/file_list_norma.html',context)
  else:
      form =TexcartaKraskaFileForm()
      context ={
        'section':''
      }
  return render(request,'universal/main.html',context)






@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','kraska','universal_user'])
def show_siryo(request):
     
      search_text = request.GET.get('search',None)

      if search_text:
            products = SiroKraska.objects.filter(
                  Q(sapcode__icontains = search_text)
            ).order_by('-created_at')
      else:
            products = SiroKraska.objects.all().order_by('-created_at')

      paginator = Paginator(products, 25)

      if request.GET.get('page') != None:
            page_number = request.GET.get('page')
      else:
            page_number=1

      page_obj = paginator.get_page(page_number)

    
      

      context ={
            'section':'Краска',
            'products':page_obj,
            'type':False,
            'search':search_text
      }

                  
      return render(request,'kraska/show_siryo.html',context)





@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','kraska','universal_user'])    
def product_add_second_org_kraska(request,id):
    file = KraskaFileClient.objects.get(id=id).file
    if 'SHABLON' in str(file):
        df = pd.read_excel(f'{MEDIA_ROOT}/{file}')
        # df = pd.read_excel(f'c:\\OpenServer\\domains\\SHABLON_RADIATOR_XXXXX.xlsx')
    else:
        df = pd.read_excel(f'{MEDIA_ROOT}/{file}',header=4)
    
    df = df.astype(str)
    
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M")
      
    order_id = request.GET.get('order_id',None)
      


      
    aluminiy_group = KraskaSapCode.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
    umumiy_counter={}
    for al in aluminiy_group:
        umumiy_counter[ al['artikul'] + '-' + al['section'] ] = al['total_max']
    
    aluminiy_group_termo = KraskaSapCode.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
    umumiy_counter_termo = {}
    for al in aluminiy_group_termo:
        umumiy_counter_termo[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      
      
   
    
    
    df_new = pd.DataFrame()

    df_new['counter'] =df['Артикул']
    
    df_new['SAP CODE 7']=''
    df_new['7 - Upakovka']=''

    
    
    
    cache_for_cratkiy_text =[[],[],[]]
    duplicat_list =[]
    
    
    for key,row in df.iterrows():  
        df_new['7 - Upakovka'][key] = df['Краткий текст'][key]

        
        if ((row['Название'] == 'nan') or (row['Название'] == '')):
            online_savdo_name = ''
        else:
            online_savdo_name = row['Название']
            
            
        if ((row['Online savdo ID'] == 'nan') or (row['Online savdo ID'] == '')):
            id_savdo = 'XXXXX'
        else:
            id_savdo = str(row['Online savdo ID']).replace('.0','')

        new_kraska = df['Артикул'][key].split('.')[1]

        if not KarkaCode.objects.filter(name__icontains=new_kraska).exists():
            KarkaCode(name=new_kraska).save()


        if KraskaSapCode.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala= df_new['7 - Upakovka'][key]).exists():
            df_new['SAP CODE 7'][key] = KraskaSapCode.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['7 - Upakovka'][key])[:1].get().material
            duplicat_list.append([df_new['SAP CODE 7'][key],df_new['7 - Upakovka'][key],'7'])
        else: 
            if KraskaSapCode.objects.filter(artikul=df['Артикул'][key],section ='7').exists():
                    umumiy_counter[df['Артикул'][key]+'-7'] += 1
                    max_values7 = umumiy_counter[df['Артикул'][key]+'-7']
                    materiale = df['Артикул'][key]+"-7{:03d}".format(max_values7)
                    KraskaSapCode(artikul = df['Артикул'][key],section ='7',counter=max_values7,kratkiy_tekst_materiala=df_new['7 - Upakovka'][key],material=materiale).save()
                    df_new['SAP CODE 7'][key] = materiale
                    
            
                    cache_for_cratkiy_text[0].append(materiale)
                    cache_for_cratkiy_text[1].append(df_new['7 - Upakovka'][key])
                    cache_for_cratkiy_text[2].append(row['Цена с НДС'])
            else:
                    materiale = df['Артикул'][key]+"-7{:03d}".format(1)
                    KraskaSapCode(artikul = df['Артикул'][key],section ='7',counter=1,kratkiy_tekst_materiala=df_new['7 - Upakovka'][key],material=materiale).save()
                    df_new['SAP CODE 7'][key] = materiale
                    umumiy_counter[df['Артикул'][key]+'-7'] = 1
        
                    cache_for_cratkiy_text[0].append(materiale)
                    cache_for_cratkiy_text[1].append(df_new['7 - Upakovka'][key])
                    cache_for_cratkiy_text[2].append(row['Цена с НДС'])
            

    

        
      
    parent_dir ='{MEDIA_ROOT}\\uploads\\kraska\\'
    
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads\\','kraska')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\kraska\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\kraska\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\kraska\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\kraska\\{year}\\{month}\\{day}\\',hour)
      
                       
    if not os.path.isfile(f'{MEDIA_ROOT}\\uploads\\kraska\\{year}\\{month}\\{day}\\{hour}\\kraska-{minut}.xlsx'):
        path_kraska =  f'{MEDIA_ROOT}\\uploads\\kraska\\{year}\\{month}\\{day}\\{hour}\\kraska-{minut}.xlsx'
    else:
        st = randint(0,1000)
        path_kraska =  f'{MEDIA_ROOT}\\uploads\\kraska\\{year}\\{month}\\{day}\\{hour}\\kraska-{minut}-{st}.xlsx'
      

    # price_all_correct = False
      
    

    del df_new['counter']

    writer = pd.ExcelWriter(path_kraska, engine='openpyxl')
    df_new.to_excel(writer,index=False,sheet_name='Schotchik')
    writer.close()


    order_id = request.GET.get('order_id',None)

    work_type = 1
    price_all_correct=True
    if order_id:
        work_type = OrderKraska.objects.get(id = order_id).work_type
        if price_all_correct:
            df ={
                'sapcode':cache_for_cratkiy_text[0],
                'kratkiy':cache_for_cratkiy_text[1],
                'narx':cache_for_cratkiy_text[2]
            }
            path = characteristika_created_txt_create(df)
            files = [File(file=p,filetype='obichniy',id=1) for p in path]
            files.append(File(file=path_kraska,filetype='kraska',id=1))
            context ={
                  'files':files,
                  'section':'Формированый краска файл'
            }

            if order_id:
                file_paths =[ file.file for file in files]
                order = OrderKraska.objects.get(id = order_id)
                paths = order.paths
                raz_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                zip_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                paths['kraska_razlovka_file']= file_paths
                paths['raz_created_at']= raz_created_at
                paths['zip_created_at']= zip_created_at
                paths['status_l']= 'done'
                paths['status_raz']= 'done'
                paths['status_zip']= 'done'
                paths['status_text_l']= 'done'
                
                order.paths = paths
                order.worker = request.user
                order.current_worker = request.user
                order.work_type = 6
                order.save()
                context['order'] = order
                paths =  order.paths
                for key,val in paths.items():
                    context[key] = val
                return render(request,'order/order_detail_kraska.html',context)  
        else:
            
            file =[File(file = path_kraska,filetype='kraska',id=1)]
            context = {
                  'files':file,
                  'section':'Формированый краска файл'
            }
            
            if order_id:
                order = OrderKraska.objects.get( id = order_id)
                paths = order.paths 
                context2 ={
                        'kraska_razlovka_file':[path_kraska,path_kraska]
                }
                paths['kraska_razlovka_file'] = [path_kraska,path_kraska]
                

                
                raz_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                paths['raz_created_at']= raz_created_at
                
                paths['status_l']= 'done'
                paths['status_raz']= 'done'
                paths['status_zip']= 'on process++'
                paths['status_text_l']= 'on process'
                

                order.paths = paths
                order.current_worker = request.user
                order.work_type = 6
                order.save()
                context2['order'] = order
                paths =  order.paths
                for key,val in paths.items():
                    context2[key] = val

                workers = User.objects.filter(role =  'moderator',is_active =True)
                context2['workers'] = workers

                return render(request,'order/order_detail_kraska.html',context2)

    
    return render(request,'universal/generated_files.html',{'a':'b'})




@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','kraska','universal_user'])
def full_update_norm(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['type']='termo'
        form = NormaKraskaFileForm(data, request.FILES)
        if form.is_valid():
            normaa =Norma7.objects.all()
            normaa.delete()
            form_file = form.save()
            file = form_file.file
            path =f'{MEDIA_ROOT}/{file}'
            
            df = pd.read_excel(path,sheet_name='1-etap', header=2)
            

            df = df.astype(str)
            df = df.replace('nan','0')
            df = df.replace('0.0','0')
            
            columns = df.columns

            Norma7(data ={'columns':list(columns)}).save()

            for key, row in df.iterrows():
                norma_dict = {}
                for col in columns:
                    norma_dict[col]=row[col]
                Norma7(data =norma_dict).save()

    return render(request,'norma/benkam/main.html')


def generate_random_string(length=10):
    letters = string.ascii_letters + string.digits  # Includes uppercase, lowercase letters, and digits
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

def generate_norma_kraska(df_sapcodes,df_not_exists):

    baza_siryo = SiroKraska.objects.all().values('code','sapcode','kratkiy')

    # print(baza_siryo)

    baza ={}
    for row in baza_siryo:
        keyy= str(row['code'])
        baza[keyy]={
            'MATNR':row['sapcode'],
            'TEXT1':row['kratkiy'],
        }
    
    df = pd.DataFrame()
    df['counter'] = [0 for x in range(len(df_sapcodes)*25)]
    df['ID'] = ""
    df['MATNR'] = ""
    df['WERKS'] = ""
    df['TEXT1'] = ""
    df['STLAL'] = ""
    df['STLAN'] = ""
    df['ZTEXT'] = ""
    df['STKTX'] = ""
    df['BMENG'] = ""
    df['BMEIN'] = ""
    df['STLST'] = ""
    df['POSNR'] = ""
    df['POSTP'] = ""
    df['MATNR1'] = ""
    df['TEXT2'] = ""
    df['MEINS'] = ""
    df['MENGE'] = ""
    df['DATUV'] = ""
    df['PUSTOY'] = ""
    df['LGORT'] = ""
    # print(df)
    # print(makt.columns)
    count_2=0
    
    itogo = Norma7.objects.filter(Q(data__MATN__icontains='Итого'))[:1].get().data
    # print(baza)
    for key, row in df_sapcodes.iterrows():
        zagolovok = str(row['CODE'])
        itogo_val =float(itogo[zagolovok])

        df['ID'][count_2] ='1'
        df['MATNR'][count_2] = row['MATNR']
        df['WERKS'][count_2] = '4702'
        df['TEXT1'][count_2] = row['TEXT1']
        df['STLAL'][count_2] = '1'
        df['STLAN'][count_2] = '1'
        df['ZTEXT'][count_2] = row['TEXT1']
        df['STKTX'][count_2] = 'Упаковка'
        df['BMENG'][count_2] = round(itogo_val,3)
        df['BMEIN'][count_2] = 'КГ'
        df['STLST'][count_2] = '1'
        df['POSNR'][count_2] = ''
        df['POSTP'][count_2] = ''
        df['MATNR1'][count_2] = ''
        df['TEXT2'][count_2] = ''
        df['MEINS'][count_2] = ''
        df['MENGE'][count_2] = ''
        df['DATUV'][count_2] = '01012023'
        df['PUSTOY'][count_2] = ''
        df['LGORT'][count_2] = ''
        
        
        
        result = Norma7.objects.filter(
                        Q(data__has_key=zagolovok) & ~Q(data__contains={zagolovok: "0"})
                    ).order_by('created_at').values('data')

        # print(itogo,'itogoogg')
        

        # print(zagolovok,'>>>>>>>',result)
        count_2 +=1
        count = 1

        

        for res in result:
            first_val = res['data']
            matn = first_val['MATN']
           
            if matn in baza and matn != '0' and matn != 0: 
                # print(matn,'<<<<<< operation one ','<<|'*40)
                baza_dat = baza[matn]
                df['ID'][count_2] = '2'
                df['POSNR'][count_2] = count
                df['POSTP'][count_2] = 'L'
                df['MATNR1'][count_2] = baza_dat['MATNR']
                df['TEXT2'][count_2] = baza_dat['TEXT1']
                # df['MEINS'][count_2] = round((float(first_val[zagolovok])/itogo_val)*1000,3)
                df['MEINS'][count_2] = round((float(first_val[zagolovok])),3)
                df['MENGE'][count_2] = 'КГ'
                df['LGORT'][count_2] = 'PS01'
                count_2 +=1
                count +=1






        # count_2 +=1
        

        # print(zagolovok,itogo_val,'gggg'*8)
        
        for norm in result:
            data = norm['data']
            matn = data['MATN']
            if (('Итого' in data['MATN']) or (str(matn) in baza)):
                continue
            df['ID'][count_2] = '2'
            df['POSNR'][count_2] = count
            df['POSTP'][count_2] = 'L'
            df['MATNR1'][count_2] = str(data['SAPCODE']).replace('.0','')
            df['TEXT2'][count_2] = data['MATN']
            # df['MEINS'][count_2] = round((float(data[zagolovok])/itogo_val)*1000,3)
            df['MEINS'][count_2] = round((float(data[zagolovok])),3)
            df['MENGE'][count_2] = 'КГ'
            df['LGORT'][count_2] = 'PS01'
            count_2 +=1
            count +=1



    del df['counter']
    # print(df)
    string_rand = generate_random_string()
    path=f'{MEDIA_ROOT}\\uploads\\kraska\\norma_{string_rand}.xlsx'
    writer = pd.ExcelWriter(path, engine='openpyxl')
   
    df.to_excel(writer,index=False,sheet_name ='NORMA KRASKA')
    df_not_exists.to_excel(writer,index=False,sheet_name ='SIRYO DOES NOT EXISTS')
    writer.close()
    
    return path

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','kraska','universal_user'])
def lenght_generate_texcarta(request,id):
    file = TexcartaFile.objects.get(id=id).file
    data = pd.read_excel(f'{MEDIA_ROOT}/{file}')
    counter = len(data)

    df_new = pd.DataFrame()
    df_new['counter'] =[ '' for i in range(0,counter*2)]
    df_new['ID']=''
    df_new['MATNR']=''
    df_new['WERKS']=''
    df_new['PLNNR']=''
    df_new['STTAG']=''
    df_new['PLNAL']=''
    df_new['KTEXT']=''
    df_new['VERWE']=''
    df_new['STATU']=''
    df_new['LOSVN']=''
    df_new['LOSBS']=''
    df_new['VORNR']=''
    df_new['ARBPL']=''
    df_new['WERKS1']=''
    df_new['STEUS']=''
    df_new['LTXA1']=''
    df_new['BMSCH']=''
    df_new['MEINH']=''
    df_new['VGW01']=''
    df_new['VGE01']=''
    df_new['ACTTYPE_01']=''
    df_new['CKSELKZ']=''
    df_new['UMREZ']=""
    df_new['UMREN']=''
    df_new['USR00']=''
    df_new['USR01']=''


    counter_2 = 0
    for key,row in data.iterrows():
        for i in range(1,3):
            if i ==1:
                df_new['ID'][counter_2] ='1'
                df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                df_new['WERKS'][counter_2] ='4702'
                df_new['STTAG'][counter_2] ='01012024'
                df_new['PLNAL'][counter_2] ='1'
                df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                df_new['VERWE'][counter_2] ='1'
                df_new['STATU'][counter_2] ='4'
                df_new['LOSVN'][counter_2] ='0.001'
                df_new['LOSBS'][counter_2] ='99999999'
            elif i == 2:
                df_new['ID'][counter_2]='2'
                df_new['VORNR'][counter_2] ='0010'
                df_new['ARBPL'][counter_2] ='4702KR01'
                df_new['WERKS1'][counter_2] ='4702'
                df_new['STEUS'][counter_2] ='ZK01'
                df_new['LTXA1'][counter_2] ='Производство Краски'
                df_new['BMSCH'][counter_2] = '1000'
                df_new['MEINH'][counter_2] ='KG'
                df_new['VGW01'][counter_2] ='24'
                df_new['VGE01'][counter_2] =''
                df_new['ACTTYPE_01'][counter_2] ='200160'
                df_new['CKSELKZ'][counter_2] ='X'
                df_new['UMREZ'][counter_2] = '1'
                df_new['UMREN'][counter_2] = '1'
                df_new['USR00'][counter_2] = '1'
                df_new['USR01'][counter_2] = '60'
                
            counter_2 +=1
    
    del df_new['counter']

    string_rand = generate_random_string()
    path2 =f'{MEDIA_ROOT}\\uploads\\kraska\\texcarta_kraska_{string_rand}.xlsx'
    df_new.to_excel(path2,index=False)

    context ={
            'file1':path2,
            'section':'Техкарта',

        }

   
    return render(request,'norma/radiator/generated_files_texcarta.html',context)



