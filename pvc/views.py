from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test,login_required
from datetime import datetime
from config.settings import MEDIA_ROOT
from .forms import FileFormPVC,FileFormCharPVC
from .models import PVCProduct,PVCFile,ArtikulKomponentPVC,CameraPvc,AbreviaturaLamination,LengthOfProfilePVC,Characteristika,Price,CharacteristikaFilePVC,RazlovkaPVX,BuxgalterskiyNazvaniye,DliniyText
from order.models import OrderPVX
from accounts.models import User
from aluminiy.models import LengthOfProfile,ExchangeValues
import pandas as pd
from django.db.models import Count,Max,Q
from onlinesavdo.models import OnlineSavdoFile,OnlineSavdoOrder
from onlinesavdo.forms import FileForm,FileForm2
from onlinesavdo.utils import zip
from django.core.paginator import Paginator
from django.http import JsonResponse
import os
import numpy as np
import sys
import json
from .BAZA import DOP_PROFIL
from functools import partial
import random 
from aluminiy.models import ExchangeValues
from .utils import create_folder,create_characteristika,create_characteristika_utils,characteristika_created_txt_create,check_for_correct,get_ozmka
from accounts.decorators import allowed_users
from aluminiy.utils import download_bs64


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','razlovka','only_razlovka'])
def download_all_characteristiki(request):
        simple_list = Characteristika.objects.all().values_list('sap_code','kratkiy','system','number_of_chambers','article','profile_type_id','length','surface_treatment','outer_side_pc_id','outer_side_wg_id','inner_side_wg_id','sealer_color','print_view','width','height','category','material_class','rawmat_type','tnved','surface_treatment_export','amount_in_a_package','wms_width','wms_height','product_type','profile_type','coating_qbic','id_savdo','online_savdo_name')
        data = pd.DataFrame(np.array(list(simple_list)),columns=[
                'SAPCOD','KRATKIY TEXT','NAZVANIYE SYSTEM','NUMBER OF CHAMBERS','ARTICLE','PROFILE TYPE ID','LENGTH','SURFACETREATMENT','OUTER SIDE PC ID','OUTER SIDE WG ID','INNER SIDE WG ID','SEALER COLOR','PRINT VIEW','WIDTH','HEIGHT','CATEGORY','MATERIAL CLASS','RAWMAT TYPE','TNVED','SURFACE TREATMENT EXPORT','AMOUNT IN A PACKAGE','WMS WIDTH','WMS HEIGHT','PRODUCT TYPE','PROFILE TYPE','COATING QBIC','ID SAVDO','ONLINE SAVDO NAME',
                                                        ])
        data = data.replace('nan','')
        
        res = download_bs64([data,],'CHARACTERISTIKA')
        return res

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','razlovka','only_razlovka'])
def show_all_artikules(request):
    search =request.GET.get('search',None)
    
    if search:
        products = ArtikulKomponentPVC.objects.filter(Q(artikul__icontains = search)|Q(component__icontains=search)).values_list('artikul','component').order_by('-created_at')
    else:
        
        products = ArtikulKomponentPVC.objects.all().values_list('artikul','component').order_by('-created_at')
                  
    paginator = Paginator(products, 25)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)

    context ={
        'section':'PVC артикул',
        'products':page_obj,
        'search':search,
        'type':'simple'

    }
    return render(request,'pvc/show_artikules.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','razlovka','only_razlovka'])
def download_all_razlovki(request):
        simple_list = RazlovkaPVX.objects.all().values_list('esapkode','ekrat','lsapkode','lkrat','sapkode7','krat7')
        data = pd.DataFrame(np.array(list(simple_list)),columns=[
                'SAP код E','Экструзия холодная резка',
                'SAP код L','Ламинация',
                'SAP код 7','U-Упаковка + Готовая Продукция'
                                                        ])
        data = data.replace('nan','')
        
        res = download_bs64([data,],'OBICHNIY')
        return res

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','razlovka','only_razlovka'])
def download_all_artikles(request):
        simple_list = ArtikulKomponentPVC.objects.all().values_list('artikul','component','component2','nazvaniye_sistem','camera','kod_k_component','width','height','category','tnved','wms_width','wms_height','product_type','profile_type','iskyucheniye','is_special','nakleyka_nt1')
        data = pd.DataFrame(np.array(list(simple_list)),columns=[
                'Артикул','Копонент','Копонент2','Название','Камера','Код к компонент','Ширина','Высота','Категория','Tnved','WMS ширина','WMS высота','Продукт тип','Тип профилей','Резина исключен.','Ламинация 2-ч xxx','Наклейка NT1'
                                                        ])
        data = data.replace('nan','')
        
        res = download_bs64([data,],'АРТИКУЛ')
        return res

class FileRazlovki:
    def __init__(self,file):
        self.file =file

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','only_razlovka','user1','razlovka'])
def get_razlovka_pvc(request):
    if request.method =='POST':
        ozmk = request.POST.get('ozmk',None)
        if ozmk:
            ozmks =ozmk.split()
            path,df = get_ozmka(ozmks)
            res = download_bs64(df,'RAZLOVKA')
            if request.user.role =='moderator':
                return res
            files = [FileRazlovki(file=p) for p in path]
            context ={
                'files':files,
                'section':'Разловка'
            }
            return render(request,'universal/generated_files.html',context)
        else:
            return render(request,'norma/razlovka_find_org.html')
    else:
        path1 = request.GET.get('path',None)
        if path1:
            if sys.platform == "win32":
                os.startfile(path1)
        return render(request,'norma/razlovka_find_org.html')




@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def update_char_title_pvc(request,id):
    file = CharacteristikaFilePVC.objects.get(id=id).file
    df = pd.read_excel(f'{MEDIA_ROOT}/{file}','title')
    df =df.astype(str)

    order_id = request.GET.get('order_id',None)
    if order_id:
        order = OrderPVX.objects.get(id = order_id)

    pathzip = characteristika_created_txt_create(df,order_id)
    fileszip = [FilePVCC(file=path,filetype='BENKAM') for path in pathzip]
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
      


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
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
@allowed_users(allowed_roles=['admin','moderator'])
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
                                    'pvc_file':f'{MEDIA_ROOT}\\{new_order.file}',
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
                  workers = User.objects.filter(role =  'moderator')
                  context ={
                  'form':form,
                  'section':'Формирование сапкода pvc',
                  'workers':workers
                  }
                  return render(request,'pvc/main.html',context)
      form =FileFormPVC()
      workers = User.objects.filter(role =  'moderator')
      context ={
      'form':form,
      'section':'Формирование сапкода pvc',
      'workers':workers
      }
      return render(request,'pvc/main.html',context)


class FilePVCC:
      def __init__(self,file,filetype):
            self.file =file
            self.filetype =filetype

