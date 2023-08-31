from django.db import models

# Create your models here.

class ExcelFilesImzo(models.Model):
    file =models.FileField(upload_to='uploads/imzo/downloads',max_length=500)
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
    
    покраска_SKM_белый_про_во_в_сутки_буй = models.CharField(max_length = 255,blank=True,null=True)
    покраска_SAT_базовый_про_во_в_сутки_буй = models.CharField(max_length = 255,blank=True,null=True)
    покраска_горизонтал_про_во_в_сутки_буй = models.CharField(max_length = 255,blank=True,null=True)
    покраска_ручная_про_во_в_сутки_буй = models.CharField(max_length = 255,blank=True,null=True)
    
    вакуум_1_печка_про_во_в_сутки_буй = models.CharField(max_length = 255,blank=True,null=True)
    термо_1_линия_про_во_в_сутки_буй = models.CharField(max_length = 255,blank=True,null=True)
    наклейка_упаковка_1_линия_про_во_в_сутки_буй = models.CharField(max_length = 255,blank=True,null=True)
    ламинат_1_линия_про_во_в_сутки_буй = models.CharField(max_length = 255,blank=True,null=True)
    
    ekstruziya = models.CharField(max_length = 255,blank=True,null=True)
    pila = models.CharField(max_length = 255,blank=True,null=True)
    strayenie = models.CharField(max_length = 255,blank=True,null=True)
    skm_pokras = models.CharField(max_length = 255,blank=True,null=True)
    sat_pokras = models.CharField(max_length = 255,blank=True,null=True)
    gr_pokras = models.CharField(max_length = 255,blank=True,null=True)
    skm_xim = models.CharField(max_length = 255,blank=True,null=True)
    sat_xim = models.CharField(max_length = 255,blank=True,null=True)
    gr_xim = models.CharField(max_length = 255,blank=True,null=True)
    ruchnoy_pokraska = models.CharField(max_length = 255,blank=True,null=True)
    sublimat = models.CharField(max_length = 255,blank=True,null=True)
    nakleyka = models.CharField(max_length = 255,blank=True,null=True)
    kombinirovan = models.CharField(max_length = 255,blank=True,null=True)
    upakovka = models.CharField(max_length = 255,blank=True,null=True)
    lam_nak_upakovka = models.CharField(max_length = 255,blank=True,null=True)
    kom_upakovka = models.CharField(max_length = 255,blank=True,null=True)



    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    