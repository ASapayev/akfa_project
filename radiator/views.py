from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from .forms import NormaFileForm,NormaExcelFiles,ViFileForm
from .models import Norma,Siryo,Korobka,Kraska,TexcartaBase,ViFiles,RadiatorFile,RadiatorSapCode,OrderRadiator,RazlovkaRadiator,RazlovkaRadiatorAurora
from config.settings import MEDIA_ROOT
import modin.pandas as pd
from accounts.models import User
import os 
from django.http import JsonResponse
import sys
from datetime import datetime
from django.db.models import Max
from aluminiy.utils import download_bs64
from random import randint
from .utils import create_characteristika,create_characteristika_utils,get_ozmka



@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','radiator','universal_user'])
def vi_file(request):
    files = ViFiles.objects.all().order_by('-created_at')
    context ={
        'files':files,
        'section':'Формирование ВИ файла',
        'link':'/radiator/vi-generate/',
        'type':'ВИ'
        }
    return render(request,'universal/file_list.html',context)


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','radiator','universal_user'])
def vi_mo_file(request):
    files = ViFiles.objects.all().order_by('-created_at')
    context ={
        'files':files,
        'section':'Формирование ВИ файла',
        'link':'/radiator/vi-generate-mo/',
        'type':'ВИ'
        }
    return render(request,'universal/file_list.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator','universal_user'])
def file_vi_upload_org(request):
      
    if request.method == 'POST':
        form = ViFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vi_file_list_radiator')
    else:
        context ={
            'section':'Загрузка ВИ файла'
        }
    return render(request,'universal/main.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator','universal_user'])
def file_vi_mo_upload_org(request):
      
    if request.method == 'POST':
        form = ViFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vi_mo_file_list_radiator')
    else:
        context ={
            'section':'Загрузка ВИ файла'
        }
    return render(request,'universal/main.html',context)


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator','universal_user'])
def vi_generate(request,id):
    file = ViFiles.objects.get(id=id).file
    file_path =f'{MEDIA_ROOT}\\{file}'
    df_new = pd.read_excel(file_path,sheet_name=['MARA','MAPL','MAST','PLPO','STKO'])
    df_new['MARA'] = df_new['MARA'].astype(str)
    df_new['MAPL'] = df_new['MAPL'].astype(str)
    df_new['MAST'] = df_new['MAST'].astype(str)
    df_new['PLPO'] = df_new['PLPO'].astype(str)
    df_new['STKO'] = df_new['STKO'].astype(str)

    df_new['MARA'] = df_new['MARA'].replace('nan','')
    df_new['MAPL'] = df_new['MAPL'].replace('nan','')
    df_new['MAST'] = df_new['MAST'].replace('nan','')
    df_new['PLPO'] = df_new['PLPO'].replace('nan','')
    df_new['STKO'] = df_new['STKO'].replace('nan','')


    # print(df)

    df_vi = pd.DataFrame()
    df_vi['WERKS'] = ['5101' for i in df_new['MAST']['Материал']]
    df_vi['MATNR'] = df_new['MAST']['Материал']
    df_vi['VERID'] = ["{:04d}".format(int(i)) for i in df_new['MAST']['АльтернСпецификация']]
    df_vi['BSTMI'] = ['1' for i in df_new['MAST']['Материал']]
    df_vi['BSTMA'] = ['99999999' for i in df_new['MAST']['Материал']]
    df_vi['ADATU'] = ['01012024' for i in df_new['MAST']['Материал']]
    df_vi['BDATU'] = ['31129999' for i in df_new['MAST']['Материал']]
    df_vi['PLNTY'] = ['N' for i in df_new['MAST']['Материал']]
    
    df_vi['ALNAL'] = ['1' for i in df_new['MAST']['Материал']]
    df_vi['STLAL'] = df_new['MAST']['АльтернСпецификация']
    df_vi['STLAN'] = ['1' for i in df_new['MAST']['Материал']]
    df_vi['ELPRO'] = ''
    df_vi['ALORT'] = ''
    df_vi['MATNR ALT'] =df_vi['MATNR']+df_vi['STLAL']
    
    # find_z =df_vi[df_vi['MATNR'].str.contains("-Z")]
    # print(find_z)
    


    df_merge1 = pd.DataFrame()
    df_merge1['Спецификация'] =df_new['MAST']['Спецификация']
    df_merge1['Материал'] =df_new['MAST']['Материал']
    df = pd.merge(df_merge1,df_new['STKO'],   how='inner',left_on=['Спецификация'],right_on=['Спецификация'])
    df['MATNR ALT'] = df['Материал'] + df['АльтернСпецификация']
    # df_new['STKO'].merge(df_new['MAST'],on='Спецификация', how='inner')

    df_text_alt = pd.DataFrame()
    df_text_alt['MATNR ALT'] =df['MATNR ALT']
    df_text_alt['TEXT1'] =df['Текст к альтернативе']

    df_new_vi = pd.merge(df_text_alt,df_vi,   how='inner',left_on=['MATNR ALT'],right_on=['MATNR ALT'])

    # find_z = df_new_vi[df_new_vi['MATNR'].str.contains("-Z")]
    # print(find_z)

    df_plpo = pd.DataFrame()
    df_plpo['Материал'] =df_new['MAPL']['Материал']
    df_plpo['Группа'] =df_new['MAPL']['Группа']
    df2 = pd.merge(df_plpo,df_new['PLPO'],   how='inner',left_on=['Группа'],right_on=['Группа'])

    df2_filtered =df2[~df2['Краткий текст к операции'].isin(['SKM Хим. обработка', 'ГР Хим. обработка', 'SAT Хим. обработка'])] 

    df2_filtered['MATNR PLPO KRATKIY'] =df2_filtered['Материал']+ df2_filtered['Краткий текст к операции']

    df_new_vi['MATNR PLPO KRATKIY'] =df_new_vi['MATNR'] +df_new_vi['TEXT1']
    

    # find_z = df_new_vi[df_new_vi['MATNR'].str.contains("-Z")]
    # print(find_z)

    df_plpo_2 =pd.DataFrame()
    df_plpo_2['MATNR PLPO KRATKIY'] = df2_filtered['MATNR PLPO KRATKIY']
    df_plpo_2['PLNNR'] = df2_filtered['Группа']

    
    df_z = df_plpo[df_plpo['Материал'].str.contains("-Z")]
    df_z['MATNR'] = df_z['Материал']
    df_z['PLNNR'] = df_z['Группа']
    del df_z["Материал"]
    del df_z["Группа"]


    find_z_in_vi = df_new_vi[df_new_vi['MATNR PLPO KRATKIY'].str.contains("-Z")]


    df_new_vi_z = pd.merge(df_z,find_z_in_vi,   how='inner',left_on=['MATNR'],right_on=['MATNR'])
    # print(df_new_vi_z,'vi')



    df_new_vi2 = pd.merge(df_plpo_2,df_new_vi,   how='inner',left_on=['MATNR PLPO KRATKIY'],right_on=['MATNR PLPO KRATKIY'])

    df_new_vi2 = pd.concat([df_new_vi2, df_new_vi_z])
    

    ################
    #algort
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['Упаковка']),'ALORT'] = 'PS08'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['Покраска']),'ALORT'] = 'PS08'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['PUMA']),'ALORT'] = 'PS07'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['Пресс']),'ALORT'] = 'PS02'
    


    ####################

    df_4_filter =df_new_vi2[df_new_vi2['VERID'].isin(['0004'])]
    df_5_filter =df_new_vi2[df_new_vi2['VERID'].isin(['0005'])]
    df_6_filter =df_new_vi2[df_new_vi2['VERID'].isin(['0006'])]

    df_pere_prisvoeniye_4 = pd.DataFrame({'MATNR':df_4_filter['MATNR'],'WERKS':['5101' for i in df_4_filter['MATNR']],'PLNNR':df_4_filter['PLNNR'],'VORNR':['010' for i in df_4_filter['MATNR']],'PLNFL':['0010' for i in df_4_filter['MATNR']]})
    df_pere_prisvoeniye_5 = pd.DataFrame({'MATNR':df_5_filter['MATNR'],'WERKS':['5101' for i in df_5_filter['MATNR']],'PLNNR':df_5_filter['PLNNR'],'VORNR':['010' for i in df_5_filter['MATNR']],'PLNFL':['0010' for i in df_5_filter['MATNR']]})
    df_pere_prisvoeniye_6 = pd.DataFrame({'MATNR':df_6_filter['MATNR'],'WERKS':['5101' for i in df_6_filter['MATNR']],'PLNNR':df_6_filter['PLNNR'],'VORNR':['010' for i in df_6_filter['MATNR']],'PLNFL':['0010' for i in df_6_filter['MATNR']]})
    
    del df_new_vi2["MATNR PLPO KRATKIY"]
    del df_new_vi2["MATNR ALT"]

    columnsTitles = ['WERKS', 'MATNR', 'VERID','TEXT1','BSTMI','BSTMA','ADATU','BDATU','PLNTY','PLNNR','ALNAL','STLAL','STLAN','ELPRO','ALORT']
    df_new_vi2 = df_new_vi2.reindex(columns=columnsTitles)
    

    df_new_vi2 = df_new_vi2.drop_duplicates()
    df_pere_prisvoeniye_4 = df_pere_prisvoeniye_4.drop_duplicates()
    df_pere_prisvoeniye_5 = df_pere_prisvoeniye_5.drop_duplicates()
    df_pere_prisvoeniye_6 = df_pere_prisvoeniye_6.drop_duplicates()

    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%d-%B-%Y %H-%M-%S")    
                 
            
    create_folder(f'{MEDIA_ROOT}\\uploads\\','vi')
    create_folder(f'{MEDIA_ROOT}\\uploads\\vi\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\vi\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\vi\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\vi\\{year}\\{month}\\{day}\\',hour)
    create_folder(f'{MEDIA_ROOT}\\uploads\\vi\\{year}\\{month}\\{day}\\{hour}',minut)

    path =f'{MEDIA_ROOT}\\uploads\\vi\\{year}\\{month}\\{day}\\{hour}\\{minut}\\ВИ_5101.xlsx'
    
    writer = pd.ExcelWriter(path, engine='openpyxl')
    df_new_vi2.to_excel(writer,index=False,sheet_name ='ВИ')
    # df_pere_prisvoeniye_4.to_excel(writer,index=False,sheet_name ='4')
    # df_pere_prisvoeniye_5.to_excel(writer,index=False,sheet_name ='5')
    # df_pere_prisvoeniye_6.to_excel(writer,index=False,sheet_name ='6')
    writer.close()

    files =[File(file =path,filetype='vi',id=None)]
    context ={
        'section':'ВИ',
        'files':files
    }
    return render(request,'universal/generated_files.html',context)


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator','universal_user'])
def vi_generate_mo(request,id):
    file = ViFiles.objects.get(id=id).file
    file_path =f'{MEDIA_ROOT}\\{file}'
    df_new = pd.read_excel(file_path,sheet_name=['MARA','MAPL','PLKO','MAST','PLPO','STKO'])
    df_new['MARA'] =df_new['MARA'].astype(str)
    df_new['MAPL'] =df_new['MAPL'].astype(str)
    df_new['PLKO'] =df_new['PLKO'].astype(str)
    df_new['MAST'] =df_new['MAST'].astype(str)
    df_new['PLPO'] =df_new['PLPO'].astype(str)
    df_new['STKO'] =df_new['STKO'].astype(str)

    df_new['MARA']=df_new['MARA'].replace('nan','')
    df_new['MAPL']=df_new['MAPL'].replace('nan','')
    df_new['PLKO']=df_new['PLKO'].replace('nan','')
    df_new['MAST']=df_new['MAST'].replace('nan','')
    df_new['PLPO']=df_new['PLPO'].replace('nan','')
    df_new['STKO']=df_new['STKO'].replace('nan','')
   

    # print(df)

    df_vi = pd.DataFrame()
    df_vi['WERKS'] = ['5101' for i in df_new['MAPL']['Материал']]
    df_vi['MATNR'] = df_new['MAPL']['Материал']
    df_vi['VERID'] = ['' for i in df_new['MAPL']['Материал']]
    df_vi['BSTMI'] = ['1' for i in df_new['MAPL']['Материал']]
    df_vi['BSTMA'] = ['99999999' for i in df_new['MAPL']['Материал']]
    df_vi['ADATU'] = ['01012024' for i in df_new['MAPL']['Материал']]
    df_vi['BDATU'] = ['31129999' for i in df_new['MAPL']['Материал']]
    df_vi['PLNTY'] = ['N' for i in df_new['MAPL']['Материал']]
    df_vi['PLNNR'] = df_new['MAPL']['Группа']
    
    df_vi['ALNAL'] = ['1' for i in df_new['MAPL']['Материал']]
    df_vi['STLAL'] =  ['' for i in df_new['MAPL']['Материал']]
    df_vi['STLAN'] = ['1' for i in df_new['MAPL']['Материал']]
    df_vi['ELPRO'] = ''
    df_vi['ALORT'] = ''
    df_vi['MATNR ALT'] =df_vi['MATNR']+df_vi['STLAL']
    
    
    


    df_merge1 = pd.DataFrame()
    df_merge1['TEXT1'] =df_new['PLKO']['ТкстТехкрт']
    df_merge1['Группа'] =df_new['PLKO']['Группа']
    df_vi = pd.merge(df_vi,df_merge1,   how='inner',left_on=['PLNNR'],right_on=['Группа'])
   
    
    # print(df_vi,'ggg')
    # df_new['STKO'].merge(df_new['MAST'],on='Спецификация', how='inner')

   



    # df_merge1 = pd.DataFrame()
    # df_merge1['Краткий текст к операции'] =df_new['PLPO']['Краткий текст к операции']
    # df_merge1['Вид работ'] =df_new['PLPO']['Вид работ']
    # filtered_df = df_merge1[df_merge1['Вид работ'] != '']
    # print(filtered_df['Краткий текст к операции'],'corected')

    # df_vi['TEXT1'] = [row for row in filtered_df['Краткий текст к операции']]

    saip = df_vi['TEXT1'].str.contains('S.A.I.P.', case=False, na=False)
    gizeta = df_vi['TEXT1'].str.contains('Gi Zeta', case=False, na=False)
    ruchnoy = df_vi['TEXT1'].str.contains('Ручная', case=False, na=False)
    
    df_vi.loc[saip,'STLAN'] = ''

    df_vi.loc[ruchnoy,'STLAL'] = '1'
    df_vi.loc[gizeta,'STLAL'] = '2'
   

    df_vi.loc[saip,'ALORT'] = 'PS06'
    df_vi.loc[gizeta,'ALORT'] = 'PS05'
    df_vi.loc[ruchnoy,'ALORT'] = 'PS04'


    df_vi.loc[saip,'VERID'] = 'S001'
    df_vi.loc[gizeta,'VERID'] = 'G001'
    df_vi.loc[ruchnoy,'VERID'] = 'R001'

    # df_vi['ELPRO'] = df_vi['ALORT']

    columnsTitles = ['WERKS', 'MATNR', 'VERID','TEXT1','BSTMI','BSTMA','ADATU','BDATU','PLNTY','PLNNR','ALNAL','STLAL','STLAN','ELPRO','ALORT']
    df_new_vi2 = df_vi.reindex(columns=columnsTitles)
    

    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%d-%B-%Y %H-%M-%S")    
                 
            
    create_folder(f'{MEDIA_ROOT}\\uploads\\','vi')
    create_folder(f'{MEDIA_ROOT}\\uploads\\vi\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\vi\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\vi\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\vi\\{year}\\{month}\\{day}\\',hour)
    create_folder(f'{MEDIA_ROOT}\\uploads\\vi\\{year}\\{month}\\{day}\\{hour}',minut)

    path =f'{MEDIA_ROOT}\\uploads\\vi\\{year}\\{month}\\{day}\\{hour}\\{minut}\\ВИ_5101.xlsx'
    
    writer = pd.ExcelWriter(path, engine='openpyxl')
    df_new_vi2.to_excel(writer,index=False,sheet_name ='ВИ')
    writer.close()

    files =[File(file =path,filetype='vi',id=None)]
    context ={
        'section':'ВИ',
        'files':files
    }
    return render(request,'universal/generated_files.html',context)





