from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from .forms import NormaEpdmFileForm
from .models import NormaEpdm,EpdmFile
from config.settings import MEDIA_ROOT
import pandas as pd
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','epdm'])
def full_update_norm(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['type']='termo'
        form = NormaEpdmFileForm(data, request.FILES)
        if form.is_valid():
            normaa =NormaEpdm.objects.all()
            normaa.delete()
            form_file = form.save()
            file = form_file.file
            path =f'{MEDIA_ROOT}/{file}'
            
            df = pd.read_excel(path,sheet_name='Baza', header=0)
            

            df = df.astype(str)
            df = df.replace('nan','0')
            df = df.replace('0.0','0')
            df = df.replace(' ','0')
            
            columns = df.columns

            NormaEpdm(data ={'columns':list(columns)}).save()

            for key, row in df.iterrows():
                norma_dict = {}
                for col in columns:
                    norma_dict[col]=row[col]
                NormaEpdm(data =norma_dict).save()

    return render(request,'norma/benkam/main.html')


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','epdm'])
def generate_norma_epdm(request,id):

    # file = KraskaFile.objects.get(id=id).file
    file = f'D:\\Users\\Muzaffar.Tursunov\\Desktop\\NORMA\\NORM_EPDM\\epdm.xlsx'
    
    # df_sapcodes = pd.read_excel(f'{MEDIA_ROOT}/{file}')
    df_sapcodes = pd.read_excel(file,sheet_name='sapcode',header=0)

    df_sapcodes = df_sapcodes.astype(str)
    df_sapcodes = df_sapcodes.replace('nan','0')
    
    df = pd.DataFrame()
    df['counter'] = [0 for x in range(len(df_sapcodes)*15)]
    df['ID'] = ""
    df['MATNR'] = ""
    df['WERKS'] = ""
    df['TEXT1'] = ""
    df['STLAL'] = ""
    df['STLAN'] = ""
    df['ZTEXT'] = ""
    df['STKTX'] = ""
    df['BMENG'] = ""
    df['BMEIN'] = ""
    df['STLST'] = ""
    df['POSNR'] = ""
    df['POSTP'] = ""
    df['MATNR1'] = ""
    df['TEXT2'] = ""
    df['MEINS'] = ""
    df['MENGE'] = ""
    df['DATUV'] = ""
    df['PUSTOY'] = ""
    df['LGORT'] = ""
    
    count_2=0
    
    itogo = NormaEpdm.objects.filter(
                        Q(data__Краткий_текст__icontains='Итого')
                    )[:1].get().data
    
    for key, row in df_sapcodes.iterrows():
        print(key)
        for i in range(1,3):
            if i == 1:
                df['ID'][count_2] ='1'
                df['MATNR'][count_2] = row['MATNR']
                df['WERKS'][count_2] = '4701'
                df['TEXT1'][count_2] = row['TEXT1']
                df['STLAL'][count_2] = '1'
                df['STLAN'][count_2] = '1'
                df['ZTEXT'][count_2] = row['TEXT1']
                df['STKTX'][count_2] = 'Упаковка'
                df['BMENG'][count_2] = '1000'
                df['BMEIN'][count_2] = 'ШТ'
                df['STLST'][count_2] = '1'
                df['POSNR'][count_2] = ''
                df['POSTP'][count_2] = ''
                df['MATNR1'][count_2] = ''
                df['TEXT2'][count_2] = ''
                df['MEINS'][count_2] = ''
                df['MENGE'][count_2] = ''
                df['DATUV'][count_2] = '01012023'
                df['PUSTOY'][count_2] = ''
                df['LGORT'][count_2] = ''
                
                zagolovok = str(row['ШОР 1'])
                
                result = NormaEpdm.objects.filter(
                                Q(data__has_key=zagolovok) & ~Q(data__contains={zagolovok: "0"}) & ~Q(data__contains={zagolovok: ""})
                            ).order_by('created_at').values('data')

            
                itogo_val =float(itogo[zagolovok])

                
                count_2 +=1
                count = 1

                
                norma_kg = float(row['Норма кг'])

                for norm in result:
                    data = norm['data']
                    
                    if 'Итого' in data['Краткий_текст']:
                        continue
                    
                    df['ID'][count_2] = '2'
                    df['POSNR'][count_2] = count
                    df['POSTP'][count_2] = 'L'
                    df['MATNR1'][count_2] = str(data['SAP код']).replace('.0','')
                    df['TEXT2'][count_2] = data['Краткий_текст']
                    df['MEINS'][count_2] = round((float(data[zagolovok])/itogo_val) * norma_kg * 1000,3)
                    df['MENGE'][count_2] = 'КГ'
                    df['LGORT'][count_2] = 'PS01'
                    count_2 +=1
                    count +=1


            if i == 2:
                if row['ШОР 2'] !='0':
                    df['ID'][count_2] ='1'
                    df['MATNR'][count_2] = row['MATNR']
                    df['WERKS'][count_2] = '4701'
                    df['TEXT1'][count_2] = row['TEXT1']
                    df['STLAL'][count_2] = '1'
                    df['STLAN'][count_2] = '2'
                    df['ZTEXT'][count_2] = row['TEXT1']
                    df['STKTX'][count_2] = 'Упаковка2'
                    df['BMENG'][count_2] = '1000'
                    df['BMEIN'][count_2] = 'ШТ'
                    df['STLST'][count_2] = '1'
                    df['POSNR'][count_2] = ''
                    df['POSTP'][count_2] = ''
                    df['MATNR1'][count_2] = ''
                    df['TEXT2'][count_2] = ''
                    df['MEINS'][count_2] = ''
                    df['MENGE'][count_2] = ''
                    df['DATUV'][count_2] = '01012023'
                    df['PUSTOY'][count_2] = ''
                    df['LGORT'][count_2] = ''
                    
                    zagolovok = str(row['ШОР 2'])
                    
                    result = NormaEpdm.objects.filter(
                                    Q(data__has_key=zagolovok) & ~Q(data__contains={zagolovok: "0"}) & ~Q(data__contains={zagolovok: ""})
                                ).order_by('created_at').values('data')

                
                    itogo_val =float(itogo[zagolovok])

                    
                    count_2 +=1
                    count = 1

                    
                    norma_kg = float(row['Норма кг'])

                    for norm in result:
                        data = norm['data']
                        
                        if 'Итого' in data['Краткий_текст']:
                            continue
                        
                        df['ID'][count_2] = '2'
                        df['POSNR'][count_2] = count
                        df['POSTP'][count_2] = 'L'
                        df['MATNR1'][count_2] = str(data['SAP код']).replace('.0','')
                        df['TEXT2'][count_2] = data['Краткий_текст']
                        df['MEINS'][count_2] = round((float(data[zagolovok])/itogo_val) * norma_kg * 1000,3)
                        df['MENGE'][count_2] = 'КГ'
                        df['LGORT'][count_2] = 'PS01'
                        count_2 +=1
                        count +=1



    del df['counter']
    # print(df)
    df.to_excel(f'{MEDIA_ROOT}\\uploads\\epdm\\norma.xlsx',index=False)
    return JsonResponse({'a':'b'})


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','epdm'])
def lenght_generate_texcarta(request,id):
    # file = KraskaFile.objects.get(id=id).file
    path = f'D:\\Users\\Muzaffar.Tursunov\\Desktop\\NORMA\\NORM_EPDM\\epdm.xlsx'
    
    # df_sapcodes = pd.read_excel(f'{MEDIA_ROOT}/{file}')
  


    data = pd.read_excel(path,sheet_name='sapcode',header=0)
    counter = len(data)

    df_new = pd.DataFrame()
    df_new['counter'] =[ '' for i in range(0,counter*2)]
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
    for key,row in data.iterrows():
        for i in range(1,3):
            if i ==1:
                df_new['ID'][counter_2] ='1'
                df_new['MATNR'][counter_2] = row['MATNR']
                df_new['WERKS'][counter_2] ='4701'
                df_new['STTAG'][counter_2] ='01012023'
                df_new['PLNAL'][counter_2] ='1'
                df_new['KTEXT'][counter_2] =row['TEXT1']
                df_new['VERWE'][counter_2] ='1'
                df_new['STATU'][counter_2] ='4'
                df_new['LOSVN'][counter_2] ='0.001'
                df_new['LOSBS'][counter_2] ='99999999'
            elif i == 2:
                df_new['ID'][counter_2]='2'
                df_new['VORNR'][counter_2] ='0010'
                df_new['ARBPL'][counter_2] ='4702KR01'
                df_new['WERKS1'][counter_2] ='4702'
                df_new['STEUS'][counter_2] ='ZK01'
                df_new['LTXA1'][counter_2] ='Производство Краски'
                df_new['BMSCH'][counter_2] = '1000'
                df_new['MEINH'][counter_2] ='КГ'
                df_new['VGW01'][counter_2] =''
                df_new['VGE01'][counter_2] =''
                df_new['ACTTYPE_01'][counter_2] ='200160'
                df_new['CKSELKZ'][counter_2] ='X'
                df_new['UMREZ'][counter_2] = '1'
                df_new['UMREN'][counter_2] = '1'
                df_new['USR00'][counter_2] = '1'
                df_new['USR01'][counter_2] = '60'
                
            counter_2 +=1

    df_new.to_excel('texcarta2.xlsx')

    df_new.to_excel(f'{MEDIA_ROOT}\\uploads\\epdm\\norma.xlsx',index=False)

    return JsonResponse({'a':'b'})


