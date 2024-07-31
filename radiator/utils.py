import pandas as pd
from radiator.models import Characteristika,RazlovkaRadiator
from django.db.models import Q
from datetime import datetime
from config.settings import MEDIA_ROOT

def create_characteristika(items):
    
    all_data = [
        [],[]
    ]
    
    
    
    for item in items:
        
        all_data[0].append(item['sap_code'])
        all_data[1].append(item['kratkiy'])
        
        data ={
            'SAP CODE':item['sap_code'],
            'KRATKIY TEXT':item['kratkiy'],
        }
        character = Characteristika( data = data )
        character.save()
        



    df_new ={
        'SAP CODE':all_data[0],
        'KRATKIY TEXT':all_data[1],
        
    }
    
    df_charakter = pd.DataFrame(df_new)
    df_charakter =  df_charakter.replace('nan','')
    return df_charakter   


def create_characteristika_utils(items):
    df =[
        [],[]
    ]
    
    
    for item in items:

        df[0].append(item['sap_code'])
        df[1].append(item['kratkiy'])
        

        

    dat = {
        'SAP CODE':df[0],
        'KRATKIY TEXT':df[1],
        
        
    }
    
    df_new = pd.DataFrame(dat)
    

    return df_new


def get_ozmka(ozmk):
    sap_code_yoqlari =[]
    sap_exists =[]
    pvc_razlovka =[]

    for ozm in ozmk:
        sap_code =ozm
        sap_code_exists =False
        if RazlovkaRadiator.objects.filter(
            Q(pk_sap_code =ozm)
            |Q(sap_code7 =ozm)
            ).exists():
            razlovkaobichniy =RazlovkaRadiator.objects.filter(
                Q(pk_sap_code =ozm)
                |Q(sap_code7 =ozm)
                # )[:1].values_list()
                )[:1].values_list('pr_sap_code','pr_kratkiy','mo_sap_code','mo_kratkiy','pm_sap_code','pm_kratkiy','pk_sap_code','pk_kratkiy','sap_code7','kratkiy7',)
            sap_code_exists=True
            if list(razlovkaobichniy)[0] not in pvc_razlovka:
                pvc_razlovka+=list(razlovkaobichniy)
        
        if not sap_code_exists:
            sap_code_yoqlari.append(sap_code)

    
    obichniy_razlovka1101 =[ raz for raz in pvc_razlovka]
   

    df_obichniy_1101 = pd.DataFrame(obichniy_razlovka1101,columns=['SAP CODE P','PR - Press','SAP CODE M','MO - Mex obrabotka','SAP CODE PM','PM - Puma','SAP CODE PK','PK - Pokraska','SAP CODE 7','7 - Upakovka'])#,'CREATED DATE','UPDATED DATE'
    df_yoqlari_1101 = pd.DataFrame({'SAP CODE':sap_code_yoqlari})
    now =datetime.now()
    minut =now.strftime('%M-%S')
    path1101 =f'{MEDIA_ROOT}\\uploads\\ozmka\\ozmka_radiator-{minut}.xlsx'
    writer = pd.ExcelWriter(path1101, engine='xlsxwriter')
    df_obichniy_1101.to_excel(writer,index=False,sheet_name='RADIATOR')
    df_yoqlari_1101.to_excel(writer,index=False,sheet_name='NOT EXISTS')
    writer.close()
    return [path1101,''],[df_obichniy_1101,df_yoqlari_1101]


