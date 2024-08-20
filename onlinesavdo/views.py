from django.shortcuts import render,redirect
from django.http import JsonResponse
import pandas as pd
from config.settings import MEDIA_ROOT
from aluminiy.models import LengthOfProfile,ExchangeValues
from functools import partial
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import FileForm,FileForm2
from accounts.models import User
from .models import OnlineSavdoOrder,OnlineSavdoFile
import os
from .utils import create_folder,zip
from accounts.decorators import allowed_users




class File:
    def __init__(self,id,file,filetype,created_at):
        self.id =id
        self.file =file
        self.filetype =filetype
        self.created_at = created_at

class FileG:
    def __init__(self,file,filetype):
        self.file =file
        self.filetype =filetype

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def upload_product_org(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
                new_order = form.save()
                files = [File(id=new_order.id,file = new_order.file,filetype = new_order.file_type,created_at=datetime.now())]
                context ={
                    'files':files,
                    'link':'generate-online-file/'
                }
                return render(request,'online_savdo/file_list.html',context)
    else:
        form =FileForm()
        context ={
        'form':form,
        'section':'Формирование сапкода обычный'
        }
    return render(request,'online_savdo/main.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def upload_sozdaniye(request):
    if request.method == 'POST':
        for f in request.FILES.getlist('file'):
            form_savdo = FileForm(request.POST, request.FILES)
            form_sozd = FileForm(request.POST, request.FILES)
        if form_savdo.is_valid() and form_sozd.is_valid():
                paths = []
                for f in request.FILES.getlist('file'):
                    file_instance = OnlineSavdoFile(file=f)
                    file_instance.save()
                    paths.append(file_instance.file)
                
                online_savdo_order = OnlineSavdoOrder()
                
                online_savdo_order.paths = { 'path_1' : str(paths[0]), 'path_2' : str(paths[1]) }
                online_savdo_order.save()

                files = [File(id=online_savdo_order.id,file = 'EXCELL FILES',filetype = 'savdo',created_at=datetime.now())]
                context ={
                    'files':files,
                    'link':'generate-sozdaniye-file/'
                }
                return render(request,'online_savdo/file_list.html',context)
    else:
        form_savdo = FileForm()
        form_sozd = FileForm()
        context ={
        'form_savdo':form_savdo,
        'form_sozd':form_sozd,
        'section':'Формирование'
        }
    return render(request,'online_savdo/sozdaniye_online_savdo.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def upload_sozdaniye_sena(request):
    if request.method == 'POST':
        form_savdo = FileForm(request.POST, request.FILES)
        form_sozd = FileForm(request.POST, request.FILES)
        if form_savdo.is_valid() and form_sozd.is_valid():
                paths = []
                for f in request.FILES.getlist('file'):
                    file_instance = OnlineSavdoFile(file=f)
                    file_instance.save()
                    paths.append(file_instance.file)

                online_savdo_order = OnlineSavdoOrder()
                online_savdo_order.paths = { 'path_1' : str(paths[0]), 'path_2' : str(paths[1]) }
                online_savdo_order.save()

                files = [File(id=online_savdo_order.id,file = 'EXCELL FILES',filetype = 'savdo',created_at=datetime.now())]
                context ={
                    'files':files,
                    'link':'generate-sozdaniye-sena/'
                }
                return render(request,'online_savdo/file_list.html',context)
    else:
        form_savdo = FileForm()
        form_sozd = FileForm()
        context ={
        'form_savdo':form_savdo,
        'form_sozd':form_sozd,
        'section':'Формирование'
        }
    return render(request,'online_savdo/sena.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def upload_sozdaniye_format(request):
    if request.method == 'POST':
        form1 = FileForm(request.POST, request.FILES)
        if form1.is_valid():
                new_order1 = form1.save()
                online_savdo_order = OnlineSavdoOrder()
                online_savdo_order.paths = { 
                    'path_1' : str(new_order1.file)
                      }
                online_savdo_order.save()

                files = [File(id=online_savdo_order.id,file = 'EXCELL FILES',filetype = 'savdo',created_at=datetime.now())]
                context ={
                    'files':files,
                    'link':'generate-sozdaniye-format/'
                }
                return render(request,'online_savdo/file_list.html',context)
    else:
        form1 = FileForm()
        context ={
        'form1':form1,
        'section':'Формирование'
        }
    return render(request,'online_savdo/sena_format.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def merging_files(request,id):
    file = OnlineSavdoFile.objects.get(id=id).file
    df = pd.read_excel(f'{MEDIA_ROOT}/{file}')
   
    df =df.astype(str)
    df = df.replace('nan','')
    df['SAP CODE']= ''
    df['KRATKIY TEXT']= ''

    for key,row in df.iterrows():
        if key ==1:
            df.at[0,'SAP CODE'] ='12345566'
            df.at[0,'KRATKIY TEXT'] ='MAXIMUM-GOODS'
        
        if (row[df.columns[0]]=='Id'):
            df.at[key,'SAP CODE'] = 'SAP CODE'
            df.at[key,'KRATKIY TEXT'] = 'KRATKIY TEXT'

        if (row[df.columns[0]]!='Id') and (row[df.columns[0]]!=''):
            df.at[key,'SAP CODE'] = key
            df.at[key,'KRATKIY TEXT'] = key
           
    zagolovok = list(df.columns)
    desired_order = zagolovok[:2] + zagolovok[-2:] +zagolovok[2:-2]
    
    df = df[desired_order]

    for i, col in enumerate(df.columns):
        if 'Unnamed: ' in col or 'SAP CODE' in col or 'KRATKIY TEXT' in col:
            df = df.rename(columns={col: ''})
    
   
    now =datetime.now()
    minut =now.strftime('%M-%S')
    pathtext1=f'{MEDIA_ROOT}/uploads/online_savdo/downloads/savdo_{minut}.xlsx'
    df.to_excel(pathtext1,index=False)
    files = [FileG(file=pathtext1,filetype='obichniy')]
    context = {
        'files':files
    }
    return render(request,'universal/generated_files.html',context)



@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def upload_file_for_preparing(request):
    if request.method == 'POST':
        form1 = FileForm(request.POST, request.FILES)
        if form1.is_valid():
            new_order1 = form1.save()
            online_savdo_order = OnlineSavdoOrder()
            online_savdo_order.paths = { 
                        'path_1' : str(new_order1.file)
                    }
            online_savdo_order.save()

            files = [File(id=new_order1.id,file = 'EXCELL FILES',filetype = 'savdo',created_at=datetime.now())]
            context ={
                'files':files,
                'link':'generate-merging-files/'
            }
            return render(request,'online_savdo/file_list.html',context)
    else:
        form1 = FileForm()
        context ={
            'form1':form1,
            'section':'Формирование'
        }
    return render(request,'online_savdo/sena_format.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def upload_for_proverka(request):
    if request.method == 'POST':
        form1 = FileForm(request.POST, request.FILES)
        if form1.is_valid():
                paths = {}
                for f in request.FILES.getlist('file'):
                    file_instance = OnlineSavdoFile(file=f)
                    file_instance.save()
                    file_name = str(file_instance.file)
                    if ('VK' in file_name and 'ZORN' in file_name):
                        paths['1'] = file_name
                    elif ('CHECK' in file_name and 'ZORN' in file_name):
                        paths['2'] = file_name

                    elif ('VK' in file_name and 'beznal' in file_name):
                        paths['3'] = file_name
                    elif ('CHECK' in file_name and 'BEZNAL' in file_name):
                        paths['4'] = file_name

                    elif ('VK' in file_name and 'ZUU' in file_name):
                        paths['5'] = file_name
                    elif ('CHECK' in file_name and 'ZUU' in file_name):
                        paths['6'] = file_name

                    elif ('VK' in file_name and 'ZFKN' in file_name):
                        paths['7'] = file_name
                    elif ('CHECK' in file_name and 'ZFKN' in file_name):
                        paths['8'] = file_name

                    elif ('VK' in file_name and 'zfdn' in file_name):
                        paths['9'] = file_name
                    elif ('CHECK' in file_name and 'ZFDN' in file_name):
                        paths['10'] = file_name

                    elif ('VK' in file_name and 'ZREN' in file_name):
                        paths['11'] = file_name
                    elif ('CHECK' in file_name and 'ZREN' in file_name):
                        paths['12'] = file_name
                

                online_savdo_order = OnlineSavdoOrder()
                online_savdo_order.paths = { 
                    'path_1' : str(paths['1']),
                    'path_2' : str(paths['2']),
                    'path_3' : str(paths['3']),
                    'path_4' : str(paths['4']),
                    'path_5' : str(paths['5']),
                    'path_6' : str(paths['6']),
                    'path_7' : str(paths['7']),
                    'path_8' : str(paths['8']),
                    'path_9' : str(paths['9']),
                    'path_10' : str(paths['10']),
                    'path_11' : str(paths['11']),
                    'path_12' : str(paths['12'])
                      }
                online_savdo_order.save()

                files = [File(id=online_savdo_order.id,file = 'EXCELL FILES',filetype = 'savdo',created_at=datetime.now())]
                context ={
                    'files':files,
                    'link':'generate-proverka-files/'
                }
                return render(request,'online_savdo/file_list.html',context)
    else:
        form1 = FileForm2()
        context ={
        'form1':form1,
        'section':'Формирование'
        }
    return render(request,'online_savdo/proverka.html',context)



def round50(n):
    return round(n, 0.01)

def round502(n):
    if str(n)=='':
        return ''
    return round(float(str(n).replace(',','.')), -2)

def round503(n):
    return round(n * 2, -2) // 2

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def create_online(request,id):
    file = OnlineSavdoFile.objects.get(id=id).file
    df = pd.read_excel(f'{MEDIA_ROOT}/{file}',sheet_name='Алюмин Навои Жомий',header=4)
    df = df[~df['Название системы'].isnull()]
    df =df.astype(str)

    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M")

    parent_dir =f'{MEDIA_ROOT}\\uploads\\online_savdo\\'
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads\\','online_savdo')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\',hour)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\','ONLINE')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\',minut)

    pathtext1 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\teams.xlsx'


    not_exists = [[],[]]
    all_corecct = True
    for key,row in df.iterrows():
        if not LengthOfProfile.objects.filter(artikul =row["Артикул"],length=row['Длина (мм)']).exists():
            not_exists[0].append(row["Артикул"])
            not_exists[1].append(row['Длина (мм)'])
            all_corecct = False

    if not all_corecct:
        new_not ={'Артикул':not_exists[0],'Длина (мм)':not_exists[1]} 
        new_df = pd.DataFrame(new_not)

        path =f'{MEDIA_ROOT}/uploads/online_savdo/not_exists.xlsx'

        new_df.to_excel(path,index=False)

        files = [FileG(file=path,filetype='obichniy')]
        context ={
            'files':files
        }
        return render(request,'universal/generated_files.html',context)

    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for key,row in df.iterrows():
        data[0].append(row["Название"])
        data[1].append(row["SAP Код вручную (вставится вручную)"])
        data[2].append(row["Группа"])
        data[3].append(row["Цвет продукта"])
        data[4].append(row["Группа закупок"])
        data[5].append(row["Сегмент"])
        data[6].append(row["Бухгалтерский товары"])
        data[7].append("Килограмм")
        data[8].append("Штука")
        data[9].append("Килограмм")
        data[10].append(1)
        ves_za_shtuk = LengthOfProfile.objects.filter(artikul =row["Артикул"],length=row['Длина (мм)'])[:1].get().ves_za_shtuk
        data[11].append(ves_za_shtuk)
        data[12].append("Пассивный")
        data[13].append(row["Завод TEX"])
        data[14].append(row["ONLINE ID"])
   
    new_row = {'ID' :data[14], 'NAME':data[0], 'SAPCODE':data[1],'GROUPNAME':data[2],'COLOR':data[3],'PURCHASING GROUP':data[4],'SEGMENT':data[5],'BUGALTER NAME':data[6],'BUGALTER UNIT':data[7],'BASE UNIT':data[8],'ALTER UNIT':data[9],'BASE UNITVAL':data[10],'ALTER UNITVAL':data[11],'STATUS':data[12],'FACTORY':data[13]}
    CS = pd.DataFrame(new_row)
    CS = CS.replace('nan','')
    CS.to_excel(pathtext1,index=False)
    files = [FileG(file=pathtext1,filetype='obichniy')]
    context ={
        'files':files
    }
    return render(request,'universal/generated_files.html',context)


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def sozdaniya_online_savdo(request,id):
    order = OnlineSavdoOrder.objects.get(id = id)
    path1 = order.paths['path_1']
    path2 = order.paths['path_2']
    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Алюмин Навои Жомий',header= 4)
    base = pd.read_excel(f'{MEDIA_ROOT}/{path2}',sheet_name='Sheet1',header= 2)
    # df1 = df1.astype(str)
    df1 = df1[~df1['Название системы'].isnull()]

    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M")

    parent_dir =f'{MEDIA_ROOT}\\uploads\\online_savdo\\'
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads\\','online_savdo')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\',hour)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\','ONLINE')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\',minut)

    pathtext1 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\teams3.xlsx'


    not_exists = [[],[]]
    all_corecct = True
    df1['Длина (мм)'].astype(str)
    for key,row in df1.iterrows():
        df1['Длина (мм)'] = df1['Длина (мм)'].replace('.0','')
        if not LengthOfProfile.objects.filter(artikul =row["Артикул"],length=df1['Длина (мм)'][key]).exists():
            not_exists[0].append(row["Артикул"])
            not_exists[1].append(row['Длина (мм)'])
            all_corecct = False
    all_corecct =True

    if not all_corecct:
        new_not ={'Артикул':not_exists[0],'Длина (мм)':not_exists[1]} 
        new_df = pd.DataFrame(new_not)

        path =f'{MEDIA_ROOT}/uploads/online_savdo/not_exists.xlsx'

        new_df.to_excel(path,index=False)

        files = [FileG(file=path,filetype='obichniy')]
        context ={
            'files':files
        }
        return render(request,'universal/generated_files.html',context)



    data =[[],[],[],[],[],[],[],[]] 
    PriceUSD = int(ExchangeValues.objects.get(id = 1).valute)
    df1['Длина (мм)'].astype(str)
    for key2,row2 in df1.iterrows():
        result = base[base['name'] ==row2['Название'] ]
        df1['Длина (мм)'] = df1['Длина (мм)'].replace('.0','')
        # print(result)
        data[0].append(result.iloc[0]['id'])
        data[1].append(result.iloc[0]['name'])
        data[2].append(row2['Тип клиента'])
        data[3].append("14.08.2023")
        if row2['Комбинация']=="Без термомоста":
                if row2['Тип покрытия']=="Неокрашенный":
                    price=5
                elif row2['Тип покрытия']=="Окрашенный":
                    price=5.8
                elif row2['Тип покрытия']=="Белый":
                    price=5.35   
                elif row2['Тип покрытия']=="Сублимированный":
                    price=6
                elif row2['Тип покрытия']=="Анодированный":
                    price=6
                elif row2['Тип покрытия']=="Ламинированный":
                    price=7
        elif row2['Комбинация']=="С термомостом":
                if row2['Тип покрытия']=="Неокрашенный":
                    price=5.4
                elif row2['Тип покрытия']=="Окрашенный":
                    price=6.2
                elif row2['Тип покрытия']=="Белый":
                    price=5.75
                elif row2['Тип покрытия']=="Сублимированный":
                    price=6.4
                elif row2['Тип покрытия']=="Анодированный":
                    price=6.4
                elif row2['Тип покрытия']=="Ламинированный":
                    price=7.4
        if row2['Базовый единица']=='КГ':
            t = 1
        else:
            print(row2["Артикул"],row2['Длина (мм)'])
            t = LengthOfProfile.objects.filter(artikul = row2["Артикул"],length = str(row2['Длина (мм)']).replace('.0',''))[:1].get().ves_za_shtuk
        
        data[5].append(round50(float(t)*(price)))
        data[4].append(round50(round50(float(t)*(price))/1.12))
        data[6].append("USD")
        data[7].append(row2['Базовый единица'])



    new_row = {'ID' :data[0], 'NAME':data[1], 'CLIENTYPE':data[2],'DATE':data[3],'COST':data[4],'RATE':data[5],'CURRENCY':data[6],'UNIT':data[7]}

    new_df =pd.DataFrame(new_row)

    new_df.to_excel(pathtext1,index=False)

    files = [FileG(file=pathtext1,filetype='obichniy')]
    context ={
        'files':files
    }
    return render(request,'universal/generated_files.html',context)



BUXPRICE = {
    'Профиль из ПВХ ламинированный':42896,
    'Подоконник из ПВХ ламинированный':27104,
    'Термоуплотненный окрашенный алюминиевый профиль':60592,
    'Анодированный алюминиевый профиль (N)':58800,
    'Профиль из ПВХ':22624,
    'Алюминиевый профиль':55216,
    'Неокрашенный алюминиевый профиль (N)':51296,
    'Алюминиевый профиль (N)':54544,
    'Термоуплотненный анодированный алюминиевый профиль (N)':63056,
    'Профиль ПВХ с уплотнителем':26432,
    'Ламинированный термоуплотненный алюминиевый профиль':72912,
    'Ламинированный алюминиевый профиль':71792,
    'Профиль из ПВХ ламинированный с уплотнителем':57456,
    'Ламинированный термоуплотненный алюминиевый профиль (N)':72912,
    'Алюминиевый профиль с декоративным покрытием  (N)':60480,
    'Алюминиевый профиль с декоративным покрытием':59360,
    'Профиль из ПВХ ламинированный (Engelberg)':45248,
    'Термоуплотненный алюминиевый профиль (N)':59920,
    'Неокрашенный алюминиевый профиль':44576,
    'Мебельный профиль из алюминия анодированный матовое серебро (N)':52528,
    'Подоконник из ПВХ':15792,
    'Ламбри из ПВХ ламинированный':36960,
    'Профиль из ПВХ (Engelberg)':38080,
    'Ламинированный алюминиевый профиль (N)':72912,
    'Ламбри из ПВХ':14672,
    'Дистанционная рамка ':70112,
    'Металлический усилитель':16688,
    'Уплотнитель для алюминиевых и ПВХ профилей':16576,

}
Segment1 = {
    'nan':"",
    'Аксессуар':0.065,
    'Стандарт':0.037,
    'Премиум':0.08,
    'Aldoks':0.037,
    'Эконом':0.037,
    'Mebel':0.03,
    'RETPEN 8-10%':0,
    'RETPEN 10-12%':0,
    'RETPEN 17%':0
}
Segment2 = {
    'nan':"",
    'Аксессуар':0.07,
    'Стандарт':0.047,
    'Премиум':0.08,
    'Aldoks':0.047,
    'Эконом':0.047,
    'Mebel':0.03,
    'RETPEN 8-10%':0,
    'RETPEN 10-12%':0,
    'RETPEN 17%':0
}
Segment3 = {
    'nan':"",
    'Аксессуар':0.07,
    'Стандарт':0.047,
    'Премиум':0.08,
    'Aldoks':0.047,
    'Эконом':0.047,
    'Mebel':0.03,
    'RETPEN 8-10%':0,
    'RETPEN 10-12%':0,
    'RETPEN 17%':0
}
Segment4 = {
    'nan':"",
    'Aldoks':0.05,
    'RETPEN 8-10%':0.08,
    'RETPEN 10-12%':0.1,
    'RETPEN 17%':0.17,
    'Премиум':0,
    'Стандарт':0,
    'Эконом':0,
    'Mebel':0
}
Segment5 = {
    'nan':"",
    'Aldoks':0.05,
    'RETPEN 8-10%':0.1,
    'RETPEN 10-12%':0.12,
    'RETPEN 17%':0.17,
    'Премиум':0,
    'Стандарт':0,
    'Эконом':0,
    'Mebel':0
}
Segment6 = {
    'nan':"",
    'Аксессуар':0.07,
    'Стандарт':0.047,
    'Премиум':0.08,
    'Aldoks':0.047,
    'Эконом':0.047,
    'RETPEN 8-10%':0,
    'RETPEN 10-12%':0,
    'RETPEN 17%':0,
    'Mebel':0
}
zavod = {
    'ZAVOD ALUMIN':'1100',
    'ZAVOD ALUMIN NAVOIY':'1200'
}

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def sozdaniye_sena(request,id):
    order = OnlineSavdoOrder.objects.get(id = id)
    path1 = order.paths['path_1']
    path2 = order.paths['path_2']
    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Алюмин Навои Жомий',header= 4)
    base = pd.read_excel(f'{MEDIA_ROOT}/{path2}',sheet_name='Sheet1',header= 2)
    df1 = df1[~df1['Название системы'].isnull()]

    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M")

    parent_dir =f'{MEDIA_ROOT}\\uploads\\online_savdo\\'
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads\\','online_savdo')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\',hour)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\','ONLINE')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\',minut)

    pathtext1 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\teams4.xlsx'
    DATA = ExchangeValues.objects.get(id = 1).start_data
    
    base = base.astype(str)
    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for key2,row2 in df1.iterrows():
        result = base[base['name'] ==row2['Название'] ]
        data[0].append(result.iloc[0]['id'])
        data[1].append(result.iloc[0]['name'])
        data[2].append(result.iloc[0]['group'])
        data[3].append(result.iloc[0]['sapcode'])   
        data[4].append(result.iloc[0]['alternate_unit_val'])
        data[5].append(result.iloc[0]['purchasing_group'])
        data[6].append(result.iloc[0]['segment'])
        data[7].append(result.iloc[0]['accounting_goods_name'])
        data[8].append(BUXPRICE[result.iloc[0]['accounting_goods_name']])
        data[9].append(DATA)
    
        data[10].append(Segment1[result.iloc[0]['segment']])
        data[11].append(Segment2[result.iloc[0]['segment']])
        data[12].append(Segment3[result.iloc[0]['segment']])
        data[13].append(Segment4[result.iloc[0]['segment']])
        data[14].append(Segment5[result.iloc[0]['segment']])
        data[15].append(Segment6[result.iloc[0]['segment']])
        data[16].append(zavod[result.iloc[0]['factory']])
        a=0
        if result.iloc[0]['akfa']!="nan":
            a=result.iloc[0]['akfa']
        elif result.iloc[0]['imzo']!="nan":
            a=result.iloc[0]['imzo']
        elif result.iloc[0]['franchising']!="nan":
            a=result.iloc[0]['franchising']
        data[17].append(float(a))
        data[18].append(row2['Базовый единица'])
        if Segment1[result.iloc[0]['segment']]==0:
            b4=''
            c4=''
            g4=''
            v4=''
        else:
            if row2['Базовый единица']=='КГ':
                t=1
            else:
                t=float(result.iloc[0]['alternate_unit_val'])         
            b4=float(a)-float(a)*Segment1[result.iloc[0]['segment']]
            c4=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))
            g4=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))*1.12
            v4=(float(a)-float(a)*Segment1[result.iloc[0]['segment']])-(round502((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12)*1.12)
        data[19].append(b4)   
        data[20].append(c4)
        data[21].append(g4)
        data[22].append(v4)
        data[23].append("")
        if Segment2[result.iloc[0]['segment']]==0:
            b3=''
            c3=''
            g3=''
            v3=''
        else:
            if row2['Базовый единица']=='КГ':
                t=1
            else:
                t=float(result.iloc[0]['alternate_unit_val'])      
            b3=float(a)-float(a)*Segment2[result.iloc[0]['segment']]
            c3=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))
            g3=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))*1.12
            v3=(float(a)-float(a)*Segment2[result.iloc[0]['segment']])-(round502((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12)*1.12)
        data[24].append(b3)   
        data[25].append(c3)
        data[26].append(g3)
        data[27].append(v3)
        data[28].append("")
        if Segment3[result.iloc[0]['segment']]==0:
            b2=''
            c2=''
            g2=''
            v2=''
        else:
            if row2['Базовый единица']=='КГ':
                t=1
            else:
                t=float(result.iloc[0]['alternate_unit_val'])
            b2=float(a)-float(a)*Segment3[result.iloc[0]['segment']]
            c2=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))
            g2=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))*1.12
            v2=(float(a)-float(a)*Segment3[result.iloc[0]['segment']])-(round502((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12)*1.12)
        data[29].append(b2)   
        data[30].append(c2)
        data[31].append(g2)
        data[32].append(v2)
        data[33].append("")
        
        if Segment4[result.iloc[0]['segment']]==0:
            b=''
            c=''
            g=''
            v=''
        else:
            if row2['Базовый единица']=='КГ':
                t=1
            else:
                t=float(result.iloc[0]['alternate_unit_val'])
            b=float(a)-float(a)*Segment4[result.iloc[0]['segment']]
            c=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))
            g=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))*1.12
            v=(float(a)-float(a)*Segment4[result.iloc[0]['segment']])-(round502((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12)*1.12)
        data[34].append(b)   
        data[35].append(c)
        data[36].append(g)
        data[37].append(v)
        data[38].append("")
        if Segment5[result.iloc[0]['segment']]==0:
            b1=''
            c1=''
            g1=''
            v1=''
        else:
            if row2['Базовый единица']=='КГ':
                t=1
            else:
                t=float(result.iloc[0]['alternate_unit_val'])
            b1=float(a)-float(a)*Segment5[result.iloc[0]['segment']]
            c1=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))
            g1=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))*1.12
            v1=(float(a)-float(a)*Segment5[result.iloc[0]['segment']])-(round502((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12)*1.12)
        data[39].append(b1)   
        data[40].append(c1)
        data[41].append(g1)
        data[42].append(v1)
        data[43].append("")
        if Segment6[result.iloc[0]['segment']]==0:
            b5=''
            c5=''
            g5=''
            v5=''
        else:
            if row2['Базовый единица']=='КГ':
                t=1
            else:
                t=float(result.iloc[0]['alternate_unit_val'])
            b5=float(a)-float(a)*Segment6[result.iloc[0]['segment']]
            c5=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))
            g5=round502(int((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12))*1.12
            v5=(float(a)-float(a)*Segment6[result.iloc[0]['segment']])-(round502((t*float(BUXPRICE[result.iloc[0]['accounting_goods_name']]))/1.12)*1.12)
        data[44].append(b5)   
        data[45].append(c5)
        data[46].append(g5)
        data[47].append(v5)
        

    new_row = {'id':data[0],
            'name':data[1],	
            'group':data[2],	
            'sapcode':data[3],	
            'alternate_unit_val':data[4],	
            'purchasing_group':data[5],	
            'segment':data[6],	
            'accounting_goods_name':data[7],	
            'цена с ндс':data[8],	
            'Дата':data[9],	
            'Shaxar diler uchun narx segmentli (Angren+Bekobod+Chirchiq)':data[10],
            'Shaxar diler (Yangiyul,Olmaliq,Guliston,Bo`ka) uchun narx segmentli':data[11],	
            'Viloyat diler uchun narx segmentli':data[12],	
            'Retpen diler (Nukus (Maxmud), Xorazm (Shixnazar),Namangan-1 ,Farg`ona (Shuhrat Aka),Andijon-3 (Azizbek) uchun narx segmentli':data[13],	
            'Retpen diler uchun narx segmentli':data[14],	
            'Imzo/Franshiza diler uchun narx segmentli':data[15],	
            'Сбытовая организация':data[16],	
            'akfa':data[17],	
            'Ед.изм':data[18],	
            'Shaxar diler uchun narx segmentli D1':data[19],	
            '70% без ндс безнал (цена для выгрузуа SAP) D1':data[20],	
            '70% с ндс безнал ( 12% ндс плюсуются после деблокирование сч/ф ) D1':data[21],	
            '30% Наличка D1':data[22],	
            'D1':data[23],	
            'Shaxar diler (Yangiyul,Olmaliq,Angren,Guliston,Bekobod,Bo`ka,Chirchiq) uchun narx segmentli D2':data[24],	
            '70% без ндс безнал (цена для выгрузуа SAP) D2':data[25],	
            '70% с ндс безнал ( 12% ндс плюсуются после деблокирование сч/ф ) D2':data[26],	
            '30% Наличка D2':data[27],	
            'D2':data[28],	
            'Viloyat diler uchun narx segmentli D3':data[29],	
            '70% без ндс безнал (цена для выгрузуа SAP) D3':data[30],	
            '70% с ндс безнал ( 12% ндс плюсуются после деблокирование сч/ф ) D3':data[31],
            '30% Наличка D3':data[32],	
            'D3':data[33],
            'Retpen diler (Nukus (Maxmud), Xorazm (Shixnazar),Namangan-1 ,Farg`ona (Shuhrat Aka),Andijon-3 (Azizbek) uchun narx segmentli D4':data[34],
            '70% без ндс безнал (цена для выгрузуа SAP) D4':data[35],	
            '70% с ндс безнал ( 12% ндс плюсуются после деблокирование сч/ф ) D4':data[36],	
            '30% Наличка D4':data[37],	
            'D4':data[38],	
            'Retpen diler uchun narx segmentli D5':data[39],	
            '70% без ндс безнал (цена для выгрузуа SAP) D5':data[40],	
            '70% с ндс безнал ( 12% ндс плюсуются после деблокирование сч/ф ) D5':data[41],	
            '30% Наличка D5':data[42],	
            'D5':data[43],	
            'Imzo/Franshiza diler uchun narx segmentli D6':data[44],	
            '70% без ндс безнал (цена для выгрузуа SAP) D6':data[45],	
            '70% с ндс безнал ( 12% ндс плюсуются после деблокирование сч/ф ) D6':data[46],	
            '30% Наличка D6':data[47]
    }

    new_df =pd.DataFrame(new_row)
    new_df =new_df.replace(0,'')
    

    new_df.to_excel(pathtext1,index=False)

    files = [FileG(file=pathtext1,filetype='obichniy')]
    context ={
        'files':files
    }
    return render(request,'universal/generated_files.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def sozdaniye_sap_format_sena(request,id):
    order = OnlineSavdoOrder.objects.get(id = id)
    path1 = order.paths['path_1']

    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)

    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M%S")

    parent_dir =f'{MEDIA_ROOT}\\uploads\\online_savdo\\'
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads\\','online_savdo')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\',hour)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\','ONLINE')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\',minut)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}','FORMAT')

    pathtext1 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT\\VK_11_1vid torg dokument ZORN 1.xlsx'
    pathtext2 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT\\VK_11_1vid torg dokument ZREN 1.xlsx'
    pathtext3 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT\\VK_11_3beznal tayyor 1.xlsx'
    pathtext4 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT\\VK_11_2prichina zakaza (ZUU) tayyor 1.xlsx'
    pathtext5 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT\\VK_11zfdn (ALUMIN) tayyor 1 ZFKN.xlsx'
    pathtext6 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT\\VK_11zfdn (ALUMIN) tayyor 1.xlsx'
    pathzip =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT'
    
    exchange_val = ExchangeValues.objects.get(id = 1)
    DATAB = exchange_val.start_data
    DATBI = exchange_val.end_data

    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(1,8):
        for key2,row2 in df1.iterrows():
            d='D'+str(i)
            data[0].append("PR00")
            data[1].append(row2["Сбытовая организация"])
            data[2].append("")
            data[3].append("10")
            data[4].append(d)
            data[5].append(row2["sapcode"])
            if i==1:
                k=row2["Shaxar diler uchun narx segmentli D1"]
            elif i==2:
                k=row2["Shaxar diler (Yangiyul,Olmaliq,Angren,Guliston,Bekobod,Bo`ka,Chirchiq) uchun narx segmentli D2"]
            elif i==3:
                k=row2["Viloyat diler uchun narx segmentli D3"]
            elif i==4:
                k=row2["Retpen diler (Nukus (Maxmud), Xorazm (Shixnazar),Namangan-1 ,Farg`ona (Shuhrat Aka),Andijon-3 (Azizbek) uchun narx segmentli D4"]
            elif i==5:
                k=row2["Retpen diler uchun narx segmentli D5"]
            elif i==6:
                k=row2["Imzo/Franshiza diler uchun narx segmentli D6"]
            elif i==7:
                k=row2["Imzo/Franshiza diler uchun narx segmentli D6"]
            data[6].append(k)
            data[7].append("UZS")
            data[8].append(1)
            data[9].append(row2["Ед.изм"])
            data[10].append(DATAB)
            data[11].append(DATBI)
            data[12].append("")
            data[13].append("")
            data[14].append("ZORN")
            data[15].append("")
    new_row = { 'KSCHL':data[0],	
                'VKORG':data[1],	
                'WERKS':data[2],	
                'VTWEG':data[3],	
                'KONDA':data[4],	
                'MATNR':data[5],	
                'KBETR':data[6],	
                'KONWA':data[7],	
                'KPEIN':data[8],	
                'KMEIN':data[9],	
                'DATAB':data[10],	
                'DATBI':data[11],	
                'KUNNR':data[12],	
                'FKART':data[13],	
                'AUART':data[14],	
                'AUGRU':data[15]
            }

    new_df =pd.DataFrame(new_row)

    new_df =new_df[~pd.isna(new_df['KBETR'])]


    new_df.to_excel(pathtext1,index=False)



    #####################2 excell#################
    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)

    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(1,8):
        for key2,row2 in df1.iterrows():
            d='D'+str(i)
            data[0].append("PR00")
            data[1].append(row2["Сбытовая организация"])
            data[2].append("")
            data[3].append("10")
            data[4].append(d)
            data[5].append(row2["sapcode"])
            if i==1:
                k=row2["Shaxar diler uchun narx segmentli D1"]
            elif i==2:
                k=row2["Shaxar diler (Yangiyul,Olmaliq,Angren,Guliston,Bekobod,Bo`ka,Chirchiq) uchun narx segmentli D2"]
            elif i==3:
                k=row2["Viloyat diler uchun narx segmentli D3"]
            elif i==4:
                k=row2["Retpen diler (Nukus (Maxmud), Xorazm (Shixnazar),Namangan-1 ,Farg`ona (Shuhrat Aka),Andijon-3 (Azizbek) uchun narx segmentli D4"]
            elif i==5:
                k=row2["Retpen diler uchun narx segmentli D5"]
            elif i==6:
                k=row2["Imzo/Franshiza diler uchun narx segmentli D6"]
            elif i==7:
                k=row2["Imzo/Franshiza diler uchun narx segmentli D6"]
            data[6].append(k)
            data[7].append("UZS")
            data[8].append(1)
            data[9].append(row2["Ед.изм"])
            data[10].append(DATAB)
            data[11].append(DATBI)
            data[12].append("")
            data[13].append("")
            data[14].append("ZREN")
            data[15].append("")
        
    new_row = {'KSCHL':data[0],	
            'VKORG':data[1],	
            'WERKS':data[2],	
            'VTWEG':data[3],	
            'KONDA':data[4],	
            'MATNR':data[5],	
            'KBETR':data[6],	
            'KONWA':data[7],	
            'KPEIN':data[8],	
            'KMEIN':data[9],	
            'DATAB':data[10],	
            'DATBI':data[11],	
            'KUNNR':data[12],	
            'FKART':data[13],	
            'AUART':data[14],	
            'AUGRU':data[15]
    }

    new_df =pd.DataFrame(new_row)
    new_df =new_df[~pd.isna(new_df['KBETR'])]
    new_df.to_excel(pathtext2,index=False)

    ###################### 3 ######################

    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)


    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(1,8):
        for key2,row2 in df1.iterrows():
            d='D'+str(i)
            data[0].append("PR00")
            data[1].append(row2["Сбытовая организация"])
            data[2].append("")
            data[3].append("10")
            data[4].append(d)
            data[5].append(row2["sapcode"])
            if i==1:
                k=row2["Shaxar diler uchun narx segmentli D1"]
            elif i==2:
                k=row2["Shaxar diler (Yangiyul,Olmaliq,Angren,Guliston,Bekobod,Bo`ka,Chirchiq) uchun narx segmentli D2"]
            elif i==3:
                k=row2["Viloyat diler uchun narx segmentli D3"]
            elif i==4:
                k=row2["Retpen diler (Nukus (Maxmud), Xorazm (Shixnazar),Namangan-1 ,Farg`ona (Shuhrat Aka),Andijon-3 (Azizbek) uchun narx segmentli D4"]
            elif i==5:
                k=row2["Retpen diler uchun narx segmentli D5"]
            elif i==6:
                k=row2["Imzo/Franshiza diler uchun narx segmentli D6"]
            elif i==7:
                k=row2["Imzo/Franshiza diler uchun narx segmentli D6"]
            data[6].append(k)
            data[7].append("UZS")
            data[8].append(1)
            data[9].append(row2["Ед.изм"])
            data[10].append(DATAB)
            data[11].append(DATBI)
            data[12].append("")
            data[13].append("")
            data[14].append("")
            data[15].append("")
        
    new_row = {'KSCHL':data[0],	
            'VKORG':data[1],	
            'WERKS':data[2],	
            'VTWEG':data[3],	
            'KONDA':data[4],	
            'MATNR':data[5],	
            'KBETR':data[6],	
            'KONWA':data[7],	
            'KPEIN':data[8],	
            'KMEIN':data[9],	
            'DATAB':data[10],	
            'DATBI':data[11],	
            'KUNNR':data[12],	
            'FKART':data[13],	
            'AUART':data[14],	
            'AUGRU':data[15]
    }


    new_df =pd.DataFrame(new_row)
    new_df =new_df[~pd.isna(new_df['KBETR'])]
    new_df.to_excel(pathtext3,index=False)

    ############## 4 ##########################

    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)


    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(1,8):
        for key2,row2 in df1.iterrows():
            d='D'+str(i)
            data[0].append("PR00")
            data[1].append(row2["Сбытовая организация"])
            data[2].append("")
            data[3].append("10")
            data[4].append(d)
            data[5].append(row2["sapcode"])
            if i==1:
                k=row2["70% без ндс безнал (цена для выгрузуа SAP) D1"]
            elif i==2:
                k=row2["70% без ндс безнал (цена для выгрузуа SAP) D2"]
            elif i==3:
                k=row2["70% без ндс безнал (цена для выгрузуа SAP) D3"]
            elif i==4:
                k=row2["70% без ндс безнал (цена для выгрузуа SAP) D4"]
            elif i==5:
                k=row2["70% без ндс безнал (цена для выгрузуа SAP) D5"]
            elif i==6:
                k=row2["70% без ндс безнал (цена для выгрузуа SAP) D6"]
            elif i==7:
                k=row2["70% без ндс безнал (цена для выгрузуа SAP) D6"]
            data[6].append(k)
            data[7].append("UZS")
            data[8].append(1)
            data[9].append(row2["Ед.изм"])
            data[10].append(DATAB)
            data[11].append(DATBI)
            data[12].append("")
            data[13].append("")
            data[14].append("")
            data[15].append("ZUU")
        
    new_row = {'KSCHL':data[0],	
            'VKORG':data[1],	
            'WERKS':data[2],	
            'VTWEG':data[3],	
            'KONDA':data[4],	
            'MATNR':data[5],	
            'KBETR':data[6],	
            'KONWA':data[7],	
            'KPEIN':data[8],	
            'KMEIN':data[9],	
            'DATAB':data[10],	
            'DATBI':data[11],	
            'KUNNR':data[12],	
            'FKART':data[13],	
            'AUART':data[14],	
            'AUGRU':data[15]
    }

    new_df =pd.DataFrame(new_row)
    new_df =new_df[~pd.isna(new_df['KBETR'])]

    new_df.to_excel(pathtext4,index=False)

    ################ 5 #######################

    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)


    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(1,8):
        for key2,row2 in df1.iterrows():
            d='D'+str(i)
            data[0].append("PR00")
            data[1].append(row2["Сбытовая организация"])
            data[2].append("")
            data[3].append("10")
            data[4].append(d)
            data[5].append(row2["sapcode"])
            if i==1:
                k=row2["30% Наличка D1"]
            elif i==2:
                k=row2["30% Наличка D2"]
            elif i==3:
                k=row2["30% Наличка D3"]
            elif i==4:
                k=row2["30% Наличка D4"]
            elif i==5:
                k=row2["30% Наличка D5"]
            elif i==6:
                k=row2["30% Наличка D6"]
            elif i==7:
                k=row2["30% Наличка D6"]
            data[6].append(k)
            data[7].append("UZS")
            data[8].append(1)
            data[9].append(row2["Ед.изм"])
            data[10].append(DATAB)
            data[11].append(DATBI)
            data[12].append("")
            data[13].append("ZFKN")
            data[14].append("")
            data[15].append("")
        
    new_row = {'KSCHL':data[0],	
            'VKORG':data[1],	
            'WERKS':data[2],	
            'VTWEG':data[3],	
            'KONDA':data[4],	
            'MATNR':data[5],	
            'KBETR':data[6],	
            'KONWA':data[7],	
            'KPEIN':data[8],	
            'KMEIN':data[9],	
            'DATAB':data[10],	
            'DATBI':data[11],	
            'KUNNR':data[12],	
            'FKART':data[13],	
            'AUART':data[14],	
            'AUGRU':data[15]
    }


    new_df =pd.DataFrame(new_row)
    new_df =new_df[~pd.isna(new_df['KBETR'])]
    new_df.to_excel(pathtext5,index=False)

    ################ 6 ###################

    
    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)


    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(1,8):
        for key2,row2 in df1.iterrows():
            d='D'+str(i)
            data[0].append("PR00")
            data[1].append(row2["Сбытовая организация"])
            data[2].append("")
            data[3].append("10")
            data[4].append(d)
            data[5].append(row2["sapcode"])
            if i==1:
                k=row2["30% Наличка D1"]
            elif i==2:
                k=row2["30% Наличка D2"]
            elif i==3:
                k=row2["30% Наличка D3"]
            elif i==4:
                k=row2["30% Наличка D4"]
            elif i==5:
                k=row2["30% Наличка D5"]
            elif i==6:
                k=row2["30% Наличка D6"]
            elif i==7:
                k=row2["30% Наличка D6"]
            data[6].append(k)
            data[7].append("UZS")
            data[8].append(1)
            data[9].append(row2["Ед.изм"])
            data[10].append(DATAB)
            data[11].append(DATBI)
            data[12].append("")
            data[13].append("ZFDN")
            data[14].append("")
            data[15].append("")
        
    new_row = {'KSCHL':data[0],	
            'VKORG':data[1],	
            'WERKS':data[2],	
            'VTWEG':data[3],	
            'KONDA':data[4],	
            'MATNR':data[5],	
            'KBETR':data[6],	
            'KONWA':data[7],	
            'KPEIN':data[8],	
            'KMEIN':data[9],	
            'DATAB':data[10],	
            'DATBI':data[11],	
            'KUNNR':data[12],	
            'FKART':data[13],	
            'AUART':data[14],	
            'AUGRU':data[15]
    }

    new_df =pd.DataFrame(new_row)
    new_df =new_df[~pd.isna(new_df['KBETR'])]

    new_df.to_excel(pathtext6,index=False)




    file_path =f'{pathzip}.zip'

    zip(pathzip, pathzip)
    

    files = [FileG(file=file_path,filetype='obichniy')]
    context ={
        'files':files
    }
    return render(request,'online_savdo/zip_file_download.html',context)
  
   
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def proverka(request,id):
    order = OnlineSavdoOrder.objects.get(id = id)
    path1 = order.paths['path_1']
    path2 = order.paths['path_2']
    path3 = order.paths['path_3']
    path4 = order.paths['path_4']
    path5 = order.paths['path_5']
    path6 = order.paths['path_6']
    path7 = order.paths['path_7']
    path8 = order.paths['path_8']
    path9 = order.paths['path_9']
    path10 = order.paths['path_10']
    path11 = order.paths['path_11']
    path12 = order.paths['path_12']

    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M%S%S")

    parent_dir =f'{MEDIA_ROOT}\\uploads\\online_savdo\\'
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads\\','online_savdo')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\',hour)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\','ONLINE')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\',minut)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}','PROVERKA')

    pathtext1 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\ZORN ERROR.xlsx'
    pathtext2 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\БЕЗНАЛ ERROR.xlsx'
    pathtext3 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\ZUU ERROR.xlsx'
    pathtext4 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\ZFKN ERROR.xlsx'
    pathtext5 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\ZFDN ERROR.xlsx'
    pathtext6 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA\\ZREN ERROR.xlsx'
    pathzip =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PROVERKA'

    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)

    to_datetime_fmt = partial(pd.to_datetime, format='%d.%m.%Y')

    df1['DATAB'] = df1['DATAB'].apply(to_datetime_fmt)

    df1 = df1.astype(str)
    df1['joined_data']= df1['VKORG'] + df1['KONDA'] + df1['MATNR'] +df1['DATAB']

    # print(df1['joined_data'])

    df2 = pd.read_excel(f'{MEDIA_ROOT}/{path2}',sheet_name='Sheet1',header=0)

    df2 = df2.astype(str)
    df2['joined_data']= df2['Сбытовая организация'] + df2['Группа цен клиента'] + df2['Материал'] +df2['Действ. с']

    # print(df2['joined_data'])
    nesovpaden_datas =[[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[],[],[],[]]

    for key1,row1 in df1.iterrows():
        result = df2[df2['joined_data'] == row1['joined_data'] ]
        result['Сумма']=result['Сумма'].astype(float)
        row1['KBETR']= float(row1['KBETR'])
        
        result2 =result[result['Сумма'] == row1['KBETR']]
        if result2.empty:
            nesovpaden_datas[0].append(row1['KSCHL'])
            nesovpaden_datas[1].append(row1['VKORG'])
            nesovpaden_datas[2].append(row1['WERKS'])
            nesovpaden_datas[3].append(row1['VTWEG'])
            nesovpaden_datas[4].append(row1['KONDA'])
            nesovpaden_datas[5].append(row1['MATNR'])
            nesovpaden_datas[6].append(row1['KBETR'])
            nesovpaden_datas[7].append(row1['KONWA'])
            nesovpaden_datas[8].append(row1['KPEIN'])
            nesovpaden_datas[9].append(row1['KMEIN'])
            nesovpaden_datas[10].append(row1['DATAB'])
            nesovpaden_datas[11].append(row1['DATBI'])
            nesovpaden_datas[12].append(row1['KUNNR'])
            nesovpaden_datas[13].append(row1['FKART'])
            nesovpaden_datas[14].append(row1['AUART'])
            nesovpaden_datas[15].append(row1['AUGRU'])
            # nesovpaden_datas[16].append(result.iloc[0]['Сумма'])
        else:
            pass

    df_nesovpa =pd.DataFrame({
    'KSCHL':nesovpaden_datas[0],
    'VKORG':nesovpaden_datas[1],
    'WERKS':nesovpaden_datas[2],
    'VTWEG':nesovpaden_datas[3],
    'KONDA':nesovpaden_datas[4],
    'MATNR':nesovpaden_datas[5],
    'KBETR':nesovpaden_datas[6],
    'KONWA':nesovpaden_datas[7],
    'KPEIN':nesovpaden_datas[8],
    'KMEIN':nesovpaden_datas[9],
    'DATAB':nesovpaden_datas[10],
    'DATBI':nesovpaden_datas[11],
    'KUNNR':nesovpaden_datas[12],
    'FKART':nesovpaden_datas[13],
    'AUART':nesovpaden_datas[14],
    'AUGRU':nesovpaden_datas[15],
    # 'ERROR':nesovpaden_datas[16]

    })
    df_nesovpa =df_nesovpa.replace('nan','')

    if not df_nesovpa.empty:
        df_nesovpa.to_excel(pathtext1)

    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path3}',sheet_name='Sheet1',header=0)

    to_datetime_fmt = partial(pd.to_datetime, format='%d.%m.%Y')

    df1['DATAB'] = df1['DATAB'].apply(to_datetime_fmt)
    df1 = df1.astype(str)
    df1['joined_data']= df1['VKORG'] + df1['KONDA'] + df1['MATNR'] +df1['DATAB']

    # print(df1['joined_data'])

    df2 = pd.read_excel(f'{MEDIA_ROOT}/{path4}',sheet_name='Sheet1',header=0)

    df2 = df2.astype(str)
    df2['joined_data']= df2['Сбытовая организация'] + df2['Группа цен клиента'] + df2['Материал'] +df2['Действ. с']

    # print(df2['joined_data'])
    nesovpaden_datas =[[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[],[],[],[]]

    for key1,row1 in df1.iterrows():
        result = df2[df2['joined_data'] == row1['joined_data'] ]
        result['Сумма'] = result['Сумма'].astype(float)
        row1['KBETR'] = float(row1['KBETR'])
        
        result2 =result[result['Сумма'] == row1['KBETR']]
        if result2.empty:
            nesovpaden_datas[0].append(row1['KSCHL'])
            nesovpaden_datas[1].append(row1['VKORG'])
            nesovpaden_datas[2].append(row1['WERKS'])
            nesovpaden_datas[3].append(row1['VTWEG'])
            nesovpaden_datas[4].append(row1['KONDA'])
            nesovpaden_datas[5].append(row1['MATNR'])
            nesovpaden_datas[6].append(row1['KBETR'])
            nesovpaden_datas[7].append(row1['KONWA'])
            nesovpaden_datas[8].append(row1['KPEIN'])
            nesovpaden_datas[9].append(row1['KMEIN'])
            nesovpaden_datas[10].append(row1['DATAB'])
            nesovpaden_datas[11].append(row1['DATBI'])
            nesovpaden_datas[12].append(row1['KUNNR'])
            nesovpaden_datas[13].append(row1['FKART'])
            nesovpaden_datas[14].append(row1['AUART'])
            nesovpaden_datas[15].append(row1['AUGRU'])
            nesovpaden_datas[16].append(result.iloc[0]['Сумма'])
            # print(result,'nesovpaden')
        else:
            pass
            # print(result2,'sovpaden')

    df_nesovpa =pd.DataFrame({
    'KSCHL':nesovpaden_datas[0],
    'VKORG':nesovpaden_datas[1],
    'WERKS':nesovpaden_datas[2],
    'VTWEG':nesovpaden_datas[3],
    'KONDA':nesovpaden_datas[4],
    'MATNR':nesovpaden_datas[5],
    'KBETR':nesovpaden_datas[6],
    'KONWA':nesovpaden_datas[7],
    'KPEIN':nesovpaden_datas[8],
    'KMEIN':nesovpaden_datas[9],
    'DATAB':nesovpaden_datas[10],
    'DATBI':nesovpaden_datas[11],
    'KUNNR':nesovpaden_datas[12],
    'FKART':nesovpaden_datas[13],
    'AUART':nesovpaden_datas[14],
    'AUGRU':nesovpaden_datas[15],
    'ERROR':nesovpaden_datas[16]

    })
    df_nesovpa =df_nesovpa.replace('nan','')
    
    if not df_nesovpa.empty:
        df_nesovpa.to_excel(pathtext2)
    

    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path5}',sheet_name='Sheet1',header=0)

    to_datetime_fmt = partial(pd.to_datetime, format='%d.%m.%Y')

    df1['DATAB'] = df1['DATAB'].apply(to_datetime_fmt)
    df1 = df1.astype(str)
    df1['joined_data']= df1['VKORG'] + df1['KONDA'] + df1['MATNR'] +df1['DATAB']

    # print(df1['joined_data'])

    df2 = pd.read_excel(f'{MEDIA_ROOT}/{path6}',sheet_name='Sheet1',header=0)

    df2 = df2.astype(str)
    df2['joined_data']= df2['Сбытовая организация'] + df2['Группа цен клиента'] + df2['Материал'] +df2['Действ. с']

    # print(df2['joined_data'])
    nesovpaden_datas =[[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[],[],[],[]]

    for key1,row1 in df1.iterrows():
        result = df2[df2['joined_data'] == row1['joined_data'] ]
        result['Сумма']=result['Сумма'].astype(float)
        row1['KBETR']= float(row1['KBETR'])
        
        result2 =result[result['Сумма'] == row1['KBETR']]
        if result2.empty:
            nesovpaden_datas[0].append(row1['KSCHL'])
            nesovpaden_datas[1].append(row1['VKORG'])
            nesovpaden_datas[2].append(row1['WERKS'])
            nesovpaden_datas[3].append(row1['VTWEG'])
            nesovpaden_datas[4].append(row1['KONDA'])
            nesovpaden_datas[5].append(row1['MATNR'])
            nesovpaden_datas[6].append(row1['KBETR'])
            nesovpaden_datas[7].append(row1['KONWA'])
            nesovpaden_datas[8].append(row1['KPEIN'])
            nesovpaden_datas[9].append(row1['KMEIN'])
            nesovpaden_datas[10].append(row1['DATAB'])
            nesovpaden_datas[11].append(row1['DATBI'])
            nesovpaden_datas[12].append(row1['KUNNR'])
            nesovpaden_datas[13].append(row1['FKART'])
            nesovpaden_datas[14].append(row1['AUART'])
            nesovpaden_datas[15].append(row1['AUGRU'])
            nesovpaden_datas[16].append(result.iloc[0]['Сумма'])
            # print(result,'nesovpaden')
        else:
            pass
            # print(result2,'sovpaden')

    df_nesovpa =pd.DataFrame({
    'KSCHL':nesovpaden_datas[0],
    'VKORG':nesovpaden_datas[1],
    'WERKS':nesovpaden_datas[2],
    'VTWEG':nesovpaden_datas[3],
    'KONDA':nesovpaden_datas[4],
    'MATNR':nesovpaden_datas[5],
    'KBETR':nesovpaden_datas[6],
    'KONWA':nesovpaden_datas[7],
    'KPEIN':nesovpaden_datas[8],
    'KMEIN':nesovpaden_datas[9],
    'DATAB':nesovpaden_datas[10],
    'DATBI':nesovpaden_datas[11],
    'KUNNR':nesovpaden_datas[12],
    'FKART':nesovpaden_datas[13],
    'AUART':nesovpaden_datas[14],
    'AUGRU':nesovpaden_datas[15],
    'ERROR':nesovpaden_datas[16]

    })
    df_nesovpa =df_nesovpa.replace('nan','')
    if not df_nesovpa.empty:
        df_nesovpa.to_excel(pathtext3)
    

    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path7}',sheet_name='Sheet1',header=0)

    to_datetime_fmt = partial(pd.to_datetime, format='%d.%m.%Y')

    df1['DATAB'] = df1['DATAB'].apply(to_datetime_fmt)
    df1 = df1.astype(str)
    df1['joined_data']= df1['VKORG'] + df1['KONDA'] + df1['MATNR'] +df1['DATAB']

    # print(df1['joined_data'])

    df2 = pd.read_excel(f'{MEDIA_ROOT}/{path8}',sheet_name='Sheet1',header=0)

    df2 = df2.astype(str)
    df2['joined_data']= df2['Сбытовая организация'] + df2['Группа цен клиента'] + df2['Материал'] +df2['Действ. с']

    # print(df2['joined_data'])
    nesovpaden_datas =[[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[],[],[],[]]

    for key1,row1 in df1.iterrows():
        result = df2[df2['joined_data'] == row1['joined_data'] ]
        # print(row1['joined_data'],result)
        result['Сумма']=result['Сумма'].astype(float)
        result['Сумма']=result['Сумма'].round(decimals = 1)
    
        row1['KBETR']= round(float(row1['KBETR']),1)
        
        result2 =result[result['Сумма'] == row1['KBETR']]
        # print(result['Сумма'])
    
        if result2.empty:
            nesovpaden_datas[0].append(row1['KSCHL'])
            nesovpaden_datas[1].append(row1['VKORG'])
            nesovpaden_datas[2].append(row1['WERKS'])
            nesovpaden_datas[3].append(row1['VTWEG'])
            nesovpaden_datas[4].append(row1['KONDA'])
            nesovpaden_datas[5].append(row1['MATNR'])
            nesovpaden_datas[6].append(row1['KBETR'])
            nesovpaden_datas[7].append(row1['KONWA'])
            nesovpaden_datas[8].append(row1['KPEIN'])
            nesovpaden_datas[9].append(row1['KMEIN'])
            nesovpaden_datas[10].append(row1['DATAB'])
            nesovpaden_datas[11].append(row1['DATBI'])
            nesovpaden_datas[12].append(row1['KUNNR'])
            nesovpaden_datas[13].append(row1['FKART'])
            nesovpaden_datas[14].append(row1['AUART'])
            nesovpaden_datas[15].append(row1['AUGRU'])
            nesovpaden_datas[16].append(result.iloc[0]['Сумма'])
            print(result,'nesovpaden')
            break
        else:
            pass
            # print(result2,'sovpaden')

    df_nesovpa =pd.DataFrame({
    'KSCHL':nesovpaden_datas[0],
    'VKORG':nesovpaden_datas[1],
    'WERKS':nesovpaden_datas[2],
    'VTWEG':nesovpaden_datas[3],
    'KONDA':nesovpaden_datas[4],
    'MATNR':nesovpaden_datas[5],
    'KBETR':nesovpaden_datas[6],
    'KONWA':nesovpaden_datas[7],
    'KPEIN':nesovpaden_datas[8],
    'KMEIN':nesovpaden_datas[9],
    'DATAB':nesovpaden_datas[10],
    'DATBI':nesovpaden_datas[11],
    'KUNNR':nesovpaden_datas[12],
    'FKART':nesovpaden_datas[13],
    'AUART':nesovpaden_datas[14],
    'AUGRU':nesovpaden_datas[15],
    'ERROR':nesovpaden_datas[16]

    })

    df_nesovpa =df_nesovpa.replace('nan','')
    if not df_nesovpa.empty:
        df_nesovpa.to_excel(pathtext4)
    


    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path9}',sheet_name='Sheet1',header=0)

    to_datetime_fmt = partial(pd.to_datetime, format='%d.%m.%Y')

    df1['DATAB'] = df1['DATAB'].apply(to_datetime_fmt)
    df1 = df1.astype(str)
    df1['joined_data']= df1['VKORG'] + df1['KONDA'] + df1['MATNR'] +df1['DATAB']

    df2 = pd.read_excel(f'{MEDIA_ROOT}/{path10}',sheet_name='Sheet1',header=0)

    df2 = df2.astype(str)
    df2['joined_data']= df2['Сбытовая организация'] + df2['Группа цен клиента'] + df2['Материал'] +df2['Действ. с']

    nesovpaden_datas =[[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[],[],[],[]]

    for key1,row1 in df1.iterrows():
        result = df2[df2['joined_data'] == row1['joined_data'] ]
        result['Сумма']=result['Сумма'].astype(float)
        result['Сумма']=result['Сумма'].round(decimals = 1)
    
        row1['KBETR']= round(float(row1['KBETR']),1)
        
        result2 =result[result['Сумма'] == row1['KBETR']]
       
    
        if result2.empty:
            nesovpaden_datas[0].append(row1['KSCHL'])
            nesovpaden_datas[1].append(row1['VKORG'])
            nesovpaden_datas[2].append(row1['WERKS'])
            nesovpaden_datas[3].append(row1['VTWEG'])
            nesovpaden_datas[4].append(row1['KONDA'])
            nesovpaden_datas[5].append(row1['MATNR'])
            nesovpaden_datas[6].append(row1['KBETR'])
            nesovpaden_datas[7].append(row1['KONWA'])
            nesovpaden_datas[8].append(row1['KPEIN'])
            nesovpaden_datas[9].append(row1['KMEIN'])
            nesovpaden_datas[10].append(row1['DATAB'])
            nesovpaden_datas[11].append(row1['DATBI'])
            nesovpaden_datas[12].append(row1['KUNNR'])
            nesovpaden_datas[13].append(row1['FKART'])
            nesovpaden_datas[14].append(row1['AUART'])
            nesovpaden_datas[15].append(row1['AUGRU'])
            nesovpaden_datas[16].append(result.iloc[0]['Сумма'])
            break
        else:
            pass

    df_nesovpa =pd.DataFrame({
    'KSCHL':nesovpaden_datas[0],
    'VKORG':nesovpaden_datas[1],
    'WERKS':nesovpaden_datas[2],
    'VTWEG':nesovpaden_datas[3],
    'KONDA':nesovpaden_datas[4],
    'MATNR':nesovpaden_datas[5],
    'KBETR':nesovpaden_datas[6],
    'KONWA':nesovpaden_datas[7],
    'KPEIN':nesovpaden_datas[8],
    'KMEIN':nesovpaden_datas[9],
    'DATAB':nesovpaden_datas[10],
    'DATBI':nesovpaden_datas[11],
    'KUNNR':nesovpaden_datas[12],
    'FKART':nesovpaden_datas[13],
    'AUART':nesovpaden_datas[14],
    'AUGRU':nesovpaden_datas[15],
    'ERROR':nesovpaden_datas[16]

    })

    df_nesovpa =df_nesovpa.replace('nan','')
    if not df_nesovpa.empty:
        df_nesovpa.to_excel(pathtext5)
    


    df1 = pd.read_excel(f'{MEDIA_ROOT}/{path11}',sheet_name='Sheet1',header=0)

    to_datetime_fmt = partial(pd.to_datetime, format='%d.%m.%Y')

    df1['DATAB'] = df1['DATAB'].apply(to_datetime_fmt)
    df1 = df1.astype(str)
    df1['joined_data']= df1['VKORG'] + df1['KONDA'] + df1['MATNR'] +df1['DATAB']

    df2 = pd.read_excel(f'{MEDIA_ROOT}/{path12}',sheet_name='Sheet1',header=0)

    df2 = df2.astype(str)
    df2['joined_data']= df2['Сбытовая организация'] + df2['Группа цен клиента'] + df2['Материал'] +df2['Действ. с']

    nesovpaden_datas =[[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[],[],[],[]]

    for key1,row1 in df1.iterrows():
        result = df2[df2['joined_data'] == row1['joined_data']]
        result['Сумма']=result['Сумма'].astype(float)
        result['Сумма']=result['Сумма'].round(decimals = 1)
    
        row1['KBETR']= round(float(row1['KBETR']),1)
        
        result2 =result[result['Сумма'] == row1['KBETR']]
    
        if result2.empty:
            nesovpaden_datas[0].append(row1['KSCHL'])
            nesovpaden_datas[1].append(row1['VKORG'])
            nesovpaden_datas[2].append(row1['WERKS'])
            nesovpaden_datas[3].append(row1['VTWEG'])
            nesovpaden_datas[4].append(row1['KONDA'])
            nesovpaden_datas[5].append(row1['MATNR'])
            nesovpaden_datas[6].append(row1['KBETR'])
            nesovpaden_datas[7].append(row1['KONWA'])
            nesovpaden_datas[8].append(row1['KPEIN'])
            nesovpaden_datas[9].append(row1['KMEIN'])
            nesovpaden_datas[10].append(row1['DATAB'])
            nesovpaden_datas[11].append(row1['DATBI'])
            nesovpaden_datas[12].append(row1['KUNNR'])
            nesovpaden_datas[13].append(row1['FKART'])
            nesovpaden_datas[14].append(row1['AUART'])
            nesovpaden_datas[15].append(row1['AUGRU'])
            nesovpaden_datas[16].append(result.iloc[0]['Сумма'])
            break
        else:
            pass

    df_nesovpa =pd.DataFrame({
    'KSCHL':nesovpaden_datas[0],
    'VKORG':nesovpaden_datas[1],
    'WERKS':nesovpaden_datas[2],
    'VTWEG':nesovpaden_datas[3],
    'KONDA':nesovpaden_datas[4],
    'MATNR':nesovpaden_datas[5],
    'KBETR':nesovpaden_datas[6],
    'KONWA':nesovpaden_datas[7],
    'KPEIN':nesovpaden_datas[8],
    'KMEIN':nesovpaden_datas[9],
    'DATAB':nesovpaden_datas[10],
    'DATBI':nesovpaden_datas[11],
    'KUNNR':nesovpaden_datas[12],
    'FKART':nesovpaden_datas[13],
    'AUART':nesovpaden_datas[14],
    'AUGRU':nesovpaden_datas[15],
    'ERROR':nesovpaden_datas[16]

    })

    df_nesovpa =df_nesovpa.replace('nan','')
    if not df_nesovpa.empty:
        df_nesovpa.to_excel(pathtext6)
    



    file_path =f'{pathzip}.zip'

    zip(pathzip, pathzip)
    

    files = [FileG(file=file_path,filetype='obichniy')]
    context ={
        'files':files
    }
    return render(request,'online_savdo/zip_file_download.html',context)

 

