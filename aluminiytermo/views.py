from django.shortcuts import render,redirect
from django.http import JsonResponse
import pandas as pd
from .models import AluFileTermo,AluminiyProductTermo,CharUtilsTwo,CharUtilsOne,CharUtilsThree,CharUtilsFour,CharacteristicTitle,BazaProfiley,Characteristika,CharacteristikaFile
from norma.models import NakleykaIskyuchenie,NormaExcelFiles
from aluminiy.models import AluminiyProduct,RazlovkaTermo,LengthOfProfile,ExchangeValues,Price
from .forms import FileFormTermo,FileFormChar
from aluminiy.utils import save_razlovka
from django.db.models import Count,Max
from config.settings import MEDIA_ROOT
from django.core.paginator import Paginator
from aluminiy.utils import download_bs64
import numpy as np
from .utils import fabrikatsiya_sap_kod,create_folder,create_characteristika,create_characteristika_utils,characteristika_created_txt_create,anodirovaka_check,check_for_correct,get_cretead_txt_for_1201,characteristika_created_txt_create_1301
import os
from accounts.models import User
from datetime import datetime
import json
from aluminiy.views import update_char_title_function
import random
from django.db.models import Q
from .BAZA import ANODIROVKA_CODE
from django.views.decorators.csrf import csrf_exempt
import ast
from django.contrib.auth.decorators import user_passes_test,login_required
from .create_char import product_add_second_termo,product_add_second_simple
from order.models import Order


now = datetime.now()

class SAPCODES:
      def __init__(self,material,kratkiy_tekst_materiala,created_at):
            self.material = material
            self.kratkiy_tekst_materiala = kratkiy_tekst_materiala
            self.crated_at = created_at



def get_sapcodes(request):

      if request.method =='POST':
            countt = request.POST.get('count',None)
            if countt:
                  sap_codes = {}
                  sap_codes_list = []

                  for i in range(1,int(countt) + 1):
                        sap_code =request.POST.get(f'sapcode{i}',None)
                        kratkiy_tekst =request.POST.get(f'kratkiy{i}',None)

                        if sap_code and kratkiy_tekst:
                              sap_codes[sap_code] = kratkiy_tekst
                              sap_codes_list.append(sap_code)

                  obichniy = AluminiyProduct.objects.filter(artikul__in = sap_codes_list).order_by('section').order_by('counter')
                  termo = AluminiyProductTermo.objects.filter(artikul__icontains = sap_codes_list).order_by('section').order_by('counter')
                  products =[]
                  for obich in obichniy:
                        if (obich.artikul in sap_codes) and (obich.material == sap_codes[obich.artikul]):
                              products.append(SAPCODES(material=obich.material,kratkiy_tekst_materiala=obich.kratkiy_tekst_materiala,created_at=obich.created_at))
                  termo_products =[]
                  for ter in termo:
                        if (ter.artikul in sap_codes) and (ter.material == sap_codes[ter.artikul]):
                              termo_products.append(SAPCODES(material=ter.material,kratkiy_tekst_materiala=ter.kratkiy_tekst_materiala,created_at=ter.created_at))

                  print(obichniy)
                  print(termo)
                  context ={
                        'section1':'Обычный',
                        'section2':'Термо',
                        'products':products,
                        'termo_products':termo_products
                  }
                  return render(request,'universal/sapcodes.html',context)

      return render(request,'norma/search_sapcode.html',{'section':'SAPCODE','section2':'Найти SAPCODE'})

def get_raube(request):
      raube_list =[[],[],[]]

      if request.method =='POST':
            ozmk =request.POST.get('ozmk',None)
            if ozmk:
                  ozmks = ozmk.split()
                  for ozm in ozmks:
                        if Characteristika.objects.filter(sap_code =ozm).exists():
                             
                              character = Characteristika.objects.filter(sap_code = ozm).order_by('-created_at')[:1].get()
                              
                              if character.surface_treatment.capitalize() =='Белый':
                                    raube_list[0].append('S0')
                                    raube_list[1].append(ozm)
                              elif character.surface_treatment.capitalize() =='Неокрашенный':
                                    raube_list[0].append('S1')
                                    raube_list[1].append(ozm)
                              elif character.surface_treatment.capitalize() =='Окрашенный':
                                    raube_list[0].append('S2')
                                    raube_list[1].append(ozm)
                              elif character.surface_treatment.capitalize() =='Сублимированный':
                                    raube_list[0].append('S3')
                                    raube_list[1].append(ozm)
                              elif character.surface_treatment.capitalize() =='Ламинированный':
                                    raube_list[0].append('S4')
                                    raube_list[1].append(ozm)
                        else:
                              raube_list[2].append(ozm)
                              
            return JsonResponse({'sap_code':raube_list[1],'raube':raube_list[0],'Does not exists':raube_list[2]})
      else:
            return render(request,'norma/character_find.html',{'section':'RAUBE','section2':'Найти RAUBE'})


def create_txt_for_1101(request):
      
      if request.method =='POST':
            sap_codes = request.POST.get('ozmk',None)
            esap_codes = request.POST.get('eozmk',None)

            if sap_codes:
                  character_dict ={}
                  character_dict['SAP код S4P 100']=[]
                  character_dict['ch_export_description']=[]
                  character_dict['ch_export_description_eng']=[]
                  character_dict['Тип покрытия']=[]
                  character_dict['Участок']=[]
                  character_dict['Короткое название SAP']=[]
                  character_dict['Общий вес за штуку']=[]
                  character_dict['ch_combination']=[]
                  character_dict['Price']=[]
                  character_dict['Польное наименование SAP']=[]
                  character_dict['ch_rawmat_type']=[]
                  character_dict['ch_article']=[]
                  character_dict['ch_tnved']=[]
                  character_dict['ch_outer_side_pc_id']=[]
                  character_dict['ch_outer_side_pc_brand']=[]
                  character_dict['ch_inner_side_pc_id']=[]
                  character_dict['ch_inner_side_pc_brand']=[]
                  character_dict['ch_outer_side_wg_s_id']=[]
                  character_dict['ch_inner_side_wg_s_id']=[]
                  character_dict['ch_outer_side_wg_id']=[]
                  character_dict['ch_inner_side_wg_id']=[]
                  character_dict['ch_width']=[]
                  character_dict['ch_height']=[]
                  character_dict['ch_system']=[]
                  character_dict['ch_alloy']=[]
                  character_dict['ch_temper']=[]
                  character_dict['ch_anodization_contact']=[]
                  character_dict['ch_anodization_type']=[]
                  character_dict['ch_anodization_method']=[]
                  character_dict['ch_print_view']=[]
                  character_dict['ch_profile_base']=[]
                  character_dict['ch_category']=[]
                  character_dict['ch_surface_treatment_export']=[]
                  character_dict['ch_artikul_old']=[]
                  character_dict['Длина']=[]
                  character_dict['WMS_WIDTH']=[]
                  character_dict['WMS_HEIGHT']=[]
                  does_not_exists = []
                  if esap_codes:

                        elist =  esap_codes.split()
                  else:
                        elist = []

                  sap_codes =sap_codes.split()
                  exchange_value = ExchangeValues.objects.get(id=1)

                  for sap_code in sap_codes:
                        all_correct = True
                        if Characteristika.objects.filter(sap_code =sap_code).exists():
                              character_txt = Characteristika.objects.filter(sap_code =sap_code).order_by('-created_at')[:1].get()
                        else:
                            all_correct = False
                            does_not_exists.append([sap_code,'НЕТ ХАРАКТЕРИСТИКИ'])

                        
                        artikul = sap_code.split('-')[0]
                        if LengthOfProfile.objects.filter(artikul =artikul).exists():
                             
                              leng_of_profile_txt = LengthOfProfile.objects.filter(artikul =artikul).order_by('-created_at')[:1].get()
                        else:
                            all_correct = False
                            does_not_exists.append([artikul,'НЕТ ВЕС'])

                        if BazaProfiley.objects.filter(Q(артикул=artikul)|Q(компонент=artikul)).exists():
                              stariy_code = BazaProfiley.objects.filter(Q(артикул=artikul)|Q(компонент=artikul))[:1].get()
                        else:
                            all_correct = False
                            does_not_exists.append([artikul,'НЕТ СТАРЫЙ КОД (Baza Profiley)'])
                        
                        
                        
                        if all_correct:
                              character_dict['SAP код S4P 100'].append(sap_code)
                              character_dict['ch_export_description'].append(character_txt.export_description)
                              character_dict['ch_export_description_eng'].append(character_txt.export_description_eng)
                              character_dict['Тип покрытия'].append(character_txt.surface_treatment)
                              character_dict['Участок'].append(character_txt.section)
                              character_dict['Короткое название SAP'].append(character_txt.kratkiy_text)
                              
                              character_dict['ch_combination'].append(character_txt.combination)
                              character_dict['ch_article'].append(artikul)
                              
                              price = Price.objects.filter(tip_pokritiya = character_txt.surface_treatment.capitalize(),tip=character_txt.combination.capitalize())[:1].get()
                              pprice = float(str(price.price).replace(',','.'))

                            
                              termo_component = AluminiyProductTermo.objects.filter(material=sap_code).exists()
                              exchange_val = float( str(exchange_value.valute).replace(',','.') )

                              if termo_component:
                                    length_profile = float(str(leng_of_profile_txt.ves_za_metr).replace(',','.'))*(float(character_txt.length)/1000)
                                    character_dict['Общий вес за штуку'].append(length_profile)
                              else:
                                    length_profile = float(str(leng_of_profile_txt.ves_za_shtuk).replace(',','.'))
                                    character_dict['Общий вес за штуку'].append(leng_of_profile_txt.ves_za_shtuk)
                              price_org =  pprice * length_profile  * exchange_val
                              
                              character_dict['Price'].append(price_org)
                              

                              baza_profiey = BazaProfiley.objects.filter(Q(артикул=artikul)|Q(компонент=artikul))[:1].get()
        

                              if (('-7' in sap_code) or ('-K' in sap_code) or ('-L'  in sap_code)):
                                    component_name ='Артикул'
                              else:
                                    component_name ='Компонент'

                              польное_наименование_sap = 'Алюминиевый '+baza_profiey.product_description +', '+component_name +' '+artikul+', '+character_txt.surface_treatment+', Длина '+character_txt.length+' мм, Тип '+character_txt.alloy+'-'+character_txt.temper+' '+character_txt.print_view


                              character_dict['Польное наименование SAP'].append(польное_наименование_sap)
                              character_dict['ch_rawmat_type'].append(character_txt.rawmat_type)
                              character_dict['Длина'].append(character_txt.length)
                              character_dict['WMS_HEIGHT'].append(character_txt.wms_height)
                              character_dict['WMS_WIDTH'].append(character_txt.wms_width)
                              character_dict['ch_tnved'].append(character_txt.tnved)
                              character_dict['ch_outer_side_pc_id'].append(character_txt.outer_side_pc_id)
                              character_dict['ch_outer_side_pc_brand'].append(character_txt.outer_side_pc_brand)
                              character_dict['ch_inner_side_pc_id'].append(character_txt.inner_side_pc_id)
                              character_dict['ch_inner_side_pc_brand'].append(character_txt.inner_side_pc_brand)
                              character_dict['ch_outer_side_wg_s_id'].append(character_txt.outer_side_wg_s_id)
                              character_dict['ch_inner_side_wg_s_id'].append(character_txt.inner_side_wg_s_id)
                              character_dict['ch_outer_side_wg_id'].append(character_txt.outer_side_wg_id)
                              character_dict['ch_inner_side_wg_id'].append(character_txt.inner_side_wg_id)
                              character_dict['ch_width'].append(character_txt.width)
                              character_dict['ch_height'].append(character_txt.height)
                              character_dict['ch_system'].append(character_txt.system)
                              character_dict['ch_alloy'].append(character_txt.alloy)
                              character_dict['ch_temper'].append(character_txt.temper)
                              character_dict['ch_anodization_contact'].append(character_txt.anodization_contact)
                              character_dict['ch_anodization_type'].append(character_txt.anodization_type)
                              character_dict['ch_anodization_method'].append(character_txt.anodization_method)
                              character_dict['ch_print_view'].append(character_txt.print_view)
                              character_dict['ch_profile_base'].append(character_txt.profile_base)
                              character_dict['ch_category'].append(character_txt.category)
                              character_dict['ch_surface_treatment_export'].append(character_txt.surface_treatment_export)
                              character_dict['ch_artikul_old'].append(stariy_code.старый_код)
                        
                  df = pd.DataFrame(character_dict)
                  path = get_cretead_txt_for_1201(df,elist,does_not_exists)
                  files =[File(file=p,filetype='txt') for p in path]
                  context ={
                        'files':files,
                        'section':'Текст'
                  }
                  return render(request,'universal/generated_files.html',context)
            else:
                  return render(request,'universal/create_text.html')
     
      return render(request,'universal/create_text.html')

def show_list_simple_sapcodes(request):

      search =request.GET.get('search',None)
      if search:
            try:
                  # print(search)
                  try:
                        f_date = datetime.strptime(search,'%d-%m-%Y %H:%M')
                        products = AluminiyProductTermo.objects.filter(
                              created_at__year =f_date.year,
                              created_at__month =f_date.month,
                              created_at__day =f_date.day,
                              created_at__hour =f_date.hour,
                              created_at__minute =f_date.minute
                        )
                  except:
                        f_date = datetime.strptime(search,'%d-%m-%Y')
                        products = AluminiyProductTermo.objects.filter(
                              created_at__year =f_date.year,
                              created_at__month =f_date.month,
                              created_at__day =f_date.day
                        )
                  
            except:
                  products = AluminiyProductTermo.objects.filter(
                        Q(material__icontains=search)
                        |Q(artikul__icontains=search)
                        |Q(section__icontains=search)
                        |Q(gruppa_materialov__icontains=search)
                        |Q(kratkiy_tekst_materiala__icontains=search)
                        |Q(kombinirovanniy__icontains=search)
                        ).order_by('-created_at')
      else:
            products =AluminiyProductTermo.objects.all().order_by('-created_at')
                  
      paginator = Paginator(products, 25)

      if request.GET.get('page') != None:
            page_number = request.GET.get('page')
      else:
            page_number=1

      page_obj = paginator.get_page(page_number)

      context ={
            'section':'Термо сапкоды',
            'products':page_obj,
            'search':search,
            'type':'termo'

      }
      return render(request,'universal/show_sapcodes.html',context)




def character_extras(request):
      df = pd.read_excel('C:\\OSPanel\\domains\\char.xlsx','Лист1')
      for key, row in df.iterrows():
            character = Characteristika(
            sap_code =row['Материал'],
            kratkiy_text =row['Краткий текст материала'],
            section ='',
            savdo_id ='',
            savdo_name ='',
            export_customer_id = row['EXPORT_CUSTOMER_ID'],
            system = row['SYSTEM'],
            article = row['ARTICLE'],
            length = row['LENGTH'],
            surface_treatment = row['SURFACE_TREATMENT'],
            alloy = row['ALLOY'],
            temper = row['TEMPER'],
            combination = row['COMBINATION'],
            outer_side_pc_id = row['OUTER_SIDE_PC_ID'],
            outer_side_pc_brand = row['OUTER_SIDE_PC_BRAND'],
            inner_side_pc_id = row['INNER_SIDE_PC_ID'],
            inner_side_pc_brand = row['INNER_SIDE_PC_BRAND'],
            outer_side_wg_s_id = row['OUTER_SIDE_WG_S_ID'],
            inner_side_wg_s_id = row['INNER_SIDE_WG_S_ID'],
            outer_side_wg_id = row['OUTER_SIDE_WG_ID'],
            inner_side_wg_id = row['INNER_SIDE_WG_ID'],
            anodization_contact = row['ANODIZATION_CONTACT'],
            anodization_type = row['ANODIZATION_TYPE'],
            anodization_method = row['ANODIZATION_METHOD'],
            print_view = row['PRINT_VIEW'],
            profile_base = row['PROFILE_BASE'],
            width = row['WIDTH'],
            height = row['HEIGHT'],
            category = row['CATEGORY'],
            rawmat_type = row['MATERIAL_CLASS'],
            benkam_id = '',
            hollow_and_solid = '',
            export_description = '',
            export_description_eng = '',
            tnved = '',
            surface_treatment_export = row['SURFACE_TREATMENT_EXPORT'],
            wms_width = '',
            wms_height = '',
            group_prise = '',
            )
            character.save()
      return JsonResponse({'a':'b'})
      

def downloading_characteristika(request):
      simple_list = Characteristika.objects.all().values_list('sap_code','kratkiy_text','section','savdo_id','savdo_name','export_customer_id','system','article','length','surface_treatment','alloy','temper','combination','outer_side_pc_id','outer_side_pc_brand','inner_side_pc_id','inner_side_pc_brand','outer_side_wg_s_id','inner_side_wg_s_id','outer_side_wg_id','inner_side_wg_id','anodization_contact','anodization_type','anodization_method','print_view','profile_base','width','height','category','rawmat_type','benkam_id','hollow_and_solid','export_description','export_description_eng','tnved','surface_treatment_export','wms_width','wms_height','group_prise')
      data = pd.DataFrame(np.array(list(simple_list)),columns=['SAP CODE','KRATKIY TEXT','SECTION','SAVDO_ID','SAVDO_NAME','EXPORT_CUSTOMER_ID','SYSTEM','ARTICLE','LENGTH','SURFACE_TREATMENT','ALLOY','TEMPER','COMBINATION','OUTER_SIDE_PC_ID','OUTER_SIDE_PC_BRAND','INNER_SIDE_PC_ID','INNER_SIDE_PC_BRAND','OUTER_SIDE_WG_S_ID','INNER_SIDE_WG_S_ID','OUTER_SIDE_WG_ID','INNER_SIDE_WG_ID','ANODIZATION_CONTACT','ANODIZATION_TYPE','ANODIZATION_METHOD','PRINT_VIEW','PROFILE_BASE','WIDTH','HEIGHT','CATEGORY','RAWMAT_TYPE','BENKAM_ID','HOLLOW AND SOLID','EXPORT_DESCRIPTION','EXPORT_DESCRIPTION ENG','TNVED','SURFACE_TREATMENT_EXPORT','WMS_WIDTH','WMS_HEIGHT','GROUP PRIZE'])
      data = data.replace('nan','')
      res = download_bs64([data,],'CHARACTERISTIKA')
      return res



def  create_characteristika_force(request,id):
      termo =request.GET.get('termo',None)
      if termo:
            product_add_second_termo(id)
      else:
            product_add_second_simple(id)
      return redirect('home')

# Create your views here.
def index(request):
      return render(request,'aluminiy/index.html')



def aluminiy_productbases(request):
      df = pd.read_excel('c:\\OpenServer\\domains\\База термо.XLSX','Лист1')
      print(df.shape)
      #   print(df['Материал'][0])
      #   print(df['Материал'][39705])

      for i in range(0,df.shape[0]):
            material =df['Материал'][i] 
            artikul =df['Ариткул'][i]
            section =df['Передел'][i]
            counter =df['Счетчик'][i]
            gruppa_materialov =df['Группа материалов'][i]
            kratkiy_tekst_materiala=df['Краткий текст материала'][i]
            kombinirovanniy=df['Комбинирования'][i]

            artiku_comp = AluminiyProductTermo(
            material =material,
            artikul =artikul,
            section =section,
            counter =counter,
            gruppa_materialov =gruppa_materialov,
            kratkiy_tekst_materiala =kratkiy_tekst_materiala,
            kombinirovanniy =kombinirovanniy
                  )
            artiku_comp.save()

      return JsonResponse({'converted':'a'})

