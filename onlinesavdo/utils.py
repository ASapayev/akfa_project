import os
import zipfile
import pandas as pd
from config.settings import MEDIA_ROOT
from datetime import datetime
from aluminiy.models import LengthOfProfile,ExchangeValues
import requests
import random
import string
from .models import BuxPrice,Segment,Zavod,PokritiyaProtsent
from django.db.models import Q
import asyncio

from .utils_async import main,main_check_sena
from decouple import config

base_url = 'http://test.app.akfa.onlinesavdo.com'


def create_session(url):
    session = requests.Session()
    login_data = {
        'login': config('LOGIN_SAVDO'), 
        'password': config('PASSWORD_SAVDO') 
    }
    response = session.post(url, data=login_data)
    return session,response.status_code

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

def create_folder(parent_dir,directory):
    path =os.path.join(parent_dir,directory)
    if not os.path.isdir(path):
        os.mkdir(path)

def zip(src, dst):
    zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            zf.write(absname, arcname)
    zf.close()

def generate_random_string(length=10):
    letters = string.ascii_letters + string.digits  # Includes uppercase, lowercase letters, and digits
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string



def  format_to_online(url,session,file):
    try:
        df = pd.read_excel(f'{file}',header=0,sheet_name='Алюмин Навои Жомий')
    except:
        df = pd.read_excel(f'{MEDIA_ROOT}/{file}',header=0,sheet_name='Алюмин Навои Жомий')

    # print(df.columns,'ss')
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
    string_rand = generate_random_string()
    pathtext1 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT_ONLINE_{string_rand}.xlsx'


    not_exists = [[],[]]
    all_corecct = True
    df['Длина (мм)'].astype(str)
    df['Длина (мм)'] = df['Длина (мм)'].replace('.0','')
    for key,row in df.iterrows():
        
        df['Длина (мм)'][key] =str(df['Длина (мм)'][key]).replace('.0','')
        if not LengthOfProfile.objects.filter((Q(artikul =row["Артикул"])|Q(component=row["Артикул"]))).exists():
            not_exists[0].append(row["Артикул"])
            not_exists[1].append(df['Длина (мм)'][key])
            all_corecct = False

    if not all_corecct:
        new_not ={'Артикул':not_exists[0],'Длина (мм)':not_exists[1]} 
        new_df = pd.DataFrame(new_not)
        string_rand = generate_random_string()
        path =f'{MEDIA_ROOT}/uploads/online_savdo/not_exists_{string_rand}.xlsx'

        new_df.to_excel(path,index=False)

        return path,'error'


    result_dict = asyncio.run(main(df=df)) 



    df['Длина (мм)'].astype(str)
    df['Длина (мм)'] = df['Длина (мм)'].replace('.0','')
    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for key,row in df.iterrows():
        df['Длина (мм)'][key] =str(df['Длина (мм)'][key]).replace('.0','')
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
        ves_za_metr = LengthOfProfile.objects.filter((Q(artikul =row["Артикул"])|Q(component=row["Артикул"])))[:1].get().ves_za_metr
        ves_za_shtuk = float(ves_za_metr[row['Тип покрытия']])*float(df['Длина (мм)'][key])/1000
        data[11].append(ves_za_shtuk)
        data[12].append(row["Статус"])
        # data[12].append("Пассивный")
        # data[12].append("Активный")
        data[13].append(row["Завод TEX"])
        online_id = row["ONLINE ID"].replace('.0','').replace('nan','')

        if row["Статус"] == "Пассивный":
            # id = check_item_from_savdo(url,session,row["Название"])
            if str(row["Название"]) in result_dict:
                data[14].append(result_dict[str(row["Название"])])
            else:
                data[14].append('')
        else:
            data[14].append(online_id)

    new_row = {'ID ' :[int(dat) if dat!='' else '' for dat in data[14]], 'NAME':data[0], 'SAPCODE':data[1],'GROUPNAME':data[2],'COLOR':data[3],'PURCHASING GROUP':data[4],'SEGMENT':data[5],'BUGALTER NAME':data[6],'BUGALTER UNIT':data[7],'BASE UNIT':data[8],'ALTER UNIT':data[9],'BASE UNITVAL':data[10],'ALTER UNITVAL':data[11],'STATUS':data[12],'FACTORY':data[13],'IS FREE':['false' for dat in data[0]]}
    new_df = pd.DataFrame(new_row)
    new_df = new_df.replace('nan','')
    # new_df = new_df.astype(str)
    writer = pd.ExcelWriter(pathtext1, engine='xlsxwriter')
    new_df.to_excel(writer,index=False,sheet_name='Goods')   
    writer.close()
    return pathtext1,'success'



def upload_file_online(file,session,status_code,url,sheet_name):
    
    if status_code == 200:
        path = os.path.join(MEDIA_ROOT, file)
        with open(path, 'rb') as file:
            files = {'file_upload': file}  
            data = {'sheetname': sheet_name}  
            response = session.post(url, files=files, data=data)
            if response.status_code ==200:
                return 200
            else:
                return 400
        return 200
    else:
        return 400




def send_request_to_savdo(url,session,name,sapcode):
    params = {
            'page': 1,
            'rows': 50,
            'sort': 'id',
            'order': 'asc',
            'filterRules': '[{"field":"name","op":"contains","value":"'+name+'"},{"field":"sapCode","op":"contains","value":"'+sapcode+'"}]'
            }
    form_response = session.get(url,params=params)
    res = form_response.json()['rows']
    return res


