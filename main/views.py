from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import Product,ExcelFiles,ExcelFilesOzmka,OrderDelovoyOtxod
from django.core.paginator import Paginator
from django.http import JsonResponse,HttpResponse,Http404
import re
from django.db.models import Count,Q
from .forms import FileForm
from aluminiy.models import RazlovkaObichniy,RazlovkaTermo
from django.conf import settings  
from config.settings import MEDIA_ROOT
from datetime import datetime
from aluminiytermo.views import File
from aluminiy.utils import download_bs64
from django.contrib import messages
from django.template.defaulttags import register
from .utils import counter_generated_data
import subprocess,sys,os
import json
from aluminiytermo.utils import zip
import requests as rq
from accounts.decorators import unauthenticated_user,allowed_users,admin_only

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')



now = datetime.now()

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def work_wast(request):
  if request.method == 'POST':
    form = FileForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('file_list_org')
  else:
      form =FileForm()
      context ={
        'form':form,
        'section':'Деловой отход'
      }
  return render(request,'universal/main.html',context)



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
      |Q(fsap_code =ozm)
      |Q(fkratkiy =ozm)
      |Q(sap_code75 =ozm)
      |Q(kratkiy75 =ozm)
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
      |Q(fsap_code =ozm)
      |Q(fkratkiy =ozm)
      |Q(sap_code75 =ozm)
      |Q(kratkiy75 =ozm)
      ).order_by('-created_at')[:1].values_list()
      sap_code_exists=True
      if list(razlovkaobichniy)[0] not in obichniy_razlovka:
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
      |Q(fsap_code =ozm)
      |Q(fkratkiy =ozm)
      |Q(sap_code75 =ozm)
      |Q(kratkiy75 =ozm)
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
      |Q(fsap_code =ozm)
      |Q(fkratkiy =ozm)
      |Q(sap_code75 =ozm)
      |Q(kratkiy75 =ozm)
      ).order_by('-created_at')[:1].get()
      id =razlovkatermo.parent_id
      if id == 0:
        if razlovkatermo.id not in sap_exists:
          termo_head =RazlovkaTermo.objects.filter(id=razlovkatermo.id)[:1].values_list()
          components =RazlovkaTermo.objects.filter(parent_id=razlovkatermo.id).values_list()
          
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
    df_termo_1201 = pd.DataFrame(termo_razlovka,columns=['ID','PARENT ID','SAP код E','Экструзия холодная резка','SAP код Z','Печь старения','SAP код P','Покраска автомат','SAP код S','Сублимация','SAP код A','Анодировка','SAP код N','Наклейка','SAP код K','K-Комбинирования','SAP код L','Ламинация','SAP код 7','U-Упаковка + Готовая Продукция','SAP код Ф','Фабрикация','SAP код 75','U-Упаковка + Готовая Продукция 75'])#,'CREATED DATE','UPDATED DATE'
    df_obichniy_1201 = pd.DataFrame(obichniy_razlovka,columns=['ID','SAP код E','Экструзия холодная резка','SAP код Z','Печь старения','SAP код P','Покраска автомат','SAP код S','Сублимация','SAP код A','Анодировка','SAP код L','Ламинация','SAP код N','Наклейка','SAP код 7','U-Упаковка + Готовая Продукция','SAP код Ф','Фабрикация','SAP код 75','U-Упаковка + Готовая Продукция 75'])#,'CREATED DATE','UPDATED DATE'
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

    df_termo_1101 = pd.DataFrame(termo_razlovka1101,zcolumns=['SAP код Z','Печь старения','SAP код P','Покраска автомат','SAP код S','Сублимация','SAP код N','Наклейка','SAP код K','K-Комбинирования','SAP код 7','U-Упаковка + Готовая Продукция'])#,'CREATED DATE','UPDATED DATE'
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
    return [path1201,path1101],[df_termo_1201,df_obichniy_1201,df_yoqlari_1201]
  
  if ((zavod1201 and not zavod1201) or ((not zavod1101) and (not zavod1101))):
    termo_razlovka =[ raz[2:16]+ raz[18:-2] for raz in termo_razlovka]
    obichniy_razlovka =[ raz[1:11]+ raz[13:-2] for raz in obichniy_razlovka]
    df_termo_1201 = pd.DataFrame(termo_razlovka,columns=['SAP код E','Экструзия холодная резка','SAP код Z','Печь старения','SAP код P','Покраска автомат','SAP код S','Сублимация','SAP код A','Анодировка','SAP код N','Наклейка','SAP код K','K-Комбинирования','SAP код 7','U-Упаковка + Готовая Продукция','SAP код F','Фабрикация','SAP код 75','U-Упаковка + Готовая Продукция 75'])#,'CREATED DATE','UPDATED DATE'
    df_obichniy_1201 = pd.DataFrame(obichniy_razlovka,columns=['SAP код E','Экструзия холодная резка','SAP код Z','Печь старения','SAP код P','Покраска автомат','SAP код S','Сублимация','SAP код A','Анодировка','SAP код N','Наклейка','SAP код 7','U-Упаковка + Готовая Продукция','SAP код F','Фабрикация','SAP код 75','U-Упаковка + Готовая Продукция 75'])#,'CREATED DATE','UPDATED DATE'
    df_yoqlari_1201 = pd.DataFrame({'SAP CODE':sap_code_yoqlari})
    now =datetime.now()
    minut =now.strftime('%M-%S')
    path1201 =f'{MEDIA_ROOT}\\uploads\\ozmka\\ozmka1201-{minut}.xlsx'
    writer = pd.ExcelWriter(path1201, engine='xlsxwriter')
    df_termo_1201.to_excel(writer,index=False,sheet_name='TERMO')
    df_obichniy_1201.to_excel(writer,index=False,sheet_name='OBICHNIY')
    df_yoqlari_1201.to_excel(writer,index=False,sheet_name='NOT EXISTS')
    writer.close()
    return [path1201,''],[df_termo_1201,df_obichniy_1201,df_yoqlari_1201]
  
  if zavod1101:
    termo_razlovka1101 =[ ('','') + raz[4:10] + raz[12:16] + raz[18:20] for raz in termo_razlovka]
    obichniy_razlovka1101 =[ raz[1:9] + ('','','','') + raz[15:17] for raz in obichniy_razlovka]
    counter = 0
    obichniy_razlovka1101org = []
    for obichniy in obichniy_razlovka1101:
      if obichniy[2] !='':
        ob =['','']+ list(obichniy[2:])
        obichniy_razlovka1101org.append(ob)
      else:
        obichniy_razlovka1101org.append(obichniy)
      counter += 1

    df_termo_1101 = pd.DataFrame(termo_razlovka1101,columns=['SAP код E','Экструзия холодная резка','SAP код Z','Печь старения','SAP код P','Покраска автомат','SAP код S','Сублимация','SAP код N','Наклейка','SAP код K','K-Комбинирования','SAP код 7','U-Упаковка + Готовая Продукция'])#,'CREATED DATE','UPDATED DATE'
    df_obichniy_1101 = pd.DataFrame(obichniy_razlovka1101org,columns=['SAP код E','Экструзия холодная резка','SAP код Z','Печь старения','SAP код P','Покраска автомат','SAP код S','Сублимация','SAP код N','Наклейка','SAP код K','K-Комбинирования','SAP код 7','U-Упаковка + Готовая Продукция'])#,'CREATED DATE','UPDATED DATE'
    df_yoqlari_1101 = pd.DataFrame({'SAP CODE':sap_code_yoqlari})
    now =datetime.now()
    minut =now.strftime('%M-%S')
    path1101 =f'{MEDIA_ROOT}\\uploads\\ozmka\\ozmka1101-{minut}.xlsx'
    writer = pd.ExcelWriter(path1101, engine='xlsxwriter')
    df_termo_1101.to_excel(writer,index=False,sheet_name='TERMO')
    df_obichniy_1101.to_excel(writer,index=False,sheet_name='OBICHNIY')
    df_yoqlari_1101.to_excel(writer,index=False,sheet_name='NOT EXISTS')
    writer.close()
    return [path1101,''],[df_termo_1101,df_obichniy_1101,df_yoqlari_1101]


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','only_razlovka','user1','razlovka'])
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
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','only_razlovka','user1','razlovka','radiator'])
def index(request):
  return render(request,'index.html')

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','only_razlovka','user1','razlovka'])
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


  # products =products

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','only_razlovka','user1','razlovka'])
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

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator'])
def file_upload_org(request):
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

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','only_razlovka','user1','razlovka'])
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

