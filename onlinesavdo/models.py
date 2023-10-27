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
  file_type = models.CharField(max_length=30,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)