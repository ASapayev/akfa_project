from django.db import models

# Create your models here.

class NormaEpdm(models.Model):
    data = models.JSONField(null=True,blank=True,default=dict)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


class SiroEpdm(models.Model):
    kg = models.CharField(max_length=50,blank=True,null=True)
    sapcode = models.CharField(max_length=50,blank=True,null=True)
    kratkiy = models.CharField(max_length=50,blank=True,null=True)
    shop = models.CharField(max_length=50,blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
   

class EpdmFile(models.Model):
  file =models.FileField(upload_to='uploads/epdm/downloads/',max_length=500)
  generated =models.BooleanField(default=False)
  file_type =models.CharField(max_length=255,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class TexcartaFile(models.Model):
  file =models.FileField(upload_to='uploads/epdm/downloads/',max_length=500)
  generated =models.BooleanField(default=False)
  file_type =models.CharField(max_length=255,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)