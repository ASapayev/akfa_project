from django.db import models

# Create your models here.


class ArtikulComponent(models.Model):
  artikul = models.CharField(max_length=250,blank=True,null=True)
  component =models.CharField(max_length=250,blank=True,null=True)
  seria =models.CharField(max_length=250,blank=True,null=True)
  product_description_ru1 =models.CharField(max_length=250,blank=True,null=True)
  product_description_ru =models.CharField(max_length=250,blank=True,null=True)
  stariy_code_benkam =models.CharField(max_length=10)
  stariy_code_jomiy =models.CharField(max_length=10)
  proverka_artikul2 =models.CharField(max_length=250,blank=True,null=True)
  proverka_component2=models.CharField(max_length=250,blank=True,null=True)
  gruppa_materialov =models.CharField(max_length=250,blank=True,null=True)
  gruppa_materialov2 =models.CharField(max_length=250,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class AluminiyProduct(models.Model):
  artikul =models.CharField(max_length=25,blank=True,null=True)
  dlina =models.FloatField(default=None)
  tip_pokritiya =models.CharField(max_length=100,blank=True,null=True)
  splav =models.CharField(max_length=30,blank=True,null=True)
  tip_zaklepnosti =models.CharField(max_length=15,blank=True,null=True)
  kombinatsiya =models.CharField(max_length=100,blank=True,null=True)
  brend_kraski =models.CharField(max_length=15,blank=True,null=True)
  kod_kraski_narujiya =models.CharField(max_length=50,blank=True,null=True)
  kod_dekor_plenki_snaruji=models.CharField(max_length=50,blank=True,null=True)
  svet_dekor_plyonki_snaruji =models.CharField(max_length=100,blank=True,null=True)
  kod_nakleyki =models.CharField(max_length=25,blank=True,null=True)
  kratkiy_teks_tovara =models.CharField(max_length=250,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)


class AluFile(models.Model):
  file =models.FileField()
  generated =models.BooleanField(default=False)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class AluminiyProductBase(models.Model):
  material =models.CharField(max_length =250)
  material_group =models.CharField(max_length=50)
  ktarkiy_tekst_materiala=models.CharField(max_length=250)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

