from django.db import models
from accounts.models import User

# Create your models here.

STATUS_CHOICES =(
     (1,'ON HOLD'),
    (2,'ON PROCESS'),
    (3,'CANCEL'),
    (4,'DONE')
)

WORK_TYPE_CHOICES =(
    (1,'ON HOLD'),
    (2,'SAP CODE CREATING'),
    (3,'SAP CODE CREATING LACKS'),
    (4,'TEXT CREATING'),
    (5,'TEXT CREATING LACKS'),
    (6,'DONE')
)


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

class KraskaFileClient(models.Model):
  file =models.FileField(upload_to='uploads/kraska/downloads/',max_length=500)
  generated =models.BooleanField(default=False)
  file_type =models.CharField(max_length=255,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class SiroKraska(models.Model):
    code = models.CharField(max_length=50,blank=True,null=True)
    artikul = models.CharField(max_length=30,blank=True,null=True)
    sapcode = models.CharField(max_length=50,blank=True,null=True)
    kratkiy = models.CharField(max_length=50,blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
  
class TexcartaFile(models.Model):
  file =models.FileField(upload_to='uploads/kraska/downloads/',max_length=500)
  generated =models.BooleanField(default=False)
  file_type =models.CharField(max_length=255,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class KarkaCode(models.Model):
  name = models.CharField(max_length=10,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class OrderKraska(models.Model):
    title = models.CharField(max_length=150)
    status = models.SmallIntegerField(choices=STATUS_CHOICES,default=1)
    work_type =models.SmallIntegerField(choices=WORK_TYPE_CHOICES,default=1)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    current_worker = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='on_time_worker_kraska')
    worker = models.ForeignKey(User,models.CASCADE,blank=True,null=True,related_name='kraska_work')
    wrongs = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='kraska_work_wrong')
    paths = models.JSONField(null=True,blank=True,default=dict)
    order_type = models.SmallIntegerField(default=1)
    order_name = models.CharField(max_length=50,blank=True,null=True)
    client_order_id = models.CharField(max_length=50,blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


class KraskaSapCode(models.Model):
  material =models.CharField(max_length=250,blank=True,null=True)
  artikul =models.CharField(max_length=250,blank=True,null=True)
  section =models.CharField(max_length=10,blank=True,null=True)
  counter =models.IntegerField(default=0)
  kratkiy_tekst_materiala =models.CharField(max_length=250,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)