@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator','universal_user'])
def full_update_korobka(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['type']='termo'
        form = NormaFileForm(data, request.FILES)
        if form.is_valid():
            # siryo = Korobka.objects.all()
            # siryo.delete()
            form_file = form.save()
            file = form_file.file
            path =f'{MEDIA_ROOT}/{file}'
            
            df = pd.read_excel(path)

            df = df.astype(str)
            df = df.replace('nan','0')
            df = df.replace('0.0','0')
            
            columns = df.columns

            # Korobka(data ={'columns':list(columns)}).save()

            for key, row in df.iterrows():
                norma_dict = {}
                for col in columns:
                    norma_dict[col]=row[col]

                if Korobka.objects.filter(data__exact=norma_dict).exists():
                    siryoo = Korobka.objects.filter(data__exact=norma_dict)[:1].get()
                    siryoo.data = norma_dict
                    
                else:
                    Korobka(data =norma_dict).save()
                
                # Korobka(data =norma_dict).save()

    return render(request,'norma/benkam/main.html')


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator','universal_user'])
def file_upload_radiator_tex(request): 
  if request.method == 'POST':
    data = request.POST.copy()
    data['type']='simple'
    form = NormaFileForm(data, request.FILES)
    if form.is_valid():
        file = form.save()
        context ={'files':[File(file=str(file.file),id=file.id,filetype='texcarta'),],
              'link':'/radiator/generate-radiator/',
              'section':'Генерация техкарта файла',
              'type':'Радиатор',
              'file_type':'simple'
              }
    return render(request,'universal/file_list_norma.html',context)
  else:
      form =NormaFileForm()
      context ={
        'section':''
      }
  return render(request,'universal/main.html',context)


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator','universal_user'])
def full_update_siryo(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['type']='termo'
        form = NormaFileForm(data, request.FILES)
        if form.is_valid():
            # siryo = Siryo.objects.all()
            # siryo.delete()
            form_file = form.save()
            file = form_file.file
            path =f'{MEDIA_ROOT}/{file}'
            
            df = pd.read_excel(path)

            df = df.astype(str)
            df = df.replace('nan','0')
            df = df.replace('0.0','0')
            
            columns = df.columns

            # Siryo(data ={'columns':list(columns)}).save()

            for key, row in df.iterrows():
                norma_dict = {}
                for col in columns:
                    norma_dict[col]=row[col]
                if Siryo.objects.filter(data__exact=norma_dict).exists():
                    siryoo = Siryo.objects.filter(data__exact=norma_dict)[:1].get()
                    siryoo.data = norma_dict
                    
                else:
                    Siryo(data =norma_dict).save()
                # Siryo(data =norma_dict).save()

    return render(request,'norma/benkam/main.html')


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator','universal_user'])
def full_update_kraska(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['type']='termo'
        form = NormaFileForm(data, request.FILES)
        if form.is_valid():
            # siryo = Kraska.objects.all()
            # siryo.delete()
            form_file = form.save()
            file = form_file.file
            path =f'{MEDIA_ROOT}/{file}'
            
            df = pd.read_excel(path)

            df = df.astype(str)
            df = df.replace('nan','0')
            df = df.replace('0.0','0')
            
            columns = df.columns

            # Kraska(data ={'columns':list(columns)}).save()

            for key, row in df.iterrows():
                norma_dict = {}
                for col in columns:
                    norma_dict[col]=row[col]
                if Kraska.objects.filter(data__exact=norma_dict).exists():
                    siryoo = Kraska.objects.filter(data__exact=norma_dict)[:1].get()
                    siryoo.data = norma_dict
                    
                else:
                    Kraska(data =norma_dict).save()

                # Kraska(data =norma_dict).save()

    return render(request,'norma/benkam/main.html')


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator','universal_user'])
def full_update_norm(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['type']='termo'
        form = NormaFileForm(data, request.FILES)
        if form.is_valid():
            normaa =Norma.objects.all()
            normaa.delete()
            form_file = form.save()
            file = form_file.file
            path =f'{MEDIA_ROOT}/{file}'
            
            df = pd.read_excel(path,sheet_name='норма + цикл', header=3)

            df = df.astype(str)
            df = df.replace('nan','0')
            df = df.replace('0.0','0')
            
            columns = df.columns

            Norma(data ={'columns':list(columns)}).save()

            for key, row in df.iterrows():
                norma_dict = {}
                for col in columns:
                    norma_dict[col]=row[col]
                Norma(data =norma_dict).save()

    return render(request,'norma/benkam/main.html')


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator','universal_user'])
def file_upload_org(request): 
    if request.method == 'POST':
        data = request.POST.copy()
        data['type']='radiator'
        form = NormaFileForm(data, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list_radiator')
    else:
        form =NormaFileForm()
    context ={
        'section':''
    }
    return render(request,'universal/main.html',context)


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator','universal_user'])
def file_list_org(request):
    files = NormaExcelFiles.objects.filter(generated =False,type='radiator').order_by('-created_at')
    context ={'files':files,
              'link':'/radiator/kombinirovaniy-process/',
              'section':'Генерация норма файла',
              'type':'Радиатор',
              'file_type':'simple'
              }
    return render(request,'universal/file_list_norma.html',context)


PROFIL_TYPE ={
    'prof_type':{
        '350':'344',
        '500':'444',
        '1000':'944',
        '1200':'1144',
        '1400':'1344',
        '1600':'1544',
        '1800':'1744',
        '2000':'1944'
    },
    'kraska':{
        '350':'17',
        '500':'24',
        '1000':'48',
        '1200':'58',
        '1400':'69',
        '1600':'83',
        '1800':'100',
        '2000':'120'
    },
    'plenka':{
        '350':'550',
        '500':'700',
        '1000':'1200',
        '1200':'1400',
        '1400':'1600',
        '1600':'1800',
        '1800':'2000',
        '2000':'2200'
    },


}




@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator','universal_user'])
def kombinirovaniy_process(request,id):
    file = NormaExcelFiles.objects.get(id=id).file
    file_path =f'{MEDIA_ROOT}\\{file}'
    df_exell_aurora = pd.read_excel(file_path,sheet_name='Schotchik_Aurora',header=0)
    df_exell = pd.read_excel(file_path,sheet_name='Schotchik',header=0)
    df_exell = df_exell.fillna('')
    df_exell_aurora = df_exell_aurora.fillna('')
    df_exell_aurora =df_exell_aurora.astype(str)
    df_exell =df_exell.astype(str)
    
    file_content ='обычный'
    df = []
    df_aurora = []
    print(df_exell_aurora) 
    
    for key,row in df_exell_aurora.iterrows():
        df_aurora.append([
                row['SAP CODE ES'],row['ES - Extrusion'],
                row['SAP CODE ER'],row['ER - Extrusion'],
                row['SAP CODE PK'],row['PK - Pokraska'],
                row['SAP CODE 7'],row['7 - Upakovka']
            ])
        
    
    for key,row in df_exell.iterrows():
        df.append([
                row['SAP CODE P'],row['PR - Press'],
                row['SAP CODE M'],row['MO - Mex obrabotka'],
                row['SAP CODE PM'],row['PM - Puma'],
                row['SAP CODE PK'],row['PK - Pokraska'],
                row['SAP CODE 7'],row['7 - Upakovka']
            ])
    
    class Xatolar:
        def __init__(self,section,xato,sap_code):
            self.section = section
            self.xato = xato
            self.sap_code = sap_code

    does_not_exist_norm =[]
    checking =[]
    k = -1
    
    for i in range(0,len(df)):
        if df[i][8] != '':
            artikul = df[i][8].split('-')[0]
            if not Norma.objects.filter(data__Артикул__icontains = artikul).exists():
                if df[i][8] not in checking:
                    does_not_exist_norm.append(Xatolar(section='Норма расход',xato='bazada yo\'q',sap_code=df[i][8]))
                    checking.append(df[i][8])
                    continue
        if df[i][6] != '':
            kraska = df[i][7].split(' ')[-1]
            if not Kraska.objects.filter(data__CODE__icontains =kraska).exists():
                if kraska not in checking:
                    checking.append(kraska)
                    does_not_exist_norm.append(Xatolar(section='Краска',xato='bazada yo\'q',sap_code=kraska))
                    continue
    
    for i in range(0,len(df_aurora)):
        if df_aurora[i][5] != '':
            pokraska_code = str(df_aurora[i][5]).split(' ')[-1]
            if not Kraska.objects.filter(data__CODE__icontains=pokraska_code).exists():
                if pokraska_code not in checking:
                    checking.append(pokraska_code)
                    does_not_exist_norm.append(Xatolar(section='Краска',xato='bazada yo\'q',sap_code=pokraska_code))
                    continue
        if df_aurora[i][7] != '':
            krat = df_aurora[i][7].split('-')
            seria = krat[0]
            korobka_type = krat[1].split(' ')[-1]
            if not Korobka.objects.filter(data__KOROBKA__icontains=seria,data__TYPE__icontains =korobka_type).exists():
                if seria +' '+korobka_type not in checking:
                    checking.append(seria +' '+korobka_type)
                    does_not_exist_norm.append(Xatolar(section='Коробка',xato='bazada yo\'q',sap_code=seria +' '+korobka_type))
                    continue
     
    
    if len(does_not_exist_norm) > 0: 
        context ={
            'does_not_exist_norm':does_not_exist_norm,
            'section':'Ошибки нормы',
            'id':id

        }
        return render(request,'norma/benkam/not_exist.html',context)
    
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
    
   
    df_new_aurora =    {
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
    
   
    j = 0
    
    norma_exists= []

    for i in range(0,len(df)):
        # print(i)
        
        artikul = df[i][8].split('-')[0]
        # print(artikul,'norma')
        norma = Norma.objects.filter(data__Артикул__icontains = artikul)[:1].get()

        ### 7  ###
        if {df[i][8]:df[i][9]} not in norma_exists:
            norma_exists.append({df[i][8]:df[i][9]})
            df_new['ID'].append('1')
            df_new['MATNR'].append(df[i][8])
            df_new['WERKS'].append('5101')
            df_new['TEXT1'].append(df[i][9])
            df_new['STLAL'].append('1')
            df_new['STLAN'].append('1')
            df_new['ZTEXT'].append(df[i][9])
            df_new['STKTX'].append('Упаковка')
            df_new['BMENG'].append( '1000')
            df_new['BMEIN'].append('ШТ')
            df_new['STLST'].append('1')
            df_new['POSNR'].append('')
            df_new['POSTP'].append('')
            df_new['MATNR1'].append('')
            df_new['TEXT2'].append('')
            df_new['MEINS'].append('')
            df_new['MENGE'].append('')
            df_new['DATUV'].append('01012023')
            df_new['PUSTOY'].append('')
            df_new['LGORT'].append('')
            for k in range(1,2):
                j+=1
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
                df_new['POSNR'].append(k)
                df_new['POSTP'].append('L')
                
                
                if k == 1 :
                    
                    df_new['MATNR1'].append(df[i][6])
                    df_new['TEXT2'].append(df[i][7])
                    # print(df[i][9],'kkk')
                    seksiya_list =df[i][9].split(' ')
                    text =''
                    for sek in seksiya_list:
                        if '-' in sek:
                            text = sek
                            break
                    seksiya = text.split('-')[1]
                    # df_new['MEINS'].append(("%.3f" % (float(alum_teks.data['расход сплава на 1000 шт профиля/кг'])*mein_percent)).replace('.',',')) 
                    df_new['MEINS'].append(int(seksiya)*1000) 
                    df_new['MENGE'].append('СКЦ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                    
                
                df_new['LGORT'].append('PS08')

            upakovka_names =[
                {'kratkiy':'Пленка полиэтиленовая 90см','sapcode':'1000006758'},
                {'kratkiy':'Пленка полиэтиленовая 65см','sapcode':'1000006759'},
                {'kratkiy':'Пленка полиэтиленовая 85см','sapcode':'1000006760'}
                ]
            t= 1
            for k in range(0,len(upakovka_names)):
                if norma.data[upakovka_names[k]['kratkiy']] !='0':
                    j+=1
                    t+=1
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
                    df_new['POSNR'].append(t)
                    df_new['POSTP'].append('L')
                    df_new['MATNR1'].append(upakovka_names[k]['sapcode'])
                    df_new['TEXT2'].append(upakovka_names[k]['kratkiy'])
                    sap_val = norma.data[upakovka_names[k]['kratkiy']].replace(' ','').replace('.0','') if norma.data[upakovka_names[k]['kratkiy']][-2:]=='.0' else ("%.3f" % float(norma.data[upakovka_names[k]['kratkiy']].replace(' ',''))).replace('.',',')
                    df_new['MEINS'].append(sap_val) 
                    df_new['MENGE'].append('КГ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                    df_new['LGORT'].append('PS08')

             
            krat = df[i][9].split('-')
            seria = krat[0]
            korobka_type = krat[1].split(' ')[-1]
            t+=1
            if Korobka.objects.filter(data__KOROBKA__icontains=seria,data__TYPE__icontains =korobka_type).exists():
                korobka = Korobka.objects.filter(data__KOROBKA__icontains=seria,data__TYPE__icontains =korobka_type)[:1].get()
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
                df_new['POSNR'].append(t)
                df_new['POSTP'].append('L')
                df_new['MATNR1'].append(korobka.data['MATNR'])
                df_new['TEXT2'].append(korobka.data['MAKTX'])
                sap_val = '1000' if 'BK' not in korobka_type else '2000'
                df_new['MEINS'].append(sap_val) 
                df_new['MENGE'].append('ШТ')
                df_new['DATUV'].append('')
                df_new['PUSTOY'].append('')
                df_new['LGORT'].append('PS08')
        
        #### PK
        if {df[i][6]:df[i][7]} not in norma_exists:
            norma_exists.append({df[i][6]:df[i][7]})
            df_new['ID'].append('1')
            df_new['MATNR'].append(df[i][6])
            df_new['WERKS'].append('5101')
            df_new['TEXT1'].append(df[i][7])
            df_new['STLAL'].append('1')
            df_new['STLAN'].append('1')
            df_new['ZTEXT'].append(df[i][7])
            df_new['STKTX'].append('Покраска')
            df_new['BMENG'].append( '1000')
            df_new['BMEIN'].append('СКЦ')
            df_new['STLST'].append('1')
            df_new['POSNR'].append('')
            df_new['POSTP'].append('')
            df_new['MATNR1'].append('')
            df_new['TEXT2'].append('')
            df_new['MEINS'].append('')
            df_new['MENGE'].append('')
            df_new['DATUV'].append('01012023')
            df_new['PUSTOY'].append('')
            df_new['LGORT'].append('')
            for k in range(1,5):
                j+=1
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
                df_new['POSNR'].append(k)
                df_new['POSTP'].append('L')
                
                
                if k == 1 :
                    
                    df_new['MATNR1'].append(df[i][4])
                    df_new['TEXT2'].append(df[i][5])
                    # df_new['MEINS'].append(("%.3f" % (float(alum_teks.data['расход сплава на 1000 шт профиля/кг'])*mein_percent)).replace('.',',')) 
                    df_new['MEINS'].append('1000') 
                    df_new['MENGE'].append('СКЦ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                if k == 2 :
                    # siryo = Siryo.objects.filter(data__Краткийтекст__icontains ='Анафорез.грунтовка ARSONKOTE 1002K CLEAR')
                    df_new['MATNR1'].append('1000006767')
                    df_new['TEXT2'].append('Анафорез.грунтовка ARSONKOTE 1002K CLEAR')
                    
                    # df_new['MEINS'].append(("%.3f" % (float(alum_teks.data['расход сплава на 1000 шт профиля/кг'])*mein_percent)).replace('.',',')) 
                    df_new['MEINS'].append(norma.data['Анафорез.грунтовка ARSONKOTE 1002K CLEAR'].replace('.0','') if norma.data['Анафорез.грунтовка ARSONKOTE 1002K CLEAR'][-2:]=='.0' else ("%.3f" % float(norma.data['Анафорез.грунтовка ARSONKOTE 1002K CLEAR'])).replace('.',',') ) 
                    df_new['MENGE'].append('КГ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                if k == 3 :
                    # siryo = Siryo.objects.filter(data__Краткийтекст__icontains ='Анафорез.грунтовка ARSONKOTE 1002K CLEAR')
                    df_new['MATNR1'].append('1000006768')
                    df_new['TEXT2'].append('Анафорез.грунтовка. 1002K PIG.PASTE')
                    
                    # df_new['MEINS'].append(("%.3f" % (float(alum_teks.data['расход сплава на 1000 шт профиля/кг'])*mein_percent)).replace('.',',')) 
                    df_new['MEINS'].append(norma.data['Анафорез.грунтовка. 1002K PIG.PASTE'].replace('.0','')  if norma.data['Анафорез.грунтовка. 1002K PIG.PASTE'][-2:]=='.0' else ("%.3f" % float(norma.data['Анафорез.грунтовка. 1002K PIG.PASTE'])).replace('.',',')) 
                    df_new['MENGE'].append('КГ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                if k == 4 :
                    kraska = df[i][7].split(' ')[-1]
                    siryo = Kraska.objects.filter(data__CODE__icontains =kraska)[:1].get()
                    df_new['MATNR1'].append(siryo.data['MATNR'])
                    df_new['TEXT2'].append(siryo.data['MAKTX'])
                    
                    # df_new['MEINS'].append(("%.3f" % (float(alum_teks.data['расход сплава на 1000 шт профиля/кг'])*mein_percent)).replace('.',',')) 
                    df_new['MEINS'].append(norma.data['расход /кг на 1000 секции'].replace('.0','')  if norma.data['расход /кг на 1000 секции'][-2:]=='.0' else ("%.3f" % float(norma.data['расход /кг на 1000 секции'])).replace('.',',')) 
                    df_new['MENGE'].append('КГ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')

                    
                df_new['LGORT'].append('PS08')
        
        
       
        #### PM
        if {df[i][4]:df[i][5]} not in norma_exists:
            norma_exists.append({df[i][4]:df[i][5]})
            df_new['ID'].append('1')
            df_new['MATNR'].append(df[i][4])
            df_new['WERKS'].append('5101')
            df_new['TEXT1'].append(df[i][5])
            df_new['STLAL'].append('1')
            df_new['STLAN'].append('1')
            df_new['ZTEXT'].append(df[i][5])
            df_new['STKTX'].append('PUMA')
            df_new['BMENG'].append( '1000')
            df_new['BMEIN'].append('СКЦ')
            df_new['STLST'].append('1')
            df_new['POSNR'].append('')
            df_new['POSTP'].append('')
            df_new['MATNR1'].append('')
            df_new['TEXT2'].append('')
            df_new['MEINS'].append('')
            df_new['MENGE'].append('')
            df_new['DATUV'].append('01012023')
            df_new['PUSTOY'].append('')
            df_new['LGORT'].append('')
            for k in range(1,2):
                j+=1
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
                df_new['POSNR'].append(k)
                df_new['POSTP'].append('L')
                
                
                if k == 1 :
                    df_new['MATNR1'].append(df[i][2])
                    df_new['TEXT2'].append(df[i][3])
                    df_new['MEINS'].append('1000') 
                    df_new['MENGE'].append('СКЦ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                    
                df_new['LGORT'].append('PS07')
        
        
        #### M
        if {df[i][2]:df[i][3]} not in norma_exists:
            norma_exists.append({df[i][2]:df[i][3]})
            df_new['ID'].append('1')
            df_new['MATNR'].append(df[i][2])
            df_new['WERKS'].append('5101')
            df_new['TEXT1'].append(df[i][3])
            df_new['STLAL'].append('1')
            df_new['STLAN'].append('1')
            df_new['ZTEXT'].append(df[i][3])
            df_new['STKTX'].append('МехОбр. Ручная')
            df_new['BMENG'].append( '1000')
            df_new['BMEIN'].append('СКЦ')
            df_new['STLST'].append('1')
            df_new['POSNR'].append('')
            df_new['POSTP'].append('')
            df_new['MATNR1'].append('')
            df_new['TEXT2'].append('')
            df_new['MEINS'].append('')
            df_new['MENGE'].append('')
            df_new['DATUV'].append('01012023')
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
            df_new['POSNR'].append(k)
            df_new['POSTP'].append('L')
            df_new['MATNR1'].append(df[i][0])
            df_new['TEXT2'].append(df[i][1])
            df_new['MEINS'].append('1000') 
            df_new['MENGE'].append('СКЦ')
            df_new['DATUV'].append('')
            df_new['PUSTOY'].append('')
            df_new['LGORT'].append('PS04')

            siryo_names =[
                {'kratkiy':'Крышка радиатора','sapcode':'1000006844','MEINS':'КГ'},
                {'kratkiy':'Паронит межсекционная','sapcode':'1000006722','MEINS':'ШТ'},
                {'kratkiy':'Соеденительная муфта','sapcode':'1000006721','MEINS':'ШТ'},
                {'kratkiy':'Тех. отход ал стружка','sapcode':'1900012782','MEINS':'КГ'},
                ]
            t= 1
            for k in range(0,len(siryo_names)):
                if norma.data[siryo_names[k]['kratkiy']] !='0':
                    if siryo_names[k]['kratkiy'] =='Крышка радиатора' and norma.data['Тип'] =='Bimetall':
                        continue
                    j+=1
                    t+=1
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
                    df_new['POSNR'].append(t)
                    df_new['POSTP'].append('L')
                    df_new['MATNR1'].append(siryo_names[k]['sapcode'])
                    df_new['TEXT2'].append(siryo_names[k]['kratkiy'])

                    if siryo_names[k]['kratkiy'] =='Тех. отход ал стружка':
                        sap_val ='20'
                    else:
                        sap_val = norma.data[siryo_names[k]['kratkiy']].replace(' ','').replace('.0','') if norma.data[siryo_names[k]['kratkiy']][-2:]=='.0' else ("%.3f" % float(norma.data[siryo_names[k]['kratkiy']].replace(' ',''))).replace('.',',')
                    df_new['MEINS'].append(sap_val if not 'отход' in siryo_names[k]['kratkiy'] else '-' + sap_val) 
                    df_new['MENGE'].append(siryo_names[k]['MEINS'])
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                    df_new['LGORT'].append('PS04')
                
               
                    # siryo = Siryo.objects.filter(data__Краткийтекст__icontains =siryo_names[k-2]['kratkiy'])[:1].get()
        
            #####M-2
            df_new['ID'].append('1')
            df_new['MATNR'].append(df[i][2])
            df_new['WERKS'].append('5101')
            df_new['TEXT1'].append(df[i][3])
            df_new['STLAL'].append('2')
            df_new['STLAN'].append('1')
            df_new['ZTEXT'].append(df[i][3])
            df_new['STKTX'].append('Уч-к GIZETTA')
            df_new['BMENG'].append( '1000')
            df_new['BMEIN'].append('СКЦ')
            df_new['STLST'].append('1')
            df_new['POSNR'].append('')
            df_new['POSTP'].append('')
            df_new['MATNR1'].append('')
            df_new['TEXT2'].append('')
            df_new['MEINS'].append('')
            df_new['MENGE'].append('')
            df_new['DATUV'].append('01012023')
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
            df_new['POSNR'].append(1)
            df_new['POSTP'].append('L')
            df_new['MATNR1'].append(df[i][0])
            df_new['TEXT2'].append(df[i][1])
            df_new['MEINS'].append('1000') 
            df_new['MENGE'].append('СКЦ')
            df_new['DATUV'].append('')
            df_new['PUSTOY'].append('')
            df_new['LGORT'].append('PS05')

            t= 1
            for k in range(0,len(siryo_names)):
                if norma.data[siryo_names[k]['kratkiy']] !='0':
                    if siryo_names[k]['kratkiy'] =='Крышка радиатора' and norma.data['Тип'] =='Bimetall':
                        continue
                    j+=1
                    t+=1
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
                    df_new['POSNR'].append(t)
                    df_new['POSTP'].append('L')
                    df_new['MATNR1'].append(siryo_names[k]['sapcode'])
                    df_new['TEXT2'].append(siryo_names[k]['kratkiy'])
                    if siryo_names[k]['kratkiy'] =='Тех. отход ал стружка':
                        sap_val ='20'
                    else:
                        sap_val = norma.data[siryo_names[k]['kratkiy']].replace(' ','').replace('.0','') if norma.data[siryo_names[k]['kratkiy']][-2:]=='.0' else ("%.3f" % float(norma.data[siryo_names[k]['kratkiy']].replace(' ',''))).replace('.',',')
                    
                    df_new['MEINS'].append(sap_val if not 'отход' in siryo_names[k]['kratkiy'] else '-' + sap_val) 
                    df_new['MENGE'].append(siryo_names[k]['MEINS'])
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                    df_new['LGORT'].append('PS05')
                    
                
                        # siryo = Siryo.objects.filter(data__Краткийтекст__icontains =siryo_names[k-2]['kratkiy'])[:1].get()
        
        
        #### PR
        if {df[i][0]:df[i][1]} not in norma_exists:
            norma_exists.append({df[i][0]:df[i][1]})
            df_new['ID'].append('1')
            df_new['MATNR'].append(df[i][0])
            df_new['WERKS'].append('5101')
            df_new['TEXT1'].append(df[i][1])
            df_new['STLAL'].append('1')
            df_new['STLAN'].append('1')
            df_new['ZTEXT'].append(df[i][1])
            df_new['STKTX'].append('Пресс')
            df_new['BMENG'].append( '1000')
            df_new['BMEIN'].append('СКЦ')
            df_new['STLST'].append('1')
            df_new['POSNR'].append('')
            df_new['POSTP'].append('')
            df_new['MATNR1'].append('')
            df_new['TEXT2'].append('')
            df_new['MEINS'].append('')
            df_new['MENGE'].append('')
            df_new['DATUV'].append('01012023')
            df_new['PUSTOY'].append('')
            df_new['LGORT'].append('')
            for k in range(1,3):
                j+=1
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
                df_new['POSNR'].append(k)
                df_new['POSTP'].append('L')
                
                
                if k == 1 :
                    df_new['MATNR1'].append('1000006841')
                    df_new['TEXT2'].append('Сплав AK12')
                    df_new['MEINS'].append(norma.data['расход сплава АК 12 на 1000 секции'].replace('.0','')  if norma.data['расход сплава АК 12 на 1000 секции'][-2:]=='.0' else ("%.3f" % float(norma.data['расход сплава АК 12 на 1000 секции'])).replace('.',',')) 
                    df_new['MENGE'].append('КГ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                # if k == 2 :
                #     df_new['MATNR1'].append('1000004484')
                #     df_new['TEXT2'].append('Тех. отход литник')
                #     df_new['MEINS'].append('-'+norma.data['Тех. отход литник'].replace('.0','') if norma.data['Тех. отход литник'][-2:]=='.0' else '-' + ("%.3f" % float(norma.data['Тех. отход литник'])).replace('.',',')) 
                #     df_new['MENGE'].append('КГ')
                #     df_new['DATUV'].append('')
                #     df_new['PUSTOY'].append('')
                    
                # if k == 3 :
                #     df_new['MATNR1'].append('1900007455')
                #     df_new['TEXT2'].append('Тех. отход промывка')
                #     df_new['MEINS'].append('-'+norma.data['Тех. отход промывка'].replace('.0','') if norma.data['Тех. отход промывка'][-2:]=='.0' else '-' + ("%.3f" % float(norma.data['Тех. отход промывка'])).replace('.',','))
                #     df_new['MENGE'].append('КГ')
                #     df_new['DATUV'].append('')
                #     df_new['PUSTOY'].append('')

                # if k == 4 :
                #     df_new['MATNR1'].append('1900007457')
                #     df_new['TEXT2'].append('Тех. отход шлак масло')
                #     df_new['MEINS'].append('-'+norma.data['Тех. отход шлак масло'].replace('.0','') if norma.data['Тех. отход шлак масло'][-2:]=='.0' else '-' + ("%.3f" % float(norma.data['Тех. отход шлак масло'])).replace('.',','))
                #     df_new['MENGE'].append('КГ')
                #     df_new['DATUV'].append('')
                #     df_new['PUSTOY'].append('')
                if k == 2 :
                    df_new['MATNR1'].append('1000006701')
                    df_new['TEXT2'].append('Сож для прес-формы')
                    df_new['MEINS'].append(norma.data['Сож для прес-формы'].replace('.0','') if norma.data['Сож для прес-формы'][-2:]=='.0' else  ("%.3f" % float(norma.data['Сож для прес-формы'])).replace('.',','))
                    df_new['MENGE'].append('Л')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                # if k == 3 :
                #     df_new['MATNR1'].append('1000004353')
                #     df_new['TEXT2'].append('Огнеупорная смазка Pyro-Mastic')
                #     df_new['MEINS'].append(norma.data['Огнеупорная смазка Pyro-Mastic'].replace('.0','') if norma.data['Огнеупорная смазка Pyro-Mastic'][-2:]=='.0' else ("%.3f" % float(norma.data['Огнеупорная смазка Pyro-Mastic'])).replace('.',','))
                #     df_new['MENGE'].append('КГ')
                #     df_new['DATUV'].append('')
                #     df_new['PUSTOY'].append('')
                df_new['LGORT'].append('PS02')
            
            if norma.data['Тип'] =='Bimetall':
                if '16' in norma.data['Вставка биметалл']: 
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
                    df_new['POSNR'].append(3)
                    df_new['POSTP'].append('L')
                    df_new['MATNR1'].append('1000006842')
                    df_new['TEXT2'].append('Вставка для радиатора 16 мм')
                    df_new['MEINS'].append('1000') 
                    df_new['MENGE'].append('ШТ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                    df_new['LGORT'].append('PS02')
                else:
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
                    df_new['POSNR'].append(3)
                    df_new['POSTP'].append('L')
                    df_new['MATNR1'].append('1000006843')
                    df_new['TEXT2'].append('Вставка для радиатора 18 мм')
                    df_new['MEINS'].append('1000') 
                    df_new['MENGE'].append('ШТ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                    df_new['LGORT'].append('PS02')


    for i in range(0,len(df_aurora)):
        # print(i)
        
        artikul = df_aurora[i][6].split('-')[0]
        # print(artikul,'norma')

        party = str(df_aurora[i][2]).split('-')[0].split('.')[2]

        profile_val =PROFIL_TYPE['prof_type'][party]
        kraska_val =PROFIL_TYPE['kraska'][party]
        plenka_val =PROFIL_TYPE['plenka'][party]

        pokraska_code = str(df_aurora[i][5]).split(' ')[-1]
        # kraska_data = Kraska.objects.filter(data__CODE__icontains=pokraska_code)
        # print(kraska_data)
        # continue
        kraska_data = Kraska.objects.filter(data__CODE__icontains=pokraska_code)[:1].get().data

        

        ### 7  ###
        if {df_aurora[i][6]:df_aurora[i][7]} not in norma_exists:
            norma_exists.append({df_aurora[i][6]:df_aurora[i][7]})
            df_new_aurora['ID'].append('1')
            df_new_aurora['MATNR'].append(df_aurora[i][6])
            df_new_aurora['WERKS'].append('5101')
            df_new_aurora['TEXT1'].append(df_aurora[i][7])
            df_new_aurora['STLAL'].append('1')
            df_new_aurora['STLAN'].append('1')
            df_new_aurora['ZTEXT'].append(df_aurora[i][7])
            df_new_aurora['STKTX'].append('Упаковка')
            df_new_aurora['BMENG'].append( '1000')
            df_new_aurora['BMEIN'].append('ШТ')
            df_new_aurora['STLST'].append('1')
            df_new_aurora['POSNR'].append('')
            df_new_aurora['POSTP'].append('')
            df_new_aurora['MATNR1'].append('')
            df_new_aurora['TEXT2'].append('')
            df_new_aurora['MEINS'].append('')
            df_new_aurora['MENGE'].append('')
            df_new_aurora['DATUV'].append('01012023')
            df_new_aurora['PUSTOY'].append('')
            df_new_aurora['LGORT'].append('')
            # print(df[i][4],df[i][5])
            seksiya_list =df_aurora[i][7].split(' ')
            text =''
            for sek in seksiya_list:
                if '-' in sek:
                    text = sek
                    break
            seksiya = text.split('-')[1]

            df_new_aurora['ID'].append('2')
            df_new_aurora['MATNR'].append('')
            df_new_aurora['WERKS'].append('')
            df_new_aurora['TEXT1'].append('')
            df_new_aurora['STLAL'].append('')
            df_new_aurora['STLAN'].append('')
            df_new_aurora['ZTEXT'].append('')
            df_new_aurora['STKTX'].append('')
            df_new_aurora['BMENG'].append('')
            df_new_aurora['BMEIN'].append('')
            df_new_aurora['STLST'].append('')
            df_new_aurora['POSNR'].append('1')
            df_new_aurora['POSTP'].append('L')
            df_new_aurora['MATNR1'].append(df_aurora[i][4])
            df_new_aurora['TEXT2'].append(df_aurora[i][5])
            df_new_aurora['MEINS'].append(int(seksiya)*1000) 
            df_new_aurora['MENGE'].append('СКЦ')
            df_new_aurora['DATUV'].append('')
            df_new_aurora['PUSTOY'].append('')
            df_new_aurora['LGORT'].append('PS08')
            
            
            krat = df_aurora[i][7].split('-')
            seria = krat[0]
            korobka_type = krat[1].split(' ')[-1]

           
            if Korobka.objects.filter(data__KOROBKA__icontains=seria,data__TYPE__icontains =korobka_type).exists():
                korobka = Korobka.objects.filter(data__KOROBKA__icontains=seria,data__TYPE__icontains =korobka_type)[:1].get()
                df_new_aurora['ID'].append('2')
                df_new_aurora['MATNR'].append('')
                df_new_aurora['WERKS'].append('')
                df_new_aurora['TEXT1'].append('')
                df_new_aurora['STLAL'].append('')
                df_new_aurora['STLAN'].append('')
                df_new_aurora['ZTEXT'].append('')
                df_new_aurora['STKTX'].append('')
                df_new_aurora['BMENG'].append('')
                df_new_aurora['BMEIN'].append('')
                df_new_aurora['STLST'].append('')
                df_new_aurora['POSNR'].append('2')
                df_new_aurora['POSTP'].append('L')
                df_new_aurora['MATNR1'].append(korobka.data['MATNR'])
                df_new_aurora['TEXT2'].append(korobka.data['MAKTX'])
                # sap_val = '1000' if 'BK' not in korobka_type else '2000'
                df_new_aurora['MEINS'].append('1000') 
                df_new_aurora['MENGE'].append('ШТ')
                df_new_aurora['DATUV'].append('')
                df_new_aurora['PUSTOY'].append('')
                df_new_aurora['LGORT'].append('PS08')
            
            for k in range(1,2):
                j+=1
                df_new_aurora['ID'].append('2')
                df_new_aurora['MATNR'].append('')
                df_new_aurora['WERKS'].append('')
                df_new_aurora['TEXT1'].append('')
                df_new_aurora['STLAL'].append('')
                df_new_aurora['STLAN'].append('')
                df_new_aurora['ZTEXT'].append('')
                df_new_aurora['STKTX'].append('')
                df_new_aurora['BMENG'].append('')
                df_new_aurora['BMEIN'].append('')
                df_new_aurora['STLST'].append('')
                df_new_aurora['POSNR'].append('3')
                df_new_aurora['POSTP'].append('L')
                
                
                if k == 1 :
                    seksiya_list =df_aurora[i][7].split(' ')
                    text =''
                    for sek in seksiya_list:
                        if '-' in sek:
                            text = sek
                            break
                    seksiya = text.split('-')[1]

                    matrn_ =''
                    sapcode_ =''

        
                    if seksiya =='03':
                        matrn_ ='Воз.пузырчатая 3-х сл.пол.пленка 90см'
                        sapcode_='1900012700'
                    elif seksiya =='04':
                        matrn_ ='Воз.пузырчатая 3-х сл.пол.пленка 90см'
                        sapcode_='1900012700'
                    if seksiya =='05':
                        matrn_ ='Воз.пузырчатая 2-х сл.пол.пленка 125см'
                        sapcode_='1900012669'
                    elif seksiya =='06':
                        matrn_ ='Воз.пузырчатая 2-х сл.пол.пленка 125см'
                        sapcode_='1900012669'
                    


                    df_new_aurora['MATNR1'].append(sapcode_)
                    df_new_aurora['TEXT2'].append(matrn_)
                    df_new_aurora['MEINS'].append(plenka_val) 
                    df_new_aurora['MENGE'].append('М')
                    df_new_aurora['DATUV'].append('')
                    df_new_aurora['PUSTOY'].append('')
                    
                
                df_new_aurora['LGORT'].append('PS08')


        
        #### PK
        if {df_aurora[i][4]:df_aurora[i][5]} not in norma_exists:
            norma_exists.append({df_aurora[i][4]:df_aurora[i][5]})
            df_new_aurora['ID'].append('1')
            df_new_aurora['MATNR'].append(df_aurora[i][4])
            df_new_aurora['WERKS'].append('5101')
            df_new_aurora['TEXT1'].append(df_aurora[i][5])
            df_new_aurora['STLAL'].append('1')
            df_new_aurora['STLAN'].append('1')
            df_new_aurora['ZTEXT'].append(df_aurora[i][5])
            df_new_aurora['STKTX'].append('Покраска')
            df_new_aurora['BMENG'].append( '1000')
            df_new_aurora['BMEIN'].append('СКЦ')
            df_new_aurora['STLST'].append('1')
            df_new_aurora['POSNR'].append('')
            df_new_aurora['POSTP'].append('')
            df_new_aurora['MATNR1'].append('')
            df_new_aurora['TEXT2'].append('')
            df_new_aurora['MEINS'].append('')
            df_new_aurora['MENGE'].append('')
            df_new_aurora['DATUV'].append('01012023')
            df_new_aurora['PUSTOY'].append('')
            df_new_aurora['LGORT'].append('')
            
            for k in range(1,3):
                j+=1
                df_new_aurora['ID'].append('2')
                df_new_aurora['MATNR'].append('')
                df_new_aurora['WERKS'].append('')
                df_new_aurora['TEXT1'].append('')
                df_new_aurora['STLAL'].append('')
                df_new_aurora['STLAN'].append('')
                df_new_aurora['ZTEXT'].append('')
                df_new_aurora['STKTX'].append('')
                df_new_aurora['BMENG'].append('')
                df_new_aurora['BMEIN'].append('')
                df_new_aurora['STLST'].append('')
                df_new_aurora['POSNR'].append(k)
                df_new_aurora['POSTP'].append('L')
                
                
                if k == 1 :
                    
                    df_new_aurora['MATNR1'].append(df_aurora[i][2])
                    df_new_aurora['TEXT2'].append(df_aurora[i][3])
                    df_new_aurora['MEINS'].append('1000') 
                    df_new_aurora['MENGE'].append('СКЦ')
                    df_new_aurora['DATUV'].append('')
                    df_new_aurora['PUSTOY'].append('')

                if k == 2 :
                    
                    df_new_aurora['MATNR1'].append(kraska_data['MATNR'])
                    df_new_aurora['TEXT2'].append(kraska_data['MAKTX'])
                    df_new_aurora['MEINS'].append(kraska_val) 
                    df_new_aurora['MENGE'].append('КГ')
                    df_new_aurora['DATUV'].append('')
                    df_new_aurora['PUSTOY'].append('')
               

                    
                df_new_aurora['LGORT'].append('PS10')
        
       
        #### ER
        if {df_aurora[i][2]:df_aurora[i][3]} not in norma_exists:
            norma_exists.append({df_aurora[i][2]:df_aurora[i][3]})
            df_new_aurora['ID'].append('1')
            df_new_aurora['MATNR'].append(df_aurora[i][2])
            df_new_aurora['WERKS'].append('5101')
            df_new_aurora['TEXT1'].append(df_aurora[i][3])
            df_new_aurora['STLAL'].append('1')
            df_new_aurora['STLAN'].append('1')
            df_new_aurora['ZTEXT'].append(df_aurora[i][3])
            df_new_aurora['STKTX'].append('Extrusion')
            df_new_aurora['BMENG'].append( '1000')
            df_new_aurora['BMEIN'].append('СКЦ')
            df_new_aurora['STLST'].append('1')
            df_new_aurora['POSNR'].append('')
            df_new_aurora['POSTP'].append('')
            df_new_aurora['MATNR1'].append('')
            df_new_aurora['TEXT2'].append('')
            df_new_aurora['MEINS'].append('')
            df_new_aurora['MENGE'].append('')
            df_new_aurora['DATUV'].append('01012023')
            df_new_aurora['PUSTOY'].append('')
            df_new_aurora['LGORT'].append('')

            

            for k in range(1,4):
                j+=1
                df_new_aurora['ID'].append('2')
                df_new_aurora['MATNR'].append('')
                df_new_aurora['WERKS'].append('')
                df_new_aurora['TEXT1'].append('')
                df_new_aurora['STLAL'].append('')
                df_new_aurora['STLAN'].append('')
                df_new_aurora['ZTEXT'].append('')
                df_new_aurora['STKTX'].append('')
                df_new_aurora['BMENG'].append('')
                df_new_aurora['BMEIN'].append('')
                df_new_aurora['STLST'].append('')
                df_new_aurora['POSNR'].append(k)
                df_new_aurora['POSTP'].append('L')
                
                
                if k == 1 :
                    df_new_aurora['MATNR1'].append(df_aurora[i][0])
                    df_new_aurora['TEXT2'].append(df_aurora[i][1])
                    df_new_aurora['MEINS'].append('1000') 
                    df_new_aurora['MENGE'].append('СКЦ')
                    df_new_aurora['DATUV'].append('')
                    df_new_aurora['PUSTOY'].append('')

                
                
                if k == 2 :
                    df_new_aurora['MATNR1'].append('1000006722')
                    df_new_aurora['TEXT2'].append('Паронит межсекционная')
                    df_new_aurora['MEINS'].append('1926')
                    df_new_aurora['MENGE'].append('ШТ')
                    df_new_aurora['DATUV'].append('')
                    df_new_aurora['PUSTOY'].append('')
                if k == 3 :
                    df_new_aurora['MATNR1'].append('1000006721')
                    df_new_aurora['TEXT2'].append('Соеденительная муфта')
                    df_new_aurora['MEINS'].append('1836')
                    df_new_aurora['MENGE'].append('ШТ')
                    df_new_aurora['DATUV'].append('')
                    df_new_aurora['PUSTOY'].append('')
                df_new_aurora['LGORT'].append('PS10')
            
       
        #### ES
        if {df_aurora[i][0]:df_aurora[i][1]} not in norma_exists:
            norma_exists.append({df_aurora[i][0]:df_aurora[i][1]})
            df_new_aurora['ID'].append('1')
            df_new_aurora['MATNR'].append(df_aurora[i][0])
            df_new_aurora['WERKS'].append('5101')
            df_new_aurora['TEXT1'].append(df_aurora[i][1])
            df_new_aurora['STLAL'].append('1')
            df_new_aurora['STLAN'].append('1')
            df_new_aurora['ZTEXT'].append(df_aurora[i][1])
            df_new_aurora['STKTX'].append('Extrusion')
            df_new_aurora['BMENG'].append( '1000')
            df_new_aurora['BMEIN'].append('СКЦ')
            df_new_aurora['STLST'].append('1')
            df_new_aurora['POSNR'].append('')
            df_new_aurora['POSTP'].append('')
            df_new_aurora['MATNR1'].append('')
            df_new_aurora['TEXT2'].append('')
            df_new_aurora['MEINS'].append('')
            df_new_aurora['MENGE'].append('')
            df_new_aurora['DATUV'].append('01012023')
            df_new_aurora['PUSTOY'].append('')
            df_new_aurora['LGORT'].append('')

            

            for k in range(1,4):
                j+=1
                df_new_aurora['ID'].append('2')
                df_new_aurora['MATNR'].append('')
                df_new_aurora['WERKS'].append('')
                df_new_aurora['TEXT1'].append('')
                df_new_aurora['STLAL'].append('')
                df_new_aurora['STLAN'].append('')
                df_new_aurora['ZTEXT'].append('')
                df_new_aurora['STKTX'].append('')
                df_new_aurora['BMENG'].append('')
                df_new_aurora['BMEIN'].append('')
                df_new_aurora['STLST'].append('')
                df_new_aurora['POSNR'].append(k)
                df_new_aurora['POSTP'].append('L')
                
                
                if k == 1 :
                    df_new_aurora['MATNR1'].append('1000006849')
                    df_new_aurora['TEXT2'].append('КОЛЛЕКТОР РАДИАТОРА AURORA')
                    df_new_aurora['MEINS'].append('2000') 
                    df_new_aurora['MENGE'].append('ШТ')
                    df_new_aurora['DATUV'].append('')
                    df_new_aurora['PUSTOY'].append('')

                
                
                if k == 2 :
                    df_new_aurora['MATNR1'].append('1000006695')
                    df_new_aurora['TEXT2'].append('RDF55.R0002-7001 профиль')
                    df_new_aurora['MEINS'].append(profile_val)
                    df_new_aurora['MENGE'].append('М')
                    df_new_aurora['DATUV'].append('')
                    df_new_aurora['PUSTOY'].append('')
                if k == 3 :
                    df_new_aurora['MATNR1'].append('1000006839')
                    df_new_aurora['TEXT2'].append('Клей для соедениние коллектора AURORA')
                    df_new_aurora['MEINS'].append('4')
                    df_new_aurora['MENGE'].append('КГ')
                    df_new_aurora['DATUV'].append('')
                    df_new_aurora['PUSTOY'].append('')
                df_new_aurora['LGORT'].append('PS10')
            
       
        
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%d.%m.%Y_%H.%M")    
                 
            
    create_folder(f'{MEDIA_ROOT}\\uploads','norma-radiator')
    create_folder(f'{MEDIA_ROOT}\\uploads\\norma-radiator',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\norma-radiator\\{year}',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\norma-radiator\\{year}\\{month}',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\norma-radiator\\{year}\\{month}\\{day}',hour)
            
            
    
    path =f'{MEDIA_ROOT}\\uploads\\norma-radiator\\{year}\\{month}\\{day}\\{hour}\\NORMA_RADIATOR_{minut}.xlsx'
    

    # for key,row in df_new.items():
    #     print(key,len(row))

    dff = pd.DataFrame(df_new)
    dff2 = pd.DataFrame(df_new_aurora)
    


    writer = pd.ExcelWriter(path, engine='openpyxl')
    dff.to_excel(writer,index=False,sheet_name ='Norma')
    dff2.to_excel(writer,index=False,sheet_name ='Norma Aurora')
    
    
    writer.close()

    
    file =[File(file=path,filetype='obichniy',id=id)]
    context = {
            'files':file,
            'section':f'Формированый {file_content} файл'
      }
    return render(request,'norma/benkam/generated_files.html',context)



def create_folder(parent_dir,directory):
    path =os.path.join(parent_dir,directory)
    if not os.path.isdir(path):
        os.mkdir(path)

class File:
    def __init__(self,file,filetype,id):
        self.file =file
        self.filetype =filetype
        self.id = id


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator','universal_user'])
def lenght_generate_texcarta(request,id):
    file = NormaExcelFiles.objects.get(id=id).file
    file_path =f'{MEDIA_ROOT}\\{file}'
    df =pd.read_excel(file_path)

    df =df.astype(str)
    df=df.replace('nan','')


    # print(df,'+' * 50)

    counter = 500
    for key,row in df.iterrows():
        if not TexcartaBase.objects.filter(material = row['МАТЕРИАЛ']).exists():
            # print(row['МАТЕРИАЛ'])
            if '-PR' in row['МАТЕРИАЛ']:
                counter +=2
            elif '-MO' in row['МАТЕРИАЛ']:
                counter +=25
            elif '-PM' in row['МАТЕРИАЛ']:
                counter +=2
            elif '-PK' in row['МАТЕРИАЛ']:
                counter +=4
            elif '-ER' in row['МАТЕРИАЛ']:
                counter +=4
            elif '-ES' in row['МАТЕРИАЛ']:
                counter +=4
            elif '-7' in row['МАТЕРИАЛ']:
                counter +=2
       
    # print(counter)
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
    
    # print(df_new,'lllll')

    counter_2 = 0
    for key,row in df.iterrows():
        if not TexcartaBase.objects.filter(material = row['МАТЕРИАЛ']).exists():
            length = row['МАТЕРИАЛ'].split('-')[0]
            # print(row['МАТЕРИАЛ'],'ddd')
            norma = Norma.objects.filter(data__Артикул__icontains=length)[:1].get()
            
            if '-PR' in row['МАТЕРИАЛ']:
                for i in range(1,3):
                    if i ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='5101'
                        df_new['STTAG'][counter_2] ='01012023'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'     
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] ='0010'
                        df_new['ARBPL'][counter_2] ='5101A301'
                        df_new['WERKS1'][counter_2] ='5101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] ='Пресс'
                        df_new['BMSCH'][counter_2] = '1000'
                        df_new['MEINH'][counter_2] ='SKC'
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] ='200003'
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = '1'
                        df_new['UMREN'][counter_2] = '1'
                        df_new['USR00'][counter_2] = '1'
                        df_new['USR01'][counter_2] = '60'
                       
                   
                    counter_2 +=1
                TexcartaBase(material = row['МАТЕРИАЛ']).save()
            
            if '-ES' in row['МАТЕРИАЛ']:
                for i in range(1,3):
                    if i ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='5101'
                        df_new['STTAG'][counter_2] ='01012023'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] ='0010'
                        df_new['ARBPL'][counter_2] ='5101B502'
                        df_new['WERKS1'][counter_2] ='5101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] ='Участок радиторов из профилей'
                        df_new['BMSCH'][counter_2] = '1000'
                        df_new['MEINH'][counter_2] ='SKC'
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] ='200320'
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = '1'
                        df_new['UMREN'][counter_2] = '1'
                        df_new['USR00'][counter_2] = '1'
                        df_new['USR01'][counter_2] = '60'
                        # df_new['UMREZ'][counter_2] = '1000'
                        # df_new['UMREN'][counter_2] = int(float(norma.data['Площадь поверхности 1000шт профилей/м²'].replace(',','.'))*float(L)/(6))
                        # df_new['USR00'][counter_2] = '1'
                        # df_new['USR01'][counter_2] = ("%.3f" % ((L*1000*3600*float(norma.data['Площадь поверхности 1000шт профилей/м²'].replace(',','.')))/(6000000*bmsch)))
                       
                   
                    counter_2 +=1
                TexcartaBase(material = row['МАТЕРИАЛ']).save()
            
            if '-ER' in row['МАТЕРИАЛ']:
                for i in range(1,3):
                    if i ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='5101'
                        df_new['STTAG'][counter_2] ='01012023'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] ='0010'
                        df_new['ARBPL'][counter_2] ='5101B501'
                        df_new['WERKS1'][counter_2] ='5101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] ='Участок радиторов из профилей'
                        df_new['BMSCH'][counter_2] = '1000'
                        df_new['MEINH'][counter_2] ='SKC'
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] ='200320'
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = '1'
                        df_new['UMREN'][counter_2] = '1'
                        df_new['USR00'][counter_2] = '1'
                        df_new['USR01'][counter_2] = '60'
                        # df_new['UMREZ'][counter_2] = '1000'
                        # df_new['UMREN'][counter_2] = int(float(norma.data['Площадь поверхности 1000шт профилей/м²'].replace(',','.'))*float(L)/(6))
                        # df_new['USR00'][counter_2] = '1'
                        # df_new['USR01'][counter_2] = ("%.3f" % ((L*1000*3600*float(norma.data['Площадь поверхности 1000шт профилей/м²'].replace(',','.')))/(6000000*bmsch)))
                       
                   
                    counter_2 +=1
                TexcartaBase(material = row['МАТЕРИАЛ']).save()
            
            if '-PM' in row['МАТЕРИАЛ']:
                for i in range(1,3):
                    if i ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='5101'
                        df_new['STTAG'][counter_2] ='01012023'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] ='0010'
                        df_new['ARBPL'][counter_2] ='5101B201'
                        df_new['WERKS1'][counter_2] ='5101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] ='PUMA'
                        df_new['BMSCH'][counter_2] = '1000'
                        df_new['MEINH'][counter_2] ='SKC'
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] ='200280'
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = '1'
                        df_new['UMREN'][counter_2] = '1'
                        df_new['USR00'][counter_2] = '1'
                        df_new['USR01'][counter_2] = '60'
                        # df_new['UMREZ'][counter_2] = '1000'
                        # df_new['UMREN'][counter_2] = int(float(norma.data['Площадь поверхности 1000шт профилей/м²'].replace(',','.'))*float(L)/(6))
                        # df_new['USR00'][counter_2] = '1'
                        # df_new['USR01'][counter_2] = ("%.3f" % ((L*1000*3600*float(norma.data['Площадь поверхности 1000шт профилей/м²'].replace(',','.')))/(6000000*bmsch)))
                       
                   
                    counter_2 +=1
                TexcartaBase(material = row['МАТЕРИАЛ']).save()
            
            if '-PK' in row['МАТЕРИАЛ']:
                for i in range(1,3):
                    if i ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='5101'
                        df_new['STTAG'][counter_2] ='01012023'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] ='0010'
                        df_new['ARBPL'][counter_2] ='5101B511'
                        df_new['WERKS1'][counter_2] ='5101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] ='Покраска'
                        df_new['BMSCH'][counter_2] = '1000'
                        df_new['MEINH'][counter_2] ='SKC'
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] ='200040'
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = '1'
                        df_new['UMREN'][counter_2] = '1'
                        df_new['USR00'][counter_2] = '1'
                        df_new['USR01'][counter_2] = '60'
                        # df_new['UMREZ'][counter_2] = '1000'
                        # df_new['UMREN'][counter_2] = int(float(norma.data['Площадь поверхности 1000шт профилей/м²'].replace(',','.'))*float(L)/(6))
                        # df_new['USR00'][counter_2] = '1'
                        # df_new['USR01'][counter_2] = ("%.3f" % ((L*1000*3600*float(norma.data['Площадь поверхности 1000шт профилей/м²'].replace(',','.')))/(6000000*bmsch)))
                       
                   
                    counter_2 +=1
                TexcartaBase(material = row['МАТЕРИАЛ']).save()
            
            if '-7' in row['МАТЕРИАЛ']:
                for i in range(1,3):
                    if i ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='5101'
                        df_new['STTAG'][counter_2] ='01012023'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] =row['КРАТКИЙ ТЕКСТ']
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] ='0010'
                        df_new['ARBPL'][counter_2] ='5101B521'
                        df_new['WERKS1'][counter_2] ='5101'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] ='Упаковка'
                        df_new['BMSCH'][counter_2] = '1000'
                        df_new['MEINH'][counter_2] ='ST'
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] ='200080'
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = '1'
                        df_new['UMREN'][counter_2] = '1'
                        df_new['USR00'][counter_2] = '1'
                        df_new['USR01'][counter_2] = '60'
                        # df_new['UMREZ'][counter_2] = '1000'
                        # df_new['UMREN'][counter_2] = int(float(norma.data['Площадь поверхности 1000шт профилей/м²'].replace(',','.'))*float(L)/(6))
                        # df_new['USR00'][counter_2] = '1'
                        # df_new['USR01'][counter_2] = ("%.3f" % ((L*1000*3600*float(norma.data['Площадь поверхности 1000шт профилей/м²'].replace(',','.')))/(6000000*bmsch)))
                       
                   
                    counter_2 +=1
                TexcartaBase(material = row['МАТЕРИАЛ']).save()

            
            if '-MO' in row['МАТЕРИАЛ']:
                
                type_art = norma.data['Тип']
                if type_art.upper() =='ALUMIN':
                    opisaniye =[
                        ['Сварка','Тест Сварки','Фреза','Барабан','Резьба и Торцовка','Шлифовка','Сборка','Тест Сборки'],
                        ['5101B111','5101B112','5101B121','5101B131','5101B141','5101B151','5101B161','5101B162']]
                    for j in range(1,4):
                        if j ==1:
                            for i in range(1,10):
                                if i ==1:
                                    df_new['ID'][counter_2] ='1'
                                    df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                    df_new['WERKS'][counter_2] ='5101'
                                    df_new['STTAG'][counter_2] ='01012023'
                                    df_new['PLNAL'][counter_2] ='1'
                                    df_new['KTEXT'][counter_2] ='МехОбработка Ручная'
                                    df_new['VERWE'][counter_2] ='1'
                                    df_new['STATU'][counter_2] ='4'
                                    df_new['LOSVN'][counter_2] ='1'
                                    df_new['LOSBS'][counter_2] ='99999999'
                                elif i >= 2:
                                    df_new['ID'][counter_2]='2'
                                    df_new['VORNR'][counter_2] =f'00{i-1}0'
                                    df_new['ARBPL'][counter_2] =opisaniye[1][i-2]
                                    df_new['WERKS1'][counter_2] ='5101'
                                    df_new['STEUS'][counter_2] ='ZK01'
                                    df_new['LTXA1'][counter_2] =opisaniye[0][i-2]
                                    df_new['BMSCH'][counter_2] = '1000'
                                    df_new['MEINH'][counter_2] ='SKC'
                                    df_new['VGW01'][counter_2] ='24'
                                    df_new['VGE01'][counter_2] ='STD'
                                    df_new['ACTTYPE_01'][counter_2] ='200280' if 'Тест Сборки' == opisaniye[0][i-2] else ''
                                    df_new['CKSELKZ'][counter_2] ='X' if 'Тест Сборки' == opisaniye[0][i-2] else ''
                                    df_new['UMREZ'][counter_2] = '1'
                                    df_new['UMREN'][counter_2] = '1'
                                    df_new['USR00'][counter_2] = '1'
                                    df_new['USR01'][counter_2] = '60'
                                    
                            
                                counter_2 +=1
                        if j==2:        
                            for i in range(1,3):
                                if i ==1:
                                    df_new['ID'][counter_2] ='1'
                                    df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                    df_new['WERKS'][counter_2] ='5101'
                                    df_new['STTAG'][counter_2] ='01012023'
                                    df_new['PLNAL'][counter_2] ='1'
                                    df_new['KTEXT'][counter_2] ='МехОбработка Gi Zeta'
                                    df_new['VERWE'][counter_2] ='1'
                                    df_new['STATU'][counter_2] ='4'
                                    df_new['LOSVN'][counter_2] ='1'
                                    df_new['LOSBS'][counter_2] ='99999999'
                                elif i == 2:
                                    df_new['ID'][counter_2]='2'
                                    df_new['VORNR'][counter_2] ='0010'
                                    df_new['ARBPL'][counter_2] ='5101B301'
                                    df_new['WERKS1'][counter_2] ='5101'
                                    df_new['STEUS'][counter_2] ='ZK01'
                                    df_new['LTXA1'][counter_2] ='МехОбработка Gi Zeta'
                                    df_new['BMSCH'][counter_2] = '1000'
                                    df_new['MEINH'][counter_2] ='SKC'
                                    df_new['VGW01'][counter_2] ='24'
                                    df_new['VGE01'][counter_2] ='STD'
                                    df_new['ACTTYPE_01'][counter_2] ='200281'
                                    df_new['CKSELKZ'][counter_2] ='X'
                                    df_new['UMREZ'][counter_2] = '1'
                                    df_new['UMREN'][counter_2] = '1'
                                    df_new['USR00'][counter_2] = '1'
                                    df_new['USR01'][counter_2] = '60'
                                counter_2 +=1
                        if j==3:        
                            for i in range(1,3):
                                if i ==1:
                                    df_new['ID'][counter_2] ='1'
                                    df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                    df_new['WERKS'][counter_2] ='5101'
                                    df_new['STTAG'][counter_2] ='01012023'
                                    df_new['PLNAL'][counter_2] ='1'
                                    df_new['KTEXT'][counter_2] ='МехОбработка S.A.I.P.'
                                    df_new['VERWE'][counter_2] ='1'
                                    df_new['STATU'][counter_2] ='4'
                                    df_new['LOSVN'][counter_2] ='1'
                                    df_new['LOSBS'][counter_2] ='99999999'
                                elif i == 2:
                                    df_new['ID'][counter_2]='2'
                                    df_new['VORNR'][counter_2] ='0010'
                                    df_new['ARBPL'][counter_2] ='5101B401'
                                    df_new['WERKS1'][counter_2] ='5101'
                                    df_new['STEUS'][counter_2] ='ZK01'
                                    df_new['LTXA1'][counter_2] ='МехОбработка S.A.I.P.'
                                    df_new['BMSCH'][counter_2] = '1000'
                                    df_new['MEINH'][counter_2] ='SKC'
                                    df_new['VGW01'][counter_2] ='24'
                                    df_new['VGE01'][counter_2] ='STD'
                                    df_new['ACTTYPE_01'][counter_2] ='200282'
                                    df_new['CKSELKZ'][counter_2] ='X'
                                    df_new['UMREZ'][counter_2] = '1'
                                    df_new['UMREN'][counter_2] = '1'
                                    df_new['USR00'][counter_2] = '1'
                                    df_new['USR01'][counter_2] = '60'
                                counter_2 +=1
                if type_art.upper() =='BIMETALL': 
                    opisaniye =[
                        ['Барабан','Торцовка','Шлифовка','Сборка','Тест Сборки'],
                        ['5101B131','5101B141','5101B151','5101B161','5101B162']]
                    for j in range(1,4):
                        if j ==1:
                            for i in range(1,7):
                                if i ==1:
                                    df_new['ID'][counter_2] ='1'
                                    df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                    df_new['WERKS'][counter_2] ='5101'
                                    df_new['STTAG'][counter_2] ='01012023'
                                    df_new['PLNAL'][counter_2] ='1'
                                    df_new['KTEXT'][counter_2] ='МехОбработка Ручная'
                                    df_new['VERWE'][counter_2] ='1'
                                    df_new['STATU'][counter_2] ='4'
                                    df_new['LOSVN'][counter_2] ='1'
                                    df_new['LOSBS'][counter_2] ='99999999'
                                elif i >= 2:
                                    df_new['ID'][counter_2]='2'
                                    df_new['VORNR'][counter_2] =f'00{i-1}0'
                                    df_new['ARBPL'][counter_2] =opisaniye[1][i-2]
                                    df_new['WERKS1'][counter_2] ='5101'
                                    df_new['STEUS'][counter_2] ='ZK01'
                                    df_new['LTXA1'][counter_2] =opisaniye[0][i-2]
                                    df_new['BMSCH'][counter_2] = '1000'
                                    df_new['MEINH'][counter_2] ='SKC'
                                    df_new['VGW01'][counter_2] ='24'
                                    df_new['VGE01'][counter_2] ='STD'
                                    df_new['ACTTYPE_01'][counter_2] ='200280' if 'Тест Сборки' == opisaniye[0][i-2] else ''
                                    df_new['CKSELKZ'][counter_2] ='X' if 'Тест Сборки' == opisaniye[0][i-2] else ''
                                    df_new['UMREZ'][counter_2] = '1'
                                    df_new['UMREN'][counter_2] = '1'
                                    df_new['USR00'][counter_2] = '1'
                                    df_new['USR01'][counter_2] = '60'
                                counter_2 +=1
                        if j==2:        
                            for i in range(1,3):
                                if i ==1:
                                    df_new['ID'][counter_2] ='1'
                                    df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                    df_new['WERKS'][counter_2] ='5101'
                                    df_new['STTAG'][counter_2] ='01012023'
                                    df_new['PLNAL'][counter_2] ='1'
                                    df_new['KTEXT'][counter_2] ='МехОбработка Gi Zeta'
                                    df_new['VERWE'][counter_2] ='1'
                                    df_new['STATU'][counter_2] ='4'
                                    df_new['LOSVN'][counter_2] ='1'
                                    df_new['LOSBS'][counter_2] ='99999999'
                                elif i == 2:
                                    df_new['ID'][counter_2]='2'
                                    df_new['VORNR'][counter_2] ='0010'
                                    df_new['ARBPL'][counter_2] ='5101B301'
                                    df_new['WERKS1'][counter_2] ='5101'
                                    df_new['STEUS'][counter_2] ='ZK01'
                                    df_new['LTXA1'][counter_2] ='МехОбработка Gi Zeta'
                                    df_new['BMSCH'][counter_2] = '1000'
                                    df_new['MEINH'][counter_2] ='SKC'
                                    df_new['VGW01'][counter_2] ='24'
                                    df_new['VGE01'][counter_2] ='STD'
                                    df_new['ACTTYPE_01'][counter_2] ='200281'
                                    df_new['CKSELKZ'][counter_2] ='X'
                                    df_new['UMREZ'][counter_2] = '1'
                                    df_new['UMREN'][counter_2] = '1'
                                    df_new['USR00'][counter_2] = '1'
                                    df_new['USR01'][counter_2] = '60'
                                counter_2 +=1
                        
                        if j==3:        
                            for i in range(1,3):
                                if i ==1:
                                    df_new['ID'][counter_2] ='1'
                                    df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                                    df_new['WERKS'][counter_2] ='5101'
                                    df_new['STTAG'][counter_2] ='01012023'
                                    df_new['PLNAL'][counter_2] ='1'
                                    df_new['KTEXT'][counter_2] ='МехОбработка S.A.I.P.'
                                    df_new['VERWE'][counter_2] ='1'
                                    df_new['STATU'][counter_2] ='4'
                                    df_new['LOSVN'][counter_2] ='1'
                                    df_new['LOSBS'][counter_2] ='99999999'
                                elif i == 2:
                                    df_new['ID'][counter_2]='2'
                                    df_new['VORNR'][counter_2] ='0010'
                                    df_new['ARBPL'][counter_2] ='5101B401'
                                    df_new['WERKS1'][counter_2] ='5101'
                                    df_new['STEUS'][counter_2] ='ZK01'
                                    df_new['LTXA1'][counter_2] ='МехОбработка S.A.I.P.'
                                    df_new['BMSCH'][counter_2] = '1000'
                                    df_new['MEINH'][counter_2] ='SKC'
                                    df_new['VGW01'][counter_2] ='24'
                                    df_new['VGE01'][counter_2] ='STD'
                                    df_new['ACTTYPE_01'][counter_2] ='200282'
                                    df_new['CKSELKZ'][counter_2] ='X'
                                    df_new['UMREZ'][counter_2] = '1'
                                    df_new['UMREN'][counter_2] = '1'
                                    df_new['USR00'][counter_2] = '1'
                                    df_new['USR01'][counter_2] = '60'
                                counter_2 +=1
                
                TexcartaBase(material = row['МАТЕРИАЛ']).save()





    # print(df_new,'newwwwww')
    df_new=df_new.replace('nan','')

    
    del df_new["counter"]
        
    from datetime import datetime
    now = datetime.now()
    
    s2 = now.strftime("%d.%m.%Y_%H.%M")

    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M-%S")     
            
    create_folder(f'{MEDIA_ROOT}\\uploads','texcarta_radiator')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta_radiator',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta_radiator\\{year}',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta_radiator\\{year}\\{month}',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta_radiator\\{year}\\{month}\\{day}',hour)
    
    # path7 =f'{MEDIA_ROOT}\\uploads\\texcarta_radiator\\{year}\\{month}\\{day}\\{hour}\\TK_PRISVOENIYE_{s2}.xlsx'
    # tk_prisvoeniye ={}
    # header ='WERKS\tPLNNR\tPLNAL_02\tMATNR_02'
    # tk_prisvoeniye['WERKS']=df_list_gp[0]
    # tk_prisvoeniye['PLNNR']=df_list_gp[1]
    # tk_prisvoeniye['PLNAL_02']=df_list_gp[2]
    # tk_prisvoeniye['MATNR_02']=df_list_gp[3]
  
    
    # df_tk_prisvoeniye= pd.DataFrame(tk_prisvoeniye)
    
    # df_tk_prisvoeniye.to_excel(path7,index=False)
    # np.savetxt(path7, df_tk_prisvoeniye.values,fmt='%s', delimiter="\t",header=header,comments='',encoding='ansi')


    path2 =f'{MEDIA_ROOT}\\uploads\\texcarta_radiator\\{year}\\{month}\\{day}\\{hour}\\TK_{s2}.xlsx'
    writer = pd.ExcelWriter(path2, engine='openpyxl')
    df_new.to_excel(writer,index=False,sheet_name ='TEXCARTA')
    writer.close()

    # files =[File(file =path2,filetype='simple',id=1),File(file =path7,filetype='simple',id=2),]
    context ={
        'file1':path2,
        'section':'Техкарта',

    }

   
    return render(request,'norma/radiator/generated_files_texcarta.html',context)




@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator','universal_user']) 
def update_sapcode(request):
    file =''
    df = pd.read_excel(file)
    for key,row in df.iterrows():
        if RadiatorSapCode.objects.filter(material=row['Материал']).exists():
            sap_code = RadiatorSapCode.objects.get(material =row['Материал'])
            sap_code.kratkiy_tekst_materiala = row['kratkiy']
            sap_code.save()

        if 'aurora' in str(row['kratkiy']).lower():
            if RazlovkaRadiatorAurora.objects.filter().exists():
                razlovka = RazlovkaRadiatorAurora.objects.filter()[:1].get()
                if '-ES' in row['Материал']:
                    razlovka.es_kratkiy = row['kratkiy']
                if '-ER' in row['Материал']:
                    razlovka.er_kratkiy = row['kratkiy']
                if '-PK' in row['Материал']:
                    razlovka.pk_kratkiy = row['kratkiy']
                if '-7' in row['Материал']:
                    razlovka.kratkiy7 = row['kratkiy']
                razlovka.save()
        else:
            if RazlovkaRadiator.objects.filter().exists():
                razlovka = RazlovkaRadiator.objects.filter()[:1].get()
                if '-PR' in row['Материал']:
                    razlovka.pr_kratkiy = row['kratkiy']
                if '-MO' in row['Материал']:
                    razlovka.mo_kratkiy = row['kratkiy']
                if '-PM' in row['Материал']:
                    razlovka.pm_kratkiy = row['kratkiy']
                if '-PK' in row['Материал']:
                    razlovka.pk_kratkiy = row['kratkiy']
                if '-7' in row['Материал']:
                    razlovka.kratkiy7 = row['kratkiy']
                razlovka.save()



    return JsonResponse({'a':'b'})

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])    
def product_add_second_org_radiator(request,id):
    file = RadiatorFile.objects.get(id=id).file
    if 'SHABLON' in str(file):
        df = pd.read_excel(f'{MEDIA_ROOT}/{file}')
        # df = pd.read_excel(f'c:\\OpenServer\\domains\\SHABLON_RADIATOR_XXXXX.xlsx')
    else:
        df = pd.read_excel(f'{MEDIA_ROOT}/{file}',header=4)
    
    df = df.astype(str)
    
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M")
      
    order_id = request.GET.get('order_id',None)
      


      
    aluminiy_group = RadiatorSapCode.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
    umumiy_counter={}
    for al in aluminiy_group:
        umumiy_counter[ al['artikul'] + '-' + al['section'] ] = al['total_max']
    
    aluminiy_group_termo = RadiatorSapCode.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
    umumiy_counter_termo = {}
    for al in aluminiy_group_termo:
        umumiy_counter_termo[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      
      
      
    
    for key,row in df.iterrows():
        if row['Модель'] == 'nan':
                df = df.drop(key)
    
        
    
    
    df_new = pd.DataFrame()

    df_new['counter'] =df['Артикул']

    df_new['SAP CODE P']=''
    df_new['PR - Press']=''

    df_new['SAP CODE M']=''
    df_new['MO - Mex obrabotka']=''

    df_new['SAP CODE PM']=''
    df_new['PM - Puma']=''

    df_new['SAP CODE PK']=''
    df_new['PK - Pokraska']=''
    
    df_new['SAP CODE 7']=''
    df_new['7 - Upakovka']=''

    df_new_aurora = pd.DataFrame()

    df_new_aurora['counter'] =df['Артикул']
    
    df_new_aurora['SAP CODE ES']=''
    df_new_aurora['ES - Extrusion']=''

    df_new_aurora['SAP CODE ER']=''
    df_new_aurora['ER - Extrusion']=''

    df_new_aurora['SAP CODE PK']=''
    df_new_aurora['PK - Pokraska']=''
    
    df_new_aurora['SAP CODE 7']=''
    df_new_aurora['7 - Upakovka']=''
    
    
    
    cache_for_cratkiy_text =[]
    duplicat_list =[]
    
    
    for key,row in df.iterrows():  
        df_new['PR - Press'][key] = 'PR-'+str(df['Модель'][key]).capitalize()
        df_new['MO - Mex obrabotka'][key] = 'MO-'+str(df['Модель'][key]).capitalize()
        df_new['PM - Puma'][key] = 'PM-'+str(df['Модель'][key]).capitalize()
        df_new['PK - Pokraska'][key] = 'PK-'+str(df['Модель'][key]).capitalize()+' ' +df['Цвет'][key]
        df_new['7 - Upakovka'][key] = df['Краткий текст'][key]

        df_new_aurora['ES - Extrusion'][key] = 'ES-'+str(df['Модель'][key]).capitalize()
        df_new_aurora['ER - Extrusion'][key] = 'ER-'+str(df['Модель'][key]).capitalize()
        df_new_aurora['PK - Pokraska'][key] = 'PK-'+str(df['Модель'][key]).capitalize()+' ' +df['Цвет'][key]
        df_new_aurora['7 - Upakovka'][key] = str(df['Краткий текст'][key]).upper().replace('AURORA','Aurora')
        
        
        if ((row['Название'] == 'nan') or (row['Название'] == '')):
            online_savdo_name = ''
        else:
            online_savdo_name = row['Название']
            
            
        if ((row['Online savdo ID'] == 'nan') or (row['Online savdo ID'] == '')):
            id_savdo = 'XXXXX'
        else:
            id_savdo = str(row['Online savdo ID']).replace('.0','')

        


        if 'aurora' in str(df['Модель'][key]).lower():
            for i in range(1,5):
                if i == 1:
                    if RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='ES',kratkiy_tekst_materiala= df_new_aurora['ES - Extrusion'][key]).exists():
                        df_new_aurora['SAP CODE ES'][key] = RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='ES',kratkiy_tekst_materiala=df_new_aurora['ES - Extrusion'][key])[:1].get().material
                        duplicat_list.append([df_new_aurora['SAP CODE ES'][key],df_new_aurora['ES - Extrusion'][key],'ES'])
                    else: 
                        if RadiatorSapCode.objects.filter(artikul=df['Артикул'][key],section ='ES').exists():
                                umumiy_counter[df['Артикул'][key]+'-ES'] += 1
                                max_valuesES = umumiy_counter[df['Артикул'][key]+'-ES']
                                materiale = df['Артикул'][key]+"-ES{:02d}".format(max_valuesES)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='ES',counter=max_valuesES,kratkiy_tekst_materiala=df_new_aurora['ES - Extrusion'][key],material=materiale).save()
                                df_new_aurora['SAP CODE ES'][key] = materiale
                                
                                cache_for_cratkiy_text.append({
                                                    'kratkiy':df_new_aurora['ES - Extrusion'][key],
                                                    'sap_code':  materiale,
                                                    
                                                    # 'system' : row['Название системы'],
                                                    # 'number_of_chambers' : row['Количество камер'],
                                                    # 'article' : row['Артикул'],
                                                    # 'profile_type_id' : row['Код к компоненту системы'],
                                                    
                                                })
                        
                        else:
                                materiale = df['Артикул'][key]+"-ES{:02d}".format(1)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='ES',counter=1,kratkiy_tekst_materiala=df_new_aurora['ES - Extrusion'][key],material=materiale).save()
                                df_new_aurora['SAP CODE ES'][key] = materiale
                                umumiy_counter[df['Артикул'][key]+'-ES'] = 1
                    
                                cache_for_cratkiy_text.append(
                                                {
                                                    'kratkiy':df_new_aurora['ES - Extrusion'][key],
                                                    'sap_code':  materiale,
                                                }
                                            )
                        
                if i == 2:
                    if RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='ER',kratkiy_tekst_materiala= df_new_aurora['ER - Extrusion'][key]).exists():
                        df_new_aurora['SAP CODE ER'][key] = RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='ER',kratkiy_tekst_materiala=df_new_aurora['ER - Extrusion'][key])[:1].get().material
                        duplicat_list.append([df_new_aurora['SAP CODE ER'][key],df_new_aurora['ER - Extrusion'][key],'ER'])
                    else: 
                        if RadiatorSapCode.objects.filter(artikul=df['Артикул'][key],section ='ER').exists():
                                umumiy_counter[df['Артикул'][key]+'-ER'] += 1
                                max_valuesER = umumiy_counter[df['Артикул'][key]+'-ER']
                                materiale = df['Артикул'][key]+"-ER{:02d}".format(max_valuesER)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='ER',counter=max_valuesER,kratkiy_tekst_materiala=df_new_aurora['ER - Extrusion'][key],material=materiale).save()
                                df_new_aurora['SAP CODE ER'][key] = materiale
                                
                                cache_for_cratkiy_text.append({
                                                    'kratkiy':df_new_aurora['ER - Extrusion'][key],
                                                    'sap_code':  materiale,
                                                    
                                                    # 'system' : row['Название системы'],
                                                    # 'number_of_chambers' : row['Количество камер'],
                                                    # 'article' : row['Артикул'],
                                                    # 'profile_type_id' : row['Код к компоненту системы'],
                                                    
                                                })
                        
                        else:
                                materiale = df['Артикул'][key]+"-ER{:02d}".format(1)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='ER',counter=1,kratkiy_tekst_materiala=df_new_aurora['ER - Extrusion'][key],material=materiale).save()
                                df_new_aurora['SAP CODE ER'][key] = materiale
                                umumiy_counter[df['Артикул'][key]+'-ER'] = 1
                    
                                cache_for_cratkiy_text.append(
                                                {
                                                    'kratkiy':df_new_aurora['ER - Extrusion'][key],
                                                    'sap_code':  materiale,
                                                }
                                            )
                        
                if i == 3:
                    if RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='PK',kratkiy_tekst_materiala= df_new_aurora['PK - Pokraska'][key]).exists():
                        df_new_aurora['SAP CODE PK'][key] = RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='PK',kratkiy_tekst_materiala=df_new_aurora['PK - Pokraska'][key])[:1].get().material
                        duplicat_list.append([df_new_aurora['SAP CODE PK'][key],df_new_aurora['PK - Pokraska'][key],'PK'])
                    else: 
                        if RadiatorSapCode.objects.filter(artikul=df['Артикул'][key],section ='PK').exists():
                                umumiy_counter[df['Артикул'][key]+'-PK'] += 1
                                max_valuesPK = umumiy_counter[df['Артикул'][key]+'-PK']
                                materiale = df['Артикул'][key]+"-PK{:02d}".format(max_valuesPK)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='PK',counter=max_valuesPK,kratkiy_tekst_materiala=df_new_aurora['PK - Pokraska'][key],material=materiale).save()
                                df_new_aurora['SAP CODE PK'][key] = materiale
                                
                                cache_for_cratkiy_text.append({
                                                    'kratkiy':df_new_aurora['PK - Pokraska'][key],
                                                    'sap_code':  materiale,
                                                    
                                                    # 'system' : row['Название системы'],
                                                    # 'number_of_chambers' : row['Количество камер'],
                                                    # 'article' : row['Артикул'],
                                                    # 'profile_type_id' : row['Код к компоненту системы'],
                                                    
                                                })
                        
                        else:
                                materiale = df['Артикул'][key]+"-PK{:02d}".format(1)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='PK',counter=1,kratkiy_tekst_materiala=df_new_aurora['PK - Pokraska'][key],material=materiale).save()
                                df_new_aurora['SAP CODE PK'][key] = materiale
                                umumiy_counter[df['Артикул'][key]+'-PK'] = 1
                    
                                cache_for_cratkiy_text.append(
                                                {
                                                    'kratkiy':df_new_aurora['PK - Pokraska'][key],
                                                    'sap_code':  materiale,
                                                }
                                            )
                        
                if i == 4:
                    if RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala= df_new_aurora['7 - Upakovka'][key]).exists():
                        df_new_aurora['SAP CODE 7'][key] = RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new_aurora['7 - Upakovka'][key])[:1].get().material
                        duplicat_list.append([df_new_aurora['SAP CODE 7'][key],df_new_aurora['7 - Upakovka'][key],'7'])
                    else: 
                        if RadiatorSapCode.objects.filter(artikul=df['Артикул'][key],section ='7').exists():
                                umumiy_counter[df['Артикул'][key]+'-7'] += 1
                                max_values7 = umumiy_counter[df['Артикул'][key]+'-7']
                                materiale = df['Артикул'][key]+"-7{:03d}".format(max_values7)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='7',counter=max_values7,kratkiy_tekst_materiala=df_new_aurora['7 - Upakovka'][key],material=materiale).save()
                                df_new_aurora['SAP CODE 7'][key] = materiale
                                
                                cache_for_cratkiy_text.append({
                                                    'kratkiy':df_new_aurora['7 - Upakovka'][key],
                                                    'sap_code':  materiale,
                                                    
                                                    # 'system' : row['Название системы'],
                                                    # 'number_of_chambers' : row['Количество камер'],
                                                    # 'article' : row['Артикул'],
                                                    # '7ofile_type_id' : row['Код к компоненту системы'],
                                                    
                                                })
                        
                        else:
                                materiale = df['Артикул'][key]+"-7{:03d}".format(1)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='7',counter=1,kratkiy_tekst_materiala=df_new_aurora['7 - Upakovka'][key],material=materiale).save()
                                df_new_aurora['SAP CODE 7'][key] = materiale
                                umumiy_counter[df['Артикул'][key]+'-7'] = 1
                    
                                cache_for_cratkiy_text.append(
                                                {
                                                    'kratkiy':df_new_aurora['7 - Upakovka'][key],
                                                    'sap_code':  materiale,
                                                }
                                            )
                        
            
            
        else:
            for i in range(1,6):

                if i == 1:
                    if RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='PR',kratkiy_tekst_materiala= df_new['PR - Press'][key]).exists():
                        df_new['SAP CODE P'][key] = RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='PR',kratkiy_tekst_materiala=df_new['PR - Press'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP CODE P'][key],df_new['PR - Press'][key],'PR'])
                    else: 
                        if RadiatorSapCode.objects.filter(artikul=df['Артикул'][key],section ='PR').exists():
                                umumiy_counter[df['Артикул'][key]+'-PR'] += 1
                                max_valuesPR = umumiy_counter[df['Артикул'][key]+'-PR']
                                materiale = df['Артикул'][key]+"-PR{:02d}".format(max_valuesPR)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='PR',counter=max_valuesPR,kratkiy_tekst_materiala=df_new['PR - Press'][key],material=materiale).save()
                                df_new['SAP CODE P'][key] = materiale
                                
                                cache_for_cratkiy_text.append({
                                                    'kratkiy':df_new['PR - Press'][key],
                                                    'sap_code':  materiale,
                                                    
                                                    # 'system' : row['Название системы'],
                                                    # 'number_of_chambers' : row['Количество камер'],
                                                    # 'article' : row['Артикул'],
                                                    # 'profile_type_id' : row['Код к компоненту системы'],
                                                    
                                                })
                        
                        else:
                                materiale = df['Артикул'][key]+"-PR{:02d}".format(1)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='PR',counter=1,kratkiy_tekst_materiala=df_new['PR - Press'][key],material=materiale).save()
                                df_new['SAP CODE P'][key] = materiale
                                umumiy_counter[df['Артикул'][key]+'-PR'] = 1
                    
                                cache_for_cratkiy_text.append(
                                                {
                                                    'kratkiy':df_new['PR - Press'][key],
                                                    'sap_code':  materiale,
                                                }
                                            )
                        
            
                if i == 2:
                    if RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='MO',kratkiy_tekst_materiala= df_new['MO - Mex obrabotka'][key]).exists():
                        df_new['SAP CODE M'][key] = RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='MO',kratkiy_tekst_materiala=df_new['MO - Mex obrabotka'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP CODE M'][key],df_new['MO - Mex obrabotka'][key],'MO'])
                    else: 
                        if RadiatorSapCode.objects.filter(artikul=df['Артикул'][key],section ='MO').exists():
                                umumiy_counter[df['Артикул'][key]+'-MO'] += 1
                                max_valuesMO = umumiy_counter[df['Артикул'][key]+'-MO']
                                materiale = df['Артикул'][key]+"-MO{:02d}".format(max_valuesMO)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='MO',counter=max_valuesMO,kratkiy_tekst_materiala=df_new['MO - Mex obrabotka'][key],material=materiale).save()
                                df_new['SAP CODE M'][key] = materiale
                                
                                cache_for_cratkiy_text.append({
                                                    'kratkiy':df_new['MO - Mex obrabotka'][key],
                                                    'sap_code':  materiale,
                                                    
                                                    # 'system' : row['Название системы'],
                                                    # 'number_of_chambers' : row['Количество камер'],
                                                    # 'article' : row['Артикул'],
                                                    # 'profile_type_id' : row['Код к компоненту системы'],
                                                    
                                                })
                        
                        else:
                                materiale = df['Артикул'][key]+"-MO{:02d}".format(1)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='MO',counter=1,kratkiy_tekst_materiala=df_new['MO - Mex obrabotka'][key],material=materiale).save()
                                df_new['SAP CODE M'][key] = materiale
                                umumiy_counter[df['Артикул'][key]+'-MO'] = 1
                    
                                cache_for_cratkiy_text.append(
                                                {
                                                    'kratkiy':df_new['MO - Mex obrabotka'][key],
                                                    'sap_code':  materiale,
                                                }
                                            )
                        
                if i == 3:
                    if RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='PM',kratkiy_tekst_materiala= df_new['PM - Puma'][key]).exists():
                        df_new['SAP CODE PM'][key] = RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='PM',kratkiy_tekst_materiala=df_new['PM - Puma'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP CODE PM'][key],df_new['PM - Puma'][key],'PM'])
                    else: 
                        if RadiatorSapCode.objects.filter(artikul=df['Артикул'][key],section ='PM').exists():
                                umumiy_counter[df['Артикул'][key]+'-PM'] += 1
                                max_valuesPM = umumiy_counter[df['Артикул'][key]+'-PM']
                                materiale = df['Артикул'][key]+"-PM{:02d}".format(max_valuesPM)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='PM',counter=max_valuesPM,kratkiy_tekst_materiala=df_new['PM - Puma'][key],material=materiale).save()
                                df_new['SAP CODE PM'][key] = materiale
                                
                                cache_for_cratkiy_text.append({
                                                    'kratkiy':df_new['PM - Puma'][key],
                                                    'sap_code':  materiale,
                                                    
                                                    # 'system' : row['Название системы'],
                                                    # 'number_of_chambers' : row['Количество камер'],
                                                    # 'article' : row['Артикул'],
                                                    # 'profile_type_id' : row['Код к компоненту системы'],
                                                    
                                                })
                        
                        else:
                                materiale = df['Артикул'][key]+"-PM{:02d}".format(1)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='PM',counter=1,kratkiy_tekst_materiala=df_new['PM - Puma'][key],material=materiale).save()
                                df_new['SAP CODE PM'][key] = materiale
                                umumiy_counter[df['Артикул'][key]+'-PM'] = 1
                    
                                cache_for_cratkiy_text.append(
                                                {
                                                    'kratkiy':df_new['PM - Puma'][key],
                                                    'sap_code':  materiale,
                                                }
                                            )
                        
                if i == 4:
                    if RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='PK',kratkiy_tekst_materiala= df_new['PK - Pokraska'][key]).exists():
                        df_new['SAP CODE PK'][key] = RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='PK',kratkiy_tekst_materiala=df_new['PK - Pokraska'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP CODE PK'][key],df_new['PK - Pokraska'][key],'PK'])
                    else: 
                        if RadiatorSapCode.objects.filter(artikul=df['Артикул'][key],section ='PK').exists():
                                umumiy_counter[df['Артикул'][key]+'-PK'] += 1
                                max_valuesPK = umumiy_counter[df['Артикул'][key]+'-PK']
                                materiale = df['Артикул'][key]+"-PK{:02d}".format(max_valuesPK)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='PK',counter=max_valuesPK,kratkiy_tekst_materiala=df_new['PK - Pokraska'][key],material=materiale).save()
                                df_new['SAP CODE PK'][key] = materiale
                                
                                cache_for_cratkiy_text.append({
                                                    'kratkiy':df_new['PK - Pokraska'][key],
                                                    'sap_code':  materiale,
                                                    
                                                    # 'system' : row['Название системы'],
                                                    # 'number_of_chambers' : row['Количество камер'],
                                                    # 'article' : row['Артикул'],
                                                    # 'profile_type_id' : row['Код к компоненту системы'],
                                                    
                                                })
                        
                        else:
                                materiale = df['Артикул'][key]+"-PK{:02d}".format(1)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='PK',counter=1,kratkiy_tekst_materiala=df_new['PK - Pokraska'][key],material=materiale).save()
                                df_new['SAP CODE PK'][key] = materiale
                                umumiy_counter[df['Артикул'][key]+'-PK'] = 1
                    
                                cache_for_cratkiy_text.append(
                                                {
                                                    'kratkiy':df_new['PK - Pokraska'][key],
                                                    'sap_code':  materiale,
                                                }
                                            )
                        
                if i == 5:
                    if RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala= df_new['7 - Upakovka'][key]).exists():
                        df_new['SAP CODE 7'][key] = RadiatorSapCode.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['7 - Upakovka'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP CODE 7'][key],df_new['7 - Upakovka'][key],'7'])
                    else: 
                        if RadiatorSapCode.objects.filter(artikul=df['Артикул'][key],section ='7').exists():
                                umumiy_counter[df['Артикул'][key]+'-7'] += 1
                                max_values7 = umumiy_counter[df['Артикул'][key]+'-7']
                                materiale = df['Артикул'][key]+"-7{:03d}".format(max_values7)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='7',counter=max_values7,kratkiy_tekst_materiala=df_new['7 - Upakovka'][key],material=materiale).save()
                                df_new['SAP CODE 7'][key] = materiale
                                
                                cache_for_cratkiy_text.append({
                                                    'kratkiy':df_new['7 - Upakovka'][key],
                                                    'sap_code':  materiale,
                                                    
                                                    # 'system' : row['Название системы'],
                                                    # 'number_of_chambers' : row['Количество камер'],
                                                    # 'article' : row['Артикул'],
                                                    # '7ofile_type_id' : row['Код к компоненту системы'],
                                                    
                                                })
                        
                        else:
                                materiale = df['Артикул'][key]+"-7{:03d}".format(1)
                                RadiatorSapCode(artikul = df['Артикул'][key],section ='7',counter=1,kratkiy_tekst_materiala=df_new['7 - Upakovka'][key],material=materiale).save()
                                df_new['SAP CODE 7'][key] = materiale
                                umumiy_counter[df['Артикул'][key]+'-7'] = 1
                    
                                cache_for_cratkiy_text.append(
                                                {
                                                    'kratkiy':df_new['7 - Upakovka'][key],
                                                    'sap_code':  materiale,
                                                }
                                            )
                        
            
                
           
        
      
    parent_dir ='{MEDIA_ROOT}\\uploads\\radiator\\'
    
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads\\','radiator')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\radiator\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\radiator\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\radiator\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\radiator\\{year}\\{month}\\{day}\\',hour)
      
      
    df_char = create_characteristika(cache_for_cratkiy_text) 
    
    df_char_title = create_characteristika_utils(cache_for_cratkiy_text)
                 
      
            
    if not os.path.isfile(f'{MEDIA_ROOT}\\uploads\\radiator\\{year}\\{month}\\{day}\\{hour}\\radiator-{minut}.xlsx'):
        path_radiator =  f'{MEDIA_ROOT}\\uploads\\radiator\\{year}\\{month}\\{day}\\{hour}\\radiator-{minut}.xlsx'
    else:
        st = randint(0,1000)
        path_radiator =  f'{MEDIA_ROOT}\\uploads\\radiator\\{year}\\{month}\\{day}\\{hour}\\radiator-{minut}-{st}.xlsx'
      



    for key,razlov in df_new_aurora.iterrows():
        if razlov['SAP CODE 7']!="":
            if not RazlovkaRadiatorAurora.objects.filter(sap_code7=razlov['SAP CODE 7'],kratkiy7=razlov['7 - Upakovka']).exists():
                RazlovkaRadiatorAurora(
                        es_sap_code =razlov['SAP CODE ES'],
                        es_kratkiy =razlov['ES - Extrusion'], 
                        er_sap_code =razlov['SAP CODE ER'],
                        er_kratkiy =razlov['ER - Extrusion'], 
                        pk_sap_code =razlov['SAP CODE PK'],
                        pk_kratkiy =razlov['PK - Pokraska'], 
                        sap_code7 =razlov['SAP CODE 7'],
                        kratkiy7 =razlov['7 - Upakovka']
                    ).save()
    
    df_new_aurora = df_new_aurora[df_new_aurora['SAP CODE ER'] !='']
                

    for key,razlov in df_new.iterrows():
        if razlov['SAP CODE 7']!="":  
               
            if not RazlovkaRadiator.objects.filter(sap_code7=razlov['SAP CODE 7'],kratkiy7=razlov['7 - Upakovka']).exists():
                RazlovkaRadiator(
                        pr_sap_code =razlov['SAP CODE P'],
                        pr_kratkiy =razlov['PR - Press'],
                        mo_sap_code =razlov['SAP CODE M'],
                        mo_kratkiy =razlov['MO - Mex obrabotka'], 
                        pm_sap_code =razlov['SAP CODE PM'],
                        pm_kratkiy =razlov['PM - Puma'], 
                        pk_sap_code =razlov['SAP CODE PK'],
                        pk_kratkiy =razlov['PK - Pokraska'], 
                        sap_code7 =razlov['SAP CODE 7'],
                        kratkiy7 =razlov['7 - Upakovka']
                    ).save()
    
    df_new = df_new[df_new['SAP CODE P'] !='']

    price_all_correct = False
      
    


    del df_new_aurora['counter']
    del df_new['counter']

    writer = pd.ExcelWriter(path_radiator, engine='openpyxl')
    df_new_aurora.to_excel(writer,index=False,sheet_name='Schotchik_Aurora')
    df_new.to_excel(writer,index=False,sheet_name='Schotchik')
    df_char.to_excel(writer,index=False,sheet_name='Characteristika')
    df_char_title.to_excel(writer,index=False,sheet_name='title')
    writer.close()


    order_id = request.GET.get('order_id',None)

    work_type = 1
    if order_id:
        work_type = OrderRadiator.objects.get(id = order_id).work_type
        if price_all_correct and  work_type != 5 :
            # path = update_char_title_function(df_char_title,order_id)
            # files =[File(file=p,filetype='radiator') for p in path]
            files = []
            files.append(File(file=path_radiator,filetype='radiator'))
            context ={
                  'files':files,
                  'section':'Формированый радиатор файл'
            }

            if order_id:
                file_paths =[ file.file for file in files]
                order = OrderRadiator.objects.get(id = order_id)
                paths = order.paths
                raz_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                zip_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                paths['radiator_razlovka_file']= file_paths
                paths['raz_created_at']= raz_created_at
                paths['zip_created_at']= zip_created_at
                paths['status_l']= 'done'
                paths['status_raz']= 'done'
                paths['status_zip']= 'done'
                paths['status_text_l']= 'done'
                
                order.paths = paths
                order.radiator_worker = request.user
                order.current_worker = request.user
                order.work_type = 6
                order.save()
                context['order'] = order
                paths =  order.paths
                for key,val in paths.items():
                    context[key] = val
                return render(request,'order/order_detail_radiator.html',context)  
        else:
            
            file =[File(file = path_radiator,filetype='radiator',id=1)]
            context = {
                  'files':file,
                  'section':'Формированый radiator файл'
            }
            
            if order_id:
                order = OrderRadiator.objects.get( id = order_id)
                paths = order.paths 
                if work_type != 5:
                    context2 ={
                            'radiator_razlovka_file':[path_radiator,path_radiator]
                    }
                    paths['radiator_razlovka_file'] = [path_radiator,path_radiator]
                else:
                    path_radiator = order.paths['radiator_razlovka_file']
                    context2 ={
                            'radiator_razlovka_file':[path_radiator,path_radiator]
                    }

                
                raz_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                paths['raz_created_at']= raz_created_at
                
                paths['status_l']= 'done'
                paths['status_raz']= 'done'
                paths['status_zip']= 'on process'
                paths['status_text_l']= 'on process'
                

                order.paths = paths
                order.current_worker = request.user
                order.work_type = 5
                order.save()
                context2['order'] = order
                paths =  order.paths
                for key,val in paths.items():
                    context2[key] = val

                workers = User.objects.filter(role =  'moderator',is_active =True)
                context2['workers'] = workers

                return render(request,'order/order_detail_radiator.html',context2)

    
    return render(request,'universal/generated_files.html',{'a':'b'})


