from django.shortcuts import render
from config.settings import MEDIA_ROOT,BASE_DIR
from .forms import AccessuarFileForm
from .models import AccessuarFiles,Norma
import pandas as pd
from .utils import get_norma_df



class File:
    def __init__(self,file):
        self.file = file



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

            df_new_gp = pd.DataFrame()
            df_new_gp['Нумерация до SAPСборка + Упк'] = df['Нумерация до SAPСборка + Упк']
            df_new_gp['Сборка + Упк'] = df['Сборка + Упк']
            df_new_gp['БЕИСборка + Упк'] = df['БЕИСборка + Упк']
            df_new_gp['Вес плановыйСборка + Упк'] = df['Вес плановыйСборка + Упк']

            data_gp = generate_datas(df_new_gp,['Нумерация до SAPСборка + Упк','Сборка + Упк','БЕИСборка + Упк','Вес плановыйСборка + Упк'],'-7')
            
            df_new_zg = pd.DataFrame()
            df_new_zg['Нумерация до SAPЗаготовка и Упковка'] = df['Нумерация до SAPЗаготовка и Упковка']
            df_new_zg['Заготовка и Упковка'] = df['Заготовка и Упковка']
            df_new_zg['БЕИЗаготовка и Упковка'] = df['БЕИЗаготовка и Упковка']
            df_new_zg['Вес плановыйЗаготовка и Упковка'] = df['Вес плановыйЗаготовка и Упковка']

            data_zg = generate_datas(df_new_zg,['Нумерация до SAPЗаготовка и Упковка','Заготовка и Упковка','БЕИЗаготовка и Упковка','Вес плановыйЗаготовка и Упковка'],'-ZG')
            
            df_new_tp = pd.DataFrame()
            df_new_tp['Нумерация до SAPТермопласт автомат 7 шт + Упк'] = df['Нумерация до SAPТермопласт автомат 7 шт + Упк']
            df_new_tp['Термопласт автомат 7 шт + Упк'] = df['Термопласт автомат 7 шт + Упк']
            df_new_tp['БЕИТермопласт автомат 7 шт + Упк'] = df['БЕИТермопласт автомат 7 шт + Упк']
            df_new_tp['Вес плановыйТермопласт автомат 7 шт + Упк'] = df['Вес плановыйТермопласт автомат 7 шт + Упк']

            data_tp = generate_datas(df_new_tp,['Нумерация до SAPТермопласт автомат 7 шт + Упк','Термопласт автомат 7 шт + Упк','БЕИТермопласт автомат 7 шт + Упк','Вес плановыйТермопласт автомат 7 шт + Упк'],'-TP')
            
            df_new_sk = pd.DataFrame()
            df_new_sk['Нумерация до SAPШтамповка + Заготовка +Упк'] = df['Нумерация до SAPШтамповка + Заготовка +Упк']
            df_new_sk['Штамповка + Заготовка +Упк'] = df['Штамповка + Заготовка +Упк']
            df_new_sk['БЕИШтамповка + Заготовка +Упк'] = df['БЕИШтамповка + Заготовка +Упк']
            df_new_sk['Вес плановыйШтамповка + Заготовка +Упк'] = df['Вес плановыйШтамповка + Заготовка +Упк']

            data_sk = generate_datas(df_new_sk,['Нумерация до SAPШтамповка + Заготовка +Упк','Штамповка + Заготовка +Упк','БЕИШтамповка + Заготовка +Упк','Вес плановыйШтамповка + Заготовка +Упк'],'-SK')
            
            df_new_kl = pd.DataFrame()
            df_new_kl['Нумерация до SAPПокраска + Нанесение логотипа (гравировка)'] = df['Нумерация до SAPПокраска + Нанесение логотипа (гравировка)']
            df_new_kl['Покраска + Нанесение логотипа (гравировка)'] = df['Покраска + Нанесение логотипа (гравировка)']
            df_new_kl['БЕИПокраска + Нанесение логотипа (гравировка)'] = df['БЕИПокраска + Нанесение логотипа (гравировка)']
            df_new_kl['Вес плановыйПокраска + Нанесение логотипа (гравировка)'] = df['Вес плановыйПокраска + Нанесение логотипа (гравировка)']

            data_kl = generate_datas(df_new_kl,['Нумерация до SAPПокраска + Нанесение логотипа (гравировка)','Покраска + Нанесение логотипа (гравировка)','БЕИПокраска + Нанесение логотипа (гравировка)','Вес плановыйПокраска + Нанесение логотипа (гравировка)'],'-KL')
            
            df_new_vs = pd.DataFrame()
            df_new_vs['Нумерация до SAPВибро.Голтовка 8 шт и Сушка'] = df['Нумерация до SAPВибро.Голтовка 8 шт и Сушка']
            df_new_vs['Вибро.Голтовка 8 шт и Сушка'] = df['Вибро.Голтовка 8 шт и Сушка']
            df_new_vs['БЕИВибро.Голтовка 8 шт и Сушка'] = df['БЕИВибро.Голтовка 8 шт и Сушка']
            df_new_vs['Вес плановыйВибро.Голтовка 8 шт и Сушка'] = df['Вес плановыйВибро.Голтовка 8 шт и Сушка']

            data_vs = generate_datas(df_new_vs,['Нумерация до SAPВибро.Голтовка 8 шт и Сушка','Вибро.Голтовка 8 шт и Сушка','БЕИВибро.Голтовка 8 шт и Сушка','Вес плановыйВибро.Голтовка 8 шт и Сушка'],'-VS')
            
            df_new_sn = pd.DataFrame()
            df_new_sn['Нумерация до SAPШтамповка'] = df['Нумерация до SAPШтамповка']
            df_new_sn['Штамповка'] = df['Штамповка']
            df_new_sn['БЕИШтамповка'] = df['БЕИШтамповка']
            df_new_sn['Вес плановыйШтамповка'] = df['Вес плановыйШтамповка']

            data_sn = generate_datas(df_new_sn,['Нумерация до SAPШтамповка','Штамповка','БЕИШтамповка','Вес плановыйШтамповка'],'-SN')
            
            df_new_ru = pd.DataFrame()
            df_new_ru['Нумерация до SAPРезка + Упк'] = df['Нумерация до SAPРезка + Упк']
            df_new_ru['Резка + Упк'] = df['Резка + Упк']
            df_new_ru['БЕИРезка + Упк'] = df['БЕИРезка + Упк']
            df_new_ru['Вес плановыйРезка + Упк'] = df['Вес плановыйРезка + Упк']

            data_ru = generate_datas(df_new_ru,['Нумерация до SAPРезка + Упк','Резка + Упк','БЕИРезка + Упк','Вес плановыйРезка + Упк'],'-RU')
            
            
            df_new_gz = pd.DataFrame()
            df_new_gz['Нумерация до SAPГальванизация'] = df['Нумерация до SAPГальванизация']
            df_new_gz['Гальванизация'] = df['Гальванизация']
            df_new_gz['БЕИГальванизация'] = df['БЕИГальванизация']
            df_new_gz['Вес плановыйГальванизация'] = df['Вес плановыйГальванизация']

            data_gz = generate_datas(df_new_gz,['Нумерация до SAPГальванизация','Гальванизация','БЕИГальванизация','Вес плановыйГальванизация'],'-GZ')
            
            
            df_new_mo = pd.DataFrame()
            df_new_mo['Нумерация до SAPМех. Обработка 20 шт'] = df['Нумерация до SAPМех. Обработка 20 шт']
            df_new_mo['Мех. Обработка 20 шт'] = df['Мех. Обработка 20 шт']
            df_new_mo['БЕИМех. Обработка 20 шт'] = df['БЕИМех. Обработка 20 шт']
            df_new_mo['Вес плановыйМех. Обработка 20 шт'] = df['Вес плановыйМех. Обработка 20 шт']

            data_mo = generate_datas(df_new_mo,['Нумерация до SAPМех. Обработка 20 шт','Мех. Обработка 20 шт','БЕИМех. Обработка 20 шт','Вес плановыйМех. Обработка 20 шт'],'-MO')
            
            df_new_pc = pd.DataFrame()
            df_new_pc['Нумерация до SAPЛитейный пресс машины мини Цинк 6 шт'] = df['Нумерация до SAPЛитейный пресс машины мини Цинк 6 шт']
            df_new_pc['Литейный пресс машины мини Цинк 6 шт'] = df['Литейный пресс машины мини Цинк 6 шт']
            df_new_pc['БЕИЛитейный пресс машины мини Цинк 6 шт'] = df['БЕИЛитейный пресс машины мини Цинк 6 шт']
            df_new_pc['Вес плановыйЛитейный пресс машины мини Цинк 6 шт'] = df['Вес плановыйЛитейный пресс машины мини Цинк 6 шт']

            data_pc = generate_datas(df_new_pc,['Нумерация до SAPЛитейный пресс машины мини Цинк 6 шт','Литейный пресс машины мини Цинк 6 шт','БЕИЛитейный пресс машины мини Цинк 6 шт','Вес плановыйЛитейный пресс машины мини Цинк 6 шт'],'-PC')
            
            df_new_pa = pd.DataFrame()
            df_new_pa['Нумерация до SAPЛитейный пресс машины мини Ал. 9 шт'] = df['Нумерация до SAPЛитейный пресс машины мини Ал. 9 шт']
            df_new_pa['Литейный пресс машины мини Ал. 9 шт'] = df['Литейный пресс машины мини Ал. 9 шт']
            df_new_pa['БЕИЛитейный пресс машины мини Ал. 9 шт'] = df['БЕИЛитейный пресс машины мини Ал. 9 шт']
            df_new_pa['Вес плановыйЛитейный пресс машины мини Ал. 9 шт'] = df['Вес плановыйЛитейный пресс машины мини Ал. 9 шт']

            data_pa = generate_datas(df_new_pa,['Нумерация до SAPЛитейный пресс машины мини Ал. 9 шт','Литейный пресс машины мини Ал. 9 шт','БЕИЛитейный пресс машины мини Ал. 9 шт','Вес плановыйЛитейный пресс машины мини Ал. 9 шт'],'-PA')
            
            df_new_la_lc = pd.DataFrame()
            df_new_la_lc['Нумерация до SAPЛитё Алюмин.2 шт / Литё Цинк 1 шт'] = df['Нумерация до SAPЛитё Алюмин.2 шт / Литё Цинк 1 шт']
            df_new_la_lc['Литё Алюмин.2 шт / Литё Цинк 1 шт'] = df['Литё Алюмин.2 шт / Литё Цинк 1 шт']
            df_new_la_lc['БЕИЛитё Алюмин.2 шт / Литё Цинк 1 шт'] = df['БЕИЛитё Алюмин.2 шт / Литё Цинк 1 шт']
            df_new_la_lc['Вес плановыйЛитё Алюмин.2 шт / Литё Цинк 1 шт'] = df['Вес плановыйЛитё Алюмин.2 шт / Литё Цинк 1 шт']

            data_la_lc = generate_datas(df_new_la_lc,['Нумерация до SAPЛитё Алюмин.2 шт / Литё Цинк 1 шт','Литё Алюмин.2 шт / Литё Цинк 1 шт','БЕИЛитё Алюмин.2 шт / Литё Цинк 1 шт','Вес плановыйЛитё Алюмин.2 шт / Литё Цинк 1 шт'],'-LA/LC')
            
            
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
            collected_data['kratkiy_tekst'] =row[names[1]]
            component_sap_codes = []

            for i in range(1,25):
                if type_profile =='-LA/LC':
                    if df.iloc[key + i][names[0]] != '0' and '-LA' not in df.iloc[key + i][names[0]] and '-LC' not in df.iloc[key + i][names[0]] and '-7' not in df.iloc[key + i][names[0]] and df.iloc[key + i][names[1]] != '0':
                        component_name =df.iloc[key + i][names[0]]
                        component_value =df.iloc[key + i][names[1]]
                        component_menge =df.iloc[key + i][names[2]]
                        component_ves =df.iloc[key + i][names[3]]   
                        components.append([component_name,component_value,component_menge,component_ves])
                        component_sap_codes.append(df.iloc[key + i][names[0]])
                    else:
                        break
                    

                else:
                    if type_profile =='-RU':
                        contd1 =df.iloc[key + i][names[0]] != '0' 
                        contd2 = type_profile not in df.iloc[key + i][names[0]] 
                        contd3 ='-7' not in df.iloc[key + i][names[0]] 
                        contd4 = df.iloc[key + i][names[1]] != '0'
                        print('profile= ',df.iloc[key][names[0]])
                        print('component = ',df.iloc[key+i][names[0]],contd1,contd2,contd3,contd4,'value= ',df.iloc[key + i][names[1]])

                    if df.iloc[key + i][names[0]] != '0' and type_profile not in df.iloc[key + i][names[0]] and '-7' not in df.iloc[key + i][names[0]] and df.iloc[key + i][names[1]] != '0':
                        if type_profile =='-RU':
                            print('components =',df.iloc[key + i][names[0]])
                        component_name =df.iloc[key + i][names[0]]
                        component_value =df.iloc[key + i][names[1]]
                        component_menge =df.iloc[key + i][names[2]]
                        component_ves =df.iloc[key + i][names[3]]   
                        components.append([component_name,component_value,component_menge,component_ves])
                        component_sap_codes.append(df.iloc[key + i][names[0]])
                    else:
                        break
            collected_data['component_sapcodes'] = component_sap_codes
            collected_data['components'] = components
            all_data.append(collected_data)

    return all_data






