from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse
import pandas as pd
import numpy as np
from django.http import JsonResponse
from .models import Norma,Nakleyka,Kraska,Ximikat,SubDekorPlonka,Skotch,Lamplonka,KleyDlyaLamp,AlyuminniysilindrEkstruziya1,AlyuminniysilindrEkstruziya2,SiryoDlyaUpakovki,ProchiyeSiryoNeno,NormaExcelFiles,CheckNormaBase,NormaDontExistInExcell,Accessuar,ZakalkaIskyuchenie,ViFiles
from .forms import NormaFileForm,NormaEditForm,ViFileForm,TexcartaEditForm,KraskaAddForm,NakleykaAddForm,LaminationAddForm
from django.db.models import Q
from aluminiytermo.models import Characteristika,CharacteristicTitle
from config.settings import MEDIA_ROOT
from .utils import excelgenerate,create_csv_file,create_folder
from django.contrib.auth.decorators import login_required
import os
from aluminiytermo.views import File
from imzo.models import TexCartaTime
from order.models import Order
from datetime import datetime
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import mimetypes
import ast
from django.utils.text import slugify
from pathlib import Path 
from django.db.models.functions import Trim
from accounts.decorators import allowed_users

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def vi_generate(request,id):
    file = ViFiles.objects.get(id=id).file
    file_path =f'{MEDIA_ROOT}\\{file}'
    df_new = pd.read_excel(file_path,sheet_name=['MARA','MAPL','MAST','PLPO','STKO'])
    df_new['MARA'] =df_new['MARA'].astype(str)
    df_new['MAPL'] =df_new['MAPL'].astype(str)
    df_new['MAST'] =df_new['MAST'].astype(str)
    df_new['PLPO'] =df_new['PLPO'].astype(str)
    df_new['STKO'] =df_new['STKO'].astype(str)

    df_new['MARA']=df_new['MARA'].replace('nan','')
    df_new['MAPL']=df_new['MAPL'].replace('nan','')
    df_new['MAST']=df_new['MAST'].replace('nan','')
    df_new['PLPO']=df_new['PLPO'].replace('nan','')
    df_new['STKO']=df_new['STKO'].replace('nan','')



    




   

    # print(df)

    df_vi = pd.DataFrame()
    df_vi['WERKS'] = ['1101' for i in df_new['MAST']['Материал']]
    df_vi['MATNR'] = df_new['MAST']['Материал']
    df_vi['VERID'] = ["{:04d}".format(int(i)) for i in df_new['MAST']['АльтернСпецификация']]
    # df_vi['TEXT1'] = df_new['MAST']['Материал']
    df_vi['BSTMI'] = ['1' for i in df_new['MAST']['Материал']]
    df_vi['BSTMA'] = ['99999999' for i in df_new['MAST']['Материал']]
    df_vi['ADATU'] = ['01012023' for i in df_new['MAST']['Материал']]
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
    df['MATNR ALT'] =df['Материал'] +df['АльтернСпецификация']
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
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['Упаковка']),'ALORT'] = 'PS10'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['SKM - SKM покраска']),'ALORT'] = 'PS04'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['SAT - SAT покраска']),'ALORT'] = 'PS05'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['ГР - ГР покраска']),'ALORT'] = 'PS06'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['SKM - Ручная покраска']),'ALORT'] = 'PS07'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['SAT - Ручная покраска']),'ALORT'] = 'PS07'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['ГР - Ручная покраска']),'ALORT'] = 'PS07'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['Алю. цилиндр. пруток 6063-1 178мм HM']),'ALORT'] = 'PS03'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['Алю. цилиндр. пруток 6063-1 102мм HM']),'ALORT'] = 'PS03'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['Сублимация - 7777']),'ALORT'] = 'PS08'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['Сублимация - 8888']),'ALORT'] = 'PS08'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['Алю. цилиндр. пруток 6063-1 A7 178мм HM']),'ALORT'] = 'PS03'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['Алю. цилиндр. пруток 6063-1 A7 102мм HM']),'ALORT'] = 'PS03'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['Сублимация - 3701']),'ALORT'] = 'PS08'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['Ламинация + Наклейка + Упаковка']),'ALORT'] = 'PS11'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['Ламинация + Упаковка']),'ALORT'] = 'PS11'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['Комбинированный + Упаковка']),'ALORT'] = 'PS09'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['Комбинирование']),'ALORT'] = 'PS09'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['Сублимация - 3702']),'ALORT'] = 'PS03'
    df_new_vi2.loc[df_new_vi2['TEXT1'].isin(['Наклейка']),'ALORT'] = 'PS10'
    


    ####################

    df_4_filter =df_new_vi2[df_new_vi2['VERID'].isin(['0004'])]
    df_5_filter =df_new_vi2[df_new_vi2['VERID'].isin(['0005'])]
    df_6_filter =df_new_vi2[df_new_vi2['VERID'].isin(['0006'])]

    df_pere_prisvoeniye_4 = pd.DataFrame({'MATNR':df_4_filter['MATNR'],'WERKS':['1101' for i in df_4_filter['MATNR']],'PLNNR':df_4_filter['PLNNR'],'VORNR':['010' for i in df_4_filter['MATNR']],'PLNFL':['0010' for i in df_4_filter['MATNR']]})
    df_pere_prisvoeniye_5 = pd.DataFrame({'MATNR':df_5_filter['MATNR'],'WERKS':['1101' for i in df_5_filter['MATNR']],'PLNNR':df_5_filter['PLNNR'],'VORNR':['010' for i in df_5_filter['MATNR']],'PLNFL':['0010' for i in df_5_filter['MATNR']]})
    df_pere_prisvoeniye_6 = pd.DataFrame({'MATNR':df_6_filter['MATNR'],'WERKS':['1101' for i in df_6_filter['MATNR']],'PLNNR':df_6_filter['PLNNR'],'VORNR':['010' for i in df_6_filter['MATNR']],'PLNFL':['0010' for i in df_6_filter['MATNR']]})
    
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

    path =f'{MEDIA_ROOT}\\uploads\\vi\\{year}\\{month}\\{day}\\{hour}\\{minut}\\ВИ.xlsx'
    
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    df_new_vi2.to_excel(writer,index=False,sheet_name ='ВИ')
    df_pere_prisvoeniye_4.to_excel(writer,index=False,sheet_name ='4')
    df_pere_prisvoeniye_5.to_excel(writer,index=False,sheet_name ='5')
    df_pere_prisvoeniye_6.to_excel(writer,index=False,sheet_name ='6')
    writer.close()

    files =[File(file =path,filetype='vi')]
    context ={
        'section':'ВИ',
        'files':files
    }
    return render(request,'universal/generated_files.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','user_accessuar','only_razlovka'])
