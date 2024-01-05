from django.db import models

# Create your models here.


class Anod(models.Model):
    code_sveta = models.CharField(max_length =50,blank=True,null=True)
    tip_anod = models.CharField(max_length =50,blank=True,null=True)
    sposob_anod = models.CharField(max_length =50,blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)