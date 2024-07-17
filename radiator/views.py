from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from .forms import NormaFileForm,NormaExcelFiles,ViFileForm
from .models import Norma,Siryo,Korobka,Kraska,TexcartaBase,ViFiles
from config.settings import MEDIA_ROOT
import pandas as pd
import os 
from datetime import datetime



@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','radiator'])
def vi_file(request):
    files = ViFiles.objects.all().order_by('-created_at')
    context ={
        'files':files,
        'section':'Формирование ВИ файла',
        'link':'/radiator/vi-generate-mo/',
        'type':'ВИ'
        }
    return render(request,'universal/file_list.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator'])
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
@allowed_users(allowed_roles=['admin','moderator','radiator'])
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
    
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
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
@allowed_users(allowed_roles=['admin','moderator','radiator'])
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
    
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    df_new_vi2.to_excel(writer,index=False,sheet_name ='ВИ')
    writer.close()

    files =[File(file =path,filetype='vi',id=None)]
    context ={
        'section':'ВИ',
        'files':files
    }
    return render(request,'universal/generated_files.html',context)





@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator'])
def full_update_korobka(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['type']='termo'
        form = NormaFileForm(data, request.FILES)
        if form.is_valid():
            siryo = Korobka.objects.all()
            siryo.delete()
            form_file = form.save()
            file = form_file.file
            path =f'{MEDIA_ROOT}/{file}'
            
            df = pd.read_excel(path)

            df = df.astype(str)
            df = df.replace('nan','0')
            df = df.replace('0.0','0')
            
            columns = df.columns

            Korobka(data ={'columns':list(columns)}).save()

            for key, row in df.iterrows():
                norma_dict = {}
                for col in columns:
                    norma_dict[col]=row[col]
                Korobka(data =norma_dict).save()

    return render(request,'norma/benkam/main.html')


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator'])
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
@allowed_users(allowed_roles=['admin','moderator','radiator'])
def full_update_siryo(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['type']='termo'
        form = NormaFileForm(data, request.FILES)
        if form.is_valid():
            siryo = Siryo.objects.all()
            siryo.delete()
            form_file = form.save()
            file = form_file.file
            path =f'{MEDIA_ROOT}/{file}'
            
            df = pd.read_excel(path)

            df = df.astype(str)
            df = df.replace('nan','0')
            df = df.replace('0.0','0')
            
            columns = df.columns

            Siryo(data ={'columns':list(columns)}).save()

            for key, row in df.iterrows():
                norma_dict = {}
                for col in columns:
                    norma_dict[col]=row[col]
                Siryo(data =norma_dict).save()

    return render(request,'norma/benkam/main.html')


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator'])
def full_update_kraska(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['type']='termo'
        form = NormaFileForm(data, request.FILES)
        if form.is_valid():
            siryo = Kraska.objects.all()
            siryo.delete()
            form_file = form.save()
            file = form_file.file
            path =f'{MEDIA_ROOT}/{file}'
            
            df = pd.read_excel(path)

            df = df.astype(str)
            df = df.replace('nan','0')
            df = df.replace('0.0','0')
            
            columns = df.columns

            Kraska(data ={'columns':list(columns)}).save()

            for key, row in df.iterrows():
                norma_dict = {}
                for col in columns:
                    norma_dict[col]=row[col]
                Kraska(data =norma_dict).save()

    return render(request,'norma/benkam/main.html')


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator'])
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
            
            df = pd.read_excel(path,sheet_name='норма', header=3)

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
@allowed_users(allowed_roles=['admin','moderator','radiator'])
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
@allowed_users(allowed_roles=['admin','moderator','radiator'])
def file_list_org(request):
    files = NormaExcelFiles.objects.filter(generated =False,type='radiator').order_by('-created_at')
    context ={'files':files,
              'link':'/radiator/kombinirovaniy-process/',
              'section':'Генерация норма файла',
              'type':'Радиатор',
              'file_type':'simple'
              }
    return render(request,'universal/file_list_norma.html',context)


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','radiator'])
def kombinirovaniy_process(request,id):
    file = NormaExcelFiles.objects.get(id=id).file
    file_path =f'{MEDIA_ROOT}\\{file}'
    df_exell = pd.read_excel(file_path,header=0,sheet_name='a')
    df_exell = df_exell.fillna('')
    df_exell =df_exell.astype(str)
    
    file_content ='обычный'
    product_type ='simple'
    df = []
    print(df_exell.columns,file) 
    
    for key,row in df_exell.iterrows():
        df.append([
            row['SAP CODE P'],row['PR - Press'],
            row['SAP CODE M'],row['MO - Mex obrabotka'],
            row['SAP CODE PM'],row['PM - Puma'],
            row['SAP CODE PK'],row['PK - Pokraska'],
            row['SAP CODE 7'],row['7 - Upakovka ']
        ])
    
    class Xatolar:
        def __init__(self,section,xato,sap_code):
            self.section = section
            self.xato = xato
            self.sap_code = sap_code

    does_not_exist_norm =[]
    # k = -1
    # if product_type =='termo':
    #     for i in range(0,len(df)):
    #         if df[i][0] != '':
    #             length = df[i][0].split('-')[0]
    #             if not Norma.objects.filter(data__новый__icontains=length).exists():
    #                 does_not_exist_norm.append(Xatolar(section='Норма расход',xato='norma rasxod yo\'q',sap_code=df[i][0]))
    #                 continue
    #             splav_code = df[i][1].split()[0][:2]
    #             splav_list = AlyuminniysilindrEkstruziya1.objects.filter(название__icontains ='60'+splav_code).exists()
    #             if not splav_list:
    #                 does_not_exist_norm.append(Xatolar(section='Алюмин Сплав',xato='60'+splav_code,sap_code=df[i][0]))
            
    #         if df[i][4] != '':
    #             kraska_code = df[i][5].split()[-1]
                
    #             kraskas = Kraska.objects.filter(код_краски_в_профилях = kraska_code).exists()
                
    #             if not kraskas:
    #                 does_not_exist_norm.append(Xatolar(section='Краска',xato=kraska_code,sap_code=df[i][4]))

    #         if df[i][6] != '':
    #             length = df[i][6].split('-')[0]
    #             alum_teks = Norma.objects.filter(data__новый__icontains=length)[:1].get()

    #             sublimatsiya_code = df[i][7].split('_')[1]
    #             code_ss = alum_teks.data['Суб. Декор. плёнка ширина пленки/ мм']
    #             mein = alum_teks.data['Суб. Декор. плёнка расход на 1000 профиль/м²']
    #             subdecorplonka = SubDekorPlonka.objects.filter(код_декор_пленки = sublimatsiya_code, ширина_декор_пленки_мм = code_ss).exists()
    #             if not subdecorplonka:
    #                 does_not_exist_norm.append(Xatolar(section='Сублимация декор',xato=sublimatsiya_code +' ' + code_ss +' bazada yo\'q',sap_code=df[i][6]))
            
    #         if df[i][10] != '':
    #             length = df[i][10].split('-')[0]
    #             alum_teks = Norma.objects.filter(data__новый__icontains=length)[:1].get()
    #             if (alum_teks.data['верх ширина ленты/мм'] =='0' and alum_teks.data['низ ширина ленты/мм'] == '0'):
    #                 does_not_exist_norm.append(Xatolar(section='Наклейка',xato='bazada qiymati 0',sap_code=df[i][10]))
    #         if df[i][12] != '':
    #             artikul = df[i][12].split('-')[0]
    #             termomostrlar = Termomost.objects.filter(data__Артикул__icontains=artikul).exists()
    #             if not termomostrlar:
    #                 does_not_exist_norm.append(Xatolar(section='Термомост',xato='termomost bazada yo\'q',sap_code=df[i][12]))
            
    # else:
    #     for i in range(0,len(df)):
    #         if df[i][0] != '':
    #             length = df[i][0].split('-')[0]
    #             if not Norma.objects.filter(data__новый__icontains=length).exists():
    #                 does_not_exist_norm.append(Xatolar(section='Норма расход',xato='bazada yo\'q',sap_code=df[i][0]))
    #                 continue
    #             splav_code = df[i][1].split()[0][:2]
    #             splav_list = AlyuminniysilindrEkstruziya1.objects.filter(название__icontains ='60'+splav_code).exists()
    #             if not splav_list:
    #                 does_not_exist_norm.append(Xatolar(section='Алюмин Сплав',xato='60'+splav_code,sap_code=df[i][0]))
            
    #         if df[i][4] != '':
    #             kraska_code = df[i][5].split()[-1]
    #             kraskas = Kraska.objects.filter(код_краски_в_профилях = kraska_code).exists()
    #             if not kraskas:
    #                 does_not_exist_norm.append(Xatolar(section='Краска',xato=kraska_code,sap_code=df[i][4]))

    #         if df[i][6] != '':
    #             length = df[i][6].split('-')[0]
    #             alum_teks = Norma.objects.filter(data__новый__icontains=length)[:1].get()
    #             sublimatsiya_code = df[i][7].split('_')[1]
    #             code_ss = alum_teks.data['Суб. Декор. плёнка ширина пленки/ мм']
    #             mein = alum_teks.data['Суб. Декор. плёнка расход на 1000 профиль/м²']
    #             subdecorplonka = SubDekorPlonka.objects.filter(код_декор_пленки = sublimatsiya_code, ширина_декор_пленки_мм = code_ss).exists()
    #             if not subdecorplonka:
    #                 does_not_exist_norm.append(Xatolar(section='Сублимация декор',xato=sublimatsiya_code +' ' + code_ss+' bazada yo\'q',sap_code=df[i][6]))
            
    #         if df[i][10] != '':
    #             length = df[i][10].split('-')[0]
    #             alum_teks = Norma.objects.filter(data__новый__icontains=length)[:1].get()
    #             if (alum_teks.data['верх ширина ленты/мм'] =='0' and alum_teks.data['низ ширина ленты/мм'] == '0'):
    #                 does_not_exist_norm.append(Xatolar(section='Наклейка',xato='bazada qiymati 0',sap_code=df[i][10]))
            
                    

     
    
    # if len(does_not_exist_norm) > 0: 
    #     context ={
    #         'does_not_exist_norm':does_not_exist_norm,
    #         'section':'Ошибки нормы',
    #         'id':id

    #     }
    #     return render(request,'norma/benkam/not_exist.html',context)
    
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
    
   
    j = 0
    
    norma_exists= []

    for i in range(0,len(df)):
        print(i)
        
        artikul = df[i][8].split('-')[0]
        print(artikul,'norma')
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
            df_new['DATUV'].append('01012021')
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
                    df_new['MENGE'].append('SKC')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                    
                
                df_new['LGORT'].append('PS08')

            upakovka_names =[
                {'kratkiy':'Пленка полиэтиленовая 90см','sapcode':'1000004426'},
                {'kratkiy':'Пленка полиэтиленовая 65см','sapcode':'1000004427'},
                {'kratkiy':'Пленка полиэтиленовая 85см','sapcode':'1000004428'}
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
                sap_val = '1000' if korobka_type !='BK' else '2000'
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
            df_new['BMEIN'].append('SKC')
            df_new['STLST'].append('1')
            df_new['POSNR'].append('')
            df_new['POSTP'].append('')
            df_new['MATNR1'].append('')
            df_new['TEXT2'].append('')
            df_new['MEINS'].append('')
            df_new['MENGE'].append('')
            df_new['DATUV'].append('01012021')
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
                    df_new['MENGE'].append('SKC')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                if k == 2 :
                    # siryo = Siryo.objects.filter(data__Краткийтекст__icontains ='Анафорез.грунтовка ARSONKOTE 1002K CLEAR')
                    df_new['MATNR1'].append('1000004435')
                    df_new['TEXT2'].append('Анафорез.грунтовка ARSONKOTE 1002K CLEAR')
                    
                    # df_new['MEINS'].append(("%.3f" % (float(alum_teks.data['расход сплава на 1000 шт профиля/кг'])*mein_percent)).replace('.',',')) 
                    df_new['MEINS'].append(norma.data['Анафорез.грунтовка ARSONKOTE 1002K CLEAR'].replace('.0','') if norma.data['Анафорез.грунтовка ARSONKOTE 1002K CLEAR'][-2:]=='.0' else ("%.3f" % float(norma.data['Анафорез.грунтовка ARSONKOTE 1002K CLEAR'])).replace('.',',') ) 
                    df_new['MENGE'].append('КГ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                if k == 3 :
                    # siryo = Siryo.objects.filter(data__Краткийтекст__icontains ='Анафорез.грунтовка ARSONKOTE 1002K CLEAR')
                    df_new['MATNR1'].append('1000004436')
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
            df_new['BMEIN'].append('SKC')
            df_new['STLST'].append('1')
            df_new['POSNR'].append('')
            df_new['POSTP'].append('')
            df_new['MATNR1'].append('')
            df_new['TEXT2'].append('')
            df_new['MEINS'].append('')
            df_new['MENGE'].append('')
            df_new['DATUV'].append('01012021')
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
                    df_new['MENGE'].append('SKC')
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
            df_new['STKTX'].append('')
            df_new['BMENG'].append( '1000')
            df_new['BMEIN'].append('SKC')
            df_new['STLST'].append('1')
            df_new['POSNR'].append('')
            df_new['POSTP'].append('')
            df_new['MATNR1'].append('')
            df_new['TEXT2'].append('')
            df_new['MEINS'].append('')
            df_new['MENGE'].append('')
            df_new['DATUV'].append('01012021')
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
            df_new['MENGE'].append('SKC')
            df_new['DATUV'].append('')
            df_new['PUSTOY'].append('')
            df_new['LGORT'].append('PS04')

            siryo_names =[
                {'kratkiy':'Лента абразивная 60 (140х2000) Барабан','sapcode':'1000004458','MEINS':'ШТ'},
                {'kratkiy':'Лента абразивная 120(140х2000) Барабан','sapcode':'1000004459','MEINS':'ШТ'},
                {'kratkiy':'Лента абразивная  80 (350х1900) Мех.обр','sapcode':'1000004455','MEINS':'ШТ'},
                {'kratkiy':'Лента абразивная 120 (350х1900) Мех.обр','sapcode':'1000004456','MEINS':'ШТ'},
                {'kratkiy':'Лента абразивная 240 (350х1900) Мех.обр','sapcode':'1000004457','MEINS':'ШТ'},
                {'kratkiy':'Тех. отход ал стружка','sapcode':'1900007454','MEINS':'КГ'},
                {'kratkiy':'Крышка радиатора','sapcode':'1000004484','MEINS':'КГ'},
                {'kratkiy':'Паронит межсекционная (Китай) Gizetta','sapcode':'1000004374','MEINS':'ШТ'},
                {'kratkiy':'Соеденительная муфта (Местный)','sapcode':'1000004372','MEINS':'ШТ'},
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
            df_new['STKTX'].append('')
            df_new['BMENG'].append( '1000')
            df_new['BMEIN'].append('SKC')
            df_new['STLST'].append('1')
            df_new['POSNR'].append('')
            df_new['POSTP'].append('')
            df_new['MATNR1'].append('')
            df_new['TEXT2'].append('')
            df_new['MEINS'].append('')
            df_new['MENGE'].append('')
            df_new['DATUV'].append('01012021')
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
            df_new['MENGE'].append('SKC')
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
            df_new['BMEIN'].append('SKC')
            df_new['STLST'].append('1')
            df_new['POSNR'].append('')
            df_new['POSTP'].append('')
            df_new['MATNR1'].append('')
            df_new['TEXT2'].append('')
            df_new['MEINS'].append('')
            df_new['MENGE'].append('')
            df_new['DATUV'].append('01012021')
            df_new['PUSTOY'].append('')
            df_new['LGORT'].append('')
            for k in range(1,7):
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
                    df_new['MATNR1'].append('1000004483')
                    df_new['TEXT2'].append('Сплав AK12')
                    df_new['MEINS'].append(norma.data['расход сплава АК 12 на 1000 секции'].replace('.0','')  if norma.data['расход сплава АК 12 на 1000 секции'][-2:]=='.0' else ("%.3f" % float(norma.data['расход сплава АК 12 на 1000 секции'])).replace('.',',')) 
                    df_new['MENGE'].append('КГ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                if k == 2 :
                    df_new['MATNR1'].append('1000004484')
                    df_new['TEXT2'].append('Тех. отход литник')
                    df_new['MEINS'].append('-'+norma.data['Тех. отход литник'].replace('.0','') if norma.data['Тех. отход литник'][-2:]=='.0' else '-' + ("%.3f" % float(norma.data['Тех. отход литник'])).replace('.',',')) 
                    df_new['MENGE'].append('КГ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                    
                if k == 3 :
                    df_new['MATNR1'].append('1900007455')
                    df_new['TEXT2'].append('Тех. отход промывка')
                    df_new['MEINS'].append('-'+norma.data['Тех. отход промывка'].replace('.0','') if norma.data['Тех. отход промывка'][-2:]=='.0' else '-' + ("%.3f" % float(norma.data['Тех. отход промывка'])).replace('.',','))
                    df_new['MENGE'].append('КГ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')

                if k == 4 :
                    df_new['MATNR1'].append('1900007457')
                    df_new['TEXT2'].append('Тех. отход шлак масло')
                    df_new['MEINS'].append('-'+norma.data['Тех. отход шлак масло'].replace('.0','') if norma.data['Тех. отход шлак масло'][-2:]=='.0' else '-' + ("%.3f" % float(norma.data['Тех. отход шлак масло'])).replace('.',','))
                    df_new['MENGE'].append('КГ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                if k == 5 :
                    df_new['MATNR1'].append('1000004351')
                    df_new['TEXT2'].append('Сож для прес-формы DIELUBRIC')
                    df_new['MEINS'].append('-'+norma.data['Сож для прес-формы DIELUBRIC'].replace('.0','') if norma.data['Сож для прес-формы DIELUBRIC'][-2:]=='.0' else '-' + ("%.3f" % float(norma.data['Сож для прес-формы DIELUBRIC'])).replace('.',','))
                    df_new['MENGE'].append('Л')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                if k == 6 :
                    df_new['MATNR1'].append('1000004353')
                    df_new['TEXT2'].append('Огнеупорная смазка Pyro-Mastic')
                    df_new['MEINS'].append('-'+norma.data['Огнеупорная смазка Pyro-Mastic'].replace('.0','') if norma.data['Огнеупорная смазка Pyro-Mastic'][-2:]=='.0' else '-' + ("%.3f" % float(norma.data['Огнеупорная смазка Pyro-Mastic'])).replace('.',','))
                    df_new['MENGE'].append('КГ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
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
                    df_new['POSNR'].append(7)
                    df_new['POSTP'].append('L')
                    df_new['MATNR1'].append('1000004481')
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
                    df_new['POSNR'].append(7)
                    df_new['POSTP'].append('L')
                    df_new['MATNR1'].append('1000004482')
                    df_new['TEXT2'].append('Вставка для радиатора 18 мм')
                    df_new['MEINS'].append('1000') 
                    df_new['MENGE'].append('ШТ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                    df_new['LGORT'].append('PS02')

                 
        
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
    


    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    dff.to_excel(writer,index=False,sheet_name ='Norma')
    
    
    writer.close()

    
    # path =os.path.join(os.path.expanduser("~/Desktop"),'new_base_cominirovaniy.xlsx')
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
@allowed_users(allowed_roles=['admin','moderator','radiator'])
def lenght_generate_texcarta(request,id):
    file = NormaExcelFiles.objects.get(id=id).file
    file_path =f'{MEDIA_ROOT}\\{file}'
    df =pd.read_excel(file_path)

    df =df.astype(str)
    df=df.replace('nan','')


    print(df,'+'*50)

    counter = 0
    for key,row in df.iterrows():
        if not TexcartaBase.objects.filter(material = row['МАТЕРИАЛ']).exists():
            if '-PR' in row['МАТЕРИАЛ']:
                counter +=2
            elif '-MO' in row['МАТЕРИАЛ']:
                counter +=25
            elif '-PM' in row['МАТЕРИАЛ']:
                counter +=2
            elif '-PK' in row['МАТЕРИАЛ']:
                counter +=2
            elif '-7' in row['МАТЕРИАЛ']:
                counter +=2
       

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
    
    print(df_new,'lllll')

    counter_2 = 0
    for key,row in df.iterrows():
        if not TexcartaBase.objects.filter(material = row['МАТЕРИАЛ']).exists():
            length = row['МАТЕРИАЛ'].split('-')[0]
            print(row['МАТЕРИАЛ'],'ddd')
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
                        df_new['ACTTYPE_01'][counter_2] ='200043'
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
                        df_new['MEINH'][counter_2] ='SKC'
                        df_new['VGW01'][counter_2] ='24'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] ='200043'
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





    print(df_new,'newwwwww')
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
    writer = pd.ExcelWriter(path2, engine='xlsxwriter')
    df_new.to_excel(writer,index=False,sheet_name ='TEXCARTA')
    writer.close()

    # files =[File(file =path2,filetype='simple',id=1),File(file =path7,filetype='simple',id=2),]
    context ={
        'file1':path2,
        'section':'Техкарта',

    }

   
    return render(request,'norma/radiator/generated_files_texcarta.html',context)

