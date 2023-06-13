import pandas as pd
from datetime import datetime
import numpy as np
import os
from config.settings import MEDIA_ROOT
import random

def excelgenerate(data):
    new_data = pd.DataFrame()
    data_length = data.shape[0] 
    new_data['id'] = [ i for i in range(120)]
    new_data['ID'] =''
    new_data['MATNR'] =''
    new_data['WERKS'] =''
    new_data['TEXT1'] =''
    new_data['STLAL'] =''
    new_data['STLAN'] =''
    new_data['ZTEXT'] =''
    new_data['STKTX'] =''
    new_data['BMENG'] =''
    new_data['BMEIN'] =''
    new_data['STLST'] =''
    new_data['POSNR'] =''
    new_data['POSTP'] =''
    new_data['MATNR1'] =''
    new_data['TEXT2'] =''
    new_data['MEINS'] =''
    new_data['MENGE'] =''
    new_data['DATUV'] =''
    new_data['PUSTOY'] =''
    new_data['LGORT'] =''
    j =0
    for key, row in data.iterrows():
        new_data['ID'][j] ='1'
        new_data['MATNR'][j] =row['A']
        new_data['WERKS'][j] ='1101'
        new_data['TEXT1'][j] =row['A_K']
        new_data['STLAL'][j] ='1'
        new_data['STLAN'][j] ='1'
        new_data['ZTEXT'][j] ='Упаковка'
        new_data['STKTX'][j] ='Упаковка'
        new_data['BMENG'][j] ='1000'
        new_data['BMEIN'][j] ='ШТ'
        new_data['STLST'][j] ='1'
        new_data['DATUV'][j] ='01012021'
                                
        j+=1
        new_data['ID'][j] = '2'
        new_data['MATNR1'][j] =row['B']
        new_data['TEXT2'][j] =row['B_K']
        new_data['MEINS'][j] ='1000'
        new_data['MENGE'][j] ='ШТ'
        new_data['POSNR'][j] ='1'
        new_data['POSTP'][j] ='L'
        new_data['LGORT'][j] ='PS10'
        j+=1
        new_data['ID'][j] = '2'
        new_data['MATNR1'][j] =row['C']
        new_data['TEXT2'][j] =row['C_K']
        new_data['MEINS'][j] =row['C_EI']
        new_data['MENGE'][j] ='М2'
        new_data['POSNR'][j] ='2'
        new_data['POSTP'][j] ='L'
        new_data['LGORT'][j] ='PS10'
        j+=1
    return new_data

counter =0

def create_csv_file(norma,alumniy_silindr,subdekor,kraska,nakleyka,kombinirovanniy,lamplyonka,file_name='termo'):
    
    
    if len(norma)>0:
        colors =[ color[12] for color in norma]
        norma =[ col[:12] for col in norma]
        
        df_norma = pd.DataFrame(np.array(norma),columns=['Component','Artikul','Nakleyka code','Sublimation code','Sublimation meins','Skotch','shirina subdecor','Laminatsiya rasxod 1000 m2','Laminatsiya rasxod 1000 shtuk','уп_пол_лн_рас_уп_лн_на_1000_штук_кг или рас_скотча_рас_скотча_на_1000_штук_шт','ala7_oddiy_ala8_qora_алю_сплав_6064','Error type'])
        # df_norma.style.apply(highlight_late,colors=colors)
        # global counter
        # counter = 0
    else:
        df_norma = pd.DataFrame(np.array([['','','','','','','','','','','','']]),columns=['Component','Artikul','Nakleyka code','Sublimation code','Sublimation meins','Skotch','shirina subdecor','Laminatsiya rasxod 1000 m2','Laminatsiya rasxod 1000 shtuk','уп_пол_лн_рас_уп_лн_на_1000_штук_кг или рас_скотча_рас_скотча_на_1000_штук_шт','ala7_oddiy_ala8_qora_алю_сплав_6064','Error type'])
    
    df_kraska = pd.DataFrame({'SAP CODE':kraska})
    df_kombinirovanniy = pd.DataFrame({'Artikul':kombinirovanniy})
    
    if len(lamplyonka)>0:
        df_lamplyonka =pd.DataFrame(np.array(lamplyonka),columns=['NORMA SAP CODE','Lamination code'])
    else:
        df_lamplyonka =pd.DataFrame(np.array([['','']]),columns=['NORMA SAP CODE','Lamination code'])
    
    if len(alumniy_silindr)>0:
        df_aluminiy_silindr = pd.DataFrame(np.array(alumniy_silindr),columns=['sap_code_s4q100','тип'])
    else:
        df_aluminiy_silindr = pd.DataFrame(np.array([['','']]),columns=['sap_code_s4q100','тип'])

    if len(subdekor) >0:
        df_subdekor = pd.DataFrame(np.array(subdekor),columns=['sap_code_s4q100','ширина_декор_пленки_мм','код_декор_пленки'])
    else:
        df_subdekor = pd.DataFrame(np.array([['','','']]),columns=['sap_code_s4q100','ширина_декор_пленки_мм','код_декор_пленки'])
    
    if len(nakleyka)>0:
        df_nakleyka =pd.DataFrame(np.array(nakleyka),columns=['SAP CODE','NAKLEYKA CODE','SHIRINA NIZKIY','SHIRINA VERX','NIZKIY','VERX'])
    else:
        df_nakleyka =pd.DataFrame(np.array([['','','','','','']]),columns=['SAP CODE','NAKLEYKA CODE','SHIRINA NIZKIY','SHIRINA VERX','NIZKIY','VERX'])
    
    

    
    now = datetime.now()
    year =now.strftime("%Y")
    hour =now.strftime("%d-%B-%Y %H-%M")
    
    
    create_folder(f'{MEDIA_ROOT}\\uploads\\','norma')
    create_folder(f'{MEDIA_ROOT}\\uploads\\norma\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\norma\\{year}\\','Not Exists')
    
            
    path =f'{MEDIA_ROOT}\\uploads\\norma\\{year}\\Not Exists\\Not_exists-{hour}.xlsx'
    
    

    
    
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    df_norma.to_excel(writer,index=False,sheet_name ='norma')
    df_aluminiy_silindr.to_excel(writer,index=False,sheet_name ='aluminiy silindr 1')
    df_subdekor.to_excel(writer,index=False,sheet_name ='Subdekor')
    df_kraska.to_excel(writer,index=False,sheet_name ='Kraska')
    df_nakleyka.to_excel(writer,index=False,sheet_name ='Nakleyka')
    df_kombinirovanniy.to_excel(writer,index=False,sheet_name ='Kombinirovanniy utils')
    df_lamplyonka.to_excel(writer,index=False,sheet_name ='Lamination code')
    writer.close()
    return 1
