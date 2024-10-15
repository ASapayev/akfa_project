from django.shortcuts import render
from accessuar.models import AccessuarFiles,OrderACS
from config.settings import MEDIA_ROOT
import pandas as pd
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from datetime import datetime
import os
from accessuar_import.models import AccessuarImportSapCode,Characteristika
from random import randint
from accessuar.utils import create_folder
from django.db.models import Max
from accounts.models import User


# Create your views here.
class File:
    def __init__(self,file,filetype,id):
        self.file =file
        self.filetype =filetype
        self.id = id

def create_characteristika(items):
    
    all_data = [
        [],[]
    ]
    
    
    
    for item in items:
        
        all_data[0].append(item['sap_code'])
        all_data[1].append(item['kratkiy'])
        
        data ={
            'SAP CODE':item['sap_code'],
            'KRATKIY TEXT':item['kratkiy'],
        }
        character = Characteristika( data = data )
        character.save()
        



    df_new ={
        'SAP CODE':all_data[0],
        'KRATKIY TEXT':all_data[1],
        
    }
    
    df_charakter = pd.DataFrame(df_new)
    df_charakter =  df_charakter.replace('nan','')
    return df_charakter   


def create_characteristika_utils(items):
    df =[
        [],[]
    ]
    
    
    for item in items:

        df[0].append(item['sap_code'])
        df[1].append(item['kratkiy'])
        

        

    dat = {
        'SAP CODE':df[0],
        'KRATKIY TEXT':df[1],
        
        
    }
    
    df_new = pd.DataFrame(dat)
    

    return df_new



