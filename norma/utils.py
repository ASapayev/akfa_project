import pandas as pd

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