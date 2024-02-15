import pandas as pd
import math


path =f'D:\\1301 DOALU KLAES.xlsx'
            
df = pd.read_excel(path,header=0)

df = df.astype(str)
df = df.replace('nan','0')
df = df.replace('0.0','0') 


def get_legth(lengg):
    lls =lengg.split()
    print(lengg)
    for ll in lls:
        if ll.startswith('WL'):
            hh =ll.replace('WL','')
            break
        if ll.startswith('L'):
            hh =ll.replace('L','')
            break
    return (int(hh)) 

df_new ={
        'ID':[],
        'MATNR': [],
        'WERKS':[],
        'TEXT1':[],
        'STLAL':[],
        'STLAN':[],
        'ZTEXT':[],
        'STKTX':[],
        'BMENG':[],
        'BMEIN':[],
        'STLST':[],
        'POSNR':[],
        'POSTP':[],
        'MATNR1':[],
        'TEXT2':[],
        'MEINS':[],
        'MENGE':[],
        'DATUV':[],
        'PUSTOY':[],
        'LGORT':[]
    }

for key , row in df.iterrows():
    print(key)
    a =get_legth(row['Кр.ткст материала'])
    b =get_legth(row['Кр.ткст материала2'])
    gcdd = math.gcd(a,b)
    ax= b/gcdd
    bx =a/gcdd
    df_new['ID'].append('1')
    df_new['MATNR'].append(row['Материал'])
    df_new['WERKS'].append('1301')
    df_new['TEXT1'].append(row['Кр.ткст материала'])
    df_new['STLAL'].append('1')
    df_new['STLAN'].append('6')
    df_new['ZTEXT'].append(row['Кр.ткст материала'])
    df_new['STKTX'].append('')
    df_new['BMENG'].append(ax)
    df_new['BMEIN'].append('ШТ')
    df_new['STLST'].append('1')
    df_new['POSNR'].append('')
    df_new['POSTP'].append('')
    df_new['MATNR1'].append('')
    df_new['TEXT2'].append('')
    df_new['MEINS'].append('')
    df_new['MENGE'].append('')
    df_new['DATUV'].append('01012021')
    df_new['PUSTOY'].append('')
    df_new['LGORT'].append('')
    #####
    df_new['ID'].append('2')
    df_new['MATNR'].append('')
    df_new['WERKS'].append('')
    df_new['TEXT1'].append('')
    df_new['STLAL'].append('')
    df_new['STLAN'].append('')
    df_new['ZTEXT'].append('')
    df_new['STKTX'].append('')
    df_new['BMENG'].append('')
    df_new['BMEIN'].append('')
    df_new['STLST'].append('')
    df_new['POSNR'].append('1')
    df_new['POSTP'].append('L')   
    df_new['MATNR1'].append(row['Материал2'])
    df_new['TEXT2'].append(row['Кр.ткст материала2'])
    df_new['MEINS'].append(bx) 
    df_new['MENGE'].append('ШТ')
    df_new['DATUV'].append('')
    df_new['PUSTOY'].append('')
    df_new['LGORT'].append('')

df =pd.DataFrame(df_new)

df.to_excel('texcarta.xlsx',index=False,sheet_name ='Texcarta')