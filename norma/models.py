from django.db import models

# Create your models here.


class Norma(models.Model):
    устаревший = models.CharField(max_length = 255,blank=True,null=True)
    компонент_1 = models.CharField(max_length = 255,blank=True,null=True)
    компонент_2 = models.CharField(max_length = 255,blank=True,null=True)
    компонент_3 = models.CharField(max_length = 255,blank=True,null=True)
    артикул = models.CharField(max_length = 255,blank=True,null=True)
    серия = models.CharField(max_length = 255,blank=True,null=True)
    наименование = models.CharField(max_length = 255,blank=True,null=True)
    внешний_периметр_профиля_мм = models.CharField(max_length = 255,blank=True,null=True)
    площадь_мм21 = models.CharField(max_length = 255,blank=True,null=True)
    площадь_мм22 = models.CharField(max_length = 255,blank=True,null=True)
    удельный_вес_профиля_кг_м = models.CharField(max_length = 255,blank=True,null=True)
    диаметр_описанной_окружности_мм = models.CharField(max_length = 255,blank=True,null=True)
    длина_профиля_м = models.CharField(max_length = 255,blank=True,null=True)
    расчетное_колво_профиля_шт = models.CharField(max_length = 255,blank=True,null=True)
    общий_вес_профиля_кг = models.CharField(max_length = 255,blank=True,null=True)
    алю_сп_6063_рас_спа_на_1000_шт_пр_кг = models.CharField(max_length = 255,blank=True,null=True)
    алю_сплав_6063_при_этом_тех_отхода1 = models.CharField(max_length = 255,blank=True,null=True)
    алю_сплав_6063_при_этом_тех_отхода2 = models.CharField(max_length = 255,blank=True,null=True)
    смазка_для_пресса_кг_графитовая = models.CharField(max_length = 255,blank=True,null=True)
    смазка_для_пресса_кг_пилы_хл_резки_сол = models.CharField(max_length = 255,blank=True,null=True)
    смазка_для_пресса_кг_горячей_резки_сол = models.CharField(max_length = 255,blank=True,null=True)
    смазка_для_пресса_кг_графитовые_плиты = models.CharField(max_length = 255,blank=True,null=True)
    хим_пг_к_окр_politeknik_кг_pol_ac_25p = models.CharField(max_length = 255,blank=True,null=True)
    хим_пг_к_окр_politeknik_кг_alupol_сr_51 = models.CharField(max_length = 255,blank=True,null=True)
    хим_пг_к_окр_politeknik_кг_alupol_ac_52 = models.CharField(max_length = 255,blank=True,null=True)
    пр_краситель_толщина_пк_мкм = models.CharField(max_length = 255,blank=True,null=True)
    порошковый_краситель_рас_кг_на_1000_пр = models.CharField(max_length = 255,blank=True,null=True)
    пр_краситель_при_этом_тех_отхода  = models.CharField(max_length = 255,blank=True,null=True)
    не_нужний = models.CharField(max_length = 255,blank=True,null=True)
    суб_ширина_декор_пленки_мм_зол_дуб = models.CharField(max_length = 255,blank=True,null=True)
    сублимация_расход_на_1000_профиль_м21 = models.CharField(max_length = 255,blank=True,null=True)
    суб_ширина_декор_пленки_мм_3д_313701 = models.CharField(max_length = 255,blank=True,null=True)
    сублимация_расход_на_1000_профиль_м22 = models.CharField(max_length = 255,blank=True,null=True)
    суб_ширина_декор_пленки_мм_дуб_мокко = models.CharField(max_length = 255,blank=True,null=True)
    сублимация_расход_на_1000_профиль_м23 = models.CharField(max_length = 255,blank=True,null=True)
    суб_ширина_декор_пленки_мм_3д_313702 = models.CharField(max_length = 255,blank=True,null=True)
    сублимация_расход_на_1000_профиль_м24 = models.CharField(max_length = 255,blank=True,null=True)
    молярный_скотч_ширина1_мол_скотча_мм = models.CharField(max_length = 255,blank=True,null=True)
    молярный_скотч_рас_на_1000_пр_шт1 = models.CharField(max_length = 255,blank=True,null=True)
    молярный_скотч_ширина2_мол_скотча_мм = models.CharField(max_length = 255,blank=True,null=True)
    молярный_скотч_рас_на_1000_пр_шт2 = models.CharField(max_length = 255,blank=True,null=True)
    термомост_1 = models.CharField(max_length = 255,blank=True,null=True)
    термомост_2 = models.CharField(max_length = 255,blank=True,null=True)
    термомост_3 = models.CharField(max_length = 255,blank=True,null=True)
    термомост_4 = models.CharField(max_length = 255,blank=True,null=True)
    
    ламинация_верх_a_ширина_ленты_мм = models.CharField(max_length = 255,blank=True,null=True)
    лам_верх_a_рас_ленты_на_1000_пр_м2 = models.CharField(max_length = 255,blank=True,null=True)
    ламинация_низ_b_ширина_ленты_мм = models.CharField(max_length = 255,blank=True,null=True)
    лам_низ_b_рас_ленты_на_1000_пр_м2 = models.CharField(max_length = 255,blank=True,null=True)
    
    ламинация_низ_c_ширина_ленты_мм = models.CharField(max_length = 255,blank=True,null=True)
    лам_низ_c_рас_ленты_на_1000_пр_м2 = models.CharField(max_length = 255,blank=True,null=True)
    лам_рас_праймера_на_1000_штук_пр_кг = models.CharField(max_length = 255,blank=True,null=True)
    лам_рас_клея_на_1000_штук_пр_кг = models.CharField(max_length = 255,blank=True,null=True)
    лам_рас_уп_материала_мешок_на_1000_пр = models.CharField(max_length = 255,blank=True,null=True)
    
    
    
    
    
    
    
    заш_пл_кг_м_akfa_верх_ширина_ленты_мм = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_akfa_бк_ст_ширина_ленты_мм = models.CharField(max_length = 255,blank=True,null=True)
    кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_akfa_низ_ширина_ленты_мм = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2 = models.CharField(max_length = 255,blank=True,null=True)
  
    заш_пл_кг_м_retpen_верх_ширина_ленты_мм = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_retpen_бк_ст_ширина_ленты = models.CharField(max_length = 255,blank=True,null=True)
    кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_retpen_низ_ширина_ленты_мм = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_retpen_низ_рас  = models.CharField(max_length = 255,blank=True,null=True)
    
    заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм  = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_benkam_жл_бк_ст_ширина_лн = models.CharField(max_length = 255,blank=True,null=True)
    кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_bn_жл_низ_рас = models.CharField(max_length = 255,blank=True,null=True)
    
    заш_пл_кг_м_голд_вр_ширина_лн_мм = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_голд_бк_ст_ширина_лн_мм = models.CharField(max_length = 255,blank=True,null=True)
    кг_м_голд_вр_и_кг_м_голд_бк_ст_рас = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_голд_низ_ширина_лн_мм = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_голд_низ_рас_лн_на_1000_пр_м2 = models.CharField(max_length = 255,blank=True,null=True)
    
    заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_imzo_akfa_бк_ст_ширина_лн = models.CharField(max_length = 255,blank=True,null=True)
    кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_imzo_ak_низ_рас = models.CharField(max_length = 255,blank=True,null=True)
    
    заш_пл_кг_м_без_бр_вр_ширина_лн_мм = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_без_бр_бк_ст_ширина_лн_мм = models.CharField(max_length = 255,blank=True,null=True)
    кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_без_бр_низ_ширина_лн_мм = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_без_бр_низ_рас = models.CharField(max_length = 255,blank=True,null=True)
    
    заш_пл_кг_м_eng_верх_ширина_ленты_мм = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_eng_бк_ст_ширина_ленты_мм = models.CharField(max_length = 255,blank=True,null=True)
    кг_м_eng_вр_и_кг_м_eng_бк_ст_рас = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_eng_низ_ширина_ленты_мм = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр = models.CharField(max_length = 255,blank=True,null=True)
    
    заш_пл_кг_м_eng_qora_вр_ширина_лн_мм = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_eng_qora_бк_ст_ширина_лн_мм = models.CharField(max_length = 255,blank=True,null=True)
    кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_eng_qora_низ_ширина_ленты = models.CharField(max_length = 255,blank=True,null=True)
    заш_пл_кг_м_eng_qora_низ_рас = models.CharField(max_length = 255,blank=True,null=True)
    уп_пол_лента_ширина_уп_ленты_мм = models.CharField(max_length = 255,blank=True,null=True)
    уп_пол_лн_рас_уп_лн_на_1000_штук_кг = models.CharField(max_length = 255,blank=True,null=True)
    расход_скотча_ширина_скотча_мм = models.CharField(max_length = 255,blank=True,null=True)
    рас_скотча_рас_скотча_на_1000_штук_шт = models.CharField(max_length = 255,blank=True,null=True)
    упаковка_колво_профилей_в_1_пачке = models.CharField(max_length = 255,blank=True,null=True)
    ala7_oddiy_ala8_qora_алю_сплав_6064 = models.CharField(max_length = 255,blank=True,null=True)
    алю_сплав_биллетов_102_178 =models.CharField(max_length = 255,blank=True,null=True)
    бумага_расход_упоковочной_ленты_на_1000_штук_кг =models.CharField(max_length = 255,blank=True,null=True)
    алюминиевый_сплав_6063_при_этом_балвашка = models.CharField(max_length = 255,blank=True,null=True)
    
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
class Nakleyka(models.Model):
    sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
    название = models.CharField(max_length=255,blank=True,null=True)
    еи = models.CharField(max_length=255,blank=True,null=True)
    склад_закупа = models.CharField(max_length=255,blank=True,null=True)
    код_наклейки = models.CharField(max_length=255,blank=True,null=True)
    название_наклейки = models.CharField(max_length=255,blank=True,null=True)
    ширина = models.CharField(max_length=255,blank=True,null=True)
    еи_ширины = models.CharField(max_length=255,blank=True,null=True)
    тип_клея = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Kraska(models.Model):
    sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
    название = models.CharField(max_length=255,blank=True,null=True)
    еи = models.CharField(max_length=255,blank=True,null=True)
    склад_закупа = models.CharField(max_length=255,blank=True,null=True)
    бренд_краски = models.CharField(max_length=255,blank=True,null=True)
    код_краски = models.CharField(max_length=255,blank=True,null=True)
    тип_краски = models.CharField(max_length=255,blank=True,null=True)
    код_краски_в_профилях = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ximikat(models.Model):
    sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
    название = models.CharField(max_length=255,blank=True,null=True)
    еи = models.CharField(max_length=255,blank=True,null=True)
    склад_закупа = models.CharField(max_length=255,blank=True,null=True)
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
    
