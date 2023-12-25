from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse
import pandas as pd
import numpy as np
from django.http import JsonResponse
from .models import AlyuminniysilindrEkstruziya1,SubDekorPlonka,Skotch,Ximikat,Kraska,Norma,Anod,Nakleyka,Termomost,TexcartaBase
from norma.models import NormaExcelFiles,CheckNormaBase,Accessuar,ZakalkaIskyuchenie,ViFiles
from .forms import NormaFileForm,NormaEditForm,ViFileForm,TexcartaEditForm,KraskaAddForm,NakleykaAddForm,SublimationAddForm,AnodForm
from django.db.models import Q
from aluminiytermo.models import Characteristika,CharacteristicTitle
from config.settings import MEDIA_ROOT,BASE_DIR
from .utils import excelgenerate,create_csv_file,create_folder
import os
from .BAZA import *
from django.db.models.functions import Cast
from django.db.models import IntegerField
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
import ast
import math

class File:
      def __init__(self,file,filetype,id):
            self.file =file
            self.filetype =filetype
            self.id = id

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


def download(request):
  file_path = request.GET.get('file_path',None)
  if file_path:
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
  raise Http404


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
        
    
def vi_file(request):
    files = ViFiles.objects.all().order_by('-created_at')
    context ={
        'files':files,
        'section':'Формирование ВИ файла',
        'link':'/norma/vi-generate/',
        'type':'ВИ'
        }
    return render(request,'universal/file_list.html',context)


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
def delete_norm(request, id):
    norma = Norma.objects.get(id= id)
    norma.delete()
    return JsonResponse({'msg':True,'text':'Deleted successfully'})

@csrf_exempt
def norma_delete_all(request):
    norma = Norma.objects.all()
    norma.delete()
    return JsonResponse({'msg':True})

@csrf_exempt
def termomost_delete_all(request):
    termomost = Termomost.objects.all()
    termomost.delete()
    return JsonResponse({'msg':True})

@csrf_exempt
def ximikat_save(request):
    data = dict(request.POST)
    for key,val in data.items():
        values = ast.literal_eval(key)
        break
    for val in values:
        ximikat = Ximikat.objects.get(id =int(val[0]))
        ximikat.chemetal7400 = int(val[1])
        ximikat.alufinish = int(val[2])
        ximikat.chemetal7406 = int(val[3])
        ximikat.save()
    
    return JsonResponse({'msg':True})

def ximikat(request):
    ximikats = Ximikat.objects.all().order_by('id')
    context = {
        'ximikats':ximikats,
        'ids':[xim.id for xim in ximikats]
    } 
    return render(request,'norma/benkam/ximikat.html',context)

def add_kraska(request):

    if request.method == 'POST':
        form = KraskaAddForm(data=request.POST)
        if form.is_valid():
                form.save()
                return redirect('kraska_list')
    else:
        form = KraskaAddForm()

    context =  {
        'form':form
    }
    return render(request,'norma/add_kraska.html',context)

def anod_list(request):

    anods = Anod.objects.all()
    context =  {
        'anods':anods
    }
    return render(request,'norma/benkam/anod_list.html',context)

def nakleyka_list(request):

    nakleyka = Nakleyka.objects.all().order_by('-created_at')
    context =  {
        'nakleyka':nakleyka
    }
    return render(request,'norma/benkam/nakleyka_list.html',context)

def sublimatsiya_list(request):

    sumlimatsiya = SubDekorPlonka.objects.all().order_by('-created_at')
    context =  {
        'sumlimatsiya':sumlimatsiya
    }
    return render(request,'norma/benkam/sumlimatsiya_list.html',context)

def kraska_list(request):

    kraska = Kraska.objects.all().order_by('-created_at')
    context =  {
        'kraska':kraska
    }
    return render(request,'norma/benkam/kraska_list.html',context)

def add_anod(request):

    if request.method == 'POST':
        form = AnodForm(data=request.POST)
        if form.is_valid():
                form.save()
                return redirect('anod_list')
    else:
        form = AnodForm()

    context =  {
        'form':form
    }
    return render(request,'norma/benkam/add_anod.html',context)


def add_nakleyka(request):

    if request.method == 'POST':
        form = NakleykaAddForm(data=request.POST)
        if form.is_valid():
                form.save()
                return redirect('nakleyka_list_benkam')
    else:
        form = NakleykaAddForm()

    context =  {
        'form':form
    }
    return render(request,'norma/benkam/add_nakleyka.html',context)

def add_sublimation_benkam(request):

    if request.method == 'POST':
        form = SublimationAddForm(data=request.POST)
        if form.is_valid():
                form.save()
                return redirect('sublimatsiya_list_benkam')
    else:
        form = SublimationAddForm()

    context =  {
        'form':form
    }
    return render(request,'norma/benkam/add_sublimation.html',context)



@csrf_exempt
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

def add_norm(request):
    return render(request,'norma/norma_crud/add.html')

