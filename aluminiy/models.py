from django.db import models

# Create your models here.


class ArtikulComponent(models.Model):
  artikul = models.CharField(max_length=250,blank=True,null=True)
  component =models.CharField(max_length=250,blank=True,null=True)
  seria =models.CharField(max_length=250,blank=True,null=True)
  product_description_ru1 =models.CharField(max_length=250,blank=True,null=True)
  product_description_ru =models.CharField(max_length=250,blank=True,null=True)
  stariy_code_benkam =models.CharField(max_length=250,blank=True,null=True)
  stariy_code_jomiy =models.CharField(max_length=250,blank=True,null=True)
  proverka_artikul2 =models.CharField(max_length=250,blank=True,null=True)
  proverka_component2=models.CharField(max_length=250,blank=True,null=True)
  gruppa_materialov =models.CharField(max_length=250,blank=True,null=True)
  gruppa_materialov2 =models.CharField(max_length=250,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class AluminiyProduct(models.Model):
  material =models.CharField(max_length=250,blank=True,null=True)
  artikul =models.CharField(max_length=250,blank=True,null=True)
  section =models.CharField(max_length=100,blank=True,null=True)
  counter =models.IntegerField(default=0)
  gruppa_materialov =models.CharField(max_length=250,blank=True,null=True)
  kratkiy_tekst_materiala =models.CharField(max_length=250,blank=True,null=True)
  kombinirovanniy =models.CharField(max_length=250,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)



class AluFile(models.Model):
  file =models.FileField(upload_to='uploads/aluminiy/downloads/')
  generated =models.BooleanField(default=False)
  file_type =models.CharField(max_length=255,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class AluminiyProductBasesimple(models.Model):
  ekstruziya_sap_kod =models.CharField(max_length=255,blank=True,null=True)
  ekstruziya_kratkiy_tekst =models.CharField(max_length=255,blank=True,null=True)
  zakalka_sap_kod =models.CharField(max_length=255,blank=True,null=True)
  zakalka_kratkiy_tekst =models.CharField(max_length=255,blank=True,null=True)
  pokraska_sap_kod =models.CharField(max_length=255,blank=True,null=True)
  pokraska_kratkiy_tekst =models.CharField(max_length=255,blank=True,null=True)
  sublimatsiya_sap_kod =models.CharField(max_length=255,blank=True,null=True)
  sublimatsiya_kratkiy_tekst =models.CharField(max_length=255,blank=True,null=True)
  anodirovka_sap_kod =models.CharField(max_length=255,blank=True,null=True)
  anodirovka_kratkiy_tekst =models.CharField(max_length=255,blank=True,null=True)
  laminatsiya_sap_kod =models.CharField(max_length=255,blank=True,null=True)
  laminatsiya_kratkiy_tekst =models.CharField(max_length=255,blank=True,null=True)
  nakleyka_sap_kod =models.CharField(max_length=255,blank=True,null=True)
  nakleyka_kratkiy_tekst =models.CharField(max_length=255,blank=True,null=True)
  upakovka_sap_kod =models.CharField(max_length=255,blank=True,null=True)
  upakovka_kratkiy_tekst =models.CharField(max_length=255,blank=True,null=True)
  fabrikatsiya_sap_kod =models.CharField(max_length=255,blank=True,null=True)
  fabrikatsiya_kratkiy_tekst =models.CharField(max_length=255,blank=True,null=True)
  upakovka2_sap_kod =models.CharField(max_length=255,blank=True,null=True)
  upakovka2_kratkiy_tekst =models.CharField(max_length=255,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)
  


