import os
from .models import Characteristika
from order.models import OrderPVX
import pandas as pd
from datetime import datetime
from config.settings import MEDIA_ROOT
from .models import ArtikulKomponentPVC,AbreviaturaLamination,CameraPvc,LengthOfProfilePVC,DliniyText,PVCProduct
from .BAZA import *
import numpy as np
import zipfile



def check_for_correct(items):
    abreviation_list =[]
    camera =[]
    component_list =[]
    
    
    for key,row in items.iterrows():
        artikle = row['Артикул']
        if items['Тип покрытия'][key] == 'Ламинированный':
            if not AbreviaturaLamination.objects.filter(abreviatura =row['Код лам пленки снаружи']).exists():
                if row['Код лам пленки снаружи'] not in abreviation_list:
                    abreviation_list.append(row['Код лам пленки снаружи'])

           
        if not CameraPvc.objects.filter(sap_code=row['Артикул']).exists():
            if artikle not in camera:
                camera.append(artikle)

        if ArtikulKomponentPVC.objects.filter(artikul=row['Артикул']).exists():
            continue
        if row['Артикул'] not in component_list:
            component_list.append(row['Артикул'])
                    
    correct = True
    char_utils_correct = abreviation_list + camera  + component_list
    if len(char_utils_correct) >0:
        correct = False
       
    return [ abreviation_list , camera , component_list ] , correct


