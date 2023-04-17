import os
import pandas as pd
from .models import Characteristika
import random





def fabrikatsiya_sap_kod(sap_kod,length):
    new =sap_kod.split(' ')
    for i in range(0,len(new)):
        if new[i].startswith('L'):
            new[i]=f'L{length}'
    return ' '.join(new)


def create_folder(parent_dir,directory):
    path =os.path.join(parent_dir,directory)
    if not os.path.isdir(path):
        os.mkdir(path) 


def create_characteristika(items):
    
    all_data =[
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[]
    ]
    for item in items:
        character = Characteristika(
            sap_code =item['material'],
            kratkiy_text =item['kratkiy'],
            section =item['section'],
            savdo_id ='',
            savdo_name ='',
            export_customer_id = item['export_customer_id'],
            system = item['system'],
            article = item['article'],
            length = item['length'],
            surface_treatment = item['surface_treatment'],
            alloy = item['alloy'],
            temper = item['temper'],
            combination = item['combination'],
            outer_side_pc_id = item['outer_side_pc_id'],
            outer_side_pc_brand = item['outer_side_pc_brand'],
            inner_side_pc_id = item['inner_side_pc_id'],
            inner_side_pc_brand = item['inner_side_pc_brand'],
            outer_side_wg_s_id = item['outer_side_wg_s_id'],
            inner_side_wg_s_id = item['inner_side_wg_s_id'],
            outer_side_wg_id = item['outer_side_wg_id'],
            inner_side_wg_id = item['inner_side_wg_id'],
            anodization_contact = item['anodization_contact'],
            anodization_type = item['anodization_type'],
            anodization_method = item['anodization_method'],
            print_view = item['print_view'],
            profile_base = item['profile_base'],
            width = item['width'],
            height = item['height'],
            category = item.get('category',''),
            rawmat_type = item['rawmat_type'],
            benkam_id = item.get('benkam_id',''),
            hollow_and_solid = item.get('hollow_and_solid',''),
            export_description = item.get('export_description',''),
            export_description_eng = item.get('export_description_eng',''),
            tnved = item.get('tnved',''),
            surface_treatment_export = item.get('surface_treatment_export',''),
            wms_width = item['wms_width'],
            wms_height = item['wms_height'],
            group_prise = item['group_prise'],
            )
        character.save()
        
        all_data[0].append(character.sap_code)
        all_data[1].append(character.kratkiy_text)
        all_data[2].append(character.section)
        all_data[3].append(character.savdo_id)
        all_data[4].append(character.savdo_name)
        all_data[5].append(character.export_customer_id)
        all_data[6].append(character.system)
        all_data[7].append(character.article)
        all_data[8].append(character.length)
        all_data[9].append(character.surface_treatment)
        all_data[10].append(character.alloy)
        all_data[11].append(character.temper)
        all_data[12].append(character.combination)
        all_data[13].append(character.outer_side_pc_id)
        all_data[14].append(character.outer_side_pc_brand)
        all_data[15].append(character.inner_side_pc_id)
        all_data[16].append(character.inner_side_pc_brand)
        all_data[17].append(character.outer_side_wg_s_id)
        all_data[18].append(character.inner_side_wg_s_id)
        all_data[19].append(character.outer_side_wg_id)
        all_data[20].append(character.inner_side_wg_id)
        all_data[21].append(character.anodization_contact)
        all_data[22].append(character.anodization_type)
        all_data[23].append(character.anodization_method)
        all_data[24].append(character.print_view)
        all_data[25].append(character.profile_base)
        all_data[26].append(character.width)
        all_data[27].append(character.height)
        all_data[28].append(character.category)
        all_data[29].append(character.rawmat_type)
        all_data[30].append(character.benkam_id)
        all_data[31].append(character.hollow_and_solid)
        all_data[32].append(character.export_description)
        all_data[33].append(character.export_description_eng)
        all_data[34].append(character.tnved)
        all_data[35].append(character.surface_treatment_export)
        all_data[36].append(character.wms_width)
        all_data[37].append(character.wms_height)
        all_data[38].append(character.group_prise)


    df_new ={
        'SAP CODE' : all_data[0],
        'KRATKIY TEXT': all_data[1],
        'SECTION': all_data[2],
        'SAVDO_ID': all_data[3],
        'SAVDO_NAME': all_data[4],
        'EXPORT_CUSTOMER_ID': all_data[5],
        'SYSTEM': all_data[6],
        'ARTICLE': all_data[7],
        'LENGTH': all_data[8],
        'SURFACE_TREATMENT': all_data[9],
        'ALLOY': all_data[10],
        'TEMPER': all_data[11],
        'COMBINATION': all_data[12],
        'OUTER_SIDE_PC_ID': all_data[13],
        'OUTER_SIDE_PC_BRAND': all_data[14],
        'INNER_SIDE_PC_ID': all_data[15],
        'INNER_SIDE_PC_BRAND': all_data[16],
        'OUTER_SIDE_WG_S_ID': all_data[17],
        'INNER_SIDE_WG_S_ID': all_data[18],
        'OUTER_SIDE_WG_ID': all_data[19],
        'INNER_SIDE_WG_ID': all_data[20],
        'ANODIZATION_CONTACT': all_data[21],
        'ANODIZATION_TYPE': all_data[22],
        'ANODIZATION_METHOD': all_data[23],
        'PRINT_VIEW': all_data[24],
        'PROFILE_BASE': all_data[25],
        'WIDTH': all_data[26],
        'HEIGHT': all_data[27],
        'CATEGORY': all_data[28],
        'RAWMAT_TYPE': all_data[29],
        'BENKAM_ID': all_data[30],
        'HOLLOW AND SOLID': all_data[31],
        'EXPORT_DESCRIPTION': all_data[32],
        'EXPORT_DESCRIPTION ENG': all_data[33],
        'TNVED': all_data[34],
        'SURFACE_TREATMENT_EXPORT': all_data[35],
        'WMS_WIDTH': all_data[36],
        'WMS_HEIGHT': all_data[37],
        'GROUP PRISE': all_data[38],
    }
    
    df_charakter = pd.DataFrame(df_new)
    df_charakter =df_charakter.replace('nan','')
    return df_charakter   