class Buxgalter:
      def __init__(self,naz_ru,naz_eng,sb):
            self.naz_ru =naz_ru
            self.naz_eng =naz_eng
            self.sb =sb

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])    
def product_add_second_org(request,id):
    file = PVCFile.objects.get(id=id).file
    if 'SHABLON' in str(file):
        df = pd.read_excel(f'{MEDIA_ROOT}/{file}')
    else:
        df = pd.read_excel(f'{MEDIA_ROOT}/{file}',header=4)
    
    df =df.astype(str)
    
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M")
      
    order_id = request.GET.get('order_id',None)
      


      
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
    
    rezina_iskyuch = ArtikulKomponentPVC.objects.filter(iskyucheniye ='1').values_list('artikul',flat=True)
    
    
    
    cache_for_cratkiy_text =[]
    duplicat_list =[]
    
    exturision_list = []
    
    for key,row in df.iterrows():  
        row['Длина (мм)'] = str(row['Длина (мм)']).replace('.0','')
        dlina = row['Длина (мм)']
        df_new['U-Упаковка + Готовая Продукция'][key] = df['Краткий текст'][key]
        
        row['Код лам пленки снаружи'] =str(row['Код лам пленки снаружи']).replace('.0','')
        row['Код лам пленки внутри'] =str(row['Код лам пленки внутри']).replace('.0','')
        row['Количество камер'] =str(row['Количество камер']).replace('.0','')
        
        
        row['Код лам пленки снаружи']='0'+row['Код лам пленки снаружи'] if row['Код лам пленки снаружи']=='550' else row['Код лам пленки снаружи']
        if ((row['Название'] == 'nan') or (row['Название'] == '')):
            online_savdo_name = ''
        else:
            online_savdo_name = row['Название']
            
        if 'Название export' in list(df.columns):
            if ((row['Название export'] == 'nan') or (row['Название export'] == '')):
                export_name = ''
            else:
                export_name = row['Название export']
        else:
            export_name = ''
            
        if ((row['Online savdo ID'] == 'nan') or (row['Online savdo ID'] == '')):
            id_savdo = 'XXXXX'
        else:
            id_savdo = str(row['Online savdo ID']).replace('.0','')

        dlinniy_text = DliniyText.objects.filter(sap_code =df['Артикул'][key])[:1].get().product_desc
        
        if df['Тип покрытия'][key] == 'Ламинированный':

            export_description =''
            if ('PDF' not in row['Артикул'] and 'L0001' not in row['Артикул'] and 'L0002' not in row['Артикул']) and ((row['Код резины'] =='NR') or(row['Код резины'] =='nan')):
                export_description ='Профиль из ПВХ ламинированный'
            elif ('PDF' not in row['Артикул'] and 'L0001' not in row['Артикул'] and 'L0002' not in row['Артикул']) and (row['Код резины'] !='NR'):
                export_description ='Профиль из ПВХ ламинированный с уплотнителем'
            elif ('PDF' not in row['Артикул']) and (row['Код резины'] =='NR' or row['Код резины'] =='nan') and ( 'L0001' in row['Артикул'] or 'L0002' in row['Артикул']) :
                export_description ='Ламбри из ПВХ ламинированный'
            elif('L0001' not in row['Артикул'] and 'L0002' not in row['Артикул']) and (row['Код резины'] =='nan'):
                export_description ='Подоконник из ПВХ ламинированный'

            if export_description !='':
                buxgalter_naz = BuxgalterskiyNazvaniye.objects.filter(naz_ru = export_description)[:1].get()
            else:
                buxgalter_naz =Buxgalter(naz_ru='',naz_eng='',sb='')

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
                        
                        outer_side_wg_id = row['Цвет лам пленки снаружи']
                        inner_side_wg_id = row['Цвет лам пленки внутри']
                        
                        if row['Код лам пленки снаружи'] ==row['Код лам пленки внутри']:
                            surface_treatment_export = AbreviaturaLamination.objects.filter(abreviatura =row['Код лам пленки внутри'])[:1].get().surface_treatment_export
                            q_bic = AbreviaturaLamination.objects.filter(abreviatura =row['Код лам пленки внутри'])[:1].get().coating_qbic
                        elif row['Код лам пленки снаружи'] =='XXXX':
                            surface_treatment_export = AbreviaturaLamination.objects.filter(abreviatura =row['Код лам пленки внутри'])[:1].get().surface_treatment_export_vn
                            q_bic = AbreviaturaLamination.objects.filter(abreviatura =row['Код лам пленки внутри'])[:1].get().coating_qbic
                        else:
                            surface_treatment_export = AbreviaturaLamination.objects.filter(abreviatura =row['Код лам пленки снаружи'])[:1].get().surface_treatment_export_na
                            q_bic = AbreviaturaLamination.objects.filter(abreviatura =row['Код лам пленки снаружи'])[:1].get().coating_qbic

                        
                       

                        
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
                                            'outer_side_wg_id' : outer_side_wg_id,
                                            'inner_side_wg_id' : inner_side_wg_id,
                                            'sealer_color' : row['Код резины'],
                                            'print_view' : row['Код наклейки'],
                                            'kod_lam_plen_snar':row['Код лам пленки снаружи'],
                                            'kod_lam_plen_vnut':row['Код лам пленки внутри'],
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
                                            'export_description':buxgalter_naz.naz_ru,
                                            'export_description_eng':buxgalter_naz.naz_eng,
                                            'sb':buxgalter_naz.sb,
                                            'coating_qbic' : q_bic,
                                            'online_savdo_name':online_savdo_name,
                                            'id_savdo' : id_savdo,
                                            'dlinniy_text':dlinniy_text,
                                            'nazvaniye_export':export_name

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
                        # print(df['Артикул'][key],'yoqlar')
                        artikulcomponent = ArtikulKomponentPVC.objects.filter(artikul = df['Артикул'][key])[:1].get()
                        
                        q_bic = ''
                        outer_side_wg_id = row['Цвет лам пленки снаружи']
                        inner_side_wg_id = row['Цвет лам пленки внутри']
                        
                        if row['Код лам пленки снаружи'] ==row['Код лам пленки внутри']:
                            surface_treatment_export = AbreviaturaLamination.objects.filter(abreviatura =row['Код лам пленки внутри'])[:1].get().surface_treatment_export
                            q_bic = AbreviaturaLamination.objects.filter(abreviatura =row['Код лам пленки внутри'])[:1].get().coating_qbic
                        elif row['Код лам пленки снаружи'] =='XXXX':
                            surface_treatment_export = AbreviaturaLamination.objects.filter(abreviatura =row['Код лам пленки внутри'])[:1].get().surface_treatment_export_vn
                            q_bic = AbreviaturaLamination.objects.filter(abreviatura =row['Код лам пленки внутри'])[:1].get().coating_qbic
                        else:
                            surface_treatment_export = AbreviaturaLamination.objects.filter(abreviatura =row['Код лам пленки снаружи'])[:1].get().surface_treatment_export_na
                            q_bic = AbreviaturaLamination.objects.filter(abreviatura =row['Код лам пленки снаружи'])[:1].get().coating_qbic

                        
                        
                        
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
                                            'outer_side_wg_id' : outer_side_wg_id,
                                            'inner_side_wg_id' : inner_side_wg_id,
                                            'sealer_color' : row['Код резины'],
                                            'print_view' : row['Код наклейки'],
                                            'kod_lam_plen_snar':row['Код лам пленки снаружи'],
                                            'kod_lam_plen_vnut':row['Код лам пленки внутри'],

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
                                            'export_description':buxgalter_naz.naz_ru,
                                            'export_description_eng':buxgalter_naz.naz_eng,
                                            'sb':buxgalter_naz.sb,

                                            'coating_qbic' : q_bic,
                                            'online_savdo_name':online_savdo_name,
                                            'id_savdo' : id_savdo,
                                            'dlinniy_text':dlinniy_text,
                                            'nazvaniye_export':export_name
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
            export_description =''
            if ('PDF' not in row['Артикул'] and 'L0001' not in row['Артикул'] and 'L0002' not in row['Артикул']) and (row['Код резины'] =='NR'):
                export_description ='Профиль из ПВХ'
            elif ('PDF' not in row['Артикул'] and 'L0001' not in row['Артикул'] and 'L0002' not in row['Артикул']) and (row['Код резины'] !='NR'):
                export_description ='Профиль из ПВХ с уплотнителем'
            elif ('PDF' not in row['Артикул']) and ( 'L0001' in row['Артикул'] or 'L0002' in row['Артикул']) and (row['Код резины'] =='NR'  or row['Код резины'] =='nan'):
                export_description ='Ламбри из ПВХ'
            elif('L0001' not in row['Артикул'] and 'L0002' not in row['Артикул']) and (row['Код резины'] =='nan'):
                export_description ='Подоконник из ПВХ'
            
            if export_description !='':
                buxgalter_naz = BuxgalterskiyNazvaniye.objects.filter(naz_ru = export_description)[:1].get()
            else:
                buxgalter_naz =Buxgalter(naz_ru='',naz_eng='',sb='')

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


                        outer_side_wg_id = ''
                        inner_side_wg_id = ''
             
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
                                            'outer_side_wg_id' : outer_side_wg_id,
                                            'inner_side_wg_id' : inner_side_wg_id,
                                            'sealer_color' : row['Код резины'],
                                            'print_view' : row['Код наклейки'],
                                            'kod_lam_plen_snar':row['Код лам пленки снаружи'],
                                            'kod_lam_plen_vnut':row['Код лам пленки внутри'],

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
                                            'export_description':buxgalter_naz.naz_ru,
                                            'export_description_eng':buxgalter_naz.naz_eng,
                                            'sb':buxgalter_naz.sb,

                                            'coating_qbic' : q_bic,
                                            'online_savdo_name':online_savdo_name,
                                            'id_savdo' : id_savdo,
                                            'dlinniy_text':dlinniy_text,
                                            'nazvaniye_export':export_name

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
                    
                    if 'подок' in str(row['Название системы']).lower():
                        outer_side_wg_id = AbreviaturaLamination.objects.filter(abreviatura =row['Код лам пленки снаружи'])[:1].get().pokritiya +' п'
                        inner_side_wg_id = AbreviaturaLamination.objects.filter(abreviatura =row['Код лам пленки внутри'])[:1].get().pokritiya +' п'
                    else:
                        outer_side_wg_id = row['Код лам пленки снаружи']
                        inner_side_wg_id = row['Код лам пленки внутри']
                    
                    
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
                                        'outer_side_wg_id' : outer_side_wg_id,
                                        'inner_side_wg_id' : inner_side_wg_id,
                                        'sealer_color' : row['Код резины'],
                                        'print_view' : row['Код наклейки'],
                                        'kod_lam_plen_snar':row['Код лам пленки снаружи'],
                                        'kod_lam_plen_vnut':row['Код лам пленки внутри'],
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
                                        'export_description':buxgalter_naz.naz_ru,
                                        'export_description_eng':buxgalter_naz.naz_eng,
                                        'sb':buxgalter_naz.sb,

                                        'coating_qbic' : q_bic,
                                        'online_savdo_name':online_savdo_name,
                                        'id_savdo' : id_savdo,
                                        'dlinniy_text':dlinniy_text,
                                        'nazvaniye_export':export_name

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
                if row['Код резины']!='nan':   
                    lamtext = row['Код лам пленки снаружи']+"/"+row['Код лам пленки внутри']+' '+row['Код резины']
                else:
                    lamtext = row['Код лам пленки снаружи']+"/"+row['Код лам пленки внутри']
                    
                df_new['Ламинация'][key] = art.component+'-L ' +row['Код цвета основы/Замес'] +' L'+dlina +' ' +lamtext+' '+ row['Код наклейки']
                
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

                            outer_side_wg_id = row['Цвет лам пленки снаружи']
                            inner_side_wg_id = row['Цвет лам пленки внутри']

                       
                        
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
                                            'outer_side_wg_id' : outer_side_wg_id,
                                            'inner_side_wg_id' : inner_side_wg_id,
                                            'sealer_color' : row['Код резины'],
                                            'print_view' : row['Код наклейки'],
                                            'kod_lam_plen_snar':row['Код лам пленки снаружи'],
                                            'kod_lam_plen_vnut':row['Код лам пленки внутри'],

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
                                            'export_description_eng':'',
                                            'sb':'',
                                            

                                            'coating_qbic' : q_bic,
                                            'online_savdo_name':'',
                                            'id_savdo' : id_savdo,
                                            'dlinniy_text':'',
                                            'nazvaniye_export':export_name
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
                            outer_side_wg_id = row['Цвет лам пленки снаружи']
                            inner_side_wg_id = row['Цвет лам пленки внутри']

                                
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
                                            'outer_side_wg_id' : outer_side_wg_id,
                                            'inner_side_wg_id' : inner_side_wg_id,
                                            'sealer_color' : row['Код резины'],
                                            'print_view' : row['Код наклейки'],
                                            'kod_lam_plen_snar':row['Код лам пленки снаружи'],
                                            'kod_lam_plen_vnut':row['Код лам пленки внутри'],

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
                                            'export_description_eng':'',
                                            'sb':'',

                                            'coating_qbic' : q_bic,
                                            'online_savdo_name':'',
                                            'id_savdo' : id_savdo,
                                            'dlinniy_text':'',
                                            'nazvaniye_export':export_name

                                            # 'id_savdo' : 1,#row[''],
                                            # 'klaes' : 1,#row[''],
                                            
                                            # 'ch_profile_type' : 1,#row[''],
                                            # 'kls_wast_length' : 1,#row[''],
                                            # 'kls_wast' : 1,#row[''],
                                            # 'ch_klaes_optm' : 1,#row[''],
                                            # 'goods_group' : 1,#row['']
                                            }
                                        )
        
        if component in rezina_iskyuch:
            text_nr = ' '
        else:
            text_nr = ' NR '


        if df['Тип покрытия'][key] == 'Ламинированный':
            
            if 'PDF' in row['Артикул'] or '.G00' in row['Артикул'] or row['Артикул'] in DOP_PROFIL:
                sd = 'NT1'
                nakleyka ='NT1'
            else:
                nakleyka = row['Код наклейки']
                sd = row['Код наклейки'] +' 1sd'

            if ((str(row['Код лам пленки внутри']).lower() =='xxxx') or (str(row['Код лам пленки снаружи']).lower() =='xxxx')):
                df_new['Экструзия холодная резка'][key] = art.component+'-E ' +row['Код цвета основы/Замес'] +' L'+row['Длина (мм)'] + text_nr + sd
            else:
                nakleyka ='NT1'
                df_new['Экструзия холодная резка'][key] = art.component+'-E ' +row['Код цвета основы/Замес'] +' L'+row['Длина (мм)'] + text_nr +'NT1'
        else:
            if component in rezina_iskyuch:
                text_nr = ' '
            elif row['Код резины'] =='' :
                text_nr = ' '
            else:
                rez =row['Код резины']
                text_nr = f' {rez} '

            nakleyka = row['Код наклейки']
            df_new['Экструзия холодная резка'][key] = art.component+'-E ' +row['Код цвета основы/Замес'] +' L'+row['Длина (мм)'] + text_nr + row['Код наклейки']
        
        
                    
       
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
                    
                    outer_side_wg_id = ''
                    inner_side_wg_id = ''

                
                    if row['Тип покрытия'] !='Неламинированный':
                        cache_for_cratkiy_text.append(
                                            {   
                                                'sap_code':  materiale,
                                                'kratkiy':df_new['Экструзия холодная резка'][key],
                                                'system' : row['Название системы'],
                                                'number_of_chambers' : row['Количество камер'],
                                                'article' : row['Артикул'],
                                                'profile_type_id' : row['Код к компоненту системы'],
                                                'length' : row['Длина (мм)'],
                                                'surface_treatment' : 'Неламинированный',
                                                'outer_side_pc_id' : row['Код цвета основы/Замес'],
                                                'outer_side_wg_id' : outer_side_wg_id,
                                                'inner_side_wg_id' : inner_side_wg_id,
                                                'sealer_color' : row['Код резины'],
                                                'print_view' : nakleyka,
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
                                                'kod_lam_plen_snar':row['Код лам пленки снаружи'],
                                                'kod_lam_plen_vnut':row['Код лам пленки внутри'],

                                                'export_description':'',
                                                'export_description_eng':'',
                                                'sb':'',
                                                'coating_qbic' : q_bic,
                                                'online_savdo_name':'',
                                                'id_savdo' : id_savdo,
                                                'dlinniy_text':dlinniy_text,
                                                'nazvaniye_export':export_name

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
                        
                    outer_side_wg_id = ''
                    inner_side_wg_id = ''
                    
                 
                    if row['Тип покрытия'] !='Неламинированный':
                        cache_for_cratkiy_text.append(
                                            {
                                                'sap_code':  materiale,
                                                'kratkiy':df_new['Экструзия холодная резка'][key],
                                                'system' : row['Название системы'],
                                                'number_of_chambers' : row['Количество камер'],
                                                'article' : row['Артикул'],
                                                'profile_type_id' : row['Код к компоненту системы'],
                                                'length' : row['Длина (мм)'],
                                                'surface_treatment' : 'Неламинированный',
                                                'outer_side_pc_id' : row['Код цвета основы/Замес'],
                                                'outer_side_wg_id' : outer_side_wg_id,
                                                'inner_side_wg_id' : inner_side_wg_id,
                                                'sealer_color' : row['Код резины'],
                                                'print_view' : nakleyka,
                                                'kod_lam_plen_snar':row['Код лам пленки снаружи'],
                                                'kod_lam_plen_vnut':row['Код лам пленки внутри'],
                                                
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
                                                'export_description_eng':'',
                                                'sb':'',

                                                'coating_qbic' : q_bic,
                                                'online_savdo_name':'',
                                                'id_savdo' : id_savdo,
                                                'dlinniy_text':dlinniy_text,
                                                'nazvaniye_export':export_name

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
    else:
        st =random.randint(0,1000)
        path_alu =  f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}\\{hour}\\pvc-{minut}-{st}.xlsx'
      



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
                    coating_qbic = razlov['COATING_QBIC'],
                    online_savdo_name = razlov['ONLINE_SAVDO_NAME'],		
                    id_savdo = razlov['ID_SAVDO']		
                ).save()

        
        
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
            files =[FilePVCC(file=p,filetype='pvc') for p in path]
            files.append(FilePVCC(file=path_alu,filetype='pvc'))
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
                order.pvc_worker = request.user
                order.current_worker = request.user
                order.work_type = 6
                order.save()
                context['order'] = order
                paths =  order.paths
                for key,val in paths.items():
                    context[key] = val
                return render(request,'order/order_detail_pvc.html',context)  
        else:
            
            file =[FilePVCC(file = path_alu,filetype='pvc')]
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

                workers = User.objects.filter(role =  'moderator',is_active =True)
                context2['workers'] = workers

                return render(request,'order/order_detail_pvc.html',context2)

    
    return render(request,'universal/generated_files.html',{'a':'b'})



def update_char_title_function(df_title,order_id):
      df = df_title
      df = df.astype(str)
      pathzip = characteristika_created_txt_create(df,order_id)
      return pathzip

#################################################################
#################################################################
###############################################################
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def show_list_history(request):
  files = OrderPVX.objects.all().order_by('-created_at')
  context ={
    'files':files
  }
  return render(request,'pvc/history.html',context)



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
def upload_new_product_pvc(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
                new_order = form.save()
                
                return render(request,'online_savdo/file_list.html',context)
    else:
        form =FileForm()
        context ={
        'form':form,
        'section':'Формирование сапкода обычный'
        }
    return render(request,'online_savdo/main.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def upload_product_org_pvc(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
                new_order = form.save()
                files = [File(id=new_order.id,file = new_order.file,filetype = new_order.file_type,created_at=datetime.now())]
                context ={
                    'files':files,
                    'link':'generate-pvc-file/'
                }
                return render(request,'online_savdo/file_list.html',context)
    else:
        form =FileForm()
        context ={
        'form':form,
        'section':'Формирование сапкода обычный'
        }
    return render(request,'online_savdo/main.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def upload_sozdaniye(request):
    if request.method == 'POST':
        for f in request.FILES.getlist('file'):
            form_savdo = FileForm(request.POST, request.FILES)
            form_sozd = FileForm(request.POST, request.FILES)
        if form_savdo.is_valid() and form_sozd.is_valid():
                paths = []
                for f in request.FILES.getlist('file'):
                    file_instance = OnlineSavdoFile(file=f)
                    file_instance.save()
                    paths.append(file_instance.file)
                
                online_savdo_order = OnlineSavdoOrder()
                
                online_savdo_order.paths = { 'path_1' : str(paths[0]), 'path_2' : str(paths[1]) }
                online_savdo_order.save()

                files = [File(id=online_savdo_order.id,file = 'EXCELL FILES',filetype = 'savdo',created_at=datetime.now())]
                context ={
                    'files':files,
                    'link':'generate-sozdaniyepvc-file/'
                }
                return render(request,'online_savdo/file_list.html',context)
    else:
        form_savdo = FileForm()
        form_sozd = FileForm()
        context ={
        'form_savdo':form_savdo,
        'form_sozd':form_sozd,
        'section':'Формирование'
        }
    return render(request,'online_savdo/sozdaniye_online_savdo.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def upload_sozdaniye_sena(request):
    if request.method == 'POST':
        form_savdo = FileForm(request.POST, request.FILES)
        form_sozd = FileForm(request.POST, request.FILES)
        if form_savdo.is_valid() and form_sozd.is_valid():
                paths = []
                for f in request.FILES.getlist('file'):
                    file_instance = OnlineSavdoFile(file=f)
                    file_instance.save()
                    paths.append(file_instance.file)

                online_savdo_order = OnlineSavdoOrder()
                online_savdo_order.paths = { 'path_1' : str(paths[0]), 'path_2' : str(paths[1]) }
                online_savdo_order.save()

                files = [File(id=online_savdo_order.id,file = 'EXCELL FILES',filetype = 'savdo',created_at=datetime.now())]
                context ={
                    'files':files,
                    'link':'generate-sozdaniyepvc-sena/'
                }
                return render(request,'online_savdo/file_list.html',context)
    else:
        form_savdo = FileForm()
        form_sozd = FileForm()
        context ={
        'form_savdo':form_savdo,
        'form_sozd':form_sozd,
        'section':'Формирование'
        }
    return render(request,'online_savdo/sena.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def upload_sozdaniye_format(request):
    if request.method == 'POST':
        form1 = FileForm(request.POST, request.FILES)
        if form1.is_valid():
                new_order1 = form1.save()
                online_savdo_order = OnlineSavdoOrder()
                online_savdo_order.paths = { 
                    'path_1' : str(new_order1.file)
                      }
                online_savdo_order.save()

                files = [File(id=online_savdo_order.id,file = 'EXCELL FILES',filetype = 'savdo',created_at=datetime.now())]
                context ={
                    'files':files,
                    'link':'generate-sozdaniyepvc-format/'
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
        form1 = FileForm2(request.POST, request.FILES)
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

                    elif ('VK' in file_name and 'beznal' in file_name):
                        paths['3'] = file_name
                    elif ('CHECK' in file_name and 'BEZNAL' in file_name):
                        paths['4'] = file_name

                    elif ('VK' in file_name and 'ZUU' in file_name):
                        paths['5'] = file_name
                    elif ('CHECK' in file_name and 'ZUU' in file_name):
                        paths['6'] = file_name

                    elif ('VK' in file_name and 'ZFKN' in file_name):
                        paths['7'] = file_name
                    elif ('CHECK' in file_name and 'ZFKN' in file_name):
                        paths['8'] = file_name

                    elif ('VK' in file_name and 'zfdn' in file_name):
                        paths['9'] = file_name
                    elif ('CHECK' in file_name and 'ZFDN' in file_name):
                        paths['10'] = file_name

                    elif ('VK' in file_name and 'ZREN' in file_name):
                        paths['11'] = file_name
                    elif ('CHECK' in file_name and 'ZREN' in file_name):
                        paths['12'] = file_name
                

                online_savdo_order = OnlineSavdoOrder()
                online_savdo_order.paths = { 
                    'path_1' : str(paths['1']),
                    'path_2' : str(paths['2']),
                    'path_3' : str(paths['3']),
                    'path_4' : str(paths['4']),
                    'path_5' : str(paths['5']),
                    'path_6' : str(paths['6']),
                    'path_7' : str(paths['7']),
                    'path_8' : str(paths['8']),
                    'path_9' : str(paths['9']),
                    'path_10' : str(paths['10']),
                    'path_11' : str(paths['11']),
                    'path_12' : str(paths['12'])
                      }
                online_savdo_order.save()

                files = [File(id=online_savdo_order.id,file = 'EXCELL FILES',filetype = 'savdo',created_at=datetime.now())]
                context ={
                    'files':files,
                    'link':'generate-proverkapvc-files/'
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
    return round(n, -2)

def round502(n):
    if str(n)=='':
        return ''
    return round(float(str(n).replace(',','.')), -2)

def round503(n):
    return round(n * 2, -2) // 2


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def create_online(request,id):
    file = OnlineSavdoFile.objects.get(id=id).file
    df = pd.read_excel(f'{MEDIA_ROOT}/{file}',sheet_name='Характеристика',header=4)
    df = df[~df['Название системы'].isnull()]
    df =df.astype(str)

    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M")

    parent_dir =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\'
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads\\','online_savdo_pvc')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\',hour)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\','ONLINE')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\',minut)

    pathtext1 =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\teams.xlsx'


    

    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for key,row in df.iterrows():
        data[0].append(row["Название"])
        data[1].append(row["SAP Код вручную (вставится вручную)"])
        data[2].append(row["Группа"])
        data[3].append(row["Цвет продукта"])
        data[4].append(row["Группа закупок"])
        data[5].append(row["Сегмент"])
        data[6].append(row["Бухгалтерский товары"])
        data[7].append("Килограмм")
        data[8].append("Штука")
        data[9].append("Килограмм")
        data[10].append(1)

        data[11].append(row["Общий вес (КГ) за штуку"])
        data[12].append("Пассивный")
        data[13].append(row["Завод"])
        data[14].append(row["Online savdo ID"])
   
    new_row = {'ID' :data[14], 'NAME':data[0], 'SAPCODE':data[1],'GROUPNAME':data[2],'COLOR':data[3],'PURCHASING GROUP':data[4],'SEGMENT':data[5],'BUGALTER NAME':data[6],'BUGALTER UNIT':data[7],'BASE UNIT':data[8],'ALTER UNIT':data[9],'BASE UNITVAL':data[10],'ALTER UNITVAL':data[11],'STATUS':data[12],'FACTORY':data[13]}
    CS = pd.DataFrame(new_row)
    CS = CS.replace('nan','')
    CS.to_excel(pathtext1,index=False)
    files = [FileG(file=pathtext1,filetype='obichniy')]
    context ={
        'files':files
    }
    return render(request,'universal/generated_files.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def sozdaniya_online_savdo(request,id):
    order = OnlineSavdoOrder.objects.get(id = id)
    path1 = order.paths['path_1']
    path2 = order.paths['path_2']
    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Характеристика',header= 4)
    df1 = df1[~df1['Название системы'].isnull()]
    base = pd.read_excel(f'{MEDIA_ROOT}/{path2}',sheet_name='Sheet1',header= 2)
    # df1 = df1.astype(str)

    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M")

    parent_dir =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\'
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads\\','online_savdo_pvc')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\',hour)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\','ONLINE')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\',minut)

    pathtext1 =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\teams3.xlsx'





    data =[[],[],[],[],[],[],[],[]] 
    PriceUSD = int(ExchangeValues.objects.get(id = 1).valute)
    for key2,row2 in df1.iterrows():
        result = base[base['name'] ==row2['Название'] ]
        data[0].append(result.iloc[0]['id'])
        data[1].append(result.iloc[0]['name'])
        data[2].append(row2['Тип клиента'])
        data[3].append("14.08.2023")
        # data[3].append(datetime(day=14,month=8,year=2023))
        data[4].append(round50(float(row2['Цена с НДС'])/1.12))
        data[5].append(round50(row2['Цена с НДС']))
        data[6].append("UZS")
        data[7].append(row2['Базовый единица'])



    new_row = {'ID' :data[0], 'NAME':data[1], 'CLIENTYPE':data[2],'DATE':data[3],'COST':data[4],'RATE':data[5],'CURRENCY':data[6],'UNIT':data[7]}

    new_df =pd.DataFrame(new_row)
    new_df['DATE'] =pd.to_datetime(new_df.DATE) 
    new_df['DATE'] = new_df['DATE'].apply(lambda x: x.strftime('%d/%m/%Y'))

    new_df.to_excel(pathtext1,index=False)


    files = [FileG(file=pathtext1,filetype='obichniy')]
    context ={
        'files':files
    }
    return render(request,'universal/generated_files.html',context)



BUXPRICE = {
    'Профиль из ПВХ ламинированный':42896,
    'Подоконник из ПВХ ламинированный':27104,
    'Термоуплотненный окрашенный алюминиевый профиль':60592,
    'Анодированный алюминиевый профиль (N)':58800,
    'Профиль из ПВХ':22624,
    'Алюминиевый профиль':55216,
    'Неокрашенный алюминиевый профиль (N)':51296,
    'Алюминиевый профиль (N)':54544,
    'Термоуплотненный анодированный алюминиевый профиль (N)':63056,
    'Профиль ПВХ с уплотнителем':26432,
    'Ламинированный термоуплотненный алюминиевый профиль':72912,
    'Ламинированный алюминиевый профиль':71792,
    'Профиль из ПВХ ламинированный с уплотнителем':57456,
    'Ламинированный термоуплотненный алюминиевый профиль (N)':72912,
    'Алюминиевый профиль с декоративным покрытием  (N)':60480,
    'Алюминиевый профиль с декоративным покрытием':59360,
    'Профиль из ПВХ ламинированный (Engelberg)':45248,
    'Термоуплотненный алюминиевый профиль (N)':59920,
    'Неокрашенный алюминиевый профиль':44576,
    'Мебельный профиль из алюминия анодированный матовое серебро (N)':52528,
    'Подоконник из ПВХ':15792,
    'Ламбри из ПВХ ламинированный':36960,
    'Профиль из ПВХ (Engelberg)':38080,
    'Ламинированный алюминиевый профиль (N)':72912,
    'Ламбри из ПВХ':14672,
    'Дистанционная рамка ':70112,
    'Металлический усилитель':16688,
    'Уплотнитель для алюминиевых и ПВХ профилей':16576,

}
Segment1 = {
    'nan':"",
    'Аксессуар':0.065,
    'Стандарт':0.037,
    'Премиум':0.08,
    'Aldoks':0.037,
    'Эконом':0.037,
    'Mebel':0.03,
    'RETPEN 8-10%':0,
    'RETPEN 10-12%':0,
    'RETPEN 17%':0
}
Segment2 = {
    'nan':"",
    'Аксессуар':0.07,
    'Стандарт':0.047,
    'Премиум':0.08,
    'Aldoks':0.047,
    'Эконом':0.047,
    'Mebel':0.03,
    'RETPEN 8-10%':0,
    'RETPEN 10-12%':0,
    'RETPEN 17%':0
}
Segment3 = {
    'nan':"",
    'Аксессуар':0.07,
    'Стандарт':0.047,
    'Премиум':0.08,
    'Aldoks':0.047,
    'Эконом':0.047,
    'Mebel':0.03,
    'RETPEN 8-10%':0,
    'RETPEN 10-12%':0,
    'RETPEN 17%':0
}
Segment4 = {
    'nan':"",
    'Aldoks':0.05,
    'RETPEN 8-10%':0.08,
    'RETPEN 10-12%':0.1,
    'RETPEN 17%':0.17,
    'Премиум':0,
    'Стандарт':0,
    'Эконом':0,
    'Mebel':0
}
Segment5 = {
    'nan':"",
    'Aldoks':0.05,
    'RETPEN 8-10%':0.1,
    'RETPEN 10-12%':0.12,
    'RETPEN 17%':0.17,
    'Премиум':0,
    'Стандарт':0,
    'Эконом':0,
    'Mebel':0
}
Segment6 = {
    'nan':"",
    'Аксессуар':0.07,
    'Стандарт':0.047,
    'Премиум':0.08,
    'Aldoks':0.047,
    'Эконом':0.047,
    'RETPEN 8-10%':0,
    'RETPEN 10-12%':0,
    'RETPEN 17%':0,
    'Mebel':0
}
zavod = {
    'ZAVOD ALUMIN':'1100',
    'ZAVOD ALUMIN NAVOIY':'1200',
    'ZAVOD PVS NAVOIY':'1200'
}


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def sozdaniye_sena(request,id):
    order = OnlineSavdoOrder.objects.get(id = id)
    path1 = order.paths['path_1']
    path2 = order.paths['path_2']
    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Характеристика',header= 4)
    base = pd.read_excel(f'{MEDIA_ROOT}/{path2}',sheet_name='Sheet1',header= 2)
    df1 = df1[~df1['Название системы'].isnull()]

    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M")

    parent_dir =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\'
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads\\','online_savdo_pvc')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\',hour)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\','ONLINE')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\',minut)

    pathtext1 =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\teams4.xlsx'
    DATA = ExchangeValues.objects.get(id = 1).start_data
    
    base = base.astype(str)
    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for key2,row2 in df1.iterrows():
        result = base[base['name'] ==row2['Название'] ]
        data[0].append(result.iloc[0]['id'])
        data[1].append(result.iloc[0]['name'])
        data[2].append(result.iloc[0]['group'])
        data[3].append(result.iloc[0]['sapcode'])   
        data[4].append(result.iloc[0]['alternate_unit_val'])
        data[5].append(result.iloc[0]['purchasing_group'])
        data[6].append(result.iloc[0]['segment'])
        data[7].append(result.iloc[0]['accounting_goods_name'])
        data[8].append(BUXPRICE[result.iloc[0]['accounting_goods_name']])
        data[9].append(DATA)
    
        data[10].append(Segment1[result.iloc[0]['segment']])
        data[11].append(Segment2[result.iloc[0]['segment']])
        data[12].append(Segment3[result.iloc[0]['segment']])
        data[13].append(Segment4[result.iloc[0]['segment']])
        data[14].append(Segment5[result.iloc[0]['segment']])
        data[15].append(Segment6[result.iloc[0]['segment']])
        data[16].append(zavod[result.iloc[0]['factory']])
        a=0
        if result.iloc[0]['akfa']!="nan":
            a=result.iloc[0]['akfa']
        elif result.iloc[0]['imzo']!="nan":
            a=result.iloc[0]['imzo']
        elif result.iloc[0]['franchising']!="nan":
            a=result.iloc[0]['franchising']
        data[17].append(float(a))
        data[18].append(row2['Базовый единица'])
        if Segment1[result.iloc[0]['segment']]==0:
            b4=''
            c4=''
            g4=''
            v4=''
        else:
            if row2['Базовый единица']=='КГ':
                t=1
            else:
                t=float(result.iloc[0]['alternate_unit_val'])         
            b4=float(a)-float(a)*Segment1[result.iloc[0]['segment']]
            c4=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))
            g4=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))*1.12
            v4=(float(a)-float(a)*Segment1[result.iloc[0]['segment']])-(round502((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12)*1.12)
        data[19].append(b4)   
        data[20].append(c4)
        data[21].append(g4)
        data[22].append(v4)
        data[23].append("")
        if Segment2[result.iloc[0]['segment']]==0:
            b3=''
            c3=''
            g3=''
            v3=''
        else:
            if row2['Базовый единица']=='КГ':
                t=1
            else:
                t=float(result.iloc[0]['alternate_unit_val'])      
            b3=float(a)-float(a)*Segment2[result.iloc[0]['segment']]
            c3=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))
            g3=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))*1.12
            v3=(float(a)-float(a)*Segment2[result.iloc[0]['segment']])-(round502((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12)*1.12)
        data[24].append(b3)   
        data[25].append(c3)
        data[26].append(g3)
        data[27].append(v3)
        data[28].append("")
        if Segment3[result.iloc[0]['segment']]==0:
            b2=''
            c2=''
            g2=''
            v2=''
        else:
            if row2['Базовый единица']=='КГ':
                t=1
            else:
                t=float(result.iloc[0]['alternate_unit_val'])
            b2=float(a)-float(a)*Segment3[result.iloc[0]['segment']]
            c2=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))
            g2=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))*1.12
            v2=(float(a)-float(a)*Segment3[result.iloc[0]['segment']])-(round502((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12)*1.12)
        data[29].append(b2)   
        data[30].append(c2)
        data[31].append(g2)
        data[32].append(v2)
        data[33].append("")
        
        if Segment4[result.iloc[0]['segment']]==0:
            b=''
            c=''
            g=''
            v=''
        else:
            if row2['Базовый единица']=='КГ':
                t=1
            else:
                t=float(result.iloc[0]['alternate_unit_val'])
            b=float(a)-float(a)*Segment4[result.iloc[0]['segment']]
            c=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))
            g=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))*1.12
            v=(float(a)-float(a)*Segment4[result.iloc[0]['segment']])-(round502((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12)*1.12)
        data[34].append(b)   
        data[35].append(c)
        data[36].append(g)
        data[37].append(v)
        data[38].append("")
        if Segment5[result.iloc[0]['segment']]==0:
            b1=''
            c1=''
            g1=''
            v1=''
        else:
            if row2['Базовый единица']=='КГ':
                t=1
            else:
                t=float(result.iloc[0]['alternate_unit_val'])
            b1=float(a)-float(a)*Segment5[result.iloc[0]['segment']]
            c1=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))
            g1=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))*1.12
            v1=(float(a)-float(a)*Segment5[result.iloc[0]['segment']])-(round502((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12)*1.12)
        data[39].append(b1)   
        data[40].append(c1)
        data[41].append(g1)
        data[42].append(v1)
        data[43].append("")
        if Segment6[result.iloc[0]['segment']]==0:
            b5=''
            c5=''
            g5=''
            v5=''
        else:
            if row2['Базовый единица']=='КГ':
                t=1
            else:
                t=float(result.iloc[0]['alternate_unit_val'])
            b5=float(a)-float(a)*Segment6[result.iloc[0]['segment']]
            c5=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))
            g5=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))*1.12
            v5=(float(a)-float(a)*Segment6[result.iloc[0]['segment']])-(round502((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12)*1.12)
        data[44].append(b5)   
        data[45].append(c5)
        data[46].append(g5)
        data[47].append(v5)
        

    new_row = {'id':data[0],
            'name':data[1],	
            'group':data[2],	
            'sapcode':data[3],	
            'alternate_unit_val':data[4],	
            'purchasing_group':data[5],	
            'segment':data[6],	
            'accounting_goods_name':data[7],	
            'цена с ндс':data[8],	
            'Дата':data[9],	
            'Shaxar diler uchun narx segmentli (Angren+Bekobod+Chirchiq)':data[10],
            'Shaxar diler (Yangiyul,Olmaliq,Guliston,Bo`ka) uchun narx segmentli':data[11],	
            'Viloyat diler uchun narx segmentli':data[12],	
            'Retpen diler (Nukus (Maxmud), Xorazm (Shixnazar),Namangan-1 ,Farg`ona (Shuhrat Aka),Andijon-3 (Azizbek) uchun narx segmentli':data[13],	
            'Retpen diler uchun narx segmentli':data[14],	
            'Imzo/Franshiza diler uchun narx segmentli':data[15],	
            'Сбытовая организация':data[16],	
            'akfa':data[17],	
            'Ед.изм':data[18],	
            'Shaxar diler uchun narx segmentli D1':data[19],	
            '70% без ндс безнал (цена для выгрузуа SAP) D1':data[20],	
            '70% с ндс безнал ( 12% ндс плюсуются после деблокирование сч/ф ) D1':data[21],	
            '30% Наличка D1':data[22],	
            'D1':data[23],	
            'Shaxar diler (Yangiyul,Olmaliq,Angren,Guliston,Bekobod,Bo`ka,Chirchiq) uchun narx segmentli D2':data[24],	
            '70% без ндс безнал (цена для выгрузуа SAP) D2':data[25],	
            '70% с ндс безнал ( 12% ндс плюсуются после деблокирование сч/ф ) D2':data[26],	
            '30% Наличка D2':data[27],	
            'D2':data[28],	
            'Viloyat diler uchun narx segmentli D3':data[29],	
            '70% без ндс безнал (цена для выгрузуа SAP) D3':data[30],	
            '70% с ндс безнал ( 12% ндс плюсуются после деблокирование сч/ф ) D3':data[31],
            '30% Наличка D3':data[32],	
            'D3':data[33],
            'Retpen diler (Nukus (Maxmud), Xorazm (Shixnazar),Namangan-1 ,Farg`ona (Shuhrat Aka),Andijon-3 (Azizbek) uchun narx segmentli D4':data[34],
            '70% без ндс безнал (цена для выгрузуа SAP) D4':data[35],	
            '70% с ндс безнал ( 12% ндс плюсуются после деблокирование сч/ф ) D4':data[36],	
            '30% Наличка D4':data[37],	
            'D4':data[38],	
            'Retpen diler uchun narx segmentli D5':data[39],	
            '70% без ндс безнал (цена для выгрузуа SAP) D5':data[40],	
            '70% с ндс безнал ( 12% ндс плюсуются после деблокирование сч/ф ) D5':data[41],	
            '30% Наличка D5':data[42],	
            'D5':data[43],	
            'Imzo/Franshiza diler uchun narx segmentli D6':data[44],	
            '70% без ндс безнал (цена для выгрузуа SAP) D6':data[45],	
            '70% с ндс безнал ( 12% ндс плюсуются после деблокирование сч/ф ) D6':data[46],	
            '30% Наличка D6':data[47]
    }

    new_df =pd.DataFrame(new_row)
    new_df =new_df.replace(0,'')
    

    new_df.to_excel(pathtext1,index=False)

    files = [FileG(file=pathtext1,filetype='obichniy')]
    context ={
        'files':files
    }
    return render(request,'universal/generated_files.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def sozdaniye_sap_format_sena(request,id):
    order = OnlineSavdoOrder.objects.get(id = id)
    path1 = order.paths['path_1']

    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)

    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M%S")

    parent_dir =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\'
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads\\','online_savdo_pvc')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\',hour)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\','ONLINE')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\',minut)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}','FORMAT')

    pathtext1 =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT\\VK_11_1vid torg dokument ZORN 1.xlsx'
    pathtext2 =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT\\VK_11_1vid torg dokument ZREN 1.xlsx'
    pathtext3 =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT\\VK_11_3beznal tayyor 1.xlsx'
    pathtext4 =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT\\VK_11_2prichina zakaza (ZUU) tayyor 1.xlsx'
    pathtext5 =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT\\VK_11zfdn (ALUMIN) tayyor 1 ZFKN.xlsx'
    pathtext6 =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT\\VK_11zfdn (ALUMIN) tayyor 1.xlsx'
    pathzip =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT'
    
    exchange_val = ExchangeValues.objects.get(id = 1)
    DATAB = exchange_val.start_data
    DATBI = exchange_val.end_data

    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(1,8):
        for key2,row2 in df1.iterrows():
            d='D'+str(i)
            data[0].append("PR00")
            data[1].append(row2["Сбытовая организация"])
            data[2].append("")
            data[3].append("10")
            data[4].append(d)
            data[5].append(row2["sapcode"])
            if i==1:
                k=row2["Shaxar diler uchun narx segmentli D1"]
            elif i==2:
                k=row2["Shaxar diler (Yangiyul,Olmaliq,Angren,Guliston,Bekobod,Bo`ka,Chirchiq) uchun narx segmentli D2"]
            elif i==3:
                k=row2["Viloyat diler uchun narx segmentli D3"]
            elif i==4:
                k=row2["Retpen diler (Nukus (Maxmud), Xorazm (Shixnazar),Namangan-1 ,Farg`ona (Shuhrat Aka),Andijon-3 (Azizbek) uchun narx segmentli D4"]
            elif i==5:
                k=row2["Retpen diler uchun narx segmentli D5"]
            elif i==6:
                k=row2["Imzo/Franshiza diler uchun narx segmentli D6"]
            elif i==7:
                k=row2["Imzo/Franshiza diler uchun narx segmentli D6"]
            data[6].append(k)
            data[7].append("UZS")
            data[8].append(1)
            data[9].append(row2["Ед.изм"])
            data[10].append(DATAB)
            data[11].append(DATBI)
            data[12].append("")
            data[13].append("")
            data[14].append("ZORN")
            data[15].append("")
    new_row = { 'KSCHL':data[0],	
                'VKORG':data[1],	
                'WERKS':data[2],	
                'VTWEG':data[3],	
                'KONDA':data[4],	
                'MATNR':data[5],	
                'KBETR':data[6],	
                'KONWA':data[7],	
                'KPEIN':data[8],	
                'KMEIN':data[9],	
                'DATAB':data[10],	
                'DATBI':data[11],	
                'KUNNR':data[12],	
                'FKART':data[13],	
                'AUART':data[14],	
                'AUGRU':data[15]
            }

    new_df =pd.DataFrame(new_row)

    new_df =new_df[~pd.isna(new_df['KBETR'])]


    new_df.to_excel(pathtext1,index=False)



    #####################2 excell#################
    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)

    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(1,8):
        for key2,row2 in df1.iterrows():
            d='D'+str(i)
            data[0].append("PR00")
            data[1].append(row2["Сбытовая организация"])
            data[2].append("")
            data[3].append("10")
            data[4].append(d)
            data[5].append(row2["sapcode"])
            if i==1:
                k=row2["Shaxar diler uchun narx segmentli D1"]
            elif i==2:
                k=row2["Shaxar diler (Yangiyul,Olmaliq,Angren,Guliston,Bekobod,Bo`ka,Chirchiq) uchun narx segmentli D2"]
            elif i==3:
                k=row2["Viloyat diler uchun narx segmentli D3"]
            elif i==4:
                k=row2["Retpen diler (Nukus (Maxmud), Xorazm (Shixnazar),Namangan-1 ,Farg`ona (Shuhrat Aka),Andijon-3 (Azizbek) uchun narx segmentli D4"]
            elif i==5:
                k=row2["Retpen diler uchun narx segmentli D5"]
            elif i==6:
                k=row2["Imzo/Franshiza diler uchun narx segmentli D6"]
            elif i==7:
                k=row2["Imzo/Franshiza diler uchun narx segmentli D6"]
            data[6].append(k)
            data[7].append("UZS")
            data[8].append(1)
            data[9].append(row2["Ед.изм"])
            data[10].append(DATAB)
            data[11].append(DATBI)
            data[12].append("")
            data[13].append("")
            data[14].append("ZREN")
            data[15].append("")
        
    new_row = {'KSCHL':data[0],	
            'VKORG':data[1],	
            'WERKS':data[2],	
            'VTWEG':data[3],	
            'KONDA':data[4],	
            'MATNR':data[5],	
            'KBETR':data[6],	
            'KONWA':data[7],	
            'KPEIN':data[8],	
            'KMEIN':data[9],	
            'DATAB':data[10],	
            'DATBI':data[11],	
            'KUNNR':data[12],	
            'FKART':data[13],	
            'AUART':data[14],	
            'AUGRU':data[15]
    }

    new_df =pd.DataFrame(new_row)
    new_df =new_df[~pd.isna(new_df['KBETR'])]
    new_df.to_excel(pathtext2,index=False)

    ###################### 3 ######################

    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)


    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(1,8):
        for key2,row2 in df1.iterrows():
            d='D'+str(i)
            data[0].append("PR00")
            data[1].append(row2["Сбытовая организация"])
            data[2].append("")
            data[3].append("10")
            data[4].append(d)
            data[5].append(row2["sapcode"])
            if i==1:
                k=row2["Shaxar diler uchun narx segmentli D1"]
            elif i==2:
                k=row2["Shaxar diler (Yangiyul,Olmaliq,Angren,Guliston,Bekobod,Bo`ka,Chirchiq) uchun narx segmentli D2"]
            elif i==3:
                k=row2["Viloyat diler uchun narx segmentli D3"]
            elif i==4:
                k=row2["Retpen diler (Nukus (Maxmud), Xorazm (Shixnazar),Namangan-1 ,Farg`ona (Shuhrat Aka),Andijon-3 (Azizbek) uchun narx segmentli D4"]
            elif i==5:
                k=row2["Retpen diler uchun narx segmentli D5"]
            elif i==6:
                k=row2["Imzo/Franshiza diler uchun narx segmentli D6"]
            elif i==7:
                k=row2["Imzo/Franshiza diler uchun narx segmentli D6"]
            data[6].append(k)
            data[7].append("UZS")
            data[8].append(1)
            data[9].append(row2["Ед.изм"])
            data[10].append(DATAB)
            data[11].append(DATBI)
            data[12].append("")
            data[13].append("")
            data[14].append("")
            data[15].append("")
        
    new_row = {'KSCHL':data[0],	
            'VKORG':data[1],	
            'WERKS':data[2],	
            'VTWEG':data[3],	
            'KONDA':data[4],	
            'MATNR':data[5],	
            'KBETR':data[6],	
            'KONWA':data[7],	
            'KPEIN':data[8],	
            'KMEIN':data[9],	
            'DATAB':data[10],	
            'DATBI':data[11],	
            'KUNNR':data[12],	
            'FKART':data[13],	
            'AUART':data[14],	
            'AUGRU':data[15]
    }


    new_df =pd.DataFrame(new_row)
    new_df =new_df[~pd.isna(new_df['KBETR'])]
    new_df.to_excel(pathtext3,index=False)

    ############## 4 ##########################

    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)


    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(1,8):
        for key2,row2 in df1.iterrows():
            d='D'+str(i)
            data[0].append("PR00")
            data[1].append(row2["Сбытовая организация"])
            data[2].append("")
            data[3].append("10")
            data[4].append(d)
            data[5].append(row2["sapcode"])
            if i==1:
                k=row2["70% без ндс безнал (цена для выгрузуа SAP) D1"]
            elif i==2:
                k=row2["70% без ндс безнал (цена для выгрузуа SAP) D2"]
            elif i==3:
                k=row2["70% без ндс безнал (цена для выгрузуа SAP) D3"]
            elif i==4:
                k=row2["70% без ндс безнал (цена для выгрузуа SAP) D4"]
            elif i==5:
                k=row2["70% без ндс безнал (цена для выгрузуа SAP) D5"]
            elif i==6:
                k=row2["70% без ндс безнал (цена для выгрузуа SAP) D6"]
            elif i==7:
                k=row2["70% без ндс безнал (цена для выгрузуа SAP) D6"]
            data[6].append(k)
            data[7].append("UZS")
            data[8].append(1)
            data[9].append(row2["Ед.изм"])
            data[10].append(DATAB)
            data[11].append(DATBI)
            data[12].append("")
            data[13].append("")
            data[14].append("")
            data[15].append("ZUU")
        
    new_row = {'KSCHL':data[0],	
            'VKORG':data[1],	
            'WERKS':data[2],	
            'VTWEG':data[3],	
            'KONDA':data[4],	
            'MATNR':data[5],	
            'KBETR':data[6],	
            'KONWA':data[7],	
            'KPEIN':data[8],	
            'KMEIN':data[9],	
            'DATAB':data[10],	
            'DATBI':data[11],	
            'KUNNR':data[12],	
            'FKART':data[13],	
            'AUART':data[14],	
            'AUGRU':data[15]
    }

    new_df =pd.DataFrame(new_row)
    new_df =new_df[~pd.isna(new_df['KBETR'])]

    new_df.to_excel(pathtext4,index=False)

    ################ 5 #######################

    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)


    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(1,8):
        for key2,row2 in df1.iterrows():
            d='D'+str(i)
            data[0].append("PR00")
            data[1].append(row2["Сбытовая организация"])
            data[2].append("")
            data[3].append("10")
            data[4].append(d)
            data[5].append(row2["sapcode"])
            if i==1:
                k=row2["30% Наличка D1"]
            elif i==2:
                k=row2["30% Наличка D2"]
            elif i==3:
                k=row2["30% Наличка D3"]
            elif i==4:
                k=row2["30% Наличка D4"]
            elif i==5:
                k=row2["30% Наличка D5"]
            elif i==6:
                k=row2["30% Наличка D6"]
            elif i==7:
                k=row2["30% Наличка D6"]
            data[6].append(k)
            data[7].append("UZS")
            data[8].append(1)
            data[9].append(row2["Ед.изм"])
            data[10].append(DATAB)
            data[11].append(DATBI)
            data[12].append("")
            data[13].append("ZFKN")
            data[14].append("")
            data[15].append("")
        
    new_row = {'KSCHL':data[0],	
            'VKORG':data[1],	
            'WERKS':data[2],	
            'VTWEG':data[3],	
            'KONDA':data[4],	
            'MATNR':data[5],	
            'KBETR':data[6],	
            'KONWA':data[7],	
            'KPEIN':data[8],	
            'KMEIN':data[9],	
            'DATAB':data[10],	
            'DATBI':data[11],	
            'KUNNR':data[12],	
            'FKART':data[13],	
            'AUART':data[14],	
            'AUGRU':data[15]
    }


    new_df =pd.DataFrame(new_row)
    new_df =new_df[~pd.isna(new_df['KBETR'])]
    new_df.to_excel(pathtext5,index=False)

    ################ 6 ###################

    
    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)


    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(1,8):
        for key2,row2 in df1.iterrows():
            d='D'+str(i)
            data[0].append("PR00")
            data[1].append(row2["Сбытовая организация"])
            data[2].append("")
            data[3].append("10")
            data[4].append(d)
            data[5].append(row2["sapcode"])
            if i==1:
                k=row2["30% Наличка D1"]
            elif i==2:
                k=row2["30% Наличка D2"]
            elif i==3:
                k=row2["30% Наличка D3"]
            elif i==4:
                k=row2["30% Наличка D4"]
            elif i==5:
                k=row2["30% Наличка D5"]
            elif i==6:
                k=row2["30% Наличка D6"]
            elif i==7:
                k=row2["30% Наличка D6"]
            data[6].append(k)
            data[7].append("UZS")
            data[8].append(1)
            data[9].append(row2["Ед.изм"])
            data[10].append(DATAB)
            data[11].append(DATBI)
            data[12].append("")
            data[13].append("ZFDN")
            data[14].append("")
            data[15].append("")
        
    new_row = {'KSCHL':data[0],	
            'VKORG':data[1],	
            'WERKS':data[2],	
            'VTWEG':data[3],	
            'KONDA':data[4],	
            'MATNR':data[5],	
            'KBETR':data[6],	
            'KONWA':data[7],	
            'KPEIN':data[8],	
            'KMEIN':data[9],	
            'DATAB':data[10],	
            'DATBI':data[11],	
            'KUNNR':data[12],	
            'FKART':data[13],	
            'AUART':data[14],	
            'AUGRU':data[15]
    }

    new_df =pd.DataFrame(new_row)
    new_df =new_df[~pd.isna(new_df['KBETR'])]

    new_df.to_excel(pathtext6,index=False)




    file_path =f'{pathzip}.zip'

    zip(pathzip, pathzip)
    

    files = [FileG(file=file_path,filetype='obichniy')]
    context ={
        'files':files
    }
    return render(request,'online_savdo/zip_file_download.html',context)
  
   
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

    parent_dir =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\'
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads\\','online_savdo_pvc')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\',hour)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\','ONLINE')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\',minut)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}','PROVERKA')

    pathtext1 =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\ZORN ERROR.xlsx'
    pathtext2 =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\БЕЗНАЛ ERROR.xlsx'
    pathtext3 =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\ZUU ERROR.xlsx'
    pathtext4 =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\ZFKN ERROR.xlsx'
    pathtext5 =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\ZFDN ERROR.xlsx'
    pathtext6 =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\ZREN ERROR.xlsx'
    pathzip =f'{MEDIA_ROOT}\\uploads\\online_savdo_pvc\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA'

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
    

    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path5}',sheet_name='Sheet1',header=0)

    to_datetime_fmt = partial(pd.to_datetime, format='%d.%m.%Y')

    df1['DATAB'] = df1['DATAB'].apply(to_datetime_fmt)
    df1 = df1.astype(str)
    df1['joined_data']= df1['VKORG'] + df1['KONDA'] + df1['MATNR'] +df1['DATAB']

    # print(df1['joined_data'])

    df2 = pd.read_excel(f'{MEDIA_ROOT}/{path6}',sheet_name='Sheet1',header=0)

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

    for key1,row1 in df1.iterrows():
        result = df2[df2['joined_data'] == row1['joined_data']]
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


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def show_list_simple_sapcodes_pvc(request):
    search =request.GET.get('search',None)
    
    if search:
        try:
            try:
               
                f_date = datetime.strptime(search,'%d-%m-%Y %H:%M')
                
                products = PVCProduct.objects.filter(
                        created_at__year =f_date.year,
                        created_at__month =f_date.month,
                        created_at__day =f_date.day,
                        created_at__hour =f_date.hour,
                        created_at__minute =f_date.minute
                ).order_by('-created_at')
            except:
                
                f_date = datetime.strptime(search,'%d-%m-%Y')
                products = PVCProduct.objects.filter(
                        created_at__year =f_date.year,
                        created_at__month =f_date.month,
                        created_at__day =f_date.day
                ).order_by('-created_at')
                  
        except:
                
                products = PVCProduct.objects.filter(
                    Q(material__icontains=search)
                    |Q(artikul__icontains=search)
                    |Q(section__icontains=search)
                    |Q(gruppa_materialov__icontains=search)
                    |Q(kratkiy_tekst_materiala__icontains=search)
                    ).order_by('-created_at')
    else:
        
        products =PVCProduct.objects.all().order_by('-created_at')
                  
    paginator = Paginator(products, 25)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)

    context ={
        'section':'PVC сапкоды',
        'products':page_obj,
        'search':search,
        'type':'simple'

    }
    return render(request,'universal/show_sapcodes.html',context)

