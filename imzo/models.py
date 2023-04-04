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
    
    
class TexCartaTime(models.Model):
    компонент_1 = models.CharField(max_length = 255,blank=True,null=True)
    компонент_2 = models.CharField(max_length = 255,blank=True,null=True)
    компонент_3 = models.CharField(max_length = 255,blank=True,null=True)
    артикул = models.CharField(max_length = 255,blank=True,null=True)
    пресс_1_линия_буй = models.CharField(max_length = 255,blank=True,null=True)
    закалка_1_печь_буй = models.CharField(max_length = 255,blank=True,null=True)	
    покраска_9016_белый_про_во_в_сутки_буй = models.CharField(max_length = 255,blank=True,null=True)
    покраска_8001_базовый_про_во_в_сутки_буй = models.CharField(max_length = 255,blank=True,null=True)
    покраска_цветной_про_во_в_сутки_буй = models.CharField(max_length = 255,blank=True,null=True)
    вакуум_1_печка_про_во_в_сутки_буй = models.CharField(max_length = 255,blank=True,null=True)
    термо_1_линия_про_во_в_сутки_буй = models.CharField(max_length = 255,blank=True,null=True)
    наклейка_упаковка_1_линия_про_во_в_сутки_буй = models.CharField(max_length = 255,blank=True,null=True)
    ламинат_1_линия_про_во_в_сутки_буй = models.CharField(max_length = 255,blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    