# def lenght_generate_texcarta(request,id):
#     file = NormaExcelFiles.objects.get(id=id).file
#     file_path =f'{MEDIA_ROOT}\\{file}'
#     df =pd.read_excel(file_path)

#     df =df.astype(str)
#     df=df.replace('nan','')

#     df_list = []
#     df_list_no_dubl = []

#     df_list_gp = [[],[],[],[]]

#     for key,row in df.iterrows():
#         if 'SAP код K'in row:
#             df_list.append([
#                 row['SAP код E'],row['Экструзия холодная резка'],
#                 row['SAP код Z'],row['Печь старения'],
#                 row['SAP код P'],row['Покраска автомат'],
#                 row['SAP код S'],row['Сублимация'],
#                 row['SAP код A'],row['Анодировка'],
#                 row['SAP код N'],row['Наклейка'],
#                 row['SAP код K'],row['K-Комбинирования'],
#                 row['SAP код 7'],row['U-Упаковка + Готовая Продукция'],
#                 row['SAP код F'],row['Фабрикация'],
#                 row['SAP код 75'],row['U-Упаковка + Готовая Продукция 75'],
#             ])
            
#             if row['SAP код F']!='' and row['SAP код 75']!='':
#                 if not TexcartaBase.objects.filter(material = row['SAP код 75']).exists():
#                     df_list_gp[0].append('1201')
#                     df_list_gp[1].append('12017500')
#                     df_list_gp[2].append('1')
#                     df_list_gp[3].append(row['SAP код 75'])
#                     TexcartaBase(material = row['SAP код 75']).save()
#             elif row['SAP код K']!='' and row['SAP код 7']!='':   
#                 if not TexcartaBase.objects.filter(material = row['SAP код 7']).exists():
#                     df_list_gp[0].append('1201')
#                     df_list_gp[1].append('12017000')
#                     df_list_gp[2].append('2')
#                     df_list_gp[3].append(row['SAP код 7'])
#                     TexcartaBase(material = row['SAP код 7']).save()

