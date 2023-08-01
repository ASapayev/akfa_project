from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import pandas as pd
from django.core.paginator import Paginator
from .models import ArtikulComponent,AluminiyProduct,AluFile,RazlovkaObichniy,RazlovkaTermo
from aluminiytermo.models import AluminiyProductTermo,CharacteristikaFile
from aluminiytermo.views import File
from .forms import FileForm
from django.db.models import Max
from config.settings import MEDIA_ROOT
import numpy as np
from .utils import fabrikatsiya_sap_kod,create_folder,CharacteristicTitle,save_razlovka,download_bs64
import os
import random
from aluminiytermo.utils import create_characteristika,create_characteristika_utils,characteristika_created_txt_create,check_for_correct,anodirovaka_check
from aluminiytermo.models import CharUtilsOne,CharUtilsTwo,CharUtilsThree,Characteristika,BazaProfiley
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import ast
from django.http import JsonResponse,HttpResponse,FileResponse
from datetime import datetime
from aluminiytermo.BAZA import ANODIROVKA_CODE
from io import BytesIO as IO





def download_all_razlovki(request):
      file_type = request.GET.get('type',None)
      if file_type =='simple':
            simple_list = RazlovkaObichniy.objects.all().values_list('esap_code','ekratkiy','zsap_code','zkratkiy','psap_code','pkratkiy','ssap_code','skratkiy','asap_code','akratkiy','lsap_code','lkratkiy','nsap_code','nkratkiy','sap_code7','kratkiy7')
            data = pd.DataFrame(np.array(list(simple_list)),columns=[
                  'SAP код E','Экструзия холодная резка',
                  'SAP код Z','Печь старения',
                  'SAP код P','Покраска автомат',
                  'SAP код S','Сублимация',
                  'SAP код A','Анодировка',
                  'SAP код L','Ламинация',
                  'SAP код N','Наклейка',
                  'SAP код 7','U-Упаковка + Готовая Продукция'
                                                            ])
            
            data = data.replace('nan','')
            
            res = download_bs64([data,],'OBICHNIY')
            return res
      else:
            termo_list = RazlovkaTermo.objects.all().order_by('created_at').values_list('esap_code','ekratkiy','zsap_code','zkratkiy','psap_code','pkratkiy','ssap_code','skratkiy','asap_code','akratkiy','nsap_code','nkratkiy','ksap_code','kratkiy','lsap_code','lkratkiy','sap_code7','kratkiy7')
            data = pd.DataFrame(np.array(list(termo_list)),columns=[
                  'SAP код E','Экструзия холодная резка',
                  'SAP код Z','Печь старения',
                  'SAP код P','Покраска автомат',
                  'SAP код S','Сублимация',
                  'SAP код A','Анодировка',
                  'SAP код N','Наклейка',
                  'SAP код K','K-Комбинирования',
                  'SAP код L','Ламинация',
                  'SAP код 7','U-Упаковка + Готовая Продукция'
                                                            ])
            data = data.replace('nan','')
            res = download_bs64([data,],'TERMO')
      
      return res
      




def show_razlovki(request):
     
      search_text = request.GET.get('search',None)

      if search_text:
            products = RazlovkaObichniy.objects.filter(
                  Q(esap_code__icontains = search_text)|
                  Q(ekratkiy__icontains = search_text)|
                  Q(zsap_code__icontains = search_text)|
                  Q(zkratkiy__icontains = search_text)|
                  Q(psap_code__icontains = search_text)|
                  Q(pkratkiy__icontains = search_text)|
                  Q(ssap_code__icontains = search_text)|
                  Q(skratkiy__icontains = search_text)|
                  Q(asap_code__icontains = search_text)|
                  Q(akratkiy__icontains = search_text)|
                  Q(lsap_code__icontains = search_text)|
                  Q(lkratkiy__icontains = search_text)|
                  Q(nsap_code__icontains = search_text)|
                  Q(nkratkiy__icontains = search_text)|
                  Q(sap_code7__icontains = search_text)|
                  Q(kratkiy7__icontains = search_text)|
                  Q(fsap_code__icontains = search_text)|
                  Q(fkratkiy__icontains = search_text)|
                  Q(sap_code75__icontains = search_text)|
                  Q(kratkiy75__icontains = search_text)
            ).order_by('-created_at')
      else:
            products = RazlovkaObichniy.objects.all().order_by('-created_at')

      paginator = Paginator(products, 25)

      if request.GET.get('page') != None:
            page_number = request.GET.get('page')
      else:
            page_number=1

      page_obj = paginator.get_page(page_number)

    
      

      context ={
            'section':'Обычный разловки',
            'products':page_obj,
            'type':False,
            'search':search_text
      }

                  
      return render(request,'universal/show_razlovki.html',context)

def show_razlovki_termo(request):
      search_text = request.GET.get('search',None)

      if search_text:
            products = RazlovkaTermo.objects.filter(
                  Q(esap_code__icontains = search_text)|
                  Q(ekratkiy__icontains = search_text)|
                  Q(zsap_code__icontains = search_text)|
                  Q(zkratkiy__icontains = search_text)|
                  Q(psap_code__icontains = search_text)|
                  Q(pkratkiy__icontains = search_text)|
                  Q(ssap_code__icontains = search_text)|
                  Q(skratkiy__icontains = search_text)|
                  Q(asap_code__icontains = search_text)|
                  Q(akratkiy__icontains = search_text)|
                  Q(lsap_code__icontains = search_text)|
                  Q(lkratkiy__icontains = search_text)|
                  Q(nsap_code__icontains = search_text)|
                  Q(nkratkiy__icontains = search_text)|
                  Q(sap_code7__icontains = search_text)|
                  Q(kratkiy7__icontains = search_text)|
                  Q(fsap_code__icontains = search_text)|
                  Q(fkratkiy__icontains = search_text)|
                  Q(sap_code75__icontains = search_text)|
                  Q(kratkiy75__icontains = search_text)
            ).order_by('-created_at')
      else:
            products = RazlovkaTermo.objects.all().order_by('created_at')

      paginator = Paginator(products, 25)

      if request.GET.get('page') != None:
            page_number = request.GET.get('page')
      else:
            page_number=1

      page_obj = paginator.get_page(page_number)
      context ={
            'section':'Термо разловки',
            'products':page_obj,
            'type':True,
            'search':search_text
            
      }
                  
      return render(request,'universal/show_razlovki.html',context)

def save_razlovka2(request):
      df = pd.read_excel('c:\\OpenServer\\domains\\Razlovka.xlsx','Лист1')
      # df = pd.read_excel('C:\\OSPanel\\domains\\Razlovka.xlsx','Лист1')
      df = df.astype(str)
      df = df.replace('nan','')
      
      save_razlovka(df,'simple')
      return JsonResponse({'a':'b'})


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
      return render(request,'aluminiy/index.html')