def alu_product_base(request):
      df = pd.read_excel('C:\\OpenServer\\domains\\Aluminiy_baza.xlsx','Лист1') 
      for i in range(0,13197):
            ekstruziya_sap_kod =df['Экструзия сап код'][i]
            ekstruziya_kratkiy_tekst =df['Экструзия краткий текст'][i]
            zakalka_sap_kod =df['Закалка сап код'][i]
            zakalka_kratkiy_tekst =df['Закалка краткий текст'][i]
            pokraska_sap_kod =df['Покраска сап код'][i]
            pokraska_kratkiy_tekst =df['Покраска краткий текст'][i]
            sublimatsiya_sap_kod =df['Сублимация сап код'][i]
            sublimatsiya_kratkiy_tekst =df['Сублимация краткий текст'][i]
            anodirovka_sap_kod =df['Анодировка сап код'][i]
            anodirovka_kratkiy_tekst =df['Анодировка краткий текст'][i]
            laminatsiya_sap_kod =df['Ламинация сап код'][i]
            laminatsiya_kratkiy_tekst =df['Ламинация краткий текст'][i]
            nakleyka_sap_kod =df['Наклейка сап код'][i]
            nakleyka_kratkiy_tekst =df['Наклейка краткий текст'][i]
            upakovka_sap_kod =df['Упаковка сап код'][i]
            upakovka_kratkiy_tekst =df['Упаковка краткий текст'][i]
            fabrikatsiya_sap_kod =df['Фабрикация сап код'][i]
            fabrikatsiya_kratkiy_tekst =df['Фабрикация краткий текст'][i]
            upakovka2_sap_kod =df['Упаковка2 сап код'][i]
            upakovka2_kratkiy_tekst =df['Упаковка2 краткий текст'][i]
            
            artiku_comp =AluminiyProductBasetermo(
                  ekstruziya_sap_kod =ekstruziya_sap_kod,
                  ekstruziya_kratkiy_tekst =ekstruziya_kratkiy_tekst,
                  zakalka_sap_kod =zakalka_sap_kod,
                  zakalka_kratkiy_tekst =zakalka_kratkiy_tekst,
                  pokraska_sap_kod =pokraska_sap_kod,
                  pokraska_kratkiy_tekst =pokraska_kratkiy_tekst,
                  sublimatsiya_sap_kod =sublimatsiya_sap_kod,
                  sublimatsiya_kratkiy_tekst =sublimatsiya_kratkiy_tekst,
                  anodirovka_sap_kod =anodirovka_sap_kod,
                  anodirovka_kratkiy_tekst =anodirovka_kratkiy_tekst,
                  laminatsiya_sap_kod =laminatsiya_sap_kod,
                  laminatsiya_kratkiy_tekst =laminatsiya_kratkiy_tekst,
                  nakleyka_sap_kod =nakleyka_sap_kod,
                  nakleyka_kratkiy_tekst =nakleyka_kratkiy_tekst,
                  upakovka_sap_kod =upakovka_sap_kod,
                  upakovka_kratkiy_tekst =upakovka_kratkiy_tekst,
                  fabrikatsiya_sap_kod =fabrikatsiya_sap_kod,
                  fabrikatsiya_kratkiy_tekst =fabrikatsiya_kratkiy_tekst,
                  upakovka2_sap_kod =upakovka2_sap_kod,
                  upakovka2_kratkiy_tekst =upakovka2_kratkiy_tekst
                  )
            artiku_comp.save()
      return JsonResponse({'converted':'a'})

@login_required(login_url='/accounts/login/')
def upload_product_org(request):
      if request.method == 'POST':
            form = FileFormTermo(request.POST, request.FILES)
            if form.is_valid():
                  title = str(form.cleaned_data['file']).split('.')[0]
                  worker_id = request.POST.get('worker',None)
                  new_order = form.save()
                  if worker_id:
                        is_1101 = request.POST.get('for1101','off')
                        is_1201 = request.POST.get('for1201','off')
                        is_1112 = request.POST.get('for1112','off')
                        o_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                        
                        paths ={
                                    'termo_file':f'{MEDIA_ROOT}\\{new_order.file}',
                                    'oid':new_order.id,
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
                         
                        order = Order(title = title,owner=request.user,current_worker_id= worker_id,aluminiy_worker_id =worker_id,paths=paths,order_type =2)
                        order.save()
                  return redirect('order_detail',id=order.id)
            else:
                  form =FileFormTermo()
                  workers = User.objects.filter(role = 1)
                  print(workers)
                  context ={
                  'form':form,
                  'section':'Формирование сапкода термо',
                  'workers':workers
                  }
                  return render(request,'universal/main.html',context)
      form =FileFormTermo()
      workers = User.objects.filter(role = 1)
      context ={
      'form':form,
      'section':'Формирование сапкода термо',
      'workers':workers
      }
      return render(request,'universal/main.html',context)

@login_required(login_url='/accounts/login/')
def upload_for_char_termo(request):
      if request.method == 'POST':
            form = FileFormTermo(request.POST, request.FILES)
            if form.is_valid():
                  form.save()
                  return redirect('char_files_org_termo')
      else:
            form =FileFormTermo()
            context ={
            'form':form,
            'section':'Формирование сапкода обычный',
            }
      return render(request,'universal/main.html',context)


def char_files_org_termo(request):
  files = AluFileTermo.objects.filter(generated =False).order_by('-created_at')[:1]
  context ={'files':files,'section':'Формированный термо файлы','type':'ТЕРМО','link':'/termo/character-force/','char':True,'char_type':'termo'}
  return render(request,'universal/file_list.html',context)



def upload_for_1301(request):
      if request.method == 'POST':
            form = FileFormTermo(request.POST, request.FILES)
            if form.is_valid():
                  file_path =form.cleaned_data["file"]
                  df = pd.read_excel(file_path)
                  file_destination = characteristika_created_txt_create_1301(df)
                  files = [File(file=f,filetype='Obichniy') for f in file_destination]
                  context = {
                        'files':files,
                  }
                  return render(request,'universal/generated_file_1301.html',context)
      return render(request,'universal/main.html')

def upload_razlovka_termo(request):
      if request.method == 'POST':
            form = FileFormTermo(request.POST, request.FILES)
            if form.is_valid():
                  file_path =form.cleaned_data["file"]
                  df = pd.read_excel(file_path)
                  df = df.astype(str)
                  df = df.replace('nan','')
                  save_razlovka(df,'termo')
                  context ={
                        'msg':'Termo razlovka successfully uploaded!'
                  }
                  return render(request,'universal/upload.html',context)
      return render(request,'universal/main.html')



def upload_product_char(request):
      if request.method == 'POST':
            form = FileFormChar(request.POST, request.FILES)
            if form.is_valid():
                  text = form.save()
                  order_id = request.POST.get('order_id',None)
                  if order_id:
                        order = Order.objects.get(id = order_id)
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
                              'link':'/termo/alum/update-char-title-org/' + str(text.id) +'?order_id=' + str(order.id)
                        }
                        for key,val in paths.items():
                              context[key] = val
                        return render(request,'order/order_detail.html',context)

                  return redirect('aluminiy_files_char_org')
            else:
                  form =FileFormChar()
                  context ={
                  'form':form
                  }
      form =FileFormChar()
      context ={
      'form':form,
      'section':'Формирование характеристики',
      'link':'/termo/downloading-characteristika/'
      }
      return render(request,'universal/main.html',context)

def upload_product(request):
      if request.method == 'POST':
            form = FileFormTermo(request.POST, request.FILES)
            if form.is_valid():
                  form.save()
                  if form.cleaned_data['file_type'] =='title':
                        return redirect('aluminiy_files_termo')
                  else:
                        return redirect('aluminiy_files_termo')
            else:
                  form =FileFormTermo()
                  context ={
                  'form':form
                  }
      form =FileFormTermo()
      context ={
      'form':form
      }
      return render(request,'excel_form.html',context)

def aluminiy_files(request):
      files = AluFileTermo.objects.filter(generated =False).order_by('-created_at')
      context ={'files':files}
      return render(request,'termo/alu_file_list.html',context)

def aluminiy_files_org(request):
      files = AluFileTermo.objects.filter(generated =False).order_by('-created_at')
      context ={'files':files,'section':'Формированный термо файлы','type':'TERMO','link':'/termo/alumtermo/add/'}
      return render(request,'universal/file_list.html',context)

def aluminiy_files_char_org(request):
      files = CharacteristikaFile.objects.all().order_by('-created_at')
      text =str(files[0].file).split('/')[-1]
      if 'termo' in text.lower():
            file_type ='termo'
      else:
            file_type ='alu'
      context ={'files':files,'section':'Формированный характеристика файлы','type':'характеристики','link':f'/{file_type}/alum/update-char-title-org/'}
      return render(request,'universal/file_list.html',context)

def aluminiy_files_termo_char_title(request):
      files = AluFileTermo.objects.filter(file_type ='title')
      context ={'files':files}
      return render(request,'termo/alu_file_list_char_title.html',context)