#             if row['SAP код K'] != '':
#                 if not TexcartaBase.objects.filter(material = row['SAP код K']).exists():
#                     df_list_gp[0].append('1201')
#                     df_list_gp[1].append('1201K001')
#                     df_list_gp[2].append('1')
#                     df_list_gp[3].append(row['SAP код K'])

#                     df_list_gp[0].append('1201')
#                     df_list_gp[1].append('1201K002')
#                     df_list_gp[2].append('1')
#                     df_list_gp[3].append(row['SAP код K'])
#                     TexcartaBase(material = row['SAP код K']).save()
            
#             if row['SAP код N'] != '':
#                 if not TexcartaBase.objects.filter(material = row['SAP код N']).exists():
#                     df_list_gp[0].append('1201')
#                     df_list_gp[1].append('1201N000')
#                     df_list_gp[2].append('1')
#                     df_list_gp[3].append(row['SAP код N'])
#                     TexcartaBase(material = row['SAP код N']).save()

#             if row['SAP код F'] != '':
#                 if not TexcartaBase.objects.filter(material = row['SAP код F']).exists():
#                     df_list_gp[0].append('1201')
#                     df_list_gp[1].append('1201F001')
#                     df_list_gp[2].append('1')
#                     df_list_gp[3].append(row['SAP код F'])
#                     TexcartaBase(material = row['SAP код F']).save()
#         else:
#             df_list.append([
#                 row['SAP код E'],row['Экструзия холодная резка'],
#                 row['SAP код Z'],row['Печь старения'],
#                 row['SAP код P'],row['Покраска автомат'],
#                 row['SAP код S'],row['Сублимация'],
#                 row['SAP код A'],row['Анодировка'],
#                 row['SAP код N'],row['Наклейка'],
#                 row['SAP код 7'],row['U-Упаковка + Готовая Продукция'],
#                 row['SAP код F'],row['Фабрикация'],
#                 row['SAP код 75'],row['U-Упаковка + Готовая Продукция 75'],
#             ])
        