@csrf_exempt
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def sap_code_bulk_delete(request):
    if request.method =='POST':
        ids = request.POST.get('ids',None)
        if ids:
            ids = ids.split(',')
            
            for id in ids:
                sapcode = PVCProduct.objects.get(id=id)
                if Characteristika.objects.filter(sap_code=sapcode.material).exists():
                    character =Characteristika.objects.filter(sap_code=sapcode.material).order_by('-created_at')[:1].get()
                    character.delete()
                if '-7' in sapcode.material:
                    if RazlovkaPVX.objects.filter(sapkode7 = sapcode.material).exists():
                            RazlovkaPVX.objects.get(sapkode7 = sapcode.material).delete()
                sapcode.delete()

        return JsonResponse({'msg':True})
    else:
        return JsonResponse({'msg':False})
    

    

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def create_artikul(request):
    if request.method =='POST':
        data_json = request.POST.get('data',None)
        datas = json.loads(data_json)
        for key,data in datas.items():
            # print(data)
            # # data =data[key]
            artikul_component = ArtikulKomponentPVC(
                artikul = data['artikul'],
                component=data['komponent'],
                component2=data['komponent']+'-7',
                category =data['сategoriya'],
                height =data['visota'],
                width =data['shirina'],
                product_type =data['product_type'],
                profile_type =data['tip_profiley'],
                tnved =data['tnved'],
                wms_height =data['wms_visota'],
                wms_width =data['wms_shirina'],
                nazvaniye_sistem =data['nazvaniye_system'],
                camera =data['kamera'],
                kod_k_component =data['kod_k_component'],
                iskyucheniye =data['isklyucheniye'],
                is_special =data['is_special'],
                nakleyka_nt1 =data['nakleykant1_'],

                
                )
            artikul_component.save()
            camera_pvc = CameraPvc(sap_code =data['artikul'],coun_of_lam=data['kamera_lam'],coun_of_pvc=data['kamera_pvx'])
            camera_pvc.save()

            dlinniy_text = DliniyText(sap_code =data['artikul'],product_desc=data['dlinniy_naz'])
            dlinniy_text.save()

        return JsonResponse({'status':201})
    return render(request,'pvc/create_artikul.html')



