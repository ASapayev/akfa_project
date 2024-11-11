from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
import pandas as pd
from .forms import TexcartaMatrixFileForm,NormaMatrixFileForm
from .models import TexcartaMatrixFile,MatrixFile,MatrixBase
from config.settings import MEDIA_ROOT
from kraska.views import generate_random_string



class File:
    def __init__(self,file,id):
        self.file =file
        self.id = id


nrz_datas =[['1000004824','СТАЛЬНОЙ ПРУТОК 1,2344 Ф131 ММ'],
            ['1000004826','СТАЛЬНОЙ ПРУТОК 1,2344 Ф152 ММ'],
            ['1000004827','СТАЛЬНОЙ ПРУТОК 1,2344 Ф182 ММ'],
            ['1000004828','СТАЛЬНОЙ ПРУТОК 1,2344 Ф204 ММ'],
            ['1000004829','СТАЛЬНОЙ ПРУТОК 1,2344 Ф223 ММ'],
            ['1000004830','СТАЛЬНОЙ ПРУТОК 1,2344 Ф252 ММ'],
            ['1000004831','СТАЛЬНОЙ ПРУТОК 1,2344 Ф283 ММ'],
            ['1000004832','СТАЛЬНОЙ ПРУТОК 1,2344 Ф324 ММ'],
            ['1000004833','СТАЛЬНОЙ ПРУТОК 1,2344 Ф354 ММ'],
            ['1000004834','СТАЛЬНОЙ ПРУТОК 1,2344 Ф364 ММ'],
            ['1000004835','СТАЛЬНОЙ ПРУТОК 1,2344 Ф405 ММ'],
            ['1000004836','СТАЛЬНОЙ ПРУТОК 1,2344 Ф455 ММ'],
            ['1000004838','СТАЛЬНОЙ ПРУТОК 1,2344 Ф121 ММ']]

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','matrix','universal_user'])
def create_norma_for_matrix(request,id):
    file = MatrixFile.objects.get(id=id).file
    df_exell = pd.read_excel(f'{MEDIA_ROOT}/{file}',sheet_name='МДО')
    df_exell = df_exell.fillna('')
    df_exell =df_exell.astype(str)


    df = []


    # print(df_exell.columns)
    for key,row in df_exell.iterrows():
            df.append([
                    row['Нарезка'],row['krat2'],
                    row['Токарный участок (черновой)'],row['krat3'],
                    row['Фрезерный участок (черновой)'],row['krat4'],
                    row['Закалка (технопарк)'],row['krat5'],
                    row['Участок плоского шлифования'],row['krat6'],
                    row['Токарный участок (чистовой)'],row['krat7'],
                    row['Фрезерный участок (чистовой)'],row['krat8'],
                    row['Участок проволочной электроэрозионной обработки (EDM)'],row['krat9'],
                    row['ГП'],row['krat1']
                ])
    
    df_new =    {
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


    dubl_norma =[]
    for i in range(0,len(df)):
        for j in reversed(range(2,18,2)):
            if df[i][j] in dubl_norma or df[i][j]=='':
                continue
            else:
                dubl_norma.append(df[i][j])
            
            if j==16:
                if df[i][j-2] =='':
                    sap_code = df[i][j-4]
                    krat = df[i][j-3]
                else:
                    sap_code = df[i][j-2]
                    krat = df[i][j-1]
            else:
                sap_code = df[i][j-2]
                krat = df[i][j-1]


            df_new['ID'].append('1')
            df_new['MATNR'].append(df[i][j])
            df_new['WERKS'].append('4901')
            df_new['TEXT1'].append(df[i][j+1])
            df_new['STLAL'].append('1')
            df_new['STLAN'].append('1')
            df_new['ZTEXT'].append(df[i][j+1])
            df_new['STKTX'].append(df[i][j+1])
            df_new['BMENG'].append( '1')
            df_new['BMEIN'].append('ШТ')
            df_new['STLST'].append('1')
            df_new['POSNR'].append('')
            df_new['POSTP'].append('')
            df_new['MATNR1'].append('')
            df_new['TEXT2'].append('')
            df_new['MEINS'].append('')
            df_new['MENGE'].append('')
            df_new['DATUV'].append('01012024')
            df_new['PUSTOY'].append('')
            df_new['LGORT'].append('')
        
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
            df_new['POSNR'].append('1')
            df_new['POSTP'].append('L')
            df_new['MATNR1'].append(sap_code)
            df_new['TEXT2'].append(krat)
            df_new['MEINS'].append('1') 
            df_new['MENGE'].append('ШТ')
            df_new['DATUV'].append('')
            df_new['PUSTOY'].append('')
            df_new['LGORT'].append('PS01')

        if df[i][0] in dubl_norma:
            continue
        else:
            dubl_norma.append(df[i][0])

        df_new['ID'].append('1')
        df_new['MATNR'].append(df[i][0])
        df_new['WERKS'].append('4901')
        df_new['TEXT1'].append(df[i][1])
        df_new['STLAL'].append('1')
        df_new['STLAN'].append('1')
        df_new['ZTEXT'].append(df[i][0])
        df_new['STKTX'].append(df[i][1])
        df_new['BMENG'].append( '1')
        df_new['BMEIN'].append('ШТ')
        df_new['STLST'].append('1')
        df_new['POSNR'].append('')
        df_new['POSTP'].append('')
        df_new['MATNR1'].append('')
        df_new['TEXT2'].append('')
        df_new['MEINS'].append('')
        df_new['MENGE'].append('')
        df_new['DATUV'].append('01012024')
        df_new['PUSTOY'].append('')
        df_new['LGORT'].append('')

        nr_count = 1
        for rn in nrz_datas:
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
            df_new['POSNR'].append(f'{nr_count}')
            df_new['POSTP'].append('L')
            df_new['MATNR1'].append(rn[0])
            df_new['TEXT2'].append(rn[1])
            df_new['MEINS'].append('0,01') 
            df_new['MENGE'].append('КГ')
            df_new['DATUV'].append('')
            df_new['PUSTOY'].append('')
            df_new['LGORT'].append('PS01')
            nr_count +=1


    dff = pd.DataFrame(df_new)

    string_rand = generate_random_string()
    path2 =f'{MEDIA_ROOT}\\uploads\\matrix\\norma_matrix_{string_rand}.xlsx'
    dff.to_excel(path2,index=False)

    context ={
            'file1':path2,
            'section':'Norma',

        }

    return render(request,'norma/radiator/generated_files_texcarta.html',context)



@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','matrix','universal_user'])
def upload_razlovka_file(request):
    if request.method == 'POST':
        data = request.POST.copy()
        form = NormaMatrixFileForm(data, request.FILES)
        if form.is_valid():
            form_file = form.save()
            file = form_file
            context ={'files':[File(file=str(file.file),id=file.id),],
                'link':'/matrix/kombinirovaniy-process-matrix/',
                'section':'Генерация норма файла',
                'type':'Matrix',
                'file_type':'simple'
                }
        return render(request,'universal/file_list_norma.html',context)

    return render(request,'norma/benkam/main.html')







@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','matrix','universal_user'])
def lenght_generate_texcarta(request,id):
    file = TexcartaMatrixFile.objects.get(id=id).file
    df = pd.read_excel(f'{MEDIA_ROOT}/{file}',sheet_name='МДО')

    df =df.astype(str)
    df=df.replace('nan','')
    counter = len(df)*2

    print(df)

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
        if MatrixBase.objects.filter(sapcode = row['МАТЕРИАЛ']).exists():
            continue
        else:
            MatrixBase(sapcode =row['МАТЕРИАЛ']).save()

        
        if '-PEO' in row['МАТЕРИАЛ']:
            for i in range(1,3):
                if i ==1:
                    df_new['ID'][counter_2] ='1'
                    df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                    df_new['WERKS'][counter_2] ='4901'
                    df_new['STTAG'][counter_2] ='01012024'
                    df_new['PLNAL'][counter_2] ='1'
                    df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                    df_new['VERWE'][counter_2] ='1'
                    df_new['STATU'][counter_2] ='4'     
                    df_new['LOSVN'][counter_2] ='1'
                    df_new['LOSBS'][counter_2] ='99999999'
                elif i == 2:
                    df_new['ID'][counter_2]='2'
                    df_new['VORNR'][counter_2] ='0010'
                    df_new['ARBPL'][counter_2] ='4901EDM'
                    df_new['WERKS1'][counter_2] ='4901'
                    df_new['STEUS'][counter_2] ='ZK01'
                    df_new['LTXA1'][counter_2] ='Матрицы участок (EDM)'
                    df_new['BMSCH'][counter_2] = '1'
                    df_new['MEINH'][counter_2] ='ST'
                    df_new['VGW01'][counter_2] ='24'
                    df_new['VGE01'][counter_2] ='STD'
                    df_new['ACTTYPE_01'][counter_2] =''
                    df_new['CKSELKZ'][counter_2] ='X'
                    df_new['UMREZ'][counter_2] = '1'
                    df_new['UMREN'][counter_2] = '1'
                    df_new['USR00'][counter_2] = '1'
                    df_new['USR01'][counter_2] = '60'
                    
                
                counter_2 +=1
                    # TexcartaBase(material = row['МАТЕРИАЛ']).save()
                
                
        if '-FCI' in row['МАТЕРИАЛ']:
            for i in range(1,3):
                if i ==1:
                    df_new['ID'][counter_2] ='1'
                    df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                    df_new['WERKS'][counter_2] ='4901'
                    df_new['STTAG'][counter_2] ='01012024'
                    df_new['PLNAL'][counter_2] ='1'
                    df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                    df_new['VERWE'][counter_2] ='1'
                    df_new['STATU'][counter_2] ='4'     
                    df_new['LOSVN'][counter_2] ='1'
                    df_new['LOSBS'][counter_2] ='99999999'
                elif i == 2:
                    df_new['ID'][counter_2]='2'
                    df_new['VORNR'][counter_2] ='0010'
                    df_new['ARBPL'][counter_2] ='4901FREZ'
                    df_new['WERKS1'][counter_2] ='4901'
                    df_new['STEUS'][counter_2] ='ZK01'
                    df_new['LTXA1'][counter_2] ='Матрицы Фрезерный участок'
                    df_new['BMSCH'][counter_2] = '1'
                    df_new['MEINH'][counter_2] ='ST'
                    df_new['VGW01'][counter_2] ='24'
                    df_new['VGE01'][counter_2] ='STD'
                    df_new['ACTTYPE_01'][counter_2] =''
                    df_new['CKSELKZ'][counter_2] ='X'
                    df_new['UMREZ'][counter_2] = '1'
                    df_new['UMREN'][counter_2] = '1'
                    df_new['USR00'][counter_2] = '1'
                    df_new['USR01'][counter_2] = '60'
                    
                
                counter_2 +=1
                    # TexcartaBase(material = row['МАТЕРИАЛ']).save()
                
                
        if '-TCI' in row['МАТЕРИАЛ']:
            for i in range(1,3):
                if i ==1:
                    df_new['ID'][counter_2] ='1'
                    df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                    df_new['WERKS'][counter_2] ='4901'
                    df_new['STTAG'][counter_2] ='01012024'
                    df_new['PLNAL'][counter_2] ='1'
                    df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                    df_new['VERWE'][counter_2] ='1'
                    df_new['STATU'][counter_2] ='4'     
                    df_new['LOSVN'][counter_2] ='1'
                    df_new['LOSBS'][counter_2] ='99999999'
                elif i == 2:
                    df_new['ID'][counter_2]='2'
                    df_new['VORNR'][counter_2] ='0010'
                    df_new['ARBPL'][counter_2] ='4901TOKR'
                    df_new['WERKS1'][counter_2] ='4901'
                    df_new['STEUS'][counter_2] ='ZK01'
                    df_new['LTXA1'][counter_2] ='Матрицы Токарный Участок'
                    df_new['BMSCH'][counter_2] = '1'
                    df_new['MEINH'][counter_2] ='ST'
                    df_new['VGW01'][counter_2] ='24'
                    df_new['VGE01'][counter_2] ='STD'
                    df_new['ACTTYPE_01'][counter_2] =''
                    df_new['CKSELKZ'][counter_2] ='X'
                    df_new['UMREZ'][counter_2] = '1'
                    df_new['UMREN'][counter_2] = '1'
                    df_new['USR00'][counter_2] = '1'
                    df_new['USR01'][counter_2] = '60'
                    
                
                counter_2 +=1
                    # TexcartaBase(material = row['МАТЕРИАЛ']).save()
                
                
        if '-PSH' in row['МАТЕРИАЛ']:
            for i in range(1,3):
                if i ==1:
                    df_new['ID'][counter_2] ='1'
                    df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                    df_new['WERKS'][counter_2] ='4901'
                    df_new['STTAG'][counter_2] ='01012024'
                    df_new['PLNAL'][counter_2] ='1'
                    df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                    df_new['VERWE'][counter_2] ='1'
                    df_new['STATU'][counter_2] ='4'     
                    df_new['LOSVN'][counter_2] ='1'
                    df_new['LOSBS'][counter_2] ='99999999'
                elif i == 2:
                    df_new['ID'][counter_2]='2'
                    df_new['VORNR'][counter_2] ='0010'
                    df_new['ARBPL'][counter_2] ='4901PLSH'
                    df_new['WERKS1'][counter_2] ='4901'
                    df_new['STEUS'][counter_2] ='ZK01'
                    df_new['LTXA1'][counter_2] ='Матрицы участок плоского шлифования'
                    df_new['BMSCH'][counter_2] = '1'
                    df_new['MEINH'][counter_2] ='ST'
                    df_new['VGW01'][counter_2] ='24'
                    df_new['VGE01'][counter_2] ='STD'
                    df_new['ACTTYPE_01'][counter_2] =''
                    df_new['CKSELKZ'][counter_2] ='X'
                    df_new['UMREZ'][counter_2] = '1'
                    df_new['UMREN'][counter_2] = '1'
                    df_new['USR00'][counter_2] = '1'
                    df_new['USR01'][counter_2] = '60'
                    
                
                counter_2 +=1
                    # TexcartaBase(material = row['МАТЕРИАЛ']).save()
                
                
        if '-ZKT' in row['МАТЕРИАЛ']:
            for i in range(1,3):
                if i ==1:
                    df_new['ID'][counter_2] ='1'
                    df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                    df_new['WERKS'][counter_2] ='4901'
                    df_new['STTAG'][counter_2] ='01012024'
                    df_new['PLNAL'][counter_2] ='1'
                    df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                    df_new['VERWE'][counter_2] ='1'
                    df_new['STATU'][counter_2] ='4'     
                    df_new['LOSVN'][counter_2] ='1'
                    df_new['LOSBS'][counter_2] ='99999999'
                elif i == 2:
                    df_new['ID'][counter_2]='2'
                    df_new['VORNR'][counter_2] ='0010'
                    df_new['ARBPL'][counter_2] ='4901ZAKL'
                    df_new['WERKS1'][counter_2] ='4901'
                    df_new['STEUS'][counter_2] ='ZK01'
                    df_new['LTXA1'][counter_2] ='Матрицы участок закалки'
                    df_new['BMSCH'][counter_2] = '1'
                    df_new['MEINH'][counter_2] ='ST'
                    df_new['VGW01'][counter_2] ='24'
                    df_new['VGE01'][counter_2] ='STD'
                    df_new['ACTTYPE_01'][counter_2] =''
                    df_new['CKSELKZ'][counter_2] ='X'
                    df_new['UMREZ'][counter_2] = '1'
                    df_new['UMREN'][counter_2] = '1'
                    df_new['USR00'][counter_2] = '1'
                    df_new['USR01'][counter_2] = '60'
                    
                
                counter_2 +=1
                    # TexcartaBase(material = row['МАТЕРИАЛ']).save()
                
                
        if '-FCE' in row['МАТЕРИАЛ']:
            for i in range(1,3):
                if i ==1:
                    df_new['ID'][counter_2] ='1'
                    df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                    df_new['WERKS'][counter_2] ='4901'
                    df_new['STTAG'][counter_2] ='01012024'
                    df_new['PLNAL'][counter_2] ='1'
                    df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                    df_new['VERWE'][counter_2] ='1'
                    df_new['STATU'][counter_2] ='4'     
                    df_new['LOSVN'][counter_2] ='1'
                    df_new['LOSBS'][counter_2] ='99999999'
                elif i == 2:
                    df_new['ID'][counter_2]='2'
                    df_new['VORNR'][counter_2] ='0010'
                    df_new['ARBPL'][counter_2] ='4901FREZ'
                    df_new['WERKS1'][counter_2] ='4901'
                    df_new['STEUS'][counter_2] ='ZK01'
                    df_new['LTXA1'][counter_2] ='Матрицы Фрезерный участок'
                    df_new['BMSCH'][counter_2] = '1'
                    df_new['MEINH'][counter_2] ='ST'
                    df_new['VGW01'][counter_2] ='24'
                    df_new['VGE01'][counter_2] ='STD'
                    df_new['ACTTYPE_01'][counter_2] =''
                    df_new['CKSELKZ'][counter_2] ='X'
                    df_new['UMREZ'][counter_2] = '1'
                    df_new['UMREN'][counter_2] = '1'
                    df_new['USR00'][counter_2] = '1'
                    df_new['USR01'][counter_2] = '60'
                    
                
                counter_2 +=1
                    # TexcartaBase(material = row['МАТЕРИАЛ']).save()
                
                
        if '-TCE' in row['МАТЕРИАЛ']:
            for i in range(1,3):
                if i ==1:
                    df_new['ID'][counter_2] ='1'
                    df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                    df_new['WERKS'][counter_2] ='4901'
                    df_new['STTAG'][counter_2] ='01012024'
                    df_new['PLNAL'][counter_2] ='1'
                    df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                    df_new['VERWE'][counter_2] ='1'
                    df_new['STATU'][counter_2] ='4'     
                    df_new['LOSVN'][counter_2] ='1'
                    df_new['LOSBS'][counter_2] ='99999999'
                elif i == 2:
                    df_new['ID'][counter_2]='2'
                    df_new['VORNR'][counter_2] ='0010'
                    df_new['ARBPL'][counter_2] ='4901TOKR'
                    df_new['WERKS1'][counter_2] ='4901'
                    df_new['STEUS'][counter_2] ='ZK01'
                    df_new['LTXA1'][counter_2] ='Матрицы Токарный Участок'
                    df_new['BMSCH'][counter_2] = '1'
                    df_new['MEINH'][counter_2] ='ST'
                    df_new['VGW01'][counter_2] ='24'
                    df_new['VGE01'][counter_2] ='STD'
                    df_new['ACTTYPE_01'][counter_2] =''
                    df_new['CKSELKZ'][counter_2] ='X'
                    df_new['UMREZ'][counter_2] = '1'
                    df_new['UMREN'][counter_2] = '1'
                    df_new['USR00'][counter_2] = '1'
                    df_new['USR01'][counter_2] = '60'
                    
                
                counter_2 +=1
                    # TexcartaBase(material = row['МАТЕРИАЛ']).save()
                
                
        if '-NRZ' in row['МАТЕРИАЛ']:
            for i in range(1,3):
                if i ==1:
                    df_new['ID'][counter_2] ='1'
                    df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                    df_new['WERKS'][counter_2] ='4901'
                    df_new['STTAG'][counter_2] ='01012024'
                    df_new['PLNAL'][counter_2] ='1'
                    df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                    df_new['VERWE'][counter_2] ='1'
                    df_new['STATU'][counter_2] ='4'     
                    df_new['LOSVN'][counter_2] ='1'
                    df_new['LOSBS'][counter_2] ='99999999'
                elif i == 2:
                    df_new['ID'][counter_2]='2'
                    df_new['VORNR'][counter_2] ='0010'
                    df_new['ARBPL'][counter_2] ='4901REZK'
                    df_new['WERKS1'][counter_2] ='4901'
                    df_new['STEUS'][counter_2] ='ZK01'
                    df_new['LTXA1'][counter_2] ='Матрицы участок нарезки'
                    df_new['BMSCH'][counter_2] = '1'
                    df_new['MEINH'][counter_2] ='ST'
                    df_new['VGW01'][counter_2] ='24'
                    df_new['VGE01'][counter_2] ='STD'
                    df_new['ACTTYPE_01'][counter_2] =''
                    df_new['CKSELKZ'][counter_2] ='X'
                    df_new['UMREZ'][counter_2] = '1'
                    df_new['UMREN'][counter_2] = '1'
                    df_new['USR00'][counter_2] = '1'
                    df_new['USR01'][counter_2] = '60'
                    
                
                counter_2 +=1
                    # TexcartaBase(material = row['МАТЕРИАЛ']).save()
                
                
        if '-7' in row['МАТЕРИАЛ']:
            for i in range(1,3):
                if i ==1:
                    df_new['ID'][counter_2] ='1'
                    df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                    df_new['WERKS'][counter_2] ='4901'
                    df_new['STTAG'][counter_2] ='01012024'
                    df_new['PLNAL'][counter_2] ='1'
                    df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                    df_new['VERWE'][counter_2] ='1'
                    df_new['STATU'][counter_2] ='4'     
                    df_new['LOSVN'][counter_2] ='1'
                    df_new['LOSBS'][counter_2] ='99999999'
                elif i == 2:
                    df_new['ID'][counter_2]='2'
                    df_new['VORNR'][counter_2] ='0010'
                    df_new['ARBPL'][counter_2] ='4901SBRK'
                    df_new['WERKS1'][counter_2] ='4901'
                    df_new['STEUS'][counter_2] ='ZK01'
                    df_new['LTXA1'][counter_2] ='Матрицы участок сборки+упаковки'
                    df_new['BMSCH'][counter_2] = '1'
                    df_new['MEINH'][counter_2] ='ST'
                    df_new['VGW01'][counter_2] ='24'
                    df_new['VGE01'][counter_2] ='STD'
                    df_new['ACTTYPE_01'][counter_2] =''
                    df_new['CKSELKZ'][counter_2] ='X'
                    df_new['UMREZ'][counter_2] = '1'
                    df_new['UMREN'][counter_2] = '1'
                    df_new['USR00'][counter_2] = '1'
                    df_new['USR01'][counter_2] = '60'
                    
                
                counter_2 +=1
                    # TexcartaBase(material = row['МАТЕРИАЛ']).save()

    del df_new['counter']            

    string_rand = generate_random_string()
    path2 =f'{MEDIA_ROOT}\\uploads\\matrix\\texcarta_matrix_{string_rand}.xlsx'
    df_new.to_excel(path2,index=False)

    context ={
            'file1':path2,
            'section':'Техкарта',

        }

   
    return render(request,'norma/radiator/generated_files_texcarta.html',context)
                


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','matrix','universal_user'])
def file_upload_matrix_tex(request): 
    if request.method == 'POST':
        data = request.POST.copy()
        data['type']='simple'
        form = TexcartaMatrixFileForm(data, request.FILES)
        if form.is_valid():
            file = form.save()
            context ={'files':[File(file=str(file.file),id=file.id),],
                'link':'/matrix/generate-matrix-texcarta/',
                'section':'Генерация техкарта файла',
                'type':'matrix',
                'file_type':'simple'
                }
        return render(request,'universal/file_list_norma.html',context)
    else:
        form =TexcartaMatrixFileForm()
        context ={
            'section':''
        }
    return render(request,'universal/main.html',context)

