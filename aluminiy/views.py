from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import pandas as pd
from django.core.paginator import Paginator
from .models import AluminiyProduct,AluFile,RazlovkaObichniy,RazlovkaTermo,Price,LengthOfProfile,ExchangeValues,AluProfilesData
from aluminiytermo.models import AluminiyProductTermo,CharacteristikaFile
from aluminiytermo.views import *
from .forms import FileForm,LengthOfProfilwForm,ExchangeValueForm,FileFormBazaprofiley
from django.db.models import Max
import zipfile
from config.settings import MEDIA_ROOT
import numpy as np
from .utils import fabrikatsiya_sap_kod,create_folder,CharacteristicTitle,save_razlovka,download_bs64,characteristika_created_txt_create_1301_v2
import os
from order.models import Order
import random
from aluminiytermo.utils import create_characteristika,create_characteristika_utils,characteristika_created_txt_create,check_for_correct,anodirovaka_check
from aluminiytermo.models import CharUtilsThree,Characteristika
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import ast
from django.http import JsonResponse,HttpResponse,FileResponse
from datetime import datetime
from aluminiytermo.BAZA import ANODIROVKA_CODE
from io import BytesIO as IO
from accounts.models import User
from django.urls import reverse
from norma.models import NormaExcelFiles
from accounts.decorators import allowed_users


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator',])
def upload_for_1301_v22(request):
      if request.method == 'POST':
            form = FileFormTermo(request.POST, request.FILES)
            if form.is_valid():
                  file_path =form.cleaned_data["file"]
                  df = pd.read_excel(file_path)
                  file_destination = characteristika_created_txt_create_1301_v2(df)
                  files = [File(file=f,filetype='Obichniy') for f in file_destination]
                  context = {
                        'files':files,
                  }
                  return render(request,'universal/generated_file_1301.html',context)
      return render(request,'universal/main.html')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator',])
def add_length_profile(request):

      if request.method == 'POST':
            form = LengthOfProfilwForm(data=request.POST)
            if form.is_valid():
                  form.save()
                  return redirect('show_profile')
      else:
            form = LengthOfProfilwForm()

      context ={
            'form':form
      }
      return render(request,'price/add.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator',])
def edit_currency(request):

      length_of_profile = ExchangeValues.objects.get(id =1)

      if request.method == 'POST':
            form = ExchangeValueForm(data=request.POST,instance=length_of_profile)
            if form.is_valid():
                  form.save()
                  return redirect('home')
      else:
            form = ExchangeValueForm(instance=length_of_profile)

      context ={
            'form':form
      }
      return render(request,'price/currency_update.html',context)

