from django.shortcuts import render,redirect
from django.http import JsonResponse
import pandas as pd
from .models import ArtikulComponent,AluminiyProduct,AluFile
from .forms import FileForm

# Create your views here.


def artikul_and_companent(request):
  df = pd.read_excel('C:\\OpenServer\\domains\\pandas\\new_komponent.xlsx','Лист1')
  for i in range(0,3750):
    artikul =df['АРТИКУЛ'][i] 
    component =df['КОМПОНЕНТ'][i]
    seria =df['Серия'][i]
    product_des_ru =df['Productdescription-RUS2'][i]
    proverka_artikul2 = df['ПроверкаАртикул2'][i]
    proverkacom2 =df['ПроверкаКомпонент2'][i]
    grupa_materialov= df['Группа материалов'][i]
    grupa_materialov2= df['Группа материалов2'][i]
    artiku_comp =ArtikulComponent(
      artikul = artikul,
      component = component,
      seria =seria,
      product_description_ru =product_des_ru,
      proverka_artikul2 =proverka_artikul2,
      proverka_component2=proverkacom2,
      gruppa_materialov =grupa_materialov,
      gruppa_materialov2 =grupa_materialov2
        )
    artiku_comp.save()
  return JsonResponse({'converted':'a'})

def alu_product_base(request):
  df = pd.read_excel('C:\\OpenServer\\domains\\pandas\\Данные по Алю.XLSX','Sheet1')
  for i in range(0,3750):
    artikul =df['АРТИКУЛ'][i] 
    component =df['КОМПОНЕНТ'][i]
    seria =df['Серия'][i]
    product_des_ru =df['Productdescription-RUS2'][i]
    proverka_artikul2 = df['ПроверкаАртикул2'][i]
    proverkacom2 =df['ПроверкаКомпонент2'][i]
    grupa_materialov= df['Группа материалов'][i]
    grupa_materialov2= df['Группа материалов2'][i]
    artiku_comp =ArtikulComponent(
      artikul = artikul,
      component = component,
      seria =seria,
      product_description_ru =product_des_ru,
      proverka_artikul2 =proverka_artikul2,
      proverka_component2=proverkacom2,
      gruppa_materialov =grupa_materialov,
      gruppa_materialov2 =grupa_materialov2
        )
  #   artiku_comp.save()
  
  print(df['Материал'][63209],df['Материал'][0])
  return JsonResponse({'converted':'a'})

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

def aluminiy_files(request):
  files = AluFile.objects.filter(generated =False)
  context ={'files':files}
  return render(request,'alu_file_list.html',context)

def AluminiyComponent(request):
  df = pd.read_excel('C:\\OpenServer\\domains\\pandas\\Дел. Отход_pro_max.xlsx','sheet')
  for i in range(1,19461):
    sap_code_materials =df['SAP код материала'][i] 
    ktartkiy_tekst_materiala =df['Краткий текст материала'][i]
    ktartkiy_tekst_materiala_split =None
    
    if (isinstance(df['Длина'][i],int) or isinstance(df['Длина'][i],float)):
      dlina = df['Длина'][i]
    else:
      dlinaw =df['Краткий текст материала'][i].split()
      for d in dlinaw:
        if d.startswith('L'):
          dlina1 =d.replace('L','')
          dlina =int(dlina1)
          break
    
    nazvaniye_sistemi = df['Название системы'][i]
    naimenovaniye_materiala_sap_imzo =df['Наименование материала SAP IMZO'][i]
    sap_kod_del_otxod =df['SAP код ДЕЛ.Отход'][i]
    new_sap_kod_del_otxod =df['new'][i]
    kratkiy_tekst_del_otxod =df['Краткий текст ДЕЛ.Отход'][i]
    proverka_duplicat =df['Проверка Дубликат'][i]
    dlina2 =df['Длина2'][i]
    id_klaes =df['ID KLAES'][i]
    vid_materiala =df['Вид материала'][i]
    gruppa_materiala =df['Группа материалов'][i]
    bazavoye_ei =df['Базовая ЕИ'][i]
    sector =df['Сектор'][i]
    sena_za_shtuk =df['Цена за шт'][i]
    sena_za_metr =df['Цена за метр'][i]
    kls_inner_id =df['KLS_INNER ID'][i]
    kls_inner_color =df['KLS_INNER COLOR'][i]
    klaes_description =df['KLAES Description'][i]
    
    product =AluminiyProduct(
      sap_code_materials = sap_code_materials,
      ktartkiy_tekst_materiala =ktartkiy_tekst_materiala,
      ktartkiy_tekst_materiala_split =ktartkiy_tekst_materiala_split,
      dlina = dlina,
      nazvaniye_sistemi = nazvaniye_sistemi,
      naimenovaniye_materiala_sap_imzo =naimenovaniye_materiala_sap_imzo,
      sap_kod_del_otxod =sap_kod_del_otxod,
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
  return render(request,'index.hmtl')