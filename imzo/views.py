from django.shortcuts import render,redirect
from .forms import FileFormImzo
from .models import ExcelFilesImzo,ImzoBase,TexCartaTime
from config.settings import MEDIA_ROOT
import pandas as pd
from .BAZA import BAZA
from aluminiytermo.models import Characteristika
from aluminiytermo.views import File
import os
from .utils import create_folder
from django.http import JsonResponse
from django.db.models import Q
from norma.models import Accessuar,CheckNormaBase
from django.contrib import messages
import math
from order.models import Order
    
# Create your views here.


def index(request):
    return render(request,'imzo/index.html')

def file_uploadImzo(request):
      
  if request.method == 'POST':
    form = FileFormImzo(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('imzo_file')
  else:
      form =FileFormImzo()
      context ={
        'form':form
      }
  return render(request,'imzo/excel_form.html',context)

def file_uploadTexcarta_org(request):
      
  if request.method == 'POST':
    form = FileFormImzo(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('texcart_files')
  else:
      form =FileFormImzo()
      context ={
        'section':'Загрузка техкарта файла'
      }
  return render(request,'universal/main.html',context)

def imzo_file(request):
    files = ExcelFilesImzo.objects.filter(generated =False).order_by('-created_at')
    context ={'files':files}
    return render(request,'imzo/file_list.html',context)

def texcart_file(request):
    files = ExcelFilesImzo.objects.filter(generated =False).order_by('-created_at')
    context ={
        'files':files,
        'section':'Формирование техкарта файла',
        'link':'/texcart/texcarta/',
        'type':'техкарта'
        }
    return render(request,'universal/file_list.html',context)


def texcartaupload(request):
    
    # df = pd.read_excel('C:\\OSPanel\\domains\\БазаTexcarta.xlsx','Лист1')
    df = pd.read_excel('C:\\OpenServer\\domains\\БазаTexcarta.xlsx','Лист1')
    df =df.astype(str)
    
    df = df.replace('nan','0')
    
    for i in range(0,df.shape[0]):
        компонент_1 = df['компонент1'][i]
        компонент_2 =df['компонент2'][i]
        компонент_3 =df['компонент3'][i]
        артикул = df['артикул'][i]
        
        пресс_1_линия_буй = df["пресс___1_линия_буй"][i].replace('.0','') if df["пресс___1_линия_буй"][i][-2:]=='.0' else df["пресс___1_линия_буй"][i]
        закалка_1_печь_буй = df["закалка_1_печь_буй"][i].replace('.0','') if df["закалка_1_печь_буй"][i][-2:]=='.0' else df["закалка_1_печь_буй"][i]
        покраска_SKM_белый_про_во_в_сутки_буй = df["покраска_покрасочная_линия_SKM_про_во_в_сутки_буй"][i].replace('.0','') if df["покраска_покрасочная_линия_SKM_про_во_в_сутки_буй"][i][-2:]=='.0' else df["покраска_покрасочная_линия_SKM_про_во_в_сутки_буй"][i]
        покраска_SAT_базовый_про_во_в_сутки_буй = df["покраска_покрасочная_линия_SAT_про_во_в_сутки_буй"][i].replace('.0','') if df["покраска_покрасочная_линия_SAT_про_во_в_сутки_буй"][i][-2:]=='.0' else df["покраска_покрасочная_линия_SAT_про_во_в_сутки_буй"][i]
        покраска_горизонтал_про_во_в_сутки_буй = df["покраска_покрасочная_линия_горизонтал_про_во_в_сутки_буй"][i].replace('.0','') if df["покраска_покрасочная_линия_горизонтал_про_во_в_сутки_буй"][i][-2:]=='.0' else df["покраска_покрасочная_линия_горизонтал_про_во_в_сутки_буй"][i]
        покраска_ручная_про_во_в_сутки_буй = df["покраска_покрасочная_линия_ручная_про_во_в_сутки_буй"][i].replace('.0','') if df["покраска_покрасочная_линия_ручная_про_во_в_сутки_буй"][i][-2:]=='.0' else df["покраска_покрасочная_линия_ручная_про_во_в_сутки_буй"][i]
        вакуум_1_печка_про_во_в_сутки_буй = df["вакуум_1_печка_про_во_в_сутки_буй"][i].replace('.0','') if df["вакуум_1_печка_про_во_в_сутки_буй"][i][-2:]=='.0' else df["вакуум_1_печка_про_во_в_сутки_буй"][i]
        термо_1_линия_про_во_в_сутки_буй = df["термо_1_линия_про_во_в_сутки_буй"][i].replace('.0','') if df["термо_1_линия_про_во_в_сутки_буй"][i][-2:]=='.0' else df["термо_1_линия_про_во_в_сутки_буй"][i]
        наклейка_упаковка_1_линия_про_во_в_сутки_буй = df["наклейка_упаковка_1_линия_про_во_в_сутки_буй"][i].replace('.0','') if df["наклейка_упаковка_1_линия_про_во_в_сутки_буй"][i][-2:]=='.0' else df["наклейка_упаковка_1_линия_про_во_в_сутки_буй"][i]
        ламинат_1_линия_про_во_в_сутки_буй = df["ламинат_1_линия_про_во_в_сутки_буй"][i].replace('.0','') if df["ламинат_1_линия_про_во_в_сутки_буй"][i][-2:]=='.0' else df["ламинат_1_линия_про_во_в_сутки_буй"][i]
        ekstruziya = df["ekstruziya"][i]
        pila = df["pila"][i]
        strayenie = df["strayenie"][i]
        skm_pokras = df["skm_pokras"][i]
        sat_pokras = df["sat_pokras"][i]
        gr_pokras = df["gr_pokras"][i]
        skm_xim = df["skm_xim"][i]
        sat_xim = df["sat_xim"][i]
        gr_xim = df["gr_xim"][i]
        ruchnoy_pokraska = df["ruchnoy_pokraska"][i]
        sublimat = df["sublimat"][i]
        nakleyka = df["nakleyka"][i]
        kombinirovan = df["kombinirovan"][i]
        upakovka = df["upakovka"][i]
        lam_nak_upakovka = df["lam_nak_upakovka"][i]
        kom_upakovka = df["kom_upakovka"][i]
        
        TexCartaTime(
        компонент_1 = компонент_1 ,
        компонент_2 = компонент_2 ,
        компонент_3 = компонент_3 ,
        артикул = артикул ,
        пресс_1_линия_буй = пресс_1_линия_буй ,
        закалка_1_печь_буй = закалка_1_печь_буй ,	
        покраска_SKM_белый_про_во_в_сутки_буй = покраска_SKM_белый_про_во_в_сутки_буй ,
        покраска_SAT_базовый_про_во_в_сутки_буй = покраска_SAT_базовый_про_во_в_сутки_буй ,
        покраска_горизонтал_про_во_в_сутки_буй = покраска_горизонтал_про_во_в_сутки_буй ,
        покраска_ручная_про_во_в_сутки_буй=покраска_ручная_про_во_в_сутки_буй,
        вакуум_1_печка_про_во_в_сутки_буй = вакуум_1_печка_про_во_в_сутки_буй ,
        термо_1_линия_про_во_в_сутки_буй = термо_1_линия_про_во_в_сутки_буй ,
        наклейка_упаковка_1_линия_про_во_в_сутки_буй = наклейка_упаковка_1_линия_про_во_в_сутки_буй ,
        ламинат_1_линия_про_во_в_сутки_буй = ламинат_1_линия_про_во_в_сутки_буй ,
        ekstruziya ='%.2f' % float(ekstruziya.replace(',','.')) if ekstruziya !='' else '0',
        pila ='%.2f' % float(pila.replace(',','.'))if ekstruziya !='' else '0',
        strayenie ='%.2f' % float(strayenie.replace(',','.'))if ekstruziya !='' else '0',
        skm_pokras = '%.2f' % float(skm_pokras.replace(',','.')) if ekstruziya !='' else '0',
        sat_pokras ='%.2f' % float(sat_pokras.replace(',','.')) if ekstruziya !='' else '0',
        gr_pokras = '%.2f' % float(gr_pokras.replace(',','.')) if ekstruziya !='' else '0',
        skm_xim = '%.2f' % float(skm_xim.replace(',','.')) if ekstruziya !='' else '0',
        sat_xim = '%.2f' % float(sat_xim.replace(',','.')) if ekstruziya !='' else '0',
        gr_xim = '%.2f' % float(gr_xim.replace(',','.')) if ekstruziya !='' else '0',
        ruchnoy_pokraska ='%.2f' % float(ruchnoy_pokraska.replace(',','.')) if ekstruziya !='' else '0',
        sublimat ='%.2f' % float(sublimat.replace(',','.')) if ekstruziya !='' else '0',
        nakleyka = '%.2f' % float(nakleyka.replace(',','.')) if ekstruziya !='' else '0',
        kombinirovan = '%.2f' % float(kombinirovan.replace(',','.')) if ekstruziya !='' else '0',
        upakovka = '%.2f' % float(upakovka.replace(',','.')) if ekstruziya !='' else '0',
        lam_nak_upakovka ='%.2f' % float(lam_nak_upakovka.replace(',','.') ) if ekstruziya !='' else '0',
        kom_upakovka = '%.2f' % float(kom_upakovka.replace(',','.')) if ekstruziya !='' else '0'
            ).save()
    
    texcartas = TexCartaTime.objects.all()
    for texs in texcartas:
        print(texs.id)
        texs.компонент_1 = texs.компонент_1.strip()
        texs.компонент_2 = texs.компонент_2.strip()
        texs.компонент_3 = texs.компонент_3.strip()
        texs.артикул = texs.артикул.strip()
        texs.save()
    return JsonResponse({'a':'b'})



def lenght_generate_imzo(request,id):
    file = ExcelFilesImzo.objects.get(id=id).file
    file_path =f'{MEDIA_ROOT}\\{file}'
    df =pd.read_excel(file_path)
    '''Shablon dlya zagruzki [ "МАТЕРИАЛ", "КРАТКИЙ ТЕКСТ", "UMREZ", "UMREN", "USR00", "USR01" ]   sheetname ="BAZA" '''
    df['Дупликат']='No'
    df =df.astype(str)
    counter = 0
    for key,row in df.iterrows():
        if not ImzoBase.objects.filter(material = row['МАТЕРИАЛ'],kratkiytekst = row['КРАТКИЙ ТЕКСТ']).exists():
            if '-7' in row['МАТЕРИАЛ'] or '-K' in row['МАТЕРИАЛ'] or '-N' in row['МАТЕРИАЛ'] or '-S' in row['МАТЕРИАЛ']:
                counter +=2
            elif '-P' in row['МАТЕРИАЛ']:
                counter +=15
            elif '-Z' in row['МАТЕРИАЛ']:
                counter +=4
            elif '-E' in row['МАТЕРИАЛ']:
                counter +=3
        else:
            df['Дупликат'][key]='Yes'

    nakleyka_nan = []
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
    df_new['ACTTYPE_01']=''
    df_new['CKSELKZ']=''
    df_new['UMREZ']=""
    df_new['UMREN']=''
    df_new['USR00']=''
    df_new['USR01']=''
    df_new['SAP CODE']=''

    
    accessuar = Accessuar.objects.all().values_list('sap_code',flat=True)
    sap_code_link = []
    pakraska_nan = []
    counter_2 = 0

    for key,row in df.iterrows():
        if row['Дупликат'] == 'No':
            sap_code = row['МАТЕРИАЛ'].split('-')[0]
            try:
                texcartatime = TexCartaTime.objects.filter(Q(компонент_1=sap_code)|Q(компонент_2=sap_code)|Q(компонент_3=sap_code)|Q(артикул=sap_code))[:1].get()
            except:
                sap_code_link.append(row['МАТЕРИАЛ'])
                
    # if len(sap_code_link) >0:
    #     return JsonResponse({'TexCartada yoqlari':sap_code_link})



    for key,row in df.iterrows():
        print(key)
        if row['Дупликат'] == 'No':
            
            sap_code = row['МАТЕРИАЛ'].split('-')[0]
            texcarta_bor = True
            if TexCartaTime.objects.filter(Q(компонент_1=sap_code)|Q(компонент_2=sap_code)|Q(компонент_3=sap_code)|Q(артикул=sap_code)).exists():
                texcartatime = TexCartaTime.objects.filter(Q(компонент_1=sap_code)|Q(компонент_2=sap_code)|Q(компонент_3=sap_code)|Q(артикул=sap_code))[:1].get()
            else:
                texcarta_bor = False
            if ImzoBase.objects.filter(material = row['МАТЕРИАЛ'],kratkiytekst = row['КРАТКИЙ ТЕКСТ']).exists():
                continue 
                
            if '-7' in row['МАТЕРИАЛ']:
                lenghtht =row['МАТЕРИАЛ'].split('-')[0]
                isklyuchenie =False
                if lenghtht in accessuar:
                    isklyuchenie = True
                if texcarta_bor:
                    if texcartatime.наклейка_упаковка_1_линия_про_во_в_сутки_буй !='nan':
                        if '.' in texcartatime.наклейка_упаковка_1_линия_про_во_в_сутки_буй:
                            nak =("%.3f" % (2 * (float(texcartatime.наклейка_упаковка_1_линия_про_во_в_сутки_буй)))).replace('.',',')
                        else:
                            nak =2 * (int(texcartatime.наклейка_упаковка_1_линия_про_во_в_сутки_буй))
                    else:
                        nak = 'nan'
                        nakleyka_nan.append(lenghtht)
                else:
                    nak='nan'
                kombiniroavniy = ('7777' in row['КРАТКИЙ ТЕКСТ']) or ('8888' in row['КРАТКИЙ ТЕКСТ']) or ('3701' in row['КРАТКИЙ ТЕКСТ']) or ('3702' in row['КРАТКИЙ ТЕКСТ'])
                
                length =len(row['КРАТКИЙ ТЕКСТ'])
                if ((length ==20) or (length ==25) or (length ==17)) :         
                    for i7 in range(1,3):
                        if i7 ==1:
                            df_new['ID'][counter_2] ='1'
                            df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                            df_new['WERKS'][counter_2] ='1101'
                            df_new['STTAG'][counter_2] ='01012023'
                            df_new['PLNAL'][counter_2] ='1'
                            df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                            df_new['VERWE'][counter_2] ='1'
                            df_new['STATU'][counter_2] ='4'
                            df_new['LOSVN'][counter_2] ='1'
                            df_new['LOSBS'][counter_2] ='99999999'
                        elif i7 == 2:
                            df_new['ID'][counter_2]='2'
                            df_new['VORNR'][counter_2] =BAZA['7']['VORNR'][0]
                            df_new['ARBPL'][counter_2] =BAZA['7']['ARBPL'][0]
                            df_new['WERKS1'][counter_2] ='1101'
                            df_new['STEUS'][counter_2] ='ZK01'
                            df_new['LTXA1'][counter_2] =BAZA['7N']['LTXA1'][0] if isklyuchenie else BAZA['7']['LTXA1'][0]
                            df_new['BMSCH'][counter_2] = ''  if isklyuchenie else nak #2 * (int(texcartatime.наклейка_упаковка_1_линия_про_во_в_сутки_буй))
                            df_new['MEINH'][counter_2] = '' if isklyuchenie else BAZA['7']['MEINH'][0] 
                            df_new['VGW01'][counter_2] ='' if isklyuchenie else '24'
                            df_new['VGE01'][counter_2] ='STD'
                            df_new['ACTTYPE_01'][counter_2] =BAZA['7']['ACTTYPE_01'][0]
                            df_new['CKSELKZ'][counter_2] ='X'
                            df_new['UMREZ'][counter_2] = row['UMREZ']
                            df_new['UMREN'][counter_2] = row['UMREN']
                            df_new['USR00'][counter_2] = row['USR00']
                            df_new['USR01'][counter_2] = row['USR01']
                            df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                        counter_2 +=1
                
                
                elif (length ==26) or ((kombiniroavniy)and(length ==36)):         
                    for i7 in range(1,3):
                        if i7 ==1:
                            df_new['ID'][counter_2] ='1'
                            df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                            df_new['WERKS'][counter_2] ='1101'
                            df_new['STTAG'][counter_2] ='01012023'
                            df_new['PLNAL'][counter_2] ='1'
                            df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                            df_new['VERWE'][counter_2] ='1'
                            df_new['STATU'][counter_2] ='4'
                            df_new['LOSVN'][counter_2] ='1'
                            df_new['LOSBS'][counter_2] ='99999999'
                        elif i7 == 2:
                            df_new['ID'][counter_2]='2'
                            df_new['VORNR'][counter_2] =BAZA['7K']['VORNR'][0]
                            df_new['ARBPL'][counter_2] =BAZA['7K']['ARBPL'][0]
                            df_new['WERKS1'][counter_2] ='1101'
                            df_new['STEUS'][counter_2] ='ZK01'
                            df_new['LTXA1'][counter_2] =BAZA['7KN']['LTXA1'][0] if isklyuchenie else BAZA['7K']['LTXA1'][0]
                            df_new['BMSCH'][counter_2] = '' if isklyuchenie else nak
                            df_new['MEINH'][counter_2] ='' if isklyuchenie else BAZA['7K']['MEINH'][0]
                            df_new['VGW01'][counter_2] ='' if isklyuchenie else '24'
                            df_new['VGE01'][counter_2] ='STD'
                            df_new['ACTTYPE_01'][counter_2] =BAZA['7K']['ACTTYPE_01'][0]
                            df_new['CKSELKZ'][counter_2] ='X'
                            df_new['UMREZ'][counter_2] = row['UMREZ']
                            df_new['UMREN'][counter_2] = row['UMREN']
                            df_new['USR00'][counter_2] = row['USR00']
                            df_new['USR01'][counter_2] = row['USR01']
                            df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                        counter_2 +=1
                
                elif ((length ==36) or (length ==30)):         
                    for i7 in range(1,3):
                        if i7 ==1:
                            df_new['ID'][counter_2] ='1'
                            df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                            df_new['WERKS'][counter_2] ='1101'
                            df_new['STTAG'][counter_2] ='01012023'
                            df_new['PLNAL'][counter_2] ='1'
                            df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                            df_new['VERWE'][counter_2] ='1'
                            df_new['STATU'][counter_2] ='4'
                            df_new['LOSVN'][counter_2] ='1'
                            df_new['LOSBS'][counter_2] ='99999999'
                        elif i7 == 2:
                            df_new['ID'][counter_2]='2'
                            df_new['VORNR'][counter_2] =BAZA['7L']['VORNR'][0]
                            df_new['ARBPL'][counter_2] =BAZA['7L']['ARBPL'][0]
                            df_new['WERKS1'][counter_2] ='1101'
                            df_new['STEUS'][counter_2] ='ZK01'
                            df_new['LTXA1'][counter_2] =BAZA['7LN']['LTXA1'][0] if isklyuchenie else BAZA['7L']['LTXA1'][0]
                            df_new['BMSCH'][counter_2] ='' if isklyuchenie else texcartatime.ламинат_1_линия_про_во_в_сутки_буй
                            df_new['MEINH'][counter_2] ='' if isklyuchenie else BAZA['7L']['MEINH'][0]
                            df_new['VGW01'][counter_2] ='' if isklyuchenie else '24'
                            df_new['VGE01'][counter_2] ='STD'
                            df_new['ACTTYPE_01'][counter_2] =BAZA['7L']['ACTTYPE_01'][0]
                            df_new['CKSELKZ'][counter_2] ='X'
                            df_new['UMREZ'][counter_2] = row['UMREZ']
                            df_new['UMREN'][counter_2] = row['UMREN']
                            df_new['USR00'][counter_2] = row['USR00']
                            df_new['USR01'][counter_2] = row['USR01']
                            df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                        counter_2 +=1                
            elif '-K' in row['МАТЕРИАЛ']:
                for i7 in range(1,3):
                    if i7 ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='1101'
                        df_new['STTAG'][counter_2] ='01012023'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i7 == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] =BAZA['K']['VORNR'][0]
                        df_new['ARBPL'][counter_2] =BAZA['K']['ARBPL'][0]
                        df_new['WERKS1'][counter_2] ='1101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] =BAZA['K']['LTXA1'][0]
                        df_new['BMSCH'][counter_2] =texcartatime.термо_1_линия_про_во_в_сутки_буй if texcarta_bor else '11111'
                        df_new['MEINH'][counter_2] =BAZA['K']['MEINH'][0]
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['K']['ACTTYPE_01'][0]
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = row['UMREZ']
                        df_new['UMREN'][counter_2] = row['UMREN']
                        df_new['USR00'][counter_2] = row['USR00']
                        df_new['USR01'][counter_2] = row['USR01']
                        df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                    counter_2 +=1
            elif '-N' in row['МАТЕРИАЛ']:
                for i7 in range(1,3):
                    if i7 ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='1101'
                        df_new['STTAG'][counter_2] ='01012023'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i7 == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] =BAZA['N']['VORNR'][0]
                        df_new['ARBPL'][counter_2] =BAZA['N']['ARBPL'][0]
                        df_new['WERKS1'][counter_2] ='1101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] =BAZA['N']['LTXA1'][0]
                        df_new['BMSCH'][counter_2] =texcartatime.наклейка_упаковка_1_линия_про_во_в_сутки_буй if texcarta_bor else '11111'
                        df_new['MEINH'][counter_2] =BAZA['N']['MEINH'][0]
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['N']['ACTTYPE_01'][0]
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = row['UMREZ']
                        df_new['UMREN'][counter_2] = row['UMREN']
                        df_new['USR00'][counter_2] = row['USR00']
                        df_new['USR01'][counter_2] = row['USR01']
                        df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                    counter_2 +=1
            elif '-S' in row['МАТЕРИАЛ']:
                for i7 in range(1,3):
                    if i7 ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='1101'
                        df_new['STTAG'][counter_2] ='01012023'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i7 == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] =BAZA['S']['VORNR'][0]
                        df_new['ARBPL'][counter_2] =BAZA['S']['ARBPL'][0]
                        df_new['WERKS1'][counter_2] ='1101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] =BAZA['S']['LTXA1'][0]
                        df_new['BMSCH'][counter_2] = texcartatime.вакуум_1_печка_про_во_в_сутки_буй if texcarta_bor else '11111'
                        df_new['MEINH'][counter_2] =BAZA['S']['MEINH'][0]
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['S']['ACTTYPE_01'][0]
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = row['UMREZ']
                        df_new['UMREN'][counter_2] = row['UMREN']
                        df_new['USR00'][counter_2] = row['USR00']
                        df_new['USR01'][counter_2] = row['USR01']
                        df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                    counter_2 +=1
            elif '-E' in row['МАТЕРИАЛ']:
                for i7 in range(1,4):
                    if i7 ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='1101'
                        df_new['STTAG'][counter_2] ='01012023'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i7 == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] =BAZA['E']['VORNR'][0]
                        df_new['ARBPL'][counter_2] =BAZA['E']['ARBPL'][0]
                        df_new['WERKS1'][counter_2] ='1101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] =BAZA['E']['LTXA1'][0]
                        df_new['BMSCH'][counter_2] = texcartatime.пресс_1_линия_буй if texcarta_bor else '11111'
                        df_new['MEINH'][counter_2] =BAZA['E']['MEINH'][0]
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['E']['ACTTYPE_01'][0]
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = row['UMREZ']
                        df_new['UMREN'][counter_2] = row['UMREN']
                        df_new['USR00'][counter_2] = row['USR00']
                        df_new['USR01'][counter_2] = row['USR01']
                        df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                    elif i7 == 3:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] =BAZA['E']['VORNR'][1]
                        df_new['ARBPL'][counter_2] =BAZA['E']['ARBPL'][1]
                        df_new['WERKS1'][counter_2] ='1101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] =BAZA['E']['LTXA1'][1]
                        df_new['BMSCH'][counter_2] = texcartatime.пресс_1_линия_буй if texcarta_bor else '11111'
                        df_new['MEINH'][counter_2] =BAZA['E']['MEINH'][1]
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['E']['ACTTYPE_01'][1]
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = row['UMREZ']
                        df_new['UMREN'][counter_2] = row['UMREN']
                        df_new['USR00'][counter_2] = row['USR00']
                        df_new['USR01'][counter_2] = row['USR01']
                        df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                    counter_2 +=1
            elif '-Z' in row['МАТЕРИАЛ']:
                for i7 in range(1,5):
                    if i7 ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='1101'
                        df_new['STTAG'][counter_2] ='01012023'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i7 == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] =BAZA['Z']['VORNR'][0]
                        df_new['ARBPL'][counter_2] =BAZA['Z']['ARBPL'][0]
                        df_new['WERKS1'][counter_2] ='1101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] =BAZA['Z']['LTXA1'][0]
                        df_new['BMSCH'][counter_2] =texcartatime.пресс_1_линия_буй if texcarta_bor else '11111'
                        df_new['MEINH'][counter_2] =BAZA['Z']['MEINH'][0]
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['Z']['ACTTYPE_01'][0]
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = row['UMREZ']
                        df_new['UMREN'][counter_2] = row['UMREN']
                        df_new['USR00'][counter_2] = row['USR00']
                        df_new['USR01'][counter_2] = row['USR01']
                        df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                    elif i7 == 3:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] =BAZA['Z']['VORNR'][1]
                        df_new['ARBPL'][counter_2] =BAZA['Z']['ARBPL'][1]
                        df_new['WERKS1'][counter_2] ='1101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] =BAZA['Z']['LTXA1'][1]
                        df_new['BMSCH'][counter_2] =texcartatime.пресс_1_линия_буй if texcarta_bor else '11111'
                        df_new['MEINH'][counter_2] =BAZA['Z']['MEINH'][1]
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['Z']['ACTTYPE_01'][1]
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = row['UMREZ']
                        df_new['UMREN'][counter_2] = row['UMREN']
                        df_new['USR00'][counter_2] = row['USR00']
                        df_new['USR01'][counter_2] = row['USR01']
                        df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                    elif i7 == 4:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] =BAZA['Z']['VORNR'][2]
                        df_new['ARBPL'][counter_2] =BAZA['Z']['ARBPL'][2]
                        df_new['WERKS1'][counter_2] ='1101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] =BAZA['Z']['LTXA1'][2]
                        df_new['BMSCH'][counter_2] = texcartatime.закалка_1_печь_буй if texcarta_bor else '11111'
                        df_new['MEINH'][counter_2] =BAZA['Z']['MEINH'][2]
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['Z']['ACTTYPE_01'][2]
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = row['UMREZ']
                        df_new['UMREN'][counter_2] = row['UMREN']
                        df_new['USR00'][counter_2] = row['USR00']
                        df_new['USR01'][counter_2] = row['USR01']
                        df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                    counter_2 +=1
            elif '-P' in row['МАТЕРИАЛ']:
                for p in range(1,7):
                    if p ==1:
                        ## SKM -SKM покраска
                        for i in range(1,3):
                            
                            if i ==1:
                                df_new['ID'][counter_2] ='1'
                                df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                df_new['WERKS'][counter_2] ='1101'
                                df_new['STTAG'][counter_2] ='01012023'
                                df_new['PLNAL'][counter_2] ='1'
                                df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ'] +' / '+' / ' + str(p)
                                df_new['VERWE'][counter_2] ='1'
                                df_new['STATU'][counter_2] ='4'
                                df_new['LOSVN'][counter_2] ='1'
                                df_new['LOSBS'][counter_2] ='99999999'
                            elif i == 2:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P1']['VORNR'][0]
                                df_new['ARBPL'][counter_2] =BAZA['P1']['ARBPL'][0]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P1']['LTXA1'][0]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_SKM_белый_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P1']['MEINH'][0]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P1']['ACTTYPE_01'][0]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] = row['USR01']
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            counter_2 +=1
                    elif p == 2:
                        for i in range(1,3):
                            if i ==1:
                                df_new['ID'][counter_2] ='1'
                                df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                df_new['WERKS'][counter_2] ='1101'
                                df_new['STTAG'][counter_2] ='01012023'
                                df_new['PLNAL'][counter_2] ='1'
                                df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']+' / ' + str(p)
                                df_new['VERWE'][counter_2] ='1'
                                df_new['STATU'][counter_2] ='4'
                                df_new['LOSVN'][counter_2] ='1'
                                df_new['LOSBS'][counter_2] ='99999999'
                            elif i == 2:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P2']['VORNR'][0]
                                df_new['ARBPL'][counter_2] =BAZA['P2']['ARBPL'][0]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P2']['LTXA1'][0]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_SAT_базовый_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P2']['MEINH'][0]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P2']['ACTTYPE_01'][0]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] = row['USR01']
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            counter_2 +=1
                    elif p == 3:
                        for i in range(1,3):
                            if i ==1:
                                df_new['ID'][counter_2] ='1'
                                df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                df_new['WERKS'][counter_2] ='1101'
                                df_new['STTAG'][counter_2] ='01012023'
                                df_new['PLNAL'][counter_2] ='1'
                                df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']+' / ' + str(p)
                                df_new['VERWE'][counter_2] ='1'
                                df_new['STATU'][counter_2] ='4'
                                df_new['LOSVN'][counter_2] ='1'
                                df_new['LOSBS'][counter_2] ='99999999'
                            elif i == 2:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P3']['VORNR'][0]
                                df_new['ARBPL'][counter_2] =BAZA['P3']['ARBPL'][0]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P3']['LTXA1'][0]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_горизонтал_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P3']['MEINH'][0]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P3']['ACTTYPE_01'][0]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] = row['USR01']
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            counter_2 +=1
                    elif p == 4:
                        for i in range(1,4):
                            if i ==1:
                                df_new['ID'][counter_2] ='1'
                                df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                df_new['WERKS'][counter_2] ='1101'
                                df_new['STTAG'][counter_2] ='01012023'
                                df_new['PLNAL'][counter_2] ='1'
                                df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']+' / ' + str(p)
                                df_new['VERWE'][counter_2] ='1'
                                df_new['STATU'][counter_2] ='4'
                                df_new['LOSVN'][counter_2] ='1'
                                df_new['LOSBS'][counter_2] ='99999999'
                            elif i == 2:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P4']['VORNR'][0]
                                df_new['ARBPL'][counter_2] =BAZA['P4']['ARBPL'][0]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P4']['LTXA1'][0]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_SKM_белый_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P4']['MEINH'][0]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P4']['ACTTYPE_01'][0]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] = row['USR01']
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            elif i == 3:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P4']['VORNR'][1]
                                df_new['ARBPL'][counter_2] =BAZA['P4']['ARBPL'][1]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P4']['LTXA1'][1]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_ручная_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P4']['MEINH'][1]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P4']['ACTTYPE_01'][1]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] = row['USR01']
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            counter_2 +=1
                    elif p == 5:
                        for i in range(1,4):
                            if i ==1:
                                df_new['ID'][counter_2] ='1'
                                df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                df_new['WERKS'][counter_2] ='1101'
                                df_new['STTAG'][counter_2] ='01012023'
                                df_new['PLNAL'][counter_2] ='1'
                                df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']+' / ' + str(p)
                                df_new['VERWE'][counter_2] ='1'
                                df_new['STATU'][counter_2] ='4'
                                df_new['LOSVN'][counter_2] ='1'
                                df_new['LOSBS'][counter_2] ='99999999'
                            elif i == 2:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P5']['VORNR'][0]
                                df_new['ARBPL'][counter_2] =BAZA['P5']['ARBPL'][0]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P5']['LTXA1'][0]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_SAT_базовый_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P5']['MEINH'][0]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P5']['ACTTYPE_01'][0]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] = row['USR01']
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            elif i == 3:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P5']['VORNR'][1]
                                df_new['ARBPL'][counter_2] =BAZA['P5']['ARBPL'][1]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P5']['LTXA1'][1]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_ручная_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P5']['MEINH'][1]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P5']['ACTTYPE_01'][1]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] = row['USR01']
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            counter_2 +=1
                    elif p == 6:
                        for i in range(1,4):
                            if i ==1:
                                df_new['ID'][counter_2] ='1'
                                df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                df_new['WERKS'][counter_2] ='1101'
                                df_new['STTAG'][counter_2] ='01012023'
                                df_new['PLNAL'][counter_2] ='1'
                                df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']+' / ' + str(p)
                                df_new['VERWE'][counter_2] ='1'
                                df_new['STATU'][counter_2] ='4'
                                df_new['LOSVN'][counter_2] ='1'
                                df_new['LOSBS'][counter_2] ='99999999'
                            elif i == 2:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P6']['VORNR'][0]
                                df_new['ARBPL'][counter_2] =BAZA['P6']['ARBPL'][0]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P6']['LTXA1'][0]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_горизонтал_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P6']['MEINH'][0]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P6']['ACTTYPE_01'][0]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] = row['USR01']
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            elif i == 3:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P6']['VORNR'][1]
                                df_new['ARBPL'][counter_2] =BAZA['P6']['ARBPL'][1]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P6']['LTXA1'][1]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_ручная_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P6']['MEINH'][1]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P6']['ACTTYPE_01'][1]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] = row['USR01']
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            counter_2 +=1
    
            ImzoBase(material = row['МАТЕРИАЛ'],kratkiytekst = row['КРАТКИЙ ТЕКСТ']).save()
    
    meins7 = []
    df_new=df_new.replace('nan','')

    for i in df_new.index:
        mein_txt = str(df_new.loc[i, "BMSCH"])
        if mein_txt[-4:] ==',000':
            meins7.append(mein_txt.replace(',000',''))
        else:
            if mein_txt !='':
                if mein_txt[-4:] ==',000':
                    meins7.append(mein_txt.replace(',000',''))
                else:
                    meins7.append(math.ceil(float(mein_txt)))
            else:
                meins7.append(mein_txt)
    df_new['BMSCH'] =meins7

    
    
    
    del df_new["counter"]
    from datetime import datetime
    now = datetime.now()
    s2 = now.strftime("%d-%m-%Y__%H-%M-%S")
    
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M-%S")    
                 
            
    create_folder(f'{MEDIA_ROOT}\\uploads','texcarta')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta\\{year}',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta\\{year}\\{month}',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta\\{year}\\{month}\\{day}',hour)
    
    path =f'{MEDIA_ROOT}\\uploads\\texcarta\\{year}\\{month}\\{day}\\{hour}\\duplicate.xlsx'
    df.to_excel(path)
    path3 =f'{MEDIA_ROOT}\\uploads\\texcarta\\{year}\\{month}\\{day}\\{hour}\\no_time.xlsx'
    path4 =f'{MEDIA_ROOT}\\uploads\\texcarta\\{year}\\{month}\\{day}\\{hour}\\no_sap_code.xlsx'
    
    df_no_sap_code =pd.DataFrame({'sap_code':sap_code_link})
    df_no_sap_code.to_excel(path4)


    df_no_time =pd.DataFrame({'artikul':nakleyka_nan})
    df_no_time.to_excel(path3)
    path2 =f'{MEDIA_ROOT}\\uploads\\texcarta\\{year}\\{month}\\{day}\\{hour}\\цикл_тайм_для_тех_карты_{day}_{month}_{year}_{hour}_{minut}.xlsx'
    df_new.to_excel(path2)
    return redirect('texcart_file_upload')

