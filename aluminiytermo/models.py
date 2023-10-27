from django.db import models

# Create your models here.

  
class AluminiyProductTermo(models.Model):
  material =models.CharField(max_length=250,blank=True,null=True)
  artikul =models.CharField(max_length=250,blank=True,null=True)
  section =models.CharField(max_length=100,blank=True,null=True)
  counter =models.IntegerField(default=0)
  gruppa_materialov =models.CharField(max_length=250,blank=True,null=True)
  kratkiy_tekst_materiala =models.CharField(max_length=250,blank=True,null=True)
  kombinirovanniy =models.CharField(max_length=250,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)
  


class AluFileTermo(models.Model):
    file =models.FileField(upload_to='uploads/aluminiytermo/downloads/',max_length=500)
    generated =models.BooleanField(default=False)
    file_type =models.CharField(max_length=255,blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class CharacteristikaFile(models.Model):
    file =models.FileField(upload_to='uploads/aluminiytermo/downloads/',max_length=500)
    generated =models.BooleanField(default=False)
    file_type =models.CharField(max_length=255,blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


class Characteristika(models.Model):
    sap_code =models.CharField(max_length=255,blank=True,null=True)
    kratkiy_text =models.CharField(max_length=255,blank=True,null=True)
    section =models.CharField(max_length=255,blank=True,null=True)
    savdo_id =models.CharField(max_length=255,blank=True,null=True)
    savdo_name =models.CharField(max_length=255,blank=True,null=True)
    export_customer_id =models.CharField(max_length=255,blank=True,null=True)
    system =models.CharField(max_length=255,blank=True,null=True)
    article =models.CharField(max_length=255,blank=True,null=True)
    length =models.CharField(max_length=255,blank=True,null=True)
    surface_treatment =models.CharField(max_length=255,blank=True,null=True)
    alloy =models.CharField(max_length=255,blank=True,null=True)
    temper =models.CharField(max_length=255,blank=True,null=True)
    combination =models.CharField(max_length=255,blank=True,null=True)
    outer_side_pc_id =models.CharField(max_length=255,blank=True,null=True)
    outer_side_pc_brand =models.CharField(max_length=255,blank=True,null=True)
    inner_side_pc_id =models.CharField(max_length=255,blank=True,null=True)
    inner_side_pc_brand =models.CharField(max_length=255,blank=True,null=True)
    outer_side_wg_s_id =models.CharField(max_length=255,blank=True,null=True)
    inner_side_wg_s_id =models.CharField(max_length=255,blank=True,null=True)
    outer_side_wg_id =models.CharField(max_length=255,blank=True,null=True)
    inner_side_wg_id =models.CharField(max_length=255,blank=True,null=True)
    anodization_contact =models.CharField(max_length=255,blank=True,null=True)
    anodization_type =models.CharField(max_length=255,blank=True,null=True)
    anodization_method =models.CharField(max_length=255,blank=True,null=True)
    print_view =models.CharField(max_length=255,blank=True,null=True)
    profile_base =models.CharField(max_length=255,blank=True,null=True)
    width =models.CharField(max_length=255,blank=True,null=True)
    height =models.CharField(max_length=255,blank=True,null=True)
    category =models.CharField(max_length=255,blank=True,null=True)
    rawmat_type =models.CharField(max_length=255,blank=True,null=True)
    benkam_id =models.CharField(max_length=255,blank=True,null=True)
    hollow_and_solid =models.CharField(max_length=255,blank=True,null=True)
    export_description =models.CharField(max_length=255,blank=True,null=True)
    export_description_eng =models.CharField(max_length=255,blank=True,null=True)
    tnved =models.CharField(max_length=255,blank=True,null=True)
    surface_treatment_export =models.CharField(max_length=255,blank=True,null=True)
    wms_width =models.CharField(max_length=255,blank=True,null=True)
    wms_height =models.CharField(max_length=255,blank=True,null=True)
    group_prise =models.CharField(max_length=255,blank=True,null=True)  
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


class CharUtilsOne(models.Model):
    матрица =models.CharField(max_length=255,blank=True,null=True) 
    артикул =models.CharField(max_length=255,blank=True,null=True) 
    высота =models.CharField(max_length=255,blank=True,null=True) 
    ширина =models.CharField(max_length=255,blank=True,null=True) 
    высота_ширина =models.CharField(max_length=255,blank=True,null=True) 
    systems =models.CharField(max_length=255,blank=True,null=True) 
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class CharUtilsTwo(models.Model):
    артикул =models.CharField(max_length=255,blank=True,null=True) 
    полый_или_фасонный =models.CharField(max_length=255,blank=True,null=True) 
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    
class CharUtilsThree(models.Model):
    bux_name_rus =models.CharField(max_length=255,blank=True,null=True) 
    bux_name_eng =models.CharField(max_length=255,blank=True,null=True) 
    tnved =models.CharField(max_length=255,blank=True,null=True) 
    group_price =models.CharField(max_length=255,blank=True,null=True) 
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
class CharUtilsFour(models.Model):
    category =models.CharField(max_length=255,blank=True,null=True) 
    type =models.CharField(max_length=255,blank=True,null=True) 
    price_for_1kg_som =models.CharField(max_length=255,blank=True,null=True) 
    price_for_1kg_usd =models.CharField(max_length=255,blank=True,null=True) 
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
class CharacteristicTitle(models.Model):
    дата_изменение_добавление =models.CharField(max_length=255,blank=True,null=True) 
    статус_изменение_добавление =models.CharField(max_length=255,blank=True,null=True) 
    ссылки_для_чертежа =models.CharField(max_length=255,blank=True,null=True) 
    sap_код_s4p_100 =models.CharField(max_length=255,blank=True,null=True) 
    нумерация_до_sap =models.CharField(max_length=255,blank=True,null=True) 
    короткое_название_sap =models.CharField(max_length=255,blank=True,null=True) 
    польное_наименование_sap =models.CharField(max_length=255,blank=True,null=True) 
    ед_изм =models.CharField(max_length=255,blank=True,null=True) 
    альтернативная_ед_изм =models.CharField(max_length=255,blank=True,null=True) 
    коэфициент_пересчета =models.CharField(max_length=255,blank=True,null=True) 
    участок =models.CharField(max_length=255,blank=True,null=True) 
    альтернативный_участок =models.CharField(max_length=255,blank=True,null=True) 
    длина =models.CharField(max_length=255,blank=True,null=True) 
    ширина =models.CharField(max_length=255,blank=True,null=True) 
    высота =models.CharField(max_length=255,blank=True,null=True) 
    группа_материалов =models.CharField(max_length=255,blank=True,null=True) 
    удельный_вес_за_метр =models.CharField(max_length=255,blank=True,null=True) 
    общий_вес_за_штуку =models.CharField(max_length=255,blank=True,null=True)
    price = models.CharField(max_length=255,blank=True,null=True) 
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
class BazaProfiley(models.Model):
    артикул =models.CharField(max_length=255,blank=True,null=True)
    серия =models.CharField(max_length=255,blank=True,null=True)
    старый_код =models.CharField(max_length=255,blank=True,null=True)
    компонент =models.CharField(max_length=255,blank=True,null=True)
    type_combination =models.CharField(max_length=100,blank=True,null=True)
    product_description =models.CharField(max_length=255,blank=True,null=True)
    link = models.CharField(max_length=200,blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    
class NakleykaCode(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)