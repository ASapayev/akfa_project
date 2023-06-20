from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import Product,ExcelFiles,ExcelFilesOzmka
from django.core.paginator import Paginator
from django.http import JsonResponse,HttpResponse,Http404
import re
from django.db.models import Count,Q
from .forms import FileForm,FileFormOZMKA
from aluminiy.models import RazlovkaObichniy,RazlovkaTermo
from django.conf import settings  
from config.settings import MEDIA_ROOT
from datetime import datetime
from django.core.files import File
import string
import random
from django.contrib import messages
from .utils import counter_generated_data
import subprocess,sys,os
now = datetime.now()


def work_wast(request):
  return render(request,'delovoy_otxod/index.html')

def get_ozmka(ozmk,zavod1101,zavod1201):
  sap_code_yoqlari =[]
  # print(df)
  sap_exists =[]
  obichniy_razlovka =[]
  termo_razlovka =[]
  for ozm in ozmk:
    sap_code =ozm
    sap_code_exists =False
    if RazlovkaObichniy.objects.filter(
      Q(esap_code =ozm)
      |Q(zsap_code =ozm)
      |Q(psap_code =ozm)
      |Q(ssap_code =ozm)
      |Q(asap_code =ozm)
      |Q(lsap_code =ozm)
      |Q(nsap_code =ozm)
      |Q(sap_code7 =ozm)
      ).exists():
      razlovkaobichniy =RazlovkaObichniy.objects.filter(
        Q(esap_code =ozm)
      |Q(zsap_code =ozm)
      |Q(psap_code =ozm)
      |Q(ssap_code =ozm)
      |Q(asap_code =ozm)
      |Q(lsap_code =ozm)
      |Q(nsap_code =ozm)
      |Q(sap_code7 =ozm)
      )[:1].values_list()
      sap_code_exists=True
      if list(razlovkaobichniy)[0][0] not in sap_exists:
        obichniy_razlovka+=list(razlovkaobichniy)

    if RazlovkaTermo.objects.filter(
      Q(esap_code =ozm)
      |Q(zsap_code =ozm)
      |Q(psap_code =ozm)
      |Q(ssap_code =ozm)
      |Q(asap_code =ozm)
      |Q(lsap_code =ozm)
      |Q(nsap_code =ozm)
      |Q(ksap_code =ozm)
      |Q(sap_code7 =ozm)
      ).exists():
      razlovkatermo =RazlovkaTermo.objects.filter(
        Q(esap_code =ozm)
      |Q(zsap_code =ozm)
      |Q(psap_code =ozm)
      |Q(ssap_code =ozm)
      |Q(asap_code =ozm)
      |Q(ksap_code =ozm)
      |Q(nsap_code =ozm)
      |Q(lsap_code =ozm)
      |Q(sap_code7 =ozm)
      )[:1].get()
      id =razlovkatermo.parent_id
      if id == 0:
        if razlovkatermo.id not in sap_exists:
          termo_head =RazlovkaTermo.objects.filter(id=razlovkatermo.id)[:1].values_list()
          components =RazlovkaTermo.objects.filter(parent_id=razlovkatermo.id).values_list()
          print(list(termo_head))
          if list(termo_head)[0] not in termo_razlovka:
            termo_razlovka+=list(termo_head)
            termo_razlovka+=list(components)
      else:
        if id not in sap_exists:
          termo_head =RazlovkaTermo.objects.filter(id=id)[:1].values_list()
          components =RazlovkaTermo.objects.filter(parent_id=id).values_list()
          if list(termo_head)[0] not in termo_razlovka:
            termo_razlovka+=list(termo_head)
            termo_razlovka+=list(components)
      sap_code_exists=True
      
    
    if not sap_code_exists:
      sap_code_yoqlari.append(sap_code)


  if (zavod1101 and zavod1201):
    termo_razlovka =[ raz[:-2] for raz in termo_razlovka]
    obichniy_razlovka =[ raz[:-2] for raz in obichniy_razlovka]
    df_termo_1201 = pd.DataFrame(termo_razlovka,columns=['ID','PARENT ID','SAP код E','Экструзия холодная резка','SAP код Z','Печь старения','SAP код P','Покраска автомат','SAP код S','Сублимация','SAP код A','Анодировка','SAP код N','Наклейка','SAP код K','K-Комбинирования','SAP код L','Ламинация','SAP код 7','U-Упаковка + Готовая Продукция'])#,'CREATED DATE','UPDATED DATE'
    df_obichniy_1201 = pd.DataFrame(obichniy_razlovka,columns=['ID','SAP код E','Экструзия холодная резка','SAP код Z','Печь старения','SAP код P','Покраска автомат','SAP код S','Сублимация','SAP код A','Анодировка','SAP код L','Ламинация','SAP код N','Наклейка','SAP код 7','U-Упаковка + Готовая Продукция'])#,'CREATED DATE','UPDATED DATE'
    df_yoqlari_1201 = pd.DataFrame({'SAP CODE':sap_code_yoqlari})
    now =datetime.now()
    minut =now.strftime('%M-%S')
    path1201 =f'{MEDIA_ROOT}\\uploads\\ozmka\\ozmka1201-{minut}.xlsx'
    writer = pd.ExcelWriter(path1201, engine='xlsxwriter')
    df_termo_1201.to_excel(writer,index=False,sheet_name='TERMO')
    df_obichniy_1201.to_excel(writer,index=False,sheet_name='OBICHNIY')
    df_yoqlari_1201.to_excel(writer,index=False,sheet_name='NOT EXISTS')
    writer.close()

    termo_razlovka1101 =[ raz[4:10] + raz[12:16] + raz[18:20] for raz in termo_razlovka]
    obichniy_razlovka1101 =[ raz[1:9] + raz[15:17] for raz in obichniy_razlovka]
    counter = 0
    obichniy_razlovka1101org = []
    for obichniy in obichniy_razlovka1101:
      if obichniy[2] !='':
        ob =['','']+ list(obichniy[2:])
        obichniy_razlovka1101org.append(ob)
      else:
        obichniy_razlovka1101org.append(obichniy)
      counter += 1

    df_termo_1101 = pd.DataFrame(termo_razlovka1101,columns=['SAP код Z','Печь старения','SAP код P','Покраска автомат','SAP код S','Сублимация','SAP код N','Наклейка','SAP код K','K-Комбинирования','SAP код 7','U-Упаковка + Готовая Продукция'])#,'CREATED DATE','UPDATED DATE'
    df_obichniy_1101 = pd.DataFrame(obichniy_razlovka1101org,columns=['SAP код E','Экструзия холодная резка','SAP код Z','Печь старения','SAP код P','Покраска автомат','SAP код S','Сублимация','SAP код 7','U-Упаковка + Готовая Продукция'])#,'CREATED DATE','UPDATED DATE'
    df_yoqlari_1101 = pd.DataFrame({'SAP CODE':sap_code_yoqlari})
    now =datetime.now()
    minut =now.strftime('%M-%S')
    path1101 =f'{MEDIA_ROOT}\\uploads\\ozmka\\ozmka1101-{minut}.xlsx'
    writer = pd.ExcelWriter(path1101, engine='xlsxwriter')
    df_termo_1101.to_excel(writer,index=False,sheet_name='TERMO')
    df_obichniy_1101.to_excel(writer,index=False,sheet_name='OBICHNIY')
    df_yoqlari_1101.to_excel(writer,index=False,sheet_name='NOT EXISTS')
    writer.close()
    return path1201
  
  if ((zavod1201 and not zavod1201) or ((not zavod1101) and (not zavod1101))):
    termo_razlovka =[ raz[:-2] for raz in termo_razlovka]
    obichniy_razlovka =[ raz[:-2] for raz in obichniy_razlovka]
    df_termo_1201 = pd.DataFrame(termo_razlovka,columns=['ID','PARENT ID','SAP код E','Экструзия холодная резка','SAP код Z','Печь старения','SAP код P','Покраска автомат','SAP код S','Сублимация','SAP код A','Анодировка','SAP код N','Наклейка','SAP код K','K-Комбинирования','SAP код L','Ламинация','SAP код 7','U-Упаковка + Готовая Продукция'])#,'CREATED DATE','UPDATED DATE'
    df_obichniy_1201 = pd.DataFrame(obichniy_razlovka,columns=['ID','SAP код E','Экструзия холодная резка','SAP код Z','Печь старения','SAP код P','Покраска автомат','SAP код S','Сублимация','SAP код A','Анодировка','SAP код L','Ламинация','SAP код N','Наклейка','SAP код 7','U-Упаковка + Готовая Продукция'])#,'CREATED DATE','UPDATED DATE'
    df_yoqlari_1201 = pd.DataFrame({'SAP CODE':sap_code_yoqlari})
    now =datetime.now()
    minut =now.strftime('%M-%S')
    path1201 =f'{MEDIA_ROOT}\\uploads\\ozmka\\ozmka1201-{minut}.xlsx'
    writer = pd.ExcelWriter(path1201, engine='xlsxwriter')
    df_termo_1201.to_excel(writer,index=False,sheet_name='TERMO')
    df_obichniy_1201.to_excel(writer,index=False,sheet_name='OBICHNIY')
    df_yoqlari_1201.to_excel(writer,index=False,sheet_name='NOT EXISTS')
    writer.close()
    return path1201
  # print(obichniy_razlovka[0])
  # return 1
  if zavod1101:
    termo_razlovka1101 =[ raz[4:10] + raz[12:16] + raz[18:20] for raz in termo_razlovka]
    obichniy_razlovka1101 =[ raz[1:9] + raz[15:17] for raz in obichniy_razlovka]
    counter = 0
    obichniy_razlovka1101org = []
    for obichniy in obichniy_razlovka1101:
      if obichniy[2] !='':
        ob =['','']+ list(obichniy[2:])
        obichniy_razlovka1101org.append(ob)
      else:
        obichniy_razlovka1101org.append(obichniy)
      counter += 1

    df_termo_1101 = pd.DataFrame(termo_razlovka1101,columns=['SAP код Z','Печь старения','SAP код P','Покраска автомат','SAP код S','Сублимация','SAP код N','Наклейка','SAP код K','K-Комбинирования','SAP код 7','U-Упаковка + Готовая Продукция'])#,'CREATED DATE','UPDATED DATE'
    df_obichniy_1101 = pd.DataFrame(obichniy_razlovka1101org,columns=['SAP код E','Экструзия холодная резка','SAP код Z','Печь старения','SAP код P','Покраска автомат','SAP код S','Сублимация','SAP код 7','U-Упаковка + Готовая Продукция'])#,'CREATED DATE','UPDATED DATE'
    df_yoqlari_1101 = pd.DataFrame({'SAP CODE':sap_code_yoqlari})
    now =datetime.now()
    minut =now.strftime('%M-%S')
    path1101 =f'{MEDIA_ROOT}\\uploads\\ozmka\\ozmka1101-{minut}.xlsx'
    writer = pd.ExcelWriter(path1101, engine='xlsxwriter')
    df_termo_1101.to_excel(writer,index=False,sheet_name='TERMO')
    df_obichniy_1101.to_excel(writer,index=False,sheet_name='OBICHNIY')
    df_yoqlari_1101.to_excel(writer,index=False,sheet_name='NOT EXISTS')
    writer.close()
    return path1101