#             if row['SAP код N']!='' and row['SAP код 7']!='':
#                 if not TexcartaBase.objects.filter(material = row['SAP код 7']).exists():
#                     df_list_gp[0].append('1201')
#                     df_list_gp[1].append('12017601')
#                     df_list_gp[2].append('1')
#                     df_list_gp[3].append(row['SAP код 7'])
#                     TexcartaBase(material = row['SAP код 7']).save()
#             elif row['SAP код N']=='' and row['SAP код 7']!='' :
#                 if not TexcartaBase.objects.filter(material = row['SAP код 7']).exists():
#                     df_list_gp[0].append('1201')
#                     df_list_gp[1].append('12017000')
#                     df_list_gp[2].append('2')
#                     df_list_gp[3].append(row['SAP код 7'])
#                     TexcartaBase(material = row['SAP код 7']).save()
            
#             if row['SAP код N'] != '':
#                 if not TexcartaBase.objects.filter(material = row['SAP код N']).exists():
#                     df_list_gp[0].append('1201')
#                     df_list_gp[1].append('1201N000')
#                     df_list_gp[2].append('1')
#                     df_list_gp[3].append(row['SAP код N'])
#                     TexcartaBase(material = row['SAP код N']).save()

#             if row['SAP код F'] != '':
#                 if not TexcartaBase.objects.filter(material = row['SAP код F']).exists():
#                     df_list_gp[0].append('1201')
#                     df_list_gp[1].append('1201F001')
#                     df_list_gp[2].append('1')
#                     df_list_gp[3].append(row['SAP код F'])
#                     TexcartaBase(material = row['SAP код F']).save()

#             if row['SAP код F']!='' and row['SAP код 75']!='':
#                 if not TexcartaBase.objects.filter(material = row['SAP код 75']).exists():
#                     df_list_gp[0].append('1201')
#                     df_list_gp[1].append('12017500')
#                     df_list_gp[2].append('1')
#                     df_list_gp[3].append(row['SAP код 75'])
#                     TexcartaBase(material = row['SAP код 75']).save()



