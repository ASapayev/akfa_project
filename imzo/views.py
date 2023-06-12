from django.shortcuts import render,redirect
from .forms import FileFormImzo
from .models import ExcelFilesImzo,ImzoBase,TexCartaTime
from config.settings import MEDIA_ROOT
import pandas as pd
from .BAZA import BAZA
from aluminiy.models import ArtikulComponent
import os
from .utils import create_folder
from django.http import JsonResponse
from django.db.models import Q
from norma.models import Accessuar,CheckNormaBase
    
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

def imzo_file(request):
    files = ExcelFilesImzo.objects.filter(generated =False).order_by('-created_at')
    context ={'files':files}
    return render(request,'imzo/file_list.html',context)


def texcartaupload(request):
    
    df = pd.read_excel('C:\\OSPanel\\domains\\БазаTexcarta.xlsx','Лист1')
    df =df.astype(str)
    
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
     
            ).save()
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
            if ImzoBase.objects().filter(material = row['МАТЕРИАЛ'],kratkiytekst = row['КРАТКИЙ ТЕКСТ']).exists():
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
                        nak = '11111'
                        nakleyka_nan.append(lenghtht)
                else:
                    nak='11111'
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
                                df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
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
                            counter_2 +=1
                    elif p == 2:
                        for i in range(1,3):
                            if i ==1:
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
                            counter_2 +=1
                    elif p == 3:
                        for i in range(1,3):
                            if i ==1:
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
                            counter_2 +=1
                    elif p == 4:
                        for i in range(1,4):
                            if i ==1:
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
                            counter_2 +=1
                    elif p == 5:
                        for i in range(1,4):
                            if i ==1:
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
                            counter_2 +=1
                    elif p == 6:
                        for i in range(1,4):
                            if i ==1:
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
                            counter_2 +=1
    
            ImzoBase(material = row['МАТЕРИАЛ'],kratkiytekst = row['КРАТКИЙ ТЕКСТ']).save()
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
                 
            
    create_folder(f'{MEDIA_ROOT}\\uploads\\','texcarta')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta\\{year}\\{month}\\{day}\\',hour)
    
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
    return redirect('abduvali')