class Lamplonka(models.Model):
    sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
    название = models.CharField(max_length=255,blank=True,null=True)
    еи = models.CharField(max_length=255,blank=True,null=True)
    склад_закупа = models.CharField(max_length=255,blank=True,null=True)
    код_лам_пленки = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class KleyDlyaLamp(models.Model):
    sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
    название = models.CharField(max_length=255,blank=True,null=True)
    еи = models.CharField(max_length=255,blank=True,null=True)
    склад_закупа = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class AlyuminniysilindrEkstruziya1(models.Model):
    sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
    название = models.CharField(max_length=255,blank=True,null=True)
    еи = models.CharField(max_length=255,blank=True,null=True)
    склад_закупа = models.CharField(max_length=255,blank=True,null=True)
    тип = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class AlyuminniysilindrEkstruziya2(models.Model):
    sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
    название = models.CharField(max_length=255,blank=True,null=True)
    еи = models.CharField(max_length=255,blank=True,null=True)
    склад_закупа = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class TermomostDlyaTermo(models.Model):
    sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
    название = models.CharField(max_length=255,blank=True,null=True)
    еи = models.CharField(max_length=255,blank=True,null=True)
    склад_закупа = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class SiryoDlyaUpakovki(models.Model):
    sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
    название = models.CharField(max_length=255,blank=True,null=True)
    еи = models.CharField(max_length=255,blank=True,null=True)
    склад_закупа = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class ProchiyeSiryoNeno(models.Model):
    sap_code_s4q100 = models.CharField(max_length=255,blank=True,null=True)
    название = models.CharField(max_length=255,blank=True,null=True)
    еи = models.CharField(max_length=255,blank=True,null=True)
    склад_закупа = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class CheckNormaBase(models.Model):
    artikul = models.CharField(max_length=255,blank=True,null=True)
    kratkiytekst = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class NormaExcelFiles(models.Model):
    file =models.FileField(upload_to='uploads/norma/downloads',max_length=500)
    generated =models.BooleanField(default=False)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    
class NormaDontExistInExcell(models.Model):
    artikul = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class KombinirovaniyUtilsInformation(models.Model):
    artikul = models.CharField(max_length=255,blank=True,null=True)
    component1 = models.CharField(max_length=255,blank=True,null=True)
    component2 = models.CharField(max_length=255,blank=True,null=True)
    component3 = models.CharField(max_length=255,blank=True,null=True)
    sap_code1 = models.CharField(max_length=255,blank=True,null=True)
    termal_bridge1 = models.CharField(max_length=255,blank=True,null=True)
    sap_code2 = models.CharField(max_length=255,blank=True,null=True)
    termal_bridge2 = models.CharField(max_length=255,blank=True,null=True)
    sap_code3 = models.CharField(max_length=255,blank=True,null=True)
    termal_bridge3 = models.CharField(max_length=255,blank=True,null=True)
    sap_code4 = models.CharField(max_length=255,blank=True,null=True)
    termal_bridge4 = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Accessuar(models.Model):
    sap_code = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)