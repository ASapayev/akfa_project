from django.shortcuts import render,redirect
from django.http import JsonResponse
import pandas as pd
from .models import AluFileTermo,AluminiyProductTermo,AluminiyProductBasetermo,CharUtilsTwo,CharUtilsOne,CharUtilsThree,CharUtilsFour,CharacteristicTitle,BazaProfiley
from main.models import ExcelFiles
from aluminiy.models import AluFile,AluminiyProduct
from .forms import FileFormTermo
from django.db.models import Count,Max
from config.settings import MEDIA_ROOT
import numpy as np
from .utils import fabrikatsiya_sap_kod,create_folder,create_characteristika,create_characteristika_utils,characteristika_created_txt_create,anodirovaka_check,check_for_correct
import os
from datetime import datetime
import json
import random
from django.db.models import Q
from .BAZA import ANODIROVKA_CODE
from django.views.decorators.csrf import csrf_exempt
import ast

now = datetime.now()


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
      files = AluFileTermo.objects.filter(generated =False)
      context ={'files':files}
      return render(request,'termo/alu_file_list.html',context)

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

######termo old
def product_add(request,id):
      file = AluFileTermo.objects.get(id=id).file
      df = pd.read_excel(f'{MEDIA_ROOT}/{file}')
      df =df.astype(str)
      c =int(df.shape[0])-1
      
      for key,row in df.iterrows():
            if ((row['Артикул'] == 'nan') and (row['Компонент'] == 'nan')) :
                  df = df.drop(key)
      
      
      ################### group by termo #########
      aluminiy_group_termo = AluminiyProductTermo.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
      umumiy_counter_termo={}
      for al in aluminiy_group_termo:
            umumiy_counter_termo[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      ############################ end grouby ######
      
      
      # print(df)
      
      
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
      df_new['nkrat_counter']=''
      df_new['nkrat']=''
      df_new['kkrat1_counter']=''
      df_new['kkrat1']=''
      df_new['lkrat_counter']=''
      df_new['lkrat']=''
      df_new['ukrat1_counter']=''
      df_new['ukrat1']=''
      df_new['fkrat_counter']=''
      df_new['fkrat']=''
      df_new['ukrat2_counter']=''
      df_new['ukrat2']=''
      
      
      termo_artukul_first = False
      for key,row in df.iterrows():
            row['Сплав'] = row['Сплав'].replace('.0','')
            row['Сплав'] = row['Сплав'].replace('.0','')
            row['Длина (мм)'] = row['Длина (мм)'].replace('.0','')
            row['Бренд краски снаружи'] = row['Бренд краски снаружи'].replace('.0','')
            row['Код краски снаружи'] = row['Код краски снаружи'].replace('.0','')
            if row['Артикул'] !='nan':
                  if termo_artukul_first:
                        if row['Артикул'] != 'nan':
                              if df['Длина при выходе из пресса'][indexx] != 'nan':
                                    dlina = df['Длина при выходе из пресса'][indexx].replace('.0','')
                                          
                                    df_new['fkrat'][indexx]=fabrikatsiya_sap_kod(df['Краткий текст товара'][indexx],df['Длина (мм)'][indexx])
                                    df_new['ukrat2'][indexx]=fabrikatsiya_sap_kod(df['Краткий текст товара'][indexx],df['Длина (мм)'][indexx])
                                    
                                    if df['Тип покрытия'][indexx] != 'Ламинированный':
                                          df_new['kkrat1'][indexx] = fabrikatsiya_sap_kod(df['Краткий текст товара'][indexx],df['Длина при выходе из пресса'][indexx].replace('.0',''))
                                    else:
                                          df_new['kkrat1'][indexx] = fabrikatsiya_sap_kod(df['Краткий текст товара'][indexx].split('_')[0] +' NT1',df['Длина при выходе из пресса'][indexx].replace('.0',''))
                                    
                                    if df['Тип покрытия'][indexx] == 'Ламинированный':
                                          plenki1 = False
                                          plenki2 = False
                                          if df['Код лам пленки снаружи'][indexx] != 'nan':
                                                laminatsiya =row['Код лам пленки снаружи'].replace('.0','')+'/XXXX'
                                                plenki1 = True
                                                
                                          if df['Код лам пленки внутри'][indexx] != 'nan':
                                                laminatsiya ='XXXX/'+df['Код лам пленки внутри'][indexx].replace('.0','')
                                                plenki2 =True
                                                
                                          if plenki1 and plenki2:
                                                laminatsiya =df['Код лам пленки снаружи'][indexx].replace('.0','') +'/'+ df['Код лам пленки внутри'][indexx].replace('.0','')
                                                
                                          ll =row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')+'/'+df['Код краски внутри'][indexx].replace('.0','')+'_'+laminatsiya +' ' +row['Код наклейки']
                                          df_new['lkrat'][indexx] = fabrikatsiya_sap_kod(ll,df['Длина при выходе из пресса'][indexx].replace('.0',''))
                  
                              else:
                                    dlina = df['Длина (мм)'][indexx]
                                    df_new['ukrat1'][indexx] = df['Краткий текст товара'][indexx]
                                    
                                    if df['Тип покрытия'][indexx] != 'Ламинированный': 
                                          df_new['kkrat1'][indexx] = df['Краткий текст товара'][indexx]
                                    else: 
                                          df_new['kkrat1'][indexx] = df['Краткий текст товара'][indexx].split('_')[0] +' NT1'
                                    
                                    if df['Тип покрытия'][indexx] == 'Ламинированный':
                                          plenki1 = False
                                          plenki2 = False
                                          if row['Код лам пленки снаружи'] != 'nan':
                                                laminatsiya =row['Код лам пленки снаружи'].replace('.0','')+'/XXXX'
                                                plenki1 = True
                                                
                                          if df['Код лам пленки внутри'][indexx] != 'nan':
                                                laminatsiya ='XXXX/'+df['Код лам пленки внутри'][indexx].replace('.0','')
                                                plenki2 =True
                                                
                                          if plenki1 and plenki2:
                                                laminatsiya =df['Код лам пленки снаружи'][indexx].replace('.0','') +'/'+ df['Код лам пленки внутри'][indexx].replace('.0','')
                                                
                                          df_new['lkrat'][indexx] = df['Краткий текст товара'][indexx]
                                    
                              if df['Длина при выходе из пресса'][indexx] != 'nan':
                                    if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='F',kratkiy_tekst_materiala=df_new['fkrat'][indexx]).exists():
                                          df_new['fkrat_counter'][indexx] = AluminiyProductTermo.objects.filter(artikul = df['Артикул'][indexx],section ='F',kratkiy_tekst_materiala=df_new['fkrat'][indexx])[:1].get().material
                                    else: 
                                          if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='F').exists():
                                                umumiy_counter_termo[df['Артикул'][indexx]+'-F'] += 1
                                                max_valuesF = umumiy_counter_termo[df['Артикул'][indexx]+'-F']
                                                materiale = df['Артикул'][indexx] +"-F{:03d}".format(max_valuesF)
                                                AluminiyProductTermo(artikul =df['Артикул'][indexx],section ='F',counter=max_valuesF,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['fkrat'][indexx],material=materiale).save()
                                                df_new['fkrat_counter'][indexx]=materiale
                                          else:
                                                materiale = df['Артикул'][indexx] +"-F{:03d}".format(1)
                                                AluminiyProductTermo(artikul =df['Артикул'][indexx],section ='F',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['fkrat'][indexx],material=materiale).save()
                                                df_new['fkrat_counter'][indexx]=materiale
                                                umumiy_counter_termo[df['Артикул'][indexx]+'-F'] = 1
                                                
                                    
                                    
                                    if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='75',kratkiy_tekst_materiala=df_new['ukrat2'][indexx]).exists():
                                          df_new['ukrat2_counter'][indexx] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='75',kratkiy_tekst_materiala=df_new['ukrat2'][indexx])[:1].get().material
                                    else: 
                                          if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='75').exists():
                                                umumiy_counter_termo[df['Артикул'][indexx]+'-75'] += 1
                                                max_values75 = umumiy_counter_termo[df['Артикул'][indexx]+'-75']
                                                
                                                if max_values75 <= 99:
                                                      materiale = df['Артикул'][indexx]+"-75{:02d}".format(max_values75)
                                                else:
                                                      counter =7500 + max_values75
                                                      materiale = df['Артикул'][indexx]+"-{:04d}".format(counter)
                                                      
                                                      
                                                AluminiyProductTermo(artikul =df['Артикул'][indexx],section ='75',counter=max_values75,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ukrat2'][indexx],material=materiale).save()
                                                df_new['ukrat2_counter'][indexx] = materiale  
                                          else:
                                                materiale = df['Артикул'][indexx]+"-75{:02d}".format(1)
                                                AluminiyProductTermo(artikul = df['Артикул'][indexx],section ='75',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ukrat2'][indexx],material=materiale).save()
                                                df_new['ukrat2_counter'][indexx] = materiale 
                                                umumiy_counter_termo[df['Артикул'][indexx]+'-75'] = 1 
                                                
                              else:     
                                    if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='7',kratkiy_tekst_materiala=df_new['ukrat1'][indexx]).exists():
                                          df_new['ukrat1_counter'][indexx] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='7',kratkiy_tekst_materiala=df_new['ukrat1'][indexx])[:1].get().material
                                    else: 
                                          if AluminiyProductTermo.objects.filter(artikul=df['Артикул'][indexx],section ='7').exists():
                                                umumiy_counter_termo[df['Артикул'][indexx]+'-7'] += 1
                                                max_values7 = umumiy_counter_termo[df['Артикул'][indexx]+'-7']
                                                materiale = df['Артикул'][indexx]+"-7{:03d}".format(max_values7)
                                                AluminiyProductTermo(artikul = df['Артикул'][indexx],section ='7',counter=max_values7,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ukrat1'][indexx],material=materiale).save()
                                                df_new['ukrat1_counter'][indexx] = materiale
                                          else:
                                                materiale = df['Артикул'][indexx]+"-7{:03d}".format(1)
                                                AluminiyProductTermo(artikul = df['Артикул'][indexx],section ='7',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ukrat1'][indexx],material=materiale).save()
                                                df_new['ukrat1_counter'][indexx] = materiale
                                                umumiy_counter_termo[df['Артикул'][indexx]+'-7'] = 1
                                    ##### kombirinovanniy
                              if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='K',kratkiy_tekst_materiala=df_new['kkrat1'][indexx]).exists():
                                    df_new['kkrat1_counter'][indexx] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='K',kratkiy_tekst_materiala=df_new['kkrat1'][indexx])[:1].get().material
                              else: 
                                    if AluminiyProductTermo.objects.filter(artikul=df['Артикул'][indexx],section ='K').exists():
                                          umumiy_counter_termo[df['Артикул'][indexx]+'-K'] += 1
                                          max_valuesK = umumiy_counter_termo[df['Артикул'][indexx]+'-K']
                                          materiale = df['Артикул'][indexx]+"-K{:03d}".format(max_valuesK)
                                          AluminiyProductTermo(artikul = df['Артикул'][indexx],section ='K',counter=max_valuesK,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['kkrat1'][indexx],material=materiale).save()
                                          df_new['kkrat1_counter'][indexx] = materiale
                                    else:
                                          materiale = df['Артикул'][indexx]+"-K{:03d}".format(1)
                                          AluminiyProductTermo(artikul = df['Артикул'][indexx],section ='K',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['kkrat1'][indexx],material=materiale).save()
                                          df_new['kkrat1_counter'][indexx] = materiale
                                          umumiy_counter_termo[df['Артикул'][indexx]+'-K'] = 1
                              
                              if df['Тип покрытия'][indexx] == 'Ламинированный':      
                                    if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='L',kratkiy_tekst_materiala=df_new['lkrat'][indexx]).exists():
                                          df_new['lkrat_counter'][indexx] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='L',kratkiy_tekst_materiala=df_new['lkrat'][indexx])[:1].get().material
                                    else: 
                                          if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='L').exists():
                                                umumiy_counter_termo[df['Артикул'][indexx]+'-L'] += 1
                                                max_valuesL = umumiy_counter_termo[ df['Артикул'][indexx] +'-L']
                                                materiale = df['Артикул'][indexx]+"-L{:03d}".format(max_valuesL)
                                                AluminiyProductTermo(artikul =df['Артикул'][indexx],section ='L',counter=max_valuesL,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['lkrat'][indexx],material=materiale).save()
                                                df_new['lkrat_counter'][indexx]=materiale
                                          else:
                                                materiale = df['Артикул'][indexx]+"-L{:03d}".format(1)
                                                AluminiyProductTermo(artikul =df['Артикул'][indexx],section ='L',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['lkrat'][indexx],material=materiale).save()
                                                df_new['lkrat_counter'][indexx]=materiale
                                                umumiy_counter_termo[df['Артикул'][indexx]+'-L'] = 1
                                    
                                     
                        indexx = key
                  else:
                        indexx = key
                  termo_artukul_first = True 
                  continue
            
            df['Код декор пленки снаружи'][key] = df['Код декор пленки снаружи'][key].replace('.0','')
            
            component = row['Компонент']
    
            # print(component,AluminiyProductTermo.objects.filter(artikul =component,section ='E').values('section').annotate(total_max=Max('counter'))[0]['total_max'])
            dlina =''
            
            if df['Длина при выходе из пресса'][key] != 'nan':
                  dlina = df['Длина при выходе из пресса'][key].replace('.0','')      
            else:
                  dlina = df['Длина (мм)'][key]
                  
                  
            df_new['ekrat'][key] = row['Сплав'][len(row['Сплав'])-2:] +'T4 '+'L'+dlina+' MF'
            df_new['zkrat'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' MF'
            
            
                        
            if ((row['Тип покрытия'] == 'Окрашенный') or (row['Тип покрытия'] == 'Белый' )):
                  df_new['pkrat'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи']+row['Код краски снаружи']
                  if row['Код наклейки'] != 'NT1':
                        df_new['nkrat'][key] = df_new['pkrat'][key] +' '+ row['Код наклейки'].replace('.0','')
            
            
                        
            elif row['Тип покрытия'] == 'Ламинированный':
                  df_new['pkrat'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи']+row['Код краски снаружи']
                  
                 
            elif row['Тип покрытия'] =='Сублимированный':
                  df_new['pkrat'][key]=row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')
                  df_new['skrat'][key]=row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')+'_'+row['Код декор пленки снаружи'].replace('.0','')
                  
                  if row['Код наклейки'] != 'NT1':
                        df_new['nkrat'][key]=df_new['skrat'][key] + ' ' + row['Код наклейки'].replace('.0','')

            elif row['Тип покрытия'] =='Анодированный':
                  df_new['akrat'][key]=row['Сплав'][len(row['Сплав'])-2:] +row['тип закаленности']+' L'+dlina+' '+row['Код цвета анодировки снаружи'].replace('.0','')
                  if row['Код наклейки'] != 'NT1':
                        df_new['nkrat'][key]= df_new['akrat'][key] +' '+row['Контактность анодировки']+' ' + row['Код наклейки'].replace('.0','')
            else:
                  print("<<<<<< Нет Тип покрытия ! >>>>>>")
            
            if AluminiyProductTermo.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['ekrat'][key]).exists():
                  df_new['ekrat_counter'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['ekrat'][key])[:1].get().material
            else:
                  if AluminiyProductTermo.objects.filter(artikul =component,section ='E').exists():
                        # max_valuesE = AluminiyProductTermo.objects.filter(artikul =component,section ='E').values('section').annotate(total_max=Max('counter'))[0]['total_max']
                        umumiy_counter_termo[component+'-E'] += 1
                        max_valuesE = umumiy_counter_termo[component+'-E']
                        materiale = component+"-E{:03d}".format(max_valuesE)
                        AluminiyProductTermo(artikul =component,section ='E',counter=max_valuesE,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ekrat'][key],material=materiale).save()
                        df_new['ekrat_counter'][key]=materiale
                  else: 
                        materiale = component+"-E{:03d}".format(1)
                        AluminiyProductTermo(artikul =component,section ='E',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ekrat'][key],material=materiale).save()
                        df_new['ekrat_counter'][key]=materiale
                        umumiy_counter_termo[component+'-E'] = 1
                        
            if AluminiyProductTermo.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['zkrat'][key]).exists():
                  df_new['zkrat_counter'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['zkrat'][key])[:1].get().material
            else: 
                  if AluminiyProductTermo.objects.filter(artikul =component,section ='Z').exists():
                        umumiy_counter_termo[ component +'-Z'] += 1
                        max_valuesZ = umumiy_counter_termo[ component +'-Z']
                        materiale = component+"-Z{:03d}".format(max_valuesZ)
                        AluminiyProductTermo(artikul =component,section ='Z',counter=max_valuesZ,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['zkrat'][key],material=materiale).save()
                        df_new['zkrat_counter'][key]=materiale
                  else:
                        materiale = component+"-Z{:03d}".format(1)
                        AluminiyProductTermo(artikul =component,section ='Z',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['zkrat'][key],material=materiale).save()
                        df_new['zkrat_counter'][key]=materiale
                        umumiy_counter_termo[ component +'-Z'] = 1
                        
            
            
            if ((row['Тип покрытия'] == 'Сублимированный') or (row['Тип покрытия'] == 'Ламинированный') or (row['Тип покрытия'] == 'Окрашенный') or (row['Тип покрытия'] == 'Белый')): 
                  if AluminiyProductTermo.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['pkrat'][key]).exists():
                        df_new['pkrat_counter'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['pkrat'][key])[:1].get().material
                  else: 
                        if AluminiyProductTermo.objects.filter(artikul =component,section ='P').exists():
                              umumiy_counter_termo[component+'-P'] += 1
                              
                              max_valuesP = umumiy_counter_termo[ component +'-P']
                              materiale = component+"-P{:03d}".format(max_valuesP)
                              AluminiyProductTermo(artikul =component,section ='P',counter=max_valuesP,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['pkrat'][key],material=materiale).save()
                              df_new['pkrat_counter'][key]=materiale
                        else:
                              materiale = component+"-P{:03d}".format(1)
                              AluminiyProductTermo(artikul =component,section ='P',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['pkrat'][key],material=materiale).save()
                              df_new['pkrat_counter'][key] = materiale
                              umumiy_counter_termo[component+'-P'] = 1
            
            if row['Тип покрытия'] =='Сублимированный':       
                  if AluminiyProductTermo.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['skrat'][key]).exists():
                        df_new['skrat_counter'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['skrat'][key])[:1].get().material
                  else: 
                        if AluminiyProductTermo.objects.filter(artikul =component,section ='S').exists():
                              umumiy_counter_termo[component+'-S'] += 1
                              max_valuesS = umumiy_counter_termo[ component +'-S']
                              materiale = component+"-S{:03d}".format(max_valuesS)
                              AluminiyProductTermo(artikul =component,section ='S',counter=max_valuesS,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['skrat'][key],material=materiale).save()
                              df_new['skrat_counter'][key]=materiale
                        else:
                              materiale = component+"-S{:03d}".format(1)
                              AluminiyProductTermo(artikul =component,section ='S',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['skrat'][key],material=materiale).save()
                              df_new['skrat_counter'][key]=materiale
                              umumiy_counter_termo[component+'-S'] = 1
            
            if row['Тип покрытия'] =='Анодированный':    
                  if AluminiyProductTermo.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['akrat'][key]).exists():
                        df_new['akrat_counter'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['akrat'][key])[:1].get().material
                  else: 
                        if AluminiyProductTermo.objects.filter(artikul =component,section ='A').exists():
                              umumiy_counter_termo[component+'-A'] += 1
                              max_valuesA = umumiy_counter_termo[ component +'-A']
                              materiale = component+"-A{:03d}".format(max_valuesA)
                              AluminiyProductTermo(artikul =component,section ='A',counter=max_valuesA,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['akrat'][key],material=materiale).save()
                              df_new['akrat_counter'][key]=materiale
                        else:
                              materiale = component+"-A{:03d}".format(1)
                              AluminiyProductTermo(artikul =component,section ='A',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['akrat'][key],material=materiale).save()
                              df_new['akrat_counter'][key]=materiale
                              umumiy_counter_termo[component+'-A'] = 1
                              
            
            
                        
            if ((row['Код наклейки'] != 'NT1') and (row['Тип покрытия'] != 'Ламинированный')) :    
                  if AluminiyProductTermo.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['nkrat'][key]).exists():
                        df_new['nkrat_counter'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['nkrat'][key])[:1].get().material
                  else:
                        if  AluminiyProductTermo.objects.filter(artikul =component,section ='N').exists():
                              umumiy_counter_termo[component+'-N'] += 1
                              max_valuesN = umumiy_counter_termo[ component +'-N']
                              materiale = component+"-N{:03d}".format(max_valuesN)
                              AluminiyProductTermo(artikul =component,section ='N',counter=max_valuesN,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['nkrat'][key],material=materiale).save()
                              df_new['nkrat_counter'][key]=materiale
                        else:
                              materiale = component+"-N{:03d}".format(1)
                              AluminiyProductTermo(artikul =component,section ='N',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['nkrat'][key],material=materiale).save()
                              df_new['nkrat_counter'][key]=materiale
                              umumiy_counter_termo[component+'-N'] = 1
            
            # print(f'key = {key}  shape = {c} indexx= {indexx}')
            if key == c:               
                  if df['Длина при выходе из пресса'][indexx] != 'nan':
                        dlina = df['Длина при выходе из пресса'][indexx].replace('.0','')
                              
                        df_new['fkrat'][indexx]=fabrikatsiya_sap_kod(df['Краткий текст товара'][indexx],df['Длина (мм)'][indexx])
                        df_new['ukrat2'][indexx]=fabrikatsiya_sap_kod(df['Краткий текст товара'][indexx],df['Длина (мм)'][indexx])
                        
                        if df['Тип покрытия'][indexx] != 'Ламинированный':
                              df_new['kkrat1'][indexx] = fabrikatsiya_sap_kod(df['Краткий текст товара'][indexx],df['Длина при выходе из пресса'][indexx].replace('.0',''))
                        else:
                              df_new['kkrat1'][indexx] = fabrikatsiya_sap_kod(df['Краткий текст товара'][indexx].split('_')[0] +' NT1',df['Длина при выходе из пресса'][indexx].replace('.0',''))
                        
                        if df['Тип покрытия'][indexx] == 'Ламинированный':
                              plenki1 = False
                              plenki2 = False
                              if df['Код лам пленки снаружи'][indexx] != 'nan':
                                    laminatsiya =row['Код лам пленки снаружи'].replace('.0','')+'/XXXX'
                                    plenki1 = True
                                    
                              if df['Код лам пленки внутри'][indexx] != 'nan':
                                    laminatsiya ='XXXX/'+df['Код лам пленки внутри'][indexx].replace('.0','')
                                    plenki2 =True
                                    
                              if plenki1 and plenki2:
                                    laminatsiya =row['Код лам пленки снаружи'].replace('.0','') +'/'+ df['Код лам пленки внутри'][indexx].replace('.0','')
                              
                              ll =row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')+'/'+df['Код краски внутри'][indexx].replace('.0','')+'_'+laminatsiya +' ' +row['Код наклейки']
                              df_new['lkrat'][indexx] = fabrikatsiya_sap_kod(ll,df['Длина при выходе из пресса'][indexx].replace('.0',''))
      
                  else:
                        dlina = df['Длина (мм)'][indexx]
                        df_new['ukrat1'][indexx] = df['Краткий текст товара'][indexx]
                        
                        if df['Тип покрытия'][indexx] != 'Ламинированный':
                              df_new['kkrat1'][indexx] = df['Краткий текст товара'][indexx]
                        else:
                              df_new['kkrat1'][indexx] = df['Краткий текст товара'][indexx].split('_')[0] +' NT1'
                        
                        if df['Тип покрытия'][indexx] == 'Ламинированный':
                              plenki1 = False
                              plenki2 = False
                              if row['Код лам пленки снаружи'] != 'nan':
                                    laminatsiya =row['Код лам пленки снаружи'].replace('.0','')+'/XXXX'
                                    plenki1 = True
                                    
                              if df['Код лам пленки внутри'][indexx] != 'nan':
                                    laminatsiya ='XXXX/'+df['Код лам пленки внутри'][indexx].replace('.0','')
                                    plenki2 =True
                                    
                              if plenki1 and plenki2:
                                    laminatsiya =row['Код лам пленки снаружи'].replace('.0','') +'/'+ df['Код лам пленки внутри'][indexx].replace('.0','')
                                    
                              df_new['lkrat'][indexx] = df['Краткий текст товара'][indexx]
                        
                  if df['Длина при выходе из пресса'][indexx] != 'nan':
                        if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='F',kratkiy_tekst_materiala=df_new['fkrat'][indexx]).exists():
                              df_new['fkrat_counter'][indexx] = AluminiyProductTermo.objects.filter(artikul = df['Артикул'][indexx],section ='F',kratkiy_tekst_materiala=df_new['fkrat'][indexx])[:1].get().material
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='F').exists():
                                    umumiy_counter_termo[df['Артикул'][indexx]+'-F'] += 1
                                    max_valuesF = umumiy_counter_termo[df['Артикул'][indexx]+'-F']
                                    materiale = df['Артикул'][indexx] +"-F{:03d}".format(max_valuesF)
                                    AluminiyProductTermo(artikul =df['Артикул'][indexx],section ='F',counter=max_valuesF,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['fkrat'][indexx],material=materiale).save()
                                    df_new['fkrat_counter'][indexx]=materiale
                              else:
                                    materiale = df['Артикул'][indexx] +"-F{:03d}".format(1)
                                    AluminiyProductTermo(artikul =df['Артикул'][indexx],section ='F',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['fkrat'][indexx],material=materiale).save()
                                    df_new['fkrat_counter'][indexx]=materiale
                                    umumiy_counter_termo[df['Артикул'][indexx]+'-F'] = 1
                                    
                        
                        
                        if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='75',kratkiy_tekst_materiala=df_new['ukrat2'][indexx]).exists():
                              df_new['ukrat2_counter'][indexx] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='75',kratkiy_tekst_materiala=df_new['ukrat2'][indexx])[:1].get().material
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='75').exists():
                                    umumiy_counter_termo[df['Артикул'][indexx]+'-75'] += 1
                                    max_values75 = umumiy_counter_termo[df['Артикул'][indexx]+'-75']
                                    
                                    if max_values75 <= 99:
                                          materiale = df['Артикул'][indexx]+"-75{:02d}".format(max_values75)
                                    else:
                                          counter =7500 + max_values75
                                          materiale = df['Артикул'][indexx]+"-{:04d}".format(counter)
                                          
                                          
                                    AluminiyProductTermo(artikul =df['Артикул'][indexx],section ='75',counter=max_values75,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ukrat2'][indexx],material=materiale).save()
                                    df_new['ukrat2_counter'][indexx] = materiale  
                              else:
                                    materiale = df['Артикул'][indexx]+"-75{:02d}".format(1)
                                    AluminiyProductTermo(artikul = df['Артикул'][indexx],section ='75',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ukrat2'][indexx],material=materiale).save()
                                    df_new['ukrat2_counter'][indexx] = materiale 
                                    umumiy_counter_termo[df['Артикул'][indexx]+'-75'] = 1 
                        if df['Тип покрытия'][indexx] == 'Ламинированный':     
                              if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='L',kratkiy_tekst_materiala=df_new['lkrat'][indexx]).exists():
                                    df_new['lkrat_counter'][indexx] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='L',kratkiy_tekst_materiala=df_new['lkrat'][indexx])[:1].get().material
                              else: 
                                    if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='L').exists():
                                          umumiy_counter_termo[df['Артикул'][indexx]+'-L'] += 1
                                          max_valuesL = umumiy_counter_termo[ df['Артикул'][indexx] +'-L']
                                          materiale = df['Артикул'][indexx]+"-L{:03d}".format(max_valuesL)
                                          AluminiyProductTermo(artikul =df['Артикул'][indexx],section ='L',counter=max_valuesL,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['lkrat'][indexx],material=materiale).save()
                                          df_new['lkrat_counter'][indexx]=materiale
                                    else:
                                          materiale = df['Артикул'][indexx]+"-L{:03d}".format(1)
                                          AluminiyProductTermo(artikul =df['Артикул'][indexx],section ='L',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['lkrat'][indexx],material=materiale).save()
                                          df_new['lkrat_counter'][indexx]=materiale
                                          umumiy_counter_termo[df['Артикул'][indexx]+'-L'] = 1
                              
                                    
                                    
                  else:     
                        if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='7',kratkiy_tekst_materiala=df_new['ukrat1'][indexx]).exists():
                              df_new['ukrat1_counter'][indexx] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='7',kratkiy_tekst_materiala=df_new['ukrat1'][indexx])[:1].get().material
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul=df['Артикул'][indexx],section ='7').exists():
                                    umumiy_counter_termo[df['Артикул'][indexx]+'-7'] += 1
                                    max_values7 = umumiy_counter_termo[df['Артикул'][indexx]+'-7']
                                    materiale = df['Артикул'][indexx]+"-7{:03d}".format(max_values7)
                                    AluminiyProductTermo(artikul = df['Артикул'][indexx],section ='7',counter=max_values7,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ukrat1'][indexx],material=materiale).save()
                                    df_new['ukrat1_counter'][indexx] = materiale
                              else:
                                    materiale = df['Артикул'][indexx]+"-7{:03d}".format(1)
                                    AluminiyProductTermo(artikul = df['Артикул'][indexx],section ='7',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ukrat1'][indexx],material=materiale).save()
                                    df_new['ukrat1_counter'][indexx] = materiale
                                    umumiy_counter_termo[df['Артикул'][indexx]+'-7'] = 1
                        ##### kombirinovanniy
                  if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='K',kratkiy_tekst_materiala=df_new['kkrat1'][indexx]).exists():
                        df_new['kkrat1_counter'][indexx] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='K',kratkiy_tekst_materiala=df_new['kkrat1'][indexx])[:1].get().material
                  else: 
                        if AluminiyProductTermo.objects.filter(artikul=df['Артикул'][indexx],section ='K').exists():
                              umumiy_counter_termo[df['Артикул'][indexx]+'-K'] += 1
                              max_valuesK = umumiy_counter_termo[df['Артикул'][indexx]+'-K']
                              materiale = df['Артикул'][indexx]+"-K{:03d}".format(max_valuesK)
                              AluminiyProductTermo(artikul = df['Артикул'][indexx],section ='K',counter=max_valuesK,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['kkrat1'][indexx],material=materiale).save()
                              df_new['kkrat1_counter'][indexx] = materiale
                        else:
                              materiale = df['Артикул'][indexx]+"-K{:03d}".format(1)
                              AluminiyProductTermo(artikul = df['Артикул'][indexx],section ='K',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['kkrat1'][indexx],material=materiale).save()
                              df_new['kkrat1_counter'][indexx] = materiale
                              umumiy_counter_termo[df['Артикул'][indexx]+'-K'] = 1
                  
                  if df['Тип покрытия'][indexx] == 'Ламинированный':   
                        if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='L',kratkiy_tekst_materiala=df_new['lkrat'][indexx]).exists():
                              df_new['lkrat_counter'][indexx] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='L',kratkiy_tekst_materiala=df_new['lkrat'][indexx])[:1].get().material
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][indexx],section ='L').exists():
                                    umumiy_counter_termo[df['Артикул'][indexx]+'-L'] += 1
                                    max_valuesL = umumiy_counter_termo[ df['Артикул'][indexx] +'-L']
                                    materiale = df['Артикул'][indexx]+"-L{:03d}".format(max_valuesL)
                                    AluminiyProductTermo(artikul =df['Артикул'][indexx],section ='L',counter=max_valuesL,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['lkrat'][indexx],material=materiale).save()
                                    df_new['lkrat_counter'][indexx]=materiale
                              else:
                                    materiale = df['Артикул'][indexx]+"-L{:03d}".format(1)
                                    AluminiyProductTermo(artikul =df['Артикул'][indexx],section ='L',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['lkrat'][indexx],material=materiale).save()
                                    df_new['lkrat_counter'][indexx]=materiale
                                    umumiy_counter_termo[df['Артикул'][indexx]+'-L'] = 1
                                                    
                                   
      # del df_new["artikul"]
      
      s2 = now.strftime("%d-%m-%Y__%H-%M-%S")
      parent_dir ='{MEDIA_ROOT}\\uploads\\aluminiytermo\\'
       
      if not os.path.isdir(parent_dir):
            create_folder(f'{MEDIA_ROOT}\\uploads\\','aluminiytermo')
            
      if not os.path.isfile(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\alumin_new-{s2}.xlsx'):
            path =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\alumin_new-{s2}.xlsx'
      else:
            st =random.randint(0,1000)
            path =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\alumin_new-{s2}{st}.xlsx'
          
      df_new.to_excel(path,index = False)
      return JsonResponse({'a':'s'})
                  
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
      'nan':''  
}

