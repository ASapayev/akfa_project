from django.shortcuts import render,redirect
from .forms import FileFormImzo
from .models import ExcelFilesImzo,ImzoBase
from config.settings import MEDIA_ROOT
import pandas as pd
from .BAZA import BAZA
import os
from .utils import create_folder
    
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
    files = ExcelFilesImzo.objects.filter(generated =False)
    context ={'files':files}
    return render(request,'imzo/file_list.html',context)

def lenght_generate_imzo(request,id):
    file = ExcelFilesImzo.objects.get(id=id).file
    file_path =f'{MEDIA_ROOT}\\{file}'
    df =pd.read_excel(file_path,'BAZA')
    df['Дупликат']='No'
    df =df.astype(str)
    counter = 0
    for key,row in df.iterrows():
        if not ImzoBase.objects.filter(material = row['МАТЕРИАЛ'],kratkiytekst = row['КРАТКИЙ ТЕКСТ']).exists():
            if '-7' in row['МАТЕРИАЛ'] or '-K' in row['МАТЕРИАЛ'] or '-N' in row['МАТЕРИАЛ'] or '-S' in row['МАТЕРИАЛ']:
                counter +=2
            elif '-P' in row['МАТЕРИАЛ']:
                counter +=8
            elif '-Z' in row['МАТЕРИАЛ']:
                counter +=4
            elif '-E' in row['МАТЕРИАЛ']:
                counter +=3
            ImzoBase(material = row['МАТЕРИАЛ'],kratkiytekst = row['КРАТКИЙ ТЕКСТ']).save()
        else:
            df['Дупликат'][key]='Yes'

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

    counter_2 = 0
    for key,row in df.iterrows():
        if row['Дупликат'] == 'No':
            if '-7' in row['МАТЕРИАЛ']:
                for i7 in range(1,3):
                    if i7 ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='1101'
                        df_new['STTAG'][counter_2] ='01012021'
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
                        df_new['LTXA1'][counter_2] =BAZA['7']['LTXA1'][0]
                        df_new['BMSCH'][counter_2] ='1000'
                        df_new['MEINH'][counter_2] =BAZA['7']['MEINH'][0]
                        df_new['VGW01'][counter_2] ='1'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['7']['ACTTYPE_01'][0]
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
                        df_new['STTAG'][counter_2] ='01012021'
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
                        df_new['BMSCH'][counter_2] ='1000'
                        df_new['MEINH'][counter_2] =BAZA['K']['MEINH'][0]
                        df_new['VGW01'][counter_2] ='1'
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
                        df_new['STTAG'][counter_2] ='01012021'
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
                        df_new['BMSCH'][counter_2] ='1000'
                        df_new['MEINH'][counter_2] =BAZA['N']['MEINH'][0]
                        df_new['VGW01'][counter_2] ='1'
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
                        df_new['STTAG'][counter_2] ='01012021'
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
                        df_new['BMSCH'][counter_2] ='1000'
                        df_new['MEINH'][counter_2] =BAZA['S']['MEINH'][0]
                        df_new['VGW01'][counter_2] ='1'
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
                        df_new['STTAG'][counter_2] ='01012021'
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
                        df_new['BMSCH'][counter_2] ='1000'
                        df_new['MEINH'][counter_2] =BAZA['E']['MEINH'][0]
                        df_new['VGW01'][counter_2] ='1'
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
                        df_new['BMSCH'][counter_2] ='1000'
                        df_new['MEINH'][counter_2] =BAZA['E']['MEINH'][1]
                        df_new['VGW01'][counter_2] ='1'
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
                        df_new['STTAG'][counter_2] ='01012021'
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
                        df_new['BMSCH'][counter_2] ='1000'
                        df_new['MEINH'][counter_2] =BAZA['Z']['MEINH'][0]
                        df_new['VGW01'][counter_2] ='1'
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
                        df_new['BMSCH'][counter_2] ='1000'
                        df_new['MEINH'][counter_2] =BAZA['Z']['MEINH'][1]
                        df_new['VGW01'][counter_2] ='1'
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
                        df_new['BMSCH'][counter_2] ='1000'
                        df_new['MEINH'][counter_2] =BAZA['Z']['MEINH'][2]
                        df_new['VGW01'][counter_2] ='1'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] =BAZA['Z']['ACTTYPE_01'][2]
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = row['UMREZ']
                        df_new['UMREN'][counter_2] = row['UMREN']
                        df_new['USR00'][counter_2] = row['USR00']
                        df_new['USR01'][counter_2] = row['USR01']
                    counter_2 +=1
            elif '-P' in row['МАТЕРИАЛ']:
                for p in range(1,5):
                    if p ==1:
                        for i in range(1,3):
                            if i ==1:
                                df_new['ID'][counter_2] ='1'
                                df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                df_new['WERKS'][counter_2] ='1101'
                                df_new['STTAG'][counter_2] ='01012021'
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
                                df_new['BMSCH'][counter_2] ='1000'
                                df_new['MEINH'][counter_2] =BAZA['P1']['MEINH'][0]
                                df_new['VGW01'][counter_2] ='1'
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
                                df_new['STTAG'][counter_2] ='01012021'
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
                                df_new['BMSCH'][counter_2] ='1000'
                                df_new['MEINH'][counter_2] =BAZA['P2']['MEINH'][0]
                                df_new['VGW01'][counter_2] ='1'
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
                                df_new['STTAG'][counter_2] ='01012021'
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
                                df_new['BMSCH'][counter_2] ='1000'
                                df_new['MEINH'][counter_2] =BAZA['P3']['MEINH'][0]
                                df_new['VGW01'][counter_2] ='1'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P3']['ACTTYPE_01'][0]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] = row['USR01']
                            counter_2 +=1
                    elif p == 4:
                        for i in range(1,3):
                            if i ==1:
                                df_new['ID'][counter_2] ='1'
                                df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                df_new['WERKS'][counter_2] ='1101'
                                df_new['STTAG'][counter_2] ='01012021'
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
                                df_new['BMSCH'][counter_2] ='1000'
                                df_new['MEINH'][counter_2] =BAZA['P4']['MEINH'][0]
                                df_new['VGW01'][counter_2] ='1'
                                df_new['VGE01'][counter_2] ='STD'
                                df_new['ACTTYPE_01'][counter_2] =BAZA['P4']['ACTTYPE_01'][0]
                                df_new['CKSELKZ'][counter_2] ='X'
                                df_new['UMREZ'][counter_2] = row['UMREZ']
                                df_new['UMREN'][counter_2] = row['UMREN']
                                df_new['USR00'][counter_2] = row['USR00']
                                df_new['USR01'][counter_2] = row['USR01']
                            counter_2 +=1

    del df_new["counter"]
    print(df_new)
    print(df)
    from datetime import datetime
    now = datetime.now()
    s2 = now.strftime("%d-%m-%Y__%H-%M-%S")
    
    parent_dir = f'{MEDIA_ROOT}\\uploads\\imzo\\{s2}\\'
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads\\imzo',s2)
        
    
    path =f'{MEDIA_ROOT}\\uploads\\imzo\\{s2}\\duplicate.xlsx'
    df.to_excel(path)
    
    path2 =f'{MEDIA_ROOT}\\uploads\\imzo\\{s2}\\generated_data.xlsx'
    df_new.to_excel(path2)
    return redirect('abduvali')