def get_ready_ozmka(request,id):
  file = ExcelFilesOzmka.objects.get(id=id).file
  file_path =f'{MEDIA_ROOT}\\{file}'
  df = pd.read_excel(file_path)
  sap_code_yoqlari =[]
  # print(df)
  sap_exists =[]
  obichniy_razlovka =[]
  termo_razlovka =[]
  for key,row in df.iterrows():
    sap_code =row['SAP CODE']
    sap_code_exists =False
    if RazlovkaObichniy.objects.filter(
      Q(esap_code =row['SAP CODE'])
      |Q(zsap_code =row['SAP CODE'])
      |Q(psap_code =row['SAP CODE'])
      |Q(ssap_code =row['SAP CODE'])
      |Q(asap_code =row['SAP CODE'])
      |Q(lsap_code =row['SAP CODE'])
      |Q(nsap_code =row['SAP CODE'])
      |Q(sap_code7 =row['SAP CODE'])
      ).exists():
      razlovkaobichniy =RazlovkaObichniy.objects.filter(
        Q(esap_code =row['SAP CODE'])
      |Q(zsap_code =row['SAP CODE'])
      |Q(psap_code =row['SAP CODE'])
      |Q(ssap_code =row['SAP CODE'])
      |Q(asap_code =row['SAP CODE'])
      |Q(lsap_code =row['SAP CODE'])
      |Q(nsap_code =row['SAP CODE'])
      |Q(sap_code7 =row['SAP CODE'])
      )[:1].values_list()
      sap_code_exists=True
      if list(razlovkaobichniy)[0][0] not in sap_exists:
        obichniy_razlovka+=list(razlovkaobichniy)

    if RazlovkaTermo.objects.filter(
      Q(esap_code =row['SAP CODE'])
      |Q(zsap_code =row['SAP CODE'])
      |Q(psap_code =row['SAP CODE'])
      |Q(ssap_code =row['SAP CODE'])
      |Q(asap_code =row['SAP CODE'])
      |Q(lsap_code =row['SAP CODE'])
      |Q(nsap_code =row['SAP CODE'])
      |Q(ksap_code =row['SAP CODE'])
      |Q(sap_code7 =row['SAP CODE'])
      ).exists():
      razlovkatermo =RazlovkaTermo.objects.filter(
        Q(esap_code =row['SAP CODE'])
      |Q(zsap_code =row['SAP CODE'])
      |Q(psap_code =row['SAP CODE'])
      |Q(ssap_code =row['SAP CODE'])
      |Q(asap_code =row['SAP CODE'])
      |Q(ksap_code =row['SAP CODE'])
      |Q(nsap_code =row['SAP CODE'])
      |Q(lsap_code =row['SAP CODE'])
      |Q(sap_code7 =row['SAP CODE'])
      )[:1].get()
      id =razlovkatermo.parent_id
      if id == 0:
        if razlovkatermo.id not in sap_exists:
          termo_head =RazlovkaTermo.objects.filter(id=razlovkatermo.id)[:1].values_list()
          components =RazlovkaTermo.objects.filter(parent_id=razlovkatermo.id).values_list()
          termo_razlovka+=list(termo_head)
          termo_razlovka+=list(components)
      else:
        if id not in sap_exists:
          termo_head =RazlovkaTermo.objects.filter(id=id)[:1].values_list()
          components =RazlovkaTermo.objects.filter(parent_id=id).values_list()
          termo_razlovka+=list(termo_head)
          termo_razlovka+=list(components)
      sap_code_exists=True
      
    
    if not sap_code_exists:
      sap_code_yoqlari.append(sap_code)
  termo_razlovka =[ raz[:-2] for raz in termo_razlovka]
  obichniy_razlovka =[ raz[:-2] for raz in obichniy_razlovka]
  df_termo = pd.DataFrame(termo_razlovka,columns=['ID','PARENT ID','SAP код E','Экструзия холодная резка','SAP код Z','Печь старения','SAP код P','Покраска автомат','SAP код S','Сублимация','SAP код A','Анодировка','SAP код N','Наклейка','SAP код K','K-Комбинирования','SAP код L','Ламинация','SAP код 7','U-Упаковка + Готовая Продукция'])#,'CREATED DATE','UPDATED DATE'
  df_obichniy = pd.DataFrame(obichniy_razlovka,columns=['ID','SAP код E','Экструзия холодная резка','SAP код Z','Печь старения','SAP код P','Покраска автомат','SAP код S','Сублимация','SAP код A','Анодировка','SAP код L','Ламинация','SAP код N','Наклейка','SAP код 7','U-Упаковка + Готовая Продукция'])#,'CREATED DATE','UPDATED DATE'
  df_yoqlari = pd.DataFrame({'SAP CODE':sap_code_yoqlari})
  now =datetime.now()
  minut =now.strftime('%M-%S')
  path =f'{MEDIA_ROOT}\\uploads\\ozmka\\ozmka-{minut}.xlsx'
  writer = pd.ExcelWriter(path, engine='xlsxwriter')
  df_termo.to_excel(writer,index=False,sheet_name='TERMO')
  df_obichniy.to_excel(writer,index=False,sheet_name='OBICHNIY')
  df_yoqlari.to_excel(writer,index=False,sheet_name='NOT EXISTS')
  writer.close()
  return JsonResponse({'a':'b'})