#         if row['SAP код E'] !='':
#                 df_list_no_dubl.append({'МАТЕРИАЛ':row['SAP код E'],'КРАТКИЙ ТЕКСТ':row['Экструзия холодная резка']})
#         if row['SAP код Z'] !='':
#             df_list_no_dubl.append({'МАТЕРИАЛ':row['SAP код Z'],'КРАТКИЙ ТЕКСТ':row['Печь старения']})
#         if row['SAP код P'] !='':
#             df_list_no_dubl.append({'МАТЕРИАЛ':row['SAP код P'],'КРАТКИЙ ТЕКСТ':row['Покраска автомат']})
#         if row['SAP код S'] !='':
#             df_list_no_dubl.append({'МАТЕРИАЛ':row['SAP код S'],'КРАТКИЙ ТЕКСТ':row['Сублимация']})
#         if row['SAP код A'] !='':
#             df_list_no_dubl.append({'МАТЕРИАЛ':row['SAP код A'],'КРАТКИЙ ТЕКСТ':row['Анодировка']})


#     counter = 0
#     for row in df_list_no_dubl:
#         if not TexcartaBase.objects.filter(material = row['МАТЕРИАЛ']).exists():
#             if '-A' in row['МАТЕРИАЛ']:
#                 counter +=3
#             elif '-S' in row['МАТЕРИАЛ']:
#                 counter +=8
#             elif '-Z' in row['МАТЕРИАЛ']:
#                 counter +=2
#             elif '-E' in row['МАТЕРИАЛ']:
#                 counter +=18
#             elif '-P' in row['МАТЕРИАЛ']:
#                 counter +=6
       

  
#     df_new = pd.DataFrame()
#     df_new['counter'] =[ '' for i in range(0,counter)]
#     df_new['ID']=''
#     df_new['MATNR']=''
#     df_new['WERKS']=''
#     df_new['PLNNR']=''
#     df_new['STTAG']=''
#     df_new['PLNAL']=''
#     df_new['KTEXT']=''
#     df_new['VERWE']=''
#     df_new['STATU']=''
#     df_new['LOSVN']=''
#     df_new['LOSBS']=''
#     df_new['VORNR']=''
#     df_new['ARBPL']=''
#     df_new['WERKS1']=''
#     df_new['STEUS']=''
#     df_new['LTXA1']=''
#     df_new['BMSCH']=''
#     df_new['MEINH']=''
#     df_new['VGW01']=''
#     df_new['VGE01']=''
#     df_new['ACTTYPE_01']=''
#     df_new['CKSELKZ']=''
#     df_new['UMREZ']=""
#     df_new['UMREN']=''
#     df_new['USR00']=''
#     df_new['USR01']=''
    

    
            
    
    


#     counter_2 = 0
#     for row in df_list_no_dubl:
#         if not TexcartaBase.objects.filter(material = row['МАТЕРИАЛ']).exists():
#             length = row['МАТЕРИАЛ'].split('-')[0]
#             norma = Norma.objects.filter(data__новый__icontains=length)[:1].get()

#             L = get_legth(row['КРАТКИЙ ТЕКСТ'])
            
#             if '-A' in row['МАТЕРИАЛ']:
#                 anod_kod = row['КРАТКИЙ ТЕКСТ'].split()[-1]
#                 bmsch = 35 if anod_kod in ['15023','15024','15025','15033','15034','15035','15043','15044','15045','15053','15054','15055'] else 50
#                 for i7 in range(1,4):
#                     if i7 ==1:
#                         df_new['ID'][counter_2] ='1'
#                         df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
#                         df_new['WERKS'][counter_2] ='1201'
#                         df_new['STTAG'][counter_2] ='01012022'
#                         df_new['PLNAL'][counter_2] ='1'
#                         df_new['KTEXT'][counter_2] ='Анодирование \ Анодирование (Вход)'
#                         df_new['VERWE'][counter_2] ='1'
#                         df_new['STATU'][counter_2] ='4'
#                         df_new['LOSVN'][counter_2] ='1'
#                         df_new['LOSBS'][counter_2] ='99999999'
#                     elif i7 == 2:
#                         df_new['ID'][counter_2]='2'
#                         df_new['VORNR'][counter_2] ='0010'
#                         df_new['ARBPL'][counter_2] ='1201A902'
#                         df_new['WERKS1'][counter_2] ='1201'
#                         df_new['STEUS'][counter_2] ='ZK01'
#                         df_new['LTXA1'][counter_2] ='Анодирование \ Анодирование (Вход)'
#                         df_new['BMSCH'][counter_2] = bmsch
#                         df_new['MEINH'][counter_2] ='M2'
#                         df_new['VGW01'][counter_2] ='1'
#                         df_new['VGE01'][counter_2] ='STD'
#                         df_new['ACTTYPE_01'][counter_2] ='200130'
#                         df_new['CKSELKZ'][counter_2] ='X'
#                         df_new['UMREZ'][counter_2] = '1000'
#                         df_new['UMREN'][counter_2] = int(float(norma.data['Площадь поверхности 1000шт профилей/м²'].replace(',','.'))*float(L)/(6))
#                         df_new['USR00'][counter_2] = '1'
#                         df_new['USR01'][counter_2] = ("%.3f" % ((L*1000*3600*float(norma.data['Площадь поверхности 1000шт профилей/м²'].replace(',','.')))/(6000000*bmsch)))
                       
