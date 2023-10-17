from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test,login_required
from datetime import datetime
from config.settings import MEDIA_ROOT
from .forms import FileFormPVC,FileFormCharPVC
from .models import PVCProduct,PVCFile,ArtikulKomponentPVC,CameraPvc,AbreviaturaLamination,LengthOfProfilePVC,Characteristika,Price,CharacteristikaFilePVC,RazlovkaPVX
from order.models import OrderPVX
from accounts.models import User
import pandas as pd
from django.db.models import Count,Max
import os
import random 
from aluminiy.models import ExchangeValues
from .utils import create_folder,create_characteristika,create_characteristika_utils,characteristika_created_txt_create

def update_char_title_pvc(request,id):
    file = CharacteristikaFilePVC.objects.get(id=id).file
    df = pd.read_excel(f'{MEDIA_ROOT}/{file}','title')
    df =df.astype(str)

    order_id = request.GET.get('order_id',None)
    if order_id:
        order = OrderPVX.objects.get(id = order_id)

    pathzip = characteristika_created_txt_create(df,order_id)
    fileszip = [File(file=path,filetype='BENKAM') for path in pathzip]
    if order_id:
        paths = order.paths
        zip_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        paths['status_zip'] ='done'
        paths['zip_created_at'] = zip_created_at
        paths['pvc_razlovka_file'][0] = pathzip[0]
        

        order.paths=paths
        order.work_type = 6
        order.save()
        context ={
                'order':order
        }

        for key,val in paths.items():
                context[key] = val
        return render(request,'order/order_detail_pvc.html',context)

    context = {
        'files':fileszip,
        'section':'Формированные файлы'
        }

    return render(request,'universal/generated_files.html',context)
      


def upload_product_char_pvc(request):
      if request.method == 'POST':
            form = FileFormCharPVC(request.POST, request.FILES)
            if form.is_valid():
                text = form.save()
                order_id = request.POST.get('order_id',None)
                if order_id:
                    order = OrderPVX.objects.get(id = order_id)
                    order.work_type = 4
                    worker = request.POST.get('worker',None)
                    if worker:
                            order.current_worker.id = worker
                    else:
                            order.current_worker = request.user
                    paths = order.paths
                    paths['characteristika_file'] =str(text.file)
                    paths['status_text_l']='done'
                    order.paths = paths
                    order.save()
                    

                    context ={
                            'order':order,
                            'section':'Формированный обычный файлы',
                            'type_work':'Характеристика',
                            'link':'/pvc/update-char-title-org/' + str(text.id) +'?order_id=' + str(order.id)
                    }
                    for key,val in paths.items():
                            context[key] = val
                    return render(request,'order/order_detail_pvc.html',context)

                return redirect('aluminiy_files_char_org')
            else:
                  form =FileFormCharPVC()
                  context ={
                  'form':form
                  }
      form =FileFormCharPVC()
      context ={
      'form':form,
      'section':'Формирование характеристики',
      'link':'/termo/downloading-characteristika/'
      }
      return render(request,'universal/main.html',context)