# Create your views here.
def excel(request):
  df = pd.read_excel('C:\\OpenServer\\domains\\new_base2.xlsx','sheet')
  print(df.shape)
  # print(df['SAP код материала'][0],df['Краткий текст материала'][0],df['SAP код ДЕЛ.Отход'][0])
  # print(df['SAP код материала'][19516],df['Краткий текст материала'][19516],df['SAP код ДЕЛ.Отход'][19516])
  for i in range(0,19526):
    sap_code_materials =df['SAP код материала'][i] 
    ktartkiy_tekst_materiala =df['Краткий текст материала'][i]
    sap_kod_del_otxod =df['SAP код ДЕЛ.Отход'][i]
    kratkiy_tekst_del_otxod =df['Краткий текст ДЕЛ.Отход'][i]
    new_sap_kod_del_otxod =df['SAP код ДЕЛ.Отход'][i].split('-')[0]
    id_klaes =df['KLAES'][i]
    ch_profile_type = df['CH_PROFILE_TYPE'][i]
    kls_wast = df['KLS_WAST'][i]
    kls_wast_length = df['KLS_WAST_LENGTH'][i]
    ch_kls_optom =df['CH_KLAES_OPTM'][i]
    kls_inner_id =df['KLS_INNER_ID'][i]
    kls_inner_color =df['KLS_INNER_COL'][i]
    kls_color =df['KLS_COLOR'][i]
    ves_gp =df['Вес ГП'][i]
    ves_del_odxod=df['Вес дел.отход'][i]
    sena_za_shtuk =df['Цена за ШТ'][i]
    sena_za_metr =df['Цена дел.отход'][i]
    
    product =Product(
      sap_code_materials =sap_code_materials ,
      ktartkiy_tekst_materiala =ktartkiy_tekst_materiala,
      sap_kod_del_otxod = sap_kod_del_otxod,
      new_sap_kod_del_otxod = new_sap_kod_del_otxod,
      kratkiy_tekst_del_otxod =kratkiy_tekst_del_otxod,
      id_klaes =id_klaes,
      ch_profile_type =ch_profile_type,
      kls_wast =kls_wast,
      kls_wast_length =kls_wast_length,
      ch_kls_optom = ch_kls_optom,
      kls_inner_id =kls_inner_id,
      kls_inner_color =kls_inner_color,
      kls_color =kls_color,
      ves_gp =ves_gp,
      ves_del_odxod=ves_del_odxod,
      sena_za_shtuk =sena_za_shtuk,
      sena_za_metr =sena_za_metr
      )
    product.save()
  return redirect('index')