@csrf_exempt
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def edit_sapcodes_simple(request,id):
      sapcode_org = AluminiyProduct.objects.get(id=id)
      if request.method =='POST':
            kratkiy = request.POST.get('kratkiy')
            if RazlovkaObichniy.objects.filter(
                  (Q(esap_code =sapcode_org.material)&Q(ekratkiy = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(zsap_code =sapcode_org.material)&Q(zkratkiy = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(psap_code =sapcode_org.material)&Q(pkratkiy = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(ssap_code =sapcode_org.material)&Q(skratkiy = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(asap_code =sapcode_org.material)&Q(akratkiy = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(lsap_code =sapcode_org.material)&Q(lkratkiy = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(nsap_code =sapcode_org.material)&Q(nkratkiy = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(sap_code7 = sapcode_org.material)&Q(kratkiy7 = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(fsap_code = sapcode_org.material)&Q(fkratkiy = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(sap_code75 = sapcode_org.material)&Q(kratkiy75 = sapcode_org.kratkiy_tekst_materiala))
                  ).exists:
                 
                  razlovka = RazlovkaObichniy.objects.filter(
                  (Q(esap_code =sapcode_org.material)&Q(ekratkiy = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(zsap_code =sapcode_org.material)&Q(zkratkiy = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(psap_code =sapcode_org.material)&Q(pkratkiy = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(ssap_code =sapcode_org.material)&Q(skratkiy = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(asap_code =sapcode_org.material)&Q(akratkiy = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(lsap_code =sapcode_org.material)&Q(lkratkiy = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(nsap_code =sapcode_org.material)&Q(nkratkiy = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(sap_code7 = sapcode_org.material)&Q(kratkiy7 = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(fsap_code = sapcode_org.material)&Q(fkratkiy = sapcode_org.kratkiy_tekst_materiala))|
                  (Q(sap_code75 = sapcode_org.material)&Q(kratkiy75 = sapcode_org.kratkiy_tekst_materiala))
                  )[:1].get()
                  if '-E' in sapcode_org.material:
                        razlovka.ekratkiy = kratkiy
                  if '-Z' in sapcode_org.material:
                        razlovka.zkratkiy =kratkiy
                  if '-P' in sapcode_org.material:
                        razlovka.pkratkiy =kratkiy
                  if '-S' in sapcode_org.material:
                        razlovka.skratkiy =kratkiy
                  if '-A' in sapcode_org.material:
                        razlovka.akratkiy =kratkiy
                  if '-L' in sapcode_org.material:
                        razlovka.lkratkiy =kratkiy
                  if '-N' in sapcode_org.material:
                        razlovka.nkratkiy =kratkiy
                  if '-7' in sapcode_org.material:
                        if '-75' in sapcode_org.material:
                              razlovka.kratkiy75 =kratkiy
                        else:
                              razlovka.kratkiy7 =kratkiy
                  
                  razlovka.save()
            sapcode_org.kratkiy_tekst_materiala = kratkiy
            sapcode_org.save()
            return JsonResponse({'status':201})
      else:
            context ={
                  'sapcode':sapcode_org,
                  'section':'ALU сапкод'
            }
            return render(request,'pvc/edit.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator',])
def profile_edit(request,id):

      length_of_profile = LengthOfProfile.objects.get(id = id)

      if request.method == 'POST':
            form = LengthOfProfilwForm(data=request.POST,instance=length_of_profile)
            if form.is_valid():
                  form.save()
                  return redirect('show_profile')
      else:
            form = LengthOfProfilwForm(instance=length_of_profile)

      context ={
            'form':form
      }
      return render(request,'price/edit.html',context)

@csrf_exempt
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator',])
def delete_length_profile(request,id):
      profile_length = LengthOfProfile.objects.get(id = id)
      profile_length.delete()
      return JsonResponse({'msg':True})

@csrf_exempt
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator',])
def bulk_delete_length_profile(request):
      ids = request.POST.get('ids',None)
      if ids:
            ids = ids.split(',')
            profile_length = LengthOfProfile.objects.filter(id__in = ids)
            profile_length.delete()
      return JsonResponse({'msg':True})

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator',])
def show_price_profile(request):

      search = request.GET.get('search',None)

      if search:
            profiles = LengthOfProfile.objects.filter(artikul__icontains = search).order_by('-created_at')
      else:
            profiles = LengthOfProfile.objects.all().order_by('-created_at')

      paginator = Paginator(profiles, 25)

      if request.GET.get('page') != None:
            page_number = request.GET.get('page')
      else:
            page_number=1

      page_obj = paginator.get_page(page_number)
      context = {
            'profiles':page_obj
      }
      return render(request,'price/show.html',context)



class File:
      def __init__(self,file,filetype):
            self.file =file
            self.filetype =filetype


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','razlovka','only_razlovka'])
def upload_razlovka_simple(request):
      if request.method == 'POST':
            form = FileForm(request.POST, request.FILES)
            if form.is_valid():
                  file_path =form.cleaned_data["file"]
                  df = pd.read_excel(file_path)
                  df = df.astype(str)
                  df = df.replace('nan','')
                  save_razlovka(df,'simple')
                  context ={
                        'msg':'Simple razlovka successfully uploaded!'
                  }
                  
                  return render(request,'universal/upload.html',context)
      return render(request,'universal/main.html')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','razlovka','only_razlovka'])
def download_all_razlovki(request):
      file_type = request.GET.get('type',None)
      if file_type =='simple':
            simple_list = RazlovkaObichniy.objects.all().values_list('esap_code','ekratkiy','zsap_code','zkratkiy','psap_code','pkratkiy','ssap_code','skratkiy','asap_code','akratkiy','lsap_code','lkratkiy','nsap_code','nkratkiy','sap_code7','kratkiy7')
            data = pd.DataFrame(np.array(list(simple_list)),columns=[
                  'SAP код E','Экструзия холодная резка',
                  'SAP код Z','Печь старения',
                  'SAP код P','Покраска автомат',
                  'SAP код S','Сублимация',
                  'SAP код A','Анодировка',
                  'SAP код L','Ламинация',
                  'SAP код N','Наклейка',
                  'SAP код 7','U-Упаковка + Готовая Продукция'
                                                            ])
            
            data = data.replace('nan','')
            
            res = download_bs64([data,],'OBICHNIY')
            return res
      else:
            termo_list = RazlovkaTermo.objects.all().order_by('created_at').values_list('esap_code','ekratkiy','zsap_code','zkratkiy','psap_code','pkratkiy','ssap_code','skratkiy','asap_code','akratkiy','nsap_code','nkratkiy','ksap_code','kratkiy','lsap_code','lkratkiy','sap_code7','kratkiy7')
            data = pd.DataFrame(np.array(list(termo_list)),columns=[
                  'SAP код E','Экструзия холодная резка',
                  'SAP код Z','Печь старения',
                  'SAP код P','Покраска автомат',
                  'SAP код S','Сублимация',
                  'SAP код A','Анодировка',
                  'SAP код N','Наклейка',
                  'SAP код K','K-Комбинирования',
                  'SAP код L','Ламинация',
                  'SAP код 7','U-Упаковка + Готовая Продукция'
                                                            ])
            data = data.replace('nan','')
            res = download_bs64([data,],'TERMO')
      
      return res
      



@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','razlovka','only_razlovka'])
def show_razlovki(request):
     
      search_text = request.GET.get('search',None)

      if search_text:
            products = RazlovkaObichniy.objects.filter(
                  Q(esap_code__icontains = search_text)|
                  Q(ekratkiy__icontains = search_text)|
                  Q(zsap_code__icontains = search_text)|
                  Q(zkratkiy__icontains = search_text)|
                  Q(psap_code__icontains = search_text)|
                  Q(pkratkiy__icontains = search_text)|
                  Q(ssap_code__icontains = search_text)|
                  Q(skratkiy__icontains = search_text)|
                  Q(asap_code__icontains = search_text)|
                  Q(akratkiy__icontains = search_text)|
                  Q(lsap_code__icontains = search_text)|
                  Q(lkratkiy__icontains = search_text)|
                  Q(nsap_code__icontains = search_text)|
                  Q(nkratkiy__icontains = search_text)|
                  Q(sap_code7__icontains = search_text)|
                  Q(kratkiy7__icontains = search_text)|
                  Q(fsap_code__icontains = search_text)|
                  Q(fkratkiy__icontains = search_text)|
                  Q(sap_code75__icontains = search_text)|
                  Q(kratkiy75__icontains = search_text)
            ).order_by('-created_at')
      else:
            products = RazlovkaObichniy.objects.all().order_by('-created_at')

      paginator = Paginator(products, 25)

      if request.GET.get('page') != None:
            page_number = request.GET.get('page')
      else:
            page_number=1

      page_obj = paginator.get_page(page_number)

    
      

      context ={
            'section':'Обычный разловки',
            'products':page_obj,
            'type':False,
            'search':search_text
      }

                  
      return render(request,'universal/show_razlovki.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','razlovka','only_razlovka'])
def show_razlovki_termo(request):
      search_text = request.GET.get('search',None)

      if search_text:
            products = RazlovkaTermo.objects.filter(
                  Q(esap_code__icontains = search_text)|
                  Q(ekratkiy__icontains = search_text)|
                  Q(zsap_code__icontains = search_text)|
                  Q(zkratkiy__icontains = search_text)|
                  Q(psap_code__icontains = search_text)|
                  Q(pkratkiy__icontains = search_text)|
                  Q(ssap_code__icontains = search_text)|
                  Q(skratkiy__icontains = search_text)|
                  Q(asap_code__icontains = search_text)|
                  Q(akratkiy__icontains = search_text)|
                  Q(lsap_code__icontains = search_text)|
                  Q(lkratkiy__icontains = search_text)|
                  Q(nsap_code__icontains = search_text)|
                  Q(nkratkiy__icontains = search_text)|
                  Q(sap_code7__icontains = search_text)|
                  Q(kratkiy7__icontains = search_text)|
                  Q(fsap_code__icontains = search_text)|
                  Q(fkratkiy__icontains = search_text)|
                  Q(sap_code75__icontains = search_text)|
                  Q(kratkiy75__icontains = search_text)
            ).order_by('-created_at')
      else:
            products = RazlovkaTermo.objects.all().order_by('created_at')

      paginator = Paginator(products, 25)

      if request.GET.get('page') != None:
            page_number = request.GET.get('page')
      else:
            page_number=1

      page_obj = paginator.get_page(page_number)
      context ={
            'section':'Термо разловки',
            'products':page_obj,
            'type':True,
            'search':search_text
            
      }
                  
      return render(request,'universal/show_razlovki.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','razlovka','only_razlovka'])
def save_razlovka2(request):
      df = pd.read_excel('c:\\OpenServer\\domains\\Razlovka.xlsx','Лист1')
      # df = pd.read_excel('C:\\OSPanel\\domains\\Razlovka.xlsx','Лист1')
      df = df.astype(str)
      df = df.replace('nan','')
      
      save_razlovka(df,'simple')
      return JsonResponse({'a':'b'})


# Create your views here.
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','razlovka','only_razlovka'])
def index(request):
      return render(request,'aluminiy/index.html')


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','razlovka','only_razlovka'])
def aluminiy_productbases(request):
  df = pd.read_excel('c:\\OpenServer\\domains\\Новая база2.XLSX','без термо')
  
  for i in range(0,df.shape[0]):
    material =df['Материал'][i] 
    artikul =df['Ариткул'][i]
    section =df['Передел'][i]
    counter =df['Счетчик'][i]
    gruppa_materialov =df['Группа материалов'][i]
    kratkiy_tekst_materiala=df['Краткий текст материала'][i]
    kombinirovanniy=df['Комбинирования'][i]
    
    artiku_comp = AluminiyProduct(
      material =material,
      artikul =artikul,
      section =section,
      counter =counter,
      gruppa_materialov =gruppa_materialov,
      kratkiy_tekst_materiala =kratkiy_tekst_materiala,
      kombinirovanniy =kombinirovanniy
        )
    artiku_comp.save()
  
  return JsonResponse({'converted':'a'})

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1','razlovka','only_razlovka'])
def alu_product_base(request):
  df = pd.read_excel('C:\\OpenServer\\domains\\Aluminiy_baza.xlsx','Лист1') 
  
  for i in range(0,df.shape[0]):
    ekstruziya_sap_kod =df['Экструзия сап код'][i]
    ekstruziya_kratkiy_tekst =df['Экструзия краткий текст'][i]
    zakalka_sap_kod =df['Закалка сап код'][i]
    zakalka_kratkiy_tekst =df['Закалка краткий текст'][i]
    pokraska_sap_kod =df['Покраска сап код'][i]
    pokraska_kratkiy_tekst =df['Покраска краткий текст'][i]
    sublimatsiya_sap_kod =df['Сублимация сап код'][i]
    sublimatsiya_kratkiy_tekst =df['Сублимация краткий текст'][i]
    anodirovka_sap_kod =df['Анодировка сап код'][i]
    anodirovka_kratkiy_tekst =df['Анодировка краткий текст'][i]
    laminatsiya_sap_kod =df['Ламинация сап код'][i]
    laminatsiya_kratkiy_tekst =df['Ламинация краткий текст'][i]
    nakleyka_sap_kod =df['Наклейка сап код'][i]
    nakleyka_kratkiy_tekst =df['Наклейка краткий текст'][i]
    upakovka_sap_kod =df['Упаковка сап код'][i]
    upakovka_kratkiy_tekst =df['Упаковка краткий текст'][i]
    fabrikatsiya_sap_kod =df['Фабрикация сап код'][i]
    fabrikatsiya_kratkiy_tekst =df['Фабрикация краткий текст'][i]
    upakovka2_sap_kod =df['Упаковка2 сап код'][i]
    upakovka2_kratkiy_tekst =df['Упаковка2 краткий текст'][i]
    
    artiku_comp =AluminiyProductBasesimple(
      ekstruziya_sap_kod =ekstruziya_sap_kod,
      ekstruziya_kratkiy_tekst =ekstruziya_kratkiy_tekst,
      zakalka_sap_kod =zakalka_sap_kod,
      zakalka_kratkiy_tekst =zakalka_kratkiy_tekst,
      pokraska_sap_kod =pokraska_sap_kod,
      pokraska_kratkiy_tekst =pokraska_kratkiy_tekst,
      sublimatsiya_sap_kod =sublimatsiya_sap_kod,
      sublimatsiya_kratkiy_tekst =sublimatsiya_kratkiy_tekst,
      anodirovka_sap_kod =anodirovka_sap_kod,
      anodirovka_kratkiy_tekst =anodirovka_kratkiy_tekst,
      laminatsiya_sap_kod =laminatsiya_sap_kod,
      laminatsiya_kratkiy_tekst =laminatsiya_kratkiy_tekst,
      nakleyka_sap_kod =nakleyka_sap_kod,
      nakleyka_kratkiy_tekst =nakleyka_kratkiy_tekst,
      upakovka_sap_kod =upakovka_sap_kod,
      upakovka_kratkiy_tekst =upakovka_kratkiy_tekst,
      fabrikatsiya_sap_kod =fabrikatsiya_sap_kod,
      fabrikatsiya_kratkiy_tekst =fabrikatsiya_kratkiy_tekst,
      upakovka2_sap_kod =upakovka2_sap_kod,
      upakovka2_kratkiy_tekst =upakovka2_kratkiy_tekst
        )
    artiku_comp.save()
  return JsonResponse({'converted':'a'})

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def upload_product(request):
  if request.method == 'POST':
    form = FileForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('aluminiy_files')
  else:
      form =FileForm()
      context ={
        'form':form
      }
  return render(request,'excel_form.html',context)


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def upload_for_char(request):
      if request.method == 'POST':
            form = FileForm(request.POST, request.FILES)
            if form.is_valid():
                  form.save()
                  return redirect('char_files_org')
      else:
            form =FileForm()
            context ={
            'form':form,
            'section':'Формирование сапкода обычный',
            }
      return render(request,'universal/main.html',context)


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def upload_product_org(request):
      if request.method == 'POST':
            form = FileForm(request.POST, request.FILES)
            if form.is_valid():
                  title = str(form.cleaned_data['file']).split('.')[0]
                  worker_id = request.POST.get('worker',None)
                  new_order = form.save()
                  if worker_id:
                        is_1101 = request.POST.get('for1101','off')
                        is_1201 = request.POST.get('for1201','off')
                        is_1112 = request.POST.get('for1112','off')

                        o_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                        
                        paths ={
                                    'obichniy_file':f'{MEDIA_ROOT}\\{new_order.file}',
                                    'oid':new_order.id,
                                    'obichniy_date':o_created_at,
                                    'is_obichniy':'yes',
                                    'type':'Обычный',
                                    'status_l':'on hold',
                                    'status_raz':'on hold',
                                    'status_zip':'on hold',
                                    'status_norma':'on hold',
                                    'status_text_l':'on hold',
                                    'status_norma_lack':'on hold',
                                    'status_texcarta':'on hold',
                                    'is_1101':is_1101,
                                    'is_1201':is_1201,
                                    'is_1112':is_1112,

                                }
                         
                        order = Order(title = title,owner=request.user,current_worker_id= worker_id,aluminiy_worker_id =worker_id,paths=paths,order_type =1)
                        order.save()
                  return redirect('order_detail',id=order.id)
            else:
                  form =FileFormTermo()
                  workers = User.objects.filter(role = 'moderator')
                  
                  context ={
                  'form':form,
                  'section':'Формирование сапкода термо',
                  'workers':workers
                  }
                  return render(request,'universal/main.html',context)
      else:
            form =FileForm()
            workers = User.objects.filter(role = 'moderator')
            context ={
            'form':form,
            'section':'Формирование сапкода обычный',
            'workers':workers
            }
      return render(request,'universal/main.html',context)


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def aluminiy_files(request):
  files = AluFile.objects.filter(generated =False).order_by('-created_at')
  context ={'files':files}
  return render(request,'aluminiy/alu_file_list.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def char_files_org(request):
  files = AluFile.objects.filter(generated =False).order_by('-created_at')[:1]
  context ={'files':files,'section':'Формированный обычный файлы','type':'ОБЫЧНЫЙ','link':'/termo/character-force/','char':True,'char_type':'simple'}
  return render(request,'universal/file_list.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def aluminiy_files_org(request):
  files = AluFile.objects.filter(generated =False).order_by('-created_at')
  context ={'files':files,'section':'Формированный обычный файлы','type':'ОБЫЧНЫЙ','link':'/alu/alum-org/add/'}
  return render(request,'universal/file_list.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def aluminiy_group(request):
      aluminiy_group =AluminiyProduct.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
      
      umumiy={}
      for al in aluminiy_group:    
            
            umumiy[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      
      return JsonResponse({'data':umumiy})


def update_char_title_function(df_title,df_t4,order_id,file_type='aluminiy'):
      df = df_title
      df_extrusion = df_t4
      e_list =df_extrusion['SAP CODE E'].values.tolist()
      df =df.astype(str)
      pathzip = characteristika_created_txt_create(df,e_list,order_id,file_name=file_type)

      return pathzip

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def update_char_title(request,id):
      file = CharacteristikaFile.objects.get(id=id).file
      df = pd.read_excel(f'{MEDIA_ROOT}/{file}','title')
      df_extrusion = pd.read_excel(f'{MEDIA_ROOT}/{file}','T4')
      e_list =df_extrusion['SAP CODE E'].values.tolist()
      df =df.astype(str)
      
      pathzip = characteristika_created_txt_create(df,e_list,'aluminiy')
      fileszip = [File(file=path,filetype='BENKAM') for path in pathzip]  

      context = {
            'files':fileszip,
            'section':'Формированные файлы'
            }

      return render(request,'universal/generated_files.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def aluminiy_files_simple_char_title(request):
      files = AluFile.objects.filter(file_type ='title')
      context ={'files':files}
      return render(request,'aluminiy/alu_file_list_char_title.html',context)

                  


brand_kraski_snaruji_ABC ={
      'A': 'AKZONOBEL',
      'R':  'RAINBOW',
      'P':  'PULVER',
      'T':  'TIGER',
      'B':  'BPC',
      'M':  'MIKROTON',
      'J':  'JOTUN',
      'C':'Caesar',
      'nan':'',
}

kod_dekorativ_snaruji_ABC ={
      '3701':'МАХАГОН',
      '7777':'ЗОЛОТОЙ ДУБ',
      '3702':'ТЁМНЫЙ ОРЕХ',
      '8888':'ДУБ МОККО',
      '9999':'ШЕФ ДУБ СЕРЫЙ',
      '3801':'3D',
      'nan':''  
}

svet_lam_plenke_POL ={
      'Алюкс антрацит':'АЛЮКС АНТРАЦИТ',
      'Метбраш Алюмин':'МЕТБРАШ АЛЮМИН',
      'Кремвейс':'КРЕМВЕЙС',
      'Алюкс антрацит ADO':'АЛЮКС АНТРАЦИТ ADO',
      'Золотой дуб':'ЗОЛОТОЙ ДУБ',
      'Орех':'ОРЕХ',
      'Дуб мокко':'ДУБ МОККО',
      'Грецкий орех':'ГРЕЦКИЙ ОРЕХ',
      'Дерево бальза':'ДЕРЕВО БАЛЬЗА',
      'Винчестер':'ВИНЧЕСТЕР',
      'Орех Ребраун':'ОРЕХ РЕБРАУН',
      'Шеффелдский дуб серый':'ШЕФ ДУБ СЕРЫЙ',
      'Шеф Альпийский дуб':'ШЕФ АЛЬП ДУБ',
      'Гранитовый шеф дуб':'ГРАНИТ ШЕФ ДУБ',
      'Метбраш серый антрацит':'МЕТБ СЕРЫЙ АНТР',
      'Красный орех':'КРАСНЫЙ ОРЕХ',
      'Шеффелдский дуб светлый':'ШЕФ ДУБ СВЕТ',
      'Орех терра':'ОРЕХ ТЕРРА',
      'Метбраш серый кварц':'МЕТБ СЕРЫЙ КВАР',
      'Метбраш платин':'МЕТБ ПЛАТИН',
      'Терновый дуб':'ТЕРНОВЫЙ ДУБ',
      'Алюкс серый алюминий':'АЛЮКС СЕРЫЙ АЛЮ',
      'Сантана':'САНТАНА',
      'Светлый дуб':'СВЕТЛЫЙ ДУБ',
      'ТЕМНЫЙ ДУБ':'ТЕМНЫЙ ДУБ',
      'GOLD BRUSH':'GOLD BRUSH',
      'X-BRUSH':'X-BRUSH',
      'Ocean Blue':'Ocean Blue',
      'Махагон':'МАХАГОН',
      'АЛЮКС БЕЛЫЙ АЛЮМИН':'АЛЮКС БЕЛЫЙ АЛЮМИН',
      'МАТОВЫЙ БЕЛЫЙ':'МАТОВЫЙ БЕЛЫЙ',
      'МАТОВЫЙ ЧЁРНЫЙ':'МАТОВЫЙ ЧЁРНЫЙ',
      'Алюкс белый алюмин':'АЛЮКС БЕЛЫЙ АЛЮМИН',
      'Матовый белый':'МАТОВЫЙ БЕЛЫЙ',
      'Матовый чёрный':'МАТОВЫЙ ЧЁРНЫЙ',
      
}

svet_lam_plenke_NA ={
      'Алюкс антрацит':'НА АЛЮКС АНТРАЦИТ',
      'Метбраш Алюмин':'НА МЕТБРАШ АЛЮМИН',
      'Кремвейс':'НА КРЕМВЕЙС',
      'Алюкс антрацит ADO':'НА АЛЮКС АНТРАЦИТ ADO',
      'Золотой дуб':'НА ЗОЛОТОЙ ДУБ',
      'Орех':'НА ОРЕХ',
      'Дуб мокко':'НА ДУБ МОККО',
      'Грецкий орех':'НА ГРЕЦКИЙ ОРЕХ',
      'Дерево бальза':'НА ДЕРЕВО БАЛЬЗА',
      'Винчестер':'НА ВИНЧЕСТЕР',
      'Орех Ребраун':'НА ОРЕХ РЕБРАУН',
      'Шеффелдский дуб серый':'НА ШЕФ ДУБ СЕРЫЙ',
      'Шеф Альпийский дуб':'НА ШЕФ АЛЬП ДУБ',
      'Гранитовый шеф дуб':'НА ГРАНИТ ШЕФ ДУБ',
      'Метбраш серый антрацит':'НА МЕТБ СЕРЫЙ АНТР',
      'Красный орех':'НА КРАСНЫЙ ОРЕХ',
      'Шеффелдский дуб светлый':'НА ШЕФ ДУБ СВЕТЛЫЙ',
      'Орех терра':'НА ОРЕХ ТЕРРА',
      'Метбраш серый кварц':'НА МЕТБ СЕРЫЙ КВАР',
      'Метбраш платин':'НА МЕТБ ПЛАТИН',
      'Терновый дуб':'НА ТЕРНОВЫЙ ДУБ',
      'Алюкс серый алюминий':'НА АЛЮКС СЕРЫЙ АЛЮ',
      'Сантана':'НА САНТАНА',
      'Светлый дуб':'НА СВЕТЛЫЙ ДУБ',
      'ТЕМНЫЙ ДУБ':'НА ТЕМНЫЙ ДУБ',
      'GOLD BRUSH':'НА GOLD BRUSH',
      'X-BRUSH':'НА X-BRUSH',
      'Ocean Blue':'Ocean Blue',
      'Махагон':'МАХАГОН',
      'АЛЮКС БЕЛЫЙ АЛЮМИН':'НА АЛЮКС БЕЛЫЙ АЛЮМИН',
      'МАТОВЫЙ БЕЛЫЙ':'НА МАТОВЫЙ БЕЛЫЙ',
      'МАТОВЫЙ ЧЁРНЫЙ':'НА МАТОВЫЙ ЧЁРНЫЙ',
      'Алюкс белый алюмин':'НА АЛЮКС БЕЛЫЙ АЛЮМИН',
      'Матовый белый':'НА МАТОВЫЙ БЕЛЫЙ',
      'Матовый чёрный':'НА МАТОВЫЙ ЧЁРНЫЙ',
}

svet_lam_plenke_VN ={
      'Алюкс антрацит':'ВН АЛЮКС АНТРАЦИТ',
      'Метбраш Алюмин':'ВН МЕТБРАШ АЛЮМИН',
      'Кремвейс':'ВН КРЕМВЕЙС',
      'Алюкс антрацит ADO':'ВН АЛЮКС АНТРАЦИТ ADO',
      'Золотой дуб':'ВН ЗОЛОТОЙ ДУБ',
      'Орех':'ВН ОРЕХ',
      'Дуб мокко':'ВН ДУБ МОККО',
      'Грецкий орех':'ВН ГРЕЦКИЙ ОРЕХ',
      'Дерево бальза':'ВН ДЕРЕВО БАЛЬЗА',
      'Винчестер':'ВН ВИНЧЕСТЕР',
      'Орех Ребраун':'ВН ОРЕХ РЕБРАУН',
      'Шеффелдский дуб серый':'ВН ШЕФ ДУБ СЕРЫЙ',
      'Шеф Альпийский дуб':'ВН ШЕФ АЛЬП ДУБ',
      'Гранитовый шеф дуб':'ВН ГРАНИТ ШЕФ ДУБ',
      'Метбраш серый антрацит':'ВН МЕТБ СЕРЫЙ АНТР',
      'Красный орех':'ВН КРАСНЫЙ ОРЕХ',
      'Шеффелдский дуб светлый':'ВН ШЕФ ДУБ СВЕТЛЫЙ',
      'Орех терра':'ВН ОРЕХ ТЕРРА',
      'Метбраш серый кварц':'ВН МЕТБ СЕРЫЙ КВАР',
      'Метбраш платин':'ВН МЕТБ ПЛАТИН',
      'Терновый дуб':'ВН ТЕРНОВЫЙ ДУБ',
      'Алюкс серый алюминий':'ВН АЛЮКС СЕРЫЙ АЛЮ',
      'Сантана':'ВН САНТАНА',
      'Светлый дуб':'ВН СВЕТЛЫЙ ДУБ',
      'ТЕМНЫЙ ДУБ':'ВН ТЕМНЫЙ ДУБ',
      'GOLD BRUSH':'ВН GOLD BRUSH',
      'X-BRUSH':'ВН X-BRUSH',
      'Ocean Blue':'Ocean Blue',
      'Махагон':'МАХАГОН',
      'АЛЮКС БЕЛЫЙ АЛЮМИН':'ВН АЛЮКС БЕЛЫЙ АЛЮМИН',
      'МАТОВЫЙ БЕЛЫЙ':'ВН МАТОВЫЙ БЕЛЫЙ',
      'МАТОВЫЙ ЧЁРНЫЙ':'ВН МАТОВЫЙ ЧЁРНЫЙ',
      'Алюкс белый алюмин':'ВН АЛЮКС БЕЛЫЙ АЛЮМИН',
      'Матовый белый':'ВН МАТОВЫЙ БЕЛЫЙ',
      'Матовый чёрный':'ВН МАТОВЫЙ ЧЁРНЫЙ',
}


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def get_bazaprofiley(request):
      data = request.GET.get('data')
      datas = json.loads(data)
      baza_profile = AluProfilesData.objects.filter(Q(data__Артикул=datas['artikul'])|Q(data__Компонент =datas['artikul']))[:1].get().data
      artikul ={
            'system' : baza_profile['Система'],
            'artikul' :  baza_profile['Артикул'],
            'komponent' :  baza_profile['Компонент'],
            'description' :  baza_profile['Product description - RUS'],
            'kombinatsiya' :  baza_profile['Комбинация'],
            'tip_combination' :  baza_profile['Тип Комбинация'],
            'tip_profilya' :  baza_profile['Тип профиля'],
            'visota' :  baza_profile['Высота'],
            'shirina' :  baza_profile['Ширина'],
            'pol_fason' :  baza_profile['Полый и Фасонный'],
            'bez_nakleyki' :  baza_profile['Без наклейки'],
            'kod_nakleyki' :  baza_profile['Код наклейки'],
            'udal_ves' :  baza_profile['Удел.вес за м'],
            'baza' :  baza_profile['BAZA'],
            'link' :  baza_profile['Ссылка для чертежей'],
      }
      return JsonResponse({"msg":True,'saved':True,'artikul':artikul})





@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def edit_bazaprofiley(request,id):
      if request.method =='POST':
            json_data = request.POST.get('data',None)
           
            if json_data:
                  data = json.loads(json_data)
                  base_profile = AluProfilesData.objects.get(id=id)
                  base_profile.data =data
                  base_profile.save()
                  return JsonResponse({'msg':True})
            else:
                  return JsonResponse({'msg':False})
      else:
            if  AluProfilesData.objects.filter(data__has_key ='columns').exists():
                  columns =  AluProfilesData.objects.filter(data__has_key ='columns')[:1].get().data['columns']
                  profile = AluProfilesData.objects.get(id = id)
                  context ={
                        'product':profile,
                        'columns':columns,
                        'json_column':json.dumps(columns,ensure_ascii=False),
                  }
                  return render(request,'aluminiy/edit_sapcode.html',context)

            return JsonResponse({'msg':True})

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def delete_bazaprofiley(request,id):
      baza_profile = AluProfilesData.objects.get(id =id)
      baza_profile.delete()
      return JsonResponse({'msg':True})

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def list_bazaprofiley(request):
      if  AluProfilesData.objects.filter(data__has_key ='columns').exists():
            columns =  AluProfilesData.objects.filter(data__has_key ='columns')[:1].get().data['columns']
            search = request.GET.get('search',None)
            if search:
                  profiles = AluProfilesData.objects.filter(Q(data__Компонент__icontains =search)|Q(data__Артикул__icontains =search)).order_by('-created_at')
            else:
                  profiles = AluProfilesData.objects.all().order_by('-created_at')

            paginator = Paginator(profiles, 25)

            if request.GET.get('page') != None:
                  page_number = request.GET.get('page')
            else:
                  page_number=1

            page_obj = paginator.get_page(page_number)
            context ={
                  'products':page_obj,
                  'columns':columns
            }
            return render(request,'aluminiy/list_sapcodes.html',context)
      else:
            return JsonResponse({'message':'Baza Profiley bosh'})

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def full_update_bazaprofiley(request):
      if request.method == 'POST':
            data = request.POST.copy()
            form = FileFormBazaprofiley(data, request.FILES)
            if form.is_valid():
                  form_file = form.save()
                  file = form_file.file
                  path =f'{MEDIA_ROOT}/{file}'
                  
                  df = pd.read_excel(path,sheet_name='ОС')
                  df = df.astype(str)
                  df = df.replace('nan','0')
                  df = df.replace('0.0','0')
                  
                  columns = df.columns
                  print(columns)
            
                  AluProfilesData(data ={'columns':list(columns)}).save()
                  for key, row in df.iterrows():
                        norma_dict = {}
                        for col in columns:
                              norma_dict[col]=row[col]
                        AluProfilesData(data =norma_dict).save()

            return redirect('list_bazaprofiley')
      else:
            return render(request,'norma/benkam/main.html')



@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])    
def product_add_second_org(request,id):
      file = AluFile.objects.get(id=id).file
      df = pd.read_excel(f'{MEDIA_ROOT}/{file}')
      df =df.astype(str)
      
      now = datetime.now()
      year =now.strftime("%Y")
      month =now.strftime("%B")
      day =now.strftime("%a%d")
      hour =now.strftime("%H HOUR")
      minut =now.strftime("%M")
      
      order_id = request.GET.get('order_id',None)
      

      doesnotexist,correct = check_for_correct(df,filename='aluminiy')
      if not correct:
            context ={
                  'AluProflesData':doesnotexist,
                  'filename':'aluminiy'
            }
           

            if order_id:
                  order = Order.objects.get(id = order_id)
                  paths = order.paths
                  l_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                  paths['obichniy_lack_file']= ''
                  # paths['obichniy_lack_file']= path_not_exists
                  paths['l_created_at']= l_created_at
                  paths['status_l']= 'on process'
                  

                  order.paths = paths
                  order.alumin_wrongs = request.user
                  order.current_worker = request.user
                  order.work_type = 3
                  order.save()
                  context['order'] = order
                  paths =  order.paths
                  for key,val in paths.items():
                        context[key] = val
                  
                  return render(request,'order/order_detail.html',context)
            # writer.save()
            return render(request,'utils/components.html',context)
      
      aluminiy_group = AluminiyProduct.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
      umumiy_counter={}
      for al in aluminiy_group:
            umumiy_counter[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      
      aluminiy_group_termo = AluminiyProductTermo.objects.values('section','artikul').order_by('section').annotate(total_max=Max('counter'))
      umumiy_counter_termo = {}
      for al in aluminiy_group_termo:
            umumiy_counter_termo[ al['artikul'] + '-' + al['section'] ] = al['total_max']
      
      
      
      
      for key,row in df.iterrows():
            if row['Тип покрытия'] == 'nan':
                  df = df.drop(key)
      
            
      
      
      df_new = pd.DataFrame()
      df_new['Название системы']=df['Название системы']
      df_new['SAP код E']=''
      df_new['Экструзия холодная резка']=''
      df_new['SAP код Z']=''
      df_new['Печь старения']=''
      df_new['SAP код P']=''
      df_new['Покраска автомат']=''
      df_new['SAP код S']=''
      df_new['Сублимация']=''
      df_new['SAP код A']=''
      df_new['Анодировка']=''
      df_new['SAP код L']=''
      df_new['Ламинация']=''
      df_new['SAP код N']=''
      df_new['Наклейка']=''
      df_new['SAP код 7']=''
      df_new['U-Упаковка + Готовая Продукция']=''
      df_new['SAP код F']=''
      df_new['Фабрикация']=''
      df_new['SAP код 75']=''
      df_new['U-Упаковка + Готовая Продукция 75']=''

      
      
      
      cache_for_cratkiy_text =[]
      duplicat_list =[]
      
      exturision_list = []
      
      for key,row in df.iterrows():
            row['Сплав'] = row['Сплав'].replace('.0','')
            row['Сплав'] = row['Сплав'].replace('.0','')
            row['Длина (мм)'] = row['Длина (мм)'].replace('.0','')
            row['Бренд краски снаружи'] = row['Бренд краски снаружи'].replace('.0','')
            row['Код краски снаружи'] = row['Код краски снаружи'].replace('.0','')
            row['Бренд краски внутри'] = row['Бренд краски внутри'].replace('.0','')
            row['Код краски внутри'] = row['Код краски внутри'].replace('.0','')
            row['Код декор пленки снаружи'] = row['Код декор пленки снаружи'].replace('.0','')
            row['Цвет декор пленки снаружи'] = row['Цвет декор пленки снаружи'].replace('.0','')
            row['Код декор пленки внутри'] = row['Код декор пленки внутри'].replace('.0','')
            row['Код цвета анодировки внутри'] = row['Код цвета анодировки внутри'].replace('.0','')
            row['Код цвета анодировки снаружи'] = row['Код цвета анодировки снаружи'].replace('.0','')
            row['Контактность анодировки'] = row['Контактность анодировки'].replace('.0','')
            row['Код лам пленки снаружи'] = row['Код лам пленки снаружи'].replace('.0','')
            row['Код лам пленки внутри'] = row['Код лам пленки внутри'].replace('.0','')
            
            
            
            product_exists = AluProfilesData.objects.filter(data__Артикул=row['Артикул']).exists()
            if row['Код декор пленки снаружи'] !='nan' and '.0' in row['Код декор пленки снаружи']:
                  df['Код декор пленки снаружи'][key] =df['Код декор пленки снаружи'][key].replace('.0','')
            
            if product_exists:
                  component = AluProfilesData.objects.filter(data__Артикул=row['Артикул'])[:1].get().data['Компонент']
                  print(component)
            else:
                  if  AluProfilesData.objects.filter(data__Компонент=row['Артикул']).exists():
                        component = row['Артикул']
                        termo = True
                  else:
                        continue

            if 'Название export' in list(df.columns):
                  if ((row['Название export'] == 'nan') or (row['Название export'] == '')):
                        export_name = ''
                  else:
                        export_name = row['Название export']
            else:
                  export_name = ''

            if ((row['Название савдо'] == 'nan') or (row['Название савдо'] == '')):
                  online_savdo_name = ''
            else:
                  online_savdo_name = row['Название савдо']
                  
            if df['Длина при выходе из пресса'][key] != 'nan' and df['Длина при выходе из пресса'][key].replace('.0','')!= row['Длина (мм)']:
                  dlina = df['Длина при выходе из пресса'][key].replace('.0','')
                        
                  df_new['Фабрикация'][key]=df['Краткий текст товара'][key]
                  df_new['U-Упаковка + Готовая Продукция 75'][key]=df['Краткий текст товара'][key]
                  
                  
                  if df['Тип покрытия'][key] == 'Ламинированный':
                        plenki1 = False
                        plenki2 = False
                        if df['Код лам пленки снаружи'][key] != 'nan':
                              laminatsiya =row['Код лам пленки снаружи'].replace('.0','')+'/XXXX'
                              plenki1 = True
                              
                        if df['Код лам пленки внутри'][key] != 'nan':
                              laminatsiya ='XXXX/'+df['Код лам пленки внутри'][key].replace('.0','')
                              plenki2 =True
                              
                        if plenki1 and plenki2:
                              laminatsiya =df['Код лам пленки снаружи'][key].replace('.0','') +'/'+ df['Код лам пленки внутри'][key].replace('.0','')
                              
                        ll =row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')+'/'+df['Код краски внутри'][key].replace('.0','')+'_'+laminatsiya +' ' +row['Код наклейки']
                        df_new['Ламинация'][key] = fabrikatsiya_sap_kod(ll,df['Длина при выходе из пресса'][key].replace('.0',''))

            else:
                  dlina = df['Длина (мм)'][key]
                  df_new['U-Упаковка + Готовая Продукция'][key] = df['Краткий текст товара'][key]
                  
                  
                  if df['Тип покрытия'][key] == 'Ламинированный':
                        plenki1 = False
                        plenki2 = False
                        if row['Код лам пленки снаружи'] != 'nan':
                              laminatsiya =row['Код лам пленки снаружи'].replace('.0','')+'/XXXX'
                              plenki1 = True
                              
                        if df['Код лам пленки внутри'][key] != 'nan':
                              laminatsiya ='XXXX/'+df['Код лам пленки внутри'][key].replace('.0','')
                              plenki2 =True
                              
                        if plenki1 and plenki2:
                              laminatsiya =df['Код лам пленки снаружи'][key].replace('.0','') +'/'+ df['Код лам пленки внутри'][key].replace('.0','')
                              
                        df_new['Ламинация'][key] = df['Краткий текст товара'][key]
                  
            if df['Длина при выходе из пресса'][key] != 'nan' and df['Длина при выходе из пресса'][key].replace('.0','')!= row['Длина (мм)']:
                  if AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='F',kratkiy_tekst_materiala=df_new['Фабрикация'][key]).exists():
                        df_new['SAP код F'][key] = AluminiyProduct.objects.filter(artikul = df['Артикул'][key],section ='F',kratkiy_tekst_materiala=df_new['Фабрикация'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код F'][key],df_new['Фабрикация'][key],'F'])
                  else: 
                        if AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='F').exists():
                              umumiy_counter[df['Артикул'][key]+'-F'] += 1
                              max_valuesF = umumiy_counter[df['Артикул'][key]+'-F']
                              materiale = df['Артикул'][key] +"-F{:03d}".format(max_valuesF)
                              AluminiyProduct(artikul =df['Артикул'][key],section ='F',counter=max_valuesF,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Фабрикация'][key],material=materiale).save()
                              df_new['SAP код F'][key]=materiale
                              component2 = materiale.split('-')[0]
                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid =aluprofiles.data['Полый и Фасонный']
                              
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()
                              
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Фабрикация'][key],
                                                'section':'F-Фабрикация',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':df['Длина (мм)'][key],
                                                'surface_treatment':row['Тип покрытия'],
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                'rawmat_type':'ПФ',
                                                'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'group_prise': export_description_eng.group_price,
                                                'nazvaniye_export':export_name,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
                              
                        else:
                              materiale = df['Артикул'][key] +"-F{:03d}".format(1)
                              AluminiyProduct(artikul =df['Артикул'][key],section ='F',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Фабрикация'][key],material=materiale).save()
                              df_new['SAP код F'][key]=materiale
                              umumiy_counter[df['Артикул'][key]+'-F'] = 1
                              component2 = materiale.split('-')[0]
                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid = aluprofiles.data['Полый и Фасонный']
                              
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()
                              
                              
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Фабрикация'][key],
                                                'section':'F-Фабрикация',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':df['Длина (мм)'][key],
                                                'surface_treatment':row['Тип покрытия'],
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                'rawmat_type':'ПФ',
                                                'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'group_prise': export_description_eng.group_price,
                                                'nazvaniye_export':export_name,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
                              
                              
                  
                  
                  if AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='75',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key]).exists():
                        df_new['SAP код 75'][key] = AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='75',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код 75'][key],df_new['U-Упаковка + Готовая Продукция 75'][key],'75'])
                  else: 
                        if AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='75').exists():
                              umumiy_counter[df['Артикул'][key]+'-75'] += 1
                              max_values75 = umumiy_counter[df['Артикул'][key]+'-75']
                              
                              if max_values75 <= 99:
                                    materiale = df['Артикул'][key]+"-75{:02d}".format(max_values75)
                              else:
                                    counter =7500 + max_values75
                                    materiale = df['Артикул'][key]+"-{:04d}".format(counter)
                                    
                                    
                              AluminiyProduct(artikul =df['Артикул'][key],section ='75',counter=max_values75,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key],material=materiale).save()
                              df_new['SAP код 75'][key] = materiale
                              
                             
                              component2 = materiale.split('-')[0]

                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid =aluprofiles.data['Полый и Фасонный']
                              
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                              
                              
                              surface_treatment_export=''
                              if row['Тип покрытия'].lower() =='неокрашенный':
                                    surface_treatment_export ='Неокрашенный'
                              elif ((row['Тип покрытия'].lower() =='окрашенный') or (row['Тип покрытия'].lower() =='белый')):
                                    surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']] +' ' + row['Код краски снаружи']
                              elif row['Тип покрытия'].lower() =='сублимированный':
                                    surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                              elif row['Тип покрытия'].lower() =='анодированный':
                                    surface_treatment_export = row['Код цвета анодировки снаружи']
                              elif row['Тип покрытия'].lower() =='ламинированный':
                                    if (row['Цвет лам пленки снаружи']=='XXXX' or row['Цвет лам пленки снаружи']=='nan'):
                                          surface_treatment_export = svet_lam_plenke_VN[row['Цвет лам пленки внутри']]                  
                                    else:
                                          if (row['Цвет лам пленки внутри']=='XXXX' or row['Цвет лам пленки внутри']=='nan'):
                                                surface_treatment_export = svet_lam_plenke_NA[row['Цвет лам пленки снаружи']] 
                                          else:
                                                surface_treatment_export = svet_lam_plenke_POL[row['Цвет лам пленки снаружи']]
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['U-Упаковка + Готовая Продукция 75'][key],
                                                'section':'V-Упаковка + Готовая продукция',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':df['Длина (мм)'][key],
                                                'surface_treatment':row['Тип покрытия'],
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ГП',
                                                'hollow_and_solid':hollow_and_solid,
                                                'export_description':export_description,
                                                'export_description_eng':export_description_eng.bux_name_eng,
                                                'tnved':export_description_eng.tnved,
                                                'surface_treatment_export':surface_treatment_export,# GP da kerak
                                                'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'group_prise': export_description_eng.group_price,
                                                'nazvaniye_export':export_name,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
                        
                        else:
                              materiale = df['Артикул'][key]+"-75{:02d}".format(1)
                              AluminiyProduct(artikul = df['Артикул'][key],section ='75',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция 75'][key],material=materiale).save()
                              df_new['SAP код 75'][key] = materiale 
                              umumiy_counter[df['Артикул'][key]+'-75'] = 1
                              
                              component2 = materiale.split('-')[0]
                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid =aluprofiles.data['Полый и Фасонный']
                              
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                              
                              
                              surface_treatment_export=''
                              if row['Тип покрытия'].lower() =='неокрашенный':
                                    surface_treatment_export ='Неокрашенный'
                              elif ((row['Тип покрытия'].lower() =='окрашенный') or (row['Тип покрытия'].lower() =='белый')):
                                    surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']]+' '+row['Код краски снаружи']
                              elif row['Тип покрытия'].lower() =='сублимированный':
                                    surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                              elif row['Тип покрытия'].lower() =='анодированный':
                                    surface_treatment_export = row['Код цвета анодировки снаружи']
                              elif row['Тип покрытия'].lower() =='ламинированный':
                                    if (row['Цвет лам пленки снаружи']=='XXXX' or row['Цвет лам пленки снаружи']=='nan'):
                                          surface_treatment_export = svet_lam_plenke_VN[row['Цвет лам пленки внутри']]                  
                                    else:
                                          if (row['Цвет лам пленки внутри']=='XXXX' or row['Цвет лам пленки внутри']=='nan'):
                                                surface_treatment_export = svet_lam_plenke_NA[row['Цвет лам пленки снаружи']] 
                                          else:
                                                surface_treatment_export = svet_lam_plenke_POL[row['Цвет лам пленки снаружи']]
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['U-Упаковка + Готовая Продукция 75'][key],
                                                'section':'V-Упаковка + Готовая продукция',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':df['Длина (мм)'][key],
                                                'surface_treatment':row['Тип покрытия'],
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ГП',
                                                'hollow_and_solid':hollow_and_solid,
                                                'export_description':export_description,
                                                'export_description_eng':export_description_eng.bux_name_eng,
                                                'tnved':export_description_eng.tnved,
                                                'surface_treatment_export':surface_treatment_export,# GP da kerak
                                                'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'group_prise': export_description_eng.group_price,
                                                'nazvaniye_export':export_name,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
                              
            else:     
                  if AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key]).exists():
                        df_new['SAP код 7'][key] = AluminiyProduct.objects.filter(artikul =df['Артикул'][key],section ='7',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код 7'][key],df_new['U-Упаковка + Готовая Продукция'][key],'7'])
                  else: 
                        if AluminiyProduct.objects.filter(artikul=df['Артикул'][key],section ='7').exists():
                              umumiy_counter[df['Артикул'][key]+'-7'] += 1
                              max_values7 = umumiy_counter[df['Артикул'][key]+'-7']
                              materiale = df['Артикул'][key]+"-7{:03d}".format(max_values7)
                              AluminiyProduct(artikul = df['Артикул'][key],section ='7',counter=max_values7,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key],material=materiale).save()
                              df_new['SAP код 7'][key] = materiale
                              
                              component2 = materiale.split('-')[0]
                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid =aluprofiles.data['Полый и Фасонный']

                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                              
                              
                              surface_treatment_export=''
                              if row['Тип покрытия'].lower() =='неокрашенный':
                                    surface_treatment_export ='Неокрашенный'
                              elif ((row['Тип покрытия'].lower() =='окрашенный') or (row['Тип покрытия'].lower() =='белый')):
                                    surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']] +' ' +row['Код краски снаружи']
                              elif row['Тип покрытия'].lower() =='сублимированный':
                                    surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                              elif row['Тип покрытия'].lower() =='анодированный':
                                    surface_treatment_export = row['Код цвета анодировки снаружи']
                              elif row['Тип покрытия'].lower() =='ламинированный':
                                    if (row['Цвет лам пленки снаружи']=='XXXX' or row['Цвет лам пленки снаружи']=='nan'):
                                          surface_treatment_export = svet_lam_plenke_VN[row['Цвет лам пленки внутри']]                  
                                    else:
                                          if (row['Цвет лам пленки внутри']=='XXXX' or row['Цвет лам пленки внутри']=='nan'):
                                                surface_treatment_export = svet_lam_plenke_NA[row['Цвет лам пленки снаружи']] 
                                          else:
                                                surface_treatment_export = svet_lam_plenke_POL[row['Цвет лам пленки снаружи']]
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['U-Упаковка + Готовая Продукция'][key],
                                                'section':'U-Упаковка + Готовая продукция',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':row['Тип покрытия'],
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ГП',
                                                'hollow_and_solid':hollow_and_solid,
                                                'export_description':export_description,
                                                'export_description_eng':export_description_eng.bux_name_eng,
                                                'tnved':export_description_eng.tnved,
                                                'surface_treatment_export':surface_treatment_export,# GP da kerak
                                                 'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'group_prise': export_description_eng.group_price,
                                                'nazvaniye_export':export_name,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
                        
                        else:
                              materiale = df['Артикул'][key]+"-7{:03d}".format(1)
                              AluminiyProduct(artikul = df['Артикул'][key],section ='7',counter=1,gruppa_materialov='ALUGP',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['U-Упаковка + Готовая Продукция'][key],material=materiale).save()
                              df_new['SAP код 7'][key] = materiale
                              umumiy_counter[df['Артикул'][key]+'-7'] = 1
                             
                              component2 = materiale.split('-')[0]
                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid =aluprofiles.data['Полый и Фасонный']

                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                              
                              
                              surface_treatment_export=''
                              if row['Тип покрытия'].lower() =='неокрашенный':
                                    surface_treatment_export ='Неокрашенный'
                              elif ((row['Тип покрытия'].lower() =='окрашенный') or (row['Тип покрытия'].lower() =='белый')):
                                    surface_treatment_export = brand_kraski_snaruji_ABC[row['Бренд краски снаружи']] + ' ' + row['Код краски снаружи']
                              elif row['Тип покрытия'].lower() =='сублимированный':
                                    surface_treatment_export = kod_dekorativ_snaruji_ABC[row['Код декор пленки снаружи']]
                              elif row['Тип покрытия'].lower() =='анодированный':
                                    surface_treatment_export = row['Код цвета анодировки снаружи']
                              elif row['Тип покрытия'].lower() =='ламинированный':
                                    if (row['Цвет лам пленки снаружи']=='XXXX' or row['Цвет лам пленки снаружи']=='nan'):
                                          surface_treatment_export = svet_lam_plenke_VN[row['Цвет лам пленки внутри']]                  
                                    else:
                                          if (row['Цвет лам пленки внутри']=='XXXX' or row['Цвет лам пленки внутри']=='nan'):
                                                surface_treatment_export = svet_lam_plenke_NA[row['Цвет лам пленки снаружи']] 
                                          else:
                                                surface_treatment_export = svet_lam_plenke_POL[row['Цвет лам пленки снаружи']]
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['U-Упаковка + Готовая Продукция'][key],
                                                'section':'U-Упаковка + Готовая продукция',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':row['Тип покрытия'],
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ГП',
                                                'hollow_and_solid':hollow_and_solid,
                                                'export_description':export_description,
                                                'export_description_eng':export_description_eng.bux_name_eng,
                                                'tnved':export_description_eng.tnved,
                                                'surface_treatment_export':surface_treatment_export,# GP da kerak
                                                'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'group_prise': export_description_eng.group_price,
                                                'nazvaniye_export':export_name,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
                        
                  ##### kombirinovanniy
            
                   
            
            if df['Тип покрытия'][key] == 'Ламинированный':      
                  if AluminiyProduct.objects.filter(artikul =component,section ='L',kratkiy_tekst_materiala=df_new['Ламинация'][key]).exists():
                        df_new['SAP код L'][key] = AluminiyProduct.objects.filter(artikul =component,section ='L',kratkiy_tekst_materiala=df_new['Ламинация'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код L'][key],df_new['Ламинация'][key],'L'])
                  else: 
                        if AluminiyProduct.objects.filter(artikul =component,section ='L').exists():
                              umumiy_counter[component+'-L'] += 1
                              max_valuesL = umumiy_counter[ component +'-L']
                              materiale = component+"-L{:03d}".format(max_valuesL)
                              AluminiyProduct(artikul =component,section ='L',counter=max_valuesL,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Ламинация'][key],material=materiale).save()
                              df_new['SAP код L'][key]=materiale
                             
                              component2 = materiale.split('-')[0]
                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid = aluprofiles.data['Полый и Фасонный']

                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                              
                              
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Ламинация'][key],
                                                'section':'L-Ламинирование',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':row['Тип покрытия'],
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':'',
                                                'inner_side_wg_s_id':'',
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                 # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'group_prise': export_description_eng.group_price,
                                                'nazvaniye_export':export_name,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
                        else:
                              materiale = df['Артикул'][key]+"-L{:03d}".format(1)
                              AluminiyProduct(artikul =df['Артикул'][key],section ='L',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Ламинация'][key],material=materiale).save()
                              df_new['SAP код L'][key]=materiale
                              umumiy_counter[df['Артикул'][key]+'-L'] = 1
                             
                              component2 = materiale.split('-')[0]
                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid = aluprofiles.data['Полый и Фасонный']

                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                              
                              
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Ламинация'][key],
                                                'section':'L-Ламинирование',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':row['Тип покрытия'],
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':'',
                                                'inner_side_wg_s_id':'',
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'group_prise': export_description_eng.group_price,
                                                'nazvaniye_export':export_name,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
            
            dlina =''
      
            if df['Длина при выходе из пресса'][key] != 'nan' and df['Длина при выходе из пресса'][key].replace('.0','')!= row['Длина (мм)']:
                  dlina = df['Длина при выходе из пресса'][key].replace('.0','')      
            else:
                  dlina = df['Длина (мм)'][key]
                  
                  
            df_new['Экструзия холодная резка'][key] = row['Сплав'][len(row['Сплав'])-2:] +'T4 '+'L'+dlina+' MF'
            if row['тип закаленности']!='T4':
                  df_new['Печь старения'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' MF'
            
            
                        
            if ((row['Тип покрытия'] == 'Окрашенный') or (row['Тип покрытия'] == 'Белый' )):
                  df_new['Покраска автомат'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи']+row['Код краски снаружи']
                  if row['Код наклейки'] != 'NT1':
                        df_new['Наклейка'][key] = df_new['Покраска автомат'][key] +' '+ row['Код наклейки'].replace('.0','')
            
            
                        
            elif row['Тип покрытия'] == 'Ламинированный':
                  df_new['Покраска автомат'][key] = row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи']+row['Код краски снаружи']
                  
            
            elif row['Тип покрытия'] =='Сублимированный':
                  df_new['Покраска автомат'][key]=row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')
                  df_new['Сублимация'][key]=row['Сплав'][len(row['Сплав'])-2:] + row['тип закаленности'] +' L'+dlina+' '+row['Бренд краски снаружи'].replace('.0','')+row['Код краски снаружи'].replace('.0','')+'_'+row['Код декор пленки снаружи'].replace('.0','')
                  
                  if row['Код наклейки'] != 'NT1':
                        df_new['Наклейка'][key]=df_new['Сублимация'][key] + ' ' + row['Код наклейки'].replace('.0','')

            elif row['Тип покрытия'] =='Анодированный':
                  df_new['Анодировка'][key]=row['Сплав'][len(row['Сплав'])-2:] +row['тип закаленности']+' L'+dlina+' '+row['Код цвета анодировки снаружи'].replace('.0','')
                  if row['Код наклейки'] != 'NT1':
                        df_new['Наклейка'][key]= df_new['Анодировка'][key] +' ' + row['Код наклейки'].replace('.0','')
            else:
                  pass
                  
            
            termo_existE =AluminiyProductTermo.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key]).exists()
            simple_existE =AluminiyProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key]).exists()

           
            
            if (termo_existE or simple_existE):
                  if termo_existE:
                        sap_code_e = AluminiyProductTermo.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key])[:1].get().material
                  else:
                        sap_code_e = AluminiyProduct.objects.filter(artikul =component,section ='E',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key])[:1].get().material
                  duplicat_list.append([df_new['SAP код E'][key],df_new['Экструзия холодная резка'][key],'E'])
                  df_new['SAP код E'][key] = sap_code_e

                  if row['тип закаленности']=='T4':
                        exturision_list.append(sap_code_e)
                  # print('sap kodde ee=> ',sap_code_e)
            else:
                  if AluminiyProduct.objects.filter(artikul =component,section ='E').exists():
                        # max_valuesE = AluminiyProduct.objects.filter(artikul =component,section ='E').values('section').annotate(total_max=Max('counter'))[0]['total_max']
                        umumiy_counter[component+'-E'] += 1
                        max_valuesE = umumiy_counter[component+'-E']
                        materiale = component+"-E{:03d}".format(max_valuesE)
                        AluminiyProduct(artikul =component,section ='E',counter=max_valuesE,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key],material=materiale).save()
                        df_new['SAP код E'][key]=materiale
                        
                        if row['тип закаленности']=='T4':
                              exturision_list.append(materiale)

                        component2 = materiale.split('-')[0]
                        aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                        artikle = aluprofiles.data['Артикул']
                        hollow_and_solid = aluprofiles.data['Полый и Фасонный']   

                        if row['Тип покрытия'].lower() == 'сублимированный':
                              tip_poktitiya ='с декоративным покрытием'
                        else:
                              tip_poktitiya = row['Тип покрытия'].lower()
                        
                        export_description = ''
                        if row['Комбинация'].lower() == 'с термомостом':  
                              export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                        else:       
                              export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                      
                        export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                              
                        
                        
                        # print(materiale,'cap koddd')
                              
                        cache_for_cratkiy_text.append(
                                          {'material':materiale,
                                          'kratkiy':df_new['Экструзия холодная резка'][key],
                                          'section':'E-Экструзия холодная резка ZPP2',
                                          'export_customer_id':row['Код заказчика экспорт если експорт'],
                                          'system':row['Название системы'],
                                          'article':artikle,
                                          'length':dlina,
                                          'surface_treatment':'Неокрашенный',
                                          'alloy':row['Сплав'],
                                          'temper':row['тип закаленности'],
                                          'combination':row['Комбинация'],
                                          'outer_side_pc_id': '',#row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                          'outer_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                          'inner_side_pc_id':'',#row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                          'inner_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                          'outer_side_wg_s_id':'',
                                          'inner_side_wg_s_id':'',
                                          'outer_side_wg_id':'',#row['Код лам пленки снаружи'],
                                          'inner_side_wg_id':'',#row['Код лам пленки внутри'],
                                          'anodization_contact':'',#row['Контактность анодировки'],
                                          'anodization_type':'',#row['Тип анодировки'],
                                          'anodization_method':'',#row['Способ анодировки'],
                                          'print_view':'',#row['Код наклейки'],
                                          'profile_base':row['База профилей'],
                                          'width':'1-1000',
                                          'height':'1-1000',
                                          # 'category':row['Название системы'],
                                          'rawmat_type':'ПФ',
                                          # 'hollow_and_solid':hollow_and_solid,
                                          # 'export_description':export_description,
                                          # 'export_description_eng':export_description_eng.bux_name_eng,
                                          # 'tnved':export_description_eng.tnved,
                                          # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                          'wms_width':aluprofiles.data['Ширина'],
                                          'wms_height':aluprofiles.data['Высота'],
                                          'group_prise': export_description_eng.group_price,
                                          'nazvaniye_export':export_name,
                                          'online_savdo_name':online_savdo_name,
                                          }
                                    )
                              
                  else: 
                        materiale = component+"-E{:03d}".format(1)
                        AluminiyProduct(artikul =component,section ='E',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Экструзия холодная резка'][key],material=materiale).save()
                        df_new['SAP код E'][key]=materiale
                        umumiy_counter[component+'-E'] = 1
                        
                        component2 = materiale.split('-')[0]
                        aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                        artikle = aluprofiles.data['Артикул']
                        hollow_and_solid = aluprofiles.data['Полый и Фасонный']
                        if row['Тип покрытия'].lower() == 'сублимированный':
                              tip_poktitiya ='с декоративным покрытием'
                        else:
                              tip_poktitiya = row['Тип покрытия'].lower()
                        
                        export_description = ''
                        if row['Комбинация'].lower() == 'с термомостом':  
                              export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                        else:       
                              export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                        
                        export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                              
                        
                        
                        
                        
                              
                        cache_for_cratkiy_text.append(
                                          {'material':materiale,
                                          'kratkiy':df_new['Экструзия холодная резка'][key],
                                          'section':'E-Экструзия холодная резка ZPP2',
                                          'export_customer_id':row['Код заказчика экспорт если експорт'],
                                          'system':row['Название системы'],
                                          'article':artikle,
                                          'length':dlina,
                                          'surface_treatment':'Неокрашенный',
                                          'alloy':row['Сплав'],
                                          'temper':row['тип закаленности'],
                                          'combination':row['Комбинация'],
                                          'outer_side_pc_id': '',#row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                          'outer_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                          'inner_side_pc_id':'',#row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                          'inner_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                          'outer_side_wg_s_id':'',
                                          'inner_side_wg_s_id':'',
                                          'outer_side_wg_id':'',#row['Код лам пленки снаружи'],
                                          'inner_side_wg_id':'',#row['Код лам пленки внутри'],
                                          'anodization_contact':'',#row['Контактность анодировки'],
                                          'anodization_type':'',#row['Тип анодировки'],
                                          'anodization_method':'',#row['Способ анодировки'],
                                          'print_view':'',#row['Код наклейки'],
                                          'profile_base':row['База профилей'],
                                          'width':'1-1000',
                                          'height':'1-1000',
                                          # 'category':row['Название системы'],
                                          'rawmat_type':'ПФ',
                                          # 'hollow_and_solid':hollow_and_solid,
                                          # 'export_description':export_description,
                                          # 'export_description_eng':export_description_eng.bux_name_eng,
                                          # 'tnved':export_description_eng.tnved,
                                          # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                         'wms_width':aluprofiles.data['Ширина'],
                                          'wms_height':aluprofiles.data['Высота'],
                                          'group_prise': export_description_eng.group_price,
                                          'nazvaniye_export':export_name,
                                          'online_savdo_name':online_savdo_name,
                                          }
                                    )
                        
            termo_existZ =AluminiyProductTermo.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['Печь старения'][key]).exists()
            simple_existZ =AluminiyProduct.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['Печь старения'][key]).exists()
            
            if row['тип закаленности']!='T4':
                  if (termo_existZ or simple_existZ):
                        if termo_existZ:
                              df_new['SAP код Z'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['Печь старения'][key])[:1].get().material
                        else:
                              df_new['SAP код Z'][key] = AluminiyProduct.objects.filter(artikul =component,section ='Z',kratkiy_tekst_materiala=df_new['Печь старения'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код Z'][key],df_new['Печь старения'][key],'Z'])
                  else: 
                        if AluminiyProduct.objects.filter(artikul =component,section ='Z').exists():
                              umumiy_counter[ component +'-Z'] += 1
                              max_valuesZ = umumiy_counter[ component +'-Z']
                              materiale = component+"-Z{:03d}".format(max_valuesZ)
                              AluminiyProduct(artikul =component,section ='Z',counter=max_valuesZ,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Печь старения'][key],material=materiale).save()
                              df_new['SAP код Z'][key]=materiale
                              
                              
                              component2 = materiale.split('-')[0]
                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid = aluprofiles.data['Полый и Фасонный']     
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                              
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Печь старения'][key],
                                                'section':'Z-Печь старения',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':'Неокрашенный',
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id':'',# row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':'',#row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':'',
                                                'inner_side_wg_s_id':'',
                                                'outer_side_wg_id':'',#row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':'',#row['Код лам пленки внутри'],
                                                'anodization_contact':'',#row['Контактность анодировки'],
                                                'anodization_type':'',#row['Тип анодировки'],
                                                'anodization_method':'',#row['Способ анодировки'],
                                                'print_view':'',#row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'nazvaniye_export':export_name,
                                                'group_prise': export_description_eng.group_price,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
                              
                        else:
                              materiale = component+"-Z{:03d}".format(1)
                              AluminiyProduct(artikul =component,section ='Z',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Печь старения'][key],material=materiale).save()
                              df_new['SAP код Z'][key]=materiale
                              umumiy_counter[ component +'-Z'] = 1
                            
                              component2 = materiale.split('-')[0]
                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid = aluprofiles.data['Полый и Фасонный']

                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                                    
                              
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Печь старения'][key],
                                                'section':'Z-Печь старения',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':'Неокрашенный',
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id':'',# row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':'',#row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':'',#brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':'',
                                                'inner_side_wg_s_id':'',
                                                'outer_side_wg_id':'',#row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':'',#row['Код лам пленки внутри'],
                                                'anodization_contact':'',#row['Контактность анодировки'],
                                                'anodization_type':'',#row['Тип анодировки'],
                                                'anodization_method':'',#row['Способ анодировки'],
                                                'print_view':'',#row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'nazvaniye_export':export_name,
                                                'group_prise': export_description_eng.group_price,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
                              
       
            
                        
            if ((row['Тип покрытия'] == 'Сублимированный') or (row['Тип покрытия'] == 'Ламинированный') or (row['Тип покрытия'] == 'Окрашенный') or (row['Тип покрытия'] == 'Белый')): 
                  termo_existP =AluminiyProductTermo.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['Покраска автомат'][key]).exists()
                  simple_existP =AluminiyProduct.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['Покраска автомат'][key]).exists()
                  if (termo_existP or simple_existP):
                        if termo_existP:
                              df_new['SAP код P'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['Покраска автомат'][key])[:1].get().material
                        else:
                              df_new['SAP код P'][key] = AluminiyProduct.objects.filter(artikul =component,section ='P',kratkiy_tekst_materiala=df_new['Покраска автомат'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код P'][key],df_new['Покраска автомат'][key],'P'])
                  else:
                        if '9016' in df_new['Покраска автомат'][key]:
                              tip_pokr ='Белый'
                        else:
                              tip_pokr ='Окрашенный' 
                        if AluminiyProduct.objects.filter(artikul =component,section ='P').exists():
                              umumiy_counter[component+'-P'] += 1
                              
                              max_valuesP = umumiy_counter[ component +'-P']
                              materiale = component+"-P{:03d}".format(max_valuesP)
                              AluminiyProduct(artikul =component,section ='P',counter=max_valuesP,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Покраска автомат'][key],material=materiale).save()
                              df_new['SAP код P'][key]=materiale
                              
                              component2 = materiale.split('-')[0]
                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid = aluprofiles.data['Полый и Фасонный']

                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                              
                              
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Покраска автомат'][key],
                                                'section':'P-Покраска автомат',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':tip_pokr,
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':'',
                                                'inner_side_wg_s_id':'',
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'group_prise': export_description_eng.group_price,
                                                'nazvaniye_export':export_name,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
                              
                              
                        else:
                              materiale = component+"-P{:03d}".format(1)
                              AluminiyProduct(artikul =component,section ='P',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Покраска автомат'][key],material=materiale).save()
                              df_new['SAP код P'][key] = materiale
                              umumiy_counter[component+'-P'] = 1
                              
                              component2 = materiale.split('-')[0]
                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid = aluprofiles.data['Полый и Фасонный']
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                              
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Покраска автомат'][key],
                                                'section':'P-Покраска автомат',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':tip_pokr,
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':'',
                                                'inner_side_wg_s_id':'',
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'group_prise': export_description_eng.group_price,
                                                'nazvaniye_export':export_name,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
                              
            
            
            if row['Тип покрытия'] =='Сублимированный':
                  
                  termo_existS =AluminiyProductTermo.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['Сублимация'][key]).exists()
                  simple_existS =AluminiyProduct.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['Сублимация'][key]).exists()
                  if (termo_existS or simple_existS):
                        if termo_existS: 
                              df_new['SAP код S'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['Сублимация'][key])[:1].get().material
                        else:
                              df_new['SAP код S'][key] = AluminiyProduct.objects.filter(artikul =component,section ='S',kratkiy_tekst_materiala=df_new['Сублимация'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код S'][key],df_new['Сублимация'][key],'S'])
                  else: 
                        if AluminiyProduct.objects.filter(artikul =component,section ='S').exists():
                              umumiy_counter[component+'-S'] += 1
                              max_valuesS = umumiy_counter[ component +'-S']
                              materiale = component+"-S{:03d}".format(max_valuesS)
                              AluminiyProduct(artikul =component,section ='S',counter=max_valuesS,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Сублимация'][key],material=materiale).save()
                              df_new['SAP код S'][key]=materiale
                              
                              component2 = materiale.split('-')[0]
                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid = aluprofiles.data['Полый и Фасонный']
                              
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                              
                              
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Сублимация'][key],
                                                'section':'S-Сублимация',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':'Сублимированный',
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'group_prise': export_description_eng.group_price,
                                                'nazvaniye_export':export_name,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
                              
                        else:
                              materiale = component+"-S{:03d}".format(1)
                              AluminiyProduct(artikul =component,section ='S',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Сублимация'][key],material=materiale).save()
                              df_new['SAP код S'][key]=materiale
                              umumiy_counter[component+'-S'] = 1
                            
                              component2 = materiale.split('-')[0]
                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid = aluprofiles.data['Полый и Фасонный']
                              
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                              
                              
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Сублимация'][key],
                                                'section':'S-Сублимация',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':'Сублимированный',
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':row['Код декор пленки снаружи'],
                                                'inner_side_wg_s_id':row['Код декор пленки внутри'],
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'group_prise': export_description_eng.group_price,
                                                'nazvaniye_export':export_name,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
                              
            
            
                        
            if row['Тип покрытия'] =='Анодированный':
                  termo_existA =AluminiyProductTermo.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['Анодировка'][key]).exists()
                  simple_existA =AluminiyProduct.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['Анодировка'][key]).exists()
                  if (termo_existA or simple_existA):
                        if termo_existA:
                              df_new['SAP код A'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['Анодировка'][key])[:1].get().material
                        else:
                              df_new['SAP код A'][key] = AluminiyProduct.objects.filter(artikul =component,section ='A',kratkiy_tekst_materiala=df_new['Анодировка'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код A'][key],df_new['Анодировка'][key],'A'])
                  
                  else: 
                        if AluminiyProduct.objects.filter(artikul =component,section ='A').exists():
                              umumiy_counter[component+'-A'] += 1
                              max_valuesA = umumiy_counter[ component +'-A']
                              materiale = component+"-A{:03d}".format(max_valuesA)
                              AluminiyProduct(artikul =component,section ='A',counter=max_valuesA,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Анодировка'][key],material=materiale).save()
                              df_new['SAP код A'][key]=materiale
                            
                              component2 = materiale.split('-')[0]
                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid = aluprofiles.data['Полый и Фасонный']
                              
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                              
                              
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Анодировка'][key],
                                                'section':'A-Анодировка',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':'Анодированный',
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':'',
                                                'inner_side_wg_s_id':'',
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':'',#row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'group_prise': export_description_eng.group_price,
                                                'nazvaniye_export':export_name,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
                        else:
                              materiale = component+"-A{:03d}".format(1)
                              AluminiyProduct(artikul =component,section ='A',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Анодировка'][key],material=materiale).save()
                              df_new['SAP код A'][key]=materiale
                              umumiy_counter[component+'-A'] = 1
                             
                              component2 = materiale.split('-')[0]
                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid = aluprofiles.data['Полый и Фасонный']
                              
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                              
                              
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Анодировка'][key],
                                                'section':'A-Анодировка',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':'Анодированный',
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':'',
                                                'inner_side_wg_s_id':'',
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':'',#row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'group_prise': export_description_eng.group_price,
                                                'nazvaniye_export':export_name,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
                              
            
            
                        
            if ((row['Код наклейки'] != 'NT1') and (row['Тип покрытия'] != 'Ламинированный')) :
                  termo_existN =AluminiyProductTermo.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['Наклейка'][key]).exists()
                  simple_existN =AluminiyProduct.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['Наклейка'][key]).exists()
                  if (termo_existN or simple_existN):
                        if termo_existN:
                              df_new['SAP код N'][key] = AluminiyProductTermo.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['Наклейка'][key])[:1].get().material
                        else:
                              df_new['SAP код N'][key] = AluminiyProduct.objects.filter(artikul =component,section ='N',kratkiy_tekst_materiala=df_new['Наклейка'][key])[:1].get().material
                        duplicat_list.append([df_new['SAP код N'][key],df_new['Наклейка'][key],'N'])
                  else:
                        name_tip_pokr =''
                        if (('7777' in df_new['Наклейка'][key]) or ('8888' in df_new['Наклейка'][key])  or ('3701' in df_new['Наклейка'][key]) or ('3702' in df_new['Наклейка'][key])):
                              name_tip_pokr = 'Сублимированный'
                        elif '9016' in df_new['Наклейка'][key]:
                              name_tip_pokr = 'Белый'
                        elif 'MF' in df_new['Наклейка'][key]:
                              name_tip_pokr = 'Неокрашенный'
                        elif anodirovaka_check(ANODIROVKA_CODE,df_new['Наклейка'][key]):
                              name_tip_pokr = 'Анодированный'
                        else:
                              name_tip_pokr = 'Окрашенный'
                        if  AluminiyProduct.objects.filter(artikul =component,section ='N').exists():
                              umumiy_counter[component+'-N'] += 1
                              max_valuesN = umumiy_counter[ component +'-N']
                              materiale = component+"-N{:03d}".format(max_valuesN)
                              AluminiyProduct(artikul =component,section ='N',counter=max_valuesN,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Наклейка'][key],material=materiale).save()
                              df_new['SAP код N'][key]=materiale
                        
                              component2 = materiale.split('-')[0]
                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid = aluprofiles.data['Полый и Фасонный']
                              
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                              
                              
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {
                                                'material':materiale,
                                                'kratkiy':df_new['Наклейка'][key],
                                                'section':'N-Наклейка',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':name_tip_pokr,
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':'',
                                                'inner_side_wg_s_id':'',
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':'',#row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'group_prise': export_description_eng.group_price,
                                                'nazvaniye_export':export_name,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
                        else:
                              materiale = component+"-N{:03d}".format(1)
                              AluminiyProduct(artikul =component,section ='N',counter=1,gruppa_materialov='ALUPF',kombinirovanniy='БЕЗ ТЕРМОМОСТА',kratkiy_tekst_materiala=df_new['Наклейка'][key],material=materiale).save()
                              df_new['SAP код N'][key]=materiale
                              umumiy_counter[component+'-N'] = 1
                             
                              component2 = materiale.split('-')[0]
                              aluprofiles = AluProfilesData.objects.get(Q(data__Артикул=component2)|Q(data__Компонент=component2))
                              artikle = aluprofiles.data['Артикул']
                              hollow_and_solid = aluprofiles.data['Полый и Фасонный']
                              
                              if row['Тип покрытия'].lower() == 'сублимированный':
                                    tip_poktitiya ='с декоративным покрытием'
                              else:
                                    tip_poktitiya = row['Тип покрытия'].lower()
                              
                              export_description = ''
                              if row['Комбинация'].lower() == 'с термомостом':  
                                    export_description ='Термоуплотненный алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              else:       
                                    export_description ='Алюминиевый профиль ' + tip_poktitiya +', ' + hollow_and_solid.lower()
                              
                              export_description_eng = CharUtilsThree.objects.filter(bux_name_rus =export_description)[:1].get()   
                              
                              
                              
                                    
                              cache_for_cratkiy_text.append(
                                                {'material':materiale,
                                                'kratkiy':df_new['Наклейка'][key],
                                                'section':'N-Наклейка',
                                                'export_customer_id':row['Код заказчика экспорт если експорт'],
                                                'system':row['Название системы'],
                                                'article':artikle,
                                                'length':dlina,
                                                'surface_treatment':name_tip_pokr,
                                                'alloy':row['Сплав'],
                                                'temper':row['тип закаленности'],
                                                'combination':row['Комбинация'],
                                                'outer_side_pc_id': row['Код цвета анодировки снаружи'] if row['Тип покрытия']=='Анодированный' else row['Код краски снаружи'],
                                                'outer_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски снаружи']],
                                                'inner_side_pc_id':row['Код цвета анодировки внутри'] if row['Тип покрытия']=='Анодированный' else row['Код краски внутри'],
                                                'inner_side_pc_brand':brand_kraski_snaruji_ABC[row['Бренд краски внутри']],
                                                'outer_side_wg_s_id':'',
                                                'inner_side_wg_s_id':'',
                                                'outer_side_wg_id':row['Код лам пленки снаружи'],
                                                'inner_side_wg_id':row['Код лам пленки внутри'],
                                                'anodization_contact':'',#row['Контактность анодировки'],
                                                'anodization_type':row['Тип анодировки'],
                                                'anodization_method':row['Способ анодировки'],
                                                'print_view':row['Код наклейки'],
                                                'profile_base':row['База профилей'],
                                                'width':'1-1000',
                                                'height':'1-1000',
                                                # 'category':row['Название системы'],
                                                'rawmat_type':'ПФ',
                                                # 'hollow_and_solid':hollow_and_solid,
                                                # 'export_description':export_description,
                                                # 'export_description_eng':export_description_eng.bux_name_eng,
                                                # 'tnved':export_description_eng.tnved,
                                                # 'surface_treatment_export':row['Название системы'],# GP da kerak
                                                'wms_width':aluprofiles.data['Ширина'],
                                                'wms_height':aluprofiles.data['Высота'],
                                                'group_prise': export_description_eng.group_price,
                                                'nazvaniye_export':export_name,
                                                'online_savdo_name':online_savdo_name,
                                                }
                                          )
            
            
      
      
      
      parent_dir ='{MEDIA_ROOT}\\uploads\\aluminiy\\'
       
      if not os.path.isdir(parent_dir):
            create_folder(f'{MEDIA_ROOT}\\uploads\\','aluminiy')
            
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\',f'{year}')
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\',f'{month}')
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\',day)
      create_folder(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\',hour)
      
      
      df_char = create_characteristika(cache_for_cratkiy_text) 
      df_char_title = create_characteristika_utils(cache_for_cratkiy_text)
                 
      
            
      if not os.path.isfile(f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\alumin_new-{minut}.xlsx'):
            path_alu =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\alumin_new-{minut}.xlsx'
            path_ramka_norma =f'uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\norma-{minut}.xlsx'
      else:
            st =random.randint(0,1000)
            path_alu =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\alumin_new-{minut}-{st}.xlsx'
            path_ramka_norma =f'uploads\\aluminiy\\{year}\\{month}\\{day}\\{hour}\\norma-{minut}-{st}.xlsx'
      
      if  len(duplicat_list)>0:     
            df_duplicates =pd.DataFrame(np.array(duplicat_list),columns=['SAP CODE','KRATKIY TEXT','SECTION'])
      else:
            df_duplicates =pd.DataFrame(np.array([['','','']]),columns=['SAP CODE','KRATKIY TEXT','SECTION'])

      df_extrusion = pd.DataFrame({'SAP CODE E' : exturision_list})


      for key,razlov in df_new.iterrows():
            if razlov['SAP код 7']!="":
                  if not RazlovkaObichniy.objects.filter(sap_code7=razlov['SAP код 7'],kratkiy7=razlov['U-Упаковка + Готовая Продукция']).exists():
                        RazlovkaObichniy(
                              esap_code =razlov['SAP код E'],
                              ekratkiy =razlov['Экструзия холодная резка'],
                              zsap_code =razlov['SAP код Z'],
                              zkratkiy =razlov['Печь старения'],
                              psap_code =razlov['SAP код P'],
                              pkratkiy =razlov['Покраска автомат'],
                              ssap_code =razlov['SAP код S'],
                              skratkiy =razlov['Сублимация'],
                              asap_code =razlov['SAP код A'],
                              akratkiy =razlov['Анодировка'],
                              lsap_code =razlov['SAP код L'],
                              lkratkiy =razlov['Ламинация'],
                              nsap_code =razlov['SAP код N'],
                              nkratkiy =razlov['Наклейка'],
                              sap_code7 =razlov['SAP код 7'],
                              kratkiy7 =razlov['U-Упаковка + Готовая Продукция'],
                              fsap_code =razlov['SAP код F'],
                              fkratkiy =razlov['Фабрикация'],
                              sap_code75 =razlov['SAP код 75'],
                              kratkiy75 =razlov['U-Упаковка + Готовая Продукция 75']
                        ).save()
            elif razlov['SAP код 75']!= '':
                  if not RazlovkaObichniy.objects.filter(sap_code75=razlov['SAP код 75'],kratkiy75=razlov['U-Упаковка + Готовая Продукция 75']).exists():
                        RazlovkaObichniy(
                              esap_code =razlov['SAP код E'],
                              ekratkiy =razlov['Экструзия холодная резка'],
                              zsap_code =razlov['SAP код Z'],
                              zkratkiy =razlov['Печь старения'],
                              psap_code =razlov['SAP код P'],
                              pkratkiy =razlov['Покраска автомат'],
                              ssap_code =razlov['SAP код S'],
                              skratkiy =razlov['Сублимация'],
                              asap_code =razlov['SAP код A'],
                              akratkiy =razlov['Анодировка'],
                              lsap_code =razlov['SAP код L'],
                              lkratkiy =razlov['Ламинация'],
                              nsap_code =razlov['SAP код N'],
                              nkratkiy =razlov['Наклейка'],
                              sap_code7 =razlov['SAP код 7'],
                              kratkiy7 =razlov['U-Упаковка + Готовая Продукция'],
                              fsap_code =razlov['SAP код F'],
                              fkratkiy =razlov['Фабрикация'],
                              sap_code75 =razlov['SAP код 75'],
                              kratkiy75 =razlov['U-Упаковка + Готовая Продукция 75']
                        ).save()
      for key,razlov in df_char.iterrows():
            if not Characteristika.objects.filter(sap_code=razlov['SAP CODE'],kratkiy_text=razlov['KRATKIY TEXT']).exists():
                  Characteristika(
                        sap_code =razlov['SAP CODE'],
                        kratkiy_text =razlov['KRATKIY TEXT'],
                        section =razlov['SECTION'],
                        savdo_id =razlov['SAVDO_ID'],
                        savdo_name =razlov['SAVDO_NAME'],
                        export_customer_id =razlov['EXPORT_CUSTOMER_ID'],
                        system =razlov['SYSTEM'],
                        article =razlov['ARTICLE'],
                        length =razlov['LENGTH'],
                        surface_treatment =razlov['SURFACE_TREATMENT'],
                        alloy =razlov['ALLOY'],
                        temper =razlov['TEMPER'],
                        combination =razlov['COMBINATION'],
                        outer_side_pc_id =razlov['OUTER_SIDE_PC_ID'],
                        outer_side_pc_brand =razlov['OUTER_SIDE_PC_BRAND'],
                        inner_side_pc_id =razlov['INNER_SIDE_PC_ID'],
                        inner_side_pc_brand =razlov['INNER_SIDE_PC_BRAND'],
                        outer_side_wg_s_id =razlov['OUTER_SIDE_WG_S_ID'],
                        inner_side_wg_s_id =razlov['INNER_SIDE_WG_S_ID'],
                        outer_side_wg_id =razlov['OUTER_SIDE_WG_ID'],
                        inner_side_wg_id =razlov['INNER_SIDE_WG_ID'],
                        anodization_contact =razlov['ANODIZATION_CONTACT'],
                        anodization_type =razlov['ANODIZATION_TYPE'],
                        anodization_method =razlov['ANODIZATION_METHOD'],
                        print_view =razlov['PRINT_VIEW'],
                        profile_base =razlov['PROFILE_BASE'],
                        width =razlov['WIDTH'],
                        height =razlov['HEIGHT'],
                        category =razlov['CATEGORY'],
                        rawmat_type =razlov['RAWMAT_TYPE'],
                        benkam_id =razlov['BENKAM_ID'],
                        hollow_and_solid =razlov['HOLLOW AND SOLID'],
                        export_description =razlov['EXPORT_DESCRIPTION'],
                        export_description_eng =razlov['EXPORT_DESCRIPTION ENG'],
                        tnved =razlov['TNVED'],
                        surface_treatment_export =razlov['SURFACE_TREATMENT_EXPORT'],
                        wms_width =razlov['WMS_WIDTH'],
                        wms_height =razlov['WMS_HEIGHT'],
                        group_prise =''					
                  ).save()
      for key,razlov in df_char_title.iterrows():
            if not CharacteristicTitle.objects.filter(sap_код_s4p_100 = razlov['SAP код S4P 100']).exists():
                  CharacteristicTitle(
                        дата_изменение_добавление =razlov['Дата изменение добавление'], 
                        статус_изменение_добавление =razlov['Статус изменение добавление'], 
                        ссылки_для_чертежа =razlov['Ссылки для чертежа'], 
                        sap_код_s4p_100 =razlov['SAP код S4P 100'], 
                        нумерация_до_sap =razlov['Нумерация до SAP'], 
                        короткое_название_sap =razlov['Короткое название SAP'], 
                        польное_наименование_sap =razlov['Польное наименование SAP'], 
                        ед_изм =razlov['Ед, Изм,'], 
                        альтернативная_ед_изм =razlov['Альтернативная ед, изм'], 
                        коэфициент_пересчета =razlov['Коэфициент пересчета'], 
                        участок =razlov['Участок'], 
                        альтернативный_участок =razlov['Альтернативный участок'], 
                        длина =razlov['Длина'], 
                        ширина =razlov['Ширина'], 
                        высота =razlov['Высота'], 
                        группа_материалов =razlov['группа материалов'], 
                        удельный_вес_за_метр =razlov['Удельный вес за метр'], 
                        общий_вес_за_штуку =razlov['Общий вес за штуку'],
                        price =razlov['Price']
                  ).save()
      exchange_value = ExchangeValues.objects.get(id=1)
      price_all_correct = True
      # print('#*'*15)
      # print(df_char_title)
      for key, row in df_char_title.iterrows():
            if LengthOfProfile.objects.filter(artikul=row['ch_article'],length=row['Длина']).exists():
                  length_of_profile = LengthOfProfile.objects.filter(artikul=row['ch_article'],length=row['Длина'])[:1].get()
                  df_char_title['Общий вес за штуку'][key] =length_of_profile.ves_za_shtuk
                  df_char_title['Удельный вес за метр'][key] = length_of_profile.ves_za_metr

                  price = Price.objects.filter(tip_pokritiya = row['Тип покрытия'],tip=row['ch_combination'])[:1].get()
                  df_char_title['Price'][key] = float(price.price.replace(',','.')) * float(length_of_profile.ves_za_shtuk.replace(',','.'))  * float(exchange_value.valute.replace(',','.'))
            else:
                  price_all_correct = False



      writer = pd.ExcelWriter(path_alu, engine='xlsxwriter')
      df_new.to_excel(writer,index=False,sheet_name='Schotchik')
      df_char.to_excel(writer,index=False,sheet_name='Characteristika')
      df_char_title.to_excel(writer,index=False,sheet_name='title')
      df_extrusion.to_excel(writer,index=False,sheet_name='T4')
      writer.close()

      del df_new['Название системы']
      del df_new['SAP код A']
      del df_new['Анодировка']
      del df_new['SAP код L']
      del df_new['Ламинация']
      df_new['SAP код K']=''
      df_new['K-Комбинирования']=''

      for key, row in df_new.iterrows():
            if row['SAP код Z'] !='':
                  df_new['SAP код E'][key] = ''
      
      norma_file = df_new.to_excel(f'{MEDIA_ROOT}\\{path_ramka_norma}',index=False)

      order_id = request.GET.get('order_id',None)
      work_type = 1
      if order_id:
            work_type = Order.objects.get(id = order_id).work_type
      
      if price_all_correct and  work_type != 5 :
            path = update_char_title_function(df_char_title,df_extrusion,order_id,'aluminiy')
            files =[File(file=p,filetype='obichniy') for p in path]
            files.append(File(file=path_alu,filetype='obichniy'))
            context ={
                  'files':files,
                  'section':'Формированый обычный файл'
            }

            if order_id:
                  norma_file = NormaExcelFiles(file = path_ramka_norma,type='simple')
                  norma_file.save()
                  file_paths =[ file.file for file in files]
                  order = Order.objects.get(id = order_id)
                  paths = order.paths
                  raz_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                  zip_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                  paths['obichniy_razlovka_file']= file_paths

                  paths['norma_formula_file'] = f'{MEDIA_ROOT}\\{path_ramka_norma}'
                  paths['norma_link'] ='/norma/process-combinirovanniy/' + str(norma_file.id) +f'?type=simple&order_id={order_id}'
                 

                  paths['raz_created_at']= raz_created_at
                  paths['zip_created_at']= zip_created_at
                  paths['status_l']= 'done'
                  paths['status_raz']= 'done'
                  paths['status_zip']= 'done'
                  paths['status_text_l']= 'done'
                  paths['status_norma']= 'on process'
                  order.paths = paths
                  order.aluminiy_worker = request.user
                  order.current_worker = request.user
                  order.work_type = 6
                  order.save()
                  context['order'] = order
                  paths =  order.paths
                  for key,val in paths.items():
                        context[key] = val
                  return render(request,'order/order_detail.html',context)  
      else:
            
            file =[File(file = path_alu,filetype='obichniy')]
            context = {
                  'files':file,
                  'section':'Формированый обычный файл'
            }
            
            if order_id:
                  norma_file = NormaExcelFiles(file = path_ramka_norma,type='simple')
                  norma_file.save()
                  order = Order.objects.get( id = order_id)
                  paths = order.paths 
                  if work_type != 5:
                        context2 ={
                              'obichniy_razlovka_file':[path_alu,path_alu]
                        }
                        paths['obichniy_razlovka_file'] = [path_alu,path_alu]
                  else:
                        path_alu = order.paths['obichniy_razlovka_file']
                        context2 ={
                              'obichniy_razlovka_file':[path_alu,path_alu]
                        }

                  
                  raz_created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                  paths['raz_created_at']= raz_created_at
                  
                  paths['status_l']= 'done'
                  paths['status_raz']= 'done'
                  paths['status_zip']= 'on process'
                  paths['status_text_l']= 'on process'
                  paths['status_norma']= 'on process'
                  paths['status_norma_lack']= 'on process'

                  paths['norma_formula_file'] =  f'{MEDIA_ROOT}\\{path_ramka_norma}'
                  paths['norma_link'] ='/norma/process-combinirovanniy/' + str(norma_file.id) +'?type=simple&order_id='+str(order_id)
                  

                  order.paths = paths
                  order.current_worker = request.user
                  order.work_type = 5
                  order.save()
                  context2['order'] = order
                  paths =  order.paths
                  for key,val in paths.items():
                        context2[key] = val

                  workers = User.objects.filter(role = 'moderator',is_active =True)
                  context2['workers'] = workers

                  return render(request,'order/order_detail.html',context2)


      return render(request,'universal/generated_files.html',context)
                  
import glob

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def razlovka_save(request):
      
      dir_path = f'{MEDIA_ROOT}\\uploads\\aluminiy\\**\*alumin*.*'
      path_list_iyun =[]
      path_list_may =[]
      path_list_aprel =[]
      for file in glob.glob(dir_path, recursive=True):
            if 'June' in file:
                  path_list_iyun.append(file)
            if 'April' in file:
                  path_list_aprel.append(file)
            if 'May' in file:
                  path_list_may.append(file)
            
      # print(path_list_iyun,'\n',path_list_aprel,'\n',path_list_may)
      # print('#'*25)
      path_list_iyun.sort()
      iyun = path_list_iyun[::-1]
      path_list_aprel.sort()
      aprel =path_list_aprel[::-1]
      path_list_may.sort()
      may =path_list_may[::-1]

      for path1 in iyun:
            if 'Копия' in path1:
                  continue
            print(path1)
            df_new = pd.read_excel(path1,sheet_name=['Schotchik','Characteristika','title'])
            df_new['Schotchik'] =df_new['Schotchik'].astype(str)
            df_new['Characteristika'] =df_new['Characteristika'].astype(str)
            df_new['title'] =df_new['title'].astype(str)
            df_new['Schotchik']=df_new['Schotchik'].replace('nan','')
            df_new['Characteristika']=df_new['Characteristika'].replace('nan','')
            df_new['title']=df_new['title'].replace('nan','')
            try:
                  df_new['Schotchik']['SAP код E']=df_new['Schotchik']['SAP код E']
                  esap ='SAP код E'
                  ekrat ='Экструзия холодная резка'
                  zsap ='SAP код Z'
                  zkrat ='Печь старения'
                  psap ='SAP код P'
                  pkrat ='Покраска автомат'
                  ssap ='SAP код S'
                  skrat ='Сублимация'
                  asap ='SAP код A'
                  akrat ='Анодировка'
                  lsap ='SAP код L'
                  lkrat ='Ламинация'
                  nsap ='SAP код N'
                  nkrat ='Наклейка'
                  sap7 ='SAP код 7'

                  try:
                        df_new['Schotchik']['U-Упаковка + Готовая Продукция 7']=df_new['Schotchik']['U-Упаковка + Готовая Продукция 7']
                        df_name ='U-Упаковка + Готовая Продукция 7'
                  except:
                        df_name ='U-Упаковка + Готовая Продукция'
            except:
                  esap ='ekrat_counter'
                  ekrat ='ekrat'
                  zsap ='zkrat_counter'
                  zkrat ='zkrat'
                  psap ='pkrat_counter'
                  pkrat ='pkrat'
                  ssap ='skrat_counter'
                  skrat ='skrat'
                  asap ='akrat_counter'
                  akrat ='akrat'
                  lsap ='lkrat_counter'
                  lkrat ='lkrat'
                  nsap ='nkrat_counter'
                  nkrat ='nkrat'
                  sap7 ='ukrat1_counter'
                  df_name='ukrat1'
            
                  

            for key,razlov in df_new['Schotchik'].iterrows():
                  if not RazlovkaObichniy.objects.filter(sap_code7=razlov[sap7],kratkiy7=razlov[df_name]).exists():
                        RazlovkaObichniy(
                              esap_code =razlov[esap],
                              ekratkiy =razlov[ekrat],
                              zsap_code =razlov[zsap],
                              zkratkiy =razlov[zkrat],
                              psap_code =razlov[psap],
                              pkratkiy =razlov[pkrat],
                              ssap_code =razlov[ssap],
                              skratkiy =razlov[skrat],
                              asap_code =razlov[asap],
                              akratkiy =razlov[akrat],
                              lsap_code =razlov[lsap],
                              lkratkiy =razlov[lkrat],
                              nsap_code =razlov[nsap],
                              nkratkiy =razlov[nkrat],
                              sap_code7 =razlov[sap7],
                              kratkiy7 =razlov[df_name]
                        ).save()
            for key,razlov in df_new['Characteristika'].iterrows():
                  if not Characteristika.objects.filter(sap_code=razlov['SAP CODE'],kratkiy_text=razlov['KRATKIY TEXT']).exists():
                        Characteristika(
                              sap_code =razlov['SAP CODE'],
                              kratkiy_text =razlov['KRATKIY TEXT'],
                              section =razlov['SECTION'],
                              savdo_id =razlov['SAVDO_ID'],
                              savdo_name =razlov['SAVDO_NAME'],
                              export_customer_id =razlov['EXPORT_CUSTOMER_ID'],
                              system =razlov['SYSTEM'],
                              article =razlov['ARTICLE'],
                              length =razlov['LENGTH'],
                              surface_treatment =razlov['SURFACE_TREATMENT'],
                              alloy =razlov['ALLOY'],
                              temper =razlov['TEMPER'],
                              combination =razlov['COMBINATION'],
                              outer_side_pc_id =razlov['OUTER_SIDE_PC_ID'],
                              outer_side_pc_brand =razlov['OUTER_SIDE_PC_BRAND'],
                              inner_side_pc_id =razlov['INNER_SIDE_PC_ID'],
                              inner_side_pc_brand =razlov['INNER_SIDE_PC_BRAND'],
                              outer_side_wg_s_id =razlov['OUTER_SIDE_WG_S_ID'],
                              inner_side_wg_s_id =razlov['INNER_SIDE_WG_S_ID'],
                              outer_side_wg_id =razlov['OUTER_SIDE_WG_ID'],
                              inner_side_wg_id =razlov['INNER_SIDE_WG_ID'],
                              anodization_contact =razlov['ANODIZATION_CONTACT'],
                              anodization_type =razlov['ANODIZATION_TYPE'],
                              anodization_method =razlov['ANODIZATION_METHOD'],
                              print_view =razlov['PRINT_VIEW'],
                              profile_base =razlov['PROFILE_BASE'],
                              width =razlov['WIDTH'],
                              height =razlov['HEIGHT'],
                              category =razlov['CATEGORY'],
                              rawmat_type =razlov['RAWMAT_TYPE'],
                              benkam_id =razlov['BENKAM_ID'],
                              hollow_and_solid =razlov['HOLLOW AND SOLID'],
                              export_description =razlov['EXPORT_DESCRIPTION'],
                              export_description_eng =razlov['EXPORT_DESCRIPTION ENG'],
                              tnved =razlov['TNVED'],
                              surface_treatment_export =razlov['SURFACE_TREATMENT_EXPORT'],
                              wms_width =razlov['WMS_WIDTH'],
                              wms_height =razlov['WMS_HEIGHT'],
                              group_prise =''					
                        ).save()
            for key,razlov in df_new['title'].iterrows():
                  if not CharacteristicTitle.objects.filter(sap_код_s4p_100 = razlov['SAP код S4P 100']).exists():
                        CharacteristicTitle(
                              дата_изменение_добавление =razlov['Дата изменение добавление'], 
                              статус_изменение_добавление =razlov['Статус изменение добавление'], 
                              ссылки_для_чертежа =razlov['Ссылки для чертежа'], 
                              sap_код_s4p_100 =razlov['SAP код S4P 100'], 
                              нумерация_до_sap =razlov['Нумерация до SAP'], 
                              короткое_название_sap =razlov['Короткое название SAP'], 
                              польное_наименование_sap =razlov['Польное наименование SAP'], 
                              ед_изм =razlov['Ед, Изм,'], 
                              альтернативная_ед_изм =razlov['Альтернативная ед, изм'], 
                              коэфициент_пересчета =razlov['Коэфициент пересчета'], 
                              участок =razlov['Участок'], 
                              альтернативный_участок =razlov['Альтернативный участок'], 
                              длина =razlov['Длина'], 
                              ширина =razlov['Ширина'], 
                              высота =razlov['Высота'], 
                              группа_материалов =razlov['группа материалов'], 
                              удельный_вес_за_метр =razlov['Удельный вес за метр'], 
                              общий_вес_за_штуку =razlov['Общий вес за штуку'],
                              price =razlov['Price']
                        ).save()
      
      return JsonResponse({'a':'b'})


      
@csrf_exempt
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def artikul_component(request):
      data = request.POST.get('data',None)
      datas = json.loads(data)
      if data:
            for dat in datas:
                  if AluProfilesData.objects.filter(Q(data__Артикул=dat['Артикул'])&Q(data__Компонент=dat['Компонент'])).exists():
                        baza = AluProfilesData.objects.filter(Q(data__Артикул=dat['Артикул'])&Q(data__Компонент=dat['Компонент']))[:1].get()
                        baza.data = dat
                        baza.save()
                  else:
                        baza = AluProfilesData(data =dat)
                        baza.save()
            return JsonResponse({'saved':True})
      return JsonResponse({'saved':False})
      
      
@csrf_exempt
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def excel_does_not_exists_add(request):
      now = datetime.now()
      year =now.strftime("%Y")
      
      path_not_exists =f'{MEDIA_ROOT}\\uploads\\aluminiy\\{year}\\Not Exists\\Not_Exists.xlsx'
      all_correct = True
      df = pd.read_excel(path_not_exists,sheet_name=['character utils one','character utils two','baza profile','artikul component'])
      # print(df['a
            
      
      return JsonResponse({'saved':all_correct})
 

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def duplicate_correct(request):
      df = pd.read_excel(f'{MEDIA_ROOT}\\example.xlsx')
      for key,row in df.iterrows():
            simple = AluminiyProduct.objects.filter(material =row['material'])
            for sim in simple:
                  sim.kratkiy_tekst_materiala =row['kratkiy_tekst_materiala']
                  sim.save()
                  
            termo = AluminiyProductTermo.objects.filter(material =row['material'])
            for ter in termo:
                  ter.kratkiy_tekst_materiala =row['kratkiy_tekst_materiala']
                  ter.save()
                  
      return JsonResponse({'a':'b'})




@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def show_list_simple_sapcodes(request):
      search =request.GET.get('search',None)
      if search:
            try:
                  try:
                        f_date = datetime.strptime(search,'%d-%m-%Y %H:%M')
                        products = AluminiyProduct.objects.filter(
                              created_at__year =f_date.year,
                              created_at__month =f_date.month,
                              created_at__day =f_date.day,
                              created_at__hour =f_date.hour,
                              created_at__minute =f_date.minute
                        )
                  except:
                        f_date = datetime.strptime(search,'%d-%m-%Y')
                        products = AluminiyProduct.objects.filter(
                              created_at__year =f_date.year,
                              created_at__month =f_date.month,
                              created_at__day =f_date.day
                        )
                  
            except:
                  products = AluminiyProduct.objects.filter(
                        Q(material__icontains=search)
                        |Q(artikul__icontains=search)
                        |Q(section__icontains=search)
                        |Q(gruppa_materialov__icontains=search)
                        |Q(kratkiy_tekst_materiala__icontains=search)
                        |Q(kombinirovanniy__icontains=search)
                        ).order_by('-created_at')
      else:
            products =AluminiyProduct.objects.all().order_by('-created_at')
                  
      paginator = Paginator(products, 25)

      if request.GET.get('page') != None:
            page_number = request.GET.get('page')
      else:
            page_number=1

      page_obj = paginator.get_page(page_number)

      context ={
            'section':'Обычный сапкоды',
            'products':page_obj,
            'search':search,
            'type':'simple'

      }
      return render(request,'universal/show_sapcodes.html',context)


@csrf_exempt
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def delete_sap_code(request,id):
      if request.method =='POST':
            file_type = request.POST.get('type',None)
            if file_type =='simple':
                  sapcode = AluminiyProduct.objects.get(id=id)
                  if Characteristika.objects.filter(sap_code=sapcode.material).exists():
                        character =Characteristika.objects.filter(sap_code=sapcode.material).order_by('-created_at')[:1].get()
                        character.delete()
                  if '-7' in sapcode.material:
                        if RazlovkaObichniy.objects.filter(sap_code7 = sapcode.material).exists():
                              RazlovkaObichniy.objects.get(sap_code7 = sapcode.material).delete()
                  sapcode.delete()
                  
            else:
                  sapcode = AluminiyProductTermo.objects.get(id=id)
                  if Characteristika.objects.filter(sap_code=sapcode.material).exists():
                        character =Characteristika.objects.filter(sap_code=sapcode.material).order_by('-created_at')[:1].get()
                        character.delete()

                  if '-7' in sapcode.material:
                        if RazlovkaTermo.objects.filter(sap_code7 = sapcode.material).exists():
                              termo =RazlovkaTermo.objects.get(sap_code7 = sapcode.material)
                              components =RazlovkaTermo.objects.filter(parent_id =termo.id)
                              components.delete()
                              termo.delete()
                  sapcode.delete()

            return JsonResponse({'msg':True})
      else:
            return JsonResponse({'msg':False})
      
@csrf_exempt
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator']) 
def sap_code_bulk_delete(request):
      if request.method =='POST':
            file_type = request.POST.get('type',None)
            ids = request.POST.get('ids',None)
            if ids:
                  ids = ids.split(',')
                  if file_type =='simple':
                        for id in ids:
                              sapcode = AluminiyProduct.objects.get(id=id)
                              if Characteristika.objects.filter(sap_code=sapcode.material).exists():
                                    character =Characteristika.objects.filter(sap_code=sapcode.material).order_by('-created_at')[:1].get()
                                    character.delete()
                              if '-7' in sapcode.material:
                                    if RazlovkaObichniy.objects.filter(sap_code7 = sapcode.material).exists():
                                          RazlovkaObichniy.objects.get(sap_code7 = sapcode.material).delete()
                              sapcode.delete()
                              
                  else:
                        for id in ids:
                              sapcode = AluminiyProductTermo.objects.get(id=id)
                              if Characteristika.objects.filter(sap_code=sapcode.material).exists():
                                    character =Characteristika.objects.filter(sap_code=sapcode.material).order_by('-created_at')[:1].get()
                                    character.delete()

                              if '-7' in sapcode.material:
                                    if RazlovkaTermo.objects.filter(sap_code7 = sapcode.material).exists():
                                          termo =RazlovkaTermo.objects.get(sap_code7 = sapcode.material)
                                          components =RazlovkaTermo.objects.filter(parent_id =termo.id)
                                          components.delete()
                                          termo.delete()
                              sapcode.delete()

            return JsonResponse({'msg':True})
      else:
            return JsonResponse({'msg':False})