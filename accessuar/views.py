from django.shortcuts import render
from config.settings import MEDIA_ROOT,BASE_DIR
from .forms import AccessuarFileForm
from .models import AccessuarFiles,Norma,Siryo
import pandas as pd
from .utils import get_norma_df,get_norma_price,create_folder,lenght_generate_texcarta
from django.contrib.auth.decorators import login_required



class File:
    def __init__(self,file):
        self.file = file


@login_required(login_url='/accounts/login/')
def get_accessuar_sapcode(request):
    if request.method =='POST':
        ozmk = request.POST.get('ozmk',None)
          
        if ozmk:
            ozmks =ozmk.split()
            path = get_norma_df(ozmks)
            files = [File(file=p) for p in path]
            context ={
                'files':files,
                'section':'SAP code'
            }
            return render(request,'norma/accessuar/generated_files.html',context)
    else:
        return render(request,'norma/accessuar/norma_sapcode.html')
    
@login_required(login_url='/accounts/login/')
def get_accessuar_sapcode_narx(request):
    if request.method =='POST':
        ozmk = request.POST.get('ozmk',None)
          
        if ozmk:
            ozmks =ozmk.split()
            path = get_norma_price(ozmks)
            files = [File(file=p) for p in path]
            context ={
                'files':files,
                'section':'SAP code'
            }
            return render(request,'norma/accessuar/generated_files.html',context)
    else:
        return render(request,'norma/accessuar/norma_sapcode.html')
    
@login_required(login_url='/accounts/login/')
def get_accessuar_sapcode_texcarta(request):
    if request.method =='POST':
        ozmk = request.POST.get('ozmk',None)
          
        if ozmk:
            ozmks =ozmk.split()
            path = lenght_generate_texcarta(ozmks)
            files = [File(file=p) for p in path]
            context ={
                'files':files,
                'section':'SAP code'
            }
            return render(request,'norma/accessuar/generated_files.html',context)
    else:
        return render(request,'norma/accessuar/norma_sapcode.html')
    

@login_required(login_url='/accounts/login/')
def full_update_siryo(request):
    if request.method == 'POST':
        data = request.POST.copy()
        form = AccessuarFileForm(data, request.FILES)
        if form.is_valid():
            siryo = Siryo.objects.all()
            siryo.delete()
            form_file = form.save()
            file = form_file.file
            path =f'{MEDIA_ROOT}/{file}'
            
            df = pd.read_excel(path,header=0)
            for key,row in df.iterrows():
                Siryo(
                    data ={'sap_code':row['SAPCODE'],'menge':row['NARX'],'price':'0'}
                ).save()

    return render(request,'norma/benkam/main.html')