def index(request):
  print(MEDIA_ROOT)
  return render(request,'index.html')

def show_list(request):
  search =request.GET.get('search',None)
  if search:
    products =Product.objects.filter(
      Q(sap_code_materials__icontains=search)|Q(ktartkiy_tekst_materiala__icontains=search)
      |Q(kratkiy_tekst_del_otxod__icontains=search)
      |Q(sap_kod_del_otxod__icontains=search)
      |Q(id_klaes__icontains=search)
      |Q(ch_profile_type__icontains=search)
      |Q(kls_wast__icontains=search)
      |Q(kls_wast_length__icontains=search)
      |Q(ch_kls_optom__icontains=search)
      |Q(kls_inner_id__icontains=search)
      |Q(kls_inner_color__icontains=search)
      |Q(kls_color__icontains=search)
      |Q(ves_gp__icontains=search)
      )
  else:
    products =Product.objects.all()
      
  paginator = Paginator(products, 25)

  if request.GET.get('page') != None:
    page_number = request.GET.get('page')
  else:
    page_number=1
  page_obj = paginator.get_page(page_number)
  context ={
    'products':page_obj
  }
  return render(request,'show_list.html',context)

def experiment_json(request):
  start=None
  end  =None
  if request.GET.get('start'):
    start =request.GET.get('start')
  if request.GET.get('end'):
    end =request.GET.get('end')
  
  if start and end:
    products = Product.objects.filter(id__gte=int(start),id__lte=int(end))
  else:
    products = Product.objects.filter(id__lte=100)
  pr ={}
  for p in products:
    sp =p.ktartkiy_tekst_materiala.split()
    if (('/' in p.ktartkiy_tekst_materiala) and ('_' in p.ktartkiy_tekst_materiala)):
      count = len(re.findall("/", p.ktartkiy_tekst_materiala)) 
      if count == 1:
        for i in range(0,len(sp)):
          if ('/' in sp[i]):
            splited_text =sp[i].split('_')
            section_one =splited_text[0]
            section_two =splited_text[1]
            sp[i]={'section_1':section_one,'section2':section_two}
        print('section_1.1',count)  
      elif count == 2:
        for i in range(0,len(sp)):
          if ('/' in sp[i]):
            splited_text =sp[i].split('_')
            section_one =splited_text[0]
            section_two =splited_text[1]
            sp[i]={'section_1':section_one,'section2':section_two}
        print('section_1.2',count)
      # section_one =
      pass
    elif (('/' in p.ktartkiy_tekst_materiala) and (not '_' in p.ktartkiy_tekst_materiala)):
      for i in range(0,len(sp)):
          if ('/' in sp[i]):
            splited_text =sp[i].split('/')
            section_one =splited_text[0]
            section_two =splited_text[1]
            sp[i]={'section_1':section_one,'section2':section_two}
      print('section_1.2',count)
      print('section_2',count)  
      # section_one =
      pass
    elif (('_' in p.ktartkiy_tekst_materiala) and (not '/' in p.ktartkiy_tekst_materiala)):
      count = len(re.findall("_", p.ktartkiy_tekst_materiala)) 
      for i in range(0,len(sp)):
          if ('_' in sp[i]):
            splited_text =sp[i].split('_')
            section_one =splited_text[0]
            section_two =splited_text[1]
            sp[i]={'section_1':section_one,'section2':section_two}
      print('section_3',count)  
      # section_one =
      pass
    # print(p.ktartkiy_tekst_materiala)
    pr[p.id]={'real':p.ktartkiy_tekst_materiala,'splited':sp}

  
  return JsonResponse(pr)