#                     elif i7 == 3:
#                         df_new['ID'][counter_2]='2'
#                         df_new['VORNR'][counter_2] ='0020'
#                         df_new['ARBPL'][counter_2] ='1201A901'
#                         df_new['WERKS1'][counter_2] ='1201'
#                         df_new['STEUS'][counter_2] ='ZK01'
#                         df_new['LTXA1'][counter_2] ='Анодирование \ Анодирование (Выход)'
#                         df_new['BMSCH'][counter_2] = '1000'
#                         df_new['MEINH'][counter_2] ='ST'
#                         df_new['VGW01'][counter_2] ='1'
#                         df_new['VGE01'][counter_2] ='S'
#                         df_new['ACTTYPE_01'][counter_2] ='200130'
#                         df_new['CKSELKZ'][counter_2] =''
#                         df_new['UMREZ'][counter_2] = '1000'
#                         df_new['UMREN'][counter_2] = '1000'
#                         df_new['USR00'][counter_2] = '1'
#                         df_new['USR01'][counter_2] = ("%.3f" % ((L*1000*3600*float(norma.data['Площадь поверхности 1000шт профилей/м²'].replace(',','.')))/(6000000*bmsch)))
                        
#                     counter_2 +=1
#                 TexcartaBase(material = row['МАТЕРИАЛ']).save()
#             elif '-S' in row['МАТЕРИАЛ']:
#                 for p in range(1,5):
#                     for i7 in range(1,3):
#                         if i7 ==1:
#                             df_new['ID'][counter_2] ='1'
#                             df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
#                             df_new['WERKS'][counter_2] ='1201'
#                             df_new['STTAG'][counter_2] ='01012022'
#                             df_new['PLNAL'][counter_2] ='1'
#                             df_new['KTEXT'][counter_2] ='Сублимация'+' №'+str(p)+' \ Сублимирование'
#                             df_new['VERWE'][counter_2] ='1'
#                             df_new['STATU'][counter_2] ='4'
#                             df_new['LOSVN'][counter_2] ='1'
#                             df_new['LOSBS'][counter_2] ='99999999'
#                         elif i7 == 2:
#                             df_new['ID'][counter_2]='2'
#                             df_new['VORNR'][counter_2] ='0010'
#                             df_new['ARBPL'][counter_2] ='1201B20' + str(p)
#                             df_new['WERKS1'][counter_2] ='1201'
#                             df_new['STEUS'][counter_2] ='ZK01'
#                             df_new['LTXA1'][counter_2] ='Сублимация'+' №'+str(p)+' \ Сублимирование'
#                             df_new['BMSCH'][counter_2] = '61914'
#                             df_new['MEINH'][counter_2] ='MM'
#                             df_new['VGW01'][counter_2] ='1'
#                             df_new['VGE01'][counter_2] ='STD'
#                             df_new['ACTTYPE_01'][counter_2] ='200050'
#                             df_new['CKSELKZ'][counter_2] ='X'
#                             df_new['UMREZ'][counter_2] = '10'
#                             df_new['UMREN'][counter_2] = int(float(norma.data['Внешний периметр профиля/ мм'].replace(',','.')) * 10)
#                             df_new['USR00'][counter_2] = '1'
#                             df_new['USR01'][counter_2] = '12'
                            
#                         counter_2 +=1
#                 TexcartaBase(material = row['МАТЕРИАЛ']).save()
#             elif '-E' in row['МАТЕРИАЛ']:
#                 for t in range(1,7):
#                     for i7 in range(1,4):
#                         if i7 ==1:
#                             df_new['ID'][counter_2] ='1'
#                             df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
#                             df_new['WERKS'][counter_2] ='1201'
#                             df_new['STTAG'][counter_2] ='01012022'
#                             df_new['PLNAL'][counter_2] ='1'
#                             df_new['KTEXT'][counter_2] =BAZA['E'][f'{t}']['KTEXT'][0]
#                             df_new['VERWE'][counter_2] ='1'
#                             df_new['STATU'][counter_2] ='4'
#                             df_new['LOSVN'][counter_2] ='1'
#                             df_new['LOSBS'][counter_2] ='99999999'
#                         elif i7 == 2:
#                             df_new['ID'][counter_2]='2'
#                             df_new['VORNR'][counter_2] =BAZA['E'][f'{t}']['VORNR'][0]
#                             df_new['ARBPL'][counter_2] =BAZA['E'][f'{t}']['ARBPL'][0]
#                             df_new['WERKS1'][counter_2] ='1201'
#                             df_new['STEUS'][counter_2] ='ZK01'
#                             df_new['LTXA1'][counter_2] =BAZA['E'][f'{t}']['LTXA1'][0]
#                             df_new['BMSCH'][counter_2] = BAZA['E'][f'{t}']['BMSCH'][0]
#                             df_new['MEINH'][counter_2] ='KG'
#                             df_new['VGW01'][counter_2] ='1'
#                             df_new['VGE01'][counter_2] ='STD'
#                             df_new['ACTTYPE_01'][counter_2] ='200020'
#                             df_new['CKSELKZ'][counter_2] ='X'
#                             df_new['UMREZ'][counter_2] = '1000'
#                             df_new['UMREN'][counter_2] = int(float(norma.data['Удельный вес профиля кг/м'].replace(',','.')) * float(L) *1000)
#                             df_new['USR00'][counter_2] = '1'
#                             df_new['USR01'][counter_2] = ("%.3f" % (float(norma.data['Удельный вес профиля кг/м'].replace(',','.')) * float(L) *3600/float(BAZA['E'][f'{t}']['BMSCH'][0])))
                            
