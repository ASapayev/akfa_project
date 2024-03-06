from config.settings import MEDIA_ROOT
from datetime import datetime
import pandas as pd
from .models import Norma,TexcartaBase
from aluminiy.models import ExchangeValues


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
        df_new['WERKS'].append('4501')
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
        if '-7' in norm.data['sap_code']:
            lgort =''
        else:
            if '-LA' in norm.data['sap_code']:
                lgort ='PL01'
            elif '-LC' in norm.data['sap_code']:
                lgort ='PL01'
            elif '-PA' in norm.data['sap_code']:
                lgort ='PL02'
            elif '-PC' in norm.data['sap_code']:
                lgort ='PL03'
            elif '-MO' in norm.data['sap_code']:
                lgort ='PL04'
            elif '-GZ' in norm.data['sap_code']:
                lgort ='PL06'
            elif '-VS' in norm.data['sap_code']:
                lgort ='PL05'
            elif '-RU' in norm.data['sap_code']:
                lgort ='PS01'
            elif '-SN' in norm.data['sap_code']:
                lgort ='PS03'
            elif '-SK' in norm.data['sap_code']:
                lgort ='PS03'
            elif '-KL' in norm.data['sap_code']:
                lgort ='PS02'
            elif '-ZG' in norm.data['sap_code']:
                lgort ='PS05'
            elif '-TP' in norm.data['sap_code']:
                lgort ='PS04'
            else:
                lgort =''

            

        for comp in norm.data['components']:
            if '-7' in norm.data['sap_code']:
                meins = str(('%0.3f' %  float(float(str(comp[6]).replace(',','.'))*1000)).replace('.',','))
            else:
                meins =str('%0.3f' % float(comp[4])).replace('.',',')

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
            df_new['MEINS'].append(meins.replace(',000','') if meins[-4:]==',000' else meins ) 
            df_new['MENGE'].append(comp[2])
            df_new['DATUV'].append('')
            df_new['PUSTOY'].append('')   
            df_new['LGORT'].append(lgort)
    
    
    now =datetime.now()
    df = pd.DataFrame(df_new)
    minut =now.strftime('%M-%S')
    path =f'{MEDIA_ROOT}\\uploads\\ozmka\\accessuar-norma-{minut}.xlsx'
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    df.to_excel(writer,index=False,sheet_name='NORMA')  
    writer.close()
    return [path,'']

def get_norma_price(ozmk) ->list:
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
        'PLANOVIY':[],
        'FACT':[],
        'SUMMA':[],
        'DATUV':[],
        'PUSTOY':[],
        'LGORT':[]
    }
    
    normalar = get_sapcodes(ozmk)
    

    for norm in normalar:
        df_new['ID'].append('1')
        df_new['MATNR'].append(norm.data['sap_code'])
        df_new['WERKS'].append('4501')
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
        df_new['SUMMA'].append(norm.data['price'])
        df_new['PLANOVIY'].append('')
        df_new['FACT'].append('')
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
            df_new['MENGE'].append(comp[8])
            df_new['PLANOVIY'].append(comp[4])
            df_new['FACT'].append(comp[6])
            df_new['SUMMA'].append(comp[7]) 
            df_new['DATUV'].append('')
            df_new['PUSTOY'].append('')   
            df_new['LGORT'].append('PS02')
    
    
    now =datetime.now()
    df = pd.DataFrame(df_new)
    minut =now.strftime('%M-%S')
    path =f'{MEDIA_ROOT}\\uploads\\ozmka\\accessuar-norma-narx-{minut}.xlsx'
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
   
import os
def create_folder(parent_dir,directory):
    path =os.path.join(parent_dir,directory)
    if not os.path.isdir(path):
        os.mkdir(path)

