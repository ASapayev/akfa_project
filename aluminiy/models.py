from django.db import models

# Create your models here.


class ArtikulComponent(models.Model):
  artikul = models.CharField(max_length=250,blank=True,null=True)
  component =models.CharField(max_length=250,blank=True,null=True)
  

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
  file =models.FileField(upload_to='uploads/aluminiy/downloads/',max_length=500)
  generated =models.BooleanField(default=False)
  file_type =models.CharField(max_length=255,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)


  

class RazlovkaObichniy(models.Model):
  esap_code =models.CharField(max_length=100)
  ekratkiy =models.CharField(max_length=150)
  zsap_code =models.CharField(max_length=100)
  zkratkiy =models.CharField(max_length=150)
  psap_code =models.CharField(max_length=100)
  pkratkiy =models.CharField(max_length=150)
  ssap_code =models.CharField(max_length=100)
  skratkiy =models.CharField(max_length=150)
  asap_code =models.CharField(max_length=100)
  akratkiy =models.CharField(max_length=150)
  lsap_code =models.CharField(max_length=100)
  lkratkiy =models.CharField(max_length=150)
  nsap_code =models.CharField(max_length=100)
  nkratkiy =models.CharField(max_length=150)
  sap_code7 =models.CharField(max_length=100)
  kratkiy7 =models.CharField(max_length=150)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class RazlovkaTermo(models.Model):
  parent_id =models.IntegerField(default=0)
  esap_code =models.CharField(max_length=100)
  ekratkiy =models.CharField(max_length=150)
  zsap_code =models.CharField(max_length=100)
  zkratkiy =models.CharField(max_length=150)
  psap_code =models.CharField(max_length=100)
  pkratkiy =models.CharField(max_length=150)
  ssap_code =models.CharField(max_length=100)
  skratkiy =models.CharField(max_length=150)
  asap_code =models.CharField(max_length=100)
  akratkiy =models.CharField(max_length=150)
  nsap_code =models.CharField(max_length=100)
  nkratkiy =models.CharField(max_length=150)
  ksap_code =models.CharField(max_length=100)
  kratkiy =models.CharField(max_length=150)
  lsap_code =models.CharField(max_length=100)
  lkratkiy =models.CharField(max_length=150)
  sap_code7 =models.CharField(max_length=100)
  kratkiy7 =models.CharField(max_length=150)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)