#                         elif i7 == 3:
#                             df_new['ID'][counter_2]='2'
#                             df_new['VORNR'][counter_2] =BAZA['E'][f'{t}']['VORNR'][1]
#                             df_new['ARBPL'][counter_2] =BAZA['E'][f'{t}']['ARBPL'][1]
#                             df_new['WERKS1'][counter_2] ='1201'
#                             df_new['STEUS'][counter_2] ='ZK01'
#                             df_new['LTXA1'][counter_2] =BAZA['E'][f'{t}']['LTXA1'][1]
#                             df_new['BMSCH'][counter_2] = '620660'
#                             df_new['MEINH'][counter_2] ='MM2'
#                             df_new['VGW01'][counter_2] ='1'
#                             df_new['VGE01'][counter_2] ='STD'
#                             df_new['ACTTYPE_01'][counter_2] ='200020'
#                             df_new['CKSELKZ'][counter_2] =''
#                             df_new['UMREZ'][counter_2] = '10'
#                             df_new['UMREN'][counter_2] = int(float(norma.data['Площадь /мм²'].replace(',','.')) * L * 10/(6))
#                             df_new['USR00'][counter_2] = '1'
#                             df_new['USR01'][counter_2] = '50'
                            
#                         counter_2 +=1
#                 TexcartaBase(material = row['МАТЕРИАЛ']).save()             
#             elif '-Z' in row['МАТЕРИАЛ']:
#                 for i7 in range(1,3):
#                     if i7 ==1:
#                         df_new['ID'][counter_2] ='1'
#                         df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
#                         df_new['WERKS'][counter_2] ='1201'
#                         df_new['STTAG'][counter_2] ='01012022'
#                         df_new['PLNAL'][counter_2] ='1'
#                         df_new['KTEXT'][counter_2] ='Печь старения (все) \ Термическая обработка (упрочение) алюм'
#                         df_new['VERWE'][counter_2] ='1'
#                         df_new['STATU'][counter_2] ='4'
#                         df_new['LOSVN'][counter_2] ='1'
#                         df_new['LOSBS'][counter_2] ='99999999'
#                     elif i7 == 2:
#                         df_new['ID'][counter_2]='2'
#                         df_new['VORNR'][counter_2] ='0010'
#                         df_new['ARBPL'][counter_2] ='1201A500'
#                         df_new['WERKS1'][counter_2] ='1201'
#                         df_new['STEUS'][counter_2] ='ZK01'
#                         df_new['LTXA1'][counter_2] ='Печь старения (все) \ Термическая обработка (упрочение) алюм'
#                         df_new['BMSCH'][counter_2] ='12500'
#                         df_new['MEINH'][counter_2] ='KG'
#                         df_new['VGW01'][counter_2] ='1'
#                         df_new['VGE01'][counter_2] ='STD'
#                         df_new['ACTTYPE_01'][counter_2] ='200030'
#                         df_new['CKSELKZ'][counter_2] ='X'
#                         df_new['UMREZ'][counter_2] = '1000'
#                         df_new['UMREN'][counter_2] = int(float(norma.data['Удельный вес профиля кг/м'].replace(',','.')) * float(L) *1000)
#                         df_new['USR00'][counter_2] = '1'
#                         df_new['USR01'][counter_2] = ("%.3f" % (float(norma.data['Удельный вес профиля кг/м'].replace(',','.')) * float(L) *3600/(12500)))
                        
