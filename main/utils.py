from .models import Product,ExcelFiles
from django.db.models import Count
from datetime import datetime
from config.settings import MEDIA_ROOT
import pandas as pd
import numpy as np
import os


group_one =['WDC47','WDT65','WDT78']


def counter_generated_data(datas,data_type):
  pr = [x['new_sap_kod_del_otxod'] for x in Product.objects.all().values('new_sap_kod_del_otxod').annotate(dcount=Count('new_sap_kod_del_otxod')).order_by('dcount')]
  products = Product.objects.all().values('id','sap_kod_del_otxod','kratkiy_tekst_del_otxod')

  counter = {}
  for p in pr:
    counter[p]=[]

  for product in products:
    sap_code = product['sap_kod_del_otxod'].split('-W')
    counter_exist = int(sap_code[1])
   
    new_counter_list = counter[sap_code[0]]
    new_counter_list.append(counter_exist)
    new_counter_list.sort()
    counter[sap_code[0]] = new_counter_list

  umumiy =[[] for i in range(0,17)]
  umumiy_without_duplicate =[[] for i in range(0,17)]
  sap_code =[]
  kratkiy_text =[]
  sap_code_krat =[]
  kratkiy_text_odxod =[]
  duplicate =[]

  new_data = []
  excel_txt5 =[]
  new_excel_txt5 =[]
  for dat in datas:
    sap_code_materials =dat['sap_code']
    ktartkiy_tekst_materiala =dat['text']
    ch_profile_type =dat['ch_profile_type']
    kls_inner_id=dat['kls_inner_id']
    kls_inner_color=dat['kls_inner_color']
    kls_color =dat['kls_color']
    ves_gp =dat['ves_gp']
    lenn =float(dat['length'])
    sena =float(dat['sena'])
    if ch_profile_type =='ALU':
      if sap_code_materials[:5] in group_one:
        kls_wast_length = 500
      else:
        kls_wast_length=2000
      num_kls_wat =1900005948
    elif ch_profile_type =='PVC':
      num_kls_wat =1900003344
      kls_wast_length=1500
    
    id_klaes =dat['id_claes']

    if dat['sap_code_krat'] in counter:
      number_list = counter[dat['sap_code_krat']]
      for da in dat['data']:
        product_exists = Product.objects.filter(ktartkiy_tekst_materiala=dat['text'],new_sap_kod_del_otxod=dat['sap_code_krat'],kratkiy_tekst_del_otxod=da['sap_del_cod']).exists()
        if product_exists:
          product=Product.objects.filter(ktartkiy_tekst_materiala=dat['text'],new_sap_kod_del_otxod=dat['sap_code_krat'],kratkiy_tekst_del_otxod=da['sap_del_cod'])[:1].get()
          umumiy = umumiy_dict(product,umumiy,duplicate='Yes')
        else:
          excel_txt5.append(da['lenn'])
          for i in range(1,10000):
            if not i in number_list:
              ################product save..
              product =Product(
                sap_code_materials =sap_code_materials ,
                ktartkiy_tekst_materiala =ktartkiy_tekst_materiala,
                sap_kod_del_otxod = dat['sap_code_krat']+"-W{:04d}".format(i),
                new_sap_kod_del_otxod = dat['sap_code_krat'],
                kratkiy_tekst_del_otxod =da['sap_del_cod'],
                id_klaes =id_klaes,
                ch_profile_type =ch_profile_type,
                kls_wast =num_kls_wat,
                kls_wast_length =kls_wast_length,
                ch_kls_optom = "X",
                kls_inner_id =kls_inner_id,
                kls_inner_color =kls_inner_color,
                kls_color =kls_color,
                ves_gp =ves_gp,
                ves_del_odxod="{:.3f}".format((float(ves_gp)/lenn)*float(da['lenn'])),
                sena_za_shtuk ="{:.2f}".format((sena/lenn)*da['lenn']),
                sena_za_metr ="{:.2f}".format(sena/lenn)
                )
              product.save()
              umumiy = umumiy_dict(product,umumiy)
              umumiy_without_duplicate = umumiy_dict(product,umumiy_without_duplicate)
              n_list = counter[dat['sap_code_krat']]
              n_list.append(i)
              counter[dat['sap_code_krat']]=n_list
              break
    else:
      t = 1
      counter_list=[]
      for da in dat['data']:
        excel_txt5.append(da['lenn'])
        product =Product(
                sap_code_materials =sap_code_materials ,
                ktartkiy_tekst_materiala =ktartkiy_tekst_materiala,
                sap_kod_del_otxod = dat['sap_code_krat']+"-W{:04d}".format(t),
                new_sap_kod_del_otxod = dat['sap_code_krat'],
                kratkiy_tekst_del_otxod =da['sap_del_cod'],
                id_klaes =id_klaes,
                ch_profile_type =ch_profile_type,
                kls_wast =num_kls_wat,
                kls_wast_length =kls_wast_length,
                ch_kls_optom = "X",
                kls_inner_id =kls_inner_id,
                kls_inner_color =kls_inner_color,
                kls_color =kls_color,
                ves_gp =ves_gp,
                ves_del_odxod="{:.3f}".format((float(ves_gp)/lenn)*float(da['lenn'])),
                sena_za_shtuk ="{:.2f}".format((sena/lenn)*da['lenn']),
                sena_za_metr ="{:.2f}".format(sena/lenn)
                )
        product.save()
        counter_list.append(t)
        t+=1
        umumiy = umumiy_dict(product,umumiy)
        umumiy_without_duplicate = umumiy_dict(product,umumiy_without_duplicate)
      counter[dat['sap_code_krat']]=counter_list
        
  now = datetime.now()
  year =now.strftime("%Y")
  month =now.strftime("%B")
  day =now.strftime("%a%d")
  hour =now.strftime("%H HOUR")
  minut =now.strftime("%M-%S")
  

  now = datetime.now()
  yearr =now.strftime("%d.%m.%Y")
  if data_type =='pvc':
    data_name ='PVC'
  else:
    data_name ='ALU'
  
  parent_dir ='{MEDIA_ROOT}\\uploads\\delovoyotxod\\'
    
  if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads\\','delovoyotxod')
        
  create_folder(f'{MEDIA_ROOT}\\uploads\\delovoyotxod\\',f'{year}')
  create_folder(f'{MEDIA_ROOT}\\uploads\\delovoyotxod\\{year}\\',f'{month}')
  create_folder(f'{MEDIA_ROOT}\\uploads\\delovoyotxod\\{year}\\{month}\\',day)
  create_folder(f'{MEDIA_ROOT}\\uploads\\delovoyotxod\\{year}\\{month}\\{day}\\',hour)
  create_folder(f'{MEDIA_ROOT}\\uploads\\delovoyotxod\\{year}\\{month}\\{day}\\{hour}\\',minut)
            
  data_type =data_type.upper()   
  path =f'{MEDIA_ROOT}\\uploads\\delovoyotxod\\{year}\\{month}\\{day}\\{hour}\\{minut}\\{year}_{data_name}.xlsx'
  path2 =f'{MEDIA_ROOT}\\uploads\\delovoyotxod\\{year}\\{month}\\{day}\\{hour}\\{minut}\\Лист в C 3.xlsx'
  d={}
  d['SAP код материала']=umumiy[0]
  d['Краткий текст материала']=umumiy[1]
  d['SAP код ДЕЛ.Отход']=umumiy[2]
  d['Краткий текст ДЕЛ.Отход']=umumiy[3]
  d['KLAES']=umumiy[4]
  d['CH_PROFILE_TYPE']=umumiy[5]
  d['KLS_WAST']=umumiy[6]
  d['KLS_WAST_LENGTH']=umumiy[7]
  d['CH_KLAES_OPTM']=umumiy[8]
  d['KLS_INNER_ID']=umumiy[9]
  d['KLS_INNER_COL']=umumiy[10]
  d['KLS_COLOR']=umumiy[11]
  d['Вес ГП']=umumiy[12]
  d['Цена за ШТ']=umumiy[13]
  d['Цена за метр']=umumiy[14]
  d['Вес дел отход']=umumiy[15]
  d['Дупликат']=umumiy[16]

  df = pd.DataFrame(d)
  df.to_excel(path)

  dd2={}
  if len(excel_txt5) > 0:
    new_d=[[] for i in range(0,6)]
    for i in range(0,len(umumiy_without_duplicate[2])):
      new_d[0]+=['001' for j in range(0,9)]
      new_d[1]+=['KLAES_REST' for j in range(0,6)]
      new_d[1]+=['KLAES_PP' for j in range(0,3)]
      new_d[2]+=['MARA' for j in range(0,9)]
      new_d[3]+=[ umumiy_without_duplicate[2][i] for j in range(0,9)]
      new_d[4]+=['KLAES','KLS_LENGTH','CH_PROFILE_TYPE','KLS_INNER_ID','KLS_INNER_COL','KLS_COLOR','KLS_WAST','KLS_WAST_LENGTH','CH_KLAES_OPTM']
      new_d[5]+=[umumiy_without_duplicate[4][i],excel_txt5[i],umumiy_without_duplicate[5][i],umumiy_without_duplicate[9][i],umumiy_without_duplicate[10][i],umumiy_without_duplicate[11][i],umumiy_without_duplicate[6][i],umumiy_without_duplicate[7][i],umumiy_without_duplicate[8][i]]
  
    dd2['Вид класса'] = new_d[0]
    dd2['Класс'] = new_d[1]
    dd2['Таблица'] = new_d[2]
    dd2['Объект'] = new_d[3]
    dd2['Имя признака'] = new_d[4]
    dd2['Значение признака'] = new_d[5]
    dd2['Статус загрузки'] = ''
  else:
    dd2['Вид класса'] = []
    dd2['Класс'] = []
    dd2['Таблица'] = []
    dd2['Объект'] = []
    dd2['Имя признака'] = []
    dd2['Значение признака'] = []
    dd2['Статус загрузки'] = []
  # print(dd2)
  ddf2 = pd.DataFrame(dd2)
  ddf2 = ddf2[((ddf2["Значение признака"] != "nan") & (ddf2["Значение признака"] != ""))]
  ddf2.to_excel(path2,index=False)

  d1={}
  header1 ='MATNR\tBISMT\tMAKTX\tMEINS\tMTART\tMATKL\tWERKS\tBESKZ\tSPART\tBRGEW\tNTGEW\tGEWEI\tMTPOS_MARA'
  d1['MATNR']=umumiy_without_duplicate[2]
  d1['BISMT']=umumiy_without_duplicate[2]
  d1['MAKTX']=umumiy_without_duplicate[3]
  d1['MEINS']=['ШТ' for i in range(0,len(umumiy_without_duplicate[0]))]
  d1['MTART']=['ZPRF' for i in range(0,len(umumiy_without_duplicate[0]))]
  d1['MATKL']=['DOALU' if x == 'ALU' else 'DOPVC' for x in umumiy_without_duplicate[5]]
  d1['WERKS']=[ 1301 for i in range(0,len(umumiy_without_duplicate[0]))]
  d1['BESKZ']=[ 'E' for i in range(0,len(umumiy_without_duplicate[0]))]
  d1['SPART']=[ '01' if x == 'ALU' else '02' for x in umumiy_without_duplicate[5]]
  d1['BRGEW']=umumiy_without_duplicate[15]
  d1['NTGEW']=umumiy_without_duplicate[15]
  d1['GEWEI']=[ 'КГ' for i in range(0,len(umumiy_without_duplicate[0]))]
  d1['MTPOS_MARA']=[ 'NORM' for i in range(0,len(umumiy_without_duplicate[0]))]
  df1= pd.DataFrame(d1)
  np.savetxt(f'{MEDIA_ROOT}\\uploads\\delovoyotxod\\{year}\\{month}\\{day}\\{hour}\\{minut}\\1.txt', df1.values,fmt='%s', delimiter="\t",header=header1,comments='',encoding='ansi')
  

  header2='MAKTX\tMEINS\tMTART\tMATNR\tWERKS\tEKGRP\tXCHPF\tDISGR\tDISMM\tDISPO\tDISLS\tWEBAZ\tBESKZ\tLGFSB\tPLIFZ\tPERKZ\tMTVFP\tSCM_STRA1\tVRMOD\tPPSKZ\tSCM_WHATBOM\tSCM_HEUR_ID\tSCM_RRP_TYPE\tSCM_PROFID\tSTRGR\tBWKEY\tMLAST\tBKLAS\tVPRSV\tPEINH\tSTPRS\tPRCTR\tEKALR\tHKMAT\tLOSGR\tSFCPF\tUEETK\tLGPRO\tSBDKZ'

  d2={}
  d2['MAKTX']= umumiy_without_duplicate[3]
  d2['MEINS']= ['ШТ' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['MTART']=['ZPRF' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['MATNR']=umumiy_without_duplicate[2]
  d2['WERKS']=[ 1301 for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['EKGRP']=[ 999 for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['XCHPF']=['X' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['DISGR']=[ '0000' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['DISMM']=[ 'ND' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['DISPO']=['DOA' if x == 'ALU' else 'DOP' for x in umumiy_without_duplicate[5]]
  d2['DISLS']=[ 'MB' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['WEBAZ']=[ 0 for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['BESKZ']=[ 'E' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['LGFSB']=['PS01' if x == 'ALU' else 'PS02' for x in umumiy_without_duplicate[5]]
  d2['PLIFZ']=[ '' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['PERKZ']=[ 'M' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['MTVFP']=[ '02' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['SCM_STRA1']=[ '' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['VRMOD']=[ '' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['PPSKZ']=[ '' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['SCM_WHATBOM']=[ 5 for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['SCM_HEUR_ID']=[ 'Z_SAP_PP_002' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['SCM_RRP_TYPE']=[ 4 for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['SCM_PROFID']=[ 'SAP999' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['STRGR']=[ '' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['BWKEY']=[ 1301 for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['MLAST']=[ 3 for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['BKLAS']=[ '0105' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['VPRSV']=[ 'S' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['PEINH']=[ 1 for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['STPRS']=umumiy_without_duplicate[13]
  d2['PRCTR']=[ 1301 for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['EKALR']=[ 'X' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['HKMAT']=[ 'X' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['LOSGR']=[ 1 for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['SFCPF']=[ '' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['UEETK']=[ 'X' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['LGPRO']=[ '' for i in range(0,len(umumiy_without_duplicate[0]))]
  d2['SBDKZ']=[ 2 for i in range(0,len(umumiy_without_duplicate[0]))]

  df2= pd.DataFrame(d2)
  np.savetxt(f'{MEDIA_ROOT}\\uploads\\delovoyotxod\\{year}\\{month}\\{day}\\{hour}\\{minut}\\2.txt', df2.values,fmt='%s', delimiter="\t",header=header2,comments='',encoding='ansi')
  

  header3 ='MAKTX\tMEINS\tMTART\tSPART\tMATNR\tWERKS\tVKORG\tMTPOS\tVTWEG\tPRCTR\tMTVFP\tALAND\tTATYP\tTAXKM\tVERSG\tKTGRM\tKONDM\tLADGR\tTRAGR'
  d3={}
  d3['MAKTX']= umumiy_without_duplicate[3]
  d3['MEINS']= ['ШТ' for i in range(0,len(umumiy_without_duplicate[0]))]
  d3['MTART']=['ZPRF' for i in range(0,len(umumiy_without_duplicate[0]))]
  d3['SPART']=['01' if x == 'ALU' else '02' for x in umumiy_without_duplicate[5]]
  d3['MATNR']=umumiy_without_duplicate[2]
  d3['WERKS']=[ 1301 for i in range(0,len(umumiy_without_duplicate[0]))]
  d3['VKORG']=[ 1300 for i in range(0,len(umumiy_without_duplicate[0]))]
  d3['MTPOS']=[ 'NORM' for i in range(0,len(umumiy_without_duplicate[0]))]
  d3['VTWEG']=[ 99 for i in range(0,len(umumiy_without_duplicate[0]))]
  d3['PRCTR']=[ 1301 for i in range(0,len(umumiy_without_duplicate[0]))]
  d3['MTVFP']=[ '02' for i in range(0,len(umumiy_without_duplicate[0]))]
  d3['ALAND']=[ 'UZ' for i in range(0,len(umumiy_without_duplicate[0]))]
  d3['TATYP']=[ 'MWST' for i in range(0,len(umumiy_without_duplicate[0]))]
  d3['TAXKM']=[ 1 for i in range(0,len(umumiy_without_duplicate[0]))]
  d3['VERSG']=[ 1 for i in range(0,len(umumiy_without_duplicate[0]))]
  d3['KTGRM']=[ '03' for i in range(0,len(umumiy_without_duplicate[0]))]
  d3['KONDM']=[ '01' for i in range(0,len(umumiy_without_duplicate[0]))]
  d3['LADGR']=[ '0001' for i in range(0,len(umumiy_without_duplicate[0]))]
  d3['TRAGR']=[ '0001' for i in range(0,len(umumiy_without_duplicate[0]))]
  
  df3= pd.DataFrame(d3)
  np.savetxt(f'{MEDIA_ROOT}\\uploads\\delovoyotxod\\{year}\\{month}\\{day}\\{hour}\\{minut}\\3.txt', df3.values, fmt='%s', delimiter="\t",header=header3,comments='',encoding='ansi')
  

  new_ll =[[],[],[]]
  for i in range(0,3):
    new_ll[0]+=umumiy_without_duplicate[2]
    new_ll[1]+=[ 1301 for j in range(0,len(umumiy_without_duplicate[0]))]
    if i ==0:
      new_ll[2]+=['PSDA'  for x in umumiy_without_duplicate[5]]
    elif i ==1:
      new_ll[2]+=['PS01' if x == 'ALU' else 'PS02' for x in umumiy_without_duplicate[5]]
    elif i==2:
      new_ll[2]+=['B100' for x in umumiy_without_duplicate[5]]
    
    


  header4='MATNR\tWERKS\tLGORT'
  d4={}
  d4['MATNR']=new_ll[0]
  d4['WERKS']=new_ll[1]
  d4['LGORT']=new_ll[2]

  df4= pd.DataFrame(d4)
  np.savetxt(f'{MEDIA_ROOT}\\uploads\\delovoyotxod\\{year}\\{month}\\{day}\\{hour}\\{minut}\\4.txt', df4.values, fmt='%s', delimiter="\t",header=header4,comments='',encoding='ansi')
  
  d5 ={}
  d5['del_otxod_sap_code']=umumiy_without_duplicate[2]
  d5['ed_iz1']=[ 1000 for i in range(0,len(umumiy_without_duplicate[0]))]
  d5['ed_iz2']=excel_txt5
  d5['naz_ed_iz']=[ 'M' for i in range(0,len(umumiy_without_duplicate[0]))]
  df5= pd.DataFrame(d5)
  np.savetxt(f'{MEDIA_ROOT}\\uploads\\delovoyotxod\\{year}\\{month}\\{day}\\{hour}\\{minut}\\Единицы изм.txt', df5.values, fmt='%s', delimiter="\t",encoding='ansi')
  
  
  file_exist =ExcelFiles(file =f'{MEDIA_ROOT}\\uploads\\delovoyotxod\\{year}\\{month}\\{day}\\{hour}\\{minut}\\{year}_{data_name}.xlsx',generated=True)
  file_exist.save()
  file_exist2 =ExcelFiles(file =f'{MEDIA_ROOT}\\uploads\\delovoyotxod\\{year}\\{month}\\{day}\\{hour}\\{minut}\\Лист в C 3.xlsx',generated=True)
  file_exist2.save()
  return [file_exist.id,file_exist2.id]


def umumiy_dict(product,text_materials_list,duplicate='No'):
  text_materials_list[0].append(product.sap_code_materials)
  text_materials_list[1].append(product.ktartkiy_tekst_materiala)
  text_materials_list[2].append(product.sap_kod_del_otxod)
  text_materials_list[3].append(product.kratkiy_tekst_del_otxod)
  text_materials_list[4].append(product.id_klaes)
  text_materials_list[5].append(product.ch_profile_type)
  text_materials_list[6].append(product.kls_wast)
  text_materials_list[7].append(product.kls_wast_length)
  text_materials_list[8].append(product.ch_kls_optom)
  text_materials_list[9].append(product.kls_inner_id)
  text_materials_list[10].append(product.kls_inner_color)
  text_materials_list[11].append(product.kls_color)
  text_materials_list[12].append(product.ves_gp)
  text_materials_list[13].append(product.sena_za_shtuk)
  text_materials_list[14].append(product.sena_za_metr)
  text_materials_list[15].append(product.ves_del_odxod)
  text_materials_list[16].append(duplicate)
  return text_materials_list



def create_folder(parent_dir,directory):
    path =os.path.join(parent_dir,directory)
    if not os.path.isdir(path):
        os.mkdir(path)
  