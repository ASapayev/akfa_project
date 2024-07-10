from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from .forms import NormaFileForm,NormaExcelFiles
from .models import Norma,Siryo
from config.settings import MEDIA_ROOT
import pandas as pd
import os 
from datetime import datetime



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
            row['SAP код P'],row['PR - Press'],
            row['SAP код M'],row['MO - Mex obrabotka'],
            row['SAP код PM'],row['PM - Puma'],
            row['SAP код PK'],row['PK - Pokraska'],
            row['SAP код 7'],row['7 - Upakovka ']
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
        # older_process ={'sapcode':'','kratkiy':''}
        
        artikul = df[i][8].split('-')[0]
        # print(artikul,'sssss')
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
                    seksiya_list =df[i][9].split(' ')
                    text =''
                    for sek in seksiya_list:
                        if '-' in sek:
                            text = sek
                            break
                    seksiya = text.split('-')[1]
                    # df_new['MEINS'].append(("%.3f" % (float(alum_teks.data['расход сплава на 1000 шт профиля/кг'])*mein_percent)).replace('.',',')) 
                    df_new['MEINS'].append(int(seksiya)*1000) 
                    df_new['MENGE'].append('скц')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                    
                df_new['LGORT'].append('')

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
                    df_new['LGORT'].append('')
           
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
            df_new['STKTX'].append('')
            df_new['BMENG'].append( '1000')
            df_new['BMEIN'].append('скц')
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
            for k in range(1,4):
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
                    df_new['MENGE'].append('скц')
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
                    
                df_new['LGORT'].append('')
        
       
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
            df_new['STKTX'].append('')
            df_new['BMENG'].append( '1000')
            df_new['BMEIN'].append('скц')
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
                    df_new['MENGE'].append('скц')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                    
                df_new['LGORT'].append('')
        
        
                    
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
            df_new['BMEIN'].append('скц')
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
            df_new['MENGE'].append('скц')
            df_new['DATUV'].append('')
            df_new['PUSTOY'].append('')
            df_new['LGORT'].append('')

            siryo_names =[
                {'kratkiy':'Лента абразивная 60 (140х2000) Барабан','sapcode':'1000004458'},
                {'kratkiy':'Лента абразивная 120(140х2000) Барабан','sapcode':'1000004459'},
                {'kratkiy':'Лента абразивная  80 (350х1900) Мех.обр','sapcode':'1000004455'},
                {'kratkiy':'Лента абразивная 120 (350х1900) Мех.обр','sapcode':'1000004456'},
                {'kratkiy':'Лента абразивная 240 (350х1900) Мех.обр','sapcode':'1000004457'},
                {'kratkiy':'Тех. отход ал стружка','sapcode':'1900007454'},
                {'kratkiy':'Крышка радиатора','sapcode':'1000004484'},
                {'kratkiy':'Паронит межсекционная (Китай) Gizetta','sapcode':'1000004374'},
                {'kratkiy':'Соеденительная муфта (Местный)','sapcode':'1000004372'},
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
                    df_new['MENGE'].append('КГ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                    df_new['LGORT'].append('')
                
               
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
            df_new['STKTX'].append('')
            df_new['BMENG'].append( '1000')
            df_new['BMEIN'].append('скц')
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
                    df_new['MENGE'].append('КГ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                if k == 6 :
                    df_new['MATNR1'].append('1000004353')
                    df_new['TEXT2'].append('Огнеупорная смазка Pyro-Mastic')
                    df_new['MEINS'].append('-'+norma.data['Огнеупорная смазка Pyro-Mastic'].replace('.0','') if norma.data['Огнеупорная смазка Pyro-Mastic'][-2:]=='.0' else '-' + ("%.3f" % float(norma.data['Огнеупорная смазка Pyro-Mastic'])).replace('.',','))
                    df_new['MENGE'].append('КГ')
                    df_new['DATUV'].append('')
                    df_new['PUSTOY'].append('')
                df_new['LGORT'].append('')
            
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
                    df_new['LGORT'].append('')
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
                    df_new['LGORT'].append('')

                 
        
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
    

    # meins7 = []
    
    # for mein in df_new['MEINS']:
    #     mein_txt = str(mein)
    #     if mein_txt[-4:] ==',000':
    #         meins7.append(mein_txt.replace(',000',''))
    #     else:
    #         meins7.append(mein_txt)
    # df_new['MEINS'] =meins7
    
    # meins7d = []
    
    # for mein in df_new_duplicate['MEINS']:
    #     mein_txt = str(mein)
    #     if mein_txt[-4:] ==',000':
    #         meins7d.append(mein_txt.replace(',000',''))
    #     else:
    #         meins7d.append(mein_txt)
    # df_new_duplicate['MEINS'] =meins7d

    for key,row in df_new.items():
        print(key,len(row))
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

def create_folder(parent_dir,directory):
    path =os.path.join(parent_dir,directory)
    if not os.path.isdir(path):
        os.mkdir(path)

class File:
    def __init__(self,file,filetype,id):
        self.file =file
        self.filetype =filetype
        self.id = id