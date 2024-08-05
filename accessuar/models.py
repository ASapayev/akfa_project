from django.db import models
from accounts.models import User

# Create your models here.


class AccessuarFiles(models.Model):
    file =  models.FileField(upload_to='uploads/norma/downloads',max_length=500)
    generated = models.BooleanField(default=False)
    type =  models.CharField(max_length=20,default='simple',blank=True,null=True)
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)


class Norma(models.Model):
    data = models.JSONField(null=True,blank=True,default=dict)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


class Siryo(models.Model):
    data = models.JSONField(null=True,blank=True,default=dict)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class TexcartaBase(models.Model):
    material =models.CharField(max_length=25)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


class DataForText(models.Model):
    data = models.JSONField(null=True,blank=True,default=dict)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

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

class OrderACS(models.Model):
    title = models.CharField(max_length=150)
    status = models.SmallIntegerField(choices=STATUS_CHOICES,default=1)
    work_type =models.SmallIntegerField(choices=WORK_TYPE_CHOICES,default=1)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    current_worker = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='on_time_worker_acs')
    worker = models.ForeignKey(User,models.CASCADE,blank=True,null=True,related_name='acs_work')
    wrongs = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='acs_work_wrong')
    paths = models.JSONField(null=True,blank=True,default=dict)
    order_type = models.SmallIntegerField(default=1)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class OrderAKP(models.Model):
    title = models.CharField(max_length=150)
    status = models.SmallIntegerField(choices=STATUS_CHOICES,default=1)
    work_type =models.SmallIntegerField(choices=WORK_TYPE_CHOICES,default=1)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    current_worker = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='on_time_worker_akp')
    worker = models.ForeignKey(User,models.CASCADE,blank=True,null=True,related_name='akp_work')
    wrongs = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='akp_work_wrong')
    paths = models.JSONField(null=True,blank=True,default=dict)
    order_type = models.SmallIntegerField(default=1)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class OrderProchiye(models.Model):
    title = models.CharField(max_length=150)
    status = models.SmallIntegerField(choices=STATUS_CHOICES,default=1)
    work_type =models.SmallIntegerField(choices=WORK_TYPE_CHOICES,default=1)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    current_worker = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='on_time_worker_prochiye')
    worker = models.ForeignKey(User,models.CASCADE,blank=True,null=True,related_name='prochiye_work')
    wrongs = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='prochiye_work_wrong')
    paths = models.JSONField(null=True,blank=True,default=dict)
    order_type = models.SmallIntegerField(default=1)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class AccessuarDownloadFile(models.Model):
  file =models.FileField(upload_to='uploads/accessuar/downloads/',max_length=500)
  generated =models.BooleanField(default=False)
  file_type =models.CharField(max_length=255,blank=True,null=True)
  created_at =models.DateTimeField(auto_now_add=True)
  updated_at =models.DateTimeField(auto_now=True)