#                     counter_2 +=1
#                 TexcartaBase(material = row['МАТЕРИАЛ']).save()
#             elif '-P' in row['МАТЕРИАЛ']:
#                 for p in range(1,3):
#                     for i in range(1,4):
#                         if i ==1:
#                             df_new['ID'][counter_2] ='1'
#                             df_new['MATNR'][counter_2] = row['МАТЕРИАЛ']
#                             df_new['WERKS'][counter_2] ='1201'
#                             df_new['STTAG'][counter_2] ='01012022'
#                             df_new['PLNAL'][counter_2] ='1'
#                             df_new['KTEXT'][counter_2] =BAZA['P'][f'{p}']['KTEXT'][0]
#                             df_new['VERWE'][counter_2] ='1'
#                             df_new['STATU'][counter_2] ='4'
#                             df_new['LOSVN'][counter_2] ='1'
#                             df_new['LOSBS'][counter_2] ='99999999'
#                         elif i == 2:
#                             df_new['ID'][counter_2]='2'
#                             df_new['VORNR'][counter_2] =BAZA['P'][f'{p}']['VORNR'][0]
#                             df_new['ARBPL'][counter_2] =BAZA['P'][f'{p}']['ARBPL'][0]
#                             df_new['WERKS1'][counter_2] ='1201'
#                             df_new['STEUS'][counter_2] ='ZK01'
#                             df_new['LTXA1'][counter_2] =BAZA['P'][f'{p}']['LTXA1'][0]
#                             df_new['BMSCH'][counter_2] ='3600'
#                             df_new['MEINH'][counter_2] ='KG'
#                             df_new['VGW01'][counter_2] ='1'
#                             df_new['VGE01'][counter_2] ='STD'
#                             df_new['ACTTYPE_01'][counter_2] ='200040'
#                             df_new['CKSELKZ'][counter_2] ='X'
#                             df_new['UMREZ'][counter_2] = '1000'
#                             df_new['UMREN'][counter_2] = int(float(norma.data['Удельный вес профиля кг/м'].replace(',','.')) * float(L) *1000)
#                             df_new['USR00'][counter_2] = '1'
#                             df_new['USR01'][counter_2] ='3'
                            
#                         elif i == 3:
#                             df_new['ID'][counter_2]='2'
#                             df_new['VORNR'][counter_2] =BAZA['P'][f'{p}']['VORNR'][1]
#                             df_new['ARBPL'][counter_2] =BAZA['P'][f'{p}']['ARBPL'][1]
#                             df_new['WERKS1'][counter_2] ='1201'
#                             df_new['STEUS'][counter_2] ='ZK01'
#                             df_new['LTXA1'][counter_2] =BAZA['P'][f'{p}']['LTXA1'][1]
#                             df_new['BMSCH'][counter_2] ='1000'
#                             df_new['MEINH'][counter_2] ='ST'
#                             df_new['VGW01'][counter_2] ='1'
#                             df_new['VGE01'][counter_2] ='S'
#                             df_new['ACTTYPE_01'][counter_2] ='200040'
#                             df_new['CKSELKZ'][counter_2] =''
#                             df_new['UMREZ'][counter_2] = '1000'
#                             df_new['UMREN'][counter_2] = '1000'
#                             df_new['USR00'][counter_2] = '1'
#                             df_new['USR01'][counter_2] ='3'
                            
#                         counter_2 +=1        
#                 TexcartaBase(material = row['МАТЕРИАЛ']).save()
    
#     for i in range(0,counter_2):
#         df_new['USR01'][i] = df_new['USR01'][i].replace('.',',')

#     df_new=df_new.replace('nan','')

    
#     del df_new["counter"]
        
#     from datetime import datetime
#     now = datetime.now()
    
#     s2 = now.strftime("%d.%m.%Y_%H.%M")

#     year =now.strftime("%Y")
#     month =now.strftime("%B")
#     day =now.strftime("%a%d")
#     hour =now.strftime("%H HOUR")
#     minut =now.strftime("%M-%S")     
            
#     create_folder(f'{MEDIA_ROOT}\\uploads','texcarta_benkam')
#     create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta_benkam',f'{year}')
#     create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta_benkam\\{year}',f'{month}')
#     create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta_benkam\\{year}\\{month}',day)
#     create_folder(f'{MEDIA_ROOT}\\uploads\\texcarta_benkam\\{year}\\{month}\\{day}',hour)
    
#     path7 =f'{MEDIA_ROOT}\\uploads\\texcarta_benkam\\{year}\\{month}\\{day}\\{hour}\\TK_PRISVOENIYE_{s2}.txt'
#     tk_prisvoeniye ={}
#     header ='WERKS\tPLNNR\tPLNAL_02\tMATNR_02'
#     tk_prisvoeniye['WERKS']=df_list_gp[0]
#     tk_prisvoeniye['PLNNR']=df_list_gp[1]
#     tk_prisvoeniye['PLNAL_02']=df_list_gp[2]
#     tk_prisvoeniye['MATNR_02']=df_list_gp[3]
  
    
#     df_tk_prisvoeniye= pd.DataFrame(tk_prisvoeniye)
    
#     np.savetxt(path7, df_tk_prisvoeniye.values,fmt='%s', delimiter="\t",header=header,comments='',encoding='ansi')


#     path2 =f'{MEDIA_ROOT}\\uploads\\texcarta_benkam\\{year}\\{month}\\{day}\\{hour}\\TK_{s2}.xlsx'
#     writer = pd.ExcelWriter(path2, engine='xlsxwriter')
#     df_new.to_excel(writer,index=False,sheet_name ='TEXCARTA')
#     writer.close()

#     # files =[File(file =path2,filetype='simple',id=1),File(file =path7,filetype='simple',id=2),]
#     context ={
#         'file1':path2,
#         'file2':path7,
#         'section':'Техкарта',

#     }

   
#     return render(request,'norma/benkam/generated_files_texcarta.html',context)





