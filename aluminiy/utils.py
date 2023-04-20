
from .models import ArtikulComponent
from aluminiytermo.models import BazaProfiley
import os
from aluminiytermo.models import CharacteristicTitle
from django.db.models import Q
import pandas as pd

def fabrikatsiya_sap_kod(sap_kod,length):
    new =sap_kod.split(' ')
    for i in range(0,len(new)):
        if new[i].startswith('L'):
            new[i]=f'L{length}'
    return ' '.join(new)

def do_exist(artikules):
    return ArtikulComponent.objects.filter(artikul__in=artikules).count() == len(artikules)

def create_folder(parent_dir,directory):
    path =os.path.join(parent_dir,directory)
    if not os.path.isdir(path):
        os.mkdir(path)
        

def create_characteristika_utils(items):
    df =[
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[]
    ]
    
    for item in items:
        if '-L' in item['material']:
            continue
        sap_kode =item['material'].split('-')[0]
        baza_profiey = BazaProfiley.objects.filter(Q(артикул=sap_kode)|Q(компонент=sap_kode))[:1].get()
        
        if '-7' in item['material']:
            component_name ='Артикул'
        else:
            component_name ='Компонент'
        
        if '-7' in item['material']:
            gruppa_material ='ALUGP'
        else:
            gruppa_material ='ALUPF'
            
        дата_изменение_добавление =''
        статус_изменение_добавление=''
        ссылки_для_чертежа=''
        sap_код_s4p_100=item['material']
        нумерация_до_sap =''
        короткое_название_sap =item['kratkiy'],
        польное_наименование_sap =  'Алюминиевый '+baza_profiey.product_description +', '+component_name +' '+sap_kode+', '+item['surface_treatment']+', Длина '+item['length']+' мм, Тип '+item['alloy']+'-'+item['temper']+' '+item['print_view']
        ед_изм ='ШТ'
        альтернативная_ед_изм='КГ'
        коэфициент_пересчета =''
        альтернативный_участок=''
        участок = item['section']
        длина = item['length']
        ширина = ''
        высота = ''
        группа_материалов =gruppa_material
        удельный_вес_за_метр =''
        общий_вес_за_штуку =''
      
        characteristik = CharacteristicTitle(
                дата_изменение_добавление =дата_изменение_добавление,
                статус_изменение_добавление =статус_изменение_добавление,
                ссылки_для_чертежа =ссылки_для_чертежа,
                sap_код_s4p_100 =sap_код_s4p_100,
                нумерация_до_sap =нумерация_до_sap,
                короткое_название_sap =короткое_название_sap,
                польное_наименование_sap =польное_наименование_sap,
                ед_изм =ед_изм,
                альтернативная_ед_изм =альтернативная_ед_изм,
                коэфициент_пересчета =коэфициент_пересчета,
                участок =участок,
                альтернативный_участок =альтернативный_участок,
                длина =длина,
                ширина =ширина,
                высота =высота,
                группа_материалов =группа_материалов,
                удельный_вес_за_метр =удельный_вес_за_метр,
                общий_вес_за_штуку =общий_вес_за_штуку
                )
        characteristik.save()
        
        df[0].append(дата_изменение_добавление)
        df[1].append(статус_изменение_добавление)
        df[2].append(ссылки_для_чертежа)
        df[3].append(sap_код_s4p_100)
        df[4].append(нумерация_до_sap)
        df[5].append(короткое_название_sap)
        df[6].append(польное_наименование_sap)
        df[7].append(ед_изм)
        df[8].append(альтернативная_ед_изм)
        df[9].append(коэфициент_пересчета)
        df[10].append(участок)
        df[11].append(альтернативный_участок)
        df[12].append(длина)
        df[13].append(ширина)
        df[14].append(высота)
        df[15].append(группа_материалов)
        df[16].append(удельный_вес_за_метр)
        df[17].append(общий_вес_за_штуку)
        
    data = {
        'Дата изменение/добавление':df[0],
        'Статус изменение/добавление':df[1],
        'Ссылки для чертежа':df[2],
        'SAP код S4P 100':df[3],
        'Нумерация до SAP':df[4],
        'Короткое название SAP':df[5],
        'Польное наименование SAP':df[6],
        'Ед, Изм,':df[7],
        'Альтернативная ед, изм':df[8],
        'Коэфициент пересчета':df[9],
        'Участок':df[10],
        'Альтернативный участок':df[11],
        'Длина':df[12],
        'Ширина':df[13],
        'Высота':df[14],
        'группа материалов':df[15],
        'Удельный вес за метр':df[16],
        'Общий вес за штуку':df[17]
    }
    
    df_new = pd.DataFrame(data)
    
    return df_new


            