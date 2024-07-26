import pandas as pd
from radiator.models import Characteristika

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