# def downloading_razlovka(request):
#   res = download_bs64([data,]'CHARACTERISTIKA')
#   return res

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','only_razlovka','user1','razlovka'])
def file_upload_for_get_ozmka_org(request):
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
      path,df = get_ozmka(ozmks,z1101,z1201)
      res = download_bs64(df,'RAZLOVKA')
      if request.user.role =='user1':
        return res
      files = [File(file=p,filetype='simple') for p in path]
      context ={
        'files':files,
        'section':'Разловка'
      }
      return render(request,'universal/generated_files.html',context)
    else:
        return render(request,'norma/razlovka_find_org.html')
  else:
    path1 = request.GET.get('path',None)
    if path1:
      if sys.platform == "win32":
        os.startfile(path1)
      else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])
    return render(request,'norma/razlovka_find_org.html')


    
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','only_razlovka','user1','razlovka'])
def file_list(request):
  files = ExcelFiles.objects.filter(generated =False).order_by('-created_at')
  context ={'files':files}
  return render(request,'file_list.html',context)


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','only_razlovka','user1','razlovka'])
def file_list_org(request):
  files = ExcelFiles.objects.filter(generated =False).order_by('-created_at')
  context ={'files':files}
  return render(request,'delovoy_otxod/file_list.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','only_razlovka','user1','razlovka'])
