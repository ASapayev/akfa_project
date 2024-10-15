from config.settings import MEDIA_ROOT
from datetime import datetime
import modin.pandas as pd
from .models import Norma,TexcartaBase
from aluminiy.models import ExchangeValues
import zipfile

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
            elif '-AN' in norm.data['sap_code']:
                lgort ='VS03'
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
    writer = pd.ExcelWriter(path, engine='openpyxl')
    df.to_excel(writer,index=False,sheet_name='NORMA',engine='openpyxl')  
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
    writer = pd.ExcelWriter(path, engine='openpyxl')
    df.to_excel(writer,index=False,sheet_name='NORMA',engine='openpyxl')  
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
                    len_arbpl = 0
                    for ar in norma.data['ARBPL']:
                        if ar !='':
                            len_arbpl += 1
                    # len_arbpl =len(norma.data['ARBPL'])
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
                            df_new['MEINH'][counter_2] ='ST' if 'ACS' in ozmk else 'KG' 
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
    writer = pd.ExcelWriter(path2, engine='openpyxl')
    df_new.to_excel(writer,index=False,sheet_name ='TEXCARTA',engine='openpyxl')
    not_exist_df.to_excel(writer,index=False,sheet_name ='NOT EXISTS',engine='openpyxl')
    writer.close()

   
    return [path2,]



def characteristika_created_txt_create(datas):
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR %M %S")
    minut =now.strftime("%M-%S MINUT")
        
   
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
    d2['FEVOR']=['AP1' if x =='1203' else '' for x in (umumiy_without_duplicate[34])] 
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
        'ed_iz2':[],
        'ed_iz3':[],
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
            ed_iz3 += [ str(float(netto[j])*1000).replace('.0','') if (float(netto[j])*10000000)%10000 == 0 else str(float(netto[j])*1000) for j in range(0,len(sap_code_title))]
            
    
    for i in ED_IZM:    
        d5['sap_code'] += sap_code_title 
        d5['ed_iz1'] += [ i for j in range(0,len(sap_code_title))]
        d5['ed_iz2'] +=['1' if i =='ШТ' else '1000' for j in range(0,len(sap_code_title)) ]
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
                    if HEADER2[j] =='ID_SAVDO':
                        dd2[1].append('SAVDO')
                    else:
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
    ddf2.to_excel(pathtext6,index=False,engine='openpyxl')

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