#         kamera_lam=NaN,
#         kamera_pvx=NaN,
#         dlinniy_naz=NaN

@csrf_exempt
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def edit_sapcode(request,id):
    sapcode_org = PVCProduct.objects.get(id=id)
    if request.method =='POST':
        kratkiy = request.POST.get('kratkiy')
        
       
        if RazlovkaPVX.objects.filter(
            (Q(esapkode = sapcode_org.material)&Q(ekrat = sapcode_org.kratkiy_tekst_materiala))
            |(Q(lsapkode = sapcode_org.material)&Q(lkrat = sapcode_org.kratkiy_tekst_materiala))
            |(Q(sapkode7 =sapcode_org.material )&Q(krat7=sapcode_org.kratkiy_tekst_materiala))).exists:
            # print(sapcode_org.material,sapcode_org.kratkiy_tekst_materiala)
            razlovka = RazlovkaPVX.objects.filter(
                (Q(esapkode = sapcode_org.material)&Q(ekrat = sapcode_org.kratkiy_tekst_materiala))
                |(Q(lsapkode = sapcode_org.material)&Q(lkrat = sapcode_org.kratkiy_tekst_materiala))
                |(Q(sapkode7 =sapcode_org.material )&Q(krat7=sapcode_org.kratkiy_tekst_materiala))
                )[:1].get()
            if '-E' in sapcode_org.material:
                razlovka.ekrat =kratkiy
            if '-L' in sapcode_org.material:
                razlovka.lkrat =kratkiy
            if '-7' in sapcode_org.material:
                razlovka.krat7 =kratkiy
            
            razlovka.save()
        sapcode_org.kratkiy_tekst_materiala = kratkiy
        sapcode_org.save()
        return JsonResponse({'status':201})
    else:
        context ={
            'sapcode':sapcode_org,
            'section':'PVC сапкод'
        }
        return render(request,'pvc/edit.html',context)


@csrf_exempt
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def delete_sap_code(request,id):
    if request.method =='POST':
        sapcode = PVCProduct.objects.get(id=id)
        if Characteristika.objects.filter(sap_code=sapcode.material).exists():
            character =Characteristika.objects.filter(sap_code=sapcode.material).order_by('-created_at')[:1].get()
            character.delete()
        if '-7' in sapcode.material:
            if RazlovkaPVX.objects.filter(sapkode7 = sapcode.material).exists():
                    RazlovkaPVX.objects.get(sapkode7 = sapcode.material).delete()
        sapcode.delete()

        return JsonResponse({'msg':True})
    else:
        return JsonResponse({'msg':False})