def counter_set(request):
  products =Product.objects.all()
  for pr in products:
    mix_text =pr.mix_sap_kod_del_otxod
    count =Product.objects.filter(mix_sap_kod_del_otxod=mix_text).count()
    if count>1:
      print(pr.id)
  return redirect('index')
  # products =products

def group(request):
  pr=Product.objects.all().values('new_sap_kod_del_otxod').annotate(dcount=Count('new_sap_kod_del_otxod')).order_by('dcount')
  
  products =Product.objects.filter(id__lte=1000).order_by('id')
  s={}
  dtt ={}
  # i=1
  new_list=[]
  for p in pr:
    if not p['new_sap_kod_del_otxod'] in new_list:
      new_list.append(p['new_sap_kod_del_otxod'])
      dtt[p['new_sap_kod_del_otxod']]=1
  
  i=1
  for pp in products:
    text =pp.mix_sap_kod_del_otxod
    if not Product.objects.filter(id__lt=pp.id).filter(mix_sap_kod_del_otxod=text).exists():
      s[i]={'old':pp.sap_kod_del_otxod,'new':pp.new_sap_kod_del_otxod+"-W{:04d}".format(dtt[pp.new_sap_kod_del_otxod]),'kratkiy_tekst_del_otxod':pp.kratkiy_tekst_del_otxod,'counter':dtt[pp.new_sap_kod_del_otxod]}
      dtt[pp.new_sap_kod_del_otxod]+=1
    i+=1
  return JsonResponse({'ss':new_list,'s':s})