class FileRazlovki:
    def __init__(self,file):
        self.file =file

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator','universal_user'])
def get_razlovka_radiator(request):
    if request.method =='POST':
        ozmk = request.POST.get('ozmk',None)
        if ozmk:
            ozmks =ozmk.split()
            path,df = get_ozmka(ozmks)
            # res = download_bs64(df,'RAZLOVKA')
            # if request.user.role =='radiator':
            #     return res
            files = [FileRazlovki(file=p) for p in path]
            context ={
                'files':files,
                'section':'Разловка'
            }
            return render(request,'universal/generated_files.html',context)
        else:
            return render(request,'norma/razlovka_find_org.html')
    else:
        path1 = request.GET.get('path',None)
        if path1:
            if sys.platform == "win32":
                os.startfile(path1)
        return render(request,'norma/razlovka_find_org.html')
    

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator','universal_user'])
def delete_texcarta(request):
    if request.method =='POST':
        ozmk = request.POST.get('ozmk',None)
        if ozmk:
            ozmks =ozmk.split()
            for ozm in ozmks:
                if  TexcartaBase.objects.filter(material=ozm).exists():
                    texcarta = TexcartaBase.objects.filter(material=ozm)[:1].get()
                    # texcarta.delete()    
        return render(request,'norma/razlovka_find_org.html')
    else:
        return render(request,'norma/razlovka_find_org.html')