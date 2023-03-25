from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import Product,ExcelFiles
from django.core.paginator import Paginator
from django.http import JsonResponse,HttpResponse,Http404
import re
from django.db.models import Count,Q
from .forms import FileForm
import os
from django.conf import settings  
from config.settings import MEDIA_ROOT
from datetime import datetime
from django.core.files import File
import string
import random
from .utils import counter_generated_data
now = datetime.now()


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

def file_list(request):
  files = ExcelFiles.objects.filter(generated =False)
  context ={'files':files}
  return render(request,'file_list.html',context)

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

group_one =['WDC47','SLT65','WDT78']
group_two =['FST','FSC','PVF','PDF']
group_three =['ALU']
group_four =['PVC']

def lenght_generate(request,id):
  s2 = now.strftime("%d-%m-%Y__%H-%M-%S")
  file = ExcelFiles.objects.get(id=id).file
  counter =0
  file_path =f'{MEDIA_ROOT}\\{file}'
  df_org = pd.read_excel(file_path)
  new_liss = []
  for key ,row in df_org.iterrows():
    new = row['Краткий текст материала'].split()
    # print(new)
    chast =1
    if row['SAP код'][:5] in group_one:
      chast =1
    elif (row['SAP код'][:2] =='FW') or (row['SAP код'][:3] in group_two):
      continue
    else:
      data_type = request.GET.get('type',None)
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
          print(lenn)
          length =int(int(nn)/500)
          for j in range(chast,length):
            new[i] =f'WL{j*500}'
            s=' '.join(new)
            new_generated_data.append({'sap_del_cod':s,'lenn':int(j*500)})
            counter+=1
    pr={'sena':row['Цена'],'length':lenn,'ves_gp':row['Вес за ШТ'],'kls_color':row['KLS_COLOR'],'kls_inner_color':row['KLS_INNER_COL'],'kls_inner_id':row['KLS_INNER_ID'],'ch_profile_type':row['Гр.мат'][len(row['Гр.мат'])-3:],'id_claes':row['KLAES ID'],'sap_code':row['SAP код'],'sap_code_krat':row['SAP код'].split('-')[0],'text':row['Краткий текст материала'],'data':new_generated_data}
    new_liss.append(pr)
  # print(new_liss)
  file_ids  =counter_generated_data(new_liss,s2)
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





@login_required(login_url='/accounts/login/')
def home(request):
  return render(request,'home.html')