def delete_tex(request):
    texx =[
        'AXC40.A0160-7045',
    'AXC40.A0160-7046'
    'AXC40.A0160-7047'
    'CDBA0720-7003'
    'CDBA0720-Z003'
    'CDBA1030-7001'
    'CDBA1030-Z001'
    'CDBA1167-7001'
    'CDBA1167-P001'
    'CDBA1167-Z001'
    'CDBA1179-7001'
    'CDBA1179-P001'
    'CDBA1193-7001'
    'CDBA1193-7002'
    'CDBA1193-Z001'
    'CDBA1193-Z002'
    'CDBA1198-7001'
    'CDBA1198-Z001'
    'CDBA1200-7001'
    'CDBA1200-Z001'
    'CDBA1202-7001'
    'CDBA1202-Z001'
    'CDBA1211-7001'
    'CDBA1211-Z001'
    'CL020011-Z004'
    'CL021148-Z002'
    'CLX02.W0148-7002'
    'CLX02.W0236-7004'
    'FS480002-P004'
    'FS480007-P026'
    'FS480007-P027'
    'FS480007-Z009'
    'FS480034-P059'
    'FS500009-P010'
    'FS500009-Z002'
    'FSC45.A0005-7005'
    'FSC45.A0005-7006'
    'FSC45.A0007-7004'
    'FSC45.A0007-7016'
    'FST48.AF001-7016'
    'FST48.AR005-7005'
    'FST48.CP001-7020'
    'FST48.S0004-7021'
    'FST48.S0007-7050'
    'FST48.S0007-7051'
    'FST50.S0013-7012'
    'FW500007-N038'
    'FW500007-N039'
    'FW500007-P023'
    'FW500008-7001'
    'FW500008-7002'
    'FW500008-7003'
    'FW500008-7004'
    'FW500008-7005'
    'FW500008-7006'
    'FW500008-P001'
    'FW500008-P002'
    'FW500008-P003'
    'FW500008-P004'
    'FW500008-P005'
    'FW500008-Z001'
    'FW500008-Z002'
    'FW500009-P024'
    'FW500019-P003'
    'FW500019-S001'
    'FWC50.F0001-7003'
    'FWT50.F0001-7018'
    'FWT50.F0002-7001'
    'FWT50.F0002-K001'
    'FWT50.V0001-7034'
    'GF550001-P002'
    'GF550004-P001'
    'GF550005-P002'
    'GFC55.A0002-7002'
    'GFC55.A0003-7003'
    'GFC55.F0001-7003'
    'MB020434 -Z001'
    'MB020434 -Z002'
    'MB700647-Z001'
    'MBC02.A0434-7001'
    'MBC02.A0434-7002'
    'MBC70.CS647-7001'
    'MSC20.F0022-7006'
    'MSC20.F0550-7003'
    'PDC77.A0337-7013'
    'PDC77.A0337-7014'
    'PDC77.A0337-7015'
    'PDC77.A0337-7016'
    'PDC77.A0337-7017'
    'RLC58.V0004-7049'
    'RLC58.V0004-7050'
    'RLC58.V0004-7051'
    'RLC58.V0004-7052'
    'RLC58.V0004-7053'
    'RLC58.V0004-7054'
    'RLC58.V0004-7055'
    'RLC58.V0004-7056'
    'RLC58.V0004-7057'
    'RLC58.V0004-7058'
    'RLC58.V0004-7059'
    'RLC58.V0004-7060'
    'RLC58.V0004-7061'
    'RLC58.V0004-7062'
    'RLC58.V0004-7063'
    'RLC58.V0004-7064'
    'RLC58.V0004-7065'
    'RLC58.V0004-7066'
    'RLC58.V0004-7067'
    'RLC58.V0004-7068'
    'RLC58.V0004-7069'
    'RLC58.V0004-7070'
    'RLC58.V0004-7071'
    'RLC58.V0004-7072'
    'RLC58.V0004-7073'
    'RLC58.V0004-7074'
    'RLC58.V0004-7075'
    'RLC58.V0004-7076'
    'RLC58.V0004-7077'
    'RLC58.V0004-7078'
    'RLC58.V0004-7079'
    'RLC58.V0004-7080'
    'RLC58.V0004-7081'
    'RLC58.V0004-7082'
    'RLC58.V0004-7083'
    'SL650003-N007'
    'SL650003-P029'
    'SL650004-N007'
    'SL650004-P026'
    'SL650011-N002'
    'SL650011-P016'
    'SL650012-P018'
    'SL650013-P018'
    'SL650015-P020'
    'SL650015-P026'
    'SL650016-P021'
    'SL650016-P026'
    'SL650017-P022'
    'SL650017-P026'
    'SL650025-N009'
    'SL650025-N018'
    'SL650025-P025'
    'SL650026-N009'
    'SL650026-N018'
    'SL650026-P025'
    'SL650027-P010'
    'SL650027-P020'
    'SL650033-P007'
    'SL650034-N001'
    'SL650034-N002'
    'SL650034-N003'
    'SL650034-N004'
    'SL650034-N005'
    'SL650034-N006'
    'SL650034-N007'
    'SL650034-N008'
    'SL650034-N009'
    'SL650034-N010'
    'SL650034-N011'
    'SL650034-P007'
    'SL650035-P007'
    'SLT65.A0003-7049'
    'SLT65.A0003-7062'
    'SLT65.A0003-7063'
    'SLT65.A0003-7065'
    'SLT65.A0003-7066'
    'SLT65.A0004-7015'
    'SLT65.A0004-7016'
    'SLT65.A0004-7025'
    'SLT65.A0004-7030'
    'SLT65.A0004-7039'
    'SLT65.A0004-7042'
    'SLT65.A0004-7045'
    'SLT65.A0004-7046'
    'SLT65.A0004-7047'
    'SLT65.A0004-7056'
    'SLT65.A0005-7023'
    'SLT65.A0005-7025'
    'SLT65.A0005-7039'
    'SLT65.A0005-7040'
    'SLT65.A0005-7041'
    'SLT65.A0005-7042'
    'SLT65.A0005-7043'
    'SLT65.A0005-7044'
    'SLT65.A0005-7045'
    'SLT65.A0006-7050'
    'SLT65.A0006-7051'
    'SLT65.A0008-7028'
    'SLT65.A0008-7029'
    'SLT65.A0008-7030'
    'SLT65.A0008-K021'
    'SLT65.F0001-7013'
    'SLT65.F0001-7027'
    'SLT65.F0001-7033'
    'SLT65.F0001-7055'
    'SLT65.F0001-7056'
    'SLT65.F0001-K042'
    'SLT65.F0002-7002'
    'SLT65.F0002-7007'
    'SLT65.F0002-7028'
    'SLT65.F0002-7029'
    'SLT65.F0002-K002'
    'SLT65.F0002-K017'
    'SLT65.V0001-7013'
    'SLT65.V0001-7017'
    'SLT65.V0001-7038'
    'SLT65.V0001-7039'
    'SLT65.V0001-7058'
    'SLT65.V0001-7060'
    'SLT65.V0001-7061'
    'SLT65.V0001-K013'
    'SLT65.V0001-K024'
    'SS230417-Z001'
    'SS230418-Z001'
    'SS231014-P001'
    'SS231014-P002'
    'SS231014-P003'
    'SS231014-P004'
    'SS231014-P005'
    'SS231014-P006'
    'SS231073-P001'
    'SS231073-P002'
    'SS231073-P003'
    'SS231073-P004'
    'SS231073-P005'
    'SS231073-P006'
    'SSC23.A1014-7002'
    'SSC23.A1014-7003'
    'SSC23.A1014-7004'
    'SSC23.A1014-7005'
    'SSC23.A1014-7006'
    'SSC23.A1073-7002'
    'SSC23.A1073-7003'
    'SSC23.A1073-7004'
    'SSC23.A1073-7005'
    'SSC23.A1073-7006'
    'SSC23.F0011-7001'
    'SSC23.F0011-7002'
    'SSC23.LS005-7001'
    'SSC23.LS005-7002'
    'STAK0010-7001'
    'STAK0010-Z001'
    'STAK0011-7001'
    'STAK0011-Z001'
    'STAK1031-7003'
    'STAK1031-7004'
    'STAK1031-7005'
    'STAK1031-7006'
    'STBK1063-7001'
    'STBK1063-Z001'
    'WD430101-P009'
    'WD450104-P022'
    'WD450104-Z004'
    'WD450116-P008'
    'WD450116-P024'
    'WD450179-P008'
    'WD450181-P001'
    'WD450182-P036'
    'WD450183-S004'
    'WD450350-Z001'
    'WD450352-Z001'
    'WD450402-Z001'
    'WD450402-Z002'
    'WD450403-P005'
    'WD450403-P007'
    'WD450403-Z001'
    'WD450403-Z002'
    'WD450403-Z003'
    'WD450440-Z001'
    'WD450442-Z001'
    'WD450840-Z001'
    'WD450842-Z001'
    'WD470001-P003'
    'WD470002-P009'
    'WD470003-P026'
    'WD470004-P021'
    'WD470005-P019'
    'WD470006-P009'
    'WD470007-P021'
    'WD470008-P016'
    'WD470009-P006'
    'WD470010-P005'
    'WD470080-P005'
    'WD470081-P025'
    'WD470082-P026'
    'WD470083-P004'
    'WD470083-P025'
    'WD470083-P029'
    'WD470084-P013'
    'WD470085-P020'
    'WD470085-P025'
    'WD470086-P026'
    'WD470087-P013'
    'WD470088-P009'
    'WD470097-P016'
    'WD470098-P005'
    'WD470099-P006'
    'WD470100-P011'
    'WD470105-P007'
    'WD470105-P015'
    'WD470110-P023'
    'WD478060-Z001'
    'WD550038-P012'
    'WD550039-P019'
    'WD550040-P021'
    'WD550049-P025'
    'WD550050-P025'
    'WD550055-P012'
    'WD570003-N009'
    'WD570003-N010'
    'WD570004-N010'
    'WD570004-N011'
    'WD570005-N007'
    'WD570006-N007'
    'WD570017-N006'
    'WD570017-N007'
    'WD570018-N007'
    'WD570018-N008'
    'WD570019-N006'
    'WD570020-N006'
    'WD570031-N010'
    'WD570031-N011'
    'WD570032-N010'
    'WD570032-N011'
    'WD570033-Z001'
    'WD570078-P004'
    'WD570086-N007'
    'WD570086-N008'
    'WD570086-N009'
    'WD570087-N007'
    'WD570087-N008'
    'WD570087-N009'
    'WD570089-N001'
    'WD570089-N002'
    'WD570089-N003'
    'WD570089-N004'
    'WD570089-N005'
    'WD570099-N001'
    'WD570099-N002'
    'WD570099-P001'
    'WD570099-P002'
    'WD570099-Z001'
    'WD650001-P023'
    'WD650001-P029'
    'WD650002-P026'
    'WD650002-P032'
    'WD650003-N001'
    'WD650003-N002'
    'WD650003-N003'
    'WD650003-N004'
    'WD650003-N005'
    'WD650003-N006'
    'WD650003-N007'
    'WD650003-N008'
    'WD650003-N009'
    'WD650003-N010'
    'WD650003-N011'
    'WD650003-P012'
    'WD650004-P012'
    'WD650005-P013'
    'WD650006-N005'
    'WD650006-N006'
    'WD650006-N007'
    'WD650006-N008'
    'WD650006-N009'
    'WD650006-N010'
    'WD650006-N011'
    'WD650006-N012'
    'WD650006-N013'
    'WD650006-N014'
    'WD650006-N015'
    'WD650006-N016'
    'WD650006-N017'
    'WD650006-N018'
    'WD650006-N019'
    'WD650006-N020'
    'WD650006-P013'
    'WD650007-N030'
    'WD650007-P003'
    'WD650007-P019'
    'WD650007-P024'
    'WD650008-N047'
    'WD650008-P006'
    'WD650008-P028'
    'WD650008-P033'
    'WD650008-P039'
    'WD650009-P023'
    'WD650010-N035'
    'WD650010-N037'
    'WD650010-P024'
    'WD650013-N011'
    'WD650013-P011'
    'WD650014-N011'
    'WD650014-P011'
    'WD650015-P020'
    'WD650016-P021'
    'WD650017-P012'
    'WD650018-P018'
    'WD650018-P024'
    'WD650019-P018'
    'WD650019-P024'
    'WD650020-P029'
    'WD650021-P029'
    'WD650022-P012'
    'WD650023-P013'
    'WD650024-N040'
    'WD650024-P028'
    'WD650024-S003'
    'WD650025-N034'
    'WD650025-N039'
    'WD650025-P014'
    'WD650025-P020'
    'WD650025-S004'
    'WD650026-P031'
    'WD650027-P012'
    'WD650028-P018'
    'WD650029-P006'
    'WD650029-P016'
    'WD650031-P013'
    'WD650031-P023'
    'WD650032-P019'
    'WD650033-N013'
    'WD650033-N019'
    'WD650033-N020'
    'WD650033-N021'
    'WD650033-N022'
    'WD650033-N023'
    'WD650033-N024'
    'WD650033-N025'
    'WD650033-N026'
    'WD650033-N027'
    'WD650033-N028'
    'WD650033-P019'
    'WD650034-P024'
    'WD650035-P023'
    'WD650036-P022'
    'WD650037-N010'
    'WD650037-N026'
    'WD650037-N027'
    'WD650037-N028'
    'WD650037-N029'
    'WD650037-N030'
    'WD650037-N031'
    'WD650037-N032'
    'WD650037-N033'
    'WD650037-N034'
    'WD650037-N035'
    'WD650037-P025'
    'WD650038-P030'
    'WD650039-P026'
    'WD650040-P024'
    'WD650045-P002'
    'WD650045-Z001'
    'WD650047-P012'
    'WD650049-P022'
    'WD650050-P017'
    'WD650053-P018'
    'WD650054-P024'
    'WD650055-P017'
    'WD650056-P012'
    'WD650057-P012'
    'WD650058-P012'
    'WD670003-N004'
    'WD670003-N005'
    'WD670003-P004'
    'WD670003-Z001'
    'WD670039-P028'
    'WD700001-P022'
    'WD700002-P022'
    'WD700003-N001'
    'WD700003-N002'
    'WD700003-N003'
    'WD700003-N004'
    'WD700003-N005'
    'WD700003-N006'
    'WD700003-N007'
    'WD700003-N008'
    'WD700003-N009'
    'WD700003-N010'
    'WD700003-N011'
    'WD700003-N012'
    'WD700003-N013'
    'WD700003-N014'
    'WD700007-P009'
    'WD700007-P027'
    'WD700009-N022'
    'WD700015-N043'
    'WD700016-N039'
    'WD700024-N039'
    'WD700029-N003'
    'WD700029-N004'
    'WD700029-N005'
    'WD700029-N006'
    'WD700029-N007'
    'WD700029-N008'
    'WD700029-N009'
    'WD700029-N010'
    'WD700029-N011'
    'WD700029-N012'
    'WD700029-N013'
    'WD700029-N014'
    'WD700029-N015'
    'WD700029-N016'
    'WD700033-N002'
    'WD700033-N003'
    'WD700033-N004'
    'WD700033-N005'
    'WD700033-N006'
    'WD700033-N007'
    'WD700033-N008'
    'WD700033-N009'
    'WD700033-N010'
    'WD700033-N011'
    'WD700033-N012'
    'WD700033-N013'
    'WD700033-N014'
    'WD700033-N015'
    'WD700039-N027'
    'WD700039-P019'
    'WD700040-N027'
    'WD700040-P019'
    'WD700062-P002'
    'WD700062-Z003'
    'WD700063-Z001'
    'WD700071-P001'
    'WD700071-Z001'
    'WD700079-P023'
    'WD700079-P024'
    'WD780001-N038'
    'WD780002-N038'
    'WD780004-N011'
    'WD780004-N020'
    'WD780004-N026'
    'WD780004-N039'
    'WD780004-P003'
    'WD780004-P009'
    'WD780004-S003'
    'WD780005-N020'
    'WD780005-N026'
    'WD780005-N039'
    'WD780005-P009'
    'WD780005-S003'
    'WD780010-N013'
    'WD780010-N023'
    'WD780010-N024'
    'WD780010-N025'
    'WD780010-N026'
    'WD780010-N027'
    'WD780010-N028'
    'WD780010-N029'
    'WD780010-N030'
    'WD780011-N032'
    'WD780013-N033'
    'WD780013-P012'
    'WD780014-N040'
    'WD780014-P017'
    'WD780036-P012'
    'WD780037-P012'
    'WD780039-N010'
    'WD780039-N011'
    'WD780039-N012'
    'WD780039-N013'
    'WD780039-N014'
    'WD780039-N015'
    'WD780039-N016'
    'WD780039-N017'
    'WD780040-P006'
    'WD780045-P012'
    'WD780046-P014'
    'WD780058-N001'
    'WD780058-N002'
    'WD780058-N003'
    'WD780058-N004'
    'WD780058-N005'
    'WD780058-N006'
    'WD780058-N007'
    'WD780058-N008'
    'WD980003-N011'
    'WD980003-N012'
    'WD980003-P008'
    'WD980004-N010'
    'WD980007-N004'
    'WD980008-N004'
    'WD980009-N004'
    'WD980009-N012'
    'WD980009-N013'
    'WD980009-P006'
    'WD980010-N002'
    'WD980010-N009'
    'WD980013-P006'
    'WD980026-N012'
    'WD980027-N012'
    'WD980028-P005'
    'WD980034-N008'
    'WD980034-N009'
    'WD980034-N010'
    'WD980034-N011'
    'WD980034-N012'
    'WD980034-N013'
    'WD980034-N014'
    'WD980034-N015'
    'WD980034-P006'
    'WD980045-N002'
    'WD980045-N003'
    'WD980045-P002'
    'WD980045-Z001'
    'WD980046-N002'
    'WD980046-N003'
    'WD980046-P002'
    'WD980046-Z001'
    'WD980048-P002'
    'WD980048-Z001'
    'WD980055-N013'
    'WD980055-P005'
    'WD980057-N011'
    'WD980057-P006'
    'WD980059-P006'
    'WD980069-N007'
    'WD980069-N015'
    'WD980069-N016'
    'WD980069-P007'
    'WD980069-Z002'
    'WD980070-N007'
    'WD980070-N015'
    'WD980070-N016'
    'WD980070-P007'
    'WD980070-Z002'
    'WD980074-N010'
    'WD980074-N011'
    'WD980074-P007'
    'WD980095-N012'
    'WD980095-P004'
    'WDC43.A0001-7019'
    'WDC43.A0001-7020'
    'WDC43.F0003-7010'
    'WDC43.F0004-7010'
    'WDC43.V0001-7014'
    'WDC43.V0001-7015'
    'WDC43.V0001-7022'
    'WDC43.V0001-7023'
    'WDC43.V0002-7010'
    'WDC43.V0002-7011'
    'WDC43.V0002-7012'
    'WDC45.A0002-7035'
    'WDC45.A0002-7046'
    'WDC45.A0002-7050'
    'WDC45.AC002-7001'
    'WDC45.F0001-7026'
    'WDC45.F0002-7034'
    'WDC45.F0002-7043'
    'WDC45.F0002-7046'
    'WDC45.F0002-7098'
    'WDC45.F0002-7099'
    'WDC45.F0002-7100'
    'WDC45.F0002-7101'
    'WDC45.F0002-7102'
    'WDC45.F0002-7103'
    'WDC45.F0004-7005'
    'WDC45.F0004-7011'
    'WDC45.G0001-7037'
    'WDC45.G0001-7048'
    'WDC45.G0001-7049'
    'WDC45.G0001-7050'
    'WDC45.G0001-7051'
    'WDC45.G0002-7050'
    'WDC45.G0002-7051'
    'WDC45.G0002-7052'
    'WDC45.G0002-7053'
    'WDC45.G0002-7054'
    'WDC45.G0002-7055'
    'WDC45.HE003-7001'
    'WDC45.HG001-7001'
    'WDC45.HG002-7001'
    'WDC45.HG005-7001'
    'WDC45.HG006-7001'
    'WDC45.L0001-7059'
    'WDC45.L0001-7085'
    'WDC45.L0001-7086'
    'WDC45.L0001-7087'
    'WDC45.L0001-7088'
    'WDC45.L0001-7090'
    'WDC45.L0001-7091'
    'WDC45.L0001-7092'
    'WDC45.L0001-7093'
    'WDC45.L0001-7109'
    'WDC45.L0002-7025'
    'WDC45.L0002-7096'
    'WDC45.L0002-7097'
    'WDC45.L0002-7101'
    'WDC45.L0002-7102'
    'WDC45.L0003-7061'
    'WDC45.L0003-7062'
    'WDC45.L0003-7063'
    'WDC45.M0001-7024'
    'WDC45.M0001-7034'
    'WDC45.M0001-7035'
    'WDC45.M0002-7003',
    'WDC45.M0002-7105',
    'WDC45.M0002-7106',
    'WDC45.M0002-7107',
    'WDC45.M0002-7108',
    'WDC45.M0002-7109',
    'WDC45.M0002-7110',
    'WDC45.V0001-7033',
    'WDC45.V0001-7034',
    'WDC45.V0002-7001',
    'WDC45.V0002-7090',
    'WDC45.V0002-7091',
    'WDC45.V0002-7092',
    'WDC45.V0002-7093',
    'WDC45.V0002-7094',
    'WDC47.A0001-7018',
    'WDC47.A0001-7023',
    'WDC47.A0001-7030',
    'WDC47.A0001-7033',
    'WDC47.A0001-7034',
    'WDC47.A0002-7003',
    'WDC47.A0002-7004',
    'WDC47.A0002-7007',
    'WDC47.A0004-7047',
    'WDC47.A0004-7048',
    'WDC47.A0004-7066',
    'WDC47.A0004-7069',
    'WDC47.A0004-7070',
    'WDC47.A0005-7015',
    'WDC47.A0005-7020',
    'WDC47.A0005-7021',
    'WDC47.A0005-7026',
    'WDC47.A0005-7027',
    'WDC47.A0005-7028',
    'WDC47.A0005-7045',
    'WDC47.A0005-7046',
    'WDC47.A0006-7016',
    'WDC47.A0006-7019',
    'WDC47.A0006-7020',
    'WDC47.A0006-7021',
    'WDC47.A0006-7022',
    'WDC47.A0006-7024',
    'WDC47.A0006-7025',
    'WDC47.A0006-7028',
    'WDC47.A0006-7039',
    'WDC47.A0006-7040',
    'WDC47.A0007-7009',
    'WDC47.A0007-7011',
    'WDC47.A0007-7012',
    'WDC47.A0007-7025',
    'WDC47.A0007-7028',
    'WDC47.A0007-7029',
    'WDC47.A0007-7030',
    'WDC47.A0008-7016',
    'WDC47.A0008-7018',
    'WDC47.A0008-7022',
    'WDC47.A0008-7030',
    'WDC47.A0008-7033',
    'WDC47.A0008-7034',
    'WDC47.A0008-7035',
    'WDC47.A0009-7002',
    'WDC47.A0009-7004',
    'WDC47.A0009-7020',
    'WDC47.F0002-7004',
    'WDC47.F0002-7007',
    'WDC47.F0002-7047',
    'WDC47.F0002-7056',
    'WDC47.F0002-7085',
    'WDC47.F0002-7087',
    'WDC47.F0002-7088',
    'WDC47.F0004-7012',
    'WDC47.F0004-7017',
    'WDC47.F0004-7020',
    'WDC47.F0004-7021',
    'WDC47.G0001-7002',
    'WDC47.G0001-7004',
    'WDC47.G0001-7006',
    'WDC47.G0001-7007',
    'WDC47.G0002-7020',
    'WDC47.G0002-7021',
    'WDC47.G0002-7027',
    'WDC47.G0002-7036',
    'WDC47.G0002-7050',
    'WDC47.G0002-7052',
    'WDC47.G0002-7053',
    'WDC47.G0002-7058',
    'WDC47.G0003-7013',
    'WDC47.G0003-7015',
    'WDC47.G0003-7018',
    'WDC47.G0003-7019',
    'WDC47.G0004-7001',
    'WDC47.G0004-7014',
    'WDC47.G0004-7015',
    'WDC47.G0004-7017',
    'WDC47.G0004-7018',
    'WDC47.G0004-7037',
    'WDC47.G0004-7039',
    'WDC47.G0004-7040',
    'WDC47.GR002-7018',
    'WDC47.GR002-7019',
    'WDC47.GR002-7021',
    'WDC47.GR002-7022',
    'WDC47.GR002-7039',
    'WDC47.GR002-7040',
    'WDC47.GR003-7002',
    'WDC47.GR003-7004',
    'WDC47.GR003-7006',
    'WDC47.GR003-7007',
    'WDC47.GR004-7008',
    'WDC47.GR004-7009',
    'WDC47.GR004-7011',
    'WDC47.GR004-7018',
    'WDC47.GR004-7029',
    'WDC47.GR004-7030',
    'WDC47.HG005-7001',
    'WDC47.M0002-7008',
    'WDC47.M0002-7050',
    'WDC47.M0002-7051',
    'WDC47.M0002-7053',
    'WDC47.M0002-7086',
    'WDC47.M0002-7087',
    'WDC47.M0003-7018',
    'WDC47.M0003-7019',
    'WDC47.M0003-7020',
    'WDC47.V0002-7042',
    'WDC47.V0002-7043',
    'WDC47.V0002-7045',
    'WDC47.V0002-7067',
    'WDC47.V0002-7070',
    'WDC47.V0002-7071',
    'WDC47.V0002-7072',
    'WDC47.V0003-7048',
    'WDC47.V0003-7075',
    'WDC47.V0003-7076',
    'WDC47.V0003-7078',
    'WDC47.V0003-7079',
    'WDC47.V0004-7043',
    'WDC47.V0004-7044',
    'WDC47.V0004-7046',
    'WDC47.V0004-7073',
    'WDC47.V0004-7074',
    'WDT55.A0007-7030',
    'WDT55.A0007-7031',
    'WDT55.A0008-7033',
    'WDT55.A0008-7034',
    'WDT55.G0020-7048',
    'WDT55.GR020-7041',
    'WDT55.GR020-7042',
    'WDT57.A0010-7014',
    'WDT57.A0010-7015',
    'WDT57.A0010-7016',
    'WDT57.A0010-7023',
    'WDT57.A0010-7024',
    'WDT57.A0010-7025',
    'WDT57.A0010-7026',
    'WDT57.A0010-7027',
    'WDT57.A0010-7028',
    'WDT57.A0010-7029',
    'WDT57.A0013-7018',
    'WDT57.A0013-7019',
    'WDT57.A0013-7020',
    'WDT57.A0013-7021',
    'WDT57.A0013-7027',
    'WDT57.A0013-7047',
    'WDT57.A0013-K009',
    'WDT57.A0013-K010',
    'WDT57.A0013-K011',
    'WDT57.A0013-K012',
    'WDT57.F0002-7020',
    'WDT57.F0002-7024',
    'WDT57.F0002-7025',
    'WDT57.F0002-7026',
    'WDT57.F0002-K013',
    'WDT57.F0002-K014',
    'WDT57.F0003-7017',
    'WDT57.F0003-7018',
    'WDT57.F0003-7019',
    'WDT57.F0003-7020',
    'WDT57.F0003-K011',
    'WDT57.M0005-7019',
    'WDT57.M0005-7020',
    'WDT57.M0005-7021',
    'WDT57.M0005-7026',
    'WDT57.M0005-7027',
    'WDT57.P0001-7012',
    'WDT57.P0001-7013',
    'WDT57.P0001-7014',
    'WDT57.P0001-7015',
    'WDT57.P0001-7016',
    'WDT57.P0001-7017',
    'WDT57.P0001-7018',
    'WDT57.P0001-7019',
    'WDT57.P0001-7020',
    'WDT57.P0001-7021',
    'WDT57.V0002-7019',
    'WDT57.V0002-7023',
    'WDT57.V0002-7024',
    'WDT57.V0002-K011',
    'WDT57.V0002-K012',
    'WDT57.V0003-7017',
    'WDT57.V0003-7018',
    'WDT57.V0003-7022',
    'WDT57.V0003-7023',
    'WDT57.V0003-K011',
    'WDT57.V0007-7022',
    'WDT57.V0007-7023',
    'WDT57.V0007-7024',
    'WDT57.V0007-7025',
    'WDT57.V0007-K011',
    'WDT57.V0007-K013',
    'WDT57.V0007-K014',
    'WDT65.A0001-7089',
    'WDT65.A0001-7090',
    'WDT65.A0001-K052',
    'WDT65.A0001-K057',
    'WDT65.A0001-K063',
    'WDT65.A0003-7042',
    'WDT65.A0003-7043',
    'WDT65.A0003-K024',
    'WDT65.A0003-K026',
    'WDT65.A0004-7043',
    'WDT65.A0005-7035',
    'WDT65.A0005-7036',
    'WDT65.A0005-K018',
    'WDT65.A0005-K022',
    'WDT65.A0006-7026',
    'WDT65.A0007-7025',
    'WDT65.A0007-7027',
    'WDT65.A0007-7051',
    'WDT65.A0007-7061',
    'WDT65.F0002-7011',
    'WDT65.F0002-7033',
    'WDT65.F0002-7098',
    'WDT65.F0002-7099',
    'WDT65.F0002-7100',
    'WDT65.F0002-K011',
    'WDT65.F0002-K034',
    'WDT65.F0002-K074',
    'WDT65.F0002-K084',
    'WDT65.F0002-K086',
    'WDT65.G0021-7002',
    'WDT65.G0027-7012',
    'WDT65.G0031-7021',
    'WDT65.K0001-K039',
    'WDT65.M0002-7015',
    'WDT65.M0002-7021',
    'WDT65.M0002-K012',
    'WDT65.M0002-K014',
    'WDT65.M0003-7089',
    'WDT65.M0003-K068',
    'WDT65.M0003-K071',
    'WDT65.M0005-7006',
    'WDT65.M0005-K008',
    'WDT65.V0001-7011',
    'WDT65.V0001-K011',
    'WDT65.V0002-K066',
    'WDT65.V0002-K069',
    'WDT65.V0003-7032',
    'WDT65.V0003-7074',
    'WDT65.V0003-7075',
    'WDT65.V0003-K065',
    'WDT65.V0004-7083',
    'WDT65.V0004-K065',
    'WDT65.V0004-K069',
    'WDT67.G0005-7020',
    'WDT67.G0005-7040',
    'WDT67.G0006-7050',
    'WDT67.G0007-7005',
    'WDT67.G0009-7004',
    'WDT70.A0001-7063',
    'WDT70.A0007-7009',
    'WDT70.A0007-K009',
    'WDT70.F0002-7078',
    'WDT70.F0003-7023',
    'WDT70.F0003-7024',
    'WDT70.F0003-7026',
    'WDT70.F0003-K023',
    'WDT70.F0003-K024',
    'WDT70.F0003-K026',
    'WDT70.F0005-7001',
    'WDT70.F0005-7002',
    'WDT70.F0005-K001',
    'WDT70.F0005-K002',
    'WDT70.G0215-7015',
    'WDT70.G0215-7020',
    'WDT70.G0215-7021',
    'WDT70.G0295-7037',
    'WDT70.G0295-7060',
    'WDT70.M0002-7028',
    'WDT70.M0002-7059',
    'WDT70.M0002-7060',
    'WDT70.M0002-7061',
    'WDT70.M0002-K030',
    'WDT70.M0003-7032',
    'WDT70.M0003-7033',
    'WDT70.M0003-7034',
    'WDT70.M0003-7035',
    'WDT70.M0003-7036',
    'WDT70.M0003-7037',
    'WDT70.M0003-7038',
    'WDT70.M0003-7039',
    'WDT70.M0003-7040',
    'WDT70.M0003-K000',
    'WDT70.M0003-K035',
    'WDT70.M0003-K036',
    'WDT70.M0003-K037',
    'WDT70.V0002-7042',
    'WDT70.V0002-7067',
    'WDT70.V0002-K044',
    'WDT70.V0006-7030',
    'WDT70.V0006-7058',
    'WDT70.V0006-K031',
    'WDT70.V0007-7045',
    'WDT70.V0007-7046',
    'WDT70.V0008-7006',
    'WDT70.V0008-K005',
    'WDT78.A0001-7018',
    'WDT78.A0001-7065',
    'WDT78.A0001-K035',
    'WDT78.A0001-K040',
    'WDT78.A0001-K053',
    'WDT78.A0003-7028',
    'WDT78.A0003-K013',
    'WDT78.A0003-K016',
    'WDT78.A0004-7023',
    'WDT78.A0004-K009',
    'WDT78.A0004-K012',
    'WDT78.A0008-7009',
    'WDT78.A0008-7010',
    'WDT78.A0008-7012',
    'WDT78.A0008-7016',
    'WDT78.A0008-7040',
    'WDT78.A0009-7002',
    'WDT78.F0001-7043',
    'WDT78.F0001-7051',
    'WDT78.F0001-7056',
    'WDT78.F0001-K021',
    'WDT78.F0001-K023',
    'WDT78.F0001-K032',
    'WDT78.F0001-K035',
    'WDT78.F0001-K036',
    'WDT78.F0001-K051',
    'WDT78.F0003-7054',
    'WDT78.F0003-K029',
    'WDT78.G0002-7022',
    'WDT78.G0002-7042',
    'WDT78.G0004-7017',
    'WDT78.G0004-7042',
    'WDT78.GR002-7042',
    'WDT78.K0001-7039',
    'WDT78.K0001-7040',
    'WDT78.K0001-7041',
    'WDT78.K0001-K023',
    'WDT78.K0001-K024',
    'WDT78.M0001-7024',
    'WDT78.M0001-7063',
    'WDT78.M0001-7064',
    'WDT78.M0001-K029',
    'WDT78.M0001-K035',
    'WDT78.M0001-K046',
    'WDT78.M0005-7034',
    'WDT78.M0005-K029',
    'WDT78.V0001-7022',
    'WDT78.V0001-7056',
    'WDT78.V0001-K027',
    'WDT78.V0001-K028',
    'WDT78.V0001-K030',
    'WDT78.V0001-K043',
    'WDT78.V0004-K013',
    'WDT78.V0005-7023',
    'WDT78.V0005-7051',
    'WDT78.V0006-K006',
    'WDT78.V0006-K008',
    'WDT78.V0007-7022',
    'WDT78.V0007-K018',
    'WDT98.A0010-7002',
    'WDT98.A0010-7003',
    'WDT98.A0010-7004',
    'WDT98.F0002-7032',
    'WDT98.F0002-7033',
    'WDT98.F0002-7034',
    'WDT98.F0002-7035',
    'WDT98.F0002-K014',
    'WDT98.F0022-7030',
    'WDT98.F0022-7031',
    'WDT98.F0022-K015',
    'WDT98.F0022-K016',
    'WDT98.F0023-7011',
    'WDT98.M0004-7032',
    'WDT98.M0004-7033',
    'WDT98.M0004-7034',
    'WDT98.M0004-7035',
    'WDT98.M0004-K016',
    'WDT98.M0025-7025',
    'WDT98.M0025-K016',
    'WDT98.P0001-7005',
    'WDT98.P0001-7006',
    'WDT98.P0001-K005',
    'WDT98.P0001-K006',
    'WDT98.V0001-7018',
    'WDT98.V0001-7019',
    'WDT98.V0001-7020',
    'WDT98.V0001-7021',
    'WDT98.V0001-7022',
    'WDT98.V0001-7023',
    'WDT98.V0001-7024',
    'WDT98.V0001-K005',
    'WDT98.V0001-K008',
    'WDT98.V0002-7009',
    'WDT98.V0002-7027',
    'WDT98.V0002-K005',
    'WDT98.V0002-K012',
    'WDT98.V0009-7012',
    'WDT98.V0009-7014',
    'WDT98.V0009-7037',
    'WDT98.V0009-7038',
    'WDT98.V0009-K009',
    'WDT98.V0009-K018',
    'WDT98.V0009-K019',
    'WDT98.V0022-7028',
    'WDT98.V0022-K015',


          ]
    
    
    # texcarta=CheckNormaBase.objects.filter(material__in=texx)
    # texcarta.delete()
    texcarta=ImzoBase.objects.filter(material__in=texx)
    texcarta.delete()
        
    return JsonResponse({'a':'b'})