from django.db import models

# Create your models here.


class Norma(models.Model):
    data = models.JSONField(null=True,blank=True,default=dict)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class Termomost(models.Model):
    data = models.JSONField(null=True,blank=True,default=dict)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
class Nakleyka(models.Model):
    sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
    название = models.CharField(max_length=255,blank=True,null=True)
    еи = models.CharField(max_length=255,blank=True,null=True)
    код_наклейки = models.CharField(max_length=255,blank=True,null=True)
    название_наклейки = models.CharField(max_length=255,blank=True,null=True)
    ширина = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Kraska(models.Model):
    sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
    название = models.CharField(max_length=255,blank=True,null=True)
    еи = models.CharField(max_length=255,blank=True,null=True,default='КГ')
    склад_закупа = models.CharField(max_length=255,blank=True,null=True)
    бренд_краски = models.CharField(max_length=255,blank=True,null=True)
    код_краски = models.CharField(max_length=255,blank=True,null=True)
    тип_краски = models.CharField(max_length=255,blank=True,null=True)
    код_краски_в_профилях = models.CharField(max_length=255,blank=True,null=True)
    order = models.IntegerField(blank=True,null=True,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ximikat(models.Model):
    sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
    название = models.CharField(max_length=255,blank=True,null=True)
    еи = models.CharField(max_length=255,blank=True,null=True)
    склад_закупа = models.CharField(max_length=255,blank=True,null=True)
    chemetal7400 =models.SmallIntegerField(default=0)
    alufinish =models.SmallIntegerField(default=0)
    chemetal7406 =models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Anod(models.Model):
    sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
    название = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class SubDekorPlonka(models.Model):
    sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
    название = models.CharField(max_length=255,blank=True,null=True)
    еи = models.CharField(max_length=255,blank=True,null=True)
    склад_закупа = models.CharField(max_length=255,blank=True,null=True)
    код_декор_пленки = models.CharField(max_length=255,blank=True,null=True)
    ширина_декор_пленки_мм = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Skotch(models.Model):
    sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
    название = models.CharField(max_length=255,blank=True,null=True)
    еи = models.CharField(max_length=255,blank=True,null=True)
    склад_закупа = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# class Lamplonka(models.Model):
#     sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
#     название = models.CharField(max_length=255,blank=True,null=True)
#     еи = models.CharField(max_length=255,blank=True,null=True)
#     склад_закупа = models.CharField(max_length=255,blank=True,null=True)
#     код_лам_пленки = models.CharField(max_length=255,blank=True,null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
# class KleyDlyaLamp(models.Model):
#     sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
#     название = models.CharField(max_length=255,blank=True,null=True)
#     еи = models.CharField(max_length=255,blank=True,null=True)
#     склад_закупа = models.CharField(max_length=255,blank=True,null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
class AlyuminniysilindrEkstruziya1(models.Model):
    sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
    название = models.CharField(max_length=255,blank=True,null=True)
    еи = models.CharField(max_length=255,blank=True,null=True)
    склад_закупа = models.CharField(max_length=255,blank=True,null=True)
    тип = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# class AlyuminniysilindrEkstruziya2(models.Model):
#     sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
#     название = models.CharField(max_length=255,blank=True,null=True)
#     еи = models.CharField(max_length=255,blank=True,null=True)
#     склад_закупа = models.CharField(max_length=255,blank=True,null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    

    
# class SiryoDlyaUpakovki(models.Model):
#     sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
#     название = models.CharField(max_length=255,blank=True,null=True)
#     еи = models.CharField(max_length=255,blank=True,null=True)
#     склад_закупа = models.CharField(max_length=255,blank=True,null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
# class ProchiyeSiryoNeno(models.Model):
#     sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
#     название = models.CharField(max_length=255,blank=True,null=True)
#     еи = models.CharField(max_length=255,blank=True,null=True)
#     склад_закупа = models.CharField(max_length=255,blank=True,null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
# class CheckNormaBase(models.Model):
#     artikul = models.CharField(max_length=255,blank=True,null=True)
#     kratkiytekst = models.CharField(max_length=255,blank=True,null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
# class NormaExcelFiles(models.Model):
#     file =models.FileField(upload_to='uploads/norma/downloads',max_length=500)
#     generated =models.BooleanField(default=False)
#     type =models.CharField(max_length=20,default='simple',blank=True,null=True)
#     created_at =models.DateTimeField(auto_now_add=True)
#     updated_at =models.DateTimeField(auto_now=True)

    
    
# class NormaDontExistInExcell(models.Model):
#     artikul = models.CharField(max_length=255,blank=True,null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
    
    
# class Accessuar(models.Model):
#     sap_code = models.CharField(max_length=255,blank=True,null=True)
#     skotch =models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class ZakalkaIskyuchenie(models.Model):
#     sap_code = models.CharField(max_length=255,blank=True,null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class TexcartaBase(models.Model):
    material =models.CharField(max_length=25)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
