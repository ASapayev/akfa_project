from django.shortcuts import render,redirect
from django.http import JsonResponse
import pandas as pd
from .models import AluFileTermo,AluminiyProductTermo,CharUtilsTwo,CharUtilsOne,CharUtilsThree,CharUtilsFour,CharacteristicTitle,BazaProfiley,Characteristika
from norma.models import Norma
from aluminiy.models import AluminiyProduct,RazlovkaTermo
from .forms import FileFormTermo
from django.db.models import Count,Max
from config.settings import MEDIA_ROOT
import numpy as np
from aluminiy.models import AluFile,AluminiyProduct,ArtikulComponent
from .utils import fabrikatsiya_sap_kod,create_folder,create_characteristika,create_characteristika_utils,characteristika_created_txt_create,anodirovaka_check,check_for_correct
import os
from datetime import datetime
import json
import random
from django.db.models import Q
from .BAZA import ANODIROVKA_CODE
from django.views.decorators.csrf import csrf_exempt
import ast

brand_kraski_snaruji_ABC ={
      'A': 'AKZONOBEL',
      'R':  'RAINBOW',
      'P':  'PULVER',
      'T':  'TIGER',
      'B':  'BPC',
      'M':  'MIKROTON',
      'J':'JOTUN',
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
      'Ocean Blue':'Ocean Blue',
      'Махагон':'МАХАГОН'
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
      'Ocean Blue':'Ocean Blue',
      'Махагон':'МАХАГОН'
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
      'Ocean Blue':'Ocean Blue',
      'Махагон':'МАХАГОН'
}