@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])    
def product_add_second_org_accessuar_uz(request,id):
    file = AccessuarFiles.objects.get(id=id).file
    if 'SHABLON' in str(file):
        df = pd.read_excel(f'{MEDIA_ROOT}/{file}')
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
      


      
    aluminiy_group = AccessuarImportSapCode.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
    umumiy_counter={}
    for al in aluminiy_group:
        umumiy_counter[ al['artikul'] + '-' + al['section'] ] = al['total_max']
    
    aluminiy_group_termo = AccessuarImportSapCode.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
    umumiy_counter_termo = {}
    for al in aluminiy_group_termo:
        umumiy_counter_termo[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      
      
      
    
    for key,row in df.iterrows():
        if row['Модель'] == 'nan':
                df = df.drop(key)
    
        
    
    
    df_new = pd.DataFrame()

    df_new['counter'] =df['Артикул']
    
    df_new['SAP CODE 7']=''
    df_new['7 - Upakovka']=''
    
    
    
    cache_for_cratkiy_text =[]
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

        
        if AccessuarImportSapCode.objects.filter(artikul =df['Артикул'][key],section ='75',kratkiy_tekst_materiala= df_new['7 - Upakovka'][key]).exists():
            df_new['SAP CODE 7'][key] = AccessuarImportSapCode.objects.filter(artikul =df['Артикул'][key],section ='75',kratkiy_tekst_materiala=df_new['7 - Upakovka'][key])[:1].get().material
            duplicat_list.append([df_new['SAP CODE 7'][key],df_new['7 - Upakovka'][key],'75'])
        else: 
            if AccessuarImportSapCode.objects.filter(artikul=df['Артикул'][key],section ='75').exists():
                    umumiy_counter[df['Артикул'][key]+'-75'] += 1
                    max_values7 = umumiy_counter[df['Артикул'][key]+'-75']
                    materiale = df['Артикул'][key]+"-75{:02d}".format(max_values7)
                    AccessuarImportSapCode(artikul = df['Артикул'][key],section ='75',counter=max_values7,kratkiy_tekst_materiala=df_new['7 - Upakovka'][key],material=materiale).save()
                    df_new['SAP CODE 7'][key] = materiale
                    
                    cache_for_cratkiy_text.append({
                                        'kratkiy':df_new['7 - Upakovka'][key],
                                        'sap_code':  materiale,
                                        
                                        # 'system' : row['Название системы'],
                                        # 'number_of_chambers' : row['Количество камер'],
                                        # 'article' : row['Артикул'],
                                        # '7ofile_type_id' : row['Код к компоненту системы'],
                                        
                                    })
            
            else:
                    materiale = df['Артикул'][key]+"-75{:02d}".format(1)
                    AccessuarImportSapCode(artikul = df['Артикул'][key],section ='75',counter=1,kratkiy_tekst_materiala=df_new['7 - Upakovka'][key],material=materiale).save()
                    df_new['SAP CODE 7'][key] = materiale
                    umumiy_counter[df['Артикул'][key]+'-75'] = 1
            
                    cache_for_cratkiy_text.append(
                                    {
                                        'kratkiy':df_new['7 - Upakovka'][key],
                                        'sap_code':  materiale,
                                    }
                                )
            
    
            
           
        
      
    parent_dir ='{MEDIA_ROOT}\\uploads\\accessuar_import\\'
    
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads\\','accessuar_import')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\accessuar_import\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\accessuar_import\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\accessuar_import\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\accessuar_import\\{year}\\{month}\\{day}\\',hour)
      
      
    df_char = create_characteristika(cache_for_cratkiy_text) 
    
    df_char_title = create_characteristika_utils(cache_for_cratkiy_text)
                 
      
            
    if not os.path.isfile(f'{MEDIA_ROOT}\\uploads\\accessuar_import\\{year}\\{month}\\{day}\\{hour}\\accessuar_import-{minut}.xlsx'):
        path_accessuar_import =  f'{MEDIA_ROOT}\\uploads\\accessuar_import\\{year}\\{month}\\{day}\\{hour}\\accessuar_import-{minut}.xlsx'
    else:
        st = randint(0,1000)
        path_accessuar_import =  f'{MEDIA_ROOT}\\uploads\\accessuar_import\\{year}\\{month}\\{day}\\{hour}\\accessuar_import-{minut}-{st}.xlsx'
      
    price_all_correct = True

    del df_new['counter']

    writer = pd.ExcelWriter(path_accessuar_import, engine='openpyxl')
    df_new.to_excel(writer,index=False,sheet_name='Schotchik')
    df_char.to_excel(writer,index=False,sheet_name='Characteristika')
    df_char_title.to_excel(writer,index=False,sheet_name='title')
    writer.close()


    order_id = request.GET.get('order_id',None)

    work_type = 1
    if order_id:
        work_type = OrderACS.objects.get(id = order_id).work_type
        if price_all_correct and  work_type != 5 :
            # path = update_char_title_function(df_char_title,order_id)
            # files =[File(file=p,filetype='radiator') for p in path]
            files = []
            files.append(File(file=path_accessuar_import,filetype='accessuar_import'))
            context ={
                  'files':files,
                  'section':'Формированый аccessuar файл'
            }

            if order_id:
                file_paths =[ file.file for file in files]
                order = OrderACS.objects.get(id = order_id)
                paths = order.paths
                raz_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                zip_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                paths['accessuar_import_razlovka_file']= file_paths
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
                return render(request,'order/order_detail_accessuar_import.html',context)  
        else:
            
            file =[File(file = path_accessuar_import,filetype='accessuar_import',id=1)]
            context = {
                  'files':file,
                  'section':'Формированый accessuar файл'
            }
            
            if order_id:
                order = OrderACS.objects.get( id = order_id)
                paths = order.paths 
                if work_type != 5:
                    context2 ={
                            'accessuar_import_razlovka_file':[path_accessuar_import,path_accessuar_import]
                    }
                    paths['accessuar_import_razlovka_file'] = [path_accessuar_import,path_accessuar_import]
                else:
                    path_accessuar_import = order.paths['accessuar_import_razlovka_file']
                    context2 ={
                            'accessuar_import_razlovka_file':[path_accessuar_import,path_accessuar_import]
                    }

                
                raz_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                paths['raz_created_at']= raz_created_at
                
                paths['status_l']= 'done'
                paths['status_raz']= 'done'
                paths['status_zip']= 'on process'
                paths['status_text_l']= 'on process'
                

                order.paths = paths
                order.current_worker = request.user
                order.work_type = 5
                order.save()
                context2['order'] = order
                paths =  order.paths
                for key,val in paths.items():
                    context2[key] = val

                workers = User.objects.filter(role =  'moderator',is_active =True)
                context2['workers'] = workers

                return render(request,'order/order_detail_accessuar_import.html',context2)

    
    return render(request,'universal/generated_files.html',{'a':'b'})