def size_product(request):
  products =Product.objects.all()
  return JsonResponse({'a':2})

def file_upload(request):
  
  if request.method == 'POST':
    form = FileForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('file_list')
  else:
      form =FileForm()
      context ={
        'form':form
      }
  return render(request,'excel_form.html',context)

def file_upload_for_get_ozmka(request):
  if request.method =='POST':
    ozmk = request.POST.get('ozmk',None)
    zavod1101 =request.POST.get('for1101',None)  
    zavod1201 =request.POST.get('for1201',None)

    if zavod1101 =='on':
      z1101 =True
    else:
      z1101 =False

    if zavod1201 =='on':
      z1201 =True
    else:
      z1201 =False  
    if ozmk:
      ozmks =ozmk.split()
      get_ozmka(ozmks,z1101,z1201)
      messages.add_message(request, messages.INFO, "Razlovka tayyor!!!")
      return render(request,'norma/razlovka_find.html')
    else:
        return render(request,'norma/razlovka_find.html')
  return render(request,'norma/razlovka_find.html')

def file_upload_for_get_ozmka_org(request):
  if request.method =='POST':
    ozmk = request.POST.get('ozmk',None)  
    if ozmk:
      ozmks =ozmk.split()
      path = get_ozmka(ozmks)
      return render(request,'norma/razlovka_find_org.html',{'path':path})
    else:
        return render(request,'norma/razlovka_find_org.html')
  else:
    path = request.GET.get('path',None)

    if path:
      if sys.platform == "win32":
        os.startfile(path)
      else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])
    return render(request,'norma/razlovka_find_org.html')


    

def file_list(request):
  files = ExcelFiles.objects.filter(generated =False).order_by('-created_at')
  context ={'files':files}
  return render(request,'file_list.html',context)

def file_list_ozmka(request):
  files = ExcelFilesOzmka.objects.filter(generated =False).order_by('-created_at')
  context ={'files':files}
  return render(request,'file_list_ozmka.html',context)

def import_file(request,id):
  file = ExcelFiles.objects.get(id=id).file
  file_path =f'{MEDIA_ROOT}\\{file}'
  df = pd.read_excel(file_path)
  items =[]
  columns =df.columns
  cls =[x for x in columns]
  i=1
  for index, row in df.iterrows():
    item={}
    for col in columns:
      item[col]=row[col]
    items.append(item)
    i+=1
    if i>100:
      break
  
  context ={
    'df':items,
    'columns':cls
  }
  
  return render(request,'result.html',context)
  

def counter_exist_data(request):
  pr = [x['new_sap_kod_del_otxod'] for x in Product.objects.all().values('new_sap_kod_del_otxod').annotate(dcount=Count('new_sap_kod_del_otxod')).order_by('dcount')]
  products = Product.objects.all().values('id','sap_kod_del_otxod','kratkiy_tekst_del_otxod')

  counter = {}
  for p in pr:
    counter[p]=[]

  
  
  for product in products:
    sap_code = product['sap_kod_del_otxod'].split('-W')
    counter_exist = int(sap_code[1])
   
    new_counter_list = counter[sap_code[0]]
    new_counter_list.append(counter_exist)
    new_counter_list.sort()
    counter[sap_code[0]] = new_counter_list


  
  return JsonResponse({'new':pr,'s':counter})

#### function one

