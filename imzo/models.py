from django.db import models

# Create your models here.

class ExcelFilesImzo(models.Model):
    file =models.FileField(upload_to='uploads/imzo/')
    generated =models.BooleanField(default=False)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
class ImzoBase(models.Model):
    material =models.CharField(max_length=255)
    kratkiytekst =models.CharField(max_length=255)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    