def lenght_generate_texcarta(request,id):
    file = ExcelFilesImzo.objects.get(id=id).file
    file_path =f'{MEDIA_ROOT}\\{file}'
    df =pd.read_excel(file_path)
    
    '''Shablon dlya zagruzki [ "МАТЕРИАЛ", "КРАТКИЙ ТЕКСТ", "UMREZ", "UMREN", "USR00", "USR01" ]   sheetname ="BAZA" '''
    df['Дупликат']='No'
    df =df.astype(str)
    counter = 0
    for key,row in df.iterrows():
        if not ImzoBase.objects.filter(material = row['МАТЕРИАЛ'],kratkiytekst = row['КРАТКИЙ ТЕКСТ']).exists():
            if '-7' in row['МАТЕРИАЛ'] or '-K' in row['МАТЕРИАЛ'] or '-N' in row['МАТЕРИАЛ'] or '-S' in row['МАТЕРИАЛ']:
                counter +=2
            elif '-P' in row['МАТЕРИАЛ']:
                counter +=15
            elif '-Z' in row['МАТЕРИАЛ']:
                counter +=4
            elif '-E' in row['МАТЕРИАЛ']:
                counter +=3
        else:
            df['Дупликат'][key]='Yes'

    nakleyka_nan = []
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
    df_new['ACTTYPE_01']=''
    df_new['CKSELKZ']=''
    df_new['UMREZ']=""
    df_new['UMREN']=''
    df_new['USR00']=''
    df_new['USR01']=''
    df_new['SAP CODE']=''

    
    accessuar = Accessuar.objects.all().values_list('sap_code',flat=True)
    sap_code_link = []
    pakraska_nan = []
    counter_2 = 0

    for key,row in df.iterrows():
        if row['Дупликат'] == 'No':
            sap_code = row['МАТЕРИАЛ'].split('-')[0]
            try:
                texcartatime = TexCartaTime.objects.filter(Q(компонент_1=sap_code)|Q(компонент_2=sap_code)|Q(компонент_3=sap_code)|Q(артикул=sap_code))[:1].get()
            except:
                sap_code_link.append(row['МАТЕРИАЛ'])
                
    # if len(sap_code_link) >0:
    #     return JsonResponse({'TexCartada yoqlari':sap_code_link})



    for key,row in df.iterrows():
        print(key)
        if row['Дупликат'] == 'No':
            
            sap_code = row['МАТЕРИАЛ'].split('-')[0]
            texcarta_bor = True
            print(sap_code)
            if TexCartaTime.objects.filter(Q(компонент_1=sap_code)|Q(компонент_2=sap_code)|Q(компонент_3=sap_code)|Q(артикул=sap_code)).exists():
                texcartatime = TexCartaTime.objects.filter(Q(компонент_1=sap_code)|Q(компонент_2=sap_code)|Q(компонент_3=sap_code)|Q(артикул=sap_code))[:1].get()
            else:
                texcarta_bor = False
            if ImzoBase.objects.filter(material = row['МАТЕРИАЛ'],kratkiytekst = row['КРАТКИЙ ТЕКСТ']).exists():
                continue 
                
            if '-7' in row['МАТЕРИАЛ']:
                lenghtht =row['МАТЕРИАЛ'].split('-')[0]
                isklyuchenie =False
                if lenghtht in accessuar:
                    isklyuchenie = True
                if texcarta_bor:
                    print(row['МАТЕРИАЛ'])
                    if ((texcartatime.наклейка_упаковка_1_линия_про_во_в_сутки_буй !='nan') or (texcartatime.наклейка_упаковка_1_линия_про_во_в_сутки_буй != "")):
                        if '.' in texcartatime.наклейка_упаковка_1_линия_про_во_в_сутки_буй:
                            if 'NT1' in row['КРАТКИЙ ТЕКСТ']:
                                nak ='nan'
                            else:
                                nak =("%.3f" % (2 * (float(texcartatime.наклейка_упаковка_1_линия_про_во_в_сутки_буй)))).replace('.',',')
                        else:
                            if 'NT1' in row['КРАТКИЙ ТЕКСТ']:
                                nak = 'nan'
                            else:
                                nak =2 * (int(texcartatime.наклейка_упаковка_1_линия_про_во_в_сутки_буй))
                    else:
                        nak = 'nan'
                        nakleyka_nan.append(lenghtht)
                else:
                    nak='nan'
                kombiniroavniy = ('7777' in row['КРАТКИЙ ТЕКСТ']) or ('8888' in row['КРАТКИЙ ТЕКСТ']) or ('3701' in row['КРАТКИЙ ТЕКСТ']) or ('3702' in row['КРАТКИЙ ТЕКСТ'])
                
                length =len(row['КРАТКИЙ ТЕКСТ'])
                if ((length ==20) or (length ==25) or (length ==17)) :         
                    for i7 in range(1,3):
                        if i7 ==1:
                            df_new['ID'][counter_2] ='1'
                            df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                            df_new['WERKS'][counter_2] ='1101'
                            df_new['STTAG'][counter_2] ='01012023'
                            df_new['PLNAL'][counter_2] ='1'
                            df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                            df_new['VERWE'][counter_2] ='1'
                            df_new['STATU'][counter_2] ='4'
                            df_new['LOSVN'][counter_2] ='1'
                            df_new['LOSBS'][counter_2] ='99999999'
                        elif i7 == 2:
                            df_new['ID'][counter_2]='2'
                            df_new['VORNR'][counter_2] =BAZA['7']['VORNR'][0]
                            df_new['ARBPL'][counter_2] =BAZA['7']['ARBPL'][0]
                            df_new['WERKS1'][counter_2] ='1101'
                            df_new['STEUS'][counter_2] ='ZK01'
                            df_new['LTXA1'][counter_2] =BAZA['7N']['LTXA1'][0] if isklyuchenie else BAZA['7']['LTXA1'][0]
                            df_new['BMSCH'][counter_2] = ''  if isklyuchenie else nak #2 * (int(texcartatime.наклейка_упаковка_1_линия_про_во_в_сутки_буй))
                            df_new['MEINH'][counter_2] = '' if isklyuchenie else BAZA['7']['MEINH'][0] 
                            df_new['VGW01'][counter_2] ='' if isklyuchenie else '24'
                            df_new['VGE01'][counter_2] ='STD'
                            df_new['ACTTYPE_01'][counter_2] =BAZA['7']['ACTTYPE_01'][0]
                            df_new['CKSELKZ'][counter_2] ='X'
                            df_new['UMREZ'][counter_2] = row['UMREZ']
                            df_new['UMREN'][counter_2] = row['UMREN']
                            df_new['USR00'][counter_2] = row['USR00']
                            df_new['USR01'][counter_2] = texcartatime.upakovka if not isklyuchenie else row['USR01']
                            df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                        counter_2 +=1
                
                
                elif (length ==26) or ((kombiniroavniy)and(length ==36)):         
                    for i7 in range(1,3):
                        if i7 ==1:
                            df_new['ID'][counter_2] ='1'
                            df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                            df_new['WERKS'][counter_2] ='1101'
                            df_new['STTAG'][counter_2] ='01012023'
                            df_new['PLNAL'][counter_2] ='1'
                            df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                            df_new['VERWE'][counter_2] ='1'
                            df_new['STATU'][counter_2] ='4'
                            df_new['LOSVN'][counter_2] ='1'
                            df_new['LOSBS'][counter_2] ='99999999'
                        elif i7 == 2:
                            df_new['ID'][counter_2]='2'
                            df_new['VORNR'][counter_2] =BAZA['7K']['VORNR'][0]
                            df_new['ARBPL'][counter_2] =BAZA['7K']['ARBPL'][0]
                            df_new['WERKS1'][counter_2] ='1101'
                            df_new['STEUS'][counter_2] ='ZK01'
                            df_new['LTXA1'][counter_2] =BAZA['7KN']['LTXA1'][0] if isklyuchenie else BAZA['7K']['LTXA1'][0]
                            df_new['BMSCH'][counter_2] = '' if isklyuchenie else nak
                            df_new['MEINH'][counter_2] ='' if isklyuchenie else BAZA['7K']['MEINH'][0]
                            df_new['VGW01'][counter_2] ='' if isklyuchenie else '24'
                            df_new['VGE01'][counter_2] ='STD'
                            df_new['ACTTYPE_01'][counter_2] =BAZA['7K']['ACTTYPE_01'][0]
                            df_new['CKSELKZ'][counter_2] ='X'
                            df_new['UMREZ'][counter_2] = row['UMREZ']
                            df_new['UMREN'][counter_2] = row['UMREN']
                            df_new['USR00'][counter_2] = row['USR00']
                            df_new['USR01'][counter_2] = texcartatime.kom_upakovka if not isklyuchenie else row['USR01']
                            df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                        counter_2 +=1
                
                elif ((length ==36) or (length ==30)):         
                    for i7 in range(1,3):
                        if i7 ==1:
                            df_new['ID'][counter_2] ='1'
                            df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                            df_new['WERKS'][counter_2] ='1101'
                            df_new['STTAG'][counter_2] ='01012023'
                            df_new['PLNAL'][counter_2] ='1'
                            df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                            df_new['VERWE'][counter_2] ='1'
                            df_new['STATU'][counter_2] ='4'
                            df_new['LOSVN'][counter_2] ='1'
                            df_new['LOSBS'][counter_2] ='99999999'
                        elif i7 == 2:
                            ltx1 = ''
                            text_tt = row['USR00']
                            if isklyuchenie:
                                ltx1 =BAZA['7LN']['LTXA1'][0]
                            elif 'NT1' in row['КРАТКИЙ ТЕКСТ']:
                                ltx1 =BAZA['7L']['LTXA1'][1]
                                text_tt = texcartatime.lam_nak_upakovka
                            else:
                                ltx1 =BAZA['7L']['LTXA1'][0]
                                text_tt = texcartatime.lam_nak_upakovka

                            df_new['ID'][counter_2]='2'
                            df_new['VORNR'][counter_2] =BAZA['7L']['VORNR'][0]
                            df_new['ARBPL'][counter_2] =BAZA['7L']['ARBPL'][0]
                            df_new['WERKS1'][counter_2] ='1101'
                            df_new['STEUS'][counter_2] ='ZK01'
                            df_new['LTXA1'][counter_2] = ltx1
                            df_new['BMSCH'][counter_2] ='' if isklyuchenie else texcartatime.ламинат_1_линия_про_во_в_сутки_буй
                            df_new['MEINH'][counter_2] ='' if isklyuchenie else BAZA['7L']['MEINH'][0]
                            df_new['VGW01'][counter_2] ='' if isklyuchenie else '24'
                            df_new['VGE01'][counter_2] ='STD'
                            df_new['ACTTYPE_01'][counter_2] =BAZA['7L']['ACTTYPE_01'][0]
                            df_new['CKSELKZ'][counter_2] ='X'
                            df_new['UMREZ'][counter_2] = row['UMREZ']
                            df_new['UMREN'][counter_2] = row['UMREN']
                            df_new['USR00'][counter_2] = row['USR00']
                            df_new['USR01'][counter_2] = text_tt
                            df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                        counter_2 +=1                
            elif '-K' in row['МАТЕРИАЛ']:
                for i7 in range(1,3):
                    if i7 ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='1101'
                        df_new['STTAG'][counter_2] ='01012023'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i7 == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] =BAZA['K']['VORNR'][0]
                        df_new['ARBPL'][counter_2] =BAZA['K']['ARBPL'][0]
                        df_new['WERKS1'][counter_2] ='1101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] =BAZA['K']['LTXA1'][0]
                        df_new['BMSCH'][counter_2] =texcartatime.термо_1_линия_про_во_в_сутки_буй if texcarta_bor else '11111'
                        df_new['MEINH'][counter_2] =BAZA['K']['MEINH'][0]
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['K']['ACTTYPE_01'][0]
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = row['UMREZ']
                        df_new['UMREN'][counter_2] = row['UMREN']
                        df_new['USR00'][counter_2] = row['USR00']
                        df_new['USR01'][counter_2] = texcartatime.kombinirovan if texcarta_bor else '0'
                        df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                    counter_2 +=1
            elif '-N' in row['МАТЕРИАЛ']:
                for i7 in range(1,3):
                    if i7 ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='1101'
                        df_new['STTAG'][counter_2] ='01012023'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i7 == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] =BAZA['N']['VORNR'][0]
                        df_new['ARBPL'][counter_2] =BAZA['N']['ARBPL'][0]
                        df_new['WERKS1'][counter_2] ='1101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] =BAZA['N']['LTXA1'][0]
                        df_new['BMSCH'][counter_2] =texcartatime.наклейка_упаковка_1_линия_про_во_в_сутки_буй if texcarta_bor else '11111'
                        df_new['MEINH'][counter_2] =BAZA['N']['MEINH'][0]
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['N']['ACTTYPE_01'][0]
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = row['UMREZ']
                        df_new['UMREN'][counter_2] = row['UMREN']
                        df_new['USR00'][counter_2] = row['USR00']
                        df_new['USR01'][counter_2] = texcartatime.nakleyka if texcarta_bor else '0'
                        df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                    counter_2 +=1
            elif '-S' in row['МАТЕРИАЛ']:
                for i7 in range(1,3):
                    if i7 ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='1101'
                        df_new['STTAG'][counter_2] ='01012023'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i7 == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] =BAZA['S']['VORNR'][0]
                        df_new['ARBPL'][counter_2] =BAZA['S']['ARBPL'][0]
                        df_new['WERKS1'][counter_2] ='1101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] =BAZA['S']['LTXA1'][0]
                        df_new['BMSCH'][counter_2] = texcartatime.вакуум_1_печка_про_во_в_сутки_буй if texcarta_bor else '11111'
                        df_new['MEINH'][counter_2] =BAZA['S']['MEINH'][0]
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['S']['ACTTYPE_01'][0]
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = row['UMREZ']
                        df_new['UMREN'][counter_2] = row['UMREN']
                        df_new['USR00'][counter_2] = row['USR00']
                        df_new['USR01'][counter_2] = texcartatime.sublimat if texcarta_bor else '0'
                        df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                    counter_2 +=1
            elif '-E' in row['МАТЕРИАЛ']:
                for i7 in range(1,4):
                    if i7 ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='1101'
                        df_new['STTAG'][counter_2] ='01012023'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i7 == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] =BAZA['E']['VORNR'][0]
                        df_new['ARBPL'][counter_2] =BAZA['E']['ARBPL'][0]
                        df_new['WERKS1'][counter_2] ='1101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] =BAZA['E']['LTXA1'][0]
                        df_new['BMSCH'][counter_2] = texcartatime.пресс_1_линия_буй if texcarta_bor else '11111'
                        df_new['MEINH'][counter_2] =BAZA['E']['MEINH'][0]
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['E']['ACTTYPE_01'][0]
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = row['UMREZ']
                        df_new['UMREN'][counter_2] = row['UMREN']
                        df_new['USR00'][counter_2] = row['USR00']
                        df_new['USR01'][counter_2] = texcartatime.ekstruziya if texcarta_bor else '0'
                        df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                    elif i7 == 3:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] =BAZA['E']['VORNR'][1]
                        df_new['ARBPL'][counter_2] =BAZA['E']['ARBPL'][1]
                        df_new['WERKS1'][counter_2] ='1101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] =BAZA['E']['LTXA1'][1]
                        df_new['BMSCH'][counter_2] = texcartatime.пресс_1_линия_буй if texcarta_bor else '11111'
                        df_new['MEINH'][counter_2] =BAZA['E']['MEINH'][1]
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['E']['ACTTYPE_01'][1]
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = row['UMREZ']
                        df_new['UMREN'][counter_2] = row['UMREN']
                        df_new['USR00'][counter_2] = row['USR00']
                        df_new['USR01'][counter_2] = texcartatime.pila if texcarta_bor else '0'
                        df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                    counter_2 +=1
            elif '-Z' in row['МАТЕРИАЛ']:
                for i7 in range(1,5):
                    if i7 ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='1101'
                        df_new['STTAG'][counter_2] ='01012023'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i7 == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] =BAZA['Z']['VORNR'][0]
                        df_new['ARBPL'][counter_2] =BAZA['Z']['ARBPL'][0]
                        df_new['WERKS1'][counter_2] ='1101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] =BAZA['Z']['LTXA1'][0]
                        df_new['BMSCH'][counter_2] =texcartatime.пресс_1_линия_буй if texcarta_bor else '11111'
                        df_new['MEINH'][counter_2] =BAZA['Z']['MEINH'][0]
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['Z']['ACTTYPE_01'][0]
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = row['UMREZ']
                        df_new['UMREN'][counter_2] = row['UMREN']
                        df_new['USR00'][counter_2] = row['USR00']
                        df_new['USR01'][counter_2] = texcartatime.ekstruziya if texcarta_bor else '0'
                        df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                    elif i7 == 3:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] =BAZA['Z']['VORNR'][1]
                        df_new['ARBPL'][counter_2] =BAZA['Z']['ARBPL'][1]
                        df_new['WERKS1'][counter_2] ='1101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] =BAZA['Z']['LTXA1'][1]
                        df_new['BMSCH'][counter_2] =texcartatime.пресс_1_линия_буй if texcarta_bor else '11111'
                        df_new['MEINH'][counter_2] =BAZA['Z']['MEINH'][1]
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['Z']['ACTTYPE_01'][1]
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = row['UMREZ']
                        df_new['UMREN'][counter_2] = row['UMREN']
                        df_new['USR00'][counter_2] = row['USR00']
                        df_new['USR01'][counter_2] = texcartatime.pila if texcarta_bor else '0'
                        df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                    elif i7 == 4:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] =BAZA['Z']['VORNR'][2]
                        df_new['ARBPL'][counter_2] =BAZA['Z']['ARBPL'][2]
                        df_new['WERKS1'][counter_2] ='1101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] =BAZA['Z']['LTXA1'][2]
                        df_new['BMSCH'][counter_2] = texcartatime.закалка_1_печь_буй if texcarta_bor else '11111'
                        df_new['MEINH'][counter_2] =BAZA['Z']['MEINH'][2]
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['Z']['ACTTYPE_01'][2]
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = row['UMREZ']
                        df_new['UMREN'][counter_2] = row['UMREN']
                        df_new['USR00'][counter_2] = row['USR00']
                        df_new['USR01'][counter_2] = texcartatime.strayenie if texcarta_bor else '0'
                        df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                    counter_2 +=1
            elif '-P' in row['МАТЕРИАЛ']:
                for p in range(1,7):
                    if p ==1:
                        ## SKM -SKM покраска
                        for i in range(1,3):
                            
                            if i ==1:
                                df_new['ID'][counter_2] ='1'
                                df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                df_new['WERKS'][counter_2] ='1101'
                                df_new['STTAG'][counter_2] ='01012023'
                                df_new['PLNAL'][counter_2] ='1'
                                df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ'] +' / ' + str(p)
                                df_new['VERWE'][counter_2] ='1'
                                df_new['STATU'][counter_2] ='4'
                                df_new['LOSVN'][counter_2] ='1'
                                df_new['LOSBS'][counter_2] ='99999999'
                            elif i == 2:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P1']['VORNR'][0]
                                df_new['ARBPL'][counter_2] =BAZA['P1']['ARBPL'][0]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P1']['LTXA1'][0]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_SKM_белый_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P1']['MEINH'][0]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P1']['ACTTYPE_01'][0]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] =texcartatime.skm_pokras if texcarta_bor else '0'
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            counter_2 +=1
                    elif p == 2:
                        for i in range(1,3):
                            if i ==1:
                                df_new['ID'][counter_2] ='1'
                                df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                df_new['WERKS'][counter_2] ='1101'
                                df_new['STTAG'][counter_2] ='01012023'
                                df_new['PLNAL'][counter_2] ='1'
                                df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']+' / ' + str(p)
                                df_new['VERWE'][counter_2] ='1'
                                df_new['STATU'][counter_2] ='4'
                                df_new['LOSVN'][counter_2] ='1'
                                df_new['LOSBS'][counter_2] ='99999999'
                            elif i == 2:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P2']['VORNR'][0]
                                df_new['ARBPL'][counter_2] =BAZA['P2']['ARBPL'][0]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P2']['LTXA1'][0]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_SAT_базовый_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P2']['MEINH'][0]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P2']['ACTTYPE_01'][0]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] = texcartatime.sat_pokras if texcarta_bor else '0'
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            counter_2 +=1
                    elif p == 3:
                        for i in range(1,3):
                            if i ==1:
                                df_new['ID'][counter_2] ='1'
                                df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                df_new['WERKS'][counter_2] ='1101'
                                df_new['STTAG'][counter_2] ='01012023'
                                df_new['PLNAL'][counter_2] ='1'
                                df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']+' / ' + str(p)
                                df_new['VERWE'][counter_2] ='1'
                                df_new['STATU'][counter_2] ='4'
                                df_new['LOSVN'][counter_2] ='1'
                                df_new['LOSBS'][counter_2] ='99999999'
                            elif i == 2:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P3']['VORNR'][0]
                                df_new['ARBPL'][counter_2] =BAZA['P3']['ARBPL'][0]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P3']['LTXA1'][0]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_горизонтал_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P3']['MEINH'][0]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P3']['ACTTYPE_01'][0]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] = texcartatime.gr_pokras if texcarta_bor else '0'
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            counter_2 +=1
                    elif p == 4:
                        for i in range(1,4):
                            if i ==1:
                                df_new['ID'][counter_2] ='1'
                                df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                df_new['WERKS'][counter_2] ='1101'
                                df_new['STTAG'][counter_2] ='01012023'
                                df_new['PLNAL'][counter_2] ='1'
                                df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']+' / ' + str(p)
                                df_new['VERWE'][counter_2] ='1'
                                df_new['STATU'][counter_2] ='4'
                                df_new['LOSVN'][counter_2] ='1'
                                df_new['LOSBS'][counter_2] ='99999999'
                            elif i == 2:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P4']['VORNR'][0]
                                df_new['ARBPL'][counter_2] =BAZA['P4']['ARBPL'][0]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P4']['LTXA1'][0]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_SKM_белый_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P4']['MEINH'][0]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P4']['ACTTYPE_01'][0]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] = texcartatime.skm_xim if texcarta_bor else '0'
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            elif i == 3:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P4']['VORNR'][1]
                                df_new['ARBPL'][counter_2] =BAZA['P4']['ARBPL'][1]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P4']['LTXA1'][1]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_ручная_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P4']['MEINH'][1]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P4']['ACTTYPE_01'][1]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] =  texcartatime.ruchnoy_pokraska if texcarta_bor else '0'
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            counter_2 +=1
                    elif p == 5:
                        for i in range(1,4):
                            if i ==1:
                                df_new['ID'][counter_2] ='1'
                                df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                df_new['WERKS'][counter_2] ='1101'
                                df_new['STTAG'][counter_2] ='01012023'
                                df_new['PLNAL'][counter_2] ='1'
                                df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']+' / ' + str(p)
                                df_new['VERWE'][counter_2] ='1'
                                df_new['STATU'][counter_2] ='4'
                                df_new['LOSVN'][counter_2] ='1'
                                df_new['LOSBS'][counter_2] ='99999999'
                            elif i == 2:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P5']['VORNR'][0]
                                df_new['ARBPL'][counter_2] =BAZA['P5']['ARBPL'][0]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P5']['LTXA1'][0]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_SAT_базовый_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P5']['MEINH'][0]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P5']['ACTTYPE_01'][0]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] =  texcartatime.sat_xim if texcarta_bor else '0'
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            elif i == 3:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P5']['VORNR'][1]
                                df_new['ARBPL'][counter_2] =BAZA['P5']['ARBPL'][1]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P5']['LTXA1'][1]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_ручная_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P5']['MEINH'][1]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P5']['ACTTYPE_01'][1]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] =  texcartatime.ruchnoy_pokraska if texcarta_bor else '0'
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            counter_2 +=1
                    elif p == 6:
                        for i in range(1,4):
                            if i ==1:
                                df_new['ID'][counter_2] ='1'
                                df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                df_new['WERKS'][counter_2] ='1101'
                                df_new['STTAG'][counter_2] ='01012023'
                                df_new['PLNAL'][counter_2] ='1'
                                df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']+' / ' + str(p)
                                df_new['VERWE'][counter_2] ='1'
                                df_new['STATU'][counter_2] ='4'
                                df_new['LOSVN'][counter_2] ='1'
                                df_new['LOSBS'][counter_2] ='99999999'
                            elif i == 2:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P6']['VORNR'][0]
                                df_new['ARBPL'][counter_2] =BAZA['P6']['ARBPL'][0]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P6']['LTXA1'][0]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_горизонтал_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P6']['MEINH'][0]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P6']['ACTTYPE_01'][0]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] = texcartatime.gr_xim if texcarta_bor else '0'
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            elif i == 3:
                                df_new['ID'][counter_2]='2'
                                df_new['VORNR'][counter_2] =BAZA['P6']['VORNR'][1]
                                df_new['ARBPL'][counter_2] =BAZA['P6']['ARBPL'][1]
                                df_new['WERKS1'][counter_2] ='1101'
                                df_new['STEUS'][counter_2] ='ZK01'
                                df_new['LTXA1'][counter_2] =BAZA['P6']['LTXA1'][1]
                                df_new['BMSCH'][counter_2] =texcartatime.покраска_ручная_про_во_в_сутки_буй if texcarta_bor else '11111'
                                df_new['MEINH'][counter_2] =BAZA['P6']['MEINH'][1]
                                df_new['VGW01'][counter_2] ='24'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P6']['ACTTYPE_01'][1]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] =texcartatime.ruchnoy_pokraska if texcarta_bor else '0'
                                df_new['SAP CODE'][counter_2]=row['МАТЕРИАЛ']
                            counter_2 +=1
    
            ImzoBase(material = row['МАТЕРИАЛ'],kratkiytekst = row['КРАТКИЙ ТЕКСТ']).save()
    
    meins7 = []
    df_new=df_new.replace('nan','')

    for i in df_new.index:
        mein_txt = str(df_new.loc[i, "BMSCH"])
        if mein_txt[-4:] ==',000':
            meins7.append(mein_txt.replace(',000',''))
        else:
            if mein_txt !='':
                if mein_txt[-4:] ==',000':
                    meins7.append(mein_txt.replace(',000',''))
                else:
                    meins7.append(math.ceil(float(mein_txt)))
            else:
                meins7.append(mein_txt)
    df_new['BMSCH'] =meins7

    
    
    
    del df_new["counter"]
    from datetime import datetime
    now = datetime.now()
    s2 = now.strftime("%d-%m-%Y__%H-%M-%S")
    
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M-%S")    
                 
            
    create_folder(f'{MEDIA_ROOT}\\uploads','texcarta')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta\\{year}',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta\\{year}\\{month}',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta\\{year}\\{month}\\{day}',hour)
    
    path =f'{MEDIA_ROOT}\\uploads\\texcarta\\{year}\\{month}\\{day}\\{hour}\\duplicate.xlsx'
    df.to_excel(path)
    path3 =f'{MEDIA_ROOT}\\uploads\\texcarta\\{year}\\{month}\\{day}\\{hour}\\no_time.xlsx'
    path4 =f'{MEDIA_ROOT}\\uploads\\texcarta\\{year}\\{month}\\{day}\\{hour}\\no_sap_code.xlsx'
    
    df_no_sap_code =pd.DataFrame({'sap_code':sap_code_link})
    df_no_sap_code.to_excel(path4)


    df_no_time =pd.DataFrame({'artikul':nakleyka_nan})
    df_no_time.to_excel(path3)
    path2 =f'{MEDIA_ROOT}\\uploads\\texcarta\\{year}\\{month}\\{day}\\{hour}\\цикл_тайм_для_тех_карты_{day}_{month}_{year}_{hour}_{minut}.xlsx'
    df_new.to_excel(path2)
    files =[File(file =path2,filetype='simple'),]
    context ={
        'files':files,
        'section':'Техкарта',

    }

    order_id =  request.GET.get('order_id',None)

    if order_id:
        context2 ={}
        order = Order.objects.get(id = order_id)
        paths = order.paths 
        paths['status_texcarta']= 'done'
        paths['texcarta_file'] = path2
        order.work_type = 10
        order.save()
        context2['order'] = order
        paths =  order.paths
        for key,val in paths.items():
            context2[key] = val
        return render(request,'order/order_detail.html',context2)

    return render(request,'universal/generated_files.html',context)


