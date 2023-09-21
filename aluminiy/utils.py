
from .models import ArtikulComponent,RazlovkaObichniy,RazlovkaTermo
from aluminiytermo.models import BazaProfiley
import os
from aluminiytermo.models import CharacteristicTitle
from django.db.models import Q
import pandas as pd
from io import BytesIO as IO
from django.http import HttpResponse,FileResponse
from datetime import datetime
from config.settings import MEDIA_ROOT
import numpy as np
import zipfile



def characteristika_created_txt_create_1301_v2(datas):
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR %S")
    minut =now.strftime("%M-%S MINUT")
    
    
    parent_dir =f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala\\'
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads','sozdaniye_materiala')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala\\{year}',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala\\{year}\\{month}',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala\\{year}\\{month}\\{day}',f'{hour}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala\\{year}\\{month}\\{day}\\{hour}','IMZO')
    create_folder(f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala\\{year}\\{month}\\{day}\\{hour}\\IMZO',minut)
    pathtext1 =f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala\\{year}\\{month}\\{day}\\{hour}\\IMZO\\{minut}\\1.txt'
    pathtext2 =f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala\\{year}\\{month}\\{day}\\{hour}\\IMZO\\{minut}\\2.txt'
    pathtext3 =f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala\\{year}\\{month}\\{day}\\{hour}\\IMZO\\{minut}\\3.txt'
    pathtext4 =f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala\\{year}\\{month}\\{day}\\{hour}\\IMZO\\{minut}\\4.txt'
    pathtext55 =f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala\\{year}\\{month}\\{day}\\{hour}\\IMZO\\{minut}\\5.txt'
    pathtext5 =f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala\\{year}\\{month}\\{day}\\{hour}\\IMZO\\{minut}\\Единицы изм.txt'
    pathtext6 =f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala\\{year}\\{month}\\{day}\\{hour}\\IMZO\\{minut}\\Лист в C 3.xlsx'
    pathtext7 =f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala\\{year}\\{month}\\{day}\\{hour}\\IMZO\\{minut}\\Длинный текс.txt'
    pathtext8 =f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala\\{year}\\{month}\\{day}\\{hour}\\IMZO\\{minut}\\Бух название SDLONGTEXT.txt'
    pathtext9 =f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala\\{year}\\{month}\\{day}\\{hour}\\IMZO\\{minut}\\ZMD_11_0008 - Прикрепление чертежей ОЗМ.xlsx'
    pathzip =f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala\\{year}\\{month}\\{day}\\{hour}'
    
    
    umumiy_without_duplicate1201 =[[] for i in range(0,49)] 
    

    for key , row in datas.iterrows():
                
        umumiy_without_duplicate1201[0].append(row['MATNR'])
        umumiy_without_duplicate1201[1].append(row['MATNR'])
        umumiy_without_duplicate1201[2].append(row['MAKTX'])
        umumiy_without_duplicate1201[3].append('М2')
        umumiy_without_duplicate1201[4].append('ZPRF')
        umumiy_without_duplicate1201[5].append('5')
        umumiy_without_duplicate1201[6].append('4')
        umumiy_without_duplicate1201[7].append('F')
        umumiy_without_duplicate1201[8].append('21')
        umumiy_without_duplicate1201[9].append('')
        umumiy_without_duplicate1201[10].append('')
        umumiy_without_duplicate1201[11].append('КГ')
        umumiy_without_duplicate1201[12].append('ZNRM')
        umumiy_without_duplicate1201[13].append(row['MAKTX'])
        umumiy_without_duplicate1201[14].append('М2')
        umumiy_without_duplicate1201[15].append('999')
        umumiy_without_duplicate1201[16].append('X')
        umumiy_without_duplicate1201[17].append('0000')
        umumiy_without_duplicate1201[18].append('PD')
        umumiy_without_duplicate1201[19].append('EX')
        umumiy_without_duplicate1201[20].append('0')
        umumiy_without_duplicate1201[21].append('E')
        umumiy_without_duplicate1201[22].append('PS01')
        umumiy_without_duplicate1201[23].append('')
        umumiy_without_duplicate1201[24].append('M')
        umumiy_without_duplicate1201[25].append('02')
        umumiy_without_duplicate1201[26].append('26')
        umumiy_without_duplicate1201[27].append('S100')
        umumiy_without_duplicate1201[28].append('X')
        umumiy_without_duplicate1201[29].append('5')
        umumiy_without_duplicate1201[30].append('Z_SAP_PP_002')
        umumiy_without_duplicate1201[31].append('4')
        umumiy_without_duplicate1201[32].append('SAP999')
        umumiy_without_duplicate1201[33].append('26')
        umumiy_without_duplicate1201[34].append('1301')
        umumiy_without_duplicate1201[35].append('3')
        umumiy_without_duplicate1201[36].append('0100')
        umumiy_without_duplicate1201[37].append('S')
        umumiy_without_duplicate1201[38].append('1')
        umumiy_without_duplicate1201[39].append(row['STPRS'])
        umumiy_without_duplicate1201[40].append('1301')
        umumiy_without_duplicate1201[41].append('X')
        umumiy_without_duplicate1201[42].append('X')
        umumiy_without_duplicate1201[43].append('1')
   
      
        umumiy_without_duplicate1201[44].append('1301AL')

        umumiy_without_duplicate1201[45].append('X')
        umumiy_without_duplicate1201[46].append('1')
        umumiy_without_duplicate1201[47].append('')
        umumiy_without_duplicate1201[48].append('')
    


    
 
    
    ########################## 1.txt ##############################
    d1={}
    header1 ='MATNR\tBISMT\tMAKTX\tMEINS\tMTART\tMATKL\tWERKS\tBESKZ\tSPART\tBRGEW\tNTGEW\tGEWEI\tMTPOS_MARA'
    
    d1['MATNR']=umumiy_without_duplicate1201[0]
    d1['BISMT']=umumiy_without_duplicate1201[1]
    d1['MAKTX']=umumiy_without_duplicate1201[2]
    d1['MEINS']=umumiy_without_duplicate1201[3]
    d1['MTART']=umumiy_without_duplicate1201[4]
    d1['MATKL']=['CFA010101' if 'ALU' in x else 'CSPVC' for x in umumiy_without_duplicate1201[1]]
    d1['WERKS']=umumiy_without_duplicate1201[34]
    d1['BESKZ']=umumiy_without_duplicate1201[7]
    d1['SPART']=['21' if 'ALU' in x else '22' for x in umumiy_without_duplicate1201[1]]
    d1['BRGEW']=umumiy_without_duplicate1201[23]
    d1['NTGEW']=umumiy_without_duplicate1201[23]
    d1['GEWEI']=umumiy_without_duplicate1201[23]
    d1['MTPOS_MARA']=umumiy_without_duplicate1201[12]
    
    
    df1= pd.DataFrame(d1)
    
    np.savetxt(pathtext1, df1.values,fmt='%s', delimiter="\t",header=header1,comments='',encoding='ansi')
        
    ########################## end 1.txt ##############################

    ########################## 2.txt ##############################
    header2='MAKTX\tMEINS\tMTART\tMATNR\tWERKS\tEKGRP\tXCHPF\tDISGR\tDISMM\tDISPO\tDISLS\tWEBAZ\tBESKZ\tLGFSB\tPLIFZ\tPERKZ\tMTVFP\tSCM_STRA1\tVRMOD\tPPSKZ\tSCM_WHATBOM\tSCM_HEUR_ID\tSCM_RRP_TYPE\tSCM_PROFID\tSTRGR\tBWKEY\tMLAST\tBKLAS\tVPRSV\tPEINH\tSTPRS\tPRCTR\tEKALR\tHKMAT\tLOSGR\tSFCPF\tUEETK\tLGPRO\tSBDKZ\tSOBSL'
  
    d2={}
    d2['MAKTX']=umumiy_without_duplicate1201[13] * 2
    d2['MEINS']=umumiy_without_duplicate1201[14] * 2
    d2['MTART']=umumiy_without_duplicate1201[4] * 2
    d2['MATNR']=umumiy_without_duplicate1201[0] * 2
    d2['WERKS']=umumiy_without_duplicate1201[34] + ['1305' for x in umumiy_without_duplicate1201[34]]
    d2['EKGRP']=umumiy_without_duplicate1201[15] + ['540' for x in umumiy_without_duplicate1201[34]]
    d2['XCHPF']=umumiy_without_duplicate1201[16] * 2
    d2['DISGR']=umumiy_without_duplicate1201[17] * 2
    d2['DISMM']=umumiy_without_duplicate1201[18] * 2
    d2['DISPO']=['IMA' if 'ALU' in x else 'IMP' for x in umumiy_without_duplicate1201[0]] * 2
    d2['DISLS']=umumiy_without_duplicate1201[19] + ['MB' for x in umumiy_without_duplicate1201[34]]
    d2['WEBAZ']=umumiy_without_duplicate1201[20] * 2
    d2['BESKZ']=umumiy_without_duplicate1201[21] + ['F' for x in umumiy_without_duplicate1201[21]]
    d2['LGFSB']=umumiy_without_duplicate1201[27] + umumiy_without_duplicate1201[23]
    d2['PLIFZ']=umumiy_without_duplicate1201[23] * 2
    d2['PERKZ']=umumiy_without_duplicate1201[24] * 2
    d2['MTVFP']=umumiy_without_duplicate1201[25] + umumiy_without_duplicate1201[23]
    d2['SCM_STRA1']=umumiy_without_duplicate1201[26] + umumiy_without_duplicate1201[23]
    d2['VRMOD']=umumiy_without_duplicate1201[23] * 2
    d2['PPSKZ']=umumiy_without_duplicate1201[45] + umumiy_without_duplicate1201[23]

    d2['SCM_WHATBOM']=umumiy_without_duplicate1201[5] + umumiy_without_duplicate1201[23]

    d2['SCM_HEUR_ID']=umumiy_without_duplicate1201[30] + umumiy_without_duplicate1201[23]
    
    d2['SCM_RRP_TYPE']=umumiy_without_duplicate1201[6] + umumiy_without_duplicate1201[23]

    d2['SCM_PROFID']=umumiy_without_duplicate1201[32] + umumiy_without_duplicate1201[23]

    d2['STRGR']=umumiy_without_duplicate1201[33] + umumiy_without_duplicate1201[23]
    d2['BWKEY']=umumiy_without_duplicate1201[34] + ['1305' for x in umumiy_without_duplicate1201[34]]
    d2['MLAST']=umumiy_without_duplicate1201[35] * 2
    d2['BKLAS']=umumiy_without_duplicate1201[36] * 2
    d2['VPRSV']=umumiy_without_duplicate1201[37] * 2
    d2['PEINH']=umumiy_without_duplicate1201[38] * 2
    d2['STPRS']=[round(float(str(n).replace(',','.')),2) for n in umumiy_without_duplicate1201[39]] * 2
    d2['PRCTR']=umumiy_without_duplicate1201[40] + ['1305' for x in umumiy_without_duplicate1201[34]]
    d2['EKALR']=umumiy_without_duplicate1201[41] * 2
    d2['HKMAT']=umumiy_without_duplicate1201[42] * 2
    d2['LOSGR']=umumiy_without_duplicate1201[43] * 2
    d2['SFCPF']=umumiy_without_duplicate1201[44] + umumiy_without_duplicate1201[23]
    d2['UEETK']=umumiy_without_duplicate1201[45] * 2
    
    d2['LGPRO']=umumiy_without_duplicate1201[22] + umumiy_without_duplicate1201[23]

    d2['SBDKZ']=umumiy_without_duplicate1201[46] + umumiy_without_duplicate1201[23]
    d2['SOBSL']=umumiy_without_duplicate1201[47] +['80' for x in umumiy_without_duplicate1201[47]]

    df2= pd.DataFrame(d2)
    np.savetxt(pathtext2, df2.values,fmt='%s', delimiter="\t",header=header2,comments='',encoding='ansi')
    ########################## end 2.txt ##############################

    ########################## 3.txt ##############################
    header3 ='MAKTX\tMEINS\tMTART\tSPART\tMATNR\tWERKS\tVKORG\tMTPOS\tVTWEG\tPRCTR\tMTVFP\tALAND\tTATYP\tTAXKM\tVERSG\tKTGRM\tKONDM\tLADGR\tTRAGR'
    d3={
        'MAKTX':[],
        'MEINS':[],
        'MTART':[],
        'SPART':[],
        'MATNR':[],
        'WERKS':[],
        'VKORG':[],
        'MTPOS':[],
        'VTWEG':[],
        'PRCTR':[],
        'MTVFP':[],
        'ALAND':[],
        'TATYP':[],
        'TAXKM':[],
        'VERSG':[],
        'KTGRM':[],
        'KONDM':[],
        'LADGR':[],
        'TRAGR':[]
    }
    VTWEG =['99','10','20']
    
    for i in range(0,3):
        d3['MAKTX'] += umumiy_without_duplicate1201[13] * 2
        d3['MEINS'] += umumiy_without_duplicate1201[14] * 2
        d3['MTART'] += umumiy_without_duplicate1201[4] * 2
        d3['SPART'] += ['21' if 'ALU' in x else '22' for x in umumiy_without_duplicate1201[0]] * 2
        d3['MATNR'] += umumiy_without_duplicate1201[0] * 2
        d3['WERKS'] += umumiy_without_duplicate1201[34] + ['1305' for x in umumiy_without_duplicate1201[34]]
        d3['VKORG'] += [ 1300 for j in range(0,len(umumiy_without_duplicate1201[13]))] * 2
        d3['MTPOS'] += umumiy_without_duplicate1201[12] * 2
        d3['VTWEG'] += [ VTWEG[i] for j in range(0,len(umumiy_without_duplicate1201[13]))] * 2
        d3['PRCTR'] += umumiy_without_duplicate1201[40] + ['1305' for x in umumiy_without_duplicate1201[40]]
        d3['MTVFP'] += [ '02' for j in range(0,len(umumiy_without_duplicate1201[13]))] * 2
        d3['ALAND'] += [ 'UZ' for j in range(0,len(umumiy_without_duplicate1201[13]))] * 2
        d3['TATYP'] += [ 'MWST' for j in range(0,len(umumiy_without_duplicate1201[13]))] * 2
        d3['TAXKM'] += [ '1' for j in range(0,len(umumiy_without_duplicate1201[13]))] * 2
        d3['VERSG'] += [ '1' for j in range(0,len(umumiy_without_duplicate1201[13]))] * 2
        d3['KTGRM'] += [ '01' for j in range(0,len(umumiy_without_duplicate1201[13]))] * 2
        d3['KONDM'] += [ '01' for j in range(0,len(umumiy_without_duplicate1201[13]))] * 2
        d3['LADGR'] += [ '0001' for j in range(0,len(umumiy_without_duplicate1201[13]))] * 2
        d3['TRAGR'] += [ '0001' for j in range(0,len(umumiy_without_duplicate1201[13]))]  * 2
    df3= pd.DataFrame(d3)
    np.savetxt(pathtext3, df3.values, fmt='%s', delimiter="\t",header=header3,comments='',encoding='ansi')
    ########################## end 3.txt ##############################
        
    
    


    file_path =f'{pathzip}.zip'

    zip(pathzip, pathzip)

    return [file_path,]

def zip(src, dst):
    zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            zf.write(absname, arcname)
    zf.close()



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


def save_razlovka(df_new,file_type):
    if file_type =='simple':
        for key,razlov in df_new.iterrows():
            if razlov['SAP код 7']!='':
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
                            fsap_code =razlov['SAP код Ф'],
                            fkratkiy =razlov['Фабрикация'],
                            sap_code75 =razlov['SAP код 75'],
                            kratkiy75 =razlov['U-Упаковка + Готовая Продукция 75']
                        ).save()
                else:
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
                            fsap_code =razlov['SAP код Ф'],
                            fkratkiy =razlov['Фабрикация'],
                            sap_code75 =razlov['SAP код 75'],
                            kratkiy75 =razlov['U-Упаковка + Готовая Продукция 75']
                        ).save()
    else:
        for key,razlov in df_new.iterrows():

            if  razlov['SAP код 7']!="":
                
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
                        fsap_code =razlov['SAP код Ф'],
                        fkratkiy =razlov['Фабрикация'],
                        sap_code75 =razlov['SAP код 75'],
                        kratkiy75 =razlov['U-Упаковка + Готовая Продукция 75']
                    )
                    razlovka_komb.save()
                else:
                    razlovka_yoq=False
            
            elif razlov['SAP код 75'] !='':
                if not RazlovkaTermo.objects.filter(sap_code75=razlov['SAP код 75'],kratkiy75=razlov['U-Упаковка + Готовая Продукция 75']).exists():
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
                        fsap_code =razlov['SAP код Ф'],
                        fkratkiy =razlov['Фабрикация'],
                        sap_code75 =razlov['SAP код 75'],
                        kratkiy75 =razlov['U-Упаковка + Готовая Продукция 75']
                    )
                    razlovka_komb.save()
                else:
                    razlovka_yoq=False
            else:
                  print(key)
                  if razlovka_yoq:
                        print(key)
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
                            fsap_code =razlov['SAP код Ф'],
                            fkratkiy =razlov['Фабрикация'],
                            sap_code75 =razlov['SAP код 75'],
                            kratkiy75 =razlov['U-Упаковка + Готовая Продукция 75']
                        ).save()

def download_bs64(download_df_list,name):
    excel_file = IO()

    xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')
    i = 1
    for download_df in download_df_list:
        download_df.to_excel(xlwriter,index=False,sheet_name=f'{i}')
        i+=1
    xlwriter.close()

    excel_file.seek(0)
    content =f"attachment; filename={name}.xlsx"
    response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = content
    return response       
