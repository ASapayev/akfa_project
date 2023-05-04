import pandas as pd
from datetime import datetime
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

def create_csv_file(norma,alumniy_silindr,subdekor,kraska,nakleyka,kombinirovanniy,lamplyonka,file_name='termo'):
    df_norma = pd.DataFrame({'SAP CODE':norma})
    df_kraska = pd.DataFrame({'SAP CODE':kraska})
    df_kombinirovanniy = pd.DataFrame({'Artikul':kombinirovanniy})
    
    norma_sap_kode = []
    lamination_code = []
    for lam in lamplyonka:
        norma_sap_kode.append(lam[0])
        lamination_code.append(lam[1])
    
    df_lamplyonka =pd.DataFrame({'NORMA SAP CODE':norma_sap_kode,'Lamination code':lamination_code})
    
    sap_code_s4q100 = []
    тип = []
    for silindr in alumniy_silindr:
        sap_code_s4q100.append(silindr[0])
        тип.append(silindr[1])
        
    pustoy_1 = ['' for i in sap_code_s4q100 ]
    df_aluminiy_silindr = pd.DataFrame({'sap_code_s4q100':sap_code_s4q100,'название':pustoy_1,'еи':pustoy_1,'склад_закупа':pustoy_1,'тип':тип})


    код_декор_пленки = []
    ширина_декор_пленки_мм = []
    sap_code = []
    
    for sub in subdekor:
        код_декор_пленки.append(sub[0])
        ширина_декор_пленки_мм.append(sub[1])
        sap_code.append(sub[2])
    
    pustoy_2 = ['' for i in код_декор_пленки]
    df_subdekor = pd.DataFrame({'sap_code_s4q100':sap_code,'название':pustoy_2,'еи':pustoy_2,'склад_закупа':pustoy_2,'код_декор_пленки':код_декор_пленки,'ширина_декор_пленки_мм':ширина_декор_пленки_мм})

    sap_code_N = []
    nakleyka_code=[]
    shirina_niz =[]
    shirina_verx =[]
    niz = []
    verx =[]
    for nak in nakleyka:
        sap_code_N.append(nak['sap_code'])
        nakleyka_code.append(nak['nakleyka_code'])
        shirina_niz.append(nak['shirina_niz'])
        shirina_verx.append(nak['shirina_verx'])
        niz.append(nak['niz'])
        verx.append(nak['verx'])
    
    df_nakleyka =pd.DataFrame({'SAP CODE':sap_code_N,'NAKLEYKA CODE':nakleyka_code,'SHIRINA NIZKIY':shirina_niz,'SHIRINA VERX':shirina_verx,'NIZIY':niz,'VERX':verx})
        
    now = datetime.now()
    year =now.strftime("%Y")
    minut =now.strftime("%M-%S")
    
    create_folder(f'{MEDIA_ROOT}\\uploads\\','norma')
    create_folder(f'{MEDIA_ROOT}\\uploads\\norma\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\norma\\{year}\\','Not Exists')
    
            
    path =f'{MEDIA_ROOT}\\uploads\\norma\\{year}\\Not Exists\\Not_Exists-{file_name}-{minut}.xlsx'
    
    
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