def read_and_write(request,id):
  file = ExcelFiles.objects.get(id=id).file
  file_path =f'{MEDIA_ROOT}\\{file}'
  df = pd.read_excel(file_path)
  df['duplicated']=False
  #######################################
  pr = [x['new_sap_kod_del_otxod'] for x in Product.objects.all().values('new_sap_kod_del_otxod').annotate(dcount=Count('new_sap_kod_del_otxod')).order_by('dcount')]
  products = Product.objects.all().values('id','sap_kod_del_otxod','kratkiy_tekst_del_otxod')

  counter = {}
  for p in pr:
    counter[p]=[]

  for product in products:
    sap_code = product['sap_kod_del_otxod'].split('-W')
    counter_exist = int(sap_code[1])
    new_counter_list = counter[sap_code[0]]
    new_counter_list.append(counter_exist)
    new_counter_list.sort()
    counter[sap_code[0]] = new_counter_list

  new_data = []
  for key,row in df.iterrows():
    sap_code_materials =row['SAP код материала']
    ktartkiy_tekst_materiala =row['Краткий текст материала']
    ktartkiy_tekst_materiala_split =None
    
    if (isinstance(row['Длина'],int) or isinstance(row['Длина'],float)):
      dlina = row['Длина']
    else:
      dlinaw =row['Краткий текст материала'].split()
      for d in dlinaw:
        if d.startswith('L'):
          dlina1 =d.replace('L','')
          dlina =int(dlina1)
          break
    nazvaniye_sistemi = row['Название системы']
    naimenovaniye_materiala_sap_imzo =row['Наименование материала SAP IMZO']
    sap_kod_del_otxod =row['SAP код ДЕЛ.Отход']
    new_sap_kod_del_otxod =row['new']
    kratkiy_tekst_del_otxod =row['Краткий текст ДЕЛ.Отход']
    proverka_duplicat =row['Проверка Дубликат']
    dlina2 =row['Длина2']
    id_klaes =row['ID KLAES']
    vid_materiala =row['Вид материала']
    gruppa_materiala =row['Группа материалов']
    bazavoye_ei =row['Базовая ЕИ']
    sector =row['Сектор']
    sena_za_shtuk =row['Цена за шт']
    sena_za_metr =row['Цена за метр']
    kls_inner_id =row['KLS_INNER ID']
    kls_inner_color =row['KLS_INNER COLOR']
    klaes_description =row['KLAES Description']

    ###################################
    # if row['new'] in counter:
    if row['new'] in counter:
      number_list = counter[row['new']]
      product_exists = Product.objects.filter(new_sap_kod_del_otxod=row['new'],kratkiy_tekst_del_otxod=row['Краткий текст ДЕЛ.Отход']).exists()
      if product_exists:
        df['SAP код ДЕЛ.Отход'][key]=Product.objects.filter(new_sap_kod_del_otxod=row['new'],kratkiy_tekst_del_otxod=row['Краткий текст ДЕЛ.Отход'])[:1].get().sap_kod_del_otxod
        df['duplicated'][key]=True
        msg = 'Data already exist!'
      else:
        for i in range(1,10000):
          if not i in number_list:
            # product save..
            product =Product(
              sap_code_materials = sap_code_materials,
              ktartkiy_tekst_materiala =ktartkiy_tekst_materiala,
              ktartkiy_tekst_materiala_split =ktartkiy_tekst_materiala_split,
              dlina = dlina,
              nazvaniye_sistemi = nazvaniye_sistemi,
              naimenovaniye_materiala_sap_imzo =naimenovaniye_materiala_sap_imzo,
              sap_kod_del_otxod =sap_kod_del_otxod+"-W{:04d}".format(i),
              new_sap_kod_del_otxod =new_sap_kod_del_otxod,
              kratkiy_tekst_del_otxod =kratkiy_tekst_del_otxod,
              proverka_duplicat =proverka_duplicat,
              dlina2 =dlina2,
              id_klaes =id_klaes,
              vid_materiala =vid_materiala,
              gruppa_materiala =gruppa_materiala,
              bazavoye_ei =bazavoye_ei,
              sector =sector,
              sena_za_shtuk =sena_za_shtuk,
              sena_za_metr =sena_za_metr,
              kls_inner_id =kls_inner_id,
              kls_inner_color =kls_inner_color,
              klaes_description =klaes_description
              )
            # product =Product(
            #   sap_code_materials =sap_code_materials ,
            #   ktartkiy_tekst_materiala =ktartkiy_tekst_materiala,
            #   sap_kod_del_otxod = sap_kod_del_otxod,
            #   new_sap_kod_del_otxod = new_sap_kod_del_otxod,
            #   kratkiy_tekst_del_otxod =kratkiy_tekst_del_otxod,
            #   id_klaes =id_klaes,
            #   ch_profile_type =ch_profile_type,
            #   kls_wast =kls_wast,
            #   kls_wast_length =kls_wast_length,
            #   ch_kls_optom = ch_kls_optom,
            #   kls_inner_id =kls_inner_id,
            #   kls_inner_color =kls_inner_color,
            #   kls_color =kls_color,
            #   ves_gp =ves_gp,
            #   ves_del_odxod=ves_del_odxod,
            #   sena_za_shtuk =sena_za_shtuk,
            #   sena_za_metr =sena_za_metr
            # )
            # product.save()
            df['SAP код ДЕЛ.Отход'][key]=sap_kod_del_otxod+"-W{:04d}".format(i)
            n_list = counter[row['new']]
            n_list.append(i)
            counter[row['new']]=n_list
            break
    else:
      product =Product(
              sap_code_materials = sap_code_materials,
              ktartkiy_tekst_materiala =ktartkiy_tekst_materiala,
              ktartkiy_tekst_materiala_split =ktartkiy_tekst_materiala_split,
              dlina = dlina,
              nazvaniye_sistemi = nazvaniye_sistemi,
              naimenovaniye_materiala_sap_imzo =naimenovaniye_materiala_sap_imzo,
              sap_kod_del_otxod =sap_kod_del_otxod+"-W{:04d}".format(1),
              new_sap_kod_del_otxod =new_sap_kod_del_otxod,
              kratkiy_tekst_del_otxod =kratkiy_tekst_del_otxod,
              proverka_duplicat =proverka_duplicat,
              dlina2 =dlina2,
              id_klaes =id_klaes,
              vid_materiala =vid_materiala,
              gruppa_materiala =gruppa_materiala,
              bazavoye_ei =bazavoye_ei,
              sector =sector,
              sena_za_shtuk =sena_za_shtuk,
              sena_za_metr =sena_za_metr,
              kls_inner_id =kls_inner_id,
              kls_inner_color =kls_inner_color,
              klaes_description =klaes_description
              )
      product.save()
      df['SAP код ДЕЛ.Отход'][key]=sap_kod_del_otxod+"-W{:04d}".format(1)
      counter[row['new']]=[1,]
      


  s2 = now.strftime("%d-%m-%Y__%H-%M-%S")
  path =f'{MEDIA_ROOT}\\uploads\\{s2}.xlsx'
  df.to_excel(path)
  file_exist =ExcelFiles(file =f'uploads/{s2}.xlsx',generated=True)
  file_exist.save()
  
  files =ExcelFiles.objects.filter(generated=True)
  context ={
    'files':files
  }
  return render(request,'result_excel.html',context)