def characteristika_created_txt_create_1101(datas,file_name='aluminiytermo'):
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M-%S MINUT")
    
    if file_name =="aluminiytermo":
        # parent_dir =
        if not os.path.isdir(f'{MEDIA_ROOT}\\uploads\\aluminiytermo'):
            create_folder(f'{MEDIA_ROOT}\\uploads',"aluminiytermo")
            
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo',f"{year}")
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}',f'{month}')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}',day)
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}',hour)
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}',minut)
        pathtext1 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\{minut}\\1.txt'
        pathtext2 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\{minut}\\2.txt'
        pathtext3 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\{minut}\\3.txt'
        pathtext4 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\{minut}\\4.txt'
        pathtext5 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\{minut}\\Единицы изм.txt'
        pathtext6 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\{minut}\\Лист в C 3.xlsx'
        pathtext7 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\{minut}\\Длинный текст.txt'
        pathtext8 =f'{MEDIA_ROOT}\\uploads\\aluminiytermo\\{year}\\{month}\\{day}\\{hour}\\{minut}\\Бухгалтерская названия.txt'
        
    elif file_name =='aluminiy':
        parent_dir ='{MEDIA_ROOT}\\uploads\\aluminiy\\'
        
        if not os.path.isdir(parent_dir):
            create_folder(f'{MEDIA_ROOT}\\uploads','aluminiy')
            
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy',f'{year}')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}',f'{month}')
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}',day)
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}',hour)
        create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}',minut)
        pathtext1 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\{minut}\\1.txt'
        pathtext2 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\{minut}\\2.txt'
        pathtext3 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\{minut}\\3.txt'
        pathtext4 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\{minut}\\4.txt'
        pathtext5 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\{minut}\\Единицы изм.txt'
        pathtext6 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\{minut}\\Лист в C 3.xlsx'
        pathtext7 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\{minut}\\Длинный текст.txt'
        pathtext8 =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\{minut}\\Бухгалтерская названия.txt'
    
    
    umumiy_without_duplicate1201 =[[] for i in range(0,49)]
    umumiy_without_duplicate1203 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D1 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D2 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D3 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D4 =[[] for i in range(0,49)]
    umumiy_without_duplicate12D5 =[[] for i in range(0,49)]
    
    dlinniy_text_zero =[[],[],[]]
    buxgalterskiy_naz =[[],[],[],[],[],[],[],[]]
    
    # print(datas.columns)
    for key , row in datas.iterrows():
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
    ########################## Длинный текст.txt ##############################
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
    
    
    ########################## end Длинный текст.txt ##############################


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
    d2['STPRS']=umumiy_without_duplicate[39]
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
        obshiy_ves_za_shtuku.append(row['Общий вес за штуку'])
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
            ed_iz3 += [j for j in obshiy_ves_za_shtuku ]
            
    
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
    
    for key , row in datas.iterrows():
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
        
        
        for j in range(0,32):
            dd2[0].append('001')
            
        for j in range(0,32):
            if HEADER[j] not in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT','TNVED']:
                dd2[1].append('ALUMINIUM_PROFILE')
            else:
                if HEADER[j] in ['RAWMAT_TYPE','WMS_WIDTH','WMS_HEIGHT']:
                    dd2[1].append('RAWMAT_TYPE')
                elif HEADER[j] =='TNVED':
                    dd2[1].append('TNVED')
            
        for j in range(0,32):
            dd2[2].append('MARA')
            
        for j in range(0,32):
            dd2[3].append(row['SAP код S4P 100'])
            
        for j in HEADER:
            dd2[4].append(j)

        dd2[5].append('')
        dd2[5].append('')
        dd2[5].append(row['ch_export_customer_id'])
        dd2[5].append(row['ch_system'])
        dd2[5].append(row['ch_article'])
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
    
    new_date={}       
    new_date['Вид класса'] = dd2[0]
    new_date['Класс'] = dd2[1]
    new_date['Таблица'] = dd2[2]
    new_date['Объект'] = dd2[3]
    new_date['Имя признака'] = dd2[4]
    new_date['Значение признака'] = dd2[5]
    new_date['Статус загрузки'] = ''
    
    
    ddf2 = pd.DataFrame(new_date)
    ddf2 = ddf2[((ddf2["Значение признака"] != "nan") & (ddf2["Значение признака"] != ""))]
    ddf2.to_excel(pathtext6,index=False)
    
    return 1

def create_folder(parent_dir,directory):
    path =os.path.join(parent_dir,directory)
    if not os.path.isdir(path):
        os.mkdir(path)
        
def highlight_late(col,colors):
    global counter 
    color = [f'background-color: {c}' for c in colors[counter] ]
    counter += 1
    return color +['background-color: white','background-color: white','background-color: white']