@login_required(login_url='/accounts/login/')
def upload_product_org(request):
      if request.method == 'POST':
            form = FileFormPVC(request.POST, request.FILES)
            if form.is_valid():
                  title = str(form.cleaned_data['file']).split('.')[0]
                  worker_id = request.POST.get('worker',None)
                  new_order = form.save()
                  if worker_id:
                        o_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                        
                        paths ={
                                    'termo_file':f'{MEDIA_ROOT}\\{new_order.file}',
                                    'oid':new_order.id,
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
                         
                        order = OrderPVX(title = title,owner=request.user,current_worker_id= worker_id,pvc_worker_id =worker_id,paths=paths,order_type =2)
                        order.save()
                  return redirect('order_detail_pvc',id=order.id)
            else:
                  form =FileFormPVC()
                  workers = User.objects.filter(role = 1)
                  context ={
                  'form':form,
                  'section':'Формирование сапкода pvc',
                  'workers':workers
                  }
                  return render(request,'pvc/main.html',context)
      form =FileFormPVC()
      workers = User.objects.filter(role = 1)
      context ={
      'form':form,
      'section':'Формирование сапкода pvc',
      'workers':workers
      }
      return render(request,'pvc/main.html',context)


class File:
      def __init__(self,file,filetype):
            self.file =file
            self.filetype =filetype

@login_required(login_url='/accounts/login/')    
def product_add_second_org(request,id):
    file = PVCFile.objects.get(id=id).file

    df = pd.read_excel(f'{MEDIA_ROOT}/{file}',header=4)
    df =df.astype(str)
    
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M")
      
    order_id = request.GET.get('order_id',None)
      

    #   doesnotexist,correct = check_for_correct(df,filename='aluminiy')
    #   if not correct:
    #         context ={
    #               'CharUtilsOne':doesnotexist[0],
    #               'CharUtilsTwo':doesnotexist[1],
    #               'BazaProfile':doesnotexist[2],
    #               'ArtikulComponent':doesnotexist[3]
    #         }
    #         df_char_utils_one = pd.DataFrame({
    #               'матрица':doesnotexist[0],
    #               'артикул':doesnotexist[0],
    #               'высота':['' for i in doesnotexist[0]],
    #               'ширина':['' for i in doesnotexist[0]],
    #               'высота_ширина':['' for i in doesnotexist[0]],
    #               'systems':['' for i in doesnotexist[0]]
    #               })
    #         df_char_utils_two =pd.DataFrame({
    #               'артикул':doesnotexist[1],
    #               'полый_или_фасонный':['' for i in doesnotexist[1]]
    #         })
    #         df_baza_profiley =pd.DataFrame({
    #               'артикул':[i[0] for i in doesnotexist[2]],
    #               'серия':[i[1] for i in doesnotexist[2]],
    #               'старый_код':[i[2] for i in doesnotexist[2]],
    #               'компонент':[i[3] for i in doesnotexist[2]],
    #               'product_description':[i[4] for i in doesnotexist[2]],
    #               'link':[i[5] for i in doesnotexist[2]],
    #         })
          
    #         df_artikul_component =pd.DataFrame({
    #               'artikul':doesnotexist[3],
    #               'component':doesnotexist[3],
    #               'seria':['' for i in doesnotexist[3]],
    #               'product_description_ru1':['' for i in doesnotexist[3]],
    #               'product_description_ru':['' for i in doesnotexist[3]],
    #               'stariy_code_benkam':['' for i in doesnotexist[3]],
    #               'stariy_code_jomiy':['' for i in doesnotexist[3]],
    #               'proverka_artikul2':['' for i in doesnotexist[3]],
    #               'proverka_component2':['' for i in doesnotexist[3]],
    #               'gruppa_materialov':['' for i in doesnotexist[3]],
    #               'gruppa_materialov2':['' for i in doesnotexist[3]]
    #         })
    #         create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\','Not Exists')
            
    #         path_not_exists =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\Not Exists\\Not_Exists.xlsx'
            
    #         if os.path.isfile(path_not_exists):
    #               try:
    #                     os.remove(path_not_exists)
    #               except:
    #                     return render(request,'utils/file_exist_org.html')
            
    #         writer = pd.ExcelWriter(path_not_exists, engine='xlsxwriter')
    #         df_char_utils_one.to_excel(writer,index=False,sheet_name ='character utils one')
    #         df_char_utils_two.to_excel(writer,index=False,sheet_name ='character utils two')
    #         df_baza_profiley.to_excel(writer,index=False,sheet_name ='baza profile')
    #         df_artikul_component.to_excel(writer,index=False,sheet_name ='artikul component')
    #         writer.close()

    #         if order_id:
    #               order = Order.objects.get(id = order_id)
    #               paths = order.paths
    #               l_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    #               paths['obichniy_lack_file']= path_not_exists
    #               paths['l_created_at']= l_created_at
    #               paths['status_l']= 'on process'
                  

    #               order.paths = paths
    #               order.alumin_wrongs = request.user
    #               order.current_worker = request.user
    #               order.work_type = 3
    #               order.save()
    #               context['order'] = order
    #               paths =  order.paths
    #               for key,val in paths.items():
    #                     context[key] = val
                  
    #               return render(request,'order/order_detail.html',context)
    #         # writer.save()
    #         return render(request,'utils/components.html',context)
      
    aluminiy_group = PVCProduct.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
    umumiy_counter={}
    for al in aluminiy_group:
        umumiy_counter[ al['artikul'] + '-' + al['section'] ] = al['total_max']
    
    aluminiy_group_termo = PVCProduct.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
    umumiy_counter_termo = {}
    for al in aluminiy_group_termo:
        umumiy_counter_termo[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      
      
      
    
    for key,row in df.iterrows():
        if row['Тип покрытия'] == 'nan':
                df = df.drop(key)
    
        
    
    
    df_new = pd.DataFrame()

    df_new['counter'] =df['Артикул']
    df_new['SAP код E']=''
    df_new['Экструзия холодная резка']=''

    df_new['SAP код L']=''
    df_new['Ламинация']=''
    
    df_new['SAP код 7']=''
    df_new['U-Упаковка + Готовая Продукция']=''
    

    
    
    
    cache_for_cratkiy_text =[]
    duplicat_list =[]
    
    exturision_list = []
    
    for key,row in df.iterrows():  
        
        dlina = df['Длина (мм)'][key]
        df_new['U-Упаковка + Готовая Продукция'][key] = df['Краткий текст'][key]
        
        
        if df['Тип покрытия'][key] == 'Ламинированный':
            if PVCProduct.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=row['Краткий текст']).exists():
                df_new['SAP код 7'][key] = PVCProduct.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=row['Краткий текст'])[:1].get().material
                duplicat_list.append([df_new['SAP код 7'][key],row['Краткий текст'],'7'])
            else: 
                if PVCProduct.objects.filter(artikul=df['Артикул'][key],section ='7').exists():
                        umumiy_counter[df['Артикул'][key]+'-7'] += 1
                        max_values7 = umumiy_counter[df['Артикул'][key]+'-7']
                        materiale = df['Артикул'][key]+"-7{:03d}".format(max_values7)
                        PVCProduct(artikul = df['Артикул'][key],section ='7',counter=max_values7,gruppa_materialov='PVCGP',kratkiy_tekst_materiala=row['Краткий текст'],material=materiale).save()
                        df_new['SAP код 7'][key] = materiale
                        
                        artikulcomponent = ArtikulKomponentPVC.objects.filter(artikul = df['Артикул'][key])[:1].get()
                        
                        q_bic = ''
                        
                        if row['Цвет лам пленки снаружи'] =='XXXX':
                            q_bic = row['Цвет лам пленки внутри']
                        else:
                            q_bic = row['Цвет лам пленки снаружи']
                        
                        surface_treatment_export = AbreviaturaLamination.objects.filter(abreviatura =row['Код лам пленки снаружи'])[:1].get().pokritiya
                        amount_in_a_package = CameraPvc.objects.filter(sap_code=df['Артикул'][key])[:1].get().coun_of_lam

                        cache_for_cratkiy_text.append({
                                            'kratkiy':row['Краткий текст'],
                                            'sap_code':  materiale,
                                            'system' : row['Название системы'],
                                            'number_of_chambers' : row['Количество камер'],
                                            'article' : row['Артикул'],
                                            'profile_type_id' : row['Код к компоненту системы'],
                                            'length' : row['Длина (мм)'],
                                            'surface_treatment' : row['Тип покрытия'],
                                            'outer_side_pc_id' : row['Код цвета основы/Замес'],
                                            'outer_side_wg_id' : row['Цвет лам пленки снаружи'],
                                            'inner_side_wg_id' : row['Цвет лам пленки внутри'],
                                            'sealer_color' : row['Цвет резины'],
                                            'print_view' : row['Надпись наклейки'],

                                            'width' : artikulcomponent.width,
                                            'height' : artikulcomponent.height,
                                            'category' : artikulcomponent.category,
                                            'material_class' : 'Готовая продукция',
                                            'rawmat_type' : 'ГП',
                                            'tnved' : artikulcomponent.tnved,
                                            'surface_treatment_export' : surface_treatment_export,
                                            'amount_in_a_package' :amount_in_a_package,
                                            'wms_width' : artikulcomponent.wms_width,
                                            'wms_height' : artikulcomponent.wms_height,
                                            'product_type' : artikulcomponent.product_type,
                                            'profile_type' : artikulcomponent.profile_type,
                                            'export_description':'',

                                            'coating_qbic' : q_bic,

                                            # 'id_savdo' : 1,#row[''],
                                            # 'klaes' : 1,#row[''],
                                            
                                            # 'ch_profile_type' : 1,#row[''],
                                            # 'kls_wast_length' : 1,#row[''],
                                            # 'kls_wast' : 1,#row[''],
                                            # 'ch_klaes_optm' : 1,#row[''],
                                            # 'goods_group' : 1,#row['']
                                        })
                
                else:
                        materiale = df['Артикул'][key]+"-7{:03d}".format(1)
                        PVCProduct(artikul = df['Артикул'][key],section ='7',counter=1,gruppa_materialov='PVCGP',kratkiy_tekst_materiala=row['Краткий текст'],material=materiale).save()
                        df_new['SAP код 7'][key] = materiale
                        umumiy_counter[df['Артикул'][key]+'-7'] = 1
                        
                        component2 = materiale.split('-')[0]
                        
                        artikulcomponent = ArtikulKomponentPVC.objects.filter(artikul = df['Артикул'][key])[:1].get()
                        
                        q_bic = ''
                        if row['Тип покрытия'] =='Неламинированный':
                            q_bic = row['Код цвета основы/Замес']
                        else:
                            if row['Цвет лам пленки снаружи'] =='XXXX':
                                q_bic = row['Цвет лам пленки внутри']
                            else:
                                q_bic = row['Цвет лам пленки снаружи']
                        
                        surface_treatment_export = AbreviaturaLamination.objects.filter(abreviatura =row['Код лам пленки снаружи'])[:1].get().pokritiya
                        amount_in_a_package = CameraPvc.objects.filter(sap_code =df['Артикул'][key])[:1].get().coun_of_lam
                              
                        cache_for_cratkiy_text.append(
                                        {
                                            'sap_code':  materiale,
                                            'kratkiy':row['Краткий текст'],
                                            'system' : row['Название системы'],
                                            'number_of_chambers' : row['Количество камер'],
                                            'article' : row['Артикул'],
                                            'profile_type_id' : row['Код к компоненту системы'],
                                            'length' : row['Длина (мм)'],
                                            'surface_treatment' : row['Тип покрытия'],
                                            'outer_side_pc_id' : row['Код цвета основы/Замес'],
                                            'outer_side_wg_id' : row['Цвет лам пленки снаружи'],
                                            'inner_side_wg_id' : row['Цвет лам пленки внутри'],
                                            'sealer_color' : row['Цвет резины'],
                                            'print_view' : row['Надпись наклейки'],

                                            'width' : artikulcomponent.width,
                                            'height' : artikulcomponent.height,
                                            'category' : artikulcomponent.category,
                                            'material_class' : 'Готовая продукция',
                                            'rawmat_type' : 'ГП',
                                            'tnved' : artikulcomponent.tnved,
                                            'surface_treatment_export' :surface_treatment_export,
                                            'amount_in_a_package' : amount_in_a_package,
                                            'wms_width' : artikulcomponent.wms_width,
                                            'wms_height' : artikulcomponent.wms_height,
                                            'product_type' : artikulcomponent.product_type,
                                            'profile_type' : artikulcomponent.profile_type,
                                            'export_description':'',

                                            'coating_qbic' : q_bic,

                                            # 'id_savdo' : 1,#row[''],
                                            # 'klaes' : 1,#row[''],
                                            
                                            # 'ch_profile_type' : 1,#row[''],
                                            # 'kls_wast_length' : 1,#row[''],
                                            # 'kls_wast' : 1,#row[''],
                                            # 'ch_klaes_optm' : 1,#row[''],
                                            # 'goods_group' : 1,#row['']
                                        }
                                    )
                
            ##### kombirinovanniy
        elif df['Тип покрытия'][key] == 'Неламинированный':
            if PVCProduct.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=row['Краткий текст']).exists():
                df_new['SAP код 7'][key] = PVCProduct.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=row['Краткий текст'])[:1].get().material
            else: 
                if PVCProduct.objects.filter(artikul=df['Артикул'][key],section ='7').exists():
                        umumiy_counter[df['Артикул'][key]+'-7'] += 1
                        max_values7 = umumiy_counter[df['Артикул'][key]+'-7']
                        materiale = df['Артикул'][key]+"-7{:03d}".format(max_values7)
                        PVCProduct(artikul = df['Артикул'][key],section ='7',counter=max_values7,gruppa_materialov='PVCGP',kratkiy_tekst_materiala=row['Краткий текст'],material=materiale).save()
                        df_new['SAP код 7'][key] = materiale
                        
                        q_bic = ''
                        q_bic = row['Код цвета основы/Замес']
                        artikulcomponent = ArtikulKomponentPVC.objects.filter(artikul = df['Артикул'][key])[:1].get()

                        surface_treatment_export =row['Код цвета основы/Замес']
                        amount_in_a_package = CameraPvc.objects.filter(sap_code =df['Артикул'][key])[:1].get().coun_of_pvc  

                        cache_for_cratkiy_text.append({
                                            'kratkiy':row['Краткий текст'],
                                            'sap_code':  materiale,
                                            'system' : row['Название системы'],
                                            'number_of_chambers' : row['Количество камер'],
                                            'article' : row['Артикул'],
                                            'profile_type_id' : row['Код к компоненту системы'],
                                            'length' : row['Длина (мм)'],
                                            'surface_treatment' : row['Тип покрытия'],
                                            'outer_side_pc_id' : row['Код цвета основы/Замес'],
                                            'outer_side_wg_id' : row['Цвет лам пленки снаружи'],
                                            'inner_side_wg_id' : row['Цвет лам пленки внутри'],
                                            'sealer_color' : row['Цвет резины'],
                                            'print_view' : row['Надпись наклейки'],

                                            'width' : artikulcomponent.width,
                                            'height' : artikulcomponent.height,
                                            'category' : artikulcomponent.category,
                                            'material_class' :'Готовая продукция',
                                            'rawmat_type' : 'ГП',
                                            'tnved' : artikulcomponent.tnved,
                                            'surface_treatment_export' : surface_treatment_export,
                                            'amount_in_a_package' : amount_in_a_package,
                                            'wms_width' : artikulcomponent.wms_width,
                                            'wms_height' : artikulcomponent.wms_height,
                                            'product_type' : artikulcomponent.product_type,
                                            'profile_type' : artikulcomponent.profile_type,
                                            'export_description':'',

                                            'coating_qbic' : q_bic,

                                            # 'id_savdo' : 1,#row[''],
                                            # 'klaes' : 1,#row[''],
                                            
                                            # 'ch_profile_type' : 1,#row[''],
                                            # 'kls_wast_length' : 1,#row[''],
                                            # 'kls_wast' : 1,#row[''],
                                            # 'ch_klaes_optm' : 1,#row[''],
                                            # 'goods_group' : 1,#row['']
                                        })
                        
                else:
                    materiale = df['Артикул'][key]+"-7{:03d}".format(1)
                    PVCProduct(artikul = df['Артикул'][key],section ='7',counter=1,gruppa_materialov='PVCGP',kratkiy_tekst_materiala=row['Краткий текст'],material=materiale).save()
                    df_new['SAP код 7'][key] = materiale
                    umumiy_counter[df['Артикул'][key]+'-7'] = 1
                    
                    component2 = materiale.split('-')[0]
                    
                    artikulcomponent = ArtikulKomponentPVC.objects.filter(artikul = df['Артикул'][key])[:1].get()
                    
                    
                    q_bic = row['Код цвета основы/Замес']
                    
                    
                    surface_treatment_export = row['Код цвета основы/Замес']
                    amount_in_a_package = CameraPvc.objects.filter(sap_code =df['Артикул'][key])[:1].get().coun_of_pvc
                            
                    cache_for_cratkiy_text.append(
                                    {
                                        'sap_code':  materiale,
                                        'kratkiy':row['Краткий текст'],
                                        'system' : row['Название системы'],
                                        'number_of_chambers' : row['Количество камер'],
                                        'article' : row['Артикул'],
                                        'profile_type_id' : row['Код к компоненту системы'],
                                        'length' : row['Длина (мм)'],
                                        'surface_treatment' : row['Тип покрытия'],
                                        'outer_side_pc_id' : row['Код цвета основы/Замес'],
                                        'outer_side_wg_id' : row['Цвет лам пленки снаружи'],
                                        'inner_side_wg_id' : row['Цвет лам пленки внутри'],
                                        'sealer_color' : row['Цвет резины'],
                                        'print_view' : row['Надпись наклейки'],

                                        'width' : artikulcomponent.width,
                                        'height' : artikulcomponent.height,
                                        'category' : artikulcomponent.category,
                                        'material_class' : 'Готовая продукция',
                                        'rawmat_type' : 'ГП',
                                        'tnved' : artikulcomponent.tnved,
                                        'surface_treatment_export' :surface_treatment_export,
                                        'amount_in_a_package' : amount_in_a_package,
                                        'wms_width' : artikulcomponent.wms_width,
                                        'wms_height' : artikulcomponent.wms_height,
                                        'product_type' : artikulcomponent.product_type,
                                        'profile_type' : artikulcomponent.profile_type,
                                        'export_description':'',

                                        'coating_qbic' : q_bic,

                                        # 'id_savdo' : 1,#row[''],
                                        # 'klaes' : 1,#row[''],
                                        
                                        # 'ch_profile_type' : 1,#row[''],
                                        # 'kls_wast_length' : 1,#row[''],
                                        # 'kls_wast' : 1,#row[''],
                                        # 'ch_klaes_optm' : 1,#row[''],
                                        # 'goods_group' : 1,#row['']
                                    }
                                )
        
        art = ArtikulKomponentPVC.objects.filter(artikul = df['Артикул'][key])[:1].get()

        component = df['Артикул'][key]
        if df['Тип покрытия'][key] == 'Ламинированный':      
                lamtext = row['Код лам пленки снаружи']+"/"+row['Код лам пленки внутри']+' '
                df_new['Ламинация'][key] = art.component+'-L ' +row['Код цвета основы/Замес'] +' L'+dlina +' ' +lamtext+row['Цвет резины']+' '+ row['Надпись наклейки']
                if PVCProduct.objects.filter(artikul =component,section ='L',kratkiy_tekst_materiala=df_new['Ламинация'][key]).exists():
                    df_new['SAP код L'][key] = PVCProduct.objects.filter(artikul =component,section ='L',kratkiy_tekst_materiala=df_new['Ламинация'][key])[:1].get().material
                    duplicat_list.append([df_new['SAP код L'][key],df_new['Ламинация'][key],'L'])
                else: 
                    if PVCProduct.objects.filter(artikul =component,section ='L').exists():
                            umumiy_counter[component+'-L'] += 1
                            max_valuesL = umumiy_counter[ component +'-L']
                            materiale = component+"-L{:03d}".format(max_valuesL)
                            PVCProduct(artikul =component,section ='L',counter=max_valuesL,gruppa_materialov='PVCPF',kratkiy_tekst_materiala=df_new['Ламинация'][key],material=materiale).save()
                            df_new['SAP код L'][key]=materiale
                            
                            component2 = materiale.split('-')[0]
                            artikulcomponent = ArtikulKomponentPVC.objects.filter(artikul = df['Артикул'][key])[:1].get()
                        
                            q_bic = ''
                            if row['Тип покрытия'] =='Неламинированный':
                                q_bic = row['Код цвета основы/Замес']
                            else:
                                if row['Цвет лам пленки снаружи'] =='XXXX':
                                    q_bic = row['Цвет лам пленки внутри']
                                else:
                                    q_bic = row['Цвет лам пленки снаружи']
                                
                            cache_for_cratkiy_text.append(
                                            {'sap_code':  materiale,
                                             'kratkiy':df_new['Ламинация'][key],
                                            'system' : row['Название системы'],
                                            'number_of_chambers' : row['Количество камер'],
                                            'article' : row['Артикул'],
                                            'profile_type_id' : row['Код к компоненту системы'],
                                            'length' : row['Длина (мм)'],
                                            'surface_treatment' : row['Тип покрытия'],
                                            'outer_side_pc_id' : row['Код цвета основы/Замес'],
                                            'outer_side_wg_id' : row['Цвет лам пленки снаружи'],
                                            'inner_side_wg_id' : row['Цвет лам пленки внутри'],
                                            'sealer_color' : row['Цвет резины'],
                                            'print_view' : row['Надпись наклейки'],

                                            'width' : artikulcomponent.width,
                                            'height' : artikulcomponent.height,
                                            'category' : artikulcomponent.category,
                                            'material_class' : 'Полуфабрикат',
                                            'rawmat_type' : 'ПФ',
                                            'tnved' : artikulcomponent.tnved,
                                            'surface_treatment_export' :'',
                                            'amount_in_a_package' : '',
                                            'wms_width' : artikulcomponent.wms_width,
                                            'wms_height' : artikulcomponent.wms_height,
                                            'product_type' : artikulcomponent.product_type,
                                            'profile_type' : artikulcomponent.profile_type,
                                            'export_description':'',

                                            'coating_qbic' : q_bic,

                                            # 'id_savdo' : 1,#row[''],
                                            # 'klaes' : 1,#row[''],
                                            
                                            # 'ch_profile_type' : 1,#row[''],
                                            # 'kls_wast_length' : 1,#row[''],
                                            # 'kls_wast' : 1,#row[''],
                                            # 'ch_klaes_optm' : 1,#row[''],
                                            # 'goods_group' : 1,#row['']
                                            }
                                        )
                    
                    else:
                            materiale = df['Артикул'][key]+"-L{:03d}".format(1)
                            PVCProduct(artikul =df['Артикул'][key],section ='L',counter=1,gruppa_materialov='PVCPF',kratkiy_tekst_materiala=df_new['Ламинация'][key],material=materiale).save()
                            df_new['SAP код L'][key]=materiale
                            umumiy_counter[df['Артикул'][key]+'-L'] = 1
                            
                            artikulcomponent = ArtikulKomponentPVC.objects.filter(artikul = df['Артикул'][key])[:1].get()
                        
                            q_bic = ''
                            if row['Тип покрытия'] =='Неламинированный':
                                q_bic = row['Код цвета основы/Замес']
                            else:
                                if row['Цвет лам пленки снаружи'] =='XXXX':
                                    q_bic = row['Цвет лам пленки внутри']
                                else:
                                    q_bic = row['Цвет лам пленки снаружи']
                           
                                
                            cache_for_cratkiy_text.append(
                                            {'sap_code':  materiale,
                                             'kratkiy':df_new['Ламинация'][key],
                                            'system' : row['Название системы'],
                                            'number_of_chambers' : row['Количество камер'],
                                            'article' : row['Артикул'],
                                            'profile_type_id' : row['Код к компоненту системы'],
                                            'length' : row['Длина (мм)'],
                                            'surface_treatment' : row['Тип покрытия'],
                                            'outer_side_pc_id' : row['Код цвета основы/Замес'],
                                            'outer_side_wg_id' : row['Цвет лам пленки снаружи'],
                                            'inner_side_wg_id' : row['Цвет лам пленки внутри'],
                                            'sealer_color' : row['Цвет резины'],
                                            'print_view' : row['Надпись наклейки'],

                                            'width' : artikulcomponent.width,
                                            'height' : artikulcomponent.height,
                                            'category' : artikulcomponent.category,
                                            'material_class' : 'Полуфабрикат',
                                            'rawmat_type' : 'ПФ',
                                            'tnved' : '',
                                            'surface_treatment_export' : '',
                                            'amount_in_a_package' :'',
                                            'wms_width' : artikulcomponent.wms_width,
                                            'wms_height' : artikulcomponent.wms_height,
                                            'product_type' : artikulcomponent.product_type,
                                            'profile_type' : artikulcomponent.profile_type,
                                            'export_description':'',

                                            'coating_qbic' : q_bic,

                                            # 'id_savdo' : 1,#row[''],
                                            # 'klaes' : 1,#row[''],
                                            
                                            # 'ch_profile_type' : 1,#row[''],
                                            # 'kls_wast_length' : 1,#row[''],
                                            # 'kls_wast' : 1,#row[''],
                                            # 'ch_klaes_optm' : 1,#row[''],
                                            # 'goods_group' : 1,#row['']
                                            }
                                        )
        
                
        
        df_new['Экструзия холодная резка'][key] = art.component+'-E ' +row['Код цвета основы/Замес'] +' L'+row['Длина (мм)'] +' ' + row['Надпись наклейки']
        
        
                    
       
        simple_existE = PVCProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala= df_new['Экструзия холодная резка'][key]).exists()

        
        if simple_existE:
            sap_code_e = PVCProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key])[:1].get().material
            duplicat_list.append([df_new['SAP код E'][key],df_new['Экструзия холодная резка'][key],'E'])
            df_new['SAP код E'][key] = sap_code_e

        else:
                if PVCProduct.objects.filter(artikul =component,section ='E').exists():
                    umumiy_counter[component+'-E'] += 1
                    max_valuesE = umumiy_counter[component+'-E']
                    materiale = component+"-E{:03d}".format(max_valuesE)
                    PVCProduct(artikul =component,section ='E',counter=max_valuesE,gruppa_materialov='PVCPF',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key],material=materiale).save()
                    df_new['SAP код E'][key]=materiale
                    
                    artikulcomponent = ArtikulKomponentPVC.objects.filter(artikul = df['Артикул'][key])[:1].get()
                        
                    q_bic = ''
                    if row['Тип покрытия'] =='Неламинированный':
                        q_bic = row['Код цвета основы/Замес']
                    else:
                        if row['Цвет лам пленки снаружи'] =='XXXX':
                            q_bic = row['Цвет лам пленки внутри']
                        else:
                            q_bic = row['Цвет лам пленки снаружи']
                            
                    cache_for_cratkiy_text.append(
                                        {   
                                            'sap_code':  materiale,
                                            'kratkiy':df_new['Экструзия холодная резка'][key],
                                            'system' : row['Название системы'],
                                            'number_of_chambers' : row['Количество камер'],
                                            'article' : row['Артикул'],
                                            'profile_type_id' : row['Код к компоненту системы'],
                                            'length' : row['Длина (мм)'],
                                            'surface_treatment' : row['Тип покрытия'],
                                            'outer_side_pc_id' : row['Код цвета основы/Замес'],
                                            'outer_side_wg_id' : row['Цвет лам пленки снаружи'],
                                            'inner_side_wg_id' : row['Цвет лам пленки внутри'],
                                            'sealer_color' : row['Цвет резины'],
                                            'print_view' : row['Надпись наклейки'],
                                            'width' : artikulcomponent.width,
                                            'height' : artikulcomponent.height,
                                            'category' : artikulcomponent.category,
                                            'material_class' : 'Полуфабрикат',
                                            'rawmat_type' : 'ПФ',
                                            'tnved' : '',
                                            'surface_treatment_export' : '',
                                            'amount_in_a_package' : '',
                                            'wms_width' : artikulcomponent.wms_width,
                                            'wms_height' : artikulcomponent.wms_height,
                                            'product_type' : artikulcomponent.product_type,
                                            'profile_type' : artikulcomponent.profile_type,

                                            'export_description':'',
                                            'coating_qbic' : q_bic,

                                            # 'id_savdo' : 1,#row[''],
                                            # 'klaes' : 1,#row[''],
                                            
                                            # 'ch_profile_type' : 1,#row[''],
                                            # 'kls_wast_length' : 1,#row[''],
                                            # 'kls_wast' : 1,#row[''],
                                            # 'ch_klaes_optm' : 1,#row[''],
                                            # 'goods_group' : 1,#row['']
                                        }
                                )
                            
                else: 
                    materiale = component+"-E{:03d}".format(1)
                    PVCProduct(artikul =component,section ='E',counter=1,gruppa_materialov='PVCPF',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key],material=materiale).save()
                    df_new['SAP код E'][key]=materiale
                    umumiy_counter[component+'-E'] = 1
                    
                    component2 = materiale.split('-')[0]
                         
                    artikulcomponent = ArtikulKomponentPVC.objects.filter(artikul = df['Артикул'][key])[:1].get()
                        
                    q_bic = ''
                    if row['Тип покрытия'] =='Неламинированный':
                        q_bic = row['Код цвета основы/Замес']
                    else:
                        if row['Цвет лам пленки снаружи'] =='XXXX':
                            q_bic = row['Цвет лам пленки внутри']
                        else:
                            q_bic = row['Цвет лам пленки снаружи']

                    cache_for_cratkiy_text.append(
                                        {
                                            'sap_code':  materiale,
                                            'kratkiy':df_new['Экструзия холодная резка'][key],
                                            'system' : row['Название системы'],
                                            'number_of_chambers' : row['Количество камер'],
                                            'article' : row['Артикул'],
                                            'profile_type_id' : row['Код к компоненту системы'],
                                            'length' : row['Длина (мм)'],
                                            'surface_treatment' : row['Тип покрытия'],
                                            'outer_side_pc_id' : row['Код цвета основы/Замес'],
                                            'outer_side_wg_id' : row['Цвет лам пленки снаружи'],
                                            'inner_side_wg_id' : row['Цвет лам пленки внутри'],
                                            'sealer_color' : row['Цвет резины'],
                                            'print_view' : row['Надпись наклейки'],
                                            'export_description':'',
                                            'width' : artikulcomponent.width,
                                            'height' : artikulcomponent.height,
                                            'category' : artikulcomponent.category,
                                            'material_class' : 'Полуфабрикат',
                                            'rawmat_type' : 'ПФ',
                                            'tnved' : '',
                                            'surface_treatment_export' : '',
                                            'amount_in_a_package' : '',
                                            'wms_width' : artikulcomponent.wms_width,
                                            'wms_height' : artikulcomponent.wms_height,
                                            'product_type' : artikulcomponent.product_type,
                                            'profile_type' : artikulcomponent.profile_type,


                                            'coating_qbic' : q_bic,

                                            # 'id_savdo' : 1,#row[''],
                                            # 'klaes' : 1,#row[''],
                                            
                                            # 'ch_profile_type' : 1,#row[''],
                                            # 'kls_wast_length' : 1,#row[''],
                                            # 'kls_wast' : 1,#row[''],
                                            # 'ch_klaes_optm' : 1,#row[''],
                                            # 'goods_group' : 1,#row['']
                                        }
                                )
                    

                    
        
      
    parent_dir ='{MEDIA_ROOT}\\uploads\\pvc\\'
    
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads\\','pvc')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\pvc\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}\\',hour)
      
      
    df_char = create_characteristika(cache_for_cratkiy_text) 
    df_char_title = create_characteristika_utils(cache_for_cratkiy_text)
                 
      
            
    if not os.path.isfile(f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}\\{hour}\\pvc-{minut}.xlsx'):
        path_alu =  f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}\\{hour}\\pvc-{minut}.xlsx'
        path_ramka_norma =  f'uploads\\pvc\\{year}\\{month}\\{day}\\{hour}\\norma-{minut}.xlsx'
    else:
        st =random.randint(0,1000)
        path_alu =  f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}\\{hour}\\pvc-{minut}-{st}.xlsx'
        path_ramka_norma =  f'uploads\\pvc\\{year}\\{month}\\{day}\\{hour}\\norma-{minut}-{st}.xlsx'
      



    for key,razlov in df_new.iterrows():
        if razlov['SAP код 7']!="":
                if not RazlovkaPVX.objects.filter(sapkode7=razlov['SAP код 7'],krat7=razlov['U-Упаковка + Готовая Продукция']).exists():
                    RazlovkaPVX(
                            esapkode =razlov['SAP код E'],
                            ekrat =razlov['Экструзия холодная резка'],
                            lsapkode =razlov['SAP код L'],
                            lkrat =razlov['Ламинация'], 
                            sapkode7 =razlov['SAP код 7'],
                            krat7 =razlov['U-Упаковка + Готовая Продукция']
                        ).save()
        
    for key,razlov in df_char.iterrows():
        if not Characteristika.objects.filter(sap_code=razlov['SAP CODE'],kratkiy=razlov['KRATKIY TEXT']).exists():
                Characteristika(
                    sap_code = razlov['SAP CODE'],
                    kratkiy=razlov['KRATKIY TEXT'], 
                    system = razlov['SYSTEM'], 
                    number_of_chambers = razlov['NUMBER_OF_CHAMBERS'], 
                    article = razlov['ARTICLE'], 
                    profile_type_id = razlov['PROFILE_TYPE_ID'], 
                    length = razlov['LENGTH'], 
                    surface_treatment = razlov['SURFACE_TREATMENT'], 
                    outer_side_pc_id = razlov['OUTER_SIDE_PC_ID'], 
                    outer_side_wg_id = razlov['OUTER_SIDE_WG_ID'], 
                    inner_side_wg_id = razlov['INNER_SIDE_WG_ID'], 
                    sealer_color = razlov['SEALER_COLOR'], 
                    print_view = razlov['PRINT_VIEW'], 
                    width = razlov['WIDTH'], 
                    height = razlov['HEIGHT'], 
                    category = razlov['CATEGORY'], 
                    material_class = razlov['MATERIAL_CLASS'], 
                    rawmat_type = razlov['RAWMAT_TYPE'], 
                    tnved = razlov['TNVED'], 
                    surface_treatment_export = razlov['SURFACE_TREATMENT_EXPORT'], 
                    amount_in_a_package = razlov['AMOUNT_IN_A_PACKAGE'], 
                    wms_width = razlov['WMS_WIDTH'], 
                    wms_height = razlov['WMS_HEIGHT'], 
                    product_type = razlov['PRODUCT_TYPE'], 
                    profile_type = razlov['PROFILE_TYPE'], 
                    coating_qbic = razlov['COATING_QBIC']		
                ).save()

        
        
    
    exchange_value = ExchangeValues.objects.get(id=1)
    price_all_correct = True
      
    for key, row in df_char_title.iterrows():
        if LengthOfProfilePVC.objects.filter(artikul = row['article'],length=row['Длина']).exists():
            length_of_profile = LengthOfProfilePVC.objects.filter(artikul = row['article'],length=row['Длина'])[:1].get()
            df_char_title['Общий вес за штуку'][key] =length_of_profile.ves_za_shtuk
            df_char_title['Удельный вес за метр'][key] = length_of_profile.ves_za_metr
            price = Price.objects.filter(tip_pokritiya = row['Тип покрытия'],zames=row['Код цвета основы/Замес'])[:1].get()
            df_char_title['Price'][key] = float(price.price.replace(',','.')) * float(str(df_char_title['Общий вес за штуку'][key]).replace(',','.'))  * float(exchange_value.valute.replace(',','.'))
        else:
            price_all_correct = False


    del df_new['counter']

    writer = pd.ExcelWriter(path_alu, engine='xlsxwriter')
    df_new.to_excel(writer,index=False,sheet_name='Schotchik')
    df_char.to_excel(writer,index=False,sheet_name='Characteristika')
    df_char_title.to_excel(writer,index=False,sheet_name='title')
    writer.close()


    order_id = request.GET.get('order_id',None)

    work_type = 1
    if order_id:
        work_type = OrderPVX.objects.get(id = order_id).work_type
        if price_all_correct and  work_type != 5 :
            path = update_char_title_function(df_char_title,order_id)
            files =[File(file=p,filetype='pvc') for p in path]
            files.append(File(file=path_alu,filetype='pvc'))
            context ={
                  'files':files,
                  'section':'Формированый обычный файл'
            }

            if order_id:
                file_paths =[ file.file for file in files]
                order = OrderPVX.objects.get(id = order_id)
                paths = order.paths
                raz_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                zip_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                paths['pvc_razlovka_file']= file_paths
                paths['raz_created_at']= raz_created_at
                paths['zip_created_at']= zip_created_at
                paths['status_l']= 'done'
                paths['status_raz']= 'done'
                paths['status_zip']= 'done'
                paths['status_text_l']= 'done'
                
                order.paths = paths
                order.aluminiy_worker = request.user
                order.current_worker = request.user
                order.work_type = 6
                order.save()
                context['order'] = order
                paths =  order.paths
                for key,val in paths.items():
                    context[key] = val
                return render(request,'order/order_detail_pvc.html',context)  
        else:
            
            file =[File(file = path_alu,filetype='pvc')]
            context = {
                  'files':file,
                  'section':'Формированый pvc файл'
            }
            
            if order_id:
                order = OrderPVX.objects.get( id = order_id)
                paths = order.paths 
                if work_type != 5:
                    context2 ={
                            'pvc_razlovka_file':[path_alu,path_alu]
                    }
                    paths['pvc_razlovka_file'] = [path_alu,path_alu]
                else:
                    path_alu = order.paths['pvc_razlovka_file']
                    context2 ={
                            'pvc_razlovka_file':[path_alu,path_alu]
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

                workers = User.objects.filter(role = 1,is_active =True)
                context2['workers'] = workers

                return render(request,'order/order_detail_pvc.html',context2)

    
    return render(request,'universal/generated_files.html',{'a':'b'})



def update_char_title_function(df_title,order_id):
      df = df_title
      df = df.astype(str)
      pathzip = characteristika_created_txt_create(df,order_id)
      return pathzip