def aluminiy_group(request):
      aluminiy_group =AluminiyProductTermo.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
      #   print(aluminiy_group)
      umumiy={}
      for al in aluminiy_group:    
            # product ={}
            # product['section']=al['section']
            # product['section_max']=al['total_max']
            # product['artikul']=al['artikul']
            umumiy[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      print('aa   ')
      return JsonResponse({'data':umumiy})
import glob
def razlovkatermo_save(request):
      
      dir_path = f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\**\*alumin*.*'
      path_list_iyun =[]
      path_list_may =[]
      path_list_aprel =[]
      for file in glob.glob(dir_path, recursive=True):
            if 'June' in file:
                  path_list_iyun.append(file)
            if 'April' in file:
                  path_list_aprel.append(file)
            if 'May' in file:
                  path_list_may.append(file)
            
     
      path_list_iyun.sort()
      iyun = path_list_iyun[::-1]
      path_list_aprel.sort()
      aprel =path_list_aprel[::-1]
      path_list_may.sort()
      may =path_list_may[::-1]

      for path1 in iyun:
            if 'Копия' in path1:
                  continue
            if 'copy' in path1:
                  continue
            print(path1)
            razlovka_yoq = True
            try:
                  df_new = pd.read_excel(path1,sheet_name=['Schotchik','Characteristika','title'])
                  schot_name ='Schotchik'
                  ch_name ='Characteristika'
            except:
                  df_new = pd.read_excel(path1,sheet_name=['schotchik','characteristika','title'])
                  schot_name ='schotchik'
                  ch_name ='characteristika'
            
            df_new[schot_name] =df_new[schot_name].astype(str)
            df_new[ch_name] =df_new[ch_name].astype(str)
            df_new['title'] =df_new['title'].astype(str)
            df_new[schot_name]=df_new[schot_name].replace('nan','')
            df_new[ch_name]=df_new[ch_name].replace('nan','')
            df_new['title']=df_new['title'].replace('nan','')
            
            try:
                  df_new[schot_name]['SAP код E']=df_new[schot_name]['SAP код E']
                  esap ='SAP код E'
                  ekrat ='Экструзия холодная резка'
                  zsap ='SAP код Z'
                  zkrat ='Печь старения'
                  psap ='SAP код P'
                  pkrat ='Покраска автомат'
                  ssap ='SAP код S'
                  skrat ='Сублимация'
                  asap ='SAP код A'
                  akrat ='Анодировка'
                  ksap ='SAP код K'
                  kratkiy ='K-Комбинирования'
                  lsap ='SAP код L'
                  lkrat ='Ламинация'
                  nsap ='SAP код N'
                  nkrat ='Наклейка'
                  sap7 ='SAP код 7'

                  try:
                        df_new[schot_name]['U-Упаковка + Готовая Продукция 7']=df_new[schot_name]['U-Упаковка + Готовая Продукция 7']
                        df_name ='U-Упаковка + Готовая Продукция 7'
                  except:
                        df_name ='U-Упаковка + Готовая Продукция'
            except:
                  esap ='ekrat_counter'
                  ekrat ='ekrat'
                  zsap ='zkrat_counter'
                  zkrat ='zkrat'
                  psap ='pkrat_counter'
                  pkrat ='pkrat'
                  ssap ='skrat_counter'
                  skrat ='skrat'
                  asap ='akrat_counter'
                  akrat ='akrat'
                  ksap ='kkrat1_counter'
                  kratkiy ='kkrat1'
                  lsap ='lkrat_counter'
                  lkrat ='lkrat'
                  nsap ='nkrat_counter'
                  nkrat ='nkrat'
                  sap7 ='ukrat1_counter'
                  df_name='ukrat1'
            
                  

            for key,razlov in df_new[schot_name].iterrows():
                  if razlov[sap7]!="":
                        if not RazlovkaTermo.objects.filter(sap_code7=razlov[sap7],kratkiy7=razlov[df_name]).exists():
                              razlovka_yoq = True
                              razlovka_komb = RazlovkaTermo(
                                    parent_id=0,
                                    esap_code =razlov[esap],
                                    ekratkiy =razlov[ekrat],
                                    zsap_code =razlov[zsap],
                                    zkratkiy =razlov[zkrat],
                                    psap_code =razlov[psap],
                                    pkratkiy =razlov[pkrat],
                                    ssap_code =razlov[ssap],
                                    skratkiy =razlov[skrat],
                                    asap_code =razlov[asap],
                                    akratkiy =razlov[akrat],
                                    nsap_code =razlov[nsap],
                                    nkratkiy =razlov[nkrat],
                                    ksap_code =razlov[ksap],
                                    kratkiy =razlov[kratkiy],
                                    lsap_code =razlov[lsap],
                                    lkratkiy =razlov[lkrat],
                                    sap_code7 =razlov[sap7],
                                    kratkiy7 =razlov[df_name]
                              )
                              razlovka_komb.save()
                        else:
                              razlovka_yoq = False 
            
                  else:
                        if razlovka_yoq:
                              RazlovkaTermo(
                                    parent_id=razlovka_komb.id,
                                    esap_code =razlov[esap],
                                    ekratkiy =razlov[ekrat],
                                    zsap_code =razlov[zsap],
                                    zkratkiy =razlov[zkrat],
                                    psap_code =razlov[psap],
                                    pkratkiy =razlov[pkrat],
                                    ssap_code =razlov[ssap],
                                    skratkiy =razlov[skrat],
                                    asap_code =razlov[asap],
                                    akratkiy =razlov[akrat],
                                    nsap_code =razlov[nsap],
                                    nkratkiy =razlov[nkrat],
                                    ksap_code =razlov[ksap],
                                    kratkiy =razlov[kratkiy],
                                    lsap_code =razlov[lsap],
                                    lkratkiy =razlov[lkrat],
                                    sap_code7 =razlov[sap7],
                                    kratkiy7 =razlov[df_name]
                              ).save()
            for key,razlov in df_new[ch_name].iterrows():
                  if not Characteristika.objects.filter(sap_code=razlov['SAP CODE'],kratkiy_text=razlov['KRATKIY TEXT']).exists():
                        Characteristika(
                              sap_code =razlov['SAP CODE'],
                              kratkiy_text =razlov['KRATKIY TEXT'],
                              section =razlov['SECTION'],
                              savdo_id =razlov['SAVDO_ID'],
                              savdo_name =razlov['SAVDO_NAME'],
                              export_customer_id =razlov['EXPORT_CUSTOMER_ID'],
                              system =razlov['SYSTEM'],
                              article =razlov['ARTICLE'],
                              length =razlov['LENGTH'],
                              surface_treatment =razlov['SURFACE_TREATMENT'],
                              alloy =razlov['ALLOY'],
                              temper =razlov['TEMPER'],
                              combination =razlov['COMBINATION'],
                              outer_side_pc_id =razlov['OUTER_SIDE_PC_ID'],
                              outer_side_pc_brand =razlov['OUTER_SIDE_PC_BRAND'],
                              inner_side_pc_id =razlov['INNER_SIDE_PC_ID'],
                              inner_side_pc_brand =razlov['INNER_SIDE_PC_BRAND'],
                              outer_side_wg_s_id =razlov['OUTER_SIDE_WG_S_ID'],
                              inner_side_wg_s_id =razlov['INNER_SIDE_WG_S_ID'],
                              outer_side_wg_id =razlov['OUTER_SIDE_WG_ID'],
                              inner_side_wg_id =razlov['INNER_SIDE_WG_ID'],
                              anodization_contact =razlov['ANODIZATION_CONTACT'],
                              anodization_type =razlov['ANODIZATION_TYPE'],
                              anodization_method =razlov['ANODIZATION_METHOD'],
                              print_view =razlov['PRINT_VIEW'],
                              profile_base =razlov['PROFILE_BASE'],
                              width =razlov['WIDTH'],
                              height =razlov['HEIGHT'],
                              category =razlov['CATEGORY'],
                              rawmat_type =razlov['RAWMAT_TYPE'],
                              benkam_id =razlov['BENKAM_ID'],
                              hollow_and_solid =razlov['HOLLOW AND SOLID'],
                              export_description =razlov['EXPORT_DESCRIPTION'],
                              export_description_eng =razlov['EXPORT_DESCRIPTION ENG'],
                              tnved =razlov['TNVED'],
                              surface_treatment_export =razlov['SURFACE_TREATMENT_EXPORT'],
                              wms_width =razlov['WMS_WIDTH'],
                              wms_height =razlov['WMS_HEIGHT'],
                              group_prise =''					
                        ).save()
            for key,razlov in df_new['title'].iterrows():
                  if not CharacteristicTitle.objects.filter(sap_код_s4p_100 = razlov['SAP код S4P 100']).exists():
                        CharacteristicTitle(
                              дата_изменение_добавление =razlov['Дата изменение добавление'], 
                              статус_изменение_добавление =razlov['Статус изменение добавление'], 
                              ссылки_для_чертежа =razlov['Ссылки для чертежа'], 
                              sap_код_s4p_100 =razlov['SAP код S4P 100'], 
                              нумерация_до_sap =razlov['Нумерация до SAP'], 
                              короткое_название_sap =razlov['Короткое название SAP'], 
                              польное_наименование_sap =razlov['Польное наименование SAP'], 
                              ед_изм =razlov['Ед, Изм,'], 
                              альтернативная_ед_изм =razlov['Альтернативная ед, изм'], 
                              коэфициент_пересчета =razlov['Коэфициент пересчета'], 
                              участок =razlov['Участок'], 
                              альтернативный_участок =razlov['Альтернативный участок'], 
                              длина =razlov['Длина'], 
                              ширина =razlov['Ширина'], 
                              высота =razlov['Высота'], 
                              группа_материалов =razlov['группа материалов'], 
                              удельный_вес_за_метр =razlov['Удельный вес за метр'], 
                              общий_вес_за_штуку =razlov['Общий вес за штуку'],
                              price =razlov['Price']
                        ).save()
            
      return JsonResponse({'a':'b'})


def add_characteristika_utils(request):
      df1 = pd.read_excel('c:\\OpenServer\\domains\\WMS&TMS.xlsx')
      df1 = df1.astype(str)
      
      for key,row in df1.iterrows():
            CharUtilsOne(
                  матрица =row['матрица'],
                  артикул =row['артикул'],
                  высота =row['высота'],
                  ширина =row['ширина'],
                  высота_ширина =row['высота_ширина'],
                  systems =row['systems'],
                  ).save()
            
      df2 = pd.read_excel('c:\\OpenServer\\domains\\HOLLOW.xlsx')
      df2 = df2.astype(str)
      
      for key,row in df2.iterrows():
            CharUtilsTwo(
                 артикул =row['артикул'],
                 полый_или_фасонный = row['полый_или_фасонный'] 
                  ).save()
            
            
      df3 = pd.read_excel('c:\\OpenServer\\domains\\Бухгалтерская.xlsx')
      df3 = df3.astype(str)
      
      for key,row in df3.iterrows():
            CharUtilsThree(
                 bux_name_rus =row['BUX_NAME_RUS'],
                 bux_name_eng = row['BUX_NAME_ENG'],
                 tnved =row['TNVED'],
                 group_price = row['GROUP_PRICE'] 
                  ).save()
            
      df4 = pd.read_excel('c:\\OpenServer\\domains\\price.xlsx')
      df4 = df4.astype(str)
      
      for key,row in df4.iterrows():
            CharUtilsFour(
                 category = row['CATEGORY'],
                  type = row['TYPE'],
                  price_for_1kg_som = row['price_for_1kg_SOM'],
                  price_for_1kg_usd = row['price_for_1kg_USD']
                  ).save()
            
      return JsonResponse({'a':'b'})

def base_profile(request):
      df1 = pd.read_excel('c:\\OpenServer\\domains\\BASA PROFIL.xlsx')
      df1 = df1.astype(str)
      
      for key,row in df1.iterrows():
            BazaProfiley(
                  артикул =row['артикул'],
                  серия =row['серия'],
                  старый_код_benkam =row['старый_код_benkam'],
                  старый_код =row['старый_код'],
                  old_product_description =row['old_product_description'],
                  компонент =row['компонент'],
                  product_description =row['product_description'],
                  ).save()
            
            
      return JsonResponse({'a':'b'})

class File:
      def __init__(self,file,filetype):
            self.file =file
            self.filetype =filetype

def update_char_title(request,id):
      file = CharacteristikaFile.objects.get(id=id).file
      df = pd.read_excel(f'{MEDIA_ROOT}/{file}','title')
      df =df.astype(str)
      df_extrusion = pd.read_excel(f'{MEDIA_ROOT}/{file}','T4')
      e_list =df_extrusion['SAP CODE E'].values.tolist()

      order_id = request.GET.get('order_id',None)
      filename ='aluminiytermo'
      if order_id:
            order = Order.objects.get(id = order_id)
            if order.order_type == 1:
                  filename ='aluminiy'

      pathzip = characteristika_created_txt_create(df,e_list,order_id,filename)
      fileszip = [File(file=path,filetype='BENKAM') for path in pathzip]
      if order_id:
            paths = order.paths
            zip_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            paths['status_zip'] ='done'
            paths['zip_created_at'] = zip_created_at
            if 'obichniy_razlovka_file' in order.paths:
                  paths['obichniy_razlovka_file'][0] = pathzip[0]
            else:
                  paths['termo_razlovka_file'][0] = pathzip[0]

            order.paths=paths
            order.work_type = 6
            order.save()
            context ={
                  'order':order
            }

            for key,val in paths.items():
                  context[key] = val
            return render(request,'order/order_detail.html',context)

      context = {
            'files':fileszip,
            'section':'Формированные файлы'
            }

      return render(request,'universal/generated_files.html',context)
      

@csrf_exempt
def add_char_utils_two(request):
      data = request.POST.get('data',None)
      if data:
            items = [CharUtilsTwo(артикул =item['artikul'],полый_или_фасонный =item['selection']) for item in ast.literal_eval(data)]
            CharUtilsTwo.objects.bulk_create(items)
            return JsonResponse({'saved':True})
      else:
            return JsonResponse({'saved':False})

@csrf_exempt
def add_char_utils_one(request):
      data = request.POST.get('data',None)
      if data:
            items = [CharUtilsOne(матрица =item['matritsa'],артикул =item['artikul'],высота=item['heigth'],ширина=item['width'],высота_ширина=item['height_and_width'],systems=item['systems']) for item in ast.literal_eval(data)]
            CharUtilsOne.objects.bulk_create(items)
            return JsonResponse({'saved':True})
      else:
            return JsonResponse({'saved':False})
      
@csrf_exempt
def baza_profile(request):
      data = request.POST.get('data',None)
      if data:
            items = [BazaProfiley(компонент =item['komponent'],артикул =item['artikul'],серия=item['seria'],старый_код_benkam=item['startiy_kod_bekam'],старый_код=item['stariykod'],old_product_description=item['oldprod_des'],product_description=item['prodesc']) for item in ast.literal_eval(data)]
            BazaProfiley.objects.bulk_create(items)
            return JsonResponse({'saved':True})
      else:
            return JsonResponse({'saved':False})
      
@csrf_exempt
def excel_does_not_exists_add(request):
      now = datetime.now()
      year =now.strftime("%Y")
      
      path_not_exists =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\Not Exists\\Not_Exists.xlsx'
      all_correct = True
      
      df = pd.read_excel(path_not_exists,sheet_name=['character utils one','character utils two','baza profile'])
      items =[]
      if df['character utils one'].shape[0] > 0:
            for key,row in df['character utils one'].iterrows():
                  items.append(CharUtilsOne(матрица =row['матрица'],артикул =row['артикул'],высота=row['высота'],ширина=row['ширина'],высота_ширина=row['высота_ширина'],systems=row['systems']))
            try:
                  CharUtilsOne.objects.bulk_create(items)
            except:
                  all_correct =False
            
      
      items =[]
      if df['character utils two'].shape[0] > 0:
            for key,row in df['character utils two'].iterrows():
                  items.append(CharUtilsTwo(артикул =row['артикул'],полый_или_фасонный =row['полый_или_фасонный']))
            try:
                  CharUtilsTwo.objects.bulk_create(items)
            except:
                  all_correct =False
            
      
      items =[]
      if df['baza profile'].shape[0] > 0:
            for key,row in df['baza profile'].iterrows():
                  items.append(BazaProfiley(компонент = row['компонент'],артикул = row['артикул'],серия= row['серия'],старый_код_benkam= row['старый_код_benkam'],старый_код= row['старый_код'],old_product_description= row['old_product_description'],product_description= row['product_description']))
            try:
                  BazaProfiley.objects.bulk_create(items)
            except:
                  all_correct =False
            
      
      return JsonResponse({'saved':all_correct})
      

      


brand_kraski_snaruji_ABC ={
      'A': 'AKZONOBEL',
      'R':  'RAINBOW',
      'P':  'PULVER',
      'T':  'TIGER',
      'B':  'BPC',
      'M':  'MIKROTON',
      'nan':'',
}

kod_dekorativ_snaruji_ABC ={
      '3701':'МАХАГОН',
      '7777':'ЗОЛОТОЙ ДУБ',
      '3702':'ТЁМНЫЙ ОРЕХ',
      '8888':'ДУБ МОККО',
      '9999':'ШЕФ ДУБ СЕРЫЙ',
      '3801':'3D',
      'nan':''  
}

svet_lam_plenke_POL ={
      'Алюкс антрацит':'АЛЮКС АНТРАЦИТ',
      'Золотой дуб':'ЗОЛОТОЙ ДУБ',
      'Орех':'ОРЕХ',
      'Дуб мокко':'ДУБ МОККО',
      'Грецкий орех':'ГРЕЦКИЙ ОРЕХ',
      'Дерево бальза':'ДЕРЕВО БАЛЬЗА',
      'Винчестер':'ВИНЧЕСТЕР',
      'Орех Ребраун':'ОРЕХ РЕБРАУН',
      'Шеффелдский дуб серый':'ШЕФ ДУБ СЕРЫЙ',
      'Шеф Альпийский дуб':'ШЕФ АЛЬП ДУБ',
      'Гранитовый шеф дуб':'ГРАНИТ ШЕФ ДУБ',
      'Метбраш серый антрацит':'МЕТБ СЕРЫЙ АНТР',
      'Красный орех':'КРАСНЫЙ ОРЕХ',
      'Шеффелдский дуб светлый':'ШЕФ ДУБ СВЕТ',
      'Орех терра':'ОРЕХ ТЕРРА',
      'Метбраш серый кварц':'МЕТБ СЕРЫЙ КВАР',
      'Метбраш платин':'МЕТБ ПЛАТИН',
      'Терновый дуб':'ТЕРНОВЫЙ ДУБ',
      'Алюкс серый алюминий':'АЛЮКС СЕРЫЙ АЛЮ',
      'Сантана':'САНТАНА',
      'Светлый дуб':'СВЕТЛЫЙ ДУБ',
      'ТЕМНЫЙ ДУБ':'ТЕМНЫЙ ДУБ',
      'GOLD BRUSH':'GOLD BRUSH',
      'X-BRUSH':'X-BRUSH',
      'Ocean Blue':'Ocean Blue'
}

svet_lam_plenke_NA ={
      'Алюкс антрацит':'НА АЛЮКС АНТРАЦИТ',
      'Золотой дуб':'НА ЗОЛОТОЙ ДУБ',
      'Орех':'НА ОРЕХ',
      'Дуб мокко':'НА ДУБ МОККО',
      'Грецкий орех':'НА ГРЕЦКИЙ ОРЕХ',
      'Дерево бальза':'НА ДЕРЕВО БАЛЬЗА',
      'Винчестер':'НА ВИНЧЕСТЕР',
      'Орех Ребраун':'НА ОРЕХ РЕБРАУН',
      'Шеффелдский дуб серый':'НА ШЕФ ДУБ СЕРЫЙ',
      'Шеф Альпийский дуб':'НА ШЕФ АЛЬП ДУБ',
      'Гранитовый шеф дуб':'НА ГРАНИТ ШЕФ ДУБ',
      'Метбраш серый антрацит':'НА МЕТБ СЕРЫЙ АНТР',
      'Красный орех':'НА КРАСНЫЙ ОРЕХ',
      'Шеффелдский дуб светлый':'НА ШЕФ ДУБ СВЕТЛЫЙ',
      'Орех терра':'НА ОРЕХ ТЕРРА',
      'Метбраш серый кварц':'НА МЕТБ СЕРЫЙ КВАР',
      'Метбраш платин':'НА МЕТБ ПЛАТИН',
      'Терновый дуб':'НА ТЕРНОВЫЙ ДУБ',
      'Алюкс серый алюминий':'НА АЛЮКС СЕРЫЙ АЛЮ',
      'Сантана':'НА САНТАНА',
      'Светлый дуб':'НА СВЕТЛЫЙ ДУБ',
      'ТЕМНЫЙ ДУБ':'НА ТЕМНЫЙ ДУБ',
      'GOLD BRUSH':'НА GOLD BRUSH',
      'X-BRUSH':'НА X-BRUSH',
      'Ocean Blue':'Ocean Blue'
}

svet_lam_plenke_VN ={
      'Алюкс антрацит':'ВН АЛЮКС АНТРАЦИТ',
      'Золотой дуб':'ВН ЗОЛОТОЙ ДУБ',
      'Орех':'ВН ОРЕХ',
      'Дуб мокко':'ВН ДУБ МОККО',
      'Грецкий орех':'ВН ГРЕЦКИЙ ОРЕХ',
      'Дерево бальза':'ВН ДЕРЕВО БАЛЬЗА',
      'Винчестер':'ВН ВИНЧЕСТЕР',
      'Орех Ребраун':'ВН ОРЕХ РЕБРАУН',
      'Шеффелдский дуб серый':'ВН ШЕФ ДУБ СЕРЫЙ',
      'Шеф Альпийский дуб':'ВН ШЕФ АЛЬП ДУБ',
      'Гранитовый шеф дуб':'ВН ГРАНИТ ШЕФ ДУБ',
      'Метбраш серый антрацит':'ВН МЕТБ СЕРЫЙ АНТР',
      'Красный орех':'ВН КРАСНЫЙ ОРЕХ',
      'Шеффелдский дуб светлый':'ВН ШЕФ ДУБ СВЕТЛЫЙ',
      'Орех терра':'ВН ОРЕХ ТЕРРА',
      'Метбраш серый кварц':'ВН МЕТБ СЕРЫЙ КВАР',
      'Метбраш платин':'ВН МЕТБ ПЛАТИН',
      'Терновый дуб':'ВН ТЕРНОВЫЙ ДУБ',
      'Алюкс серый алюминий':'ВН АЛЮКС СЕРЫЙ АЛЮ',
      'Сантана':'ВН САНТАНА',
      'Светлый дуб':'ВН СВЕТЛЫЙ ДУБ',
      'ТЕМНЫЙ ДУБ':'ВН ТЕМНЫЙ ДУБ',
      'GOLD BRUSH':'ВН GOLD BRUSH',
      'X-BRUSH':'ВН X-BRUSH',
      'Ocean Blue':'Ocean Blue'
}

def product_add_second(request,id):
      file = AluFileTermo.objects.get(id=id).file
      df = pd.read_excel(f'{MEDIA_ROOT}/{file}')
      df =df.astype(str)
      
      now = datetime.now()
      year =now.strftime("%Y")
      month =now.strftime("%B")
      day =now.strftime("%a%d")
      hour =now.strftime("%H HOUR")
      minut =now.strftime("%M")
      
      nakleyka_iskyucheniye =NakleykaIskyuchenie.objects.all().values_list('sap_code',flat=True)
      doesnotexist,correct = check_for_correct(df)
      if not correct:
            context ={
                  'CharUtilsOne':doesnotexist[0],
                  'CharUtilsTwo':doesnotexist[1],
                  'BazaProfile':doesnotexist[2]
            }
            df_char_utils_one = pd.DataFrame({
                  'матрица':doesnotexist[0],
                  'артикул':doesnotexist[0],
                  'высота':['' for i in doesnotexist[0]],
                  'ширина':['' for i in doesnotexist[0]],
                  'высота_ширина':['' for i in doesnotexist[0]],
                  'systems':['' for i in doesnotexist[0]]
                  })
            df_char_utils_two =pd.DataFrame({
                  'артикул':doesnotexist[1],
                  'полый_или_фасонный':['' for i in doesnotexist[1]]
            })
            df_baza_profiley =pd.DataFrame({
                  'артикул':doesnotexist[2],
                  'серия':['' for i in doesnotexist[2]],
                  'старый_код_benkam':['' for i in doesnotexist[2]],
                  'старый_код':['' for i in doesnotexist[2]],
                  'old_product_description':['' for i in doesnotexist[2]],
                  'компонент':['' for i in doesnotexist[2]],
                  'product_description':['' for i in doesnotexist[2]]
            })
            create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}','Not Exists')
            
            path_not_exists =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\Not Exists\\Not_Exists.xlsx'
            
            if os.path.isfile(path_not_exists):
                  try:
                        os.remove(path_not_exists)
                  except:
                        return render(request,'utils/file_exist.html')
            
            writer = pd.ExcelWriter(path_not_exists, engine='xlsxwriter')
            df_char_utils_one.to_excel(writer,index=False,sheet_name ='character utils one')
            df_char_utils_two.to_excel(writer,index=False,sheet_name ='character utils two')
            df_baza_profiley.to_excel(writer,index=False,sheet_name ='baza profile')
            writer.close()
            return render(request,'termo/check_for_correct.html',context)
      ################### group by#########
      aluminiy_group = AluminiyProduct.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
      umumiy_counter={}
      for al in aluminiy_group:
            umumiy_counter[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      ################ termo max ########
      aluminiy_group_termo = AluminiyProductTermo.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
      umumiy_counter_termo = {}
      for al in aluminiy_group_termo:
            umumiy_counter_termo[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      ############################ end grouby ######
      
      
      a=datetime.now()
      for key,row in df.iterrows():
            if row['Тип покрытия'] == 'nan':
                  df = df.drop(key)
      
      
      df_new =pd.DataFrame()
      df_new['Название системы']=df['Название системы']
      df_new['SAP код E']=''
      df_new['Экструзия холодная резка']=''
      df_new['SAP код Z']=''
      df_new['Печь старения']=''
      df_new['SAP код P']=''
      df_new['Покраска автомат']=''
      df_new['SAP код S']=''
      df_new['Сублимация']=''
      df_new['SAP код A']=''
      df_new['Анодировка']=''
      df_new['SAP код N']=''
      df_new['Наклейка']=''
      df_new['SAP код K']=''
      df_new['K-Комбинирования']=''
      df_new['SAP код L']=''
      df_new['Ламинация']=''
      df_new['SAP код 7']=''
      df_new['U-Упаковка + Готовая Продукция']=''
      df_new['SAP код F']=''
      df_new['Фабрикация']=''
      df_new['SAP код 75']=''
      df_new['U-Упаковка + Готовая Продукция 75']=''
      
      
      
      cache_for_cratkiy_text =[]
      
      for key,row in df.iterrows():
            print(key)
            row['Сплав'] = row['Сплав'].replace('.0','')
            row['Сплав'] = row['Сплав'].replace('.0','')
            row['Длина (мм)'] = row['Длина (мм)'].replace('.0','')
            row['Бренд краски снаружи'] = row['Бренд краски снаружи'].replace('.0','')
            row['Код краски снаружи'] = row['Код краски снаружи'].replace('.0','')
            row['Бренд краски внутри'] = row['Бренд краски внутри'].replace('.0','')
            row['Код краски внутри'] = row['Код краски внутри'].replace('.0','')
            row['Код декор пленки снаружи'] = row['Код декор пленки снаружи'].replace('.0','')
            row['Цвет декор пленки снаружи'] = row['Цвет декор пленки снаружи'].replace('.0','')
            row['Код декор пленки внутри'] = row['Код декор пленки внутри'].replace('.0','')
            row['Код цвета анодировки внутри'] = row['Код цвета анодировки внутри'].replace('.0','')
            row['Код цвета анодировки снаружи'] = row['Код цвета анодировки снаружи'].replace('.0','')
            row['Контактность анодировки'] = row['Контактность анодировки'].replace('.0','')
            row['Код лам пленки снаружи'] = row['Код лам пленки снаружи'].replace('.0','')
            row['Код лам пленки внутри'] = row['Код лам пленки внутри'].replace('.0','')
            row['Код лам пленки внутри'] = row['Код лам пленки внутри'].replace('.0','')
            
            
            
            artikul = df['Артикул'][key]
            component = df['Компонент'][key]
            
            duplicat_list =[]
            
            if artikul !='nan':
                  print('artikulllllllll')
                  if df['Длина при выходе из пресса'][key] != 'nan':
                        dlina = df['Длина при выходе из пресса'][key].replace('.0','')
                              
                        df_new['Фабрикация'][key]=fabrikatsiya_sap_kod(df['Краткий текст товара'][key],df['Длина (мм)'][key])
                        df_new['U-Упаковка + Готовая Продукция 75'][key]=fabrikatsiya_sap_kod(df['Краткий текст товара'][key],df['Длина (мм)'][key])
                        
                        if df['Тип покрытия'][key] != 'Ламинированный':
                              df_new['K-Комбинирования'][key] = fabrikatsiya_sap_kod(df['Краткий текст товара'][key],df['Длина при выходе из пресса'][key].replace('.0',''))
                        else:
                              df_new['K-Комбинирования'][key] = fabrikatsiya_sap_kod(df['Краткий текст товара'][key].split('_')[0] +' NT1',df['Длина при выходе из пресса'][key].replace('.0',''))
                        
                        if df['Тип покрытия'][key] == 'Ламинированный':
                              plenki1 = False
                              plenki2 = False
                              if df['Код лам пленки снаружи'][key] != 'nan':
                                    laminatsiya =row['Код лам пленки снаружи'].replace('.0','')+'/XXXX'
                                    plenki1 = True
                                    
                              if df['Код лам пленки внутри'][key] != 'nan':
                                    laminatsiya ='XXXX/'+df['Код лам пленки внутри'][key].replace('.0','')
                                    plenki2 =True
                                    
                              if plenki1 and plenki2:
                                    laminatsiya =df['Код лам пленки снаружи'][key].replace('.0','') +'/'+ df['Код лам пленки внутри'][key].replace('.0','')
                                    
                              ll =row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')+'/'+df['Код краски внутри'][key].replace('.0','')+'_'+laminatsiya +' ' +row['Код наклейки']
                              df_new['Ламинация'][key] = fabrikatsiya_sap_kod(ll,df['Длина при выходе из пресса'][key].replace('.0',''))

                  else:
                        dlina = df['Длина (мм)'][key]
                        df_new['U-Упаковка + Готовая Продукция'][key] = df['Краткий текст товара'][key]
                        
                        if df['Тип покрытия'][key] != 'Ламинированный': 
                              df_new['K-Комбинирования'][key] = df['Краткий текст товара'][key]
                        else: 
                              df_new['K-Комбинирования'][key] = df['Краткий текст товара'][key].split('_')[0] +' NT1'
                        
                        if df['Тип покрытия'][key] == 'Ламинированный':
                              plenki1 = False
                              plenki2 = False
                              if row['Код лам пленки снаружи'] != 'nan':
                                    laminatsiya =row['Код лам пленки снаружи'].replace('.0','')+'/XXXX'
                                    plenki1 = True
                                    
                              if df['Код лам пленки внутри'][key] != 'nan':
                                    laminatsiya ='XXXX/'+df['Код лам пленки внутри'][key].replace('.0','')
                                    plenki2 =True
                                    
                              if plenki1 and plenki2:
                                    laminatsiya =df['Код лам пленки снаружи'][key].replace('.0','') +'/'+ df['Код лам пленки внутри'][key].replace('.0','')
                                    
                              df_new['Ламинация'][key] = df['Краткий текст товара'][key]
                        
                  if df['Длина при выходе из пресса'][key] != 'nan':
                        if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='F',kratkiy_tekst_materiala=df_new['Фабрикация'][key]).exists():
                              df_new['SAP код F'][key] = AluminiyProductTermo.objects.filter(artikul = df['Артикул'][key],section ='F',kratkiy_tekst_materiala=df_new['Фабрикация'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код Ф'][key],df_new['Фабрикация'][key],'F'])
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='F').exists():
                                    umumiy_counter_termo[df['Артикул'][key]+'-F'] += 1
                                    max_valuesF = umumiy_counter_termo[df['Артикул'][key]+'-F']
                                    materiale = df['Артикул'][key] +"-F{:03d}".format(max_valuesF)
                                    AluminiyProductTermo(artikul =df['Артикул'][key],section ='F',counter=max_valuesF,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Фабрикация'][key],material=materiale).save()
                                    df_new['SAP код F'][key]=materiale
                                    artikle = materiale.split('-')[0]
                              
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Фабрикация'][key],
                                                      'section':'F-Фабрикация',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':row['Тип покрытия'],
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                              else:
                                    materiale = df['Артикул'][key] +"-F{:03d}".format(1)
                                    AluminiyProductTermo(artikul =df['Артикул'][key],section ='F',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Фабрикация'][key],material=materiale).save()
                                    df_new['SAP код F'][key]=materiale
                                    umumiy_counter_termo[df['Артикул'][key]+'-F'] = 1
                                    artikle = materiale.split('-')[0]
                              
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Фабрикация'][key],
                                                      'section':'F-Фабрикация',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':row['Тип покрытия'],
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                                    
                        
                        
                        if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='75',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key]).exists():
                              df_new['SAP код 75'][key] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='75',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код 75'][key],df_new['U-Упаковка + Готовая Продукция 75'][key],'75'])
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='75').exists():
                                    umumiy_counter_termo[df['Артикул'][key]+'-75'] += 1
                                    max_values75 = umumiy_counter_termo[df['Артикул'][key]+'-75']
                                    
                                    if max_values75 <= 99:
                                          materiale = df['Артикул'][key]+"-75{:02d}".format(max_values75)
                                    else:
                                          counter =7500 + max_values75
                                          materiale = df['Артикул'][key]+"-{:04d}".format(counter)
                                          
                                          
                                    AluminiyProductTermo(artikul =df['Артикул'][key],section ='75',counter=max_values75,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key],material=materiale).save()
                                    df_new['SAP код 75'][key] = materiale
                                    
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    surface_treatment_export=''
                                    if row['Тип покрытия'].lower() =='неокрашенный':
                                          surface_treatment_export ='Неокрашенный'
                                    elif ((row['Тип покрытия'].lower() =='окрашенный') or (row['Тип покрытия'].lower() =='белый')):
                                          surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']]+" " + row['Код краски снаружи']
                                    elif row['Тип покрытия'].lower() =='сублимированный':
                                          surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                                    elif row['Тип покрытия'].lower() =='анодированный':
                                          surface_treatment_export = str(row['Код цвета анодировки снаружи']).replace('.0','')
                                    elif row['Тип покрытия'].lower() =='ламинированный':
                                          if (row['Цвет лам пленки снаружи']=='XXXX' or row['Цвет лам пленки снаружи']=='nan'):
                                                surface_treatment_export = svet_lam_plenke_VN[row['Цвет лам пленки внутри']]                  
                                          else:
                                                if (row['Цвет лам пленки внутри']=='XXXX' or row['Цвет лам пленки внутри']=='nan'):
                                                      surface_treatment_export = svet_lam_plenke_NA[row['Цвет лам пленки снаружи']] 
                                                else:
                                                      surface_treatment_export = svet_lam_plenke_POL[row['Цвет лам пленки снаружи']]
                                          
                                    
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['U-Упаковка + Готовая Продукция 75'][key],
                                                      'section':'V-Упаковка + Готовая продукция',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':row['Тип покрытия'],
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ГП',
                                                      'hollow_and_solid':hollow_and_solid,
                                                      'export_description':export_description,
                                                      'export_description_eng':export_description_eng.bux_name_eng,
                                                      'tnved':export_description_eng.tnved,
                                                      'surface_treatment_export':surface_treatment_export,# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                              
                              else:
                                    materiale = df['Артикул'][key]+"-75{:02d}".format(1)
                                    AluminiyProductTermo(artikul = df['Артикул'][key],section ='75',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key],material=materiale).save()
                                    df_new['SAP код 75'][key] = materiale 
                                    umumiy_counter_termo[df['Артикул'][key]+'-75'] = 1
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    surface_treatment_export=''
                                    if row['Тип покрытия'].lower() =='неокрашенный':
                                          surface_treatment_export ='Неокрашенный'
                                    elif ((row['Тип покрытия'].lower() =='окрашенный') or (row['Тип покрытия'].lower() =='белый')):
                                          surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']] +' ' +row['Код краски снаружи']
                                    elif row['Тип покрытия'].lower() =='сублимированный':
                                          surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                                    elif row['Тип покрытия'].lower() =='анодированный':
                                          surface_treatment_export = str(row['Код цвета анодировки снаружи']).replace('.0','')
                                    elif row['Тип покрытия'].lower() =='ламинированный':
                                          if (row['Цвет лам пленки снаружи']=='XXXX' or row['Цвет лам пленки снаружи']=='nan'):
                                                surface_treatment_export = svet_lam_plenke_VN[row['Цвет лам пленки внутри']]                  
                                          else:
                                                if (row['Цвет лам пленки внутри']=='XXXX' or row['Цвет лам пленки внутри']=='nan'):
                                                      surface_treatment_export = svet_lam_plenke_NA[row['Цвет лам пленки снаружи']] 
                                                else:
                                                      surface_treatment_export = svet_lam_plenke_POL[row['Цвет лам пленки снаружи']]
                                          
                                    
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['U-Упаковка + Готовая Продукция 75'][key],
                                                      'section':'V-Упаковка + Готовая продукция',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':row['Тип покрытия'],
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ГП',
                                                      'hollow_and_solid':hollow_and_solid,
                                                      'export_description':export_description,
                                                      'export_description_eng':export_description_eng.bux_name_eng,
                                                      'tnved':export_description_eng.tnved,
                                                      'surface_treatment_export':surface_treatment_export,# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                  else:     
                        if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key]).exists():
                              df_new['SAP код 7'][key] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код 7'][key],df_new['U-Упаковка + Готовая Продукция'][key],'75'])
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul=df['Артикул'][key],section ='7').exists():
                                    umumiy_counter_termo[df['Артикул'][key]+'-7'] += 1
                                    max_values7 = umumiy_counter_termo[df['Артикул'][key]+'-7']
                                    materiale = df['Артикул'][key]+"-7{:03d}".format(max_values7)
                                    AluminiyProductTermo(artikul = df['Артикул'][key],section ='7',counter=max_values7,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key],material=materiale).save()
                                    df_new['SAP код 7'][key] = materiale
                                    artikle = str(materiale).split('-')[0]
                                   
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    # print(export_description)
                                    # print(df_new['SAP код 7'][key],key)
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    surface_treatment_export=''
                                    if row['Тип покрытия'].lower() =='неокрашенный':
                                          surface_treatment_export ='Неокрашенный'
                                    elif ((row['Тип покрытия'].lower() =='окрашенный') or (row['Тип покрытия'].lower() =='белый')):
                                          surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']] + ' ' + row['Код краски снаружи']
                                    elif row['Тип покрытия'].lower() =='сублимированный':
                                          surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                                    elif row['Тип покрытия'].lower() =='анодированный':
                                          surface_treatment_export = str(row['Код цвета анодировки снаружи']).replace('.0','')
                                    elif row['Тип покрытия'].lower() =='ламинированный':
                                          if (row['Цвет лам пленки снаружи']=='XXXX' or row['Цвет лам пленки снаружи']=='nan'):
                                                surface_treatment_export = svet_lam_plenke_VN[row['Цвет лам пленки внутри']]                  
                                          else:
                                                if (row['Цвет лам пленки внутри']=='XXXX' or row['Цвет лам пленки внутри']=='nan'):
                                                      surface_treatment_export = svet_lam_plenke_NA[row['Цвет лам пленки снаружи']] 
                                                else:
                                                      surface_treatment_export = svet_lam_plenke_POL[row['Цвет лам пленки снаружи']]
                                          
                                    print(f"Ukrat1 tip pokr {row['Тип покрытия']}")
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['U-Упаковка + Готовая Продукция'][key],
                                                      'section':'U-Упаковка + Готовая продукция',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':row['Тип покрытия'],
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ГП',
                                                      'hollow_and_solid':hollow_and_solid,
                                                      'export_description':export_description,
                                                      'export_description_eng':export_description_eng.bux_name_eng,
                                                      'tnved':export_description_eng.tnved,
                                                      'surface_treatment_export':surface_treatment_export,# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                              
                              else:
                                    materiale = df['Артикул'][key]+"-7{:03d}".format(1)
                                    AluminiyProductTermo(artikul = df['Артикул'][key],section ='7',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key],material=materiale).save()
                                    df_new['SAP код 7'][key] = materiale
                                    umumiy_counter_termo[df['Артикул'][key]+'-7'] = 1
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    surface_treatment_export=''
                                    if row['Тип покрытия'].lower() =='неокрашенный':
                                          surface_treatment_export ='Неокрашенный'
                                    elif ((row['Тип покрытия'].lower() =='окрашенный') or (row['Тип покрытия'].lower() =='белый')):
                                          surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']] + row['Код краски снаружи']
                                    elif row['Тип покрытия'].lower() =='сублимированный':
                                          surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                                    elif row['Тип покрытия'].lower() =='анодированный':
                                          surface_treatment_export = str(row['Код цвета анодировки снаружи']).replace('.0','')
                                    elif row['Тип покрытия'].lower() =='ламинированный':
                                          if (row['Цвет лам пленки снаружи']=='XXXX' or row['Цвет лам пленки снаружи']=='nan'):
                                                surface_treatment_export = svet_lam_plenke_VN[row['Цвет лам пленки внутри']]                  
                                          else:
                                                if (row['Цвет лам пленки внутри']=='XXXX' or row['Цвет лам пленки внутри']=='nan'):
                                                      surface_treatment_export = svet_lam_plenke_NA[row['Цвет лам пленки снаружи']] 
                                                else:
                                                      surface_treatment_export = svet_lam_plenke_POL[row['Цвет лам пленки снаружи']]
                                          
                                    print(f"Ukrat1 tip pokr {row['Тип покрытия']}")
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['U-Упаковка + Готовая Продукция'][key],
                                                      'section':'U-Упаковка + Готовая продукция',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':row['Тип покрытия'],
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ГП',
                                                      'hollow_and_solid':hollow_and_solid,
                                                      'export_description':export_description,
                                                      'export_description_eng':export_description_eng.bux_name_eng,
                                                      'tnved':export_description_eng.tnved,
                                                      'surface_treatment_export':surface_treatment_export,# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                              
                        ##### kombirinovanniy
                  
                  if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='K',kratkiy_tekst_materiala=df_new['K-Комбинирования'][key]).exists():
                        df_new['SAP код K'][key] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='K',kratkiy_tekst_materiala=df_new['K-Комбинирования'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код K'][key],df_new['K-Комбинирования'][key],'K'])
                  else: 
                        
                        name_tip_pokr =''
                        if (('7777' in df_new['K-Комбинирования'][key]) or ('8888' in df_new['K-Комбинирования'][key])  or ('3701' in df_new['K-Комбинирования'][key]) or ('3702' in df_new['K-Комбинирования'][key])):
                              name_tip_pokr = 'Сублимированный'
                        elif '9016' in df_new['K-Комбинирования'][key]:
                              name_tip_pokr = 'Белый'
                        elif 'MF' in df_new['K-Комбинирования'][key]:
                              name_tip_pokr = 'Неокрашенный'
                        elif anodirovaka_check(ANODIROVKA_CODE,df_new['K-Комбинирования'][key]):
                              name_tip_pokr = 'Анодированный'
                        else:
                              name_tip_pokr = 'Окрашенный'
                              
                        if AluminiyProductTermo.objects.filter(artikul=df['Артикул'][key],section ='K').exists():
                              umumiy_counter_termo[df['Артикул'][key]+'-K'] += 1
                              max_valuesK = umumiy_counter_termo[df['Артикул'][key]+'-K']
                              materiale = df['Артикул'][key]+"-K{:03d}".format(max_valuesK)
                              AluminiyProductTermo(artikul = df['Артикул'][key],section ='K',counter=max_valuesK,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['K-Комбинирования'][key],material=materiale).save()
                              df_new['SAP код K'][key] = materiale
                              
                              artikle = str(materiale).split('-')[0]
                              
                              
                              hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                              
                              width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                              
                              print(f"K-Комбинирования tip pokr {row['Тип покрытия']}") 
                              
                              
                                    
                                    
                                  
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['K-Комбинирования'][key],
                                                'section':'K-Комбинирования',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':name_tip_pokr,
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':width_and_height.ширина,
                                                'wms_height':width_and_height.высота,
                                                'group_prise': export_description_eng.group_price,
                                                }
                                          )
                                      
                        else:
                              materiale = df['Артикул'][key]+"-K{:03d}".format(1)
                              AluminiyProductTermo(artikul = df['Артикул'][key],section ='K',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['K-Комбинирования'][key],material=materiale).save()
                              df_new['SAP код K'][key] = materiale
                              umumiy_counter_termo[df['Артикул'][key]+'-K'] = 1
                              artikle = materiale.split('-')[0]
                              
                              hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                              
                              width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                              
                              print(f"K-Комбинирования tip pokr {row['Тип покрытия']}")
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['K-Комбинирования'][key],
                                                'section':'K-Комбинирования',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':name_tip_pokr,
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':width_and_height.ширина,
                                                'wms_height':width_and_height.высота,
                                                'group_prise': export_description_eng.group_price,
                                                }
                                          )
                              
                  
                  if df['Тип покрытия'][key] == 'Ламинированный':      
                        if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='L',kratkiy_tekst_materiala=df_new['Ламинация'][key]).exists():
                              df_new['SAP код L'][key] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='L',kratkiy_tekst_materiala=df_new['Ламинация'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код L'][key],df_new['Ламинация'][key],'L'])
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='L').exists():
                                    umumiy_counter_termo[df['Артикул'][key]+'-L'] += 1
                                    max_valuesL = umumiy_counter_termo[ df['Артикул'][key] +'-L']
                                    materiale = df['Артикул'][key]+"-L{:03d}".format(max_valuesL)
                                    AluminiyProductTermo(artikul =df['Артикул'][key],section ='L',counter=max_valuesL,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Ламинация'][key],material=materiale).save()
                                    df_new['SAP код L'][key]=materiale
                                    artikle = materiale.split('-')[0]
                                    
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"Ламинация1 tip pokr {row['Тип покрытия']}")   
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Ламинация'][key],
                                                      'section':'L-Ламинирование',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':'Ламинированный',
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                              else:
                                    materiale = df['Артикул'][key]+"-L{:03d}".format(1)
                                    AluminiyProductTermo(artikul =df['Артикул'][key],section ='L',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Ламинация'][key],material=materiale).save()
                                    df_new['SAP код L'][key]=materiale
                                    umumiy_counter_termo[df['Артикул'][key]+'-L'] = 1
                                    
                                    artikle = materiale.split('-')[0]
                                    
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    print(f"Ukrat1 tip pokr {row['Тип покрытия']}")
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Ламинация'][key],
                                                      'section':'L-Ламинирование',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':'Ламинированный',
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
            elif  component !='nan':
                  print('komponenttttttt')
                  dlina =''
            
                  if df['Длина при выходе из пресса'][key] != 'nan':
                        dlina = df['Длина при выходе из пресса'][key].replace('.0','')      
                  else:
                        dlina = df['Длина (мм)'][key]
                        
                        
                  df_new['Экструзия холодная резка'][key] = row['Сплав'][len(row['Сплав'])-2:] +'T4 '+'L'+dlina+' MF'
                  if row['тип закаленности']!='T4':
                        df_new['Печь старения'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' MF'
                  
                  
                              
                  if ((row['Тип покрытия'] == 'Окрашенный') or (row['Тип покрытия'] == 'Белый' )):
                        df_new['Покраска автомат'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи']+row['Код краски снаружи']
                        if row['Код наклейки'] != 'NT1':
                              df_new['Наклейка'][key] = df_new['Покраска автомат'][key] +' '+ row['Код наклейки'].replace('.0','')
                  
                  
                              
                  elif row['Тип покрытия'] == 'Ламинированный':
                        df_new['Покраска автомат'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи']+row['Код краски снаружи']
                        
                  
                  elif row['Тип покрытия'] =='Сублимированный':
                        df_new['Покраска автомат'][key]=row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')
                        df_new['Сублимация'][key]=row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')+'_'+row['Код декор пленки снаружи'].replace('.0','')
                        
                        if row['Код наклейки'] != 'NT1':
                              df_new['Наклейка'][key]=df_new['Сублимация'][key] + ' ' + row['Код наклейки'].replace('.0','')

                  elif row['Тип покрытия'] =='Анодированный':
                        df_new['Анодировка'][key]=row['Сплав'][len(row['Сплав'])-2:] +row['тип закаленности']+' L'+dlina+' '+row['Код цвета анодировки снаружи'].replace('.0','')
                        if row['Код наклейки'] != 'NT1':
                              df_new['Наклейка'][key]= df_new['Анодировка'][key] +' '+row['Контактность анодировки']+' ' + row['Код наклейки'].replace('.0','')
                  else:
                        print("<<<<<< Нет Тип покрытия ! >>>>>>")
                  
                  termo_existE = AluminiyProductTermo.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key]).exists()
                  simple_existE = AluminiyProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key]).exists()
                  # print('existsance = ',termo_existE,simple_existE)
                  if (termo_existE or simple_existE):
                        if termo_existE:
                              df_new['SAP код E'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key])[:1].get().material
                        else:
                              
                              df_new['SAP код E'][key] = AluminiyProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код E'][key],df_new['Экструзия холодная резка'][key],'E'])
                  else:
                        if AluminiyProductTermo.objects.filter(artikul =component,section ='E').exists():
                              # max_valuesE = AluminiyProductTermo.objects.filter(artikul =component,section ='E').values('section').annotate(total_max=Max('counter'))[0]['total_max']
                              umumiy_counter_termo[component+'-E'] += 1
                              max_valuesE = umumiy_counter_termo[component+'-E']
                              materiale = component+"-E{:03d}".format(max_valuesE)
                              AluminiyProductTermo(artikul =component,section ='E',counter=max_valuesE,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key],material=materiale).save()
                              df_new['SAP код E'][key]=materiale
                              
                              artikle = materiale.split('-')[0]
                              print(artikle)
                              hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                              
                              width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                              print(f"EEE tip pokr {row['Тип покрытия']}")
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Экструзия холодная резка'][key],
                                                'section':'E-Экструзия холодная резка ZPP2',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':'Неокрашенный',
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id':'',# row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':'',#row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':'',
                                                'inner_side_wg_s_id':'',
                                                'outer_side_wg_id':'',#row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':'',#row['Код лам пленки внутри'],
                                                'anodization_contact':'',#row['Контактность анодировки'],
                                                'anodization_type':'',#row['Тип анодировки'],
                                                'anodization_method':'',#row['Способ анодировки'],
                                                'print_view':'',#row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':width_and_height.ширина,
                                                'wms_height':width_and_height.высота,
                                                'group_prise': export_description_eng.group_price,
                                                }
                                          )
                                
                        else: 
                              materiale = component+"-E{:03d}".format(1)
                              AluminiyProductTermo(artikul =component,section ='E',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key],material=materiale).save()
                              df_new['SAP код E'][key]=materiale
                              umumiy_counter_termo[component+'-E'] = 1
                              
                              artikle = materiale.split('-')[0]
                              
                              hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                              
                              
                              width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                              
                              print(f"EEE tip pokr {row['Тип покрытия']}")    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Экструзия холодная резка'][key],
                                                'section':'E-Экструзия холодная резка ZPP2',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':'Неокрашенный',
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id':'',# row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':'',#row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':'',
                                                'inner_side_wg_s_id':'',
                                                'outer_side_wg_id':'',#row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':'',#row['Код лам пленки внутри'],
                                                'anodization_contact':'',#row['Контактность анодировки'],
                                                'anodization_type':'',#row['Тип анодировки'],
                                                'anodization_method':'',#row['Способ анодировки'],
                                                'print_view':'',#row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':width_and_height.ширина,
                                                'wms_height':width_and_height.высота,
                                                'group_prise': export_description_eng.group_price,
                                                }
                                          )
                              
                  termo_existZ =AluminiyProductTermo.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['Печь старения'][key]).exists()
                  simple_existZ =AluminiyProduct.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['Печь старения'][key]).exists()
                  if row['тип закаленности']!='T4':
                        if (termo_existZ or simple_existZ):
                              if termo_existZ:
                                    df_new['SAP код Z'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['Печь старения'][key])[:1].get().material
                              else:
                                    df_new['SAP код Z'][key] = AluminiyProduct.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['Печь старения'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код Z'][key],df_new['Печь старения'][key],'Z'])
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =component,section ='Z').exists():
                                    umumiy_counter_termo[ component +'-Z'] += 1
                                    max_valuesZ = umumiy_counter_termo[ component +'-Z']
                                    materiale = component+"-Z{:03d}".format(max_valuesZ)
                                    AluminiyProductTermo(artikul =component,section ='Z',counter=max_valuesZ,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Печь старения'][key],material=materiale).save()
                                    df_new['SAP код Z'][key]=materiale
                                    
                                    artikle = materiale.split('-')[0]
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                          
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                          
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"ZZZ tip pokr {row['Тип покрытия']}")    
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Печь старения'][key],
                                                      'section':'Z-Печь старения',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':'Неокрашенный',
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id':'',# row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':'',#row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':'',#row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':'',#row['Код лам пленки внутри'],
                                                      'anodization_contact':'',#row['Контактность анодировки'],
                                                      'anodization_type':'',#row['Тип анодировки'],
                                                      'anodization_method':'',#row['Способ анодировки'],
                                                      'print_view':'',#row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                              else:
                                    materiale = component+"-Z{:03d}".format(1)
                                    AluminiyProductTermo(artikul =component,section ='Z',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Печь старения'][key],material=materiale).save()
                                    df_new['SAP код Z'][key]=materiale
                                    umumiy_counter_termo[ component +'-Z'] = 1
                                    artikle = materiale.split('-')[0]
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                          
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                          
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"ZZZ tip pokr {row['Тип покрытия']}")  
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Печь старения'][key],
                                                      'section':'Z-Печь старения',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':'Неокрашенный',
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id':'',# row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':'',#row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':'',#row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':'',#row['Код лам пленки внутри'],
                                                      'anodization_contact':'',#row['Контактность анодировки'],
                                                      'anodization_type':'',#row['Тип анодировки'],
                                                      'anodization_method':'',#row['Способ анодировки'],
                                                      'print_view':'',#row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                              
                  
                  
                              
                  if ((row['Тип покрытия'] == 'Сублимированный') or (row['Тип покрытия'] == 'Ламинированный') or (row['Тип покрытия'] == 'Окрашенный') or (row['Тип покрытия'] == 'Белый')): 
                        termo_existP =AluminiyProductTermo.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['Покраска автомат'][key]).exists()
                        simple_existP =AluminiyProduct.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['Покраска автомат'][key]).exists()
                        if (termo_existP or simple_existP):
                              if termo_existP:
                                    df_new['SAP код P'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['Покраска автомат'][key])[:1].get().material
                              else:
                                    df_new['SAP код P'][key] = AluminiyProduct.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['Покраска автомат'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код P'][key],df_new['Покраска автомат'][key],'P'])
                        else: 
                              if '9016' in df_new['Покраска автомат'][key]:
                                    tip_pokr ='Белый'
                              else:
                                    tip_pokr ='Окрашенный'
                              if AluminiyProductTermo.objects.filter(artikul =component,section ='P').exists():
                                    umumiy_counter_termo[component+'-P'] += 1
                                    
                                    max_valuesP = umumiy_counter_termo[ component +'-P']
                                    materiale = component+"-P{:03d}".format(max_valuesP)
                                    AluminiyProductTermo(artikul =component,section ='P',counter=max_valuesP,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Покраска автомат'][key],material=materiale).save()
                                    df_new['SAP код P'][key]=materiale
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"p tip pokr {row['Тип покрытия']}")
                                    
                                    
                                    
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Покраска автомат'][key],
                                                      'section':'P-Покраска автомат',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':tip_pokr,
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                                    
                              else:
                                    materiale = component+"-P{:03d}".format(1)
                                    AluminiyProductTermo(artikul =component,section ='P',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Покраска автомат'][key],material=materiale).save()
                                    df_new['SAP код P'][key] = materiale
                                    umumiy_counter_termo[component+'-P'] = 1
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"p tip pokr {row['Тип покрытия']}")
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Покраска автомат'][key],
                                                      'section':'P-Покраска автомат',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':tip_pokr,
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                  
                  
                  
                  
                  
                  if row['Тип покрытия'] =='Сублимированный':
                        
                        termo_existS =AluminiyProductTermo.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['Сублимация'][key]).exists()
                        simple_existS =AluminiyProduct.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['Сублимация'][key]).exists()
                        if (termo_existS or simple_existS):
                              if termo_existS: 
                                    df_new['SAP код S'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['Сублимация'][key])[:1].get().material
                              else:
                                    df_new['SAP код S'][key] = AluminiyProduct.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['Сублимация'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код S'][key],df_new['Сублимация'][key],'S'])
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =component,section ='S').exists():
                                    umumiy_counter_termo[component+'-S'] += 1
                                    max_valuesS = umumiy_counter_termo[ component +'-S']
                                    materiale = component+"-S{:03d}".format(max_valuesS)
                                    AluminiyProductTermo(artikul =component,section ='S',counter=max_valuesS,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Сублимация'][key],material=materiale).save()
                                    df_new['SAP код S'][key]=materiale
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"S tip pokr {row['Тип покрытия']}")
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Сублимация'][key],
                                                      'section':'S-Сублимация',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':'Сублимированный',
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                              else:
                                    materiale = component+"-S{:03d}".format(1)
                                    AluminiyProductTermo(artikul =component,section ='S',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Сублимация'][key],material=materiale).save()
                                    df_new['SAP код S'][key]=materiale
                                    umumiy_counter_termo[component+'-S'] = 1
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    print(f"S tip pokr {row['Тип покрытия']}")
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Сублимация'][key],
                                                      'section':'S-Сублимация',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':'Сублимированный',
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                  
                  
                              
                  if row['Тип покрытия'] =='Анодированный':
                        termo_existA =AluminiyProductTermo.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['Анодировка'][key]).exists()
                        simple_existA =AluminiyProduct.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['Анодировка'][key]).exists()
                        if (termo_existA or simple_existA):
                              if termo_existA:
                                    df_new['SAP код A'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['Анодировка'][key])[:1].get().material
                              else:
                                    df_new['SAP код A'][key] = AluminiyProduct.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['Анодировка'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код A'][key],df_new['Анодировка'][key],'A'])
                        
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =component,section ='A').exists():
                                    umumiy_counter_termo[component+'-A'] += 1
                                    max_valuesA = umumiy_counter_termo[ component +'-A']
                                    materiale = component+"-A{:03d}".format(max_valuesA)
                                    AluminiyProductTermo(artikul =component,section ='A',counter=max_valuesA,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Анодировка'][key],material=materiale).save()
                                    df_new['SAP код A'][key]=materiale
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"A tip pokr {row['Тип покрытия']}")    
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Анодировка'][key],
                                                      'section':'A-Анодировка',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':'Анодированный',
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':'',#row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                              else:
                                    materiale = component+"-A{:03d}".format(1)
                                    AluminiyProductTermo(artikul =component,section ='A',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Анодировка'][key],material=materiale).save()
                                    df_new['SAP код A'][key]=materiale
                                    umumiy_counter_termo[component+'-A'] = 1
                                    artikle = materiale.split('-')[0]
                                    
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"A tip pokr {row['Тип покрытия']}")  
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Анодировка'][key],
                                                      'section':'A-Анодировка',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':'Анодированный',
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':'',#row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                  
                  
                              
                  if ((row['Код наклейки'] != 'NT1') and (row['Тип покрытия'] != 'Ламинированный')) :
                        if component in nakleyka_iskyucheniye:
                              continue
                        termo_existN =AluminiyProductTermo.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['Наклейка'][key]).exists()
                        simple_existN =AluminiyProduct.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['Наклейка'][key]).exists()
                        if (termo_existN or simple_existN):
                              if termo_existN:
                                    df_new['SAP код N'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['Наклейка'][key])[:1].get().material
                              else:
                                    df_new['SAP код N'][key] = AluminiyProduct.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['Наклейка'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код N'][key],df_new['Наклейка'][key],'N'])
                        else:
                              name_tip_pokr =''
                              if (('7777' in df_new['Наклейка'][key]) or ('8888' in df_new['Наклейка'][key])  or ('3701' in df_new['Наклейка'][key]) or ('3702' in df_new['Наклейка'][key])):
                                    name_tip_pokr = 'Сублимированный'
                              elif '9016' in df_new['Наклейка'][key]:
                                    name_tip_pokr = 'Белый'
                              elif 'MF' in df_new['Наклейка'][key]:
                                    name_tip_pokr = 'Неокрашенный'
                              elif anodirovaka_check(ANODIROVKA_CODE,df_new['Наклейка'][key]):
                                    name_tip_pokr = 'Анодированный'
                              else:
                                    name_tip_pokr = 'Окрашенный'
                              
                              if  AluminiyProductTermo.objects.filter(artikul =component,section ='N').exists():
                                    umumiy_counter_termo[component+'-N'] += 1
                                    max_valuesN = umumiy_counter_termo[ component +'-N']
                                    materiale = component+"-N{:03d}".format(max_valuesN)
                                    AluminiyProductTermo(artikul =component,section ='N',counter=max_valuesN,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Наклейка'][key],material=materiale).save()
                                    df_new['SAP код N'][key]=materiale
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"N tip pokr {row['Тип покрытия']}")      
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Наклейка'][key],
                                                      'section':'N-Наклейка',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':name_tip_pokr,
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':'',#row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                              else:
                                    materiale = component+"-N{:03d}".format(1)
                                    AluminiyProductTermo(artikul =component,section ='N',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Наклейка'][key],material=materiale).save()
                                    df_new['SAP код N'][key]=materiale
                                    umumiy_counter_termo[component+'-N'] = 1
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    print(f"N tip pokr {row['Тип покрытия']}")  
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Наклейка'][key],
                                                      'section':'N-Наклейка',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':name_tip_pokr,
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':'',#row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                  
      
      df_char = create_characteristika(cache_for_cratkiy_text) 
      
      df_char_title =create_characteristika_utils(cache_for_cratkiy_text)

      
      parent_dir ='{MEDIA_ROOT}\\uploads\\aluminiytermo\\'
       
      if not os.path.isdir(parent_dir):
            create_folder(f'{MEDIA_ROOT}\\uploads\\','aluminiytermo')
            
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\',f'{year}')
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\',f'{month}')
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\',day)
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\',hour)
            
            
      if not os.path.isfile(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\alumin_new_termo-{minut}.xlsx'):
            path =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\alumin_new_termo-{minut}.xlsx'
            path_ramka_norma =f'uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\norma-{minut}.xlsx'
      else:
            st =random.randint(0,1000)
            path =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\alumin_new_termo-{minut}-{st}.xlsx'
            path_ramka_norma =f'uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\norma-{minut}-{st}.xlsx'
            
      if  len(duplicat_list)>0:     
            df_duplicates =pd.DataFrame(np.array(duplicat_list),columns=['SAP CODE','KRATKIY TEXT','SECTION'])
      else:
            df_duplicates =pd.DataFrame(np.array([['','','']]),columns=['SAP CODE','KRATKIY TEXT','SECTION'])

      
      # df_char_title_full = pd.DataFrame(df_char_title)
      # characteristika_created_txt_create(df_char_title_full)
      df_new = df_new.replace('nan','')

      razlovka_yoq = True
      for key,razlov in df_new.iterrows():
            if razlov['SAP код 7']!="":
                  if not RazlovkaTermo.objects.filter(sap_code7=razlov['SAP код 7'],kratkiy7=razlov['U-Упаковка + Готовая Продукция']).exists():
                        razlovka_yoq = True
                        razlovka_komb = RazlovkaTermo(
                              parent_id=0,
                              esap_code =razlov['SAP код E'],
                              ekratkiy =razlov['Экструзия холодная резка'],
                              zsap_code =razlov['SAP код Z'],
                              zkratkiy =razlov['Печь старения'],
                              psap_code =razlov['SAP код P'],
                              pkratkiy =razlov['Покраска автомат'],
                              ssap_code =razlov['SAP код S'],
                              skratkiy =razlov['Сублимация'],
                              asap_code =razlov['SAP код A'],
                              akratkiy =razlov['Анодировка'],
                              nsap_code =razlov['SAP код N'],
                              nkratkiy =razlov['Наклейка'],
                              ksap_code =razlov['SAP код K'],
                              kratkiy =razlov['K-Комбинирования'],
                              lsap_code =razlov['SAP код L'],
                              lkratkiy =razlov['Ламинация'],
                              sap_code7 =razlov['SAP код 7'],
                              kratkiy7 =razlov['U-Упаковка + Готовая Продукция']
                        )
                        razlovka_komb.save()
                  else:
                        razlovka_yoq = False 
            
            else:
                  if razlovka_yoq:
                        RazlovkaTermo(
                              parent_id=razlovka_komb.id,
                              esap_code =razlov['SAP код E'],
                              ekratkiy =razlov['Экструзия холодная резка'],
                              zsap_code =razlov['SAP код Z'],
                              zkratkiy =razlov['Печь старения'],
                              psap_code =razlov['SAP код P'],
                              pkratkiy =razlov['Покраска автомат'],
                              ssap_code =razlov['SAP код S'],
                              skratkiy =razlov['Сублимация'],
                              asap_code =razlov['SAP код A'],
                              akratkiy =razlov['Анодировка'],
                              nsap_code =razlov['SAP код N'],
                              nkratkiy =razlov['Наклейка'],
                              ksap_code =razlov['SAP код K'],
                              kratkiy =razlov['K-Комбинирования'],
                              lsap_code =razlov['SAP код L'],
                              lkratkiy =razlov['Ламинация'],
                              sap_code7 =razlov['SAP код 7'],
                              kratkiy7 =razlov['U-Упаковка + Готовая Продукция']
                        ).save()

      
      for key,razlov in df_char.iterrows():
            if not Characteristika.objects.filter(sap_code=razlov['SAP CODE'],kratkiy_text=razlov['KRATKIY TEXT']).exists():
                  Characteristika(
                        sap_code =razlov['SAP CODE'],
                        kratkiy_text =razlov['KRATKIY TEXT'],
                        section =razlov['SECTION'],
                        savdo_id =razlov['SAVDO_ID'],
                        savdo_name =razlov['SAVDO_NAME'],
                        export_customer_id =razlov['EXPORT_CUSTOMER_ID'],
                        system =razlov['SYSTEM'],
                        article =razlov['ARTICLE'],
                        length =razlov['LENGTH'],
                        surface_treatment =razlov['SURFACE_TREATMENT'],
                        alloy =razlov['ALLOY'],
                        temper =razlov['TEMPER'],
                        combination =razlov['COMBINATION'],
                        outer_side_pc_id =razlov['OUTER_SIDE_PC_ID'],
                        outer_side_pc_brand =razlov['OUTER_SIDE_PC_BRAND'],
                        inner_side_pc_id =razlov['INNER_SIDE_PC_ID'],
                        inner_side_pc_brand =razlov['INNER_SIDE_PC_BRAND'],
                        outer_side_wg_s_id =razlov['OUTER_SIDE_WG_S_ID'],
                        inner_side_wg_s_id =razlov['INNER_SIDE_WG_S_ID'],
                        outer_side_wg_id =razlov['OUTER_SIDE_WG_ID'],
                        inner_side_wg_id =razlov['INNER_SIDE_WG_ID'],
                        anodization_contact =razlov['ANODIZATION_CONTACT'],
                        anodization_type =razlov['ANODIZATION_TYPE'],
                        anodization_method =razlov['ANODIZATION_METHOD'],
                        print_view =razlov['PRINT_VIEW'],
                        profile_base =razlov['PROFILE_BASE'],
                        width =razlov['WIDTH'],
                        height =razlov['HEIGHT'],
                        category =razlov['CATEGORY'],
                        rawmat_type =razlov['RAWMAT_TYPE'],
                        benkam_id =razlov['BENKAM_ID'],
                        hollow_and_solid =razlov['HOLLOW AND SOLID'],
                        export_description =razlov['EXPORT_DESCRIPTION'],
                        export_description_eng =razlov['EXPORT_DESCRIPTION ENG'],
                        tnved =razlov['TNVED'],
                        surface_treatment_export =razlov['SURFACE_TREATMENT_EXPORT'],
                        wms_width =razlov['WMS_WIDTH'],
                        wms_height =razlov['WMS_HEIGHT'],
                        group_prise =''					
                  ).save()
      for key,razlov in df_char_title.iterrows():
            if not CharacteristicTitle.objects.filter(sap_код_s4p_100 = razlov['SAP код S4P 100']).exists():
                  CharacteristicTitle(
                        дата_изменение_добавление =razlov['Дата изменение добавление'], 
                        статус_изменение_добавление =razlov['Статус изменение добавление'], 
                        ссылки_для_чертежа =razlov['Ссылки для чертежа'], 
                        sap_код_s4p_100 =razlov['SAP код S4P 100'], 
                        нумерация_до_sap =razlov['Нумерация до SAP'], 
                        короткое_название_sap =razlov['Короткое название SAP'], 
                        польное_наименование_sap =razlov['Польное наименование SAP'], 
                        ед_изм =razlov['Ед, Изм,'], 
                        альтернативная_ед_изм =razlov['Альтернативная ед, изм'], 
                        коэфициент_пересчета =razlov['Коэфициент пересчета'], 
                        участок =razlov['Участок'], 
                        альтернативный_участок =razlov['Альтернативный участок'], 
                        длина =razlov['Длина'], 
                        ширина =razlov['Ширина'], 
                        высота =razlov['Высота'], 
                        группа_материалов =razlov['группа материалов'], 
                        удельный_вес_за_метр =razlov['Удельный вес за метр'], 
                        общий_вес_за_штуку =razlov['Общий вес за штуку'],
                        price =razlov['Price']
                  ).save()
      
      
      writer = pd.ExcelWriter(path, engine='xlsxwriter')
      df_new.to_excel(writer,index=False,sheet_name ='Schotchik')
      df_char.to_excel(writer,index=False,sheet_name ='Characteristika')
      df_char_title.to_excel(writer,index=False,sheet_name ='title')
      df_duplicates.to_excel(writer,index=False,sheet_name='Duplicates')
      writer.close()
      return redirect('upload_product_termo')
                  
@login_required(login_url='/accounts/login/')
def product_add_second_org(request,id):
      file = AluFileTermo.objects.get(id=id).file
      df = pd.read_excel(f'{MEDIA_ROOT}/{file}')
      df =df.astype(str)
      
      now = datetime.now()
      year =now.strftime("%Y")
      month =now.strftime("%B")
      day =now.strftime("%a%d")
      hour =now.strftime("%H HOUR")
      minut =now.strftime("%M")
      
      nakleyka_iskyucheniye =NakleykaIskyuchenie.objects.all().values_list('sap_code',flat=True)
      doesnotexist,correct = check_for_correct(df)
      if not correct:
            context ={
                  'CharUtilsOne':doesnotexist[0],
                  'CharUtilsTwo':doesnotexist[1],
                  'BazaProfile':doesnotexist[2]
            }
            df_char_utils_one = pd.DataFrame({
                  'матрица':doesnotexist[0],
                  'артикул':doesnotexist[0],
                  'высота':['' for i in doesnotexist[0]],
                  'ширина':['' for i in doesnotexist[0]],
                  'высота_ширина':['' for i in doesnotexist[0]],
                  'systems':['' for i in doesnotexist[0]]
                  })
            df_char_utils_two =pd.DataFrame({
                  'артикул':doesnotexist[1],
                  'полый_или_фасонный':['' for i in doesnotexist[1]]
            })

            df_baza_profiley =pd.DataFrame({
                  'артикул':[i[0] for i in doesnotexist[2]],
                  'серия':[i[1] for i in doesnotexist[2]],
                  'старый_код':[i[2] for i in doesnotexist[2]],
                  'компонент':[i[3] for i in doesnotexist[2]],
                  'product_description':[i[4] for i in doesnotexist[2]],
                  'link':[i[5] for i in doesnotexist[2]],
            })
            create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}','Not Exists')
            
            path_not_exists =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\Not Exists\\Not_Exists.xlsx'
            
            if os.path.isfile(path_not_exists):
                  try:
                        os.remove(path_not_exists)
                  except:
                        return render(request,'utils/file_exist_org.html')
            
            writer = pd.ExcelWriter(path_not_exists, engine='xlsxwriter')
            df_char_utils_one.to_excel(writer,index=False,sheet_name ='character utils one')
            df_char_utils_two.to_excel(writer,index=False,sheet_name ='character utils two')
            df_baza_profiley.to_excel(writer,index=False,sheet_name ='baza profile')
            writer.close()

            order_id = request.GET.get('order_id',None)
            if order_id:
                  order = Order.objects.get(id = order_id)
                  paths = order.paths
                  l_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                  paths['termo_lack_file']= path_not_exists
                  paths['l_created_at']= l_created_at
                  paths['status_l']= 'on process'
                  order.paths = paths
                  order.alumin_wrongs = request.user
                  order.current_worker = request.user
                  order.work_type = 3
                  order.save()
                  context['order'] = order
                  paths =  order.paths
                  for key,val in paths.items():
                        context[key] = val
                  
                  return render(request,'order/order_detail.html',context)

            return render(request,'utils/components.html',context)
      ################### group by#########
      aluminiy_group = AluminiyProduct.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
      umumiy_counter={}
      for al in aluminiy_group:
            umumiy_counter[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      ################ termo max ########
      aluminiy_group_termo = AluminiyProductTermo.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
      umumiy_counter_termo = {}
      for al in aluminiy_group_termo:
            umumiy_counter_termo[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      ############################ end grouby ######
      
      
      a=datetime.now()
      for key,row in df.iterrows():
            if row['Тип покрытия'] == 'nan':
                  df = df.drop(key)
      
      
      df_new =pd.DataFrame()
      df_new['Название системы']=df['Название системы']
      df_new['SAP код E']=''
      df_new['Экструзия холодная резка']=''
      df_new['SAP код Z']=''
      df_new['Печь старения']=''
      df_new['SAP код P']=''
      df_new['Покраска автомат']=''
      df_new['SAP код S']=''
      df_new['Сублимация']=''
      df_new['SAP код A']=''
      df_new['Анодировка']=''
      df_new['SAP код N']=''
      df_new['Наклейка']=''
      df_new['SAP код K']=''
      df_new['K-Комбинирования']=''
      df_new['SAP код L']=''
      df_new['Ламинация']=''
      df_new['SAP код 7']=''
      df_new['U-Упаковка + Готовая Продукция']=''
      df_new['SAP код F']=''
      df_new['Фабрикация']=''
      df_new['SAP код 75']=''
      df_new['U-Упаковка + Готовая Продукция 75']=''
      

      exturision_list = []
      
      
      cache_for_cratkiy_text =[]
      
      for key,row in df.iterrows():
            print(key)
            row['Сплав'] = row['Сплав'].replace('.0','')
            row['Сплав'] = row['Сплав'].replace('.0','')
            row['Длина (мм)'] = row['Длина (мм)'].replace('.0','')
            row['Бренд краски снаружи'] = row['Бренд краски снаружи'].replace('.0','')
            row['Код краски снаружи'] = row['Код краски снаружи'].replace('.0','')
            row['Бренд краски внутри'] = row['Бренд краски внутри'].replace('.0','')
            row['Код краски внутри'] = row['Код краски внутри'].replace('.0','')
            row['Код декор пленки снаружи'] = row['Код декор пленки снаружи'].replace('.0','')
            row['Цвет декор пленки снаружи'] = row['Цвет декор пленки снаружи'].replace('.0','')
            row['Код декор пленки внутри'] = row['Код декор пленки внутри'].replace('.0','')
            row['Код цвета анодировки внутри'] = row['Код цвета анодировки внутри'].replace('.0','')
            row['Код цвета анодировки снаружи'] = row['Код цвета анодировки снаружи'].replace('.0','')
            row['Контактность анодировки'] = row['Контактность анодировки'].replace('.0','')
            row['Код лам пленки снаружи'] = row['Код лам пленки снаружи'].replace('.0','')
            row['Код лам пленки внутри'] = row['Код лам пленки внутри'].replace('.0','')
            row['Код лам пленки внутри'] = row['Код лам пленки внутри'].replace('.0','')
            
            
            
            artikul = df['Артикул'][key]
            component = df['Компонент'][key]
            
            duplicat_list =[]
            
            if artikul !='nan':
                  print('artikulllllllll')
                  if df['Длина при выходе из пресса'][key] != 'nan':
                        dlina = df['Длина при выходе из пресса'][key].replace('.0','')
                              
                        df_new['Фабрикация'][key]=fabrikatsiya_sap_kod(df['Краткий текст товара'][key],df['Длина (мм)'][key])
                        df_new['U-Упаковка + Готовая Продукция 75'][key]=fabrikatsiya_sap_kod(df['Краткий текст товара'][key],df['Длина (мм)'][key])
                        
                        if df['Тип покрытия'][key] != 'Ламинированный':
                              df_new['K-Комбинирования'][key] = fabrikatsiya_sap_kod(df['Краткий текст товара'][key],df['Длина при выходе из пресса'][key].replace('.0',''))
                        else:
                              df_new['K-Комбинирования'][key] = fabrikatsiya_sap_kod(df['Краткий текст товара'][key].split('_')[0] +' NT1',df['Длина при выходе из пресса'][key].replace('.0',''))
                        
                        if df['Тип покрытия'][key] == 'Ламинированный':
                              plenki1 = False
                              plenki2 = False
                              if df['Код лам пленки снаружи'][key] != 'nan':
                                    laminatsiya =row['Код лам пленки снаружи'].replace('.0','')+'/XXXX'
                                    plenki1 = True
                                    
                              if df['Код лам пленки внутри'][key] != 'nan':
                                    laminatsiya ='XXXX/'+df['Код лам пленки внутри'][key].replace('.0','')
                                    plenki2 =True
                                    
                              if plenki1 and plenki2:
                                    laminatsiya =df['Код лам пленки снаружи'][key].replace('.0','') +'/'+ df['Код лам пленки внутри'][key].replace('.0','')
                                    
                              ll =row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')+'/'+df['Код краски внутри'][key].replace('.0','')+'_'+laminatsiya +' ' +row['Код наклейки']
                              df_new['Ламинация'][key] = fabrikatsiya_sap_kod(ll,df['Длина при выходе из пресса'][key].replace('.0',''))

                  else:
                        dlina = df['Длина (мм)'][key]
                        df_new['U-Упаковка + Готовая Продукция'][key] = df['Краткий текст товара'][key]
                        
                        if df['Тип покрытия'][key] != 'Ламинированный': 
                              df_new['K-Комбинирования'][key] = df['Краткий текст товара'][key]
                        else: 
                              df_new['K-Комбинирования'][key] = df['Краткий текст товара'][key].split('_')[0] +' NT1'
                        
                        if df['Тип покрытия'][key] == 'Ламинированный':
                              plenki1 = False
                              plenki2 = False
                              if row['Код лам пленки снаружи'] != 'nan':
                                    laminatsiya =row['Код лам пленки снаружи'].replace('.0','')+'/XXXX'
                                    plenki1 = True
                                    
                              if df['Код лам пленки внутри'][key] != 'nan':
                                    laminatsiya ='XXXX/'+df['Код лам пленки внутри'][key].replace('.0','')
                                    plenki2 =True
                                    
                              if plenki1 and plenki2:
                                    laminatsiya =df['Код лам пленки снаружи'][key].replace('.0','') +'/'+ df['Код лам пленки внутри'][key].replace('.0','')
                                    
                              df_new['Ламинация'][key] = df['Краткий текст товара'][key]
                        
                  if df['Длина при выходе из пресса'][key] != 'nan':
                        if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='F',kratkiy_tekst_materiala=df_new['Фабрикация'][key]).exists():
                              df_new['SAP код F'][key] = AluminiyProductTermo.objects.filter(artikul = df['Артикул'][key],section ='F',kratkiy_tekst_materiala=df_new['Фабрикация'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код Ф'][key],df_new['Фабрикация'][key],'F'])
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='F').exists():
                                    umumiy_counter_termo[df['Артикул'][key]+'-F'] += 1
                                    max_valuesF = umumiy_counter_termo[df['Артикул'][key]+'-F']
                                    materiale = df['Артикул'][key] +"-F{:03d}".format(max_valuesF)
                                    AluminiyProductTermo(artikul =df['Артикул'][key],section ='F',counter=max_valuesF,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Фабрикация'][key],material=materiale).save()
                                    df_new['SAP код F'][key]=materiale
                                    artikle = materiale.split('-')[0]
                              
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Фабрикация'][key],
                                                      'section':'F-Фабрикация',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':row['Тип покрытия'],
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                              else:
                                    materiale = df['Артикул'][key] +"-F{:03d}".format(1)
                                    AluminiyProductTermo(artikul =df['Артикул'][key],section ='F',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Фабрикация'][key],material=materiale).save()
                                    df_new['SAP код F'][key]=materiale
                                    umumiy_counter_termo[df['Артикул'][key]+'-F'] = 1
                                    artikle = materiale.split('-')[0]
                              
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Фабрикация'][key],
                                                      'section':'F-Фабрикация',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':row['Тип покрытия'],
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                                    
                        
                        
                        if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='75',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key]).exists():
                              df_new['SAP код 75'][key] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='75',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код 75'][key],df_new['U-Упаковка + Готовая Продукция 75'][key],'75'])
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='75').exists():
                                    umumiy_counter_termo[df['Артикул'][key]+'-75'] += 1
                                    max_values75 = umumiy_counter_termo[df['Артикул'][key]+'-75']
                                    
                                    if max_values75 <= 99:
                                          materiale = df['Артикул'][key]+"-75{:02d}".format(max_values75)
                                    else:
                                          counter =7500 + max_values75
                                          materiale = df['Артикул'][key]+"-{:04d}".format(counter)
                                          
                                          
                                    AluminiyProductTermo(artikul =df['Артикул'][key],section ='75',counter=max_values75,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key],material=materiale).save()
                                    df_new['SAP код 75'][key] = materiale
                                    
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    surface_treatment_export=''
                                    if row['Тип покрытия'].lower() =='неокрашенный':
                                          surface_treatment_export ='Неокрашенный'
                                    elif ((row['Тип покрытия'].lower() =='окрашенный') or (row['Тип покрытия'].lower() =='белый')):
                                          surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']]+" " + row['Код краски снаружи']
                                    elif row['Тип покрытия'].lower() =='сублимированный':
                                          surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                                    elif row['Тип покрытия'].lower() =='анодированный':
                                          surface_treatment_export = str(row['Код цвета анодировки снаружи']).replace('.0','')
                                    elif row['Тип покрытия'].lower() =='ламинированный':
                                          if (row['Цвет лам пленки снаружи']=='XXXX' or row['Цвет лам пленки снаружи']=='nan'):
                                                surface_treatment_export = svet_lam_plenke_VN[row['Цвет лам пленки внутри']]                  
                                          else:
                                                if (row['Цвет лам пленки внутри']=='XXXX' or row['Цвет лам пленки внутри']=='nan'):
                                                      surface_treatment_export = svet_lam_plenke_NA[row['Цвет лам пленки снаружи']] 
                                                else:
                                                      surface_treatment_export = svet_lam_plenke_POL[row['Цвет лам пленки снаружи']]
                                          
                                    
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['U-Упаковка + Готовая Продукция 75'][key],
                                                      'section':'V-Упаковка + Готовая продукция',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':row['Тип покрытия'],
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ГП',
                                                      'hollow_and_solid':hollow_and_solid,
                                                      'export_description':export_description,
                                                      'export_description_eng':export_description_eng.bux_name_eng,
                                                      'tnved':export_description_eng.tnved,
                                                      'surface_treatment_export':surface_treatment_export,# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                              
                              else:
                                    materiale = df['Артикул'][key]+"-75{:02d}".format(1)
                                    AluminiyProductTermo(artikul = df['Артикул'][key],section ='75',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key],material=materiale).save()
                                    df_new['SAP код 75'][key] = materiale 
                                    umumiy_counter_termo[df['Артикул'][key]+'-75'] = 1
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    surface_treatment_export=''
                                    if row['Тип покрытия'].lower() =='неокрашенный':
                                          surface_treatment_export ='Неокрашенный'
                                    elif ((row['Тип покрытия'].lower() =='окрашенный') or (row['Тип покрытия'].lower() =='белый')):
                                          surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']] +' ' +row['Код краски снаружи']
                                    elif row['Тип покрытия'].lower() =='сублимированный':
                                          surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                                    elif row['Тип покрытия'].lower() =='анодированный':
                                          surface_treatment_export = str(row['Код цвета анодировки снаружи']).replace('.0','')
                                    elif row['Тип покрытия'].lower() =='ламинированный':
                                          if (row['Цвет лам пленки снаружи']=='XXXX' or row['Цвет лам пленки снаружи']=='nan'):
                                                surface_treatment_export = svet_lam_plenke_VN[row['Цвет лам пленки внутри']]                  
                                          else:
                                                if (row['Цвет лам пленки внутри']=='XXXX' or row['Цвет лам пленки внутри']=='nan'):
                                                      surface_treatment_export = svet_lam_plenke_NA[row['Цвет лам пленки снаружи']] 
                                                else:
                                                      surface_treatment_export = svet_lam_plenke_POL[row['Цвет лам пленки снаружи']]
                                          
                                    
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['U-Упаковка + Готовая Продукция 75'][key],
                                                      'section':'V-Упаковка + Готовая продукция',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':row['Тип покрытия'],
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ГП',
                                                      'hollow_and_solid':hollow_and_solid,
                                                      'export_description':export_description,
                                                      'export_description_eng':export_description_eng.bux_name_eng,
                                                      'tnved':export_description_eng.tnved,
                                                      'surface_treatment_export':surface_treatment_export,# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                  else:     
                        if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key]).exists():
                              df_new['SAP код 7'][key] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код 7'][key],df_new['U-Упаковка + Готовая Продукция'][key],'75'])
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul=df['Артикул'][key],section ='7').exists():
                                    umumiy_counter_termo[df['Артикул'][key]+'-7'] += 1
                                    max_values7 = umumiy_counter_termo[df['Артикул'][key]+'-7']
                                    materiale = df['Артикул'][key]+"-7{:03d}".format(max_values7)
                                    AluminiyProductTermo(artikul = df['Артикул'][key],section ='7',counter=max_values7,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key],material=materiale).save()
                                    df_new['SAP код 7'][key] = materiale
                                    artikle = str(materiale).split('-')[0]
                                   
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    # print(export_description)
                                    # print(df_new['SAP код 7'][key],key)
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    surface_treatment_export=''
                                    if row['Тип покрытия'].lower() =='неокрашенный':
                                          surface_treatment_export ='Неокрашенный'
                                    elif ((row['Тип покрытия'].lower() =='окрашенный') or (row['Тип покрытия'].lower() =='белый')):
                                          surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']] + ' ' + row['Код краски снаружи']
                                    elif row['Тип покрытия'].lower() =='сублимированный':
                                          surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                                    elif row['Тип покрытия'].lower() =='анодированный':
                                          surface_treatment_export = str(row['Код цвета анодировки снаружи']).replace('.0','')
                                    elif row['Тип покрытия'].lower() =='ламинированный':
                                          if (row['Цвет лам пленки снаружи']=='XXXX' or row['Цвет лам пленки снаружи']=='nan'):
                                                surface_treatment_export = svet_lam_plenke_VN[row['Цвет лам пленки внутри']]                  
                                          else:
                                                if (row['Цвет лам пленки внутри']=='XXXX' or row['Цвет лам пленки внутри']=='nan'):
                                                      surface_treatment_export = svet_lam_plenke_NA[row['Цвет лам пленки снаружи']] 
                                                else:
                                                      surface_treatment_export = svet_lam_plenke_POL[row['Цвет лам пленки снаружи']]
                                          
                                   
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['U-Упаковка + Готовая Продукция'][key],
                                                      'section':'U-Упаковка + Готовая продукция',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':row['Тип покрытия'],
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ГП',
                                                      'hollow_and_solid':hollow_and_solid,
                                                      'export_description':export_description,
                                                      'export_description_eng':export_description_eng.bux_name_eng,
                                                      'tnved':export_description_eng.tnved,
                                                      'surface_treatment_export':surface_treatment_export,# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                              
                              else:
                                    materiale = df['Артикул'][key]+"-7{:03d}".format(1)
                                    AluminiyProductTermo(artikul = df['Артикул'][key],section ='7',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key],material=materiale).save()
                                    df_new['SAP код 7'][key] = materiale
                                    umumiy_counter_termo[df['Артикул'][key]+'-7'] = 1
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    print(export_description)
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    surface_treatment_export=''
                                    if row['Тип покрытия'].lower() =='неокрашенный':
                                          surface_treatment_export ='Неокрашенный'
                                    elif ((row['Тип покрытия'].lower() =='окрашенный') or (row['Тип покрытия'].lower() =='белый')):
                                          surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']] +' ' + row['Код краски снаружи']
                                    elif row['Тип покрытия'].lower() =='сублимированный':
                                          surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                                    elif row['Тип покрытия'].lower() =='анодированный':
                                          surface_treatment_export = str(row['Код цвета анодировки снаружи']).replace('.0','')
                                    elif row['Тип покрытия'].lower() =='ламинированный':
                                          if (row['Цвет лам пленки снаружи']=='XXXX' or row['Цвет лам пленки снаружи']=='nan'):
                                                surface_treatment_export = svet_lam_plenke_VN[row['Цвет лам пленки внутри']]                  
                                          else:
                                                if (row['Цвет лам пленки внутри']=='XXXX' or row['Цвет лам пленки внутри']=='nan'):
                                                      surface_treatment_export = svet_lam_plenke_NA[row['Цвет лам пленки снаружи']] 
                                                else:
                                                      surface_treatment_export = svet_lam_plenke_POL[row['Цвет лам пленки снаружи']]
                                          
                                    print(f"Ukrat1 tip pokr {row['Тип покрытия']}")
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['U-Упаковка + Готовая Продукция'][key],
                                                      'section':'U-Упаковка + Готовая продукция',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':row['Тип покрытия'],
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ГП',
                                                      'hollow_and_solid':hollow_and_solid,
                                                      'export_description':export_description,
                                                      'export_description_eng':export_description_eng.bux_name_eng,
                                                      'tnved':export_description_eng.tnved,
                                                      'surface_treatment_export':surface_treatment_export,# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                              
                        ##### kombirinovanniy
                  
                  if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='K',kratkiy_tekst_materiala=df_new['K-Комбинирования'][key]).exists():
                        df_new['SAP код K'][key] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='K',kratkiy_tekst_materiala=df_new['K-Комбинирования'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код K'][key],df_new['K-Комбинирования'][key],'K'])
                  else: 
                        
                        name_tip_pokr =''
                        if (('7777' in df_new['K-Комбинирования'][key]) or ('8888' in df_new['K-Комбинирования'][key])  or ('3701' in df_new['K-Комбинирования'][key]) or ('3702' in df_new['K-Комбинирования'][key])):
                              name_tip_pokr = 'Сублимированный'
                        elif '9016' in df_new['K-Комбинирования'][key]:
                              name_tip_pokr = 'Белый'
                        elif 'MF' in df_new['K-Комбинирования'][key]:
                              name_tip_pokr = 'Неокрашенный'
                        elif anodirovaka_check(ANODIROVKA_CODE,df_new['K-Комбинирования'][key]):
                              name_tip_pokr = 'Анодированный'
                        else:
                              name_tip_pokr = 'Окрашенный'
                              
                        if AluminiyProductTermo.objects.filter(artikul=df['Артикул'][key],section ='K').exists():
                              umumiy_counter_termo[df['Артикул'][key]+'-K'] += 1
                              max_valuesK = umumiy_counter_termo[df['Артикул'][key]+'-K']
                              materiale = df['Артикул'][key]+"-K{:03d}".format(max_valuesK)
                              AluminiyProductTermo(artikul = df['Артикул'][key],section ='K',counter=max_valuesK,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['K-Комбинирования'][key],material=materiale).save()
                              df_new['SAP код K'][key] = materiale
                              
                              artikle = str(materiale).split('-')[0]
                              
                              
                              hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                              
                              width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                              
                              print(f"K-Комбинирования tip pokr {row['Тип покрытия']}") 
                              
                              
                                    
                                    
                                  
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['K-Комбинирования'][key],
                                                'section':'K-Комбинирования',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':name_tip_pokr,
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':width_and_height.ширина,
                                                'wms_height':width_and_height.высота,
                                                'group_prise': export_description_eng.group_price,
                                                }
                                          )
                                      
                        else:
                              materiale = df['Артикул'][key]+"-K{:03d}".format(1)
                              AluminiyProductTermo(artikul = df['Артикул'][key],section ='K',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['K-Комбинирования'][key],material=materiale).save()
                              df_new['SAP код K'][key] = materiale
                              umumiy_counter_termo[df['Артикул'][key]+'-K'] = 1
                              artikle = materiale.split('-')[0]
                              
                              hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                              
                              width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                              
                              print(f"K-Комбинирования tip pokr {row['Тип покрытия']}")
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['K-Комбинирования'][key],
                                                'section':'K-Комбинирования',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':name_tip_pokr,
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':width_and_height.ширина,
                                                'wms_height':width_and_height.высота,
                                                'group_prise': export_description_eng.group_price,
                                                }
                                          )
                              
                  
                  if df['Тип покрытия'][key] == 'Ламинированный':      
                        if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='L',kratkiy_tekst_materiala=df_new['Ламинация'][key]).exists():
                              df_new['SAP код L'][key] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='L',kratkiy_tekst_materiala=df_new['Ламинация'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код L'][key],df_new['Ламинация'][key],'L'])
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='L').exists():
                                    umumiy_counter_termo[df['Артикул'][key]+'-L'] += 1
                                    max_valuesL = umumiy_counter_termo[ df['Артикул'][key] +'-L']
                                    materiale = df['Артикул'][key]+"-L{:03d}".format(max_valuesL)
                                    AluminiyProductTermo(artikul =df['Артикул'][key],section ='L',counter=max_valuesL,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Ламинация'][key],material=materiale).save()
                                    df_new['SAP код L'][key]=materiale
                                    artikle = materiale.split('-')[0]
                                    
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"Ламинация1 tip pokr {row['Тип покрытия']}")   
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Ламинация'][key],
                                                      'section':'L-Ламинирование',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':'Ламинированный',
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                              else:
                                    materiale = df['Артикул'][key]+"-L{:03d}".format(1)
                                    AluminiyProductTermo(artikul =df['Артикул'][key],section ='L',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Ламинация'][key],material=materiale).save()
                                    df_new['SAP код L'][key]=materiale
                                    umumiy_counter_termo[df['Артикул'][key]+'-L'] = 1
                                    
                                    artikle = materiale.split('-')[0]
                                    
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    print(f"Ukrat1 tip pokr {row['Тип покрытия']}")
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Ламинация'][key],
                                                      'section':'L-Ламинирование',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':'Ламинированный',
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
            elif  component !='nan':
                  dlina =''
            
                  if df['Длина при выходе из пресса'][key] != 'nan':
                        dlina = df['Длина при выходе из пресса'][key].replace('.0','')      
                  else:
                        dlina = df['Длина (мм)'][key]
                        
                        
                  df_new['Экструзия холодная резка'][key] = row['Сплав'][len(row['Сплав'])-2:] +'T4 '+'L'+dlina+' MF'
                  if row['тип закаленности']!='T4':
                        df_new['Печь старения'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' MF'
                  
                  
                              
                  if ((row['Тип покрытия'] == 'Окрашенный') or (row['Тип покрытия'] == 'Белый' )):
                        df_new['Покраска автомат'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи']+row['Код краски снаружи']
                        if row['Код наклейки'] != 'NT1':
                              df_new['Наклейка'][key] = df_new['Покраска автомат'][key] +' '+ row['Код наклейки'].replace('.0','')
                  
                  
                              
                  elif row['Тип покрытия'] == 'Ламинированный':
                        df_new['Покраска автомат'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи']+row['Код краски снаружи']
                        
                  
                  elif row['Тип покрытия'] =='Сублимированный':
                        df_new['Покраска автомат'][key]=row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')
                        df_new['Сублимация'][key]=row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')+'_'+row['Код декор пленки снаружи'].replace('.0','')
                        
                        if row['Код наклейки'] != 'NT1':
                              df_new['Наклейка'][key]=df_new['Сублимация'][key] + ' ' + row['Код наклейки'].replace('.0','')

                  elif row['Тип покрытия'] =='Анодированный':
                        df_new['Анодировка'][key]=row['Сплав'][len(row['Сплав'])-2:] +row['тип закаленности']+' L'+dlina+' '+row['Код цвета анодировки снаружи'].replace('.0','')
                        if row['Код наклейки'] != 'NT1':
                              df_new['Наклейка'][key]= df_new['Анодировка'][key] +' '+row['Контактность анодировки']+' ' + row['Код наклейки'].replace('.0','')
                  else:
                        print("<<<<<< Нет Тип покрытия ! >>>>>>")
                  
                  termo_existE = AluminiyProductTermo.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key]).exists()
                  simple_existE = AluminiyProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key]).exists()
                  # print('existsance = ',termo_existE,simple_existE)
                  if (termo_existE or simple_existE):
                        if termo_existE:
                              sap_code_e = AluminiyProductTermo.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key])[:1].get().material
                        else:
                              
                              sap_code_e = AluminiyProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key])[:1].get().material
                        df_new['SAP код E'][key] = sap_code_e
                        duplicat_list.append([df_new['SAP код E'][key],df_new['Экструзия холодная резка'][key],'E'])
                        
                        if row['тип закаленности']=='T4':
                              exturision_list.append(sap_code_e)
                  else:
                        if AluminiyProductTermo.objects.filter(artikul =component,section ='E').exists():
                              # max_valuesE = AluminiyProductTermo.objects.filter(artikul =component,section ='E').values('section').annotate(total_max=Max('counter'))[0]['total_max']
                              umumiy_counter_termo[component+'-E'] += 1
                              max_valuesE = umumiy_counter_termo[component+'-E']
                              materiale = component+"-E{:03d}".format(max_valuesE)
                              AluminiyProductTermo(artikul =component,section ='E',counter=max_valuesE,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key],material=materiale).save()
                              df_new['SAP код E'][key]=materiale
                              

                              if row['тип закаленности']=='T4':
                                    exturision_list.append(sap_code_e)

                              artikle = materiale.split('-')[0]
                              
                              hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                              
                              width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Экструзия холодная резка'][key],
                                                'section':'E-Экструзия холодная резка ZPP2',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':'Неокрашенный',
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id':'',# row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':'',#row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':'',
                                                'inner_side_wg_s_id':'',
                                                'outer_side_wg_id':'',#row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':'',#row['Код лам пленки внутри'],
                                                'anodization_contact':'',#row['Контактность анодировки'],
                                                'anodization_type':'',#row['Тип анодировки'],
                                                'anodization_method':'',#row['Способ анодировки'],
                                                'print_view':'',#row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':width_and_height.ширина,
                                                'wms_height':width_and_height.высота,
                                                'group_prise': export_description_eng.group_price,
                                                }
                                          )
                                
                        else: 
                              materiale = component+"-E{:03d}".format(1)
                              AluminiyProductTermo(artikul =component,section ='E',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key],material=materiale).save()
                              df_new['SAP код E'][key]=materiale
                              umumiy_counter_termo[component+'-E'] = 1
                              
                              artikle = materiale.split('-')[0]
                              
                              hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                              
                              
                              width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                              
                                 
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Экструзия холодная резка'][key],
                                                'section':'E-Экструзия холодная резка ZPP2',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':'Неокрашенный',
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id':'',# row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':'',#row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':'',
                                                'inner_side_wg_s_id':'',
                                                'outer_side_wg_id':'',#row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':'',#row['Код лам пленки внутри'],
                                                'anodization_contact':'',#row['Контактность анодировки'],
                                                'anodization_type':'',#row['Тип анодировки'],
                                                'anodization_method':'',#row['Способ анодировки'],
                                                'print_view':'',#row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':width_and_height.ширина,
                                                'wms_height':width_and_height.высота,
                                                'group_prise': export_description_eng.group_price,
                                                }
                                          )
                              
                  termo_existZ =AluminiyProductTermo.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['Печь старения'][key]).exists()
                  simple_existZ =AluminiyProduct.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['Печь старения'][key]).exists()
                  if row['тип закаленности']!='T4':
                        if (termo_existZ or simple_existZ):
                              if termo_existZ:
                                    df_new['SAP код Z'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['Печь старения'][key])[:1].get().material
                              else:
                                    df_new['SAP код Z'][key] = AluminiyProduct.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['Печь старения'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код Z'][key],df_new['Печь старения'][key],'Z'])
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =component,section ='Z').exists():
                                    umumiy_counter_termo[ component +'-Z'] += 1
                                    max_valuesZ = umumiy_counter_termo[ component +'-Z']
                                    materiale = component+"-Z{:03d}".format(max_valuesZ)
                                    AluminiyProductTermo(artikul =component,section ='Z',counter=max_valuesZ,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Печь старения'][key],material=materiale).save()
                                    df_new['SAP код Z'][key]=materiale
                                    
                                    artikle = materiale.split('-')[0]
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                          
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                          
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"ZZZ tip pokr {row['Тип покрытия']}")    
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Печь старения'][key],
                                                      'section':'Z-Печь старения',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':'Неокрашенный',
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id':'',# row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':'',#row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':'',#row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':'',#row['Код лам пленки внутри'],
                                                      'anodization_contact':'',#row['Контактность анодировки'],
                                                      'anodization_type':'',#row['Тип анодировки'],
                                                      'anodization_method':'',#row['Способ анодировки'],
                                                      'print_view':'',#row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                              else:
                                    materiale = component+"-Z{:03d}".format(1)
                                    AluminiyProductTermo(artikul =component,section ='Z',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Печь старения'][key],material=materiale).save()
                                    df_new['SAP код Z'][key]=materiale
                                    umumiy_counter_termo[ component +'-Z'] = 1
                                    artikle = materiale.split('-')[0]
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                          
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                          
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"ZZZ tip pokr {row['Тип покрытия']}")  
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Печь старения'][key],
                                                      'section':'Z-Печь старения',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':'Неокрашенный',
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id':'',# row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':'',#row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':'',#row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':'',#row['Код лам пленки внутри'],
                                                      'anodization_contact':'',#row['Контактность анодировки'],
                                                      'anodization_type':'',#row['Тип анодировки'],
                                                      'anodization_method':'',#row['Способ анодировки'],
                                                      'print_view':'',#row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                              
                  
                  
                              
                  if ((row['Тип покрытия'] == 'Сублимированный') or (row['Тип покрытия'] == 'Ламинированный') or (row['Тип покрытия'] == 'Окрашенный') or (row['Тип покрытия'] == 'Белый')): 
                        termo_existP =AluminiyProductTermo.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['Покраска автомат'][key]).exists()
                        simple_existP =AluminiyProduct.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['Покраска автомат'][key]).exists()
                        if (termo_existP or simple_existP):
                              if termo_existP:
                                    df_new['SAP код P'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['Покраска автомат'][key])[:1].get().material
                              else:
                                    df_new['SAP код P'][key] = AluminiyProduct.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['Покраска автомат'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код P'][key],df_new['Покраска автомат'][key],'P'])
                        else: 
                              if '9016' in df_new['Покраска автомат'][key]:
                                    tip_pokr ='Белый'
                              else:
                                    tip_pokr ='Окрашенный'
                              if AluminiyProductTermo.objects.filter(artikul =component,section ='P').exists():
                                    umumiy_counter_termo[component+'-P'] += 1
                                    
                                    max_valuesP = umumiy_counter_termo[ component +'-P']
                                    materiale = component+"-P{:03d}".format(max_valuesP)
                                    AluminiyProductTermo(artikul =component,section ='P',counter=max_valuesP,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Покраска автомат'][key],material=materiale).save()
                                    df_new['SAP код P'][key]=materiale
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"p tip pokr {row['Тип покрытия']}")
                                    
                                    
                                    
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Покраска автомат'][key],
                                                      'section':'P-Покраска автомат',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':tip_pokr,
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                                    
                              else:
                                    materiale = component+"-P{:03d}".format(1)
                                    AluminiyProductTermo(artikul =component,section ='P',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Покраска автомат'][key],material=materiale).save()
                                    df_new['SAP код P'][key] = materiale
                                    umumiy_counter_termo[component+'-P'] = 1
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"p tip pokr {row['Тип покрытия']}")
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Покраска автомат'][key],
                                                      'section':'P-Покраска автомат',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':tip_pokr,
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                  
                  
                  
                  
                  
                  if row['Тип покрытия'] =='Сублимированный':
                        
                        termo_existS =AluminiyProductTermo.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['Сублимация'][key]).exists()
                        simple_existS =AluminiyProduct.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['Сублимация'][key]).exists()
                        if (termo_existS or simple_existS):
                              if termo_existS: 
                                    df_new['SAP код S'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['Сублимация'][key])[:1].get().material
                              else:
                                    df_new['SAP код S'][key] = AluminiyProduct.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['Сублимация'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код S'][key],df_new['Сублимация'][key],'S'])
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =component,section ='S').exists():
                                    umumiy_counter_termo[component+'-S'] += 1
                                    max_valuesS = umumiy_counter_termo[ component +'-S']
                                    materiale = component+"-S{:03d}".format(max_valuesS)
                                    AluminiyProductTermo(artikul =component,section ='S',counter=max_valuesS,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Сублимация'][key],material=materiale).save()
                                    df_new['SAP код S'][key]=materiale
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"S tip pokr {row['Тип покрытия']}")
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Сублимация'][key],
                                                      'section':'S-Сублимация',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':'Сублимированный',
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                              else:
                                    materiale = component+"-S{:03d}".format(1)
                                    AluminiyProductTermo(artikul =component,section ='S',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Сублимация'][key],material=materiale).save()
                                    df_new['SAP код S'][key]=materiale
                                    umumiy_counter_termo[component+'-S'] = 1
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    print(f"S tip pokr {row['Тип покрытия']}")
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Сублимация'][key],
                                                      'section':'S-Сублимация',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':'Сублимированный',
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                  
                  
                              
                  if row['Тип покрытия'] =='Анодированный':
                        termo_existA =AluminiyProductTermo.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['Анодировка'][key]).exists()
                        simple_existA =AluminiyProduct.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['Анодировка'][key]).exists()
                        if (termo_existA or simple_existA):
                              if termo_existA:
                                    df_new['SAP код A'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['Анодировка'][key])[:1].get().material
                              else:
                                    df_new['SAP код A'][key] = AluminiyProduct.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['Анодировка'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код A'][key],df_new['Анодировка'][key],'A'])
                        
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =component,section ='A').exists():
                                    umumiy_counter_termo[component+'-A'] += 1
                                    max_valuesA = umumiy_counter_termo[ component +'-A']
                                    materiale = component+"-A{:03d}".format(max_valuesA)
                                    AluminiyProductTermo(artikul =component,section ='A',counter=max_valuesA,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Анодировка'][key],material=materiale).save()
                                    df_new['SAP код A'][key]=materiale
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"A tip pokr {row['Тип покрытия']}")    
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Анодировка'][key],
                                                      'section':'A-Анодировка',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':'Анодированный',
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':'',#row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                              else:
                                    materiale = component+"-A{:03d}".format(1)
                                    AluminiyProductTermo(artikul =component,section ='A',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Анодировка'][key],material=materiale).save()
                                    df_new['SAP код A'][key]=materiale
                                    umumiy_counter_termo[component+'-A'] = 1
                                    artikle = materiale.split('-')[0]
                                    
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"A tip pokr {row['Тип покрытия']}")  
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Анодировка'][key],
                                                      'section':'A-Анодировка',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':'Анодированный',
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':'',#row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                                    
                  
                  
                              
                  if ((row['Код наклейки'] != 'NT1') and (row['Тип покрытия'] != 'Ламинированный')) :
                        if component in nakleyka_iskyucheniye:
                              continue
                        termo_existN =AluminiyProductTermo.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['Наклейка'][key]).exists()
                        simple_existN =AluminiyProduct.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['Наклейка'][key]).exists()
                        if (termo_existN or simple_existN):
                              if termo_existN:
                                    df_new['SAP код N'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['Наклейка'][key])[:1].get().material
                              else:
                                    df_new['SAP код N'][key] = AluminiyProduct.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['Наклейка'][key])[:1].get().material
                              duplicat_list.append([df_new['SAP код N'][key],df_new['Наклейка'][key],'N'])
                        else:
                              name_tip_pokr =''
                              if (('7777' in df_new['Наклейка'][key]) or ('8888' in df_new['Наклейка'][key])  or ('3701' in df_new['Наклейка'][key]) or ('3702' in df_new['Наклейка'][key])):
                                    name_tip_pokr = 'Сублимированный'
                              elif '9016' in df_new['Наклейка'][key]:
                                    name_tip_pokr = 'Белый'
                              elif 'MF' in df_new['Наклейка'][key]:
                                    name_tip_pokr = 'Неокрашенный'
                              elif anodirovaka_check(ANODIROVKA_CODE,df_new['Наклейка'][key]):
                                    name_tip_pokr = 'Анодированный'
                              else:
                                    name_tip_pokr = 'Окрашенный'
                              
                              if  AluminiyProductTermo.objects.filter(artikul =component,section ='N').exists():
                                    umumiy_counter_termo[component+'-N'] += 1
                                    max_valuesN = umumiy_counter_termo[ component +'-N']
                                    materiale = component+"-N{:03d}".format(max_valuesN)
                                    AluminiyProductTermo(artikul =component,section ='N',counter=max_valuesN,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Наклейка'][key],material=materiale).save()
                                    df_new['SAP код N'][key]=materiale
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                    print(f"N tip pokr {row['Тип покрытия']}")      
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Наклейка'][key],
                                                      'section':'N-Наклейка',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':name_tip_pokr,
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':'',#row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                              else:
                                    materiale = component+"-N{:03d}".format(1)
                                    AluminiyProductTermo(artikul =component,section ='N',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Наклейка'][key],material=materiale).save()
                                    df_new['SAP код N'][key]=materiale
                                    umumiy_counter_termo[component+'-N'] = 1
                                    artikle = materiale.split('-')[0]
                              
                                    hollow_and_solid =CharUtilsTwo.objects.filter(артикул = artikle)[:1].get().полый_или_фасонный
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    export_description = ''
                                    if row['Комбинация'].lower() == 'с термомостом':  
                                          export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    else:       
                                          export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                                    
                                    export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    print(f"N tip pokr {row['Тип покрытия']}")  
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['Наклейка'][key],
                                                      'section':'N-Наклейка',
                                                      'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                      'system':row['Название системы'],
                                                      'article':artikle,
                                                      'length':dlina,
                                                      'surface_treatment':name_tip_pokr,
                                                      'alloy':row['Сплав'],
                                                      'temper':row['тип закаленности'],
                                                      'combination':row['Комбинация'],
                                                      'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                      'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                      'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                      'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                      'outer_side_wg_s_id':'',
                                                      'inner_side_wg_s_id':'',
                                                      'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                      'inner_side_wg_id':row['Код лам пленки внутри'],
                                                      'anodization_contact':'',#row['Контактность анодировки'],
                                                      'anodization_type':row['Тип анодировки'],
                                                      'anodization_method':row['Способ анодировки'],
                                                      'print_view':row['Код наклейки'],
                                                      'profile_base':row['База профилей'],
                                                      'width':'1-1000',
                                                      'height':'1-1000',
                                                      # 'category':row['Название системы'],
                                                      'rawmat_type':'ПФ',
                                                      # 'hollow_and_solid':hollow_and_solid,
                                                      # 'export_description':export_description,
                                                      # 'export_description_eng':export_description_eng.bux_name_eng,
                                                      # 'tnved':export_description_eng.tnved,
                                                      # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                      'wms_width':width_and_height.ширина,
                                                      'wms_height':width_and_height.высота,
                                                      'group_prise': export_description_eng.group_price,
                                                      }
                                                )
                  
      

      
      parent_dir ='{MEDIA_ROOT}\\uploads\\aluminiytermo\\'
       
      if not os.path.isdir(parent_dir):
            create_folder(f'{MEDIA_ROOT}\\uploads\\','aluminiytermo')
            
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\',f'{year}')
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\',f'{month}')
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\',day)
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\',hour)
            
      df_char = create_characteristika(cache_for_cratkiy_text) 
      df_char_title =create_characteristika_utils(cache_for_cratkiy_text)
            
      if not os.path.isfile(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\alumin_new_termo-{minut}.xlsx'):
            path_alu =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\alumin_new_termo-{minut}.xlsx'
            path_ramka_norma =f'uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\norma-{minut}.xlsx'
      else:
            st =random.randint(0,1000)
            path_alu =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\alumin_new_termo-{minut}-{st}.xlsx'
            path_ramka_norma =f'uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\norma-{minut}-{st}.xlsx'
            
     
      df_extrusion = pd.DataFrame({'SAP CODE E' : exturision_list})
    
      df_new = df_new.replace('nan','')

      razlovka_yoq = True
      for key,razlov in df_new.iterrows():
            if razlov['SAP код 7']!="":
                  if not RazlovkaTermo.objects.filter(sap_code7=razlov['SAP код 7'],kratkiy7=razlov['U-Упаковка + Готовая Продукция']).exists():
                        razlovka_yoq = True
                        razlovka_komb = RazlovkaTermo(
                              parent_id=0,
                              esap_code =razlov['SAP код E'],
                              ekratkiy =razlov['Экструзия холодная резка'],
                              zsap_code =razlov['SAP код Z'],
                              zkratkiy =razlov['Печь старения'],
                              psap_code =razlov['SAP код P'],
                              pkratkiy =razlov['Покраска автомат'],
                              ssap_code =razlov['SAP код S'],
                              skratkiy =razlov['Сублимация'],
                              asap_code =razlov['SAP код A'],
                              akratkiy =razlov['Анодировка'],
                              nsap_code =razlov['SAP код N'],
                              nkratkiy =razlov['Наклейка'],
                              ksap_code =razlov['SAP код K'],
                              kratkiy =razlov['K-Комбинирования'],
                              lsap_code =razlov['SAP код L'],
                              lkratkiy =razlov['Ламинация'],
                              sap_code7 =razlov['SAP код 7'],
                              kratkiy7 =razlov['U-Упаковка + Готовая Продукция'],
                              fsap_code =razlov['SAP код F'],
                              fkratkiy =razlov['Фабрикация'],
                              sap_code75 =razlov['SAP код 75'],
                              kratkiy75 =razlov['U-Упаковка + Готовая Продукция 75']
                        )
                        razlovka_komb.save()
                  else:
                        razlovka_yoq = False 
            elif razlov['SAP код 75'] != '':
                  if not RazlovkaTermo.objects.filter(sap_code7=razlov['SAP код 75'],kratkiy7=razlov['U-Упаковка + Готовая Продукция 75']).exists():
                        razlovka_yoq = True
                        razlovka_komb = RazlovkaTermo(
                              parent_id=0,
                              esap_code =razlov['SAP код E'],
                              ekratkiy =razlov['Экструзия холодная резка'],
                              zsap_code =razlov['SAP код Z'],
                              zkratkiy =razlov['Печь старения'],
                              psap_code =razlov['SAP код P'],
                              pkratkiy =razlov['Покраска автомат'],
                              ssap_code =razlov['SAP код S'],
                              skratkiy =razlov['Сублимация'],
                              asap_code =razlov['SAP код A'],
                              akratkiy =razlov['Анодировка'],
                              nsap_code =razlov['SAP код N'],
                              nkratkiy =razlov['Наклейка'],
                              ksap_code =razlov['SAP код K'],
                              kratkiy =razlov['K-Комбинирования'],
                              lsap_code =razlov['SAP код L'],
                              lkratkiy =razlov['Ламинация'],
                              sap_code7 =razlov['SAP код 7'],
                              kratkiy7 =razlov['U-Упаковка + Готовая Продукция'],
                              fsap_code =razlov['SAP код F'],
                              fkratkiy =razlov['Фабрикация'],
                              sap_code75 =razlov['SAP код 75'],
                              kratkiy75 =razlov['U-Упаковка + Готовая Продукция 75']
                        )
                        razlovka_komb.save()
                  else:
                        razlovka_yoq = False 
            
            else:
                  if razlovka_yoq:
                        RazlovkaTermo(
                              parent_id=razlovka_komb.id,
                              esap_code =razlov['SAP код E'],
                              ekratkiy =razlov['Экструзия холодная резка'],
                              zsap_code =razlov['SAP код Z'],
                              zkratkiy =razlov['Печь старения'],
                              psap_code =razlov['SAP код P'],
                              pkratkiy =razlov['Покраска автомат'],
                              ssap_code =razlov['SAP код S'],
                              skratkiy =razlov['Сублимация'],
                              asap_code =razlov['SAP код A'],
                              akratkiy =razlov['Анодировка'],
                              nsap_code =razlov['SAP код N'],
                              nkratkiy =razlov['Наклейка'],
                              ksap_code =razlov['SAP код K'],
                              kratkiy =razlov['K-Комбинирования'],
                              lsap_code =razlov['SAP код L'],
                              lkratkiy =razlov['Ламинация'],
                              sap_code7 =razlov['SAP код 7'],
                              kratkiy7 =razlov['U-Упаковка + Готовая Продукция'],
                              fsap_code =razlov['SAP код F'],
                              fkratkiy =razlov['Фабрикация'],
                              sap_code75 =razlov['SAP код 75'],
                              kratkiy75 =razlov['U-Упаковка + Готовая Продукция 75']
                        ).save()

      
      for key,razlov in df_char.iterrows():
            if not Characteristika.objects.filter(sap_code=razlov['SAP CODE'],kratkiy_text=razlov['KRATKIY TEXT']).exists():
                  Characteristika(
                        sap_code =razlov['SAP CODE'],
                        kratkiy_text =razlov['KRATKIY TEXT'],
                        section =razlov['SECTION'],
                        savdo_id =razlov['SAVDO_ID'],
                        savdo_name =razlov['SAVDO_NAME'],
                        export_customer_id =razlov['EXPORT_CUSTOMER_ID'],
                        system =razlov['SYSTEM'],
                        article =razlov['ARTICLE'],
                        length =razlov['LENGTH'],
                        surface_treatment =razlov['SURFACE_TREATMENT'],
                        alloy =razlov['ALLOY'],
                        temper =razlov['TEMPER'],
                        combination =razlov['COMBINATION'],
                        outer_side_pc_id =razlov['OUTER_SIDE_PC_ID'],
                        outer_side_pc_brand =razlov['OUTER_SIDE_PC_BRAND'],
                        inner_side_pc_id =razlov['INNER_SIDE_PC_ID'],
                        inner_side_pc_brand =razlov['INNER_SIDE_PC_BRAND'],
                        outer_side_wg_s_id =razlov['OUTER_SIDE_WG_S_ID'],
                        inner_side_wg_s_id =razlov['INNER_SIDE_WG_S_ID'],
                        outer_side_wg_id =razlov['OUTER_SIDE_WG_ID'],
                        inner_side_wg_id =razlov['INNER_SIDE_WG_ID'],
                        anodization_contact =razlov['ANODIZATION_CONTACT'],
                        anodization_type =razlov['ANODIZATION_TYPE'],
                        anodization_method =razlov['ANODIZATION_METHOD'],
                        print_view =razlov['PRINT_VIEW'],
                        profile_base =razlov['PROFILE_BASE'],
                        width =razlov['WIDTH'],
                        height =razlov['HEIGHT'],
                        category =razlov['CATEGORY'],
                        rawmat_type =razlov['RAWMAT_TYPE'],
                        benkam_id =razlov['BENKAM_ID'],
                        hollow_and_solid =razlov['HOLLOW AND SOLID'],
                        export_description =razlov['EXPORT_DESCRIPTION'],
                        export_description_eng =razlov['EXPORT_DESCRIPTION ENG'],
                        tnved =razlov['TNVED'],
                        surface_treatment_export =razlov['SURFACE_TREATMENT_EXPORT'],
                        wms_width =razlov['WMS_WIDTH'],
                        wms_height =razlov['WMS_HEIGHT'],
                        group_prise =''					
                  ).save()
      for key,razlov in df_char_title.iterrows():
            if not CharacteristicTitle.objects.filter(sap_код_s4p_100 = razlov['SAP код S4P 100']).exists():
                  CharacteristicTitle(
                        дата_изменение_добавление =razlov['Дата изменение добавление'], 
                        статус_изменение_добавление =razlov['Статус изменение добавление'], 
                        ссылки_для_чертежа =razlov['Ссылки для чертежа'], 
                        sap_код_s4p_100 =razlov['SAP код S4P 100'], 
                        нумерация_до_sap =razlov['Нумерация до SAP'], 
                        короткое_название_sap =razlov['Короткое название SAP'], 
                        польное_наименование_sap =razlov['Польное наименование SAP'], 
                        ед_изм =razlov['Ед, Изм,'], 
                        альтернативная_ед_изм =razlov['Альтернативная ед, изм'], 
                        коэфициент_пересчета =razlov['Коэфициент пересчета'], 
                        участок =razlov['Участок'], 
                        альтернативный_участок =razlov['Альтернативный участок'], 
                        длина =razlov['Длина'], 
                        ширина =razlov['Ширина'], 
                        высота =razlov['Высота'], 
                        группа_материалов =razlov['группа материалов'], 
                        удельный_вес_за_метр =razlov['Удельный вес за метр'], 
                        общий_вес_за_штуку =razlov['Общий вес за штуку'],
                        price =razlov['Price']
                  ).save()
      
      exchange_value = ExchangeValues.objects.get(id=1)
      price_all_correct = True
      for key, row in df_char_title.iterrows():
            if LengthOfProfile.objects.filter(artikul=row['ch_article'],length=row['Длина']).exists():
                  length_of_profile = LengthOfProfile.objects.filter(artikul=row['ch_article'],length=row['Длина'])[:1].get()
                  df_char_title['Общий вес за штуку'][key] =length_of_profile.ves_za_shtuk
                  df_char_title['Удельный вес за метр'][key] = length_of_profile.ves_za_metr
                  price = Price.objects.filter(tip_pokritiya = row['Тип покрытия'],tip=row['ch_combination'])[:1].get()
                  # print(row['ch_article'],df_char_title['Общий вес за штуку'][key],price.price.replace(',','.'),exchange_value.valute.replace(',','.'))
                  df_char_title['Price'][key] = float(price.price.replace(',','.')) * float(str(df_char_title['Общий вес за штуку'][key]).replace(',','.'))  * float(exchange_value.valute.replace(',','.'))
            elif row['ch_combination'].lower() ==str("Без термомоста").lower():
                  if LengthOfProfile.objects.filter(artikul=row['ch_article']).exists():
                        length_of_profile = LengthOfProfile.objects.filter(artikul=row['ch_article'])[:1].get()
                        df_char_title['Общий вес за штуку'][key] =float(length_of_profile.ves_za_metr.replace(',','.')) * float(row['Длина'].replace(',','.'))/(1000)
                        df_char_title['Удельный вес за метр'][key] = length_of_profile.ves_za_metr
                        price = Price.objects.filter(tip_pokritiya = row['Тип покрытия'],tip=row['ch_combination'])[:1].get()
                        df_char_title['Price'][key] = float(str(price.price).replace(',','.')) * float(str(df_char_title['Общий вес за штуку'][key]).replace(',','.'))  * float( str(exchange_value.valute).replace(',','.') )
            else:
                  price_all_correct = False

      writer = pd.ExcelWriter(path_alu, engine='xlsxwriter')
      df_new.to_excel(writer,index=False,sheet_name ='Schotchik')
      df_char.to_excel(writer,index=False,sheet_name ='Characteristika')
      df_char_title.to_excel(writer,index=False,sheet_name ='title')
      df_extrusion.to_excel(writer,index=False,sheet_name='T4')
      writer.close()

      del df_new['Название системы']
      del df_new['SAP код A']
      del df_new['Анодировка']
      del df_new['SAP код L']
      del df_new['Ламинация']

      for key, row in df_new.iterrows():
            if row['SAP код Z'] !='':
                  df_new['SAP код E'][key] = ''
                  df_new['Экструзия холодная резка'][key] = ''

      norma_file = df_new.to_excel(f'{MEDIA_ROOT}\\{path_ramka_norma}',index=False)
      
      order_id = request.GET.get('order_id',None)
      work_type = 1
      if order_id:
            work_type = Order.objects.get(id = order_id).work_type

      if price_all_correct  and  work_type != 5:
            path = update_char_title_function(df_char_title,df_extrusion,order_id,'aluminiytermo')
            files =[File(file=p,filetype='termo') for p in path]
            files.append(File(file=path_alu,filetype='termo'))
            context ={
                  'files':files,
                  'section':'Формированый термо файл'
            }
            if order_id:
                  print('*1*'*15)
                  norma_file = NormaExcelFiles(file = path_ramka_norma,type='termo')
                  norma_file.save()
                  file_paths =[ file.file for file in files]
                  order = Order.objects.get(id = order_id)
                  paths = order.paths
                  raz_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                  zip_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                  paths['termo_razlovka_file']= file_paths
                  
                  paths['norma_formula_file'] = f'{MEDIA_ROOT}\\{path_ramka_norma}'
                  paths['norma_link'] ='/norma/process-combinirovanniy/' + str(norma_file.id) +f'?type=termo&order_id={order_id}'

                  paths['raz_created_at']= raz_created_at
                  paths['zip_created_at']= zip_created_at
                  paths['status_l']= 'done'
                  paths['status_raz']= 'done'
                  paths['status_zip']= 'done'
                  paths['status_text_l']= 'done'
                  paths['status_norma']= 'on process'
                  order.paths = paths
                  order.aluminiy_worker = request.user
                  order.current_worker = request.user
                  order.work_type = 6
                  order.save()
                  context['order'] = order
                  paths =  order.paths
                  for key,val in paths.items():
                        context[key] = val
                  return render(request,'order/order_detail.html',context) 
      else:
            

            file =[File(file=path_alu,filetype='termo')]
            context ={
                  'files':file,
                  'section':'Формированый термо файл'
            }

            if order_id:
                  print('*2*'*15)
                  norma_file = NormaExcelFiles(file = path_ramka_norma,type='simple')
                  norma_file.save()
                  order = Order.objects.get( id = order_id)
                  paths = order.paths 
                  if work_type != 5:
                        context2 ={
                              'termo_razlovka_file':[path_alu,path_alu]
                        }
                        paths['termo_razlovka_file'] = [path_alu,path_alu]
                  else:
                        path_alu = order.paths['termo_razlovka_file']
                        context2 ={
                              'termo_razlovka_file':[path_alu,path_alu]
                        }

                  
                  raz_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                  paths['raz_created_at']= raz_created_at
                  
                  paths['status_l']= 'done'
                  paths['status_raz']= 'done'
                  paths['status_zip']= 'on process'
                  paths['status_text_l']= 'on process'
                  paths['status_norma']= 'on process'
                  paths['status_norma_lack']= 'on process'

                  paths['norma_formula_file'] = f'{MEDIA_ROOT}\\{path_ramka_norma}'
                  paths['norma_link'] ='/norma/process-combinirovanniy/' + str(norma_file.id) +'?type=termo&order_id='+str(order.id)
                  
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

                  return render(request,'order/order_detail.html',context2)

      return render(request,'universal/generated_files.html',context)
      
                  
    