def check_item_from_savdo(url,session,name):
    params = {
            'page': 1,
            'rows': 50,
            'sort': 'id',
            'order': 'asc',
            'filterRules': '[{"field":"name","op":"contains","value":"'+name+'"}]'
            }
    form_response = session.get(url,params=params)
    response = form_response.json()['rows']
    if len(response) > 0:
        for res in response:
            if res['name'] == name:
                return res['id']
    return None






def get_id(path,status_code=200):
    try:
        df1 = pd.read_excel(f'{path}',header=0,sheet_name='Алюмин Навои Жомий')
    except:
        df1 = pd.read_excel(f'{MEDIA_ROOT}/{path}',header=0,sheet_name='Алюмин Навои Жомий')

    # df1 = pd.read_excel(f'{MEDIA_ROOT}/{path}',sheet_name='Алюмин Навои Жомий',header= 0)
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
    string_rand = generate_random_string()
    pathtext1 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\SAVDO_ID_FILE_{string_rand}.xlsx'


    not_exists = [[],[],[]]
    all_corecct = True
    df1['Длина (мм)'].astype(str)
    df1['Длина (мм)'] = df1['Длина (мм)'].replace('.0','')
    for key,row in df1.iterrows():
        
        if not LengthOfProfile.objects.filter((Q(artikul =row["Артикул"])|Q(component=row["Артикул"]))).exists():
            not_exists[0].append(row["Артикул"])
            not_exists[1].append(row['Длина (мм)'])
            not_exists[2].append('VES ZA METR')
            all_corecct = False
        if not PokritiyaProtsent.objects.filter(name__icontains = str(row['Название системы']).upper(), pokritiya__icontains=str(row['Тип покрытия']).upper()).exists():
            # print(row['Название системы'],row['Тип покрытия'])
            not_exists[0].append(row["Артикул"])
            not_exists[1].append(row['Название системы'])
            not_exists[2].append('POKRITIYA PROTSENT')
            all_corecct = False

    # all_corecct =True

    if not all_corecct:
        new_not ={'Артикул':not_exists[0],'Длина (мм)':not_exists[1],'ERROR TYPE':not_exists[2]} 
        new_df = pd.DataFrame(new_not)
        string_rand = generate_random_string()
        path2 =f'{MEDIA_ROOT}/uploads/online_savdo/not_exists_{string_rand}.xlsx'

        new_df.to_excel(path2,index=False)

        return 400, path2



    data =[[],[],[],[],[],[],[],[]] 
    df1['Длина (мм)'].astype(str)

    doesnot_exist =[[],[]]
    
    result_dict = asyncio.run(main(df=df1,search_multiple=True)) 

    if status_code == 200:
        for key2,row2 in df1.iterrows():
            # name = row2['Название']
            # sapcode = row2['SAP Код вручную (вставится вручную)']
            # form_url = f"{base_url}/ajax-goods-datagrid"  
            # res = send_request_to_savdo(form_url,session,name,sapcode)

            if str(row2['Название']) in result_dict:
                id = result_dict[str(row2['Название'])]
                df1['Длина (мм)'] = df1['Длина (мм)'].replace('.0','')

                if 'AKFA' in row2['Тип клиента']:
                    data[0].append(id)
                    data[1].append(row2['Название'])
                    data[2].append('AKFA')
                    data[3].append(datetime.now())
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
                        ves_za_m =LengthOfProfile.objects.filter((Q(artikul =row["Артикул"])|Q(component=row["Артикул"])))[:1].get().ves_za_metr
                        print(ves_za_m,row2['Тип покрытия'],row["Артикул"])
                        t = float(ves_za_m[row2['Тип покрытия']])*float(str(row2['Длина (мм)']).replace('.0',''))/1000

                    protsent = PokritiyaProtsent.objects.filter(name__icontains = str(row2['Название системы']).upper(), pokritiya__icontains=str(row2['Тип покрытия']).upper())[:1].get().protsent
                    price_prosent =float(t)*(price)*float(protsent)
                    data[5].append(round50(price_prosent))
                    data[4].append(round50(price_prosent/1.12))
                    data[6].append("USD")
                    data[7].append(row2['Базовый единица'])

                if 'IMZO' in row2['Тип клиента']:
                    data[0].append(id)
                    data[1].append(row2['Название'])
                    data[2].append('IMZO')
                    data[3].append(datetime.now())
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
                        ves_za_m =LengthOfProfile.objects.filter((Q(artikul =row["Артикул"])|Q(component=row["Артикул"])))[:1].get().ves_za_metr
                        # print(ves_za_m)
                        t = float(ves_za_m[row2['Тип покрытия']])*float(str(row2['Длина (мм)']).replace('.0',''))/1000

                    protsent = PokritiyaProtsent.objects.filter(name__icontains = str(row2['Название системы']).upper(), pokritiya__icontains=str(row2['Тип покрытия']).upper())[:1].get().protsent
                    price_prosent =float(t)*(price)*float(protsent)
                    data[5].append(round50(price_prosent))
                    data[4].append(round50(price_prosent/1.12))
                    data[6].append("USD")
                    data[7].append(row2['Базовый единица'])

                if 'FRANCHISING' in row2['Тип клиента']:
                    data[0].append(id)
                    data[1].append(row2['Название'])
                    data[2].append('FRANCHISING')
                    data[3].append(datetime.now())
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
                        ves_za_m =LengthOfProfile.objects.filter((Q(artikul =row["Артикул"])|Q(component=row["Артикул"])))[:1].get().ves_za_metr
                        # print(ves_za_m)
                        t = float(ves_za_m[row2['Тип покрытия']])*float(str(row2['Длина (мм)']).replace('.0',''))/1000

                    protsent = PokritiyaProtsent.objects.filter(name__icontains = str(row2['Название системы']).upper(), pokritiya__icontains=str(row2['Тип покрытия']).upper())[:1].get().protsent
                    price_prosent =float(t)*(price)*float(protsent)
                    data[5].append(round50(price_prosent))
                    data[4].append(round50(price_prosent/1.12))
                    data[6].append("USD")
                    data[7].append(row2['Базовый единица'])
                

            else:
                doesnot_exist[0].append(row2['Название'])
                doesnot_exist[1].append(row2['SAP Код вручную (вставится вручную)'])



    new_row = {'ID' :data[0], 'NAME':data[1], 'CLIENTYPE':data[2],'DATE':data[3],'COST':data[4],'RATE':data[5],'CURRENCY':data[6],'UNIT':data[7]}

    new_df =pd.DataFrame(new_row)
    new_df_doesnot =pd.DataFrame({})

    with pd.ExcelWriter(pathtext1, engine='openpyxl') as writer:
        # Write both DataFrames to separate sheets
        new_df.to_excel(writer, index=False, sheet_name='SENA')
        new_df_doesnot.to_excel(writer, index=False, sheet_name='NOT EXISTS')
        
        workbook = writer.book
        sena_sheet = workbook['SENA']
        
        for row in range(2, len(new_df) + 2):  # Start from row 2 to skip the header
            cell = sena_sheet.cell(row=row, column=4)  # Column 4 is 'DATE'
            cell.number_format = 'DD.MM.YYYY'
   

    return 200, pathtext1



