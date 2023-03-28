from django.shortcuts import render,redirect
from django.http import JsonResponse
import pandas as pd
from .models import ArtikulComponent,AluminiyProduct,AluFile,AluminiyProductTermo,AluminiyProductBasesimple,AluminiyProductBasetermo
from main.models import ExcelFiles
from .forms import FileForm
from django.db.models import Count,Max
from config.settings import MEDIA_ROOT
import numpy as np
from .utils import fabrikatsiya_sap_kod,do_exist
import datetime


# Create your views here.


def artikul_and_companent(request):
      df = pd.read_excel('c:\\OpenServer\\domains\\new_component.xlsx','Лист1')
      print(df.shape)
      # print(df['АРТИКУЛ'][0])
      # print(df['АРТИКУЛ'][3749])
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
  print(df.shape)
#   print(df['Материал'][0])
#   print(df['Материал'][39705])
  
  for i in range(0,60696):
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
  print(df.shape)
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

def aluminiy_files(request):
  files = AluFile.objects.filter(generated =False)
  context ={'files':files}
  return render(request,'alu_file_list.html',context)

def aluminiy_group(request):
      aluminiy_group =AluminiyProduct.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
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


def product_add(request,id):
      file = AluFile.objects.get(id=id).file
      df = pd.read_excel(f'{MEDIA_ROOT}/{file}')
      df =df.astype(str)
      
      
      ################### group by#########
      aluminiy_group = AluminiyProduct.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
      umumiy_counter={}
      for al in aluminiy_group:
            umumiy_counter[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      ############################ end grouby ######
      
      
      a=datetime.datetime.now()
      print('starts in ...',a)
      for key,row in df.iterrows():
            if row['Тип покрытия'] == 'nan':
                  df = df.drop(key)
      
      
      
      df_new =pd.DataFrame()
      df_new['artikul']=df['Артикул']
      df_new['ekrat_counter']=''
      df_new['ekrat']=''
      df_new['zkrat_counter']=''
      df_new['zkrat']=''
      df_new['pkrat_counter']=''
      df_new['pkrat']=''
      df_new['skrat_counter']=''
      df_new['skrat']=''
      df_new['akrat_counter']=''
      df_new['akrat']=''
      df_new['lkrat_counter']=''
      df_new['lkrat']=''
      df_new['nkrat_counter']=''
      df_new['nkrat']=''
      df_new['ukrat1_counter']=''
      df_new['ukrat1']=''
      df_new['fkrat_counter']=''
      df_new['fkrat']=''
      df_new['ukrat2_counter']=''
      df_new['ukrat2']=''
      
      
      
      # exists =ArtikulComponent.objects.filter(artikul__in =df['Артикул'])
      # print(df['Артикул'])
      # print(type(df['Артикул']))
      
      for key,row in df.iterrows():
            
            product_exists = ArtikulComponent.objects.filter(artikul=row['Артикул']).exists()
            if row['Код декор пленки снаружи'] !='nan' and '.0' in row['Код декор пленки снаружи']:
                  df['Код декор пленки снаружи'][key] =df['Код декор пленки снаружи'][key].replace('.0','')
            
            if product_exists:
                  component = ArtikulComponent.objects.filter(artikul=row['Артикул'])[:1].get().component
            else:
                  print('no components!!')
                  continue
            
            
            # print(component,AluminiyProduct.objects.filter(artikul =component,section ='E').values('section').annotate(total_max=Max('counter'))[0]['total_max'])
            dlina =''
            if row['Длина при выходе из пресса'] != 'nan':
                  if '.0' in row['Длина при выходе из пресса']:
                        dlina = row['Длина при выходе из пресса'].replace('.0','')
                  else:
                        dlina = row['Длина при выходе из пресса']
                        
                  df_new['fkrat'][key]=fabrikatsiya_sap_kod(row['Краткий текст товара'],row['Длина (мм)'])
                  df_new['ukrat2'][key]=fabrikatsiya_sap_kod(row['Краткий текст товара'],row['Длина (мм)'])
            else:
                  dlina = row['Длина (мм)']
                  df_new['ukrat1'][key]=row['Краткий текст товара']
                  
            df_new['ekrat'][key] = row['Сплав'][len(row['Сплав'])-2:] +'T4 '+'L'+dlina+' MF'
            df_new['zkrat'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' MF'
            
            
                        
            if ((row['Тип покрытия'] == 'Окрашенный') or (row['Тип покрытия'] == 'Белый' )):
                  df_new['pkrat'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи']+row['Код краски снаружи']
                  if row['Код наклейки'] != 'NT1':
                        df_new['nkrat'][key] = df_new['pkrat'][key] +' '+ row['Код наклейки'].replace('.0','')
                  
                        
            elif row['Тип покрытия'] == 'Ламинированный':
                  df_new['pkrat'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи']+row['Код краски снаружи']
                  
                  if row['Код лам пленки снаружи'] != 'nan':
                        laminatsiya =row['Код лам пленки снаружи'].replace('.0','')+'/XXXX'
                        
                  if row['Код лам пленки внутри'] != 'nan':
                        laminatsiya ='XXXX/'+row['Код лам пленки внутри'].replace('.0','')
                        
                  if ((row['Код лам пленки снаружи'] != 'nan') and (row['Код лам пленки внутри'] != 'nan')):
                        laminatsiya =row['Код лам пленки снаружи'].replace('.0','') +'/'+ row['Код лам пленки внутри'].replace('.0','')
                        
                        
                  df_new['lkrat'][key]=row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')+'_'+laminatsiya +' ' +row['Код наклейки']
                  
                  # if row['Код наклейки'] != 'NT1':
                  #       df_new['nkrat'][key]=df_new['lkrat'][key] + ' ' +row['Код наклейки'].replace('.0','')
                        
            elif row['Тип покрытия'] =='Сублимированный':
                  df_new['pkrat'][key]=row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')
                  df_new['skrat'][key]=row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')+'_'+row['Код декор пленки снаружи'].replace('.0','')
                  
                  if row['Код наклейки'] != 'NT1':
                        df_new['nkrat'][key]=df_new['skrat'][key] + ' ' + row['Код наклейки'].replace('.0','')

            elif row['Тип покрытия'] =='Анодированный':
                  df_new['akrat'][key]=row['Сплав'][len(row['Сплав'])-2:] +'T6'+' L'+dlina+' '+row['Код цвета анодировки снаружи'].replace('.0','')
                  if row['Код наклейки'] != 'NT1':
                        df_new['nkrat'][key]= df_new['akrat'][key] +' '+row['Контактность анодировки']+' ' + row['Код наклейки'].replace('.0','')
            else:
                  print("<<<<<< Нет Тип покрытия ! >>>>>>")
            
            if AluminiyProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['ekrat'][key]).exists():
                  df_new['ekrat_counter'][key] = AluminiyProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['ekrat'][key])[:1].get().material
            else:
                  if AluminiyProduct.objects.filter(artikul =component,section ='E').exists():
                        # max_valuesE = AluminiyProduct.objects.filter(artikul =component,section ='E').values('section').annotate(total_max=Max('counter'))[0]['total_max']
                        umumiy_counter[ component +'-E'] += 1
                        max_valuesE = umumiy_counter[ component +'-E']
                        materiale = component+"-E{:03d}".format(max_valuesE)
                        AluminiyProduct(artikul =component,section ='E',counter=max_valuesE,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ekrat'][key],material=materiale).save()
                        df_new['ekrat_counter'][key]=materiale
                  else: 
                        materiale = component+"-E{:03d}".format(1)
                        AluminiyProduct(artikul =component,section ='E',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ekrat'][key],material=materiale).save()
                        df_new['ekrat_counter'][key]=materiale
                        
            if AluminiyProduct.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['zkrat'][key]).exists():
                  df_new['zkrat_counter'][key] = AluminiyProduct.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['zkrat'][key])[:1].get().material
            else: 
                  if AluminiyProduct.objects.filter(artikul =component,section ='Z').exists():
                        umumiy_counter[ component +'-Z'] += 1
                        max_valuesZ = umumiy_counter[ component +'-Z']
                        materiale = component+"-Z{:03d}".format(max_valuesZ)
                        AluminiyProduct(artikul =component,section ='Z',counter=max_valuesZ,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['zkrat'][key],material=materiale).save()
                        df_new['zkrat_counter'][key]=materiale
                  else:
                        materiale = component+"-Z{:03d}".format(1)
                        AluminiyProduct(artikul =component,section ='Z',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['zkrat'][key],material=materiale).save()
                        df_new['zkrat_counter'][key]=materiale
                        
            
            
            if ((row['Тип покрытия'] == 'Сублимированный') or (row['Тип покрытия'] == 'Ламинированный') or (row['Тип покрытия'] == 'Окрашенный') or (row['Тип покрытия'] == 'Белый')): 
                  if AluminiyProduct.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['pkrat'][key]).exists():
                        df_new['pkrat_counter'][key] = AluminiyProduct.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['pkrat'][key])[:1].get().material
                  else: 
                        if AluminiyProduct.objects.filter(artikul =component,section ='P').exists():
                              umumiy_counter[component+'-P'] += 1
                              
                              max_valuesP = umumiy_counter[ component +'-P']
                              materiale = component+"-P{:03d}".format(max_valuesP)
                              AluminiyProduct(artikul =component,section ='P',counter=max_valuesP,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['pkrat'][key],material=materiale).save()
                              df_new['pkrat_counter'][key]=materiale
                        else:
                              materiale = component+"-P{:03d}".format(1)
                              AluminiyProduct(artikul =component,section ='P',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['pkrat'][key],material=materiale).save()
                              df_new['pkrat_counter'][key] = materiale
                              umumiy_counter[component+'-P'] = 1
            
            if row['Тип покрытия'] =='Сублимированный':       
                  if AluminiyProduct.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['skrat'][key]).exists():
                        df_new['skrat_counter'][key] = AluminiyProduct.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['skrat'][key])[:1].get().material
                  else: 
                        if AluminiyProduct.objects.filter(artikul =component,section ='S').exists():
                              umumiy_counter[component+'-S'] += 1
                              max_valuesS = umumiy_counter[ component +'-S']
                              materiale = component+"-S{:03d}".format(max_valuesS)
                              AluminiyProduct(artikul =component,section ='S',counter=max_valuesS,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['skrat'][key],material=materiale).save()
                              df_new['skrat_counter'][key]=materiale
                        else:
                              materiale = component+"-S{:03d}".format(1)
                              AluminiyProduct(artikul =component,section ='S',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['skrat'][key],material=materiale).save()
                              df_new['skrat_counter'][key]=materiale
                              umumiy_counter[component+'-S'] = 1
            
            if row['Тип покрытия'] =='Анодированный':    
                  if AluminiyProduct.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['akrat'][key]).exists():
                        df_new['akrat_counter'][key] = AluminiyProduct.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['akrat'][key])[:1].get().material
                  else: 
                        if AluminiyProduct.objects.filter(artikul =component,section ='A').exists():
                              umumiy_counter[component+'-A'] += 1
                              max_valuesA = umumiy_counter[ component +'-A']
                              materiale = component+"-A{:03d}".format(max_valuesA)
                              AluminiyProduct(artikul =component,section ='A',counter=max_valuesA,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['akrat'][key],material=materiale).save()
                              df_new['akrat_counter'][key]=materiale
                        else:
                              materiale = component+"-A{:03d}".format(1)
                              AluminiyProduct(artikul =component,section ='A',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['akrat'][key],material=materiale).save()
                              df_new['akrat_counter'][key]=materiale
                              umumiy_counter[component+'-A'] = 1
                              
            
            if row['Тип покрытия'] == 'Ламинированный':     
                  if AluminiyProduct.objects.filter(artikul =component,section ='L',kratkiy_tekst_materiala=df_new['lkrat'][key]).exists():
                        df_new['lkrat_counter'][key] = AluminiyProduct.objects.filter(artikul =component,section ='L',kratkiy_tekst_materiala=df_new['lkrat'][key])[:1].get().material
                  else: 
                        if AluminiyProduct.objects.filter(artikul =component,section ='L').exists():
                              umumiy_counter[component+'-L'] += 1
                              max_valuesL = umumiy_counter[ component +'-L']
                              materiale = component+"-L{:03d}".format(max_valuesL)
                              AluminiyProduct(artikul =component,section ='L',counter=max_valuesL,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['lkrat'][key],material=materiale).save()
                              df_new['lkrat_counter'][key]=materiale
                        else:
                              materiale = component+"-L{:03d}".format(1)
                              AluminiyProduct(artikul =component,section ='L',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['lkrat'][key],material=materiale).save()
                              df_new['lkrat_counter'][key]=materiale
                              umumiy_counter[component+'-L'] = 1
                        
            if ((row['Код наклейки'] != 'NT1') and (row['Тип покрытия'] != 'Ламинированный')) :    
                  if AluminiyProduct.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['nkrat'][key]).exists():
                        df_new['nkrat_counter'][key] = AluminiyProduct.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['nkrat'][key])[:1].get().material
                  else:
                        if  AluminiyProduct.objects.filter(artikul =component,section ='N').exists():
                              umumiy_counter[component+'-N'] += 1
                              max_valuesN = umumiy_counter[ component +'-N']
                              materiale = component+"-N{:03d}".format(max_valuesN)
                              AluminiyProduct(artikul =component,section ='N',counter=max_valuesN,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['nkrat'][key],material=materiale).save()
                              df_new['nkrat_counter'][key]=materiale
                        else:
                              materiale = component+"-N{:03d}".format(1)
                              AluminiyProduct(artikul =component,section ='N',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['nkrat'][key],material=materiale).save()
                              df_new['nkrat_counter'][key]=materiale
                              umumiy_counter[component+'-N'] = 1
                  
                  
            if row['Длина при выходе из пресса'] != 'nan':
                  if AluminiyProduct.objects.filter(artikul =row['Артикул'],section ='F',kratkiy_tekst_materiala=df_new['fkrat'][key]).exists():
                        df_new['fkrat_counter'][key] = AluminiyProduct.objects.filter(artikul = row['Артикул'],section ='F',kratkiy_tekst_materiala=df_new['fkrat'][key])[:1].get().material
                  else: 
                        if AluminiyProduct.objects.filter(artikul =row['Артикул'],section ='F').exists():
                              umumiy_counter[row['Артикул']+'-F'] += 1
                              max_valuesF = umumiy_counter[row['Артикул']+'-F']
                              materiale = row['Артикул'] +"-F{:03d}".format(max_valuesF)
                              AluminiyProduct(artikul =row['Артикул'],section ='F',counter=max_valuesF,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['fkrat'][key],material=materiale).save()
                              df_new['fkrat_counter'][key]=materiale
                        else:
                              materiale = row['Артикул'] +"-F{:03d}".format(1)
                              AluminiyProduct(artikul =row['Артикул'],section ='F',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['fkrat'][key],material=materiale).save()
                              df_new['fkrat_counter'][key]=materiale
                              umumiy_counter[row['Артикул']+'-F'] = 1
                              
                  
                  if AluminiyProduct.objects.filter(artikul =row['Артикул'],section ='75',kratkiy_tekst_materiala=df_new['ukrat2'][key]).exists():
                        df_new['ukrat2_counter'][key] = AluminiyProduct.objects.filter(artikul =row['Артикул'],section ='75',kratkiy_tekst_materiala=df_new['ukrat2'][key])[:1].get().material
                  else: 
                        if AluminiyProduct.objects.filter(artikul =row['Артикул'],section ='75').exists():
                              umumiy_counter[row['Артикул']+'-75'] += 1
                              max_values75 = umumiy_counter[row['Артикул']+'-75']
                              
                              if max_values75 <= 99:
                                    materiale = row['Артикул']+"-75{:02d}".format(max_values75)
                              else:
                                    counter =7500 + max_values75
                                    materiale = row['Артикул']+"-{:04d}".format(counter)
                                    
                                    
                              AluminiyProduct(artikul =row['Артикул'],section ='75',counter=max_values75,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ukrat2'][key],material=materiale).save()
                              df_new['ukrat2_counter'][key]=materiale  
                        else:
                              materiale = row['Артикул']+"-75{:02d}".format(1)
                              AluminiyProduct(artikul =row['Артикул'],section ='75',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ukrat2'][key],material=materiale).save()
                              df_new['ukrat2_counter'][key]=materiale 
                              umumiy_counter[row['Артикул']+'-75'] = 1 
                               
            else:     
                  if AluminiyProduct.objects.filter(artikul =row['Артикул'],section ='7',kratkiy_tekst_materiala=df_new['ukrat1'][key]).exists():
                        df_new['ukrat1_counter'][key] = AluminiyProduct.objects.filter(artikul =row['Артикул'],section ='7',kratkiy_tekst_materiala=df_new['ukrat1'][key])[:1].get().material
                  else: 
                        if AluminiyProduct.objects.filter(artikul=row['Артикул'],section ='7').exists():
                              umumiy_counter[row['Артикул']+'-7'] += 1
                              max_values7 = umumiy_counter[row['Артикул']+'-7']
                              materiale = row['Артикул']+"-7{:03d}".format(max_values7)
                              AluminiyProduct(artikul = row['Артикул'],section ='7',counter=max_values7,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ukrat1'][key],material=materiale).save()
                              df_new['ukrat1_counter'][key] = materiale
                        else:
                              materiale = row['Артикул']+"-7{:03d}".format(1)
                              AluminiyProduct(artikul = row['Артикул'],section ='7',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ukrat1'][key],material=materiale).save()
                              df_new['ukrat1_counter'][key] = materiale
                              umumiy_counter[row['Артикул']+'-7'] = 1
                  
      b = datetime.datetime.now()
      print('ends in ...',b)
      print('difference =',b-a)  
      path =f'{MEDIA_ROOT}\\uploads\\alumin_new.xlsx'
      df_new.to_excel(path)
      return JsonResponse({'a':'s'})
                  
    