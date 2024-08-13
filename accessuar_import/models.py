from django.db import models

# Create your models here.

# class AccessuarImportSapcode(models.Model):
#     artiku =  models.CharField(max_length=20,blank=True,null=True)
#     created_at =    models.DateTimeField(auto_now_add=True)
#     updated_at =    models.DateTimeField(auto_now=True)


class GroupProduct(models.Model):
    name =  models.CharField(max_length=50,blank=True,null=True)
    code =  models.CharField(max_length=20,blank=True,null=True)
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)

class Category(models.Model):
    name =  models.CharField(max_length=50,blank=True,null=True)
    code =  models.CharField(max_length=20,blank=True,null=True)
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)

class AccessuarImportSapCode(models.Model):
  material =models.CharField(max_length=25,blank=True,null=True)
  artikul =models.CharField(max_length=20,blank=True,null=True)
  section =models.CharField(max_length=10,blank=True,null=True)
  counter =models.IntegerField(default=0)
  kratkiy_tekst_materiala =models.CharField(max_length=80,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class Characteristika(models.Model):
    data = models.JSONField(null=True,blank=True,default=dict)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