def full_update_termomost(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['type']='termo'
        form = NormaFileForm(data, request.FILES)
        if form.is_valid():
            temomostt =Termomost.objects.all()
            temomostt.delete()
            form_file = form.save()
            file = form_file.file
            path =f'{MEDIA_ROOT}/{file}'
            
            df = pd.read_excel(path,sheet_name='Лист4', header=0)
            
            context ={
            'section':''
            }
            df = df.astype(str)
            df = df.replace('nan','0')
            
            columns = df.columns
            for key, row in df.iterrows():
                norma_dict = {}
                for col in columns:
                    norma_dict[col]=row[col]
                Termomost(data =norma_dict).save()

    return render(request,'norma/benkam/main.html')

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
            
            df = pd.read_excel(path,sheet_name='нормы', header=4)
            
            context ={
            'section':''
            }
            df = df.astype(str)
            df = df.replace('nan','0')
            df = df.replace('0.0','0')
            
            columns = df.columns
            for key, row in df.iterrows():
                norma_dict = {}
                for col in columns:
                    norma_dict[col]=row[col]
                Norma(data =norma_dict).save()

    return render(request,'norma/benkam/main.html')


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
   


    



def file_upload_termo_org(request): 
    if request.method == 'POST':
        type_r = request.POST.get('type_r',None)
        if type_r:
            data = request.POST.copy()
            data['type']='termo'
            form = NormaFileForm(data, request.FILES)
            if form.is_valid():
                form.save()
                res = redirect('norma_file_list_termo_org_benkam')
                res['Location'] +='?type=texcarta'
                return res
        else:
            data = request.POST.copy()
            data['type']='termo'
            form = NormaFileForm(data, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('norma_file_list_termo_org_benkam')
    else:
        form =NormaFileForm()
        context ={
            'section':''
        }
 
    return render(request,'universal/main.html',context)

def file_upload_org(request): 
  if request.method == 'POST':
    data = request.POST.copy()
    data['type']='simple'
    form = NormaFileForm(data, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('norma_file_list_org_benkam')
  else:
      form =NormaFileForm()
      context ={
        'section':''
      }
  return render(request,'universal/main.html',context)



def file_list_org(request):
    files = NormaExcelFiles.objects.filter(generated =False,type='simple').order_by('-created_at')
    context ={'files':files,
              'link':'/norma-benkam/process-combinirovanniy/',
              'section':'Генерация норма обычного файла',
              'type':'обычный',
              'file_type':'simple'
              }
    return render(request,'universal/file_list_norma.html',context)

def file_list_termo_org(request):
    files = NormaExcelFiles.objects.filter(generated =False,type='termo').order_by('-created_at')
    
    type_r = request.GET.get('type',None)
    if type_r:
        link ='/norma-benkam/generate-texcarta/'
    else:
        link ='/norma-benkam/process-combinirovanniy/'
    context ={'files':files,
              'link':link,
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
    
    for key,row in df_exell.iterrows():
        if product_type =='termo':
            df.append([
                row['SAP код E'],row['Экструзия холодная резка'],
                row['SAP код Z'],row['Печь старения'],
                row['SAP код P'],row['Покраска автомат'],
                row['SAP код S'],row['Сублимация'],
                row['SAP код A'],row['Анодировка'],
                row['SAP код N'],row['Наклейка'],
                row['SAP код K'],row['K-Комбинирования'],
                row['SAP код 7'],row['U-Упаковка + Готовая Продукция'],
                row['SAP код F'],row['Фабрикация'],
                row['SAP код 75'],row['U-Упаковка + Готовая Продукция 75'],
            ])
        else:
            df.append([
                row['SAP код E'],row['Экструзия холодная резка'],
                row['SAP код Z'],row['Печь старения'],
                row['SAP код P'],row['Покраска автомат'],
                row['SAP код S'],row['Сублимация'],
                row['SAP код A'],row['Анодировка'],
                row['SAP код N'],row['Наклейка'],
                row['SAP код 7'],row['U-Упаковка + Готовая Продукция'],
                row['SAP код F'],row['Фабрикация'],
                row['SAP код 75'],row['U-Упаковка + Готовая Продукция 75'],
            ])
        
    class Xatolar:
        def __init__(self,section,xato,sap_code):
            self.section = section
            self.xato = xato
            self.sap_code = sap_code

    does_not_exist_norm =[]
    k = -1
    if product_type =='termo':
        for i in range(0,len(df)):
            if df[i][0] != '':
                length = df[i][0].split('-')[0]
                if not Norma.objects.filter(data__новый__icontains=length).exists():
                    does_not_exist_norm.append(Xatolar(section='Норма расход',xato='norma rasxod yo\'q',sap_code=df[i][0]))
                    continue
                splav_code = df[i][1].split()[0][:2]
                splav_list = AlyuminniysilindrEkstruziya1.objects.filter(название__icontains ='60'+splav_code).exists()
                if not splav_list:
                    does_not_exist_norm.append(Xatolar(section='Алюмин Сплав',xato='60'+splav_code,sap_code=df[i][0]))
            
            if df[i][4] != '':
                kraska_code = df[i][5].split()[-1]
                kraskas = Kraska.objects.filter(код_краски = kraska_code).exists()
                if not kraskas:
                    does_not_exist_norm.append(Xatolar(section='Краска',xato=kraska_code,sap_code=df[i][4]))

            if df[i][6] != '':
                length = df[i][6].split('-')[0]
                alum_teks = Norma.objects.filter(data__новый__icontains=length)[:1].get()

                sublimatsiya_code = df[i][7].split('_')[1]
                code_ss = alum_teks.data['Суб. Декор. плёнка ширина пленки/ мм']
                mein = alum_teks.data['Суб. Декор. плёнка расход на 1000 профиль/м²']
                subdecorplonka = SubDekorPlonka.objects.filter(код_декор_пленки = sublimatsiya_code, ширина_декор_пленки_мм = code_ss).exists()
                if not subdecorplonka:
                    does_not_exist_norm.append(Xatolar(section='Сублимация декор',xato=sublimatsiya_code +' ' + code_ss +' bazada yo\'q',sap_code=df[i][6]))
            
            if df[i][10] != '':
                length = df[i][10].split('-')[0]
                alum_teks = Norma.objects.filter(data__новый__icontains=length)[:1].get()
                if (alum_teks.data['верх ширина ленты/мм'] =='0' and alum_teks.data['низ ширина ленты/мм'] == '0'):
                    does_not_exist_norm.append(Xatolar(section='Наклейка',xato='bazada qiymati 0',sap_code=df[i][10]))
            if df[i][12] != '':
                length = df[i][12].split('-')[0]
                if not Norma.objects.filter(data__новый__icontains=length).exists():
                    does_not_exist_norm.append(Xatolar(section='Норма расход',xato='bazada yo\'q',sap_code=df[i][12]))
                    continue
                artikul = df[i][12].split('-')[0]
                termomostrlar = Termomost.objects.filter(data__Артикул__icontains=artikul).exists()
                if not termomostrlar:
                    does_not_exist_norm.append(Xatolar(section='Термомост',xato='termomost bazada yo\'q',sap_code=df[i][12]))
            
    else:
        for i in range(0,len(df)):
            if df[i][0] != '':
                length = df[i][0].split('-')[0]
                if not Norma.objects.filter(data__новый__icontains=length).exists():
                    does_not_exist_norm.append(Xatolar(section='Норма расход',xato='bazada yo\'q',sap_code=df[i][0]))
                    continue
                splav_code = df[i][1].split()[0][:2]
                splav_list = AlyuminniysilindrEkstruziya1.objects.filter(название__icontains ='60'+splav_code).exists()
                if not splav_list:
                    does_not_exist_norm.append(Xatolar(section='Алюмин Сплав',xato='60'+splav_code,sap_code=df[i][0]))
            
            if df[i][4] != '':
                kraska_code = df[i][5].split()[-1]
                kraskas = Kraska.objects.filter(код_краски = kraska_code).exists()
                if not kraskas:
                    does_not_exist_norm.append(Xatolar(section='Краска',xato=kraska_code,sap_code=df[i][4]))

            if df[i][6] != '':
                length = df[i][6].split('-')[0]
                alum_teks = Norma.objects.filter(data__новый__icontains=length)[:1].get()
                sublimatsiya_code = df[i][7].split('_')[1]
                code_ss = alum_teks.data['Суб. Декор. плёнка ширина пленки/ мм']
                mein = alum_teks.data['Суб. Декор. плёнка расход на 1000 профиль/м²']
                subdecorplonka = SubDekorPlonka.objects.filter(код_декор_пленки = sublimatsiya_code, ширина_декор_пленки_мм = code_ss).exists()
                if not subdecorplonka:
                    does_not_exist_norm.append(Xatolar(section='Сублимация декор',xato=sublimatsiya_code +' ' + code_ss+' bazada yo\'q',sap_code=df[i][6]))
            
            if df[i][10] != '':
                length = df[i][10].split('-')[0]
                alum_teks = Norma.objects.filter(data__новый__icontains=length)[:1].get()
                if (alum_teks.data['верх ширина ленты/мм'] =='0' and alum_teks.data['низ ширина ленты/мм'] == '0'):
                    does_not_exist_norm.append(Xatolar(section='Наклейка',xato='bazada qiymati 0',sap_code=df[i][10]))
            
                    

     
    
    if len(does_not_exist_norm) > 0: 
        context ={
            'does_not_exist_norm':does_not_exist_norm,
            'section':'Ошибки нормы',
            'id':id

        }
        return render(request,'norma/benkam/not_exist.html',context)
    
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
    
    norma_exists= []

    for i in range(0,len(df)):
        
        older_process ={'sapcode':'','kratkiy':''}
        
        if {df[i][0]:df[i][1]} not in norma_exists:
            if df[i][0] !="":
                norma_exists.append({df[i][0]:df[i][1]})
                older_process['sapcode'] =df[i][0]
                older_process['kratkiy'] =df[i][1]
                if df[i][0].split('-')[1][:1]=='E':
                    splav_code = df[i][1].split()[0][:2]
                    splav_list = AlyuminniysilindrEkstruziya1.objects.filter(название__icontains ='60'+splav_code)
                    spav_counter = 1
                    for splav in splav_list:
                        df_new['ID'].append('1')
                        df_new['MATNR'].append(df[i][0])
                        df_new['WERKS'].append('1201')
                        df_new['TEXT1'].append(df[i][1])
                        df_new['STLAL'].append(str(spav_counter))
                        spav_counter +=1
                        df_new['STLAN'].append('1')
                        df_new['ZTEXT'].append('Экструзия холодная резка')
                        length = df[i][0].split('-')[0]
                        # print(length)
                        alum_teks = Norma.objects.filter(data__новый__icontains=length)[:1].get()
                        
                        
                        mein_percent =((get_legth(df[i][1]))/6)
                        df_new['STKTX'].append(splav.название)
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
                                
                                df_new['MATNR1'].append(splav.sap_code_s4q100)
                                df_new['TEXT2'].append(splav.название)
                                
                                df_new['MEINS'].append(("%.3f" % (float(alum_teks.data['расход сплава на 1000 шт профиля/кг'])*mein_percent)).replace('.',',')) 
                                df_new['MENGE'].append('КГ')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            
                            
                            if k == 2:
                                df_new['MATNR1'].append('1900000080')
                                df_new['TEXT2'].append('Тех. отход Экструзия')
                                df_new['MENGE'].append('КГ')
                                
                                df_new['MEINS'].append(("%.3f" % ((-1)*(float(alum_teks.data['при этом % тех.отхода возвратного=12,9%'])*mein_percent))).replace('.',',')) 
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                                
                            df_new['LGORT'].append('PS02')
        
        else:
            pass
                    
        norma_z =[]
        
        
        if {df[i][2]:df[i][3]} not in norma_exists:
            if df[i][2] !="":
                norma_exists.append({df[i][2]:df[i][3]})
                lenghtht = df[i][2].split('-')[0]
                
                sap_code_zak = df[i][2].split('-')[0]
                
                j+=1
                if (df[i][2].split('-')[1][:1]=='Z'):
                    df_new['ID'].append('1')
                    df_new['MATNR'].append(df[i][2])
                    df_new['WERKS'].append('1201')
                    df_new['TEXT1'].append(df[i][3])
                    df_new['STLAL'].append('1')
                    df_new['STLAN'].append('1')
                    df_new['ZTEXT'].append('Печь старения')
                    
                    df_new['STKTX'].append('')
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
                    df_new['MATNR1'].append(older_process['sapcode'])
                    df_new['TEXT2'].append(older_process['kratkiy'])
                    df_new['MEINS'].append('1000') 
                    df_new['MENGE'].append('ШТ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')        
                    df_new['LGORT'].append('P021')
                
                older_process['sapcode'] =df[i][2]
                older_process['kratkiy'] =df[i][3] 
       
        else:
            pass        
        
        sklad ={
            'sklad_pokraski':['Chemetal + 7400','Alufinish','Chemetal + 7406'],
            'number_sklad':[
                ['P050','PS05','PS05','PS05','PS05'],
                ['P050','PS05','PS05','PS05','PS05'],
                ['P050','PS05','PS05','PS05','PS05'],
                ]
        }
        
       
        if {df[i][4]:df[i][5]} not in norma_exists:
            if df[i][4] !="":
                norma_exists.append({df[i][4]:df[i][5]})
                if (df[i][4].split('-')[1][:1]=='P'):
                    kraska_code = df[i][5].split()[-1]
                    kraskas = Kraska.objects.filter(код_краски = kraska_code)[:1].get()
                    for p in range(0,3):    
                        j+=1
                        df_new['ID'].append('1')
                        df_new['MATNR'].append(df[i][4])
                        df_new['WERKS'].append('1201')
                        df_new['TEXT1'].append(df[i][5])
                        df_new['STLAL'].append(f'{p+1}')
                        df_new['STLAN'].append('1')
                        ztekst = sklad['sklad_pokraski'][p]
                        df_new['ZTEXT'].append('Покраска автомат')
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
                            alum_teks = Norma.objects.filter(data__новый__icontains=length)[:1].get()
                        else:
                            alum_teks = Norma.objects.filter(data__новый__icontains=length)[:1].get()
                        
                        if p == 0:
                            ximikats = Ximikat.objects.filter(chemetal7400 = 1)
                        elif p==1:   
                            ximikats = Ximikat.objects.filter(alufinish = 1)
                        elif p==2:   
                            ximikats = Ximikat.objects.filter(chemetal7406 = 1)

                        mein_percent =((get_legth(df[i][5]))/6)
                        ximikat_counter = 2 + len(ximikats)
                        
                        
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
                        df_new['POSNR'].append('1')
                        df_new['POSTP'].append('L')  
                        df_new['MATNR1'].append(older_process['sapcode'])
                        df_new['TEXT2'].append(older_process['kratkiy'])
                        df_new['MEINS'].append('1000')
                        df_new['MENGE'].append('ШТ')
                        df_new['DATUV'].append('')
                        df_new['PUSTOY'].append('')
                        df_new['LGORT'].append('P050')
                            
                        ximikat_counter =2
                        for ximik in ximikats:
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
                            df_new['POSNR'].append(ximikat_counter)
                            df_new['POSTP'].append('L') 
                            df_new['MATNR1'].append(ximik.sap_code_s4q100)
                            df_new['TEXT2'].append(ximik.название)
                            df_new['MENGE'].append("КГ")
                            df_new['MEINS'].append(("%.3f" % (float(alum_teks.data[f'({p+1})'+ximik.название])*mein_percent) ).replace('.',',')) 
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('PS05')
                            ximikat_counter+=1
                            
                            
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
                        df_new['POSNR'].append(ximikat_counter)
                        df_new['POSTP'].append('L')      
                        df_new['MATNR1'].append(kraskas.sap_code_s4q100)
                        df_new['TEXT2'].append(kraskas.название)
                        df_new['MENGE'].append('КГ')
                        df_new['MEINS'].append( ("%.3f" % (float(alum_teks.data['расход /кг на 1000 профилей'])*mein_percent)).replace('.',','))
                        df_new['DATUV'].append('')
                        df_new['PUSTOY'].append('')
                        df_new['LGORT'].append('PS05')
                    
                    
                                
                older_process['sapcode'] =df[i][4]
                older_process['kratkiy'] =df[i][5]
        
        else:
            pass
            
        
        if {df[i][6]:df[i][7]} not in norma_exists:
            if df[i][6] !="":
                norma_exists.append({df[i][6]:df[i][7]})
                if (df[i][6].split('-')[1][:1]=='S'):
                    j+=1
                    df_new['ID'].append('1')
                    df_new['MATNR'].append(df[i][6])
                    df_new['WERKS'].append('1201')
                    df_new['TEXT1'].append(df[i][7])
                    df_new['STLAL'].append('1')
                    df_new['STLAN'].append('1')
                    df_new['ZTEXT'].append('Сублимация')
                    df_new['STKTX'].append('')
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
                    
                    alum_teks = Norma.objects.filter(data__новый__icontains=length)[:1].get()
                    
                    mein_percent =((get_legth(df[i][7]))/6)
                    
                    sublimatsiya_code = df[i][7].split('_')[1]
                    code_ss = alum_teks.data['Суб. Декор. плёнка ширина пленки/ мм']
                    mein = alum_teks.data['Суб. Декор. плёнка расход на 1000 профиль/м²']
                    
                    
                    
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
                            df_new['LGORT'].append('P060')
                        
                        if k==1:
                            
                            subdecor = SubDekorPlonka.objects.get(код_декор_пленки = sublimatsiya_code, ширина_декор_пленки_мм = code_ss)
                            df_new['MATNR1'].append(subdecor.sap_code_s4q100)
                            df_new['TEXT2'].append(subdecor.название)
                            df_new['MENGE'].append('М2')
                            df_new['MEINS'].append( ("%.3f" % (float(mein)*mein_percent)).replace('.',','))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('PS06')

                        
                            
                        
                            
                older_process['sapcode'] =df[i][6]
                older_process['kratkiy'] =df[i][7]
        
        else:
            pass
        
            
       
        if {df[i][8]:df[i][9]} not in norma_exists:
            if df[i][8] !="":
                norma_exists.append({df[i][8]:df[i][9]})
                if (df[i][8].split('-')[1][:1]=='A'):
                    j+=1
                    df_new['ID'].append('1')
                    df_new['MATNR'].append(df[i][8])
                    df_new['WERKS'].append('1201')
                    df_new['TEXT1'].append(df[i][9])
                    df_new['STLAL'].append(f'1')
                    df_new['STLAN'].append('1')
                    df_new['ZTEXT'].append('Анодировка')
                    df_new['STKTX'].append('Chemetal')
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
                    
                    code_anod = df[i][9].split()[-1]
                    
                    length = df[i][8].split('-')[0]
                    norma = Norma.objects.filter(data__новый__icontains=length)[:1].get()
        
                    mein_percent =((get_legth(df[i][9]))/6)
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
                    df_new['POSNR'].append('1')
                    df_new['POSTP'].append('L')
                    df_new['MATNR1'].append(older_process['sapcode'])
                    df_new['TEXT2'].append(older_process['kratkiy'])
                    df_new['MEINS'].append('1000')
                    df_new['MENGE'].append('ШТ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                    df_new['LGORT'].append('P130') 
                    
                    anodirovka = Anod.objects.all()
                    anodirovka_dict = {}
                    for anod in anodirovka:
                        anodirovka_dict[f'{anod.название}'] = anod.sap_code_s4q100
                    anod_counter = 1
                    for key,val in norma.data.items():
                        if code_anod in key:
                            j+=1
                            header_anodirovki = key.split(')')[-1]
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
                            df_new['POSNR'].append(anod_counter+1)
                            df_new['POSTP'].append('L')
                            df_new['MATNR1'].append(anodirovka_dict[header_anodirovki])
                            df_new['TEXT2'].append(header_anodirovki)
                            df_new['MENGE'].append('КГ')
                            df_new['MEINS'].append( ("%.3f" % (float(val)*mein_percent)).replace('.',','))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('PS13')
                            anod_counter += 1
                            
                older_process['sapcode'] =df[i][8]
                older_process['kratkiy'] =df[i][9]
        
        else:
            pass
        
            
        
        if {df[i][10]:df[i][11]} not in norma_exists:
            if df[i][10] !="":
                
                norma_exists.append({df[i][10]:df[i][11]})
                if (df[i][10].split('-')[1][:1]=='N'):
                    
                    length = df[i][10].split('-')[0]
                    alum_teks = Norma.objects.filter(data__новый__icontains=length)[:1].get()
                    mein_percent =((get_legth(df[i][11]))/6)
                    nakleyka_code = df[i][11].split()[-1]
                    
                    nakleyka_result1 = None
                    nakleyka_result2 = None
                    nakleyka_result3 = None
                    nakleyka_result4 = None
                    meinss1 = None
                    meinss2 = None
                    meinss3 = None
                    meinss4 = None
                    if (alum_teks.data['верх ширина ленты/мм'] =='0' or alum_teks.data['верх ширина ленты/мм'] =='0.0') and alum_teks.data['низ ширина ленты/мм'] != '0':
                        meinss = float(alum_teks.data['низ расход ленты на 1000 профиль/м2']) 
                        
                        if Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина= alum_teks.data['низ ширина ленты/мм'].replace('.0','')).exists():
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина= alum_teks.data['низ ширина ленты/мм'].replace('.0',''))[:1].get()
                            meinss1 = meinss
                        else:
                            nakleyka_width = alum_teks.data['низ ширина ленты/мм']
                            nakleyka_shirinas = list(Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина__lte = str(nakleyka_width)).distinct('ширина').values('ширина'))
                            
                            nakleyka_shirinas =[float(val['ширина']) for val in nakleyka_shirinas]
                            nakleyka_shirinas.sort()
                            
                            
                            qoldiq = 0 
                            for shirina in nakleyka_shirinas[::-1]:
                                if float(nakleyka_width) >= float(shirina):
                                    nakleyka_result1 =Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина = int(shirina))[:1].get()
                                    meinss1 = (meinss * float(shirina))/float(nakleyka_width)
                                    qoldiq = float(nakleyka_width) -float(shirina)
                                    break
                    
                            for shirina in nakleyka_shirinas:
                                if float(qoldiq) <= float(shirina):
                                    nakleyka_result2 =Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина = int(shirina))[:1].get()
                                    meinss2 = (meinss * float(shirina))/float(nakleyka_width)
                                    break
                            

                    elif (alum_teks.data['низ ширина ленты/мм'] =='0' or alum_teks.data['низ ширина ленты/мм'] =='0.0') and alum_teks.data['верх ширина ленты/мм'] !='0':
                        meinss = float(alum_teks.data['верх расход ленты на 1000 профиль/м2'])
                        if Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина= alum_teks.data['верх ширина ленты/мм'].replace('.0','')).exists():
                            nakleyka_result3 = Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина= alum_teks.data['верх ширина ленты/мм'].replace('.0',''))[:1].get()
                            meinss3 = meinss
                        else:
                            nakleyka_width = alum_teks.data['верх ширина ленты/мм']
                            nakleyka_shirinas = list(Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина__lte = str(nakleyka_width)).distinct('ширина').values('ширина'))
                            nakleyka_shirinas =[float(val['ширина']) for val in nakleyka_shirinas]
                            nakleyka_shirinas.sort()
                            

                            qoldiq = 0 
                            for shirina in nakleyka_shirinas[::-1]:
                                if float(nakleyka_width) >= float(shirina):
                                    nakleyka_result3 =Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина = int(shirina))[:1].get()
                                    meinss3 = (meinss * float(shirina))/float(nakleyka_width)
                                    qoldiq = float(nakleyka_width) -float(shirina)
                                    break 
                    
                            for shirina in nakleyka_shirinas:
                                if float(qoldiq) <= float(shirina):
                                    nakleyka_result4 =Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина = int(shirina))[:1].get()
                                    meinss4 = (meinss * float(shirina))/float(nakleyka_width)
                                    break

                    elif alum_teks.data['низ ширина ленты/мм'] !='0' and alum_teks.data['низ ширина ленты/мм'] !='0.0' and alum_teks.data['верх ширина ленты/мм'] !='0' and alum_teks.data['верх ширина ленты/мм'] !='0.0':
                        meinss_niz = float(alum_teks.data['низ расход ленты на 1000 профиль/м2'])
                        meinss_verx = float(alum_teks.data['верх расход ленты на 1000 профиль/м2'])
                        print(alum_teks.data['новый'])
                        if Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина= alum_teks.data['низ ширина ленты/мм'].replace('.0','')).exists():
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина= alum_teks.data['низ ширина ленты/мм'].replace('.0',''))[:1].get()
                            meinss1 = meinss_niz
                        else:
                            nakleyka_width = alum_teks.data['низ ширина ленты/мм'].replace('.0','')
                            nakleyka_shirinas = list(Nakleyka.objects.filter(код_наклейки = nakleyka_code).distinct('ширина').values('ширина'))
                            nakleyka_shirinas =[float(val['ширина']) for val in nakleyka_shirinas]
                            nakleyka_shirinas.sort()
                           
                            qoldiq = 0 
                            for shirina in nakleyka_shirinas[::-1]:
                                if float(nakleyka_width) >= float(shirina):
                                    nakleyka_result1 =Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина = int(shirina))[:1].get()
                                    meinss1 = (meinss_niz * float(shirina))/float(nakleyka_width)
                                    qoldiq = float(nakleyka_width) -float(shirina)
                                    break
                           

            
                            for shirina in nakleyka_shirinas:
                                if float(qoldiq) <= float(shirina):
                                    nakleyka_result2 =Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина = int(shirina))[:1].get()
                                    meinss2 = (meinss_niz * float(shirina))/float(nakleyka_width)
                                    break
                               
                           
                        
                        if Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина= alum_teks.data['верх ширина ленты/мм'].replace('.0','')).exists():
                            nakleyka_result3 = Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина= alum_teks.data['верх ширина ленты/мм'].replace('.0',''))[:1].get()
                            meinss3 = meinss_verx
                        else:
                            nakleyka_width = alum_teks.data['верх ширина ленты/мм'].replace('.0','')
                            nakleyka_shirinas = list(Nakleyka.objects.filter(код_наклейки = nakleyka_code).distinct('ширина').values('ширина'))
                            nakleyka_shirinas =[float(val['ширина']) for val in nakleyka_shirinas]
                            
                            nakleyka_shirinas.sort()
                            

                           
                            qoldiq = 0 
                            for shirina in nakleyka_shirinas[::-1]:
                                if float(nakleyka_width) >= float(shirina):
                                    nakleyka_result3 =Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина = int(shirina))[:1].get()
                                    meinss3 = (meinss_niz * float(shirina))/float(nakleyka_width)
                                    qoldiq = float(nakleyka_width) -float(shirina)
                                    break
                            
                            for shirina in nakleyka_shirinas:
                                if float(qoldiq) <= float(shirina):
                                    nakleyka_result4 =Nakleyka.objects.filter(код_наклейки = nakleyka_code,ширина = int(shirina))[:1].get()
                                    meinss4 = (meinss_verx * float(shirina))/float(nakleyka_width)
                                    break
                    else:
                        print('nakleyka razmer not')
                              
                    if nakleyka_result1 or nakleyka_result2 or nakleyka_result3 or nakleyka_result4:
                        j+=1
                        if (df[i][10].split('-')[1][:1]=='N'):
                            df_new['ID'].append('1')
                            df_new['MATNR'].append(df[i][10])
                            df_new['WERKS'].append('1201')
                            df_new['TEXT1'].append(df[i][11])
                            df_new['STLAL'].append('1')
                            df_new['STLAN'].append('1')
                            df_new['ZTEXT'].append('Наклейка')
                            df_new['STKTX'].append('')
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
                            df_new['MATNR1'].append(older_process['sapcode'])
                            df_new['TEXT2'].append(older_process['kratkiy'])
                            df_new['MEINS'].append('1000')
                            df_new['MENGE'].append('ШТ')
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('P070')
                        nakleyka_counter = 2
                        if nakleyka_result1:
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
                            df_new['POSNR'].append(f'{nakleyka_counter}')
                            df_new['POSTP'].append('L')
                            df_new['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                            df_new['TEXT2'].append(nakleyka_result1.название)
                            df_new['MENGE'].append('М2')
                            df_new['MEINS'].append( ("%.3f" % round503(float(meinss1)*mein_percent)).replace('.',','))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('PS07')
                            nakleyka_counter += 1
                        if nakleyka_result2:
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
                            df_new['POSNR'].append(f'{nakleyka_counter}')
                            df_new['POSTP'].append('L')
                            df_new['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                            df_new['TEXT2'].append(nakleyka_result2.название)
                            df_new['MENGE'].append('М2')
                            df_new['MEINS'].append( ("%.3f" % round503(float(meinss2)*mein_percent)).replace('.',','))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('PS07')
                            nakleyka_counter += 1
                        if nakleyka_result3:
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
                            df_new['POSNR'].append(f'{nakleyka_counter}')
                            df_new['POSTP'].append('L')
                            df_new['MATNR1'].append(nakleyka_result3.sap_code_s4q100)
                            df_new['TEXT2'].append(nakleyka_result3.название)
                            df_new['MENGE'].append('М2')
                            df_new['MEINS'].append( ("%.3f" % round503(float(meinss3)*mein_percent)).replace('.',','))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('PS07')
                            nakleyka_counter += 1
                        if nakleyka_result4:
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
                            df_new['POSNR'].append(f'{nakleyka_counter}')
                            df_new['POSTP'].append('L')
                            df_new['MATNR1'].append(nakleyka_result4.sap_code_s4q100)
                            df_new['TEXT2'].append(nakleyka_result4.название)
                            df_new['MENGE'].append('М2')
                            df_new['MEINS'].append( ("%.3f" % round503(float(meinss4)*mein_percent)).replace('.',','))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('PS07')
                            nakleyka_counter += 1
                                
                older_process['sapcode'] =df[i][10]
                older_process['kratkiy'] =df[i][11]
        
        else:
            pass
            
        if product_type =='termo':

            if {df[i][12]:df[i][13]} not in norma_exists:
                if df[i][12] !="":
                    norma_exists.append({df[i][12]:df[i][13]})
                    if (df[i][12].split('-')[1][:1]=='K'):
                        
                        older_process_kombinirovanniy = {'s1':None,'k1':None,'s2':None,'k2':None,'s3':None,'k3':None}
                        
                        if df[i+1][10] !='':
                            older_process_kombinirovanniy['s1'] = df[i+1][10]
                            older_process_kombinirovanniy['k1'] = df[i+1][11]
                        elif df[i+1][8] !='':
                            older_process_kombinirovanniy['s1'] = df[i+1][8]
                            older_process_kombinirovanniy['k1'] = df[i+1][9]
                        elif df[i+1][6] !='':
                            older_process_kombinirovanniy['s1'] = df[i+1][6]
                            older_process_kombinirovanniy['k1'] = df[i+1][7]
                        elif df[i+1][4] !='':
                            older_process_kombinirovanniy['s1'] = df[i+1][4]
                            older_process_kombinirovanniy['k1'] = df[i+1][5]
                        elif df[i+1][2] !='':
                            older_process_kombinirovanniy['s1'] = df[i+1][2]
                            older_process_kombinirovanniy['k1'] = df[i+1][3]
                        elif df[i+1][0] !='':
                            older_process_kombinirovanniy['s1'] = df[i+1][0]
                            older_process_kombinirovanniy['k1'] = df[i+1][1]
                        else:
                            older_process_kombinirovanniy['s1'] = None
                            older_process_kombinirovanniy['k1'] = None

                        if df[i+2][10] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][10]
                            older_process_kombinirovanniy['k2'] = df[i+2][11]
                        elif df[i+2][8] !='':
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
                        else:
                            older_process_kombinirovanniy['s2'] = None
                            older_process_kombinirovanniy['k2'] = None
                        try:
                            if df[i+3][12] =='':
                                if df[i+3][10] !='':
                                    older_process_kombinirovanniy['s3'] = df[i+3][10]
                                    older_process_kombinirovanniy['k3'] = df[i+3][11]
                                elif df[i+3][8] !='':
                                    older_process_kombinirovanniy['s3'] = df[i+3][8]
                                    older_process_kombinirovanniy['k3'] = df[i+3][9]
                                elif df[i+3][6] !='':
                                    older_process_kombinirovanniy['s3'] = df[i+3][6]
                                    older_process_kombinirovanniy['k3'] = df[i+3][7]
                                elif df[i+3][4] !='':
                                    older_process_kombinirovanniy['s3'] = df[i+3][4]
                                    older_process_kombinirovanniy['k3'] = df[i+3][5]
                                elif df[i+3][2] !='':
                                    older_process_kombinirovanniy['s3'] = df[i+3][2]
                                    older_process_kombinirovanniy['k3'] = df[i+3][3]
                                elif df[i+3][0] !='':
                                    older_process_kombinirovanniy['s3'] = df[i+3][0]
                                    older_process_kombinirovanniy['k3'] = df[i+3][1]
                            else:
                                older_process_kombinirovanniy['s3'] = None
                                older_process_kombinirovanniy['k3'] = None
                        except:
                            older_process_kombinirovanniy['s3'] = None
                            older_process_kombinirovanniy['k3'] = None
                                
                    
                        
                        j+=1
                        
                        df_new['ID'].append('1')
                        df_new['MATNR'].append(df[i][12])
                        df_new['WERKS'].append('1201')
                        df_new['TEXT1'].append(df[i][13])
                        df_new['STLAL'].append('1')
                        df_new['STLAN'].append('1')
                        df_new['ZTEXT'].append('K-Комбинирования')
                        df_new['STKTX'].append('')
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
                        
                        artikul = df[i][12].split('-')[0]
                        termomostrlar = Termomost.objects.get(data__Артикул__icontains=artikul)
                        

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
                                df_new['LGORT'].append('P080')
                            
                            termomost_list ={}

                            if termomostrlar.data['1'] != '0':
                                termomost_list['1'] ={'sap_code':termomostrlar.data['1'],'text':termomostrlar.data['Термомост 1']}

                            if termomostrlar.data['2'] != '0':
                                termomost_list['2'] ={'sap_code':termomostrlar.data['2'],'text':termomostrlar.data['Термомост 2']}

                            if termomostrlar.data['3'] != '0':
                                termomost_list['3'] ={'sap_code':termomostrlar.data['3'],'text':termomostrlar.data['Термомост 3']}

                            if termomostrlar.data['4'] != '0':
                                termomost_list['4'] ={'sap_code':termomostrlar.data['4'],'text':termomostrlar.data['Термомост 4']}


                            t = 3 
                            for key,val in termomost_list.items(): 
                                j += 1
                                t += 1
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
                                df_new['MATNR1'].append(val['sap_code'].replace('.0',''))
                                df_new['TEXT2'].append(val['text'])
                                df_new['MEINS'].append('6500') 
                                df_new['MENGE'].append('М')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS08')
                                
                        
                                
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
                                df_new['LGORT'].append('P080')
                            
                            termomost_list ={}

                            if termomostrlar.data['1'] != '0':
                                termomost_list['1'] ={'sap_code':termomostrlar.data['1'],'text':termomostrlar.data['Термомост 1']}

                            if termomostrlar.data['2'] != '0':
                                termomost_list['2'] ={'sap_code':termomostrlar.data['2'],'text':termomostrlar.data['Термомост 2']}

                            if termomostrlar.data['3'] != '0':
                                termomost_list['3'] ={'sap_code':termomostrlar.data['3'],'text':termomostrlar.data['Термомост 3']}

                            if termomostrlar.data['4'] != '0':
                                termomost_list['4'] ={'sap_code':termomostrlar.data['4'],'text':termomostrlar.data['Термомост 4']}

                            t = 2 
                            for key,val in termomost_list.items(): 
                                j += 1
                                t += 1
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
                                df_new['MATNR1'].append(val['sap_code'].replace('.0',''))
                                df_new['TEXT2'].append(val['text'])
                                df_new['MEINS'].append('6500') 
                                df_new['MENGE'].append('М')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS08')
                                
                                
                                
                    older_process['sapcode'] =df[i][12]
                    older_process['kratkiy'] =df[i][13]
            
            else:
                pass
            
            
        
            if {df[i][14]:df[i][15]} not in norma_exists:
                
                if df[i][14] !="":
                    norma_exists.append({df[i][14]:df[i][15]})
                    if (df[i][14].split('-')[1][:1]=='7'):
                        lenghtht = df[i][14].split('-')[0]
                        
                        j += 1
                        df_new['ID'].append('1')
                        df_new['MATNR'].append(df[i][14])
                        df_new['WERKS'].append('1201')
                        df_new['TEXT1'].append(df[i][15])
                        df_new['STLAL'].append('1')
                        df_new['STLAN'].append('1')
                        df_new['ZTEXT'].append('U-Упаковка + Готовая Продукция')
                        df_new['STKTX'].append('')
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
                        df_new['LGORT'].append('P170')
                                
                            
                        
                    older_process['sapcode'] =df[i][14]
                    older_process['kratkiy'] =df[i][15]
                    
            
            else:      
                pass

        
            
            if {df[i][16]:df[i][17]} not in norma_exists:
                
                if df[i][16] !="":
                    norma_exists.append({df[i][16]:df[i][17]})
                    if (df[i][16].split('-')[1][:1]=='F'):
                        
                        length = df[i][16].split('-')[0]
                        
                        j += 1

                        if product_type =='termo':
                            sap_code1 = None
                            sap_code2 = None
                            sap_code3 = None
                            alum_teks1 = 0
                            alum_teks2 = 0
                            alum_teks3 = 0
                            if older_process_kombinirovanniy['s1']:
                                sap_code1 = older_process_kombinirovanniy['s1'].split('-')[0]
                                alum_teks1 = Norma.objects.filter(data__новый__icontains=sap_code1)[:1].get().data['Удельный вес профиля кг/м']
                            if older_process_kombinirovanniy['s2']:
                                sap_code2 = older_process_kombinirovanniy['s2'].split('-')[0]
                                alum_teks2 = Norma.objects.filter(data__новый__icontains=sap_code2)[:1].get().data['Удельный вес профиля кг/м']
                            if older_process_kombinirovanniy['s3']:
                                sap_code3 = older_process_kombinirovanniy['s3'].split('-')[0]
                                alum_teks3 = Norma.objects.filter(data__новый__icontains=sap_code3)[:1].get().data['Удельный вес профиля кг/м']

                            L = ((get_legth(older_process_kombinirovanniy['k1'])))
                            Lk= ((get_legth(df[i][17])))
                            n = int(L/Lk)
                            delta_L = L - n * Lk
                            meins1= int(1000/n)

                            tex_otxod = (-1000)*(float(alum_teks1) + float(alum_teks2) + float(alum_teks3))*delta_L
                        else:
                            L = ((get_legth(older_process['kratkiy'])))
                            Lk= ((get_legth(df[i][17])))
                            n = int(L/Lk)
                            delta_L = L - n * Lk
                            meins1= int(1000/n)
                            alum_teks = Norma.objects.filter(data__новый__icontains=length)[:1].get()
                            tex_otxod = (-1000)*float(alum_teks.data['Удельный вес профиля кг/м'])*delta_L

                        df_new['ID'].append('1')
                        df_new['MATNR'].append(df[i][16])
                        df_new['WERKS'].append('1201')
                        df_new['TEXT1'].append(df[i][17])
                        df_new['STLAL'].append('1')
                        df_new['STLAN'].append('1')
                        df_new['ZTEXT'].append('Фабрикация')
                        df_new['STKTX'].append('')
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
                        df_new['POSNR'].append('1')
                        df_new['POSTP'].append('L')
                        df_new['MATNR1'].append(older_process['sapcode'])
                        df_new['TEXT2'].append(older_process['kratkiy'])
                        df_new['MEINS'].append(meins1) 
                        df_new['MENGE'].append('ШТ')
                        df_new['DATUV'].append('')
                        df_new['PUSTOY'].append('')
                        df_new['LGORT'].append('P090')

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
                        df_new['POSNR'].append('2')
                        df_new['POSTP'].append('L')
                        df_new['MATNR1'].append('1900003318')
                        df_new['TEXT2'].append('Тех. отход ал. профиль с фабрикации')
                        df_new['MEINS'].append(("%.3f" % (tex_otxod)).replace('.',',')) 
                        df_new['MENGE'].append('КГ')
                        df_new['DATUV'].append('')
                        df_new['PUSTOY'].append('')
                        df_new['LGORT'].append('PS09')
                        
                                
                            
                        
                    older_process['sapcode'] =df[i][16]
                    older_process['kratkiy'] =df[i][17]
                    
            
            else:      
                pass
            
        

            if {df[i][18]:df[i][19]} not in norma_exists:
                
                if df[i][18] !="":
                    norma_exists.append({df[i][18]:df[i][19]})
                    if (df[i][18].split('-')[1][:2]=='75'):
                        
                        lenghtht = df[i][18].split('-')[0]
                        
                        j += 1
                        df_new['ID'].append('1')
                        df_new['MATNR'].append(df[i][18])
                        df_new['WERKS'].append('1201')
                        df_new['TEXT1'].append(df[i][19])
                        df_new['STLAL'].append('1')
                        df_new['STLAN'].append('1')
                        df_new['ZTEXT'].append('Упаковка12')
                        df_new['STKTX'].append('')
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
                        df_new['POSNR'].append('1')
                        df_new['POSTP'].append('L')
                        df_new['MATNR1'].append(older_process['sapcode'])
                        df_new['TEXT2'].append(older_process['kratkiy'])
                        df_new['MEINS'].append('1000') 
                        df_new['MENGE'].append('ШТ')
                        df_new['DATUV'].append('')
                        df_new['PUSTOY'].append('')
                        df_new['LGORT'].append('P170')
                            
                        
                    older_process['sapcode'] =df[i][18]
                    older_process['kratkiy'] =df[i][19]
                    
            
            else:      
                pass
        else:  
            
        
            if {df[i][12]:df[i][13]} not in norma_exists:
                
                if df[i][12] !="":
                    norma_exists.append({df[i][12]:df[i][13]})
                    if (df[i][12].split('-')[1][:1]=='7'):
                        lenghtht = df[i][12].split('-')[0]
                        
                        j += 1
                        df_new['ID'].append('1')
                        df_new['MATNR'].append(df[i][12])
                        df_new['WERKS'].append('1201')
                        df_new['TEXT1'].append(df[i][13])
                        df_new['STLAL'].append('1')
                        df_new['STLAN'].append('1')
                        df_new['ZTEXT'].append('U-Упаковка + Готовая Продукция')
                        df_new['STKTX'].append('')
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
                        if df[i][10] !='':
                            df_new['LGORT'].append('P070')
                        else:
                            df_new['LGORT'].append('P170')
                                
                            
                        
                    older_process['sapcode'] =df[i][12]
                    older_process['kratkiy'] =df[i][13]
                    
            
            else:      
                pass

        
            
            if {df[i][14]:df[i][15]} not in norma_exists:
                
                if df[i][14] !="":
                    norma_exists.append({df[i][14]:df[i][15]})
                    if (df[i][14].split('-')[1][:1]=='F'):
                        
                        length = df[i][14].split('-')[0]
                        
                        j += 1

                        if product_type =='termo':
                            sap_code1 = None
                            sap_code2 = None
                            sap_code3 = None
                            alum_teks1 = 0
                            alum_teks2 = 0
                            alum_teks3 = 0
                            if older_process_kombinirovanniy['s1']:
                                sap_code1 = older_process_kombinirovanniy['s1'].split('-')[0]
                                alum_teks1 = Norma.objects.filter(data__новый__icontains=sap_code1)[:1].get().data['Удельный вес профиля кг/м']
                            if older_process_kombinirovanniy['s2']:
                                sap_code2 = older_process_kombinirovanniy['s2'].split('-')[0]
                                alum_teks2 = Norma.objects.filter(data__новый__icontains=sap_code2)[:1].get().data['Удельный вес профиля кг/м']
                            if older_process_kombinirovanniy['s3']:
                                sap_code3 = older_process_kombinirovanniy['s3'].split('-')[0]
                                alum_teks3 = Norma.objects.filter(data__новый__icontains=sap_code3)[:1].get().data['Удельный вес профиля кг/м']

                            L = ((get_legth(older_process_kombinirovanniy['k1'])))
                            Lk= ((get_legth(df[i][15])))
                            n = int(L/Lk)
                            delta_L = L - n * Lk
                            meins1= int(1000/n)

                            tex_otxod = (-1000)*(float(alum_teks1) + float(alum_teks2) + float(alum_teks3))*delta_L
                        else:
                            L = ((get_legth(older_process['kratkiy'])))
                            Lk= ((get_legth(df[i][15])))
                            n = int(L/Lk)
                            delta_L = L - n * Lk
                            meins1= int(1000/n)
                            alum_teks = Norma.objects.filter(data__новый__icontains=length)[:1].get()
                            tex_otxod = (-1000)*float(alum_teks.data['Удельный вес профиля кг/м'])*delta_L

                        df_new['ID'].append('1')
                        df_new['MATNR'].append(df[i][14])
                        df_new['WERKS'].append('1201')
                        df_new['TEXT1'].append(df[i][15])
                        df_new['STLAL'].append('1')
                        df_new['STLAN'].append('1')
                        df_new['ZTEXT'].append('Фабрикация')
                        df_new['STKTX'].append('')
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
                        df_new['POSNR'].append('1')
                        df_new['POSTP'].append('L')
                        df_new['MATNR1'].append(older_process['sapcode'])
                        df_new['TEXT2'].append(older_process['kratkiy'])
                        df_new['MEINS'].append(meins1) 
                        df_new['MENGE'].append('ШТ')
                        df_new['DATUV'].append('')
                        df_new['PUSTOY'].append('')
                        df_new['LGORT'].append('P090')

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
                        df_new['POSNR'].append('2')
                        df_new['POSTP'].append('L')
                        df_new['MATNR1'].append('1900003318')
                        df_new['TEXT2'].append('Тех. отход ал. профиль с фабрикации')
                        df_new['MEINS'].append(("%.3f" % (tex_otxod)).replace('.',',')) 
                        df_new['MENGE'].append('КГ')
                        df_new['DATUV'].append('')
                        df_new['PUSTOY'].append('')
                        df_new['LGORT'].append('PS09')
                        
                                
                            
                        
                    older_process['sapcode'] =df[i][14]
                    older_process['kratkiy'] =df[i][15]
                    
            
            else:      
                pass
            
        

            if {df[i][16]:df[i][17]} not in norma_exists:
                
                if df[i][16] !="":
                    norma_exists.append({df[i][16]:df[i][17]})
                    if (df[i][16].split('-')[1][:2]=='75'):
                        
                        lenghtht = df[i][16].split('-')[0]
                        
                        j += 1
                        df_new['ID'].append('1')
                        df_new['MATNR'].append(df[i][16])
                        df_new['WERKS'].append('1201')
                        df_new['TEXT1'].append(df[i][17])
                        df_new['STLAL'].append('1')
                        df_new['STLAN'].append('1')
                        df_new['ZTEXT'].append('Упаковка12')
                        df_new['STKTX'].append('')
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
                        df_new['POSNR'].append('1')
                        df_new['POSTP'].append('L')
                        df_new['MATNR1'].append(older_process['sapcode'])
                        df_new['TEXT2'].append(older_process['kratkiy'])
                        df_new['MEINS'].append('1000') 
                        df_new['MENGE'].append('ШТ')
                        df_new['DATUV'].append('')
                        df_new['PUSTOY'].append('')
                        df_new['LGORT'].append('P170')
                            
                        
                    older_process['sapcode'] =df[i][16]
                    older_process['kratkiy'] =df[i][17]
                    
            
            else:      
                pass  

            
        
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

    
    # for key,val in df_new.items():
    #     print(key,len(val))
    # print(df_new)
    dff =pd.DataFrame(df_new)
    


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

def round503(n):
    if (n*100 % 1000) < 750 and (n*100 % 1000)>=250 :
        return int(n/10)*10 + 5
    elif (n*100 % 1000) >= 750:
        return int(n/10)*10 + 10
    else:
        return int(n/10)*10
    return 

def norma_delete(request):
    return 






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
    
def norma_delete_org(request):
    if request.method =='POST':
        ozmk =request.POST.get('ozmk',None)
        if ozmk:
            ozmks =ozmk.split()
            norma_base = CheckNormaBase.objects.filter(artikul__in =ozmks)
            norma_base.delete()
            messages.add_message(request, messages.INFO, "Normalar arxividan ochirildi")
        return render(request,'delete_/delete_norm.html')
    else:
        return render(request,'delete_/delete_norm.html')
    

def lenght_generate_texcarta(request,id):
    file = NormaExcelFiles.objects.get(id=id).file
    file_path =f'{MEDIA_ROOT}\\{file}'
    df =pd.read_excel(file_path)

    df =df.astype(str)
    df=df.replace('nan','')

    df_list = []
    df_list_no_dubl = []

    df_list_gp = [[],[],[],[]]

    for key,row in df.iterrows():
        if 'SAP код K'in row:
            df_list.append([
                row['SAP код E'],row['Экструзия холодная резка'],
                row['SAP код Z'],row['Печь старения'],
                row['SAP код P'],row['Покраска автомат'],
                row['SAP код S'],row['Сублимация'],
                row['SAP код A'],row['Анодировка'],
                row['SAP код N'],row['Наклейка'],
                row['SAP код K'],row['K-Комбинирования'],
                row['SAP код 7'],row['U-Упаковка + Готовая Продукция'],
                row['SAP код F'],row['Фабрикация'],
                row['SAP код 75'],row['U-Упаковка + Готовая Продукция 75'],
            ])
            
            if row['SAP код F']!='' and row['SAP код 75']!='':
                if not TexcartaBase.objects.filter(material = row['SAP код 75']).exists():
                    df_list_gp[0].append('1201')
                    df_list_gp[1].append('12017500')
                    df_list_gp[2].append('1')
                    df_list_gp[3].append(row['SAP код 75'])
                    TexcartaBase(material = row['SAP код 75']).save()
            elif row['SAP код K']!='' and row['SAP код 7']!='':   
                if not TexcartaBase.objects.filter(material = row['SAP код 7']).exists():
                    df_list_gp[0].append('1201')
                    df_list_gp[1].append('12017000')
                    df_list_gp[2].append('2')
                    df_list_gp[3].append(row['SAP код 7'])
                    TexcartaBase(material = row['SAP код 7']).save()

            if row['SAP код K'] != '':
                if not TexcartaBase.objects.filter(material = row['SAP код K']).exists():
                    df_list_gp[0].append('1201')
                    df_list_gp[1].append('1201K001')
                    df_list_gp[2].append('1')
                    df_list_gp[3].append(row['SAP код K'])

                    df_list_gp[0].append('1201')
                    df_list_gp[1].append('1201K002')
                    df_list_gp[2].append('1')
                    df_list_gp[3].append(row['SAP код K'])
                    TexcartaBase(material = row['SAP код K']).save()
            
            if row['SAP код N'] != '':
                if not TexcartaBase.objects.filter(material = row['SAP код N']).exists():
                    df_list_gp[0].append('1201')
                    df_list_gp[1].append('1201N000')
                    df_list_gp[2].append('1')
                    df_list_gp[3].append(row['SAP код N'])
                    TexcartaBase(material = row['SAP код N']).save()

            if row['SAP код F'] != '':
                if not TexcartaBase.objects.filter(material = row['SAP код F']).exists():
                    df_list_gp[0].append('1201')
                    df_list_gp[1].append('1201F001')
                    df_list_gp[2].append('1')
                    df_list_gp[3].append(row['SAP код F'])
                    TexcartaBase(material = row['SAP код F']).save()
        else:
            df_list.append([
                row['SAP код E'],row['Экструзия холодная резка'],
                row['SAP код Z'],row['Печь старения'],
                row['SAP код P'],row['Покраска автомат'],
                row['SAP код S'],row['Сублимация'],
                row['SAP код A'],row['Анодировка'],
                row['SAP код N'],row['Наклейка'],
                row['SAP код 7'],row['U-Упаковка + Готовая Продукция'],
                row['SAP код F'],row['Фабрикация'],
                row['SAP код 75'],row['U-Упаковка + Готовая Продукция 75'],
            ])
        
            if row['SAP код N']!='' and row['SAP код 7']!='':
                if not TexcartaBase.objects.filter(material = row['SAP код 7']).exists():
                    df_list_gp[0].append('1201')
                    df_list_gp[1].append('12017601')
                    df_list_gp[2].append('1')
                    df_list_gp[3].append(row['SAP код 7'])
                    TexcartaBase(material = row['SAP код 7']).save()
            elif row['SAP код N']=='' and row['SAP код 7']!='' :
                if not TexcartaBase.objects.filter(material = row['SAP код 7']).exists():
                    df_list_gp[0].append('1201')
                    df_list_gp[1].append('12017000')
                    df_list_gp[2].append('2')
                    df_list_gp[3].append(row['SAP код 7'])
                    TexcartaBase(material = row['SAP код 7']).save()
            
            if row['SAP код N'] != '':
                if not TexcartaBase.objects.filter(material = row['SAP код N']).exists():
                    df_list_gp[0].append('1201')
                    df_list_gp[1].append('1201N000')
                    df_list_gp[2].append('1')
                    df_list_gp[3].append(row['SAP код N'])
                    TexcartaBase(material = row['SAP код N']).save()

            if row['SAP код F'] != '':
                if not TexcartaBase.objects.filter(material = row['SAP код F']).exists():
                    df_list_gp[0].append('1201')
                    df_list_gp[1].append('1201F001')
                    df_list_gp[2].append('1')
                    df_list_gp[3].append(row['SAP код F'])
                    TexcartaBase(material = row['SAP код F']).save()

            if row['SAP код F']!='' and row['SAP код 75']!='':
                if not TexcartaBase.objects.filter(material = row['SAP код 75']).exists():
                    df_list_gp[0].append('1201')
                    df_list_gp[1].append('12017500')
                    df_list_gp[2].append('1')
                    df_list_gp[3].append(row['SAP код 75'])
                    TexcartaBase(material = row['SAP код 75']).save()



        if row['SAP код E'] !='':
                df_list_no_dubl.append({'МАТЕРИАЛ':row['SAP код E'],'КРАТКИЙ ТЕКСТ':row['Экструзия холодная резка']})
        if row['SAP код Z'] !='':
            df_list_no_dubl.append({'МАТЕРИАЛ':row['SAP код Z'],'КРАТКИЙ ТЕКСТ':row['Печь старения']})
        if row['SAP код P'] !='':
            df_list_no_dubl.append({'МАТЕРИАЛ':row['SAP код P'],'КРАТКИЙ ТЕКСТ':row['Покраска автомат']})
        if row['SAP код S'] !='':
            df_list_no_dubl.append({'МАТЕРИАЛ':row['SAP код S'],'КРАТКИЙ ТЕКСТ':row['Сублимация']})
        if row['SAP код A'] !='':
            df_list_no_dubl.append({'МАТЕРИАЛ':row['SAP код A'],'КРАТКИЙ ТЕКСТ':row['Анодировка']})


    counter = 0
    for row in df_list_no_dubl:
        if not TexcartaBase.objects.filter(material = row['МАТЕРИАЛ']).exists():
            if '-A' in row['МАТЕРИАЛ']:
                counter +=3
            elif '-S' in row['МАТЕРИАЛ']:
                counter +=8
            elif '-Z' in row['МАТЕРИАЛ']:
                counter +=2
            elif '-E' in row['МАТЕРИАЛ']:
                counter +=18
            elif '-P' in row['МАТЕРИАЛ']:
                counter +=6
       

  
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
    for row in df_list_no_dubl:
        if not TexcartaBase.objects.filter(material = row['МАТЕРИАЛ']).exists():
            length = row['МАТЕРИАЛ'].split('-')[0]
            norma = Norma.objects.filter(data__новый__icontains=length)[:1].get()

            L = get_legth(row['КРАТКИЙ ТЕКСТ'])
            
            if '-A' in row['МАТЕРИАЛ']:
                anod_kod = row['КРАТКИЙ ТЕКСТ'].split()[-1]
                bmsch = 35 if anod_kod in ['15023','15024','15025','15033','15034','15035','15043','15044','15045','15053','15054','15055'] else 50
                for i7 in range(1,4):
                    if i7 ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='1201'
                        df_new['STTAG'][counter_2] ='01012022'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] ='Анодирование \ Анодирование (Вход)'
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i7 == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] ='0010'
                        df_new['ARBPL'][counter_2] ='1201A902'
                        df_new['WERKS1'][counter_2] ='1201'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] ='Анодирование \ Анодирование (Вход)'
                        df_new['BMSCH'][counter_2] = bmsch
                        df_new['MEINH'][counter_2] ='M2'
                        df_new['VGW01'][counter_2] ='1'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] ='200130'
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = '1000'
                        df_new['UMREN'][counter_2] = int(float(norma.data['Площадь поверхности 1000шт профилей/м²'].replace(',','.'))*float(L)/(6))
                        df_new['USR00'][counter_2] = '1'
                        df_new['USR01'][counter_2] = ("%.3f" % ((L*1000*3600*float(norma.data['Площадь поверхности 1000шт профилей/м²'].replace(',','.')))/(6000000*bmsch)))
                       
                    elif i7 == 3:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] ='0020'
                        df_new['ARBPL'][counter_2] ='1201A901'
                        df_new['WERKS1'][counter_2] ='1201'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] ='Анодирование \ Анодирование (Выход)'
                        df_new['BMSCH'][counter_2] = '1000'
                        df_new['MEINH'][counter_2] ='ST'
                        df_new['VGW01'][counter_2] ='1'
                        df_new['VGE01'][counter_2] ='S'
                        df_new['ACTTYPE_01'][counter_2] ='200130'
                        df_new['CKSELKZ'][counter_2] =''
                        df_new['UMREZ'][counter_2] = '1000'
                        df_new['UMREN'][counter_2] = '1000'
                        df_new['USR00'][counter_2] = '1'
                        df_new['USR01'][counter_2] = ("%.3f" % ((L*1000*3600*float(norma.data['Площадь поверхности 1000шт профилей/м²'].replace(',','.')))/(6000000*bmsch)))
                        
                    counter_2 +=1
                TexcartaBase(material = row['МАТЕРИАЛ']).save()
            elif '-S' in row['МАТЕРИАЛ']:
                for p in range(1,5):
                    for i7 in range(1,3):
                        if i7 ==1:
                            df_new['ID'][counter_2] ='1'
                            df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                            df_new['WERKS'][counter_2] ='1201'
                            df_new['STTAG'][counter_2] ='01012022'
                            df_new['PLNAL'][counter_2] ='1'
                            df_new['KTEXT'][counter_2] ='Сублимация'+' №'+str(p)+' \ Сублимирование'
                            df_new['VERWE'][counter_2] ='1'
                            df_new['STATU'][counter_2] ='4'
                            df_new['LOSVN'][counter_2] ='1'
                            df_new['LOSBS'][counter_2] ='99999999'
                        elif i7 == 2:
                            df_new['ID'][counter_2]='2'
                            df_new['VORNR'][counter_2] ='0010'
                            df_new['ARBPL'][counter_2] ='1201B20' + str(p)
                            df_new['WERKS1'][counter_2] ='1201'
                            df_new['STEUS'][counter_2] ='ZK01'
                            df_new['LTXA1'][counter_2] ='Сублимация'+' №'+str(p)+' \ Сублимирование'
                            df_new['BMSCH'][counter_2] = '61914'
                            df_new['MEINH'][counter_2] ='MM'
                            df_new['VGW01'][counter_2] ='1'
                            df_new['VGE01'][counter_2] ='STD'
                            df_new['ACTTYPE_01'][counter_2] ='200050'
                            df_new['CKSELKZ'][counter_2] ='X'
                            df_new['UMREZ'][counter_2] = '10'
                            df_new['UMREN'][counter_2] = int(float(norma.data['Внешний периметр профиля/ мм'].replace(',','.')) * 10)
                            df_new['USR00'][counter_2] = '1'
                            df_new['USR01'][counter_2] = '12'
                            
                        counter_2 +=1
                TexcartaBase(material = row['МАТЕРИАЛ']).save()
            elif '-E' in row['МАТЕРИАЛ']:
                for t in range(1,7):
                    for i7 in range(1,4):
                        if i7 ==1:
                            df_new['ID'][counter_2] ='1'
                            df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                            df_new['WERKS'][counter_2] ='1201'
                            df_new['STTAG'][counter_2] ='01012022'
                            df_new['PLNAL'][counter_2] ='1'
                            df_new['KTEXT'][counter_2] =BAZA['E'][f'{t}']['KTEXT'][0]
                            df_new['VERWE'][counter_2] ='1'
                            df_new['STATU'][counter_2] ='4'
                            df_new['LOSVN'][counter_2] ='1'
                            df_new['LOSBS'][counter_2] ='99999999'
                        elif i7 == 2:
                            df_new['ID'][counter_2]='2'
                            df_new['VORNR'][counter_2] =BAZA['E'][f'{t}']['VORNR'][0]
                            df_new['ARBPL'][counter_2] =BAZA['E'][f'{t}']['ARBPL'][0]
                            df_new['WERKS1'][counter_2] ='1201'
                            df_new['STEUS'][counter_2] ='ZK01'
                            df_new['LTXA1'][counter_2] =BAZA['E'][f'{t}']['LTXA1'][0]
                            df_new['BMSCH'][counter_2] = BAZA['E'][f'{t}']['BMSCH'][0]
                            df_new['MEINH'][counter_2] ='KG'
                            df_new['VGW01'][counter_2] ='1'
                            df_new['VGE01'][counter_2] ='STD'
                            df_new['ACTTYPE_01'][counter_2] ='200020'
                            df_new['CKSELKZ'][counter_2] ='X'
                            df_new['UMREZ'][counter_2] = '1000'
                            df_new['UMREN'][counter_2] = int(float(norma.data['Удельный вес профиля кг/м'].replace(',','.')) * float(L) *1000)
                            df_new['USR00'][counter_2] = '1'
                            df_new['USR01'][counter_2] = ("%.3f" % (float(norma.data['Удельный вес профиля кг/м'].replace(',','.')) * float(L) *3600/float(BAZA['E'][f'{t}']['BMSCH'][0])))
                            
                        elif i7 == 3:
                            df_new['ID'][counter_2]='2'
                            df_new['VORNR'][counter_2] =BAZA['E'][f'{t}']['VORNR'][1]
                            df_new['ARBPL'][counter_2] =BAZA['E'][f'{t}']['ARBPL'][1]
                            df_new['WERKS1'][counter_2] ='1201'
                            df_new['STEUS'][counter_2] ='ZK01'
                            df_new['LTXA1'][counter_2] =BAZA['E'][f'{t}']['LTXA1'][1]
                            df_new['BMSCH'][counter_2] = '620660'
                            df_new['MEINH'][counter_2] ='MM2'
                            df_new['VGW01'][counter_2] ='1'
                            df_new['VGE01'][counter_2] ='STD'
                            df_new['ACTTYPE_01'][counter_2] ='200020'
                            df_new['CKSELKZ'][counter_2] =''
                            df_new['UMREZ'][counter_2] = '10'
                            df_new['UMREN'][counter_2] = int(float(norma.data['Площадь /мм²'].replace(',','.')) * L * 10/(6))
                            df_new['USR00'][counter_2] = '1'
                            df_new['USR01'][counter_2] = '50'
                            
                        counter_2 +=1
                TexcartaBase(material = row['МАТЕРИАЛ']).save()             
            elif '-Z' in row['МАТЕРИАЛ']:
                for i7 in range(1,3):
                    if i7 ==1:
                        df_new['ID'][counter_2] ='1'
                        df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                        df_new['WERKS'][counter_2] ='1201'
                        df_new['STTAG'][counter_2] ='01012022'
                        df_new['PLNAL'][counter_2] ='1'
                        df_new['KTEXT'][counter_2] ='Печь старения (все) \ Термическая обработка (упрочение) алюм'
                        df_new['VERWE'][counter_2] ='1'
                        df_new['STATU'][counter_2] ='4'
                        df_new['LOSVN'][counter_2] ='1'
                        df_new['LOSBS'][counter_2] ='99999999'
                    elif i7 == 2:
                        df_new['ID'][counter_2]='2'
                        df_new['VORNR'][counter_2] ='0010'
                        df_new['ARBPL'][counter_2] ='1201A500'
                        df_new['WERKS1'][counter_2] ='1201'
                        df_new['STEUS'][counter_2] ='ZK01'
                        df_new['LTXA1'][counter_2] ='Печь старения (все) \ Термическая обработка (упрочение) алюм'
                        df_new['BMSCH'][counter_2] ='12500'
                        df_new['MEINH'][counter_2] ='KG'
                        df_new['VGW01'][counter_2] ='1'
                        df_new['VGE01'][counter_2] ='STD'
                        df_new['ACTTYPE_01'][counter_2] ='200030'
                        df_new['CKSELKZ'][counter_2] ='X'
                        df_new['UMREZ'][counter_2] = '1000'
                        df_new['UMREN'][counter_2] = int(float(norma.data['Удельный вес профиля кг/м'].replace(',','.')) * float(L) *1000)
                        df_new['USR00'][counter_2] = '1'
                        df_new['USR01'][counter_2] = ("%.3f" % (float(norma.data['Удельный вес профиля кг/м'].replace(',','.')) * float(L) *3600/(12500)))
                        
                    counter_2 +=1
                TexcartaBase(material = row['МАТЕРИАЛ']).save()
            elif '-P' in row['МАТЕРИАЛ']:
                for p in range(1,3):
                    for i in range(1,4):
                        if i ==1:
                            df_new['ID'][counter_2] ='1'
                            df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
                            df_new['WERKS'][counter_2] ='1201'
                            df_new['STTAG'][counter_2] ='01012022'
                            df_new['PLNAL'][counter_2] ='1'
                            df_new['KTEXT'][counter_2] =BAZA['P'][f'{p}']['KTEXT'][0]
                            df_new['VERWE'][counter_2] ='1'
                            df_new['STATU'][counter_2] ='4'
                            df_new['LOSVN'][counter_2] ='1'
                            df_new['LOSBS'][counter_2] ='99999999'
                        elif i == 2:
                            df_new['ID'][counter_2]='2'
                            df_new['VORNR'][counter_2] =BAZA['P'][f'{p}']['VORNR'][0]
                            df_new['ARBPL'][counter_2] =BAZA['P'][f'{p}']['ARBPL'][0]
                            df_new['WERKS1'][counter_2] ='1201'
                            df_new['STEUS'][counter_2] ='ZK01'
                            df_new['LTXA1'][counter_2] =BAZA['P'][f'{p}']['LTXA1'][0]
                            df_new['BMSCH'][counter_2] ='3600'
                            df_new['MEINH'][counter_2] ='KG'
                            df_new['VGW01'][counter_2] ='1'
                            df_new['VGE01'][counter_2] ='STD'
                            df_new['ACTTYPE_01'][counter_2] ='200040'
                            df_new['CKSELKZ'][counter_2] ='X'
                            df_new['UMREZ'][counter_2] = '1000'
                            df_new['UMREN'][counter_2] = int(float(norma.data['Удельный вес профиля кг/м'].replace(',','.')) * float(L) *1000)
                            df_new['USR00'][counter_2] = '1'
                            df_new['USR01'][counter_2] ='3'
                            
                        elif i == 3:
                            df_new['ID'][counter_2]='2'
                            df_new['VORNR'][counter_2] =BAZA['P'][f'{p}']['VORNR'][1]
                            df_new['ARBPL'][counter_2] =BAZA['P'][f'{p}']['ARBPL'][1]
                            df_new['WERKS1'][counter_2] ='1201'
                            df_new['STEUS'][counter_2] ='ZK01'
                            df_new['LTXA1'][counter_2] =BAZA['P'][f'{p}']['LTXA1'][1]
                            df_new['BMSCH'][counter_2] ='1000'
                            df_new['MEINH'][counter_2] ='ST'
                            df_new['VGW01'][counter_2] ='1'
                            df_new['VGE01'][counter_2] ='S'
                            df_new['ACTTYPE_01'][counter_2] ='200040'
                            df_new['CKSELKZ'][counter_2] =''
                            df_new['UMREZ'][counter_2] = '1000'
                            df_new['UMREN'][counter_2] = '1000'
                            df_new['USR00'][counter_2] = '1'
                            df_new['USR01'][counter_2] ='3'
                            
                        counter_2 +=1        
                TexcartaBase(material = row['МАТЕРИАЛ']).save()
    
    for i in range(0,counter_2):
        df_new['USR01'][i] = df_new['USR01'][i].replace('.',',')

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
            
    create_folder(f'{MEDIA_ROOT}\\uploads','texcarta_benkam')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta_benkam',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta_benkam\\{year}',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta_benkam\\{year}\\{month}',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta_benkam\\{year}\\{month}\\{day}',hour)
    
    path7 =f'{MEDIA_ROOT}\\uploads\\texcarta_benkam\\{year}\\{month}\\{day}\\{hour}\\TK_PRISVOENIYE_{s2}.txt'
    tk_prisvoeniye ={}
    header ='WERKS\tPLNNR\tPLNAL_02\tMATNR_02'
    tk_prisvoeniye['WERKS']=df_list_gp[0]
    tk_prisvoeniye['PLNNR']=df_list_gp[1]
    tk_prisvoeniye['PLNAL_02']=df_list_gp[2]
    tk_prisvoeniye['MATNR_02']=df_list_gp[3]
  
    
    df_tk_prisvoeniye= pd.DataFrame(tk_prisvoeniye)
    
    np.savetxt(path7, df_tk_prisvoeniye.values,fmt='%s', delimiter="\t",header=header,comments='',encoding='ansi')


    path2 =f'{MEDIA_ROOT}\\uploads\\texcarta_benkam\\{year}\\{month}\\{day}\\{hour}\\TK_{s2}.xlsx'
    writer = pd.ExcelWriter(path2, engine='xlsxwriter')
    df_new.to_excel(writer,index=False,sheet_name ='TEXCARTA')
    writer.close()

    # files =[File(file =path2,filetype='simple',id=1),File(file =path7,filetype='simple',id=2),]
    context ={
        'file1':path2,
        'file2':path7,
        'section':'Техкарта',

    }

   
    return render(request,'norma/benkam/generated_files_texcarta.html',context)