def product_add_second_termo(id):
        file = AluFileTermo.objects.get(id=id).file
        df = pd.read_excel(f'{MEDIA_ROOT}/{file}')
        df =df.astype(str)
        
        now = datetime.now()
        year =now.strftime("%Y")
        month =now.strftime("%B")
        day =now.strftime("%a%d")
        hour =now.strftime("%H HOUR")
        minut =now.strftime("%M")
        
        nak_norma1 = Norma.objects.filter(наклейка_исключение ='1',артикул='0').values_list('компонент_1',flat=True)
        nak_norma2 = Norma.objects.filter(Q(наклейка_исключение ='1') & ~Q(артикул='0')).values_list('артикул',flat=True)
        nakleyka_iskyucheniye = list(nak_norma1) + list(nak_norma2)
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
        print('**'*20)
        
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
                        else:
                               df_new['U-Упаковка + Готовая Продукция'][key] = df['Краткий текст товара'][key]
                               
                        if df['Тип покрытия'][key] != 'Ламинированный':
                                df_new['K-Комбинирования'][key] = fabrikatsiya_sap_kod(df['Краткий текст товара'][key],df['Длина при выходе из пресса'][key].replace('.0',''))
                        else:
                                df_new['K-Комбинирования'][key] = fabrikatsiya_sap_kod(df['Краткий текст товара'][key].split('_')[0] +' NT1',df['Длина при выходе из пресса'][key].replace('.0',''))
                        
                        if df['Тип покрытия'][key] == 'Ламинированный':
                                plenki1 = False
                                plenki2 = False
                                dlina = df['Длина (мм)'][key]
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
                                print(df['Краткий текст товара'][key],'gg'*40)
                        
                        
                        
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
                                        termo = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='F',kratkiy_tekst_materiala=df_new['Фабрикация'][key])[:1].get()
                                        if row['Тип покрытия'].lower() == 'сублимированный':
                                                tip_poktitiya ='с декоративным покрытием'
                                        else:
                                                tip_poktitiya = row['Тип покрытия'].lower()
                                                                
                                        width_and_height = CharUtilsOne.objects.filter(Q(матрица = termo.artikul) | Q(артикул = termo.artikul))[:1].get()
                                        
                                                
                                        cache_for_cratkiy_text.append(
                                                        {'material':termo.material,
                                                        'kratkiy':df_new['Фабрикация'][key],
                                                        'section':'F-Фабрикация',
                                                        'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                        'system':row['Название системы'],
                                                        'article':termo.artikul,
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
                                termo = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='75',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key])[:1].get()
                        
                                hollow_and_solid =CharUtilsTwo.objects.filter(артикул = termo.artikul)[:1].get().полый_или_фасонный
                                
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
                                
                                width_and_height = CharUtilsOne.objects.filter(Q(матрица = termo.artikul) | Q(артикул = termo.artikul))[:1].get()
                                
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
                                                {'material':termo.material,
                                                'kratkiy':df_new['U-Упаковка + Готовая Продукция 75'][key],
                                                'section':'V-Упаковка + Готовая продукция',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':termo.artikul,
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
                        
                                print('ddd')
                        else:
                                print('ttteeeeeeee'*40,df['Артикул'][key],'***'*10,df_new['U-Упаковка + Готовая Продукция'][key])      
                                if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key]).exists():
                                        print(df['Артикул'][key])
                                        termo = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key])[:1].get()
                                        
                                        hollow_and_solid =CharUtilsTwo.objects.filter(артикул = termo.artikul)[:1].get().полый_или_фасонный
                                        
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
                                        
                                        width_and_height = CharUtilsOne.objects.filter(Q(матрица = termo.artikul) | Q(артикул = termo.artikul))[:1].get()
                                        
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
                                                        {'material':termo.material,
                                                        'kratkiy':df_new['U-Упаковка + Готовая Продукция'][key],
                                                        'section':'U-Упаковка + Готовая продукция',
                                                        'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                        'system':row['Название системы'],
                                                        'article':termo.artikul,
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
                                
                        if AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='K',kratkiy_tekst_materiala=df_new['K-Комбинирования'][key]).exists():
                                termo = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='K',kratkiy_tekst_materiala=df_new['K-Комбинирования'][key])[:1].get()
                                
                                hollow_and_solid =CharUtilsTwo.objects.filter(артикул = termo.artikul)[:1].get().полый_или_фасонный
                                
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
                                
                                
                                width_and_height = CharUtilsOne.objects.filter(Q(матрица = termo.artikul) | Q(артикул = termo.artikul))[:1].get()
                                
                                print(f"K-Комбинирования tip pokr {row['Тип покрытия']}") 
                                
                                
                                
                                
                                
                                cache_for_cratkiy_text.append(
                                                {'material':termo.material,
                                                'kratkiy':df_new['K-Комбинирования'][key],
                                                'section':'K-Комбинирования',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':termo.artikul,
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
                                        termo = AluminiyProductTermo.objects.filter(artikul =df['Артикул'][key],section ='L',kratkiy_tekst_materiala=df_new['Ламинация'][key])[:1].get()
                                        
                                        hollow_and_solid =CharUtilsTwo.objects.filter(артикул = termo.artikul)[:1].get().полый_или_фасонный
                                        
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
                                        
                                        
                                        width_and_height = CharUtilsOne.objects.filter(Q(матрица = termo.artikul) | Q(артикул = termo.artikul))[:1].get()
                                        
                                        print(f"Ламинация1 tip pokr {row['Тип покрытия']}")   
                                        cache_for_cratkiy_text.append(
                                                        {'material':termo.material,
                                                        'kratkiy':df_new['Ламинация'][key],
                                                        'section':'L-Ламинирование',
                                                        'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                        'system':row['Название системы'],
                                                        'article':termo.artikul,
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
                                        print('#'*10,df_new['Покраска автомат'][key],'#'*10,row['Код наклейки'])
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
                        
                        
                        
                        if AluminiyProductTermo.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key]).exists():
                                termo =AluminiyProductTermo.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key])[:1].get()# max_valuesE = AluminiyProductTermo.objects.filter(artikul =component,section ='E').values('section').annotate(total_max=Max('counter'))[0]['total_max']
                                
                                hollow_and_solid =CharUtilsTwo.objects.filter(артикул = termo.artikul)[:1].get().полый_или_фасонный
                                
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
                                
                                
                                width_and_height = CharUtilsOne.objects.filter(Q(матрица = termo.artikul) | Q(артикул = termo.artikul))[:1].get()
                                
                                
                                cache_for_cratkiy_text.append(
                                                {'material':termo.material,
                                                'kratkiy':df_new['Экструзия холодная резка'][key],
                                                'section':'E-Экструзия холодная резка ZPP2',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':termo.artikul,
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
                                
                        
                        if row['тип закаленности']!='T4':
                        
                                if AluminiyProductTermo.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['Печь старения'][key]).exists():
                                        termo = AluminiyProductTermo.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['Печь старения'][key])[:1].get()
                                        
                                        hollow_and_solid =CharUtilsTwo.objects.filter(артикул = termo.artikul)[:1].get().полый_или_фасонный
                                                
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
                                                
                                        
                                        width_and_height = CharUtilsOne.objects.filter(Q(матрица = termo.artikul) | Q(артикул = termo.artikul))[:1].get()
                                        
                                        
                                        cache_for_cratkiy_text.append(
                                                        {'material':termo.material,
                                                        'kratkiy':df_new['Печь старения'][key],
                                                        'section':'Z-Печь старения',
                                                        'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                        'system':row['Название системы'],
                                                        'article':termo.artikul,
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
                                if '9016' in df_new['Покраска автомат'][key]:
                                        tip_pokr ='Белый'
                                else:
                                        tip_pokr ='Окрашенный'
                                if AluminiyProductTermo.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['Покраска автомат'][key]).exists():
                                        termo =AluminiyProductTermo.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['Покраска автомат'][key])[:1].get()
                                        
                                
                                        hollow_and_solid =CharUtilsTwo.objects.filter(артикул = termo.artikul)[:1].get().полый_или_фасонный
                                        
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
                                        
                                        
                                        width_and_height = CharUtilsOne.objects.filter(Q(матрица = termo.artikul) | Q(артикул = termo.artikul))[:1].get()
                                        
                                        print(f"p tip pokr {row['Тип покрытия']}")
                                        
                                        
                                        
                                        cache_for_cratkiy_text.append(
                                                        {'material':termo.material,
                                                        'kratkiy':df_new['Покраска автомат'][key],
                                                        'section':'P-Покраска автомат',
                                                        'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                        'system':row['Название системы'],
                                                        'article':termo.artikul,
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
                        
                        
                                if AluminiyProductTermo.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['Сублимация'][key]).exists():
                                        termo = AluminiyProductTermo.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['Сублимация'][key])[:1].get()
                                
                                        hollow_and_solid =CharUtilsTwo.objects.filter(артикул = termo.artikul)[:1].get().полый_или_фасонный
                                        
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
                                        
                                        
                                        width_and_height = CharUtilsOne.objects.filter(Q(матрица = termo.artikul) | Q(артикул = termo.artikul))[:1].get()
                                        
                                        print(f"S tip pokr {row['Тип покрытия']}")
                                                
                                        cache_for_cratkiy_text.append(
                                                        {'material':termo.material,
                                                        'kratkiy':df_new['Сублимация'][key],
                                                        'section':'S-Сублимация',
                                                        'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                        'system':row['Название системы'],
                                                        'article':termo.artikul,
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
                                if AluminiyProductTermo.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['Анодировка'][key]).exists():
                                        termo =AluminiyProductTermo.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['Анодировка'][key])[:1].get()
                                        
                                
                                        hollow_and_solid =CharUtilsTwo.objects.filter(артикул = termo.artikul)[:1].get().полый_или_фасонный
                                        
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
                                        
                                        
                                        width_and_height = CharUtilsOne.objects.filter(Q(матрица = termo.artikul) | Q(артикул = termo.artikul))[:1].get()
                                        
                                        cache_for_cratkiy_text.append(
                                                        {'material':termo.material,
                                                        'kratkiy':df_new['Анодировка'][key],
                                                        'section':'A-Анодировка',
                                                        'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                        'system':row['Название системы'],
                                                        'article':termo.artikul,
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
                               
                                if  AluminiyProductTermo.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['Наклейка'][key]).exists():
                                        
                                        termo = AluminiyProductTermo.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['Наклейка'][key])[:1].get()
                                
                                        hollow_and_solid =CharUtilsTwo.objects.filter(артикул = termo.artikul)[:1].get().полый_или_фасонный
                                        
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
                                        
                                        
                                        width_and_height = CharUtilsOne.objects.filter(Q(матрица = termo.artikul) | Q(артикул = termo.artikul))[:1].get()
                                        
                                        cache_for_cratkiy_text.append(
                                                        {'material':termo.material,
                                                        'kratkiy':df_new['Наклейка'][key],
                                                        'section':'N-Наклейка',
                                                        'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                        'system':row['Название системы'],
                                                        'article':termo.artikul,
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
        print(cache_for_cratkiy_text)
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
        else:
                st =random.randint(0,1000)
                path =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\alumin_new_termo-{minut}-{st}.xlsx'
                
        if  len(duplicat_list)>0:     
                df_duplicates =pd.DataFrame(np.array(duplicat_list),columns=['SAP CODE','KRATKIY TEXT','SECTION'])
        else:
                df_duplicates =pd.DataFrame(np.array([['','','']]),columns=['SAP CODE','KRATKIY TEXT','SECTION'])

        
        
        
        writer = pd.ExcelWriter(path, engine='xlsxwriter')
        df_new.to_excel(writer,index=False,sheet_name ='Schotchik')
        df_char.to_excel(writer,index=False,sheet_name ='Characteristika')
        df_char_title.to_excel(writer,index=False,sheet_name ='title')
        df_duplicates.to_excel(writer,index=False,sheet_name='Duplicates')
        # df_char_title_full.to_excel(writer,index=False,sheet_name ='title')
        writer.close()
        return redirect('upload_product_termo')
                


def product_add_second_simple(id):
        file = AluFile.objects.get(id=id).file
        df = pd.read_excel(f'{MEDIA_ROOT}/{file}')
        df =df.astype(str)
        
        now = datetime.now()
        year =now.strftime("%Y")
        month =now.strftime("%B")
        day =now.strftime("%a%d")
        hour =now.strftime("%H HOUR")
        minut =now.strftime("%M")
        
        
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
        df_new['SAP код Ф']=''
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
                        obichniy = AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='F',kratkiy_tekst_materiala=df_new['Фабрикация'][key])[:1].get()
                       
                        
                        hollow_and_solid =CharUtilsTwo.objects.filter(артикул = obichniy.artikul)[:1].get().полый_или_фасонный
                        
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
                        
                        width_and_height = CharUtilsOne.objects.filter(Q(матрица = obichniy.artikul) | Q(артикул = obichniy.artikul))[:1].get()
                        
                                
                        cache_for_cratkiy_text.append(
                                            {'material':obichniy.material,
                                            'kratkiy':df_new['Фабрикация'][key],
                                            'section':'F-Фабрикация',
                                            'export_customer_id':row['Код заказчика экспорт если експорт'],
                                            'system':row['Название системы'],
                                            'article':obichniy.artikul,
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
                        obichniy =AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='75',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key])[:1].get()
                        
                        hollow_and_solid =CharUtilsTwo.objects.filter(артикул = obichniy.artikul)[:1].get().полый_или_фасонный
                        
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
                        
                        width_and_height = CharUtilsOne.objects.filter(Q(матрица = obichniy.artikul) | Q(артикул = obichniy.artikul))[:1].get()
                        
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
                                                {'material':obichniy.material,
                                                'kratkiy':df_new['U-Упаковка + Готовая Продукция 75'][key],
                                                'section':'V-Упаковка + Готовая продукция',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':obichniy.artikul,
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
                print('sap code',df['Артикул'][key])      
                if AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key]).exists():
                        obichniy =AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key])[:1].get()
                
                hollow_and_solid =CharUtilsTwo.objects.filter(артикул = obichniy.artikul)[:1].get().полый_или_фасонный
                
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
                
                width_and_height = CharUtilsOne.objects.filter(Q(матрица = obichniy.artikul) | Q(артикул = obichniy.artikul))[:1].get()
                
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
                                        {'material':obichniy.material,
                                        'kratkiy':df_new['U-Упаковка + Готовая Продукция'][key],
                                        'section':'U-Упаковка + Готовая продукция',
                                        'export_customer_id':row['Код заказчика экспорт если експорт'],
                                        'system':row['Название системы'],
                                        'article':obichniy.artikul,
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
                
                
        
                    
                
                if df['Тип покрытия'][key] == 'Ламинированный':       
                    if AluminiyProduct.objects.filter(artikul =component,section ='L',kratkiy_tekst_materiala=df_new['Ламинация'][key]).exists():
                        obichniy = AluminiyProduct.objects.filter(artikul =component,section ='L',kratkiy_tekst_materiala=df_new['Ламинация'][key])[:1].get()
                        
                        hollow_and_solid =CharUtilsTwo.objects.filter(артикул = obichniy.artikul)[:1].get().полый_или_фасонный
                        
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
                        
                        
                        width_and_height = CharUtilsOne.objects.filter(Q(матрица = obichniy.artikul) | Q(артикул = obichniy.artikul))[:1].get()
                        
                                
                        cache_for_cratkiy_text.append(
                                            {'material':obichniy.material,
                                            'kratkiy':df_new['Ламинация'][key],
                                            'section':'L-Ламинирование',
                                            'export_customer_id':row['Код заказчика экспорт если експорт'],
                                            'system':row['Название системы'],
                                            'article':obichniy.artikul,
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
                    
                
                
                
                if AluminiyProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key]).exists():
                        obichniy = AluminiyProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key])[:1].get()
                        
                        
                        hollow_and_solid =CharUtilsTwo.objects.filter(артикул = obichniy.artikul)[:1].get().полый_или_фасонный
                            
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
                            
                        print(obichniy.artikul)
                        width_and_height = CharUtilsOne.objects.filter(Q(матрица = obichniy.artikul) | Q(артикул = obichniy.artikul))[:1].get()
                        
                            
                        cache_for_cratkiy_text.append(
                                        {'material':obichniy.material,
                                        'kratkiy':df_new['Экструзия холодная резка'][key],
                                        'section':'E-Экструзия холодная резка ZPP2',
                                        'export_customer_id':row['Код заказчика экспорт если експорт'],
                                        'system':row['Название системы'],
                                        'article':obichniy.artikul,
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
                            
                        
                
                if row['тип закаленности']!='T4':
                    if AluminiyProduct.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['Печь старения'][key]).exists():
                        obichniy = AluminiyProduct.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['Печь старения'][key])[:1].get()
                        
                        hollow_and_solid =CharUtilsTwo.objects.filter(артикул = obichniy.artikul)[:1].get().полый_или_фасонный
                                
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
                                
                        
                        width_and_height = CharUtilsOne.objects.filter(Q(матрица = obichniy.artikul) | Q(артикул = obichniy.artikul))[:1].get()
                        
                                
                        cache_for_cratkiy_text.append(
                                            {'material':obichniy.material,
                                            'kratkiy':df_new['Печь старения'][key],
                                            'section':'Z-Печь старения',
                                            'export_customer_id':row['Код заказчика экспорт если експорт'],
                                            'system':row['Название системы'],
                                            'article':obichniy.artikul,
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
                    
                    if '9016' in df_new['Покраска автомат'][key]:
                        tip_pokr ='Белый'
                    else:
                        tip_pokr ='Окрашенный' 
                    if AluminiyProduct.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['Покраска автомат'][key]).exists():
                        obichniy =AluminiyProduct.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['Покраска автомат'][key])[:1].get()
                        
                    
                        hollow_and_solid =CharUtilsTwo.objects.filter(артикул = obichniy.artikul)[:1].get().полый_или_фасонный
                        
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
                        
                        
                        width_and_height = CharUtilsOne.objects.filter(Q(матрица = obichniy.artikul) | Q(артикул = obichniy.artikul))[:1].get()
                        
                                
                        cache_for_cratkiy_text.append(
                                            {'material':obichniy.material,
                                            'kratkiy':df_new['Покраска автомат'][key],
                                            'section':'P-Покраска автомат',
                                            'export_customer_id':row['Код заказчика экспорт если експорт'],
                                            'system':row['Название системы'],
                                            'article':obichniy.artikul,
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
                     
                    if AluminiyProduct.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['Сублимация'][key]).exists():
                        obichniy =AluminiyProduct.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['Сублимация'][key])[:1].get()
                    
                        hollow_and_solid =CharUtilsTwo.objects.filter(артикул = obichniy.artikul)[:1].get().полый_или_фасонный
                        
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
                        
                        
                        width_and_height = CharUtilsOne.objects.filter(Q(матрица = obichniy.artikul) | Q(артикул = obichniy.artikul))[:1].get()
                        
                                
                        cache_for_cratkiy_text.append(
                                            {'material':obichniy.material,
                                            'kratkiy':df_new['Сублимация'][key],
                                            'section':'S-Сублимация',
                                            'export_customer_id':row['Код заказчика экспорт если експорт'],
                                            'system':row['Название системы'],
                                            'article':obichniy.artikul,
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
                    
                    if AluminiyProduct.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['Анодировка'][key]).exists():
                        obichniy = AluminiyProduct.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['Анодировка'][key])[:1].get()
                        
                    
                        hollow_and_solid =CharUtilsTwo.objects.filter(артикул = obichniy.artikul)[:1].get().полый_или_фасонный
                        
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
                        
                        
                        width_and_height = CharUtilsOne.objects.filter(Q(матрица = obichniy.artikul) | Q(артикул = obichniy.artikul))[:1].get()
                        
                                
                        cache_for_cratkiy_text.append(
                                            {'material':obichniy.material,
                                            'kratkiy':df_new['Анодировка'][key],
                                            'section':'A-Анодировка',
                                            'export_customer_id':row['Код заказчика экспорт если експорт'],
                                            'system':row['Название системы'],
                                            'article':obichniy.artikul,
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
                    if  AluminiyProduct.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['Наклейка'][key]).exists():
                        obichniy = AluminiyProduct.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['Наклейка'][key])[:1].get()
                        
                        hollow_and_solid =CharUtilsTwo.objects.filter(артикул = obichniy.artikul)[:1].get().полый_или_фасонный
                        
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
                        
                        
                        width_and_height = CharUtilsOne.objects.filter(Q(матрица = obichniy.artikul) | Q(артикул = obichniy.artikul))[:1].get()
                        
                                
                        cache_for_cratkiy_text.append(
                                            {
                                            'material':obichniy.material,
                                            'kratkiy':df_new['Наклейка'][key],
                                            'section':'N-Наклейка',
                                            'export_customer_id':row['Код заказчика экспорт если експорт'],
                                            'system':row['Название системы'],
                                            'article':obichniy.artikul,
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
        print(cache_for_cratkiy_text)
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



       
        writer = pd.ExcelWriter(path, engine='xlsxwriter')
        df_new.to_excel(writer,index=False,sheet_name='Schotchik')
        df_char.to_excel(writer,index=False,sheet_name='Characteristika')
        df_char_title.to_excel(writer,index=False,sheet_name='title')
        df_duplicates.to_excel(writer,index=False,sheet_name='Duplicates')
        writer.close()
        
        return redirect('upload_product')
                    