def lenght_generate_texcarta(ozmks) -> list:
    counter = 5*len(ozmks)
    df_new = pd.DataFrame()
    df_new['counter'] =[ '' for i in range(0,counter)]
    df_new['ID']=''
    df_new['MATNR']=''
    df_new['WERKS']=''
    df_new['PLNNR']=''
    df_new['STTAG']=''
    df_new['PLNAL']=''
    df_new['KTEXT']=''
    df_new['VERWE']=''
    df_new['STATU']=''
    df_new['LOSVN']=''
    df_new['LOSBS']=''
    df_new['VORNR']=''
    df_new['ARBPL']=''
    df_new['WERKS1']=''
    df_new['STEUS']=''
    df_new['LTXA1']=''
    df_new['BMSCH']=''
    df_new['MEINH']=''
    df_new['VGW01']=''
    df_new['VGE01']=''
    df_new['VGW03']=''
    df_new['VGE03']=''
    df_new['ACTTYPE_01']=''
    df_new['CKSELKZ']=''
    df_new['UMREZ']=""
    df_new['UMREN']=''
    df_new['USR00']=''
    df_new['USR01']=''
    
    exchange_value = float(ExchangeValues.objects.get(id=1).valute)

    counter_2 = 0
    not_exists =[]
    for ozmk in ozmks:
        if not TexcartaBase.objects.filter(material = ozmk).exists():
            if  Norma.objects.filter(data__sap_code__icontains=ozmk).exists():
                norma = Norma.objects.filter(data__sap_code__icontains=ozmk)[:1].get()
                if 'ARBPL' in norma.data:
                    len_arbpl =len(norma.data['ARBPL'])
                    price = ((float(norma.data['price'])*1000)/exchange_value)/len_arbpl
                    for i in range(1,len_arbpl+2):
                        if i ==1:
                            df_new['ID'][counter_2] ='1'
                            df_new['MATNR'][counter_2] = ozmk
                            df_new['WERKS'][counter_2] ='4501'
                            df_new['STTAG'][counter_2] ='01012023'
                            df_new['PLNAL'][counter_2] ='1'
                            df_new['KTEXT'][counter_2] = norma.data['kratkiy_tekst']
                            df_new['VERWE'][counter_2] ='1'
                            df_new['STATU'][counter_2] ='4'
                            df_new['LOSVN'][counter_2] ='1'
                            df_new['LOSBS'][counter_2] ='99999999'
                        else:
                            df_new['ID'][counter_2]='2'
                            df_new['VORNR'][counter_2] =f'00{i-1}0'
                            df_new['ARBPL'][counter_2] =norma.data['ARBPL'][i-2]
                            df_new['WERKS1'][counter_2] ='4501'
                            df_new['STEUS'][counter_2] ='ZK01'
                            df_new['LTXA1'][counter_2] =norma.data['kratkiy_tekst']
                            df_new['BMSCH'][counter_2] = '1000'
                            df_new['MEINH'][counter_2] ='ST'
                            df_new['VGW01'][counter_2] ='24'
                            df_new['VGE01'][counter_2] ='STD'
                            df_new['VGW03'][counter_2]="%.3f" % price
                            df_new['VGE03'][counter_2]='ZUS'
                            df_new['CKSELKZ'][counter_2] ='X'
                            df_new['UMREZ'][counter_2] = '1'
                            df_new['UMREN'][counter_2] = '1'
                            df_new['USR00'][counter_2] = '1'
                            df_new['USR01'][counter_2] = '1'#("%.3f" % ((L*1000*3600*float(norma.data['Площадь поверхности 1000шт профилей/м²'].replace(',','.')))/(6000000*bmsch)))
                            
                        counter_2 +=1
                    TexcartaBase(material = ozmk).save()
                else:
                    not_exists.append(ozmk)
            else:
                not_exists.append(ozmk)
                print(ozmk)
            
    for i in range(0,counter_2):
        df_new['USR01'][i] = df_new['USR01'][i].replace('.',',')

    df_new=df_new.replace('nan','')

    not_exist_df = pd.DataFrame({'SAP CODE':not_exists})

    del df_new["counter"]
        
    from datetime import datetime
    now = datetime.now()
    
    s2 = now.strftime("%d.%m.%Y_%H.%M")

    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M-%S")     
            
    create_folder(f'{MEDIA_ROOT}\\uploads','texcarta_accessuar')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta_accessuar',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta_accessuar\\{year}',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta_accessuar\\{year}\\{month}',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta_accessuar\\{year}\\{month}\\{day}',hour)
    
   

    path2 =f'{MEDIA_ROOT}\\uploads\\texcarta_accessuar\\{year}\\{month}\\{day}\\{hour}\\Texcarta_{s2}.xlsx'
    writer = pd.ExcelWriter(path2, engine='xlsxwriter')
    df_new.to_excel(writer,index=False,sheet_name ='TEXCARTA')
    not_exist_df.to_excel(writer,index=False,sheet_name ='NOT EXISTS')
    writer.close()

   
    return [path2,]