def download_txt(request):
    file_path = request.GET.get('file_path',None)
    if file_path:
        read_file = open(file_path, "r")
        response = HttpResponse(read_file.read(), content_type="text/plain,charset=utf8")
        read_file.close()

        response['Content-Disposition'] = 'attachment; filename="{}.txt"'.format('file_name')
        return response
    else:
        return JsonResponse({'msg':'File not found'})

@csrf_exempt
def bulk_delete_texcarta(request):
    ids = request.POST.get('ids',None)
    if ids:
        ids = ids.split(',')
        for id in ids:
            texcartaa= TexcartaBase.objects.get(id=id)
            texcartaa.delete()
    return JsonResponse({'msg':True})

@csrf_exempt
def delete_texcarta_one(request,id):
    if request.method =="POST":
        texcartaa= TexcartaBase.objects.get(id=int(id))
        texcartaa.delete()
        return JsonResponse({'msg':True})
    else:
        return JsonResponse({'msg':False})

def delete_anod(request,id):
    anod = Anod.objects.get(id=id)
    anod.delete()
    return redirect('anod_list')

def kraska_anod(request,id):
    kraska = Kraska.objects.get(id=id)
    kraska.delete()
    return redirect('kraska_list')

def nakleyka_del(request,id):
    nakleyka = Nakleyka.objects.get(id=id)
    nakleyka.delete()
    return redirect('nakleyka_list_benkam')

def sublimatsiya_del(request,id):
    sub = SubDekorPlonka.objects.get(id=id)
    sub.delete()
    return redirect('sublimatsiya_list_benkam')

def delete_texcarta(request):
    products = TexcartaBase.objects.all().order_by('-created_at')
    paginator = Paginator(products, 25)

    if request.GET.get('page') != None:
        page_number = request.GET.get('page')
    else:
        page_number=1

    page_obj = paginator.get_page(page_number)
    context ={
        'section':'Техкарта база',
        'products':page_obj,
    }
    return render(request,'norma/benkam/delete_texcarta.html',context)
