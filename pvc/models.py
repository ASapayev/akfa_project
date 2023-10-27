from django.db import models

# Create your models here.


class PVCProduct(models.Model):
  material =models.CharField(max_length=250,blank=True,null=True)
  artikul =models.CharField(max_length=250,blank=True,null=True)
  section =models.CharField(max_length=100,blank=True,null=True)
  counter =models.IntegerField(default=0)
  gruppa_materialov =models.CharField(max_length=250,blank=True,null=True)
  kratkiy_tekst_materiala =models.CharField(max_length= 250,blank = True, null = True)
  created_at =models.DateTimeField(auto_now_add = True)
  updated_at =models.DateTimeField(auto_now = True)

class PVCFile(models.Model):
  file =  models.FileField(upload_to='uploads/pvc/downloads/',max_length=500)
  file_type = models.CharField(max_length=255,blank=True,null=True)
  created_at =  models.DateTimeField(auto_now_add=True)
  updated_at =  models.DateTimeField(auto_now=True)
  

class Characteristika(models.Model):
  sap_code =models.CharField(max_length=255,blank=True,null=True)
  kratkiy =models.CharField(max_length=255,blank=True,null=True)
  system = models.CharField(max_length=255,blank=True,null=True)
  number_of_chambers = models.CharField(max_length=255,blank=True,null=True)
  article = models.CharField(max_length=255,blank=True,null=True)
  profile_type_id = models.CharField(max_length=255,blank=True,null=True)
  length = models.CharField(max_length=255,blank=True,null=True)
  surface_treatment = models.CharField(max_length=255,blank=True,null=True)
  outer_side_pc_id = models.CharField(max_length=255,blank=True,null=True)
  outer_side_wg_id = models.CharField(max_length=255,blank=True,null=True)
  inner_side_wg_id = models.CharField(max_length=255,blank=True,null=True)
  sealer_color = models.CharField(max_length=255,blank=True,null=True)
  print_view = models.CharField(max_length=255,blank=True,null=True)
  width = models.CharField(max_length=255,blank=True,null=True)
  height = models.CharField(max_length=255,blank=True,null=True)
  category = models.CharField(max_length=255,blank=True,null=True)
  material_class = models.CharField(max_length=255,blank=True,null=True)
  rawmat_type = models.CharField(max_length=255,blank=True,null=True)
  tnved = models.CharField(max_length=255,blank=True,null=True)
  surface_treatment_export = models.CharField(max_length=255,blank=True,null=True)
  amount_in_a_package = models.CharField(max_length=255,blank=True,null=True)
  wms_width = models.CharField(max_length=255,blank=True,null=True)
  wms_height = models.CharField(max_length=255,blank=True,null=True)
  product_type = models.CharField(max_length=255,blank=True,null=True)
  profile_type = models.CharField(max_length=255,blank=True,null=True)
  coating_qbic = models.CharField(max_length=255,blank=True,null=True)
  id_savdo = models.CharField(max_length=255,blank=True,null=True)
  online_savdo_name = models.CharField(max_length=255,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class ArtikulKomponentPVC(models.Model):
  artikul = models.CharField(max_length = 50)
  component = models.CharField(max_length = 50)
  component2 = models.CharField(max_length = 50,blank=True,null=True)
  width = models.CharField(max_length = 50,blank=True,null=True)
  height = models.CharField(max_length = 50,blank=True,null=True)
  category = models.CharField(max_length = 50,blank=True,null=True)
  tnved = models.CharField(max_length = 50,blank=True,null=True)
  wms_width = models.CharField(max_length = 50,blank=True,null=True)
  wms_height = models.CharField(max_length = 50,blank=True,null=True)
  product_type = models.CharField(max_length = 50,blank=True,null=True)
  profile_type = models.CharField(max_length = 50,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)


class CameraPvc(models.Model):
  sap_code = models.CharField(max_length = 50,blank=True,null=True)
  coun_of_lam = models.CharField(max_length = 50,blank=True,null=True)
  coun_of_pvc = models.CharField(max_length = 50,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class AbreviaturaLamination(models.Model):
  abreviatura = models.CharField(max_length = 50,blank=True,null=True)
  pokritiya = models.CharField(max_length = 50,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class LengthOfProfilePVC(models.Model):
  artikul = models.CharField(max_length=100)
  length = models.CharField(max_length=150)
  ves_za_shtuk = models.CharField(max_length=150)
  ves_za_metr = models.CharField(max_length=150)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class Price(models.Model):
  tip_pokritiya = models.CharField(max_length=150)
  price = models.CharField(max_length=150)
  zames =  models.CharField(max_length=150,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class CharacteristikaFilePVC(models.Model):
  file =models.FileField(upload_to='uploads/pvc/downloads/',max_length=500)
  generated =models.BooleanField(default=False)
  file_type =models.CharField(max_length=255,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)


class RazlovkaPVX(models.Model):
  esapkode = models.CharField(max_length = 50,blank=True,null=True)
  ekrat = models.CharField(max_length = 50,blank=True,null=True)
  lsapkode = models.CharField(max_length = 50,blank=True,null=True)
  lkrat = models.CharField(max_length = 50,blank=True,null=True)
  sapkode7 = models.CharField(max_length = 50,blank=True,null=True)
  krat7 = models.CharField(max_length = 50,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class BuxgalterskiyNazvaniye(models.Model):
  naz_ru = models.CharField(max_length = 150,blank=True,null=True)
  naz_eng = models.CharField(max_length = 150,blank=True,null=True)
  sb = models.CharField(max_length = 150,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class DliniyText(models.Model):
  sap_code = models.CharField(max_length = 150,blank=True,null=True)
  product_desc = models.CharField(max_length = 150,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)