def characteristika_created_txt_create(datas,order_id):
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR %M %S")
    minut =now.strftime("%M-%S MINUT")
    if order_id:
        order = OrderPVX.objects.get(id = order_id)
        
   
    parent_dir =f'{MEDIA_ROOT}\\uploads\\pvc'
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads','pvc')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\pvc',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\pvc\\{year}',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}',f'{hour} PVC')
    create_folder(f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}\\{hour} PVC',minut)
    pathtext1 =f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}\\{hour} PVC\\{minut}\\1.txt'
    pathtext2 =f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}\\{hour} PVC\\{minut}\\2.txt'
    pathtext3 =f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}\\{hour} PVC\\{minut}\\3.txt'
    pathtext4 =f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}\\{hour} PVC\\{minut}\\4.txt'
    pathtext55 =f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}\\{hour} PVC\\{minut}\\5.txt'
    pathtext5 =f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}\\{hour} PVC\\{minut}\\Единицы изм.txt'
    pathtext6 =f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}\\{hour} PVC\\{minut}\\Лист в C 3.xlsx'
    pathtext7 =f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}\\{hour} PVC\\{minut}\\Длинный текс.txt'
    pathtext8 =f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}\\{hour} PVC\\{minut}\\Бух название SDLONGTEXT.txt'
    pathtext9 =f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}\\{hour} PVC\\{minut}\\ZMD_11_0008 - Прикрепление чертежей ОЗМ.xlsx'
    pathzip =f'{MEDIA_ROOT}\\uploads\\pvc\\{year}\\{month}\\{day}\\{hour} PVC'
    
    

    umumiy_without_duplicate1203 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D1 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D2 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D3 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D4 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D5 =[[] for i in range(0,49)]
    
    dlinniy_text_zero =[[],[],[]]
    buxgalterskiy_naz =[[],[],[],[],[],[],[],[]]
    

    for key , row in datas.iterrows():
        if '-L' in row['SAP код S4P 100']:
            continue 

        row['Длина'] = row['Длина'].replace('.0','')

        if PVCProduct.objects.filter( material= row['SAP код S4P 100']).exists():
            product_pvc = PVCProduct.objects.filter(material = row['SAP код S4P 100'])[:1].get()
            product_pvc.brutto = row['Brutto']
            product_pvc.netto = row['Netto']
            product_pvc.standart_price = row['Price']
            product_pvc.save()

        if '-E' not in row['SAP код S4P 100']:
            dlinniy_text_zero[0].append('1')
            dlinniy_text_zero[1].append(row['SAP код S4P 100'])
            dlinniy_text_zero[2].append(row['Польное наименование SAP'])
            
            dlinniy_text_zero[0].append('2')
            dlinniy_text_zero[1].append(row['SAP код S4P 100'])
            dlinniy_text_zero[2].append(row['Польное наименование SAP'])
        
        
        ############################ bugalter nazvaniya###
        if '-7' in row['SAP код S4P 100']:
            
            for ii in range(0,3):
                if ii ==0:
                    vtweg ='20'
                elif ii ==1:
                    vtweg ='10'
                elif ii ==2:
                    vtweg ='99'

                if ii == 0: 
                    buxgalterskiy_naz[0].append('1')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1200')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('RU')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append('')

                    buxgalterskiy_naz[0].append('1')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1200')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('EN')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append('')
                
                    buxgalterskiy_naz[0].append('2')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1200')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('RU')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append(row['export_description'])
                
                    buxgalterskiy_naz[0].append('2')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1200')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('EN')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append(row['export_description_eng'])
                
                if ((ii!= 0) and (row['online_savdo_name'] != '' and row['online_savdo_name'] != 'nan')):
                    buxgalterskiy_naz[0].append('1')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1200')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('RU')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append('')
                
                    buxgalterskiy_naz[0].append('2')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1200')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('RU')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append(row['online_savdo_name'])
                elif ii > 0 :
                    buxgalterskiy_naz[0].append('1')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1200')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('RU')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append('')

                    buxgalterskiy_naz[0].append('1')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1200')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('EN')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append('')
                
                    buxgalterskiy_naz[0].append('2')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1200')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('RU')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append(row['export_description'])
                
                    buxgalterskiy_naz[0].append('2')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1200')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('EN')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append(row['export_description_eng'])
        
        ############################ end bugalter nazvaniya###
        
        if '-7' in row['SAP код S4P 100']:
            gruppa_material ='PVCGP'
        else:
            gruppa_material ='PVCPF'
                
        umumiy_without_duplicate1203[0].append(row['SAP код S4P 100'])
        umumiy_without_duplicate1203[1].append(row['SAP код S4P 100'])
        umumiy_without_duplicate1203[2].append(row['Короткое название SAP'])
        umumiy_without_duplicate1203[3].append('ШТ')
        umumiy_without_duplicate1203[4].append('ZPRF')
        umumiy_without_duplicate1203[5].append(gruppa_material)
        umumiy_without_duplicate1203[6].append(row['sb'])
        umumiy_without_duplicate1203[7].append('E')
        umumiy_without_duplicate1203[8].append('02')
        umumiy_without_duplicate1203[9].append(row['Brutto'])
        umumiy_without_duplicate1203[10].append(row['Netto'])
        umumiy_without_duplicate1203[11].append('КГ')
        umumiy_without_duplicate1203[12].append('NORM')
        umumiy_without_duplicate1203[13].append(row['Короткое название SAP'])
        umumiy_without_duplicate1203[14].append('ШТ')
        umumiy_without_duplicate1203[15].append('999')
        umumiy_without_duplicate1203[16].append('X')
        umumiy_without_duplicate1203[17].append('0000')
        umumiy_without_duplicate1203[18].append('PD')
        umumiy_without_duplicate1203[19].append('EX')
        umumiy_without_duplicate1203[20].append('0')
        umumiy_without_duplicate1203[21].append('E')
        ss =''
        sartrr =''
        if gruppa_material =='PVCGP':
            ss ='S400'
            sartrr ='5'
            
        bklast ='0100'
        if gruppa_material =='PVCPF':
            bklast ='0102'
            
            
        umumiy_without_duplicate1203[22].append(ss)
        umumiy_without_duplicate1203[23].append('')
        umumiy_without_duplicate1203[24].append('M')
        umumiy_without_duplicate1203[25].append('02')
        umumiy_without_duplicate1203[26].append('26')
        umumiy_without_duplicate1203[27].append(sartrr)
        umumiy_without_duplicate1203[28].append('X')
        umumiy_without_duplicate1203[29].append('5')
        umumiy_without_duplicate1203[30].append('Z_SAP_PP_002')
        umumiy_without_duplicate1203[31].append('4')
        umumiy_without_duplicate1203[32].append('SAP999')
        umumiy_without_duplicate1203[33].append('26')
        umumiy_without_duplicate1203[34].append('1203')
        umumiy_without_duplicate1203[35].append('3')
        umumiy_without_duplicate1203[36].append(bklast)
        umumiy_without_duplicate1203[37].append('S')
        umumiy_without_duplicate1203[38].append('1')
        umumiy_without_duplicate1203[39].append(row['Price'])
        umumiy_without_duplicate1203[40].append('1203')
        umumiy_without_duplicate1203[41].append('X')
        umumiy_without_duplicate1203[42].append('X')
        umumiy_without_duplicate1203[43].append('1')
        
        if row['Тип покрытия'] =='Ламинированный':
            if '-7' in row['SAP код S4P 100']:
                sap_code_simvol ='7L'
            else:
                sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
        else:
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]

        umumiy_without_duplicate1203[44].append(SFSPF1203[sap_code_simvol])
        umumiy_without_duplicate1203[45].append('X')
        umumiy_without_duplicate1203[46].append(LGPRO1203[sap_code_simvol])
        umumiy_without_duplicate1203[47].append('')
        umumiy_without_duplicate1203[48].append(row['combination'] + row['Тип покрытия'])
            
        if gruppa_material=='PVCGP':
            #######12D1
            umumiy_without_duplicate12D1[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D1[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D1[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D1[3].append('ШТ')
            umumiy_without_duplicate12D1[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='PVCGP'
            else:
                gruppa_material ='PVCPF'
            umumiy_without_duplicate12D1[5].append(gruppa_material)
            umumiy_without_duplicate12D1[6].append(row['sb'])
            umumiy_without_duplicate12D1[7].append('E')
            umumiy_without_duplicate12D1[8].append('02')
            umumiy_without_duplicate12D1[9].append(row['Brutto'])
            umumiy_without_duplicate12D1[10].append(row['Netto'])
            umumiy_without_duplicate12D1[11].append('КГ')
            umumiy_without_duplicate12D1[12].append('NORM')
            umumiy_without_duplicate12D1[13].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D1[14].append('ШТ')
            umumiy_without_duplicate12D1[15].append('999')
            umumiy_without_duplicate12D1[16].append('X')
            umumiy_without_duplicate12D1[17].append('0000')
            umumiy_without_duplicate12D1[18].append('PD')
            umumiy_without_duplicate12D1[19].append('EX')
            umumiy_without_duplicate12D1[20].append('0')
            umumiy_without_duplicate12D1[21].append('E')
            
            sartrr =''
            if gruppa_material =='PVCGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='PVCPF':
                bklast ='0102'
                
                
            umumiy_without_duplicate12D1[22].append('D100')
            umumiy_without_duplicate12D1[23].append('')
            umumiy_without_duplicate12D1[24].append('M')
            umumiy_without_duplicate12D1[25].append('02')
            umumiy_without_duplicate12D1[26].append('10')
            umumiy_without_duplicate12D1[27].append(sartrr)
            umumiy_without_duplicate12D1[28].append('X')
            umumiy_without_duplicate12D1[29].append('5')
            umumiy_without_duplicate12D1[30].append('Z_SAP_PP_002')
            umumiy_without_duplicate12D1[31].append('4')
            umumiy_without_duplicate12D1[32].append('SAP999')
            umumiy_without_duplicate12D1[33].append('10')
            umumiy_without_duplicate12D1[34].append('12D1')
            umumiy_without_duplicate12D1[35].append('3')
            umumiy_without_duplicate12D1[36].append(bklast)
            umumiy_without_duplicate12D1[37].append('S')
            umumiy_without_duplicate12D1[38].append('1')
            umumiy_without_duplicate12D1[39].append(row['Price'])
            umumiy_without_duplicate12D1[40].append('1203')
            umumiy_without_duplicate12D1[41].append('X')
            umumiy_without_duplicate12D1[42].append('X')
            umumiy_without_duplicate12D1[43].append('1')
            umumiy_without_duplicate12D1[44].append('')
            umumiy_without_duplicate12D1[45].append('X')
            umumiy_without_duplicate12D1[46].append('')
            umumiy_without_duplicate12D1[47].append('X')
            umumiy_without_duplicate12D1[48].append(row['combination'] + row['Тип покрытия'])
            
        if gruppa_material=='PVCGP':
            ######12D2
            umumiy_without_duplicate12D2[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D2[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D2[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D2[3].append('ШТ')
            umumiy_without_duplicate12D2[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='PVCGP'
            else:
                gruppa_material ='PVCPF'
            umumiy_without_duplicate12D2[5].append(gruppa_material)
            umumiy_without_duplicate12D2[6].append(row['sb'])
            umumiy_without_duplicate12D2[7].append('E')
            umumiy_without_duplicate12D2[8].append('02')
            umumiy_without_duplicate12D2[9].append(row['Brutto'])
            umumiy_without_duplicate12D2[10].append(row['Netto'])
            umumiy_without_duplicate12D2[11].append('КГ')
            umumiy_without_duplicate12D2[12].append('NORM')
            umumiy_without_duplicate12D2[13].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D2[14].append('ШТ')
            umumiy_without_duplicate12D2[15].append('999')
            umumiy_without_duplicate12D2[16].append('X')
            umumiy_without_duplicate12D2[17].append('0000')
            umumiy_without_duplicate12D2[18].append('PD')
            umumiy_without_duplicate12D2[19].append('EX')
            umumiy_without_duplicate12D2[20].append('0')
            umumiy_without_duplicate12D2[21].append('E')
            
            sartrr =''
            if gruppa_material =='PVCGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='PVCPF':
                bklast ='0102'
                
                
            umumiy_without_duplicate12D2[22].append('D100')
            umumiy_without_duplicate12D2[23].append('')
            umumiy_without_duplicate12D2[24].append('M')
            umumiy_without_duplicate12D2[25].append('02')
            umumiy_without_duplicate12D2[26].append('10')
            umumiy_without_duplicate12D2[27].append(sartrr)
            umumiy_without_duplicate12D2[28].append('X')
            umumiy_without_duplicate12D2[29].append('5')
            umumiy_without_duplicate12D2[30].append('Z_SAP_PP_002')
            umumiy_without_duplicate12D2[31].append('4')
            umumiy_without_duplicate12D2[32].append('SAP999')
            umumiy_without_duplicate12D2[33].append('10')
            umumiy_without_duplicate12D2[34].append('12D2')
            umumiy_without_duplicate12D2[35].append('3')
            umumiy_without_duplicate12D2[36].append(bklast)
            umumiy_without_duplicate12D2[37].append('S')
            umumiy_without_duplicate12D2[38].append('1')
            umumiy_without_duplicate12D2[39].append(row['Price'])
            umumiy_without_duplicate12D2[40].append('1203')
            umumiy_without_duplicate12D2[41].append('X')
            umumiy_without_duplicate12D2[42].append('X')
            umumiy_without_duplicate12D2[43].append('1')
            umumiy_without_duplicate12D2[44].append('')
            umumiy_without_duplicate12D2[45].append('X')
            umumiy_without_duplicate12D2[46].append('')
            umumiy_without_duplicate12D2[47].append('X')
            umumiy_without_duplicate12D2[48].append(row['combination'] + row['Тип покрытия'])
            
        if gruppa_material=='PVCGP':
            ######12D3
            umumiy_without_duplicate12D3[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D3[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D3[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D3[3].append('ШТ')
            umumiy_without_duplicate12D3[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='PVCGP'
            else:
                gruppa_material ='PVCPF'
            umumiy_without_duplicate12D3[5].append(gruppa_material)
            umumiy_without_duplicate12D3[6].append(row['sb'])
            umumiy_without_duplicate12D3[7].append('E')
            umumiy_without_duplicate12D3[8].append('02')
            umumiy_without_duplicate12D3[9].append(row['Brutto'])
            umumiy_without_duplicate12D3[10].append(row['Netto'])
            umumiy_without_duplicate12D3[11].append('КГ')
            umumiy_without_duplicate12D3[12].append('NORM')
            umumiy_without_duplicate12D3[13].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D3[14].append('ШТ')
            umumiy_without_duplicate12D3[15].append('999')
            umumiy_without_duplicate12D3[16].append('X')
            umumiy_without_duplicate12D3[17].append('0000')
            umumiy_without_duplicate12D3[18].append('PD')
            umumiy_without_duplicate12D3[19].append('EX')
            umumiy_without_duplicate12D3[20].append('0')
            umumiy_without_duplicate12D3[21].append('E')
            
            sartrr =''
            if gruppa_material =='PVCGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='PVCPF':
                bklast ='0102'
                
                
            umumiy_without_duplicate12D3[22].append('D100')
            umumiy_without_duplicate12D3[23].append('')
            umumiy_without_duplicate12D3[24].append('M')
            umumiy_without_duplicate12D3[25].append('02')
            umumiy_without_duplicate12D3[26].append('10')
            umumiy_without_duplicate12D3[27].append(sartrr)
            umumiy_without_duplicate12D3[28].append('X')
            umumiy_without_duplicate12D3[29].append('5')
            umumiy_without_duplicate12D3[30].append('Z_SAP_PP_002')
            umumiy_without_duplicate12D3[31].append('4')
            umumiy_without_duplicate12D3[32].append('SAP999')
            umumiy_without_duplicate12D3[33].append('10')
            umumiy_without_duplicate12D3[34].append('12D3')
            umumiy_without_duplicate12D3[35].append('3')
            umumiy_without_duplicate12D3[36].append(bklast)
            umumiy_without_duplicate12D3[37].append('S')
            umumiy_without_duplicate12D3[38].append('1')
            umumiy_without_duplicate12D3[39].append(row['Price'])
            umumiy_without_duplicate12D3[40].append('1203')
            umumiy_without_duplicate12D3[41].append('X')
            umumiy_without_duplicate12D3[42].append('X')
            umumiy_without_duplicate12D3[43].append('1')
            umumiy_without_duplicate12D3[44].append('')
            umumiy_without_duplicate12D3[45].append('X')
            umumiy_without_duplicate12D3[46].append('')
            umumiy_without_duplicate12D3[47].append('X')
            umumiy_without_duplicate12D3[48].append(row['combination'] + row['Тип покрытия'])
        
        if gruppa_material=='PVCGP':
            ######12D4
            umumiy_without_duplicate12D4[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D4[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D4[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D4[3].append('ШТ')
            umumiy_without_duplicate12D4[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='PVCGP'
            else:
                gruppa_material ='PVCPF'
            umumiy_without_duplicate12D4[5].append(gruppa_material)
            umumiy_without_duplicate12D4[6].append(row['sb'])
            umumiy_without_duplicate12D4[7].append('E')
            umumiy_without_duplicate12D4[8].append('02')
            umumiy_without_duplicate12D4[9].append(row['Brutto'])
            umumiy_without_duplicate12D4[10].append(row['Netto'])
            umumiy_without_duplicate12D4[11].append('КГ')
            umumiy_without_duplicate12D4[12].append('NORM')
            umumiy_without_duplicate12D4[13].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D4[14].append('ШТ')
            umumiy_without_duplicate12D4[15].append('999')
            umumiy_without_duplicate12D4[16].append('X')
            umumiy_without_duplicate12D4[17].append('0000')
            umumiy_without_duplicate12D4[18].append('PD')
            umumiy_without_duplicate12D4[19].append('EX')
            umumiy_without_duplicate12D4[20].append('0')
            umumiy_without_duplicate12D4[21].append('E')
            
            sartrr =''
            if gruppa_material =='PVCGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='PVCPF':
                bklast ='0102'
                
                
            umumiy_without_duplicate12D4[22].append('D100')
            umumiy_without_duplicate12D4[23].append('')
            umumiy_without_duplicate12D4[24].append('M')
            umumiy_without_duplicate12D4[25].append('02')
            umumiy_without_duplicate12D4[26].append('10')
            umumiy_without_duplicate12D4[27].append(sartrr)
            umumiy_without_duplicate12D4[28].append('X')
            umumiy_without_duplicate12D4[29].append('5')
            umumiy_without_duplicate12D4[30].append('Z_SAP_PP_002')
            umumiy_without_duplicate12D4[31].append('4')
            umumiy_without_duplicate12D4[32].append('SAP999')
            umumiy_without_duplicate12D4[33].append('10')
            umumiy_without_duplicate12D4[34].append('12D4')
            umumiy_without_duplicate12D4[35].append('3')
            umumiy_without_duplicate12D4[36].append(bklast)
            umumiy_without_duplicate12D4[37].append('S')
            umumiy_without_duplicate12D4[38].append('1')
            umumiy_without_duplicate12D4[39].append(row['Price'])
            umumiy_without_duplicate12D4[40].append('1203')
            umumiy_without_duplicate12D4[41].append('X')
            umumiy_without_duplicate12D4[42].append('X')
            umumiy_without_duplicate12D4[43].append('1')
            umumiy_without_duplicate12D4[44].append('')
            umumiy_without_duplicate12D4[45].append('X')
            umumiy_without_duplicate12D4[46].append('')
            umumiy_without_duplicate12D4[47].append('X')
            umumiy_without_duplicate12D4[48].append(row['combination'] + row['Тип покрытия'])
            
        if gruppa_material=='PVCGP':
            ######12D5
            umumiy_without_duplicate12D5[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D5[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D5[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D5[3].append('ШТ')
            umumiy_without_duplicate12D5[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='PVCGP'
            else:
                gruppa_material ='PVCPF'
            umumiy_without_duplicate12D5[5].append(gruppa_material)
            umumiy_without_duplicate12D5[6].append(row['sb'])
            umumiy_without_duplicate12D5[7].append('E')
            umumiy_without_duplicate12D5[8].append('02')
            umumiy_without_duplicate12D5[9].append(row['Brutto'])
            umumiy_without_duplicate12D5[10].append(row['Netto'])
            umumiy_without_duplicate12D5[11].append('КГ')
            umumiy_without_duplicate12D5[12].append('NORM')
            umumiy_without_duplicate12D5[13].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D5[14].append('ШТ')
            umumiy_without_duplicate12D5[15].append('999')
            umumiy_without_duplicate12D5[16].append('X')
            umumiy_without_duplicate12D5[17].append('0000')
            umumiy_without_duplicate12D5[18].append('PD')
            umumiy_without_duplicate12D5[19].append('EX')
            umumiy_without_duplicate12D5[20].append('0')
            umumiy_without_duplicate12D5[21].append('E')
            
            sartrr =''
            if gruppa_material =='PVCGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='PVCPF':
                bklast ='0102'
                
                
            umumiy_without_duplicate12D5[22].append('D100')
            umumiy_without_duplicate12D5[23].append('')
            umumiy_without_duplicate12D5[24].append('M')
            umumiy_without_duplicate12D5[25].append('02')
            umumiy_without_duplicate12D5[26].append('10')
            umumiy_without_duplicate12D5[27].append(sartrr)
            umumiy_without_duplicate12D5[28].append('X')
            umumiy_without_duplicate12D5[29].append('5')
            umumiy_without_duplicate12D5[30].append('Z_SAP_PP_002')
            umumiy_without_duplicate12D5[31].append('4')
            umumiy_without_duplicate12D5[32].append('SAP999')
            umumiy_without_duplicate12D5[33].append('10')
            umumiy_without_duplicate12D5[34].append('12D5')
            umumiy_without_duplicate12D5[35].append('3')
            umumiy_without_duplicate12D5[36].append(bklast)
            umumiy_without_duplicate12D5[37].append('S')
            umumiy_without_duplicate12D5[38].append('1')
            umumiy_without_duplicate12D5[39].append(row['Price'])
            umumiy_without_duplicate12D5[40].append('1203')
            umumiy_without_duplicate12D5[41].append('X')
            umumiy_without_duplicate12D5[42].append('X')
            umumiy_without_duplicate12D5[43].append('1')
            umumiy_without_duplicate12D5[44].append('')
            umumiy_without_duplicate12D5[45].append('X')
            umumiy_without_duplicate12D5[46].append('')
            umumiy_without_duplicate12D5[47].append('X')
            umumiy_without_duplicate12D5[48].append(row['combination'] + row['Тип покрытия'])
            
        
    umumiy_without_duplicate =[[] for i in range(0,49)]
            
    for i in range(0,len(umumiy_without_duplicate1203)):
        umumiy_without_duplicate[i]+=umumiy_without_duplicate1203[i] 
            
    for i in range(0,len(umumiy_without_duplicate12D1)):
        umumiy_without_duplicate[i]+=umumiy_without_duplicate12D1[i]
             
    for i in range(0,len(umumiy_without_duplicate12D2)):
        umumiy_without_duplicate[i]+=umumiy_without_duplicate12D2[i]
             
    for i in range(0,len(umumiy_without_duplicate12D3)):
        umumiy_without_duplicate[i]+=umumiy_without_duplicate12D3[i]
             
    for i in range(0,len(umumiy_without_duplicate12D4)):
        umumiy_without_duplicate[i]+=umumiy_without_duplicate12D4[i]
             
    for i in range(0,len(umumiy_without_duplicate12D5)):
        umumiy_without_duplicate[i]+=umumiy_without_duplicate12D5[i]     


    
    ######################### Бухгалтерская название.txt ##############################
    
    buxgalterskiy_t ={}
    header_buxgalter ='ID\tMATNR\tVKORG\tVTWEG\tLANG\tTDID\tPOS\tLTEXT'
    buxgalterskiy_t['ID']=buxgalterskiy_naz[0]       
    buxgalterskiy_t['MATNR']=buxgalterskiy_naz[1] 
    buxgalterskiy_t['VKORG']=buxgalterskiy_naz[2] 
    buxgalterskiy_t['VTWEG']=buxgalterskiy_naz[3] 
    buxgalterskiy_t['LANG']=buxgalterskiy_naz[4]         
    buxgalterskiy_t['TDID']=buxgalterskiy_naz[5]         
    buxgalterskiy_t['POS']=buxgalterskiy_naz[6]        
    buxgalterskiy_t['LTEXT']=buxgalterskiy_naz[7] 
    df_bug_text= pd.DataFrame(buxgalterskiy_t)
    
    np.savetxt(pathtext8, df_bug_text.values,fmt='%s', delimiter="\t",header=header_buxgalter,comments='',encoding='ansi')
        
        
    ########################## end Бухгалтерская название.txt ##############################
    ########################## Длинный текс.txt ##############################
    #dlinniy_text_zero
    dlinniy_t ={}
    header_dlinniy ='\tBISMT\t\t\t\tTEXT'
    dlinniy_t['ID']=dlinniy_text_zero[0] 
    dlinniy_t['BISMT']=dlinniy_text_zero[1] 
    dlinniy_t['RU']=['RU' for x in (dlinniy_text_zero[1])] 
    dlinniy_t['GRUN']=['GRUN' for x in (dlinniy_text_zero[1])]
    dlinniy_t['sa']=['' for x in (dlinniy_text_zero[1])]
    dlinniy_t['TEXT']=dlinniy_text_zero[2]
    
    df_dlinniy_text = pd.DataFrame(dlinniy_t)
    
    np.savetxt(pathtext7, df_dlinniy_text.values,fmt='%s', delimiter="\t",header=header_dlinniy,comments='',encoding='ansi')
        
        
    ########################## end Длинный текс.txt ##############################


    ########################## 1.txt ##############################
    d1 = {}
    header1 = 'MATNR\tBISMT\tMAKTX\tMEINS\tMTART\tMATKL\tWERKS\tBESKZ\tSPART\tBRGEW\tNTGEW\tGEWEI\tMTPOS_MARA'
    
    d1['MATNR']=umumiy_without_duplicate1203[0] 
    d1['BISMT']=umumiy_without_duplicate1203[1] 
    d1['MAKTX']=umumiy_without_duplicate1203[2] 
    d1['MEINS']=umumiy_without_duplicate1203[3] 
    d1['MTART']=umumiy_without_duplicate1203[4] 
    d1['MATKL']=umumiy_without_duplicate1203[5] 
    d1['WERKS']=umumiy_without_duplicate1203[34] 
    d1['BESKZ']=umumiy_without_duplicate1203[7] 
    d1['SPART']=umumiy_without_duplicate1203[8]
    d1['BRGEW']=[str(round(float(k1.replace(',','.')),3)).replace('.',',') if isinstance(k1,str) else str(round(k1,3)).replace('.',',') for k1 in (umumiy_without_duplicate1203[9])]
    d1['NTGEW']=[str(round(float(k2.replace(',','.')),3)).replace('.',',') for k2 in (umumiy_without_duplicate1203[10])]
    d1['GEWEI']=umumiy_without_duplicate1203[11]
    d1['MTPOS_MARA']=umumiy_without_duplicate1203[12]
    
    
    df1= pd.DataFrame(d1)

    
    
    
    np.savetxt(pathtext1, df1.values,fmt='%s', delimiter="\t",header=header1,comments='',encoding='ansi')
        
    ########################## end 1.txt ##############################

    ########################## 2.txt ##############################
    header2='MAKTX\tMEINS\tMTART\tMATNR\tWERKS\tEKGRP\tXCHPF\tDISGR\tDISMM\tDISPO\tDISLS\tWEBAZ\tBESKZ\tLGFSB\tPLIFZ\tPERKZ\tMTVFP\tSCM_STRA1\tVRMOD\tPPSKZ\tSCM_WHATBOM\tSCM_HEUR_ID\tSCM_RRP_TYPE\tSCM_PROFID\tSTRGR\tBWKEY\tMLAST\tBKLAS\tVPRSV\tPEINH\tSTPRS\tPRCTR\tEKALR\tHKMAT\tLOSGR\tSFCPF\tFEVOR\tUEETK\tLGPRO\tAUTO_P_ORD'
    zavod_code ={
        '1203':'PVC',
        '12D1':'001',
        '12D2':'001',
        '12D3':'001',
        '12D4':'001',
        '12D5':'001',
    }
    d2={}
    d2['MAKTX']=umumiy_without_duplicate[13] 
    d2['MEINS']=umumiy_without_duplicate[14] 
    d2['MTART']=umumiy_without_duplicate[4] 
    d2['MATNR']=umumiy_without_duplicate[0] 
    d2['WERKS']=umumiy_without_duplicate[34]
    d2['EKGRP']=umumiy_without_duplicate[15]
    d2['XCHPF']=umumiy_without_duplicate[16]
    d2['DISGR']=umumiy_without_duplicate[17]
    d2['DISMM']=umumiy_without_duplicate[18]
    d2['DISPO']=[zavod_code[x] for x in umumiy_without_duplicate[34] ]
    d2['DISLS']=umumiy_without_duplicate[19]
    d2['WEBAZ']=umumiy_without_duplicate[20] 
    d2['BESKZ']=umumiy_without_duplicate[21]
    d2['LGFSB']=umumiy_without_duplicate[22]
    d2['PLIFZ']=umumiy_without_duplicate[23]
    d2['PERKZ']=umumiy_without_duplicate[24]
    d2['MTVFP']=umumiy_without_duplicate[25]
    d2['SCM_STRA1']=umumiy_without_duplicate[26]
    d2['VRMOD']=umumiy_without_duplicate[27] 
    d2['PPSKZ']=umumiy_without_duplicate[28] 
    d2['SCM_WHATBOM']=umumiy_without_duplicate[29]
    d2['SCM_HEUR_ID']=umumiy_without_duplicate[30]
    d2['SCM_RRP_TYPE']=umumiy_without_duplicate[31]
    d2['SCM_PROFID']=umumiy_without_duplicate[32] 
    d2['STRGR']=umumiy_without_duplicate[33]
    d2['BWKEY']=umumiy_without_duplicate[34]
    d2['MLAST']=umumiy_without_duplicate[35]
    d2['BKLAS']=umumiy_without_duplicate[36]
    d2['VPRSV']=umumiy_without_duplicate[37]
    d2['PEINH']=umumiy_without_duplicate[38]
    d2['STPRS']=[round(float(n.replace(',','.')),2) for n in (umumiy_without_duplicate[39] )]
    d2['PRCTR']=umumiy_without_duplicate[40] 
    d2['EKALR']=umumiy_without_duplicate[41] 
    d2['HKMAT']=umumiy_without_duplicate[42] 
    d2['LOSGR']=umumiy_without_duplicate[43] 
    d2['SFCPF']=umumiy_without_duplicate[44] 
    d2['FEVOR']=['AP1' for x in (umumiy_without_duplicate[44])] 
    d2['UEETK']=umumiy_without_duplicate[45] 
    d2['LGPRO']=umumiy_without_duplicate[46] 
    d2['AUTO_P_ORD']=umumiy_without_duplicate[47] 

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
    VTWEG = ['99','10','20']
   
    for i in range(0,3):
        d3['MAKTX'] += umumiy_without_duplicate[13] 
        d3['MEINS'] += umumiy_without_duplicate[14] 
        d3['MTART'] += umumiy_without_duplicate[4] 
        d3['SPART'] += umumiy_without_duplicate[8] 
        d3['MATNR'] += umumiy_without_duplicate[0] 
        d3['WERKS'] += umumiy_without_duplicate[34] 
        d3['VKORG'] += [ 1200 for j in range(0,len(umumiy_without_duplicate[13] ))]
        d3['MTPOS'] += umumiy_without_duplicate[12] 
        d3['VTWEG'] += [ VTWEG[i] for j in range(0,len(umumiy_without_duplicate[13] ))]
        d3['PRCTR'] += [ '1203' if umumiy_without_duplicate[34][i] =='1203' else '1203' for i in range(0,len(umumiy_without_duplicate[34]))] 
        d3['MTVFP'] += [ '02' for j in range(0,len(umumiy_without_duplicate[13] ))]
        d3['ALAND'] += [ 'UZ' for j in range(0,len(umumiy_without_duplicate[13]))] 
        d3['TATYP'] += [ 'MWST' for j in range(0,len(umumiy_without_duplicate[13]))] 
        d3['TAXKM'] += [ '1' for j in range(0,len(umumiy_without_duplicate[13]))] 
        d3['VERSG'] += [ '1' for j in range(0,len(umumiy_without_duplicate[13] ))]
        d3['KTGRM'] += [ '01' for j in range(0,len(umumiy_without_duplicate[13]))]
        if i!=2:
            d3['KONDM'] +=['01' for x in range(len(umumiy_without_duplicate[6]))]
        else:
            d3['KONDM'] +=umumiy_without_duplicate[6]
            
        d3['LADGR'] += [ '0001' for j in range(0,len(umumiy_without_duplicate[13]))] 
        d3['TRAGR'] += [ '0001' for j in range(0,len(umumiy_without_duplicate[13]))] 
        
    df3= pd.DataFrame(d3)
    df3 = df3[(df3['MATNR'].str.contains('-E') & (df3['VTWEG'] =='99')|(~df3['MATNR'].str.contains('-E')))]
    
    np.savetxt(pathtext3, df3.values, fmt='%s', delimiter="\t",header=header3,comments='',encoding='ansi')
    ########################## end 3.txt ##############################
        
    ########################## 4.txt ##############################    
    new_ll =[[],[],[]]
    sap_code_title =[]
    dlina_title =[]
    obshiy_ves_za_shtuku =[]
    netto = []
    wms_width =[]
    wms_height =[]
    
    for key , row in datas.iterrows():
        row['Длина'] = (row['Длина']).replace('.0','')
        sap_code_title.append(row['SAP код S4P 100'])
        netto.append(float(row['Netto']))
        dlina_title.append(row['Длина'])
        obshiy_ves_za_shtuku.append(1)
        wms_width.append(row['WMS_WIDTH'])
        wms_height.append(row['WMS_HEIGHT'])

        
        sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]        
        if sap_code_simvol =='E':
            for i in range(0,len(LGORT['E'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT['E'][i]['zavod_code'])
                new_ll[2].append(LGORT['E'][i]['zavod_sap'])
        
        
        if sap_code_simvol =='7':
            if (row['Тип покрытия'] =='Ламинированный'):
                for i in range(0,len(LGORT['7L'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['7L'][i]['zavod_code'])
                    new_ll[2].append(LGORT['7L'][i]['zavod_sap'])
            else:
                for i in range(0,len(LGORT['7'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['7'][i]['zavod_code'])
                    new_ll[2].append(LGORT['7'][i]['zavod_sap'])
        
       

    header4 = 'MATNR\tWERKS\tLGORT'
    d4={}
    d4['MATNR']= new_ll[0] 
    d4['WERKS']= new_ll[1] 
    d4['LGORT']= new_ll[2] 
    # d4['RAUBE']= ['' for x in new_ll[2]]
    df4 = pd.DataFrame(d4)
    np.savetxt(pathtext4, df4.values, fmt='%s', delimiter="\t",header=header4,comments='',encoding='ansi')
    ########################## end 4.txt ##############################

    ########################## 55.txt ##############################    
    new_ll_55 =[[],[],[]]
    
    for key , row in datas.iterrows():
        sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]        
        
        if sap_code_simvol =='7':
            if (row['Тип покрытия'] =='Ламинированный'):
                for i in range(0,len(LGORT['7L'])):
                    new_ll_55[0].append(row['SAP код S4P 100'])
                    new_ll_55[1].append(LGORT['7L'][i]['zavod_code'])
                    new_ll_55[2].append(LGORT['7L'][i]['zavod_sap'])
            else:
                for i in range(0,len(LGORT['7'])):
                    new_ll_55[0].append(row['SAP код S4P 100'])
                    new_ll_55[1].append(LGORT['7'][i]['zavod_code'])
                    new_ll_55[2].append(LGORT['7'][i]['zavod_sap'])

    header55='MATNR\tWERKS\tRAUBE'
    d55={}
    d55['MATNR'] = new_ll_55[0] 
    d55['WERKS'] = new_ll_55[1] 
    # d55['LGORT'] = new_ll_55[2] 
    d55['RAUBE'] = ['' for x in new_ll_55[2]] 
    df55 = pd.DataFrame(d55)
    np.savetxt(pathtext55, df55.values, fmt='%s', delimiter="\t",header=header55,comments='',encoding='ansi')
    ########################## end 55.txt ##############################
        
    ########################## 5.txt ##############################
    d5 ={
        'sap_code':[],
        'ed_iz1':[],
        'ed_iz3':[],
        'ed_iz2':[],
        'ed_iz4':[],
        'ed_iz5':[],
        'ed_iz6':[],
        'ed_iz7':[]
    }
    ED_IZM =['ШТ','М','КГ']
    
    ed_iz3 =[]
    for i in range(0,3):
        if i == 0 :
            ed_iz3 += ['1' for j in range(0,len(sap_code_title)) ]
        elif i == 1 :
            ed_iz3 += [j for j in dlina_title ]
        elif i == 2 :
            ed_iz3 += [int(float(j)*1000) for j in obshiy_ves_za_shtuku ]
            
    
    for i in ED_IZM:    
        d5['sap_code'] += sap_code_title 
        d5['ed_iz1'] += [ i for j in range(0,len(sap_code_title))]
        d5['ed_iz2'] +=['1' if i =='ШТ' else '1000' if i=='М' else float(netto[j])*1000 for j in range(0,len(sap_code_title)) ]
        d5['ed_iz4'] +=[j for j in dlina_title ]
        d5['ed_iz5'] +=[j for j in wms_width ]
        d5['ed_iz6'] +=[j for j in wms_height ]
        d5['ed_iz7'] +=[ 'мм' for j in range(0,len(sap_code_title))]
    

    d5['ed_iz3'] = ed_iz3 
    df5 = pd.DataFrame(d5)
    np.savetxt(pathtext5, df5.values, fmt='%s', delimiter="\t",encoding='ansi')
    ########################## end 5.txt ##############################
    ########################## List v 3 ##############################
    dd2 = [[],[],[],[],[],[]]
 
    

    for key , row in datas.iterrows():
        
        row['tnved'] =str(row['tnved']).replace('.0','')
        row['amount_in_a_package'] =str(row['amount_in_a_package']).replace('.0','')
        row['wms_width'] =str(row['wms_width']).replace('.0','')
        row['wms_height'] =str(row['wms_height']).replace('.0','')
        row['number_of_chambers'] =str(row['number_of_chambers']).replace('.0','')
        row['length'] =str(row['length']).replace('.0','')

        if '-7' in row['SAP код S4P 100']:
            for j in range(0,25):
                dd2[0].append('001')
            
            for j in range(0,25):
                if HEADER2[j] not in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT','TNVED']:
                    dd2[1].append('PVC_PROFILE')
                else:
                    if HEADER2[j] in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT']:
                        dd2[1].append('RAWMAT_TYPE')
                    elif HEADER2[j] =='TNVED':
                        dd2[1].append('TNVED')
                
            for j in range(0,25):
                dd2[2].append('MARA')
                
            for j in range(0,25):
                dd2[3].append(row['SAP код S4P 100'])
                
            for j in HEADER2:
                dd2[4].append(j)

            id_savdo = row['id_savdo']

            dd2[5].append(row['system'])
            dd2[5].append(row['number_of_chambers'])
            dd2[5].append(row['article'])
            dd2[5].append(row['profile_type_id'])
            dd2[5].append(row['length'])
            dd2[5].append(row['surface_treatment'])
            dd2[5].append(row['outer_side_pc_id'])
            dd2[5].append(row['outer_side_wg_id'])
            dd2[5].append(row['inner_side_wg_id'])
            dd2[5].append(row['sealer_color'])
            dd2[5].append(row['print_view'])
            dd2[5].append(row['width'])
            dd2[5].append(row['height'])
            dd2[5].append(row['category'])
            dd2[5].append(row['material_class'])
            dd2[5].append(row['rawmat_type'])
            dd2[5].append(row['tnved'])
            dd2[5].append(row['surface_treatment_export'])
            dd2[5].append(row['amount_in_a_package'])
            dd2[5].append(row['wms_width'])
            dd2[5].append(row['wms_height'])
            dd2[5].append(row['product_type'])
            dd2[5].append(row['profile_type'])
            dd2[5].append(row['coating_qbic'])
            dd2[5].append(row['id_savdo'])
        else:
            for j in range(0,21):
                dd2[0].append('001')
            
            for j in range(0,21):
                if HEADER[j] not in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT','TNVED']:
                    dd2[1].append('PVC_PROFILE')
                else:
                    if HEADER[j] in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT']:
                        dd2[1].append('RAWMAT_TYPE')
                    elif HEADER[j] =='TNVED':
                        dd2[1].append('TNVED')
                
            for j in range(0,21):
                dd2[2].append('MARA')
                
            for j in range(0,21):
                dd2[3].append(row['SAP код S4P 100'])
                
            for j in HEADER:
                dd2[4].append(j)


            dd2[5].append(row['system'])
            dd2[5].append(row['number_of_chambers'])
            dd2[5].append(row['article'])
            dd2[5].append(row['profile_type_id'])
            dd2[5].append(row['length'])
            dd2[5].append(row['surface_treatment'])
            dd2[5].append(row['outer_side_pc_id'])
            dd2[5].append('NR')
            dd2[5].append(row['print_view'])
            dd2[5].append(row['width'])
            dd2[5].append(row['height'])
            dd2[5].append(row['category'])
            dd2[5].append(row['material_class'])
            dd2[5].append(row['rawmat_type'])
            dd2[5].append(row['tnved'])
            dd2[5].append(row['surface_treatment_export'])
            dd2[5].append(row['amount_in_a_package'])
            dd2[5].append(row['wms_width'])
            dd2[5].append(row['wms_height'])
            dd2[5].append(row['product_type'])
            dd2[5].append(row['profile_type'])


    new_date={}       
    new_date['Вид класса'] = dd2[0] 
    new_date['Класс'] = dd2[1] 
    new_date['Таблица'] = dd2[2] 
    new_date['Объект'] = dd2[3] 
    new_date['Имя признака'] = dd2[4] 
    new_date['Значение признака'] = dd2[5] 
    new_date['Статус загрузки'] = ['' for x in dd2[5] ] 
    
    
    ddf2 = pd.DataFrame(new_date)
    ddf2 = ddf2[((ddf2["Значение признака"] != "nan") & (ddf2["Значение признака"] != ""))]
    ddf2 = ddf2.replace('XXXXX','')
    ddf2.to_excel(pathtext6,index=False)

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





def create_folder(parent_dir,directory):
    path =os.path.join(parent_dir,directory)
    if not os.path.isdir(path):
        os.mkdir(path)


def create_characteristika_utils(items):
    df =[
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[]
    ]
    
    
    for item in items:
        if '-L' in item['sap_code']:
            continue
        
        ед_изм ='ШТ'
        альтернативная_ед_изм='КГ'
       
        tip_pokritiya = item['surface_treatment']
        wms_width = item['wms_width'].replace('.0','')
        wms_height =    item['wms_height'].replace('.0','')
        
        ########Characteristica variables############
        
        
        
        ########End Characteristica variables############

       
        df[0].append(item['sap_code'])
        df[1].append('')
        df[2].append(item['kratkiy'])
        df[3].append('1')

        df[4].append(ед_изм)
        df[5].append(альтернативная_ед_изм)
        df[6].append('')
        df[9].append(item['length'])
        df[10].append(item['width'])
        df[11].append(item['height'])
        df[12].append('')
        df[13].append('')
        df[14].append('')
        df[15].append('')
        df[16].append(item['surface_treatment'])
        df[17].append(item['wms_width'])
        df[18].append(item['wms_height'])
        
        df[19].append(item['sap_code'])
        df[20].append(item['system'])
        df[21].append(item['number_of_chambers'])
        df[22].append(item['article'])
        df[23].append(item['profile_type_id'])
        df[24].append(item['length'])
        df[25].append(item['surface_treatment'])
        df[26].append(item['outer_side_pc_id'])
        df[27].append(item['outer_side_wg_id'])
        df[28].append(item['inner_side_wg_id'])
        df[29].append(item['sealer_color'])
        df[30].append(item['print_view'])
        df[31].append(item['width'])
        df[32].append(item['height'])
        df[33].append(item['category'])
        df[34].append(item['material_class'])
        df[35].append(item['rawmat_type'])
        df[36].append(item['tnved'])
        df[37].append(item['surface_treatment_export'])
        df[38].append(item['amount_in_a_package'])
        df[39].append(item['wms_width'])
        df[40].append(item['wms_height'])
        df[41].append(item['product_type'])
        df[42].append(item['profile_type'])
        df[43].append(item['coating_qbic'])
        # df[44].append(item['id_savdo'])
        df[45].append(item['export_description'])
        df[46].append(item['export_description_eng'])
        df[47].append(item['sb'])
        df[48].append('')

        df[49].append(item['online_savdo_name'])
        df[50].append(item['id_savdo'])
        dlinniy_text =''
        if item['sealer_color'] =='' or item['sealer_color'] =='nan':
            sealor_color =''
        else:
            sealor_color = item['sealer_color'] +'-'

        if item['surface_treatment'].lower()=='неламинированный' and (item['outer_side_wg_id']!='' or item['outer_side_wg_id']!='nan') :
            dlinniy_text =item['dlinniy_text'] + ', ' +'артикул ' + item['article'] +', ' + item['surface_treatment'] +', цвет '+ item['outer_side_wg_id'] + ', длина ' + item['length'] + ' мм. Тип ' + item['outer_side_pc_id'] +'-'+ sealor_color +item['print_view']
        elif item['surface_treatment'].lower()=='неламинированный' and (item['outer_side_wg_id']=='' or item['outer_side_wg_id']=='nan'):
            dlinniy_text =item['dlinniy_text'] + ', ' +'артикул ' + item['article'] +', ' + item['surface_treatment'] +', цвет белый, длина ' + item['length'] + ' мм. Тип ' + item['outer_side_pc_id'] +'-'+ sealor_color + item['print_view']
        elif item['surface_treatment'].lower()=='ламинированный':
            if item['outer_side_wg_id'] != item['inner_side_wg_id']:   
                dlinniy_text =item['dlinniy_text'] + ', ' +'артикул ' + item['article'] +', ' + item['surface_treatment'] +', цвет '+ item['outer_side_wg_id'] +'/'+item['inner_side_wg_id']+ ', длина ' + item['length'] + ' мм. Тип ' + item['outer_side_pc_id'] +'-'+sealor_color + item['print_view']
            else:
                dlinniy_text =item['dlinniy_text'] + ', ' +'артикул ' + item['article'] +', ' + item['surface_treatment'] +', цвет '+ item['outer_side_wg_id'] + ', длина ' + item['length'] + ' мм. Тип ' + item['outer_side_pc_id'] +'-'+sealor_color + item['print_view']
        
        df[51].append(dlinniy_text)
        df[52].append(item['kod_lam_plen_snar'])
        df[53].append(item['kod_lam_plen_vnut'])

        

    dat = {
        'SAP код S4P 100':df[0],
        'Нумерация до SAP':df[1],
        'Короткое название SAP':df[2],
        'Польное наименование SAP':df[51],
        'Ед, Изм,':df[4],
        'Альтернативная ед, изм':df[5],
        'Коэфициент пересчета':df[6],
        # 'Участок':df[7],
        # 'Альтернативный участок':df[8],
        'Длина':df[9],
        'Ширина':df[10],
        'Высота':df[11],
        'группа материалов':df[12],
        'Brutto':df[13],
        'Netto':df[14],
        'Price':df[15],
        'Тип покрытия':df[16],
        'WMS_WIDTH':df[17],
        'WMS_HEIGHT':df[18],

        'sap_code' :df[19],
        'system' :df[20],
        'number_of_chambers' :df[21],
        'article' :df[22],
        'profile_type_id' :df[23],
        'length' :df[24],
        'surface_treatment' :df[25],
        'outer_side_pc_id' :df[26],
        'outer_side_wg_id' :df[27],
        'inner_side_wg_id' :df[28],
        'sealer_color' :df[29],
        'print_view' :df[30],
        'width' :df[31],
        'height' :df[32],
        'category' :df[33],
        'material_class' :df[34],
        'rawmat_type' :df[35],
        'tnved' :df[36],
        'surface_treatment_export' :df[37],
        'amount_in_a_package' :df[38],
        'wms_width' :df[39],
        'wms_height' :df[40],
        'product_type' :df[41],
        'profile_type' :df[42],
        'coating_qbic' :df[43],
        'export_description':df[45],
        'export_description_eng':df[46],
        'sb':df[47],
        'combination':df[48],
        'online_savdo_name' :df[49],
        'id_savdo' :df[50],
        'kod_lam_plen_snar' :df[52],
        'kod_lam_plen_vnut' :df[53]
        
    }
    
    df_new = pd.DataFrame(dat)
    

    return df_new



    

def create_characteristika(items):
    
    all_data = [
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[]
    ]
    # nakleyka_codes =[ code[0] for code in NakleykaCode.objects.values_list('name')]
    
    
    j=1 
    for item in items:
        j+=1
        
        character = Characteristika(
            sap_code = item['sap_code'],
            kratkiy = item['kratkiy'],
            system = item['system'], 
            number_of_chambers = item['number_of_chambers'], 
            article = item['article'], 
            profile_type_id = item['profile_type_id'], 
            length = item['length'], 
            surface_treatment = item['surface_treatment'], 
            outer_side_pc_id = item['outer_side_pc_id'], 
            outer_side_wg_id = item['outer_side_wg_id'], 
            inner_side_wg_id = item['inner_side_wg_id'], 
            sealer_color = item['sealer_color'], 
            print_view = item['print_view'], 
            width = item['width'], 
            height = item['height'], 
            category = item['category'], 
            material_class = item['material_class'], 
            rawmat_type = item['rawmat_type'], 
            tnved = item['tnved'], 
            surface_treatment_export = item['surface_treatment_export'], 
            amount_in_a_package = item['amount_in_a_package'], 
            wms_width = item['wms_width'], 
            wms_height = item['wms_height'], 
            product_type = item['product_type'], 
            profile_type = item['profile_type'], 
            coating_qbic = item['coating_qbic'], 
            id_savdo = item['id_savdo'], 
            online_savdo_name = item['online_savdo_name']
            )
        
        character.save()
        
        all_data[0].append(character.sap_code)
        all_data[1].append(character.system)
        all_data[2].append(character.number_of_chambers)
        all_data[3].append(character.article)
        all_data[4].append(character.profile_type_id)
        all_data[5].append(character.length)
        all_data[6].append(character.surface_treatment)
        all_data[7].append(character.outer_side_pc_id)
        all_data[8].append(character.outer_side_wg_id)
        all_data[9].append(character.inner_side_wg_id)
        all_data[10].append(character.sealer_color)
        all_data[11].append(character.print_view)
        all_data[12].append(character.width)
        all_data[13].append(character.height)
        all_data[14].append(character.category)
        all_data[15].append(character.material_class)
        all_data[16].append(character.rawmat_type)
        all_data[17].append(character.tnved)
        all_data[18].append(character.surface_treatment_export)
        all_data[19].append(character.amount_in_a_package)
        all_data[20].append(character.wms_width)
        all_data[21].append(character.wms_height)
        all_data[22].append(character.product_type)
        all_data[23].append(character.profile_type)
        all_data[24].append(character.coating_qbic)
        all_data[25].append(character.kratkiy)
        all_data[26].append(character.online_savdo_name)
        all_data[27].append(character.id_savdo)
        # all_data[28].append(character.kls_wast_length)
        # all_data[29].append(character.kls_wast)
        # all_data[30].append(character.ch_klaes_optm)
        # all_data[31].append(character.goods_group)
        
        



    df_new ={
        'SAP CODE':all_data[0],
        'KRATKIY TEXT':all_data[25],
        'SYSTEM':all_data[1],
        'NUMBER_OF_CHAMBERS':all_data[2],
        'ARTICLE':all_data[3],
        'PROFILE_TYPE_ID':all_data[4],
        'LENGTH':all_data[5],
        'SURFACE_TREATMENT':all_data[6],
        'OUTER_SIDE_PC_ID':all_data[7],
        'OUTER_SIDE_WG_ID':all_data[8],
        'INNER_SIDE_WG_ID':all_data[9],
        'SEALER_COLOR':all_data[10],
        'PRINT_VIEW':all_data[11],
        'WIDTH':all_data[12],
        'HEIGHT':all_data[13],
        'CATEGORY':all_data[14],
        'MATERIAL_CLASS':all_data[15],
        'RAWMAT_TYPE':all_data[16],
        'TNVED':all_data[17],
        'SURFACE_TREATMENT_EXPORT':all_data[18],
        'AMOUNT_IN_A_PACKAGE':all_data[19],
        'WMS_WIDTH':all_data[20],
        'WMS_HEIGHT':all_data[21],
        'PRODUCT_TYPE':all_data[22],
        'PROFILE_TYPE':all_data[23],
        'COATING_QBIC':all_data[24],
        'ONLINE_SAVDO_NAME':all_data[26],
        'ID_SAVDO':all_data[27],
        # 'CH_PROFILE_TYPE':all_data[27],
        # 'KLS_WAST_LENGTH':all_data[28],
        # 'KLS_WAST':all_data[29],
        # 'CH_KLAES_OPTM':all_data[30],
        # 'GOODS_GROUP':all_data[31]
    }
    
    df_charakter = pd.DataFrame(df_new)
    df_charakter =  df_charakter.replace('nan','')
    return df_charakter   

