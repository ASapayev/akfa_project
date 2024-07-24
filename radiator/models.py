from django.db import models

# Create your models here.


class Norma(models.Model):
    data = models.JSONField(null=True,blank=True,default=dict)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


class Siryo(models.Model):
    data = models.JSONField(null=True,blank=True,default=dict)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)



class Korobka(models.Model):
    data = models.JSONField(null=True,blank=True,default=dict)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


class Kraska(models.Model):
    data = models.JSONField(null=True,blank=True,default=dict)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


class TexcartaBase(models.Model):
    material =models.CharField(max_length=25)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class ViFiles(models.Model):
    file =models.FileField(upload_to='uploads/vi/downloads',max_length=500)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


class RadiatorSapCode(models.Model):
  material =models.CharField(max_length=250,blank=True,null=True)
  artikul =models.CharField(max_length=250,blank=True,null=True)
  section =models.CharField(max_length=10,blank=True,null=True)
  counter =models.IntegerField(default=0)
  kratkiy_tekst_materiala =models.CharField(max_length=250,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)


class RazlovkaRadiator(models.Model):
  pr_sap_code =models.CharField(max_length=100)
  pr_kratkiy =models.CharField(max_length=150)
  mo_sap_code =models.CharField(max_length=100)
  mo_kratkiy =models.CharField(max_length=150)
  pm_sap_code =models.CharField(max_length=100)
  pm_kratkiy =models.CharField(max_length=150)
  pk_sap_code =models.CharField(max_length=100)
  pk_kratkiy =models.CharField(max_length=150)
  sap_code7 =models.CharField(max_length=100)
  kratkiy7 =models.CharField(max_length=150)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)