def artikul_and_companent(request):
      df = pd.read_excel('c:\\OpenServer\\domains\\new_component.xlsx','Лист1')
      for i in range(0,3750):
            artikul =df['АРТИКУЛ'][i] 
            component =df['КОМПОНЕНТ'][i]
            seria =df['Серия'][i]
            product_des_ru =df['Productdescription-RUS'][i]
            product_des_ru2 =df['Productdescription-RUS2'][i]
            stariy_code_benkam=df['Stariy kod benkam'][i]
            stariy_code_jomiy=df['Stariy kod jomiy'][i]
            proverka_artikul2 = df['ПроверкаАртикул2'][i]
            proverkacom2 =df['ПроверкаКомпонент2'][i]
            grupa_materialov= df['Группа материалов ГП'][i]
            grupa_materialov2= df['Группа материалов ПФ'][i]
            artiku_comp = ArtikulComponent(
            artikul = artikul,
            component = component,
            seria =seria,
            product_description_ru1=product_des_ru,
            product_description_ru =product_des_ru2,
            stariy_code_benkam=stariy_code_benkam,
            stariy_code_jomiy=stariy_code_jomiy,
            proverka_artikul2 =proverka_artikul2,
            proverka_component2=proverkacom2,
            gruppa_materialov =grupa_materialov,
            gruppa_materialov2 =grupa_materialov2
            )
            artiku_comp.save()
  
      return JsonResponse({'converted':'a'})

