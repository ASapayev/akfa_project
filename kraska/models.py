from django.db import models

# Create your models here.


class Norma7(models.Model):
    data = models.JSONField(null=True,blank=True,default=dict)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class KraskaFile(models.Model):
  file =models.FileField(upload_to='uploads/kraska/downloads/',max_length=500)
  generated =models.BooleanField(default=False)
  file_type =models.CharField(max_length=255,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)