def download(request):
  file_path = request.GET.get('file_path',None)
  if file_path:
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
  raise Http404

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','user_accessuar','only_razlovka'])
def download_zip_file(request):
    file_path = request.GET.get('file_path',None)
    if file_path and '[' in file_path:
        file_pathh =ast.literal_eval(file_path)
        file_path =file_pathh[0]
    if file_path:
        filename = Path(file_path).name
        

        fl = open(file_path,'rb')
        mime_type, _ = mimetypes.guess_type(file_path)
        response = HttpResponse(fl, content_type=mime_type)
        # response.add_header('Content-Disposition', 'attachment', filename=filename)
        response['Content-Disposition'] = f'attachment; filename={slugify(filename)}.zip'
        return response
    return response
        
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','only_razlovka'])
def vi_file(request):
    files = ViFiles.objects.all().order_by('-created_at')
    context ={
        'files':files,
        'section':'Формирование ВИ файла',
        'link':'/norma/vi-generate/',
        'type':'ВИ'
        }
    return render(request,'universal/file_list.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def file_vi_upload_org(request):
      
    if request.method == 'POST':
        form = ViFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vi_file_list')
    else:
        context ={
            'section':'Загрузка ВИ файла'
        }
    return render(request,'universal/main.html',context)




@csrf_exempt
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def delete_norm(request, id):
    norma = Norma.objects.get(id= id)
    if TexCartaTime.objects.filter(компонент_1 =norma.компонент_1,компонент_2=norma.компонент_2,компонент_3=norma.компонент_3,артикул=norma.артикул).exists():
        texcarta = TexCartaTime.objects.filter(компонент_1 =norma.компонент_1,компонент_2=norma.компонент_2,компонент_3=norma.компонент_3,артикул=norma.артикул)
        print(texcarta)
        texcarta.delete()
    norma.delete()
    return JsonResponse({'msg':True,'text':'Deleted successfully'})

@csrf_exempt
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def norma_delete_all(request):
    norma = Norma.objects.all()
    texcarta = TexCartaTime.objects.all()
    norma.delete()
    texcarta.delete()
    return JsonResponse({'msg':True})

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def add_kraska(request):

    if request.method == 'POST':
        form = KraskaAddForm(data=request.POST)
        if form.is_valid():
                form.save()
                return redirect('home')
    else:
        form = KraskaAddForm()

    context =  {
        'form':form
    }
    return render(request,'norma/add_kraska.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def add_nakleyka(request):

    if request.method == 'POST':
        form = NakleykaAddForm(data=request.POST)
        if form.is_valid():
                form.save()
                return redirect('home')
    else:
        form = NakleykaAddForm()

    context =  {
        'form':form
    }
    return render(request,'norma/add_nakleyka.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def add_lamination(request):

    if request.method == 'POST':
        form = LaminationAddForm(data=request.POST)
        if form.is_valid():
                form.save()
                return redirect('home')
    else:
        form = LaminationAddForm()

    context =  {
        'form':form
    }
    return render(request,'norma/add_lamination.html',context)



@csrf_exempt
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def full_update_norma(request):
    data = dict(request.POST)

    counter = 0
    columns =data['data[3][]']
    for i in range(0,len(columns)):
        columns[i] = columns[i] + str(i)
        print(columns[i]) 

    new_data = []
    for j in range(4,len(data)):
        new_data.append(data[f'data[{j}][]'])
   
    for i in range(0,len(new_data)):
        if len(new_data[i]) == 179:
            new_data[i] += ['','','']
        
    df = pd.DataFrame(np.array(new_data),columns=columns)
    df = df.replace('','0')
    # print(columns)
    for key,row in df.iterrows():
        norma = Norma(
            устаревший = row['Устаревший0'],
            компонент_1 = row['КОМПОНЕНТ1'],
            компонент_2 = row['КОМПОНЕНТ2'],
            компонент_3 = row['КОМПОНЕНТ3'],
            артикул = row['АРТИКУЛ4'],
            серия = str(row['Серия5']).strip(),
            наименование = str(row['Наименование6']).strip(),
            внешний_периметр_профиля_мм = str(row['Внешний периметр профиля/ мм7']).strip(),
            площадь_мм21 = str(row['Площадь /мм²8']).strip(),
            площадь_мм22 = str(row['Площадь /мм²9']).strip(),
            удельный_вес_профиля_кг_м = str(row['Удельный вес профиля кг/м10']).strip(),
            диаметр_описанной_окружности_мм = str(row['Диаметр описанной окружности/мм11']).strip(),
            длина_профиля_м = str(row['Длина профиля/м12']).strip(),
            расчетное_колво_профиля_шт = str(row['Расчетное кол-во профиля/шт13']).strip(),
            общий_вес_профиля_кг = str(row['Общий вес профиля/кг14']).strip(),
            #############################
            алю_сп_6063_рас_спа_на_1000_шт_пр_кг = str(row['расход сплава на 1000 шт профиля/кг15']).strip(),
            алюминиевый_сплав_6063_при_этом_балвашка = str(row['при этом % тех.отхода \r\nБАЛВАШКА16']).strip(),
            алю_сплав_6063_при_этом_тех_отхода1 = str(row['при этом % тех.отхода \r\n1-МЕТР БРАК17']).strip(),
            алю_сплав_6063_при_этом_тех_отхода2 = str(row['при этом % тех.отхода \r\nСТРУЖКА18']).strip(),
            ###############

            смазка_для_пресса_кг_графитовая = str(row['Графитовая19']).strip(),
            смазка_для_пресса_кг_пилы_хл_резки_сол = str(row['пилы холодной резки (Солярка)20']).strip(),
            смазка_для_пресса_кг_горячей_резки_сол = str(row[' горячей резки (Солярка)21']).strip(),
            смазка_для_пресса_кг_графитовые_плиты = str(row['графитовые плиты22']).strip(),
            хим_пг_к_окр_politeknik_кг_pol_ac_25p = str(row['POLITOKSAL AC 25P23']).strip(),
            хим_пг_к_окр_politeknik_кг_alupol_сr_51 = str(row['ALUPOL СR 5124']).strip(),
            хим_пг_к_окр_politeknik_кг_alupol_ac_52 = str(row['ALUPOL AC 5225']).strip(),
            пр_краситель_толщина_пк_мкм = str(row['толщина покрытия, мкм26']).strip(),
            порошковый_краситель_рас_кг_на_1000_пр = str(row['расход /кг на 1000 профилей27']).strip(),
            пр_краситель_при_этом_тех_отхода  = str(row['при этом % тех.отхода 28']).strip(),
            не_нужний = str(row['29']).strip(),
            суб_ширина_декор_пленки_мм_зол_дуб = str(row['ширина декор пленки/мм (Зол.дуб)30']).strip(),
            сублимация_расход_на_1000_профиль_м21 = str(row['расход на 1000 профиль/м²31']).strip(),
            суб_ширина_декор_пленки_мм_3д_313701 = str(row['ширина декор пленки/мм (3Д 3137-01) 32']).strip(),
            сублимация_расход_на_1000_профиль_м22 = str(row['расход на 1000 профиль/м²33']).strip(),
            суб_ширина_декор_пленки_мм_дуб_мокко = str(row['ширина декор пленки/мм (Дуб.мокко) 34']).strip(),
            сублимация_расход_на_1000_профиль_м23 = str(row['расход на 1000 профиль/м²35']).strip(),
            суб_ширина_декор_пленки_мм_3д_313702 = str(row['ширина декор пленки/мм (3Д 3137-02) 36']).strip(),
            сублимация_расход_на_1000_профиль_м24 = str(row['расход на 1000 профиль/м²37']).strip(),
            молярный_скотч_ширина1_мол_скотча_мм = str(row['ширина \r\nмол- скотча/мм38']).strip(),
            молярный_скотч_рас_на_1000_пр_шт1 = str(row['расход на 1000 профиль/шт39']).strip(),
            молярный_скотч_ширина2_мол_скотча_мм = str(row['ширина \r\nмол- скотча/мм40']).strip(),
            молярный_скотч_рас_на_1000_пр_шт2 = str(row['расход на 1000 профиль/шт41']).strip(),
            термомост_1 = str(row['Термомост 42']).strip(),
            краткий_текст_1 = str(row['Термомост 43']).strip(),
            термомост_2 = str(row['Термомост 44']).strip(),
            краткий_текст_2 = str(row['Термомост 45']).strip(),
            термомост_3 = str(row['Термомост 46']).strip(),
            краткий_текст_3 = str(row['Термомост 47']).strip(),
            термомост_4 = str(row['Термомост 48']).strip(),
            краткий_текст_4 = str(row['Термомост 49']).strip(),

            
            ламинация_верх_a_ширина_ленты_мм = str(row['ширина ленты/мм50']).strip(),
            лам_верх_a_рас_ленты_на_1000_пр_м2 = str(row['расход ленты на 1000 профилей/м²51']).strip(),
            ламинация_низ_b_ширина_ленты_мм = str(row['ширина ленты/мм52']).strip(),
            лам_низ_b_рас_ленты_на_1000_пр_м2 = str(row['расход ленты на 1000 профилей/м²53']).strip(),
            
            ламинация_низ_c_ширина_ленты_мм = str(row['ширина ленты/мм54']).strip(),
            лам_низ_c_рас_ленты_на_1000_пр_м2 = str(row['расход ленты на 1000 профилей/м²55']).strip(),
            лам_рас_праймера_на_1000_штук_пр_кг = str(row['расход праймера на 1000 штук профилей/кг56']).strip(),
            лам_рас_клея_на_1000_штук_пр_кг = str(row['расход клея на 1000 штук профилей/кг57']).strip(),
            лам_рас_уп_материала_мешок_на_1000_пр = str(row['Расход упаковочного материала (мешок) на 1000 профилей58']).strip(),
            

            заш_пл_кг_м_akfa_верх_ширина_ленты_мм = str(row['ширина ленты/мм59']).strip(),
            заш_пл_кг_м_akfa_бк_ст_ширина_ленты_мм = str(row['ширина ленты/мм60']).strip(),
            кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн = str(row['расход ленты на 1000 профилей/м261']).strip(),
            заш_пл_кг_м_akfa_низ_ширина_ленты_мм = str(row['ширина ленты/мм62']).strip(),
            заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2 = str(row['расход ленты на 1000 профиль/м263']).strip(),
        
            заш_пл_кг_м_retpen_верх_ширина_ленты_мм = str(row['ширина ленты/мм64']).strip(),
            заш_пл_кг_м_retpen_бк_ст_ширина_ленты = str(row['ширина ленты/мм65']).strip(),
            кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас = str(row['расход ленты на 1000 профилей/м266']).strip(),
            заш_пл_кг_м_retpen_низ_ширина_ленты_мм = str(row['ширина ленты/мм67']).strip(),
            заш_пл_кг_м_retpen_низ_рас  = str(row['расход ленты на 1000 профиль/м268']).strip(),
            
            заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм  = str(row['ширина ленты/мм69']).strip(),
            заш_пл_кг_м_benkam_жл_бк_ст_ширина_лн = str(row['ширина ленты/мм70']).strip(),
            кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас = str(row['расход ленты на 1000 профилей/м271']).strip(),
            заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм = str(row['ширина ленты/мм72']).strip(),
            заш_пл_кг_м_bn_жл_низ_рас = str(row['расход ленты на 1000 профиль/м273']).strip(),
            
            заш_пл_кг_м_голд_вр_ширина_лн_мм = str(row['ширина ленты/мм74']).strip(),
            заш_пл_кг_м_голд_бк_ст_ширина_лн_мм = str(row['ширина ленты/мм75']).strip(),
            кг_м_голд_вр_и_кг_м_голд_бк_ст_рас = str(row['расход ленты на 1000 профилей/м276']).strip(),
            заш_пл_кг_м_голд_низ_ширина_лн_мм = str(row['ширина ленты/мм77']).strip(),
            заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2 = str(row['расход ленты на 1000 профиль/м278']).strip(),
            
            заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм = str(row['ширина ленты/мм79']).strip(),
            заш_пл_кг_м_imzo_akfa_бк_ст_ширина_лн = str(row['ширина ленты/мм80']).strip(),
            кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст = str(row['расход ленты на 1000 профилей/м281']).strip(),
            заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм = str(row['ширина ленты/мм82']).strip(),
            заш_пл_кг_м_imzo_ak_низ_рас = str(row['расход ленты на 1000 профиль/м283']).strip(),
            
            заш_пл_кг_м_без_бр_вр_ширина_лн_мм = str(row['ширина ленты/мм84']).strip(),
            заш_пл_кг_м_без_бр_бк_ст_ширина_лн_мм = str(row['ширина ленты/мм85']).strip(),
            кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас = str(row['расход ленты на 1000 профилей/м286']).strip(),
            заш_пл_кг_м_без_бр_низ_ширина_лн_мм = str(row['ширина ленты/мм87']).strip(),
            заш_пл_кг_м_без_бр_низ_рас = str(row['расход ленты на 1000 профиль/м288']).strip(),
            
            заш_пл_кг_м_eng_верх_ширина_ленты_мм = str(row['ширина ленты/мм89']).strip(),
            заш_пл_кг_м_eng_бк_ст_ширина_ленты_мм = str(row['ширина ленты/мм90']).strip(),
            кг_м_eng_вр_и_кг_м_eng_бк_ст_рас = str(row['расход ленты на 1000 профилей/м291']).strip(),
            заш_пл_кг_м_eng_низ_ширина_ленты_мм = str(row['ширина ленты/мм92']).strip(),
            заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр = str(row['расход ленты на 1000 профиль/м293']).strip(),
            
            заш_пл_кг_м_eng_qora_вр_ширина_лн_мм = str(row['ширина ленты/мм94']).strip(),
            заш_пл_кг_м_eng_qora_бк_ст_ширина_лн_мм = str(row['ширина ленты/мм95']).strip(),
            кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст = str(row['расход ленты на 1000 профилей/м296']).strip(),
            заш_пл_кг_м_eng_qora_низ_ширина_ленты = str(row['ширина ленты/мм97']).strip(),
            заш_пл_кг_м_eng_qora_низ_рас = str(row['расход ленты на 1000 профиль/м298']).strip(),
            уп_пол_лента_ширина_уп_ленты_мм = str(row['ширина упоковочной ленты/мм99']).strip(),
            уп_пол_лн_рас_уп_лн_на_1000_штук_кг = str(row['расход упоковочной ленты на 1000 штук /кг100']).strip(),
            бумага_расход_упоковочной_ленты_на_1000_штук_кг = str(row['расход упоковочной ленты на 1000 штук /кг101']).strip(),


            расход_скотча_ширина_скотча_мм = str(row['ширина скотча/мм102']).strip(),
            рас_скотча_рас_скотча_на_1000_штук_шт = str(row['расход скотча на 1000 штук /Шт103']).strip(),
            упаковка_колво_профилей_в_1_пачке = str(row['Кол-во профилей в 1- пачке104']).strip(),
            qora_алю_сплав_6064_sap_code = str(row['Алюминиевый сплав 6063105']).strip(),
            закалка_исключение = str(row['Неокрашенный \r\n7000 ГП106']).strip(),
            наклейка_исключение = str(row['Наклейка исключения107']).strip(),
            
            )
        
        texcarta = TexCartaTime(
            компонент_1 = row['КОМПОНЕНТ1'],
            компонент_2 = row['КОМПОНЕНТ2'],
            компонент_3 = row['КОМПОНЕНТ3'],
            артикул = row['АРТИКУЛ4'],
            пресс_1_линия_буй = str(row['буй115']).strip(),
            закалка_1_печь_буй = str(row['буй125']).strip(),	
            
            покраска_SKM_белый_про_во_в_сутки_буй = str(row['Про-во в сутки\r\n(буй)133']).strip(),
            покраска_SAT_базовый_про_во_в_сутки_буй = str(row['Про-во в сутки\r\n(буй)138']).strip(),
            покраска_горизонтал_про_во_в_сутки_буй = str(row['Про-во в сутки\r\n(буй)143']).strip(),
            покраска_ручная_про_во_в_сутки_буй = str(row['Про-во в сутки\r\n(буй)148']).strip(),
            
            вакуум_1_печка_про_во_в_сутки_буй = str(row['Про-во в сутки\r\n(буй)159']).strip(),
            термо_1_линия_про_во_в_сутки_буй = str(row['Про-во в сутки\r\n(буй)165']).strip(),
            наклейка_упаковка_1_линия_про_во_в_сутки_буй = str(row['Про-во в сутки\r\n(буй)172']).strip(),
            ламинат_1_линия_про_во_в_сутки_буй = str(row['Про-во в сутки\r\n(буй)180']).strip(),
            
            ekstruziya = str(row['Экструзия (пресс)\r\n 1 буй(сек)117']).strip(),
            pila = str(row['Пила холодной резки \r\n 1 буй(сек)118']).strip(),
            strayenie = str(row['Старение\r\n 1 буй(сек)126']).strip(),
            skm_pokras = str(row['SKM - SKM покраска\r\n 1 буй(сек)134']).strip(),
            sat_pokras = str(row['SAT - SAT покраска\r\n 1 буй(сек)139']).strip(),
            gr_pokras = str(row['ГР - ГР покраска\r\n 1 буй(сек)144']).strip(),
            skm_xim = str(row['SKM Хим. Обработка\r\n 1 буй(сек)149']).strip(),
            sat_xim = str(row['SAT Хим. Обработка\r\n 1 буй(сек)150']).strip(),
            gr_xim = str(row['ГР Хим. Обработка\r\n 1 буй(сек)151']).strip(),
            ruchnoy_pokraska = str(row['Ручная покраска\r\n 1 буй(сек)152']).strip(),
            sublimat = str(row['Сублимация\r\n 1 буй(сек)160']).strip(),
            kombinirovan = str(row['Комбинирование \r\n 1 буй(сек)166']).strip(),
            kom_upakovka = str(row['Комбинированный + Упаковка\r\n 1 буй(сек)167']).strip(),
            nakleyka = str(row['Наклейка\r\n 1 буй(сек)174']).strip(),
            upakovka = str(row['Упаковка\r\n 1 буй(сек)175']).strip(),
            lam_nak_upakovka = str(row['Ламинация + Наклейка + Упаковка\r\nЛаминация + Упаковка\r\n 1 буй(сек)181']).strip()
            )
        norma.save()
        texcarta.save()

    Norma.objects.update(компонент_1 = Trim("компонент_1"), компонент_2 = Trim("компонент_2"), компонент_3 = Trim("компонент_3"),артикул = Trim("артикул"))
    TexCartaTime.objects.update(компонент_1 = Trim("компонент_1"), компонент_2 = Trim("компонент_2"), компонент_3 = Trim("компонент_3"),артикул = Trim("артикул"))
    

    return JsonResponse({'msg':True,'text':'Full updated'})

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def edit_norm(request,id):
    norma = Norma.objects.get( id = id)

    if request.method =='POST':
        instance = get_object_or_404(Norma, id=id)
        form = NormaEditForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('show_norm_base')
        
    form = NormaEditForm(instance = norma)
    context ={
        'norm':form,
    }
    return render(request,'norma/norma_crud/edit.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def edit_sikl(request,id):
    norma = TexCartaTime.objects.get( id = id)

    if request.method =='POST':
        instance = get_object_or_404(TexCartaTime, id=id)
        form = TexcartaEditForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('show_sikl_base')
        
    form = TexcartaEditForm(instance = norma)
    context ={
        'texcarta':form,
    }
    return render(request,'norma/norma_crud/edit_sikl_data.html',context)

@csrf_exempt
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def add_norm_post(request):   
    data = dict(request.POST)

    counter = 0
    for key,item in data.items():
        counter += 1

        if counter <= 4:
            continue
        if len(item) < 105:
            return JsonResponse({'msg':False,'text':'Kiritilayotgan shablon notog\'ri'})
        
        if not Norma.objects.filter(компонент_1 = str(item[1]).strip(),компонент_2 = str(item[2]).strip(),компонент_3 = str(item[3]).strip(),артикул = str(item[4]).strip()).exists():
            norma  = Norma.objects.update_or_create(
                устаревший = str(item[0]).strip(), 
                компонент_1 = str(item[1]).strip(),
                компонент_2 = str(item[2]).strip(),
                компонент_3 = str(item[3]).strip(),
                артикул = str(item[4]).strip(),
                серия = str(item[5]).strip(),
                наименование = str(item[6]).strip(),
                внешний_периметр_профиля_мм = str(item[7]).strip(),
                площадь_мм21 = str(item[8]).strip(),
                площадь_мм22 = str(item[9]).strip(),
                удельный_вес_профиля_кг_м = str(item[10]).strip(),
                диаметр_описанной_окружности_мм = str(item[11]).strip(),
                длина_профиля_м = str(item[12]).strip(),
                расчетное_колво_профиля_шт = str(item[13]).strip(),
                общий_вес_профиля_кг = str(item[14]).strip(),
                алю_сп_6063_рас_спа_на_1000_шт_пр_кг = str(item[15]).strip(),
                алюминиевый_сплав_6063_при_этом_балвашка = str(item[16]).strip(),
                алю_сплав_6063_при_этом_тех_отхода1 = str(item[17]).strip(),
                алю_сплав_6063_при_этом_тех_отхода2 = str(item[18]).strip(),
                смазка_для_пресса_кг_графитовая = str(item[19]).strip(),
                смазка_для_пресса_кг_пилы_хл_резки_сол = str(item[20]).strip(),
                смазка_для_пресса_кг_горячей_резки_сол = str(item[21]).strip(),
                смазка_для_пресса_кг_графитовые_плиты = str(item[22]).strip(),
                хим_пг_к_окр_politeknik_кг_pol_ac_25p = str(item[23]).strip(),
                хим_пг_к_окр_politeknik_кг_alupol_сr_51 = str(item[24]).strip(),
                хим_пг_к_окр_politeknik_кг_alupol_ac_52 = str(item[25]).strip(),
                пр_краситель_толщина_пк_мкм = str(item[26]).strip(),
                порошковый_краситель_рас_кг_на_1000_пр = str(item[27]).strip(),
                пр_краситель_при_этом_тех_отхода  = str(item[28]).strip(),
                не_нужний = str(item[29]).strip(),
                суб_ширина_декор_пленки_мм_зол_дуб = str(item[30]).strip(),
                сублимация_расход_на_1000_профиль_м21 = str(item[31]).strip(),
                суб_ширина_декор_пленки_мм_3д_313701 = str(item[32]).strip(),
                сублимация_расход_на_1000_профиль_м22 = str(item[33]).strip(),
                суб_ширина_декор_пленки_мм_дуб_мокко = str(item[34]).strip(),
                сублимация_расход_на_1000_профиль_м23 = str(item[35]).strip(),
                суб_ширина_декор_пленки_мм_3д_313702 = str(item[36]).strip(),
                сублимация_расход_на_1000_профиль_м24 = str(item[37]).strip(),
                молярный_скотч_ширина1_мол_скотча_мм = str(item[38]).strip(),
                молярный_скотч_рас_на_1000_пр_шт1 = str(item[39]).strip(),
                молярный_скотч_ширина2_мол_скотча_мм = str(item[40]).strip(),
                молярный_скотч_рас_на_1000_пр_шт2 = str(item[41]).strip(),
                термомост_1 = str(item[42]).strip(),
                термомост_2 = str(item[43]).strip(),
                термомост_3 = str(item[44]).strip(),
                термомост_4 = str(item[45]).strip(),
                
                ламинация_верх_a_ширина_ленты_мм = str(item[46]).strip(),
                лам_верх_a_рас_ленты_на_1000_пр_м2 = str(item[47]).strip(),
                ламинация_низ_b_ширина_ленты_мм = str(item[48]).strip(),
                лам_низ_b_рас_ленты_на_1000_пр_м2 = str(item[49]).strip(),
                
                ламинация_низ_c_ширина_ленты_мм = str(item[50]).strip(),
                лам_низ_c_рас_ленты_на_1000_пр_м2 = str(item[51]).strip(),
                лам_рас_праймера_на_1000_штук_пр_кг = str(item[52]).strip(),
                лам_рас_клея_на_1000_штук_пр_кг = str(item[53]).strip(),
                лам_рас_уп_материала_мешок_на_1000_пр = str(item[54]).strip(),
            
                заш_пл_кг_м_akfa_верх_ширина_ленты_мм = str(item[55]).strip(),
                заш_пл_кг_м_akfa_бк_ст_ширина_ленты_мм = str(item[56]).strip(),
                кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн = str(item[57]).strip(),
                заш_пл_кг_м_akfa_низ_ширина_ленты_мм = str(item[58]).strip(),
                заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2 = str(item[59]).strip(),
            
                заш_пл_кг_м_retpen_верх_ширина_ленты_мм = str(item[60]).strip(),
                заш_пл_кг_м_retpen_бк_ст_ширина_ленты = str(item[61]).strip(),
                кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас = str(item[62]).strip(),
                заш_пл_кг_м_retpen_низ_ширина_ленты_мм = str(item[63]).strip(),
                заш_пл_кг_м_retpen_низ_рас  = str(item[64]).strip(),
                
                заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм  = str(item[65]).strip(),
                заш_пл_кг_м_benkam_жл_бк_ст_ширина_лн = str(item[66]).strip(),
                кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас = str(item[67]).strip(),
                заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм = str(item[68]).strip(),
                заш_пл_кг_м_bn_жл_низ_рас = str(item[69]).strip(),
                
                заш_пл_кг_м_голд_вр_ширина_лн_мм = str(item[70]).strip(),
                заш_пл_кг_м_голд_бк_ст_ширина_лн_мм = str(item[71]).strip(),
                кг_м_голд_вр_и_кг_м_голд_бк_ст_рас = str(item[72]).strip(),
                заш_пл_кг_м_голд_низ_ширина_лн_мм = str(item[73]).strip(),
                заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2 = str(item[74]).strip(),
                
                заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм = str(item[75]).strip(),
                заш_пл_кг_м_imzo_akfa_бк_ст_ширина_лн = str(item[76]).strip(),
                кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст = str(item[77]).strip(),
                заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм = str(item[78]).strip(),
                заш_пл_кг_м_imzo_ak_низ_рас = str(item[79]).strip(),
                
                заш_пл_кг_м_без_бр_вр_ширина_лн_мм = str(item[80]).strip(),
                заш_пл_кг_м_без_бр_бк_ст_ширина_лн_мм = str(item[81]).strip(),
                кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас = str(item[82]).strip(),
                заш_пл_кг_м_без_бр_низ_ширина_лн_мм = str(item[83]).strip(),
                заш_пл_кг_м_без_бр_низ_рас = str(item[84]).strip(),
                
                заш_пл_кг_м_eng_верх_ширина_ленты_мм = str(item[85]).strip(),
                заш_пл_кг_м_eng_бк_ст_ширина_ленты_мм = str(item[86]).strip(),
                кг_м_eng_вр_и_кг_м_eng_бк_ст_рас = str(item[87]).strip(),
                заш_пл_кг_м_eng_низ_ширина_ленты_мм = str(item[88]).strip(),
                заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр = str(item[89]).strip(),
                
                заш_пл_кг_м_eng_qora_вр_ширина_лн_мм = str(item[90]).strip(),
                заш_пл_кг_м_eng_qora_бк_ст_ширина_лн_мм = str(item[91]).strip(),
                кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст = str(item[92]).strip(),
                заш_пл_кг_м_eng_qora_низ_ширина_ленты = str(item[93]).strip(),
                заш_пл_кг_м_eng_qora_низ_рас = str(item[94]).strip(),

                уп_пол_лента_ширина_уп_ленты_мм = str(item[95]).strip(),
                уп_пол_лн_рас_уп_лн_на_1000_штук_кг = str(item[96]).strip(),
                бумага_расход_упоковочной_ленты_на_1000_штук_кг =str(item[97]).strip(),
                расход_скотча_ширина_скотча_мм = str(item[98]).strip(),
                рас_скотча_рас_скотча_на_1000_штук_шт = str(item[99]).strip(),
                упаковка_колво_профилей_в_1_пачке = str(item[100]).strip(),
                qora_алю_сплав_6064_sap_code = str(item[101]).strip()
            )
        else:
            elem =[item[1],item[2],item[3],item[4]]
            return JsonResponse({'msg':False,'text':f'Bunday {elem} element mavjud, o\'chirib boshidan harakat qiling!'})
            # norma.save()
    
    return JsonResponse({'msg':True,'text':"Successfuly saved!"})

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def add_norm(request):
    return render(request,'norma/norma_crud/add.html')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def full_update_norm(request):
    return render(request,'norma/norma_crud/update.html')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def index(request):
    return render(request,'norma/index.html')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def show_norm_base(request):
    search_text = request.GET.get('search',None)

    if search_text:
        normas = Norma.objects.filter(Q(устаревший__icontains = search_text)|Q(компонент_1__icontains = search_text)|Q(компонент_2__icontains = search_text)|Q(компонент_3__icontains = search_text)|Q(артикул__icontains=search_text))
    else:
        normas = Norma.objects.all().order_by('created_at')

    paginator = Paginator(normas, 25)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)
    context = {
        'products':page_obj,
        'search':search_text,
        'section':'Все нормы'
    }
    return render(request,'norma/norma_crud/show_list.html',context)

# Create your views here.
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def show_sikl_base(request):
    search_text = request.GET.get('search',None)

    if search_text:
        texcartas = TexCartaTime.objects.filter(Q(компонент_1__icontains = search_text)|Q(компонент_2__icontains = search_text)|Q(компонент_3__icontains = search_text)|Q(артикул__icontains=search_text))
    else:
        texcartas = TexCartaTime.objects.all().order_by('created_at')

    paginator = Paginator(texcartas, 25)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)
    context = {
        'products':page_obj,
        'search':search_text,
        'section':'Все техкарты'
    }
    return render(request,'norma/norma_crud/show_list_sikl_data.html',context)

# Create your views here.
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def norma_excel(request):
    # df = pd.read_excel('c:\OSPanel\domains\\Norma22.xlsx','Общий')
    df = pd.read_excel('C:\\OpenServer\\domains\\Norma22.xlsx','Общий')
    df =df.astype(str)
    
    df =df.replace('nan','0')
    
    for i in range(0,df.shape[0]):
        if ((df["Устаревший"][i][-2:] =='.0') or (df["Устаревший"][i][-2:] ==',0')) :
            устаревший = df["Устаревший"][i].replace('.0','').replace(',0','')
        else:
            устаревший = df["Устаревший"][i].replace('.0','')
            
        if ((df["КОМПОНЕНТ 1"][i][-2:] =='.0') or (df["КОМПОНЕНТ 1"][i][-2:] ==',0')) :
            компонент_1 = df["КОМПОНЕНТ 1"][i].replace('.0','').replace(',0','')
        else:
            компонент_1 = df["КОМПОНЕНТ 1"][i]
            
        if ((df["КОМПОНЕНТ 2"][i] =='.0') or (df["КОМПОНЕНТ 2"][i] ==',0')) :
            компонент_2 = df["КОМПОНЕНТ 2"][i].replace('.0','').replace(',0','')
        else:
            компонент_2 = df["КОМПОНЕНТ 2"][i]
            
        if ((df["КОМПОНЕНТ 3"][i] =='.0') or (df["КОМПОНЕНТ 3"][i] ==',0')) :
            компонент_3 = df["КОМПОНЕНТ 3"][i].replace('.0','').replace(',0','')
        else:
            компонент_3 = df["КОМПОНЕНТ 3"][i]
            
        if ((df["АРТИКУЛ"][i] =='.0') or (df["АРТИКУЛ"][i] ==',0')) :
            артикул = df["АРТИКУЛ"][i].replace('.0','').replace(',0','')
        else:
            артикул = df["АРТИКУЛ"][i]
            
        if ((df["Серия"][i] =='.0') or (df["Серия"][i] ==',0')) :
            серия = df["Серия"][i].replace('.0','').replace(',0','')
        else:
            серия = df["Серия"][i]
            
        if ((df["Наименование"][i] =='.0') or (df["Наименование"][i] ==',0')) :
            наименование = df["Наименование"][i].replace('.0','').replace(',0','')
        else:
            наименование = df["Наименование"][i]
            
        if ((df["Внешний периметр профиля__ мм"][i] =='.0') or (df["Внешний периметр профиля__ мм"][i] ==',0')) :
            внешний_периметр_профиля_мм = df["Внешний периметр профиля__ мм"][i].replace('.0','').replace(',0','')
        else:
            внешний_периметр_профиля_мм = df["Внешний периметр профиля__ мм"][i]
            
        if ((df["Площадь __мм²"][i] =='.0') or (df["Площадь __мм²"][i] ==',0')) :
            площадь_мм21 = df["Площадь __мм²"][i].replace('.0','').replace(',0','')
        else:
            площадь_мм21 = df["Площадь __мм²"][i]
            
        if ((df["Площадь __мм²"][i] =='.0') or (df["Площадь __мм²"][i] ==',0')) :
            площадь_мм22 = df["Площадь __мм²"][i].replace('.0','').replace(',0','')
        else:
            площадь_мм22 = df["Площадь __мм²"][i]
            
        if ((df["Удельный вес профиля кг__м"][i] =='.0') or (df["Удельный вес профиля кг__м"][i] ==',0')) :
            удельный_вес_профиля_кг_м = df["Удельный вес профиля кг__м"][i].replace('.0','').replace(',0','')
        else:
            удельный_вес_профиля_кг_м = df["Удельный вес профиля кг__м"][i]
            
        if ((df["Диаметр описанной окружности__мм"][i] =='.0') or (df["Диаметр описанной окружности__мм"][i] ==',0')) :
            диаметр_описанной_окружности_мм = df["Диаметр описанной окружности__мм"][i].replace('.0','').replace(',0','')
        else:
            диаметр_описанной_окружности_мм = df["Диаметр описанной окружности__мм"][i]
            
        if ((df["Длина профиля__м"][i] =='.0') or (df["Длина профиля__м"][i] ==',0')) :
            длина_профиля_м = df["Длина профиля__м"][i].replace('.0','').replace(',0','')
        else:
            длина_профиля_м = df["Длина профиля__м"][i]
        if ((df["Расчетное кол-во профиля__шт"][i] =='.0') or (df["Расчетное кол-во профиля__шт"][i] ==',0')) :
            расчетное_колво_профиля_шт = df["Расчетное кол-во профиля__шт"][i].replace('.0','').replace(',0','')
        else:
            расчетное_колво_профиля_шт = df["Расчетное кол-во профиля__шт"][i]
        if ((df["Общий вес профиля__кг"][i] =='.0') or (df["Общий вес профиля__кг"][i] ==',0')) :
            общий_вес_профиля_кг = df["Общий вес профиля__кг"][i].replace('.0','').replace(',0','')
        else:
            общий_вес_профиля_кг = df["Общий вес профиля__кг"][i]
        if ((df["Алюминиевый сплав 6063 __ расход сплава на 1000 шт профиля__кг"][i] =='.0') or (df["Алюминиевый сплав 6063 __ расход сплава на 1000 шт профиля__кг"][i] ==',0')) :
            алю_сп_6063_рас_спа_на_1000_шт_пр_кг = df["Алюминиевый сплав 6063 __ расход сплава на 1000 шт профиля__кг"][i].replace('.0','').replace(',0','')
        else:
            алю_сп_6063_рас_спа_на_1000_шт_пр_кг = df["Алюминиевый сплав 6063 __ расход сплава на 1000 шт профиля__кг"][i]
        if ((df["Алюминиевый сплав 6063 __ при этом __ тех.отхода1"][i] =='.0') or (df["Алюминиевый сплав 6063 __ при этом __ тех.отхода1"][i] ==',0')) :
            алю_сплав_6063_при_этом_тех_отхода1 = df["Алюминиевый сплав 6063 __ при этом __ тех.отхода1"][i].replace('.0','').replace(',0','')
        else:
            алю_сплав_6063_при_этом_тех_отхода1 = df["Алюминиевый сплав 6063 __ при этом __ тех.отхода1"][i]
        if ((df["Алюминиевый сплав 6063 __ при этом __ тех.отхода2"][i] =='.0') or (df["Алюминиевый сплав 6063 __ при этом __ тех.отхода2"][i] ==',0')) :
            алю_сплав_6063_при_этом_тех_отхода2 = df["Алюминиевый сплав 6063 __ при этом __ тех.отхода2"][i].replace('.0','').replace(',0','')
        else:
            алю_сплав_6063_при_этом_тех_отхода2 = df["Алюминиевый сплав 6063 __ при этом __ тех.отхода2"][i]
        if ((df["Смазка для пресса__кг __ Графитовая"][i] =='.0') or (df["Смазка для пресса__кг __ Графитовая"][i] ==',0')) :
            смазка_для_пресса_кг_графитовая = df["Смазка для пресса__кг __ Графитовая"][i].replace('.0','').replace(',0','')
        else:
            смазка_для_пресса_кг_графитовая = df["Смазка для пресса__кг __ Графитовая"][i]
        
        
        
    
        смазка_для_пресса_кг_пилы_хл_резки_сол = df["Смазка для пресса__кг __ пилы холодной резки (Солярка)"][i].replace('.0','') if df["Смазка для пресса__кг __ пилы холодной резки (Солярка)"][i][-2:]=='.0' else df["Смазка для пресса__кг __ пилы холодной резки (Солярка)"][i]
        смазка_для_пресса_кг_горячей_резки_сол = df["Смазка для пресса__кг __ горячей резки (Солярка)"][i].replace('.0','') if df["Смазка для пресса__кг __ горячей резки (Солярка)"][i][-2:]=='.0' else df["Смазка для пресса__кг __ горячей резки (Солярка)"][i]
        смазка_для_пресса_кг_графитовые_плиты = df["Смазка для пресса__кг __ графитовые плиты"][i].replace('.0','') if df["Смазка для пресса__кг __ графитовые плиты"][i][-2:]=='.0' else df["Смазка для пресса__кг __ графитовые плиты"][i]
        хим_пг_к_окр_politeknik_кг_pol_ac_25p = df["Химикаты (подготовка к окрашиванию)__ POLITEKNIK кг __ POLITOKSAL AC 25P"][i].replace('.0','') if df["Химикаты (подготовка к окрашиванию)__ POLITEKNIK кг __ POLITOKSAL AC 25P"][i][-2:]=='.0' else df["Химикаты (подготовка к окрашиванию)__ POLITEKNIK кг __ POLITOKSAL AC 25P"][i]
        хим_пг_к_окр_politeknik_кг_alupol_сr_51 = df["Химикаты (подготовка к окрашиванию)__ POLITEKNIK кг __ ALUPOL СR 51"][i].replace('.0','') if df["Химикаты (подготовка к окрашиванию)__ POLITEKNIK кг __ ALUPOL СR 51"][i][-2:]=='.0' else df["Химикаты (подготовка к окрашиванию)__ POLITEKNIK кг __ ALUPOL СR 51"][i]
        хим_пг_к_окр_politeknik_кг_alupol_ac_52 = df["Химикаты (подготовка к окрашиванию)__ POLITEKNIK кг __ ALUPOL AC 52"][i].replace('.0','') if df["Химикаты (подготовка к окрашиванию)__ POLITEKNIK кг __ ALUPOL AC 52"][i][-2:]=='.0' else df["Химикаты (подготовка к окрашиванию)__ POLITEKNIK кг __ ALUPOL AC 52"][i]
        пр_краситель_толщина_пк_мкм = df["Порошковый краситель __ толщина покрытия, мкм"][i].replace('.0','') if df["Порошковый краситель __ толщина покрытия, мкм"][i][-2:]=='.0' else df["Порошковый краситель __ толщина покрытия, мкм"][i]
        
        порошковый_краситель_рас_кг_на_1000_пр = df["Порошковый краситель __ расход __кг на 1000 профилей"][i].replace('.0','') if df["Порошковый краситель __ расход __кг на 1000 профилей"][i][-2:]=='.0' else df["Порошковый краситель __ расход __кг на 1000 профилей"][i]
        пр_краситель_при_этом_тех_отхода = df["Порошковый краситель __ при этом __ тех.отхода "][i].replace('.0','') if df["Порошковый краситель __ при этом __ тех.отхода "][i][-2:]=='.0' else df["Порошковый краситель __ при этом __ тех.отхода "][i]
        не_нужний = df["Не нужний"][i].replace('.0','') if df["Не нужний"][i][-2:]=='.0' else df["Не нужний"][i]
        суб_ширина_декор_пленки_мм_зол_дуб = df["Сублимация __ ширина декор пленки__мм (Зол.дуб)"][i].replace('.0','') if df["Сублимация __ ширина декор пленки__мм (Зол.дуб)"][i][-2:]=='.0' else df["Сублимация __ ширина декор пленки__мм (Зол.дуб)"][i]
        сублимация_расход_на_1000_профиль_м21 = df["Сублимация __ расход на 1000 профиль__м21"][i].replace('.0','') if df["Сублимация __ расход на 1000 профиль__м21"][i][-2:]=='.0' else df["Сублимация __ расход на 1000 профиль__м21"][i]
        суб_ширина_декор_пленки_мм_3д_313701 = df["Сублимация __ ширина декор пленки__мм (3Д 3137-01) "][i].replace('.0','') if df["Сублимация __ ширина декор пленки__мм (3Д 3137-01) "][i][-2:]=='.0' else df["Сублимация __ ширина декор пленки__мм (3Д 3137-01) "][i]
        сублимация_расход_на_1000_профиль_м22 = df["Сублимация __ расход на 1000 профиль__м22"][i].replace('.0','') if df["Сублимация __ расход на 1000 профиль__м22"][i][-2:]=='.0' else df["Сублимация __ расход на 1000 профиль__м22"][i]
        суб_ширина_декор_пленки_мм_дуб_мокко = df["Сублимация __ ширина декор пленки__мм (Дуб.мокко) "][i].replace('.0','') if df["Сублимация __ ширина декор пленки__мм (Дуб.мокко) "][i][-2:]=='.0' else df["Сублимация __ ширина декор пленки__мм (Дуб.мокко) "][i]
        сублимация_расход_на_1000_профиль_м23 = df["Сублимация __ расход на 1000 профиль__м23"][i].replace('.0','') if df["Сублимация __ расход на 1000 профиль__м23"][i][-2:]=='.0' else df["Сублимация __ расход на 1000 профиль__м23"][i]
        суб_ширина_декор_пленки_мм_3д_313702 = df["Сублимация __ ширина декор пленки__мм (3Д 3137-02) "][i].replace('.0','') if df["Сублимация __ ширина декор пленки__мм (3Д 3137-02) "][i][-2:]=='.0' else df["Сублимация __ ширина декор пленки__мм (3Д 3137-02) "][i]
        сублимация_расход_на_1000_профиль_м24 = df["Сублимация __ расход на 1000 профиль__м24"][i].replace('.0','') if df["Сублимация __ расход на 1000 профиль__м24"][i][-2:]=='.0' else df["Сублимация __ расход на 1000 профиль__м24"][i]
        молярный_скотч_ширина1_мол_скотча_мм = df["Молярный скотч __ ширина1мол- скотча__мм"][i].replace('.0','') if df["Молярный скотч __ ширина1мол- скотча__мм"][i][-2:]=='.0' else df["Молярный скотч __ ширина1мол- скотча__мм"][i]
        молярный_скотч_рас_на_1000_пр_шт1 = df["Молярный скотч __ расход на 1000 профиль__шт1"][i].replace('.0','') if df["Молярный скотч __ расход на 1000 профиль__шт1"][i][-2:]=='.0' else df["Молярный скотч __ расход на 1000 профиль__шт1"][i]
        молярный_скотч_ширина2_мол_скотча_мм = df["Молярный скотч __ ширина2мол- скотча__мм"][i].replace('.0','') if df["Молярный скотч __ ширина2мол- скотча__мм"][i][-2:]=='.0' else df["Молярный скотч __ ширина2мол- скотча__мм"][i]
        молярный_скотч_рас_на_1000_пр_шт2 = df["Молярный скотч __ расход на 1000 профиль__шт2"][i].replace('.0','') if df["Молярный скотч __ расход на 1000 профиль__шт2"][i][-2:]=='.0' else df["Молярный скотч __ расход на 1000 профиль__шт2"][i]
        термомост_1 = df["Термомост 1"][i].replace('.0','') if df["Термомост 1"][i][-2:]=='.0' else df["Термомост 1"][i]
        термомост_2 = df["Термомост 2"][i].replace('.0','') if df["Термомост 2"][i][-2:]=='.0' else df["Термомост 2"][i]
        термомост_3 = df["Термомост 3"][i].replace('.0','') if df["Термомост 3"][i][-2:]=='.0' else df["Термомост 3"][i]
        термомост_4 = df["Термомост 4"][i].replace('.0','') if df["Термомост 4"][i][-2:]=='.0' else df["Термомост 4"][i]
        ламинация_верх_a_ширина_ленты_мм = df["Ламинация __ верх A __ ширина ленты__мм"][i].replace('.0','') if df["Ламинация __ верх A __ ширина ленты__мм"][i][-2:]=='.0' else df["Ламинация __ верх A __ ширина ленты__мм"][i]
        лам_верх_a_рас_ленты_на_1000_пр_м2 = df["Ламинация __ верх A __ расход ленты на 1000 профилей__м²"][i].replace('.0','') if df["Ламинация __ верх A __ расход ленты на 1000 профилей__м²"][i][-2:]=='.0' else df["Ламинация __ верх A __ расход ленты на 1000 профилей__м²"][i]
        ламинация_низ_b_ширина_ленты_мм = df["Ламинация __ низ B __ ширина ленты__мм"][i].replace('.0','') if df["Ламинация __ низ B __ ширина ленты__мм"][i][-2:]=='.0' else df["Ламинация __ низ B __ ширина ленты__мм"][i]
        лам_низ_b_рас_ленты_на_1000_пр_м2 = df["Ламинация __ низ B __ расход ленты на 1000 профилей__м²"][i].replace('.0','') if df["Ламинация __ низ B __ расход ленты на 1000 профилей__м²"][i][-2:]=='.0' else df["Ламинация __ низ B __ расход ленты на 1000 профилей__м²"][i]
        ламинация_низ_c_ширина_ленты_мм = df["Ламинация __ низ C __ ширина ленты__мм"][i].replace('.0','') if df["Ламинация __ низ C __ ширина ленты__мм"][i][-2:]=='.0' else df["Ламинация __ низ C __ ширина ленты__мм"][i]
        лам_низ_c_рас_ленты_на_1000_пр_м2 = df["Ламинация __ низ C __ расход ленты на 1000 профилей__м²"][i].replace('.0','') if df["Ламинация __ низ C __ расход ленты на 1000 профилей__м²"][i][-2:]=='.0' else df["Ламинация __ низ C __ расход ленты на 1000 профилей__м²"][i]
        лам_рас_праймера_на_1000_штук_пр_кг = df["Ламинация __ расход праймера на 1000 штук профилей__кг"][i].replace('.0','') if df["Ламинация __ расход праймера на 1000 штук профилей__кг"][i][-2:]=='.0' else df["Ламинация __ расход праймера на 1000 штук профилей__кг"][i]
        лам_рас_клея_на_1000_штук_пр_кг = df["Ламинация __ расход клея на 1000 штук профилей__кг"][i].replace('.0','') if df["Ламинация __ расход клея на 1000 штук профилей__кг"][i][-2:]=='.0' else df["Ламинация __ расход клея на 1000 штук профилей__кг"][i]
        лам_рас_уп_материала_мешок_на_1000_пр = df["Ламинация __ Расход упаковочного материала (мешок) на 1000 профилей"][i].replace('.0','') if df["Ламинация __ Расход упаковочного материала (мешок) на 1000 профилей"][i][-2:]=='.0' else df["Ламинация __ Расход упаковочного материала (мешок) на 1000 профилей"][i]
        заш_пл_кг_м_akfa_верх_ширина_ленты_мм = df["Защитная пленка__кг__м Akfa __ верх ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м Akfa __ верх ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м Akfa __ верх ширина ленты__мм"][i]
        заш_пл_кг_м_akfa_бк_ст_ширина_ленты_мм = df["Защитная пленка__кг__м Akfa __ (Боковая сторона) ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м Akfa __ (Боковая сторона) ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м Akfa __ (Боковая сторона) ширина ленты__мм"][i]
        кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн = df["Защитная пленка__кг__м Akfa __ верх и Защитная пленка__кг__м Akfa __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i].replace('.0','') if df["Защитная пленка__кг__м Akfa __ верх и Защитная пленка__кг__м Akfa __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i][-2:]=='.0' else df["Защитная пленка__кг__м Akfa __ верх и Защитная пленка__кг__м Akfa __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i]
        заш_пл_кг_м_akfa_низ_ширина_ленты_мм = df["Защитная пленка__кг__м Akfa __ низ ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м Akfa __ низ ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м Akfa __ низ ширина ленты__мм"][i]
        заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2 = df["Защитная пленка__кг__м Akfa __ низ расход ленты на 1000 профиль__м2"][i].replace('.0','') if df["Защитная пленка__кг__м Akfa __ низ расход ленты на 1000 профиль__м2"][i][-2:]=='.0' else df["Защитная пленка__кг__м Akfa __ низ расход ленты на 1000 профиль__м2"][i]
        заш_пл_кг_м_retpen_верх_ширина_ленты_мм = df["Защитная пленка__кг__м RETPEN __ верх ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м RETPEN __ верх ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м RETPEN __ верх ширина ленты__мм"][i]
        заш_пл_кг_м_retpen_бк_ст_ширина_ленты = df["Защитная пленка__кг__м RETPEN __ (Боковая сторона) ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м RETPEN __ (Боковая сторона) ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м RETPEN __ (Боковая сторона) ширина ленты__мм"][i]
        кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас = df["Защитная пленка__кг__м RETPEN __ верх и Защитная пленка__кг__м RETPEN __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i].replace('.0','') if df["Защитная пленка__кг__м RETPEN __ верх и Защитная пленка__кг__м RETPEN __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i][-2:]=='.0' else df["Защитная пленка__кг__м RETPEN __ верх и Защитная пленка__кг__м RETPEN __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i]
        заш_пл_кг_м_retpen_низ_ширина_ленты_мм = df["Защитная пленка__кг__м RETPEN __ низ ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м RETPEN __ низ ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м RETPEN __ низ ширина ленты__мм"][i]
        заш_пл_кг_м_retpen_низ_рас = df["Защитная пленка__кг__м RETPEN __ низ расход ленты на 1000 профиль__м2"][i].replace('.0','') if df["Защитная пленка__кг__м RETPEN __ низ расход ленты на 1000 профиль__м2"][i][-2:]=='.0' else df["Защитная пленка__кг__м RETPEN __ низ расход ленты на 1000 профиль__м2"][i]
        заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм = df["Защитная пленка__кг__м BENKAM (желтый) __ верх ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м BENKAM (желтый) __ верх ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м BENKAM (желтый) __ верх ширина ленты__мм"][i]
        заш_пл_кг_м_benkam_жл_бк_ст_ширина_лн = df["Защитная пленка__кг__м BENKAM (желтый) __ (Боковая сторона) ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м BENKAM (желтый) __ (Боковая сторона) ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м BENKAM (желтый) __ (Боковая сторона) ширина ленты__мм"][i]
        кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас = df["Защитная пленка__кг__м BENKAM (желтый) __ верх и Защитная пленка__кг__м BENKAM (желтый) __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i].replace('.0','') if df["Защитная пленка__кг__м BENKAM (желтый) __ верх и Защитная пленка__кг__м BENKAM (желтый) __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i][-2:]=='.0' else df["Защитная пленка__кг__м BENKAM (желтый) __ верх и Защитная пленка__кг__м BENKAM (желтый) __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i]
        заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм = df["Защитная пленка__кг__м BENKAM (желтый) __ низ ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м BENKAM (желтый) __ низ ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м BENKAM (желтый) __ низ ширина ленты__мм"][i]
        заш_пл_кг_м_bn_жл_низ_рас = df["Защитная пленка__кг__м BENKAM (желтый) __ низ расход ленты на 1000 профиль__м2"][i].replace('.0','') if df["Защитная пленка__кг__м BENKAM (желтый) __ низ расход ленты на 1000 профиль__м2"][i][-2:]=='.0' else df["Защитная пленка__кг__м BENKAM (желтый) __ низ расход ленты на 1000 профиль__м2"][i]
        
        заш_пл_кг_м_голд_вр_ширина_лн_мм = df["Защитная пленка__кг__м GOLD __ верх ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м GOLD __ верх ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м GOLD __ верх ширина ленты__мм"][i]
        заш_пл_кг_м_голд_бк_ст_ширина_лн_мм = df["Защитная пленка__кг__м GOLD __ (Боковая сторона) ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м GOLD __ (Боковая сторона) ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м GOLD __ (Боковая сторона) ширина ленты__мм"][i]
        кг_м_голд_вр_и_кг_м_голд_бк_ст_рас = df["Защитная пленка__кг__м GOLD __ верх и Защитная пленка__кг__м GOLD __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i].replace('.0','') if df["Защитная пленка__кг__м GOLD __ верх и Защитная пленка__кг__м GOLD __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i][-2:]=='.0' else df["Защитная пленка__кг__м GOLD __ верх и Защитная пленка__кг__м GOLD __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i]
        заш_пл_кг_м_голд_низ_ширина_лн_мм = df["Защитная пленка__кг__м GOLD __ низ ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м GOLD __ низ ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м GOLD __ низ ширина ленты__мм"][i]
        заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2 = df["Защитная пленка__кг__м GOLD __ низ расход ленты на 1000 профиль__м2"][i].replace('.0','') if df["Защитная пленка__кг__м GOLD __ низ расход ленты на 1000 профиль__м2"][i][-2:]=='.0' else df["Защитная пленка__кг__м GOLD __ низ расход ленты на 1000 профиль__м2"][i]
        
        заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм = df["Защитная пленка__кг__м IMZO AKFA __ верх ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м IMZO AKFA __ верх ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м IMZO AKFA __ верх ширина ленты__мм"][i]
        заш_пл_кг_м_imzo_akfa_бк_ст_ширина_лн = df["Защитная пленка__кг__м IMZO AKFA __ (Боковая сторона) ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м IMZO AKFA __ (Боковая сторона) ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м IMZO AKFA __ (Боковая сторона) ширина ленты__мм"][i]
        кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст = df["Защитная пленка__кг__м IMZO AKFA __ верх и Защитная пленка__кг__м IMZO AKFA __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i].replace('.0','') if df["Защитная пленка__кг__м IMZO AKFA __ верх и Защитная пленка__кг__м IMZO AKFA __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i][-2:]=='.0' else df["Защитная пленка__кг__м IMZO AKFA __ верх и Защитная пленка__кг__м IMZO AKFA __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i]
        заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм = df["Защитная пленка__кг__м IMZO AKFA __ низ ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м IMZO AKFA __ низ ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м IMZO AKFA __ низ ширина ленты__мм"][i]
        заш_пл_кг_м_imzo_ak_низ_рас = df["Защитная пленка__кг__м IMZO AKFA __ низ расход ленты на 1000 профиль__м2"][i].replace('.0','') if df["Защитная пленка__кг__м IMZO AKFA __ низ расход ленты на 1000 профиль__м2"][i][-2:]=='.0' else df["Защитная пленка__кг__м IMZO AKFA __ низ расход ленты на 1000 профиль__м2"][i]

        
        
        заш_пл_кг_м_без_бр_вр_ширина_лн_мм = df["Защитная пленка__кг__м Без бренд __ верх ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м Без бренд __ верх ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м Без бренд __ верх ширина ленты__мм"][i]
        заш_пл_кг_м_без_бр_бк_ст_ширина_лн_мм = df["Защитная пленка__кг__м Без бренд __ (Боковая сторона) ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м Без бренд __ (Боковая сторона) ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м Без бренд __ (Боковая сторона) ширина ленты__мм"][i]
        кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас = df["Защитная пленка__кг__м Без бренд __ верх и Защитная пленка__кг__м Без бренд __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i].replace('.0','') if df["Защитная пленка__кг__м Без бренд __ верх и Защитная пленка__кг__м Без бренд __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i][-2:]=='.0' else df["Защитная пленка__кг__м Без бренд __ верх и Защитная пленка__кг__м Без бренд __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i]
        заш_пл_кг_м_без_бр_низ_ширина_лн_мм = df["Защитная пленка__кг__м Без бренд __ низ ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м Без бренд __ низ ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м Без бренд __ низ ширина ленты__мм"][i]
        заш_пл_кг_м_без_бр_низ_рас = df["Защитная пленка__кг__м Без бренд __ низ расход ленты на 1000 профиль__м2"][i].replace('.0','') if df["Защитная пленка__кг__м Без бренд __ низ расход ленты на 1000 профиль__м2"][i][-2:]=='.0' else df["Защитная пленка__кг__м Без бренд __ низ расход ленты на 1000 профиль__м2"][i]
        заш_пл_кг_м_eng_верх_ширина_ленты_мм = df["Защитная пленка__кг__м Engelberg __ верх ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м Engelberg __ верх ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м Engelberg __ верх ширина ленты__мм"][i]
        заш_пл_кг_м_eng_бк_ст_ширина_ленты_мм = df["Защитная пленка__кг__м Engelberg __ (Боковая сторона) ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м Engelberg __ (Боковая сторона) ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м Engelberg __ (Боковая сторона) ширина ленты__мм"][i]
        кг_м_eng_вр_и_кг_м_eng_бк_ст_рас = df["Защитная пленка__кг__м Engelberg __ верх и Защитная пленка__кг__м Engelberg __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i].replace('.0','') if df["Защитная пленка__кг__м Engelberg __ верх и Защитная пленка__кг__м Engelberg __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i][-2:]=='.0' else df["Защитная пленка__кг__м Engelberg __ верх и Защитная пленка__кг__м Engelberg __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i]
        заш_пл_кг_м_eng_низ_ширина_ленты_мм = df["Защитная пленка__кг__м Engelberg __ низ ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м Engelberg __ низ ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м Engelberg __ низ ширина ленты__мм"][i]
        заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр = df["Защитная пленка__кг__м Engelberg __ низ расход ленты на 1000 профиль__м2"][i].replace('.0','') if df["Защитная пленка__кг__м Engelberg __ низ расход ленты на 1000 профиль__м2"][i][-2:]=='.0' else df["Защитная пленка__кг__м Engelberg __ низ расход ленты на 1000 профиль__м2"][i]
        заш_пл_кг_м_eng_qora_вр_ширина_лн_мм = df["Защитная пленка__кг__м Engelberg (QORA) __ верх ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м Engelberg (QORA) __ верх ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м Engelberg (QORA) __ верх ширина ленты__мм"][i]
        заш_пл_кг_м_eng_qora_бк_ст_ширина_лн_мм = df["Защитная пленка__кг__м Engelberg (QORA) __ (Боковая сторона) ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м Engelberg (QORA) __ (Боковая сторона) ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м Engelberg (QORA) __ (Боковая сторона) ширина ленты__мм"][i]
        кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст = df["Защитная пленка__кг__м Engelberg (QORA) __ верх и Защитная пленка__кг__м Engelberg (QORA) __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i].replace('.0','') if df["Защитная пленка__кг__м Engelberg (QORA) __ верх и Защитная пленка__кг__м Engelberg (QORA) __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i][-2:]=='.0' else df["Защитная пленка__кг__м Engelberg (QORA) __ верх и Защитная пленка__кг__м Engelberg (QORA) __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i]
        заш_пл_кг_м_eng_qora_низ_ширина_ленты = df["Защитная пленка__кг__м Engelberg (QORA) __ низ ширина ленты__мм"][i].replace('.0','') if df["Защитная пленка__кг__м Engelberg (QORA) __ низ ширина ленты__мм"][i][-2:]=='.0' else df["Защитная пленка__кг__м Engelberg (QORA) __ низ ширина ленты__мм"][i]
        заш_пл_кг_м_eng_qora_низ_рас = df["Защитная пленка__кг__м Engelberg (QORA) __ низ расход ленты на 1000 профиль__м2"][i].replace('.0','') if df["Защитная пленка__кг__м Engelberg (QORA) __ низ расход ленты на 1000 профиль__м2"][i][-2:]=='.0' else df["Защитная пленка__кг__м Engelberg (QORA) __ низ расход ленты на 1000 профиль__м2"][i]
        уп_пол_лента_ширина_уп_ленты_мм = df["Упаковочная полиэтиленовая лента __ ширина упоковочной ленты__мм"][i].replace('.0','') if df["Упаковочная полиэтиленовая лента __ ширина упоковочной ленты__мм"][i][-2:]=='.0' else df["Упаковочная полиэтиленовая лента __ ширина упоковочной ленты__мм"][i]
        уп_пол_лн_рас_уп_лн_на_1000_штук_кг = df["Упаковочная полиэтиленовая лента __ расход упоковочной ленты на 1000 штук __кг"][i].replace('.0','') if df["Упаковочная полиэтиленовая лента __ расход упоковочной ленты на 1000 штук __кг"][i][-2:]=='.0' else df["Упаковочная полиэтиленовая лента __ расход упоковочной ленты на 1000 штук __кг"][i]
        расход_скотча_ширина_скотча_мм = df["Расход скотча __ ширина скотча__мм"][i].replace('.0','') if df["Расход скотча __ ширина скотча__мм"][i][-2:]=='.0' else df["Расход скотча __ ширина скотча__мм"][i]
        рас_скотча_рас_скотча_на_1000_штук_шт = df["Расход скотча __ расход скотча на 1000 штук __Шт"][i].replace('.0','') if df["Расход скотча __ расход скотча на 1000 штук __Шт"][i][-2:]=='.0' else df["Расход скотча __ расход скотча на 1000 штук __Шт"][i]
        упаковка_колво_профилей_в_1_пачке = df["Упаковка __ Кол-во профилей в 1- пачке"][i].replace('.0','') if df["Упаковка __ Кол-во профилей в 1- пачке"][i][-2:]=='.0' else df["Упаковка __ Кол-во профилей в 1- пачке"][i]
        бумага_расход_упоковочной_ленты_на_1000_штук_кг = df["Крафт бумага_расход упоковочной ленты на 1000 штук__кг"][i].replace('.0','') if df["Крафт бумага_расход упоковочной ленты на 1000 штук__кг"][i][-2:]=='.0' else df["Крафт бумага_расход упоковочной ленты на 1000 штук__кг"][i]
        qora_алю_сплав_6064_sap_code = df["AL-A7 (Oddiy) __ AL-A8 (Qora) Алюминиевый сплав 6064"][i].replace('.0','') if df["AL-A7 (Oddiy) __ AL-A8 (Qora) Алюминиевый сплав 6064"][i][-2:]=='.0' else df["AL-A7 (Oddiy) __ AL-A8 (Qora) Алюминиевый сплав 6064"][i]
        алюминиевый_сплав_6063_при_этом_балвашка =df['Алюминиевый сплав 6063 __ при этом __балвашка'][i].replace('.0','') if df['Алюминиевый сплав 6063 __ при этом __балвашка'][i][-2:]=='.0' else df['Алюминиевый сплав 6063 __ при этом __балвашка'][i]
        
        Norma(
        устаревший =устаревший,  
        компонент_1 =компонент_1,  
        компонент_2 =компонент_2,  
        компонент_3 =компонент_3,  
        артикул =артикул,  
        серия =серия,  
        наименование =наименование,  
        внешний_периметр_профиля_мм =внешний_периметр_профиля_мм,  
        площадь_мм21 =площадь_мм21,  
        площадь_мм22 =площадь_мм22,  
        удельный_вес_профиля_кг_м =удельный_вес_профиля_кг_м,  
        диаметр_описанной_окружности_мм =диаметр_описанной_окружности_мм,  
        длина_профиля_м =длина_профиля_м,  
        расчетное_колво_профиля_шт =расчетное_колво_профиля_шт,  
        общий_вес_профиля_кг =общий_вес_профиля_кг,  
        алю_сп_6063_рас_спа_на_1000_шт_пр_кг =алю_сп_6063_рас_спа_на_1000_шт_пр_кг,  
        алю_сплав_6063_при_этом_тех_отхода1 =алю_сплав_6063_при_этом_тех_отхода1,  
        алю_сплав_6063_при_этом_тех_отхода2 =алю_сплав_6063_при_этом_тех_отхода2,  
        смазка_для_пресса_кг_графитовая =смазка_для_пресса_кг_графитовая,  
        смазка_для_пресса_кг_пилы_хл_резки_сол =смазка_для_пресса_кг_пилы_хл_резки_сол,  
        смазка_для_пресса_кг_горячей_резки_сол =смазка_для_пресса_кг_горячей_резки_сол,  
        смазка_для_пресса_кг_графитовые_плиты =смазка_для_пресса_кг_графитовые_плиты,  
        хим_пг_к_окр_politeknik_кг_pol_ac_25p =хим_пг_к_окр_politeknik_кг_pol_ac_25p,  
        хим_пг_к_окр_politeknik_кг_alupol_сr_51 =хим_пг_к_окр_politeknik_кг_alupol_сr_51,  
        хим_пг_к_окр_politeknik_кг_alupol_ac_52 =хим_пг_к_окр_politeknik_кг_alupol_ac_52,  
        пр_краситель_толщина_пк_мкм =пр_краситель_толщина_пк_мкм,  
        порошковый_краситель_рас_кг_на_1000_пр =порошковый_краситель_рас_кг_на_1000_пр,  
        пр_краситель_при_этом_тех_отхода  =пр_краситель_при_этом_тех_отхода ,  
        не_нужний =не_нужний,  
        суб_ширина_декор_пленки_мм_зол_дуб =суб_ширина_декор_пленки_мм_зол_дуб,  
        сублимация_расход_на_1000_профиль_м21 =сублимация_расход_на_1000_профиль_м21,  
        суб_ширина_декор_пленки_мм_3д_313701 =суб_ширина_декор_пленки_мм_3д_313701,  
        сублимация_расход_на_1000_профиль_м22 =сублимация_расход_на_1000_профиль_м22,  
        суб_ширина_декор_пленки_мм_дуб_мокко =суб_ширина_декор_пленки_мм_дуб_мокко,  
        сублимация_расход_на_1000_профиль_м23 =сублимация_расход_на_1000_профиль_м23,  
        суб_ширина_декор_пленки_мм_3д_313702 =суб_ширина_декор_пленки_мм_3д_313702,  
        сублимация_расход_на_1000_профиль_м24 =сублимация_расход_на_1000_профиль_м24,  
        молярный_скотч_ширина1_мол_скотча_мм =молярный_скотч_ширина1_мол_скотча_мм,   
        молярный_скотч_рас_на_1000_пр_шт1 =молярный_скотч_рас_на_1000_пр_шт1,  
        молярный_скотч_ширина2_мол_скотча_мм =молярный_скотч_ширина2_мол_скотча_мм,   
        молярный_скотч_рас_на_1000_пр_шт2 =молярный_скотч_рас_на_1000_пр_шт2,  
        термомост_1 =термомост_1,  
        термомост_2 =термомост_2,  
        термомост_3 =термомост_3,  
        термомост_4 =термомост_4,  
        ламинация_верх_a_ширина_ленты_мм =ламинация_верх_a_ширина_ленты_мм,  
        лам_верх_a_рас_ленты_на_1000_пр_м2 =лам_верх_a_рас_ленты_на_1000_пр_м2,  
        ламинация_низ_b_ширина_ленты_мм =ламинация_низ_b_ширина_ленты_мм,  
        лам_низ_b_рас_ленты_на_1000_пр_м2 =лам_низ_b_рас_ленты_на_1000_пр_м2,  
        ламинация_низ_c_ширина_ленты_мм =ламинация_низ_c_ширина_ленты_мм,  
        лам_низ_c_рас_ленты_на_1000_пр_м2 =лам_низ_c_рас_ленты_на_1000_пр_м2,  
        лам_рас_праймера_на_1000_штук_пр_кг =лам_рас_праймера_на_1000_штук_пр_кг,  
        лам_рас_клея_на_1000_штук_пр_кг =лам_рас_клея_на_1000_штук_пр_кг,  
        лам_рас_уп_материала_мешок_на_1000_пр =лам_рас_уп_материала_мешок_на_1000_пр,  
        заш_пл_кг_м_akfa_верх_ширина_ленты_мм =заш_пл_кг_м_akfa_верх_ширина_ленты_мм,  
        заш_пл_кг_м_akfa_бк_ст_ширина_ленты_мм =заш_пл_кг_м_akfa_бк_ст_ширина_ленты_мм,  
        кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн =кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн,  
        заш_пл_кг_м_akfa_низ_ширина_ленты_мм =заш_пл_кг_м_akfa_низ_ширина_ленты_мм,  
        заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2 =заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2,  
        заш_пл_кг_м_retpen_верх_ширина_ленты_мм =заш_пл_кг_м_retpen_верх_ширина_ленты_мм,  
        заш_пл_кг_м_retpen_бк_ст_ширина_ленты =заш_пл_кг_м_retpen_бк_ст_ширина_ленты,  
        кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас =кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас,  
        заш_пл_кг_м_retpen_низ_ширина_ленты_мм =заш_пл_кг_м_retpen_низ_ширина_ленты_мм,  
        заш_пл_кг_м_retpen_низ_рас  =заш_пл_кг_м_retpen_низ_рас ,  
        заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм  =заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм ,  
        заш_пл_кг_м_benkam_жл_бк_ст_ширина_лн =заш_пл_кг_м_benkam_жл_бк_ст_ширина_лн,  
        кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас =кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас,  
        заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм =заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,  
        заш_пл_кг_м_bn_жл_низ_рас =заш_пл_кг_м_bn_жл_низ_рас,  
        
        заш_пл_кг_м_голд_вр_ширина_лн_мм =заш_пл_кг_м_голд_вр_ширина_лн_мм,  
        заш_пл_кг_м_голд_бк_ст_ширина_лн_мм =заш_пл_кг_м_голд_бк_ст_ширина_лн_мм,  
        кг_м_голд_вр_и_кг_м_голд_бк_ст_рас =кг_м_голд_вр_и_кг_м_голд_бк_ст_рас,  
        заш_пл_кг_м_голд_низ_ширина_лн_мм =заш_пл_кг_м_голд_низ_ширина_лн_мм,  
        заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2 =заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2,  
        
        заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,  
        заш_пл_кг_м_imzo_akfa_бк_ст_ширина_лн =заш_пл_кг_м_imzo_akfa_бк_ст_ширина_лн,  
        кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст =кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст,  
        заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм =заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,  
        заш_пл_кг_м_imzo_ak_низ_рас =заш_пл_кг_м_imzo_ak_низ_рас,  
        заш_пл_кг_м_без_бр_вр_ширина_лн_мм =заш_пл_кг_м_без_бр_вр_ширина_лн_мм,  
        заш_пл_кг_м_без_бр_бк_ст_ширина_лн_мм =заш_пл_кг_м_без_бр_бк_ст_ширина_лн_мм,  
        кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас =кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас,  
        заш_пл_кг_м_без_бр_низ_ширина_лн_мм =заш_пл_кг_м_без_бр_низ_ширина_лн_мм,  
        заш_пл_кг_м_без_бр_низ_рас =заш_пл_кг_м_без_бр_низ_рас,  
        заш_пл_кг_м_eng_верх_ширина_ленты_мм =заш_пл_кг_м_eng_верх_ширина_ленты_мм,  
        заш_пл_кг_м_eng_бк_ст_ширина_ленты_мм =заш_пл_кг_м_eng_бк_ст_ширина_ленты_мм,  
        кг_м_eng_вр_и_кг_м_eng_бк_ст_рас =кг_м_eng_вр_и_кг_м_eng_бк_ст_рас,  
        заш_пл_кг_м_eng_низ_ширина_ленты_мм =заш_пл_кг_м_eng_низ_ширина_ленты_мм,  
        заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр =заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр,  
        заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,  
        заш_пл_кг_м_eng_qora_бк_ст_ширина_лн_мм =заш_пл_кг_м_eng_qora_бк_ст_ширина_лн_мм,  
        кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст =кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст,  
        заш_пл_кг_м_eng_qora_низ_ширина_ленты =заш_пл_кг_м_eng_qora_низ_ширина_ленты,  
        заш_пл_кг_м_eng_qora_низ_рас =заш_пл_кг_м_eng_qora_низ_рас,  
        уп_пол_лента_ширина_уп_ленты_мм =уп_пол_лента_ширина_уп_ленты_мм,  
        уп_пол_лн_рас_уп_лн_на_1000_штук_кг =уп_пол_лн_рас_уп_лн_на_1000_штук_кг,  
        расход_скотча_ширина_скотча_мм =расход_скотча_ширина_скотча_мм,  
        рас_скотча_рас_скотча_на_1000_штук_шт =рас_скотча_рас_скотча_на_1000_штук_шт,  
        упаковка_колво_профилей_в_1_пачке =упаковка_колво_профилей_в_1_пачке,  
        qora_алю_сплав_6064_sap_code = qora_алю_сплав_6064_sap_code,
        бумага_расход_упоковочной_ленты_на_1000_штук_кг = бумага_расход_упоковочной_ленты_на_1000_штук_кг,
        алюминиевый_сплав_6063_при_этом_балвашка = алюминиевый_сплав_6063_при_этом_балвашка
        ).save()  
    
    normas = Norma.objects.all()
    
    for norma in normas:
        print(norma.id)
        norma.компонент_1 = norma.компонент_1.strip()
        norma.компонент_2 = norma.компонент_2.strip()
        norma.компонент_3 = norma.компонент_3.strip()
        norma.артикул = norma.артикул.strip()
        norma.save()
        
    return redirect('index')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])   
def receipt_all(request):
    df = pd.read_excel('C:\\OpenServer\\domains\\Наклейка.xlsx','Наклейка')
    df =df.astype(str)
    
    for i in range(0,df.shape[0]):
        sap_code_s4q100 = df['SAP code S4Q100'][i]
        название = df['Название'][i]
        еи = df['ЕИ'][i]
        склад_закупа = df['Склад закупа'][i]
        код_наклейки = df['Код наклейки'][i]
        название_наклейки = df['название наклейки'][i]
        ширина = df['Ширина'][i]
        еи_ширины = df['ЕИ ширины'][i]
        тип_клея = df['Тип клея '][i]
        Nakleyka(
            sap_code_s4q100 = sap_code_s4q100, 
            название = название, 
            еи = еи, 
            склад_закупа = склад_закупа, 
            код_наклейки = код_наклейки, 
            название_наклейки = название_наклейки, 
            ширина = ширина, 
            еи_ширины = еи_ширины, 
            тип_клея = тип_клея
            ).save()
    ######end Nakleyka
    print('nakleyka tugadi')
    
    
    
    print('prochiye siryo tugadi')
    
    return JsonResponse({'Hammasi bo\'ldi':'ok'})

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def norma_add(request):
    df = pd.read_excel('c:\\Users\\Acer\\Desktop\\Копия Thermo profilesййй2.xlsx','Лист1')
    df =df.astype(str)
    print(df)
    for key, row in df.iterrows():
        artikul = row['Articale']
        component1 = row['Component № 1']
        component2 = row['Component № 2']
        component3 = row['Component № 3']
        sap_code1 = row['SAP код1']
        termal_bridge1 =row['Thermal bridge № 1']
        sap_code2 =row['SAP код2']
        termal_bridge2 = row['Thermal bridge № 2']
        sap_code3 = row['SAP код3']
        termal_bridge3 = row['Thermal bridge № 3']
        sap_code4 =row['SAP код4']
        termal_bridge4 =row['Thermal bridge № 4']
        
       
    
    return JsonResponse({'a':'b'})
    
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def file_upload(request): 
  if request.method == 'POST':
    form = NormaFileForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('norma_file_list')
  else:
      form =NormaFileForm()
      context ={
        'form':form
      }
  return render(request,'norma/excel_form.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def file_upload_termo_org(request): 
  if request.method == 'POST':
    data = request.POST.copy()
    data['type']='termo'
    form = NormaFileForm(data, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('norma_file_list_termo_org')
  else:
      form =NormaFileForm()
      context ={
        'section':''
      }
  return render(request,'universal/main.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def file_upload_org(request): 
  if request.method == 'POST':
    data = request.POST.copy()
    data['type']='simple'
    form = NormaFileForm(data, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('norma_file_list_org')
  else:
      form =NormaFileForm()
      context ={
        'section':''
      }
  return render(request,'universal/main.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def file_list(request):
    files = NormaExcelFiles.objects.filter(generated =False).order_by('-created_at')
    context ={'files':files}
    return render(request,'norma/file_list.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def file_list_org(request):
    files = NormaExcelFiles.objects.filter(generated =False,type='simple').order_by('-created_at')
    context ={'files':files,
              'link':'/norma/process-combinirovanniy/',
              'section':'Генерация норма обычного файла',
              'type':'обычный',
              'file_type':'simple'
              }
    return render(request,'universal/file_list_norma.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def file_list_termo_org(request):
    files = NormaExcelFiles.objects.filter(generated =False,type='termo').order_by('-created_at')
    context ={'files':files,
              'link':'/norma/process-combinirovanniy/',
              'section':'Генерация норма термо файла',
              'type':'термо',
              'file_type':'termo'
              }
    return render(request,'universal/file_list_norma.html',context)

def get_legth(lengg):
    lls =lengg.split()
    for ll in lls:
        if ll.startswith('L'):
            hh =ll.replace('L','')
            break
    return (float(hh)/1000) 


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def kombinirovaniy_process(request,id):
    file = NormaExcelFiles.objects.get(id=id).file
    file_path =f'{MEDIA_ROOT}\\{file}'
    df_exell = pd.read_excel(file_path)
    df_exell = df_exell.fillna('')
    df_exell =df_exell.astype(str)
    
   
    pro_type = request.GET.get('type','termo')

    if pro_type.replace("'","") =='termo':
        product_type ='termo'
        file_content ='термо'
    else:
        file_content ='обычный'
        product_type ='simple'
    df = []
    
    norma_list,kraska_list,accessuar,nakleyka_iskyuch,zakalka_iskyuchenie,zakalka_iskyuchenie6064 = norma_for_list()
   
    check_for_existing =[]
    artikul_org=''
    kratkiy_org=''
    for key,row in df_exell.iterrows():
        df.append([
            row['SAP код E'],row['Экструзия холодная резка'],
            row['SAP код Z'],row['Печь старения'],
            row['SAP код P'],row['Покраска автомат'],
            row['SAP код S'],row['Сублимация'],
            row['SAP код N'],row['Наклейка'],
            row['SAP код K'],row['K-Комбинирования'],
            row['SAP код 7'],row['U-Упаковка + Готовая Продукция']
        ])
        
    norma = []
    does_not_exist_norm =[]
    alumniy_silindr = []
    subdekor = []
    kraska =[]
    nakleyka_N = []
    kombinirovanniy = []
    isklyucheniye_ids = []
    lamplyonka = []
    k = -1
    for fullsapkod in df:
        k += 1
        if df[k][12] != '':
            artikul_org = df[k][12].split('-')[0]
        
        if df[k][13] != '':
            kratkiy_org = df[k][13]
        for i in range(0,7):
            t= fullsapkod[i * 2]
            length = fullsapkod[i * 2].split('-')
            
            if fullsapkod[i * 2]!='':
                if length[0] not in  norma_list:
                    isklyucheniye_ids.append(k)
                    does_not_exist_norm.append(length[0])
                    if [length[0],'','','','','','','','','','','Normada Sap code yo\'q',['#e2d810','white','white','white','white','white','white']] not in norma:
                        norma.append([length[0],'','','','','','','','','','','Normada Sap code yo\'q',['#e2d810','white','white','white','white','white','white']])
                
                if ((('-E' in t) or ('-Z' in t) or ('-P' in t)) and (length[0] not in does_not_exist_norm)):
                    if '-P' in t:
                        kraska_code = fullsapkod[i*2+1].split()[-1]
                        if kraska_code!='MF':
                            if kraska_code[1:] not in kraska_list:
                                isklyucheniye_ids.append(k) 
                                if kraska_code not in  kraska:                                  
                                    kraska.append(kraska_code)       
                    if artikul_org!='':
                        if product_type =='termo':              
                            alum_teks_all =  Norma.objects.filter(Q(компонент_1=length[0])|Q(компонент_2=length[0])|Q(компонент_3=length[0]) | Q(артикул =artikul_org))
                        else:
                            alum_teks_all = Norma.objects.filter(Q(компонент_1=length[0])|Q(компонент_2=length[0])|Q(компонент_3=length[0])|Q(артикул =artikul_org))
                    else:
                        alum_teks_all = Norma.objects.filter(Q(компонент_1=length[0])|Q(компонент_2=length[0])|Q(компонент_3=length[0]))
                    alum_teks = alum_teks_all[:1].get()
                    if ((alum_teks.qora_алю_сплав_6064_sap_code !='0')):
                        if not AlyuminniysilindrEkstruziya1.objects.filter(sap_code_s4q100 =alum_teks.qora_алю_сплав_6064_sap_code).exists():
                            isklyucheniye_ids.append(k)
                            if [length[0],alum_teks.qora_алю_сплав_6064_sap_code] not in alumniy_silindr:
                                alumniy_silindr.append([length[0],alum_teks.qora_алю_сплав_6064_sap_code])
                    
                    elif alum_teks.qora_алю_сплав_6064_sap_code == '0' :
                        isklyucheniye_ids.append(k)
                        norma.append([length[0],artikul_org,'','','','','','','','','Xato 0','Normada qora_алю_сплав_6064_sap_code 0 ga teng',['#12a4d9','#12a4d9','white','white','white','white','white']])
                    else:
                        if [length[0],alum_teks.qora_алю_сплав_6064_sap_code] not in alumniy_silindr:
                            isklyucheniye_ids.append(k)
                            alumniy_silindr.append([length[0],alum_teks.qora_алю_сплав_6064_sap_code])


                    
                if (('-S' in t) and (length[0] not in does_not_exist_norm)) :
                    if artikul_org!='':                
                        alum_teks_all = Norma.objects.filter(Q(компонент_1=length[0])|Q(компонент_2=length[0])|Q(компонент_3=length[0]))
                    else:
                        alum_teks_all = Norma.objects.filter(Q(компонент_1=length[0])|Q(компонент_2=length[0])|Q(компонент_3=length[0]))
                    alum_teks = alum_teks_all[:1].get()
                    
                    sublimatsiya_code = fullsapkod[i * 2+1].split('_')[1]
                    if sublimatsiya_code =='7777':
                        code_ss = alum_teks.суб_ширина_декор_пленки_мм_зол_дуб
                        mein =alum_teks.сублимация_расход_на_1000_профиль_м21
                    elif sublimatsiya_code =='8888':
                        code_ss = alum_teks.суб_ширина_декор_пленки_мм_дуб_мокко
                        mein =alum_teks.сублимация_расход_на_1000_профиль_м23
                    elif sublimatsiya_code =='3701':
                        code_ss = alum_teks.суб_ширина_декор_пленки_мм_3д_313701
                        mein =alum_teks.сублимация_расход_на_1000_профиль_м22
                    elif sublimatsiya_code =='3702':
                        code_ss = alum_teks.суб_ширина_декор_пленки_мм_3д_313702
                        mein =alum_teks.сублимация_расход_на_1000_профиль_м24
                    
                    mein_bor = True   
                    if mein =='0':
                        mein_bor = False
                    # skotголд_bor =True
                    # if alum_teks.молярный_скотч_рас_на_1000_пр_шт1 =='0':
                    #     skotголд_bor =False
                    
                        
                    if ((code_ss =='0') or (not mein_bor)):
                        if not mein_bor:
                           
                            if code_ss =='0':
                                norma.append([length[0],'','',sublimatsiya_code,'Xato 0 berilgan','Xato 0 berilgan','Xato 0 berilgan','','','','','Norma Sublimatsiya shirinasi 0 ga teng va boshqalar',['white','white','white','white','#d9138a','#d9138a','#d9138a']])
                            else:
                                norma.append([length[0],'','',sublimatsiya_code,'Xato 0 berilgan','Xato 0 berilgan','','','','','Norma Sublimatsiya xatolari',['white','white','white','white','#d9138a','#d9138a','white']])
                            
                        else:
                           
                            if code_ss =='0':
                                norma.append([length[0],'','',sublimatsiya_code,'','Xato 0 berilgan','','','','','Norma Sublimatsiya shirinasi 0 ga teng va boshqalar',['white','white','white','white','white','#d9138a','#d9138a']])
                            else:
                                norma.append([length[0],'','',sublimatsiya_code,'','Xato 0 berilgan','','','','','Norma Sublimatsiya xatolari',['white','white','white','white','white','#d9138a','white']])
                            
                        isklyucheniye_ids.append(k)
                    else:    
                        if not SubDekorPlonka.objects.filter(код_декор_пленки = sublimatsiya_code, ширина_декор_пленки_мм = code_ss).exists():
                            isklyucheniye_ids.append(k) 
                            if [sublimatsiya_code,code_ss,length[0]] not in subdekor:
                                subdekor.append([sublimatsiya_code,code_ss,length[0]])
                
                if ((('-N' in t) or ('-7' in t)) and (length[0] not in does_not_exist_norm)):
                    
                    if '_' in kratkiy_org:
                        ddd = kratkiy_org.split()[2]
                        
                    its_kombinirovanniy ='-K' in df[k][10]
                    
                    if its_kombinirovanniy:
                        print('k ga kiryapti')
                        norma_1 = Norma.objects.filter(артикул=length[0])[:1].get()
                        if ((norma_1.уп_пол_лн_рас_уп_лн_на_1000_штук_кг =='0' ) and (length[0] not in accessuar)):
                            isklyucheniye_ids.append(k)
                            norma.append([length[0],artikul_org,'','','','','','','','xato 0','','Normada Gp bez nakleyka',['#12a4d9','#12a4d9','white','white','white','white','white']])
                            
                        
                    if ('-N' in t):
                        if length[0] in nakleyka_iskyuch:
                            continue
                        if artikul_org != '':
                            try:
                                norma_1 = Norma.objects.filter(Q(компонент_1=length[0])|Q(компонент_2=length[0])|Q(компонент_3=length[0]))[:1].get()
                            except Norma.DoesNotExist:
                                norma.append([length[0],artikul_org,'','','','','','','','','','Normada Komponenta va artikul birgalikda kelmagan',['#12a4d9','#12a4d9','white','white','white','white','white']])
                                isklyucheniye_ids.append(k)
                                continue
                        else:
                            try:
                                norma_1 = Norma.objects.filter(Q(компонент_1=length[0])|Q(компонент_2=length[0])|Q(компонент_3=length[0]))[:1].get()
                            except Norma.DoesNotExist:
                                norma.append([length[0],artikul_org,'','','','','','','','','','Normada Komponenta va artikul birgalikda kelmagan',['#12a4d9','#12a4d9','white','white','white','white','white']])
                                isklyucheniye_ids.append(k)
                                continue
                                 
                    else:
                        if artikul_org != '':
                            print(artikul_org)    
                            norma_1 = Norma.objects.filter(Q(компонент_1=length[0])|Q(компонент_2=length[0])|Q(компонент_3=length[0])|Q(артикул=artikul_org))[:1].get()
                            if ((not '_' in kratkiy_org) or ('7777' in ddd.split('_')[1]) or ('8888' in ddd.split('_')[1]) or ('3701' in ddd.split('_')[1]) or ('3702' in ddd.split('_')[1])):
                                nakley_code = kratkiy_org.split()[-1]
                                if nakley_code !='NT1':
                                    if ((norma_1.уп_пол_лн_рас_уп_лн_на_1000_штук_кг =='0')and(length[0] not in accessuar)):
                                        isklyucheniye_ids.append(k)
                                        norma.append([length[0],artikul_org,'','','','','','','','xato 0','','Normada Gp bez nakleyka',['#12a4d9','#12a4d9','white','white','white','white','white']])
                            else:
                                
                                laminatsiya_code = ddd.split('_')[1].split('/')
                                laminatsiya_code1 = laminatsiya_code[0]
                                laminatsiya_code2 = laminatsiya_code[1]
                                qatorlar_soni = 0
                                lam_text =''
                                if ((laminatsiya_code1 == laminatsiya_code2) or (laminatsiya_code1 =='XXXX' or laminatsiya_code2 == 'XXXX')):
                                    qatorlar_soni = 1
                                    if laminatsiya_code1 =='XXXX':
                                        if norma_1.лам_низ_b_рас_ленты_на_1000_пр_м2 =='0':
                                            lam_text ='Лам низ 0'
                                    elif laminatsiya_code2 =='XXXX':
                                        if norma_1.лам_верх_a_рас_ленты_на_1000_пр_м2 =='0':
                                            lam_text ='Лам верх 0'
                                    elif laminatsiya_code1 == laminatsiya_code2:
                                        if (norma_1.лам_низ_b_рас_ленты_на_1000_пр_м2 =='0' and norma_1.лам_верх_a_рас_ленты_на_1000_пр_м2 =='0'):
                                            lam_text ='Лам низ-верх 0'
                                else:
                                    qatorlar_soni = 2
                                    if norma_1.лам_верх_a_рас_ленты_на_1000_пр_м2 =='0':
                                        lam_text ='Лам верх 0'
                                    if norma_1.лам_низ_b_рас_ленты_на_1000_пр_м2 =='0':
                                        if lam_text =='':
                                            lam_text +='Лам верх-низ 0'
                                        else:
                                            lam_text +=' низ'
                                    
                                
                                
                                if lam_text !='':
                                    isklyucheniye_ids.append(k)  
                                    norma.append([length[0],artikul_org,'','','','','',lam_text,'','','','Normada Laminatsiyada xatolar bor',['#12a4d9','#12a4d9','white','white','white','white','white']])
                                    
                                if ((norma_1.лам_рас_клея_на_1000_штук_пр_кг =='0') or (norma_1.лам_рас_праймера_на_1000_штук_пр_кг=='0') or (norma_1.лам_рас_уп_материала_мешок_на_1000_пр=='0')):
                                    isklyucheniye_ids.append(k)
                                    norma.append([length[0],artikul_org,'','','','','','','лам_рас 1000_штук da 0','','','Normada Laminatsiyada xatolar bor',['#12a4d9','#12a4d9','white','white','white','white','white']])
                            
                        else:
                            continue
                        
                    nakleyka_code = fullsapkod[i * 2+1].split()[-1]
                    
                    
                    
                    
                    ###############
                    if nakleyka_code =='A01':
                        aluminiy_norma_log = (norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм == norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм and norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм != '0') or ((norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм != norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)and((norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0')or(norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм=='0')))
                        if aluminiy_norma_log:
                            if norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'A01',ширина= norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,True,False] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,True,False])
                            elif norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'A01',ширина= norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,False,True] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,False,True])
                            else:
                                if not Nakleyka.objects.filter(код_наклейки = 'A01',ширина= norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,True,True] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,True,True])
                        elif ((norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0') and (norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм == '0')):
                            norma.append(['',length[0],'A01','','','','','','','','','Nakleykani qiymati 0',['white','white','#e75874','white','white','white','white']])
                            isklyucheniye_ids.append(k)
                        else:
                            if not Nakleyka.objects.filter(код_наклейки = 'A01',ширина= norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм).exists():
                                isklyucheniye_ids.append(k)
                                if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,True,False] not in nakleyka_N:
                                    nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,True,True])
                            if not Nakleyka.objects.filter(код_наклейки = 'A01',ширина= norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм).exists():
                                isklyucheniye_ids.append(k)
                                if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,True,True] not in nakleyka_N:
                                    nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,True,True])
                    
                    elif nakleyka_code =='R05':
                        aluminiy_norma_log = (norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм == norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм and norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм != '0') or ((norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм != norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)and((norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм =='0')or(norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм=='0')))
                        if aluminiy_norma_log:
                            if norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'R05',ширина= norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,True,False] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,True,False])
                            elif norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'R05',ширина= norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,False,True] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,False,True])
                            else:
                                if not Nakleyka.objects.filter(код_наклейки = 'R05',ширина= norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,True,True] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,True,True])
                        elif ((norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм =='0') and (norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм == '0')):
                            norma.append(['',length[0],'R05','','','','','','','','','Nakleykani qiymati 0',['white','white','#e75874','white','white','white','white']])
                            isklyucheniye_ids.append(k)
                        else:
                            if not Nakleyka.objects.filter(код_наклейки = 'R05',ширина= norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм).exists():
                                isklyucheniye_ids.append(k)
                                if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,True,False] not in nakleyka_N:
                                    nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,True,True])
                            if not Nakleyka.objects.filter(код_наклейки = 'R05',ширина= norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм).exists():
                                isklyucheniye_ids.append(k)
                                if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,False,True] not in nakleyka_N:
                                    nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,True,True])
                        
                    elif nakleyka_code =='B01':
                        aluminiy_norma_log = (norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм == norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм and norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм != '0') or ((norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм != norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)and((norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм =='0')or(norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            if norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'B01',ширина= norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,True,False] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,True,False])
                            elif norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'B01',ширина= norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,False,True] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,False,True])
                            else:
                                if not Nakleyka.objects.filter(код_наклейки = 'B01',ширина= norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,True,True] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,True,True])
                        elif ((norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм =='0') and (norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм == '0')):
                          
                            norma.append(['',length[0],'B01','','','','','','','','','Nakleykani qiymati 0',['white','white','#e75874','white','white','white','white']])
                            isklyucheniye_ids.append(k)
                        else:
                            if not Nakleyka.objects.filter(код_наклейки = 'B01',ширина= norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм).exists():
                                isklyucheniye_ids.append(k)
                                if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,True,False] not in nakleyka_N:
                                    nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,True,True])
                            if not Nakleyka.objects.filter(код_наклейки = 'B01',ширина= norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм).exists():
                                isklyucheniye_ids.append(k)
                                if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,False,True] not in nakleyka_N:
                                    nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,True,True])
                     
                    elif nakleyka_code =='G01':
                        aluminiy_norma_log = (norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм == norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм and norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм != '0') or ((norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм != norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм)and((norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм =='0')or(norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            if norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'G01',ширина= norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм,True,False] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм,True,False])
                            elif norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'G01',ширина= norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм,False,True] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм,False,True])
                            else:
                                if not Nakleyka.objects.filter(код_наклейки = 'G01',ширина= norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм,True,True] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм,True,True])
                        elif ((norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм =='0') and (norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм == '0')):
                            norma.append(['',length[0],'G01','','','','','','','','','Nakleykani qiymati 0',['white','white','#e75874','white','white','white','white']])
                            isklyucheniye_ids.append(k)
                        else:
                            if not Nakleyka.objects.filter(код_наклейки = 'G01',ширина= norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм).exists():
                                isklyucheniye_ids.append(k)
                                if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм,True,False] not in nakleyka_N:
                                    nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм,True,True])
                            if not Nakleyka.objects.filter(код_наклейки = 'G01',ширина= norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм).exists():
                                isklyucheniye_ids.append(k)
                                if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм,False,True] not in nakleyka_N:
                                    nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_голд_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_голд_вр_ширина_лн_мм,True,True])
                         
                    elif nakleyka_code =='I01':
                        aluminiy_norma_log = (norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм == norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм and norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм != '0') or ((norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм != norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)and((norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =='0')or(norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            if norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'I01',ширина= norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,True,False] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,True,False])
                            elif norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'I01',ширина= norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,False,True] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,False,True])
                            else:
                                if not Nakleyka.objects.filter(код_наклейки = 'I01',ширина= norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,True,True] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,True,True])
                        elif ((norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =='0') and (norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм == '0')):
                            norma.append(['',length[0],'I01','','','','','','','','','Nakleykani qiymati 0',['white','white','#e75874','white','white','white','white']])
                            isklyucheniye_ids.append(k)
                        else:
                            if not Nakleyka.objects.filter(код_наклейки = 'I01',ширина= norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм).exists():
                                isklyucheniye_ids.append(k)
                                if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,True,False] not in nakleyka_N:
                                    nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,True,True])
                            if not Nakleyka.objects.filter(код_наклейки = 'I01',ширина= norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм).exists():
                                isklyucheniye_ids.append(k)
                                if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,False,True] not in nakleyka_N:
                                    nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,True,True])
                                     
                    elif nakleyka_code =='NB1':
                        aluminiy_norma_log = (norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм == norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм and norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм != '0') or ((norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм != norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)and((norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм =='0')or(norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            if norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,True,False] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,True,False])
                            elif norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,False,True] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,False,True])
                            else:
                                if not Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,True,True] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,True,True])
                        elif ((norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм =='0') and (norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм == '0')):
                            norma.append(['',length[0],'NB1','','','','','','','','','Nakleykani qiymati 0',['white','white','#e75874','white','white','white','white']])
                            isklyucheniye_ids.append(k)
                        else:
                            if not Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм).exists():
                                isklyucheniye_ids.append(k)
                                if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,True,False] not in nakleyka_N:
                                    nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,True,True])
                            if not Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм).exists():
                                isklyucheniye_ids.append(k)
                                if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,False,True] not in nakleyka_N:
                                    nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,True,True])
                    
                    elif nakleyka_code =='E01':
                        
                        aluminiy_norma_log = (norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм == norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм and norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм != '0') or ((norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм != norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм)and((norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм =='0')or(norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм=='0')))
                        if aluminiy_norma_log:
                            if norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'E01',ширина= norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,True,False] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,True,False])
                            elif norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'E01',ширина= norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,False,True] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,False,True])
                            else:
                                if not Nakleyka.objects.filter(код_наклейки = 'E01',ширина= norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,True,True] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,True,True])
                        elif ((norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм =='0') and (norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм == '0')):
                            norma.append(['',length[0],'E01','','','','','','','','','Nakleykani qiymati 0',['white','white','#e75874','white','white','white','white']])
                            isklyucheniye_ids.append(k)
                        else:
                            if not Nakleyka.objects.filter(код_наклейки = 'E01',ширина= norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм).exists():
                                isklyucheniye_ids.append(k)
                                if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,True,False] not in nakleyka_N:
                                    nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,True,True])
                            if not Nakleyka.objects.filter(код_наклейки = 'E01',ширина= norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм).exists():
                                isklyucheniye_ids.append(k)
                                if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,False,True] not in nakleyka_N:
                                    nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,True,True])
                          
                    elif nakleyka_code =='E02': 
                        
                        aluminiy_norma_log = (norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм == norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты and norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты != '0') or ((norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм != norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты)and((norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =='0')or(norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты=='0')))
                        if aluminiy_norma_log:
                            
                            if norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'E02',ширина= norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,True,False] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,True,False])
                            elif norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'E02',ширина= norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,False,True] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,False,True])
                            else:
                                if not Nakleyka.objects.filter(код_наклейки = 'E02',ширина= norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,True,True] not in nakleyka_N:
                                        nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,True,True])
                            
                        elif ((norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =='0') and (norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты == '0')):
                            norma.append(['',length[0],'E02','','','','','','','','','Nakleykani qiymati 0',['white','white','#e75874','white','white','white','white']])
                            isklyucheniye_ids.append(k)
                        else:
                            if not Nakleyka.objects.filter(код_наклейки = 'E02',ширина= norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм).exists():
                                isklyucheniye_ids.append(k)
                                if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,True,True] not in nakleyka_N:
                                    nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,True,False])
                            if not Nakleyka.objects.filter(код_наклейки = 'E02',ширина= norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты).exists():
                                isklyucheniye_ids.append(k)
                                if [length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,False,True] not in nakleyka_N:
                                    nakleyka_N.append([length[0],nakleyka_code,norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,True,True])
                
                if (('-K' in t) and (length[0] not in does_not_exist_norm)):
                    
                    if not Norma.objects.filter(Q(артикул=length[0])&~Q(термомост_1='0')).exists():
                        isklyucheniye_ids.append(k)
                        if length[0] not in kombinirovanniy:
                            kombinirovanniy.append(length[0])
                            
                if ((i*2+1) == 13  and (length[0] not in does_not_exist_norm)):

                    
                    if '_' in fullsapkod[13]:
                        ddd = fullsapkod[13].split()[2]
   
                        if ((not '_' in fullsapkod[13]) or ('7777' in ddd.split('_')[1]) or ('8888' in ddd.split('_')[1]) or ('3701' in ddd.split('_')[1]) or ('3702' in ddd.split('_')[1])):
                            continue
                        else:
                            alum_teks = Norma.objects.filter(артикул = artikul_org)[:1].get()
                            laminatsiya_code = ddd.split('_')[1].split('/')
                            laminatsiya_code1 = laminatsiya_code[0]
                            laminatsiya_code2 = laminatsiya_code[1]
                            if ((laminatsiya_code1 == laminatsiya_code2) or (laminatsiya_code1 =='XXXX' or laminatsiya_code2 == 'XXXX')):
                                if laminatsiya_code1 =='XXXX':
                                    if not Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code2).exists():
                                        isklyucheniye_ids.append(k)
                                        lamplyonka.append([length[0],laminatsiya_code2])
                                elif laminatsiya_code2 =='XXXX':
                                    if not Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code1).exists():
                                        isklyucheniye_ids.append(k)
                                        lamplyonka.append([length[0],laminatsiya_code1])
                                elif laminatsiya_code1 == laminatsiya_code2:
                                    if not Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code1).exists():
                                        isklyucheniye_ids.append(k)
                                        lamplyonka.append([length[0],laminatsiya_code1])
                                    
                            else:
                                if not Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code1).exists():
                                    isklyucheniye_ids.append(k)
                                    lamplyonka.append([length[0],laminatsiya_code1])
                                if not Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code2).exists():
                                    isklyucheniye_ids.append(k)
                                    lamplyonka.append([length[0],laminatsiya_code2])
                    else:
                        norma_1 = Norma.objects.filter(Q(компонент_1=length[0])|Q(компонент_2=length[0])|Q(компонент_3=length[0])|Q(артикул=length[0]))[:1].get()
                        nakley_code = fullsapkod[13].split()[-1]
                        if nakley_code !='NT1':
                            if ((norma_1.уп_пол_лн_рас_уп_лн_на_1000_штук_кг =='0')and(length[0] not in accessuar)):
                                isklyucheniye_ids.append(k)
                                norma.append([length[0],length[0],'','','','','','','','xato 0','','Normada Gp bez nakleyka',['#12a4d9','#12a4d9','white','white','white','white','white']])
                        
                                    
                                 
    existing = norma + alumniy_silindr + subdekor + kraska + nakleyka_N + kombinirovanniy + lamplyonka
    
    if len(existing) > 0 : 
        path = create_csv_file(norma,alumniy_silindr,subdekor,kraska,nakleyka_N,kombinirovanniy,lamplyonka,str(product_type))
        files =[File(file=path,filetype='norma')]     
        context ={
            'files':files,
            'section':'Ошибки нормы'

        }
        order_id = request.GET.get('order_id',None)

        if order_id:
            context2 ={}
            order = Order.objects.get(id = order_id)
            paths = order.paths 
            norma_l_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            paths['status_norma_lack']= 'on process'
            paths['norma_file_lack'] = path
            paths['norma_l_created_at'] = norma_l_created_at
            order.norma_wrongs = request.user
            order.current_worker =request.user
            order.work_type = 7
            order.save()
            context2['order'] = order
            paths =  order.paths
            for key,val in paths.items():
                context2[key] = val
            return render(request,'order/order_detail.html',context2)
        
        return render(request,'universal/generated_files.html',context)
    
    df_new ={
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
    
    df_new_duplicate ={
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
    
    siryo_dlya_upakovki1 = SiryoDlyaUpakovki.objects.get(id=1)
    
    kleydlyalamp1 =KleyDlyaLamp.objects.get(id=1)
    kleydlyalamp2 =KleyDlyaLamp.objects.get(id=2)
    kleydlyalamp3 =KleyDlyaLamp.objects.get(id=3)

    zakalka_iskyucheniye1 = Norma.objects.filter(закалка_исключение ='1').values_list('артикул',flat=True)
    zakalka_iskyucheniye2 = Norma.objects.filter(закалка_исключение ='1').values_list('компонент_1',flat=True)
    zakalka_iskyucheniye7 =list(zakalka_iskyucheniye1) + list(zakalka_iskyucheniye2)

    for i in range(0,len(df)):
        if i in isklyucheniye_ids:
            continue
        older_process ={'sapcode':'','kratkiy':''}
        norma_existsE = CheckNormaBase.objects.filter(artikul=df[i][0],kratkiytekst=df[i][1]).exists()
        
        
        if not norma_existsE:
            if df[i][0] !="":
                CheckNormaBase(artikul=df[i][0],kratkiytekst=df[i][1]).save()
                older_process['sapcode'] =df[i][0]
                older_process['kratkiy'] =df[i][1]
                if df[i][0].split('-')[1][:1]=='E':
                    df_new['ID'].append('1')
                    df_new['MATNR'].append(df[i][0])
                    df_new['WERKS'].append('1101')
                    df_new['TEXT1'].append(df[i][1])
                    df_new['STLAL'].append('1')
                    df_new['STLAN'].append('1')
                    if df[i][0].split('-')[1][:1]=='E':
                        ztekst ='Экструзия (пресс) + Пила'
                    df_new['ZTEXT'].append(ztekst)
                    length = df[i][0].split('-')[0]
                    alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length))[:1].get()
                    
                   
                    aliminisi = AlyuminniysilindrEkstruziya1.objects.filter(sap_code_s4q100 =alum_teks.qora_алю_сплав_6064_sap_code)[:1].get()
                   
                    
                    mein_percent =((get_legth(df[i][1]))/float(alum_teks.длина_профиля_м))
                    df_new['STKTX'].append(aliminisi.название)
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
                            
                            df_new['MATNR1'].append(aliminisi.sap_code_s4q100)
                            df_new['TEXT2'].append(aliminisi.название)
                            
                            df_new['MEINS'].append(("%.3f" % (float(alum_teks.алю_сп_6063_рас_спа_на_1000_шт_пр_кг)*mein_percent)).replace('.',',')) 
                            df_new['MENGE'].append('КГ')
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        
                        
                        if k == 2:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=4)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            
                            df_new['MEINS'].append(("%.3f" % ((-1)*float(alum_teks.алюминиевый_сплав_6063_при_этом_балвашка)*mein_percent)).replace('.',',')) ##XATO
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k == 3:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=5)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            
                            df_new['MEINS'].append( ("%.3f" % (((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода1)))*mein_percent) ).replace('.',',')) ##XATO
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k == 4:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=6)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            
                            df_new['MEINS'].append(("%.3f" % (((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода2)))*mein_percent) ).replace('.',',')) ##XATO
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                            
                        df_new['LGORT'].append('PS01')
        
        else:
            normaexist = CheckNormaBase.objects.filter(artikul=df[i][0],kratkiytekst=df[i][1])[:1].get()
            if df[i][0] !="":
                older_process['sapcode'] =df[i][0]
                older_process['kratkiy'] =df[i][1]
                if df[i][0].split('-')[1][:1]=='E':
                    df_new_duplicate['ID'].append('1')
                    df_new_duplicate['MATNR'].append(df[i][0])
                    df_new_duplicate['WERKS'].append('1101')
                    df_new_duplicate['TEXT1'].append(df[i][1])
                    df_new_duplicate['STLAL'].append('1')
                    df_new_duplicate['STLAN'].append('1')
                    if df[i][0].split('-')[1][:1]=='E':
                        ztekst ='Экструзия (пресс) + Пила'
                    df_new_duplicate['ZTEXT'].append(ztekst)
                    length = df[i][0].split('-')[0]
                    alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length))[:1].get()
                    
                    
                    aliminisi = AlyuminniysilindrEkstruziya1.objects.filter(sap_code_s4q100 =alum_teks.qora_алю_сплав_6064_sap_code)[:1].get()
                    
                    mein_percent =((get_legth(df[i][1]))/float(alum_teks.длина_профиля_м))
                    df_new_duplicate['STKTX'].append(aliminisi.название)
                    df_new_duplicate['BMENG'].append( '1000')
                    df_new_duplicate['BMEIN'].append('ШТ')
                    df_new_duplicate['STLST'].append('1')
                    df_new_duplicate['POSNR'].append('')
                    df_new_duplicate['POSTP'].append('')
                    df_new_duplicate['MATNR1'].append('')
                    df_new_duplicate['TEXT2'].append('')
                    df_new_duplicate['MEINS'].append('')
                    df_new_duplicate['MENGE'].append('')
                    df_new_duplicate['DATUV'].append('01012021')
                    df_new_duplicate['PUSTOY'].append('')
                    df_new_duplicate['LGORT'].append('')
                    for k in range(1,5):
                        j+=1
                        df_new_duplicate['ID'].append('2')
                        df_new_duplicate['MATNR'].append('')
                        df_new_duplicate['WERKS'].append('')
                        df_new_duplicate['TEXT1'].append('')
                        df_new_duplicate['STLAL'].append('')
                        df_new_duplicate['STLAN'].append('')
                        df_new_duplicate['ZTEXT'].append('')
                        df_new_duplicate['STKTX'].append('')
                        df_new_duplicate['BMENG'].append('')
                        df_new_duplicate['BMEIN'].append('')
                        df_new_duplicate['STLST'].append('')
                        df_new_duplicate['POSNR'].append(k)
                        df_new_duplicate['POSTP'].append('L')
                        
                        
                        if k == 1 :
                            
                            df_new_duplicate['MATNR1'].append(aliminisi.sap_code_s4q100)
                            df_new_duplicate['TEXT2'].append(aliminisi.название)
                            
                            df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.алю_сп_6063_рас_спа_на_1000_шт_пр_кг)*mein_percent)).replace('.',',')) 
                            df_new_duplicate['MENGE'].append('КГ')
                            df_new_duplicate['DATUV'].append('')
                            df_new_duplicate['PUSTOY'].append('')
                        
                        if k == 2:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=4)
                            df_new_duplicate['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new_duplicate['TEXT2'].append(alummm.название)
                            df_new_duplicate['MENGE'].append(alummm.еи)
                            
                            df_new_duplicate['MEINS'].append(("%.3f" % ((-1)*float(alum_teks.алюминиевый_сплав_6063_при_этом_балвашка)*mein_percent)).replace('.',',')) ##XATO
                            df_new_duplicate['DATUV'].append('')
                            df_new_duplicate['PUSTOY'].append('')
                        if k == 3:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=5)
                            df_new_duplicate['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new_duplicate['TEXT2'].append(alummm.название)
                            df_new_duplicate['MENGE'].append(alummm.еи)
                            
                            df_new_duplicate['MEINS'].append( ("%.3f" % (((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода1)))*mein_percent) ).replace('.',',')) ##XATO
                            df_new_duplicate['DATUV'].append('')
                            df_new_duplicate['PUSTOY'].append('')
                        if k == 4:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=6)
                            df_new_duplicate['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new_duplicate['TEXT2'].append(alummm.название)
                            df_new_duplicate['MENGE'].append(alummm.еи)
                            
                            df_new_duplicate['MEINS'].append(("%.3f" % (((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода2)))*mein_percent) ).replace('.',',')) ##XATO
                            df_new_duplicate['DATUV'].append('')
                            df_new_duplicate['PUSTOY'].append('')
                            
                        df_new_duplicate['LGORT'].append('PS01')
        
            
            older_process['sapcode'] =normaexist.artikul
            older_process['kratkiy'] =normaexist.kratkiytekst
                    
        norma_z =[]
        norma_existsZ = CheckNormaBase.objects.filter(artikul=df[i][2],kratkiytekst=df[i][3]).exists()
        
        if not norma_existsZ:
            if df[i][2] !="":
                lenghtht = df[i][2].split('-')[0]
                if lenghtht not in zakalka_iskyucheniye7:
                        
                    CheckNormaBase(artikul=df[i][2],kratkiytekst=df[i][3]).save()

                    sap_code_zak = df[i][2].split('-')[0]
                    older_process['sapcode'] =df[i][2]
                    older_process['kratkiy'] =df[i][3] 

                    
                    j+=1
                    if (df[i][2].split('-')[1][:1]=='Z'):
                        df_new['ID'].append('1')
                        df_new['MATNR'].append(df[i][2])
                        df_new['WERKS'].append('1101')
                        df_new['TEXT1'].append(df[i][3])
                        df_new['STLAL'].append('1')
                        df_new['STLAN'].append('1')
                        if df[i][2].split('-')[1][:1]=='Z':
                            ztekst ='Экструзия (пресс) + Пила + Старение'
                        df_new['ZTEXT'].append(ztekst)
                        length = df[i][2].split('-')[0]
                        
                        alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                        
                        
                        aliminisi =AlyuminniysilindrEkstruziya1.objects.filter(sap_code_s4q100 =alum_teks.qora_алю_сплав_6064_sap_code)[:1].get()
                        
                        
                        mein_percent =((get_legth(df[i][3]))/float(alum_teks.длина_профиля_м))
                        df_new['STKTX'].append(aliminisi.название)
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
                                df_new['MATNR1'].append(aliminisi.sap_code_s4q100)
                                df_new['TEXT2'].append(aliminisi.название)
                                df_new['MEINS'].append(("%.3f" % (float(alum_teks.алю_сп_6063_рас_спа_на_1000_шт_пр_кг)*mein_percent)).replace('.',',')) ##XATO
                                df_new['MENGE'].append('КГ')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            
                            
                            if k == 2:
                                alummm = AlyuminniysilindrEkstruziya2.objects.get(id=4)
                                df_new['MATNR1'].append(alummm.sap_code_s4q100)
                                df_new['TEXT2'].append(alummm.название)
                                df_new['MENGE'].append(alummm.еи)
                                df_new['MEINS'].append(("%.3f" % ((-1)*float(alum_teks.алюминиевый_сплав_6063_при_этом_балвашка)*mein_percent)).replace('.',',')) ##XATO
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            if k == 3:
                                alummm = AlyuminniysilindrEkstruziya2.objects.get(id=5)
                                df_new['MATNR1'].append(alummm.sap_code_s4q100)
                                df_new['TEXT2'].append(alummm.название)
                                df_new['MENGE'].append(alummm.еи)
                                df_new['MEINS'].append(("%.3f" % (((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода1)))*mein_percent) ).replace('.',',')) ##XATO
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            if k == 4:
                                alummm = AlyuminniysilindrEkstruziya2.objects.get(id=6)
                                df_new['MATNR1'].append(alummm.sap_code_s4q100)
                                df_new['TEXT2'].append(alummm.название)
                                df_new['MENGE'].append(alummm.еи)
                                df_new['MEINS'].append(("%.3f" % (((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода2)))*mein_percent) ).replace('.',',')) ##XATO
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                                
                            df_new['LGORT'].append('PS01')
       
        else:
            normaexist = CheckNormaBase.objects.filter(artikul=df[i][2],kratkiytekst=df[i][3])[:1].get()
            if df[i][2] !="":
                older_process['sapcode'] =df[i][2]
                older_process['kratkiy'] =df[i][3]  
                j+=1
                if (df[i][2].split('-')[1][:1]=='Z'):
                    df_new_duplicate['ID'].append('1')
                    df_new_duplicate['MATNR'].append(df[i][2])
                    df_new_duplicate['WERKS'].append('1101')
                    df_new_duplicate['TEXT1'].append(df[i][3])
                    df_new_duplicate['STLAL'].append('1')
                    df_new_duplicate['STLAN'].append('1')
                    if df[i][2].split('-')[1][:1]=='Z':
                        ztekst ='Экструзия (пресс) + Пила + Старение'
                    df_new_duplicate['ZTEXT'].append(ztekst)
                    length = df[i][2].split('-')[0]
                    
                    alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                    
                   
                    aliminisi =AlyuminniysilindrEkstruziya1.objects.filter(sap_code_s4q100 =alum_teks.qora_алю_сплав_6064_sap_code)[:1].get()
                    
                    
                    mein_percent =((get_legth(df[i][3]))/float(alum_teks.длина_профиля_м))
                    df_new_duplicate['STKTX'].append(aliminisi.название)
                    df_new_duplicate['BMENG'].append( '1000')
                    df_new_duplicate['BMEIN'].append('ШТ')
                    df_new_duplicate['STLST'].append('1')
                    df_new_duplicate['POSNR'].append('')
                    df_new_duplicate['POSTP'].append('')
                    df_new_duplicate['MATNR1'].append('')
                    df_new_duplicate['TEXT2'].append('')
                    df_new_duplicate['MEINS'].append('')
                    df_new_duplicate['MENGE'].append('')
                    df_new_duplicate['DATUV'].append('01012021')
                    df_new_duplicate['PUSTOY'].append('')
                    df_new_duplicate['LGORT'].append('')
                    
                    for k in range(1,5):
                        j+=1
                        df_new_duplicate['ID'].append('2')
                        df_new_duplicate['MATNR'].append('')
                        df_new_duplicate['WERKS'].append('')
                        df_new_duplicate['TEXT1'].append('')
                        df_new_duplicate['STLAL'].append('')
                        df_new_duplicate['STLAN'].append('')
                        df_new_duplicate['ZTEXT'].append('')
                        df_new_duplicate['STKTX'].append('')
                        df_new_duplicate['BMENG'].append('')
                        df_new_duplicate['BMEIN'].append('')
                        df_new_duplicate['STLST'].append('')
                        df_new_duplicate['POSNR'].append(k)
                        df_new_duplicate['POSTP'].append('L')
                        
                        
                        if k == 1 :
                            df_new_duplicate['MATNR1'].append(aliminisi.sap_code_s4q100)
                            df_new_duplicate['TEXT2'].append(aliminisi.название)
                            df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.алю_сп_6063_рас_спа_на_1000_шт_пр_кг)*mein_percent)).replace('.',',')) ##XATO
                            df_new_duplicate['MENGE'].append('КГ')
                            df_new_duplicate['DATUV'].append('')
                            df_new_duplicate['PUSTOY'].append('')
                        
                       
                        if k == 2:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=4)
                            df_new_duplicate['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new_duplicate['TEXT2'].append(alummm.название)
                            df_new_duplicate['MENGE'].append(alummm.еи)
                            df_new_duplicate['MEINS'].append(("%.3f" % ((-1)*float(alum_teks.алюминиевый_сплав_6063_при_этом_балвашка)*mein_percent)).replace('.',',')) ##XATO
                            df_new_duplicate['DATUV'].append('')
                            df_new_duplicate['PUSTOY'].append('')
                        if k == 3:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=5)
                            df_new_duplicate['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new_duplicate['TEXT2'].append(alummm.название)
                            df_new_duplicate['MENGE'].append(alummm.еи)
                            df_new_duplicate['MEINS'].append(("%.3f" % (((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода1)))*mein_percent) ).replace('.',',')) ##XATO
                            df_new_duplicate['DATUV'].append('')
                            df_new_duplicate['PUSTOY'].append('')
                        if k == 4:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=6)
                            df_new_duplicate['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new_duplicate['TEXT2'].append(alummm.название)
                            df_new_duplicate['MENGE'].append(alummm.еи)
                            df_new_duplicate['MEINS'].append(("%.3f" % (((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода2)))*mein_percent) ).replace('.',',')) ##XATO
                            df_new_duplicate['DATUV'].append('')
                            df_new_duplicate['PUSTOY'].append('')
                            
                        df_new_duplicate['LGORT'].append('PS01')                
        
            
            older_process['sapcode'] =normaexist.artikul
            older_process['kratkiy'] =normaexist.kratkiytekst            
        
        sklad ={
            'sklad_pokraski':['SKM - SKM покраска','SAT - SAT покраска','ГР - ГР покраска','SKM - Ручная покраска','SAT - Ручная покраска','ГР - Ручная покраска'],
            'number_sklad':[
                ['PS04','PS04','PS04','PS04','PS04','PS04'],
                ['PS05','PS05','PS05','PS05','PS05','PS05'],
                ['PS06','PS06','PS06','PS06','PS06','PS06'],
                ['PS07','PS07','PS07','PS04','PS04','PS04'],
                ['PS07','PS07','PS07','PS05','PS05','PS05'],
                ['PS07','PS07','PS07','PS06','PS06','PS06']
                ]
        }
        
        norma_existsP = CheckNormaBase.objects.filter(artikul=df[i][4],kratkiytekst=df[i][5]).exists()
        if not norma_existsP:
            if df[i][4] !="":
                CheckNormaBase(artikul=df[i][4],kratkiytekst=df[i][5]).save()
                if (df[i][4].split('-')[1][:1]=='P'):
                    if (('8001' in df[i][5]) or ('7042' in df[i][5])or ('8024' in df[i][5])or ('8003' in df[i][5])):

                        for p in range(0,6):    
                            j+=1
                            
                            if (df[i][4].split('-')[1][:1]=='P'):
                                df_new['ID'].append('1')
                                df_new['MATNR'].append(df[i][4])
                                df_new['WERKS'].append('1101')
                                df_new['TEXT1'].append(df[i][5])
                                df_new['STLAL'].append(f'{p+1}')
                                df_new['STLAN'].append('1')
                                ztekst = sklad['sklad_pokraski'][p]
                                df_new['ZTEXT'].append('Покраска')
                                df_new['STKTX'].append(ztekst)
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
                                length = df[i][4].split('-')[0]
                                if product_type =='termo':
                                    alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length))[:1].get()
                                else:
                                    alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                                
                                
                                mein_percent =((get_legth(df[i][5]))/float(alum_teks.длина_профиля_м))
                                
                                for k in range(0,6):
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
                                    df_new['POSNR'].append(k+1)
                                    df_new['POSTP'].append('L')
                                    
                                    
                                    if k == 0 :
                                        
                                        df_new['MATNR1'].append(older_process['sapcode'])
                                        df_new['TEXT2'].append(older_process['kratkiy'])
                                        df_new['MEINS'].append('1000')
                                        df_new['MENGE'].append('ШТ')
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==1:
                                        kraska_code1 = df[i][5].split()[-1]
                                        kraska_code = kraska_code1.replace('A','R')
                                                                        
                                        kraska =Kraska.objects.filter(код_краски_в_профилях = kraska_code)[:1].get()
                                        df_new['MATNR1'].append(kraska.sap_code_s4q100)
                                        df_new['TEXT2'].append(kraska.название)
                                        df_new['MENGE'].append('КГ')
                                        df_new['MEINS'].append( ("%.3f" % (float(alum_teks.порошковый_краситель_рас_кг_на_1000_пр)*mein_percent)).replace('.',','))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    if k == 2:
                                        himikat_kraska = Ximikat.objects.get(id=4)
                                        df_new['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                        df_new['TEXT2'].append(himikat_kraska.название)
                                        df_new['MENGE'].append("КГ")
                                        df_new['MEINS'].append(("%.3f" % ((-1)*float(alum_teks.пр_краситель_при_этом_тех_отхода)*mein_percent) ).replace('.',',')) ##XATO
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==3:
                                        himikat_kraska = Ximikat.objects.get(id=1)
                                        df_new['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                        df_new['TEXT2'].append(himikat_kraska.название)
                                        df_new['MENGE'].append("КГ")
                                        df_new['MEINS'].append(("%.3f" % (float(alum_teks.хим_пг_к_окр_politeknik_кг_alupol_сr_51)*mein_percent)).replace('.',',')) ##XATO
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    if k == 4:
                                        himikat_kraska = Ximikat.objects.get(id=2)
                                        df_new['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                        df_new['TEXT2'].append(himikat_kraska.название)
                                        df_new['MENGE'].append("КГ")
                                        df_new['MEINS'].append(("%.3f" % (float(alum_teks.хим_пг_к_окр_politeknik_кг_alupol_ac_52)*mein_percent)).replace('.',',')) ##XATO
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    if k == 5:
                                        himikat_kraska = Ximikat.objects.get(id=3)
                                        df_new['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                        df_new['TEXT2'].append(himikat_kraska.название)
                                        df_new['MENGE'].append("КГ")
                                        df_new['MEINS'].append(("%.3f" % (float(alum_teks.хим_пг_к_окр_politeknik_кг_pol_ac_25p)*mein_percent)).replace('.',',')) ##XATO
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                        
                                    df_new['LGORT'].append(sklad['number_sklad'][p][k])
                            
                                # df_new['STKTX'][j-6+i]=(df_new['TEXT2'][j-4+i])
                    
                    else:
                        kraska_code = df[i][5].split()[-1][1:]
                        kraskas =Kraska.objects.filter(код_краски = kraska_code).order_by('order')
                        kraska_counter =0
                        for kras in kraskas:
                            for p in range(0,6):    
                                j+=1
                                kraska_counter +=1
                                if (df[i][4].split('-')[1][:1]=='P'):
                                    df_new['ID'].append('1')
                                    df_new['MATNR'].append(df[i][4])
                                    df_new['WERKS'].append('1101')
                                    df_new['TEXT1'].append(df[i][5])
                                    df_new['STLAL'].append(f'{kraska_counter}')
                                    df_new['STLAN'].append('1')
                                    ztekst = sklad['sklad_pokraski'][p]
                                    df_new['ZTEXT'].append('Покраска')
                                    df_new['STKTX'].append(ztekst)
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
                                    length = df[i][4].split('-')[0]
                                    if product_type =='termo':
                                        alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length))[:1].get()
                                    else:
                                        alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                                    
                                    
                                    mein_percent =((get_legth(df[i][5]))/float(alum_teks.длина_профиля_м))
                                    
                                    for k in range(0,6):
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
                                        df_new['POSNR'].append(k+1)
                                        df_new['POSTP'].append('L')
                                        
                                        
                                        if k == 0 :
                                            df_new['MATNR1'].append(older_process['sapcode'])
                                            df_new['TEXT2'].append(older_process['kratkiy'])
                                            df_new['MEINS'].append('1000')
                                            df_new['MENGE'].append('ШТ')
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        if k==1:
                                            
                                            df_new['MATNR1'].append(kras.sap_code_s4q100)
                                            df_new['TEXT2'].append(kras.название)
                                            df_new['MENGE'].append('КГ')
                                            df_new['MEINS'].append( ("%.3f" % (float(alum_teks.порошковый_краситель_рас_кг_на_1000_пр)*mein_percent)).replace('.',','))
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        if k == 2:
                                            himikat_kraska = Ximikat.objects.get(id=4)
                                            df_new['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                            df_new['TEXT2'].append(himikat_kraska.название)
                                            df_new['MENGE'].append("КГ")
                                            df_new['MEINS'].append(("%.3f" % ((-1)*float(alum_teks.пр_краситель_при_этом_тех_отхода)*mein_percent) ).replace('.',',')) ##XATO
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        if k==3:
                                            himikat_kraska = Ximikat.objects.get(id=1)
                                            df_new['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                            df_new['TEXT2'].append(himikat_kraska.название)
                                            df_new['MENGE'].append("КГ")
                                            df_new['MEINS'].append(("%.3f" % (float(alum_teks.хим_пг_к_окр_politeknik_кг_alupol_сr_51)*mein_percent)).replace('.',',')) ##XATO
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        if k == 4:
                                            himikat_kraska = Ximikat.objects.get(id=2)
                                            df_new['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                            df_new['TEXT2'].append(himikat_kraska.название)
                                            df_new['MENGE'].append("КГ")
                                            df_new['MEINS'].append(("%.3f" % (float(alum_teks.хим_пг_к_окр_politeknik_кг_alupol_ac_52)*mein_percent)).replace('.',',')) ##XATO
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        if k == 5:
                                            himikat_kraska = Ximikat.objects.get(id=3)
                                            df_new['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                            df_new['TEXT2'].append(himikat_kraska.название)
                                            df_new['MENGE'].append("КГ")
                                            df_new['MEINS'].append(("%.3f" % (float(alum_teks.хим_пг_к_окр_politeknik_кг_pol_ac_25p)*mein_percent)).replace('.',',')) ##XATO
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                            
                                        df_new['LGORT'].append(sklad['number_sklad'][p][k])
                                
                                    # df_new['STKTX'][j-6+i]=(df_new['TEXT2'][j-4+i])
                        
                                    
                older_process['sapcode'] =df[i][4]
                older_process['kratkiy'] =df[i][5]
        
        else:
            normaexist = CheckNormaBase.objects.filter(artikul=df[i][4],kratkiytekst=df[i][5])[:1].get()
            if df[i][4] !="":
                if (df[i][4].split('-')[1][:1]=='P'):
                    if (('8001' in df[i][5]) or ('7042' in df[i][5])or ('8024' in df[i][5])or ('8003' in df[i][5])):

                        for p in range(0,6):    
                            j+=1
                            
                            if (df[i][4].split('-')[1][:1]=='P'):
                                df_new_duplicate['ID'].append('1')
                                df_new_duplicate['MATNR'].append(df[i][4])
                                df_new_duplicate['WERKS'].append('1101')
                                df_new_duplicate['TEXT1'].append(df[i][5])
                                df_new_duplicate['STLAL'].append(f'{p+1}')
                                df_new_duplicate['STLAN'].append('1')
                                ztekst = sklad['sklad_pokraski'][p]
                                df_new_duplicate['ZTEXT'].append('Покраска')
                                df_new_duplicate['STKTX'].append(ztekst)
                                df_new_duplicate['BMENG'].append( '1000')
                                df_new_duplicate['BMEIN'].append('ШТ')
                                df_new_duplicate['STLST'].append('1')
                                df_new_duplicate['POSNR'].append('')
                                df_new_duplicate['POSTP'].append('')
                                df_new_duplicate['MATNR1'].append('')
                                df_new_duplicate['TEXT2'].append('')
                                df_new_duplicate['MEINS'].append('')
                                df_new_duplicate['MENGE'].append('')
                                df_new_duplicate['DATUV'].append('01012021')
                                df_new_duplicate['PUSTOY'].append('')
                                df_new_duplicate['LGORT'].append('')
                                length = df[i][4].split('-')[0]
                                if product_type =='termo':
                                    alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length))[:1].get()
                                else:
                                    alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length))[:1].get()
                                
                                
                                mein_percent =((get_legth(df[i][5]))/float(alum_teks.длина_профиля_м))
                                
                                for k in range(0,6):
                                    j+=1
                                    df_new_duplicate['ID'].append('2')
                                    df_new_duplicate['MATNR'].append('')
                                    df_new_duplicate['WERKS'].append('')
                                    df_new_duplicate['TEXT1'].append('')
                                    df_new_duplicate['STLAL'].append('')
                                    df_new_duplicate['STLAN'].append('')
                                    df_new_duplicate['ZTEXT'].append('')
                                    df_new_duplicate['STKTX'].append('')
                                    df_new_duplicate['BMENG'].append('')
                                    df_new_duplicate['BMEIN'].append('')
                                    df_new_duplicate['STLST'].append('')
                                    df_new_duplicate['POSNR'].append(k+1)
                                    df_new_duplicate['POSTP'].append('L')
                                    
                                    
                                    if k == 0 :
                                        
                                        df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                        df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                        df_new_duplicate['MEINS'].append('1000')
                                        df_new_duplicate['MENGE'].append('ШТ')
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    
                                    if k==1:
                                        kraska_code1 = df[i][5].split()[-1]
                                        kraska_code = kraska_code1.replace('A','R')
                                                                        
                                        kraska =Kraska.objects.filter(код_краски_в_профилях = kraska_code)[:1].get()
                                        df_new_duplicate['MATNR1'].append(kraska.sap_code_s4q100)
                                        df_new_duplicate['TEXT2'].append(kraska.название)
                                        df_new_duplicate['MENGE'].append('КГ')
                                        df_new_duplicate['MEINS'].append( ("%.3f" % (float(alum_teks.порошковый_краситель_рас_кг_на_1000_пр)*mein_percent)).replace('.',','))
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    if k == 2:
                                        himikat_kraska = Ximikat.objects.get(id=4)
                                        df_new_duplicate['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                        df_new_duplicate['TEXT2'].append(himikat_kraska.название)
                                        df_new_duplicate['MENGE'].append("КГ")
                                        df_new_duplicate['MEINS'].append(("%.3f" % ((-1)*float(alum_teks.пр_краситель_при_этом_тех_отхода)*mein_percent) ).replace('.',',')) ##XATO
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    
                                    if k==3:
                                        himikat_kraska = Ximikat.objects.get(id=1)
                                        df_new_duplicate['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                        df_new_duplicate['TEXT2'].append(himikat_kraska.название)
                                        df_new_duplicate['MENGE'].append("КГ")
                                        df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.хим_пг_к_окр_politeknik_кг_alupol_сr_51)*mein_percent)).replace('.',',')) ##XATO
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    if k == 4:
                                        himikat_kraska = Ximikat.objects.get(id=2)
                                        df_new_duplicate['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                        df_new_duplicate['TEXT2'].append(himikat_kraska.название)
                                        df_new_duplicate['MENGE'].append("КГ")
                                        df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.хим_пг_к_окр_politeknik_кг_alupol_ac_52)*mein_percent)).replace('.',',')) ##XATO
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    if k == 5:
                                        himikat_kraska = Ximikat.objects.get(id=3)
                                        df_new_duplicate['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                        df_new_duplicate['TEXT2'].append(himikat_kraska.название)
                                        df_new_duplicate['MENGE'].append("КГ")
                                        df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.хим_пг_к_окр_politeknik_кг_pol_ac_25p)*mein_percent)).replace('.',',')) ##XATO
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    
                                        
                                    df_new_duplicate['LGORT'].append(sklad['number_sklad'][p][k])
                            
                                # df_new_duplicate['STKTX'][j-6+i]=(df_new_duplicate['TEXT2'][j-4+i])
                    
                    else:
                        kraska_code = df[i][5].split()[-1][1:]
                        kraskas =Kraska.objects.filter(код_краски = kraska_code).order_by('order')
                        kraska_counter =0
                        for kras in kraskas:
                            for p in range(0,6):    
                                j+=1
                                kraska_counter +=1
                                if (df[i][4].split('-')[1][:1]=='P'):
                                    df_new_duplicate['ID'].append('1')
                                    df_new_duplicate['MATNR'].append(df[i][4])
                                    df_new_duplicate['WERKS'].append('1101')
                                    df_new_duplicate['TEXT1'].append(df[i][5])
                                    df_new_duplicate['STLAL'].append(f'{kraska_counter}')
                                    df_new_duplicate['STLAN'].append('1')
                                    ztekst = sklad['sklad_pokraski'][p]
                                    df_new_duplicate['ZTEXT'].append('Покраска')
                                    df_new_duplicate['STKTX'].append(ztekst)
                                    df_new_duplicate['BMENG'].append( '1000')
                                    df_new_duplicate['BMEIN'].append('ШТ')
                                    df_new_duplicate['STLST'].append('1')
                                    df_new_duplicate['POSNR'].append('')
                                    df_new_duplicate['POSTP'].append('')
                                    df_new_duplicate['MATNR1'].append('')
                                    df_new_duplicate['TEXT2'].append('')
                                    df_new_duplicate['MEINS'].append('')
                                    df_new_duplicate['MENGE'].append('')
                                    df_new_duplicate['DATUV'].append('01012021')
                                    df_new_duplicate['PUSTOY'].append('')
                                    df_new_duplicate['LGORT'].append('')
                                    length = df[i][4].split('-')[0]
                                    if product_type =='termo':
                                        alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length))[:1].get()
                                    else:
                                        alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                                    
                                    
                                    mein_percent =((get_legth(df[i][5]))/float(alum_teks.длина_профиля_м))
                                    
                                    for k in range(0,6):
                                        j+=1
                                        df_new_duplicate['ID'].append('2')
                                        df_new_duplicate['MATNR'].append('')
                                        df_new_duplicate['WERKS'].append('')
                                        df_new_duplicate['TEXT1'].append('')
                                        df_new_duplicate['STLAL'].append('')
                                        df_new_duplicate['STLAN'].append('')
                                        df_new_duplicate['ZTEXT'].append('')
                                        df_new_duplicate['STKTX'].append('')
                                        df_new_duplicate['BMENG'].append('')
                                        df_new_duplicate['BMEIN'].append('')
                                        df_new_duplicate['STLST'].append('')
                                        df_new_duplicate['POSNR'].append(k+1)
                                        df_new_duplicate['POSTP'].append('L')
                                        
                                        
                                        if k == 0 :
                                            df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                            df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                            df_new_duplicate['MEINS'].append('1000')
                                            df_new_duplicate['MENGE'].append('ШТ')
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        
                                        if k==1:
                                            df_new_duplicate['MATNR1'].append(kras.sap_code_s4q100)
                                            df_new_duplicate['TEXT2'].append(kras.название)
                                            df_new_duplicate['MENGE'].append('КГ')
                                            df_new_duplicate['MEINS'].append( ("%.3f" % (float(alum_teks.порошковый_краситель_рас_кг_на_1000_пр)*mein_percent)).replace('.',','))
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        if k == 2:
                                            himikat_kraska = Ximikat.objects.get(id=4)
                                            df_new_duplicate['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                            df_new_duplicate['TEXT2'].append(himikat_kraska.название)
                                            df_new_duplicate['MENGE'].append("КГ")
                                            df_new_duplicate['MEINS'].append(("%.3f" % ((-1)*float(alum_teks.пр_краситель_при_этом_тех_отхода)*mein_percent) ).replace('.',',')) ##XATO
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        
                                        if k==3:
                                            himikat_kraska = Ximikat.objects.get(id=1)
                                            df_new_duplicate['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                            df_new_duplicate['TEXT2'].append(himikat_kraska.название)
                                            df_new_duplicate['MENGE'].append("КГ")
                                            df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.хим_пг_к_окр_politeknik_кг_alupol_сr_51)*mein_percent)).replace('.',',')) ##XATO
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        if k == 4:
                                            himikat_kraska = Ximikat.objects.get(id=2)
                                            df_new_duplicate['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                            df_new_duplicate['TEXT2'].append(himikat_kraska.название)
                                            df_new_duplicate['MENGE'].append("КГ")
                                            df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.хим_пг_к_окр_politeknik_кг_alupol_ac_52)*mein_percent)).replace('.',',')) ##XATO
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        if k == 5:
                                            himikat_kraska = Ximikat.objects.get(id=3)
                                            df_new_duplicate['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                            df_new_duplicate['TEXT2'].append(himikat_kraska.название)
                                            df_new_duplicate['MENGE'].append("КГ")
                                            df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.хим_пг_к_окр_politeknik_кг_pol_ac_25p)*mein_percent)).replace('.',',')) ##XATO
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        
                                            
                                        df_new_duplicate['LGORT'].append(sklad['number_sklad'][p][k])
        
            
            older_process['sapcode'] =normaexist.artikul
            older_process['kratkiy'] =normaexist.kratkiytekst
            
        norma_existsS = CheckNormaBase.objects.filter(artikul=df[i][6],kratkiytekst=df[i][7]).exists()
        if not norma_existsS:
            if df[i][6] !="":
                CheckNormaBase(artikul=df[i][6],kratkiytekst=df[i][7]).save()
                if (df[i][6].split('-')[1][:1]=='S'):
                    j+=1
                    if (df[i][6].split('-')[1][:1]=='S'):
                        df_new['ID'].append('1')
                        df_new['MATNR'].append(df[i][6])
                        df_new['WERKS'].append('1101')
                        df_new['TEXT1'].append(df[i][7])
                        df_new['STLAL'].append(f'1')
                        df_new['STLAN'].append('1')
                        ztekst = 'Сублимация - Декоративное покрытие'
                        ateks2='Сублимация - '+df[i][7].split('_')[1]
                        df_new['ZTEXT'].append(ztekst)
                        df_new['STKTX'].append(ateks2)
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
                        length = df[i][6].split('-')[0]
                        
                        alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length))[:1].get()
                        
                        mein_percent =((get_legth(df[i][7]))/float(alum_teks.длина_профиля_м))
                        
                        sublimatsiya_code = df[i][7].split('_')[1]
                        if sublimatsiya_code =='7777':
                            code_ss = alum_teks.суб_ширина_декор_пленки_мм_зол_дуб
                            mein =alum_teks.сублимация_расход_на_1000_профиль_м21
                            
                        elif sublimatsiya_code =='8888':
                            
                            code_ss = alum_teks.суб_ширина_декор_пленки_мм_дуб_мокко
                            mein =alum_teks.сублимация_расход_на_1000_профиль_м23
                        elif sublimatsiya_code =='3701':
                            
                            code_ss = alum_teks.суб_ширина_декор_пленки_мм_3д_313701
                            mein =alum_teks.сублимация_расход_на_1000_профиль_м22
                        elif sublimatsiya_code =='3702':
                            
                            code_ss = alum_teks.суб_ширина_декор_пленки_мм_3д_313702
                            mein =alum_teks.сублимация_расход_на_1000_профиль_м24
                        
                        
                        for k in range(0,2):
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
                            df_new['POSNR'].append(k+1)
                            df_new['POSTP'].append('L')
                            
                            
                            if k == 0 :
                                df_new['MATNR1'].append(older_process['sapcode'])
                                df_new['TEXT2'].append(older_process['kratkiy'])
                                df_new['MEINS'].append('1000')
                                df_new['MENGE'].append('ШТ')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            
                            if k==1:
                                
                                subdecor = SubDekorPlonka.objects.get(код_декор_пленки = sublimatsiya_code, ширина_декор_пленки_мм = code_ss)
                                df_new['MATNR1'].append(subdecor.sap_code_s4q100)
                                df_new['TEXT2'].append(subdecor.название)
                                df_new['MENGE'].append('М2')
                                df_new['MEINS'].append( ("%.3f" % (float(mein)*mein_percent)).replace('.',','))
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            
                                
                            df_new['LGORT'].append('PS08')
                            
                older_process['sapcode'] =df[i][6]
                older_process['kratkiy'] =df[i][7]
        
        else:
            normaexist = CheckNormaBase.objects.filter(artikul=df[i][6],kratkiytekst=df[i][7])[:1].get()
            if df[i][6] !="":
                if (df[i][6].split('-')[1][:1]=='S'):
                    j+=1
                    if (df[i][6].split('-')[1][:1]=='S'):
                        df_new_duplicate['ID'].append('1')
                        df_new_duplicate['MATNR'].append(df[i][6])
                        df_new_duplicate['WERKS'].append('1101')
                        df_new_duplicate['TEXT1'].append(df[i][7])
                        df_new_duplicate['STLAL'].append(f'1')
                        df_new_duplicate['STLAN'].append('1')
                        ztekst = 'Сублимация - Декоративное покрытие'
                        ateks2='Сублимация - '+df[i][7].split('_')[1]
                        df_new_duplicate['ZTEXT'].append(ztekst)
                        df_new_duplicate['STKTX'].append(ateks2)
                        df_new_duplicate['BMENG'].append( '1000')
                        df_new_duplicate['BMEIN'].append('ШТ')
                        df_new_duplicate['STLST'].append('1')
                        df_new_duplicate['POSNR'].append('')
                        df_new_duplicate['POSTP'].append('')
                        df_new_duplicate['MATNR1'].append('')
                        df_new_duplicate['TEXT2'].append('')
                        df_new_duplicate['MEINS'].append('')
                        df_new_duplicate['MENGE'].append('')
                        df_new_duplicate['DATUV'].append('01012021')
                        df_new_duplicate['PUSTOY'].append('')
                        df_new_duplicate['LGORT'].append('')
                        length = df[i][6].split('-')[0]
                        
                        alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length))[:1].get()
                        
                        mein_percent =((get_legth(df[i][7]))/float(alum_teks.длина_профиля_м))
                        
                        sublimatsiya_code = df[i][7].split('_')[1]
                        if sublimatsiya_code =='7777':
                            code_ss = alum_teks.суб_ширина_декор_пленки_мм_зол_дуб
                            mein =alum_teks.сублимация_расход_на_1000_профиль_м21
                            
                        elif sublimatsiya_code =='8888':
                            
                            code_ss = alum_teks.суб_ширина_декор_пленки_мм_дуб_мокко
                            mein =alum_teks.сублимация_расход_на_1000_профиль_м23
                        elif sublimatsiya_code =='3701':
                            
                            code_ss = alum_teks.суб_ширина_декор_пленки_мм_3д_313701
                            mein =alum_teks.сублимация_расход_на_1000_профиль_м22
                        elif sublimatsiya_code =='3702':
                            
                            code_ss = alum_teks.суб_ширина_декор_пленки_мм_3д_313702
                            mein =alum_teks.сублимация_расход_на_1000_профиль_м24
                        
                        
                        for k in range(0,2):
                            j+=1
                            df_new_duplicate['ID'].append('2')
                            df_new_duplicate['MATNR'].append('')
                            df_new_duplicate['WERKS'].append('')
                            df_new_duplicate['TEXT1'].append('')
                            df_new_duplicate['STLAL'].append('')
                            df_new_duplicate['STLAN'].append('')
                            df_new_duplicate['ZTEXT'].append('')
                            df_new_duplicate['STKTX'].append('')
                            df_new_duplicate['BMENG'].append('')
                            df_new_duplicate['BMEIN'].append('')
                            df_new_duplicate['STLST'].append('')
                            df_new_duplicate['POSNR'].append(k+1)
                            df_new_duplicate['POSTP'].append('L')
                            
                            
                            if k == 0 :
                                df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                df_new_duplicate['MEINS'].append('1000')
                                df_new_duplicate['MENGE'].append('ШТ')
                                df_new_duplicate['DATUV'].append('')
                                df_new_duplicate['PUSTOY'].append('')
                            
                            if k==1:
                                
                                subdecor = SubDekorPlonka.objects.get(код_декор_пленки = sublimatsiya_code, ширина_декор_пленки_мм = code_ss)
                                df_new_duplicate['MATNR1'].append(subdecor.sap_code_s4q100)
                                df_new_duplicate['TEXT2'].append(subdecor.название)
                                df_new_duplicate['MENGE'].append('М2')
                                df_new_duplicate['MEINS'].append( ("%.3f" % (float(mein)*mein_percent)).replace('.',','))
                                df_new_duplicate['DATUV'].append('')
                                df_new_duplicate['PUSTOY'].append('')
                            
                            
                                
                            df_new_duplicate['LGORT'].append('PS08')
        
            older_process['sapcode'] =normaexist.artikul
            older_process['kratkiy'] =normaexist.kratkiytekst
        
            
        norma_existsN = CheckNormaBase.objects.filter(artikul=df[i][8],kratkiytekst=df[i][9]).exists()
        if not norma_existsN:
            if df[i][8] !="":
                if df[i][8].split('-')[0] in nakleyka_iskyuch:
                    continue
                CheckNormaBase(artikul=df[i][8],kratkiytekst=df[i][9]).save()
                if (df[i][8].split('-')[1][:1]=='N'):
                    
                        length = df[i][8].split('-')[0]
                      
                        alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length))[:1].get()
                        
                        mein_percent =((get_legth(df[i][9]))/float(alum_teks.длина_профиля_м))
                        
                        nakleyka_code = df[i][9].split()[-1]
                        
                        qatorlar_soni = 0
                        
                        if nakleyka_code =='A01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм == alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм != alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0')or(alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni = 4
                                if alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)
                                    meinss = float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                                elif alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                    meinss = float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)+float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                            elif ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni = 5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                                meinss2 =float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                                
                        elif nakleyka_code =='R05':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм=='0'))) 
                            log2 = ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм == '0'))
                            
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                
                                if alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)
                                    meinss = float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                                elif alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                            elif log2:
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)[:1].get()
                                meinss1 = float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                                meinss2 = float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                                
                        elif nakleyka_code =='B01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4        
                                if alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                                elif alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                                
                        elif nakleyka_code =='G01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                if alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                                elif alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                            elif ((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                                
                        elif nakleyka_code =='I01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                if alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                                elif alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)+float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                                meinss2 =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                                
                        elif nakleyka_code =='NB1':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                if alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                                elif alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                                
                        elif nakleyka_code =='E01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                if alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                                elif alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            elif ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            
                        elif nakleyka_code =='E02':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты and alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты !='0') or ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)and((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                if alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)
                                    meinss =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                                elif alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)+float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)[:1].get()
                                meinss1 =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                                meinss2 =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            
                        elif (nakleyka_code =='NT1') :
                            qatorlar_soni = 0

                        if qatorlar_soni == 4 :
                            for nakleykaa in nakleyka_results:
                                j+=1
                                if (df[i][8].split('-')[1][:1]=='N'):
                                    df_new['ID'].append('1')
                                    df_new['MATNR'].append(df[i][8])
                                    df_new['WERKS'].append('1101')
                                    df_new['TEXT1'].append(df[i][9])
                                    df_new['STLAL'].append(f'1')
                                    df_new['STLAN'].append('1')
                                    ztekst = 'Наклейка'
                                    df_new['ZTEXT'].append(ztekst)
                                    df_new['STKTX'].append(ztekst)
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
                                for k in range(0,2):
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
                                    df_new['POSNR'].append(k+1)
                                    df_new['POSTP'].append('L')
                                    
                                    
                                    if k == 0 :
                                        df_new['MATNR1'].append(older_process['sapcode'])
                                        df_new['TEXT2'].append(older_process['kratkiy'])
                                        df_new['MEINS'].append('1000')
                                        df_new['MENGE'].append('ШТ')
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==1:
                                        df_new['MATNR1'].append(nakleykaa.sap_code_s4q100)
                                        df_new['TEXT2'].append(nakleykaa.название)
                                        df_new['MENGE'].append('М2')
                                        df_new['MEINS'].append( ("%.3f" % (float(meinss)*mein_percent)).replace('.',','))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                        
                                    df_new['LGORT'].append('PS10')
                        elif qatorlar_soni == 5:
                            j+=1
                            if (df[i][8].split('-')[1][:1]=='N'):
                                df_new['ID'].append('1')
                                df_new['MATNR'].append(df[i][8])
                                df_new['WERKS'].append('1101')
                                df_new['TEXT1'].append(df[i][9])
                                df_new['STLAL'].append(f'1')
                                df_new['STLAN'].append('1')
                                ztekst = 'Наклейка'
                                df_new['ZTEXT'].append(ztekst)
                                df_new['STKTX'].append(ztekst)
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
                            for k in range(0,2):
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
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                
                                
                                if k == 0 :
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result1.название)
                                    df_new['MENGE'].append('М2')
                                    df_new['MEINS'].append( ("%.3f" % (float(meinss1)*mein_percent)).replace('.',','))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS10') 
                                
                            j+=1
                            if (df[i][8].split('-')[1][:1]=='N'):
                                df_new['ID'].append('1')
                                df_new['MATNR'].append(df[i][8])
                                df_new['WERKS'].append('1101')
                                df_new['TEXT1'].append(df[i][9])
                                df_new['STLAL'].append(f'1')
                                df_new['STLAN'].append('1')
                                ztekst = 'Наклейка'
                                df_new['ZTEXT'].append(ztekst)
                                df_new['STKTX'].append(ztekst)
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
                            for k in range(0,2):
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
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                
                                
                                if k == 0 :
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result2.название)
                                    df_new['MENGE'].append('М2')
                                    df_new['MEINS'].append( ("%.3f" % (float(meinss2)*mein_percent)).replace('.',','))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS10') 
                                
                                       
                older_process['sapcode'] =df[i][8]
                older_process['kratkiy'] =df[i][9]
        
        else:
            normaexist = CheckNormaBase.objects.filter(artikul=df[i][8],kratkiytekst=df[i][9])[:1].get()
            if df[i][8] !="":
                if df[i][8].split('-')[0] in nakleyka_iskyuch:
                    continue
                if (df[i][8].split('-')[1][:1]=='N'):
                    
                        length = df[i][8].split('-')[0]
                      
                        alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length))[:1].get()
                        
                        mein_percent =((get_legth(df[i][9]))/float(alum_teks.длина_профиля_м))
                        
                        nakleyka_code = df[i][9].split()[-1]
                        
                        qatorlar_soni = 0
                        
                        if nakleyka_code =='A01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм == alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм != alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0')or(alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni = 4
                                if alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)
                                    meinss = float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                                elif alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                    meinss = float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)+float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                            elif ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni = 5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                                meinss2 =float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                                
                        elif nakleyka_code =='R05':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм=='0'))) 
                            log2 = ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм == '0'))
                            
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                
                                if alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)
                                    meinss = float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                                elif alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                            elif log2:
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)[:1].get()
                                meinss1 = float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                                meinss2 = float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                                
                        elif nakleyka_code =='B01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4        
                                if alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                                elif alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                                
                        elif nakleyka_code =='G01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                if alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                                elif alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                            elif ((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                                
                        elif nakleyka_code =='I01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                if alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                                elif alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)+float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                                meinss2 =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                                
                        elif nakleyka_code =='NB1':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                if alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                                elif alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                                
                        elif nakleyka_code =='E01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                if alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                                elif alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            elif ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            
                        elif nakleyka_code =='E02':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты and alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты !='0') or ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)and((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                if alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)
                                    meinss =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                                elif alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)+float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)[:1].get()
                                meinss1 =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                                meinss2 =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            
                        elif (nakleyka_code =='NT1') :
                            qatorlar_soni = 0

                        if qatorlar_soni == 4 :
                            for nakleykaa in nakleyka_results:
                                j+=1
                                if (df[i][8].split('-')[1][:1]=='N'):
                                    df_new_duplicate['ID'].append('1')
                                    df_new_duplicate['MATNR'].append(df[i][8])
                                    df_new_duplicate['WERKS'].append('1101')
                                    df_new_duplicate['TEXT1'].append(df[i][9])
                                    df_new_duplicate['STLAL'].append(f'1')
                                    df_new_duplicate['STLAN'].append('1')
                                    ztekst = 'Наклейка'
                                    df_new_duplicate['ZTEXT'].append(ztekst)
                                    df_new_duplicate['STKTX'].append(ztekst)
                                    df_new_duplicate['BMENG'].append( '1000')
                                    df_new_duplicate['BMEIN'].append('ШТ')
                                    df_new_duplicate['STLST'].append('1')
                                    df_new_duplicate['POSNR'].append('')
                                    df_new_duplicate['POSTP'].append('')
                                    df_new_duplicate['MATNR1'].append('')
                                    df_new_duplicate['TEXT2'].append('')
                                    df_new_duplicate['MEINS'].append('')
                                    df_new_duplicate['MENGE'].append('')
                                    df_new_duplicate['DATUV'].append('01012021')
                                    df_new_duplicate['PUSTOY'].append('')
                                    df_new_duplicate['LGORT'].append('')
                                for k in range(0,2):
                                    j+=1
                                    df_new_duplicate['ID'].append('2')
                                    df_new_duplicate['MATNR'].append('')
                                    df_new_duplicate['WERKS'].append('')
                                    df_new_duplicate['TEXT1'].append('')
                                    df_new_duplicate['STLAL'].append('')
                                    df_new_duplicate['STLAN'].append('')
                                    df_new_duplicate['ZTEXT'].append('')
                                    df_new_duplicate['STKTX'].append('')
                                    df_new_duplicate['BMENG'].append('')
                                    df_new_duplicate['BMEIN'].append('')
                                    df_new_duplicate['STLST'].append('')
                                    df_new_duplicate['POSNR'].append(k+1)
                                    df_new_duplicate['POSTP'].append('L')
                                    
                                    
                                    if k == 0 :
                                        df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                        df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                        df_new_duplicate['MEINS'].append('1000')
                                        df_new_duplicate['MENGE'].append('ШТ')
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    
                                    if k==1:
                                        df_new_duplicate['MATNR1'].append(nakleykaa.sap_code_s4q100)
                                        df_new_duplicate['TEXT2'].append(nakleykaa.название)
                                        df_new_duplicate['MENGE'].append('М2')
                                        df_new_duplicate['MEINS'].append( ("%.3f" % (float(meinss)*mein_percent)).replace('.',','))
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    
                                    df_new_duplicate['LGORT'].append('PS10')
                        elif qatorlar_soni == 5:
                            j+=1
                            if (df[i][8].split('-')[1][:1]=='N'):
                                df_new_duplicate['ID'].append('1')
                                df_new_duplicate['MATNR'].append(df[i][8])
                                df_new_duplicate['WERKS'].append('1101')
                                df_new_duplicate['TEXT1'].append(df[i][9])
                                df_new_duplicate['STLAL'].append(f'1')
                                df_new_duplicate['STLAN'].append('1')
                                ztekst = 'Наклейка'
                                df_new_duplicate['ZTEXT'].append(ztekst)
                                df_new_duplicate['STKTX'].append(ztekst)
                                df_new_duplicate['BMENG'].append( '1000')
                                df_new_duplicate['BMEIN'].append('ШТ')
                                df_new_duplicate['STLST'].append('1')
                                df_new_duplicate['POSNR'].append('')
                                df_new_duplicate['POSTP'].append('')
                                df_new_duplicate['MATNR1'].append('')
                                df_new_duplicate['TEXT2'].append('')
                                df_new_duplicate['MEINS'].append('')
                                df_new_duplicate['MENGE'].append('')
                                df_new_duplicate['DATUV'].append('01012021')
                                df_new_duplicate['PUSTOY'].append('')
                                df_new_duplicate['LGORT'].append('')
                            for k in range(0,2):
                                j+=1
                                df_new_duplicate['ID'].append('2')
                                df_new_duplicate['MATNR'].append('')
                                df_new_duplicate['WERKS'].append('')
                                df_new_duplicate['TEXT1'].append('')
                                df_new_duplicate['STLAL'].append('')
                                df_new_duplicate['STLAN'].append('')
                                df_new_duplicate['ZTEXT'].append('')
                                df_new_duplicate['STKTX'].append('')
                                df_new_duplicate['BMENG'].append('')
                                df_new_duplicate['BMEIN'].append('')
                                df_new_duplicate['STLST'].append('')
                                df_new_duplicate['POSNR'].append(k+1)
                                df_new_duplicate['POSTP'].append('L')
                                
                                
                                if k == 0 :
                                    df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                    df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                    df_new_duplicate['MEINS'].append('1000')
                                    df_new_duplicate['MENGE'].append('ШТ')
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new_duplicate['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(nakleyka_result1.название)
                                    df_new_duplicate['MENGE'].append('М2')
                                    df_new_duplicate['MEINS'].append( ("%.3f" % (float(meinss1)*mein_percent)).replace('.',','))
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                df_new_duplicate['LGORT'].append('PS10') 
                                
                            j+=1
                            if (df[i][8].split('-')[1][:1]=='N'):
                                df_new_duplicate['ID'].append('1')
                                df_new_duplicate['MATNR'].append(df[i][8])
                                df_new_duplicate['WERKS'].append('1101')
                                df_new_duplicate['TEXT1'].append(df[i][9])
                                df_new_duplicate['STLAL'].append(f'1')
                                df_new_duplicate['STLAN'].append('1')
                                ztekst = 'Наклейка'
                                df_new_duplicate['ZTEXT'].append(ztekst)
                                df_new_duplicate['STKTX'].append(ztekst)
                                df_new_duplicate['BMENG'].append( '1000')
                                df_new_duplicate['BMEIN'].append('ШТ')
                                df_new_duplicate['STLST'].append('1')
                                df_new_duplicate['POSNR'].append('')
                                df_new_duplicate['POSTP'].append('')
                                df_new_duplicate['MATNR1'].append('')
                                df_new_duplicate['TEXT2'].append('')
                                df_new_duplicate['MEINS'].append('')
                                df_new_duplicate['MENGE'].append('')
                                df_new_duplicate['DATUV'].append('01012021')
                                df_new_duplicate['PUSTOY'].append('')
                                df_new_duplicate['LGORT'].append('')
                            for k in range(0,2):
                                j+=1
                                df_new_duplicate['ID'].append('2')
                                df_new_duplicate['MATNR'].append('')
                                df_new_duplicate['WERKS'].append('')
                                df_new_duplicate['TEXT1'].append('')
                                df_new_duplicate['STLAL'].append('')
                                df_new_duplicate['STLAN'].append('')
                                df_new_duplicate['ZTEXT'].append('')
                                df_new_duplicate['STKTX'].append('')
                                df_new_duplicate['BMENG'].append('')
                                df_new_duplicate['BMEIN'].append('')
                                df_new_duplicate['STLST'].append('')
                                df_new_duplicate['POSNR'].append(k+1)
                                df_new_duplicate['POSTP'].append('L')
                                
                                
                                if k == 0 :
                                    df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                    df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                    df_new_duplicate['MEINS'].append('1000')
                                    df_new_duplicate['MENGE'].append('ШТ')
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new_duplicate['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(nakleyka_result2.название)
                                    df_new_duplicate['MENGE'].append('М2')
                                    df_new_duplicate['MEINS'].append( ("%.3f" % (float(meinss2)*mein_percent)).replace('.',','))
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                df_new_duplicate['LGORT'].append('PS10') 
                                
                                       
                older_process['sapcode'] =df[i][8]
                older_process['kratkiy'] =df[i][9]
        
            older_process['sapcode'] = normaexist.artikul
            older_process['kratkiy'] = normaexist.kratkiytekst
            
        norma_existsK = CheckNormaBase.objects.filter(artikul=df[i][10],kratkiytekst=df[i][11]).exists()
        if not norma_existsK:
            if df[i][10] !="":
                CheckNormaBase(artikul=df[i][10],kratkiytekst=df[i][11]).save()
                if (df[i][10].split('-')[1][:1]=='K'):
                    
                    older_process_kombinirovanniy = {'s1':None,'k1':None,'s2':None,'k2':None,'s3':None,'k3':None}
                    ###############  Nakleyka   ###################
                    if df[i+1][8] !='':
                        older_process_kombinirovanniy['s1'] = df[i+1][8]
                        older_process_kombinirovanniy['k1'] = df[i+1][9]
                        if df[i+2][8] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][8]
                            older_process_kombinirovanniy['k2'] = df[i+2][9]
                        elif df[i+2][6] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][6]
                            older_process_kombinirovanniy['k2'] = df[i+2][7]
                        elif df[i+2][4] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][4]
                            older_process_kombinirovanniy['k2'] = df[i+2][5]
                        elif df[i+2][2] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][2]
                            older_process_kombinirovanniy['k2'] = df[i+2][3]
                        elif df[i+2][0] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][0]
                            older_process_kombinirovanniy['k2'] = df[i+2][1]
                        try:
                            if df[i+3][8] !='':
                                older_process_kombinirovanniy['s3'] = df[i+3][8]
                                older_process_kombinirovanniy['k3'] = df[i+3][9]
                        except:
                            older_process_kombinirovanniy['s3'] = None
                            older_process_kombinirovanniy['k3'] = None
                            
                    elif df[i+1][6] !='':
                        older_process_kombinirovanniy['s1'] = df[i+1][6]
                        older_process_kombinirovanniy['k1'] = df[i+1][7]
                        if df[i+2][8] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][8]
                            older_process_kombinirovanniy['k2'] = df[i+2][9]
                        elif df[i+2][6] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][6]
                            older_process_kombinirovanniy['k2'] = df[i+2][7]
                        elif df[i+2][4] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][4]
                            older_process_kombinirovanniy['k2'] = df[i+2][5]
                        elif df[i+2][2] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][2]
                            older_process_kombinirovanniy['k2'] = df[i+2][3]
                        elif df[i+2][0] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][0]
                            older_process_kombinirovanniy['k2'] = df[i+2][1]
                        try:
                            if df[i+3][6] !='':
                                older_process_kombinirovanniy['s3'] = df[i+3][6]
                                older_process_kombinirovanniy['k3'] = df[i+3][7]
                        except:
                            older_process_kombinirovanniy['s3'] = None
                            older_process_kombinirovanniy['k3'] = None
                        
                    elif df[i+1][4] !='':
                        older_process_kombinirovanniy['s1'] = df[i+1][4]
                        older_process_kombinirovanniy['k1'] = df[i+1][5]
                        if df[i+2][8] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][8]
                            older_process_kombinirovanniy['k2'] = df[i+2][9]
                        elif df[i+2][6] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][6]
                            older_process_kombinirovanniy['k2'] = df[i+2][7]
                        elif df[i+2][4] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][4]
                            older_process_kombinirovanniy['k2'] = df[i+2][5]
                        elif df[i+2][2] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][2]
                            older_process_kombinirovanniy['k2'] = df[i+2][3]
                        elif df[i+2][0] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][0]
                            older_process_kombinirovanniy['k2'] = df[i+2][1]
                        try:
                            if df[i+3][4] !='':
                                older_process_kombinirovanniy['s3'] = df[i+3][4]
                                older_process_kombinirovanniy['k3'] = df[i+3][5]
                        except:
                            older_process_kombinirovanniy['s3'] = None
                            older_process_kombinirovanniy['k3'] = None   
                        
                    elif df[i+1][2] !='':
                        older_process_kombinirovanniy['s1'] = df[i+1][2]
                        older_process_kombinirovanniy['k1'] = df[i+1][3]
                        if df[i+2][8] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][8]
                            older_process_kombinirovanniy['k2'] = df[i+2][9]
                        elif df[i+2][6] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][6]
                            older_process_kombinirovanniy['k2'] = df[i+2][7]
                        elif df[i+2][4] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][4]
                            older_process_kombinirovanniy['k2'] = df[i+2][5]
                        elif df[i+2][2] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][2]
                            older_process_kombinirovanniy['k2'] = df[i+2][3]
                        elif df[i+2][0] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][0]
                            older_process_kombinirovanniy['k2'] = df[i+2][1]
                        try:
                            if df[i+3][2] !='':
                                older_process_kombinirovanniy['s3'] = df[i+3][2]
                                older_process_kombinirovanniy['k3'] = df[i+3][3]
                        except:
                            older_process_kombinirovanniy['s3'] = None
                            older_process_kombinirovanniy['k3'] = None
                        
                    elif df[i+1][0] !='':
                        older_process_kombinirovanniy['s1'] = df[i+1][0]
                        older_process_kombinirovanniy['k1'] = df[i+1][1]
                        if df[i+2][8] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][8]
                            older_process_kombinirovanniy['k2'] = df[i+2][9]
                        elif df[i+2][6] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][6]
                            older_process_kombinirovanniy['k2'] = df[i+2][7]
                        elif df[i+2][4] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][4]
                            older_process_kombinirovanniy['k2'] = df[i+2][5]
                        elif df[i+2][2] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][2]
                            older_process_kombinirovanniy['k2'] = df[i+2][3]
                        elif df[i+2][0] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][0]
                            older_process_kombinirovanniy['k2'] = df[i+2][1]
                        try:
                            if df[i+3][0] !='':
                                older_process_kombinirovanniy['s3'] = df[i+3][0]
                                older_process_kombinirovanniy['k3'] = df[i+3][1]
                        except:
                            older_process_kombinirovanniy['s3'] = None
                            older_process_kombinirovanniy['k3'] = None
                        
                    
                    j+=1
                    if (df[i][10].split('-')[1][:1]=='K'):
                        df_new['ID'].append('1')
                        df_new['MATNR'].append(df[i][10])
                        df_new['WERKS'].append('1101')
                        df_new['TEXT1'].append(df[i][11])
                        df_new['STLAL'].append(f'1')
                        df_new['STLAN'].append('1')
                        ztekst = 'Комбинирование'
                        ateks2='Комбинирование'
                        df_new['ZTEXT'].append(ztekst)
                        df_new['STKTX'].append(ateks2)
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
                        length = df[i][10].split('-')[0]
                        
                        alum_teks = Norma.objects.filter(артикул=length)[:1].get()
                        
                        mein_percent =((get_legth(df[i][11]))/float(alum_teks.длина_профиля_м))
                        
                        artikul = df[i][10].split('-')[0]
                        kombininovanniy_utils = Norma.objects.get(артикул=artikul)
                        dddd =[
                                    {
                                        'sap_code':kombininovanniy_utils.термомост_1,
                                        'bridge':kombininovanniy_utils.краткий_текст_1
                                    },
                                    {
                                        'sap_code':kombininovanniy_utils.термомост_1,
                                        'bridge':kombininovanniy_utils.краткий_текст_2
                                    },
                                    {
                                        'sap_code':kombininovanniy_utils.термомост_3,
                                        'bridge':kombininovanniy_utils.краткий_текст_3
                                    },
                                    {
                                        'sap_code':kombininovanniy_utils.термомост_4,
                                        'bridge':kombininovanniy_utils.краткий_текст_4
                                    }
                                    ]
                        length_of_profile = get_legth(df[i][11]) * 1000
                        if older_process_kombinirovanniy['s3'] != None:
                            for k in range(0,3):
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
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                df_new['MATNR1'].append(older_process_kombinirovanniy[f's{k+1}'])
                                df_new['TEXT2'].append(older_process_kombinirovanniy[f'k{k+1}'])
                                df_new['MEINS'].append('1000')
                                df_new['MENGE'].append('ШТ')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS09')
                            
                            new_list_for_com = []
                            sap_code_new ={}
                            
                            for ii in range(0,4):
                            
                                if not dddd[ii]['bridge'] in sap_code_new:
                                    sap_code_new[dddd[ii]['bridge']] ={'sum':length_of_profile,'sap_code':dddd[ii]['sap_code']}
                                    
                                    
                                if not dddd[ii]['bridge'] in new_list_for_com:
                                    for jj in range(ii + 1 , 4):
                                        if dddd[ii]['bridge'] == dddd[jj]['bridge']:
                                            sap_code_new[dddd[ii]['bridge']]['sum']+=length_of_profile
                                        
                                new_list_for_com.append(dddd[ii]['bridge'])
                            ttt = 4
                            for key,val in sap_code_new.items(): 
                                j += 1
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
                                df_new['POSNR'].append(ttt)
                                df_new['POSTP'].append('L')
                                df_new['MATNR1'].append(val['sap_code'])
                                df_new['TEXT2'].append(key)
                                df_new['MEINS'].append(("%.3f" % (float(val['sum']))).replace('.',',')) ##XATO
                                df_new['MENGE'].append('М')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS09')
                                ttt +=1
                        
                                
                        else:
                            for k in range(0,2):
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
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                df_new['MATNR1'].append(older_process_kombinirovanniy[f's{k+1}'])
                                df_new['TEXT2'].append(older_process_kombinirovanniy[f'k{k+1}'])
                                df_new['MEINS'].append('1000')
                                df_new['MENGE'].append('ШТ')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS09')
                            
                            
                            if kombininovanniy_utils.краткий_текст_1 == kombininovanniy_utils.краткий_текст_2:
                                j += 1
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
                                df_new['MATNR1'].append(kombininovanniy_utils.термомост_1)
                                df_new['TEXT2'].append(kombininovanniy_utils.краткий_текст_1)
                                df_new['MEINS'].append( ("%.3f" % ( length_of_profile * 2 )).replace('.',','))
                                df_new['MENGE'].append('М')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS09')
                            else:
                                j += 1
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
                                df_new['MATNR1'].append(kombininovanniy_utils.термомост_1)
                                df_new['TEXT2'].append(kombininovanniy_utils.краткий_текст_1)
                                df_new['MEINS'].append(("%.3f" % ( length_of_profile)).replace('.',',')) ##XATO
                                df_new['MENGE'].append('М')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS09')
                                
                                j += 1
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
                                df_new['POSNR'].append(4)
                                df_new['POSTP'].append('L')
                                df_new['MATNR1'].append(kombininovanniy_utils.термомост_2)
                                df_new['TEXT2'].append(kombininovanniy_utils.краткий_текст_2)
                                df_new['MEINS'].append(("%.3f" % (length_of_profile)).replace('.',',')) ##XATO
                                df_new['MENGE'].append('М')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS09')
                                
                            
                            
                older_process['sapcode'] =df[i][10]
                older_process['kratkiy'] =df[i][11]
        
        else:
            normaexist = CheckNormaBase.objects.filter(artikul=df[i][10],kratkiytekst=df[i][11])[:1].get()
            if df[i][10] !="":
                if (df[i][10].split('-')[1][:1]=='K'):
                    
                    older_process_kombinirovanniy = {'s1':None,'k1':None,'s2':None,'k2':None,'s3':None,'k3':None}
                    ###############  Nakleyka   ###################
                    if df[i+1][8] !='':
                        older_process_kombinirovanniy['s1'] = df[i+1][8]
                        older_process_kombinirovanniy['k1'] = df[i+1][9]
                        if df[i+2][8] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][8]
                            older_process_kombinirovanniy['k2'] = df[i+2][9]
                        elif df[i+2][6] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][6]
                            older_process_kombinirovanniy['k2'] = df[i+2][7]
                        elif df[i+2][4] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][4]
                            older_process_kombinirovanniy['k2'] = df[i+2][5]
                        elif df[i+2][2] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][2]
                            older_process_kombinirovanniy['k2'] = df[i+2][3]
                        elif df[i+2][0] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][0]
                            older_process_kombinirovanniy['k2'] = df[i+2][1]
                        try:
                            if df[i+3][8] !='':
                                older_process_kombinirovanniy['s3'] = df[i+3][8]
                                older_process_kombinirovanniy['k3'] = df[i+3][9]
                        except:
                            older_process_kombinirovanniy['s3'] = None
                            older_process_kombinirovanniy['k3'] = None
                            
                    elif df[i+1][6] !='':
                        older_process_kombinirovanniy['s1'] = df[i+1][6]
                        older_process_kombinirovanniy['k1'] = df[i+1][7]
                        if df[i+2][8] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][8]
                            older_process_kombinirovanniy['k2'] = df[i+2][9]
                        elif df[i+2][6] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][6]
                            older_process_kombinirovanniy['k2'] = df[i+2][7]
                        elif df[i+2][4] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][4]
                            older_process_kombinirovanniy['k2'] = df[i+2][5]
                        elif df[i+2][2] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][2]
                            older_process_kombinirovanniy['k2'] = df[i+2][3]
                        elif df[i+2][0] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][0]
                            older_process_kombinirovanniy['k2'] = df[i+2][1]
                        try:
                            if df[i+3][6] !='':
                                older_process_kombinirovanniy['s3'] = df[i+3][6]
                                older_process_kombinirovanniy['k3'] = df[i+3][7]
                        except:
                            older_process_kombinirovanniy['s3'] = None
                            older_process_kombinirovanniy['k3'] = None
                        
                    elif df[i+1][4] !='':
                        older_process_kombinirovanniy['s1'] = df[i+1][4]
                        older_process_kombinirovanniy['k1'] = df[i+1][5]
                        if df[i+2][8] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][8]
                            older_process_kombinirovanniy['k2'] = df[i+2][9]
                        elif df[i+2][6] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][6]
                            older_process_kombinirovanniy['k2'] = df[i+2][7]
                        elif df[i+2][4] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][4]
                            older_process_kombinirovanniy['k2'] = df[i+2][5]
                        elif df[i+2][2] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][2]
                            older_process_kombinirovanniy['k2'] = df[i+2][3]
                        elif df[i+2][0] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][0]
                            older_process_kombinirovanniy['k2'] = df[i+2][1]
                        try:
                            if df[i+3][4] !='':
                                older_process_kombinirovanniy['s3'] = df[i+3][4]
                                older_process_kombinirovanniy['k3'] = df[i+3][5]
                        except:
                            older_process_kombinirovanniy['s3'] = None
                            older_process_kombinirovanniy['k3'] = None   
                        
                    elif df[i+1][2] !='':
                        older_process_kombinirovanniy['s1'] = df[i+1][2]
                        older_process_kombinirovanniy['k1'] = df[i+1][3]
                        if df[i+2][8] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][8]
                            older_process_kombinirovanniy['k2'] = df[i+2][9]
                        elif df[i+2][6] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][6]
                            older_process_kombinirovanniy['k2'] = df[i+2][7]
                        elif df[i+2][4] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][4]
                            older_process_kombinirovanniy['k2'] = df[i+2][5]
                        elif df[i+2][2] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][2]
                            older_process_kombinirovanniy['k2'] = df[i+2][3]
                        elif df[i+2][0] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][0]
                            older_process_kombinirovanniy['k2'] = df[i+2][1]
                        try:
                            if df[i+3][2] !='':
                                older_process_kombinirovanniy['s3'] = df[i+3][2]
                                older_process_kombinirovanniy['k3'] = df[i+3][3]
                        except:
                            older_process_kombinirovanniy['s3'] = None
                            older_process_kombinirovanniy['k3'] = None
                        
                    elif df[i+1][0] !='':
                        older_process_kombinirovanniy['s1'] = df[i+1][0]
                        older_process_kombinirovanniy['k1'] = df[i+1][1]
                        if df[i+2][8] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][8]
                            older_process_kombinirovanniy['k2'] = df[i+2][9]
                        elif df[i+2][6] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][6]
                            older_process_kombinirovanniy['k2'] = df[i+2][7]
                        elif df[i+2][4] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][4]
                            older_process_kombinirovanniy['k2'] = df[i+2][5]
                        elif df[i+2][2] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][2]
                            older_process_kombinirovanniy['k2'] = df[i+2][3]
                        elif df[i+2][0] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][0]
                            older_process_kombinirovanniy['k2'] = df[i+2][1]
                        try:
                            if df[i+3][0] !='':
                                older_process_kombinirovanniy['s3'] = df[i+3][0]
                                older_process_kombinirovanniy['k3'] = df[i+3][1]
                        except:
                            older_process_kombinirovanniy['s3'] = None
                            older_process_kombinirovanniy['k3'] = None
                        
                    
                    j+=1
                    if (df[i][10].split('-')[1][:1]=='K'):
                        df_new_duplicate['ID'].append('1')
                        df_new_duplicate['MATNR'].append(df[i][10])
                        df_new_duplicate['WERKS'].append('1101')
                        df_new_duplicate['TEXT1'].append(df[i][11])
                        df_new_duplicate['STLAL'].append(f'1')
                        df_new_duplicate['STLAN'].append('1')
                        ztekst = 'Комбинирование'
                        ateks2='Комбинирование'
                        df_new_duplicate['ZTEXT'].append(ztekst)
                        df_new_duplicate['STKTX'].append(ateks2)
                        df_new_duplicate['BMENG'].append( '1000')
                        df_new_duplicate['BMEIN'].append('ШТ')
                        df_new_duplicate['STLST'].append('1')
                        df_new_duplicate['POSNR'].append('')
                        df_new_duplicate['POSTP'].append('')
                        df_new_duplicate['MATNR1'].append('')
                        df_new_duplicate['TEXT2'].append('')
                        df_new_duplicate['MEINS'].append('')
                        df_new_duplicate['MENGE'].append('')
                        df_new_duplicate['DATUV'].append('01012021')
                        df_new_duplicate['PUSTOY'].append('')
                        df_new_duplicate['LGORT'].append('')
                        length = df[i][10].split('-')[0]
                        
                        alum_teks = Norma.objects.filter(артикул=length)[:1].get()
                        
                        mein_percent =((get_legth(df[i][11]))/float(alum_teks.длина_профиля_м))
                        
                        artikul = df[i][10].split('-')[0]
                        kombininovanniy_utils = Norma.objects.get(артикул=artikul)
                        dddd =[
                                    {
                                        'sap_code':kombininovanniy_utils.термомост_1,
                                        'bridge':kombininovanniy_utils.краткий_текст_1
                                    },
                                    {
                                        'sap_code':kombininovanniy_utils.термомост_1,
                                        'bridge':kombininovanniy_utils.краткий_текст_2
                                    },
                                    {
                                        'sap_code':kombininovanniy_utils.термомост_3,
                                        'bridge':kombininovanniy_utils.краткий_текст_3
                                    },
                                    {
                                        'sap_code':kombininovanniy_utils.термомост_4,
                                        'bridge':kombininovanniy_utils.краткий_текст_4
                                    }
                                    ]
                        length_of_profile = get_legth(df[i][11]) * 1000
                        if older_process_kombinirovanniy['s3'] != None:
                            for k in range(0,3):
                                j+=1
                                df_new_duplicate['ID'].append('2')
                                df_new_duplicate['MATNR'].append('')
                                df_new_duplicate['WERKS'].append('')
                                df_new_duplicate['TEXT1'].append('')
                                df_new_duplicate['STLAL'].append('')
                                df_new_duplicate['STLAN'].append('')
                                df_new_duplicate['ZTEXT'].append('')
                                df_new_duplicate['STKTX'].append('')
                                df_new_duplicate['BMENG'].append('')
                                df_new_duplicate['BMEIN'].append('')
                                df_new_duplicate['STLST'].append('')
                                df_new_duplicate['POSNR'].append(k+1)
                                df_new_duplicate['POSTP'].append('L')
                                df_new_duplicate['MATNR1'].append(older_process_kombinirovanniy[f's{k+1}'])
                                df_new_duplicate['TEXT2'].append(older_process_kombinirovanniy[f'k{k+1}'])
                                df_new_duplicate['MEINS'].append('1000')
                                df_new_duplicate['MENGE'].append('ШТ')
                                df_new_duplicate['DATUV'].append('')
                                df_new_duplicate['PUSTOY'].append('')
                                df_new_duplicate['LGORT'].append('PS09')
                            
                            new_list_for_com = []
                            sap_code_new ={}
                            
                            for ii in range(0,4):
                            
                                if not dddd[ii]['bridge'] in sap_code_new:
                                    sap_code_new[dddd[ii]['bridge']] ={'sum':length_of_profile,'sap_code':dddd[ii]['sap_code']}
                                    
                                    
                                if not dddd[ii]['bridge'] in new_list_for_com:
                                    for jj in range(ii + 1 , 4):
                                        if dddd[ii]['bridge'] == dddd[jj]['bridge']:
                                            sap_code_new[dddd[ii]['bridge']]['sum']+=length_of_profile
                                        
                                new_list_for_com.append(dddd[ii]['bridge'])
                            ttt = 4
                            for key,val in sap_code_new.items(): 
                                j += 1
                                df_new_duplicate['ID'].append('2')
                                df_new_duplicate['MATNR'].append('')
                                df_new_duplicate['WERKS'].append('')
                                df_new_duplicate['TEXT1'].append('')
                                df_new_duplicate['STLAL'].append('')
                                df_new_duplicate['STLAN'].append('')
                                df_new_duplicate['ZTEXT'].append('')
                                df_new_duplicate['STKTX'].append('')
                                df_new_duplicate['BMENG'].append('')
                                df_new_duplicate['BMEIN'].append('')
                                df_new_duplicate['STLST'].append('')
                                df_new_duplicate['POSNR'].append(ttt)
                                df_new_duplicate['POSTP'].append('L')
                                df_new_duplicate['MATNR1'].append(val['sap_code'])
                                df_new_duplicate['TEXT2'].append(key)
                                df_new_duplicate['MEINS'].append(("%.3f" % (float(val['sum']))).replace('.',',')) ##XATO
                                df_new_duplicate['MENGE'].append('М')
                                df_new_duplicate['DATUV'].append('')
                                df_new_duplicate['PUSTOY'].append('')
                                df_new_duplicate['LGORT'].append('PS09')
                                ttt +=1
                        
                                
                        else:
                            for k in range(0,2):
                                j+=1
                                df_new_duplicate['ID'].append('2')
                                df_new_duplicate['MATNR'].append('')
                                df_new_duplicate['WERKS'].append('')
                                df_new_duplicate['TEXT1'].append('')
                                df_new_duplicate['STLAL'].append('')
                                df_new_duplicate['STLAN'].append('')
                                df_new_duplicate['ZTEXT'].append('')
                                df_new_duplicate['STKTX'].append('')
                                df_new_duplicate['BMENG'].append('')
                                df_new_duplicate['BMEIN'].append('')
                                df_new_duplicate['STLST'].append('')
                                df_new_duplicate['POSNR'].append(k+1)
                                df_new_duplicate['POSTP'].append('L')
                                df_new_duplicate['MATNR1'].append(older_process_kombinirovanniy[f's{k+1}'])
                                df_new_duplicate['TEXT2'].append(older_process_kombinirovanniy[f'k{k+1}'])
                                df_new_duplicate['MEINS'].append('1000')
                                df_new_duplicate['MENGE'].append('ШТ')
                                df_new_duplicate['DATUV'].append('')
                                df_new_duplicate['PUSTOY'].append('')
                                df_new_duplicate['LGORT'].append('PS09')
                            
                            
                            if kombininovanniy_utils.краткий_текст_1 == kombininovanniy_utils.краткий_текст_2:
                                j += 1
                                df_new_duplicate['ID'].append('2')
                                df_new_duplicate['MATNR'].append('')
                                df_new_duplicate['WERKS'].append('')
                                df_new_duplicate['TEXT1'].append('')
                                df_new_duplicate['STLAL'].append('')
                                df_new_duplicate['STLAN'].append('')
                                df_new_duplicate['ZTEXT'].append('')
                                df_new_duplicate['STKTX'].append('')
                                df_new_duplicate['BMENG'].append('')
                                df_new_duplicate['BMEIN'].append('')
                                df_new_duplicate['STLST'].append('')
                                df_new_duplicate['POSNR'].append(3)
                                df_new_duplicate['POSTP'].append('L')
                                df_new_duplicate['MATNR1'].append(kombininovanniy_utils.термомост_1)
                                df_new_duplicate['TEXT2'].append(kombininovanniy_utils.краткий_текст_1)
                                df_new_duplicate['MEINS'].append( ("%.3f" % ( length_of_profile * 2 )).replace('.',','))
                                df_new_duplicate['MENGE'].append('М')
                                df_new_duplicate['DATUV'].append('')
                                df_new_duplicate['PUSTOY'].append('')
                                df_new_duplicate['LGORT'].append('PS09')
                            else:
                                j += 1
                                df_new_duplicate['ID'].append('2')
                                df_new_duplicate['MATNR'].append('')
                                df_new_duplicate['WERKS'].append('')
                                df_new_duplicate['TEXT1'].append('')
                                df_new_duplicate['STLAL'].append('')
                                df_new_duplicate['STLAN'].append('')
                                df_new_duplicate['ZTEXT'].append('')
                                df_new_duplicate['STKTX'].append('')
                                df_new_duplicate['BMENG'].append('')
                                df_new_duplicate['BMEIN'].append('')
                                df_new_duplicate['STLST'].append('')
                                df_new_duplicate['POSNR'].append(3)
                                df_new_duplicate['POSTP'].append('L')
                                df_new_duplicate['MATNR1'].append(kombininovanniy_utils.термомост_1)
                                df_new_duplicate['TEXT2'].append(kombininovanniy_utils.краткий_текст_1)
                                df_new_duplicate['MEINS'].append(("%.3f" % ( length_of_profile)).replace('.',',')) ##XATO
                                df_new_duplicate['MENGE'].append('М')
                                df_new_duplicate['DATUV'].append('')
                                df_new_duplicate['PUSTOY'].append('')
                                df_new_duplicate['LGORT'].append('PS09')
                                
                                j += 1
                                df_new_duplicate['ID'].append('2')
                                df_new_duplicate['MATNR'].append('')
                                df_new_duplicate['WERKS'].append('')
                                df_new_duplicate['TEXT1'].append('')
                                df_new_duplicate['STLAL'].append('')
                                df_new_duplicate['STLAN'].append('')
                                df_new_duplicate['ZTEXT'].append('')
                                df_new_duplicate['STKTX'].append('')
                                df_new_duplicate['BMENG'].append('')
                                df_new_duplicate['BMEIN'].append('')
                                df_new_duplicate['STLST'].append('')
                                df_new_duplicate['POSNR'].append(4)
                                df_new_duplicate['POSTP'].append('L')
                                df_new_duplicate['MATNR1'].append(kombininovanniy_utils.термомост_2)
                                df_new_duplicate['TEXT2'].append(kombininovanniy_utils.краткий_текст_2)
                                df_new_duplicate['MEINS'].append(("%.3f" % (length_of_profile)).replace('.',',')) ##XATO
                                df_new_duplicate['MENGE'].append('М')
                                df_new_duplicate['DATUV'].append('')
                                df_new_duplicate['PUSTOY'].append('')
                                df_new_duplicate['LGORT'].append('PS09')
                                
                            
            older_process['sapcode'] =normaexist.artikul
            older_process['kratkiy'] =normaexist.kratkiytekst
            
         
        
                     
        norma_exists7 = CheckNormaBase.objects.filter(artikul=df[i][12],kratkiytekst=df[i][13]).exists()
       
        if not norma_exists7:
            
            if df[i][12] !="":
                
                if (df[i][12].split('-')[1][:1]=='7'):
                    
                    lenghtht = df[i][12].split('-')[0]
                    
                    if lenghtht in zakalka_iskyucheniye7:
                        CheckNormaBase(artikul=df[i][12],kratkiytekst=df[i][13]).save()
                        j += 1
                        df_new['ID'].append('1')
                        df_new['MATNR'].append(df[i][12])
                        df_new['WERKS'].append('1101')
                        df_new['TEXT1'].append(df[i][13])
                        df_new['STLAL'].append('1')
                        df_new['STLAN'].append('1')
                        ztekst ='Упаковка'
                        df_new['ZTEXT'].append(ztekst)
                        length = df[i][12].split('-')[0]
                        
                        alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                        
                        
                        aliminisi =AlyuminniysilindrEkstruziya1.objects.filter(sap_code_s4q100 =alum_teks.qora_алю_сплав_6064_sap_code)[:1].get()
                        
                        
                        mein_percent =((get_legth(df[i][13]))/float(alum_teks.длина_профиля_м))
                        df_new['STKTX'].append(aliminisi.название)
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
                                df_new['MATNR1'].append(aliminisi.sap_code_s4q100)
                                df_new['TEXT2'].append(aliminisi.название)
                                df_new['MEINS'].append(("%.3f" % (float(alum_teks.алю_сп_6063_рас_спа_на_1000_шт_пр_кг)*mein_percent)).replace('.',',')) ##XATO
                                df_new['MENGE'].append('КГ')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            
                            
                            if k == 2:
                                alummm = AlyuminniysilindrEkstruziya2.objects.get(id=4)
                                df_new['MATNR1'].append(alummm.sap_code_s4q100)
                                df_new['TEXT2'].append(alummm.название)
                                df_new['MENGE'].append(alummm.еи)
                                df_new['MEINS'].append(("%.3f" % ((-1)*float(alum_teks.алюминиевый_сплав_6063_при_этом_балвашка)*mein_percent)).replace('.',',')) ##XATO
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            if k == 3:
                                alummm = AlyuminniysilindrEkstruziya2.objects.get(id=5)
                                df_new['MATNR1'].append(alummm.sap_code_s4q100)
                                df_new['TEXT2'].append(alummm.название)
                                df_new['MENGE'].append(alummm.еи)
                                df_new['MEINS'].append(("%.3f" % (((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода1)))*mein_percent) ).replace('.',',')) ##XATO
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            if k == 4:
                                alummm = AlyuminniysilindrEkstruziya2.objects.get(id=6)
                                df_new['MATNR1'].append(alummm.sap_code_s4q100)
                                df_new['TEXT2'].append(alummm.название)
                                df_new['MENGE'].append(alummm.еи)
                                df_new['MEINS'].append(("%.3f" % (((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода2)))*mein_percent) ).replace('.',',')) ##XATO
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('PS01')
                        continue

                    if '_' in df[i][13]:
                        ddd = df[i][13].split()[2]
                    
                    nakleyka_code = df[i][13].split()[-1]
                    length = df[i][12].split('-')[0]
                    
                    alum_teks =  Norma.objects.filter(Q(артикул=length)|Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length))[:1].get()
                    
                    mein_percent =((get_legth(df[i][13]))/float(alum_teks.длина_профиля_м))
                    
                    its_lamination = not ((not '_' in df[i][13]) or ('7777' in ddd.split('_')[1]) or ('8888' in ddd.split('_')[1]) or ('3701' in ddd.split('_')[1]) or ('3702' in ddd.split('_')[1]))
                    







                    if nakleyka_code =='A01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм == alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм != alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0')or(alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)
                                meinss = float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                            elif alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                meinss = float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн.replace(',','.'))
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)+float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                        elif ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni = 5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                            meinss2 =float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                            
                    elif nakleyka_code =='R05':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм=='0'))) 
                        log2 = ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм == '0'))
                        
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            
                            if alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)
                                meinss = float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                            elif alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                        elif log2:
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)[:1].get()
                            meinss1 = float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                            meinss2 = float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                            
                    elif nakleyka_code =='B01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4        
                            if alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                            elif alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                        elif ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                            meinss2 =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                            
                    elif nakleyka_code =='G01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                            elif alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                        elif ((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)
                            meinss2 =float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                            
                    elif nakleyka_code =='I01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                            elif alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)+float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                        elif ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                            meinss2 =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                            
                    elif nakleyka_code =='NB1':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                            elif alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                        elif ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                            meinss2 =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                            
                    elif nakleyka_code =='E01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            elif alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                        elif ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                            meinss2 =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                        
                    elif nakleyka_code =='E02':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты and alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты !='0') or ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)and((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)
                                meinss =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            elif alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)+float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                        elif ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)[:1].get()
                            meinss1 =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                            meinss2 =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                        
                    elif (nakleyka_code =='NT1') :
                        qatorlar_soni = 3
                
                    if its_lamination:
                        
                        if nakleyka_code =='A01' :
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм == alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм != alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0')or(alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni = 5
                                if alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                                elif alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)+float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                            elif ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni = 6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                                meinss2 =float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                                
                        elif nakleyka_code =='R05':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм=='0'))) 
                            log2 = ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм == '0'))
                            
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                                elif alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                            elif log2:
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                                    
                        elif nakleyka_code =='B01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                                elif alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                                
                        elif nakleyka_code =='G01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni = 5
                                if alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                                elif alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                            elif ((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                                
                        elif nakleyka_code =='I01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                                elif alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)+float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                                meinss2 =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                                
                        elif nakleyka_code =='NB1':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                                elif alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                                
                        elif nakleyka_code =='E01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                                elif alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            elif ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            
                        elif nakleyka_code =='E02':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты and alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты !='0') or ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)and((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)
                                    meinss =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                                elif alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)+float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)[:1].get()
                                meinss1 =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                                meinss2 =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            
                        elif (nakleyka_code =='NT1') :
                            qatorlar_soni = 4
                        
                        
                    ############Laminatsiya
                    
                    
                        
                        
                    its_kombinirovanniy ='-K' in df[i][10]
                    
                    
                    craft_counter = 0
                    if ((not '_' in df[i][13]) or ('7777' in ddd.split('_')[1]) or ('8888' in ddd.split('_')[1]) or ('3701' in ddd.split('_')[1]) or ('3702' in ddd.split('_')[1])):
                        
                        if its_kombinirovanniy:
                            if qatorlar_soni == 3:
                                j+=1
                                df_new['ID'].append('1')
                                df_new['MATNR'].append(df[i][12])
                                df_new['WERKS'].append('1101')
                                df_new['TEXT1'].append(df[i][13])
                                df_new['STLAL'].append('1')
                                df_new['STLAN'].append('1')
                                ztekst = 'Комбинированный + Упаковка'
                                df_new['ZTEXT'].append(ztekst)
                                df_new['STKTX'].append(ztekst)
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
                                length = df[i][12].split('-')[0]
                                
                                if length in accessuar:
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
                                    df_new['POSNR'].append(1)
                                    df_new['POSTP'].append('L')
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                    df_new['LGORT'].append('PS09')
                                    craft_counter += 1
                                else:
                                    print('#1',qatorlar_soni-1,2)
                                    for k in range(0,qatorlar_soni-1):
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
                                        df_new['POSNR'].append(k+1)
                                        df_new['POSTP'].append('L')
                                        craft_counter += 1
                                        
                                        if k == 0 :
                                            df_new['MATNR1'].append(older_process['sapcode'])
                                            df_new['TEXT2'].append(older_process['kratkiy'])
                                            df_new['MEINS'].append('1000')
                                            df_new['MENGE'].append('ШТ')
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        if k == 1:
                                            df_new['MATNR1'].append(siryo_dlya_upakovki1.sap_code_s4q100)
                                            df_new['TEXT2'].append(siryo_dlya_upakovki1.название)
                                            df_new['MENGE'].append('КГ')
                                            df_new['MEINS'].append( ("%.3f" % (float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent)).replace('.',','))
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        
                                        df_new['LGORT'].append('PS09')

                                
                            if ((qatorlar_soni == 4) or (qatorlar_soni == 5)):
                                j+=1
                                df_new['ID'].append('1')
                                df_new['MATNR'].append(df[i][12])
                                df_new['WERKS'].append('1101')
                                df_new['TEXT1'].append(df[i][13])
                                df_new['STLAL'].append(f'1')
                                df_new['STLAN'].append('1')
                                ztekst = 'Упаковка'
                                df_new['ZTEXT'].append(ztekst)
                                df_new['STKTX'].append('Комбинированный + Упаковка')
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
                                length = df[i][12].split('-')[0]
                                if length in accessuar:
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
                                    df_new['POSNR'].append(1)
                                    df_new['POSTP'].append('L')
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                    df_new['LGORT'].append('PS09')
                                    craft_counter+=1
                                else:
                                    for k in range(0,2):
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
                                        df_new['POSNR'].append(k+1)
                                        df_new['POSTP'].append('L')
                                        craft_counter+=1
                                        
                                        if k == 0 :
                                            df_new['MATNR1'].append(older_process['sapcode'])
                                            df_new['TEXT2'].append(older_process['kratkiy'])
                                            df_new['MEINS'].append('1000')
                                            df_new['MENGE'].append('ШТ')
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        if k==1:
                                            df_new['MATNR1'].append(siryo_dlya_upakovki1.sap_code_s4q100)
                                            df_new['TEXT2'].append(siryo_dlya_upakovki1.название)
                                            df_new['MENGE'].append('КГ')
                                            df_new['MEINS'].append(("%.3f" % (float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent)).replace('.',',')) ##XATO
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        
                                        
                                        df_new['LGORT'].append('PS09')

                        ##############################################     
                        else:
                            if qatorlar_soni == 3:
                                j+=1
                                df_new['ID'].append('1')
                                df_new['MATNR'].append(df[i][12])
                                df_new['WERKS'].append('1101')
                                df_new['TEXT1'].append(df[i][13])
                                df_new['STLAL'].append('1')
                                df_new['STLAN'].append('1')
                                ztekst = 'Упаковка'
                                df_new['ZTEXT'].append(ztekst)
                                df_new['STKTX'].append(ztekst)
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
                                length = df[i][12].split('-')[0]
                                if length in accessuar:
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
                                    df_new['POSNR'].append(1)
                                    df_new['POSTP'].append('L')                                                                               
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')    
                                    df_new['LGORT'].append('PS10')
                                    craft_counter+=1
                                else:
                                    print('#2',qatorlar_soni-1,2)
                                    for k in range(0,qatorlar_soni-1):
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
                                        df_new['POSNR'].append(k+1)
                                        df_new['POSTP'].append('L')
                                        craft_counter+=1
                                        
                                        if k == 0 :
                                            df_new['MATNR1'].append(older_process['sapcode'])
                                            df_new['TEXT2'].append(older_process['kratkiy'])
                                            df_new['MEINS'].append('1000')
                                            df_new['MENGE'].append('ШТ')
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        if k == 1:
                                            df_new['MATNR1'].append(siryo_dlya_upakovki1.sap_code_s4q100)
                                            df_new['TEXT2'].append(siryo_dlya_upakovki1.название)
                                            df_new['MENGE'].append('КГ')
                                            df_new['MEINS'].append( ("%.3f" % (float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent)).replace('.',','))
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        df_new['LGORT'].append('PS10')
                                
                                
                            if qatorlar_soni == 4:
                                jjj =0
                                for nakleykaa in nakleyka_results:
                                    jjj += 1
                                    j+=1
                                    df_new['ID'].append('1')
                                    df_new['MATNR'].append(df[i][12])
                                    df_new['WERKS'].append('1101')
                                    df_new['TEXT1'].append(df[i][13])
                                    df_new['STLAL'].append(f'{jjj}')
                                    df_new['STLAN'].append('1')
                                    ztekst = 'Упаковка'
                                    df_new['ZTEXT'].append(ztekst)
                                    df_new['STKTX'].append(ztekst)
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
                                    length = df[i][12].split('-')[0]
                                    if length in accessuar:   
                                        for k in range(0,2):
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
                                            df_new['POSNR'].append(k+1)
                                            df_new['POSTP'].append('L')
                                            craft_counter+=1
                                            
                                            if k == 0 :
                                                df_new['MATNR1'].append(older_process['sapcode'])
                                                df_new['TEXT2'].append(older_process['kratkiy'])
                                                df_new['MEINS'].append('1000')
                                                df_new['MENGE'].append('ШТ')
                                                df_new['DATUV'].append('')
                                                df_new['PUSTOY'].append('')
                                            
                                            if k == 1:
                                                df_new['MATNR1'].append(nakleykaa.sap_code_s4q100)
                                                df_new['TEXT2'].append(nakleykaa.название)
                                                df_new['MENGE'].append("М2")
                                                df_new['MEINS'].append(("%.3f" % ((meinss)*mein_percent)).replace('.',',')) ##XATO
                                                df_new['DATUV'].append('')
                                                df_new['PUSTOY'].append('')
                                            
                                            df_new['LGORT'].append('PS10')
                                
                            
                                    else:
                                        print('#3',qatorlar_soni-1,3)
                                        for k in range(0,qatorlar_soni-1):
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
                                            df_new['POSNR'].append(k+1)
                                            df_new['POSTP'].append('L')
                                            
                                            craft_counter+=1
                                            if k == 0 :
                                                df_new['MATNR1'].append(older_process['sapcode'])
                                                df_new['TEXT2'].append(older_process['kratkiy'])
                                                df_new['MEINS'].append('1000')
                                                df_new['MENGE'].append('ШТ')
                                                df_new['DATUV'].append('')
                                                df_new['PUSTOY'].append('')
                                            
                                            if k==1:
                                                df_new['MATNR1'].append(siryo_dlya_upakovki1.sap_code_s4q100)
                                                df_new['TEXT2'].append(siryo_dlya_upakovki1.название)
                                                df_new['MENGE'].append('КГ')
                                                df_new['MEINS'].append( ("%.3f" % (float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent)).replace('.',','))
                                                df_new['DATUV'].append('')
                                                df_new['PUSTOY'].append('')
                                            
                                            
                                            
                                            if k==2:
                                                df_new['MATNR1'].append(nakleykaa.sap_code_s4q100)
                                                df_new['TEXT2'].append(nakleykaa.название)
                                                df_new['MENGE'].append("М2")
                                                df_new['MEINS'].append(("%.3f" % ((meinss)*mein_percent)).replace('.',',')) ##XATO
                                                df_new['DATUV'].append('')
                                                df_new['PUSTOY'].append('')
                                            
                                            df_new['LGORT'].append('PS10')

                                    
                            if qatorlar_soni == 5:
                                j += 1
                                df_new['ID'].append('1')
                                df_new['MATNR'].append(df[i][12])
                                df_new['WERKS'].append('1101')
                                df_new['TEXT1'].append(df[i][13])
                                df_new['STLAL'].append('1')
                                df_new['STLAN'].append('1')
                                ztekst = 'Упаковка'
                                df_new['ZTEXT'].append(ztekst)
                                df_new['STKTX'].append(ztekst)
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
                                length = df[i][12].split('-')[0]
                                
                                if length in accessuar:
                                    for k in range(0,3):
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
                                        df_new['POSNR'].append(k+1)
                                        df_new['POSTP'].append('L')
                                        
                                        craft_counter +=1
                                        if k == 0 :
                                            df_new['MATNR1'].append(older_process['sapcode'])
                                            df_new['TEXT2'].append(older_process['kratkiy'])
                                            df_new['MEINS'].append('1000')
                                            df_new['MENGE'].append('ШТ')
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        
                                        if k==1:
                                            df_new['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                            df_new['TEXT2'].append(nakleyka_result1.название)
                                            df_new['MENGE'].append("М2")
                                            df_new['MEINS'].append(("%.3f" % (float(meinss1)*mein_percent)).replace('.',',')) ##XATO
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        if k==2:
                                            df_new['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                                            df_new['TEXT2'].append(nakleyka_result2.название)
                                            df_new['MENGE'].append("М2")
                                            df_new['MEINS'].append(("%.3f" % (float(meinss2)*mein_percent)).replace('.',',')) ##XATO
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        df_new['LGORT'].append('PS10')
                        
                                else:
                                    print('#4',qatorlar_soni-1,4)
                                    for k in range(0,qatorlar_soni-1):
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
                                        df_new['POSNR'].append(k+1)
                                        df_new['POSTP'].append('L')
                                        craft_counter +=1
                                        
                                        if k == 0 :
                                            df_new['MATNR1'].append(older_process['sapcode'])
                                            df_new['TEXT2'].append(older_process['kratkiy'])
                                            df_new['MEINS'].append('1000')
                                            df_new['MENGE'].append('ШТ')
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        if k==1:
                                            df_new['MATNR1'].append(siryo_dlya_upakovki1.sap_code_s4q100)
                                            df_new['TEXT2'].append(siryo_dlya_upakovki1.название)
                                            df_new['MENGE'].append('КГ')
                                            df_new['MEINS'].append( ("%.3f" % (float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent)).replace('.',','))
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        
                                        
                                        if k==2:
                                            df_new['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                            df_new['TEXT2'].append(nakleyka_result1.название)
                                            df_new['MENGE'].append("М2")
                                            df_new['MEINS'].append(("%.3f" % (float(meinss1)*mein_percent)).replace('.',',')) ##XATO
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        if k==3:
                                            df_new['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                                            df_new['TEXT2'].append(nakleyka_result2.название)
                                            df_new['MENGE'].append("М2")
                                            df_new['MEINS'].append(("%.3f" % (float(meinss2)*mein_percent)).replace('.',',')) ##XATO
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        df_new['LGORT'].append('PS10')

                        if alum_teks.бумага_расход_упоковочной_ленты_на_1000_штук_кг != '0' :
                            kraft_bumaga =Ximikat.objects.get(id=5)
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
                            df_new['POSNR'].append(craft_counter+1)
                            df_new['POSTP'].append('L')
                            df_new['MATNR1'].append(kraft_bumaga.sap_code_s4q100)
                            df_new['TEXT2'].append(kraft_bumaga.название)
                            df_new['MENGE'].append('КГ')
                            df_new['MEINS'].append( ("%.3f" % (float(alum_teks.бумага_расход_упоковочной_ленты_на_1000_штук_кг))).replace('.',','))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('PS09')

                                
                    else:
                        
                        laminatsiya_code = ddd.split('_')[1].split('/')
                        laminatsiya_code1 = laminatsiya_code[0]
                        laminatsiya_code2 = laminatsiya_code[1]
                        
                        if ((laminatsiya_code1 == laminatsiya_code2) or (laminatsiya_code1 =='XXXX' or laminatsiya_code2 == 'XXXX')):
                            qatorlar_soni +=1
                            
                            if laminatsiya_code1 =='XXXX':
                                meinsL = alum_teks.лам_низ_b_рас_ленты_на_1000_пр_м2
                                laminatsiya =Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code2)[:1].get() 
                            elif laminatsiya_code2 =='XXXX':
                                
                                meinsL = alum_teks.лам_верх_a_рас_ленты_на_1000_пр_м2
                                laminatsiya =Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code1)[:1].get() 
                            elif laminatsiya_code1 == laminatsiya_code2:
                                meinsL = float(alum_teks.лам_верх_a_рас_ленты_на_1000_пр_м2)+float(alum_teks.лам_низ_b_рас_ленты_на_1000_пр_м2)
                                
                                laminatsiya =Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code1)[:1].get() 
                                
                        else:
                            if qatorlar_soni ==5:
                                qatorlar_soni +=4
                            else:
                                # qatorlar_soni +=2
                                if qatorlar_soni == 4:
                                    qatorlar_soni += 6
                                else: 
                                    qatorlar_soni +=2
                            
                            laminatsiya_result1 = Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code1)[:1].get() 
                            laminatsiya_result2 = Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code2)[:1].get() 
                            meinsL1 = float(alum_teks.лам_верх_a_рас_ленты_на_1000_пр_м2)
                            meinsL2 = float(alum_teks.лам_низ_b_рас_ленты_на_1000_пр_м2)
                            
                        
                        if qatorlar_soni == 5:
                            j+=1
                            df_new['ID'].append('1')
                            df_new['MATNR'].append(df[i][12])
                            df_new['WERKS'].append('1101')
                            df_new['TEXT1'].append(df[i][13])
                            df_new['STLAL'].append('1')
                            df_new['STLAN'].append('1')
                            ztekst = 'Ламинация + Упаковка'
                            df_new['ZTEXT'].append(ztekst)
                            df_new['STKTX'].append(ztekst)
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
                            length = df[i][12].split('-')[0]
                            print('#5',qatorlar_soni,5)
                            for k in range(0,qatorlar_soni):
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
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                craft_counter+=1
                                
                                if k == 0 :
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new['MATNR1'].append(kleydlyalamp1.sap_code_s4q100)
                                    df_new['TEXT2'].append(kleydlyalamp1.название)
                                    df_new['MENGE'].append('КГ')
                                    df_new['MEINS'].append( ("%.3f" % (float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent)).replace('.',','))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==2:
                                    df_new['MATNR1'].append(kleydlyalamp2.sap_code_s4q100)
                                    df_new['TEXT2'].append(kleydlyalamp2.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==3:
                                    df_new['MATNR1'].append(kleydlyalamp3.sap_code_s4q100)
                                    df_new['TEXT2'].append(kleydlyalamp3.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==4:
                                    df_new['MATNR1'].append(laminatsiya.sap_code_s4q100)
                                    df_new['TEXT2'].append(laminatsiya.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(("%.3f" % (float(meinsL)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                
                                df_new['LGORT'].append('PS11')
                        
                        
                        if qatorlar_soni == 6:
                           
                            jjj =0
                            for nakleykaa in nakleyka_results:
                                jjj += 1
                                j+=1
                                df_new['ID'].append('1')
                                df_new['MATNR'].append(df[i][12])
                                df_new['WERKS'].append('1101')
                                df_new['TEXT1'].append(df[i][13])
                                df_new['STLAL'].append(f'{jjj}')
                                df_new['STLAN'].append('1')
                                ztekst = 'Ламинация + Наклейка + Упаковка'
                                df_new['ZTEXT'].append(ztekst)
                                df_new['STKTX'].append(ztekst)
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
                                length = df[i][12].split('-')[0]
                                print('#6',qatorlar_soni,6)
                                for k in range(0,qatorlar_soni):
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
                                    df_new['POSNR'].append(k+1)
                                    df_new['POSTP'].append('L')
                                    craft_counter+=1
                                    
                                    if k == 0 :
                                        df_new['MATNR1'].append(older_process['sapcode'])
                                        df_new['TEXT2'].append(older_process['kratkiy'])
                                        df_new['MEINS'].append('1000')
                                        df_new['MENGE'].append('ШТ')
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==1:
                                        df_new['MATNR1'].append(kleydlyalamp1.sap_code_s4q100)
                                        df_new['TEXT2'].append(kleydlyalamp1.название)
                                        df_new['MENGE'].append('КГ')
                                        df_new['MEINS'].append( ("%.3f" % (float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent)).replace('.',','))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==2:
                                        df_new['MATNR1'].append(kleydlyalamp2.sap_code_s4q100)
                                        df_new['TEXT2'].append(kleydlyalamp2.название)
                                        df_new['MENGE'].append("КГ")
                                        df_new['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent)).replace('.',',')) ##XATO
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==3:
                                        df_new['MATNR1'].append(kleydlyalamp3.sap_code_s4q100)
                                        df_new['TEXT2'].append(kleydlyalamp3.название)
                                        df_new['MENGE'].append("КГ")
                                        df_new['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent)).replace('.',',')) ##XATO
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==4:
                                        
                                        df_new['MATNR1'].append(nakleykaa.sap_code_s4q100)
                                        df_new['TEXT2'].append(nakleykaa.название)
                                        df_new['MENGE'].append("М2")
                                        df_new['MEINS'].append(("%.3f" % ((meinss*mein_percent))).replace('.',',')) ##XATO
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==5:
                                        
                                        df_new['MATNR1'].append(laminatsiya.sap_code_s4q100)
                                        df_new['TEXT2'].append(laminatsiya.название)
                                        df_new['MENGE'].append("М2")
                                        df_new['MEINS'].append(("%.3f" % (float(meinsL)*mein_percent)).replace('.',',')) ##XATO
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    
                                    df_new['LGORT'].append('PS11')
                    
                        if qatorlar_soni == 7:
                            j+=1
                            df_new['ID'].append('1')
                            df_new['MATNR'].append(df[i][12])
                            df_new['WERKS'].append('1101')
                            df_new['TEXT1'].append(df[i][13])
                            df_new['STLAL'].append(f'1')
                            df_new['STLAN'].append('1')
                            ztekst = 'Ламинация + Наклейка + Упаковка'
                            df_new['ZTEXT'].append(ztekst)
                            df_new['STKTX'].append(ztekst)
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
                            length = df[i][12].split('-')[0]
                            for k in range(0,qatorlar_soni):
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
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                craft_counter+=1
                                
                                if k == 0 :
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new['MATNR1'].append(kleydlyalamp1.sap_code_s4q100)
                                    df_new['TEXT2'].append(kleydlyalamp1.название)
                                    df_new['MENGE'].append('КГ')
                                    df_new['MEINS'].append( ("%.3f" % (float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent)).replace('.',','))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==2:
                                    df_new['MATNR1'].append(kleydlyalamp2.sap_code_s4q100)
                                    df_new['TEXT2'].append(kleydlyalamp2.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==3:
                                    df_new['MATNR1'].append(kleydlyalamp3.sap_code_s4q100)
                                    df_new['TEXT2'].append(kleydlyalamp3.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==4:
                                    df_new['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result1.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(("%.3f" % (float(meinss1)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k==5:
                                    df_new['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result2.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(("%.3f" % (float(meinss2)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==6:
                                    
                                    df_new['MATNR1'].append(laminatsiya.sap_code_s4q100)
                                    df_new['TEXT2'].append(laminatsiya.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(("%.3f" % (float(meinsL)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                
                                df_new['LGORT'].append('PS11')
                    
                        if qatorlar_soni == 8:
                            j += 1
                            df_new['ID'].append('1')
                            df_new['MATNR'].append(df[i][12])
                            df_new['WERKS'].append('1101')
                            df_new['TEXT1'].append(df[i][13])
                            df_new['STLAL'].append('1')
                            df_new['STLAN'].append('1')
                            ztekst = 'Ламинация + Наклейка + Упаковка'
                            df_new['ZTEXT'].append(ztekst)
                            df_new['STKTX'].append(ztekst)
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
                            length = df[i][12].split('-')[0]
                            for k in range(0,qatorlar_soni):
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
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                craft_counter+=1
                                
                                if k == 0 :
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new['MATNR1'].append(kleydlyalamp1.sap_code_s4q100)
                                    df_new['TEXT2'].append(kleydlyalamp1.название)
                                    df_new['MENGE'].append('КГ')
                                    df_new['MEINS'].append( ("%.3f" % (float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent)).replace('.',','))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==2:
                                    df_new['MATNR1'].append(kleydlyalamp2.sap_code_s4q100)
                                    df_new['TEXT2'].append(kleydlyalamp2.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==3:
                                    df_new['MATNR1'].append(kleydlyalamp3.sap_code_s4q100)
                                    df_new['TEXT2'].append(kleydlyalamp3.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==4:
                                    df_new['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result1.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(("%.3f" % (float(meinss1)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k==5:
                                    df_new['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result2.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(("%.3f" % (float(meinss2)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k == 6:
                                    df_new['MATNR1'].append(laminatsiya_result1.sap_code_s4q100)
                                    df_new['TEXT2'].append(laminatsiya_result1.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(("%.3f" % (float(meinsL1)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k == 7:
                                    df_new['MATNR1'].append(laminatsiya_result2.sap_code_s4q100)
                                    df_new['TEXT2'].append(laminatsiya_result2.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(("%.3f" % (float(meinsL2)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                df_new['LGORT'].append('PS11')
                        
                        if qatorlar_soni == 9:
                            nakleyka_result1 = nakleyka_results[:1].get()
                            j += 1
                            df_new['ID'].append('1')
                            df_new['MATNR'].append(df[i][12])
                            df_new['WERKS'].append('1101')
                            df_new['TEXT1'].append(df[i][13])
                            df_new['STLAL'].append('1')
                            df_new['STLAN'].append('1')
                            ztekst = 'Ламинация + Наклейка + Упаковка'
                            df_new['ZTEXT'].append(ztekst)
                            df_new['STKTX'].append(ztekst)
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
                            length = df[i][12].split('-')[0]
                            for k in range(0,7):
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
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                craft_counter+=1
                                
                                if k == 0 :
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new['MATNR1'].append(kleydlyalamp1.sap_code_s4q100)
                                    df_new['TEXT2'].append(kleydlyalamp1.название)
                                    df_new['MENGE'].append('КГ')
                                    df_new['MEINS'].append( ("%.3f" % (float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent)).replace('.',','))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==2:
                                    df_new['MATNR1'].append(kleydlyalamp2.sap_code_s4q100)
                                    df_new['TEXT2'].append(kleydlyalamp2.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==3:
                                    df_new['MATNR1'].append(kleydlyalamp3.sap_code_s4q100)
                                    df_new['TEXT2'].append(kleydlyalamp3.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==4:
                                    df_new['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result1.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(("%.3f" % (float(meinss)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k == 5:
                                    df_new['MATNR1'].append(laminatsiya_result1.sap_code_s4q100)
                                    df_new['TEXT2'].append(laminatsiya_result1.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(("%.3f" % (float(meinsL1)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k == 6:
                                    df_new['MATNR1'].append(laminatsiya_result2.sap_code_s4q100)
                                    df_new['TEXT2'].append(laminatsiya_result2.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(("%.3f" % (float(meinsL2)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS11')

                        if qatorlar_soni == 10:
                            j+=1
                            df_new['ID'].append('1')
                            df_new['MATNR'].append(df[i][12])
                            df_new['WERKS'].append('1101')
                            df_new['TEXT1'].append(df[i][13])
                            df_new['STLAL'].append('1')
                            df_new['STLAN'].append('1')
                            ztekst = 'Ламинация + Упаковка'
                            df_new['ZTEXT'].append(ztekst)
                            df_new['STKTX'].append(ztekst)
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
                            length = df[i][12].split('-')[0]
                            print('#5',qatorlar_soni,5)
                            for k in range(0,6):
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
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                craft_counter+=1
                                
                                if k == 0 :
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new['MATNR1'].append(kleydlyalamp1.sap_code_s4q100)
                                    df_new['TEXT2'].append(kleydlyalamp1.название)
                                    df_new['MENGE'].append('КГ')
                                    df_new['MEINS'].append( ("%.3f" % (float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent)).replace('.',','))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==2:
                                    df_new['MATNR1'].append(kleydlyalamp2.sap_code_s4q100)
                                    df_new['TEXT2'].append(kleydlyalamp2.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==3:
                                    df_new['MATNR1'].append(kleydlyalamp3.sap_code_s4q100)
                                    df_new['TEXT2'].append(kleydlyalamp3.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==4:
                                    df_new['MATNR1'].append(laminatsiya_result1.sap_code_s4q100)
                                    df_new['TEXT2'].append(laminatsiya_result1.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(("%.3f" % (float(meinsL1)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==5:
                                    df_new['MATNR1'].append(laminatsiya_result2.sap_code_s4q100)
                                    df_new['TEXT2'].append(laminatsiya_result2.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(("%.3f" % (float(meinsL2)*mein_percent)).replace('.',',')) ##XATO
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                
                                df_new['LGORT'].append('PS11')
                        
                        
                        
                        
                        if alum_teks.бумага_расход_упоковочной_ленты_на_1000_штук_кг != '0' :
                            kraft_bumaga =Ximikat.objects.get(id=5)
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
                            df_new['POSNR'].append(craft_counter+1)
                            df_new['POSTP'].append('L')
                            df_new['MATNR1'].append(kraft_bumaga.sap_code_s4q100)
                            df_new['TEXT2'].append(kraft_bumaga.название)
                            df_new['MENGE'].append('КГ')
                            df_new['MEINS'].append( ("%.3f" % (float(alum_teks.бумага_расход_упоковочной_ленты_на_1000_штук_кг))).replace('.',','))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('PS11')
                    
                older_process['sapcode'] =df[i][12]
                older_process['kratkiy'] =df[i][13]
                CheckNormaBase(artikul=df[i][12],kratkiytekst=df[i][13]).save()
        
        else:      
            if df[i][12] !="":
               
                if (df[i][12].split('-')[1][:1]=='7'):
                    
                    
                    if '_' in df[i][13]:
                        ddd = df[i][13].split()[2]
                    
                    nakleyka_code = df[i][13].split()[-1]
                    length = df[i][12].split('-')[0]
                    
                    alum_teks =  Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                    
                    mein_percent =((get_legth(df[i][13]))/float(alum_teks.длина_профиля_м))
                    
                    its_lamination = not ((not '_' in df[i][13]) or ('7777' in ddd.split('_')[1]) or ('8888' in ddd.split('_')[1]) or ('3701' in ddd.split('_')[1]) or ('3702' in ddd.split('_')[1]))
                    
                    if nakleyka_code =='A01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм == alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм != alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0')or(alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)
                                meinss = float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                            elif alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                meinss = float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)+float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                        elif ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni = 5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                            meinss2 =float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                            
                    elif nakleyka_code =='R05':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм=='0'))) 
                        log2 = ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм == '0'))
                        
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            
                            if alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)
                                meinss = float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                            elif alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                        elif log2:
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)[:1].get()
                            meinss1 = float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                            meinss2 = float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                            
                    elif nakleyka_code =='B01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4        
                            if alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                            elif alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                        elif ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                            meinss2 =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                            
                    elif nakleyka_code =='G01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                            elif alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                        elif ((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)
                            meinss2 =float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                            
                    elif nakleyka_code =='I01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                            elif alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)+float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                        elif ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                            meinss2 =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                            
                    elif nakleyka_code =='NB1':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                            elif alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                        elif ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                            meinss2 =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                            
                    elif nakleyka_code =='E01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            elif alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                        elif ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                            meinss2 =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                        
                    elif nakleyka_code =='E02':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты and alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты !='0') or ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)and((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)
                                meinss =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            elif alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)+float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                        elif ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)[:1].get()
                            meinss1 =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                            meinss2 =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                        
                    elif (nakleyka_code =='NT1') :
                        qatorlar_soni = 3
                
                    if its_lamination:
                        
                        if nakleyka_code =='A01' :
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм == alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм != alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0')or(alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni = 5
                                if alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                                elif alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)+float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                            elif ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni = 6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                                meinss2 =float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                                
                        elif nakleyka_code =='R05':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм=='0'))) 
                            log2 = ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм == '0'))
                            
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                                elif alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                            elif log2:
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                                    
                        elif nakleyka_code =='B01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                                elif alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                                
                        elif nakleyka_code =='G01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni = 5
                                if alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                                elif alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                            elif ((alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'G01',ширина= alum_teks.заш_пл_кг_м_голд_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_голд_вр_и_кг_м_голд_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2)
                                
                        elif nakleyka_code =='I01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                                elif alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)+float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                                meinss2 =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                                
                        elif nakleyka_code =='NB1':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                                elif alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                                
                        elif nakleyka_code =='E01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                                elif alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            elif ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            
                        elif nakleyka_code =='E02':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты and alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты !='0') or ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)and((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                print('shuyerdaadad qiymat 5')
                                if alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)
                                    meinss =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                                elif alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)+float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты == '0')):
                                qatorlar_soni = 4
                                print('shuyerdaadad qiymat 4')
                            else:
                                qatorlar_soni =6
                                print('shuyerdaadad qiymat 6')
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)[:1].get()
                                meinss1 =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                                meinss2 =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            
                        elif (nakleyka_code =='NT1') :
                            qatorlar_soni = 4
                        
                        
                    ############Laminatsiya
                    
                    
                        
                        
                    its_kombinirovanniy ='-K' in df[i][10]
                    
                    
                    craft_counter = 0
                    if ((not '_' in df[i][13]) or ('7777' in ddd.split('_')[1]) or ('8888' in ddd.split('_')[1]) or ('3701' in ddd.split('_')[1]) or ('3702' in ddd.split('_')[1])):
                        
                        if its_kombinirovanniy:
                            if qatorlar_soni == 3:
                                j+=1
                                df_new_duplicate['ID'].append('1')
                                df_new_duplicate['MATNR'].append(df[i][12])
                                df_new_duplicate['WERKS'].append('1101')
                                df_new_duplicate['TEXT1'].append(df[i][13])
                                df_new_duplicate['STLAL'].append('1')
                                df_new_duplicate['STLAN'].append('1')
                                ztekst = 'Упаковка'
                                df_new_duplicate['ZTEXT'].append(ztekst)
                                df_new_duplicate['STKTX'].append(ztekst)
                                df_new_duplicate['BMENG'].append( '1000')
                                df_new_duplicate['BMEIN'].append('ШТ')
                                df_new_duplicate['STLST'].append('1')
                                df_new_duplicate['POSNR'].append('')
                                df_new_duplicate['POSTP'].append('')
                                df_new_duplicate['MATNR1'].append('')
                                df_new_duplicate['TEXT2'].append('')
                                df_new_duplicate['MEINS'].append('')
                                df_new_duplicate['MENGE'].append('')
                                df_new_duplicate['DATUV'].append('01012021')
                                df_new_duplicate['PUSTOY'].append('')
                                df_new_duplicate['LGORT'].append('')
                                length = df[i][12].split('-')[0]
                                
                                if length in accessuar:
                                    j+=1
                                    df_new_duplicate['ID'].append('2')
                                    df_new_duplicate['MATNR'].append('')
                                    df_new_duplicate['WERKS'].append('')
                                    df_new_duplicate['TEXT1'].append('')
                                    df_new_duplicate['STLAL'].append('')
                                    df_new_duplicate['STLAN'].append('')
                                    df_new_duplicate['ZTEXT'].append('')
                                    df_new_duplicate['STKTX'].append('')
                                    df_new_duplicate['BMENG'].append('')
                                    df_new_duplicate['BMEIN'].append('')
                                    df_new_duplicate['STLST'].append('')
                                    df_new_duplicate['POSNR'].append(1)
                                    df_new_duplicate['POSTP'].append('L')
                                    df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                    df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                    df_new_duplicate['MEINS'].append('1000')
                                    df_new_duplicate['MENGE'].append('ШТ')
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                    df_new_duplicate['LGORT'].append('PS09')
                                    craft_counter += 1
                                else:
                                    for k in range(0,qatorlar_soni-1):
                                        j+=1
                                        df_new_duplicate['ID'].append('2')
                                        df_new_duplicate['MATNR'].append('')
                                        df_new_duplicate['WERKS'].append('')
                                        df_new_duplicate['TEXT1'].append('')
                                        df_new_duplicate['STLAL'].append('')
                                        df_new_duplicate['STLAN'].append('')
                                        df_new_duplicate['ZTEXT'].append('')
                                        df_new_duplicate['STKTX'].append('')
                                        df_new_duplicate['BMENG'].append('')
                                        df_new_duplicate['BMEIN'].append('')
                                        df_new_duplicate['STLST'].append('')
                                        df_new_duplicate['POSNR'].append(k+1)
                                        df_new_duplicate['POSTP'].append('L')
                                        craft_counter += 1
                                        
                                        if k == 0 :
                                            df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                            df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                            df_new_duplicate['MEINS'].append('1000')
                                            df_new_duplicate['MENGE'].append('ШТ')
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        
                                        if k==1:
                                            df_new_duplicate['MATNR1'].append(siryo_dlya_upakovki1.sap_code_s4q100)
                                            df_new_duplicate['TEXT2'].append(siryo_dlya_upakovki1.название)
                                            df_new_duplicate['MENGE'].append('КГ')
                                            df_new_duplicate['MEINS'].append( ("%.3f" % (float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent)).replace('.',','))
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        df_new_duplicate['LGORT'].append('PS09')

                                
                            if ((qatorlar_soni == 4) or (qatorlar_soni == 5)):
                                j+=1
                                df_new_duplicate['ID'].append('1')
                                df_new_duplicate['MATNR'].append(df[i][12])
                                df_new_duplicate['WERKS'].append('1101')
                                df_new_duplicate['TEXT1'].append(df[i][13])
                                df_new_duplicate['STLAL'].append(f'1')
                                df_new_duplicate['STLAN'].append('1')
                                ztekst = 'Упаковка'
                                df_new_duplicate['ZTEXT'].append(ztekst)
                                df_new_duplicate['STKTX'].append('Комбинированный + Упаковка')
                                df_new_duplicate['BMENG'].append( '1000')
                                df_new_duplicate['BMEIN'].append('ШТ')
                                df_new_duplicate['STLST'].append('1')
                                df_new_duplicate['POSNR'].append('')
                                df_new_duplicate['POSTP'].append('')
                                df_new_duplicate['MATNR1'].append('')
                                df_new_duplicate['TEXT2'].append('')
                                df_new_duplicate['MEINS'].append('')
                                df_new_duplicate['MENGE'].append('')
                                df_new_duplicate['DATUV'].append('01012021')
                                df_new_duplicate['PUSTOY'].append('')
                                df_new_duplicate['LGORT'].append('')
                                length = df[i][12].split('-')[0]
                                if length in accessuar:
                                    j+=1
                                    df_new_duplicate['ID'].append('2')
                                    df_new_duplicate['MATNR'].append('')
                                    df_new_duplicate['WERKS'].append('')
                                    df_new_duplicate['TEXT1'].append('')
                                    df_new_duplicate['STLAL'].append('')
                                    df_new_duplicate['STLAN'].append('')
                                    df_new_duplicate['ZTEXT'].append('')
                                    df_new_duplicate['STKTX'].append('')
                                    df_new_duplicate['BMENG'].append('')
                                    df_new_duplicate['BMEIN'].append('')
                                    df_new_duplicate['STLST'].append('')
                                    df_new_duplicate['POSNR'].append(1)
                                    df_new_duplicate['POSTP'].append('L')
                                    df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                    df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                    df_new_duplicate['MEINS'].append('1000')
                                    df_new_duplicate['MENGE'].append('ШТ')
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                    df_new_duplicate['LGORT'].append('PS09')
                                    craft_counter+=1
                                else:
                                    for k in range(0,2):
                                        j+=1
                                        df_new_duplicate['ID'].append('2')
                                        df_new_duplicate['MATNR'].append('')
                                        df_new_duplicate['WERKS'].append('')
                                        df_new_duplicate['TEXT1'].append('')
                                        df_new_duplicate['STLAL'].append('')
                                        df_new_duplicate['STLAN'].append('')
                                        df_new_duplicate['ZTEXT'].append('')
                                        df_new_duplicate['STKTX'].append('')
                                        df_new_duplicate['BMENG'].append('')
                                        df_new_duplicate['BMEIN'].append('')
                                        df_new_duplicate['STLST'].append('')
                                        df_new_duplicate['POSNR'].append(k+1)
                                        df_new_duplicate['POSTP'].append('L')
                                        craft_counter+=1
                                        
                                        if k == 0 :
                                            df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                            df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                            df_new_duplicate['MEINS'].append('1000')
                                            df_new_duplicate['MENGE'].append('ШТ')
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        
                                        if k==1:
                                            df_new_duplicate['MATNR1'].append(siryo_dlya_upakovki1.sap_code_s4q100)
                                            df_new_duplicate['TEXT2'].append(siryo_dlya_upakovki1.название)
                                            df_new_duplicate['MENGE'].append('КГ')
                                            df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent)).replace('.',',')) ##XATO
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        
                                        df_new_duplicate['LGORT'].append('PS09')

                        ##############################################     
                        else:
                            if qatorlar_soni == 3:
                                j+=1
                                df_new_duplicate['ID'].append('1')
                                df_new_duplicate['MATNR'].append(df[i][12])
                                df_new_duplicate['WERKS'].append('1101')
                                df_new_duplicate['TEXT1'].append(df[i][13])
                                df_new_duplicate['STLAL'].append('1')
                                df_new_duplicate['STLAN'].append('1')
                                ztekst = 'Упаковка'
                                df_new_duplicate['ZTEXT'].append(ztekst)
                                df_new_duplicate['STKTX'].append(ztekst)
                                df_new_duplicate['BMENG'].append( '1000')
                                df_new_duplicate['BMEIN'].append('ШТ')
                                df_new_duplicate['STLST'].append('1')
                                df_new_duplicate['POSNR'].append('')
                                df_new_duplicate['POSTP'].append('')
                                df_new_duplicate['MATNR1'].append('')
                                df_new_duplicate['TEXT2'].append('')
                                df_new_duplicate['MEINS'].append('')
                                df_new_duplicate['MENGE'].append('')
                                df_new_duplicate['DATUV'].append('01012021')
                                df_new_duplicate['PUSTOY'].append('')
                                df_new_duplicate['LGORT'].append('')
                                length = df[i][12].split('-')[0]
                                if length in accessuar:
                                    j+=1
                                    df_new_duplicate['ID'].append('2')
                                    df_new_duplicate['MATNR'].append('')
                                    df_new_duplicate['WERKS'].append('')
                                    df_new_duplicate['TEXT1'].append('')
                                    df_new_duplicate['STLAL'].append('')
                                    df_new_duplicate['STLAN'].append('')
                                    df_new_duplicate['ZTEXT'].append('')
                                    df_new_duplicate['STKTX'].append('')
                                    df_new_duplicate['BMENG'].append('')
                                    df_new_duplicate['BMEIN'].append('')
                                    df_new_duplicate['STLST'].append('')
                                    df_new_duplicate['POSNR'].append(1)
                                    df_new_duplicate['POSTP'].append('L')                                                                               
                                    df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                    df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                    df_new_duplicate['MEINS'].append('1000')
                                    df_new_duplicate['MENGE'].append('ШТ')
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')    
                                    df_new_duplicate['LGORT'].append('PS10')
                                    craft_counter+=1
                                else:
                                    for k in range(0,qatorlar_soni-1):
                                        j+=1
                                        df_new_duplicate['ID'].append('2')
                                        df_new_duplicate['MATNR'].append('')
                                        df_new_duplicate['WERKS'].append('')
                                        df_new_duplicate['TEXT1'].append('')
                                        df_new_duplicate['STLAL'].append('')
                                        df_new_duplicate['STLAN'].append('')
                                        df_new_duplicate['ZTEXT'].append('')
                                        df_new_duplicate['STKTX'].append('')
                                        df_new_duplicate['BMENG'].append('')
                                        df_new_duplicate['BMEIN'].append('')
                                        df_new_duplicate['STLST'].append('')
                                        df_new_duplicate['POSNR'].append(k+1)
                                        df_new_duplicate['POSTP'].append('L')
                                        craft_counter+=1
                                        
                                        if k == 0 :
                                            df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                            df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                            df_new_duplicate['MEINS'].append('1000')
                                            df_new_duplicate['MENGE'].append('ШТ')
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        
                                        if k==1:
                                            df_new_duplicate['MATNR1'].append(siryo_dlya_upakovki1.sap_code_s4q100)
                                            df_new_duplicate['TEXT2'].append(siryo_dlya_upakovki1.название)
                                            df_new_duplicate['MENGE'].append('КГ')
                                            df_new_duplicate['MEINS'].append( ("%.3f" % (float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent)).replace('.',','))
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        
                                        df_new_duplicate['LGORT'].append('PS10')
                                
                                
                            if qatorlar_soni == 4:
                                jjj =0
                                for nakleykaa in nakleyka_results:
                                    jjj += 1
                                    j+=1
                                    df_new_duplicate['ID'].append('1')
                                    df_new_duplicate['MATNR'].append(df[i][12])
                                    df_new_duplicate['WERKS'].append('1101')
                                    df_new_duplicate['TEXT1'].append(df[i][13])
                                    df_new_duplicate['STLAL'].append(f'{jjj}')
                                    df_new_duplicate['STLAN'].append('1')
                                    ztekst = 'Упаковка'
                                    df_new_duplicate['ZTEXT'].append(ztekst)
                                    df_new_duplicate['STKTX'].append(ztekst)
                                    df_new_duplicate['BMENG'].append( '1000')
                                    df_new_duplicate['BMEIN'].append('ШТ')
                                    df_new_duplicate['STLST'].append('1')
                                    df_new_duplicate['POSNR'].append('')
                                    df_new_duplicate['POSTP'].append('')
                                    df_new_duplicate['MATNR1'].append('')
                                    df_new_duplicate['TEXT2'].append('')
                                    df_new_duplicate['MEINS'].append('')
                                    df_new_duplicate['MENGE'].append('')
                                    df_new_duplicate['DATUV'].append('01012021')
                                    df_new_duplicate['PUSTOY'].append('')
                                    df_new_duplicate['LGORT'].append('')
                                    length = df[i][12].split('-')[0]
                                    if length in accessuar:   
                                        for k in range(0,2):
                                            j+=1
                                            df_new_duplicate['ID'].append('2')
                                            df_new_duplicate['MATNR'].append('')
                                            df_new_duplicate['WERKS'].append('')
                                            df_new_duplicate['TEXT1'].append('')
                                            df_new_duplicate['STLAL'].append('')
                                            df_new_duplicate['STLAN'].append('')
                                            df_new_duplicate['ZTEXT'].append('')
                                            df_new_duplicate['STKTX'].append('')
                                            df_new_duplicate['BMENG'].append('')
                                            df_new_duplicate['BMEIN'].append('')
                                            df_new_duplicate['STLST'].append('')
                                            df_new_duplicate['POSNR'].append(k+1)
                                            df_new_duplicate['POSTP'].append('L')
                                            craft_counter+=1
                                            
                                            if k == 0 :
                                                df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                                df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                                df_new_duplicate['MEINS'].append('1000')
                                                df_new_duplicate['MENGE'].append('ШТ')
                                                df_new_duplicate['DATUV'].append('')
                                                df_new_duplicate['PUSTOY'].append('')
                                            
                                            if k == 1:
                                                df_new_duplicate['MATNR1'].append(nakleykaa.sap_code_s4q100)
                                                df_new_duplicate['TEXT2'].append(nakleykaa.название)
                                                df_new_duplicate['MENGE'].append("М2")
                                                df_new_duplicate['MEINS'].append(("%.3f" % ((meinss)*mein_percent)).replace('.',',')) ##XATO
                                                df_new_duplicate['DATUV'].append('')
                                                df_new_duplicate['PUSTOY'].append('')
                                            
                                            df_new_duplicate['LGORT'].append('PS10')
                                
                            
                                    else:
                                        for k in range(0,qatorlar_soni-1):
                                            j+=1
                                            df_new_duplicate['ID'].append('2')
                                            df_new_duplicate['MATNR'].append('')
                                            df_new_duplicate['WERKS'].append('')
                                            df_new_duplicate['TEXT1'].append('')
                                            df_new_duplicate['STLAL'].append('')
                                            df_new_duplicate['STLAN'].append('')
                                            df_new_duplicate['ZTEXT'].append('')
                                            df_new_duplicate['STKTX'].append('')
                                            df_new_duplicate['BMENG'].append('')
                                            df_new_duplicate['BMEIN'].append('')
                                            df_new_duplicate['STLST'].append('')
                                            df_new_duplicate['POSNR'].append(k+1)
                                            df_new_duplicate['POSTP'].append('L')
                                            
                                            craft_counter+=1
                                            if k == 0 :
                                                df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                                df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                                df_new_duplicate['MEINS'].append('1000')
                                                df_new_duplicate['MENGE'].append('ШТ')
                                                df_new_duplicate['DATUV'].append('')
                                                df_new_duplicate['PUSTOY'].append('')
                                            
                                            if k==1:
                                                df_new_duplicate['MATNR1'].append(siryo_dlya_upakovki1.sap_code_s4q100)
                                                df_new_duplicate['TEXT2'].append(siryo_dlya_upakovki1.название)
                                                df_new_duplicate['MENGE'].append('КГ')
                                                df_new_duplicate['MEINS'].append( ("%.3f" % (float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent)).replace('.',','))
                                                df_new_duplicate['DATUV'].append('')
                                                df_new_duplicate['PUSTOY'].append('')
                                            
                                            
                                            
                                            if k==2:
                                                df_new_duplicate['MATNR1'].append(nakleykaa.sap_code_s4q100)
                                                df_new_duplicate['TEXT2'].append(nakleykaa.название)
                                                df_new_duplicate['MENGE'].append("М2")
                                                df_new_duplicate['MEINS'].append(("%.3f" % ((meinss)*mein_percent)).replace('.',',')) ##XATO
                                                df_new_duplicate['DATUV'].append('')
                                                df_new_duplicate['PUSTOY'].append('')
                                            
                                            df_new_duplicate['LGORT'].append('PS10')

                                    
                            if qatorlar_soni == 5:
                                j += 1
                                df_new_duplicate['ID'].append('1')
                                df_new_duplicate['MATNR'].append(df[i][12])
                                df_new_duplicate['WERKS'].append('1101')
                                df_new_duplicate['TEXT1'].append(df[i][13])
                                df_new_duplicate['STLAL'].append('1')
                                df_new_duplicate['STLAN'].append('1')
                                ztekst = 'Упаковка'
                                df_new_duplicate['ZTEXT'].append(ztekst)
                                df_new_duplicate['STKTX'].append(ztekst)
                                df_new_duplicate['BMENG'].append( '1000')
                                df_new_duplicate['BMEIN'].append('ШТ')
                                df_new_duplicate['STLST'].append('1')
                                df_new_duplicate['POSNR'].append('')
                                df_new_duplicate['POSTP'].append('')
                                df_new_duplicate['MATNR1'].append('')
                                df_new_duplicate['TEXT2'].append('')
                                df_new_duplicate['MEINS'].append('')
                                df_new_duplicate['MENGE'].append('')
                                df_new_duplicate['DATUV'].append('01012021')
                                df_new_duplicate['PUSTOY'].append('')
                                df_new_duplicate['LGORT'].append('')
                                length = df[i][12].split('-')[0]
                                
                                if length in accessuar:
                                    for k in range(0,3):
                                        j+=1
                                        df_new_duplicate['ID'].append('2')
                                        df_new_duplicate['MATNR'].append('')
                                        df_new_duplicate['WERKS'].append('')
                                        df_new_duplicate['TEXT1'].append('')
                                        df_new_duplicate['STLAL'].append('')
                                        df_new_duplicate['STLAN'].append('')
                                        df_new_duplicate['ZTEXT'].append('')
                                        df_new_duplicate['STKTX'].append('')
                                        df_new_duplicate['BMENG'].append('')
                                        df_new_duplicate['BMEIN'].append('')
                                        df_new_duplicate['STLST'].append('')
                                        df_new_duplicate['POSNR'].append(k+1)
                                        df_new_duplicate['POSTP'].append('L')
                                        
                                        craft_counter +=1
                                        if k == 0 :
                                            df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                            df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                            df_new_duplicate['MEINS'].append('1000')
                                            df_new_duplicate['MENGE'].append('ШТ')
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        
                                        
                                        if k==1:
                                            df_new_duplicate['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                            df_new_duplicate['TEXT2'].append(nakleyka_result1.название)
                                            df_new_duplicate['MENGE'].append("М2")
                                            df_new_duplicate['MEINS'].append(("%.3f" % (float(meinss1)*mein_percent)).replace('.',',')) ##XATO
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        
                                        if k==2:
                                            df_new_duplicate['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                                            df_new_duplicate['TEXT2'].append(nakleyka_result2.название)
                                            df_new_duplicate['MENGE'].append("М2")
                                            df_new_duplicate['MEINS'].append(("%.3f" % (float(meinss2)*mein_percent)).replace('.',',')) ##XATO
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        
                                        df_new_duplicate['LGORT'].append('PS10')
                        
                                else:
                                    for k in range(0,qatorlar_soni-1):
                                        j+=1
                                        df_new_duplicate['ID'].append('2')
                                        df_new_duplicate['MATNR'].append('')
                                        df_new_duplicate['WERKS'].append('')
                                        df_new_duplicate['TEXT1'].append('')
                                        df_new_duplicate['STLAL'].append('')
                                        df_new_duplicate['STLAN'].append('')
                                        df_new_duplicate['ZTEXT'].append('')
                                        df_new_duplicate['STKTX'].append('')
                                        df_new_duplicate['BMENG'].append('')
                                        df_new_duplicate['BMEIN'].append('')
                                        df_new_duplicate['STLST'].append('')
                                        df_new_duplicate['POSNR'].append(k+1)
                                        df_new_duplicate['POSTP'].append('L')
                                        craft_counter +=1
                                        
                                        if k == 0 :
                                            df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                            df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                            df_new_duplicate['MEINS'].append('1000')
                                            df_new_duplicate['MENGE'].append('ШТ')
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        
                                        if k==1:
                                            df_new_duplicate['MATNR1'].append(siryo_dlya_upakovki1.sap_code_s4q100)
                                            df_new_duplicate['TEXT2'].append(siryo_dlya_upakovki1.название)
                                            df_new_duplicate['MENGE'].append('КГ')
                                            df_new_duplicate['MEINS'].append( ("%.3f" % (float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent)).replace('.',','))
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        
                                        
                                        
                                        if k==2:
                                            df_new_duplicate['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                            df_new_duplicate['TEXT2'].append(nakleyka_result1.название)
                                            df_new_duplicate['MENGE'].append("М2")
                                            df_new_duplicate['MEINS'].append(("%.3f" % (float(meinss1)*mein_percent)).replace('.',',')) ##XATO
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        
                                        if k==3:
                                            df_new_duplicate['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                                            df_new_duplicate['TEXT2'].append(nakleyka_result2.название)
                                            df_new_duplicate['MENGE'].append("М2")
                                            df_new_duplicate['MEINS'].append(("%.3f" % (float(meinss2)*mein_percent)).replace('.',',')) ##XATO
                                            df_new_duplicate['DATUV'].append('')
                                            df_new_duplicate['PUSTOY'].append('')
                                        
                                        df_new_duplicate['LGORT'].append('PS10')

                        if alum_teks.бумага_расход_упоковочной_ленты_на_1000_штук_кг != '0' :
                            kraft_bumaga =Ximikat.objects.get(id=5)
                            j+=1
                            df_new_duplicate['ID'].append('2')
                            df_new_duplicate['MATNR'].append('')
                            df_new_duplicate['WERKS'].append('')
                            df_new_duplicate['TEXT1'].append('')
                            df_new_duplicate['STLAL'].append('')
                            df_new_duplicate['STLAN'].append('')
                            df_new_duplicate['ZTEXT'].append('')
                            df_new_duplicate['STKTX'].append('')
                            df_new_duplicate['BMENG'].append('')
                            df_new_duplicate['BMEIN'].append('')
                            df_new_duplicate['STLST'].append('')
                            df_new_duplicate['POSNR'].append(craft_counter+1)
                            df_new_duplicate['POSTP'].append('L')
                            df_new_duplicate['MATNR1'].append(kraft_bumaga.sap_code_s4q100)
                            df_new_duplicate['TEXT2'].append(kraft_bumaga.название)
                            df_new_duplicate['MENGE'].append('КГ')
                            df_new_duplicate['MEINS'].append( ("%.3f" % (float(alum_teks.бумага_расход_упоковочной_ленты_на_1000_штук_кг))).replace('.',','))
                            df_new_duplicate['DATUV'].append('')
                            df_new_duplicate['PUSTOY'].append('')
                            df_new_duplicate['LGORT'].append('PS09')

                                
                    else:
                        
                        laminatsiya_code = ddd.split('_')[1].split('/')
                        laminatsiya_code1 = laminatsiya_code[0]
                        laminatsiya_code2 = laminatsiya_code[1]
                        
                        if ((laminatsiya_code1 == laminatsiya_code2) or (laminatsiya_code1 =='XXXX' or laminatsiya_code2 == 'XXXX')):
                            qatorlar_soni +=1
                            
                            if laminatsiya_code1 =='XXXX':
                                meinsL = alum_teks.лам_низ_b_рас_ленты_на_1000_пр_м2
                                laminatsiya =Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code2)[:1].get() 
                            elif laminatsiya_code2 =='XXXX':
                                
                                meinsL = alum_teks.лам_верх_a_рас_ленты_на_1000_пр_м2
                                laminatsiya =Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code1)[:1].get() 
                            elif laminatsiya_code1 == laminatsiya_code2:
                                meinsL = float(alum_teks.лам_верх_a_рас_ленты_на_1000_пр_м2)+float(alum_teks.лам_низ_b_рас_ленты_на_1000_пр_м2)
                                
                                laminatsiya =Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code1)[:1].get() 
                            print('shuyerdaadad lam 1')
                        else:
                            print('shuyerdaadad lam 2')
                            if qatorlar_soni == 5:
                                qatorlar_soni += 4
                            else:
                                qatorlar_soni +=2

                            laminatsiya_result1 = Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code1)[:1].get() 
                            laminatsiya_result2 = Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code2)[:1].get() 
                            meinsL1 = float(alum_teks.лам_верх_a_рас_ленты_на_1000_пр_м2)
                            meinsL2 = float(alum_teks.лам_низ_b_рас_ленты_на_1000_пр_м2)
                            
                        
                        if qatorlar_soni == 5:
                            j+=1
                            df_new_duplicate['ID'].append('1')
                            df_new_duplicate['MATNR'].append(df[i][12])
                            df_new_duplicate['WERKS'].append('1101')
                            df_new_duplicate['TEXT1'].append(df[i][13])
                            df_new_duplicate['STLAL'].append('1')
                            df_new_duplicate['STLAN'].append('1')
                            ztekst = 'Ламинация + Наклейка + Упаковка'
                            df_new_duplicate['ZTEXT'].append(ztekst)
                            df_new_duplicate['STKTX'].append(ztekst)
                            df_new_duplicate['BMENG'].append( '1000')
                            df_new_duplicate['BMEIN'].append('ШТ')
                            df_new_duplicate['STLST'].append('1')
                            df_new_duplicate['POSNR'].append('')
                            df_new_duplicate['POSTP'].append('')
                            df_new_duplicate['MATNR1'].append('')
                            df_new_duplicate['TEXT2'].append('')
                            df_new_duplicate['MEINS'].append('')
                            df_new_duplicate['MENGE'].append('')
                            df_new_duplicate['DATUV'].append('01012021')
                            df_new_duplicate['PUSTOY'].append('')
                            df_new_duplicate['LGORT'].append('')
                            length = df[i][12].split('-')[0]
                            for k in range(0,qatorlar_soni):
                                j+=1
                                df_new_duplicate['ID'].append('2')
                                df_new_duplicate['MATNR'].append('')
                                df_new_duplicate['WERKS'].append('')
                                df_new_duplicate['TEXT1'].append('')
                                df_new_duplicate['STLAL'].append('')
                                df_new_duplicate['STLAN'].append('')
                                df_new_duplicate['ZTEXT'].append('')
                                df_new_duplicate['STKTX'].append('')
                                df_new_duplicate['BMENG'].append('')
                                df_new_duplicate['BMEIN'].append('')
                                df_new_duplicate['STLST'].append('')
                                df_new_duplicate['POSNR'].append(k+1)
                                df_new_duplicate['POSTP'].append('L')
                                craft_counter+=1
                                
                                if k == 0 :
                                    df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                    df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                    df_new_duplicate['MEINS'].append('1000')
                                    df_new_duplicate['MENGE'].append('ШТ')
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new_duplicate['MATNR1'].append(kleydlyalamp1.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(kleydlyalamp1.название)
                                    df_new_duplicate['MENGE'].append('КГ')
                                    df_new_duplicate['MEINS'].append( ("%.3f" % (float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent)).replace('.',','))
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                if k==2:
                                    df_new_duplicate['MATNR1'].append(kleydlyalamp2.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(kleydlyalamp2.название)
                                    df_new_duplicate['MENGE'].append("КГ")
                                    df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent)).replace('.',',')) ##XATO
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                if k==3:
                                    df_new_duplicate['MATNR1'].append(kleydlyalamp3.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(kleydlyalamp3.название)
                                    df_new_duplicate['MENGE'].append("КГ")
                                    df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent)).replace('.',',')) ##XATO
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                if k==4:
                                    df_new_duplicate['MATNR1'].append(laminatsiya.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(laminatsiya.название)
                                    df_new_duplicate['MENGE'].append("М2")
                                    df_new_duplicate['MEINS'].append(("%.3f" % (float(meinsL)*mein_percent)).replace('.',',')) ##XATO
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                
                                df_new_duplicate['LGORT'].append('PS11')
                        
                        
                        if qatorlar_soni == 6:
                           
                            jjj =0
                            for nakleykaa in nakleyka_results:
                                jjj += 1
                                j+=1
                                df_new_duplicate['ID'].append('1')
                                df_new_duplicate['MATNR'].append(df[i][12])
                                df_new_duplicate['WERKS'].append('1101')
                                df_new_duplicate['TEXT1'].append(df[i][13])
                                df_new_duplicate['STLAL'].append(f'{jjj}')
                                df_new_duplicate['STLAN'].append('1')
                                ztekst = 'Ламинация + Наклейка + Упаковка'
                                df_new_duplicate['ZTEXT'].append(ztekst)
                                df_new_duplicate['STKTX'].append(ztekst)
                                df_new_duplicate['BMENG'].append( '1000')
                                df_new_duplicate['BMEIN'].append('ШТ')
                                df_new_duplicate['STLST'].append('1')
                                df_new_duplicate['POSNR'].append('')
                                df_new_duplicate['POSTP'].append('')
                                df_new_duplicate['MATNR1'].append('')
                                df_new_duplicate['TEXT2'].append('')
                                df_new_duplicate['MEINS'].append('')
                                df_new_duplicate['MENGE'].append('')
                                df_new_duplicate['DATUV'].append('01012021')
                                df_new_duplicate['PUSTOY'].append('')
                                df_new_duplicate['LGORT'].append('')
                                length = df[i][12].split('-')[0]
                                for k in range(0,qatorlar_soni):
                                    j+=1
                                    df_new_duplicate['ID'].append('2')
                                    df_new_duplicate['MATNR'].append('')
                                    df_new_duplicate['WERKS'].append('')
                                    df_new_duplicate['TEXT1'].append('')
                                    df_new_duplicate['STLAL'].append('')
                                    df_new_duplicate['STLAN'].append('')
                                    df_new_duplicate['ZTEXT'].append('')
                                    df_new_duplicate['STKTX'].append('')
                                    df_new_duplicate['BMENG'].append('')
                                    df_new_duplicate['BMEIN'].append('')
                                    df_new_duplicate['STLST'].append('')
                                    df_new_duplicate['POSNR'].append(k+1)
                                    df_new_duplicate['POSTP'].append('L')
                                    craft_counter+=1
                                    
                                    if k == 0 :
                                        df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                        df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                        df_new_duplicate['MEINS'].append('1000')
                                        df_new_duplicate['MENGE'].append('ШТ')
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    
                                    if k==1:
                                        df_new_duplicate['MATNR1'].append(kleydlyalamp1.sap_code_s4q100)
                                        df_new_duplicate['TEXT2'].append(kleydlyalamp1.название)
                                        df_new_duplicate['MENGE'].append('КГ')
                                        df_new_duplicate['MEINS'].append( ("%.3f" % (float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent)).replace('.',','))
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    
                                    if k==2:
                                        df_new_duplicate['MATNR1'].append(kleydlyalamp2.sap_code_s4q100)
                                        df_new_duplicate['TEXT2'].append(kleydlyalamp2.название)
                                        df_new_duplicate['MENGE'].append("КГ")
                                        df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent)).replace('.',',')) ##XATO
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    
                                    if k==3:
                                        df_new_duplicate['MATNR1'].append(kleydlyalamp3.sap_code_s4q100)
                                        df_new_duplicate['TEXT2'].append(kleydlyalamp3.название)
                                        df_new_duplicate['MENGE'].append("КГ")
                                        df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent)).replace('.',',')) ##XATO
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    
                                    if k==4:
                                        
                                        df_new_duplicate['MATNR1'].append(nakleykaa.sap_code_s4q100)
                                        df_new_duplicate['TEXT2'].append(nakleykaa.название)
                                        df_new_duplicate['MENGE'].append("М2")
                                        df_new_duplicate['MEINS'].append(("%.3f" % ((meinss*mein_percent))).replace('.',',')) ##XATO
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    
                                    if k==5:
                                        
                                        df_new_duplicate['MATNR1'].append(laminatsiya.sap_code_s4q100)
                                        df_new_duplicate['TEXT2'].append(laminatsiya.название)
                                        df_new_duplicate['MENGE'].append("М2")
                                        df_new_duplicate['MEINS'].append(("%.3f" % (float(meinsL)*mein_percent)).replace('.',',')) ##XATO
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    
                                    
                                    df_new_duplicate['LGORT'].append('PS11')
                    
                        if qatorlar_soni == 7:
                            print('sdfsdsdsd  ',df[i][12],df[i][13])
                            j+=1
                            df_new_duplicate['ID'].append('1')
                            df_new_duplicate['MATNR'].append(df[i][12])
                            df_new_duplicate['WERKS'].append('1101')
                            df_new_duplicate['TEXT1'].append(df[i][13])
                            df_new_duplicate['STLAL'].append(f'1')
                            df_new_duplicate['STLAN'].append('1')
                            ztekst = 'Ламинация + Наклейка + Упаковка'
                            df_new_duplicate['ZTEXT'].append(ztekst)
                            df_new_duplicate['STKTX'].append(ztekst)
                            df_new_duplicate['BMENG'].append( '1000')
                            df_new_duplicate['BMEIN'].append('ШТ')
                            df_new_duplicate['STLST'].append('1')
                            df_new_duplicate['POSNR'].append('')
                            df_new_duplicate['POSTP'].append('')
                            df_new_duplicate['MATNR1'].append('')
                            df_new_duplicate['TEXT2'].append('')
                            df_new_duplicate['MEINS'].append('')
                            df_new_duplicate['MENGE'].append('')
                            df_new_duplicate['DATUV'].append('01012021')
                            df_new_duplicate['PUSTOY'].append('')
                            df_new_duplicate['LGORT'].append('')
                            length = df[i][12].split('-')[0]
                            for k in range(0,qatorlar_soni):
                                j+=1
                                df_new_duplicate['ID'].append('2')
                                df_new_duplicate['MATNR'].append('')
                                df_new_duplicate['WERKS'].append('')
                                df_new_duplicate['TEXT1'].append('')
                                df_new_duplicate['STLAL'].append('')
                                df_new_duplicate['STLAN'].append('')
                                df_new_duplicate['ZTEXT'].append('')
                                df_new_duplicate['STKTX'].append('')
                                df_new_duplicate['BMENG'].append('')
                                df_new_duplicate['BMEIN'].append('')
                                df_new_duplicate['STLST'].append('')
                                df_new_duplicate['POSNR'].append(k+1)
                                df_new_duplicate['POSTP'].append('L')
                                craft_counter+=1
                                
                                if k == 0 :
                                    df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                    df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                    df_new_duplicate['MEINS'].append('1000')
                                    df_new_duplicate['MENGE'].append('ШТ')
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new_duplicate['MATNR1'].append(kleydlyalamp1.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(kleydlyalamp1.название)
                                    df_new_duplicate['MENGE'].append('КГ')
                                    df_new_duplicate['MEINS'].append( ("%.3f" % (float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent)).replace('.',','))
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                if k==2:
                                    df_new_duplicate['MATNR1'].append(kleydlyalamp2.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(kleydlyalamp2.название)
                                    df_new_duplicate['MENGE'].append("КГ")
                                    df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent)).replace('.',',')) ##XATO
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                if k==3:
                                    df_new_duplicate['MATNR1'].append(kleydlyalamp3.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(kleydlyalamp3.название)
                                    df_new_duplicate['MENGE'].append("КГ")
                                    df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent)).replace('.',',')) ##XATO
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                if k==4:
                                    df_new_duplicate['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(nakleyka_result1.название)
                                    df_new_duplicate['MENGE'].append("М2")
                                    df_new_duplicate['MEINS'].append(("%.3f" % (float(meinss1)*mein_percent)).replace('.',',')) ##XATO
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                if k==5:
                                    df_new_duplicate['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(nakleyka_result2.название)
                                    df_new_duplicate['MENGE'].append("М2")
                                    df_new_duplicate['MEINS'].append(("%.3f" % (float(meinss2)*mein_percent)).replace('.',',')) ##XATO
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                if k==6:
                                    
                                    df_new_duplicate['MATNR1'].append(laminatsiya.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(laminatsiya.название)
                                    df_new_duplicate['MENGE'].append("М2")
                                    df_new_duplicate['MEINS'].append(("%.3f" % (float(meinsL)*mein_percent)).replace('.',',')) ##XATO
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                
                                df_new_duplicate['LGORT'].append('PS11')
                    
                        if qatorlar_soni == 8:
                            j += 1
                            df_new_duplicate['ID'].append('1')
                            df_new_duplicate['MATNR'].append(df[i][12])
                            df_new_duplicate['WERKS'].append('1101')
                            df_new_duplicate['TEXT1'].append(df[i][13])
                            df_new_duplicate['STLAL'].append('1')
                            df_new_duplicate['STLAN'].append('1')
                            ztekst = 'Ламинация + Наклейка + Упаковка'
                            df_new_duplicate['ZTEXT'].append(ztekst)
                            df_new_duplicate['STKTX'].append(ztekst)
                            df_new_duplicate['BMENG'].append( '1000')
                            df_new_duplicate['BMEIN'].append('ШТ')
                            df_new_duplicate['STLST'].append('1')
                            df_new_duplicate['POSNR'].append('')
                            df_new_duplicate['POSTP'].append('')
                            df_new_duplicate['MATNR1'].append('')
                            df_new_duplicate['TEXT2'].append('')
                            df_new_duplicate['MEINS'].append('')
                            df_new_duplicate['MENGE'].append('')
                            df_new_duplicate['DATUV'].append('01012021')
                            df_new_duplicate['PUSTOY'].append('')
                            df_new_duplicate['LGORT'].append('')
                            length = df[i][12].split('-')[0]
                            for k in range(0,qatorlar_soni):
                                j+=1
                                df_new_duplicate['ID'].append('2')
                                df_new_duplicate['MATNR'].append('')
                                df_new_duplicate['WERKS'].append('')
                                df_new_duplicate['TEXT1'].append('')
                                df_new_duplicate['STLAL'].append('')
                                df_new_duplicate['STLAN'].append('')
                                df_new_duplicate['ZTEXT'].append('')
                                df_new_duplicate['STKTX'].append('')
                                df_new_duplicate['BMENG'].append('')
                                df_new_duplicate['BMEIN'].append('')
                                df_new_duplicate['STLST'].append('')
                                df_new_duplicate['POSNR'].append(k+1)
                                df_new_duplicate['POSTP'].append('L')
                                craft_counter+=1
                                
                                if k == 0 :
                                    df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                    df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                    df_new_duplicate['MEINS'].append('1000')
                                    df_new_duplicate['MENGE'].append('ШТ')
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new_duplicate['MATNR1'].append(kleydlyalamp1.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(kleydlyalamp1.название)
                                    df_new_duplicate['MENGE'].append('КГ')
                                    df_new_duplicate['MEINS'].append( ("%.3f" % (float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent)).replace('.',','))
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                if k==2:
                                    df_new_duplicate['MATNR1'].append(kleydlyalamp2.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(kleydlyalamp2.название)
                                    df_new_duplicate['MENGE'].append("КГ")
                                    df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent)).replace('.',',')) ##XATO
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                if k==3:
                                    df_new_duplicate['MATNR1'].append(kleydlyalamp3.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(kleydlyalamp3.название)
                                    df_new_duplicate['MENGE'].append("КГ")
                                    df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent)).replace('.',',')) ##XATO
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                if k==4:
                                    df_new_duplicate['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(nakleyka_result1.название)
                                    df_new_duplicate['MENGE'].append("М2")
                                    df_new_duplicate['MEINS'].append(("%.3f" % (float(meinss1)*mein_percent)).replace('.',',')) ##XATO
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                if k==5:
                                    df_new_duplicate['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(nakleyka_result2.название)
                                    df_new_duplicate['MENGE'].append("М2")
                                    df_new_duplicate['MEINS'].append(("%.3f" % (float(meinss1)*mein_percent)).replace('.',',')) ##XATO
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                if k == 6:
                                    df_new_duplicate['MATNR1'].append(laminatsiya_result1.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(laminatsiya_result1.название)
                                    df_new_duplicate['MENGE'].append("М2")
                                    df_new_duplicate['MEINS'].append(("%.3f" % (float(meinsL1)*mein_percent)).replace('.',',')) ##XATO
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                if k == 7:
                                    df_new_duplicate['MATNR1'].append(laminatsiya_result2.sap_code_s4q100)
                                    df_new_duplicate['TEXT2'].append(laminatsiya_result2.название)
                                    df_new_duplicate['MENGE'].append("М2")
                                    df_new_duplicate['MEINS'].append(("%.3f" % (float(meinsL2)*mein_percent)).replace('.',',')) ##XATO
                                    df_new_duplicate['DATUV'].append('')
                                    df_new_duplicate['PUSTOY'].append('')
                                
                                df_new_duplicate['LGORT'].append('PS11')

                        
                        if qatorlar_soni == 9:
                            for nakleykaa in nakleyka_results:
                                j += 1
                                df_new_duplicate['ID'].append('1')
                                df_new_duplicate['MATNR'].append(df[i][12])
                                df_new_duplicate['WERKS'].append('1101')
                                df_new_duplicate['TEXT1'].append(df[i][13])
                                df_new_duplicate['STLAL'].append('1')
                                df_new_duplicate['STLAN'].append('1')
                                ztekst = 'Ламинация + Наклейка + Упаковка'
                                df_new_duplicate['ZTEXT'].append(ztekst)
                                df_new_duplicate['STKTX'].append(ztekst)
                                df_new_duplicate['BMENG'].append( '1000')
                                df_new_duplicate['BMEIN'].append('ШТ')
                                df_new_duplicate['STLST'].append('1')
                                df_new_duplicate['POSNR'].append('')
                                df_new_duplicate['POSTP'].append('')
                                df_new_duplicate['MATNR1'].append('')
                                df_new_duplicate['TEXT2'].append('')
                                df_new_duplicate['MEINS'].append('')
                                df_new_duplicate['MENGE'].append('')
                                df_new_duplicate['DATUV'].append('01012021')
                                df_new_duplicate['PUSTOY'].append('')
                                df_new_duplicate['LGORT'].append('')
                                length = df[i][12].split('-')[0]
                                for k in range(0,qatorlar_soni):
                                    j+=1
                                    df_new_duplicate['ID'].append('2')
                                    df_new_duplicate['MATNR'].append('')
                                    df_new_duplicate['WERKS'].append('')
                                    df_new_duplicate['TEXT1'].append('')
                                    df_new_duplicate['STLAL'].append('')
                                    df_new_duplicate['STLAN'].append('')
                                    df_new_duplicate['ZTEXT'].append('')
                                    df_new_duplicate['STKTX'].append('')
                                    df_new_duplicate['BMENG'].append('')
                                    df_new_duplicate['BMEIN'].append('')
                                    df_new_duplicate['STLST'].append('')
                                    df_new_duplicate['POSNR'].append(k+1)
                                    df_new_duplicate['POSTP'].append('L')
                                    craft_counter+=1
                                    
                                    if k == 0 :
                                        df_new_duplicate['MATNR1'].append(older_process['sapcode'])
                                        df_new_duplicate['TEXT2'].append(older_process['kratkiy'])
                                        df_new_duplicate['MEINS'].append('1000')
                                        df_new_duplicate['MENGE'].append('ШТ')
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    
                                    if k==1:
                                        df_new_duplicate['MATNR1'].append(kleydlyalamp1.sap_code_s4q100)
                                        df_new_duplicate['TEXT2'].append(kleydlyalamp1.название)
                                        df_new_duplicate['MENGE'].append('КГ')
                                        df_new_duplicate['MEINS'].append( ("%.3f" % (float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent)).replace('.',','))
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    
                                    if k==2:
                                        df_new_duplicate['MATNR1'].append(kleydlyalamp2.sap_code_s4q100)
                                        df_new_duplicate['TEXT2'].append(kleydlyalamp2.название)
                                        df_new_duplicate['MENGE'].append("КГ")
                                        df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent)).replace('.',',')) ##XATO
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    
                                    if k==3:
                                        df_new_duplicate['MATNR1'].append(kleydlyalamp3.sap_code_s4q100)
                                        df_new_duplicate['TEXT2'].append(kleydlyalamp3.название)
                                        df_new_duplicate['MENGE'].append("КГ")
                                        df_new_duplicate['MEINS'].append(("%.3f" % (float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent)).replace('.',',')) ##XATO
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    
                                    if k==4:
                                        df_new_duplicate['MATNR1'].append(nakleykaa.sap_code_s4q100)
                                        df_new_duplicate['TEXT2'].append(nakleykaa.название)
                                        df_new_duplicate['MENGE'].append("М2")
                                        df_new_duplicate['MEINS'].append(("%.3f" % (float(meinss)*mein_percent)).replace('.',',')) ##XATO
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    if k == 6:
                                        df_new_duplicate['MATNR1'].append(laminatsiya_result1.sap_code_s4q100)
                                        df_new_duplicate['TEXT2'].append(laminatsiya_result1.название)
                                        df_new_duplicate['MENGE'].append("М2")
                                        df_new_duplicate['MEINS'].append(("%.3f" % (float(meinsL1)*mein_percent)).replace('.',',')) ##XATO
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    if k == 7:
                                        df_new_duplicate['MATNR1'].append(laminatsiya_result2.sap_code_s4q100)
                                        df_new_duplicate['TEXT2'].append(laminatsiya_result2.название)
                                        df_new_duplicate['MENGE'].append("М2")
                                        df_new_duplicate['MEINS'].append(("%.3f" % (float(meinsL2)*mein_percent)).replace('.',',')) ##XATO
                                        df_new_duplicate['DATUV'].append('')
                                        df_new_duplicate['PUSTOY'].append('')
                                    
                                    df_new_duplicate['LGORT'].append('PS11')

                        
                        
                        if alum_teks.бумага_расход_упоковочной_ленты_на_1000_штук_кг != '0' :
                            kraft_bumaga =Ximikat.objects.get(id=5)
                            j+=1
                            df_new_duplicate['ID'].append('2')
                            df_new_duplicate['MATNR'].append('')
                            df_new_duplicate['WERKS'].append('')
                            df_new_duplicate['TEXT1'].append('')
                            df_new_duplicate['STLAL'].append('')
                            df_new_duplicate['STLAN'].append('')
                            df_new_duplicate['ZTEXT'].append('')
                            df_new_duplicate['STKTX'].append('')
                            df_new_duplicate['BMENG'].append('')
                            df_new_duplicate['BMEIN'].append('')
                            df_new_duplicate['STLST'].append('')
                            df_new_duplicate['POSNR'].append(craft_counter+1)
                            df_new_duplicate['POSTP'].append('L')
                            df_new_duplicate['MATNR1'].append(kraft_bumaga.sap_code_s4q100)
                            df_new_duplicate['TEXT2'].append(kraft_bumaga.название)
                            df_new_duplicate['MENGE'].append('КГ')
                            df_new_duplicate['MEINS'].append( ("%.3f" % (float(alum_teks.бумага_расход_упоковочной_ленты_на_1000_штук_кг))).replace('.',','))
                            df_new_duplicate['DATUV'].append('')
                            df_new_duplicate['PUSTOY'].append('')
                            df_new_duplicate['LGORT'].append('PS11')
                    
                older_process['sapcode'] =df[i][12]
                older_process['kratkiy'] =df[i][13]
                
        
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%d-%B-%Y %H-%M")    
                 
            
    create_folder(f'{MEDIA_ROOT}\\uploads','norma')
    create_folder(f'{MEDIA_ROOT}\\uploads\\norma',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\norma\\{year}',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\norma\\{year}\\{month}',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\norma\\{year}\\{month}\\{day}',hour)
            
            
    
    path =f'{MEDIA_ROOT}\\uploads\\norma\\{year}\\{month}\\{day}\\{hour}\\NORMA-{minut}-{product_type}.xlsx'
    

    meins7 = []
    
    for mein in df_new['MEINS']:
        mein_txt = str(mein)
        if mein_txt[-4:] ==',000':
            meins7.append(mein_txt.replace(',000',''))
        else:
            meins7.append(mein_txt)
    df_new['MEINS'] =meins7
    
    meins7d = []
    
    for mein in df_new_duplicate['MEINS']:
        mein_txt = str(mein)
        if mein_txt[-4:] ==',000':
            meins7d.append(mein_txt.replace(',000',''))
        else:
            meins7d.append(mein_txt)
    df_new_duplicate['MEINS'] =meins7d

   

    dff =pd.DataFrame(df_new)
    


    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    dff.to_excel(writer,index=False,sheet_name ='Norma')
    try:
        dff_duplicate =pd.DataFrame(df_new_duplicate)
        dff_duplicate.to_excel(writer,index=False,sheet_name ='EXISTS')
    except:
        pass
    
    writer.close()

    order_id = request.GET.get('order_id',None)

    if order_id:
        context2 ={}
        order = Order.objects.get(id = order_id)
        paths = order.paths 
        norma_org_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        paths['status_norma_lack']= 'done'
        paths['status_norma']= 'done'
        paths['norma_file_ready'] = path
        paths['norma_org_created_at'] = norma_org_created_at
        paths['tex_link'] ='/texcart/texcarta/' + str(paths['texid']) + '?order_id=' +str(order.id)
        order.norma_wrongs = request.user
        order.current_worker =request.user
        order.work_type = 8
        order.save()
        context2['order'] = order
        paths =  order.paths
        for key,val in paths.items():
            context2[key] = val
        return render(request,'order/order_detail.html',context2)
    
    # path =os.path.join(os.path.expanduser("~/Desktop"),'new_base_cominirovaniy.xlsx')
    file =[File(file=path,filetype='obichniy')]
    context = {
            'files':file,
            'section':f'Формированый {file_content} файл'
      }
    return render(request,'universal/generated_files.html',context)
  
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def generatenewexceldata(request):
    path1 =os.path.join(os.path.expanduser("~/Desktop/generate"),'data.xlsx')
    df0 = pd.read_excel(path1,'baza1')
    
    df =excelgenerate(df0)
    path2 =os.path.join(os.path.expanduser("~/Desktop/generate"),'generated_data.xlsx')
    df.to_excel(path2)
    
    return JsonResponse({'File':'Genarated!!'})

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def remove_whitespace(request):
    normas = Norma.objects.all()
    
    for norma in normas:
        print(norma.id)
        norma.компонент_1 = norma.компонент_1.strip()
        norma.компонент_2 = norma.компонент_2.strip()
        norma.компонент_3 = norma.компонент_3.strip()
        norma.артикул = norma.артикул.strip()
        norma.save()
        
    return JsonResponse({'a':'b'})


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def nakleyka_duplicate_del(request):
    nakleykas = Nakleyka.objects.all()
      
    for nakleyka in nakleykas:
        nak =Nakleyka.objects.filter(код_наклейки =nakleyka.код_наклейки,ширина=nakleyka.ширина)
        if len(nak)>1:
            i=1
            for n in nak:
                if i ==1:
                    i+=1
                    continue
                n.delete()
                i+=1
              
    return JsonResponse({'a':'b'})


def norma_for_list():
        normas = Norma.objects.all().values("компонент_1","компонент_2","компонент_3","артикул")
        normass =[]
        for norm in normas:
            if ((norm['компонент_1'] !='0') and (norm['компонент_1']!='nan')):
                    normass.append(norm['компонент_1'])
            if ((norm['компонент_2'] !='0') and (norm['компонент_2']!='nan')):
                    normass.append(norm['компонент_2'])
            if ((norm['компонент_3'] !='0') and (norm['компонент_3']!='nan')):
                    normass.append(norm['компонент_3'])
            if ((norm['артикул'] !='0') and (norm['артикул']!='nan')):
                    normass.append(norm['артикул'])
        
        kraskas = Kraska.objects.all().values_list('код_краски',flat=True)
        accessuar = Accessuar.objects.all().values_list('sap_code',flat=True)
        nak_norma1 = Norma.objects.filter(наклейка_исключение ='1',артикул='0').values_list('компонент_1',flat=True)
        nak_norma2 = Norma.objects.filter(Q(наклейка_исключение ='1') & ~Q(артикул='0')).values_list('артикул',flat=True)
        nakleyka = list(nak_norma1) + list(nak_norma2)

        zakalka = ZakalkaIskyuchenie.objects.all().values_list('sap_code',flat=True)
        zakalka_iskyucheniye1 = Norma.objects.filter(закалка_исключение ='1').values_list('артикул',flat=True)
        zakalka_iskyucheniye2 = Norma.objects.filter(закалка_исключение ='1').values_list('компонент_1',flat=True)
        zakalka_6064 =list(zakalka_iskyucheniye1) + list(zakalka_iskyucheniye2)
        
        return normass,kraskas,accessuar,nakleyka,zakalka,zakalka_6064


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def norma_update(request):
    normalar = Norma.objects.all()[:50]
    return render(request,'norma/norma_crud/update.html',{'normas':normalar})

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def norma_delete(request):
    if request.method =='POST':
        ozmk =request.POST.get('ozmk',None)
        if ozmk:
            ozmks =ozmk.split()
            norma_base = CheckNormaBase.objects.filter(artikul__in =ozmks)
            norma_base.delete()
            messages.add_message(request, messages.INFO, "Normalar arxividan ochirildi")
        return render(request,'norma/norma_find.html')
    else:
        return render(request,'norma/norma_find.html')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1']) 
def find_characteristics(request):
    all_data = [ [] for i in range(38)]
    does_not_exists = []
    if request.method =='POST':
        ozmk =request.POST.get('ozmk',None)
        if ozmk:
            ozmks = ozmk.split()
            for ozm in ozmks:
                if Characteristika.objects.filter(sap_code =ozm).exists():
                    character = Characteristika.objects.filter(sap_code = ozm).order_by('-created_at')[:1].get()
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
                    all_data[34].append(character.tnved.replace('.0',''))
                    all_data[35].append(character.surface_treatment_export)
                    all_data[36].append(character.wms_width.replace('.0',''))
                    all_data[37].append(character.wms_height.replace('.0',''))
         
                else:
                    does_not_exists.append(ozm)
          
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
                    'WMS_HEIGHT': all_data[37]
                    }
            now = datetime.now()
            day =now.strftime("%Y%B%a%d")
            hour =now.strftime("%H HOUR")
            minut =now.strftime("%H-SOAT %M-MINUT %S- SECUND")
            create_folder(f'{MEDIA_ROOT}\\uploads','characteristika')
            create_folder(f'{MEDIA_ROOT}\\uploads\\characteristika',f'{day}')
            create_folder(f'{MEDIA_ROOT}\\uploads\\characteristika\\{day}',f'{minut}')
            path =f'{MEDIA_ROOT}\\uploads\\characteristika\\{day}\\{minut}\\characteristika.xlsx'
            df_charakter = pd.DataFrame(df_new)
            df_charakter_sap = pd.DataFrame({'SAP CODE':does_not_exists})
            df_charakter =df_charakter.replace('nan','')
            writer = pd.ExcelWriter(path, engine='xlsxwriter')
            df_charakter.to_excel(writer,index=False,sheet_name ='Characteristika')
            df_charakter_sap.to_excel(writer,index=False,sheet_name ='DOES NOT EXISTS')
            writer.close()
            messages.add_message(request, messages.INFO, "Characteristika yaratildi")
        return render(request,'norma/find_characteristics.html')
    else:
        return render(request,'norma/find_characteristics.html')

@login_required(login_url='/accounts/login/') 
@allowed_users(allowed_roles=['admin','moderator','user1']) 
def find_characteristics_org(request):
    all_data = [ [] for i in range(38)]
    does_not_exists = []
    if request.method =='POST':
        ozmk =request.POST.get('ozmk',None)
        if ozmk:
            ozmks = ozmk.split()
            for ozm in ozmks:
                if Characteristika.objects.filter(sap_code =ozm).exists():
                    character = Characteristika.objects.filter(sap_code = ozm).order_by('-created_at')[:1].get()
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
                    all_data[34].append(character.tnved.replace('.0',''))
                    all_data[35].append(character.surface_treatment_export)
                    all_data[36].append(character.wms_width.replace('.0',''))
                    all_data[37].append(character.wms_height.replace('.0',''))
         
                else:
                    does_not_exists.append(ozm)
          
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
                    'WMS_HEIGHT': all_data[37]
                    }
            now = datetime.now()
            day =now.strftime("%Y%B%a%d")
            hour =now.strftime("%H HOUR")
            minut =now.strftime("%H-SOAT %M-MINUT %S- SECUND")
            create_folder(f'{MEDIA_ROOT}\\uploads','characteristika')
            create_folder(f'{MEDIA_ROOT}\\uploads\\characteristika',f'{day}')
            create_folder(f'{MEDIA_ROOT}\\uploads\\characteristika\\{day}',f'{minut}')
            path =f'{MEDIA_ROOT}\\uploads\\characteristika\\{day}\\{minut}\\characteristika.xlsx'
            df_charakter = pd.DataFrame(df_new)
            df_charakter_sap = pd.DataFrame({'SAP CODE':does_not_exists})
            df_charakter =df_charakter.replace('nan','')
            writer = pd.ExcelWriter(path, engine='xlsxwriter')
            df_charakter.to_excel(writer,index=False,sheet_name ='Characteristika')
            df_charakter_sap.to_excel(writer,index=False,sheet_name ='DOES NOT EXISTS')
            writer.close()
            files =[File(file=path,filetype='obichniy'),]
            context ={
                'files':files,
                'section':'Найденные характеристики'
            }
        return render(request,'universal/generated_files.html',context)
    else:
        return render(request,'norma/character_find.html',{'section':'Характеристики','section2':'Найти Характеристики'})

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1']) 
def norma_delete_org(request):
    if request.method =='POST':
        ozmk =request.POST.get('ozmk',None)
        if ozmk:
            ozmks =ozmk.split()
            norma_base = CheckNormaBase.objects.filter(artikul__in =ozmks)
            norma_base.delete()
            # messages.add_message(request, messages, "Normalar arxividan ochirildi")
        return render(request,'delete_/delete_norm.html')
    else:
        return render(request,'delete_/delete_norm.html')
  