def file_list_ozmka(request):
  files = ExcelFilesOzmka.objects.filter(generated =False).order_by('-created_at')
  context ={'files':files}
  return render(request,'file_list_ozmka.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','only_razlovka','user1','razlovka'])
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
  


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','only_razlovka','user1','razlovka'])
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


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','only_razlovka','user1','razlovka'])
def download(request, id):
  path =str(ExcelFiles.objects.get(id=id).file)
  file_path = os.path.join(settings.MEDIA_ROOT, path)
  if os.path.exists(file_path):
      with open(file_path, 'rb') as fh:
          response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
          response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
          return response
  raise Http404

group_one =['WDC47','WDT65','WDT78','WDT57','WDT98','SLT65']
group_two =['FST','FSC','PVF','PDF']
group_three =['ALU']
group_four =['PVC']


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
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

  return render(request,'generated_file.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def lenght_generate_org(request,id):
  file = ExcelFiles.objects.get(id=id)
  
  counter =0
  file_path =f'{MEDIA_ROOT}\\{file.file}'
  df_org = pd.read_excel(file_path)
  new_liss = []
  data_type = request.GET.get('type',None)
  for key ,row in df_org.iterrows():
    new = row['Краткий текст материала'].split()
    # print(new)
    if data_type and (data_type =='alu') and int(row['Длина Дел.отхода'])==600:
      new_generated_data =[]
      for i in range(0,len(new)):
        if new[i].startswith('L'):
          nn=new[i].replace('L','')
          lenn=int(nn)
          for j in range(6,10):
            new[i] =f'WL{j*100}'
            s=' '.join(new)
            new_generated_data.append({'sap_del_cod':s,'lenn':int(j*100)})
            counter+=1
      pr={'sena':row['Цена'],'length':lenn,'ves_gp':row['Вес за ШТ'],'kls_color':row['KLS_COLOR'],'kls_inner_color':row['KLS_INNER_COL'],'kls_inner_id':row['KLS_INNER_ID'],'ch_profile_type':row['Гр.мат'][len(row['Гр.мат'])-3:],'id_claes':row['KLAES ID'],'sap_code':row['SAP код'],'sap_code_krat':row['SAP код'].split('-')[0],'text':row['Краткий текст материала'],'dlina_del_otxod':row['Длина Дел.отхода'],'data':new_generated_data}
      new_liss.append(pr)

    else:
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
      pr={'sena':row['Цена'],'length':lenn,'ves_gp':row['Вес за ШТ'],'kls_color':row['KLS_COLOR'],'kls_inner_color':row['KLS_INNER_COL'],'kls_inner_id':row['KLS_INNER_ID'],'ch_profile_type':row['Гр.мат'][len(row['Гр.мат'])-3:],'id_claes':row['KLAES ID'],'sap_code':row['SAP код'],'sap_code_krat':row['SAP код'].split('-')[0],'text':row['Краткий текст материала'],'dlina_del_otxod':row['Длина Дел.отхода'],'data':new_generated_data}
      new_liss.append(pr)
  # print(new_liss)
  file_ids,zip_path  = counter_generated_data(new_liss,data_type)
  # files = ExcelFiles.objects.filter(id__in=file_ids)
  files = [File(file=f'{zip_path}.zip',filetype='delovoy'),]
  zip(zip_path,zip_path)
  data ={
    'excel_file_path':f'{MEDIA_ROOT}/' + str(file.file),
    'zip_file_path':f'{zip_path}.zip',
    'created_at':str(file.created_at)

  }
  # print(data)
  order_delov = OrderDelovoyOtxod(data = data)
  order_delov.save()
  context={
    'files':files,
    'section':'Деловой отход файлы'
  }

  return render(request,'universal/generated_files.html',context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
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
@allowed_users(allowed_roles=['admin','moderator','user1'])
def open_folder_path_in_explorer(request):
  path =request.GET.get('path',None)
  path = os.path.normpath(path)
  open_type = request.GET.get('open_type',None)
  if open_type =='true':
    if os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])
  elif open_type =='false':
    os.startfile(path)

  return JsonResponse({'msg':True})
  

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','moderator','user1'])
def show_list_history(request):
  files =OrderDelovoyOtxod.objects.all().order_by('-created_at')
  context ={
    'files':files
  }
  return render(request,'delovoy_otxod/history.html',context)