def delete_tex(request):
    texx =[
        


          ]
    
    chartext =[]
    ids =[]
    characteristika = Characteristika.objects.all().order_by('-created_at')
    i=0
    for char in characteristika:
        text =char.sap_code + char.kratkiy_text
        if text not in chartext:
            chartext.append(text)
        else:
            ids.append(char.id)
    # print(ids)
    ch =Characteristika.objects.filter(id__in =ids)
    ch.delete()
    # print(len(ids))
    # razlovka =RazlovkaTermo.objects.all()
    # for raz in razlovka:
    #     if raz.nsap_code =='':
    #         raz.nkratkiy =''
    #         raz.save()


    
    
    # texcarta=CheckNormaBase.objects.filter(artikul__in=texx)
    # texcarta.delete()
    # texcarta=ImzoBase.objects.filter(material__in=texx)
    # texcarta.delete()
        
    return JsonResponse({'a':'b'})



def tex_delete(request):
    if request.method =='POST':
        ozmk =request.POST.get('tex',None)
        if ozmk:
            ozmks =ozmk.split()
            norma_base = ImzoBase.objects.filter(material__in =ozmks)
            norma_base.delete()
            messages.add_message(request, messages.INFO, "Texcarta arxividan ochirildi")
        return render(request,'imzo/tex_find.html')
    else:
        return render(request,'imzo/tex_find.html')

def tex_delete_org(request):
    if request.method =='POST':
        ozmk =request.POST.get('ozmk',None)
        if ozmk:
            ozmks =ozmk.split()
            norma_base = ImzoBase.objects.filter(material__in =ozmks)
            norma_base.delete()
            messages.add_message(request, messages.INFO, "Texcarta arxividan ochirildi")
        return render(request,'delete_/delete_texcart.html')
    else:
        return render(request,'delete_/delete_texcart.html')