@login_required(login_url='/accounts/login/')
def full_update_norm(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['type']='termo'
        form = AccessuarFileForm(data, request.FILES)
        if form.is_valid():
            normaa = Norma.objects.all()
            normaa.delete()
            form_file = form.save()
            file = form_file.file
            path =f'{MEDIA_ROOT}/{file}'
            
            df = pd.read_excel(path,sheet_name='ГП ПЕРЕДЕЛИ',header=0)
            
            df = df.astype(str)
            df = df.replace('nan','0')
            df = df.replace('0.0','0')

            df_new_la_lc = pd.DataFrame()
            df_new_la_lc['Нумерация до SAPЛитё Алюмин.2 шт / Литё Цинк 1 шт'] = df['Нумерация до SAPЛитё Алюмин.2 шт / Литё Цинк 1 шт']
            df_new_la_lc['Литё Алюмин.2 шт / Литё Цинк 1 шт'] = df['Литё Алюмин.2 шт / Литё Цинк 1 шт']
            df_new_la_lc['БЕИЛитё Алюмин.2 шт / Литё Цинк 1 шт'] = df['БЕИЛитё Алюмин.2 шт / Литё Цинк 1 шт']
            df_new_la_lc['Вес плановыйЛитё Алюмин.2 шт / Литё Цинк 1 шт'] = df['Вес плановыйЛитё Алюмин.2 шт / Литё Цинк 1 шт']
            df_new_la_lc['Вес фактическийЛитё Алюмин.2 шт / Литё Цинк 1 шт'] = df['Вес фактическийЛитё Алюмин.2 шт / Литё Цинк 1 шт']

            data_la_lc = generate_datas(df_new_la_lc,['Нумерация до SAPЛитё Алюмин.2 шт / Литё Цинк 1 шт','Литё Алюмин.2 шт / Литё Цинк 1 шт','БЕИЛитё Алюмин.2 шт / Литё Цинк 1 шт','Вес плановыйЛитё Алюмин.2 шт / Литё Цинк 1 шт','Вес фактическийЛитё Алюмин.2 шт / Литё Цинк 1 шт'],'-LA/LC')
            data_la_lc = generate_sap_code_price(data_la_lc)
            
            df_new_pa = pd.DataFrame()
            df_new_pa['Нумерация до SAPЛитейный пресс машины мини Ал. 9 шт'] = df['Нумерация до SAPЛитейный пресс машины мини Ал. 9 шт']
            df_new_pa['Литейный пресс машины мини Ал. 9 шт'] = df['Литейный пресс машины мини Ал. 9 шт']
            df_new_pa['БЕИЛитейный пресс машины мини Ал. 9 шт'] = df['БЕИЛитейный пресс машины мини Ал. 9 шт']
            df_new_pa['Вес плановыйЛитейный пресс машины мини Ал. 9 шт'] = df['Вес плановыйЛитейный пресс машины мини Ал. 9 шт']
            df_new_pa['Вес фактическийЛитейный пресс машины мини Ал. 9 шт'] = df['Вес фактическийЛитейный пресс машины мини Ал. 9 шт']

            data_pa = generate_datas(df_new_pa,['Нумерация до SAPЛитейный пресс машины мини Ал. 9 шт','Литейный пресс машины мини Ал. 9 шт','БЕИЛитейный пресс машины мини Ал. 9 шт','Вес плановыйЛитейный пресс машины мини Ал. 9 шт','Вес фактическийЛитейный пресс машины мини Ал. 9 шт'],'-PA')
            data_pa = generate_sap_code_price(data_pa)

            df_new_pc = pd.DataFrame()
            df_new_pc['Нумерация до SAPЛитейный пресс машины мини Цинк 6 шт'] = df['Нумерация до SAPЛитейный пресс машины мини Цинк 6 шт']
            df_new_pc['Литейный пресс машины мини Цинк 6 шт'] = df['Литейный пресс машины мини Цинк 6 шт']
            df_new_pc['БЕИЛитейный пресс машины мини Цинк 6 шт'] = df['БЕИЛитейный пресс машины мини Цинк 6 шт']
            df_new_pc['Вес плановыйЛитейный пресс машины мини Цинк 6 шт'] = df['Вес плановыйЛитейный пресс машины мини Цинк 6 шт']
            df_new_pc['Вес фактическийЛитейный пресс машины мини Цинк 6 шт'] = df['Вес фактическийЛитейный пресс машины мини Цинк 6 шт']

            data_pc = generate_datas(df_new_pc,['Нумерация до SAPЛитейный пресс машины мини Цинк 6 шт','Литейный пресс машины мини Цинк 6 шт','БЕИЛитейный пресс машины мини Цинк 6 шт','Вес плановыйЛитейный пресс машины мини Цинк 6 шт','Вес фактическийЛитейный пресс машины мини Цинк 6 шт'],'-PC')
            data_pc = generate_sap_code_price(data_pc)

            df_new_mo = pd.DataFrame()
            df_new_mo['Нумерация до SAPМех. Обработка 20 шт'] = df['Нумерация до SAPМех. Обработка 20 шт']
            df_new_mo['Мех. Обработка 20 шт'] = df['Мех. Обработка 20 шт']
            df_new_mo['БЕИМех. Обработка 20 шт'] = df['БЕИМех. Обработка 20 шт']
            df_new_mo['Вес плановыйМех. Обработка 20 шт'] = df['Вес плановыйМех. Обработка 20 шт']
            df_new_mo['Вес фактическийМех. Обработка 20 шт'] = df['Вес фактическийМех. Обработка 20 шт']

            data_mo = generate_datas(df_new_mo,['Нумерация до SAPМех. Обработка 20 шт','Мех. Обработка 20 шт','БЕИМех. Обработка 20 шт','Вес плановыйМех. Обработка 20 шт','Вес фактическийМех. Обработка 20 шт'],'-MO')
            data_mo = generate_sap_code_price(data_mo)


            df_new_gz = pd.DataFrame()
            df_new_gz['Нумерация до SAPГальванизация'] = df['Нумерация до SAPГальванизация']
            df_new_gz['Гальванизация'] = df['Гальванизация']
            df_new_gz['БЕИГальванизация'] = df['БЕИГальванизация']
            df_new_gz['Вес плановыйГальванизация'] = df['Вес плановыйГальванизация']
            df_new_gz['Вес фактическийГальванизация'] = df['Вес фактическийГальванизация']

            data_gz = generate_datas(df_new_gz,['Нумерация до SAPГальванизация','Гальванизация','БЕИГальванизация','Вес плановыйГальванизация','Вес фактическийГальванизация'],'-GZ')
            data_gz = generate_sap_code_price(data_gz)



            
            df_new_ru = pd.DataFrame()
            df_new_ru['Нумерация до SAPРезка + Упк'] = df['Нумерация до SAPРезка + Упк']
            df_new_ru['Резка + Упк'] = df['Резка + Упк']
            df_new_ru['БЕИРезка + Упк'] = df['БЕИРезка + Упк']
            df_new_ru['Вес плановыйРезка + Упк'] = df['Вес плановыйРезка + Упк']
            df_new_ru['Вес фактическийРезка + Упк'] = df['Вес фактическийРезка + Упк']

            data_ru = generate_datas(df_new_ru,['Нумерация до SAPРезка + Упк','Резка + Упк','БЕИРезка + Упк','Вес плановыйРезка + Упк','Вес фактическийРезка + Упк'],'-RU')
            data_ru = generate_sap_code_price(data_ru)

            df_new_sn = pd.DataFrame()
            df_new_sn['Нумерация до SAPШтамповка'] = df['Нумерация до SAPШтамповка']
            df_new_sn['Штамповка'] = df['Штамповка']
            df_new_sn['БЕИШтамповка'] = df['БЕИШтамповка']
            df_new_sn['Вес плановыйШтамповка'] = df['Вес плановыйШтамповка']
            df_new_sn['Вес фактическийШтамповка'] = df['Вес фактическийШтамповка']

            data_sn = generate_datas(df_new_sn,['Нумерация до SAPШтамповка','Штамповка','БЕИШтамповка','Вес плановыйШтамповка','Вес фактическийШтамповка'],'-SN')
            data_sn = generate_sap_code_price(data_sn)


            df_new_vs = pd.DataFrame()
            df_new_vs['Нумерация до SAPВибро.Голтовка 8 шт и Сушка'] = df['Нумерация до SAPВибро.Голтовка 8 шт и Сушка']
            df_new_vs['Вибро.Голтовка 8 шт и Сушка'] = df['Вибро.Голтовка 8 шт и Сушка']
            df_new_vs['БЕИВибро.Голтовка 8 шт и Сушка'] = df['БЕИВибро.Голтовка 8 шт и Сушка']
            df_new_vs['Вес плановыйВибро.Голтовка 8 шт и Сушка'] = df['Вес плановыйВибро.Голтовка 8 шт и Сушка']
            df_new_vs['Вес фактическийВибро.Голтовка 8 шт и Сушка'] = df['Вес фактическийВибро.Голтовка 8 шт и Сушка']

            data_vs = generate_datas(df_new_vs,['Нумерация до SAPВибро.Голтовка 8 шт и Сушка','Вибро.Голтовка 8 шт и Сушка','БЕИВибро.Голтовка 8 шт и Сушка','Вес плановыйВибро.Голтовка 8 шт и Сушка','Вес фактическийВибро.Голтовка 8 шт и Сушка'],'-VS')
            data_vs = generate_sap_code_price(data_vs)


            df_new_kl = pd.DataFrame()
            df_new_kl['Нумерация до SAPПокраска + Нанесение логотипа (гравировка)'] = df['Нумерация до SAPПокраска + Нанесение логотипа (гравировка)']
            df_new_kl['Покраска + Нанесение логотипа (гравировка)'] = df['Покраска + Нанесение логотипа (гравировка)']
            df_new_kl['БЕИПокраска + Нанесение логотипа (гравировка)'] = df['БЕИПокраска + Нанесение логотипа (гравировка)']
            df_new_kl['Вес плановыйПокраска + Нанесение логотипа (гравировка)'] = df['Вес плановыйПокраска + Нанесение логотипа (гравировка)']
            df_new_kl['Вес фактическийПокраска + Нанесение логотипа (гравировка)'] = df['Вес фактическийПокраска + Нанесение логотипа (гравировка)']

            data_kl = generate_datas(df_new_kl,['Нумерация до SAPПокраска + Нанесение логотипа (гравировка)','Покраска + Нанесение логотипа (гравировка)','БЕИПокраска + Нанесение логотипа (гравировка)','Вес плановыйПокраска + Нанесение логотипа (гравировка)','Вес фактическийПокраска + Нанесение логотипа (гравировка)'],'-KL')
            data_kl = generate_sap_code_price(data_kl)


            df_new_sk = pd.DataFrame()
            df_new_sk['Нумерация до SAPШтамповка + Заготовка +Упк'] = df['Нумерация до SAPШтамповка + Заготовка +Упк']
            df_new_sk['Штамповка + Заготовка +Упк'] = df['Штамповка + Заготовка +Упк']
            df_new_sk['БЕИШтамповка + Заготовка +Упк'] = df['БЕИШтамповка + Заготовка +Упк']
            df_new_sk['Вес плановыйШтамповка + Заготовка +Упк'] = df['Вес плановыйШтамповка + Заготовка +Упк']
            df_new_sk['Вес фактическийШтамповка + Заготовка +Упк'] = df['Вес фактическийШтамповка + Заготовка +Упк']

            data_sk = generate_datas(df_new_sk,['Нумерация до SAPШтамповка + Заготовка +Упк','Штамповка + Заготовка +Упк','БЕИШтамповка + Заготовка +Упк','Вес плановыйШтамповка + Заготовка +Упк','Вес фактическийШтамповка + Заготовка +Упк'],'-SK')
            data_sk = generate_sap_code_price(data_sk)

            df_new_tp = pd.DataFrame()
            df_new_tp['Нумерация до SAPТермопласт автомат 7 шт + Упк'] = df['Нумерация до SAPТермопласт автомат 7 шт + Упк']
            df_new_tp['Термопласт автомат 7 шт + Упк'] = df['Термопласт автомат 7 шт + Упк']
            df_new_tp['БЕИТермопласт автомат 7 шт + Упк'] = df['БЕИТермопласт автомат 7 шт + Упк']
            df_new_tp['Вес плановыйТермопласт автомат 7 шт + Упк'] = df['Вес плановыйТермопласт автомат 7 шт + Упк']
            df_new_tp['Вес фактическийТермопласт автомат 7 шт + Упк'] = df['Вес фактическийТермопласт автомат 7 шт + Упк']

            data_tp = generate_datas(df_new_tp,['Нумерация до SAPТермопласт автомат 7 шт + Упк','Термопласт автомат 7 шт + Упк','БЕИТермопласт автомат 7 шт + Упк','Вес плановыйТермопласт автомат 7 шт + Упк','Вес фактическийТермопласт автомат 7 шт + Упк'],'-TP')
            data_tp = generate_sap_code_price(data_tp)


            df_new_zg = pd.DataFrame()
            df_new_zg['Нумерация до SAPЗаготовка и Упковка'] = df['Нумерация до SAPЗаготовка и Упковка']
            df_new_zg['Заготовка и Упковка'] = df['Заготовка и Упковка']
            df_new_zg['БЕИЗаготовка и Упковка'] = df['БЕИЗаготовка и Упковка']
            df_new_zg['Вес плановыйЗаготовка и Упковка'] = df['Вес плановыйЗаготовка и Упковка']
            df_new_zg['Вес фактическийЗаготовка и Упковка'] = df['Вес фактическийЗаготовка и Упковка']

            data_zg = generate_datas(df_new_zg,['Нумерация до SAPЗаготовка и Упковка','Заготовка и Упковка','БЕИЗаготовка и Упковка','Вес плановыйЗаготовка и Упковка','Вес фактическийЗаготовка и Упковка'],'-ZG')
            data_zg = generate_sap_code_price(data_zg)

            
            df_new_gp = pd.DataFrame()
            df_new_gp['Нумерация до SAPСборка + Упк'] = df['Нумерация до SAPСборка + Упк']
            df_new_gp['Сборка + Упк'] = df['Сборка + Упк']
            df_new_gp['БЕИСборка + Упк'] = df['БЕИСборка + Упк']
            df_new_gp['Вес плановыйСборка + Упк'] = df['Вес плановыйСборка + Упк']
            df_new_gp['Вес фактическийСборка + Упк'] = df['Вес фактическийСборка + Упк']

            data_gp = generate_datas(df_new_gp,['Нумерация до SAPСборка + Упк','Сборка + Упк','БЕИСборка + Упк','Вес плановыйСборка + Упк','Вес фактическийСборка + Упк'],'-7')
            data_gp = generate_sap_code_price(data_gp)
            
            data_list =data_gp + data_zg + data_tp + data_sk + data_kl + data_vs + data_sn + data_ru + data_gz + data_mo + data_pc +data_pa + data_la_lc
            instances_to_create = [Norma(data=data) for data in data_list]
            Norma.objects.bulk_create(instances_to_create)

    return render(request,'norma/benkam/main.html')



def generate_datas(df,names,type_profile) -> list:
    all_data = []
    sap_codesss = []
    for key,row in df.iterrows():
        if type_profile =='-LA/LC':
            conditon = ('-LA' in row[names[0]] or '-LC' in row[names[0]] or '-7' in row[names[0]]) and row[names[0]] not in sap_codesss
        else:
            conditon = (type_profile in row[names[0]]  or '-7' in row[names[0]]) and row[names[0]] not in sap_codesss
        
        if conditon:
            sap_codesss.append(row[names[0]])
            components = []
            collected_data ={}
            collected_data['sap_code'] =row[names[0]]
            collected_data['ves_corredted'] = False
            collected_data['kratkiy_tekst'] =row[names[1]]
            collected_data['price'] ='0'

            component_sap_codes = []

            for i in range(1,25):
                if type_profile =='-LA/LC':
                    if df.iloc[key + i][names[0]] != '0' and '-LA' not in df.iloc[key + i][names[0]] and '-LC' not in df.iloc[key + i][names[0]] and '-7' not in df.iloc[key + i][names[0]] and df.iloc[key + i][names[1]] != '0':
                        component_name =df.iloc[key + i][names[0]]
                        component_value =df.iloc[key + i][names[1]]
                        component_menge =df.iloc[key + i][names[2]]
                        component_ves =df.iloc[key + i][names[3]]   
                        component_fakt =df.iloc[key + i][names[4]]   
                        components.append([component_name,component_value,component_menge,'0',component_ves,'0',component_fakt,'0','0'])
                        
                        component_sap_codes.append(df.iloc[key + i][names[0]])
                    else:
                        break
                else:
                    if df.iloc[key + i][names[0]] != '0' and type_profile not in df.iloc[key + i][names[0]] and '-7' not in df.iloc[key + i][names[0]] and df.iloc[key + i][names[1]] != '0':
                        component_name =df.iloc[key + i][names[0]]
                        component_value =df.iloc[key + i][names[1]]
                        component_menge =df.iloc[key + i][names[2]]
                        component_ves =df.iloc[key + i][names[3]]  
                        component_fakt =df.iloc[key + i][names[4]]  
                        components.append([component_name,component_value,component_menge,'0',component_ves,'0',component_fakt,'0','0'])
                        
                        component_sap_codes.append(df.iloc[key + i][names[0]])
                    else:
                        break
            collected_data['component_sapcodes'] = component_sap_codes
            collected_data['components'] = components
            all_data.append(collected_data)

    return all_data



def generate_sap_code_price(sapcodes):
    siryolar = Siryo.objects.all()
    
    sapcodes_copy = sapcodes.copy()
    siryo_menge ={}
    siryo_price ={}
    for siryo in siryolar:
        siryo_menge[f'{siryo.data["sap_code"]}']=str(siryo.data["menge"])
        siryo_price[f'{siryo.data["sap_code"]}']=str(siryo.data["price"])


    # components.append([component_name,component_value,component_menge,'0',component_ves,'0',component_fakt,'0'])

    for i in range(0,len(sapcodes)):
        component_count = 0
        value = 0
        price = 0
        for j in range(0,len(sapcodes[i]['components'])):
            if sapcodes[i]['components'][j][0] in siryo_menge:
                sapcodes_copy[i]['components'][j][3] = (float(siryo_menge[sapcodes[i]['components'][j][0]]) )
                sapcodes_copy[i]['components'][j][5] =(float(siryo_menge[sapcodes[i]['components'][j][0]]) * float(sapcodes_copy[i]['components'][j][4]))
                value += float(siryo_menge[sapcodes[i]['components'][j][0]])
                component_count += 1
                
                if '-LA' in sapcodes[i]['sap_code'] or '-LC' in sapcodes[i]['sap_code']:
                    
                    sapcodes_copy[i]['components'][j][8] = sapcodes_copy[i]['components'][j][3]
                    sapcodes_copy[i]['components'][j][7] = float(sapcodes_copy[i]['components'][j][3]) * float(sapcodes_copy[i]['components'][j][4])/1000
                    price += float(sapcodes_copy[i]['components'][j][3]) * float(sapcodes_copy[i]['components'][j][4])/1000
                else:
                    print(sapcodes[i]['sap_code'],'Gp- 7777 >>>>>> ',siryo_price[sapcodes[i]['components'][j][0]])
                    sapcodes_copy[i]['components'][j][8] = float(siryo_price[sapcodes[i]['components'][j][0]])
                    if '-7' in sapcodes[i]['sap_code']:
                        if siryo_price[sapcodes[i]['components'][j][0]] !='0':
                            # sapcodes_copy[i]['components'][j][8] =
                            sapcodes_copy[i]['components'][j][7] =(float(siryo_price[sapcodes[i]['components'][j][0]]) * float(sapcodes_copy[i]['components'][j][6]))/1000
                            price += (float(siryo_price[sapcodes[i]['components'][j][0]]) * float(sapcodes_copy[i]['components'][j][6]))/1000
                        else:
                            sapcodes_copy[i]['components'][j][8] = sapcodes_copy[i]['components'][j][3]
                            sapcodes_copy[i]['components'][j][7] = float(sapcodes_copy[i]['components'][j][3]) * float(sapcodes_copy[i]['components'][j][4])/1000
                            price += float(sapcodes_copy[i]['components'][j][3]) * float(sapcodes_copy[i]['components'][j][4])/1000
                    else:
                        if siryo_price[sapcodes[i]['components'][j][0]] !='0':
                            sapcodes_copy[i]['components'][j][7] =(float(siryo_price[sapcodes[i]['components'][j][0]]) * float(sapcodes_copy[i]['components'][j][4]))/1000
                            price += (float(siryo_price[sapcodes[i]['components'][j][0]]) * float(sapcodes_copy[i]['components'][j][4]))/1000
                        else:
                            sapcodes_copy[i]['components'][j][8] = sapcodes_copy[i]['components'][j][3]
                            sapcodes_copy[i]['components'][j][7] = float(sapcodes_copy[i]['components'][j][3]) * float(sapcodes_copy[i]['components'][j][4])/1000
                            price += float(sapcodes_copy[i]['components'][j][3]) * float(sapcodes_copy[i]['components'][j][4])/1000
                        

        if component_count == len(sapcodes[i]['components']):
            sapcodes_copy[i]['ves_corredted'] = True
            sapcodes_copy[i]['price'] = price
            if Siryo.objects.filter(data__sap_code =sapcodes[i]['sap_code']).exists():
                siryo = Siryo.objects.filter(data__sap_code =sapcodes[i]['sap_code'])[:1].get()
                siryo.data['price'] = price
            else:
                Siryo(
                    data ={'sap_code':sapcodes[i]['sap_code'],'menge':value,'price':price}
                ).save()
        
    return sapcodes_copy
    