@login_required(login_url='/accounts/login/')
@admin_only
def home(request):
  # res = rq.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
  # print(res.json())
  currency ={
    'USD':{'Rate':0,'Diff':0},
    'RUB':{'Rate':0,'Diff':0},
    'EUR':{'Rate':0,'Diff':0},
    'GBP':{'Rate':0,'Diff':0},
  }
  # for r in res.json():
  #   if r['Ccy'] =='USD':
  #     currency['USD'] =r
  #   if r['Ccy'] =='RUB':
  #     currency['RUB'] =r
  #   if r['Ccy'] =='EUR':
  #     currency['EUR'] =r
  #   if r['Ccy'] =='GBP':
  #     currency['GBP'] =r
  
  return render(request,'home.html',{'data':currency})


@register.filter(name='split_text')
def split_text(value):
    txt =str(value)
    if '\\' in txt:
      text = txt.split('\\')[-1]
      if '/' in text:
        text = text.split('/')[-1]
      if  len(text)>15:
        text =text[:6]+'..'+text[-7:]
      return text
    elif '/' in txt:
      text = txt.split('/')[-1]
      if '\\' in text:
        text = text.split('\\')[-1]
      if  len(text)>15:
        text =text[:6]+'..'+text[-7:]
      return text
    else:
      return txt
    
@register.filter(name='get_dynamic_key')
def get_dynamic_key(data, key):
    if data.get(key, "") =='0':
      return ''
    return data.get(key, "") 

@register.filter(name='split_sapcode')
def split_sapcode(value):
    txt =str(value).split('-')[0]
    return txt
    
@register.filter(name='order_number_format')
def order_number_format(value):
  return "A{:05d}".format(value)
  
@register.filter(name='convert_str_date')
def convert_str_date(value):
    print(value)
    return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')