def round50(n):
    return round(n/0.01)*0.01

def round502(n):
    if str(n)=='':
        return ''
    return round(float(str(n).replace(',','.')), -2)

def round503(n):
    return round(n * 2, -2) // 2


def check_sena(path):
    df1 = pd.read_excel(path,sheet_name='SENA')
    df_filechek = [[],[],[],[],[]]
    doesnot_exists =[[],[],[],[]]

    # url_sena ='http://test.app.akfa.onlinesavdo.com/ajax-goodsRate-datagrid'
    sena = asyncio.run(main_check_sena(df=df1))

    # print(sena)

    for key, row in df1.iterrows():
        # print(row['ID'],int(row['ID']),'id'*20)
        if int(row['ID']) in sena:
            id_= int(row['ID'])
            df_filechek[0].append(row['ID'])
            df_filechek[1].append(sena[id_]['cost'])
            df_filechek[2].append(sena[id_]['rate'])
            df_filechek[3].append(sena[id_]['dateStr'])

            is_cost_similar = str(row['COST']) == str(sena[id_]['cost'])
            is_rate_similar = str(row['RATE']) == str(sena[id_]['rate'])
            is_date_similar = str(row['DATE']).split(' ')[0] == str(sena[id_]['dateStr'])
            # print()
            if is_cost_similar and is_rate_similar and is_date_similar:
                df_filechek[4].append(True)
            else:
                df_filechek[4].append(False)
        else:
            doesnot_exists[0].append(row['ID'])
            doesnot_exists[1].append(row['NAME'])
            doesnot_exists[2].append(row['CLIENTYPE'])
            doesnot_exists[3].append(row['DATE'])
    

    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M")

    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\',hour)
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\','ONLINE')
    create_folder(f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\',minut)
    string_rand = generate_random_string()
    pathtext1 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\SAVDO_CHECKER_FILE_{string_rand}.xlsx'

    new_df = pd.DataFrame({'ID':df_filechek[0],'COST':df_filechek[1],'RATE':df_filechek[2],'DATE':df_filechek[3],'STATUS':df_filechek[4]})
    df_not_exists = pd.DataFrame({'ID':doesnot_exists[0],'NAME':doesnot_exists[1],'CLIENTYPE':doesnot_exists[2],'DATE':doesnot_exists[3]})

    with pd.ExcelWriter(pathtext1, engine='openpyxl') as writer:
        new_df.to_excel(writer, index=False, sheet_name='SENA CHECK')
        df_not_exists.to_excel(writer, index=False, sheet_name='SENA NOT EXISTS')
    
    return pathtext1


def sozdaniye_sena_sap(path,session):
    try:
        df1 = pd.read_excel(f'{path}',header=0,sheet_name='Алюмин Навои Жомий')
    except:
        df1 = pd.read_excel(f'{MEDIA_ROOT}/{path}',header=0,sheet_name='Алюмин Навои Жомий')

    # df1 = pd.read_excel(f'{MEDIA_ROOT}/{path}',sheet_name='Алюмин Навои Жомий',header= 0)
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

    string_rand = generate_random_string()

    pathtext1 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\PREPARATION_FOR_SAP_{string_rand}.xlsx'
    DATA = ExchangeValues.objects.get(id = 1).start_data
    

    buxprice_data = BuxPrice.objects.all().values('name','price')
    buxprice ={}
    for bux in buxprice_data:
        buxprice[bux['name']] = bux['price']

    segment1_data = Segment.objects.filter(segment_name='segment1').values('name','price')
    # print(segment1_data)
    segment1 ={}
    for seg in segment1_data:
        segment1[seg['name']] = seg['price']

    # print(segment1,'segment')
    segment2_data = Segment.objects.filter(segment_name='segment2').values('name','price')
    segment2 ={}
    for seg in segment2_data:
        segment2[seg['name']] = seg['price']

    segment3_data = Segment.objects.filter(segment_name='segment3').values('name','price')
    segment3 ={}
    for seg in segment3_data:
        segment3[seg['name']] = seg['price']

    segment4_data = Segment.objects.filter(segment_name='segment4').values('name','price')
    segment4 ={}
    for seg in segment4_data:
        segment4[seg['name']] = seg['price']

    segment5_data = Segment.objects.filter(segment_name='segment5').values('name','price')
    segment5 ={}
    for seg in segment5_data:
        segment5[seg['name']] = seg['price']

    segment6_data = Segment.objects.filter(segment_name='segment6').values('name','price')
    segment6 ={}
    for seg in segment6_data:
        segment6[seg['name']] = seg['price']

    zavod_data = Zavod.objects.all().values('name','price')
    zavod ={}
    for zav in zavod_data:
        zavod[zav['name']] = zav['price']

    #### get data from base #####
    form_url = f"{base_url}/ajax-goods-datagrid"
    
    ####### end get baza #######

    does_not_exists =[[],[]]
    data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for key2,row2 in df1.iterrows():
        name = row2['Название']
        sapcode = row2['SAP Код вручную (вставится вручную)']
        result = send_request_to_savdo(form_url,session,name,sapcode)

        if len(result)>0:
            result = result[0]
            data[0].append(result['id'])
            data[1].append(result['name'])
            # print(result,'kkkkk')
            if 'group' in result:
                if 'name' in result['group']:
                    data[2].append(result['group']['name'])
                else:
                    data[2].append('')
                # data[2].append(result['group']['name'])
            else:
                data[2].append('')

            if 'sapCode' in result:
                data[3].append(result['sapCode'])
            else:
                data[3].append('')
            # data[3].append(result.iloc[0]['sapcode'])   
            if 'alternateUnitVal' in result:
                data[4].append(result['alternateUnitVal'])
            else:
                data[4].append('')
            # data[4].append(result.iloc[0]['alternate_unit_val'])

            if 'purchasingGroup' in result:
                if 'name' in result['purchasingGroup']:
                    data[5].append(result['purchasingGroup']['name'])
                else:
                    data[5].append('')
                # data[5].append(result['purchasingGroup']['name'])
            else:
                data[5].append('')
            # data[5].append(result.iloc[0]['purchasing_group'])
            if 'segment' in result:
                if 'name' in result['segment']:
                    segment_name = result['segment']['name']
                else:
                    segment_name = ''
            else:
                segment_name = ''

            data[6].append(segment_name)

            # data[6].append(result.iloc[0]['segment'])
            accounting_goods_name =''
            if 'accountingGoods' in result:
                if isinstance(result['accountingGoods'],dict) and 'name' in result['accountingGoods']:
                    accounting_goods_name = result['accountingGoods']['name']
                else:
                    accounting_goods_name =''
                # accounting_goods_name = result['accountingGoods']['name']
            else:
                accounting_goods_name = ''
                
            data[7].append(accounting_goods_name)
            # data[7].append(result.iloc[0]['accounting_goods_name'])
            if accounting_goods_name !='':
                data[8].append(buxprice[accounting_goods_name])
            else:
                data[8].append('')
            # data[8].append(buxprice[result.iloc[0]['accounting_goods_name']])
            data[9].append(DATA)

            if segment_name in segment1:
                data[10].append(segment1[segment_name])
            else:
                data[10].append('')

            if segment_name in segment2:
                data[11].append(segment2[segment_name])
            else:
                data[11].append('')

            if segment_name in segment3:
                data[12].append(segment3[segment_name])
            else:
                data[12].append('')

            if segment_name in segment4:
                data[13].append(segment4[segment_name])
            else:
                data[13].append('')

            if segment_name in segment5:
                data[14].append(segment5[segment_name])
            else:
                data[14].append('')

            if segment_name in segment6:
                data[15].append(segment6[segment_name])
            else:
                data[15].append('')

            

            if 'factory' in result:
                if 'name' in result['factory']:
                    data[16].append(zavod[result['factory']['name']])
                else:
                    data[16].append('')
            else:
                data[16].append('')
            
            a = 0

            url_sena ='http://test.app.akfa.onlinesavdo.com/ajax-goodsRate-datagrid'
            sena = get_sena(url_sena,session,result['id'])['cost']
            # print(sena,'sennaaaaa')
            if sena:
                a = sena

            data[17].append(float(a))
            data[18].append(row2['Базовый единица'])

            if segment_name in segment1:
                if int(float(segment1[segment_name]))==0:
                    b4=''
                    c4=''
                    g4=''
                    v4=''
                else:
                    if row2['Базовый единица']=='КГ':
                        t=1
                    else:
                        t=float(result['alternateUnitVal'])         
                    b4=float(a)-float(a)*float(segment1[segment_name])
                    c4=round502(int((t*float(buxprice[accounting_goods_name]))/1.12))
                    g4=round502(int((t*float(buxprice[accounting_goods_name]))/1.12))*1.12
                    v4=(float(a)-float(a)*float(segment1[segment_name]))-(round502((t*float(buxprice[accounting_goods_name]))/1.12)*1.12)
            else:
                b4=''
                c4=''
                g4=''
                v4=''
            
            data[19].append(b4)   
            data[20].append(c4)
            data[21].append(g4)
            data[22].append(v4)
            data[23].append("")

            if segment_name in segment2:

                if int(float(segment2[segment_name]))==0:
                    b3=''
                    c3=''
                    g3=''
                    v3=''
                else:
                    if row2['Базовый единица']=='КГ':
                        t=1
                    else:
                        t=float(result['alternateUnitVal'])      
                    b3=float(a)-float(a)*float(segment2[segment_name])
                    c3=round502(int((t*float(buxprice[accounting_goods_name]))/1.12))
                    g3=round502(int((t*float(buxprice[accounting_goods_name]))/1.12))*1.12
                    v3=(float(a)-float(a)*float(segment2[segment_name]))-(round502((t*float(buxprice[accounting_goods_name]))/1.12)*1.12)
            else:
                b3=''
                c3=''
                g3=''
                v3=''

            
            data[24].append(b3)   
            data[25].append(c3)
            data[26].append(g3)
            data[27].append(v3)
            data[28].append("")

            if segment_name in segment3:
                if int(float(segment3[segment_name]))==0:
                    b2=''
                    c2=''
                    g2=''
                    v2=''
                else:
                    if row2['Базовый единица']=='КГ':
                        t=1
                    else:
                        t=float(result['alternateUnitVal'])
                    b2=float(a)-float(a)*float(segment3[segment_name])
                    c2=round502(int((t*float(buxprice[accounting_goods_name]))/1.12))
                    g2=round502(int((t*float(buxprice[accounting_goods_name]))/1.12))*1.12
                    v2=(float(a)-float(a)*float(segment3[segment_name]))-(round502((t*float(buxprice[accounting_goods_name]))/1.12)*1.12)
            else:
                b2=''
                c2=''
                g2=''
                v2=''

            data[29].append(b2)   
            data[30].append(c2)
            data[31].append(g2)
            data[32].append(v2)
            data[33].append("")
            
            if segment_name in segment4:
                if int(float(segment4[segment_name]))==0:
                    b=''
                    c=''
                    g=''
                    v=''
                else:
                    if row2['Базовый единица']=='КГ':
                        t=1
                    else:
                        t=float(result['alternateUnitVal'])
                    b=float(a)-float(a)*float(segment4[segment_name])
                    c=round502(int((t*float(buxprice[accounting_goods_name]))/1.12))
                    g=round502(int((t*float(buxprice[accounting_goods_name]))/1.12))*1.12
                    v=(float(a)-float(a)*float(segment4[segment_name]))-(round502((t*float(buxprice[accounting_goods_name]))/1.12)*1.12)
            else:
                b=''
                c=''
                g=''
                v=''

            data[34].append(b)   
            data[35].append(c)
            data[36].append(g)
            data[37].append(v)
            data[38].append("")
            if segment_name in segment5:
                if int(float(segment5[segment_name]))==0:
                    b1=''
                    c1=''
                    g1=''
                    v1=''
                else:
                    if row2['Базовый единица']=='КГ':
                        t=1
                    else:
                        t=float(result['alternateUnitVal'])
                    b1=float(a)-float(a)*float(segment5[segment_name])
                    c1=round502(int((t*float(buxprice[accounting_goods_name]))/1.12))
                    g1=round502(int((t*float(buxprice[accounting_goods_name]))/1.12))*1.12
                    v1=(float(a)-float(a)*float(segment5[segment_name]))-(round502((t*float(buxprice[accounting_goods_name]))/1.12)*1.12)
            else:
                b1=''
                c1=''
                g1=''
                v1=''

            data[39].append(b1)   
            data[40].append(c1)
            data[41].append(g1)
            data[42].append(v1)
            data[43].append("")

            if segment_name in segment6:
                if int(float(segment6[segment_name]))==0:
                    b5=''
                    c5=''
                    g5=''
                    v5=''
                else:
                    if row2['Базовый единица']=='КГ':
                        t=1
                    else:
                        t=float(result['alternateUnitVal'])
                    b5=float(a)-float(a)*float(segment6[segment_name])
                    c5=round502(int((t*float(buxprice[accounting_goods_name]))/1.12))
                    g5=round502(int((t*float(buxprice[accounting_goods_name]))/1.12))*1.12
                    v5=(float(a)-float(a)*float(segment6[segment_name]))-(round502((t*float(buxprice[accounting_goods_name]))/1.12)*1.12)
            else:
                b5=''
                c5=''
                g5=''
                v5=''

            data[44].append(b5)   
            data[45].append(c5)
            data[46].append(g5)
            data[47].append(v5)
        else:
            does_not_exists[0].append(name)
            does_not_exists[1].append(sapcode)

    

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
    does_not_exists_df =pd.DataFrame(new_row)
    new_df =new_df.replace(0,'')
    
    writer = pd.ExcelWriter(pathtext1, engine='xlsxwriter')
    new_df.to_excel(writer,index=False,sheet_name='SAPFORMAT')
    does_not_exists_df.to_excel(writer,index=False,sheet_name='NOT EXISTS')
    writer.close()
    
    return pathtext1



def get_sena(url,session,id):
    client_types =[1,2,4]
    for client_type in client_types:
        params = {
                'clientTypeId': client_type,
                'typeStr': 'PURCHASE_RATE',
                'goodId': id,
                }
        form_response = session.post(url,params=params)
        res = form_response.json()['rows']
        if len(res) > 0:
            return res[-1]
            
        
    return None


    



def sozdaniye_sap_format_sena_create(path_sena_file):

    df1 = pd.read_excel(path_sena_file,header=0)

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
    # pathtext3 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT\\VK_11_3beznal tayyor 1.xlsx'
    pathtext4 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT\\VK_11_2prichina zakaza (ZUU) tayyor 1.xlsx'
    # pathtext5 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT\\VK_11zfdn (ALUMIN) tayyor 1 ZFKN.xlsx'
    # pathtext6 =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT\\VK_11zfdn (ALUMIN) tayyor 1.xlsx'
    pathzip =f'{MEDIA_ROOT}\\uploads\\online_savdo\\{year}\\{month}\\{day}\\{hour}\\ONLINE\\{minut}\\FORMAT'
    
    exchange_val = ExchangeValues.objects.get(id = 1)
    DATAB = exchange_val.start_data
    DATBI = exchange_val.end_data

    data1 =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    data2 =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    data3 =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(1,8):
        for key2,row2 in df1.iterrows():
            ####1 #######
            d='D'+str(i)
            data1[0].append("PR00")
            data1[1].append(row2["Сбытовая организация"])
            data1[2].append("")
            data1[3].append("10")
            data1[4].append(d)
            data1[5].append(row2["sapcode"])
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
            data1[6].append(k)
            data1[7].append("UZS")
            data1[8].append(1)
            data1[9].append(row2["Ед.изм"])
            data1[10].append(DATAB)
            data1[11].append(DATBI)
            data1[12].append("")
            data1[13].append("")
            data1[14].append("ZORN")
            data1[15].append("")

            ###### 2#####
            # d='D'+str(i)
            data2[0].append("PR00")
            data2[1].append(row2["Сбытовая организация"])
            data2[2].append("")
            data2[3].append("10")
            data2[4].append(d)
            data2[5].append(row2["sapcode"])
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
            data2[6].append(k)
            data2[7].append("UZS")
            data2[8].append(1)
            data2[9].append(row2["Ед.изм"])
            data2[10].append(DATAB)
            data2[11].append(DATBI)
            data2[12].append("")
            data2[13].append("")
            data2[14].append("ZREN")
            data2[15].append("")

            ###### 3 #######

            data3[0].append("PR00")
            data3[1].append(row2["Сбытовая организация"])
            data3[2].append("")
            data3[3].append("10")
            data3[4].append(d)
            data3[5].append(row2["sapcode"])
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
            data3[6].append(k)
            data3[7].append("UZS")
            data3[8].append(1)
            data3[9].append(row2["Ед.изм"])
            data3[10].append(DATAB)
            data3[11].append(DATBI)
            data3[12].append("")
            data3[13].append("")
            data3[14].append("")
            data3[15].append("ZUU")
        





    new_row = { 'KSCHL':data1[0],	
                'VKORG':data1[1],	
                'WERKS':data1[2],	
                'VTWEG':data1[3],	
                'KONDA':data1[4],	
                'MATNR':data1[5],	
                'KBETR':data1[6],	
                'KONWA':data1[7],	
                'KPEIN':data1[8],	
                'KMEIN':data1[9],	
                'DATAB':data1[10],	
                'DATBI':data1[11],	
                'KUNNR':data1[12],	
                'FKART':data1[13],	
                'AUART':data1[14],	
                'AUGRU':data1[15]
            }


    new_df =pd.DataFrame(new_row)

    new_df =new_df[~pd.isna(new_df['KBETR'])]


    new_df.to_excel(pathtext1,index=False)


    new_row2 = {'KSCHL':data2[0],	
            'VKORG':data2[1],	
            'WERKS':data2[2],	
            'VTWEG':data2[3],	
            'KONDA':data2[4],	
            'MATNR':data2[5],	
            'KBETR':data2[6],	
            'KONWA':data2[7],	
            'KPEIN':data2[8],	
            'KMEIN':data2[9],	
            'DATAB':data2[10],	
            'DATBI':data2[11],	
            'KUNNR':data2[12],	
            'FKART':data2[13],	
            'AUART':data2[14],	
            'AUGRU':data2[15]
    }

    new_df2 =pd.DataFrame(new_row2)
    new_df2 =new_df2[~pd.isna(new_df2['KBETR'])]
    new_df2.to_excel(pathtext2,index=False)

    new_row3 = {'KSCHL':data3[0],	
            'VKORG':data3[1],	
            'WERKS':data3[2],	
            'VTWEG':data3[3],	
            'KONDA':data3[4],	
            'MATNR':data3[5],	
            'KBETR':data3[6],	
            'KONWA':data3[7],	
            'KPEIN':data3[8],	
            'KMEIN':data3[9],	
            'DATAB':data3[10],	
            'DATBI':data3[11],	
            'KUNNR':data3[12],	
            'FKART':data3[13],	
            'AUART':data3[14],	
            'AUGRU':data3[15]
    }

    new_df3 =pd.DataFrame(new_row3)
    new_df3 =new_df3[~pd.isna(new_df3['KBETR'])]

    new_df3.to_excel(pathtext4,index=False)



    #####################2 excell#################
    # df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)

    # data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    # for i in range(1,8):
    #     for key2,row2 in df1.iterrows():
    #         d='D'+str(i)
    #         data[0].append("PR00")
    #         data[1].append(row2["Сбытовая организация"])
    #         data[2].append("")
    #         data[3].append("10")
    #         data[4].append(d)
    #         data[5].append(row2["sapcode"])
    #         if i==1:
    #             k=row2["Shaxar diler uchun narx segmentli D1"]
    #         elif i==2:
    #             k=row2["Shaxar diler (Yangiyul,Olmaliq,Angren,Guliston,Bekobod,Bo`ka,Chirchiq) uchun narx segmentli D2"]
    #         elif i==3:
    #             k=row2["Viloyat diler uchun narx segmentli D3"]
    #         elif i==4:
    #             k=row2["Retpen diler (Nukus (Maxmud), Xorazm (Shixnazar),Namangan-1 ,Farg`ona (Shuhrat Aka),Andijon-3 (Azizbek) uchun narx segmentli D4"]
    #         elif i==5:
    #             k=row2["Retpen diler uchun narx segmentli D5"]
    #         elif i==6:
    #             k=row2["Imzo/Franshiza diler uchun narx segmentli D6"]
    #         elif i==7:
    #             k=row2["Imzo/Franshiza diler uchun narx segmentli D6"]
    #         data[6].append(k)
    #         data[7].append("UZS")
    #         data[8].append(1)
    #         data[9].append(row2["Ед.изм"])
    #         data[10].append(DATAB)
    #         data[11].append(DATBI)
    #         data[12].append("")
    #         data[13].append("")
    #         data[14].append("ZREN")
    #         data[15].append("")
        
    # new_row = {'KSCHL':data[0],	
    #         'VKORG':data[1],	
    #         'WERKS':data[2],	
    #         'VTWEG':data[3],	
    #         'KONDA':data[4],	
    #         'MATNR':data[5],	
    #         'KBETR':data[6],	
    #         'KONWA':data[7],	
    #         'KPEIN':data[8],	
    #         'KMEIN':data[9],	
    #         'DATAB':data[10],	
    #         'DATBI':data[11],	
    #         'KUNNR':data[12],	
    #         'FKART':data[13],	
    #         'AUART':data[14],	
    #         'AUGRU':data[15]
    # }

    # new_df =pd.DataFrame(new_row)
    # new_df =new_df[~pd.isna(new_df['KBETR'])]
    # new_df.to_excel(pathtext2,index=False)

    ###################### 3 ######################

    # df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)


    # data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    # for i in range(1,8):
    #     for key2,row2 in df1.iterrows():
    #         d='D'+str(i)
    #         data[0].append("PR00")
    #         data[1].append(row2["Сбытовая организация"])
    #         data[2].append("")
    #         data[3].append("10")
    #         data[4].append(d)
    #         data[5].append(row2["sapcode"])
    #         if i==1:
    #             k=row2["Shaxar diler uchun narx segmentli D1"]
    #         elif i==2:
    #             k=row2["Shaxar diler (Yangiyul,Olmaliq,Angren,Guliston,Bekobod,Bo`ka,Chirchiq) uchun narx segmentli D2"]
    #         elif i==3:
    #             k=row2["Viloyat diler uchun narx segmentli D3"]
    #         elif i==4:
    #             k=row2["Retpen diler (Nukus (Maxmud), Xorazm (Shixnazar),Namangan-1 ,Farg`ona (Shuhrat Aka),Andijon-3 (Azizbek) uchun narx segmentli D4"]
    #         elif i==5:
    #             k=row2["Retpen diler uchun narx segmentli D5"]
    #         elif i==6:
    #             k=row2["Imzo/Franshiza diler uchun narx segmentli D6"]
    #         elif i==7:
    #             k=row2["Imzo/Franshiza diler uchun narx segmentli D6"]
    #         data[6].append(k)
    #         data[7].append("UZS")
    #         data[8].append(1)
    #         data[9].append(row2["Ед.изм"])
    #         data[10].append(DATAB)
    #         data[11].append(DATBI)
    #         data[12].append("")
    #         data[13].append("")
    #         data[14].append("")
    #         data[15].append("")
        
    # new_row = {'KSCHL':data[0],	
    #         'VKORG':data[1],	
    #         'WERKS':data[2],	
    #         'VTWEG':data[3],	
    #         'KONDA':data[4],	
    #         'MATNR':data[5],	
    #         'KBETR':data[6],	
    #         'KONWA':data[7],	
    #         'KPEIN':data[8],	
    #         'KMEIN':data[9],	
    #         'DATAB':data[10],	
    #         'DATBI':data[11],	
    #         'KUNNR':data[12],	
    #         'FKART':data[13],	
    #         'AUART':data[14],	
    #         'AUGRU':data[15]
    # }


    # new_df =pd.DataFrame(new_row)
    # new_df =new_df[~pd.isna(new_df['KBETR'])]
    # new_df.to_excel(pathtext3,index=False)

    ############## 4 ##########################

    # df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)


    # data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    # for i in range(1,8):
    #     for key2,row2 in df1.iterrows():
    #         d='D'+str(i)
    #         data[0].append("PR00")
    #         data[1].append(row2["Сбытовая организация"])
    #         data[2].append("")
    #         data[3].append("10")
    #         data[4].append(d)
    #         data[5].append(row2["sapcode"])
    #         if i==1:
    #             k=row2["70% без ндс безнал (цена для выгрузуа SAP) D1"]
    #         elif i==2:
    #             k=row2["70% без ндс безнал (цена для выгрузуа SAP) D2"]
    #         elif i==3:
    #             k=row2["70% без ндс безнал (цена для выгрузуа SAP) D3"]
    #         elif i==4:
    #             k=row2["70% без ндс безнал (цена для выгрузуа SAP) D4"]
    #         elif i==5:
    #             k=row2["70% без ндс безнал (цена для выгрузуа SAP) D5"]
    #         elif i==6:
    #             k=row2["70% без ндс безнал (цена для выгрузуа SAP) D6"]
    #         elif i==7:
    #             k=row2["70% без ндс безнал (цена для выгрузуа SAP) D6"]
    #         data[6].append(k)
    #         data[7].append("UZS")
    #         data[8].append(1)
    #         data[9].append(row2["Ед.изм"])
    #         data[10].append(DATAB)
    #         data[11].append(DATBI)
    #         data[12].append("")
    #         data[13].append("")
    #         data[14].append("")
    #         data[15].append("ZUU")
        
    # new_row = {'KSCHL':data[0],	
    #         'VKORG':data[1],	
    #         'WERKS':data[2],	
    #         'VTWEG':data[3],	
    #         'KONDA':data[4],	
    #         'MATNR':data[5],	
    #         'KBETR':data[6],	
    #         'KONWA':data[7],	
    #         'KPEIN':data[8],	
    #         'KMEIN':data[9],	
    #         'DATAB':data[10],	
    #         'DATBI':data[11],	
    #         'KUNNR':data[12],	
    #         'FKART':data[13],	
    #         'AUART':data[14],	
    #         'AUGRU':data[15]
    # }

    # new_df =pd.DataFrame(new_row)
    # new_df =new_df[~pd.isna(new_df['KBETR'])]

    # new_df.to_excel(pathtext4,index=False)

    ################ 5 #######################

    # df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)


    # data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    # for i in range(1,8):
    #     for key2,row2 in df1.iterrows():
    #         d='D'+str(i)
    #         data[0].append("PR00")
    #         data[1].append(row2["Сбытовая организация"])
    #         data[2].append("")
    #         data[3].append("10")
    #         data[4].append(d)
    #         data[5].append(row2["sapcode"])
    #         if i==1:
    #             k=row2["30% Наличка D1"]
    #         elif i==2:
    #             k=row2["30% Наличка D2"]
    #         elif i==3:
    #             k=row2["30% Наличка D3"]
    #         elif i==4:
    #             k=row2["30% Наличка D4"]
    #         elif i==5:
    #             k=row2["30% Наличка D5"]
    #         elif i==6:
    #             k=row2["30% Наличка D6"]
    #         elif i==7:
    #             k=row2["30% Наличка D6"]
    #         data[6].append(k)
    #         data[7].append("UZS")
    #         data[8].append(1)
    #         data[9].append(row2["Ед.изм"])
    #         data[10].append(DATAB)
    #         data[11].append(DATBI)
    #         data[12].append("")
    #         data[13].append("ZFKN")
    #         data[14].append("")
    #         data[15].append("")
        
    # new_row = {'KSCHL':data[0],	
    #         'VKORG':data[1],	
    #         'WERKS':data[2],	
    #         'VTWEG':data[3],	
    #         'KONDA':data[4],	
    #         'MATNR':data[5],	
    #         'KBETR':data[6],	
    #         'KONWA':data[7],	
    #         'KPEIN':data[8],	
    #         'KMEIN':data[9],	
    #         'DATAB':data[10],	
    #         'DATBI':data[11],	
    #         'KUNNR':data[12],	
    #         'FKART':data[13],	
    #         'AUART':data[14],	
    #         'AUGRU':data[15]
    # }


    # new_df =pd.DataFrame(new_row)
    # new_df =new_df[~pd.isna(new_df['KBETR'])]
    # new_df.to_excel(pathtext5,index=False)

    ################ 6 ###################

    
    # df1 = pd.read_excel(f'{MEDIA_ROOT}/{path1}',sheet_name='Sheet1',header=0)


    # data =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    # for i in range(1,8):
    #     for key2,row2 in df1.iterrows():
    #         d='D'+str(i)
    #         data[0].append("PR00")
    #         data[1].append(row2["Сбытовая организация"])
    #         data[2].append("")
    #         data[3].append("10")
    #         data[4].append(d)
    #         data[5].append(row2["sapcode"])
    #         if i==1:
    #             k=row2["30% Наличка D1"]
    #         elif i==2:
    #             k=row2["30% Наличка D2"]
    #         elif i==3:
    #             k=row2["30% Наличка D3"]
    #         elif i==4:
    #             k=row2["30% Наличка D4"]
    #         elif i==5:
    #             k=row2["30% Наличка D5"]
    #         elif i==6:
    #             k=row2["30% Наличка D6"]
    #         elif i==7:
    #             k=row2["30% Наличка D6"]
    #         data[6].append(k)
    #         data[7].append("UZS")
    #         data[8].append(1)
    #         data[9].append(row2["Ед.изм"])
    #         data[10].append(DATAB)
    #         data[11].append(DATBI)
    #         data[12].append("")
    #         data[13].append("ZFDN")
    #         data[14].append("")
    #         data[15].append("")
        
    # new_row = {'KSCHL':data[0],	
    #         'VKORG':data[1],	
    #         'WERKS':data[2],	
    #         'VTWEG':data[3],	
    #         'KONDA':data[4],	
    #         'MATNR':data[5],	
    #         'KBETR':data[6],	
    #         'KONWA':data[7],	
    #         'KPEIN':data[8],	
    #         'KMEIN':data[9],	
    #         'DATAB':data[10],	
    #         'DATBI':data[11],	
    #         'KUNNR':data[12],	
    #         'FKART':data[13],	
    #         'AUART':data[14],	
    #         'AUGRU':data[15]
    # }

    # new_df =pd.DataFrame(new_row)
    # new_df =new_df[~pd.isna(new_df['KBETR'])]

    # new_df.to_excel(pathtext6,index=False)




    file_path =f'{pathzip}.zip'

    zip(pathzip, pathzip)
    

    # files = [FileG(file=file_path,filetype='obichniy')]
    # context ={
    #     'files':files
    # }
    return file_path
  
   