def download(request, id):
  path =str(ExcelFiles.objects.get(id=id).file)
  file_path = os.path.join(settings.MEDIA_ROOT, path)
  if os.path.exists(file_path):
      with open(file_path, 'rb') as fh:
          response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
          response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
          return response
  raise Http404

group_one =['WDC47','WDT65','WDT78']
group_two =['FST','FSC','PVF','PDF']
group_three =['ALU']
group_four =['PVC']

def lenght_generate(request,id):
  file = ExcelFiles.objects.get(id=id).file
  counter =0
  file_path =f'{MEDIA_ROOT}\\{file}'
  df_org = pd.read_excel(file_path)
  new_liss = []
  data_type = request.GET.get('type',None)
  for key ,row in df_org.iterrows():
    new = row['Краткий текст материала'].split()
    # print(new)
    chast =1
    if row['SAP код'][:5] in group_one:
      chast =1
    elif (row['SAP код'][:2] =='FW') or (row['SAP код'][:3] in group_two):
      continue
    else:
      
      if data_type and (data_type =='alu'):
        chast = 4
      elif data_type and (data_type =='pvc'):
        chast =3
    new_generated_data =[]
    for i in range(0,len(new)):
      if new[i].startswith('L'):
        nn=new[i].replace('L','')
        if nn.isdigit():
          lenn=int(nn)
          length =int(int(nn)/500)
          for j in range(chast,length):
            new[i] =f'WL{j*500}'
            s=' '.join(new)
            new_generated_data.append({'sap_del_cod':s,'lenn':int(j*500)})
            counter+=1
    pr={'sena':row['Цена'],'length':lenn,'ves_gp':row['Вес за ШТ'],'kls_color':row['KLS_COLOR'],'kls_inner_color':row['KLS_INNER_COL'],'kls_inner_id':row['KLS_INNER_ID'],'ch_profile_type':row['Гр.мат'][len(row['Гр.мат'])-3:],'id_claes':row['KLAES ID'],'sap_code':row['SAP код'],'sap_code_krat':row['SAP код'].split('-')[0],'text':row['Краткий текст материала'],'data':new_generated_data}
    new_liss.append(pr)
  # print(new_liss)
  file_ids  =counter_generated_data(new_liss,data_type)
  files =ExcelFiles.objects.filter(id__in=file_ids)
  context={
    'files':files
  }
  # counter+=5
  # s2 = res = ''.join(random.choices(string.ascii_letters, k=7))
  # path =f'{MEDIA_ROOT}\\uploads\\fake_data-{s2}.xlsx'
  # df =pd.DataFrame()
  # df['sap']=['' for x in range(0,counter)]
  # df['krat']=['' for x in range(0,counter)]
  # t=0
  # for i in range(0,len(new_liss)):
  #   for key,values in new_liss[i].items():
  #     for val in values:
  #       df.loc[t]=[key,val]
  #       t+=1
  # df.to_excel(path)
  # return JsonResponse({'a':'b'})
  return render(request,'generated_file.html',context)


def delete_file(request,id):
  file =get_object_or_404(ExcelFiles,id=id)
  a=request.GET.get('generated',None)
  if a:
    return redirect('index')
  # print(file.file)
  path =f'{MEDIA_ROOT}\\{file.file}'
  if os.path.isfile(path):
        os.remove(path)
  file.delete()
  return redirect('file_list')





# @login_required(login_url='/accounts/login/')
def home(request):
  return render(request,'home.html')