def aluminiy_productbases(request):
  df = pd.read_excel('c:\\OpenServer\\domains\\Новая база2.XLSX','без термо')
  
  for i in range(0,df.shape[0]):
    material =df['Материал'][i] 
    artikul =df['Ариткул'][i]
    section =df['Передел'][i]
    counter =df['Счетчик'][i]
    gruppa_materialov =df['Группа материалов'][i]
    kratkiy_tekst_materiala=df['Краткий текст материала'][i]
    kombinirovanniy=df['Комбинирования'][i]
    
    artiku_comp = AluminiyProduct(
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
  
  for i in range(0,df.shape[0]):
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
    
    artiku_comp =AluminiyProductBasesimple(
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

def upload_product(request):
  if request.method == 'POST':
    form = FileForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('aluminiy_files')
  else:
      form =FileForm()
      context ={
        'form':form
      }
  return render(request,'excel_form.html',context)

def upload_product_org(request):
  if request.method == 'POST':
    form = FileForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('aluminiy_files_org')
  else:
      form =FileForm()
      context ={
        'form':form,
        'section':'Формирование сапкода обычный'
      }
  return render(request,'universal/main.html',context)



def aluminiy_files(request):
  files = AluFile.objects.filter(generated =False).order_by('-created_at')
  context ={'files':files}
  return render(request,'aluminiy/alu_file_list.html',context)

def aluminiy_files_org(request):
  files = AluFile.objects.filter(generated =False).order_by('-created_at')
  context ={'files':files,'section':'Формированный обычный файлы','type':'ОБЫЧНЫЙ','link':'/alu/alum-org/add/'}
  return render(request,'universal/file_list.html',context)

def aluminiy_group(request):
      aluminiy_group =AluminiyProduct.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
      
      umumiy={}
      for al in aluminiy_group:    
            
            umumiy[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      
      return JsonResponse({'data':umumiy})

def update_char_title(request,id):
      file = CharacteristikaFile.objects.get(id=id).file
      df = pd.read_excel(f'{MEDIA_ROOT}/{file}','title')
      df_extrusion = pd.read_excel(f'{MEDIA_ROOT}/{file}','T4')
      e_list =df_extrusion['SAP CODE E'].values.tolist()
      df =df.astype(str)
      
      pathbenkam,pathjomiy = characteristika_created_txt_create(df,e_list,'aluminiy')
      filesbenkam = [File(file=path,filetype='BENKAM') for path in pathbenkam]
      filesjomiy = [File(file=path,filetype='JOMIY') for path in pathjomiy]
      context = {
            'filesbenkam':filesbenkam,
            'filesjomiy':filesjomiy,
            'section':'Формированные файлы'
            }

      return render(request,'universal/generated_files_char.html',context)


def aluminiy_files_simple_char_title(request):
      files = AluFile.objects.filter(file_type ='title')
      context ={'files':files}
      return render(request,'aluminiy/alu_file_list_char_title.html',context)

                  


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
      file = AluFile.objects.get(id=id).file
      df = pd.read_excel(f'{MEDIA_ROOT}/{file}')
      df =df.astype(str)
      
      now = datetime.now()
      year =now.strftime("%Y")
      month =now.strftime("%B")
      day =now.strftime("%a%d")
      hour =now.strftime("%H HOUR")
      minut =now.strftime("%M")
      
      doesnotexist,correct = check_for_correct(df,filename='aluminiy')
      if not correct:
            context ={
                  'CharUtilsOne':doesnotexist[0],
                  'CharUtilsTwo':doesnotexist[1],
                  'BazaProfile':doesnotexist[2],
                  'ArtikulComponent':doesnotexist[3]
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
            
            df_artikul_component =pd.DataFrame({
                  'artikul':doesnotexist[3],
                  'component':doesnotexist[3],
                  'seria':['' for i in doesnotexist[3]],
                  'product_description_ru1':['' for i in doesnotexist[3]],
                  'product_description_ru':['' for i in doesnotexist[3]],
                  'stariy_code_benkam':['' for i in doesnotexist[3]],
                  'stariy_code_jomiy':['' for i in doesnotexist[3]],
                  'proverka_artikul2':['' for i in doesnotexist[3]],
                  'proverka_component2':['' for i in doesnotexist[3]],
                  'gruppa_materialov':['' for i in doesnotexist[3]],
                  'gruppa_materialov2':['' for i in doesnotexist[3]]
            })
            create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\','Not Exists')
            
            path_not_exists =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\Not Exists\\Not_Exists.xlsx'
            
            if os.path.isfile(path_not_exists):
                  try:
                        os.remove(path_not_exists)
                  except:
                        return render(request,'utils/file_exist.html')
            
            writer = pd.ExcelWriter(path_not_exists, engine='xlsxwriter')
            df_char_utils_one.to_excel(writer,index=False,sheet_name ='character utils one')
            df_char_utils_two.to_excel(writer,index=False,sheet_name ='character utils two')
            df_baza_profiley.to_excel(writer,index=False,sheet_name ='baza profile')
            df_artikul_component.to_excel(writer,index=False,sheet_name ='artikul component')
            writer.close()
            # writer.save()
            return render(request,'aluminiy/check_for_correct.html',context)
      
      aluminiy_group = AluminiyProduct.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
      umumiy_counter={}
      for al in aluminiy_group:
            umumiy_counter[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      
      aluminiy_group_termo = AluminiyProductTermo.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
      umumiy_counter_termo = {}
      for al in aluminiy_group_termo:
            umumiy_counter_termo[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      
      
      
      
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
      df_new['SAP код L']=''
      df_new['Ламинация']=''
      df_new['SAP код N']=''
      df_new['Наклейка']=''
      df_new['SAP код 7']=''
      df_new['U-Упаковка + Готовая Продукция']=''
      df_new['SAP код F']=''
      df_new['Фабрикация']=''
      df_new['SAP код 75']=''
      df_new['U-Упаковка + Готовая Продукция 75']=''

      
      
      
      cache_for_cratkiy_text =[]
      duplicat_list =[]
      
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
            
            
            
            product_exists = ArtikulComponent.objects.filter(artikul=row['Артикул']).exists()
            if row['Код декор пленки снаружи'] !='nan' and '.0' in row['Код декор пленки снаружи']:
                  df['Код декор пленки снаружи'][key] =df['Код декор пленки снаружи'][key].replace('.0','')
            
            if product_exists:
                  component = ArtikulComponent.objects.filter(artikul=row['Артикул'])[:1].get().component
            else:
                  if ArtikulComponent.objects.filter(component=row['Артикул']).exists():
                        component = row['Артикул']
                        termo = True
                  else:
                        continue
                  
            if df['Длина при выходе из пресса'][key] != 'nan':
                  dlina = df['Длина при выходе из пресса'][key].replace('.0','')
                        
                  df_new['Фабрикация'][key]=fabrikatsiya_sap_kod(df['Краткий текст товара'][key],df['Длина (мм)'][key])
                  df_new['U-Упаковка + Готовая Продукция 75'][key]=fabrikatsiya_sap_kod(df['Краткий текст товара'][key],df['Длина (мм)'][key])
                  
                  
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
                  if AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='F',kratkiy_tekst_materiala=df_new['Фабрикация'][key]).exists():
                        df_new['SAP код F'][key] = AluminiyProduct.objects.filter(artikul = df['Артикул'][key],section ='F',kratkiy_tekst_materiala=df_new['Фабрикация'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код F'][key],df_new['Фабрикация'][key],'F'])
                  else: 
                        if AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='F').exists():
                              umumiy_counter[df['Артикул'][key]+'-F'] += 1
                              max_valuesF = umumiy_counter[df['Артикул'][key]+'-F']
                              materiale = df['Артикул'][key] +"-F{:03d}".format(max_valuesF)
                              AluminiyProduct(artikul =df['Артикул'][key],section ='F',counter=max_valuesF,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Фабрикация'][key],material=materiale).save()
                              df_new['SAP код F'][key]=materiale
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
                              AluminiyProduct(artikul =df['Артикул'][key],section ='F',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Фабрикация'][key],material=materiale).save()
                              df_new['SAP код F'][key]=materiale
                              umumiy_counter[df['Артикул'][key]+'-F'] = 1
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
                              
                              
                  
                  
                  if AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='75',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key]).exists():
                        df_new['SAP код 75'][key] = AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='75',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код 75'][key],df_new['U-Упаковка + Готовая Продукция 75'][key],'75'])
                  else: 
                        if AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='75').exists():
                              umumiy_counter[df['Артикул'][key]+'-75'] += 1
                              max_values75 = umumiy_counter[df['Артикул'][key]+'-75']
                              
                              if max_values75 <= 99:
                                    materiale = df['Артикул'][key]+"-75{:02d}".format(max_values75)
                              else:
                                    counter =7500 + max_values75
                                    materiale = df['Артикул'][key]+"-{:04d}".format(counter)
                                    
                                    
                              AluminiyProduct(artikul =df['Артикул'][key],section ='75',counter=max_values75,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key],material=materiale).save()
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
                                    surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']] +' ' + row['Код краски снаружи']
                              elif row['Тип покрытия'].lower() =='сублимированный':
                                    surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                              elif row['Тип покрытия'].lower() =='анодированный':
                                    surface_treatment_export = row['Код цвета анодировки снаружи']
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
                              AluminiyProduct(artikul = df['Артикул'][key],section ='75',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key],material=materiale).save()
                              df_new['SAP код 75'][key] = materiale 
                              umumiy_counter[df['Артикул'][key]+'-75'] = 1
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
                                    surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']]+''+row['Код краски снаружи']
                              elif row['Тип покрытия'].lower() =='сублимированный':
                                    surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                              elif row['Тип покрытия'].lower() =='анодированный':
                                    surface_treatment_export = row['Код цвета анодировки снаружи']
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
                  if AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key]).exists():
                        df_new['SAP код 7'][key] = AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код 7'][key],df_new['U-Упаковка + Готовая Продукция'][key],'7'])
                  else: 
                        if AluminiyProduct.objects.filter(artikul=df['Артикул'][key],section ='7').exists():
                              umumiy_counter[df['Артикул'][key]+'-7'] += 1
                              max_values7 = umumiy_counter[df['Артикул'][key]+'-7']
                              materiale = df['Артикул'][key]+"-7{:03d}".format(max_values7)
                              AluminiyProduct(artikul = df['Артикул'][key],section ='7',counter=max_values7,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key],material=materiale).save()
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
                                    surface_treatment_export = row['Код цвета анодировки снаружи']
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
                              AluminiyProduct(artikul = df['Артикул'][key],section ='7',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key],material=materiale).save()
                              df_new['SAP код 7'][key] = materiale
                              umumiy_counter[df['Артикул'][key]+'-7'] = 1
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
                                    surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']] + ' ' + row['Код краски снаружи']
                              elif row['Тип покрытия'].lower() =='сублимированный':
                                    surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                              elif row['Тип покрытия'].lower() =='анодированный':
                                    surface_treatment_export = row['Код цвета анодировки снаружи']
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
                        
                  ##### kombirinovanniy
            
                   
            
            if df['Тип покрытия'][key] == 'Ламинированный':      
                  if AluminiyProduct.objects.filter(artikul =component,section ='L',kratkiy_tekst_materiala=df_new['Ламинация'][key]).exists():
                        df_new['SAP код L'][key] = AluminiyProduct.objects.filter(artikul =component,section ='L',kratkiy_tekst_materiala=df_new['Ламинация'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код L'][key],df_new['Ламинация'][key],'L'])
                  else: 
                        if AluminiyProduct.objects.filter(artikul =component,section ='L').exists():
                              umumiy_counter[component+'-L'] += 1
                              max_valuesL = umumiy_counter[ component +'-L']
                              materiale = component+"-L{:03d}".format(max_valuesL)
                              AluminiyProduct(artikul =component,section ='L',counter=max_valuesL,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Ламинация'][key],material=materiale).save()
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
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Ламинация'][key],
                                                'section':'L-Ламинирование',
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
                              AluminiyProduct(artikul =df['Артикул'][key],section ='L',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Ламинация'][key],material=materiale).save()
                              df_new['SAP код L'][key]=materiale
                              umumiy_counter[df['Артикул'][key]+'-L'] = 1
                              
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
                                                'kratkiy':df_new['Ламинация'][key],
                                                'section':'L-Ламинирование',
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
                        df_new['Наклейка'][key]= df_new['Анодировка'][key] +' ' + row['Код наклейки'].replace('.0','')
            else:
                  pass
                  
            
            termo_existE =AluminiyProductTermo.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key]).exists()
            simple_existE =AluminiyProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key]).exists()

           
            
            if (termo_existE or simple_existE):
                  if termo_existE:
                        df_new['SAP код E'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key])[:1].get().material
                  else:
                        df_new['SAP код E'][key] = AluminiyProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key])[:1].get().material
                  duplicat_list.append([df_new['SAP код E'][key],df_new['Экструзия холодная резка'][key],'E'])
            else:
                  if AluminiyProduct.objects.filter(artikul =component,section ='E').exists():
                        # max_valuesE = AluminiyProduct.objects.filter(artikul =component,section ='E').values('section').annotate(total_max=Max('counter'))[0]['total_max']
                        umumiy_counter[component+'-E'] += 1
                        max_valuesE = umumiy_counter[component+'-E']
                        materiale = component+"-E{:03d}".format(max_valuesE)
                        AluminiyProduct(artikul =component,section ='E',counter=max_valuesE,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key],material=materiale).save()
                        df_new['SAP код E'][key]=materiale
                        
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
                                          'outer_side_pc_id': '',#row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
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
                        AluminiyProduct(artikul =component,section ='E',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key],material=materiale).save()
                        df_new['SAP код E'][key]=materiale
                        umumiy_counter[component+'-E'] = 1
                        
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
                                          'outer_side_pc_id': '',#row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
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
                        if AluminiyProduct.objects.filter(artikul =component,section ='Z').exists():
                              umumiy_counter[ component +'-Z'] += 1
                              max_valuesZ = umumiy_counter[ component +'-Z']
                              materiale = component+"-Z{:03d}".format(max_valuesZ)
                              AluminiyProduct(artikul =component,section ='Z',counter=max_valuesZ,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Печь старения'][key],material=materiale).save()
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
                              AluminiyProduct(artikul =component,section ='Z',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Печь старения'][key],material=materiale).save()
                              df_new['SAP код Z'][key]=materiale
                              umumiy_counter[ component +'-Z'] = 1
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
                        if AluminiyProduct.objects.filter(artikul =component,section ='P').exists():
                              umumiy_counter[component+'-P'] += 1
                              
                              max_valuesP = umumiy_counter[ component +'-P']
                              materiale = component+"-P{:03d}".format(max_valuesP)
                              AluminiyProduct(artikul =component,section ='P',counter=max_valuesP,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Покраска автомат'][key],material=materiale).save()
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
                              AluminiyProduct(artikul =component,section ='P',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Покраска автомат'][key],material=materiale).save()
                              df_new['SAP код P'][key] = materiale
                              umumiy_counter[component+'-P'] = 1
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
                        if AluminiyProduct.objects.filter(artikul =component,section ='S').exists():
                              umumiy_counter[component+'-S'] += 1
                              max_valuesS = umumiy_counter[ component +'-S']
                              materiale = component+"-S{:03d}".format(max_valuesS)
                              AluminiyProduct(artikul =component,section ='S',counter=max_valuesS,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Сублимация'][key],material=materiale).save()
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
                              AluminiyProduct(artikul =component,section ='S',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Сублимация'][key],material=materiale).save()
                              df_new['SAP код S'][key]=materiale
                              umumiy_counter[component+'-S'] = 1
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
                        if AluminiyProduct.objects.filter(artikul =component,section ='A').exists():
                              umumiy_counter[component+'-A'] += 1
                              max_valuesA = umumiy_counter[ component +'-A']
                              materiale = component+"-A{:03d}".format(max_valuesA)
                              AluminiyProduct(artikul =component,section ='A',counter=max_valuesA,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Анодировка'][key],material=materiale).save()
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
                              AluminiyProduct(artikul =component,section ='A',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Анодировка'][key],material=materiale).save()
                              df_new['SAP код A'][key]=materiale
                              umumiy_counter[component+'-A'] = 1
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
                        if  AluminiyProduct.objects.filter(artikul =component,section ='N').exists():
                              umumiy_counter[component+'-N'] += 1
                              max_valuesN = umumiy_counter[ component +'-N']
                              materiale = component+"-N{:03d}".format(max_valuesN)
                              AluminiyProduct(artikul =component,section ='N',counter=max_valuesN,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Наклейка'][key],material=materiale).save()
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
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {
                                                'material':materiale,
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
                              AluminiyProduct(artikul =component,section ='N',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Наклейка'][key],material=materiale).save()
                              df_new['SAP код N'][key]=materiale
                              umumiy_counter[component+'-N'] = 1
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
            
            
      
      
      
      parent_dir ='{MEDIA_ROOT}\\uploads\\aluminiy\\'
       
      if not os.path.isdir(parent_dir):
            create_folder(f'{MEDIA_ROOT}\\uploads\\','aluminiy')
            
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\',f'{year}')
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\',f'{month}')
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\',day)
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\',hour)
      
      df_char = create_characteristika(cache_for_cratkiy_text) 
      df_char_title =create_characteristika_utils(cache_for_cratkiy_text)
                 
      
            
      if not os.path.isfile(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\alumin_new-{minut}.xlsx'):
            path =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\alumin_new-{minut}.xlsx'
      else:
            st =random.randint(0,1000)
            path =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\alumin_new-{minut}-{st}.xlsx'
      if  len(duplicat_list)>0:     
            df_duplicates =pd.DataFrame(np.array(duplicat_list),columns=['SAP CODE','KRATKIY TEXT','SECTION'])
      else:
            df_duplicates =pd.DataFrame(np.array([['','','']]),columns=['SAP CODE','KRATKIY TEXT','SECTION'])



      for key,razlov in df_new.iterrows():
            if not RazlovkaObichniy.objects.filter(sap_code7=razlov['SAP код 7'],kratkiy7=razlov['U-Упаковка + Готовая Продукция']).exists():
                  RazlovkaObichniy(
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
                        lsap_code =razlov['SAP код L'],
                        lkratkiy =razlov['Ламинация'],
                        nsap_code =razlov['SAP код N'],
                        nkratkiy =razlov['Наклейка'],
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
      df_new.to_excel(writer,index=False,sheet_name='Schotchik')
      df_char.to_excel(writer,index=False,sheet_name='Characteristika')
      df_char_title.to_excel(writer,index=False,sheet_name='title')
      df_duplicates.to_excel(writer,index=False,sheet_name='Duplicates')
      writer.close()
      
      return redirect('upload_product')
                  
def product_add_second_org(request,id):
      file = AluFile.objects.get(id=id).file
      df = pd.read_excel(f'{MEDIA_ROOT}/{file}')
      df =df.astype(str)
      
      now = datetime.now()
      year =now.strftime("%Y")
      month =now.strftime("%B")
      day =now.strftime("%a%d")
      hour =now.strftime("%H HOUR")
      minut =now.strftime("%M")
      
      doesnotexist,correct = check_for_correct(df,filename='aluminiy')
      if not correct:
            context ={
                  'CharUtilsOne':doesnotexist[0],
                  'CharUtilsTwo':doesnotexist[1],
                  'BazaProfile':doesnotexist[2],
                  'ArtikulComponent':doesnotexist[3]
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
          
            df_artikul_component =pd.DataFrame({
                  'artikul':doesnotexist[3],
                  'component':doesnotexist[3],
                  'seria':['' for i in doesnotexist[3]],
                  'product_description_ru1':['' for i in doesnotexist[3]],
                  'product_description_ru':['' for i in doesnotexist[3]],
                  'stariy_code_benkam':['' for i in doesnotexist[3]],
                  'stariy_code_jomiy':['' for i in doesnotexist[3]],
                  'proverka_artikul2':['' for i in doesnotexist[3]],
                  'proverka_component2':['' for i in doesnotexist[3]],
                  'gruppa_materialov':['' for i in doesnotexist[3]],
                  'gruppa_materialov2':['' for i in doesnotexist[3]]
            })
            create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\','Not Exists')
            
            path_not_exists =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\Not Exists\\Not_Exists.xlsx'
            
            if os.path.isfile(path_not_exists):
                  try:
                        os.remove(path_not_exists)
                  except:
                        return render(request,'utils/file_exist_org.html')
            
            writer = pd.ExcelWriter(path_not_exists, engine='xlsxwriter')
            df_char_utils_one.to_excel(writer,index=False,sheet_name ='character utils one')
            df_char_utils_two.to_excel(writer,index=False,sheet_name ='character utils two')
            df_baza_profiley.to_excel(writer,index=False,sheet_name ='baza profile')
            df_artikul_component.to_excel(writer,index=False,sheet_name ='artikul component')
            writer.close()
            # writer.save()
            return render(request,'utils/components.html',context)
      
      aluminiy_group = AluminiyProduct.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
      umumiy_counter={}
      for al in aluminiy_group:
            umumiy_counter[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      
      aluminiy_group_termo = AluminiyProductTermo.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
      umumiy_counter_termo = {}
      for al in aluminiy_group_termo:
            umumiy_counter_termo[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      
      
      
      
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
      df_new['SAP код L']=''
      df_new['Ламинация']=''
      df_new['SAP код N']=''
      df_new['Наклейка']=''
      df_new['SAP код 7']=''
      df_new['U-Упаковка + Готовая Продукция']=''
      df_new['SAP код F']=''
      df_new['Фабрикация']=''
      df_new['SAP код 75']=''
      df_new['U-Упаковка + Готовая Продукция 75']=''

      
      
      
      cache_for_cratkiy_text =[]
      duplicat_list =[]
      
      exturision_list = []
      
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
            
            
            
            product_exists = ArtikulComponent.objects.filter(artikul=row['Артикул']).exists()
            if row['Код декор пленки снаружи'] !='nan' and '.0' in row['Код декор пленки снаружи']:
                  df['Код декор пленки снаружи'][key] =df['Код декор пленки снаружи'][key].replace('.0','')
            
            if product_exists:
                  component = ArtikulComponent.objects.filter(artikul=row['Артикул'])[:1].get().component
            else:
                  if ArtikulComponent.objects.filter(component=row['Артикул']).exists():
                        component = row['Артикул']
                        termo = True
                  else:
                        continue
                  
            if df['Длина при выходе из пресса'][key] != 'nan':
                  dlina = df['Длина при выходе из пресса'][key].replace('.0','')
                        
                  df_new['Фабрикация'][key]=fabrikatsiya_sap_kod(df['Краткий текст товара'][key],df['Длина (мм)'][key])
                  df_new['U-Упаковка + Готовая Продукция 75'][key]=fabrikatsiya_sap_kod(df['Краткий текст товара'][key],df['Длина (мм)'][key])
                  
                  
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
                  if AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='F',kratkiy_tekst_materiala=df_new['Фабрикация'][key]).exists():
                        df_new['SAP код F'][key] = AluminiyProduct.objects.filter(artikul = df['Артикул'][key],section ='F',kratkiy_tekst_materiala=df_new['Фабрикация'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код F'][key],df_new['Фабрикация'][key],'F'])
                  else: 
                        if AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='F').exists():
                              umumiy_counter[df['Артикул'][key]+'-F'] += 1
                              max_valuesF = umumiy_counter[df['Артикул'][key]+'-F']
                              materiale = df['Артикул'][key] +"-F{:03d}".format(max_valuesF)
                              AluminiyProduct(artikul =df['Артикул'][key],section ='F',counter=max_valuesF,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Фабрикация'][key],material=materiale).save()
                              df_new['SAP код F'][key]=materiale
                              component2 = materiale.split('-')[0]
                             
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                                                'rawmat_type':'ПФ',
                                                'wms_width':width_and_height.ширина,
                                                'wms_height':width_and_height.высота,
                                                'group_prise': export_description_eng.group_price,
                                                }
                                          )
                              
                        else:
                              materiale = df['Артикул'][key] +"-F{:03d}".format(1)
                              AluminiyProduct(artikul =df['Артикул'][key],section ='F',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Фабрикация'][key],material=materiale).save()
                              df_new['SAP код F'][key]=materiale
                              umumiy_counter[df['Артикул'][key]+'-F'] = 1
                              component2 = materiale.split('-')[0]
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                                                'rawmat_type':'ПФ',
                                                'wms_width':width_and_height.ширина,
                                                'wms_height':width_and_height.высота,
                                                'group_prise': export_description_eng.group_price,
                                                }
                                          )
                              
                              
                  
                  
                  if AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='75',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key]).exists():
                        df_new['SAP код 75'][key] = AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='75',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код 75'][key],df_new['U-Упаковка + Готовая Продукция 75'][key],'75'])
                  else: 
                        if AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='75').exists():
                              umumiy_counter[df['Артикул'][key]+'-75'] += 1
                              max_values75 = umumiy_counter[df['Артикул'][key]+'-75']
                              
                              if max_values75 <= 99:
                                    materiale = df['Артикул'][key]+"-75{:02d}".format(max_values75)
                              else:
                                    counter =7500 + max_values75
                                    materiale = df['Артикул'][key]+"-{:04d}".format(counter)
                                    
                                    
                              AluminiyProduct(artikul =df['Артикул'][key],section ='75',counter=max_values75,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key],material=materiale).save()
                              df_new['SAP код 75'][key] = materiale
                              
                             
                              component2 = materiale.split('-')[0]
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                                    surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']] +' ' + row['Код краски снаружи']
                              elif row['Тип покрытия'].lower() =='сублимированный':
                                    surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                              elif row['Тип покрытия'].lower() =='анодированный':
                                    surface_treatment_export = row['Код цвета анодировки снаружи']
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
                              AluminiyProduct(artikul = df['Артикул'][key],section ='75',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key],material=materiale).save()
                              df_new['SAP код 75'][key] = materiale 
                              umumiy_counter[df['Артикул'][key]+'-75'] = 1
                              
                              component2 = materiale.split('-')[0]
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                                    surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']]+' '+row['Код краски снаружи']
                              elif row['Тип покрытия'].lower() =='сублимированный':
                                    surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                              elif row['Тип покрытия'].lower() =='анодированный':
                                    surface_treatment_export = row['Код цвета анодировки снаружи']
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
                  if AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key]).exists():
                        df_new['SAP код 7'][key] = AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код 7'][key],df_new['U-Упаковка + Готовая Продукция'][key],'7'])
                  else: 
                        if AluminiyProduct.objects.filter(artikul=df['Артикул'][key],section ='7').exists():
                              umumiy_counter[df['Артикул'][key]+'-7'] += 1
                              max_values7 = umumiy_counter[df['Артикул'][key]+'-7']
                              materiale = df['Артикул'][key]+"-7{:03d}".format(max_values7)
                              AluminiyProduct(artikul = df['Артикул'][key],section ='7',counter=max_values7,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key],material=materiale).save()
                              df_new['SAP код 7'][key] = materiale
                              
                              component2 = materiale.split('-')[0]
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                                    surface_treatment_export = row['Код цвета анодировки снаружи']
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
                              AluminiyProduct(artikul = df['Артикул'][key],section ='7',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key],material=materiale).save()
                              df_new['SAP код 7'][key] = materiale
                              umumiy_counter[df['Артикул'][key]+'-7'] = 1
                             
                              component2 = materiale.split('-')[0]
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                                    surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']] + ' ' + row['Код краски снаружи']
                              elif row['Тип покрытия'].lower() =='сублимированный':
                                    surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                              elif row['Тип покрытия'].lower() =='анодированный':
                                    surface_treatment_export = row['Код цвета анодировки снаружи']
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
                        
                  ##### kombirinovanniy
            
                   
            
            if df['Тип покрытия'][key] == 'Ламинированный':      
                  if AluminiyProduct.objects.filter(artikul =component,section ='L',kratkiy_tekst_materiala=df_new['Ламинация'][key]).exists():
                        df_new['SAP код L'][key] = AluminiyProduct.objects.filter(artikul =component,section ='L',kratkiy_tekst_materiala=df_new['Ламинация'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код L'][key],df_new['Ламинация'][key],'L'])
                  else: 
                        if AluminiyProduct.objects.filter(artikul =component,section ='L').exists():
                              umumiy_counter[component+'-L'] += 1
                              max_valuesL = umumiy_counter[ component +'-L']
                              materiale = component+"-L{:03d}".format(max_valuesL)
                              AluminiyProduct(artikul =component,section ='L',counter=max_valuesL,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Ламинация'][key],material=materiale).save()
                              df_new['SAP код L'][key]=materiale
                             
                              component2 = materiale.split('-')[0]
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                                                'kratkiy':df_new['Ламинация'][key],
                                                'section':'L-Ламинирование',
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
                              AluminiyProduct(artikul =df['Артикул'][key],section ='L',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Ламинация'][key],material=materiale).save()
                              df_new['SAP код L'][key]=materiale
                              umumiy_counter[df['Артикул'][key]+'-L'] = 1
                             
                              component2 = materiale.split('-')[0]
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Ламинация'][key],
                                                'section':'L-Ламинирование',
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
                        df_new['Наклейка'][key]= df_new['Анодировка'][key] +' ' + row['Код наклейки'].replace('.0','')
            else:
                  pass
                  
            
            termo_existE =AluminiyProductTermo.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key]).exists()
            simple_existE =AluminiyProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key]).exists()

           
            
            if (termo_existE or simple_existE):
                  if termo_existE:
                        sap_code_e = AluminiyProductTermo.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key])[:1].get().material
                  else:
                        sap_code_e = AluminiyProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key])[:1].get().material
                  duplicat_list.append([df_new['SAP код E'][key],df_new['Экструзия холодная резка'][key],'E'])
                  df_new['SAP код E'][key] = sap_code_e

                  if row['тип закаленности']=='T4':
                        exturision_list.append(sap_code_e)
            else:
                  if AluminiyProduct.objects.filter(artikul =component,section ='E').exists():
                        # max_valuesE = AluminiyProduct.objects.filter(artikul =component,section ='E').values('section').annotate(total_max=Max('counter'))[0]['total_max']
                        umumiy_counter[component+'-E'] += 1
                        max_valuesE = umumiy_counter[component+'-E']
                        materiale = component+"-E{:03d}".format(max_valuesE)
                        AluminiyProduct(artikul =component,section ='E',counter=max_valuesE,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key],material=materiale).save()
                        df_new['SAP код E'][key]=materiale
                        
                        if row['тип закаленности']=='T4':
                              exturision_list.append(materiale)

                        component2 = materiale.split('-')[0]
                        artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                                          'outer_side_pc_id': '',#row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
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
                        AluminiyProduct(artikul =component,section ='E',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key],material=materiale).save()
                        df_new['SAP код E'][key]=materiale
                        umumiy_counter[component+'-E'] = 1
                        
                        component2 = materiale.split('-')[0]
                        artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                                          'outer_side_pc_id': '',#row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
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
                        if AluminiyProduct.objects.filter(artikul =component,section ='Z').exists():
                              umumiy_counter[ component +'-Z'] += 1
                              max_valuesZ = umumiy_counter[ component +'-Z']
                              materiale = component+"-Z{:03d}".format(max_valuesZ)
                              AluminiyProduct(artikul =component,section ='Z',counter=max_valuesZ,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Печь старения'][key],material=materiale).save()
                              df_new['SAP код Z'][key]=materiale
                              
                              
                              component2 = materiale.split('-')[0]
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                              AluminiyProduct(artikul =component,section ='Z',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Печь старения'][key],material=materiale).save()
                              df_new['SAP код Z'][key]=materiale
                              umumiy_counter[ component +'-Z'] = 1
                            
                              component2 = materiale.split('-')[0]
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                        if AluminiyProduct.objects.filter(artikul =component,section ='P').exists():
                              umumiy_counter[component+'-P'] += 1
                              
                              max_valuesP = umumiy_counter[ component +'-P']
                              materiale = component+"-P{:03d}".format(max_valuesP)
                              AluminiyProduct(artikul =component,section ='P',counter=max_valuesP,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Покраска автомат'][key],material=materiale).save()
                              df_new['SAP код P'][key]=materiale
                              
                              component2 = materiale.split('-')[0]
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                              AluminiyProduct(artikul =component,section ='P',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Покраска автомат'][key],material=materiale).save()
                              df_new['SAP код P'][key] = materiale
                              umumiy_counter[component+'-P'] = 1
                              
                              component2 = materiale.split('-')[0]
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                        if AluminiyProduct.objects.filter(artikul =component,section ='S').exists():
                              umumiy_counter[component+'-S'] += 1
                              max_valuesS = umumiy_counter[ component +'-S']
                              materiale = component+"-S{:03d}".format(max_valuesS)
                              AluminiyProduct(artikul =component,section ='S',counter=max_valuesS,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Сублимация'][key],material=materiale).save()
                              df_new['SAP код S'][key]=materiale
                              
                              component2 = materiale.split('-')[0]
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                              AluminiyProduct(artikul =component,section ='S',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Сублимация'][key],material=materiale).save()
                              df_new['SAP код S'][key]=materiale
                              umumiy_counter[component+'-S'] = 1
                            
                              component2 = materiale.split('-')[0]
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                        if AluminiyProduct.objects.filter(artikul =component,section ='A').exists():
                              umumiy_counter[component+'-A'] += 1
                              max_valuesA = umumiy_counter[ component +'-A']
                              materiale = component+"-A{:03d}".format(max_valuesA)
                              AluminiyProduct(artikul =component,section ='A',counter=max_valuesA,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Анодировка'][key],material=materiale).save()
                              df_new['SAP код A'][key]=materiale
                            
                              component2 = materiale.split('-')[0]
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                              AluminiyProduct(artikul =component,section ='A',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Анодировка'][key],material=materiale).save()
                              df_new['SAP код A'][key]=materiale
                              umumiy_counter[component+'-A'] = 1
                             
                              component2 = materiale.split('-')[0]
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                        if  AluminiyProduct.objects.filter(artikul =component,section ='N').exists():
                              umumiy_counter[component+'-N'] += 1
                              max_valuesN = umumiy_counter[ component +'-N']
                              materiale = component+"-N{:03d}".format(max_valuesN)
                              AluminiyProduct(artikul =component,section ='N',counter=max_valuesN,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Наклейка'][key],material=materiale).save()
                              df_new['SAP код N'][key]=materiale
                        
                              component2 = materiale.split('-')[0]
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
                                                {
                                                'material':materiale,
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
                              AluminiyProduct(artikul =component,section ='N',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Наклейка'][key],material=materiale).save()
                              df_new['SAP код N'][key]=materiale
                              umumiy_counter[component+'-N'] = 1
                             
                              component2 = materiale.split('-')[0]
                              artikle = ArtikulComponent.objects.get(Q(artikul=component2)|Q(component=component2)).artikul
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
            
            
      
      
      
      parent_dir ='{MEDIA_ROOT}\\uploads\\aluminiy\\'
       
      if not os.path.isdir(parent_dir):
            create_folder(f'{MEDIA_ROOT}\\uploads\\','aluminiy')
            
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\',f'{year}')
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\',f'{month}')
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\',day)
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\',hour)
      
      df_char = create_characteristika(cache_for_cratkiy_text) 
      df_char_title =create_characteristika_utils(cache_for_cratkiy_text)
                 
      
            
      if not os.path.isfile(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\alumin_new-{minut}.xlsx'):
            path =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\alumin_new-{minut}.xlsx'
      else:
            st =random.randint(0,1000)
            path =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\alumin_new-{minut}-{st}.xlsx'
      if  len(duplicat_list)>0:     
            df_duplicates =pd.DataFrame(np.array(duplicat_list),columns=['SAP CODE','KRATKIY TEXT','SECTION'])
      else:
            df_duplicates =pd.DataFrame(np.array([['','','']]),columns=['SAP CODE','KRATKIY TEXT','SECTION'])

      df_extrusion = pd.DataFrame({'SAP CODE E' : exturision_list})


      for key,razlov in df_new.iterrows():
            if razlov['SAP код 7']!="":
                  if not RazlovkaObichniy.objects.filter(sap_code7=razlov['SAP код 7'],kratkiy7=razlov['U-Упаковка + Готовая Продукция']).exists():
                        RazlovkaObichniy(
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
                              lsap_code =razlov['SAP код L'],
                              lkratkiy =razlov['Ламинация'],
                              nsap_code =razlov['SAP код N'],
                              nkratkiy =razlov['Наклейка'],
                              sap_code7 =razlov['SAP код 7'],
                              kratkiy7 =razlov['U-Упаковка + Готовая Продукция'],
                              fsap_code =razlov['SAP код F'],
                              fkratkiy =razlov['Фабрикация'],
                              sap_code75 =razlov['SAP код 75'],
                              kratkiy75 =razlov['U-Упаковка + Готовая Продукция 75']
                        ).save()
            elif razlov['SAP код 75']!= '':
                  if not RazlovkaObichniy.objects.filter(sap_code75=razlov['SAP код 75'],kratkiy75=razlov['U-Упаковка + Готовая Продукция 75']).exists():
                        RazlovkaObichniy(
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
                              lsap_code =razlov['SAP код L'],
                              lkratkiy =razlov['Ламинация'],
                              nsap_code =razlov['SAP код N'],
                              nkratkiy =razlov['Наклейка'],
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

      writer = pd.ExcelWriter(path, engine='xlsxwriter')
      df_new.to_excel(writer,index=False,sheet_name='Schotchik')
      df_char.to_excel(writer,index=False,sheet_name='Characteristika')
      df_char_title.to_excel(writer,index=False,sheet_name='title')
      df_extrusion.to_excel(writer,index=False,sheet_name='T4')
      writer.close()
      file =[File(file=path,filetype='obichniy')]
      context ={
            'files':file,
            'section':'Формированый обычный файл'
      }
      return render(request,'universal/generated_files.html',context)
                  
import glob
def razlovka_save(request):
      
      dir_path = f'{MEDIA_ROOT}\\uploads\\aluminiy\\**\*alumin*.*'
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
            
      # print(path_list_iyun,'\n',path_list_aprel,'\n',path_list_may)
      # print('#'*25)
      path_list_iyun.sort()
      iyun = path_list_iyun[::-1]
      path_list_aprel.sort()
      aprel =path_list_aprel[::-1]
      path_list_may.sort()
      may =path_list_may[::-1]

      for path1 in iyun:
            if 'Копия' in path1:
                  continue
            print(path1)
            df_new = pd.read_excel(path1,sheet_name=['Schotchik','Characteristika','title'])
            df_new['Schotchik'] =df_new['Schotchik'].astype(str)
            df_new['Characteristika'] =df_new['Characteristika'].astype(str)
            df_new['title'] =df_new['title'].astype(str)
            df_new['Schotchik']=df_new['Schotchik'].replace('nan','')
            df_new['Characteristika']=df_new['Characteristika'].replace('nan','')
            df_new['title']=df_new['title'].replace('nan','')
            try:
                  df_new['Schotchik']['SAP код E']=df_new['Schotchik']['SAP код E']
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
                  lsap ='SAP код L'
                  lkrat ='Ламинация'
                  nsap ='SAP код N'
                  nkrat ='Наклейка'
                  sap7 ='SAP код 7'

                  try:
                        df_new['Schotchik']['U-Упаковка + Готовая Продукция 7']=df_new['Schotchik']['U-Упаковка + Готовая Продукция 7']
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
                  lsap ='lkrat_counter'
                  lkrat ='lkrat'
                  nsap ='nkrat_counter'
                  nkrat ='nkrat'
                  sap7 ='ukrat1_counter'
                  df_name='ukrat1'
            
                  

            for key,razlov in df_new['Schotchik'].iterrows():
                  if not RazlovkaObichniy.objects.filter(sap_code7=razlov[sap7],kratkiy7=razlov[df_name]).exists():
                        RazlovkaObichniy(
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
                              lsap_code =razlov[lsap],
                              lkratkiy =razlov[lkrat],
                              nsap_code =razlov[nsap],
                              nkratkiy =razlov[nkrat],
                              sap_code7 =razlov[sap7],
                              kratkiy7 =razlov[df_name]
                        ).save()
            for key,razlov in df_new['Characteristika'].iterrows():
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
            items = [CharUtilsOne(матрица =item['matritsa'],артикул =item['artikul'],высота=item['heigth'],ширина=item['width'],высота_ширина=item['heigth']+'X'+item['width'],systems=item['systems']) for item in ast.literal_eval(data)]
            CharUtilsOne.objects.bulk_create(items)
            return JsonResponse({'saved':True})
      else:
            return JsonResponse({'saved':False})
      
@csrf_exempt
def baza_profile(request):
      data = request.POST.get('data',None)
      for item in ast.literal_eval(data):
            if BazaProfiley.objects.filter(артикул =item['artikul'],компонент =item['komponent']).exists():
                  bazaprofiles = BazaProfiley.objects.filter(артикул =item['artikul'],компонент =item['komponent'])[:1].get()
                  bazaprofiles.delete()

      if data:
            items = [BazaProfiley(компонент =item['komponent'],артикул =item['artikul'],серия=item['seria'],старый_код=item['stariykod'],product_description=item['prodesc'],link = item['link']) for item in ast.literal_eval(data)]
            BazaProfiley.objects.bulk_create(items)
            return JsonResponse({'saved':True})
      else:
            return JsonResponse({'saved':False})
      
@csrf_exempt
def artikul_component(request):
      data = request.POST.get('data',None)
      if data:
            items = [ArtikulComponent(artikul =item['artikul'],component =item['komponent']) for item in ast.literal_eval(data)]
            ArtikulComponent.objects.bulk_create(items)
            return JsonResponse({'saved':True})
      else:
            return JsonResponse({'saved':False})
      
@csrf_exempt
def excel_does_not_exists_add(request):
      now = datetime.now()
      year =now.strftime("%Y")
      
      path_not_exists =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\Not Exists\\Not_Exists.xlsx'
      all_correct = True
      df = pd.read_excel(path_not_exists,sheet_name=['character utils one','character utils two','baza profile','artikul component'])
      # print(df['artikul component'])
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
                  print('character utils two')
                  all_correct =False
            
      
      items =[]
      if df['baza profile'].shape[0] > 0:
            for key,row in df['baza profile'].iterrows():
                  items.append(BazaProfiley(компонент = row['компонент'],артикул = row['артикул'],серия= row['серия'],старый_код= row['старый_код'],product_description= row['product_description'],link =row['link']))
            try:
                  BazaProfiley.objects.bulk_create(items)
            except:
                  all_correct =False
                  
      items =[]
      if df['artikul component'].shape[0] > 0:
            for key,row in df['artikul component'].iterrows():
                  items.append(ArtikulComponent(artikul = row['artikul'],component = row['component']))
            try:
                  ArtikulComponent.objects.bulk_create(items)
            except:
                  print('artikul component')
                  all_correct =False
            
      
      return JsonResponse({'saved':all_correct})
 
 
def duplicate_correct(request):
      df = pd.read_excel(f'{MEDIA_ROOT}\\example.xlsx')
      for key,row in df.iterrows():
            simple = AluminiyProduct.objects.filter(material =row['material'])
            for sim in simple:
                  sim.kratkiy_tekst_materiala =row['kratkiy_tekst_materiala']
                  sim.save()
                  
            termo = AluminiyProductTermo.objects.filter(material =row['material'])
            for ter in termo:
                  ter.kratkiy_tekst_materiala =row['kratkiy_tekst_materiala']
                  ter.save()
                  
      return JsonResponse({'a':'b'})

def show_list_simple_sapcodes(request):
      search =request.GET.get('search',None)
      if search:
            try:
                  try:
                        f_date = datetime.strptime(search,'%m.%d.%Y %H:%M')
                        products = AluminiyProduct.objects.filter(
                              created_at__year =f_date.year,
                              created_at__month =f_date.month,
                              created_at__day =f_date.day,
                              created_at__hour =f_date.hour,
                              created_at__minute =f_date.minute
                        )
                  except:
                        f_date = datetime.strptime(search,'%m.%d.%Y')
                        products = AluminiyProduct.objects.filter(
                              created_at__year =f_date.year,
                              created_at__month =f_date.month,
                              created_at__day =f_date.day
                        )
                  
            except:
                  products = AluminiyProduct.objects.filter(
                        Q(material__icontains=search)
                        |Q(artikul__icontains=search)
                        |Q(section__icontains=search)
                        |Q(gruppa_materialov__icontains=search)
                        |Q(kratkiy_tekst_materiala__icontains=search)
                        |Q(kombinirovanniy__icontains=search)
                        ).order_by('-created_at')
      else:
            products =AluminiyProduct.objects.all().order_by('-created_at')
                  
      paginator = Paginator(products, 25)

      if request.GET.get('page') != None:
            page_number = request.GET.get('page')
      else:
            page_number=1

      page_obj = paginator.get_page(page_number)

      context ={
            'section':'Обычный сапкоды',
            'products':page_obj,
            'search':search,
            'type':'simple'

      }
      return render(request,'universal/show_sapcodes.html',context)


@csrf_exempt
def delete_sap_code(request,id):
      if request.method =='POST':
            file_type = request.POST.get('type',None)
            if file_type =='simple':
                  sapcode = AluminiyProduct.objects.get(id=id)
                  if Characteristika.objects.filter(sap_code=sapcode.material).exists():
                        character =Characteristika.objects.filter(sap_code=sapcode.material).order_by('-created_at')[:1].get()
                        character.delete()
                  if '-7' in sapcode.material:
                        if RazlovkaObichniy.objects.filter(sap_code7 = sapcode.material).exists():
                              RazlovkaObichniy.objects.get(sap_code7 = sapcode.material).delete()
                  sapcode.delete()
                  
            else:
                  sapcode = AluminiyProductTermo.objects.get(id=id)
                  if Characteristika.objects.filter(sap_code=sapcode.material).exists():
                        character =Characteristika.objects.filter(sap_code=sapcode.material).order_by('-created_at')[:1].get()
                        character.delete()

                  if '-7' in sapcode.material:
                        if RazlovkaTermo.objects.filter(sap_code7 = sapcode.material).exists():
                              termo =RazlovkaTermo.objects.get(sap_code7 = sapcode.material)
                              components =RazlovkaTermo.objects.filter(parent_id =termo.id)
                              components.delete()
                              termo.delete()
                  sapcode.delete()

            return JsonResponse({'msg':True})
      else:
            return JsonResponse({'msg':False})