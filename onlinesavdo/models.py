from django.db import models


class OnlineSavdoFile(models.Model):
  file =models.FileField(upload_to='uploads/online_savdo/downloads/',max_length=500)
  generated =models.BooleanField(default=False)
  file_type =models.CharField(max_length=255,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class OnlineSavdoOrder(models.Model):
  parent = models.IntegerField(default = 0)
  paths = models.JSONField(null=True,blank=True,default=dict)
  status=models.SmallIntegerField(blank=True,null=True,default=1)
  file_type = models.CharField(max_length=30,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)



class Segment(models.Model):
    segment_name = models.CharField(max_length=150,blank=True,null=True)
    name = models.CharField(max_length=150,blank=True,null=True)
    price = models.CharField(max_length=10,blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class BuxPrice(models.Model):
    name = models.CharField(max_length=150,blank=True,null=True)
    price = models.CharField(max_length=10,blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class Zavod(models.Model):
    name = models.CharField(max_length=150,blank=True,null=True)
    price = models.CharField(max_length=10,blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


class PokritiyaProtsent(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    pokritiya = models.CharField(max_length=50,blank=True,null=True)
    protsent = models.CharField(max_length=10,blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)