### new
def product_add_second(request,id):
      file = AluFileTermo.objects.get(id=id).file
      df = pd.read_excel(f'{MEDIA_ROOT}/{file}')
      df =df.astype(str)
      
      doesnotexist,correct = check_for_correct(df)
      if not correct:
            context ={
                  'CharUtilsOne':doesnotexist[0],
                  'CharUtilsTwo':doesnotexist[1],
                  'BazaProfile':doesnotexist[2]
            }
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
      
      
      # print(df)
      df_new =pd.DataFrame()
      df_new['Название системы']=df['Название системы']
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
      df_new['nkrat_counter']=''
      df_new['nkrat']=''
      df_new['kkrat1_counter']=''
      df_new['kkrat1']=''
      df_new['lkrat_counter']=''
      df_new['lkrat']=''
      df_new['ukrat1_counter']=''
      df_new['ukrat1']=''
      df_new['fkrat_counter']=''
      df_new['fkrat']=''
      df_new['ukrat2_counter']=''
      df_new['ukrat2']=''
      
      
      
      cache_for_cratkiy_text =[]
      
      for key,row in df.iterrows():
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
            row['Код лам пленки внутри'] = row['Код лам пленки снаружи'].replace('.0','')
            
            artikul = df['Артикул'][key]
            component = df['Компонент'][key]
            
            if artikul !='nan':
                  print('artikulllllllll')
                  if df['Длина при выходе из пресса'][key] != 'nan':
                        dlina = df['Длина при выходе из пресса'][key].replace('.0','')
                              
                        df_new['fkrat'][key]=fabrikatsiya_sap_kod(df['Краткий текст товара'][key],df['Длина (мм)'][key])
                        df_new['ukrat2'][key]=fabrikatsiya_sap_kod(df['Краткий текст товара'][key],df['Длина (мм)'][key])
                        
                        if df['Тип покрытия'][key] != 'Ламинированный':
                              df_new['kkrat1'][key] = fabrikatsiya_sap_kod(df['Краткий текст товара'][key],df['Длина при выходе из пресса'][key].replace('.0',''))
                        else:
                              df_new['kkrat1'][key] = fabrikatsiya_sap_kod(df['Краткий текст товара'][key].split('_')[0] +' NT1',df['Длина при выходе из пресса'][key].replace('.0',''))
                        
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
                              df_new['lkrat'][key] = fabrikatsiya_sap_kod(ll,df['Длина при выходе из пресса'][key].replace('.0',''))

                  else:
                        dlina = df['Длина (мм)'][key]
                        df_new['ukrat1'][key] = df['Краткий текст товара'][key]
                        
                        if df['Тип покрытия'][key] != 'Ламинированный': 
                              df_new['kkrat1'][key] = df['Краткий текст товара'][key]
                        else: 
                              df_new['kkrat1'][key] = df['Краткий текст товара'][key].split('_')[0] +' NT1'
                        
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
                                    
                              df_new['lkrat'][key] = df['Краткий текст товара'][key]
                        
                  if df['Длина при выходе из пресса'][key] != 'nan':
                        if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='F',kratkiy_tekst_materiala=df_new['fkrat'][key]).exists():
                              df_new['fkrat_counter'][key] = AluminiyProductTermo.objects.filter(artikul = df['Артикул'][key],section ='F',kratkiy_tekst_materiala=df_new['fkrat'][key])[:1].get().material
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='F').exists():
                                    umumiy_counter_termo[df['Артикул'][key]+'-F'] += 1
                                    max_valuesF = umumiy_counter_termo[df['Артикул'][key]+'-F']
                                    materiale = df['Артикул'][key] +"-F{:03d}".format(max_valuesF)
                                    AluminiyProductTermo(artikul =df['Артикул'][key],section ='F',counter=max_valuesF,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['fkrat'][key],material=materiale).save()
                                    df_new['fkrat_counter'][key]=materiale
                                    artikle = materiale.split('-')[0]
                              
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['fkrat'][key],
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
                                                      'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                                    AluminiyProductTermo(artikul =df['Артикул'][key],section ='F',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['fkrat'][key],material=materiale).save()
                                    df_new['fkrat_counter'][key]=materiale
                                    umumiy_counter_termo[df['Артикул'][key]+'-F'] = 1
                                    artikle = materiale.split('-')[0]
                              
                                    
                                    if row['Тип покрытия'].lower() == 'сублимированный':
                                          tip_poktitiya ='с декоративным покрытием'
                                    else:
                                          tip_poktitiya = row['Тип покрытия'].lower()
                                    
                                    
                                    width_and_height = CharUtilsOne.objects.filter(Q(матрица = artikle) | Q(артикул = artikle))[:1].get()
                                    
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['fkrat'][key],
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
                                                      'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                                    
                                    
                        
                        
                        if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='75',kratkiy_tekst_materiala=df_new['ukrat2'][key]).exists():
                              df_new['ukrat2_counter'][key] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='75',kratkiy_tekst_materiala=df_new['ukrat2'][key])[:1].get().material
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='75').exists():
                                    umumiy_counter_termo[df['Артикул'][key]+'-75'] += 1
                                    max_values75 = umumiy_counter_termo[df['Артикул'][key]+'-75']
                                    
                                    if max_values75 <= 99:
                                          materiale = df['Артикул'][key]+"-75{:02d}".format(max_values75)
                                    else:
                                          counter =7500 + max_values75
                                          materiale = df['Артикул'][key]+"-{:04d}".format(counter)
                                          
                                          
                                    AluminiyProductTermo(artikul =df['Артикул'][key],section ='75',counter=max_values75,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ukrat2'][key],material=materiale).save()
                                    df_new['ukrat2_counter'][key] = materiale
                                    
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
                                          surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']]
                                    elif row['Тип покрытия'].lower() =='сублимированный':
                                          surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                                    elif row['Тип покрытия'].lower() =='анодированный':
                                          surface_treatment_export = row['Код цвета анодировки снаружи']
                                    elif row['Тип покрытия'].lower() =='ламинированный':
                                          surface_treatment_export = row['Цвет лам пленки снаружи']
                                          
                                          
                                    
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['ukrat2'][key],
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
                                                      'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                                    AluminiyProductTermo(artikul = df['Артикул'][key],section ='75',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ukrat2'][key],material=materiale).save()
                                    df_new['ukrat2_counter'][key] = materiale 
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
                                          surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']]
                                    elif row['Тип покрытия'].lower() =='сублимированный':
                                          surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                                    elif row['Тип покрытия'].lower() =='анодированный':
                                          surface_treatment_export = row['Код цвета анодировки снаружи']
                                    elif row['Тип покрытия'].lower() =='ламинированный':
                                          surface_treatment_export = row['Цвет лам пленки снаружи']
                                          
                                          
                                    
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['ukrat2'][key],
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
                                                      'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                        if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['ukrat1'][key]).exists():
                              df_new['ukrat1_counter'][key] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['ukrat1'][key])[:1].get().material
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul=df['Артикул'][key],section ='7').exists():
                                    umumiy_counter_termo[df['Артикул'][key]+'-7'] += 1
                                    max_values7 = umumiy_counter_termo[df['Артикул'][key]+'-7']
                                    materiale = df['Артикул'][key]+"-7{:03d}".format(max_values7)
                                    AluminiyProductTermo(artikul = df['Артикул'][key],section ='7',counter=max_values7,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ukrat1'][key],material=materiale).save()
                                    df_new['ukrat1_counter'][key] = materiale
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
                                          surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']]
                                    elif row['Тип покрытия'].lower() =='сублимированный':
                                          surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                                    elif row['Тип покрытия'].lower() =='анодированный':
                                          surface_treatment_export = row['Код цвета анодировки снаружи']
                                    elif row['Тип покрытия'].lower() =='ламинированный':
                                          surface_treatment_export = row['Цвет лам пленки снаружи']
                                          
                                          
                                    print(f"Ukrat1 tip pokr {row['Тип покрытия']}")
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['ukrat1'][key],
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
                                                      'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                                    AluminiyProductTermo(artikul = df['Артикул'][key],section ='7',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ukrat1'][key],material=materiale).save()
                                    df_new['ukrat1_counter'][key] = materiale
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
                                          surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']]
                                    elif row['Тип покрытия'].lower() =='сублимированный':
                                          surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                                    elif row['Тип покрытия'].lower() =='анодированный':
                                          surface_treatment_export = row['Код цвета анодировки снаружи']
                                    elif row['Тип покрытия'].lower() =='ламинированный':
                                          surface_treatment_export = row['Цвет лам пленки снаружи']
                                          
                                          
                                    print(f"Ukrat1 tip pokr {row['Тип покрытия']}")
                                          
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['ukrat1'][key],
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
                                                      'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                  
                  if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='K',kratkiy_tekst_materiala=df_new['kkrat1'][key]).exists():
                        df_new['kkrat1_counter'][key] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='K',kratkiy_tekst_materiala=df_new['kkrat1'][key])[:1].get().material
                  else: 
                        
                        name_tip_pokr =''
                        if (('7777' in df_new['kkrat1'][key]) or ('8888' in df_new['kkrat1'][key])  or ('3701' in df_new['kkrat1'][key]) or ('3702' in df_new['kkrat1'][key])):
                              name_tip_pokr = 'Сублимированный'
                        elif '9016' in df_new['kkrat1'][key]:
                              name_tip_pokr = 'Белый'
                        elif 'MF' in df_new['kkrat1'][key]:
                              name_tip_pokr = 'Неокрашенный'
                        elif anodirovaka_check(ANODIROVKA_CODE,df_new['kkrat1'][key]):
                              name_tip_pokr = 'Анодированный'
                        else:
                              name_tip_pokr = 'Окрашенный'
                              
                        if AluminiyProductTermo.objects.filter(artikul=df['Артикул'][key],section ='K').exists():
                              umumiy_counter_termo[df['Артикул'][key]+'-K'] += 1
                              max_valuesK = umumiy_counter_termo[df['Артикул'][key]+'-K']
                              materiale = df['Артикул'][key]+"-K{:03d}".format(max_valuesK)
                              AluminiyProductTermo(artikul = df['Артикул'][key],section ='K',counter=max_valuesK,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['kkrat1'][key],material=materiale).save()
                              df_new['kkrat1_counter'][key] = materiale
                              
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
                              
                              print(f"kkrat1 tip pokr {row['Тип покрытия']}") 
                              
                              
                                    
                                    
                                  
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['kkrat1'][key],
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
                                                'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                              AluminiyProductTermo(artikul = df['Артикул'][key],section ='K',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['kkrat1'][key],material=materiale).save()
                              df_new['kkrat1_counter'][key] = materiale
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
                              
                              print(f"kkrat1 tip pokr {row['Тип покрытия']}")
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['kkrat1'][key],
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
                                                'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                        if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='L',kratkiy_tekst_materiala=df_new['lkrat'][key]).exists():
                              df_new['lkrat_counter'][key] = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='L',kratkiy_tekst_materiala=df_new['lkrat'][key])[:1].get().material
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='L').exists():
                                    umumiy_counter_termo[df['Артикул'][key]+'-L'] += 1
                                    max_valuesL = umumiy_counter_termo[ df['Артикул'][key] +'-L']
                                    materiale = df['Артикул'][key]+"-L{:03d}".format(max_valuesL)
                                    AluminiyProductTermo(artikul =df['Артикул'][key],section ='L',counter=max_valuesL,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['lkrat'][key],material=materiale).save()
                                    df_new['lkrat_counter'][key]=materiale
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
                                    
                                    print(f"lkrat1 tip pokr {row['Тип покрытия']}")   
                                    cache_for_cratkiy_text.append(
                                                      {'material':materiale,
                                                      'kratkiy':df_new['lkrat'][key],
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
                                                      'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                                    AluminiyProductTermo(artikul =df['Артикул'][key],section ='L',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['lkrat'][key],material=materiale).save()
                                    df_new['lkrat_counter'][key]=materiale
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
                                                      'kratkiy':df_new['lkrat'][key],
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
                                                      'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                        
                        
                  df_new['ekrat'][key] = row['Сплав'][len(row['Сплав'])-2:] +'T4 '+'L'+dlina+' MF'
                  df_new['zkrat'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' MF'
                  
                  
                              
                  if ((row['Тип покрытия'] == 'Окрашенный') or (row['Тип покрытия'] == 'Белый' )):
                        df_new['pkrat'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи']+row['Код краски снаружи']
                        if row['Код наклейки'] != 'NT1':
                              df_new['nkrat'][key] = df_new['pkrat'][key] +' '+ row['Код наклейки'].replace('.0','')
                  
                  
                              
                  elif row['Тип покрытия'] == 'Ламинированный':
                        df_new['pkrat'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи']+row['Код краски снаружи']
                        
                  
                  elif row['Тип покрытия'] =='Сублимированный':
                        df_new['pkrat'][key]=row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')
                        df_new['skrat'][key]=row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')+'_'+row['Код декор пленки снаружи'].replace('.0','')
                        
                        if row['Код наклейки'] != 'NT1':
                              df_new['nkrat'][key]=df_new['skrat'][key] + ' ' + row['Код наклейки'].replace('.0','')

                  elif row['Тип покрытия'] =='Анодированный':
                        df_new['akrat'][key]=row['Сплав'][len(row['Сплав'])-2:] +row['тип закаленности']+' L'+dlina+' '+row['Код цвета анодировки снаружи'].replace('.0','')
                        if row['Код наклейки'] != 'NT1':
                              df_new['nkrat'][key]= df_new['akrat'][key] +' '+row['Контактность анодировки']+' ' + row['Код наклейки'].replace('.0','')
                  else:
                        print("<<<<<< Нет Тип покрытия ! >>>>>>")
                  
                  termo_existE = AluminiyProductTermo.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['ekrat'][key]).exists()
                  simple_existE = AluminiyProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['ekrat'][key]).exists()
                  # print('existsance = ',termo_existE,simple_existE)
                  if (termo_existE or simple_existE):
                        if termo_existE:
                              df_new['ekrat_counter'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['ekrat'][key])[:1].get().material
                        else:
                              
                              df_new['ekrat_counter'][key] = AluminiyProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['ekrat'][key])[:1].get().material
                  else:
                        if AluminiyProductTermo.objects.filter(artikul =component,section ='E').exists():
                              # max_valuesE = AluminiyProductTermo.objects.filter(artikul =component,section ='E').values('section').annotate(total_max=Max('counter'))[0]['total_max']
                              umumiy_counter_termo[component+'-E'] += 1
                              max_valuesE = umumiy_counter_termo[component+'-E']
                              materiale = component+"-E{:03d}".format(max_valuesE)
                              AluminiyProductTermo(artikul =component,section ='E',counter=max_valuesE,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ekrat'][key],material=materiale).save()
                              df_new['ekrat_counter'][key]=materiale
                              
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
                                                'kratkiy':df_new['ekrat'][key],
                                                'section':'E-Экструзия холодная резка ZPP2',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':'Неокрашенный',
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                              materiale = component+"-E{:03d}".format(1)
                              AluminiyProductTermo(artikul =component,section ='E',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['ekrat'][key],material=materiale).save()
                              df_new['ekrat_counter'][key]=materiale
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
                                                'kratkiy':df_new['ekrat'][key],
                                                'section':'E-Экструзия холодная резка ZPP2',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':'Неокрашенный',
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                              
                  termo_existZ =AluminiyProductTermo.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['zkrat'][key]).exists()
                  simple_existZ =AluminiyProduct.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['zkrat'][key]).exists()
                  if (termo_existZ or simple_existZ):
                        if termo_existZ:
                              df_new['zkrat_counter'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['zkrat'][key])[:1].get().material
                        else:
                              df_new['zkrat_counter'][key] = AluminiyProduct.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['zkrat'][key])[:1].get().material
                  else: 
                        if AluminiyProductTermo.objects.filter(artikul =component,section ='Z').exists():
                              umumiy_counter_termo[ component +'-Z'] += 1
                              max_valuesZ = umumiy_counter_termo[ component +'-Z']
                              materiale = component+"-Z{:03d}".format(max_valuesZ)
                              AluminiyProductTermo(artikul =component,section ='Z',counter=max_valuesZ,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['zkrat'][key],material=materiale).save()
                              df_new['zkrat_counter'][key]=materiale
                              
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
                                                'kratkiy':df_new['zkrat'][key],
                                                'section':'Z-Печь старения',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':'Неокрашенный',
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                              materiale = component+"-Z{:03d}".format(1)
                              AluminiyProductTermo(artikul =component,section ='Z',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['zkrat'][key],material=materiale).save()
                              df_new['zkrat_counter'][key]=materiale
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
                                                'kratkiy':df_new['zkrat'][key],
                                                'section':'Z-Печь старения',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':'Неокрашенный',
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                              
                              
                  
                  
                              
                  if ((row['Тип покрытия'] == 'Сублимированный') or (row['Тип покрытия'] == 'Ламинированный') or (row['Тип покрытия'] == 'Окрашенный') or (row['Тип покрытия'] == 'Белый')): 
                        termo_existP =AluminiyProductTermo.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['pkrat'][key]).exists()
                        simple_existP =AluminiyProduct.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['pkrat'][key]).exists()
                        if (termo_existP or simple_existP):
                              if termo_existP:
                                    df_new['pkrat_counter'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['pkrat'][key])[:1].get().material
                              else:
                                    df_new['pkrat_counter'][key] = AluminiyProduct.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['pkrat'][key])[:1].get().material
                        else: 
                              if '9016' in df_new['pkrat'][key]:
                                    tip_pokr ='Белый'
                              else:
                                    tip_pokr ='Окрашенный'
                              if AluminiyProductTermo.objects.filter(artikul =component,section ='P').exists():
                                    umumiy_counter_termo[component+'-P'] += 1
                                    
                                    max_valuesP = umumiy_counter_termo[ component +'-P']
                                    materiale = component+"-P{:03d}".format(max_valuesP)
                                    AluminiyProductTermo(artikul =component,section ='P',counter=max_valuesP,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['pkrat'][key],material=materiale).save()
                                    df_new['pkrat_counter'][key]=materiale
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
                                                      'kratkiy':df_new['pkrat'][key],
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
                                                      'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                                    AluminiyProductTermo(artikul =component,section ='P',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['pkrat'][key],material=materiale).save()
                                    df_new['pkrat_counter'][key] = materiale
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
                                                      'kratkiy':df_new['pkrat'][key],
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
                                                      'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                        
                        termo_existS =AluminiyProductTermo.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['skrat'][key]).exists()
                        simple_existS =AluminiyProduct.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['skrat'][key]).exists()
                        if (termo_existS or simple_existS):
                              if termo_existS: 
                                    df_new['skrat_counter'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['skrat'][key])[:1].get().material
                              else:
                                    df_new['skrat_counter'][key] = AluminiyProduct.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['skrat'][key])[:1].get().material
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =component,section ='S').exists():
                                    umumiy_counter_termo[component+'-S'] += 1
                                    max_valuesS = umumiy_counter_termo[ component +'-S']
                                    materiale = component+"-S{:03d}".format(max_valuesS)
                                    AluminiyProductTermo(artikul =component,section ='S',counter=max_valuesS,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['skrat'][key],material=materiale).save()
                                    df_new['skrat_counter'][key]=materiale
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
                                                      'kratkiy':df_new['skrat'][key],
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
                                                      'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                                    AluminiyProductTermo(artikul =component,section ='S',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['skrat'][key],material=materiale).save()
                                    df_new['skrat_counter'][key]=materiale
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
                                                      'kratkiy':df_new['skrat'][key],
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
                                                      'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                        termo_existA =AluminiyProductTermo.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['akrat'][key]).exists()
                        simple_existA =AluminiyProduct.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['akrat'][key]).exists()
                        if (termo_existA or simple_existA):
                              if termo_existA:
                                    df_new['akrat_counter'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['akrat'][key])[:1].get().material
                              else:
                                    df_new['akrat_counter'][key] = AluminiyProduct.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['akrat'][key])[:1].get().material
                        
                        else: 
                              if AluminiyProductTermo.objects.filter(artikul =component,section ='A').exists():
                                    umumiy_counter_termo[component+'-A'] += 1
                                    max_valuesA = umumiy_counter_termo[ component +'-A']
                                    materiale = component+"-A{:03d}".format(max_valuesA)
                                    AluminiyProductTermo(artikul =component,section ='A',counter=max_valuesA,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['akrat'][key],material=materiale).save()
                                    df_new['akrat_counter'][key]=materiale
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
                                                      'kratkiy':df_new['akrat'][key],
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
                                                      'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                                    materiale = component+"-A{:03d}".format(1)
                                    AluminiyProductTermo(artikul =component,section ='A',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['akrat'][key],material=materiale).save()
                                    df_new['akrat_counter'][key]=materiale
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
                                                      'kratkiy':df_new['akrat'][key],
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
                                                      'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                                    
                  
                  
                              
                  if ((row['Код наклейки'] != 'NT1') and (row['Тип покрытия'] != 'Ламинированный')) :
                        termo_existN =AluminiyProductTermo.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['nkrat'][key]).exists()
                        simple_existN =AluminiyProduct.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['nkrat'][key]).exists()
                        if (termo_existN or simple_existN):
                              if termo_existN:
                                    df_new['nkrat_counter'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['nkrat'][key])[:1].get().material
                              else:
                                    df_new['nkrat_counter'][key] = AluminiyProduct.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['nkrat'][key])[:1].get().material
                        else:
                              name_tip_pokr =''
                              if (('7777' in df_new['nkrat'][key]) or ('8888' in df_new['nkrat'][key])  or ('3701' in df_new['nkrat'][key]) or ('3702' in df_new['nkrat'][key])):
                                    name_tip_pokr = 'Сублимированный'
                              elif '9016' in df_new['nkrat'][key]:
                                    name_tip_pokr = 'Белый'
                              elif 'MF' in df_new['nkrat'][key]:
                                    name_tip_pokr = 'Неокрашенный'
                              elif anodirovaka_check(ANODIROVKA_CODE,df_new['nkrat'][key]):
                                    name_tip_pokr = 'Анодированный'
                              else:
                                    name_tip_pokr = 'Окрашенный'
                              
                              if  AluminiyProductTermo.objects.filter(artikul =component,section ='N').exists():
                                    umumiy_counter_termo[component+'-N'] += 1
                                    max_valuesN = umumiy_counter_termo[ component +'-N']
                                    materiale = component+"-N{:03d}".format(max_valuesN)
                                    AluminiyProductTermo(artikul =component,section ='N',counter=max_valuesN,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['nkrat'][key],material=materiale).save()
                                    df_new['nkrat_counter'][key]=materiale
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
                                                      'kratkiy':df_new['nkrat'][key],
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
                                                      'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                                    materiale = component+"-N{:03d}".format(1)
                                    AluminiyProductTermo(artikul =component,section ='N',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['nkrat'][key],material=materiale).save()
                                    df_new['nkrat_counter'][key]=materiale
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
                                                      'kratkiy':df_new['nkrat'][key],
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
                                                      'outer_side_wg_s_id':row['Цвет декор пленки снаружи'],
                                                      'inner_side_wg_s_id':row['Цвет декор пленки внутри'],
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
                  
                  
      
      
     
      # print(cache_for_cratkiy_text)
      
      df_char = create_characteristika(cache_for_cratkiy_text) 
      
      df_char_title =create_characteristika_utils(cache_for_cratkiy_text)
      
      # created =request.GET.get('created',None)
      # if not created:
      #       create_all(df_char_title)
      # else:
      #       ves_za_metr = request.GET.get('ves_za_metr',None)    
      #       ves_za_shtuk = request.GET.get('ves_za_shtuk',None)    
      #       price = request.GET.get('price',None)
            
      #       df_char_title['Удельный вес за метр'] = ves_za_metr
      #       df_char_title['Общий вес за штуку'] = ves_za_shtuk
      #       df_char_title['Price'] = price
          
      now = datetime.now()
      year =now.strftime("%Y")
      month =now.strftime("%B")
      day =now.strftime("%a%d")
      hour =now.strftime("%H HOUR")
      minut =now.strftime("%M")

      
      parent_dir ='{MEDIA_ROOT}\\uploads\\aluminiytermo\\'
       
      if not os.path.isdir(parent_dir):
            create_folder(f'{MEDIA_ROOT}\\uploads\\','aluminiytermo')
            
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\',f'{year}')
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\',f'{month}')
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\',day)
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\',hour)
            
            
      if not os.path.isfile(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\alumin_new_termo-{minut}.xlsx'):
            path =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\alumin_new_termo-{minut}.xlsx'
      else:
            st =random.randint(0,1000)
            path =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\alumin_new_termo-{minut}-{st}.xlsx'
            
      
      
      # df_char_title_full = pd.DataFrame(df_char_title)
      # characteristika_created_txt_create(df_char_title_full)
      
      writer = pd.ExcelWriter(path, engine='xlsxwriter')
      df_new.to_excel(writer,index=False,sheet_name ='schotchik')
      df_char.to_excel(writer,index=False,sheet_name ='characteristika')
      df_char_title.to_excel(writer,index=False,sheet_name ='title')
      # df_char_title_full.to_excel(writer,index=False,sheet_name ='title')
      writer.save()
      return redirect('upload_product_termo')
                  
    

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


def update_char_title(request,id):
      file = AluFileTermo.objects.get(id=id).file
      df = pd.read_excel(f'{MEDIA_ROOT}/{file}','title')
      df =df.astype(str)
      
      characteristika_created_txt_create(df)
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