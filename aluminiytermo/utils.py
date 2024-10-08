import os
from .models import Characteristika,CharacteristicTitle,NakleykaCode,CharUtilsThree
import random
from django.db.models import Count,Q
from datetime import datetime
from order.models import Order
from config.settings import MEDIA_ROOT
import pandas as pd
import numpy as np
from .BAZA import LGORT,HEADER,SFSPF1201,LGPRO1201,SFSPF1203,LGPRO1203,SFSPF1101,LGORT_1101,HEADER2,LGORT_1301,HEADER_1301
from django.shortcuts import render
from aluminiy.models import LengthOfProfile,RazlovkaTermo,AluProfilesData
from datetime import datetime
import math
import zipfile
from imzo.models import ExcelFilesImzo
from norma.models import Norma

def get_cretead_txt_for_1201(datas,elist,does_not_exists):
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M-%S MINUT")
    
    
    parent_dir =f'{MEDIA_ROOT}\\uploads\\TXT'
    
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads','TXT')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\TXT',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\TXT\\{year}',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}',hour)
    create_folder(f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}','BENKAM')
    create_folder(f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\BENKAM',minut)
    pathtext1 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\BENKAM\\{minut}\\1.txt'
    pathtext2 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\BENKAM\\{minut}\\2.txt'
    pathtext3 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\BENKAM\\{minut}\\3.txt'
    pathtext4 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\BENKAM\\{minut}\\4.txt'
    pathtext55 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\BENKAM\\{minut}\\5.txt'
    pathtext5 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\BENKAM\\{minut}\\Единицы изм.txt'
    pathtext6 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\BENKAM\\{minut}\\Лист в C 3.xlsx'
    pathtext7 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\BENKAM\\{minut}\\Длинный текс.txt'
    pathtext8 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\BENKAM\\{minut}\\Бух название SDLONGTEXT.txt'
    pathtext9 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\BENKAM\\{minut}\\ZMD_11_0008 - Прикрепление чертежей ОЗМ.xlsx'
    pathdoesnot_exists =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\NOT.xlsx'
    pathzip =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}'
   
    umumiy_without_duplicate1201 =[[] for i in range(0,49)]
    umumiy_without_duplicate1203 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D1 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D2 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D3 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D4 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D5 =[[] for i in range(0,49)]
    
    dlinniy_text_zero =[[],[],[]]
    buxgalterskiy_naz =[[],[],[],[],[],[],[],[]]
    

    for key , row in datas.iterrows():

        # if not LengthOfProfile.objects.filter(artikul=row['ch_article'],length=row['Длина']).exists():
            # LengthOfProfile(
            #     artikul = row['ch_article'],
            #     length = row['Длина'],
            #     ves_za_shtuk = row['Общий вес за штуку'],
            #     ves_za_metr = row['Удельный вес за метр']
            # ).save()
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
                    vtweg ='99'
                elif ii ==1:
                    vtweg ='10'
                elif ii ==2:
                    vtweg ='20'
                    
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
                buxgalterskiy_naz[7].append(row['ch_export_description'])
                
                buxgalterskiy_naz[0].append('2')
                buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                buxgalterskiy_naz[2].append('1200')
                buxgalterskiy_naz[3].append(vtweg)
                buxgalterskiy_naz[4].append('EN')
                buxgalterskiy_naz[5].append('0001')
                buxgalterskiy_naz[6].append('')
                buxgalterskiy_naz[7].append(row['ch_export_description_eng'])
                
        
        
        ############################ end bugalter nazvaniya###
        
        if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
        else:
            gruppa_material ='ALUPF'
                
        if ((row['Тип покрытия'] =='Ламинированный') and (row['Участок'] =='U-Упаковка + Готовая продукция') or ((row['Тип покрытия'] =='Ламинированный') and (row['Участок'] =='K-Комбинирования'))):
            umumiy_without_duplicate1203[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate1203[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate1203[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate1203[3].append('ШТ')
            umumiy_without_duplicate1203[4].append('ZPRF')
            umumiy_without_duplicate1203[5].append(gruppa_material)
            umumiy_without_duplicate1203[6].append(gruppa_material)
            umumiy_without_duplicate1203[7].append('E')
            umumiy_without_duplicate1203[8].append('01')
            umumiy_without_duplicate1203[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate1203[10].append(row['Общий вес за штуку'])
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
            if gruppa_material =='ALUGP':
                ss ='S400'
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
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
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate1203[44].append(SFSPF1203[sap_code_simvol])
            umumiy_without_duplicate1203[45].append('X')
            umumiy_without_duplicate1203[46].append(LGPRO1203[sap_code_simvol])
            umumiy_without_duplicate1203[47].append('')
            umumiy_without_duplicate1203[48].append(row['ch_combination'] + row['Тип покрытия'])
            
        if gruppa_material=='ALUGP':
            #######12D1
            umumiy_without_duplicate12D1[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D1[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D1[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D1[3].append('ШТ')
            umumiy_without_duplicate12D1[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D1[5].append(gruppa_material)
            umumiy_without_duplicate12D1[6].append(gruppa_material)
            umumiy_without_duplicate12D1[7].append('E')
            umumiy_without_duplicate12D1[8].append('01')
            umumiy_without_duplicate12D1[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D1[10].append(row['Общий вес за штуку'])
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
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
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
            umumiy_without_duplicate12D1[40].append('1201')
            umumiy_without_duplicate12D1[41].append('X')
            umumiy_without_duplicate12D1[42].append('X')
            umumiy_without_duplicate12D1[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D1[44].append('')
            umumiy_without_duplicate12D1[45].append('X')
            umumiy_without_duplicate12D1[46].append('')
            umumiy_without_duplicate12D1[47].append('X')
            umumiy_without_duplicate12D1[48].append(row['ch_combination'] + row['Тип покрытия'])
            
        if gruppa_material=='ALUGP':
            ######12D2
            umumiy_without_duplicate12D2[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D2[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D2[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D2[3].append('ШТ')
            umumiy_without_duplicate12D2[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D2[5].append(gruppa_material)
            umumiy_without_duplicate12D2[6].append(gruppa_material)
            umumiy_without_duplicate12D2[7].append('E')
            umumiy_without_duplicate12D2[8].append('01')
            umumiy_without_duplicate12D2[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D2[10].append(row['Общий вес за штуку'])
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
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
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
            umumiy_without_duplicate12D2[40].append('1201')
            umumiy_without_duplicate12D2[41].append('X')
            umumiy_without_duplicate12D2[42].append('X')
            umumiy_without_duplicate12D2[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D2[44].append('')
            umumiy_without_duplicate12D2[45].append('X')
            umumiy_without_duplicate12D2[46].append('')
            umumiy_without_duplicate12D2[47].append('X')
            umumiy_without_duplicate12D2[48].append(row['ch_combination'] + row['Тип покрытия'])
            
        if gruppa_material=='ALUGP':
            ######12D3
            umumiy_without_duplicate12D3[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D3[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D3[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D3[3].append('ШТ')
            umumiy_without_duplicate12D3[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D3[5].append(gruppa_material)
            umumiy_without_duplicate12D3[6].append(gruppa_material)
            umumiy_without_duplicate12D3[7].append('E')
            umumiy_without_duplicate12D3[8].append('01')
            umumiy_without_duplicate12D3[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D3[10].append(row['Общий вес за штуку'])
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
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
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
            umumiy_without_duplicate12D3[40].append('1201')
            umumiy_without_duplicate12D3[41].append('X')
            umumiy_without_duplicate12D3[42].append('X')
            umumiy_without_duplicate12D3[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D3[44].append('')
            umumiy_without_duplicate12D3[45].append('X')
            umumiy_without_duplicate12D3[46].append('')
            umumiy_without_duplicate12D3[47].append('X')
            umumiy_without_duplicate12D3[48].append(row['ch_combination'] + row['Тип покрытия'])
        if gruppa_material=='ALUGP':
            ######12D4
            umumiy_without_duplicate12D4[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D4[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D4[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D4[3].append('ШТ')
            umumiy_without_duplicate12D4[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D4[5].append(gruppa_material)
            umumiy_without_duplicate12D4[6].append(gruppa_material)
            umumiy_without_duplicate12D4[7].append('E')
            umumiy_without_duplicate12D4[8].append('01')
            umumiy_without_duplicate12D4[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D4[10].append(row['Общий вес за штуку'])
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
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
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
            umumiy_without_duplicate12D4[40].append('1201')
            umumiy_without_duplicate12D4[41].append('X')
            umumiy_without_duplicate12D4[42].append('X')
            umumiy_without_duplicate12D4[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D4[44].append('')
            umumiy_without_duplicate12D4[45].append('X')
            umumiy_without_duplicate12D4[46].append('')
            umumiy_without_duplicate12D4[47].append('X')
            umumiy_without_duplicate12D4[48].append(row['ch_combination'] + row['Тип покрытия'])
            
        if gruppa_material=='ALUGP':
            ######12D5
            umumiy_without_duplicate12D5[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D5[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D5[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D5[3].append('ШТ')
            umumiy_without_duplicate12D5[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D5[5].append(gruppa_material)
            umumiy_without_duplicate12D5[6].append(gruppa_material)
            umumiy_without_duplicate12D5[7].append('E')
            umumiy_without_duplicate12D5[8].append('01')
            umumiy_without_duplicate12D5[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D5[10].append(row['Общий вес за штуку'])
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
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
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
            umumiy_without_duplicate12D5[40].append('1201')
            umumiy_without_duplicate12D5[41].append('X')
            umumiy_without_duplicate12D5[42].append('X')
            umumiy_without_duplicate12D5[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D5[44].append('')
            umumiy_without_duplicate12D5[45].append('X')
            umumiy_without_duplicate12D5[46].append('')
            umumiy_without_duplicate12D5[47].append('X')
            umumiy_without_duplicate12D5[48].append(row['ch_combination'] + row['Тип покрытия'])
            
        umumiy_without_duplicate1201[0].append(row['SAP код S4P 100'])
        umumiy_without_duplicate1201[1].append(row['SAP код S4P 100'])
        umumiy_without_duplicate1201[2].append(row['Короткое название SAP'])
        umumiy_without_duplicate1201[3].append('ШТ')
        umumiy_without_duplicate1201[4].append('ZPRF')
        if '-7' in row['SAP код S4P 100']:
            gruppa_material ='ALUGP'
        else:
            gruppa_material ='ALUPF'
        umumiy_without_duplicate1201[5].append(gruppa_material)
        umumiy_without_duplicate1201[6].append(gruppa_material)
        umumiy_without_duplicate1201[7].append('E')
        umumiy_without_duplicate1201[8].append('01')
        umumiy_without_duplicate1201[9].append(str(row['Общий вес за штуку']).replace('.',','))
        umumiy_without_duplicate1201[10].append(str(row['Общий вес за штуку']).replace('.',','))
        umumiy_without_duplicate1201[11].append('КГ')
        umumiy_without_duplicate1201[12].append('NORM')
        umumiy_without_duplicate1201[13].append(row['Короткое название SAP'])
        umumiy_without_duplicate1201[14].append('ШТ')
        umumiy_without_duplicate1201[15].append('999')
        umumiy_without_duplicate1201[16].append('X')
        umumiy_without_duplicate1201[17].append('0000')
        umumiy_without_duplicate1201[18].append('PD')
        umumiy_without_duplicate1201[19].append('EX')
        umumiy_without_duplicate1201[20].append('0')
        umumiy_without_duplicate1201[21].append('E')
        ss =''
        sartrr =''
        if gruppa_material =='ALUGP':
            ss ='S400'
            sartrr ='5'
            
        bklast ='0100'
        if gruppa_material =='ALUPF':
            bklast ='0102'
            
            
        umumiy_without_duplicate1201[22].append(ss)
        umumiy_without_duplicate1201[23].append('')
        umumiy_without_duplicate1201[24].append('M')
        umumiy_without_duplicate1201[25].append('02')
        umumiy_without_duplicate1201[26].append('26')
        umumiy_without_duplicate1201[27].append(sartrr)
        umumiy_without_duplicate1201[28].append('X')
        umumiy_without_duplicate1201[29].append('5')
        umumiy_without_duplicate1201[30].append('Z_SAP_PP_002')
        umumiy_without_duplicate1201[31].append('4')
        umumiy_without_duplicate1201[32].append('SAP999')
        umumiy_without_duplicate1201[33].append('26')
        umumiy_without_duplicate1201[34].append('1201')
        umumiy_without_duplicate1201[35].append('3')
        umumiy_without_duplicate1201[36].append(bklast)
        umumiy_without_duplicate1201[37].append('S')
        umumiy_without_duplicate1201[38].append('1')
        umumiy_without_duplicate1201[39].append(row['Price'])
        umumiy_without_duplicate1201[40].append('1201')
        umumiy_without_duplicate1201[41].append('X')
        umumiy_without_duplicate1201[42].append('X')
        umumiy_without_duplicate1201[43].append('1')
        sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
        umumiy_without_duplicate1201[44].append(SFSPF1201[sap_code_simvol])
        umumiy_without_duplicate1201[45].append('X')
        umumiy_without_duplicate1201[46].append(LGPRO1201[sap_code_simvol])
        umumiy_without_duplicate1201[47].append('')
        umumiy_without_duplicate1201[48].append(row['ch_combination'] + row['Тип покрытия'])
    umumiy_without_duplicate =[[] for i in range(0,49)]
    for i in range(0,len(umumiy_without_duplicate1201)):
        umumiy_without_duplicate[i]+=umumiy_without_duplicate1201[i] 
            
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



########################## Бухгалтерская название.txt ##############################
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
    dlinniy_t['RU']=['RU' for x in dlinniy_text_zero[1]]
    dlinniy_t['GRUN']=['GRUN' for x in dlinniy_text_zero[1]]
    dlinniy_t['sa']=['' for x in dlinniy_text_zero[1]]
    dlinniy_t['TEXT']=dlinniy_text_zero[2]
    
    df_dlinniy_text= pd.DataFrame(dlinniy_t)
    
    np.savetxt(pathtext7, df_dlinniy_text.values,fmt='%s', delimiter="\t",header=header_dlinniy,comments='',encoding='ansi')
    
    
########################## end Длинный текс.txt ##############################


########################## 1.txt ##############################
    d1={}
    header1 ='MATNR\tBISMT\tMAKTX\tMEINS\tMTART\tMATKL\tWERKS\tBESKZ\tSPART\tBRGEW\tNTGEW\tGEWEI\tMTPOS_MARA'
    
    d1['MATNR']=umumiy_without_duplicate1201[0]
    d1['BISMT']=umumiy_without_duplicate1201[1]
    d1['MAKTX']=umumiy_without_duplicate1201[2]
    d1['MEINS']=umumiy_without_duplicate1201[3]
    d1['MTART']=umumiy_without_duplicate1201[4]
    d1['MATKL']=umumiy_without_duplicate1201[5]
    d1['WERKS']=umumiy_without_duplicate1201[34]
    d1['BESKZ']=umumiy_without_duplicate1201[7]
    d1['SPART']=umumiy_without_duplicate1201[8]
   
    d1['BRGEW']=[str(round(float(k1.replace(',','.')),3)).replace('.',',') for k1 in umumiy_without_duplicate1201[9]]
    d1['NTGEW']=[str(round(float(k2.replace(',','.')),3)).replace('.',',') for k2 in umumiy_without_duplicate1201[10]]
    d1['GEWEI']=umumiy_without_duplicate1201[11]
    d1['MTPOS_MARA']=umumiy_without_duplicate1201[12]
    
    
    df1= pd.DataFrame(d1)
    
    np.savetxt(pathtext1, df1.values,fmt='%s', delimiter="\t",header=header1,comments='',encoding='ansi')
    
########################## end 1.txt ##############################

########################## 2.txt ##############################
    header2='MAKTX\tMEINS\tMTART\tMATNR\tWERKS\tEKGRP\tXCHPF\tDISGR\tDISMM\tDISPO\tDISLS\tWEBAZ\tBESKZ\tLGFSB\tPLIFZ\tPERKZ\tMTVFP\tSCM_STRA1\tVRMOD\tPPSKZ\tSCM_WHATBOM\tSCM_HEUR_ID\tSCM_RRP_TYPE\tSCM_PROFID\tSTRGR\tBWKEY\tMLAST\tBKLAS\tVPRSV\tPEINH\tSTPRS\tPRCTR\tEKALR\tHKMAT\tLOSGR\tSFCPF\tUEETK\tLGPRO\tAUTO_P_ORD'
    zavod_code ={
        '1203':'PVC',
        '1201':'PR1',
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
    d2['DISPO']=[zavod_code[x] for x in umumiy_without_duplicate[34]]
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
    d2['STPRS']=[round(n,2) for n in umumiy_without_duplicate[39]]
    d2['PRCTR']=umumiy_without_duplicate[40]
    d2['EKALR']=umumiy_without_duplicate[41]
    d2['HKMAT']=umumiy_without_duplicate[42]
    d2['LOSGR']=umumiy_without_duplicate[43]
    d2['SFCPF']=umumiy_without_duplicate[44]
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
    VTWEG =['99','10','20']
    KONDM ={
        'с термомостоманодированный':'A0',
        'без термомостаокрашенный':'A1',
        'без термомостабелый':'A1',
        'без термомостасублимированный':'A2',
        'без термомостаанодированный':'A3',
        'без термомосталаминированный':'A4',
        'с термомостомламинированный':'A5',
        'без термомостанеокрашенный':'A6',
        'с термомостомокрашенный':'A7',
        'с термомостомбелый':'A7',
        'с термомостомнеокрашенный':'A8',
        'с термомостомсублимированный':'A9',
    }
    for i in range(0,3):
        d3['MAKTX'] += umumiy_without_duplicate[13]
        d3['MEINS'] += umumiy_without_duplicate[14]
        d3['MTART'] += umumiy_without_duplicate[4]
        d3['SPART'] += umumiy_without_duplicate[8]
        d3['MATNR'] += umumiy_without_duplicate[0]
        d3['WERKS'] += umumiy_without_duplicate[34]
        d3['VKORG'] += [ 1200 for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['MTPOS'] += umumiy_without_duplicate[12]
        d3['VTWEG'] += [ VTWEG[i] for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['PRCTR'] += [ '1203' if umumiy_without_duplicate[34][i] =='1203' else '1201' for i in range(0,len(umumiy_without_duplicate[34]))]
        d3['MTVFP'] += [ '02' for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['ALAND'] += [ 'UZ' for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['TATYP'] += [ 'MWST' for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['TAXKM'] += [ '1' for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['VERSG'] += [ '1' for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['KTGRM'] += [ '01' for j in range(0,len(umumiy_without_duplicate[13]))]
        if i!=2:
            d3['KONDM'] += [ '01' for j in range(0,len(umumiy_without_duplicate[13]))]
        else:
            d3['KONDM'] += [ '01' if '-7' not in umumiy_without_duplicate[0][x] else KONDM[umumiy_without_duplicate[48][x].lower()] for x in range(0,len(umumiy_without_duplicate[0]))]
            
        d3['LADGR'] += [ '0001' for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['TRAGR'] += [ '0001' for j in range(0,len(umumiy_without_duplicate[13]))]
    df3= pd.DataFrame(d3)
    np.savetxt(pathtext3, df3.values, fmt='%s', delimiter="\t",header=header3,comments='',encoding='ansi')
########################## end 3.txt ##############################
    
########################## 4.txt ##############################    
    new_ll =[[],[],[]]
    sap_code_title =[]
    dlina_title =[]
    obshiy_ves_za_shtuku =[]
    wms_width =[]
    wms_height =[]
    
    for key , row in datas.iterrows():
        sap_code_title.append(row['SAP код S4P 100'])
        dlina_title.append(row['Длина'])
        obshiy_ves_za_shtuku.append(str(row['Общий вес за штуку']).replace(',','.'))
        wms_width.append(row['WMS_WIDTH'])
        wms_height.append(row['WMS_HEIGHT'])

        
        sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]        
        if sap_code_simvol =='E':
            for i in range(0,len(LGORT['E'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT['E'][i]['zavod_code'])
                new_ll[2].append(LGORT['E'][i]['zavod_sap'])
        if sap_code_simvol =='Z':
            for i in range(0,len(LGORT['Z'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT['Z'][i]['zavod_code'])
                new_ll[2].append(LGORT['Z'][i]['zavod_sap'])
        if sap_code_simvol =='P':
            if (row['Тип покрытия'] =='Ламинированный'):
                for i in range(0,len(LGORT['PL'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['PL'][i]['zavod_code'])
                    new_ll[2].append(LGORT['PL'][i]['zavod_sap'])
            else:
                for i in range(0,len(LGORT['P'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['P'][i]['zavod_code'])
                    new_ll[2].append(LGORT['P'][i]['zavod_sap'])
        
        if sap_code_simvol =='S':
            for i in range(0,len(LGORT['S'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT['S'][i]['zavod_code'])
                new_ll[2].append(LGORT['S'][i]['zavod_sap'])
        if sap_code_simvol =='N':
            for i in range(0,len(LGORT['N'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT['N'][i]['zavod_code'])
                new_ll[2].append(LGORT['N'][i]['zavod_sap'])
        if sap_code_simvol =='K':
            for i in range(0,len(LGORT['K'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT['K'][i]['zavod_code'])
                new_ll[2].append(LGORT['K'][i]['zavod_sap'])
        if sap_code_simvol =='A':
            for i in range(0,len(LGORT['A'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT['A'][i]['zavod_code'])
                new_ll[2].append(LGORT['A'][i]['zavod_sap'])
        
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
        
        if sap_code_simvol =='F':
            for i in range(0,len(LGORT['F'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT['F'][i]['zavod_code'])
                new_ll[2].append(LGORT['F'][i]['zavod_sap'])

    header4='MATNR\tWERKS\tLGORT'
    d4={}
    d4['MATNR']=new_ll[0]
    d4['WERKS']=new_ll[1]
    d4['LGORT']=new_ll[2]
    df4= pd.DataFrame(d4)
    np.savetxt(pathtext4, df4.values, fmt='%s', delimiter="\t",header=header4,comments='',encoding='ansi')
########################## end 4.txt ##############################
########################## 55.txt ##############################    
    # new_ll_55 =[[],[],[]]
    
    # for key , row in datas.iterrows():
    #     sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]        

    #     if sap_code_simvol =='7':
    #         if (row['Тип покрытия'] =='Ламинированный'):
    #             for i in range(0,len(LGORT['7L'])):
    #                 new_ll_55[0].append(row['SAP код S4P 100'])
    #                 new_ll_55[1].append(LGORT['7L'][i]['zavod_code'])
    #                 new_ll_55[2].append(LGORT['7L'][i]['zavod_sap'])
    #         else:
    #             for i in range(0,len(LGORT['7'])):
    #                 new_ll_55[0].append(row['SAP код S4P 100'])
    #                 new_ll_55[1].append(LGORT['7'][i]['zavod_code'])
    #                 new_ll_55[2].append(LGORT['7'][i]['zavod_sap'])

    # header55='MATNR\tWERKS\tLGORT\tRAUBE'
    # d55={}
    # d55['MATNR']=new_ll_55[0] 
    # d55['WERKS']=new_ll_55[1] 
    # d55['LGORT']=new_ll_55[2] 
    # d55['RAUBE']=['' for x in new_ll_55[2]] 
    # df55= pd.DataFrame(d55)
    # np.savetxt(pathtext55, df55.values, fmt='%s', delimiter="\t",header=header55,comments='',encoding='ansi')
    ########################## end 55.txt ##############################
    
    
########################## 5.txt ##############################
    d5 ={
        'sap_code':[],
        'ed_iz1':[],
        'ed_iz2':[],
        'ed_iz3':[],
        'ed_iz4':[],
        'ed_iz5':[],
        'ed_iz6':[],
        'ed_iz7':[]
    }
    ED_IZM =['ШТ','М','КГ']
    
    # sap_code_title =[]
    # dlina_title =[]
    # obshiy_ves_za_shtuku =[]
    # wms_width =[]
    # wms_height =[]
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
        d5['ed_iz2'] +=['1' if i =='ШТ' else '1000'  for j in range(0,len(sap_code_title)) ]
        # d5['ed_iz3'] +=['1' if i =='ШТ' elif i=='М' for j in range(0,len(sap_code_title)) ]
        d5['ed_iz4'] +=[j for j in dlina_title ]
        d5['ed_iz5'] +=[j for j in wms_height ]
        d5['ed_iz6'] +=[j for j in wms_width ]
        d5['ed_iz7'] +=[ 'мм' for j in range(0,len(sap_code_title))]
    
    d5['ed_iz3'] = ed_iz3
    df5= pd.DataFrame(d5)
    np.savetxt(pathtext5, df5.values, fmt='%s', delimiter="\t",encoding='ansi')
########################## end 5.txt ##############################
########################## List v 3 ##############################
    dd2 = [[],[],[],[],[],[]]
    baza_profile_links =[[],[]]
    

    for key , row in datas.iterrows():
        sap_code = row['SAP код S4P 100'].split('-')[0]
        bazaprofiley = AluProfilesData.objects.filter(Q(data__Артикул =sap_code)|Q(data__Компонент=sap_code))[:1].get()
         
        baza_profile_links[0].append(row['SAP код S4P 100'])
        baza_profile_links[1].append(bazaprofiley.data['Ссылка для чертежей'])

        row['ch_tnved'] =str(row['ch_tnved']).replace('.0','')
        row['ch_outer_side_pc_id'] =str(row['ch_outer_side_pc_id']).replace('.0','')
        row['ch_outer_side_pc_brand'] =str(row['ch_outer_side_pc_brand']).replace('.0','')
        row['ch_inner_side_pc_id'] =str(row['ch_inner_side_pc_id']).replace('.0','')
        row['ch_inner_side_pc_brand'] =str(row['ch_inner_side_pc_brand']).replace('.0','')
        row['ch_outer_side_wg_s_id'] =str(row['ch_outer_side_wg_s_id']).replace('.0','')
        row['ch_inner_side_wg_s_id'] =str(row['ch_inner_side_wg_s_id']).replace('.0','')
        row['ch_outer_side_wg_id'] =str(row['ch_outer_side_wg_id']).replace('.0','')
        row['ch_inner_side_wg_id'] =str(row['ch_inner_side_wg_id']).replace('.0','')
        row['ch_width'] =str(row['ch_width']).replace('.0','')
        row['ch_height'] =str(row['ch_height']).replace('.0','')
        
        if (('-E' in row['SAP код S4P 100']) or ('-Z' in row['SAP код S4P 100']) or ('-P' in row['SAP код S4P 100']) or ('-A' in row['SAP код S4P 100']) or ('-S' in row['SAP код S4P 100'])):

            for j in range(0,32):
                dd2[0].append('001')
            dd2[0].append('023')
                
            for j in range(0,32):
                if HEADER2[j] not in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT','TNVED']:

                    dd2[1].append('ALUMINIUM_PROFILE')
                else:
                    if HEADER2[j] in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT']:
                        dd2[1].append('RAWMAT_TYPE')
                    elif HEADER2[j] =='TNVED':
                        dd2[1].append('TNVED')
            dd2[1].append('ZPP_023_HALB')
                
            for j in range(0,33):
                dd2[2].append('MARA')
                
            for j in range(0,33):
                dd2[3].append(row['SAP код S4P 100'])
                
            for j in HEADER2:
                dd2[4].append(j)
            dd2[4].append('ZBATCH_NUM')


            dd2[5].append('')
            dd2[5].append('')
            dd2[5].append(row['ch_system'])
            dd2[5].append(row['SAP код S4P 100'].split('-')[0])
            dd2[5].append(row['Длина'])
            dd2[5].append(row['Тип покрытия'])
            dd2[5].append(row['ch_alloy'])
            dd2[5].append(row['ch_temper'])
            dd2[5].append(row['ch_combination'])
            dd2[5].append(row['ch_outer_side_pc_id'])
            dd2[5].append(row['ch_outer_side_pc_brand'])
            dd2[5].append(row['ch_inner_side_pc_id'])
            dd2[5].append(row['ch_inner_side_pc_brand'])
            dd2[5].append(row['ch_outer_side_wg_s_id'])
            dd2[5].append(row['ch_inner_side_wg_s_id'])
            dd2[5].append(row['ch_outer_side_wg_id'])
            dd2[5].append(row['ch_inner_side_wg_id'])
           
            if row['ch_anodization_contact'].lower() =='yc':
                dd2[5].append('С КОНТАКТОМ')
            elif row['ch_anodization_contact'].lower()=='nc' :
                dd2[5].append('БЕЗ КОНТАКТА')
            else:
                dd2[5].append(row['ch_anodization_contact'])

            dd2[5].append(row['ch_anodization_type'])
            dd2[5].append(row['ch_anodization_method'])
            dd2[5].append(row['ch_profile_base'])
            dd2[5].append(row['ch_width'])
            dd2[5].append(row['ch_height'])
            dd2[5].append(row['ch_category'])
            dd2[5].append(row['ch_rawmat_type'])
            dd2[5].append('')
            dd2[5].append(row['ch_tnved'])
            dd2[5].append(str(row['ch_surface_treatment_export']).replace('.0',''))
            dd2[5].append(row['WMS_WIDTH'])
            dd2[5].append(row['WMS_HEIGHT'])
            dd2[5].append('')
            dd2[5].append(bazaprofiley.data['Тип Комбинация'])
            dd2[5].append('XXXX')
        else:
            
            for j in range(0,33):
                dd2[0].append('001')
                
            for j in range(0,33):
                if HEADER[j] not in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT','TNVED']:
                    dd2[1].append('ALUMINIUM_PROFILE')
                else:
                    if HEADER[j] in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT']:
                        dd2[1].append('RAWMAT_TYPE')
                    elif HEADER[j] =='TNVED':
                        dd2[1].append('TNVED')

            if '-7' in row['SAP код S4P 100']:
                dd2[0].append('001')
                dd2[0].append('023')
                dd2[1].append('QBIC')
                dd2[1].append('ZPP_023_FERT')
            else:
                dd2[0].append('023')
                dd2[1].append('ZPP_023_HALB')

            for j in range(0,33):
                dd2[2].append('MARA')
                
            for j in range(0,33):
                dd2[3].append(row['SAP код S4P 100'])
                
            for j in HEADER:
                dd2[4].append(j)

            if '-7' in row['SAP код S4P 100']:
                dd2[2].append('MARA')
                dd2[2].append('MARA')
                dd2[3].append(row['SAP код S4P 100'])
                dd2[3].append(row['SAP код S4P 100'])
                dd2[4].append('COATING_QBIC')
                dd2[4].append('ZBATCH_NUM')
            else:
                dd2[2].append('MARA')
                dd2[3].append(row['SAP код S4P 100'])
                dd2[4].append('ZBATCH_NUM')

            dd2[5].append('')
            dd2[5].append('')
            dd2[5].append(row['ch_system'])
            dd2[5].append(row['SAP код S4P 100'].split('-')[0])
            dd2[5].append(row['Длина'])
            dd2[5].append(row['Тип покрытия'])
            dd2[5].append(row['ch_alloy'])
            dd2[5].append(row['ch_temper'])
            dd2[5].append(row['ch_combination'])
            dd2[5].append(row['ch_outer_side_pc_id'])
            dd2[5].append(row['ch_outer_side_pc_brand'])
            dd2[5].append(row['ch_inner_side_pc_id'])
            dd2[5].append(row['ch_inner_side_pc_brand'])
            dd2[5].append(row['ch_outer_side_wg_s_id'])
            dd2[5].append(row['ch_inner_side_wg_s_id'])
            dd2[5].append(row['ch_outer_side_wg_id'])
            dd2[5].append(row['ch_inner_side_wg_id'])
            
            if row['ch_anodization_contact'].lower() =='yc':
                dd2[5].append('С КОНТАКТОМ')
            elif row['ch_anodization_contact'].lower()=='nc' :
                dd2[5].append('БЕЗ КОНТАКТА')
            else:
                dd2[5].append(row['ch_anodization_contact'])
            
            dd2[5].append(row['ch_anodization_type'])
            dd2[5].append(row['ch_anodization_method'])
            dd2[5].append(row['ch_print_view'])
            dd2[5].append(row['ch_profile_base'])
            dd2[5].append(row['ch_width'])
            dd2[5].append(row['ch_height'])
            dd2[5].append(row['ch_category'])
            dd2[5].append(row['ch_rawmat_type'])
            dd2[5].append('')
            dd2[5].append(row['ch_tnved'])
            dd2[5].append(str(row['ch_surface_treatment_export']).replace('.0',''))
            dd2[5].append(row['WMS_WIDTH'])
            dd2[5].append(row['WMS_HEIGHT'])
            dd2[5].append('')
            
            dd2[5].append(bazaprofiley.data['Тип Комбинация'])

            if '-7' in row['SAP код S4P 100']:
                if row['Тип покрытия'] =='Неокрашенный':
                    qbic ='XXXX'
                elif row['Тип покрытия'] =='Окрашенный':
                    qbic = row['ch_outer_side_pc_id']
                elif row['Тип покрытия'] =='Анодированный':
                    qbic = row['ch_outer_side_pc_id']
                elif row['Тип покрытия'] =='Ламинированный':
                    if row['ch_outer_side_wg_id'] =='XXXX':
                        qbic = row['ch_inner_side_wg_id']
                    else:
                        qbic = row['ch_outer_side_wg_id']
                elif row['Тип покрытия'] =='Сублимированный':
                    qbic = row['ch_outer_side_wg_s_id']
                else:
                    qbic ='XXXX'
                dd2[5].append(qbic)
                dd2[5].append('XXXX')
            else:
                dd2[5].append('XXXX')

    new_date={}       
    new_date['Вид класса'] = dd2[0]
    new_date['Класс'] = dd2[1]
    new_date['Таблица'] = dd2[2]
    new_date['Объект'] = dd2[3]
    new_date['Имя признака'] = dd2[4]
    new_date['Значение признака'] = dd2[5]
    new_date['Статус загрузки'] = ''
    
    
    df_baza_profiley_link = pd.DataFrame({'SAP CODE':baza_profile_links[0],'link':baza_profile_links[1]})
    df_baza_profiley_link.to_excel(pathtext9,index=False)
    
    ddf2 = pd.DataFrame(new_date)
    ddf2 = ddf2[((ddf2["Значение признака"] != "nan") & (ddf2["Значение признака"] != ""))]
    ddf2 = ddf2.replace('XXXX','')
    ddf2.to_excel(pathtext6,index=False)


    if  len(does_not_exists)>0:     
        not_exists =pd.DataFrame(np.array(does_not_exists),columns=['SAP CODE','Error'])
    else:
        not_exists =pd.DataFrame(np.array([['','']]),columns=['SAP CODE','Error'])

    not_exists.to_excel(pathdoesnot_exists,index=False)

    path_1101,path_zip2 = get_cretead_txt_for_1101(datas,elist)

    file_path =f'{path_zip2}.zip'
    
    zip(path_zip2, path_zip2)

    return [file_path,]
    
    
def get_cretead_txt_for_1101(datas,elist):
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M-%S MINUT")
    
    
       
    if not os.path.isdir(f'{MEDIA_ROOT}\\uploads\\TXT'):
        create_folder(f'{MEDIA_ROOT}\\uploads',"TXT")
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\TXT',f"{year}")
    create_folder(f'{MEDIA_ROOT}\\uploads\\TXT\\{year}',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}',hour)
    create_folder(f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}','JOMIY')
    create_folder(f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\JOMIY',minut)
    pathtext1 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\JOMIY\\{minut}\\1.txt'
    pathtext2 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\JOMIY\\{minut}\\2.txt'
    pathtext3 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\JOMIY\\{minut}\\3.txt'
    pathtext4 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\JOMIY\\{minut}\\4.txt'
    pathtext55 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\JOMIY\\{minut}\\5.txt'
    pathtext5 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\JOMIY\\{minut}\\Единицы изм.txt'
    pathtext6 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\JOMIY\\{minut}\\Лист в C 3.xlsx'
    pathtext7 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\JOMIY\\{minut}\\Длинный текс.txt'
    pathtext8 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\JOMIY\\{minut}\\Бух название SDLONGTEXT.txt'
    pathtext9 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\JOMIY\\{minut}\\RAUBE.txt'
    pathtext10 =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}\\JOMIY\\{minut}\\ZMD_11_0008 - Прикрепление чертежей ОЗМ.xlsx'
    pathzip =f'{MEDIA_ROOT}\\uploads\\TXT\\{year}\\{month}\\{day}\\{hour}'
        
    
    umumiy_without_duplicate1201 =[[] for i in range(0,51)]
    umumiy_without_duplicate1203 =[[] for i in range(0,51)]
    umumiy_without_duplicate12D1 =[[] for i in range(0,51)]
    umumiy_without_duplicate12D2 =[[] for i in range(0,51)]
    umumiy_without_duplicate12D3 =[[] for i in range(0,51)]
    umumiy_without_duplicate12D4 =[[] for i in range(0,51)]
    umumiy_without_duplicate12D5 =[[] for i in range(0,51)]
    
    dlinniy_text_zero =[[],[],[]]
    buxgalterskiy_naz =[[],[],[],[],[],[],[],[]]

    zakalka_iskyucheniye = Norma.objects.filter(закалка_исключение ='1').values_list('артикул',flat=True)
    for key , row in datas.iterrows():

        sap_codee = row['SAP код S4P 100'].split('-')[0]

        if ((sap_codee in zakalka_iskyucheniye) and ('-Z' in row['SAP код S4P 100'])):
           continue 

        if  (('-E' in row['SAP код S4P 100']) and (row['SAP код S4P 100'] not in elist)):
            continue 

        if row['Тип покрытия'] =='Анодированный':
            continue
        
        filte_type2 = ('-E' in row['SAP код S4P 100']) or ('-Z' in row['SAP код S4P 100']) or ('-P' in row['SAP код S4P 100']) or ('-S' in row['SAP код S4P 100']) or ('-N' in row['SAP код S4P 100']) or ('-K' in row['SAP код S4P 100']) or ('-7' in row['SAP код S4P 100'])
        
        if not filte_type2:
            continue

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
                    vtweg ='99'
                elif ii ==1:
                    vtweg ='10'
                elif ii ==2:
                    vtweg ='20'
                    
                buxgalterskiy_naz[0].append('1')
                buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                buxgalterskiy_naz[2].append('1100')
                buxgalterskiy_naz[3].append(vtweg)
                buxgalterskiy_naz[4].append('RU')
                buxgalterskiy_naz[5].append('0001')
                buxgalterskiy_naz[6].append('')
                buxgalterskiy_naz[7].append('')
                
                buxgalterskiy_naz[0].append('1')
                buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                buxgalterskiy_naz[2].append('1100')
                buxgalterskiy_naz[3].append(vtweg)
                buxgalterskiy_naz[4].append('EN')
                buxgalterskiy_naz[5].append('0001')
                buxgalterskiy_naz[6].append('')
                buxgalterskiy_naz[7].append('')
                
                buxgalterskiy_naz[0].append('2')
                buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                buxgalterskiy_naz[2].append('1100')
                buxgalterskiy_naz[3].append(vtweg)
                buxgalterskiy_naz[4].append('RU')
                buxgalterskiy_naz[5].append('0001')
                buxgalterskiy_naz[6].append('')
                buxgalterskiy_naz[7].append(row['ch_export_description'])
                
                buxgalterskiy_naz[0].append('2')
                buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                buxgalterskiy_naz[2].append('1100')
                buxgalterskiy_naz[3].append(vtweg)
                buxgalterskiy_naz[4].append('EN')
                buxgalterskiy_naz[5].append('0001')
                buxgalterskiy_naz[6].append('')
                buxgalterskiy_naz[7].append(row['ch_export_description_eng'])
                
        
        
        ############################ end bugalter nazvaniya###
        
        if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
        else:
            gruppa_material ='ALUPF'
                
          
        if gruppa_material=='ALUGP':
            #######12D1
            umumiy_without_duplicate12D1[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D1[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D1[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D1[3].append('ШТ')
            umumiy_without_duplicate12D1[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D1[5].append(gruppa_material)
            umumiy_without_duplicate12D1[6].append(gruppa_material)
            umumiy_without_duplicate12D1[7].append('E')
            umumiy_without_duplicate12D1[8].append('01')
            umumiy_without_duplicate12D1[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D1[10].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D1[11].append('КГ')
            umumiy_without_duplicate12D1[12].append('NORM')
            umumiy_without_duplicate12D1[13].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D1[14].append('ШТ')
            umumiy_without_duplicate12D1[15].append('999')
            umumiy_without_duplicate12D1[16].append('X')
            umumiy_without_duplicate12D1[17].append('0000')
            umumiy_without_duplicate12D1[18].append('PD')
            umumiy_without_duplicate12D1[19].append('MB')
            umumiy_without_duplicate12D1[20].append('0')
            umumiy_without_duplicate12D1[21].append('F')
            
            sartrr =''
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
                bklast ='0102'
                
                
            umumiy_without_duplicate12D1[22].append('')
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
            umumiy_without_duplicate12D1[34].append('11D1')
            umumiy_without_duplicate12D1[35].append('3')
            umumiy_without_duplicate12D1[36].append(bklast)
            umumiy_without_duplicate12D1[37].append('S')
            umumiy_without_duplicate12D1[38].append('1')
            umumiy_without_duplicate12D1[39].append(row['Price'])
            umumiy_without_duplicate12D1[40].append('1101')
            umumiy_without_duplicate12D1[41].append('X')
            umumiy_without_duplicate12D1[42].append('X')
            umumiy_without_duplicate12D1[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D1[44].append('')
            umumiy_without_duplicate12D1[45].append('X')
            umumiy_without_duplicate12D1[46].append('')
            umumiy_without_duplicate12D1[47].append('X')
            umumiy_without_duplicate12D1[48].append(row['ch_combination'] + row['Тип покрытия'])
            umumiy_without_duplicate12D1[49].append('')

            if row['Тип покрытия'].capitalize() =='Белый':
                umumiy_without_duplicate12D1[50].append('S0')
            elif row['Тип покрытия'].capitalize() =='Неокрашенный':
                umumiy_without_duplicate12D1[50].append('S1')
            elif row['Тип покрытия'].capitalize() =='Окрашенный':
                umumiy_without_duplicate12D1[50].append('S2')
            elif row['Тип покрытия'].capitalize() =='Сублимированный':
                umumiy_without_duplicate12D1[50].append('S3')
            elif row['Тип покрытия'].capitalize() =='Ламинированный':
                umumiy_without_duplicate12D1[50].append('0001')
            elif row['Тип покрытия'].capitalize() =='Анодированный':
                umumiy_without_duplicate12D1[50].append('0001')
            


            
        if gruppa_material=='ALUGP':
            ######12D2
            umumiy_without_duplicate12D2[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D2[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D2[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D2[3].append('ШТ')
            umumiy_without_duplicate12D2[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D2[5].append(gruppa_material)
            umumiy_without_duplicate12D2[6].append(gruppa_material)
            umumiy_without_duplicate12D2[7].append('E')
            umumiy_without_duplicate12D2[8].append('01')
            umumiy_without_duplicate12D2[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D2[10].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D2[11].append('КГ')
            umumiy_without_duplicate12D2[12].append('NORM')
            umumiy_without_duplicate12D2[13].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D2[14].append('ШТ')
            umumiy_without_duplicate12D2[15].append('999')
            umumiy_without_duplicate12D2[16].append('X')
            umumiy_without_duplicate12D2[17].append('0000')
            umumiy_without_duplicate12D2[18].append('PD')
            umumiy_without_duplicate12D2[19].append('MB')
            umumiy_without_duplicate12D2[20].append('0')
            umumiy_without_duplicate12D2[21].append('F')
            
            sartrr =''
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
                bklast ='0102'
                
                
            umumiy_without_duplicate12D2[22].append('')
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
            umumiy_without_duplicate12D2[34].append('11D2')
            umumiy_without_duplicate12D2[35].append('3')
            umumiy_without_duplicate12D2[36].append(bklast)
            umumiy_without_duplicate12D2[37].append('S')
            umumiy_without_duplicate12D2[38].append('1')
            umumiy_without_duplicate12D2[39].append(row['Price'])
            umumiy_without_duplicate12D2[40].append('1101')
            umumiy_without_duplicate12D2[41].append('X')
            umumiy_without_duplicate12D2[42].append('X')
            umumiy_without_duplicate12D2[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D2[44].append('')
            umumiy_without_duplicate12D2[45].append('X')
            umumiy_without_duplicate12D2[46].append('')
            umumiy_without_duplicate12D2[47].append('X')
            umumiy_without_duplicate12D2[48].append(row['ch_combination'] + row['Тип покрытия'])
            umumiy_without_duplicate12D2[49].append('')

            if row['Тип покрытия'].capitalize() =='Белый':
                umumiy_without_duplicate12D2[50].append('S0')
            elif row['Тип покрытия'].capitalize() =='Неокрашенный':
                umumiy_without_duplicate12D2[50].append('S1')
            elif row['Тип покрытия'].capitalize() =='Окрашенный':
                umumiy_without_duplicate12D2[50].append('S2')
            elif row['Тип покрытия'].capitalize() =='Сублимированный':
                umumiy_without_duplicate12D2[50].append('S3')
            elif row['Тип покрытия'].capitalize() =='Ламинированный':
                umumiy_without_duplicate12D2[50].append('0001')
            elif row['Тип покрытия'].capitalize() =='Анодированный':
                umumiy_without_duplicate12D1[50].append('0001')
            

        if gruppa_material=='ALUGP':
            ######12D3
            umumiy_without_duplicate12D3[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D3[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D3[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D3[3].append('ШТ')
            umumiy_without_duplicate12D3[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D3[5].append(gruppa_material)
            umumiy_without_duplicate12D3[6].append(gruppa_material)
            umumiy_without_duplicate12D3[7].append('E')
            umumiy_without_duplicate12D3[8].append('01')
            umumiy_without_duplicate12D3[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D3[10].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D3[11].append('КГ')
            umumiy_without_duplicate12D3[12].append('NORM')
            umumiy_without_duplicate12D3[13].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D3[14].append('ШТ')
            umumiy_without_duplicate12D3[15].append('999')
            umumiy_without_duplicate12D3[16].append('X')
            umumiy_without_duplicate12D3[17].append('0000')
            umumiy_without_duplicate12D3[18].append('PD')
            umumiy_without_duplicate12D3[19].append('MB')
            umumiy_without_duplicate12D3[20].append('0')
            umumiy_without_duplicate12D3[21].append('F')
            
            sartrr =''
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
                bklast ='0102'
                
                
            umumiy_without_duplicate12D3[22].append('')
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
            umumiy_without_duplicate12D3[34].append('11D3')
            umumiy_without_duplicate12D3[35].append('3')
            umumiy_without_duplicate12D3[36].append(bklast)
            umumiy_without_duplicate12D3[37].append('S')
            umumiy_without_duplicate12D3[38].append('1')
            umumiy_without_duplicate12D3[39].append(row['Price'])
            umumiy_without_duplicate12D3[40].append('1101')
            umumiy_without_duplicate12D3[41].append('X')
            umumiy_without_duplicate12D3[42].append('X')
            umumiy_without_duplicate12D3[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D3[44].append('')
            umumiy_without_duplicate12D3[45].append('X')
            umumiy_without_duplicate12D3[46].append('')
            umumiy_without_duplicate12D3[47].append('X')
            umumiy_without_duplicate12D3[48].append(row['ch_combination'] + row['Тип покрытия'])
            umumiy_without_duplicate12D3[49].append('')

            if row['Тип покрытия'].capitalize() =='Белый':
                umumiy_without_duplicate12D3[50].append('S0')
            elif row['Тип покрытия'].capitalize() =='Неокрашенный':
                umumiy_without_duplicate12D3[50].append('S1')
            elif row['Тип покрытия'].capitalize() =='Окрашенный':
                umumiy_without_duplicate12D3[50].append('S2')
            elif row['Тип покрытия'].capitalize() =='Сублимированный':
                umumiy_without_duplicate12D3[50].append('S3')
            elif row['Тип покрытия'].capitalize() =='Ламинированный':
                umumiy_without_duplicate12D3[50].append('0001')
            elif row['Тип покрытия'].capitalize() =='Анодированный':
                umumiy_without_duplicate12D1[50].append('0001')
           
        
        if gruppa_material=='ALUGP':
            ######12D4
            umumiy_without_duplicate12D4[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D4[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D4[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D4[3].append('ШТ')
            umumiy_without_duplicate12D4[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D4[5].append(gruppa_material)
            umumiy_without_duplicate12D4[6].append(gruppa_material)
            umumiy_without_duplicate12D4[7].append('E')
            umumiy_without_duplicate12D4[8].append('01')
            umumiy_without_duplicate12D4[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D4[10].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D4[11].append('КГ')
            umumiy_without_duplicate12D4[12].append('NORM')
            umumiy_without_duplicate12D4[13].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D4[14].append('ШТ')
            umumiy_without_duplicate12D4[15].append('999')
            umumiy_without_duplicate12D4[16].append('X')
            umumiy_without_duplicate12D4[17].append('0000')
            umumiy_without_duplicate12D4[18].append('PD')
            umumiy_without_duplicate12D4[19].append('MB')
            umumiy_without_duplicate12D4[20].append('0')
            umumiy_without_duplicate12D4[21].append('F')
            
            sartrr =''
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
                bklast ='0102'
                
                
            umumiy_without_duplicate12D4[22].append('')
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
            umumiy_without_duplicate12D4[34].append('11D4')
            umumiy_without_duplicate12D4[35].append('3')
            umumiy_without_duplicate12D4[36].append(bklast)
            umumiy_without_duplicate12D4[37].append('S')
            umumiy_without_duplicate12D4[38].append('1')
            umumiy_without_duplicate12D4[39].append(row['Price'])
            umumiy_without_duplicate12D4[40].append('1101')
            umumiy_without_duplicate12D4[41].append('X')
            umumiy_without_duplicate12D4[42].append('X')
            umumiy_without_duplicate12D4[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D4[44].append('')
            umumiy_without_duplicate12D4[45].append('X')
            umumiy_without_duplicate12D4[46].append('')
            umumiy_without_duplicate12D4[47].append('X')
            umumiy_without_duplicate12D4[48].append(row['ch_combination'] + row['Тип покрытия'])
            umumiy_without_duplicate12D4[49].append('')

            if row['Тип покрытия'].capitalize() =='Белый':
                umumiy_without_duplicate12D4[50].append('S0')
            elif row['Тип покрытия'].capitalize() =='Неокрашенный':
                umumiy_without_duplicate12D4[50].append('S1')
            elif row['Тип покрытия'].capitalize() =='Окрашенный':
                umumiy_without_duplicate12D4[50].append('S2')
            elif row['Тип покрытия'].capitalize() =='Сублимированный':
                umumiy_without_duplicate12D4[50].append('S3')
            elif row['Тип покрытия'].capitalize() =='Ламинированный':
                umumiy_without_duplicate12D4[50].append('0001')
            elif row['Тип покрытия'].capitalize() =='Анодированный':
                umumiy_without_duplicate12D1[50].append('0001')
            

        if gruppa_material=='ALUGP':
            ######12D5
            umumiy_without_duplicate12D5[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D5[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D5[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D5[3].append('ШТ')
            umumiy_without_duplicate12D5[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D5[5].append(gruppa_material)
            umumiy_without_duplicate12D5[6].append(gruppa_material)
            umumiy_without_duplicate12D5[7].append('E')
            umumiy_without_duplicate12D5[8].append('01')
            umumiy_without_duplicate12D5[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D5[10].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D5[11].append('КГ')
            umumiy_without_duplicate12D5[12].append('NORM')
            umumiy_without_duplicate12D5[13].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D5[14].append('ШТ')
            umumiy_without_duplicate12D5[15].append('999')
            umumiy_without_duplicate12D5[16].append('X')
            umumiy_without_duplicate12D5[17].append('0000')
            umumiy_without_duplicate12D5[18].append('PD')
            umumiy_without_duplicate12D5[19].append('MB')
            umumiy_without_duplicate12D5[20].append('0')
            umumiy_without_duplicate12D5[21].append('F')
            
            sartrr =''
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
                bklast ='0102'
                
                
            umumiy_without_duplicate12D5[22].append('')
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
            umumiy_without_duplicate12D5[34].append('11D5')
            umumiy_without_duplicate12D5[35].append('3')
            umumiy_without_duplicate12D5[36].append(bklast)
            umumiy_without_duplicate12D5[37].append('S')
            umumiy_without_duplicate12D5[38].append('1')
            umumiy_without_duplicate12D5[39].append(row['Price'])
            umumiy_without_duplicate12D5[40].append('1101')
            umumiy_without_duplicate12D5[41].append('X')
            umumiy_without_duplicate12D5[42].append('X')
            umumiy_without_duplicate12D5[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D5[44].append('')
            umumiy_without_duplicate12D5[45].append('X')
            umumiy_without_duplicate12D5[46].append('')
            umumiy_without_duplicate12D5[47].append('X')
            umumiy_without_duplicate12D5[48].append(row['ch_combination'] + row['Тип покрытия'])
            umumiy_without_duplicate12D5[49].append('')

            if row['Тип покрытия'].capitalize() =='Белый':
                umumiy_without_duplicate12D5[50].append('S0')
            elif row['Тип покрытия'].capitalize() =='Неокрашенный':
                umumiy_without_duplicate12D5[50].append('S1')
            elif row['Тип покрытия'].capitalize() =='Окрашенный':
                umumiy_without_duplicate12D5[50].append('S2')
            elif row['Тип покрытия'].capitalize() =='Сублимированный':
                umumiy_without_duplicate12D5[50].append('S3')
            elif row['Тип покрытия'].capitalize() =='Ламинированный':
                umumiy_without_duplicate12D5[50].append('0001')
            elif row['Тип покрытия'].capitalize() =='Анодированный':
                umumiy_without_duplicate12D1[50].append('0001')
            

        if (('-F' not in row['SAP код S4P 100']) and ('-A' not in row['SAP код S4P 100'])):
            umumiy_without_duplicate1201[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate1201[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate1201[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate1201[3].append('ШТ')
            umumiy_without_duplicate1201[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate1201[5].append(gruppa_material)
            umumiy_without_duplicate1201[6].append(gruppa_material)
            umumiy_without_duplicate1201[7].append('E')
            umumiy_without_duplicate1201[8].append('01')
            umumiy_without_duplicate1201[9].append(str(row['Общий вес за штуку']).replace('.',','))
            umumiy_without_duplicate1201[10].append(str(row['Общий вес за штуку']).replace('.',','))
            umumiy_without_duplicate1201[11].append('КГ')
            umumiy_without_duplicate1201[12].append('NORM')
            umumiy_without_duplicate1201[13].append(row['Короткое название SAP'])
            umumiy_without_duplicate1201[14].append('ШТ')
            umumiy_without_duplicate1201[15].append('999')
            umumiy_without_duplicate1201[16].append('X')
            umumiy_without_duplicate1201[17].append('0000')
            umumiy_without_duplicate1201[18].append('PD')
            umumiy_without_duplicate1201[19].append('EX')
            umumiy_without_duplicate1201[20].append('0')
            umumiy_without_duplicate1201[21].append('E')
            ss =''
            sartrr =''
            if gruppa_material =='ALUGP':
                ss ='S400'
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
                bklast ='0102'
                
                
            umumiy_without_duplicate1201[22].append('')
            umumiy_without_duplicate1201[23].append('')
            umumiy_without_duplicate1201[24].append('M')
            umumiy_without_duplicate1201[25].append('02')
            umumiy_without_duplicate1201[26].append('10')
            umumiy_without_duplicate1201[27].append('')
            umumiy_without_duplicate1201[28].append('')
            umumiy_without_duplicate1201[29].append('')
            umumiy_without_duplicate1201[30].append('')
            umumiy_without_duplicate1201[31].append('')
            umumiy_without_duplicate1201[32].append('')
            umumiy_without_duplicate1201[33].append('10')
            umumiy_without_duplicate1201[34].append('1101')
            umumiy_without_duplicate1201[35].append('3')
            umumiy_without_duplicate1201[36].append(bklast)
            umumiy_without_duplicate1201[37].append('S')
            umumiy_without_duplicate1201[38].append('1')
            umumiy_without_duplicate1201[39].append(row['Price'])
            umumiy_without_duplicate1201[40].append('1101')
            umumiy_without_duplicate1201[41].append('X')
            umumiy_without_duplicate1201[42].append('X')
            umumiy_without_duplicate1201[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            sap_codee =row['SAP код S4P 100'].split('-')[0]
            if (sap_codee in zakalka_iskyucheniye):
                sap_code_simvol ='Z'
            umumiy_without_duplicate1201[44].append(SFSPF1101[sap_code_simvol])
            umumiy_without_duplicate1201[45].append('X')
            umumiy_without_duplicate1201[46].append('')
            umumiy_without_duplicate1201[47].append('X')
            umumiy_without_duplicate1201[48].append(row['ch_combination'] + row['Тип покрытия'])
            if (sap_codee in zakalka_iskyucheniye):
                umumiy_without_duplicate1201[49].append('JPZ')
            else:
                if ( (row['Тип покрытия'] =='Ламинированный') and ('-7' in row['SAP код S4P 100']) ):
                    umumiy_without_duplicate1201[49].append('JPL')
                elif (('-7' in row['SAP код S4P 100']) or ('-K' in row['SAP код S4P 100'])):
                    if row['ch_combination'].lower() == "с термомостом":
                        umumiy_without_duplicate1201[49].append('JPK')
                    else:
                        umumiy_without_duplicate1201[49].append('JPG')
                else:
                    umumiy_without_duplicate1201[49].append('JP1')
            
            if row['Тип покрытия'].capitalize() =='Белый':
                umumiy_without_duplicate1201[50].append('S0')
            elif row['Тип покрытия'].capitalize() =='Неокрашенный':
                umumiy_without_duplicate1201[50].append('S1')
            elif row['Тип покрытия'].capitalize() =='Окрашенный':
                umumiy_without_duplicate1201[50].append('S2')
            elif row['Тип покрытия'].capitalize() =='Сублимированный':
                umumiy_without_duplicate1201[50].append('S3')
            elif row['Тип покрытия'].capitalize() =='Ламинированный':
                umumiy_without_duplicate1201[50].append('S4')
            elif row['Тип покрытия'].capitalize() =='Анодированный':
                umumiy_without_duplicate12D1[50].append('0001')
            

    umumiy_without_duplicate =[[] for i in range(0,51)]
    for i in range(0,len(umumiy_without_duplicate1201)):
        umumiy_without_duplicate[i]+=umumiy_without_duplicate1201[i] 
            
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

    ########################## RAUBE.txt ##############################
    # header_raube='MAKTX\tMATNR\tRAUBE'
    
    # d9={}
    # d9['MAKTX']=[]
    # d9['MATNR']=[]
    # d9['RAUBE']=[]
    # i = 0
    
    # for row in umumiy_without_duplicate[0]:
    #     if '-7' in row:
    #         d9['MAKTX'].append(umumiy_without_duplicate[13][i])
    #         d9['MATNR'].append(umumiy_without_duplicate[0][i])
    #         d9['RAUBE'].append(umumiy_without_duplicate[50][i])
    #     if '-P' in row:
    #         d9['MAKTX'].append(umumiy_without_duplicate[13][i])
    #         d9['MATNR'].append(umumiy_without_duplicate[0][i])
    #         d9['RAUBE'].append(umumiy_without_duplicate[50][i])
    #     if '-K' in row:
    #         d9['MAKTX'].append(umumiy_without_duplicate[13][i])
    #         d9['MATNR'].append(umumiy_without_duplicate[0][i])
    #         d9['RAUBE'].append(umumiy_without_duplicate[50][i])
    #     i += 1

    # df9= pd.DataFrame(d9)
    # df9 = df9.drop_duplicates()
    # np.savetxt(pathtext9, df9.values,fmt='%s', delimiter="\t",header=header_raube,comments='',encoding='ansi')

    ########################## Бухгалтерская название.txt ##############################
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
    dlinniy_t['RU']=['RU' for x in dlinniy_text_zero[1]]
    dlinniy_t['GRUN']=['GRUN' for x in dlinniy_text_zero[1]]
    dlinniy_t['sa']=['' for x in dlinniy_text_zero[1]]
    dlinniy_t['TEXT']=dlinniy_text_zero[2]
    
    df_dlinniy_text= pd.DataFrame(dlinniy_t)
    
    np.savetxt(pathtext7, df_dlinniy_text.values,fmt='%s', delimiter="\t",header=header_dlinniy,comments='',encoding='ansi')
    
    
    ########################## end Длинный текс.txt ##############################


    ########################## 1.txt ##############################
    d1={}
    header1 ='MATNR\tBISMT\tMAKTX\tMEINS\tMTART\tMATKL\tWERKS\tBESKZ\tSPART\tBRGEW\tNTGEW\tGEWEI\tMTPOS_MARA'
    
    d1['MATNR']=umumiy_without_duplicate1201[0]
    d1['BISMT']=umumiy_without_duplicate1201[1]
    d1['MAKTX']=umumiy_without_duplicate1201[2]
    d1['MEINS']=umumiy_without_duplicate1201[3]
    d1['MTART']=umumiy_without_duplicate1201[4]
    d1['MATKL']=umumiy_without_duplicate1201[5]
    d1['WERKS']=umumiy_without_duplicate1201[34]
    d1['BESKZ']=umumiy_without_duplicate1201[7]
    d1['SPART']=umumiy_without_duplicate1201[8]
    d1['BRGEW']=[str(round(float(k1.replace(',','.')),3)).replace('.',',') for k1 in umumiy_without_duplicate1201[9]]
    d1['NTGEW']=[str(round(float(k2.replace(',','.')),3)).replace('.',',') for k2 in umumiy_without_duplicate1201[10]]
    d1['GEWEI']=umumiy_without_duplicate1201[11]
    d1['MTPOS_MARA']=umumiy_without_duplicate1201[12]
    
    
    df1= pd.DataFrame(d1)
    
    np.savetxt(pathtext1, df1.values,fmt='%s', delimiter="\t",header=header1,comments='',encoding='ansi')
    
    ########################## end 1.txt ##############################

    ########################## 2.txt ##############################
    header2='MAKTX\tMEINS\tMTART\tMATNR\tWERKS\tEKGRP\tXCHPF\tDISGR\tDISMM\tDISPO\tDISLS\tWEBAZ\tBESKZ\tLGFSB\tPLIFZ\tPERKZ\tMTVFP\tSCM_STRA1\tVRMOD\tPPSKZ\tSCM_WHATBOM\tSCM_HEUR_ID\tSCM_RRP_TYPE\tSCM_PROFID\tSTRGR\tBWKEY\tMLAST\tBKLAS\tVPRSV\tPEINH\tSTPRS\tPRCTR\tEKALR\tHKMAT\tLOSGR\tSFCPF\tFEVOR\tUEETK\tLGPRO\tAUTO_P_ORD'
    
    zavod_code_1101 ={
        '1103':'PVC',
        '1101':'PR1',
        '11D1':'001',
        '11D2':'001',
        '11D3':'001',
        '11D4':'001',
        '11D5':'001',
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
    d2['DISPO']=[zavod_code_1101[x] for x in umumiy_without_duplicate[34]]
    d2['DISLS']=umumiy_without_duplicate[19]
    d2['WEBAZ']=umumiy_without_duplicate[20]
    d2['BESKZ']=umumiy_without_duplicate[21]
    d2['LGFSB']=umumiy_without_duplicate[22]
    d2['PLIFZ']=umumiy_without_duplicate[23]
    d2['PERKZ']=umumiy_without_duplicate[24]
    d2['MTVFP']=umumiy_without_duplicate[25]
    d2['SCM_STRA1']=umumiy_without_duplicate[26]
    d2['VRMOD']=['' for x in umumiy_without_duplicate[27]]
    d2['PPSKZ']=['' for x in umumiy_without_duplicate[27]]
    d2['SCM_WHATBOM']= ['' for x in umumiy_without_duplicate[27]]
    d2['SCM_HEUR_ID']= ['' for x in umumiy_without_duplicate[27]]
    d2['SCM_RRP_TYPE']= ['' for x in umumiy_without_duplicate[27]]
    d2['SCM_PROFID']= ['' for x in umumiy_without_duplicate[27]]
    d2['STRGR']=umumiy_without_duplicate[33]
    d2['BWKEY']=umumiy_without_duplicate[34]
    d2['MLAST']=umumiy_without_duplicate[35]
    d2['BKLAS']=umumiy_without_duplicate[36]
    d2['VPRSV']=umumiy_without_duplicate[37]
    d2['PEINH']=umumiy_without_duplicate[38]
    d2['STPRS']=[round(n,2) for n in umumiy_without_duplicate[39]]
    d2['PRCTR']=umumiy_without_duplicate[40]
    d2['EKALR']=umumiy_without_duplicate[41]
    d2['HKMAT']=umumiy_without_duplicate[42]
    d2['LOSGR']=umumiy_without_duplicate[43]
    d2['SFCPF']=umumiy_without_duplicate[44]
    d2['FEVOR']=umumiy_without_duplicate[49]
    d2['UEETK']=umumiy_without_duplicate[45]
    d2['LGPRO']=umumiy_without_duplicate[46]
    d2['AUTO_P_ORD']=umumiy_without_duplicate[47]
    # d2['RAUBE']=umumiy_without_duplicate[50]

   
    df2= pd.DataFrame(d2)
    np.savetxt(pathtext2, df2.values,fmt='%s', delimiter="\t",header=header2,comments='',encoding='ansi')
    ########################## end 2.txt ##############################

    ########################## 3.txt ##############################
    header3 ='MAKTX\tMEINS\tMTART\tSPART\tMATNR\tWERKS\tVKORG\tMTPOS\tVTWEG\tPRCTR\tMTVFP\tALAND\tTATYP\tTAXKM\tVERSG\tKTGRM\tKONDM\tTRAGR\tLADGR'
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
        'TRAGR':[],
        'LADGR':[]
    }
    VTWEG =['99','10','20']
    KONDM ={
        'с термомостоманодированный':'A0',
        'без термомостаокрашенный':'A1',
        'без термомостабелый':'A1',
        'без термомостасублимированный':'A2',
        'без термомостаанодированный':'A3',
        'без термомосталаминированный':'A4',
        'с термомостомламинированный':'A5',
        'без термомостанеокрашенный':'A6',
        'с термомостомокрашенный':'A7',
        'с термомостомбелый':'A7',
        'с термомостомнеокрашенный':'A8',
        'с термомостомсублимированный':'A9',
    }
    for i in range(0,3):
        d3['MAKTX'] += umumiy_without_duplicate[13]
        d3['MEINS'] += umumiy_without_duplicate[14]
        d3['MTART'] += umumiy_without_duplicate[4]
        d3['SPART'] += umumiy_without_duplicate[8]
        d3['MATNR'] += umumiy_without_duplicate[0]
        d3['WERKS'] += umumiy_without_duplicate[34]
        d3['VKORG'] += [ 1100 for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['MTPOS'] += umumiy_without_duplicate[12]
        d3['VTWEG'] += [ VTWEG[i] for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['PRCTR'] += [ '1103' if umumiy_without_duplicate[34][i] =='1103' else '1101' for i in range(0,len(umumiy_without_duplicate[34]))]
        d3['MTVFP'] += [ '02' for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['ALAND'] += [ 'UZ' for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['TATYP'] += [ 'MWST' for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['TAXKM'] += [ '1' for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['VERSG'] += [ '1' for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['KTGRM'] += [ '01' for j in range(0,len(umumiy_without_duplicate[13]))]
        if i!=2:
            d3['KONDM'] += [ '01' for j in range(0,len(umumiy_without_duplicate[13]))]
        else:
            d3['KONDM'] += [ '01' if '-7' not in umumiy_without_duplicate[0][x] else KONDM[umumiy_without_duplicate[48][x].lower()] for x in range(0,len(umumiy_without_duplicate[0]))]
            
        d3['TRAGR'] += [ '0001' for j in range(0,len(umumiy_without_duplicate[13]))]
        
        ladgr =[]
        j = 0
        for sap_code in umumiy_without_duplicate[0]:
            if (('-7' in sap_code ) or ('-P' in sap_code ) or ('-K' in sap_code )):
                if umumiy_without_duplicate[34][j]=='1101':
                    if umumiy_without_duplicate[50][j]!='0001':
                        ladgr.append('11' + umumiy_without_duplicate[50][j])
                    else:
                        ladgr.append(umumiy_without_duplicate[50][j])
                else:
                    ladgr.append('0001')

            else:
                ladgr.append('0001')
            j += 1

        d3['LADGR'] += ladgr
    df3= pd.DataFrame(d3)
    np.savetxt(pathtext3, df3.values, fmt='%s', delimiter="\t",header=header3,comments='',encoding='ansi')
    ########################## end 3.txt ##############################
    
    ########################## 4.txt ##############################    
    new_ll =[[],[],[],[]]
    sap_code_title =[]
    dlina_title =[]
    obshiy_ves_za_shtuku =[]
    wms_width =[]
    wms_height =[]
    
    for key , row in datas.iterrows():
        if (('-E' in row['SAP код S4P 100']) and (row['SAP код S4P 100'] not in elist)):
            continue
        sap_code_title.append(row['SAP код S4P 100'])
        dlina_title.append(row['Длина'])
        obshiy_ves_za_shtuku.append(row['Общий вес за штуку'])
        wms_width.append(row['WMS_WIDTH'])
        wms_height.append(row['WMS_HEIGHT'])

        
        raube_txt = ''

        if row['Тип покрытия'].capitalize() =='Белый':
            raube_txt = 'S0'
        elif row['Тип покрытия'].capitalize() =='Неокрашенный':
            raube_txt = 'S1'
        elif row['Тип покрытия'].capitalize() =='Окрашенный':
            raube_txt = 'S2'
        elif row['Тип покрытия'].capitalize() =='Сублимированный':
            raube_txt = 'S3'
        elif row['Тип покрытия'].capitalize() =='Ламинированный':
            raube_txt = 'S4'

        sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]        
        if sap_code_simvol =='E':
            for i in range(0,len(LGORT_1101['E'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT_1101['E'][i]['zavod_code'])
                new_ll[2].append(LGORT_1101['E'][i]['zavod_sap'])
                new_ll[3].append('')

        if sap_code_simvol =='Z':
            for i in range(0,len(LGORT_1101['Z'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT_1101['Z'][i]['zavod_code'])
                new_ll[2].append(LGORT_1101['Z'][i]['zavod_sap'])
                new_ll[3].append('')
        if sap_code_simvol =='P':
            for i in range(0,len(LGORT_1101['P'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT_1101['P'][i]['zavod_code'])
                new_ll[2].append(LGORT_1101['P'][i]['zavod_sap'])
                new_ll[3].append(raube_txt)
        
        if sap_code_simvol =='S':
            for i in range(0,len(LGORT_1101['S'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT_1101['S'][i]['zavod_code'])
                new_ll[2].append(LGORT_1101['S'][i]['zavod_sap'])
                new_ll[3].append('')
        if RazlovkaTermo.objects.filter(nsap_code =row['SAP код S4P 100']).exists():
            if sap_code_simvol =='N':
                for i in range(0,len(LGORT_1101['N'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT_1101['N'][i]['zavod_code'])
                    new_ll[2].append(LGORT_1101['N'][i]['zavod_sap'])
                    new_ll[3].append('')
        if sap_code_simvol =='K':
            for i in range(0,len(LGORT_1101['K'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT_1101['K'][i]['zavod_code'])
                new_ll[2].append(LGORT_1101['K'][i]['zavod_sap'])
                new_ll[3].append(raube_txt)
        
        
        if sap_code_simvol =='7':
            for i in range(0,len(LGORT_1101['7'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT_1101['7'][i]['zavod_code'])
                new_ll[2].append(LGORT_1101['7'][i]['zavod_sap'])
                if LGORT_1101['7'][i]['zavod_code'] =='1101':
                    new_ll[3].append(raube_txt)
                else:
                    new_ll[3].append('')
            
        
        
    header4='MATNR\tWERKS\tLGORT\tRAUBE'
    d4={}
    d4['MATNR']=new_ll[0]
    d4['WERKS']=new_ll[1]
    d4['LGORT']=new_ll[2]
    d4['RAUBE']=new_ll[3]
    df4= pd.DataFrame(d4)
  
    np.savetxt(pathtext4, df4.values, fmt='%s', delimiter="\t",header=header4,comments='',encoding='ansi')
    ########################## end 4.txt ##############################

    ########################## 55.txt ##############################    
    new_ll_55 =[[],[],[],[]]
    
    for key , row in datas.iterrows():
        if (('-E' in row['SAP код S4P 100']) and (row['SAP код S4P 100'] not in elist)):
            continue
        sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]   

        raube_txt = ''
        
        if row['Тип покрытия'].capitalize() =='Белый':
            raube_txt = 'S0'
        elif row['Тип покрытия'].capitalize() =='Неокрашенный':
            raube_txt = 'S1'
        elif row['Тип покрытия'].capitalize() =='Окрашенный':
            raube_txt = 'S2'
        elif row['Тип покрытия'].capitalize() =='Сублимированный':
            raube_txt = 'S3'
        elif row['Тип покрытия'].capitalize() =='Ламинированный':
            raube_txt = 'S4'     

        if sap_code_simvol =='7':
            
            for i in range(0,len(LGORT_1101['7'])):
                if LGORT_1101['7'][i]['zavod_code'] =='1101':
                    new_ll_55[0].append(row['SAP код S4P 100'])
                    new_ll_55[1].append(LGORT_1101['7'][i]['zavod_code'])
                    new_ll_55[2].append(LGORT_1101['7'][i]['zavod_sap'])
                    if LGORT_1101['7'][i]['zavod_code'] =='1101':
                        new_ll_55[3].append(raube_txt)
                    else:
                        new_ll_55[3].append('')

    header55='MATNR\tWERKS\tRAUBE'
    d55={}
    d55['MATNR']=new_ll_55[0] 
    d55['WERKS']=new_ll_55[1]  
    d55['RAUBE']=new_ll_55[3] 
    df55= pd.DataFrame(d55)
    df55=df55.drop_duplicates()
    np.savetxt(pathtext55, df55.values, fmt='%s', delimiter="\t",header=header55,comments='',encoding='ansi')
    ########################## end 55.txt ##############################
    
    ########################## 5.txt ##############################
    d5 ={
        'sap_code':[],
        'ed_iz1':[],
        'ed_iz2':[],
        'ed_iz3':[],
        'ed_iz4':[],
        'ed_iz5':[],
        'ed_iz6':[],
        'ed_iz7':[]
    }
    ED_IZM =['ШТ','М','КГ']
    
    # sap_code_title =[]
    # dlina_title =[]
    # obshiy_ves_za_shtuku =[]
    # wms_width =[]
    # wms_height =[]
    ed_iz3 =[]
    for i in range(0,3):
        if i == 0 :
            ed_iz3 += ['1' for j in range(0,len(sap_code_title)) ]
        elif i == 1 :
            ed_iz3 += [j for j in dlina_title ]
        elif i == 2 :
            ed_iz3 += [int(float(str(j).replace(',','.'))*1000) for j in obshiy_ves_za_shtuku ]
            
    
    for i in ED_IZM:    
        d5['sap_code'] += sap_code_title
        d5['ed_iz1'] += [ i for j in range(0,len(sap_code_title))]
        d5['ed_iz2'] +=['1' if i =='ШТ' else '1000'  for j in range(0,len(sap_code_title)) ]
        # d5['ed_iz3'] +=['1' if i =='ШТ' elif i=='М' for j in range(0,len(sap_code_title)) ]
        d5['ed_iz4'] +=[j for j in dlina_title ]
        d5['ed_iz5'] +=[j for j in wms_height ]
        d5['ed_iz6'] +=[j for j in wms_width ]
        d5['ed_iz7'] +=[ 'мм' for j in range(0,len(sap_code_title))]
    
    d5['ed_iz3'] = ed_iz3
    df5= pd.DataFrame(d5)
    np.savetxt(pathtext5, df5.values, fmt='%s', delimiter="\t",encoding='ansi')
    ########################## end 5.txt ##############################
    ########################## List v 3 ##############################
    dd2 = [[],[],[],[],[],[]]
    baza_profile_links =[[],[]]

    for key , row in datas.iterrows():

        if (('-E' in row['SAP код S4P 100']) and (row['SAP код S4P 100'] not in elist)):
            continue

        if not RazlovkaTermo.objects.filter(nsap_code =row['SAP код S4P 100']).exists():
            if '-N' in row['SAP код S4P 100']:
                continue

        sap_code = row['SAP код S4P 100'].split('-')[0]
        bazaprofiley =AluProfilesData.objects.filter(Q(data__Артикул =sap_code)|Q(data__Компонент=sap_code))[:1].get()   
        baza_profile_links[0].append(row['SAP код S4P 100'])
        baza_profile_links[1].append(bazaprofiley.data['Ссылка для чертежей'])

        row['ch_tnved'] =str(row['ch_tnved']).replace('.0','')
        row['ch_outer_side_pc_id'] =str(row['ch_outer_side_pc_id']).replace('.0','')
        row['ch_outer_side_pc_brand'] =str(row['ch_outer_side_pc_brand']).replace('.0','')
        row['ch_inner_side_pc_id'] =str(row['ch_inner_side_pc_id']).replace('.0','')
        row['ch_inner_side_pc_brand'] =str(row['ch_inner_side_pc_brand']).replace('.0','')
        row['ch_outer_side_wg_s_id'] =str(row['ch_outer_side_wg_s_id']).replace('.0','')
        row['ch_inner_side_wg_s_id'] =str(row['ch_inner_side_wg_s_id']).replace('.0','')
        row['ch_outer_side_wg_id'] =str(row['ch_outer_side_wg_id']).replace('.0','')
        row['ch_inner_side_wg_id'] =str(row['ch_inner_side_wg_id']).replace('.0','')
        row['ch_width'] =str(row['ch_width']).replace('.0','')
        row['ch_height'] =str(row['ch_height']).replace('.0','')
        
        if '-7' in row['SAP код S4P 100']:
            for j in range(0,35):
                dd2[0].append('001')
            dd2[0].append('023')
                
            for j in range(0,33):
                if HEADER[j] not in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT','TNVED']:
                    dd2[1].append('ALUMINIUM_PROFILE')
                else:
                    if HEADER[j] in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT']:
                        dd2[1].append('RAWMAT_TYPE')
                    elif HEADER[j] =='TNVED':
                        dd2[1].append('TNVED')
            
           

            dd2[1].append('QBIC')
            dd2[1].append('QBIC')
            dd2[1].append('ZPP_023_FERT')
        
            for j in range(0,36):
                dd2[2].append('MARA')
                
            for j in range(0,36):
                dd2[3].append(row['SAP код S4P 100'])
                
            for j in HEADER:
                dd2[4].append(j)
            
            dd2[4].append('AMOUNT_IN_A_PACKAGE')
            dd2[4].append('COATING_QBIC')
            dd2[4].append('ZBATCH_NUM')

            dd2[5].append('')
            dd2[5].append('')
            dd2[5].append(row['ch_system'])
            dd2[5].append(row['SAP код S4P 100'].split('-')[0])
            dd2[5].append(row['Длина'])
            dd2[5].append(row['Тип покрытия'])
            dd2[5].append(row['ch_alloy'])
            dd2[5].append(row['ch_temper'])
            dd2[5].append(row['ch_combination'])
            dd2[5].append(row['ch_outer_side_pc_id'])
            dd2[5].append(row['ch_outer_side_pc_brand'])
            dd2[5].append(row['ch_inner_side_pc_id'])
            dd2[5].append(row['ch_inner_side_pc_brand'])
            dd2[5].append(row['ch_outer_side_wg_s_id'])
            dd2[5].append(row['ch_inner_side_wg_s_id'])
            dd2[5].append(row['ch_outer_side_wg_id'])
            dd2[5].append(row['ch_inner_side_wg_id'])
            if row['ch_anodization_contact'].lower() =='yc':
                dd2[5].append('С КОНТАКТОМ')
            elif row['ch_anodization_contact'].lower()=='nc' :
                dd2[5].append('БЕЗ КОНТАКТА')
            else:
                dd2[5].append(row['ch_anodization_contact'])

            dd2[5].append(row['ch_anodization_type'])
            dd2[5].append(row['ch_anodization_method'])
            dd2[5].append(row['ch_print_view'])
            dd2[5].append(row['ch_profile_base'])
            dd2[5].append(row['ch_width'])
            dd2[5].append(row['ch_height'])
            dd2[5].append(row['ch_category'])
            dd2[5].append(row['ch_rawmat_type'])
            dd2[5].append('')
            dd2[5].append(row['ch_tnved'])
            dd2[5].append(str(row['ch_surface_treatment_export']).replace('.0',''))
            dd2[5].append(row['WMS_WIDTH'])
            dd2[5].append(row['WMS_HEIGHT'])
            dd2[5].append('')
            dd2[5].append(bazaprofiley.data['Тип Комбинация'])
            artikul_for_qbic = row['SAP код S4P 100'].split('-')[0]
            if Norma.objects.filter(Q(артикул=artikul_for_qbic)&~Q(упаковка_колво_профилей_в_1_пачке ='0')).exists():
                qbicc = Norma.objects.filter(Q(артикул=artikul_for_qbic)&~Q(упаковка_колво_профилей_в_1_пачке ='0'))[:1].get().упаковка_колво_профилей_в_1_пачке
                dd2[5].append(qbicc)
            else:
                dd2[5].append('XXXX')
           
            if row['Тип покрытия'] =='Неокрашенный':
                qbic ='XXXX'
            elif row['Тип покрытия'] =='Окрашенный':
                qbic = row['ch_outer_side_pc_id']
            elif row['Тип покрытия'] =='Анодированный':
                qbic = row['ch_outer_side_pc_id']
            elif row['Тип покрытия'] =='Ламинированный':
                if row['ch_outer_side_wg_id'] =='XXXX':
                    qbic = row['ch_inner_side_wg_id']
                else:
                    qbic = row['ch_outer_side_wg_id']
            elif row['Тип покрытия'] =='Сублимированный':
                qbic = row['ch_outer_side_wg_s_id']
            else:
                qbic ='XXXX'

            dd2[5].append(qbic)
            dd2[5].append('XXXX')
        else:
            for j in range(0,33):
                dd2[0].append('001')
            dd2[0].append('023')
                
            for j in range(0,33):
                if HEADER[j] not in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT','TNVED']:
                    dd2[1].append('ALUMINIUM_PROFILE')
                else:
                    if HEADER[j] in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT']:
                        dd2[1].append('RAWMAT_TYPE')
                    elif HEADER[j] =='TNVED':
                        dd2[1].append('TNVED')
            dd2[1].append('ZPP_023_HALB')
            for j in range(0,34):
                dd2[2].append('MARA')
                
            for j in range(0,34):
                dd2[3].append(row['SAP код S4P 100'])
                
            for j in HEADER:
                dd2[4].append(j)
            dd2[4].append('ZBATCH_NUM')

            dd2[5].append('')
            dd2[5].append('')
            dd2[5].append(row['ch_system'])
            dd2[5].append(row['SAP код S4P 100'].split('-')[0])
            dd2[5].append(row['Длина'])
            dd2[5].append(row['Тип покрытия'])
            dd2[5].append(row['ch_alloy'])
            dd2[5].append(row['ch_temper'])
            dd2[5].append(row['ch_combination'])
            dd2[5].append(row['ch_outer_side_pc_id'])
            dd2[5].append(row['ch_outer_side_pc_brand'])
            dd2[5].append(row['ch_inner_side_pc_id'])
            dd2[5].append(row['ch_inner_side_pc_brand'])
            dd2[5].append(row['ch_outer_side_wg_s_id'])
            dd2[5].append(row['ch_inner_side_wg_s_id'])
            dd2[5].append(row['ch_outer_side_wg_id'])
            dd2[5].append(row['ch_inner_side_wg_id'])
            dd2[5].append(row['ch_anodization_contact'])
            dd2[5].append(row['ch_anodization_type'])
            dd2[5].append(row['ch_anodization_method'])
            dd2[5].append(row['ch_print_view'])
            dd2[5].append(row['ch_profile_base'])
            dd2[5].append(row['ch_width'])
            dd2[5].append(row['ch_height'])
            dd2[5].append(row['ch_category'])
            dd2[5].append(row['ch_rawmat_type'])
            dd2[5].append('')
            dd2[5].append(row['ch_tnved'])
            dd2[5].append(str(row['ch_surface_treatment_export']).replace('.0',''))
            dd2[5].append(row['WMS_WIDTH'])
            dd2[5].append(row['WMS_HEIGHT'])
            dd2[5].append('')
            dd2[5].append(bazaprofiley.data['Тип Комбинация'])
            dd2[5].append('XXXX')

    new_date={}       
    new_date['Вид класса'] = dd2[0]
    new_date['Класс'] = dd2[1]
    new_date['Таблица'] = dd2[2]
    new_date['Объект'] = dd2[3]

    new_date['Имя признака'] = dd2[4]
    new_date['Значение признака'] = dd2[5]
    new_date['Статус загрузки'] = ''
    
    df_baza_profiley_link =pd.DataFrame({'SAP CODE':baza_profile_links[0],'link':baza_profile_links[1]})
    df_baza_profiley_link.to_excel(pathtext10,index=False)

    ddf2 = pd.DataFrame(new_date)
    ddf2 = ddf2[((ddf2["Значение признака"] != "nan") & (ddf2["Значение признака"] != ""))]
    ddf2 =ddf2.replace('XXXX','')
    ddf2.to_excel(pathtext6,index=False)
    
    return [pathtext1,pathtext2,pathtext3,pathtext4,pathtext5,pathtext6,pathtext7,pathtext8,pathtext9,pathtext10],pathzip
    #########################################################################################################################
    ###############################################################################################################
    #######################################################################################



def fabrikatsiya_sap_kod(sap_kod,length):
    new =sap_kod.split(' ')
    for i in range(0,len(new)):
        if new[i].startswith('L'):
            new[i]=f'L{length}'
    return ' '.join(new)


def create_folder(parent_dir,directory):
    path =os.path.join(parent_dir,directory)
    if not os.path.isdir(path):
        os.mkdir(path) 


def create_characteristika(items):
    
    all_data =[
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
            sap_code =item['material'],
            kratkiy_text =item['kratkiy'],
            section =item['section'],
            savdo_id ='',
            savdo_name ='',
            export_customer_id = item['export_customer_id'],
            system = item['system'],
            article = item['article'],
            length = item['length'],
            surface_treatment = item['surface_treatment'],
            alloy = item['alloy'],
            temper = item['temper'],
            combination = item['combination'],
            outer_side_pc_id = item['outer_side_pc_id'],
            outer_side_pc_brand = item['outer_side_pc_brand'],
            inner_side_pc_id = item['inner_side_pc_id'],
            inner_side_pc_brand = item['inner_side_pc_brand'],
            outer_side_wg_s_id = item['outer_side_wg_s_id'],
            inner_side_wg_s_id = item['inner_side_wg_s_id'],
            outer_side_wg_id = item['outer_side_wg_id'],
            inner_side_wg_id = item['inner_side_wg_id'],
            anodization_contact = item['anodization_contact'],
            anodization_type = item['anodization_type'],
            anodization_method = item['anodization_method'],
            print_view = item['print_view'],
            profile_base = item['profile_base'],
            width = item['width'],
            height = item['height'],
            category = item.get('category',''),
            rawmat_type = item['rawmat_type'],
            benkam_id = item.get('benkam_id',''),
            hollow_and_solid = item.get('hollow_and_solid',''),
            export_description = item.get('export_description',''),
            export_description_eng = item.get('export_description_eng',''),
            tnved = item.get('tnved',''),
            surface_treatment_export = item.get('surface_treatment_export',''),
            wms_width = item['wms_width'],
            wms_height = item['wms_height'],
            group_prise = item['group_prise'],
            )
        character.save()
        
        if character.sap_code =='nan':
            character.sap_code=''
        if character.kratkiy_text =='nan':
            character.kratkiy_text=''
        if character.section =='nan':
            character.section=''
        if character.savdo_id =='nan':
            character.savdo_id=''
        if character.savdo_name =='nan':
            character.savdo_name=''
        if character.export_customer_id =='nan':
            character.export_customer_id=''
        if character.system =='nan':
            character.system=''
        if character.article =='nan':
            character.article=''
        if character.length =='nan':
            character.length=''
        if character.surface_treatment =='nan':
            character.surface_treatment=''
        if character.alloy =='nan':
            character.alloy=''
        if character.temper =='nan':
            character.temper=''
        if character.combination =='nan':
            character.combination=''
        if character.outer_side_pc_id =='nan':
            character.outer_side_pc_id=''
        if character.outer_side_pc_brand =='nan':
            character.outer_side_pc_brand=''
        if character.inner_side_pc_id =='nan':
            character.inner_side_pc_id=''
        if character.inner_side_pc_brand =='nan':
            character.inner_side_pc_brand=''
        if character.outer_side_wg_s_id =='nan':
            character.outer_side_wg_s_id=''
        if character.inner_side_wg_s_id =='nan':
            character.inner_side_wg_s_id=''
        if character.outer_side_wg_id =='nan':
            character.outer_side_wg_id=''
        if character.inner_side_wg_id =='nan':
            character.inner_side_wg_id=''
        if character.anodization_contact =='nan':
            character.anodization_contact=''
        if character.anodization_type =='nan':
            character.anodization_type=''
        if character.anodization_method =='nan':
            character.anodization_method=''
        if character.print_view =='nan':
            character.print_view=''
        if character.profile_base =='nan':
            character.profile_base=''
        if character.width =='nan':
            character.width=''
        if character.height =='nan':
            character.height=''
        if character.category =='nan':
            character.category=''
        if character.rawmat_type =='nan':
            character.rawmat_type=''
        if character.benkam_id =='nan':
            character.benkam_id=''
        if character.hollow_and_solid =='nan':
            character.hollow_and_solid=''
        if character.export_description =='nan':
            character.export_description=''
        if character.export_description_eng =='nan':
            character.export_description_eng=''
        if character.tnved =='nan':
            character.tnved=''
        if character.surface_treatment_export =='nan':
            character.surface_treatment_export=''
        if character.wms_width == 'nan':
            character.wms_width=''
        if character.wms_height == 'nan':
            character.wms_height=''
        if character.group_prise == 'nan':
            character.group_prise = ''
        
        all_data[0].append(character.sap_code)
        all_data[1].append(character.kratkiy_text)
        all_data[2].append(character.section)
        all_data[3].append(character.savdo_id)
        all_data[4].append(character.savdo_name)
        all_data[5].append(character.export_customer_id)
        all_data[6].append(character.system)
        all_data[7].append(character.article)
        all_data[8].append(character.length)
        all_data[9].append(character.surface_treatment)
        all_data[10].append(character.alloy)
        all_data[11].append(character.temper)
        all_data[12].append(character.combination)
        all_data[13].append(character.outer_side_pc_id)
        all_data[14].append(character.outer_side_pc_brand)
        all_data[15].append(character.inner_side_pc_id)
        all_data[16].append(character.inner_side_pc_brand)
        all_data[17].append(character.outer_side_wg_s_id)
        all_data[18].append(character.inner_side_wg_s_id)
        all_data[19].append(character.outer_side_wg_id)
        all_data[20].append(character.inner_side_wg_id)
        all_data[21].append(character.anodization_contact)
        all_data[22].append(character.anodization_type)
        all_data[23].append(character.anodization_method)
        all_data[24].append(character.print_view)
        all_data[25].append(character.profile_base)
        all_data[26].append(character.width)
        all_data[27].append(character.height)
        all_data[28].append(character.category)
        all_data[29].append(character.rawmat_type)
        all_data[30].append(character.benkam_id)
        all_data[31].append(character.hollow_and_solid)
        all_data[32].append(character.export_description)
        all_data[33].append(character.export_description_eng)
        all_data[34].append(character.tnved.replace('.0',''))
        all_data[35].append(character.surface_treatment_export)
        all_data[36].append(character.wms_width.replace('.0',''))
        all_data[37].append(character.wms_height.replace('.0',''))
        



    df_new ={
        'SAP CODE' : all_data[0],
        'KRATKIY TEXT': all_data[1],
        'SECTION': all_data[2],
        'SAVDO_ID': all_data[3],
        'SAVDO_NAME': all_data[4],
        'EXPORT_CUSTOMER_ID': all_data[5],
        'SYSTEM': all_data[6],
        'ARTICLE': all_data[7],
        'LENGTH': all_data[8],
        'SURFACE_TREATMENT': all_data[9],
        'ALLOY': all_data[10],
        'TEMPER': all_data[11],
        'COMBINATION': all_data[12],
        'OUTER_SIDE_PC_ID': all_data[13],
        'OUTER_SIDE_PC_BRAND': all_data[14],
        'INNER_SIDE_PC_ID': all_data[15],
        'INNER_SIDE_PC_BRAND': all_data[16],
        'OUTER_SIDE_WG_S_ID': all_data[17],
        'INNER_SIDE_WG_S_ID': all_data[18],
        'OUTER_SIDE_WG_ID': all_data[19],
        'INNER_SIDE_WG_ID': all_data[20],
        'ANODIZATION_CONTACT': all_data[21],
        'ANODIZATION_TYPE': all_data[22],
        'ANODIZATION_METHOD': all_data[23],
        'PRINT_VIEW': all_data[24],
        'PROFILE_BASE': all_data[25],
        'WIDTH': all_data[26],
        'HEIGHT': all_data[27],
        'CATEGORY': all_data[28],
        'RAWMAT_TYPE': all_data[29],
        'BENKAM_ID': all_data[30],
        'HOLLOW AND SOLID': all_data[31],
        'EXPORT_DESCRIPTION': all_data[32],
        'EXPORT_DESCRIPTION ENG': all_data[33],
        'TNVED': all_data[34],
        'SURFACE_TREATMENT_EXPORT': all_data[35],
        'WMS_WIDTH': all_data[36],
        'WMS_HEIGHT': all_data[37]
    }
    
    df_charakter = pd.DataFrame(df_new)
    df_charakter =df_charakter.replace('nan','')
    return df_charakter   


def char_title_import(items):
    for key,row in items.iterrows():
        characteristik = CharacteristicTitle.objects.filter(sap_код_s4p_100 = row['SAP код S4P 100'])[:1].get()
        characteristik.удельный_вес_за_метр = row['Удельный вес за метр']
        characteristik.общий_вес_за_штуку = row['Общий вес за штуку'],
        characteristik.price = row['Price']
        characteristik.save()


def create_characteristika_utils(items):
    df =[
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[]
    ]
    
    # nakleyka_codes =[ code[0] for code in NakleykaCode.objects.values_list('name')]
    
    # bazaprofiley_link =[[],[]]
    
    for item in items:
        if '-L' in item['material']:
            continue
        
        # krat_nak_code = item['kratkiy'][-3:]
        # if krat_nak_code not in nakleyka_codes:
        #     item['print_view'] = ''
        
        
        
        sap_kode =item['material'].split('-')[0]
        baza_profiey = AluProfilesData.objects.filter(Q(data__Артикул=sap_kode)|Q(data__Компонент=sap_kode))[:1].get()
        

        if (('-7' in item['material']) or ('-K' in item['material']) or ('-L'  in item['material'])):
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
        короткое_название_sap =item['kratkiy']
        польное_наименование_sap = 'Алюминиевый '+baza_profiey.data['Product description - RUS'] +', '+component_name +' '+sap_kode+', '+item['surface_treatment']+', Длина '+item['length']+' мм, Тип '+item['alloy']+'-'+item['temper']+' '+item['print_view']
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
        tip_pokritiya =item['surface_treatment']
        wms_width =item['wms_width'].replace('.0','')
        wms_height =item['wms_height'].replace('.0','')
        
        ########Characteristica variables############
        ch_material = item['material']
        ch_kratkiy = item['kratkiy']
        ch_section = item['section']
        ch_export_customer_id = item['export_customer_id']
        ch_system = item['system']
        ch_article = item['article']
        ch_alloy = item['alloy']
        ch_temper = item['temper']
        ch_combination = item['combination']
        ch_outer_side_pc_id = item['outer_side_pc_id']
        ch_outer_side_pc_brand = item['outer_side_pc_brand']
        ch_inner_side_pc_id = item['inner_side_pc_id']
        ch_inner_side_pc_brand = item['inner_side_pc_brand']
        ch_outer_side_wg_s_id = item['outer_side_wg_s_id']
        ch_inner_side_wg_s_id = item['inner_side_wg_s_id']
        ch_outer_side_wg_id = item['outer_side_wg_id']
        ch_inner_side_wg_id = item['inner_side_wg_id']
        ch_anodization_contact = item['anodization_contact']
        ch_anodization_type = item['anodization_type']
        ch_anodization_method = item['anodization_method']
        ch_print_view = item['print_view']
        ch_profile_base = item['profile_base']
        ch_width = item.get('width','')
        if ch_width !='':
            ch_width =ch_width.replace('.0','')
        ch_height = item.get('height','')
        if ch_height !='':
            ch_height =ch_height.replace('.0','')
        
        ch_category = ''
        ch_rawmat_type = item['rawmat_type']
        ch_hollow_and_solid = item.get('hollow_and_solid','')
        ch_export_description = item.get('export_description','')
        ch_export_description_eng = item.get('export_description_eng','')
        ch_tnved = item.get('tnved','')
        ch_surface_treatment_export = item.get('surface_treatment_export','')
        
        
        ########End Characteristica variables############
        
        
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
        
        df[0].append(characteristik.дата_изменение_добавление)
        df[1].append(characteristik.статус_изменение_добавление)
        df[2].append(characteristik.ссылки_для_чертежа)
        df[3].append(characteristik.sap_код_s4p_100)
        df[4].append(characteristik.нумерация_до_sap)
        df[5].append(characteristik.короткое_название_sap)

        df[6].append(characteristik.польное_наименование_sap)
        df[7].append(characteristik.ед_изм)
        df[8].append(characteristik.альтернативная_ед_изм)
        df[9].append(characteristik.коэфициент_пересчета)
        df[10].append(characteristik.участок)
        df[11].append(characteristik.альтернативный_участок)
        df[12].append(characteristik.длина)
        
        df[13].append(characteristik.ширина)
        df[14].append(characteristik.высота)
        df[15].append(characteristik.группа_материалов)
        df[16].append(characteristik.удельный_вес_за_метр)
        df[17].append(characteristik.общий_вес_за_штуку)
        df[18].append(tip_pokritiya)
        df[19].append(wms_width)
        df[20].append(wms_height)
        
        df[21].append(ch_material)
        df[22].append(ch_kratkiy)
        df[23].append(ch_section)
        df[24].append(ch_export_customer_id)
        df[25].append(ch_system)
        df[26].append(ch_article)
        df[27].append(ch_alloy)
        df[28].append(ch_temper)
        df[29].append(ch_combination)
        df[30].append(ch_outer_side_pc_id)
        df[31].append(ch_outer_side_pc_brand)
        df[32].append(ch_inner_side_pc_id)
        df[33].append(ch_inner_side_pc_brand)
        df[34].append(ch_outer_side_wg_s_id)
        df[35].append(ch_inner_side_wg_s_id)
        df[36].append(ch_outer_side_wg_id)
        df[37].append(ch_inner_side_wg_id)
        df[38].append(ch_anodization_contact)
        df[39].append(ch_anodization_type)
        df[40].append(ch_anodization_method)
        df[41].append(ch_print_view)
        df[42].append(ch_profile_base)
        df[43].append(ch_width)
        df[44].append(ch_height)
        df[45].append(ch_category)
        df[46].append(ch_rawmat_type)
        df[47].append(ch_hollow_and_solid)
        df[48].append(ch_export_description)
        df[49].append(ch_export_description_eng)
        df[50].append(ch_tnved)
        df[51].append(ch_surface_treatment_export)
        sap_kode =item['material'].split('-')[0]
        df[52].append('')
        df[53].append(item['nazvaniye_export'])
        df[54].append(item['online_savdo_name'])

        
    dat = {
        'Дата изменение добавление':df[0],
        'Статус изменение добавление':df[1],
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
        'Общий вес за штуку':df[17],
        'Price':df[17],
        'Тип покрытия':df[18],
        'WMS_WIDTH':df[19],
        'WMS_HEIGHT':df[20],
        'ch_material': df[21],
        'ch_kratkiy': df[22],
        'ch_section': df[23],
        'ch_export_customer_id': df[24],
        'ch_system': df[25],
        'ch_article': df[26],
        'ch_alloy': df[27],
        'ch_temper': df[28],
        'ch_combination': df[29],
        'ch_outer_side_pc_id': df[30],
        'ch_outer_side_pc_brand': df[31],
        'ch_inner_side_pc_id': df[32],
        'ch_inner_side_pc_brand': df[33],
        'ch_outer_side_wg_s_id': df[34],
        'ch_inner_side_wg_s_id': df[35],
        'ch_outer_side_wg_id': df[36],
        'ch_inner_side_wg_id': df[37],
        'ch_anodization_contact': df[38],
        'ch_anodization_type': df[39],
        'ch_anodization_method': df[40],
        'ch_print_view': df[41],
        'ch_profile_base': df[42],
        'ch_width': df[43],
        'ch_height': df[44],
        'ch_category': df[45],
        'ch_rawmat_type': df[46],
        'ch_hollow_and_solid': df[47],
        'ch_export_description': df[48],
        'ch_export_description_eng': df[49],
        'ch_tnved': df[50],
        'ch_surface_treatment_export': df[51],
        'ch_artikul_old': df[52],
        'nazvaniye_export':df[53],
        'online_savdo_name' :df[54],
    }
    df_new = pd.DataFrame(dat)
    
    # baza_link ={
    #     'Номер материала':bazaprofiley_link[0],
    #     'Ссылка на чертеж':bazaprofiley_link[1]
    # }
    # df_link = pd.DataFrame(baza_link)

    return df_new



    



def characteristika_created_txt_create_1301(datas):
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR %M %S")
    minut =now.strftime("%M-%S MINUT")
    
   
            
    create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo',f"{year}")
    create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}',f'{hour} ТЕРМО')
    create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО','IMZO')
    create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\IMZO',minut)
    pathtext1 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\IMZO\\{minut}\\1.txt'
    pathtext2 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\IMZO\\{minut}\\2.txt'
    pathtext3 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\IMZO\\{minut}\\3.txt'
    pathtext4 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\IMZO\\{minut}\\4.txt'
    pathtext6 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\IMZO\\{minut}\\Лист в C 3.xlsx'
    pathzip =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО'
        
    # elif file_name =='aluminiy':
    #     parent_dir ='{MEDIA_ROOT}\\uploads\\aluminiy\\'
        
    #     if not os.path.isdir(parent_dir):
    #         create_folder(f'{MEDIA_ROOT}\\uploads','aluminiy')
            
    #     create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy',f'{year}')
    #     create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}',f'{month}')
    #     create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}',day)
    #     create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}',f'{hour} ОБЫЧНЫЙ')
    #     create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ','IMZO')
    #     create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\IMZO',minut)
    #     pathtext1 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\IMZO\\{minut}\\1.txt'
    #     pathtext2 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\IMZO\\{minut}\\2.txt'
    #     pathtext3 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\IMZO\\{minut}\\3.txt'
    #     pathtext4 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\IMZO\\{minut}\\4.txt'
    #     pathzip =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ'
    
    
    umumiy_without_duplicate1201 =[[] for i in range(0,49)]
    
    
    zakalka_iskyucheniye1 = Norma.objects.filter(закалка_исключение ='1').values_list('артикул',flat=True)
    zakalka_iskyucheniye2 = Norma.objects.filter(закалка_исключение ='1').values_list('компонент_1',flat=True)
    zakalka_iskyucheniye =list(zakalka_iskyucheniye1) + list(zakalka_iskyucheniye2)
    for key , row in datas.iterrows():
        
        
        if '-7' in row['MATNR']:
                gruppa_material ='ALUGP'
        else:
            gruppa_material ='ALUPF'
                
        umumiy_without_duplicate1201[0].append(row['MATNR'])
        umumiy_without_duplicate1201[1].append(row['MATNR'])
        umumiy_without_duplicate1201[2].append(row['MAKTX'])
        umumiy_without_duplicate1201[3].append('ШТ')
        umumiy_without_duplicate1201[4].append('ZPRF')

        if 'PVC' in row['MATKL']:
            spart ='02'
            dispo ='102'
        else:
            dispo ='101'
            spart ='01'
        umumiy_without_duplicate1201[5].append(row['MATKL'])

        umumiy_without_duplicate1201[6].append(gruppa_material)
        umumiy_without_duplicate1201[7].append('F')

        umumiy_without_duplicate1201[8].append(spart)

        umumiy_without_duplicate1201[9].append(str(row['BRGEW']).replace('.',','))
        umumiy_without_duplicate1201[10].append(str(row['NTGEW']).replace('.',','))
        umumiy_without_duplicate1201[11].append('КГ')
        umumiy_without_duplicate1201[12].append('NORM')
        umumiy_without_duplicate1201[13].append(row['MAKTX'])
        umumiy_without_duplicate1201[14].append('ШТ')
        umumiy_without_duplicate1201[15].append('120')
        umumiy_without_duplicate1201[16].append('X')
        umumiy_without_duplicate1201[17].append('0000')
        umumiy_without_duplicate1201[18].append('PD')
        umumiy_without_duplicate1201[19].append('MB')
        umumiy_without_duplicate1201[20].append('0')
        umumiy_without_duplicate1201[21].append('F')
        umumiy_without_duplicate1201[22].append('S100')
        umumiy_without_duplicate1201[23].append('0')
        umumiy_without_duplicate1201[24].append('M')
        umumiy_without_duplicate1201[25].append('02')
        umumiy_without_duplicate1201[26].append('')
        umumiy_without_duplicate1201[27].append('')
        umumiy_without_duplicate1201[28].append('x')
        umumiy_without_duplicate1201[29].append('5')
        umumiy_without_duplicate1201[30].append('Z_SAP_PP_002')
        umumiy_without_duplicate1201[31].append('4')
        umumiy_without_duplicate1201[32].append('SAP999')
        umumiy_without_duplicate1201[33].append('26')
        umumiy_without_duplicate1201[34].append('1301')
        umumiy_without_duplicate1201[35].append('3')
        umumiy_without_duplicate1201[36].append('0101')
        umumiy_without_duplicate1201[37].append('S')
        umumiy_without_duplicate1201[38].append('1')
        umumiy_without_duplicate1201[39].append(row['STPRS'])

        umumiy_without_duplicate1201[40].append('1301')

        umumiy_without_duplicate1201[41].append('X')
        umumiy_without_duplicate1201[42].append('X')

        
        umumiy_without_duplicate1201[43].append(dispo)

        sap_code_simvol =row['MATNR'].split('-')[1][0]
        sap_codee =row['MATNR'].split('-')[0]
        if sap_codee in zakalka_iskyucheniye:
            sap_code_simvol ='Z'
        umumiy_without_duplicate1201[44].append(SFSPF1101[sap_code_simvol])
        umumiy_without_duplicate1201[45].append('X')
        umumiy_without_duplicate1201[46].append('')
        umumiy_without_duplicate1201[47].append('2')
        umumiy_without_duplicate1201[48].append('20')

       

        


        

    # umumiy_without_duplicate =[[] for i in range(0,49)]
    # for i in range(0,len(umumiy_without_duplicate1201)):
    #     umumiy_without_duplicate[i]+=umumiy_without_duplicate1201[i] 
            
    
    ########################## 1.txt ##############################
    d1={}
    header1 ='MATNR\tBISMT\tMAKTX\tMEINS\tMTART\tMATKL\tWERKS\tBESKZ\tSPART\tBRGEW\tNTGEW\tGEWEI\tMTPOS_MARA'
    
    d1['MATNR']=umumiy_without_duplicate1201[0]
    d1['BISMT']=umumiy_without_duplicate1201[1]
    d1['MAKTX']=umumiy_without_duplicate1201[2]
    d1['MEINS']=umumiy_without_duplicate1201[3]
    d1['MTART']=umumiy_without_duplicate1201[4]
    d1['MATKL']=umumiy_without_duplicate1201[5]
    d1['WERKS']=umumiy_without_duplicate1201[34]
    d1['BESKZ']=umumiy_without_duplicate1201[7]
    d1['SPART']=umumiy_without_duplicate1201[8]
    d1['BRGEW']=umumiy_without_duplicate1201[9]
    d1['NTGEW']=umumiy_without_duplicate1201[10]
    d1['GEWEI']=umumiy_without_duplicate1201[11]
    d1['MTPOS_MARA']=umumiy_without_duplicate1201[12]
    
    
    df1= pd.DataFrame(d1)
    
    np.savetxt(pathtext1, df1.values,fmt='%s', delimiter="\t",header=header1,comments='',encoding='ansi')
    
    ########################## end 1.txt ##############################

    ########################## 2.txt ##############################
    header2='MAKTX\tMEINS\tMTART\tMATNR\tWERKS\tEKGRP\tXCHPF\tDISGR\tDISMM\tDISPO\tDISLS\tWEBAZ\tBESKZ\tLGFSB\tPLIFZ\tPERKZ\tMTVFP\tSCM_STRA1\tVRMOD\tPPSKZ\tSCM_WHATBOM\tSCM_HEUR_ID\tSCM_RRP_TYPE\tSCM_PROFID\tSTRGR\tBWKEY\tMLAST\tBKLAS\tVPRSV\tPEINH\tSTPRS\tPRCTR\tEKALR\tHKMAT\tLOSGR\tSFCPF\tUEETK\tSBDKZ\tSOBSL\tAUTO_P_ORD\tAUSME'
    
   
    d2={}
    d2['MAKTX']=umumiy_without_duplicate1201[2]
    d2['MEINS']=umumiy_without_duplicate1201[3]
    d2['MTART']=umumiy_without_duplicate1201[4]
    d2['MATNR']=umumiy_without_duplicate1201[0]
    d2['WERKS']=umumiy_without_duplicate1201[34]
    d2['EKGRP']=umumiy_without_duplicate1201[15]
    d2['XCHPF']=umumiy_without_duplicate1201[16]
    d2['DISGR']=umumiy_without_duplicate1201[17]
    d2['DISMM']=umumiy_without_duplicate1201[18]

    d2['DISPO']= umumiy_without_duplicate1201[43]

    d2['DISLS']=umumiy_without_duplicate1201[19]
    d2['WEBAZ']=umumiy_without_duplicate1201[20]    
    d2['BESKZ']=umumiy_without_duplicate1201[21]
    d2['LGFSB']=umumiy_without_duplicate1201[22]
    d2['PLIFZ']=umumiy_without_duplicate1201[23]
    d2['PERKZ']=umumiy_without_duplicate1201[24]
    d2['MTVFP']=umumiy_without_duplicate1201[25]
    d2['SCM_STRA1']=umumiy_without_duplicate1201[26]
    d2['VRMOD']=umumiy_without_duplicate1201[27]
    d2['PPSKZ']=umumiy_without_duplicate1201[27]
    d2['SCM_WHATBOM']= umumiy_without_duplicate1201[29]
    d2['SCM_HEUR_ID']= umumiy_without_duplicate1201[30]
    d2['SCM_RRP_TYPE']= umumiy_without_duplicate1201[31]
    d2['SCM_PROFID']= umumiy_without_duplicate1201[32]
    d2['STRGR']=umumiy_without_duplicate1201[33]
    d2['BWKEY']=umumiy_without_duplicate1201[34]
    d2['MLAST']=umumiy_without_duplicate1201[35]
    d2['BKLAS']=umumiy_without_duplicate1201[36]
    d2['VPRSV']=umumiy_without_duplicate1201[37]
    d2['PEINH']=umumiy_without_duplicate1201[38]

    d2['STPRS']=umumiy_without_duplicate1201[39]

    d2['PRCTR']=umumiy_without_duplicate1201[40]
    d2['EKALR']=umumiy_without_duplicate1201[41]
    d2['HKMAT']=umumiy_without_duplicate1201[42]
    d2['LOSGR']=umumiy_without_duplicate1201[38]
    d2['SFCPF']=['1301LM' for x in umumiy_without_duplicate1201[48]]
    
    d2['UEETK']=umumiy_without_duplicate1201[45]
    d2['SBDKZ']=umumiy_without_duplicate1201[47]
    d2['SOBSL']=umumiy_without_duplicate1201[48]
    d2['AUTO_P_ORD']=['X' for x in umumiy_without_duplicate1201[48]]
    d2['AUSME']=['M' for x in umumiy_without_duplicate1201[48]]
    
    # d2['RAUBE']=umumiy_without_duplicate[50]

   
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
        'TRAGR':[],
        'LADGR':[]
    }
    VTWEG =['99','10','20']
   
    for i in range(0,3):
        d3['MAKTX'] += umumiy_without_duplicate1201[13]
        d3['MEINS'] += umumiy_without_duplicate1201[14]
        d3['MTART'] += umumiy_without_duplicate1201[4]

        d3['SPART'] += umumiy_without_duplicate1201[8]


        d3['MATNR'] += umumiy_without_duplicate1201[0]
        d3['WERKS'] += umumiy_without_duplicate1201[34]
        d3['VKORG'] += [ 1300 for j in range(0,len(umumiy_without_duplicate1201[13]))]

        d3['MTPOS'] += ['NORM' if VTWEG[i]=='99' else 'ZORM' for x in  umumiy_without_duplicate1201[12]]

        d3['VTWEG'] += [ VTWEG[i] for j in range(0,len(umumiy_without_duplicate1201[13]))]

        d3['PRCTR'] += umumiy_without_duplicate1201[34]
        d3['MTVFP'] += [ '02' for j in range(0,len(umumiy_without_duplicate1201[13]))]
        d3['ALAND'] += [ 'UZ' for j in range(0,len(umumiy_without_duplicate1201[13]))]
        d3['TATYP'] += [ 'MWST' for j in range(0,len(umumiy_without_duplicate1201[13]))]
        d3['TAXKM'] += [ '1' for j in range(0,len(umumiy_without_duplicate1201[13]))]
        d3['VERSG'] += [ '1' for j in range(0,len(umumiy_without_duplicate1201[13]))]
        d3['KTGRM'] += [ '03' for j in range(0,len(umumiy_without_duplicate1201[13]))]
        d3['KONDM'] += [ '01' for j in range(0,len(umumiy_without_duplicate1201[13]))]
        d3['LADGR'] += [ '0001' for j in range(0,len(umumiy_without_duplicate1201[13]))]
        d3['TRAGR'] += [ '0001' for j in range(0,len(umumiy_without_duplicate1201[13]))]
        
       

    df3= pd.DataFrame(d3)
    np.savetxt(pathtext3, df3.values, fmt='%s', delimiter="\t",header=header3,comments='',encoding='ansi')
    ########################## end 3.txt ##############################
    
    ########################## 4.txt ##############################    
    new_ll =[[],[],[]]
    
    
    for key , row in datas.iterrows():
        
        
        sap_code_simvol =row['MATNR'].split('-')[1][0]        
        if sap_code_simvol =='E':
            for i in range(0,len(LGORT_1301['E'])):
                new_ll[0].append(row['MATNR'])
                new_ll[1].append(LGORT_1301['E'][i]['zavod_code'])
                new_ll[2].append(LGORT_1301['E'][i]['zavod_sap'])
                
        
                
        if sap_code_simvol =='P':
            for i in range(0,len(LGORT_1301['P'])):
                new_ll[0].append(row['MATNR'])
                new_ll[1].append(LGORT_1301['P'][i]['zavod_code'])
                new_ll[2].append(LGORT_1301['P'][i]['zavod_sap'])
                

                    
        if sap_code_simvol =='K':
            for i in range(0,len(LGORT_1301['K'])):
                new_ll[0].append(row['MATNR'])
                new_ll[1].append(LGORT_1301['K'][i]['zavod_code'])
                new_ll[2].append(LGORT_1301['K'][i]['zavod_sap'])
                
        
        if sap_code_simvol =='7':
            if row['MATKL'] =='PVCGP':
                for i in range(0,len(LGORT_1301['7P'])):
                    new_ll[0].append(row['MATNR'])
                    new_ll[1].append(LGORT_1301['7P'][i]['zavod_code'])
                    new_ll[2].append(LGORT_1301['7P'][i]['zavod_sap'])
            else:
                for i in range(0,len(LGORT_1301['7'])):
                    new_ll[0].append(row['MATNR'])
                    new_ll[1].append(LGORT_1301['7'][i]['zavod_code'])
                    new_ll[2].append(LGORT_1301['7'][i]['zavod_sap'])
                
                
        

        
        
    header4='MATNR\tWERKS\tLGORT\tRAUBE'
    d4={}
    d4['MATNR']=new_ll[0]
    d4['WERKS']=new_ll[1]
    d4['LGORT']=new_ll[2]
    
    df4= pd.DataFrame(d4)
    np.savetxt(pathtext4, df4.values, fmt='%s', delimiter="\t",header=header4,comments='',encoding='ansi')
    ########################## end 4.txt ##############################

    dd2 = [[],[],[],[],[],[]]
    

    for key , row in datas.iterrows():
        for j in range(0,6):
            dd2[0].append('001')
            
        for j in range(0,6):
            if HEADER_1301[j] != 'GOODS_GROUP':
                dd2[1].append('KLAES')
            else:
                dd2[1].append('GOODS_GROUP')
                
            
        for j in range(0,6):
            dd2[2].append('MARA')
            
        for j in range(0,6):
            dd2[3].append(row['MATNR'])
            
        for j in HEADER_1301:
            dd2[4].append(j)


        dd2[5].append(row['KLAES'])
        dd2[5].append(row['CH_PROFILE_TYPE'])
        dd2[5].append(row['KLS_WAST_LENGTH'])
        dd2[5].append(row['KLS_WAST'])
        dd2[5].append(row['CH_KLAES_OPTM'])
        dd2[5].append(row['GOODS_GROUP'])
    
        
    
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
    ddf2 =ddf2.replace('XXXXXXXXXX','')
    ddf2.to_excel(pathtext6,index=False)

 
    file_path =f'{pathzip}.zip'
    
    zip(pathzip, pathzip)

    return [file_path,]
    
    #########################################################################################################################

def characteristika_created_txt_create_1301_v2(datas):
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR %M %S")
    minut =now.strftime("%M-%S MINUT")
    
    
    parent_dir =f'{MEDIA_ROOT}\\uploads\\sozdaniye_materiala'
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

        if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
        else:
            gruppa_material ='ALUPF'
                
       
        umumiy_without_duplicate1201[0].append(row['SAP код S4P 100'])
        umumiy_without_duplicate1201[1].append(row['SAP код S4P 100'])
        umumiy_without_duplicate1201[2].append(row['Короткое название SAP'])
        umumiy_without_duplicate1201[3].append('M2')
        umumiy_without_duplicate1201[4].append('ZPRF')
        if '-7' in row['SAP код S4P 100']:
            gruppa_material ='ALUGP'
        else:
            gruppa_material ='ALUPF'
        umumiy_without_duplicate1201[5].append(gruppa_material)
        umumiy_without_duplicate1201[6].append(gruppa_material)
        umumiy_without_duplicate1201[7].append('F')
        umumiy_without_duplicate1201[8].append('21')
        umumiy_without_duplicate1201[9].append(str(row['Общий вес за штуку']).replace('.',','))
        umumiy_without_duplicate1201[10].append(str(row['Общий вес за штуку']).replace('.',','))
        umumiy_without_duplicate1201[11].append('КГ')
        umumiy_without_duplicate1201[12].append('ZNRM')
        umumiy_without_duplicate1201[13].append(row['Короткое название SAP'])
        umumiy_without_duplicate1201[14].append('M2')
        umumiy_without_duplicate1201[15].append('999')
        umumiy_without_duplicate1201[16].append('X')
        umumiy_without_duplicate1201[17].append('0000')
        umumiy_without_duplicate1201[18].append('PD')
        umumiy_without_duplicate1201[19].append('EX')
        umumiy_without_duplicate1201[20].append('0')
        umumiy_without_duplicate1201[21].append('E')
        ss =''
        sartrr =''
        if gruppa_material =='ALUGP':
            ss ='S400'
            sartrr ='5'
      
            
            
        umumiy_without_duplicate1201[22].append(ss)
        umumiy_without_duplicate1201[23].append('')
        umumiy_without_duplicate1201[24].append('M')
        umumiy_without_duplicate1201[25].append('02')
        umumiy_without_duplicate1201[26].append('26')
        umumiy_without_duplicate1201[27].append(sartrr)
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
        sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
        #!
        umumiy_without_duplicate1201[44].append('1301AL')

        umumiy_without_duplicate1201[45].append('X')
        umumiy_without_duplicate1201[46].append('2')
        umumiy_without_duplicate1201[47].append('20')
        umumiy_without_duplicate1201[48].append(row['ch_combination'] + row['Тип покрытия'])
    


    
 
    
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
    d2['EKGRP']=umumiy_without_duplicate1201[15] * 2
    d2['XCHPF']=umumiy_without_duplicate1201[16] * 2
    d2['DISGR']=umumiy_without_duplicate1201[17] * 2
    d2['DISMM']=umumiy_without_duplicate1201[18] * 2
    d2['DISPO']=['IMA' if 'ALU' in x else 'IMP' for x in umumiy_without_duplicate1201[0]] * 2
    d2['DISLS']=umumiy_without_duplicate1201[19] * 2
    d2['WEBAZ']=umumiy_without_duplicate1201[20] * 2
    d2['BESKZ']=umumiy_without_duplicate1201[21] + ['F' for x in umumiy_without_duplicate1201[21]]
    d2['LGFSB']=umumiy_without_duplicate1201[23] * 2
    d2['PLIFZ']=umumiy_without_duplicate1201[23] * 2
    d2['PERKZ']=umumiy_without_duplicate1201[24] * 2
    d2['MTVFP']=umumiy_without_duplicate1201[25] * 2
    d2['SCM_STRA1']=umumiy_without_duplicate1201[26] * 2
    d2['VRMOD']=umumiy_without_duplicate1201[23] * 2
    d2['PPSKZ']=umumiy_without_duplicate1201[23] * 2
    d2['SCM_WHATBOM']=umumiy_without_duplicate1201[23] * 2
    d2['SCM_HEUR_ID']=umumiy_without_duplicate1201[23] * 2
    d2['SCM_RRP_TYPE']=umumiy_without_duplicate1201[23] * 2
    d2['SCM_PROFID']=umumiy_without_duplicate1201[23] * 2
    d2['STRGR']=umumiy_without_duplicate1201[33] * 2
    d2['BWKEY']=umumiy_without_duplicate1201[34] + ['1305' for x in umumiy_without_duplicate1201[34]]
    d2['MLAST']=umumiy_without_duplicate1201[35] * 2
    d2['BKLAS']=umumiy_without_duplicate1201[36] * 2
    d2['VPRSV']=umumiy_without_duplicate1201[37] * 2
    d2['PEINH']=umumiy_without_duplicate1201[38] * 2
    d2['STPRS']=[round(float(n.replace(',','.')),2) for n in umumiy_without_duplicate1201[39]] * 2
    d2['PRCTR']=umumiy_without_duplicate1201[40] + ['1305' for x in umumiy_without_duplicate1201[34]]
    d2['EKALR']=umumiy_without_duplicate1201[41] * 2
    d2['HKMAT']=umumiy_without_duplicate1201[42] * 2
    d2['LOSGR']=umumiy_without_duplicate1201[43] * 2
    d2['SFCPF']=umumiy_without_duplicate1201[44] + umumiy_without_duplicate1201[23]
    d2['UEETK']=umumiy_without_duplicate1201[45] * 2
    d2['LGPRO']=umumiy_without_duplicate1201[23] * 2
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





def characteristika_created_txt_create_1101(datas,elist,is_1101,is_1112,file_name='aluminiytermo'):
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR %M %S")
    minut =now.strftime("%M-%S MINUT")
    
    if file_name =="aluminiytermo":
        # parent_dir =
        if not os.path.isdir(f'{MEDIA_ROOT}\\uploads\\aluminiytermo'):
            create_folder(f'{MEDIA_ROOT}\\uploads',"aluminiytermo")
            
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo',f"{year}")
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}',f'{month}')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}',day)
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}',f'{hour} ТЕРМО')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО','JOMIY')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\JOMIY',minut)
        pathtext1 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\JOMIY\\{minut}\\1.txt'
        pathtext2 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\JOMIY\\{minut}\\2.txt'
        pathtext3 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\JOMIY\\{minut}\\3.txt'
        pathtext4 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\JOMIY\\{minut}\\4.txt'
        pathtext55 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\JOMIY\\{minut}\\5.txt'
        pathtext5 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\JOMIY\\{minut}\\Единицы изм.txt'
        pathtext6 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\JOMIY\\{minut}\\Лист в C 3.xlsx'
        pathtext7 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\JOMIY\\{minut}\\Длинный текс.txt'
        # pathtextsavdo =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\JOMIY\\{minut}\\Длинный текс савдо.txt'
        pathtext8 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\JOMIY\\{minut}\\Бух название SDLONGTEXT.txt'
        pathtext9 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\JOMIY\\{minut}\\RAUBE.txt'
        pathtext10 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\JOMIY\\{minut}\\ZMD_11_0008 - Прикрепление чертежей ОЗМ.xlsx'
        pathtexcarta =f'uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\JOMIY\\{minut}\\texcarta_{day}_{month}_{year}_{hour}_{minut}.xlsx'
        pathzip =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО'
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\JOMIY\\{minut}',"ХАРАКТЕРИСТИКИ")
        char_path =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\JOMIY\\{minut}\\ХАРАКТЕРИСТИКИ'
    elif file_name =='aluminiy':
        parent_dir ='{MEDIA_ROOT}\\uploads\\aluminiy\\'
        
        if not os.path.isdir(parent_dir):
            create_folder(f'{MEDIA_ROOT}\\uploads','aluminiy')
            
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy',f'{year}')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}',f'{month}')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}',day)
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}',f'{hour} ОБЫЧНЫЙ')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ','JOMIY')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\JOMIY',minut)
        pathtext1 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\JOMIY\\{minut}\\1.txt'
        pathtext2 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\JOMIY\\{minut}\\2.txt'
        pathtext3 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\JOMIY\\{minut}\\3.txt'
        pathtext4 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\JOMIY\\{minut}\\4.txt'
        pathtext55 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\JOMIY\\{minut}\\5.txt'
        pathtext5 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\JOMIY\\{minut}\\Единицы изм.txt'
        pathtext6 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\JOMIY\\{minut}\\Лист в C 3.xlsx'
        pathtext7 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\JOMIY\\{minut}\\Длинный текс.txt'
        # pathtextsavdo =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\JOMIY\\{minut}\\Длинный текс савдо.txt'
        pathtext8 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\JOMIY\\{minut}\\Бух название SDLONGTEXT.txt'
        pathtext9 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\JOMIY\\{minut}\\RAUBE.txt'
        pathtext10 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\JOMIY\\{minut}\\ZMD_11_0008 - Прикрепление чертежей ОЗМ.xlsx'
        pathtexcarta =f'uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\JOMIY\\{minut}\\texcarta_{day}_{month}_{year}_{hour}_{minut}.xlsx'
        pathzip =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ'
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\JOMIY\\{minut}',"ХАРАКТЕРИСТИКИ")
        char_path =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\JOMIY\\{minut}\\ХАРАКТЕРИСТИКИ'
    
    umumiy_without_duplicate1201 =[[] for i in range(0,51)]
    umumiy_without_duplicate1203 =[[] for i in range(0,51)]
    umumiy_without_duplicate12D1 =[[] for i in range(0,51)]
    umumiy_without_duplicate12D2 =[[] for i in range(0,51)]
    umumiy_without_duplicate12D3 =[[] for i in range(0,51)]
    umumiy_without_duplicate12D4 =[[] for i in range(0,51)]
    umumiy_without_duplicate12D5 =[[] for i in range(0,51)]
    
    dlinniy_text_zero =[[],[],[]]
    dlinniy_text_savdo =[[],[],[]]
    buxgalterskiy_naz =[[],[],[],[],[],[],[],[]]
    
    zakalka_iskyucheniye1 = Norma.objects.filter(закалка_исключение ='1').values_list('артикул',flat=True)
    zakalka_iskyucheniye2 = Norma.objects.filter(закалка_исключение ='1').values_list('компонент_1',flat=True)
    zakalka_iskyucheniye =list(zakalka_iskyucheniye1) + list(zakalka_iskyucheniye2)
   
    for key , row in datas.iterrows():
        sap_codee = row['SAP код S4P 100'].split('-')[0]

        if ((sap_codee in zakalka_iskyucheniye) and ('-Z' in row['SAP код S4P 100'])):
           continue 

        if  (('-E' in row['SAP код S4P 100']) and (row['SAP код S4P 100'] not in elist)):
            continue 

        # if row['Тип покрытия'] =='Анодированный':
        #     continue
        if file_name =='aluminiy':
            filte_type2 = ('-E' in row['SAP код S4P 100']) or ('-Z' in row['SAP код S4P 100']) or ('-P' in row['SAP код S4P 100']) or ('-S' in row['SAP код S4P 100'])or('-A' in row['SAP код S4P 100']) or ('-7' in row['SAP код S4P 100'])
        else:
            filte_type2 = ('-Z' in row['SAP код S4P 100']) or ('-P' in row['SAP код S4P 100']) or ('-S' in row['SAP код S4P 100']) or ('-N' in row['SAP код S4P 100']) or ('-A' in row['SAP код S4P 100']) or ('-K' in row['SAP код S4P 100']) or ('-7' in row['SAP код S4P 100'])
        
        if not filte_type2:
            continue
        
        if '-7' in row['SAP код S4P 100']:
            if row['online_savdo_name'] !='' and row['online_savdo_name'] !='nan':
                dlinniy_text_savdo[0].append('1')
                dlinniy_text_savdo[1].append(row['SAP код S4P 100'])
                dlinniy_text_savdo[2].append(row['online_savdo_name'])
                
                dlinniy_text_savdo[0].append('2')
                dlinniy_text_savdo[1].append(row['SAP код S4P 100'])
                dlinniy_text_savdo[2].append(row['online_savdo_name'])

        dlinniy_text_zero[0].append('1')
        dlinniy_text_zero[1].append(row['SAP код S4P 100'])
        dlinniy_text_zero[2].append(row['Польное наименование SAP'])
        
        dlinniy_text_zero[0].append('2')
        dlinniy_text_zero[1].append(row['SAP код S4P 100'])
        dlinniy_text_zero[2].append(row['Польное наименование SAP'])
        
        
        ############################ bugalter nazvaniya###
        if 'ГП' == row['ch_rawmat_type']:
            
            
            for ii in range(0,3):
                if ii ==0:
                    vtweg ='20'
                elif ii ==1:
                    vtweg ='10'
                elif ii ==2:
                    vtweg ='99'
                
                if ii== 0:
                    buxgalterskiy_naz[0].append('1')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1100')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('RU')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append('')
                    
                    buxgalterskiy_naz[0].append('1')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1100')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('EN')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append('')
                    
                    buxgalterskiy_naz[0].append('2')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1100')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('RU')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append(row['ch_export_description'])
                    
                    buxgalterskiy_naz[0].append('2')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1100')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('EN')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append(row['ch_export_description_eng'])

                if ((ii== 0) and (row['nazvaniye_export'] != '' and row['nazvaniye_export'] != 'nan')):
                    buxgalterskiy_naz[0].append('1')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1100')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('JA')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append('')

                    buxgalterskiy_naz[0].append('2')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1100')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('JA')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append(row['nazvaniye_export'])
                
                if ((ii!= 0) and (row['online_savdo_name'] != '' and row['online_savdo_name'] != 'nan')):
                    buxgalterskiy_naz[0].append('1')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1100')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('RU')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append('')
                
                    buxgalterskiy_naz[0].append('2')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1100')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('RU')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append(row['online_savdo_name'])
                elif ii > 0 :
                    buxgalterskiy_naz[0].append('1')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1100')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('RU')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append('')

                    buxgalterskiy_naz[0].append('1')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1100')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('EN')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append('')
                
                    buxgalterskiy_naz[0].append('2')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1100')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('RU')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append(row['ch_export_description'])
                
                    buxgalterskiy_naz[0].append('2')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1100')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('EN')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append(row['ch_export_description_eng'])
        
                
        
        
        ############################ end bugalter nazvaniya###
        
        if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
        else:
            gruppa_material ='ALUPF'
                
          
        if gruppa_material=='ALUGP':
            #######12D1
            umumiy_without_duplicate12D1[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D1[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D1[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D1[3].append('ШТ')
            umumiy_without_duplicate12D1[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D1[5].append(gruppa_material)
            umumiy_without_duplicate12D1[6].append(gruppa_material)
            umumiy_without_duplicate12D1[7].append('E')
            umumiy_without_duplicate12D1[8].append('01')
            umumiy_without_duplicate12D1[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D1[10].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D1[11].append('КГ')
            umumiy_without_duplicate12D1[12].append('NORM')
            umumiy_without_duplicate12D1[13].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D1[14].append('ШТ')
            umumiy_without_duplicate12D1[15].append('999')
            umumiy_without_duplicate12D1[16].append('X')
            umumiy_without_duplicate12D1[17].append('0000')
            umumiy_without_duplicate12D1[18].append('PD')
            umumiy_without_duplicate12D1[19].append('MB')
            umumiy_without_duplicate12D1[20].append('0')
            umumiy_without_duplicate12D1[21].append('F')
            
            sartrr =''
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
                bklast ='0102'
                
                
            umumiy_without_duplicate12D1[22].append('')
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
            umumiy_without_duplicate12D1[34].append('11D1')
            umumiy_without_duplicate12D1[35].append('3')
            umumiy_without_duplicate12D1[36].append(bklast)
            umumiy_without_duplicate12D1[37].append('S')
            umumiy_without_duplicate12D1[38].append('1')
            umumiy_without_duplicate12D1[39].append(row['Price'])
            umumiy_without_duplicate12D1[40].append('1101')
            umumiy_without_duplicate12D1[41].append('X')
            umumiy_without_duplicate12D1[42].append('X')
            umumiy_without_duplicate12D1[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D1[44].append('')
            umumiy_without_duplicate12D1[45].append('X')
            umumiy_without_duplicate12D1[46].append('')
            umumiy_without_duplicate12D1[47].append('X')
            umumiy_without_duplicate12D1[48].append(row['ch_combination'] + row['Тип покрытия'])
            umumiy_without_duplicate12D1[49].append('')

            if row['Тип покрытия'] =='Белый':
                umumiy_without_duplicate12D1[50].append('S0')
            elif row['Тип покрытия'] =='Неокрашенный':
                umumiy_without_duplicate12D1[50].append('S1')
            elif row['Тип покрытия'] =='Окрашенный':
                umumiy_without_duplicate12D1[50].append('S2')
            elif row['Тип покрытия'] =='Анодированный':
                umumiy_without_duplicate12D1[50].append('S2')
            elif row['Тип покрытия'] =='Сублимированный':
                umumiy_without_duplicate12D1[50].append('S3')
            elif row['Тип покрытия'] =='Ламинированный':
                umumiy_without_duplicate12D1[50].append('0001')
            # else:
            #     umumiy_without_duplicate12D1[50].append('')


            
        if gruppa_material=='ALUGP':
            ######12D2
            umumiy_without_duplicate12D2[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D2[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D2[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D2[3].append('ШТ')
            umumiy_without_duplicate12D2[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D2[5].append(gruppa_material)
            umumiy_without_duplicate12D2[6].append(gruppa_material)
            umumiy_without_duplicate12D2[7].append('E')
            umumiy_without_duplicate12D2[8].append('01')
            umumiy_without_duplicate12D2[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D2[10].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D2[11].append('КГ')
            umumiy_without_duplicate12D2[12].append('NORM')
            umumiy_without_duplicate12D2[13].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D2[14].append('ШТ')
            umumiy_without_duplicate12D2[15].append('999')
            umumiy_without_duplicate12D2[16].append('X')
            umumiy_without_duplicate12D2[17].append('0000')
            umumiy_without_duplicate12D2[18].append('PD')
            umumiy_without_duplicate12D2[19].append('MB')
            umumiy_without_duplicate12D2[20].append('0')
            umumiy_without_duplicate12D2[21].append('F')
            
            sartrr =''
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
                bklast ='0102'
                
                
            umumiy_without_duplicate12D2[22].append('')
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
            umumiy_without_duplicate12D2[34].append('11D2')
            umumiy_without_duplicate12D2[35].append('3')
            umumiy_without_duplicate12D2[36].append(bklast)
            umumiy_without_duplicate12D2[37].append('S')
            umumiy_without_duplicate12D2[38].append('1')
            umumiy_without_duplicate12D2[39].append(row['Price'])
            umumiy_without_duplicate12D2[40].append('1101')
            umumiy_without_duplicate12D2[41].append('X')
            umumiy_without_duplicate12D2[42].append('X')
            umumiy_without_duplicate12D2[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D2[44].append('')
            umumiy_without_duplicate12D2[45].append('X')
            umumiy_without_duplicate12D2[46].append('')
            umumiy_without_duplicate12D2[47].append('X')
            umumiy_without_duplicate12D2[48].append(row['ch_combination'] + row['Тип покрытия'])
            umumiy_without_duplicate12D2[49].append('')

            if row['Тип покрытия'] =='Белый':
                umumiy_without_duplicate12D2[50].append('S0')
            elif row['Тип покрытия'] =='Неокрашенный':
                umumiy_without_duplicate12D2[50].append('S1')
            elif row['Тип покрытия'] =='Окрашенный':
                umumiy_without_duplicate12D2[50].append('S2')
            elif row['Тип покрытия'] =='Анодированный':
                umumiy_without_duplicate12D1[50].append('S2')
            elif row['Тип покрытия'] =='Сублимированный':
                umumiy_without_duplicate12D2[50].append('S3')
            elif row['Тип покрытия'] =='Ламинированный':
                umumiy_without_duplicate12D2[50].append('0001')

        if gruppa_material=='ALUGP':
            ######12D3
            umumiy_without_duplicate12D3[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D3[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D3[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D3[3].append('ШТ')
            umumiy_without_duplicate12D3[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D3[5].append(gruppa_material)
            umumiy_without_duplicate12D3[6].append(gruppa_material)
            umumiy_without_duplicate12D3[7].append('E')
            umumiy_without_duplicate12D3[8].append('01')
            umumiy_without_duplicate12D3[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D3[10].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D3[11].append('КГ')
            umumiy_without_duplicate12D3[12].append('NORM')
            umumiy_without_duplicate12D3[13].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D3[14].append('ШТ')
            umumiy_without_duplicate12D3[15].append('999')
            umumiy_without_duplicate12D3[16].append('X')
            umumiy_without_duplicate12D3[17].append('0000')
            umumiy_without_duplicate12D3[18].append('PD')
            umumiy_without_duplicate12D3[19].append('MB')
            umumiy_without_duplicate12D3[20].append('0')
            umumiy_without_duplicate12D3[21].append('F')
            
            sartrr =''
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
                bklast ='0102'
                
                
            umumiy_without_duplicate12D3[22].append('')
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
            umumiy_without_duplicate12D3[34].append('11D3')
            umumiy_without_duplicate12D3[35].append('3')
            umumiy_without_duplicate12D3[36].append(bklast)
            umumiy_without_duplicate12D3[37].append('S')
            umumiy_without_duplicate12D3[38].append('1')
            umumiy_without_duplicate12D3[39].append(row['Price'])
            umumiy_without_duplicate12D3[40].append('1101')
            umumiy_without_duplicate12D3[41].append('X')
            umumiy_without_duplicate12D3[42].append('X')
            umumiy_without_duplicate12D3[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D3[44].append('')
            umumiy_without_duplicate12D3[45].append('X')
            umumiy_without_duplicate12D3[46].append('')
            umumiy_without_duplicate12D3[47].append('X')
            umumiy_without_duplicate12D3[48].append(row['ch_combination'] + row['Тип покрытия'])
            umumiy_without_duplicate12D3[49].append('')

            if row['Тип покрытия'] =='Белый':
                umumiy_without_duplicate12D3[50].append('S0')
            elif row['Тип покрытия'] =='Неокрашенный':
                umumiy_without_duplicate12D3[50].append('S1')
            elif row['Тип покрытия'] =='Анодированный':
                umumiy_without_duplicate12D1[50].append('S2')
            elif row['Тип покрытия'] =='Окрашенный':
                umumiy_without_duplicate12D3[50].append('S2')
            elif row['Тип покрытия'] =='Сублимированный':
                umumiy_without_duplicate12D3[50].append('S3')
            elif row['Тип покрытия'] =='Ламинированный':
                umumiy_without_duplicate12D3[50].append('0001')
        
        if gruppa_material=='ALUGP':
            ######12D4
            umumiy_without_duplicate12D4[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D4[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D4[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D4[3].append('ШТ')
            umumiy_without_duplicate12D4[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D4[5].append(gruppa_material)
            umumiy_without_duplicate12D4[6].append(gruppa_material)
            umumiy_without_duplicate12D4[7].append('E')
            umumiy_without_duplicate12D4[8].append('01')
            umumiy_without_duplicate12D4[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D4[10].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D4[11].append('КГ')
            umumiy_without_duplicate12D4[12].append('NORM')
            umumiy_without_duplicate12D4[13].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D4[14].append('ШТ')
            umumiy_without_duplicate12D4[15].append('999')
            umumiy_without_duplicate12D4[16].append('X')
            umumiy_without_duplicate12D4[17].append('0000')
            umumiy_without_duplicate12D4[18].append('PD')
            umumiy_without_duplicate12D4[19].append('MB')
            umumiy_without_duplicate12D4[20].append('0')
            umumiy_without_duplicate12D4[21].append('F')
            
            sartrr =''
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
                bklast ='0102'
                
                
            umumiy_without_duplicate12D4[22].append('')
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
            umumiy_without_duplicate12D4[34].append('11D4')
            umumiy_without_duplicate12D4[35].append('3')
            umumiy_without_duplicate12D4[36].append(bklast)
            umumiy_without_duplicate12D4[37].append('S')
            umumiy_without_duplicate12D4[38].append('1')
            umumiy_without_duplicate12D4[39].append(row['Price'])
            umumiy_without_duplicate12D4[40].append('1101')
            umumiy_without_duplicate12D4[41].append('X')
            umumiy_without_duplicate12D4[42].append('X')
            umumiy_without_duplicate12D4[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D4[44].append('')
            umumiy_without_duplicate12D4[45].append('X')
            umumiy_without_duplicate12D4[46].append('')
            umumiy_without_duplicate12D4[47].append('X')
            umumiy_without_duplicate12D4[48].append(row['ch_combination'] + row['Тип покрытия'])
            umumiy_without_duplicate12D4[49].append('')

            if row['Тип покрытия'] =='Белый':
                umumiy_without_duplicate12D4[50].append('S0')
            elif row['Тип покрытия'] =='Неокрашенный':
                umumiy_without_duplicate12D4[50].append('S1')
            elif row['Тип покрытия'] =='Анодированный':
                umumiy_without_duplicate12D1[50].append('S2')
            elif row['Тип покрытия'] =='Окрашенный':
                umumiy_without_duplicate12D4[50].append('S2')
            elif row['Тип покрытия'] =='Сублимированный':
                umumiy_without_duplicate12D4[50].append('S3')
            elif row['Тип покрытия'] =='Ламинированный':
                umumiy_without_duplicate12D4[50].append('0001')


        if gruppa_material=='ALUGP':
            ######12D5
            umumiy_without_duplicate12D5[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D5[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D5[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D5[3].append('ШТ')
            umumiy_without_duplicate12D5[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D5[5].append(gruppa_material)
            umumiy_without_duplicate12D5[6].append(gruppa_material)
            umumiy_without_duplicate12D5[7].append('E')
            umumiy_without_duplicate12D5[8].append('01')
            umumiy_without_duplicate12D5[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D5[10].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D5[11].append('КГ')
            umumiy_without_duplicate12D5[12].append('NORM')
            umumiy_without_duplicate12D5[13].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D5[14].append('ШТ')
            umumiy_without_duplicate12D5[15].append('999')
            umumiy_without_duplicate12D5[16].append('X')
            umumiy_without_duplicate12D5[17].append('0000')
            umumiy_without_duplicate12D5[18].append('PD')
            umumiy_without_duplicate12D5[19].append('MB')
            umumiy_without_duplicate12D5[20].append('0')
            umumiy_without_duplicate12D5[21].append('F')
            
            sartrr =''
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
                bklast ='0102'
                
                
            umumiy_without_duplicate12D5[22].append('')
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
            umumiy_without_duplicate12D5[34].append('11D5')
            umumiy_without_duplicate12D5[35].append('3')
            umumiy_without_duplicate12D5[36].append(bklast)
            umumiy_without_duplicate12D5[37].append('S')
            umumiy_without_duplicate12D5[38].append('1')
            umumiy_without_duplicate12D5[39].append(row['Price'])
            umumiy_without_duplicate12D5[40].append('1101')
            umumiy_without_duplicate12D5[41].append('X')
            umumiy_without_duplicate12D5[42].append('X')
            umumiy_without_duplicate12D5[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D5[44].append('')
            umumiy_without_duplicate12D5[45].append('X')
            umumiy_without_duplicate12D5[46].append('')
            umumiy_without_duplicate12D5[47].append('X')
            umumiy_without_duplicate12D5[48].append(row['ch_combination'] + row['Тип покрытия'])
            umumiy_without_duplicate12D5[49].append('')

            if row['Тип покрытия'] =='Белый':
                umumiy_without_duplicate12D5[50].append('S0')
            elif row['Тип покрытия'] =='Неокрашенный':
                umumiy_without_duplicate12D5[50].append('S1')
            elif row['Тип покрытия'] =='Анодированный':
                umumiy_without_duplicate12D1[50].append('S2')
            elif row['Тип покрытия'] =='Окрашенный':
                umumiy_without_duplicate12D5[50].append('S2')
            elif row['Тип покрытия'] =='Сублимированный':
                umumiy_without_duplicate12D5[50].append('S3')
            elif row['Тип покрытия'] =='Ламинированный':
                umumiy_without_duplicate12D5[50].append('0001')

        if (('-F' not in row['SAP код S4P 100']) and ('-A' not in row['SAP код S4P 100'])):
            umumiy_without_duplicate1201[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate1201[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate1201[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate1201[3].append('ШТ')
            umumiy_without_duplicate1201[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate1201[5].append(gruppa_material)
            umumiy_without_duplicate1201[6].append(gruppa_material)
            umumiy_without_duplicate1201[7].append('E')
            umumiy_without_duplicate1201[8].append('01')
            umumiy_without_duplicate1201[9].append(str(row['Общий вес за штуку']).replace('.',','))
            umumiy_without_duplicate1201[10].append(str(row['Общий вес за штуку']).replace('.',','))
            umumiy_without_duplicate1201[11].append('КГ')
            umumiy_without_duplicate1201[12].append('NORM')
            umumiy_without_duplicate1201[13].append(row['Короткое название SAP'])
            umumiy_without_duplicate1201[14].append('ШТ')
            umumiy_without_duplicate1201[15].append('999')
            umumiy_without_duplicate1201[16].append('X')
            umumiy_without_duplicate1201[17].append('0000')
            umumiy_without_duplicate1201[18].append('PD')
            umumiy_without_duplicate1201[19].append('EX')
            umumiy_without_duplicate1201[20].append('0')
            umumiy_without_duplicate1201[21].append('E')
            ss =''
            sartrr =''
            if gruppa_material =='ALUGP':
                ss ='S400'
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
                bklast ='0102'
                
                
            umumiy_without_duplicate1201[22].append('')
            umumiy_without_duplicate1201[23].append('')
            umumiy_without_duplicate1201[24].append('M')
            umumiy_without_duplicate1201[25].append('02')
            umumiy_without_duplicate1201[26].append('10')
            umumiy_without_duplicate1201[27].append('')
            umumiy_without_duplicate1201[28].append('')
            umumiy_without_duplicate1201[29].append('')
            umumiy_without_duplicate1201[30].append('')
            umumiy_without_duplicate1201[31].append('')
            umumiy_without_duplicate1201[32].append('')
            umumiy_without_duplicate1201[33].append('10')
            umumiy_without_duplicate1201[34].append('1101')
            umumiy_without_duplicate1201[35].append('3')
            umumiy_without_duplicate1201[36].append(bklast)
            umumiy_without_duplicate1201[37].append('S')
            umumiy_without_duplicate1201[38].append('1')
            umumiy_without_duplicate1201[39].append(row['Price'])
            umumiy_without_duplicate1201[40].append('1101')
            umumiy_without_duplicate1201[41].append('X')
            umumiy_without_duplicate1201[42].append('X')
            umumiy_without_duplicate1201[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            sap_codee =row['SAP код S4P 100'].split('-')[0]
            if sap_codee in zakalka_iskyucheniye:
                sap_code_simvol ='Z'
            umumiy_without_duplicate1201[44].append(SFSPF1101[sap_code_simvol])
            umumiy_without_duplicate1201[45].append('X')
            umumiy_without_duplicate1201[46].append('')
            umumiy_without_duplicate1201[47].append('X')
            umumiy_without_duplicate1201[48].append(row['ch_combination'] + row['Тип покрытия'])

            if sap_codee in zakalka_iskyucheniye:
                umumiy_without_duplicate1201[49].append('JPZ')
            else:
                if ( (row['Тип покрытия'] =='Ламинированный') and ('-7' in row['SAP код S4P 100']) ):
                    umumiy_without_duplicate1201[49].append('JPL')
                elif (('-7' in row['SAP код S4P 100']) or ('-K' in row['SAP код S4P 100'])):
                    if file_name =="aluminiytermo":
                        umumiy_without_duplicate1201[49].append('JPK')
                    else:
                        umumiy_without_duplicate1201[49].append('JPG')

                else:
                    umumiy_without_duplicate1201[49].append('JP1')

            


            if row['Тип покрытия'] =='Белый':
                umumiy_without_duplicate1201[50].append('S0')
            elif row['Тип покрытия'] =='Неокрашенный':
                    umumiy_without_duplicate1201[50].append('S1')
            elif row['Тип покрытия'] =='Анодированный':
                umumiy_without_duplicate1201[50].append('S2')
            elif row['Тип покрытия'] =='Окрашенный':
                if '9016/' in row['Короткое название SAP']:
                    umumiy_without_duplicate1201[50].append('S0')
                else:
                    umumiy_without_duplicate1201[50].append('S2')
            elif row['Тип покрытия'] =='Сублимированный':
                umumiy_without_duplicate1201[50].append('S3')
            elif row['Тип покрытия'] =='Ламинированный':
                umumiy_without_duplicate1201[50].append('S4')

    umumiy_without_duplicate =[[] for i in range(0,51)]
    for i in range(0,len(umumiy_without_duplicate1201)):
        umumiy_without_duplicate[i]+=umumiy_without_duplicate1201[i] 
            
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

    ########################## RAUBE.txt ##############################
    # header_raube='MAKTX\tMATNR\tRAUBE'
    
    # d9={}
    # d9['MAKTX']=[]
    # d9['MATNR']=[]
    # d9['RAUBE']=[]
    # i = 0
    # for row in umumiy_without_duplicate[0]:
    #     if '-7' in row:
    #         d9['MAKTX'].append(umumiy_without_duplicate[13][i])
    #         d9['MATNR'].append(umumiy_without_duplicate[0][i])
    #         d9['RAUBE'].append(umumiy_without_duplicate[50][i])
    #     if '-P' in row:
    #         d9['MAKTX'].append(umumiy_without_duplicate[13][i])
    #         d9['MATNR'].append(umumiy_without_duplicate[0][i])
    #         d9['RAUBE'].append(umumiy_without_duplicate[50][i])
    #     if '-K' in row:
    #         d9['MAKTX'].append(umumiy_without_duplicate[13][i])
    #         d9['MATNR'].append(umumiy_without_duplicate[0][i])
    #         d9['RAUBE'].append(umumiy_without_duplicate[50][i])
    #     i += 1

    # df9= pd.DataFrame(d9)
    # df9 = df9.drop_duplicates()
    # np.savetxt(pathtext9, df9.values,fmt='%s', delimiter="\t",header=header_raube,comments='',encoding='ansi')

    ########################## Бухгалтерская название.txt ##############################
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
    dlinniy_t['ID']=dlinniy_text_zero[0] + dlinniy_text_savdo[0]
    dlinniy_t['BISMT']=dlinniy_text_zero[1] + dlinniy_text_savdo[1]
    dlinniy_t['RU']=['RU' for x in dlinniy_text_zero[1]] + ['Z' for x in dlinniy_text_savdo[1]]
    dlinniy_t['GRUN']=['GRUN' for x in dlinniy_text_zero[1]] + ['GRUN' for x in dlinniy_text_savdo[1]]
    dlinniy_t['sa']=['' for x in dlinniy_text_zero[1]] + ['' for x in dlinniy_text_savdo[1]]
    dlinniy_t['TEXT']=dlinniy_text_zero[2] + dlinniy_text_savdo[2]
    
    df_dlinniy_text= pd.DataFrame(dlinniy_t)
    
    np.savetxt(pathtext7, df_dlinniy_text.values,fmt='%s', delimiter="\t",header=header_dlinniy,comments='',encoding='ansi')
    
    
    ########################## end Длинный текс.txt ##############################

    ########################## Длинный текс Savdo.txt ##############################
    #dlinniy_text_zero
    # dlinniy_t_savdo ={}
    # header_dlinniy_savdo ='\tMATNR\t\t\t\tTEXT'
    # dlinniy_t_savdo['ID']=dlinniy_text_savdo[0] 
    # dlinniy_t_savdo['MATNR']=dlinniy_text_savdo[1] 
    # dlinniy_t_savdo['RU']=['Z' for x in (dlinniy_text_savdo[1])] 
    # dlinniy_t_savdo['GRUN']=['GRUN' for x in (dlinniy_text_savdo[1])]
    # dlinniy_t_savdo['sa']=['' for x in (dlinniy_text_savdo[1])]
    # dlinniy_t_savdo['TEXT']=dlinniy_text_savdo[2]
    
    # df_dlinniy_text_savdo = pd.DataFrame(dlinniy_t_savdo)
    
    # np.savetxt(pathtextsavdo, df_dlinniy_text_savdo.values,fmt='%s', delimiter="\t",header=header_dlinniy_savdo,comments='',encoding='ansi')
        
        
    
    ########################## end Длинный текс.txt ##############################


    ########################## 1.txt ##############################
    d1={}
    header1 ='MATNR\tBISMT\tMAKTX\tMEINS\tMTART\tMATKL\tWERKS\tBESKZ\tSPART\tBRGEW\tNTGEW\tGEWEI\tMTPOS_MARA'
    
    d1['MATNR']=umumiy_without_duplicate1201[0]
    d1['BISMT']=umumiy_without_duplicate1201[1]
    d1['MAKTX']=umumiy_without_duplicate1201[2]
    d1['MEINS']=umumiy_without_duplicate1201[3]
    d1['MTART']=umumiy_without_duplicate1201[4]
    d1['MATKL']=umumiy_without_duplicate1201[5]
    d1['WERKS']=umumiy_without_duplicate1201[34]
    d1['BESKZ']=umumiy_without_duplicate1201[7]
    d1['SPART']=umumiy_without_duplicate1201[8]
    d1['BRGEW']=[str(round(float(k1.replace(',','.')),3)).replace('.',',') for k1 in umumiy_without_duplicate1201[9]]
    d1['NTGEW']=[str(round(float(k2.replace(',','.')),3)).replace('.',',') for k2 in umumiy_without_duplicate1201[10]]
    d1['GEWEI']=umumiy_without_duplicate1201[11]
    d1['MTPOS_MARA']=umumiy_without_duplicate1201[12]
    
    
    df1= pd.DataFrame(d1)

    df_texcarta = pd.DataFrame({
            'МАТЕРИАЛ':d1['MATNR'],
            'КРАТКИЙ ТЕКСТ':d1['MAKTX'],
            'UMREZ':['1' for x in d1['MATNR']],
            'UMREN':['1' for x in d1['MATNR']],
            'USR00':['1' for x in d1['MATNR']],
            'USR01':['1' for x in d1['MATNR']]
            })
    df_texcarta.to_excel(f'{MEDIA_ROOT}\\{pathtexcarta}',index=False)
    
    np.savetxt(pathtext1, df1.values,fmt='%s', delimiter="\t",header=header1,comments='',encoding='ansi')
    
    ########################## end 1.txt ##############################

    ########################## 2.txt ##############################
    header2='MAKTX\tMEINS\tMTART\tMATNR\tWERKS\tEKGRP\tXCHPF\tDISGR\tDISMM\tDISPO\tDISLS\tWEBAZ\tBESKZ\tLGFSB\tPLIFZ\tPERKZ\tMTVFP\tSCM_STRA1\tVRMOD\tPPSKZ\tSCM_WHATBOM\tSCM_HEUR_ID\tSCM_RRP_TYPE\tSCM_PROFID\tSTRGR\tBWKEY\tMLAST\tBKLAS\tVPRSV\tPEINH\tSTPRS\tPRCTR\tEKALR\tHKMAT\tLOSGR\tSFCPF\tFEVOR\tUEETK\tLGPRO\tAUTO_P_ORD'
    
    zavod_code_1101 ={
        '1103':'PVC',
        '1101':'PR1',
        '11D1':'001',
        '11D2':'001',
        '11D3':'001',
        '11D4':'001',
        '11D5':'001',
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
    d2['DISPO']=[zavod_code_1101[x] for x in umumiy_without_duplicate[34]]
    d2['DISLS']=umumiy_without_duplicate[19]
    d2['WEBAZ']=umumiy_without_duplicate[20]
    d2['BESKZ']=umumiy_without_duplicate[21]
    d2['LGFSB']=umumiy_without_duplicate[22]
    d2['PLIFZ']=umumiy_without_duplicate[23]
    d2['PERKZ']=umumiy_without_duplicate[24]
    d2['MTVFP']=umumiy_without_duplicate[25]
    d2['SCM_STRA1']=umumiy_without_duplicate[26]
    d2['VRMOD']=['' for x in umumiy_without_duplicate[27]]
    d2['PPSKZ']=['' for x in umumiy_without_duplicate[27]]
    d2['SCM_WHATBOM']= ['' for x in umumiy_without_duplicate[27]]
    d2['SCM_HEUR_ID']= ['' for x in umumiy_without_duplicate[27]]
    d2['SCM_RRP_TYPE']= ['' for x in umumiy_without_duplicate[27]]
    d2['SCM_PROFID']= ['' for x in umumiy_without_duplicate[27]]
    d2['STRGR']=umumiy_without_duplicate[33]
    d2['BWKEY']=umumiy_without_duplicate[34]
    d2['MLAST']=umumiy_without_duplicate[35]
    d2['BKLAS']=umumiy_without_duplicate[36]
    d2['VPRSV']=umumiy_without_duplicate[37]
    d2['PEINH']=umumiy_without_duplicate[38]
    d2['STPRS']=[round(float(n.replace(',','.')),2) for n in umumiy_without_duplicate[39]]
    d2['PRCTR']=umumiy_without_duplicate[40]
    d2['EKALR']=umumiy_without_duplicate[41]
    d2['HKMAT']=umumiy_without_duplicate[42]
    d2['LOSGR']=umumiy_without_duplicate[43]
    d2['SFCPF']=umumiy_without_duplicate[44]
    d2['FEVOR']=umumiy_without_duplicate[49]
    d2['UEETK']=umumiy_without_duplicate[45]
    d2['LGPRO']=umumiy_without_duplicate[46]
    d2['AUTO_P_ORD']=umumiy_without_duplicate[47]
    # d2['RAUBE']=umumiy_without_duplicate[50]

   
    df2= pd.DataFrame(d2)
    np.savetxt(pathtext2, df2.values,fmt='%s', delimiter="\t",header=header2,comments='',encoding='ansi')
    ########################## end 2.txt ##############################

    ########################## 3.txt ##############################
    header3 ='MAKTX\tMEINS\tMTART\tSPART\tMATNR\tWERKS\tVKORG\tMTPOS\tVTWEG\tPRCTR\tMTVFP\tALAND\tTATYP\tTAXKM\tVERSG\tKTGRM\tKONDM\tTRAGR\tLADGR'
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
        'TRAGR':[],
        'LADGR':[]
    }
    VTWEG =['99','10','20']
    KONDM ={
        'с термомостоманодированный':'A0',
        'без термомостаокрашенный':'A1',
        'без термомостабелый':'A1',
        'без термомостасублимированный':'A2',
        'без термомостаанодированный':'A3',
        'без термомосталаминированный':'A4',
        'с термомостомламинированный':'A5',
        'без термомостанеокрашенный':'A6',
        'с термомостомокрашенный':'A7',
        'с термомостомбелый':'A7',
        'с термомостомнеокрашенный':'A8',
        'с термомостомсублимированный':'A9',
    }
    for i in range(0,3):
        d3['MAKTX'] += umumiy_without_duplicate[13]
        d3['MEINS'] += umumiy_without_duplicate[14]
        d3['MTART'] += umumiy_without_duplicate[4]
        d3['SPART'] += umumiy_without_duplicate[8]
        d3['MATNR'] += umumiy_without_duplicate[0]
        d3['WERKS'] += umumiy_without_duplicate[34]
        d3['VKORG'] += [ 1100 for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['MTPOS'] += umumiy_without_duplicate[12]
        d3['VTWEG'] += [ VTWEG[i] for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['PRCTR'] += [ '1103' if umumiy_without_duplicate[34][i] =='1103' else '1101' for i in range(0,len(umumiy_without_duplicate[34]))]
        d3['MTVFP'] += [ '02' for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['ALAND'] += [ 'UZ' for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['TATYP'] += [ 'MWST' for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['TAXKM'] += [ '1' for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['VERSG'] += [ '1' for j in range(0,len(umumiy_without_duplicate[13]))]
        d3['KTGRM'] += [ '01' for j in range(0,len(umumiy_without_duplicate[13]))]
        if i!=2:
            d3['KONDM'] += [ '01' for j in range(0,len(umumiy_without_duplicate[13]))]
        else:
            d3['KONDM'] += [ '01' if '-7' not in umumiy_without_duplicate[0][x] else KONDM[umumiy_without_duplicate[48][x].lower()] for x in range(0,len(umumiy_without_duplicate[0]))]
            
        d3['TRAGR'] += [ '0001' for j in range(0,len(umumiy_without_duplicate[13]))]
        
        ladgr =[]
        j = 0
        for sap_code in umumiy_without_duplicate[0]:
            if (('-7' in sap_code ) or ('-P' in sap_code ) or ('-K' in sap_code )):
                
                if umumiy_without_duplicate[34][j]=='1101':
                    if umumiy_without_duplicate[50][j]!='0001':
                        # print('11' + umumiy_without_duplicate[50][j],'<<<<>>>>>>',sap_code)
                        ladgr.append('11' + umumiy_without_duplicate[50][j])
                    else:
                        ladgr.append(umumiy_without_duplicate[50][j])
                else:
                    ladgr.append('0001')

            elif '-Z' in sap_code:
                ladgr.append('11S1')
            else:
                ladgr.append('0001')
            j += 1

        d3['LADGR'] += ladgr
    df3= pd.DataFrame(d3)
    np.savetxt(pathtext3, df3.values, fmt='%s', delimiter="\t",header=header3,comments='',encoding='ansi')
    ########################## end 3.txt ##############################
    
    ########################## 4.txt ##############################    
    new_ll =[[],[],[],[]]
    sap_code_title =[]
    dlina_title =[]
    obshiy_ves_za_shtuku =[]
    wms_width =[]
    wms_height =[]
    
    for key , row in datas.iterrows():
        if (('-E' in row['SAP код S4P 100']) and (row['SAP код S4P 100'] not in elist)):
            continue
        sap_code_title.append(row['SAP код S4P 100'])
        dlina_title.append(row['Длина'])
        obshiy_ves_za_shtuku.append(row['Общий вес за штуку'])
        wms_width.append(row['WMS_WIDTH'])
        wms_height.append(row['WMS_HEIGHT'])

        raube_txt = ''

        if row['Тип покрытия'].capitalize() =='Белый':
            raube_txt = 'S0'
        elif row['Тип покрытия'].capitalize() =='Неокрашенный':
            raube_txt = 'S1'
        elif row['Тип покрытия'].capitalize() =='Окрашенный':
            if '9016/' in row['Короткое название SAP']:
                raube_txt = 'S0'
            else:
                raube_txt = 'S2'
        elif row['Тип покрытия'].capitalize() =='Анодированный':
            raube_txt = 'S2'
        elif row['Тип покрытия'].capitalize() =='Сублимированный':
            raube_txt = 'S3'
        elif row['Тип покрытия'].capitalize() =='Ламинированный':
            raube_txt = 'S4'
        
        sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]        
        if sap_code_simvol =='E':
            for i in range(0,len(LGORT_1101['E'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT_1101['E'][i]['zavod_code'])
                new_ll[2].append(LGORT_1101['E'][i]['zavod_sap'])
                new_ll[3].append('')
        if sap_code_simvol =='Z':
            for i in range(0,len(LGORT_1101['Z'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT_1101['Z'][i]['zavod_code'])
                new_ll[2].append(LGORT_1101['Z'][i]['zavod_sap'])
                new_ll[3].append('S1')
        if sap_code_simvol =='P':
            for i in range(0,len(LGORT_1101['P'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT_1101['P'][i]['zavod_code'])
                new_ll[2].append(LGORT_1101['P'][i]['zavod_sap'])
                new_ll[3].append(raube_txt)

        
        if sap_code_simvol =='S':
            for i in range(0,len(LGORT_1101['S'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT_1101['S'][i]['zavod_code'])
                new_ll[2].append(LGORT_1101['S'][i]['zavod_sap'])
                new_ll[3].append('')
        if file_name !='aluminiy':
            if sap_code_simvol =='N':
                for i in range(0,len(LGORT_1101['N'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT_1101['N'][i]['zavod_code'])
                    new_ll[2].append(LGORT_1101['N'][i]['zavod_sap'])
                    new_ll[3].append('')
        if sap_code_simvol =='K':
            for i in range(0,len(LGORT_1101['K'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT_1101['K'][i]['zavod_code'])
                new_ll[2].append(LGORT_1101['K'][i]['zavod_sap'])
                new_ll[3].append(raube_txt)
        
        if sap_code_simvol =='7':
            for i in range(0,len(LGORT_1101['7'])):
                new_ll[0].append(row['SAP код S4P 100'])
                new_ll[1].append(LGORT_1101['7'][i]['zavod_code'])
                new_ll[2].append(LGORT_1101['7'][i]['zavod_sap'])
                if LGORT_1101['7'][i]['zavod_code'] =='1101':
                    new_ll[3].append(raube_txt)
                else:
                    new_ll[3].append('')
                
        

        
        
    header4='MATNR\tWERKS\tLGORT\tRAUBE'
    d4={}
    d4['MATNR']=new_ll[0]
    d4['WERKS']=new_ll[1]
    d4['LGORT']=new_ll[2]
    d4['RAUBE']=new_ll[3]
    df4= pd.DataFrame(d4)
    np.savetxt(pathtext4, df4.values, fmt='%s', delimiter="\t",header=header4,comments='',encoding='ansi')
    ########################## end 4.txt ##############################

    ########################## 55.txt ##############################    
    new_ll_55 =[[],[],[],[]]
    
    for key , row in datas.iterrows():
        sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]        
        
        raube_txt = ''

        if row['Тип покрытия'].capitalize() =='Белый':
            raube_txt = 'S0'
        elif row['Тип покрытия'].capitalize() =='Неокрашенный':
            raube_txt = 'S1'
        elif row['Тип покрытия'].capitalize() =='Окрашенный' or row['Тип покрытия'].capitalize() =='Анодированный':
            raube_txt = 'S2'
        elif row['Тип покрытия'].capitalize() =='Сублимированный':
            raube_txt = 'S3'
        elif row['Тип покрытия'].capitalize() =='Ламинированный':
            raube_txt = 'S4'

        if sap_code_simvol =='7':
            for i in range(0,len(LGORT_1101['7'])):
                if LGORT_1101['7'][i]['zavod_code'] =='1101':
                    new_ll_55[0].append(row['SAP код S4P 100'])
                    new_ll_55[1].append(LGORT_1101['7'][i]['zavod_code'])
                    new_ll_55[2].append(LGORT_1101['7'][i]['zavod_sap'])
                    if LGORT_1101['7'][i]['zavod_code'] =='1101':
                        new_ll_55[3].append(raube_txt)
                    else:
                        new_ll_55[3].append('')

    header55='MATNR\tWERKS\tLGORT\tRAUBE'
    d55={}
    d55['MATNR']=new_ll_55[0] 
    d55['WERKS']=new_ll_55[1]  
    d55['RAUBE']=new_ll_55[3]
    df55= pd.DataFrame(d55)
    df55=df55.drop_duplicates()
    np.savetxt(pathtext55, df55.values, fmt='%s', delimiter="\t",header=header55,comments='',encoding='ansi')
    ########################## end 55.txt ##############################
    
    ########################## 5.txt ##############################
    d5 ={
        'sap_code':[],
        'ed_iz1':[],
        'ed_iz2':[],
        'ed_iz3':[],
        'ed_iz4':[],
        'ed_iz5':[],
        'ed_iz6':[],
        'ed_iz7':[]
    }
    ED_IZM =['ШТ','М','КГ']
    
    # sap_code_title =[]
    # dlina_title =[]
    # obshiy_ves_za_shtuku =[]
    # wms_width =[]
    # wms_height =[]
    ed_iz3 =[]
    for i in range(0,3):
        if i == 0 :
            ed_iz3 += ['1' for j in range(0,len(sap_code_title)) ]
        elif i == 1 :
            ed_iz3 += [j for j in dlina_title ]
        elif i == 2 :
            ed_iz3 += [int(float(j.replace(',','.'))*1000) for j in obshiy_ves_za_shtuku ]
            
    
    for i in ED_IZM:    
        d5['sap_code'] += sap_code_title
        d5['ed_iz1'] += [ i for j in range(0,len(sap_code_title))]
        d5['ed_iz2'] +=['1' if i =='ШТ' else '1000'  for j in range(0,len(sap_code_title)) ]
        # d5['ed_iz3'] +=['1' if i =='ШТ' elif i=='М' for j in range(0,len(sap_code_title)) ]
        d5['ed_iz4'] +=[j for j in dlina_title ]
        d5['ed_iz5'] +=[j for j in wms_height ]
        d5['ed_iz6'] +=[j for j in wms_width ]
        d5['ed_iz7'] +=[ 'мм' for j in range(0,len(sap_code_title))]
    
    d5['ed_iz3'] = ed_iz3
    df5= pd.DataFrame(d5)
    np.savetxt(pathtext5, df5.values, fmt='%s', delimiter="\t",encoding='ansi')
    ########################## end 5.txt ##############################
    ########################## List v 3 ##############################
    dd2 = [[],[],[],[],[],[]]
    baza_profile_links =[[],[]]

    for key , row in datas.iterrows():

        if (('-E' in row['SAP код S4P 100']) and (row['SAP код S4P 100'] not in elist)):
            continue

        if file_name =='aluminiy':
            if '-N' in row['SAP код S4P 100']:
                continue

        sap_code = row['SAP код S4P 100'].split('-')[0]
        bazaprofiley =AluProfilesData.objects.filter(Q(data__Артикул =sap_code)|Q(data__Компонент=sap_code))[:1].get()     
        baza_profile_links[0].append(row['SAP код S4P 100'])
        baza_profile_links[1].append(bazaprofiley.data['Ссылка для чертежей'])

        row['ch_tnved'] =str(row['ch_tnved']).replace('.0','')
        row['ch_outer_side_pc_id'] =str(row['ch_outer_side_pc_id']).replace('.0','')
        row['ch_outer_side_pc_brand'] =str(row['ch_outer_side_pc_brand']).replace('.0','')
        row['ch_inner_side_pc_id'] =str(row['ch_inner_side_pc_id']).replace('.0','')
        row['ch_inner_side_pc_brand'] =str(row['ch_inner_side_pc_brand']).replace('.0','')
        row['ch_outer_side_wg_s_id'] =str(row['ch_outer_side_wg_s_id']).replace('.0','')
        row['ch_inner_side_wg_s_id'] =str(row['ch_inner_side_wg_s_id']).replace('.0','')
        row['ch_outer_side_wg_id'] =str(row['ch_outer_side_wg_id']).replace('.0','')
        row['ch_inner_side_wg_id'] =str(row['ch_inner_side_wg_id']).replace('.0','')
        row['ch_width'] =str(row['ch_width']).replace('.0','')
        row['ch_height'] =str(row['ch_height']).replace('.0','')
        
        if '-7' in row['SAP код S4P 100']:
            for j in range(0,35):
                dd2[0].append('001')
            dd2[0].append('023')
                
            for j in range(0,33):
                if HEADER[j] not in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT','TNVED']:
                    dd2[1].append('ALUMINIUM_PROFILE')
                else:
                    if HEADER[j] in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT']:
                        dd2[1].append('RAWMAT_TYPE')
                    elif HEADER[j] =='TNVED':
                        dd2[1].append('TNVED')
            
           

            dd2[1].append('QBIC')
            dd2[1].append('QBIC')
            dd2[1].append('ZPP_023_FERT')
        
            for j in range(0,36):
                dd2[2].append('MARA')
                
            for j in range(0,36):
                dd2[3].append(row['SAP код S4P 100'])
                
            for j in HEADER:
                dd2[4].append(j)
            
            dd2[4].append('AMOUNT_IN_A_PACKAGE')
            dd2[4].append('COATING_QBIC')
            dd2[4].append('ZBATCH_NUM')

            dd2[5].append('')
            dd2[5].append('')
            dd2[5].append(row['ch_system'])
            dd2[5].append(row['SAP код S4P 100'].split('-')[0])
            dd2[5].append(row['Длина'])
            dd2[5].append(row['Тип покрытия'])
            dd2[5].append(row['ch_alloy'])
            dd2[5].append(row['ch_temper'])
            dd2[5].append(row['ch_combination'])
            dd2[5].append(row['ch_outer_side_pc_id'])
            dd2[5].append(row['ch_outer_side_pc_brand'])
            dd2[5].append(row['ch_inner_side_pc_id'])
            dd2[5].append(row['ch_inner_side_pc_brand'])
            dd2[5].append(row['ch_outer_side_wg_s_id'])
            dd2[5].append(row['ch_inner_side_wg_s_id'])
            dd2[5].append(row['ch_outer_side_wg_id'])
            dd2[5].append(row['ch_inner_side_wg_id'])
            # print('7 1101 >>>>>>>  ',row['ch_anodization_contact'])
            if row['ch_anodization_contact'].lower() =='yc':
                dd2[5].append('С КОНТАКТОМ')
            elif row['ch_anodization_contact'].lower()=='nc' :
                dd2[5].append('БЕЗ КОНТАКТА')
            else:
                dd2[5].append(row['ch_anodization_contact'])

            dd2[5].append(row['ch_anodization_type'])
            dd2[5].append(row['ch_anodization_method'])
            dd2[5].append(row['ch_print_view'])
            dd2[5].append(row['ch_profile_base'])
            dd2[5].append(row['ch_width'])
            dd2[5].append(row['ch_height'])
            dd2[5].append(row['ch_category'])
            dd2[5].append(row['ch_rawmat_type'])
            dd2[5].append('')
            dd2[5].append(row['ch_tnved'])
            dd2[5].append(str(row['ch_surface_treatment_export']).replace('.0',''))
            dd2[5].append(row['WMS_WIDTH'])
            dd2[5].append(row['WMS_HEIGHT'])
            dd2[5].append('')
            dd2[5].append(bazaprofiley.data['Тип Комбинация'])
            artikul_for_qbic = str(row['SAP код S4P 100']).split('-')[0]
            if Norma.objects.filter(Q(артикул=artikul_for_qbic)&~Q(упаковка_колво_профилей_в_1_пачке ='0')).exists():
                qbicc = Norma.objects.filter(Q(артикул=artikul_for_qbic)&~Q(упаковка_колво_профилей_в_1_пачке ='0'))[:1].get().упаковка_колво_профилей_в_1_пачке
                dd2[5].append(qbicc)
            else:
                dd2[5].append('XXXX')
            if row['Тип покрытия'] =='Неокрашенный':
                qbic ='XXXX'
            elif row['Тип покрытия'] =='Окрашенный':
                qbic = row['ch_outer_side_pc_id']
            elif row['Тип покрытия'] =='Анодированный':
                qbic = row['ch_outer_side_pc_id']
            elif row['Тип покрытия'] =='Ламинированный':
                if row['ch_outer_side_wg_id'] =='XXXX':
                    qbic = row['ch_inner_side_wg_id']
                else:
                    qbic = row['ch_outer_side_wg_id']
            elif row['Тип покрытия'] =='Сублимированный':
                qbic = row['ch_outer_side_wg_s_id']
            else:
                qbic ='XXXX'

            dd2[5].append(qbic)
            dd2[5].append('XXXX')
        else:
            for j in range(0,33):
                dd2[0].append('001')
            dd2[0].append('023')
                
            for j in range(0,33):
                if HEADER[j] not in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT','TNVED']:
                    dd2[1].append('ALUMINIUM_PROFILE')
                else:
                    if HEADER[j] in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT']:
                        dd2[1].append('RAWMAT_TYPE')
                    elif HEADER[j] =='TNVED':
                        dd2[1].append('TNVED')
            dd2[1].append('ZPP_023_HALB')
            for j in range(0,34):
                dd2[2].append('MARA')
                
            for j in range(0,34):
                dd2[3].append(row['SAP код S4P 100'])
                
            for j in HEADER:
                dd2[4].append(j)
            dd2[4].append('ZBATCH_NUM')

            dd2[5].append('')
            dd2[5].append('')
            dd2[5].append(row['ch_system'])
            dd2[5].append(row['SAP код S4P 100'].split('-')[0])
            dd2[5].append(row['Длина'])
            dd2[5].append(row['Тип покрытия'])
            dd2[5].append(row['ch_alloy'])
            dd2[5].append(row['ch_temper'])
            dd2[5].append(row['ch_combination'])
            dd2[5].append(row['ch_outer_side_pc_id'])
            dd2[5].append(row['ch_outer_side_pc_brand'])
            dd2[5].append(row['ch_inner_side_pc_id'])
            dd2[5].append(row['ch_inner_side_pc_brand'])
            dd2[5].append(row['ch_outer_side_wg_s_id'])
            dd2[5].append(row['ch_inner_side_wg_s_id'])
            dd2[5].append(row['ch_outer_side_wg_id'])
            dd2[5].append(row['ch_inner_side_wg_id'])
            if row['ch_anodization_contact'].lower() =='yc':
                dd2[5].append('С КОНТАКТОМ')
            elif row['ch_anodization_contact'].lower()=='nc' :
                dd2[5].append('БЕЗ КОНТАКТА')
            else:
                dd2[5].append(row['ch_anodization_contact'])
            # dd2[5].append(row['ch_anodization_contact'])
            dd2[5].append(row['ch_anodization_type'])
            dd2[5].append(row['ch_anodization_method'])
            dd2[5].append(row['ch_print_view'])
            dd2[5].append(row['ch_profile_base'])
            dd2[5].append(row['ch_width'])
            dd2[5].append(row['ch_height'])
            dd2[5].append(row['ch_category'])
            dd2[5].append(row['ch_rawmat_type'])
            dd2[5].append('')
            dd2[5].append(row['ch_tnved'])
            dd2[5].append(str(row['ch_surface_treatment_export']).replace('.0',''))
            dd2[5].append(row['WMS_WIDTH'])
            dd2[5].append(row['WMS_HEIGHT'])
            dd2[5].append('')
            dd2[5].append(bazaprofiley.data['Тип Комбинация'])
            dd2[5].append('XXXX')

    new_date={}       
    new_date['Вид класса'] = dd2[0]
    new_date['Класс'] = dd2[1]
    new_date['Таблица'] = dd2[2]
    new_date['Объект'] = dd2[3]
    new_date['Имя признака'] = dd2[4]
    new_date['Значение признака'] = dd2[5]
    new_date['Статус загрузки'] = ['' for x in dd2[5]]
    
    df_baza_profiley_link =pd.DataFrame({'SAP CODE':baza_profile_links[0],'link':baza_profile_links[1]})
    df_baza_profiley_link.to_excel(pathtext10,index=False)

    ddf2 = pd.DataFrame(new_date)
    ddf2 = ddf2[((ddf2["Значение признака"] != "nan") & (ddf2["Значение признака"] != ""))]
    ddf2 =ddf2.replace('XXXX','')
    ddf2.to_excel(pathtext6,index=False)

    grouped_by_name = ddf2.groupby('Имя признака')

    # Save each group to a separate Excel file named after the unique value in the "Имя признака" column
    for group_name, group_df in grouped_by_name:
        # Remove duplicates
        group_df = group_df.drop_duplicates()
        
        # Prepare the output file path using the group_name
        output_file = f'{group_name}.xlsx'  # This saves the file using the group name
        
        # Save the group to Excel
        
        group_df.to_excel(f'{char_path}\\{output_file}.xlsx', index=False)

    if is_1101 =='on':
        return [pathtext1,pathtext2,pathtext3,pathtext4,pathtext5,pathtext6,pathtext7,pathtext8,pathtext9,pathtext10],pathzip,pathtexcarta
    elif is_1112 =='on':
        return [buxgalterskiy_t,dlinniy_t,d1,d2,d3,d4,d5,new_date,d55],pathtexcarta
    #########################################################################################################################
    ###############################################################################################################
    #######################################################################################




def characteristika_created_txt_create(datas,elist,order_id,file_name='aluminiytermo'):
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR %M %S")
    minut =now.strftime("%M-%S MINUT")
    if order_id:
        order =Order.objects.get(id = order_id)
        is_1101 =order.paths['is_1101']
        is_1201 =order.paths['is_1201']
        is_1112 =order.paths['is_1112']

        if is_1101 =='on' and is_1201 !='on':
            path_1101,path_zip2,path_texcarta = characteristika_created_txt_create_1101(datas,elist,is_1101,is_1112,file_name)
            paths = order.paths
            paths['texcarta_file']=f'{MEDIA_ROOT}\\{path_texcarta}'
            paths['status_texcarta'] ='on process'
            file = ExcelFilesImzo(file = path_texcarta)
            file.save()
            paths['texid']= file.id
            order.paths =paths
            order.save()

            file_path =f'{path_zip2}.zip'
            
            zip(path_zip2, path_zip2)

            return [file_path,],path_texcarta
    
    
    if file_name =='aluminiytermo':
        parent_dir =f'{MEDIA_ROOT}\\uploads\\aluminiytermo'
        if not os.path.isdir(parent_dir):
            create_folder(f'{MEDIA_ROOT}\\uploads','aluminiytermo')
            
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo',f'{year}')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}',f'{month}')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}',day)
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}',f'{hour} ТЕРМО')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО','BENKAM')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\BENKAM',minut)
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\BENKAM\\{minut}',"ХАРАКТЕРИСТИКИ")
        pathtext1 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\BENKAM\\{minut}\\1.txt'
        pathtext2 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\BENKAM\\{minut}\\2.txt'
        pathtext3 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\BENKAM\\{minut}\\3.txt'
        pathtext4 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\BENKAM\\{minut}\\4.txt'
        pathtext55 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\BENKAM\\{minut}\\5.txt'
        pathtext5 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\BENKAM\\{minut}\\Единицы изм.txt'
        pathtext6 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\BENKAM\\{minut}\\Лист в C 3.xlsx'
        pathtext7 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\BENKAM\\{minut}\\Длинный текс.txt'
        pathtextsavdo =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\BENKAM\\{minut}\\Длинный текс савдо.txt'
        pathtext8 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\BENKAM\\{minut}\\Бух название SDLONGTEXT.txt'
        pathtext9 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\BENKAM\\{minut}\\ZMD_11_0008 - Прикрепление чертежей ОЗМ.xlsx'
        pathzip =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО'
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\BENKAM\\{minut}',"ХАРАКТЕРИСТИКИ")
        char_path = f"{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour} ТЕРМО\\BENKAM\\{minut}\\ХАРАКТЕРИСТИКИ"
    elif file_name =='aluminiy':
        parent_dir ='{MEDIA_ROOT}\\uploads\\aluminiy'
        
        if not os.path.isdir(parent_dir):
            create_folder(f'{MEDIA_ROOT}\\uploads','aluminiy')
            
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy',f'{year}')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}',f'{month}')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}',day)
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}',f'{hour} ОБЫЧНЫЙ')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ','BENKAM')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\BENKAM',minut)
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\BENKAM\\{minut}',"ХАРАКТЕРИСТИКИ")
        pathtext1 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\BENKAM\\{minut}\\1.txt'
        pathtext2 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\BENKAM\\{minut}\\2.txt'
        pathtext3 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\BENKAM\\{minut}\\3.txt'
        pathtext4 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\BENKAM\\{minut}\\4.txt'
        pathtext55 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\BENKAM\\{minut}\\5.txt'
        pathtext5 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\BENKAM\\{minut}\\Единицы изм.txt'
        pathtext6 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\BENKAM\\{minut}\\Лист в C 3.xlsx'
        pathtext7 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\BENKAM\\{minut}\\Длинный текс.txt'
        pathtextsavdo =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\BENKAM\\{minut}\\Длинный текс савдо.txt'
        pathtext8 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\BENKAM\\{minut}\\Бух название SDLONGTEXT.txt'
        pathtext9 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\BENKAM\\{minut}\\ZMD_11_0008 - Прикрепление чертежей ОЗМ.xlsx'
        pathzip =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ'
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\BENKAM\\{minut}',"ХАРАКТЕРИСТИКИ")
        char_path = f"{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour} ОБЫЧНЫЙ\\BENKAM\\{minut}\\ХАРАКТЕРИСТИКИ"
       
    
    umumiy_without_duplicate1201 =[[] for i in range(0,49)]
    umumiy_without_duplicate1203 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D1 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D2 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D3 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D4 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D5 =[[] for i in range(0,49)]
    
    dlinniy_text_zero =[[],[],[]]
    dlinniy_text_savdo =[[],[],[]]
    buxgalterskiy_naz =[[],[],[],[],[],[],[],[]]
    

    for key , row in datas.iterrows():

        if not LengthOfProfile.objects.filter(artikul=row['ch_article'],length=row['Длина']).exists():
            LengthOfProfile(
                artikul = row['ch_article'],
                length = row['Длина'],
                ves_za_shtuk = row['Общий вес за штуку'],
                ves_za_metr = row['Удельный вес за метр']
            ).save()
        dlinniy_text_zero[0].append('1')
        dlinniy_text_zero[1].append(row['SAP код S4P 100'])
        dlinniy_text_zero[2].append(row['Польное наименование SAP'])
        
        dlinniy_text_zero[0].append('2')
        dlinniy_text_zero[1].append(row['SAP код S4P 100'])
        dlinniy_text_zero[2].append(row['Польное наименование SAP'])


        if '-7' in row['SAP код S4P 100']:
            if row['online_savdo_name'] !='' and row['online_savdo_name'] !='nan':
                dlinniy_text_savdo[0].append('1')
                dlinniy_text_savdo[1].append(row['SAP код S4P 100'])
                dlinniy_text_savdo[2].append(row['online_savdo_name'])
                
                dlinniy_text_savdo[0].append('2')
                dlinniy_text_savdo[1].append(row['SAP код S4P 100'])
                dlinniy_text_savdo[2].append(row['online_savdo_name'])
        
        
        ############################ bugalter nazvaniya###
        if 'ГП' == row['ch_rawmat_type']:
            
            
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
                    buxgalterskiy_naz[7].append(row['ch_export_description'])
                    
                    buxgalterskiy_naz[0].append('2')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1200')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('EN')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append(row['ch_export_description_eng'])

                if ((ii== 0) and (row['nazvaniye_export'] != '' and row['nazvaniye_export'] != 'nan')):
                    buxgalterskiy_naz[0].append('1')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1200')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('JA')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append('')

                    buxgalterskiy_naz[0].append('2')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1200')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('JA')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append(row['nazvaniye_export'])
                
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
                    buxgalterskiy_naz[7].append(row['ch_export_description'])
                
                    buxgalterskiy_naz[0].append('2')
                    buxgalterskiy_naz[1].append(row['SAP код S4P 100'])
                    buxgalterskiy_naz[2].append('1200')
                    buxgalterskiy_naz[3].append(vtweg)
                    buxgalterskiy_naz[4].append('EN')
                    buxgalterskiy_naz[5].append('0001')
                    buxgalterskiy_naz[6].append('')
                    buxgalterskiy_naz[7].append(row['ch_export_description_eng'])
                
        
        
        ############################ end bugalter nazvaniya###
        
        if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
        else:
            gruppa_material ='ALUPF'
                
        if ((row['Тип покрытия'] =='Ламинированный') and (row['Участок'] =='U-Упаковка + Готовая продукция') or ((row['Тип покрытия'] =='Ламинированный') and (row['Участок'] =='K-Комбинирования'))):
            umumiy_without_duplicate1203[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate1203[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate1203[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate1203[3].append('ШТ')
            umumiy_without_duplicate1203[4].append('ZPRF')
            umumiy_without_duplicate1203[5].append(gruppa_material)
            umumiy_without_duplicate1203[6].append(gruppa_material)
            umumiy_without_duplicate1203[7].append('E')
            umumiy_without_duplicate1203[8].append('01')
            umumiy_without_duplicate1203[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate1203[10].append(row['Общий вес за штуку'])
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
            if gruppa_material =='ALUGP':
                ss ='S400'
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
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
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate1203[44].append(SFSPF1203[sap_code_simvol])
            umumiy_without_duplicate1203[45].append('X')
            umumiy_without_duplicate1203[46].append(LGPRO1203[sap_code_simvol])
            umumiy_without_duplicate1203[47].append('X')
            umumiy_without_duplicate1203[48].append(row['ch_combination'] + row['Тип покрытия'])
            
        if gruppa_material=='ALUGP':
            #######12D1
            umumiy_without_duplicate12D1[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D1[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D1[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D1[3].append('ШТ')
            umumiy_without_duplicate12D1[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D1[5].append(gruppa_material)
            umumiy_without_duplicate12D1[6].append(gruppa_material)
            umumiy_without_duplicate12D1[7].append('E')
            umumiy_without_duplicate12D1[8].append('01')
            umumiy_without_duplicate12D1[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D1[10].append(row['Общий вес за штуку'])
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
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
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
            umumiy_without_duplicate12D1[40].append('1201')
            umumiy_without_duplicate12D1[41].append('X')
            umumiy_without_duplicate12D1[42].append('X')
            umumiy_without_duplicate12D1[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D1[44].append('')
            umumiy_without_duplicate12D1[45].append('X')
            umumiy_without_duplicate12D1[46].append('')
            umumiy_without_duplicate12D1[47].append('X')
            umumiy_without_duplicate12D1[48].append(row['ch_combination'] + row['Тип покрытия'])
            
        if gruppa_material=='ALUGP':
            ######12D2
            umumiy_without_duplicate12D2[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D2[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D2[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D2[3].append('ШТ')
            umumiy_without_duplicate12D2[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D2[5].append(gruppa_material)
            umumiy_without_duplicate12D2[6].append(gruppa_material)
            umumiy_without_duplicate12D2[7].append('E')
            umumiy_without_duplicate12D2[8].append('01')
            umumiy_without_duplicate12D2[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D2[10].append(row['Общий вес за штуку'])
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
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
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
            umumiy_without_duplicate12D2[40].append('1201')
            umumiy_without_duplicate12D2[41].append('X')
            umumiy_without_duplicate12D2[42].append('X')
            umumiy_without_duplicate12D2[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D2[44].append('')
            umumiy_without_duplicate12D2[45].append('X')
            umumiy_without_duplicate12D2[46].append('')
            umumiy_without_duplicate12D2[47].append('X')
            umumiy_without_duplicate12D2[48].append(row['ch_combination'] + row['Тип покрытия'])
            
        if gruppa_material=='ALUGP':
            ######12D3
            umumiy_without_duplicate12D3[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D3[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D3[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D3[3].append('ШТ')
            umumiy_without_duplicate12D3[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D3[5].append(gruppa_material)
            umumiy_without_duplicate12D3[6].append(gruppa_material)
            umumiy_without_duplicate12D3[7].append('E')
            umumiy_without_duplicate12D3[8].append('01')
            umumiy_without_duplicate12D3[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D3[10].append(row['Общий вес за штуку'])
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
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
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
            umumiy_without_duplicate12D3[40].append('1201')
            umumiy_without_duplicate12D3[41].append('X')
            umumiy_without_duplicate12D3[42].append('X')
            umumiy_without_duplicate12D3[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D3[44].append('')
            umumiy_without_duplicate12D3[45].append('X')
            umumiy_without_duplicate12D3[46].append('')
            umumiy_without_duplicate12D3[47].append('X')
            umumiy_without_duplicate12D3[48].append(row['ch_combination'] + row['Тип покрытия'])
        if gruppa_material=='ALUGP':
            ######12D4
            umumiy_without_duplicate12D4[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D4[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D4[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D4[3].append('ШТ')
            umumiy_without_duplicate12D4[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D4[5].append(gruppa_material)
            umumiy_without_duplicate12D4[6].append(gruppa_material)
            umumiy_without_duplicate12D4[7].append('E')
            umumiy_without_duplicate12D4[8].append('01')
            umumiy_without_duplicate12D4[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D4[10].append(row['Общий вес за штуку'])
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
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
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
            umumiy_without_duplicate12D4[40].append('1201')
            umumiy_without_duplicate12D4[41].append('X')
            umumiy_without_duplicate12D4[42].append('X')
            umumiy_without_duplicate12D4[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D4[44].append('')
            umumiy_without_duplicate12D4[45].append('X')
            umumiy_without_duplicate12D4[46].append('')
            umumiy_without_duplicate12D4[47].append('X')
            umumiy_without_duplicate12D4[48].append(row['ch_combination'] + row['Тип покрытия'])
            
        if gruppa_material=='ALUGP':
            ######12D5
            umumiy_without_duplicate12D5[0].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D5[1].append(row['SAP код S4P 100'])
            umumiy_without_duplicate12D5[2].append(row['Короткое название SAP'])
            umumiy_without_duplicate12D5[3].append('ШТ')
            umumiy_without_duplicate12D5[4].append('ZPRF')
            if '-7' in row['SAP код S4P 100']:
                gruppa_material ='ALUGP'
            else:
                gruppa_material ='ALUPF'
            umumiy_without_duplicate12D5[5].append(gruppa_material)
            umumiy_without_duplicate12D5[6].append(gruppa_material)
            umumiy_without_duplicate12D5[7].append('E')
            umumiy_without_duplicate12D5[8].append('01')
            umumiy_without_duplicate12D5[9].append(row['Общий вес за штуку'])
            umumiy_without_duplicate12D5[10].append(row['Общий вес за штуку'])
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
            if gruppa_material =='ALUGP':
                sartrr ='5'
                
            bklast ='0100'
            if gruppa_material =='ALUPF':
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
            umumiy_without_duplicate12D5[40].append('1201')
            umumiy_without_duplicate12D5[41].append('X')
            umumiy_without_duplicate12D5[42].append('X')
            umumiy_without_duplicate12D5[43].append('1')
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
            umumiy_without_duplicate12D5[44].append('')
            umumiy_without_duplicate12D5[45].append('X')
            umumiy_without_duplicate12D5[46].append('')
            umumiy_without_duplicate12D5[47].append('X')
            umumiy_without_duplicate12D5[48].append(row['ch_combination'] + row['Тип покрытия'])
            
        umumiy_without_duplicate1201[0].append(row['SAP код S4P 100'])
        umumiy_without_duplicate1201[1].append(row['SAP код S4P 100'])
        umumiy_without_duplicate1201[2].append(row['Короткое название SAP'])
        umumiy_without_duplicate1201[3].append('ШТ')
        umumiy_without_duplicate1201[4].append('ZPRF')
        if '-7' in row['SAP код S4P 100']:
            gruppa_material ='ALUGP'
        else:
            gruppa_material ='ALUPF'
        umumiy_without_duplicate1201[5].append(gruppa_material)
        umumiy_without_duplicate1201[6].append(gruppa_material)
        umumiy_without_duplicate1201[7].append('E')
        umumiy_without_duplicate1201[8].append('01')
        umumiy_without_duplicate1201[9].append(str(row['Общий вес за штуку']).replace('.',','))
        umumiy_without_duplicate1201[10].append(str(row['Общий вес за штуку']).replace('.',','))
        umumiy_without_duplicate1201[11].append('КГ')
        umumiy_without_duplicate1201[12].append('NORM')
        umumiy_without_duplicate1201[13].append(row['Короткое название SAP'])
        umumiy_without_duplicate1201[14].append('ШТ')
        umumiy_without_duplicate1201[15].append('999')
        umumiy_without_duplicate1201[16].append('X')
        umumiy_without_duplicate1201[17].append('0000')
        umumiy_without_duplicate1201[18].append('PD')
        umumiy_without_duplicate1201[19].append('EX')
        umumiy_without_duplicate1201[20].append('0')
        umumiy_without_duplicate1201[21].append('E')
        ss =''
        sartrr =''
        if gruppa_material =='ALUGP':
            ss ='S400'
            sartrr ='5'
            
        bklast ='0100'
        if gruppa_material =='ALUPF':
            bklast ='0102'
            
            
        umumiy_without_duplicate1201[22].append(ss)
        umumiy_without_duplicate1201[23].append('')
        umumiy_without_duplicate1201[24].append('M')
        umumiy_without_duplicate1201[25].append('02')
        umumiy_without_duplicate1201[26].append('26')
        umumiy_without_duplicate1201[27].append(sartrr)
        umumiy_without_duplicate1201[28].append('X')
        umumiy_without_duplicate1201[29].append('5')
        umumiy_without_duplicate1201[30].append('Z_SAP_PP_002')
        umumiy_without_duplicate1201[31].append('4')
        umumiy_without_duplicate1201[32].append('SAP999')
        umumiy_without_duplicate1201[33].append('26')
        umumiy_without_duplicate1201[34].append('1201')
        umumiy_without_duplicate1201[35].append('3')
        umumiy_without_duplicate1201[36].append(bklast)
        umumiy_without_duplicate1201[37].append('S')
        umumiy_without_duplicate1201[38].append('1')
        umumiy_without_duplicate1201[39].append(row['Price'])
        umumiy_without_duplicate1201[40].append('1201')
        umumiy_without_duplicate1201[41].append('X')
        umumiy_without_duplicate1201[42].append('X')
        umumiy_without_duplicate1201[43].append('1')
        sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]
        umumiy_without_duplicate1201[44].append(SFSPF1201[sap_code_simvol])
        umumiy_without_duplicate1201[45].append('X')
        umumiy_without_duplicate1201[46].append(LGPRO1201[sap_code_simvol])
        umumiy_without_duplicate1201[47].append('X')
        umumiy_without_duplicate1201[48].append(row['ch_combination'] + row['Тип покрытия'])
    
    umumiy_without_duplicate =[[] for i in range(0,49)]
    for i in range(0,len(umumiy_without_duplicate1201)):
        umumiy_without_duplicate[i]+=umumiy_without_duplicate1201[i] 
            
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


    if order_id:
        if is_1112 =='on':
            datas_1112,path_texcarta = characteristika_created_txt_create_1101(datas,elist,is_1101='off',is_1112='on',file_name=file_name)
            order = Order.objects.get(id = order_id)
            paths = order.paths
            paths['texcarta_file'] =f'{MEDIA_ROOT}\\{path_texcarta}'
            paths['status_texcarta'] ='on process'
            file = ExcelFilesImzo(file = path_texcarta)
            file.save()
            paths['texid']= file.id
            order.paths = paths
            order.save()
        elif is_1201 =='on':
            path_texcarta =f'uploads\\texcarta\\1201_not.xlsx'
            order = Order.objects.get(id = order_id)
            paths = order.paths
            paths['texcarta_file'] =f'{MEDIA_ROOT}\\{path_texcarta}'
            paths['status_texcarta'] ='on process'
            file = ExcelFilesImzo(file = path_texcarta)
            file.save()
            paths['texid']= file.id
            order.paths = paths
            order.save()
        else:
            datas_1112,path_texcarta = characteristika_created_txt_create_1101(datas,elist,is_1101='off',is_1112='on',file_name=file_name)
            order = Order.objects.get(id = order_id)
            paths = order.paths
            paths['texcarta_file'] =f'{MEDIA_ROOT}\\{path_texcarta}'
            paths['status_texcarta'] ='on process'
            file = ExcelFilesImzo(file = path_texcarta)
            file.save()
            paths['texid']= file.id
            order.paths = paths
            order.save()
    else:
        path_1101,path_zip2,path_texcarta = characteristika_created_txt_create_1101(datas,elist,is_1101='on',is_1112='off',file_name=file_name)

    if is_1112 =='on':
        ######################### Бухгалтерская название.txt ##############################
        
        buxgalterskiy_t ={}
        header_buxgalter ='ID\tMATNR\tVKORG\tVTWEG\tLANG\tTDID\tPOS\tLTEXT'
        buxgalterskiy_t['ID']=buxgalterskiy_naz[0] + datas_1112[0]['ID']
        buxgalterskiy_t['MATNR']=buxgalterskiy_naz[1] + datas_1112[0]['MATNR']
        buxgalterskiy_t['VKORG']=buxgalterskiy_naz[2] + datas_1112[0]['VKORG']
        buxgalterskiy_t['VTWEG']=buxgalterskiy_naz[3] + datas_1112[0]['VTWEG']
        buxgalterskiy_t['LANG']=buxgalterskiy_naz[4] + datas_1112[0]['LANG']
        buxgalterskiy_t['TDID']=buxgalterskiy_naz[5] + datas_1112[0]['TDID']
        buxgalterskiy_t['POS']=buxgalterskiy_naz[6] + datas_1112[0]['POS']
        buxgalterskiy_t['LTEXT']=buxgalterskiy_naz[7] + datas_1112[0]['LTEXT']
        

        
        df_bug_text= pd.DataFrame(buxgalterskiy_t)
        
        np.savetxt(pathtext8, df_bug_text.values,fmt='%s', delimiter="\t",header=header_buxgalter,comments='',encoding='ansi')
        
        
    ########################## end Бухгалтерская название.txt ##############################
    ########################## Длинный текс.txt ##############################
    #dlinniy_text_zero
        dlinniy_t ={}
        header_dlinniy ='\tBISMT\t\t\t\tTEXT'
        dlinniy_t['ID']=dlinniy_text_zero[0] + datas_1112[1]['ID']
        dlinniy_t['BISMT']=dlinniy_text_zero[1] + datas_1112[1]['BISMT']
        dlinniy_t['RU']=['RU' for x in (dlinniy_text_zero[1])] + datas_1112[1]['RU']
        dlinniy_t['GRUN']=['GRUN' for x in (dlinniy_text_zero[1])]+ datas_1112[1]['GRUN']
        dlinniy_t['sa']=['' for x in (dlinniy_text_zero[1])]+ datas_1112[1]['sa']
        dlinniy_t['TEXT']=dlinniy_text_zero[2]+ datas_1112[1]['TEXT']
        
        df_dlinniy_text= pd.DataFrame(dlinniy_t)
        
        np.savetxt(pathtext7, df_dlinniy_text.values,fmt='%s', delimiter="\t",header=header_dlinniy,comments='',encoding='ansi')
        
        
    ########################## end Длинный текс.txt ##############################

    ########################## Длинный текс Savdo.txt ##############################
    #dlinniy_text_zero
        # dlinniy_t ={}
        # header_dlinniy ='\tMATNR\t\t\t\tTEXT'
        # dlinniy_t['ID']=dlinniy_text_savdo[0] 
        # dlinniy_t['MATNR']=dlinniy_text_savdo[1] 
        # dlinniy_t['RU']=['Z' for x in (dlinniy_text_savdo[1])] 
        # dlinniy_t['GRUN']=['GRUN' for x in (dlinniy_text_savdo[1])]
        # dlinniy_t['sa']=['' for x in (dlinniy_text_savdo[1])]
        # dlinniy_t['TEXT']=dlinniy_text_savdo[2]
        
        # df_dlinniy_text = pd.DataFrame(dlinniy_t)
        
        # np.savetxt(pathtextsavdo, df_dlinniy_text.values,fmt='%s', delimiter="\t",header=header_dlinniy,comments='',encoding='ansi')
        
        
    
    ########################## end Длинный текс.txt ##############################

    ########################## 1.txt ##############################
        d1={}
        header1 ='MATNR\tBISMT\tMAKTX\tMEINS\tMTART\tMATKL\tWERKS\tBESKZ\tSPART\tBRGEW\tNTGEW\tGEWEI\tMTPOS_MARA'
        
        d1['MATNR']=umumiy_without_duplicate1201[0] + datas_1112[2]['MATNR']
        d1['BISMT']=umumiy_without_duplicate1201[1] + datas_1112[2]['BISMT']
        d1['MAKTX']=umumiy_without_duplicate1201[2] + datas_1112[2]['MAKTX']
        d1['MEINS']=umumiy_without_duplicate1201[3] + datas_1112[2]['MEINS']
        d1['MTART']=umumiy_without_duplicate1201[4] + datas_1112[2]['MTART']
        d1['MATKL']=umumiy_without_duplicate1201[5] + datas_1112[2]['MATKL']
        d1['WERKS']=umumiy_without_duplicate1201[34] + datas_1112[2]['WERKS']
        d1['BESKZ']=umumiy_without_duplicate1201[7] + datas_1112[2]['BESKZ']
        d1['SPART']=umumiy_without_duplicate1201[8]+ datas_1112[2]['SPART']
        d1['BRGEW']=[str(round(float(k1.replace(',','.')),3)).replace('.',',') if isinstance(k1,str) else str(round(k1,3)).replace('.',',') for k1 in (umumiy_without_duplicate1201[9])]+ datas_1112[2]['BRGEW']
        d1['NTGEW']=[str(round(float(k2.replace(',','.')),3)).replace('.',',') for k2 in (umumiy_without_duplicate1201[10])]+ datas_1112[2]['NTGEW']
        d1['GEWEI']=umumiy_without_duplicate1201[11]+ datas_1112[2]['GEWEI']
        d1['MTPOS_MARA']=umumiy_without_duplicate1201[12]+ datas_1112[2]['MTPOS_MARA']
        
        
        df1= pd.DataFrame(d1)

        
        
        
        np.savetxt(pathtext1, df1.values,fmt='%s', delimiter="\t",header=header1,comments='',encoding='ansi')
        
    ########################## end 1.txt ##############################

    ########################## 2.txt ##############################
        header2='MAKTX\tMEINS\tMTART\tMATNR\tWERKS\tEKGRP\tXCHPF\tDISGR\tDISMM\tDISPO\tDISLS\tWEBAZ\tBESKZ\tLGFSB\tPLIFZ\tPERKZ\tMTVFP\tSCM_STRA1\tVRMOD\tPPSKZ\tSCM_WHATBOM\tSCM_HEUR_ID\tSCM_RRP_TYPE\tSCM_PROFID\tSTRGR\tBWKEY\tMLAST\tBKLAS\tVPRSV\tPEINH\tSTPRS\tPRCTR\tEKALR\tHKMAT\tLOSGR\tSFCPF\tFEVOR\tUEETK\tLGPRO\tAUTO_P_ORD'
        zavod_code ={
            '1203':'PVC',
            '1201':'PR1',
            '12D1':'001',
            '12D2':'001',
            '12D3':'001',
            '12D4':'001',
            '12D5':'001',
        }
        d2={}
        d2['MAKTX']=umumiy_without_duplicate[13] + datas_1112[3]['MAKTX']
        d2['MEINS']=umumiy_without_duplicate[14] + datas_1112[3]['MEINS']
        d2['MTART']=umumiy_without_duplicate[4] + datas_1112[3]['MTART']
        d2['MATNR']=umumiy_without_duplicate[0] + datas_1112[3]['MATNR']
        d2['WERKS']=umumiy_without_duplicate[34] + datas_1112[3]['WERKS']
        d2['EKGRP']=umumiy_without_duplicate[15] + datas_1112[3]['EKGRP']
        d2['XCHPF']=umumiy_without_duplicate[16] + datas_1112[3]['XCHPF']
        d2['DISGR']=umumiy_without_duplicate[17] + datas_1112[3]['DISGR']
        d2['DISMM']=umumiy_without_duplicate[18] + datas_1112[3]['DISMM']
        d2['DISPO']=[zavod_code[x] for x in umumiy_without_duplicate[34] ]+ datas_1112[3]['DISPO']
        d2['DISLS']=umumiy_without_duplicate[19] + datas_1112[3]['DISLS']
        d2['WEBAZ']=umumiy_without_duplicate[20] + datas_1112[3]['WEBAZ']
        d2['BESKZ']=umumiy_without_duplicate[21] + datas_1112[3]['BESKZ']
        d2['LGFSB']=umumiy_without_duplicate[22] + datas_1112[3]['LGFSB']
        d2['PLIFZ']=umumiy_without_duplicate[23] + datas_1112[3]['PLIFZ']
        d2['PERKZ']=umumiy_without_duplicate[24] + datas_1112[3]['PERKZ']
        d2['MTVFP']=umumiy_without_duplicate[25] + datas_1112[3]['MTVFP']
        d2['SCM_STRA1']=umumiy_without_duplicate[26] + datas_1112[3]['SCM_STRA1']
        d2['VRMOD']=umumiy_without_duplicate[27] + datas_1112[3]['VRMOD']
        d2['PPSKZ']=umumiy_without_duplicate[28] + datas_1112[3]['PPSKZ']
        d2['SCM_WHATBOM']=umumiy_without_duplicate[29] + datas_1112[3]['SCM_WHATBOM']
        d2['SCM_HEUR_ID']=umumiy_without_duplicate[30] + datas_1112[3]['SCM_HEUR_ID']
        d2['SCM_RRP_TYPE']=umumiy_without_duplicate[31] + datas_1112[3]['SCM_RRP_TYPE']
        d2['SCM_PROFID']=umumiy_without_duplicate[32] + datas_1112[3]['SCM_PROFID']
        d2['STRGR']=umumiy_without_duplicate[33] + datas_1112[3]['STRGR']
        d2['BWKEY']=umumiy_without_duplicate[34] + datas_1112[3]['BWKEY']
        d2['MLAST']=umumiy_without_duplicate[35] + datas_1112[3]['MLAST']
        d2['BKLAS']=umumiy_without_duplicate[36] + datas_1112[3]['BKLAS']
        d2['VPRSV']=umumiy_without_duplicate[37] + datas_1112[3]['VPRSV']
        d2['PEINH']=umumiy_without_duplicate[38] + datas_1112[3]['PEINH']
        d2['STPRS']=[round(float(n.replace(',','.')),2) for n in (umumiy_without_duplicate[39] )]+ datas_1112[3]['STPRS']
        d2['PRCTR']=umumiy_without_duplicate[40] + datas_1112[3]['PRCTR']
        d2['EKALR']=umumiy_without_duplicate[41] + datas_1112[3]['EKALR']
        d2['HKMAT']=umumiy_without_duplicate[42] + datas_1112[3]['HKMAT']
        d2['LOSGR']=umumiy_without_duplicate[43] + datas_1112[3]['LOSGR']
        d2['SFCPF']=umumiy_without_duplicate[44] + datas_1112[3]['SFCPF']
        d2['FEVOR']=['' for x in (umumiy_without_duplicate[44])] + datas_1112[3]['FEVOR']
        d2['UEETK']=umumiy_without_duplicate[45] + datas_1112[3]['UEETK']
        d2['LGPRO']=umumiy_without_duplicate[46] + datas_1112[3]['LGPRO']
        d2['AUTO_P_ORD']=umumiy_without_duplicate[47] + datas_1112[3]['AUTO_P_ORD']

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
        KONDM ={
            'с термомостоманодированный':'A0',
            'без термомостаокрашенный':'A1',
            'без термомостабелый':'A1',
            'без термомостасублимированный':'A2',
            'без термомостаанодированный':'A3',
            'без термомосталаминированный':'A4',
            'с термомостомламинированный':'A5',
            'без термомостанеокрашенный':'A6',
            'с термомостомокрашенный':'A7',
            'с термомостомбелый':'A7',
            'с термомостомнеокрашенный':'A8',
            'с термомостомсублимированный':'A9',
        }
        for i in range(0,3):
            d3['MAKTX'] += umumiy_without_duplicate[13] + datas_1112[4]['MAKTX']
            d3['MEINS'] += umumiy_without_duplicate[14] + datas_1112[4]['MEINS']
            d3['MTART'] += umumiy_without_duplicate[4] + datas_1112[4]['MTART']
            d3['SPART'] += umumiy_without_duplicate[8] + datas_1112[4]['SPART']
            d3['MATNR'] += umumiy_without_duplicate[0] + datas_1112[4]['MATNR']
            d3['WERKS'] += umumiy_without_duplicate[34] + datas_1112[4]['WERKS']
            d3['VKORG'] += [ 1200 for j in range(0,len(umumiy_without_duplicate[13] ))]+ datas_1112[4]['VKORG']
            d3['MTPOS'] += umumiy_without_duplicate[12] + datas_1112[4]['MTPOS']
            d3['VTWEG'] += [ VTWEG[i] for j in range(0,len(umumiy_without_duplicate[13] ))]+ datas_1112[4]['VTWEG']
            d3['PRCTR'] += [ '1203' if umumiy_without_duplicate[34][i] =='1203' else '1201' for i in range(0,len(umumiy_without_duplicate[34]))] + datas_1112[4]['PRCTR']
            d3['MTVFP'] += [ '02' for j in range(0,len(umumiy_without_duplicate[13] ))]+ datas_1112[4]['MTVFP']
            d3['ALAND'] += [ 'UZ' for j in range(0,len(umumiy_without_duplicate[13]))] + datas_1112[4]['ALAND']
            d3['TATYP'] += [ 'MWST' for j in range(0,len(umumiy_without_duplicate[13]))] + datas_1112[4]['TATYP']
            d3['TAXKM'] += [ '1' for j in range(0,len(umumiy_without_duplicate[13]))] + datas_1112[4]['TAXKM']
            d3['VERSG'] += [ '1' for j in range(0,len(umumiy_without_duplicate[13] ))]+ datas_1112[4]['VERSG']
            d3['KTGRM'] += [ '01' for j in range(0,len(umumiy_without_duplicate[13]))] + datas_1112[4]['KTGRM']
            if i!=2:
                d3['KONDM'] += [ '01' for j in range(0,len(umumiy_without_duplicate[13] ))]+ datas_1112[4]['KONDM']
            else:
                d3['KONDM'] += [ '01' if '-7' not in umumiy_without_duplicate[0][x] else KONDM[umumiy_without_duplicate[48][x].lower()] for x in range(0,len(umumiy_without_duplicate[0]))]  + datas_1112[4]['KONDM']
                
            d3['LADGR'] += [ '0001' for j in range(0,len(umumiy_without_duplicate[13]))] + datas_1112[4]['LADGR']
            d3['TRAGR'] += [ '0001' for j in range(0,len(umumiy_without_duplicate[13]))] + datas_1112[4]['TRAGR']
        df3= pd.DataFrame(d3)
        np.savetxt(pathtext3, df3.values, fmt='%s', delimiter="\t",header=header3,comments='',encoding='ansi')
    ########################## end 3.txt ##############################
        
    ########################## 4.txt ##############################    
        new_ll =[[],[],[]]
        sap_code_title =[]
        dlina_title =[]
        obshiy_ves_za_shtuku =[]
        wms_width =[]
        wms_height =[]
        
        for key , row in datas.iterrows():
            sap_code_title.append(row['SAP код S4P 100'])
            dlina_title.append(row['Длина'])
            obshiy_ves_za_shtuku.append(row['Общий вес за штуку'].replace(',','.'))
            wms_width.append(row['WMS_WIDTH'])
            wms_height.append(row['WMS_HEIGHT'])

            
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]        
            if sap_code_simvol =='E':
                for i in range(0,len(LGORT['E'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['E'][i]['zavod_code'])
                    new_ll[2].append(LGORT['E'][i]['zavod_sap'])
            if sap_code_simvol =='Z':
                for i in range(0,len(LGORT['Z'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['Z'][i]['zavod_code'])
                    new_ll[2].append(LGORT['Z'][i]['zavod_sap'])
            if sap_code_simvol =='P':
                if (row['Тип покрытия'] =='Ламинированный'):
                    for i in range(0,len(LGORT['PL'])):
                        new_ll[0].append(row['SAP код S4P 100'])
                        new_ll[1].append(LGORT['PL'][i]['zavod_code'])
                        new_ll[2].append(LGORT['PL'][i]['zavod_sap'])
                else:
                    for i in range(0,len(LGORT['P'])):
                        new_ll[0].append(row['SAP код S4P 100'])
                        new_ll[1].append(LGORT['P'][i]['zavod_code'])
                        new_ll[2].append(LGORT['P'][i]['zavod_sap'])
            
            if sap_code_simvol =='S':
                for i in range(0,len(LGORT['S'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['S'][i]['zavod_code'])
                    new_ll[2].append(LGORT['S'][i]['zavod_sap'])
            if sap_code_simvol =='N':
                for i in range(0,len(LGORT['N'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['N'][i]['zavod_code'])
                    new_ll[2].append(LGORT['N'][i]['zavod_sap'])
            if sap_code_simvol =='K':
                for i in range(0,len(LGORT['K'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['K'][i]['zavod_code'])
                    new_ll[2].append(LGORT['K'][i]['zavod_sap'])
            if sap_code_simvol =='A':
                for i in range(0,len(LGORT['A'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['A'][i]['zavod_code'])
                    new_ll[2].append(LGORT['A'][i]['zavod_sap'])
            
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
            
            if sap_code_simvol =='F':
                for i in range(0,len(LGORT['F'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['F'][i]['zavod_code'])
                    new_ll[2].append(LGORT['F'][i]['zavod_sap'])

        header4='MATNR\tWERKS\tLGORT\tRAUBE'
        d4={}
        d4['MATNR']=new_ll[0] + datas_1112[5]['MATNR']
        d4['WERKS']=new_ll[1] + datas_1112[5]['WERKS']
        d4['LGORT']=new_ll[2] + datas_1112[5]['LGORT']
        d4['RAUBE']=['' for x in new_ll[2]] + datas_1112[5]['RAUBE']
        df4= pd.DataFrame(d4)
        np.savetxt(pathtext4, df4.values, fmt='%s', delimiter="\t",header=header4,comments='',encoding='ansi')
    ########################## end 4.txt ##############################

    ########################## 55.txt ##############################    
        # new_ll_55 =[[],[],[]]
        
        # for key , row in datas.iterrows():
        #     sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]        
            
        #     if sap_code_simvol =='7':
        #         if (row['Тип покрытия'] =='Ламинированный'):
        #             for i in range(0,len(LGORT['7L'])):
        #                 new_ll_55[0].append(row['SAP код S4P 100'])
        #                 new_ll_55[1].append(LGORT['7L'][i]['zavod_code'])
        #                 new_ll_55[2].append(LGORT['7L'][i]['zavod_sap'])
        #         else:
        #             for i in range(0,len(LGORT['7'])):
        #                 new_ll_55[0].append(row['SAP код S4P 100'])
        #                 new_ll_55[1].append(LGORT['7'][i]['zavod_code'])
        #                 new_ll_55[2].append(LGORT['7'][i]['zavod_sap'])
        if is_1112 =='on':
            header55 = 'MATNR\tWERKS\tRAUBE'
            df55= pd.DataFrame(datas_1112[8])
            df55=df55.drop_duplicates()
            np.savetxt(pathtext55, df55.values, fmt='%s', delimiter="\t",header=header55,comments='',encoding='ansi')
    ########################## end 55.txt ##############################
        
    ########################## 5.txt ##############################
        d5 ={
            'sap_code':[],
            'ed_iz1':[],
            'ed_iz2':[],
            'ed_iz3':[],
            'ed_iz4':[],
            'ed_iz5':[],
            'ed_iz6':[],
            'ed_iz7':[]
        }
        ED_IZM =['ШТ','М','КГ']
        
        # sap_code_title =[]
        # dlina_title =[]
        # obshiy_ves_za_shtuku =[]
        # wms_width =[]
        # wms_height =[]
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
            d5['ed_iz2'] +=['1' if i =='ШТ' else '1000'  for j in range(0,len(sap_code_title)) ]
            # d5['ed_iz3'] +=['1' if i =='ШТ' elif i=='М' for j in range(0,len(sap_code_title)) ]
            d5['ed_iz4'] +=[j for j in dlina_title ]
            d5['ed_iz5'] +=[j for j in wms_height ]
            d5['ed_iz6'] +=[j for j in wms_width ]
            d5['ed_iz7'] +=[ 'мм' for j in range(0,len(sap_code_title))]
        
        d5['sap_code'] += datas_1112[6]['sap_code']
        d5['ed_iz1'] += datas_1112[6]['ed_iz1']
        d5['ed_iz2'] += datas_1112[6]['ed_iz2']
        d5['ed_iz4'] += datas_1112[6]['ed_iz4']
        d5['ed_iz5'] += datas_1112[6]['ed_iz5']
        d5['ed_iz6'] += datas_1112[6]['ed_iz6']
        d5['ed_iz7'] += datas_1112[6]['ed_iz7']

        d5['ed_iz3'] = ed_iz3 + datas_1112[6]['ed_iz3']
        df5= pd.DataFrame(d5)
        np.savetxt(pathtext5, df5.values, fmt='%s', delimiter="\t",encoding='ansi')
    ########################## end 5.txt ##############################
    ########################## List v 3 ##############################
        dd2 = [[],[],[],[],[],[]]
        baza_profile_links =[[],[]]
        

        for key , row in datas.iterrows():
            sap_code = row['SAP код S4P 100'].split('-')[0]
            bazaprofiley =AluProfilesData.objects.filter(Q(data__Артикул =sap_code)|Q(data__Компонент=sap_code))[:1].get()    
            baza_profile_links[0].append(row['SAP код S4P 100'])
            baza_profile_links[1].append(bazaprofiley.data['Ссылка для чертежей'])

            row['ch_tnved'] =str(row['ch_tnved']).replace('.0','')
            row['ch_outer_side_pc_id'] =str(row['ch_outer_side_pc_id']).replace('.0','')
            row['ch_outer_side_pc_brand'] =str(row['ch_outer_side_pc_brand']).replace('.0','')
            row['ch_inner_side_pc_id'] =str(row['ch_inner_side_pc_id']).replace('.0','')
            row['ch_inner_side_pc_brand'] =str(row['ch_inner_side_pc_brand']).replace('.0','')
            row['ch_outer_side_wg_s_id'] =str(row['ch_outer_side_wg_s_id']).replace('.0','')
            row['ch_inner_side_wg_s_id'] =str(row['ch_inner_side_wg_s_id']).replace('.0','')
            row['ch_outer_side_wg_id'] =str(row['ch_outer_side_wg_id']).replace('.0','')
            row['ch_inner_side_wg_id'] =str(row['ch_inner_side_wg_id']).replace('.0','')
            row['ch_width'] =str(row['ch_width']).replace('.0','')
            row['ch_height'] =str(row['ch_height']).replace('.0','')
            
            if (('-E' in row['SAP код S4P 100']) or ('-Z' in row['SAP код S4P 100']) or ('-P' in row['SAP код S4P 100']) or ('-A' in row['SAP код S4P 100']) or ('-S' in row['SAP код S4P 100'])):

                for j in range(0,32):
                    dd2[0].append('001')
                dd2[0].append('023')
                    
                for j in range(0,32):
                    if HEADER2[j] not in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT','TNVED']:

                        dd2[1].append('ALUMINIUM_PROFILE')
                    else:
                        if HEADER2[j] in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT']:
                            dd2[1].append('RAWMAT_TYPE')
                        elif HEADER2[j] =='TNVED':
                            dd2[1].append('TNVED')
                dd2[1].append('ZPP_023_HALB')
                    
                for j in range(0,33):
                    dd2[2].append('MARA')
                    
                for j in range(0,33):
                    dd2[3].append(row['SAP код S4P 100'])
                    
                for j in HEADER2:
                    dd2[4].append(j)
                dd2[4].append('ZBATCH_NUM')


                dd2[5].append('')
                dd2[5].append('')
                dd2[5].append(row['ch_system'])
                dd2[5].append(row['SAP код S4P 100'].split('-')[0])
                dd2[5].append(row['Длина'])
                dd2[5].append(row['Тип покрытия'])
                dd2[5].append(row['ch_alloy'])
                dd2[5].append(row['ch_temper'])
                dd2[5].append(row['ch_combination'])
                dd2[5].append(row['ch_outer_side_pc_id'])
                dd2[5].append(row['ch_outer_side_pc_brand'])
                dd2[5].append(row['ch_inner_side_pc_id'])
                dd2[5].append(row['ch_inner_side_pc_brand'])
                dd2[5].append(row['ch_outer_side_wg_s_id'])
                dd2[5].append(row['ch_inner_side_wg_s_id'])
                dd2[5].append(row['ch_outer_side_wg_id'])
                dd2[5].append(row['ch_inner_side_wg_id'])
            
                if row['ch_anodization_contact'].lower() =='yc':
                    dd2[5].append('С КОНТАКТОМ')
                elif row['ch_anodization_contact'].lower()=='nc' :
                    dd2[5].append('БЕЗ КОНТАКТА')
                else:
                    dd2[5].append(row['ch_anodization_contact'])

                dd2[5].append(row['ch_anodization_type'])
                dd2[5].append(row['ch_anodization_method'])
                dd2[5].append(row['ch_profile_base'])
                dd2[5].append(row['ch_width'])
                dd2[5].append(row['ch_height'])
                dd2[5].append(row['ch_category'])
                dd2[5].append(row['ch_rawmat_type'])
                dd2[5].append('')
                dd2[5].append(row['ch_tnved'])
                dd2[5].append(str(row['ch_surface_treatment_export']).replace('.0',''))
                dd2[5].append(row['WMS_WIDTH'])
                dd2[5].append(row['WMS_HEIGHT'])
                dd2[5].append('')
                dd2[5].append(bazaprofiley.data['Тип Комбинация'])
                dd2[5].append('XXXX')
            else:
                
                for j in range(0,33):
                    dd2[0].append('001')
                    
                for j in range(0,33):
                    if HEADER[j] not in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT','TNVED']:
                        dd2[1].append('ALUMINIUM_PROFILE')
                    else:
                        if HEADER[j] in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT']:
                            dd2[1].append('RAWMAT_TYPE')
                        elif HEADER[j] =='TNVED':
                            dd2[1].append('TNVED')

                if '-7' in row['SAP код S4P 100']:
                    dd2[0].append('001')
                    dd2[0].append('023')
                    dd2[1].append('QBIC')
                    dd2[1].append('ZPP_023_FERT')
                else:
                    dd2[0].append('023')
                    dd2[1].append('ZPP_023_HALB')

                for j in range(0,33):
                    dd2[2].append('MARA')
                    
                for j in range(0,33):
                    dd2[3].append(row['SAP код S4P 100'])
                    
                for j in HEADER:
                    dd2[4].append(j)

                if '-7' in row['SAP код S4P 100']:
                    dd2[2].append('MARA')
                    dd2[2].append('MARA')
                    dd2[3].append(row['SAP код S4P 100'])
                    dd2[3].append(row['SAP код S4P 100'])
                    dd2[4].append('COATING_QBIC')
                    dd2[4].append('ZBATCH_NUM')
                else:
                    dd2[2].append('MARA')
                    dd2[3].append(row['SAP код S4P 100'])
                    dd2[4].append('ZBATCH_NUM')

                dd2[5].append('')
                dd2[5].append('')
                dd2[5].append(row['ch_system'])
                dd2[5].append(row['SAP код S4P 100'].split('-')[0])
                dd2[5].append(row['Длина'])
                dd2[5].append(row['Тип покрытия'])
                dd2[5].append(row['ch_alloy'])
                dd2[5].append(row['ch_temper'])
                dd2[5].append(row['ch_combination'])
                dd2[5].append(row['ch_outer_side_pc_id'])
                dd2[5].append(row['ch_outer_side_pc_brand'])
                dd2[5].append(row['ch_inner_side_pc_id'])
                dd2[5].append(row['ch_inner_side_pc_brand'])
                dd2[5].append(row['ch_outer_side_wg_s_id'])
                dd2[5].append(row['ch_inner_side_wg_s_id'])
                dd2[5].append(row['ch_outer_side_wg_id'])
                dd2[5].append(row['ch_inner_side_wg_id'])
                
                if row['ch_anodization_contact'].lower() =='yc':
                    dd2[5].append('С КОНТАКТОМ')
                elif row['ch_anodization_contact'].lower()=='nc' :
                    dd2[5].append('БЕЗ КОНТАКТА')
                else:
                    dd2[5].append(row['ch_anodization_contact'])
                
                dd2[5].append(row['ch_anodization_type'])
                dd2[5].append(row['ch_anodization_method'])
                dd2[5].append(row['ch_print_view'])
                dd2[5].append(row['ch_profile_base'])
                dd2[5].append(row['ch_width'])
                dd2[5].append(row['ch_height'])
                dd2[5].append(row['ch_category'])
                dd2[5].append(row['ch_rawmat_type'])
                dd2[5].append('')
                dd2[5].append(row['ch_tnved'])
                dd2[5].append(str(row['ch_surface_treatment_export']).replace('.0',''))
                dd2[5].append(row['WMS_WIDTH'])
                dd2[5].append(row['WMS_HEIGHT'])
                dd2[5].append('')
                dd2[5].append(bazaprofiley.data['Тип Комбинация'])
                if '-7' in row['SAP код S4P 100']:
                    if row['Тип покрытия'] =='Неокрашенный':
                        qbic ='XXXX'
                    elif row['Тип покрытия'] =='Окрашенный':
                        qbic = row['ch_outer_side_pc_id']
                    elif row['Тип покрытия'] =='Анодированный':
                        qbic = row['ch_outer_side_pc_id']
                    elif row['Тип покрытия'] =='Ламинированный':
                        if row['ch_outer_side_wg_id'] =='XXXX':
                            qbic = row['ch_inner_side_wg_id']
                        else:
                            qbic = row['ch_outer_side_wg_id']
                    elif row['Тип покрытия'] =='Сублимированный':
                        qbic = row['ch_outer_side_wg_s_id']
                    else:
                        qbic ='XXXX'
                    dd2[5].append(qbic)
                    dd2[5].append('XXXX')
                else:
                    dd2[5].append('XXXX')




        new_date={}       
        new_date['Вид класса'] = dd2[0]  + datas_1112[7]['Вид класса']
        new_date['Класс'] = dd2[1] + datas_1112[7]['Класс']
        new_date['Таблица'] = dd2[2] + datas_1112[7]['Таблица']
        new_date['Объект'] = dd2[3] + datas_1112[7]['Объект']
        new_date['Имя признака'] = dd2[4] + datas_1112[7]['Имя признака']
        new_date['Значение признака'] = dd2[5] + datas_1112[7]['Значение признака']
        new_date['Статус загрузки'] = ['' for x in dd2[5] ] + datas_1112[7]['Статус загрузки']
        
        
        df_baza_profiley_link = pd.DataFrame({'SAP CODE':baza_profile_links[0],'link':baza_profile_links[1]})
        df_baza_profiley_link.to_excel(pathtext9,index=False)
        
        ddf2 = pd.DataFrame(new_date)
        ddf2 = ddf2[((ddf2["Значение признака"] != "nan") & (ddf2["Значение признака"] != ""))]
        ddf2 =ddf2.replace('XXXX','')
        ddf2.to_excel(pathtext6,index=False)
        grouped_by_name = ddf2.groupby('Имя признака')

        # Save each group to a separate Excel file named after the unique value in the "Имя признака" column
        for group_name, group_df in grouped_by_name:
            # Remove duplicates
            group_df = group_df.drop_duplicates()
            
            # Prepare the output file path using the group_name
            output_file = f'{char_path}\\{group_name}.xlsx'
            
            
            # Save the group to Excel
            group_df.to_excel(output_file, index=False)
    
    else:
    ########################## Бухгалтерская название.txt ##############################
        
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
        dlinniy_t['RU']=['RU' for x in dlinniy_text_zero[1]]
        dlinniy_t['GRUN']=['GRUN' for x in dlinniy_text_zero[1]]
        dlinniy_t['sa']=['' for x in dlinniy_text_zero[1]]
        dlinniy_t['TEXT']=dlinniy_text_zero[2]
        
        df_dlinniy_text= pd.DataFrame(dlinniy_t)
        
        np.savetxt(pathtext7, df_dlinniy_text.values,fmt='%s', delimiter="\t",header=header_dlinniy,comments='',encoding='ansi')
        
        
    ########################## end Длинный текс.txt ##############################
    ########################## Длинный текс Savdo.txt ##############################
    #dlinniy_text_zero
        dlinniy_t ={}
        header_dlinniy ='\tMATNR\t\t\t\tTEXT'
        dlinniy_t['ID']=dlinniy_text_savdo[0] 
        dlinniy_t['MATNR']=dlinniy_text_savdo[1] 
        dlinniy_t['RU']=['Z' for x in (dlinniy_text_savdo[1])] 
        dlinniy_t['GRUN']=['GRUN' for x in (dlinniy_text_savdo[1])]
        dlinniy_t['sa']=['' for x in (dlinniy_text_savdo[1])]
        dlinniy_t['TEXT']=dlinniy_text_savdo[2]
        
        df_dlinniy_text = pd.DataFrame(dlinniy_t)
        
        np.savetxt(pathtextsavdo, df_dlinniy_text.values,fmt='%s', delimiter="\t",header=header_dlinniy,comments='',encoding='ansi')
        
        
    
    ########################## end Длинный текс.txt ##############################


    ########################## 1.txt ##############################
        d1={}
        header1 ='MATNR\tBISMT\tMAKTX\tMEINS\tMTART\tMATKL\tWERKS\tBESKZ\tSPART\tBRGEW\tNTGEW\tGEWEI\tMTPOS_MARA'
        
        d1['MATNR']=umumiy_without_duplicate1201[0]
        d1['BISMT']=umumiy_without_duplicate1201[1]
        d1['MAKTX']=umumiy_without_duplicate1201[2]
        d1['MEINS']=umumiy_without_duplicate1201[3]
        d1['MTART']=umumiy_without_duplicate1201[4]
        d1['MATKL']=umumiy_without_duplicate1201[5]
        d1['WERKS']=umumiy_without_duplicate1201[34]
        d1['BESKZ']=umumiy_without_duplicate1201[7]
        d1['SPART']=umumiy_without_duplicate1201[8]
        d1['BRGEW']=[str(round(float(k1.replace(',','.')),3)).replace('.',',') if isinstance(k1,str) else str(round(k1,3)).replace('.',',') for k1 in umumiy_without_duplicate1201[9]]
        d1['NTGEW']=[str(round(float(k2.replace(',','.')),3)).replace('.',',') for k2 in umumiy_without_duplicate1201[10]]
        d1['GEWEI']=umumiy_without_duplicate1201[11]
        d1['MTPOS_MARA']=umumiy_without_duplicate1201[12]
        
        
        df1= pd.DataFrame(d1)
        
        np.savetxt(pathtext1, df1.values,fmt='%s', delimiter="\t",header=header1,comments='',encoding='ansi')
        
    ########################## end 1.txt ##############################

    ########################## 2.txt ##############################
        header2='MAKTX\tMEINS\tMTART\tMATNR\tWERKS\tEKGRP\tXCHPF\tDISGR\tDISMM\tDISPO\tDISLS\tWEBAZ\tBESKZ\tLGFSB\tPLIFZ\tPERKZ\tMTVFP\tSCM_STRA1\tVRMOD\tPPSKZ\tSCM_WHATBOM\tSCM_HEUR_ID\tSCM_RRP_TYPE\tSCM_PROFID\tSTRGR\tBWKEY\tMLAST\tBKLAS\tVPRSV\tPEINH\tSTPRS\tPRCTR\tEKALR\tHKMAT\tLOSGR\tSFCPF\tFEVOR\tUEETK\tLGPRO\tAUTO_P_ORD'
        zavod_code ={
            '1203':'PVC',
            '1201':'PR1',
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
        d2['DISPO']=[zavod_code[x] for x in umumiy_without_duplicate[34]]
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
        d2['STPRS']=[round(float(n.replace(',','.')),2) for n in umumiy_without_duplicate[39]]
        d2['PRCTR']=umumiy_without_duplicate[40]
        d2['EKALR']=umumiy_without_duplicate[41]
        d2['HKMAT']=umumiy_without_duplicate[42]
        d2['LOSGR']=umumiy_without_duplicate[43]
        d2['SFCPF']=umumiy_without_duplicate[44]
        d2['FEVOR']=['' for x in umumiy_without_duplicate[44]]
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
        VTWEG =['99','10','20']
        KONDM ={
            'с термомостоманодированный':'A0',
            'без термомостаокрашенный':'A1',
            'без термомостабелый':'A1',
            'без термомостасублимированный':'A2',
            'без термомостаанодированный':'A3',
            'без термомосталаминированный':'A4',
            'с термомостомламинированный':'A5',
            'без термомостанеокрашенный':'A6',
            'с термомостомокрашенный':'A7',
            'с термомостомбелый':'A7',
            'с термомостомнеокрашенный':'A8',
            'с термомостомсублимированный':'A9',
        }
        for i in range(0,3):
            d3['MAKTX'] += umumiy_without_duplicate[13]
            d3['MEINS'] += umumiy_without_duplicate[14]
            d3['MTART'] += umumiy_without_duplicate[4]
            d3['SPART'] += umumiy_without_duplicate[8]
            d3['MATNR'] += umumiy_without_duplicate[0]
            d3['WERKS'] += umumiy_without_duplicate[34]
            d3['VKORG'] += [ 1200 for j in range(0,len(umumiy_without_duplicate[13]))]
            d3['MTPOS'] += umumiy_without_duplicate[12]
            d3['VTWEG'] += [ VTWEG[i] for j in range(0,len(umumiy_without_duplicate[13]))]
            d3['PRCTR'] += [ '1203' if umumiy_without_duplicate[34][i] =='1203' else '1201' for i in range(0,len(umumiy_without_duplicate[34]))]
            d3['MTVFP'] += [ '02' for j in range(0,len(umumiy_without_duplicate[13]))]
            d3['ALAND'] += [ 'UZ' for j in range(0,len(umumiy_without_duplicate[13]))]
            d3['TATYP'] += [ 'MWST' for j in range(0,len(umumiy_without_duplicate[13]))]
            d3['TAXKM'] += [ '1' for j in range(0,len(umumiy_without_duplicate[13]))]
            d3['VERSG'] += [ '1' for j in range(0,len(umumiy_without_duplicate[13]))]
            d3['KTGRM'] += [ '01' for j in range(0,len(umumiy_without_duplicate[13]))]
            if i!=2:
                d3['KONDM'] += [ '01' for j in range(0,len(umumiy_without_duplicate[13]))]
            else:
                d3['KONDM'] += [ '01' if '-7' not in umumiy_without_duplicate[0][x] else KONDM[umumiy_without_duplicate[48][x].lower()] for x in range(0,len(umumiy_without_duplicate[0]))]
                
            d3['LADGR'] += [ '0001' for j in range(0,len(umumiy_without_duplicate[13]))]
            d3['TRAGR'] += [ '0001' for j in range(0,len(umumiy_without_duplicate[13]))]
        df3= pd.DataFrame(d3)
        np.savetxt(pathtext3, df3.values, fmt='%s', delimiter="\t",header=header3,comments='',encoding='ansi')
    ########################## end 3.txt ##############################
        
    ########################## 4.txt ##############################    
        new_ll =[[],[],[]]
        sap_code_title =[]
        dlina_title =[]
        obshiy_ves_za_shtuku =[]
        wms_width =[]
        wms_height =[]
        
        for key , row in datas.iterrows():
            sap_code_title.append(row['SAP код S4P 100'])
            dlina_title.append(row['Длина'])
            obshiy_ves_za_shtuku.append(row['Общий вес за штуку'].replace(',','.'))
            wms_width.append(row['WMS_WIDTH'])
            wms_height.append(row['WMS_HEIGHT'])

            
            sap_code_simvol =row['SAP код S4P 100'].split('-')[1][0]        
            if sap_code_simvol =='E':
                for i in range(0,len(LGORT['E'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['E'][i]['zavod_code'])
                    new_ll[2].append(LGORT['E'][i]['zavod_sap'])
            if sap_code_simvol =='Z':
                for i in range(0,len(LGORT['Z'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['Z'][i]['zavod_code'])
                    new_ll[2].append(LGORT['Z'][i]['zavod_sap'])
            if sap_code_simvol =='P':
                if (row['Тип покрытия'] =='Ламинированный'):
                    for i in range(0,len(LGORT['PL'])):
                        new_ll[0].append(row['SAP код S4P 100'])
                        new_ll[1].append(LGORT['PL'][i]['zavod_code'])
                        new_ll[2].append(LGORT['PL'][i]['zavod_sap'])
                else:
                    for i in range(0,len(LGORT['P'])):
                        new_ll[0].append(row['SAP код S4P 100'])
                        new_ll[1].append(LGORT['P'][i]['zavod_code'])
                        new_ll[2].append(LGORT['P'][i]['zavod_sap'])
            
            if sap_code_simvol =='S':
                for i in range(0,len(LGORT['S'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['S'][i]['zavod_code'])
                    new_ll[2].append(LGORT['S'][i]['zavod_sap'])
            if sap_code_simvol =='N':
                for i in range(0,len(LGORT['N'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['N'][i]['zavod_code'])
                    new_ll[2].append(LGORT['N'][i]['zavod_sap'])
            if sap_code_simvol =='K':
                for i in range(0,len(LGORT['K'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['K'][i]['zavod_code'])
                    new_ll[2].append(LGORT['K'][i]['zavod_sap'])
            if sap_code_simvol =='A':
                for i in range(0,len(LGORT['A'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['A'][i]['zavod_code'])
                    new_ll[2].append(LGORT['A'][i]['zavod_sap'])
            
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
            
            if sap_code_simvol =='F':
                for i in range(0,len(LGORT['F'])):
                    new_ll[0].append(row['SAP код S4P 100'])
                    new_ll[1].append(LGORT['F'][i]['zavod_code'])
                    new_ll[2].append(LGORT['F'][i]['zavod_sap'])

        header4='MATNR\tWERKS\tLGORT\tRAUBE'
        d4={}
        d4['MATNR']=new_ll[0]
        d4['WERKS']=new_ll[1]
        d4['LGORT']=new_ll[2]
        d4['RAUBE']=['' for x in new_ll[0]]
        df4= pd.DataFrame(d4)
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
        d55['MATNR']=[] 
        d55['WERKS']=[]
        d55['RAUBE']=[] 
        df55= pd.DataFrame(d55)
        df55=df55.drop_duplicates()
        np.savetxt(pathtext55, df55.values, fmt='%s', delimiter="\t",header=header55,comments='',encoding='ansi')
    ########################## end 55.txt ##############################
        
    ########################## 5.txt ##############################
        d5 ={
            'sap_code':[],
            'ed_iz1':[],
            'ed_iz2':[],
            'ed_iz3':[],
            'ed_iz4':[],
            'ed_iz5':[],
            'ed_iz6':[],
            'ed_iz7':[]
        }
        ED_IZM =['ШТ','М','КГ']
        
        # sap_code_title =[]
        # dlina_title =[]
        # obshiy_ves_za_shtuku =[]
        # wms_width =[]
        # wms_height =[]
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
            d5['ed_iz2'] +=['1' if i =='ШТ' else '1000'  for j in range(0,len(sap_code_title)) ]
            # d5['ed_iz3'] +=['1' if i =='ШТ' elif i=='М' for j in range(0,len(sap_code_title)) ]
            d5['ed_iz4'] +=[j for j in dlina_title ]
            d5['ed_iz5'] +=[j for j in wms_height ]
            d5['ed_iz6'] +=[j for j in wms_width ]
            d5['ed_iz7'] +=[ 'мм' for j in range(0,len(sap_code_title))]
        
        d5['ed_iz3'] = ed_iz3
        df5= pd.DataFrame(d5)
        np.savetxt(pathtext5, df5.values, fmt='%s', delimiter="\t",encoding='ansi')
    ########################## end 5.txt ##############################
    ########################## List v 3 ##############################
        dd2 = [[],[],[],[],[],[]]
        baza_profile_links =[[],[]]
        

        for key , row in datas.iterrows():
            sap_code = row['SAP код S4P 100'].split('-')[0]
            bazaprofiley =AluProfilesData.objects.filter(Q(data__Артикул =sap_code)|Q(data__Компонент=sap_code))[:1].get()    
            baza_profile_links[0].append(row['SAP код S4P 100'])
            baza_profile_links[1].append(bazaprofiley.data['Ссылка для чертежей'])

            row['ch_tnved'] =str(row['ch_tnved']).replace('.0','')
            row['ch_outer_side_pc_id'] =str(row['ch_outer_side_pc_id']).replace('.0','')
            row['ch_outer_side_pc_brand'] =str(row['ch_outer_side_pc_brand']).replace('.0','')
            row['ch_inner_side_pc_id'] =str(row['ch_inner_side_pc_id']).replace('.0','')
            row['ch_inner_side_pc_brand'] =str(row['ch_inner_side_pc_brand']).replace('.0','')
            row['ch_outer_side_wg_s_id'] =str(row['ch_outer_side_wg_s_id']).replace('.0','')
            row['ch_inner_side_wg_s_id'] =str(row['ch_inner_side_wg_s_id']).replace('.0','')
            row['ch_outer_side_wg_id'] =str(row['ch_outer_side_wg_id']).replace('.0','')
            row['ch_inner_side_wg_id'] =str(row['ch_inner_side_wg_id']).replace('.0','')
            row['ch_width'] =str(row['ch_width']).replace('.0','')
            row['ch_height'] =str(row['ch_height']).replace('.0','')
            
            if (('-E' in row['SAP код S4P 100']) or ('-Z' in row['SAP код S4P 100']) or ('-P' in row['SAP код S4P 100']) or ('-A' in row['SAP код S4P 100']) or ('-S' in row['SAP код S4P 100'])):

                for j in range(0,32):
                    dd2[0].append('001')
                dd2[0].append('023')
                    
                for j in range(0,32):
                    if HEADER2[j] not in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT','TNVED']:

                        dd2[1].append('ALUMINIUM_PROFILE')
                    else:
                        if HEADER2[j] in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT']:
                            dd2[1].append('RAWMAT_TYPE')
                        elif HEADER2[j] =='TNVED':
                            dd2[1].append('TNVED')
                dd2[1].append('ZPP_023_HALB')
                    
                for j in range(0,33):
                    dd2[2].append('MARA')
                    
                for j in range(0,33):
                    dd2[3].append(row['SAP код S4P 100'])
                    
                for j in HEADER2:
                    dd2[4].append(j)
                dd2[4].append('ZBATCH_NUM')


                dd2[5].append('')
                dd2[5].append('')
                dd2[5].append(row['ch_system'])
                dd2[5].append(row['SAP код S4P 100'].split('-')[0])
                dd2[5].append(row['Длина'])
                dd2[5].append(row['Тип покрытия'])
                dd2[5].append(row['ch_alloy'])
                dd2[5].append(row['ch_temper'])
                dd2[5].append(row['ch_combination'])
                dd2[5].append(row['ch_outer_side_pc_id'])
                dd2[5].append(row['ch_outer_side_pc_brand'])
                dd2[5].append(row['ch_inner_side_pc_id'])
                dd2[5].append(row['ch_inner_side_pc_brand'])
                dd2[5].append(row['ch_outer_side_wg_s_id'])
                dd2[5].append(row['ch_inner_side_wg_s_id'])
                dd2[5].append(row['ch_outer_side_wg_id'])
                dd2[5].append(row['ch_inner_side_wg_id'])

                

                if row['ch_anodization_contact'].lower() =='yc' :
                    dd2[5].append('С КОНТАКТОМ')
                elif row['ch_anodization_contact'].lower()=='nc' :
                    dd2[5].append('БЕЗ КОНТАКТА')
                else:
                    # print('>>>>>>>',row['ch_anodization_contact'])
                    dd2[5].append(row['ch_anodization_contact'])

                dd2[5].append(row['ch_anodization_type'])
                dd2[5].append(row['ch_anodization_method'])
                dd2[5].append(row['ch_profile_base'])
                dd2[5].append(row['ch_width'])
                dd2[5].append(row['ch_height'])
                dd2[5].append(row['ch_category'])
                dd2[5].append(row['ch_rawmat_type'])
                dd2[5].append('')
                dd2[5].append(row['ch_tnved'])
                dd2[5].append(str(row['ch_surface_treatment_export']).replace('.0',''))
                dd2[5].append(row['WMS_WIDTH'])
                dd2[5].append(row['WMS_HEIGHT'])
                dd2[5].append('')
                dd2[5].append(bazaprofiley.data['Тип Комбинация'])
                dd2[5].append('XXXX')
            else:
                
                for j in range(0,33):
                    dd2[0].append('001')
                    
                for j in range(0,33):
                    if HEADER[j] not in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT','TNVED']:
                        dd2[1].append('ALUMINIUM_PROFILE')
                    else:
                        if HEADER[j] in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT']:
                            dd2[1].append('RAWMAT_TYPE')
                        elif HEADER[j] =='TNVED':
                            dd2[1].append('TNVED')

                if '-7' in row['SAP код S4P 100']:
                    dd2[0].append('001')
                    dd2[0].append('023')
                    dd2[1].append('QBIC')
                    dd2[1].append('ZPP_023_FERT')
                else:
                    dd2[0].append('023')
                    dd2[1].append('ZPP_023_HALB')

                for j in range(0,33):
                    dd2[2].append('MARA')
                    
                for j in range(0,33):
                    dd2[3].append(row['SAP код S4P 100'])
                    
                for j in HEADER:
                    dd2[4].append(j)

                if '-7' in row['SAP код S4P 100']:
                    dd2[2].append('MARA')
                    dd2[2].append('MARA')
                    dd2[3].append(row['SAP код S4P 100'])
                    dd2[3].append(row['SAP код S4P 100'])
                    dd2[4].append('COATING_QBIC')
                    dd2[4].append('ZBATCH_NUM')
                else:
                    dd2[2].append('MARA')
                    dd2[3].append(row['SAP код S4P 100'])
                    dd2[4].append('ZBATCH_NUM')

                dd2[5].append('')
                dd2[5].append('')
                dd2[5].append(row['ch_system'])
                dd2[5].append(row['SAP код S4P 100'].split('-')[0])
                dd2[5].append(row['Длина'])
                dd2[5].append(row['Тип покрытия'])
                dd2[5].append(row['ch_alloy'])
                dd2[5].append(row['ch_temper'])
                dd2[5].append(row['ch_combination'])
                dd2[5].append(row['ch_outer_side_pc_id'])
                dd2[5].append(row['ch_outer_side_pc_brand'])
                dd2[5].append(row['ch_inner_side_pc_id'])
                dd2[5].append(row['ch_inner_side_pc_brand'])
                dd2[5].append(row['ch_outer_side_wg_s_id'])
                dd2[5].append(row['ch_inner_side_wg_s_id'])
                dd2[5].append(row['ch_outer_side_wg_id'])
                dd2[5].append(row['ch_inner_side_wg_id'])
                
                if row['ch_anodization_contact'].lower() =='yc':
                    dd2[5].append('С КОНТАКТОМ')
                elif row['ch_anodization_contact'].lower()=='nc' :
                    dd2[5].append('БЕЗ КОНТАКТА')
                else:
                    # print('FFFF>>>>',row['ch_anodization_contact'])
                    dd2[5].append(row['ch_anodization_contact'])
                
                dd2[5].append(row['ch_anodization_type'])
                dd2[5].append(row['ch_anodization_method'])
                dd2[5].append(row['ch_print_view'])
                dd2[5].append(row['ch_profile_base'])
                dd2[5].append(row['ch_width'])
                dd2[5].append(row['ch_height'])
                dd2[5].append(row['ch_category'])
                dd2[5].append(row['ch_rawmat_type'])
                dd2[5].append('')
                dd2[5].append(row['ch_tnved'])
                dd2[5].append(str(row['ch_surface_treatment_export']).replace('.0',''))
                dd2[5].append(row['WMS_WIDTH'])
                dd2[5].append(row['WMS_HEIGHT'])
                dd2[5].append('')
                dd2[5].append(bazaprofiley.data['Тип Комбинация'])
                if '-7' in row['SAP код S4P 100']:
                    if row['Тип покрытия'] =='Неокрашенный':
                        qbic ='XXXX'
                    elif row['Тип покрытия'] =='Окрашенный':
                        qbic = row['ch_outer_side_pc_id']
                    elif row['Тип покрытия'] =='Анодированный':
                        qbic = row['ch_outer_side_pc_id']
                    elif row['Тип покрытия'] =='Ламинированный':
                        if row['ch_outer_side_wg_id'] =='XXXX':
                            qbic = row['ch_inner_side_wg_id']
                        else:
                            qbic = row['ch_outer_side_wg_id']
                    elif row['Тип покрытия'] =='Сублимированный':
                        qbic = row['ch_outer_side_wg_s_id']
                    else:
                        qbic ='XXXX'
                    dd2[5].append(qbic)
                    dd2[5].append('XXXX')
                else:
                    dd2[5].append('XXXX')

        new_date={}       
        new_date['Вид класса'] = dd2[0]
        new_date['Класс'] = dd2[1]
        new_date['Таблица'] = dd2[2]
        new_date['Объект'] = dd2[3]
        new_date['Имя признака'] = dd2[4]
        new_date['Значение признака'] = dd2[5]
        new_date['Статус загрузки'] = ''
        
        
        df_baza_profiley_link =pd.DataFrame({'SAP CODE':baza_profile_links[0],'link':baza_profile_links[1]})
        df_baza_profiley_link.to_excel(pathtext9,index=False)
        
        ddf2 = pd.DataFrame(new_date)
        ddf2 = ddf2[((ddf2["Значение признака"] != "nan") & (ddf2["Значение признака"] != ""))]
        ddf2 =ddf2.replace('XXXX','')
        ddf2.to_excel(pathtext6,index=False)

        grouped_by_name = ddf2.groupby('Имя признака')

        # Save each group to a separate Excel file named after the unique value in the "Имя признака" column
        for group_name, group_df in grouped_by_name:
            # Remove duplicates
            group_df = group_df.drop_duplicates()
            
            # Prepare the output file path using the group_name
            output_file = f'{char_path}\\{group_name}.xlsx'
            # Save the group to Excel
            group_df.to_excel(output_file, index=False)



        
    

    file_path =f'{pathzip}.zip'
    
    zip(pathzip, pathzip)

    return [file_path,],path_texcarta





def create_folder(parent_dir,directory):
    path =os.path.join(parent_dir,directory)
    if not os.path.isdir(path):
        os.mkdir(path)
        

def anodirovaka_check(items,data):
    for item in items:
        if item in data:
            return True
    return False 




def check_for_correct(items,filename='termo'):
    aluprofile = []
    
    for key,row in items.iterrows():
        if row['Артикул'] !='nan':
       
            artikle =row['Артикул']
            if not AluProfilesData.objects.filter(data__Артикул__icontains =artikle).exists():
                if [artikle,'new'] not in aluprofile:
                    aluprofile.append([artikle,'new'])
            else:
                bazaprof = AluProfilesData.objects.filter(data__Артикул__icontains =artikle)[:1].get()
                for key, val in bazaprof.data.items():
                    if key =='Артикул' or key =='Компонент' or key =='Код наклейки' :
                        continue
                    else:
                        if val=='' and [artikle,'old'] not in aluprofile:
                            aluprofile.append([artikle,'old'])
            
                    
        if  filename =='termo':   
            if row['Компонент'] !='nan':
               
                artikle =row['Компонент']
                if not AluProfilesData.objects.filter(data__Компонент__icontains =artikle).exists():
                    if [artikle,'new'] not in aluprofile:
                        aluprofile.append([artikle,'new'])
                else:
                    bazaprof = AluProfilesData.objects.filter(Q(data__Артикул__icontains =artikle)|Q(data__Компонент=artikle))[:1].get()
                    for key, val in bazaprof.data.items():
                        if key =='Артикул' or key =='Компонент' or key =='Код наклейки' :
                            continue
                        else:
                            if val=='' and [artikle,'old'] not in aluprofile:
                                aluprofile.append([artikle,'old'])
                    
    correct = True
    if len(aluprofile) >0:
        correct = False
    return aluprofile , correct


def  create_all(request,df_char_title):
    context ={
        'df_char_title':df_char_title
    }
    return render(request,'termo/complete_ves.html',context)

def zip(src, dst):
    zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            zf.write(absname, arcname)
    zf.close()

