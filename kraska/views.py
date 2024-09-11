from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from .forms import NormaKraskaFileForm
from .models import Norma7
from config.settings import MEDIA_ROOT
import pandas as pd
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.



@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','kraska'])
def full_update_norm(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['type']='termo'
        form = NormaKraskaFileForm(data, request.FILES)
        if form.is_valid():
            normaa =Norma7.objects.all()
            normaa.delete()
            form_file = form.save()
            file = form_file.file
            path =f'{MEDIA_ROOT}/{file}'
            
            df = pd.read_excel(path,sheet_name='1-etap', header=2)
            

            df = df.astype(str)
            df = df.replace('nan','0')
            df = df.replace('0.0','0')
            
            columns = df.columns

            Norma7(data ={'columns':list(columns)}).save()

            for key, row in df.iterrows():
                norma_dict = {}
                for col in columns:
                    norma_dict[col]=row[col]
                Norma7(data =norma_dict).save()

    return render(request,'norma/benkam/main.html')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','kraska'])
def generate_norma(request,id):

    # file = KraskaFile.objects.get(id=id).file
    file = f'D:\\Users\\Muzaffar.Tursunov\\Desktop\\NORMA\\NORMA\\MAKT.xlsx'
    file2 = f'D:\\Users\\Muzaffar.Tursunov\\Desktop\\NORMA\\NORMA\\SAPCODE_BAZA.xlsx'
    df_baza = pd.read_excel(file2)

    df_baza.astype(str)
    df_baza.replace('nan','0')
    df_sapcodes = pd.read_excel(file)


    baza ={}
    for key,row in df_baza.iterrows():
        keyy= str(row['KOD'])
        baza[keyy]={
            'MATNR':row['MATNR'],
            'TEXT1':row['TEXT1'],
        }
    
    df = pd.DataFrame()
    df['counter'] = [0 for x in range(len(df_sapcodes)*25)]
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
    # print(df)
    # print(makt.columns)
    count_2=0
    
    itogo = Norma7.objects.filter(
                        Q(data__MATN__icontains='Итого')
                    )[:1].get().data
    # print(baza)
    for key, row in df_sapcodes.iterrows():
        df['ID'][count_2] ='1'
        df['MATNR'][count_2] = row['MATNR']
        df['WERKS'][count_2] = '4702'
        df['TEXT1'][count_2] = row['TEXT1']
        df['STLAL'][count_2] = '1'
        df['STLAN'][count_2] = '1'
        df['ZTEXT'][count_2] = row['TEXT1']
        df['STKTX'][count_2] = 'Упаковка'
        df['BMENG'][count_2] = '1000'
        df['BMEIN'][count_2] = 'КГ'
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
        
        zagolovok = str(row['KOD'])
        
        result = Norma7.objects.filter(
                        Q(data__has_key=zagolovok) & ~Q(data__contains={zagolovok: "0"})
                    ).order_by('created_at').values('data')

        # print(itogo,'itogoogg')
        itogo_val =float(itogo[zagolovok])

        # print(zagolovok,'>>>>>>>',result)
        count_2 +=1
        count = 1

        

        for res in result:
            first_val = res['data']
            matn = first_val['MATN']
           
            if matn in baza and matn != '0' and matn != 0: 
                # print(matn,'<<<<<< operation one ','<<|'*40)
                baza_dat = baza[matn]
                df['ID'][count_2] = '2'
                df['POSNR'][count_2] = count
                df['POSTP'][count_2] = 'L'
                df['MATNR1'][count_2] = baza_dat['MATNR']
                df['TEXT2'][count_2] = baza_dat['TEXT1']
                df['MEINS'][count_2] = round((float(first_val[zagolovok])/itogo_val)*1000,3)
                df['MENGE'][count_2] = 'КГ'
                df['LGORT'][count_2] = 'PS02'
                count_2 +=1
                count +=1






        # count_2 +=1
        

        # print(zagolovok,itogo_val,'gggg'*8)
        
        for norm in result:
            data = norm['data']
            matn = data['MATN']
            if (('Итого' in data['MATN']) or (str(matn) in baza)):
                continue
            df['ID'][count_2] = '2'
            df['POSNR'][count_2] = count
            df['POSTP'][count_2] = 'L'
            df['MATNR1'][count_2] = str(data['SAPCODE']).replace('.0','')
            df['TEXT2'][count_2] = data['MATN']
            df['MEINS'][count_2] = round((float(data[zagolovok])/itogo_val)*1000,3)
            df['MENGE'][count_2] = 'КГ'
            df['LGORT'][count_2] = 'PS02'
            count_2 +=1
            count +=1



    del df['counter']
    # print(df)
    df.to_excel(f'{MEDIA_ROOT}\\uploads\\kraska\\norma.xlsx',index=False)
    return JsonResponse({'a':'b'})





@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','kraska'])
def lenght_generate_texcarta(request,id):
    # file = KraskaFile.objects.get(id=id).file
    path = f'D:\\Users\\Muzaffar.Tursunov\\Desktop\\NORMA\\NORMA\\simple texcart.xlsx'
    data = pd.read_excel(path)
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
                df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                df_new['WERKS'][counter_2] ='4702'
                df_new['STTAG'][counter_2] ='01012024'
                df_new['PLNAL'][counter_2] ='1'
                df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
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
                df_new['MEINH'][counter_2] ='KG'
                df_new['VGW01'][counter_2] =''
                df_new['VGE01'][counter_2] =''
                df_new['ACTTYPE_01'][counter_2] ='200160'
                df_new['CKSELKZ'][counter_2] ='X'
                df_new['UMREZ'][counter_2] = '1'
                df_new['UMREN'][counter_2] = '1'
                df_new['USR00'][counter_2] = '1'
                df_new['USR01'][counter_2] = '60'
                
            counter_2 +=1
    
    del df_new['counter']

    df_new.to_excel(f'{MEDIA_ROOT}\\uploads\\kraska\\texcarta_kraska.xlsx',index=False)

    # df_new.to_excel(f'{MEDIA_ROOT}\\uploads\\kraska\\norma.xlsx',index=False)

    return JsonResponse({'a':'b'})


