from django.db import models

# Create your models here.


class AccessuarFiles(models.Model):
    file =models.FileField(upload_to='uploads/norma/downloads',max_length=500)
    generated =models.BooleanField(default=False)
    type =models.CharField(max_length=20,default='simple',blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)