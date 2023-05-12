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
    writer.save()
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