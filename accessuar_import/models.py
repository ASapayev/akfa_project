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
