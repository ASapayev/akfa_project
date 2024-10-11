from django.db import models
from accounts.models import User

# Create your models here.


class Norma(models.Model):
    data = models.JSONField(null=True,blank=True,default=dict)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

# class NormaAurora(models.Model):
#     data = models.JSONField(null=True,blank=True,default=dict)
#     created_at =models.DateTimeField(auto_now_add=True)
#     updated_at =models.DateTimeField(auto_now=True)


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




class ArtikulRadiator(models.Model):
    model_radiator =models.CharField(max_length=100,blank=True,null=True)
    artikul =models.CharField(max_length=20,blank=True,null=True)
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
  
class RazlovkaRadiatorAurora(models.Model):
  es_sap_code =models.CharField(max_length=100,blank=True,null=True)
  es_kratkiy =models.CharField(max_length=150,blank=True,null=True)
  er_sap_code =models.CharField(max_length=100)
  er_kratkiy =models.CharField(max_length=150)
  pk_sap_code =models.CharField(max_length=100)
  pk_kratkiy =models.CharField(max_length=150)
  sap_code7 =models.CharField(max_length=100)
  kratkiy7 =models.CharField(max_length=150)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)


class RadiatorFile(models.Model):
  file =models.FileField(upload_to='uploads/radiator/downloads/',max_length=500)
  generated =models.BooleanField(default=False)
  file_type =models.CharField(max_length=255,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class ProchiyeFile(models.Model):
  file =models.FileField(upload_to='uploads/prochiye/downloads/',max_length=500)
  generated =models.BooleanField(default=False)
  file_type =models.CharField(max_length=255,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

class AkpFile(models.Model):
  file =models.FileField(upload_to='uploads/akp/downloads/',max_length=500)
  generated =models.BooleanField(default=False)
  file_type =models.CharField(max_length=255,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)

STATUS_CHOICES_RADIATOR =(
     (1,'ON HOLD'),
    (2,'ON PROCESS'),
    (3,'CANCEL'),
    (4,'DONE')
)

WORK_TYPE_CHOICES_RADIATOR =(
    (1,'ON HOLD'),
    (2,'SAP CODE CREATING'),
    (3,'SAP CODE CREATING LACKS'),
    (4,'TEXT CREATING'),
    (5,'TEXT CREATING LACKS'),
    (6,'DONE')
)

class OrderRadiator(models.Model):
    title = models.CharField(max_length=150)
    status = models.SmallIntegerField(choices=STATUS_CHOICES_RADIATOR,default=1)
    work_type =models.SmallIntegerField(choices=WORK_TYPE_CHOICES_RADIATOR,default=1)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    current_worker = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='on_time_worker_radiator')
    radiator_worker = models.ForeignKey(User,models.CASCADE,blank=True,null=True,related_name='radiator_work')
    radiator_wrongs = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='radiator_work_wrong')
    paths = models.JSONField(null=True,blank=True,default=dict)
    order_type = models.SmallIntegerField(default=1)
    order_name = models.CharField(max_length=50, blank=True,null=True)
    client_order_id = models.CharField(max_length=50, blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class Characteristika(models.Model):
    data = models.JSONField(null=True,blank=True,default=dict)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
