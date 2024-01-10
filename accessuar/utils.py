from config.settings import MEDIA_ROOT
from datetime import datetime
import pandas as pd
from .models import Norma

def get_norma_df(ozmk) ->list:
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
    
    normalar = get_sapcodes(ozmk)
    

    for norm in normalar:
        df_new['ID'].append('1')
        df_new['MATNR'].append(norm.data['sap_code'])
        df_new['WERKS'].append('1201')
        df_new['TEXT1'].append(norm.data['kratkiy_tekst'])
        df_new['STLAL'].append('1')
        df_new['STLAN'].append('1')
        df_new['ZTEXT'].append(norm.data['kratkiy_tekst'])

        df_new['STKTX'].append('')
        df_new['BMENG'].append( '1000')
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
        k = 0
        for comp in norm.data['components']:
            k+=1
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
            df_new['POSNR'].append(k)
            df_new['POSTP'].append('L')
            df_new['MATNR1'].append(comp[0])
            df_new['TEXT2'].append(comp[1])
            df_new['MEINS'].append(comp[2]) 
            df_new['MENGE'].append(comp[3])
            df_new['DATUV'].append('')
            df_new['PUSTOY'].append('')   
            df_new['LGORT'].append('PS02')
    
    
    now =datetime.now()
    df = pd.DataFrame(df_new)
    minut =now.strftime('%M-%S')
    path =f'{MEDIA_ROOT}\\uploads\\ozmka\\accessuar-norma-{minut}.xlsx'
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    df.to_excel(writer,index=False,sheet_name='NORMA')  
    writer.close()
    return [path,'']

def get_sapcodes(sap_codes) -> list:
    norma =[]
    for sap_code in sap_codes:
        if Norma.objects.filter(data__sap_code__icontains=sap_code).exists():
            norma.append(Norma.objects.filter(data__sap_code__icontains=sap_code)[:1].get())
    for norm in norma:
        for component in norm.data['component_sapcodes']:
            if Norma.objects.filter(data__sap_code__icontains=component).exists():
                if Norma.objects.filter(data__sap_code__icontains=component)[:1].get() not in norma:
                    norma.append(Norma.objects.filter(data__sap_code__icontains=component)[:1].get())
       
    return norma
   
   