from django.shortcuts import render,redirect
import pandas as pd
from django.http import JsonResponse
from .models import Norma,Nakleyka,Kraska,Ximikat,SubDekorPlonka,Skotch,Lamplonka,KleyDlyaLamp,AlyuminniysilindrEkstruziya1,AlyuminniysilindrEkstruziya2,TermomostDlyaTermo,SiryoDlyaUpakovki,ProchiyeSiryoNeno,NormaExcelFiles,CheckNormaBase,NormaDontExistInExcell,KombinirovaniyUtilsInformation
from .forms import NormaFileForm
from django.db.models import Q
from config.settings import MEDIA_ROOT
from .utils import excelgenerate,create_csv_file
import os
from datetime import datetime

def index(request):
    return render(request,'norma/index.html')

# Create your views here.
def norma_excel(request):
    df = pd.read_excel('C:\\OpenServer\\domains\\Norma22.xlsx','Общий')
    df =df.astype(str)
    for i in range(0,df.shape[0]):
        устаревший = df["Устаревший"][i]
        компонент_1 = df["КОМПОНЕНТ 1"][i]
        компонент_2 = df["КОМПОНЕНТ 2"][i]
        компонент_3 = df["КОМПОНЕНТ 3"][i]
        артикул = df["АРТИКУЛ"][i]
        серия = df["Серия"][i]
        наименование = df["Наименование"][i]
        внешний_периметр_профиля_мм = df["Внешний периметр профиля__ мм"][i]
        площадь_мм21 = df["Площадь __мм²"][i]
        площадь_мм22 = df["Площадь __мм²"][i]
        удельный_вес_профиля_кг_м = df["Удельный вес профиля кг__м"][i]
        диаметр_описанной_окружности_мм = df["Диаметр описанной окружности__мм"][i]
        длина_профиля_м = df["Длина профиля__м"][i]
        расчетное_колво_профиля_шт = df["Расчетное кол-во профиля__шт"][i]
        общий_вес_профиля_кг = df["Общий вес профиля__кг"][i]
        алю_сп_6063_рас_спа_на_1000_шт_пр_кг = df["Алюминиевый сплав 6063 __ расход сплава на 1000 шт профиля__кг"][i]
        алю_сплав_6063_при_этом_тех_отхода1 = df["Алюминиевый сплав 6063 __ при этом __ тех.отхода1"][i]
        алю_сплав_6063_при_этом_тех_отхода2 = df["Алюминиевый сплав 6063 __ при этом __ тех.отхода2"][i]
        смазка_для_пресса_кг_графитовая = df["Смазка для пресса__кг __ Графитовая"][i]
        смазка_для_пресса_кг_пилы_хл_резки_сол = df["Смазка для пресса__кг __ пилы холодной резки (Солярка)"][i]
        смазка_для_пресса_кг_горячей_резки_сол = df["Смазка для пресса__кг __ горячей резки (Солярка)"][i]
        смазка_для_пресса_кг_графитовые_плиты = df["Смазка для пресса__кг __ графитовые плиты"][i]
        хим_пг_к_окр_politeknik_кг_pol_ac_25p = df["Химикаты (подготовка к окрашиванию)__ POLITEKNIK кг __ POLITOKSAL AC 25P"][i]
        хим_пг_к_окр_politeknik_кг_alupol_сr_51 = df["Химикаты (подготовка к окрашиванию)__ POLITEKNIK кг __ ALUPOL СR 51"][i]
        хим_пг_к_окр_politeknik_кг_alupol_ac_52 = df["Химикаты (подготовка к окрашиванию)__ POLITEKNIK кг __ ALUPOL AC 52"][i]
        пр_краситель_толщина_пк_мкм = df["Порошковый краситель __ толщина покрытия, мкм"][i]
        порошковый_краситель_рас_кг_на_1000_пр = df["Порошковый краситель __ расход __кг на 1000 профилей"][i]
        пр_краситель_при_этом_тех_отхода = df["Порошковый краситель __ при этом __ тех.отхода "][i]
        не_нужний = df["Не нужний"][i]
        суб_ширина_декор_пленки_мм_зол_дуб = df["Сублимация __ ширина декор пленки__мм (Зол.дуб)"][i]
        сублимация_расход_на_1000_профиль_м21 = df["Сублимация __ расход на 1000 профиль__м21"][i]
        суб_ширина_декор_пленки_мм_3д_313701 = df["Сублимация __ ширина декор пленки__мм (3Д 3137-01) "][i]
        сублимация_расход_на_1000_профиль_м22 = df["Сублимация __ расход на 1000 профиль__м22"][i]
        суб_ширина_декор_пленки_мм_дуб_мокко = df["Сублимация __ ширина декор пленки__мм (Дуб.мокко) "][i]
        сублимация_расход_на_1000_профиль_м23 = df["Сублимация __ расход на 1000 профиль__м23"][i]
        суб_ширина_декор_пленки_мм_3д_313702 = df["Сублимация __ ширина декор пленки__мм (3Д 3137-02) "][i]
        сублимация_расход_на_1000_профиль_м24 = df["Сублимация __ расход на 1000 профиль__м24"][i]
        молярный_скотч_ширина1_мол_скотча_мм = df["Молярный скотч __ ширина1мол- скотча__мм"][i]
        молярный_скотч_рас_на_1000_пр_шт1 = df["Молярный скотч __ расход на 1000 профиль__шт1"][i]
        молярный_скотч_ширина2_мол_скотча_мм = df["Молярный скотч __ ширина2мол- скотча__мм"][i]
        молярный_скотч_рас_на_1000_пр_шт2 = df["Молярный скотч __ расход на 1000 профиль__шт2"][i]
        термомост_1 = df["Термомост 1"][i]
        термомост_2 = df["Термомост 2"][i]
        термомост_3 = df["Термомост 3"][i]
        термомост_4 = df["Термомост 4"][i]
        ламинация_верх_a_ширина_ленты_мм = df["Ламинация __ верх A __ ширина ленты__мм"][i]
        лам_верх_a_рас_ленты_на_1000_пр_м2 = df["Ламинация __ верх A __ расход ленты на 1000 профилей__м²"][i]
        ламинация_низ_b_ширина_ленты_мм = df["Ламинация __ низ B __ ширина ленты__мм"][i]
        лам_низ_b_рас_ленты_на_1000_пр_м2 = df["Ламинация __ низ B __ расход ленты на 1000 профилей__м²"][i]
        ламинация_низ_c_ширина_ленты_мм = df["Ламинация __ низ C __ ширина ленты__мм"][i]
        лам_низ_c_рас_ленты_на_1000_пр_м2 = df["Ламинация __ низ C __ расход ленты на 1000 профилей__м²"][i]
        лам_рас_праймера_на_1000_штук_пр_кг = df["Ламинация __ расход праймера на 1000 штук профилей__кг"][i]
        лам_рас_клея_на_1000_штук_пр_кг = df["Ламинация __ расход клея на 1000 штук профилей__кг"][i]
        лам_рас_уп_материала_мешок_на_1000_пр = df["Ламинация __ Расход упаковочного материала (мешок) на 1000 профилей"][i]
        заш_пл_кг_м_akfa_верх_ширина_ленты_мм = df["Защитная пленка__кг__м Akfa __ верх ширина ленты__мм"][i]
        заш_пл_кг_м_akfa_бк_ст_ширина_ленты_мм = df["Защитная пленка__кг__м Akfa __ (Боковая сторона) ширина ленты__мм"][i]
        кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн = df["Защитная пленка__кг__м Akfa __ верх и Защитная пленка__кг__м Akfa __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i]
        заш_пл_кг_м_akfa_низ_ширина_ленты_мм = df["Защитная пленка__кг__м Akfa __ низ ширина ленты__мм"][i]
        заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2 = df["Защитная пленка__кг__м Akfa __ низ расход ленты на 1000 профиль__м2"][i]
        заш_пл_кг_м_retpen_верх_ширина_ленты_мм = df["Защитная пленка__кг__м RETPEN __ верх ширина ленты__мм"][i]
        заш_пл_кг_м_retpen_бк_ст_ширина_ленты = df["Защитная пленка__кг__м RETPEN __ (Боковая сторона) ширина ленты__мм"][i]
        кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас = df["Защитная пленка__кг__м RETPEN __ верх и Защитная пленка__кг__м RETPEN __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i]
        заш_пл_кг_м_retpen_низ_ширина_ленты_мм = df["Защитная пленка__кг__м RETPEN __ низ ширина ленты__мм"][i]
        заш_пл_кг_м_retpen_низ_рас = df["Защитная пленка__кг__м RETPEN __ низ расход ленты на 1000 профиль__м2"][i]
        заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм = df["Защитная пленка__кг__м BENKAM (желтый) __ верх ширина ленты__мм"][i]
        заш_пл_кг_м_benkam_жл_бк_ст_ширина_лн = df["Защитная пленка__кг__м BENKAM (желтый) __ (Боковая сторона) ширина ленты__мм"][i]
        кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас = df["Защитная пленка__кг__м BENKAM (желтый) __ верх и Защитная пленка__кг__м BENKAM (желтый) __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i]
        заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм = df["Защитная пленка__кг__м BENKAM (желтый) __ низ ширина ленты__мм"][i]
        заш_пл_кг_м_bn_жл_низ_рас = df["Защитная пленка__кг__м BENKAM (желтый) __ низ расход ленты на 1000 профиль__м2"][i]
        заш_пл_кг_м_ch_вр_ширина_лн_мм = df["Защитная пленка__кг__м IMZO CHEMPION __ верх ширина ленты__мм"][i]
        заш_пл_кг_м_ch_бк_ст_ширина_лн_мм = df["Защитная пленка__кг__м IMZO CHEMPION __ (Боковая сторона) ширина ленты__мм"][i]
        кг_м_ch_вр_и_кг_м_ch_бк_ст_рас = df["Защитная пленка__кг__м IMZO CHEMPION __ верх и Защитная пленка__кг__м IMZO CHEMPION __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i]
        заш_пл_кг_м_ch_низ_ширина_лн_мм = df["Защитная пленка__кг__м IMZO CHEMPION __ низ ширина ленты__мм"][i]
        заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2 = df["Защитная пленка__кг__м IMZO CHEMPION __ низ расход ленты на 1000 профиль__м2"][i]
        заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм = df["Защитная пленка__кг__м IMZO AKFA __ верх ширина ленты__мм"][i]
        заш_пл_кг_м_imzo_akfa_бк_ст_ширина_лн = df["Защитная пленка__кг__м IMZO AKFA __ (Боковая сторона) ширина ленты__мм"][i]
        кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст = df["Защитная пленка__кг__м IMZO AKFA __ верх и Защитная пленка__кг__м IMZO AKFA __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i]
        заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм = df["Защитная пленка__кг__м IMZO AKFA __ низ ширина ленты__мм"][i]
        заш_пл_кг_м_imzo_ak_низ_рас = df["Защитная пленка__кг__м IMZO AKFA __ низ расход ленты на 1000 профиль__м2"][i]
        заш_пл_кг_м_без_бр_вр_ширина_лн_мм = df["Защитная пленка__кг__м Без бренд __ верх ширина ленты__мм"][i]
        заш_пл_кг_м_без_бр_бк_ст_ширина_лн_мм = df["Защитная пленка__кг__м Без бренд __ (Боковая сторона) ширина ленты__мм"][i]
        кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас = df["Защитная пленка__кг__м Без бренд __ верх и Защитная пленка__кг__м Без бренд __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i]
        заш_пл_кг_м_без_бр_низ_ширина_лн_мм = df["Защитная пленка__кг__м Без бренд __ низ ширина ленты__мм"][i]
        заш_пл_кг_м_без_бр_низ_рас = df["Защитная пленка__кг__м Без бренд __ низ расход ленты на 1000 профиль__м2"][i]
        заш_пл_кг_м_eng_верх_ширина_ленты_мм = df["Защитная пленка__кг__м Engelberg __ верх ширина ленты__мм"][i]
        заш_пл_кг_м_eng_бк_ст_ширина_ленты_мм = df["Защитная пленка__кг__м Engelberg __ (Боковая сторона) ширина ленты__мм"][i]
        кг_м_eng_вр_и_кг_м_eng_бк_ст_рас = df["Защитная пленка__кг__м Engelberg __ верх и Защитная пленка__кг__м Engelberg __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i]
        заш_пл_кг_м_eng_низ_ширина_ленты_мм = df["Защитная пленка__кг__м Engelberg __ низ ширина ленты__мм"][i]
        заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр = df["Защитная пленка__кг__м Engelberg __ низ расход ленты на 1000 профиль__м2"][i]
        заш_пл_кг_м_eng_qora_вр_ширина_лн_мм = df["Защитная пленка__кг__м Engelberg (QORA) __ верх ширина ленты__мм"][i]
        заш_пл_кг_м_eng_qora_бк_ст_ширина_лн_мм = df["Защитная пленка__кг__м Engelberg (QORA) __ (Боковая сторона) ширина ленты__мм"][i]
        кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст = df["Защитная пленка__кг__м Engelberg (QORA) __ верх и Защитная пленка__кг__м Engelberg (QORA) __ (Боковая сторона) расход ленты на 1000 профилей__м2"][i]
        заш_пл_кг_м_eng_qora_низ_ширина_ленты = df["Защитная пленка__кг__м Engelberg (QORA) __ низ ширина ленты__мм"][i]
        заш_пл_кг_м_eng_qora_низ_рас = df["Защитная пленка__кг__м Engelberg (QORA) __ низ расход ленты на 1000 профиль__м2"][i]
        уп_пол_лента_ширина_уп_ленты_мм = df["Упаковочная полиэтиленовая лента __ ширина упоковочной ленты__мм"][i]
        уп_пол_лн_рас_уп_лн_на_1000_штук_кг = df["Упаковочная полиэтиленовая лента __ расход упоковочной ленты на 1000 штук __кг"][i]
        расход_скотча_ширина_скотча_мм = df["Расход скотча __ ширина скотча__мм"][i]
        рас_скотча_рас_скотча_на_1000_штук_шт = df["Расход скотча __ расход скотча на 1000 штук __Шт"][i]
        упаковка_колво_профилей_в_1_пачке = df["Упаковка __ Кол-во профилей в 1- пачке"][i]
        ala7_oddiy_ala8_qora_алю_сплав_6064 = df["AL-A7 (Oddiy) __ AL-A8 (Qora) Алюминиевый сплав 6064"][i]
        алю_сплав_биллетов_102_178 =df['Алюминиевый сплав биллетов Ø102 Ø178'][i]
        # print(len(ala7_oddiy_ala8_qora_алю_сплав_6064))
      
        Norma(
        устаревший =устаревший,  
        компонент_1 =компонент_1,  
        компонент_2 =компонент_2,  
        компонент_3 =компонент_3,  
        артикул =артикул,  
        серия =серия,  
        наименование =наименование,  
        внешний_периметр_профиля_мм =внешний_периметр_профиля_мм,  
        площадь_мм21 =площадь_мм21,  
        площадь_мм22 =площадь_мм22,  
        удельный_вес_профиля_кг_м =удельный_вес_профиля_кг_м,  
        диаметр_описанной_окружности_мм =диаметр_описанной_окружности_мм,  
        длина_профиля_м =длина_профиля_м,  
        расчетное_колво_профиля_шт =расчетное_колво_профиля_шт,  
        общий_вес_профиля_кг =общий_вес_профиля_кг,  
        алю_сп_6063_рас_спа_на_1000_шт_пр_кг =алю_сп_6063_рас_спа_на_1000_шт_пр_кг,  
        алю_сплав_6063_при_этом_тех_отхода1 =алю_сплав_6063_при_этом_тех_отхода1,  
        алю_сплав_6063_при_этом_тех_отхода2 =алю_сплав_6063_при_этом_тех_отхода2,  
        смазка_для_пресса_кг_графитовая =смазка_для_пресса_кг_графитовая,  
        смазка_для_пресса_кг_пилы_хл_резки_сол =смазка_для_пресса_кг_пилы_хл_резки_сол,  
        смазка_для_пресса_кг_горячей_резки_сол =смазка_для_пресса_кг_горячей_резки_сол,  
        смазка_для_пресса_кг_графитовые_плиты =смазка_для_пресса_кг_графитовые_плиты,  
        хим_пг_к_окр_politeknik_кг_pol_ac_25p =хим_пг_к_окр_politeknik_кг_pol_ac_25p,  
        хим_пг_к_окр_politeknik_кг_alupol_сr_51 =хим_пг_к_окр_politeknik_кг_alupol_сr_51,  
        хим_пг_к_окр_politeknik_кг_alupol_ac_52 =хим_пг_к_окр_politeknik_кг_alupol_ac_52,  
        пр_краситель_толщина_пк_мкм =пр_краситель_толщина_пк_мкм,  
        порошковый_краситель_рас_кг_на_1000_пр =порошковый_краситель_рас_кг_на_1000_пр,  
        пр_краситель_при_этом_тех_отхода  =пр_краситель_при_этом_тех_отхода ,  
        не_нужний =не_нужний,  
        суб_ширина_декор_пленки_мм_зол_дуб =суб_ширина_декор_пленки_мм_зол_дуб,  
        сублимация_расход_на_1000_профиль_м21 =сублимация_расход_на_1000_профиль_м21,  
        суб_ширина_декор_пленки_мм_3д_313701 =суб_ширина_декор_пленки_мм_3д_313701,  
        сублимация_расход_на_1000_профиль_м22 =сублимация_расход_на_1000_профиль_м22,  
        суб_ширина_декор_пленки_мм_дуб_мокко =суб_ширина_декор_пленки_мм_дуб_мокко,  
        сублимация_расход_на_1000_профиль_м23 =сублимация_расход_на_1000_профиль_м23,  
        суб_ширина_декор_пленки_мм_3д_313702 =суб_ширина_декор_пленки_мм_3д_313702,  
        сублимация_расход_на_1000_профиль_м24 =сублимация_расход_на_1000_профиль_м24,  
        молярный_скотч_ширина1_мол_скотча_мм =молярный_скотч_ширина1_мол_скотча_мм,   
        молярный_скотч_рас_на_1000_пр_шт1 =молярный_скотч_рас_на_1000_пр_шт1,  
        молярный_скотч_ширина2_мол_скотча_мм =молярный_скотч_ширина2_мол_скотча_мм,   
        молярный_скотч_рас_на_1000_пр_шт2 =молярный_скотч_рас_на_1000_пр_шт2,  
        термомост_1 =термомост_1,  
        термомост_2 =термомост_2,  
        термомост_3 =термомост_3,  
        термомост_4 =термомост_4,  
        ламинация_верх_a_ширина_ленты_мм =ламинация_верх_a_ширина_ленты_мм,  
        лам_верх_a_рас_ленты_на_1000_пр_м2 =лам_верх_a_рас_ленты_на_1000_пр_м2,  
        ламинация_низ_b_ширина_ленты_мм =ламинация_низ_b_ширина_ленты_мм,  
        лам_низ_b_рас_ленты_на_1000_пр_м2 =лам_низ_b_рас_ленты_на_1000_пр_м2,  
        ламинация_низ_c_ширина_ленты_мм =ламинация_низ_c_ширина_ленты_мм,  
        лам_низ_c_рас_ленты_на_1000_пр_м2 =лам_низ_c_рас_ленты_на_1000_пр_м2,  
        лам_рас_праймера_на_1000_штук_пр_кг =лам_рас_праймера_на_1000_штук_пр_кг,  
        лам_рас_клея_на_1000_штук_пр_кг =лам_рас_клея_на_1000_штук_пр_кг,  
        лам_рас_уп_материала_мешок_на_1000_пр =лам_рас_уп_материала_мешок_на_1000_пр,  
        заш_пл_кг_м_akfa_верх_ширина_ленты_мм =заш_пл_кг_м_akfa_верх_ширина_ленты_мм,  
        заш_пл_кг_м_akfa_бк_ст_ширина_ленты_мм =заш_пл_кг_м_akfa_бк_ст_ширина_ленты_мм,  
        кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн =кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн,  
        заш_пл_кг_м_akfa_низ_ширина_ленты_мм =заш_пл_кг_м_akfa_низ_ширина_ленты_мм,  
        заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2 =заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2,  
        заш_пл_кг_м_retpen_верх_ширина_ленты_мм =заш_пл_кг_м_retpen_верх_ширина_ленты_мм,  
        заш_пл_кг_м_retpen_бк_ст_ширина_ленты =заш_пл_кг_м_retpen_бк_ст_ширина_ленты,  
        кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас =кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас,  
        заш_пл_кг_м_retpen_низ_ширина_ленты_мм =заш_пл_кг_м_retpen_низ_ширина_ленты_мм,  
        заш_пл_кг_м_retpen_низ_рас  =заш_пл_кг_м_retpen_низ_рас ,  
        заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм  =заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм ,  
        заш_пл_кг_м_benkam_жл_бк_ст_ширина_лн =заш_пл_кг_м_benkam_жл_бк_ст_ширина_лн,  
        кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас =кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас,  
        заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм =заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,  
        заш_пл_кг_м_bn_жл_низ_рас =заш_пл_кг_м_bn_жл_низ_рас,  
        заш_пл_кг_м_ch_вр_ширина_лн_мм =заш_пл_кг_м_ch_вр_ширина_лн_мм,  
        заш_пл_кг_м_ch_бк_ст_ширина_лн_мм =заш_пл_кг_м_ch_бк_ст_ширина_лн_мм,  
        кг_м_ch_вр_и_кг_м_ch_бк_ст_рас =кг_м_ch_вр_и_кг_м_ch_бк_ст_рас,  
        заш_пл_кг_м_ch_низ_ширина_лн_мм =заш_пл_кг_м_ch_низ_ширина_лн_мм,  
        заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2 =заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2,  
        заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,  
        заш_пл_кг_м_imzo_akfa_бк_ст_ширина_лн =заш_пл_кг_м_imzo_akfa_бк_ст_ширина_лн,  
        кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст =кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст,  
        заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм =заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,  
        заш_пл_кг_м_imzo_ak_низ_рас =заш_пл_кг_м_imzo_ak_низ_рас,  
        заш_пл_кг_м_без_бр_вр_ширина_лн_мм =заш_пл_кг_м_без_бр_вр_ширина_лн_мм,  
        заш_пл_кг_м_без_бр_бк_ст_ширина_лн_мм =заш_пл_кг_м_без_бр_бк_ст_ширина_лн_мм,  
        кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас =кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас,  
        заш_пл_кг_м_без_бр_низ_ширина_лн_мм =заш_пл_кг_м_без_бр_низ_ширина_лн_мм,  
        заш_пл_кг_м_без_бр_низ_рас =заш_пл_кг_м_без_бр_низ_рас,  
        заш_пл_кг_м_eng_верх_ширина_ленты_мм =заш_пл_кг_м_eng_верх_ширина_ленты_мм,  
        заш_пл_кг_м_eng_бк_ст_ширина_ленты_мм =заш_пл_кг_м_eng_бк_ст_ширина_ленты_мм,  
        кг_м_eng_вр_и_кг_м_eng_бк_ст_рас =кг_м_eng_вр_и_кг_м_eng_бк_ст_рас,  
        заш_пл_кг_м_eng_низ_ширина_ленты_мм =заш_пл_кг_м_eng_низ_ширина_ленты_мм,  
        заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр =заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр,  
        заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,  
        заш_пл_кг_м_eng_qora_бк_ст_ширина_лн_мм =заш_пл_кг_м_eng_qora_бк_ст_ширина_лн_мм,  
        кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст =кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст,  
        заш_пл_кг_м_eng_qora_низ_ширина_ленты =заш_пл_кг_м_eng_qora_низ_ширина_ленты,  
        заш_пл_кг_м_eng_qora_низ_рас =заш_пл_кг_м_eng_qora_низ_рас,  
        уп_пол_лента_ширина_уп_ленты_мм =уп_пол_лента_ширина_уп_ленты_мм,  
        уп_пол_лн_рас_уп_лн_на_1000_штук_кг =уп_пол_лн_рас_уп_лн_на_1000_штук_кг,  
        расход_скотча_ширина_скотча_мм =расход_скотча_ширина_скотча_мм,  
        рас_скотча_рас_скотча_на_1000_штук_шт =рас_скотча_рас_скотча_на_1000_штук_шт,  
        упаковка_колво_профилей_в_1_пачке =упаковка_колво_профилей_в_1_пачке,  
        ala7_oddiy_ala8_qora_алю_сплав_6064 =ala7_oddiy_ala8_qora_алю_сплав_6064,
        алю_сплав_биллетов_102_178=алю_сплав_биллетов_102_178
        ).save()  
    
    
    return redirect('index')

    
def receipt_all(request):
    ########## Nakleyka
    df = pd.read_excel('C:\\OpenServer\\domains\\Наклейка.xlsx','Наклейка')
    df =df.astype(str)
    
    for i in range(0,df.shape[0]):
        sap_code_s4q100 = df['SAP code S4Q100'][i]
        название = df['Название'][i]
        еи = df['ЕИ'][i]
        склад_закупа = df['Склад закупа'][i]
        код_наклейки = df['Код наклейки'][i]
        название_наклейки = df['название наклейки'][i]
        ширина = df['Ширина'][i]
        еи_ширины = df['ЕИ ширины'][i]
        тип_клея = df['Тип клея '][i]
        Nakleyka(
            sap_code_s4q100 = sap_code_s4q100, 
            название = название, 
            еи = еи, 
            склад_закупа = склад_закупа, 
            код_наклейки = код_наклейки, 
            название_наклейки = название_наклейки, 
            ширина = ширина, 
            еи_ширины = еи_ширины, 
            тип_клея = тип_клея
            ).save()
    ######end Nakleyka
    print('nakleyka tugadi')
    # ########## Краска
    # df = pd.read_excel('C:\\OpenServer\\domains\\Норма для ИТ-1 (2).xlsx','Краска')
    # df =df.astype(str)
    
    # for i in range(0,df.shape[0]):
    #     sap_code_s4q100 = df['SAP code S4Q100'][i]
    #     название = df['Название'][i]
    #     еи = df['ЕИ'][i]
    #     склад_закупа = df['Склад закупа'][i]
    #     бренд_краски = df['Бренд краски'][i]
    #     код_краски = df['Код краски'][i]
    #     тип_краски = df['тип краски'][i]
    #     код_краски_в_профилях = df['Код краски в профилях'][i]
    #     Kraska(
    #     sap_code_s4q100 = sap_code_s4q100, 
    #     название = название, 
    #     еи = еи, 
    #     склад_закупа = склад_закупа, 
    #     бренд_краски = бренд_краски, 
    #     код_краски = код_краски, 
    #     тип_краски = тип_краски, 
    #     код_краски_в_профилях = код_краски_в_профилях 
    #         ).save()

    # ######end Nakleyka
    # print('kraska tugadi')
    # ########## химикаты
    # df = pd.read_excel('C:\\OpenServer\\domains\\Норма для ИТ-1 (2).xlsx','химикаты')
    # df =df.astype(str)
    
    # for i in range(0,df.shape[0]):
    #     sap_code_s4q100 = df['SAP code S4Q100'][i]
    #     название = df['Название'][i]
    #     еи = df['ЕИ'][i]
    #     склад_закупа = df['Склад закупа'][i]
    #     Ximikat(
    #     sap_code_s4q100 =sap_code_s4q100, 
    #     название =название, 
    #     еи =еи, 
    #     склад_закупа =склад_закупа 
    #         ).save()

    # ######end химикаты
    # print('ximikat tugadi')
    # ########## Суб декор пленка
    # df = pd.read_excel('C:\\OpenServer\\domains\\Норма для ИТ-1 (2).xlsx','Суб декор пленка')
    # df =df.astype(str)
    
    # for i in range(0,df.shape[0]):
    #     sap_code_s4q100 = df['SAP code S4Q100'][i]
    #     название = df['Название'][i]
    #     еи = df['ЕИ'][i]
    #     склад_закупа = df['Склад закупа'][i]
    #     код_декор_пленки = df['Код декор пленки'][i]
    #     ширина_декор_пленки_мм = df['ширина декор пленки/мм'][i]
    #     SubDekorPlonka(
    #     sap_code_s4q100 = sap_code_s4q100, 
    #     название = название, 
    #     еи = еи, 
    #     склад_закупа = склад_закупа, 
    #     код_декор_пленки = код_декор_пленки, 
    #     ширина_декор_пленки_мм = ширина_декор_пленки_мм 
    #         ).save()

    # ######end Nakleyka
    # print('subdekor tugadi')
    # ########## скотч
    # df = pd.read_excel('C:\\OpenServer\\domains\\Норма для ИТ-1 (2).xlsx','скотч')
    # df =df.astype(str)
    
    # for i in range(0,df.shape[0]):
    #     sap_code_s4q100 = df['SAP code S4Q100'][i]
    #     название = df['Название'][i]
    #     еи = df['ЕИ'][i]
    #     склад_закупа = df['Склад закупа'][i]
    #     Skotch(
    #     sap_code_s4q100 = sap_code_s4q100, 
    #     название = название, 
    #     еи = еи, 
    #     склад_закупа = склад_закупа 
    #         ).save()

    # ######end скотч
    # print('skotch tugadi')
    # ########## Лам пленка
    # df = pd.read_excel('C:\\OpenServer\\domains\\Норма для ИТ-1 (2).xlsx','Лам пленка')
    # df =df.astype(str)
    
    # for i in range(0,df.shape[0]):
    #     sap_code_s4q100 = df['SAP code S4Q100'][i]
    #     название = df['Название'][i]
    #     еи = df['ЕИ'][i]
    #     склад_закупа = df['Склад закупа'][i]
    #     код_лам_пленки = df['Код лам пленки'][i]
    #     Lamplonka(
    #     sap_code_s4q100 = sap_code_s4q100, 
    #     название = название, 
    #     еи = еи, 
    #     склад_закупа = склад_закупа, 
    #     код_лам_пленки = код_лам_пленки 
    #         ).save()

    # ######end Nakleyka
    # print('lam plyon tugadi')
    # ########## клей для лам
    # df = pd.read_excel('C:\\OpenServer\\domains\\Норма для ИТ-1 (2).xlsx','клей для лам')
    # df =df.astype(str)
    
    # for i in range(0,df.shape[0]):
    #     sap_code_s4q100 = df['SAP code S4Q100'][i]
    #     название = df['Название'][i]
    #     еи = df['ЕИ'][i]
    #     склад_закупа = df['Склад закупа'][i]
    #     KleyDlyaLamp(
    #     sap_code_s4q100 = sap_code_s4q100, 
    #     название = название, 
    #     еи = еи, 
    #     склад_закупа = склад_закупа 
    #         ).save()

    # ######end Nakleyka
    # print('kley dlya lam tugadi')
    # ########## Алю цилиндр и для экструзии1
    # df = pd.read_excel('C:\\OpenServer\\domains\\Норма для ИТ-1 (2).xlsx','Алю цилиндр и для экструзии1')
    # df =df.astype(str)
    
    # for i in range(0,df.shape[0]):
    #     sap_code_s4q100 = df['SAP code S4Q100'][i]
    #     название = df['Название'][i]
    #     еи = df['ЕИ'][i]
    #     склад_закупа = df['Склад закупа'][i]
    #     тип = df['ТИП'][i]
    #     AlyuminniysilindrEkstruziya1(
    #     sap_code_s4q100 = sap_code_s4q100, 
    #     название = название, 
    #     еи = еи, 
    #     склад_закупа = склад_закупа, 
    #     тип = тип 
    #         ).save()

    # ######end Nakleyka
    # print('alu silind dlya ekst1 tugadi')
    # ########## Алю цилиндр и для экструзии2
    # df = pd.read_excel('C:\\OpenServer\\domains\\Норма для ИТ-1 (2).xlsx','Алю цилиндр и для экструзии2')
    # df =df.astype(str)
    
    # for i in range(0,df.shape[0]):
    #     sap_code_s4q100 = df['SAP code S4Q100'][i]
    #     название = df['Название'][i]
    #     еи = df['ЕИ'][i]
    #     склад_закупа = df['Склад закупа'][i]
    #     AlyuminniysilindrEkstruziya2(
    #     sap_code_s4q100 = sap_code_s4q100, 
    #     название = название, 
    #     еи = еи, 
    #     склад_закупа = склад_закупа
    #         ).save()

    # ######end Nakleyka
    # print('alu silind dlya ekst2 tugadi')
    # ########## Термомост для термо
    # df = pd.read_excel('C:\\OpenServer\\domains\\Норма для ИТ-1 (2).xlsx','Термомост для термо')
    # df =df.astype(str)
    
    # for i in range(0,df.shape[0]):
    #     sap_code_s4q100 = df['SAP code S4Q100'][i]
    #     название = df['Название'][i]
    #     еи = df['ЕИ'][i]
    #     склад_закупа = df['Склад закупа'][i]
    #     TermomostDlyaTermo(
    #     sap_code_s4q100 = sap_code_s4q100,
    #     название = название,
    #     еи = еи,
    #     склад_закупа = склад_закупа
    #         ).save()

    # ######end Nakleyka
    # print('termomost dlya termo tugadi')
    # ########## Сырьё Упаковки
    # df = pd.read_excel('C:\\OpenServer\\domains\\Норма для ИТ-1 (2).xlsx','Сырьё Упаковки')
    # df =df.astype(str)
    
    # for i in range(0,df.shape[0]):
    #     sap_code_s4q100 = df['SAP code S4Q100'][i]
    #     название = df['Название'][i]
    #     еи = df['ЕИ'][i]
    #     склад_закупа = df['Склад закупа'][i]
    #     SiryoDlyaUpakovki(
    #     sap_code_s4q100 = sap_code_s4q100, 
    #     название = название, 
    #     еи = еи, 
    #     склад_закупа = склад_закупа
    #         ).save()

    # ######end Nakleyka
    # print('siryo dlya upakovki tugadi')
    # ########## Прочие сырьё ненормированный
    # df = pd.read_excel('C:\\OpenServer\\domains\\Норма для ИТ-1 (2).xlsx','Прочие сырьё ненормированный')
    # df =df.astype(str)
    
    # for i in range(0,df.shape[0]):
    #     sap_code_s4q100 = df['SAP code S4Q100'][i]
    #     название = df['Название'][i]
    #     еи = df['ЕИ'][i]
    #     склад_закупа = df['Склад закупа'][i]
    #     ProchiyeSiryoNeno(
    #     sap_code_s4q100 = sap_code_s4q100, 
    #     название = название, 
    #     еи = еи, 
    #     склад_закупа = склад_закупа
    #         ).save()

    ######end Nakleyka
    
    
    print('prochiye siryo tugadi')
    
    return JsonResponse({'Hammasi bo\'ldi':'ok'})


def norma_add(request):
    df = pd.read_excel('c:\\Users\\Acer\\Desktop\\Копия Thermo profilesййй2.xlsx','Лист1')
    df =df.astype(str)
    print(df)
    for key, row in df.iterrows():
        artikul = row['Articale']
        component1 = row['Component № 1']
        component2 = row['Component № 2']
        component3 = row['Component № 3']
        sap_code1 = row['SAP код1']
        termal_bridge1 =row['Thermal bridge № 1']
        sap_code2 =row['SAP код2']
        termal_bridge2 = row['Thermal bridge № 2']
        sap_code3 = row['SAP код3']
        termal_bridge3 = row['Thermal bridge № 3']
        sap_code4 =row['SAP код4']
        termal_bridge4 =row['Thermal bridge № 4']
        
        KombinirovaniyUtilsInformation(
            artikul = artikul, 
            component1 = component1, 
            component2 = component2, 
            component3 = component3, 
            sap_code1 = sap_code1, 
            termal_bridge1 = termal_bridge1, 
            sap_code2 = sap_code2, 
            termal_bridge2 = termal_bridge2, 
            sap_code3 = sap_code3, 
            termal_bridge3 = termal_bridge3, 
            sap_code4 = sap_code4, 
            termal_bridge4 = termal_bridge4, 
            ).save()
    
    return JsonResponse({'a':'b'})
    

def file_upload(request): 
  if request.method == 'POST':
    form = NormaFileForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('norma_file_list')
  else:
      form =NormaFileForm()
      context ={
        'form':form
      }
  return render(request,'norma/excel_form.html',context)

def file_list(request):
    files = NormaExcelFiles.objects.filter(generated =False)
    context ={'files':files}
    return render(request,'norma/file_list.html',context)

def get_legth(lengg):
    lls =lengg.split()
    for ll in lls:
        if ll.startswith('L'):
            hh =ll.replace('L','')
            break
    return (float(hh)/1000) 

######### Integratsiya 1 ########
def process(request,id):
    file = NormaExcelFiles.objects.get(id=id).file
    file_path =f'{MEDIA_ROOT}\\{file}'
    df_exell = pd.read_excel(file_path)
    df_exell = df_exell.fillna('')
    df_exell =df_exell.astype(str)
    
    df = []
    
    check_for_existing =[]
    for key,row in df_exell.iterrows():
        df.append([
            row['SAP код E'],row['Экструзия холодная резка'],
            row['SAP код Z'],row['Печь старения'],
            row['SAP код P'],row['Покраска автомат'],
            row['SAP код S'],row['Сублимация'],
            row['SAP код 7'],row['U-Упаковка + Готовая Продукция']
        ])
        if row['SAP код E'] !='':
            check_for_existing.append({'sapkom':row['SAP код E'],'sapgp':row['SAP код 7']})
            continue
        if row['SAP код Z'] !='':
            check_for_existing.append({'sapkom':row['SAP код Z'],'sapgp':row['SAP код 7']})
            continue
        if row['SAP код P'] !='':
            check_for_existing.append({'sapkom':row['SAP код P'],'sapgp':row['SAP код 7']})
            continue
        if row['SAP код S'] !='':
            check_for_existing.append({'sapkom':row['SAP код S'],'sapgp':row['SAP код 7']})
            
    
    print(df)
    
    
    df_new ={
        'ID':[],
        'MATNR': [],
        'WERKS':[],
        'TEXT1':[],
        'STLAL':[],
        'STLAN':[],
        'ZTEXT':[],
        'STKTX':[],
        'BMENG':[],
        'BMEIN':[],
        'STLST':[],
        'POSNR':[],
        'POSTP':[],
        'MATNR1':[],
        'TEXT2':[],
        'MEINS':[],
        'MENGE':[],
        'DATUV':[],
        'PUSTOY':[],
        'LGORT':[]
    }
    
    j=0
    
    
    for i in range(0,len(df)):
        sap_dict = check_for_existing[i]['sapkom'].split('-')[0]
        sap_dictgp = check_for_existing[i]['sapgp'].split('-')[0]
        existskom = Norma.objects.filter(Q(компонент_1=sap_dict)|Q(компонент_2=sap_dict)|Q(компонент_3=sap_dict)|Q(артикул=sap_dict)).exists() 
        existsgp = Norma.objects.filter(Q(компонент_1=sap_dictgp)|Q(компонент_2=sap_dictgp)|Q(компонент_3=sap_dictgp)|Q(артикул=sap_dictgp)).exists() 
        if not ((existskom and existsgp)):
            if not existskom:
                NormaDontExistInExcell(artikul =sap_dict).save()
            if not existsgp:
                NormaDontExistInExcell(artikul =sap_dictgp).save()
            continue
        older_process ={'sapcode':'','kratkiy':''}
        
        norma_existsE = CheckNormaBase.objects.filter(artikul=df[i][0],kratkiytekst=df[i][1]).exists()
        if not norma_existsE:
            if df[i][0] !="":
                CheckNormaBase(artikul=df[i][0],kratkiytekst=df[i][1]).save()
                older_process['sapcode'] =df[i][0]
                older_process['kratkiy'] =df[i][1]
                if df[i][0].split('-')[1][:1]=='E':
                    df_new['ID'].append('1')
                    df_new['MATNR'].append(df[i][0])
                    df_new['WERKS'].append('1101')
                    df_new['TEXT1'].append(df[i][1])
                    df_new['STLAL'].append('1')
                    df_new['STLAN'].append('1')
                    if df[i][0].split('-')[1][:1]=='E':
                        ztekst ='Экструзия (пресс) + Пила'
                    df_new['ZTEXT'].append(ztekst)
                    length = df[i][0].split('-')[0]
                    alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                    
                    aliminisi =AlyuminniysilindrEkstruziya1.objects.filter(тип =alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064)[:1].get()
                    
                    mein_percent =((get_legth(df[i][1]))/float(alum_teks.длина_профиля_м))
                    df_new['STKTX'].append(aliminisi.название)
                    df_new['BMENG'].append( '1000')
                    df_new['BMEIN'].append('ШТ')
                    df_new['STLST'].append('1')
                    df_new['POSNR'].append('')
                    df_new['POSTP'].append('')
                    df_new['MATNR1'].append('')
                    df_new['TEXT2'].append('')
                    df_new['MEINS'].append('')
                    df_new['MENGE'].append('')
                    df_new['DATUV'].append('01012021')
                    df_new['PUSTOY'].append('')
                    df_new['LGORT'].append('')
                    for k in range(1,6):
                        j+=1
                        df_new['ID'].append('2')
                        df_new['MATNR'].append('')
                        df_new['WERKS'].append('')
                        df_new['TEXT1'].append('')
                        df_new['STLAL'].append('')
                        df_new['STLAN'].append('')
                        df_new['ZTEXT'].append('')
                        df_new['STKTX'].append('')
                        df_new['BMENG'].append('')
                        df_new['BMEIN'].append('')
                        df_new['STLST'].append('')
                        df_new['POSNR'].append(k)
                        df_new['POSTP'].append('L')
                        
                        
                        if k == 1 :
                            
                            df_new['MATNR1'].append(aliminisi.sap_code_s4q100)
                            df_new['TEXT2'].append(aliminisi.название)
                            df_new['MEINS'].append("{:0f}".format(float(alum_teks.алю_сп_6063_рас_спа_на_1000_шт_пр_кг)*mein_percent))
                            df_new['MENGE'].append('КГ')
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        
                        if k==2:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=1)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append( "{:0f}".format(float(alum_teks.смазка_для_пресса_кг_графитовая)*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k==3:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=2)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append("{:0f}".format((float(alum_teks.смазка_для_пресса_кг_пилы_хл_резки_сол) + float(alum_teks.смазка_для_пресса_кг_горячей_резки_сол))*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k == 4:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=3)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append("{:0f}".format(float(alum_teks.смазка_для_пресса_кг_графитовые_плиты)*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k == 5:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=4)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append("{:0f}".format(((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода1)+float(alum_teks.алю_сплав_6063_при_этом_тех_отхода2)))*mein_percent)) 
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                            
                        df_new['LGORT'].append('PS01')
                    
                    j+=1
                    df_new['ID'].append('1')
                    df_new['MATNR'].append( df[i][0])
                    df_new['WERKS'].append('1101')
                    df_new['TEXT1'].append(df[i][1])
                    df_new['STLAL'].append('2')
                    df_new['STLAN'].append('1')
                
                    if df[i][0].split('-')[1][:1]=='E':
                        ztekst='Экструзия (пресс) + Пила'
                    df_new['ZTEXT'].append( ztekst)
                    length = df[i][0].split('-')[0]
                    
                    alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                    aliminisi =AlyuminniysilindrEkstruziya1.objects.filter(тип =alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064)[1:2].get()       
                    df_new['STKTX'].append(aliminisi.название)
                    df_new['BMENG'].append( '1000')
                    df_new['BMEIN'].append('ШТ')
                    df_new['STLST'].append('1')
                    df_new['POSNR'].append('')
                    df_new['POSTP'].append('')
                    df_new['MATNR1'].append('')
                    df_new['TEXT2'].append('')
                    df_new['MEINS'].append('')
                    df_new['MENGE'].append('')
                    df_new['DATUV'].append('01012021')
                    df_new['PUSTOY'].append('')
                    df_new['LGORT'].append('')
                    for k in range(1,6):
                        j+=1
                        df_new['ID'].append( '2')
                        df_new['MATNR'].append( '')
                        df_new['WERKS'].append( '')
                        df_new['TEXT1'].append( '')
                        df_new['STLAL'].append( '')
                        df_new['STLAN'].append( '')
                        df_new['ZTEXT'].append( '')
                        df_new['STKTX'].append( '')
                        df_new['BMENG'].append( '')
                        df_new['BMEIN'].append('')
                        df_new['STLST'].append('')
                        df_new['POSNR'].append(k)
                        df_new['POSTP'].append('L')
                        if k == 1 :
                            df_new['MATNR1'].append(aliminisi.sap_code_s4q100)
                            df_new['TEXT2'].append(aliminisi.название)
                            df_new['MEINS'].append( "{:0f}".format(float(alum_teks.алю_сп_6063_рас_спа_на_1000_шт_пр_кг)*mein_percent))
                            df_new['MENGE'].append( 'КГ')
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        
                        if k==2:
                            alummm = AlyuminniysilindrEkstruziya2.objects.first()
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append( "{:0f}".format(float(alum_teks.смазка_для_пресса_кг_графитовая)*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k==3:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=2)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append( "{:0f}".format((float(alum_teks.смазка_для_пресса_кг_пилы_хл_резки_сол) + float(alum_teks.смазка_для_пресса_кг_горячей_резки_сол))*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k == 4:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=3)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append( "{:0f}".format(float(alum_teks.смазка_для_пресса_кг_графитовые_плиты)*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k == 5:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=4)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append( "{:0f}".format(((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода1)+float(alum_teks.алю_сплав_6063_при_этом_тех_отхода2)))*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        df_new['LGORT'].append('PS01')
        else:
            normaexist = CheckNormaBase.objects.filter(artikul=df[i][0],kratkiytekst=df[i][1])[:1].get()
            older_process['sapcode'] =normaexist.artikul
            older_process['kratkiy'] =normaexist.kratkiytekst
                    
                
        norma_existsZ = CheckNormaBase.objects.filter(artikul=df[i][2],kratkiytekst=df[i][3]).exists()
        if not norma_existsZ:
            if df[i][2] !="":
                print(df[i][2])
                CheckNormaBase(artikul=df[i][2],kratkiytekst=df[i][3]).save()
                older_process['sapcode'] =df[i][2]
                older_process['kratkiy'] =df[i][3]  
                j+=1
                if (df[i][2].split('-')[1][:1]=='Z'):
                    df_new['ID'].append('1')
                    df_new['MATNR'].append(df[i][2])
                    df_new['WERKS'].append('1101')
                    df_new['TEXT1'].append(df[i][3])
                    df_new['STLAL'].append('1')
                    df_new['STLAN'].append('1')
                    if df[i][2].split('-')[1][:1]=='Z':
                        ztekst ='Экструзия (пресс) + Пила + Старение'
                    df_new['ZTEXT'].append(ztekst)
                    length = df[i][2].split('-')[0]
                    
                    alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                    
                    
                    aliminisi =AlyuminniysilindrEkstruziya1.objects.filter(тип =alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064)[:1].get()
                    
                    mein_percent =((get_legth(df[i][3]))/float(alum_teks.длина_профиля_м))
                    df_new['STKTX'].append(aliminisi.название)
                    df_new['BMENG'].append( '1000')
                    df_new['BMEIN'].append('ШТ')
                    df_new['STLST'].append('1')
                    df_new['POSNR'].append('')
                    df_new['POSTP'].append('')
                    df_new['MATNR1'].append('')
                    df_new['TEXT2'].append('')
                    df_new['MEINS'].append('')
                    df_new['MENGE'].append('')
                    df_new['DATUV'].append('01012021')
                    df_new['PUSTOY'].append('')
                    df_new['LGORT'].append('')
                    
                    for k in range(1,6):
                        j+=1
                        df_new['ID'].append('2')
                        df_new['MATNR'].append('')
                        df_new['WERKS'].append('')
                        df_new['TEXT1'].append('')
                        df_new['STLAL'].append('')
                        df_new['STLAN'].append('')
                        df_new['ZTEXT'].append('')
                        df_new['STKTX'].append('')
                        df_new['BMENG'].append('')
                        df_new['BMEIN'].append('')
                        df_new['STLST'].append('')
                        df_new['POSNR'].append(k)
                        df_new['POSTP'].append('L')
                        
                        
                        if k == 1 :
                            df_new['MATNR1'].append(aliminisi.sap_code_s4q100)
                            df_new['TEXT2'].append(aliminisi.название)
                            df_new['MEINS'].append("{:0f}".format(float(alum_teks.алю_сп_6063_рас_спа_на_1000_шт_пр_кг)*mein_percent))
                            df_new['MENGE'].append('КГ')
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        
                        if k==2:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=1)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append( "{:0f}".format(float(alum_teks.смазка_для_пресса_кг_графитовая)*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k==3:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=2)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append("{:0f}".format((float(alum_teks.смазка_для_пресса_кг_пилы_хл_резки_сол) + float(alum_teks.смазка_для_пресса_кг_горячей_резки_сол))*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k == 4:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=3)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append("{:0f}".format(float(alum_teks.смазка_для_пресса_кг_графитовые_плиты)*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k == 5:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=4)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append("{:0f}".format(((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода1)+float(alum_teks.алю_сплав_6063_при_этом_тех_отхода2)))*mein_percent)) 
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                            
                        df_new['LGORT'].append('PS01')

                    
                    
                    j+=1
                    df_new['ID'].append('1')
                    df_new['MATNR'].append( df[i][2])
                    df_new['WERKS'].append('1101')
                    df_new['TEXT1'].append(df[i][3])
                    df_new['STLAL'].append('2')
                    df_new['STLAN'].append('1')
                
                    length = df[i][2].split('-')[0]
                    
                    alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                    if df[i][2].split('-')[1][:1]=='E':
                        ztekst='Экструзия (пресс) + Пила'
                    df_new['ZTEXT'].append( ztekst)
                    aliminisi =AlyuminniysilindrEkstruziya1.objects.filter(тип =alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064)[1:2].get()
                    df_new['STKTX'].append(aliminisi.название)
                    df_new['BMENG'].append( '1000')
                    df_new['BMEIN'].append('ШТ')
                    df_new['STLST'].append('1')
                    df_new['POSNR'].append('')
                    df_new['POSTP'].append('')
                    df_new['MATNR1'].append('')
                    df_new['TEXT2'].append('')
                    df_new['MEINS'].append('')
                    df_new['MENGE'].append('')
                    df_new['DATUV'].append('01012021')
                    df_new['PUSTOY'].append('')
                    df_new['LGORT'].append('')
                    for k in range(1,6):
                        j+=1
                        df_new['ID'].append( '2')
                        df_new['MATNR'].append( '')
                        df_new['WERKS'].append( '')
                        df_new['TEXT1'].append( '')
                        df_new['STLAL'].append( '')
                        df_new['STLAN'].append( '')
                        df_new['ZTEXT'].append( '')
                        df_new['STKTX'].append( '')
                        df_new['BMENG'].append( '')
                        df_new['BMEIN'].append('')
                        df_new['STLST'].append('')
                        df_new['POSNR'].append(k)
                        df_new['POSTP'].append('L')
                        if k == 1 :
                            
                            df_new['MATNR1'].append(aliminisi.sap_code_s4q100)
                            df_new['TEXT2'].append(aliminisi.название)
                            df_new['MEINS'].append( "{:0f}".format(float(alum_teks.алю_сп_6063_рас_спа_на_1000_шт_пр_кг)*mein_percent))
                            df_new['MENGE'].append( 'КГ')
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        
                        if k==2:
                            alummm = AlyuminniysilindrEkstruziya2.objects.first()
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append( "{:0f}".format(float(alum_teks.смазка_для_пресса_кг_графитовая)*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k==3:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=2)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append( "{:0f}".format((float(alum_teks.смазка_для_пресса_кг_пилы_хл_резки_сол) + float(alum_teks.смазка_для_пресса_кг_горячей_резки_сол))*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k == 4:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=3)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append( "{:0f}".format(float(alum_teks.смазка_для_пресса_кг_графитовые_плиты)*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k == 5:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=4)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append( "{:0f}".format(((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода1)+float(alum_teks.алю_сплав_6063_при_этом_тех_отхода2)))*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        df_new['LGORT'].append('PS01')
        else:
            normaexist = CheckNormaBase.objects.filter(artikul=df[i][2],kratkiytekst=df[i][3])[:1].get()
            older_process['sapcode'] =normaexist.artikul
            older_process['kratkiy'] =normaexist.kratkiytekst            
        
        sklad ={
            'sklad_pokraski':['SKM - SKM покраска','SAT - SAT покраска','ГР - ГР покраска','SKM - Ручная покраска','SAT - Ручная покраска','ГР - Ручная покраска'],
            'number_sklad':[
                ['PS04','PS04','PS04','PS04','PS04','PS04'],
                ['PS05','PS05','PS05','PS05','PS05','PS05'],
                ['PS06','PS06','PS06','PS06','PS06','PS06'],
                ['PS07','PS07','PS07','PS04','PS04','PS04'],
                ['PS07','PS07','PS07','PS05','PS05','PS05'],
                ['PS07','PS07','PS07','PS06','PS06','PS06']
                ]
        }
        
        norma_existsP = CheckNormaBase.objects.filter(artikul=df[i][4],kratkiytekst=df[i][5]).exists()
        if not norma_existsP:
            if df[i][4] !="":
                CheckNormaBase(artikul=df[i][4],kratkiytekst=df[i][5]).save()
                if (df[i][4].split('-')[1][:1]=='P'):
                    print(df[i][4])
                    for p in range(0,6):    
                        j+=1
                        
                        if (df[i][4].split('-')[1][:1]=='P'):
                            df_new['ID'].append('1')
                            df_new['MATNR'].append(df[i][4])
                            df_new['WERKS'].append('1101')
                            df_new['TEXT1'].append(df[i][5])
                            df_new['STLAL'].append(f'{p+1}')
                            df_new['STLAN'].append('1')
                            ztekst = sklad['sklad_pokraski'][p]
                            df_new['ZTEXT'].append(ztekst)
                            df_new['STKTX'].append(ztekst)
                            df_new['BMENG'].append( '1000')
                            df_new['BMEIN'].append('ШТ')
                            df_new['STLST'].append('1')
                            df_new['POSNR'].append('')
                            df_new['POSTP'].append('')
                            df_new['MATNR1'].append('')
                            df_new['TEXT2'].append('')
                            df_new['MEINS'].append('')
                            df_new['MENGE'].append('')
                            df_new['DATUV'].append('01012021')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('')
                            length = df[i][4].split('-')[0]
                            
                            alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                            
                            
                            mein_percent =((get_legth(df[i][5]))/float(alum_teks.длина_профиля_м))
                            
                            for k in range(0,6):
                                j+=1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                
                                
                                if k == 0 :
                                    aliminisi =AlyuminniysilindrEkstruziya1.objects.filter(тип =alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064)[:1].get()
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    alummm = AlyuminniysilindrEkstruziya2.objects.get(id=1)
                                    kraska_code = df[i][5].split()[-1]
                                    print('kraskaaa======= ',kraska_code)                                    
                                    kraska =Kraska.objects.filter(код_краски_в_профилях = kraska_code)[:1].get()
                                    df_new['MATNR1'].append(kraska.sap_code_s4q100)
                                    df_new['TEXT2'].append(kraska.название)
                                    df_new['MENGE'].append('КГ')
                                    df_new['MEINS'].append( "{:0f}".format(float(alum_teks.порошковый_краситель_рас_кг_на_1000_пр)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k == 2:
                                    himikat_kraska = Ximikat.objects.get(id=4)
                                    df_new['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                    df_new['TEXT2'].append(himikat_kraska.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format((-1)*float(alum_teks.пр_краситель_при_этом_тех_отхода)*mein_percent)) 
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==3:
                                    himikat_kraska = Ximikat.objects.get(id=1)
                                    df_new['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                    df_new['TEXT2'].append(himikat_kraska.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.хим_пг_к_окр_politeknik_кг_alupol_сr_51)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k == 4:
                                    himikat_kraska = Ximikat.objects.get(id=2)
                                    df_new['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                    df_new['TEXT2'].append(himikat_kraska.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.хим_пг_к_окр_politeknik_кг_alupol_ac_52)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k == 5:
                                    himikat_kraska = Ximikat.objects.get(id=3)
                                    df_new['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                    df_new['TEXT2'].append(himikat_kraska.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.хим_пг_к_окр_politeknik_кг_pol_ac_25p)*mein_percent)) 
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                    
                                df_new['LGORT'].append(sklad['number_sklad'][p][k])
                        
                            # df_new['STKTX'][j-6+i]=(df_new['TEXT2'][j-4+i])
                            
                older_process['sapcode'] =df[i][4]
                older_process['kratkiy'] =df[i][5]
        else:
            normaexist = CheckNormaBase.objects.filter(artikul=df[i][4],kratkiytekst=df[i][5])[:1].get()
            older_process['sapcode'] =normaexist.artikul
            older_process['kratkiy'] =normaexist.kratkiytekst
            
        norma_existsS = CheckNormaBase.objects.filter(artikul=df[i][6],kratkiytekst=df[i][7]).exists()
        if not norma_existsS:
            if df[i][6] !="":
                CheckNormaBase(artikul=df[i][6],kratkiytekst=df[i][7]).save()
                if (df[i][6].split('-')[1][:1]=='S'):
                    j+=1
                    if (df[i][6].split('-')[1][:1]=='S'):
                        df_new['ID'].append('1')
                        df_new['MATNR'].append(df[i][6])
                        df_new['WERKS'].append('1101')
                        df_new['TEXT1'].append(df[i][7])
                        df_new['STLAL'].append(f'1')
                        df_new['STLAN'].append('1')
                        ztekst = 'Сублимация - Декоративное покрытие'
                        ateks2='Сублимация - '+df[i][7].split('_')[1]
                        df_new['ZTEXT'].append(ztekst)
                        df_new['STKTX'].append(ateks2)
                        df_new['BMENG'].append( '1000')
                        df_new['BMEIN'].append('ШТ')
                        df_new['STLST'].append('1')
                        df_new['POSNR'].append('')
                        df_new['POSTP'].append('')
                        df_new['MATNR1'].append('')
                        df_new['TEXT2'].append('')
                        df_new['MEINS'].append('')
                        df_new['MENGE'].append('')
                        df_new['DATUV'].append('01012021')
                        df_new['PUSTOY'].append('')
                        df_new['LGORT'].append('')
                        length = df[i][6].split('-')[0]
                        
                        alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                        
                        mein_percent =((get_legth(df[i][7]))/float(alum_teks.длина_профиля_м))
                        
                        sublimatsiya_code = df[i][7].split('_')[1]
                        if sublimatsiya_code =='7777':
                            code_ss = alum_teks.суб_ширина_декор_пленки_мм_зол_дуб
                            mein =alum_teks.сублимация_расход_на_1000_профиль_м21
                            
                        elif sublimatsiya_code =='8888':
                            print('exceldagi qator ##### ',i,' #######')
                            code_ss = alum_teks.суб_ширина_декор_пленки_мм_дуб_мокко
                            mein =alum_teks.сублимация_расход_на_1000_профиль_м23
                        elif sublimatsiya_code =='3701':
                            print('exceldagi qator ##### ',i,' #######')
                            code_ss = alum_teks.суб_ширина_декор_пленки_мм_3д_313701
                            mein =alum_teks.сублимация_расход_на_1000_профиль_м22
                        elif sublimatsiya_code =='3702':
                            print('exceldagi qator ##### ',i,' #######')
                            code_ss = alum_teks.суб_ширина_декор_пленки_мм_3д_313702
                            mein =alum_teks.сублимация_расход_на_1000_профиль_м24
                        
                        
                        for k in range(0,4):
                            j+=1
                            df_new['ID'].append('2')
                            df_new['MATNR'].append('')
                            df_new['WERKS'].append('')
                            df_new['TEXT1'].append('')
                            df_new['STLAL'].append('')
                            df_new['STLAN'].append('')
                            df_new['ZTEXT'].append('')
                            df_new['STKTX'].append('')
                            df_new['BMENG'].append('')
                            df_new['BMEIN'].append('')
                            df_new['STLST'].append('')
                            df_new['POSNR'].append(k+1)
                            df_new['POSTP'].append('L')
                            
                            
                            if k == 0 :
                                df_new['MATNR1'].append(older_process['sapcode'])
                                df_new['TEXT2'].append(older_process['kratkiy'])
                                df_new['MEINS'].append('1000')
                                df_new['MENGE'].append('ШТ')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            
                            if k==1:
                                print('sub decor ployka ****** ',sublimatsiya_code,'*****<<shirina=== ',code_ss)
                                subdecor = SubDekorPlonka.objects.get(код_декор_пленки = sublimatsiya_code, ширина_декор_пленки_мм = code_ss)
                                df_new['MATNR1'].append(subdecor.sap_code_s4q100)
                                df_new['TEXT2'].append(subdecor.название)
                                df_new['MENGE'].append('М2')
                                df_new['MEINS'].append( "{:0f}".format(float(mein)*mein_percent))
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            
                            if k==2:
                                skotch = Skotch.objects.get(id=1)
                                df_new['MATNR1'].append(skotch.sap_code_s4q100)
                                df_new['TEXT2'].append(skotch.название)
                                df_new['MENGE'].append("ШТ")
                                df_new['MEINS'].append("{:0f}".format(float(alum_teks.молярный_скотч_рас_на_1000_пр_шт1)*mein_percent))
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            if k == 3:
                                skotch = Skotch.objects.get(id=2)
                                df_new['MATNR1'].append(skotch.sap_code_s4q100)
                                df_new['TEXT2'].append(skotch.название)
                                df_new['MENGE'].append("ШТ")
                                df_new['MEINS'].append("{:0f}".format(float(alum_teks.молярный_скотч_рас_на_1000_пр_шт2)*mein_percent))
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            
                                
                            df_new['LGORT'].append('PS08')
                            
                older_process['sapcode'] =df[i][6]
                older_process['kratkiy'] =df[i][7]
        else:
            normaexist = CheckNormaBase.objects.filter(artikul=df[i][6],kratkiytekst=df[i][7])[:1].get()
            older_process['sapcode'] =normaexist.artikul
            older_process['kratkiy'] =normaexist.kratkiytekst
            
                           
        norma_exists7 = CheckNormaBase.objects.filter(artikul=df[i][8],kratkiytekst=df[i][9]).exists()
        if not norma_exists7:
            if df[i][8] !="":
                CheckNormaBase(artikul=df[i][8],kratkiytekst=df[i][9]).save()
                if (df[i][8].split('-')[1][:1]=='7'):
                    
                    
                    if '_' in df[i][9]:
                        ddd = df[i][9].split()[2]
                    
                    nakleyka_code = df[i][9].split()[-1]
                    length = df[i][8].split('-')[0]
                    
                    
                    alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                    
                    mein_percent =((get_legth(df[i][9]))/float(alum_teks.длина_профиля_м))
                    
                    its_lamination = not ((not '_' in df[i][9]) or ('7777' in ddd.split('_')[1]) or ('8888' in ddd.split('_')[1]) or ('3701' in ddd.split('_')[1]) or ('3702' in ddd.split('_')[1]))
                    
                    if nakleyka_code =='A01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм == alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм != alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0')or(alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)
                                meinss = float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                            elif alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                meinss = float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)+float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                        elif ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni = 5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                            meinss2 =float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                            
                    elif nakleyka_code =='R05':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм=='0'))) 
                        log2 = ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм == '0'))
                        
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            
                            if alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)
                                meinss = float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                            elif alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                        elif log2:
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)[:1].get()
                            meinss1 = float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                            meinss2 = float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                            
                    elif nakleyka_code =='B01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4        
                            if alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                            elif alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                        elif ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                            meinss2 =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                            
                    elif nakleyka_code =='I02':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2)
                            elif alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_ch_вр_и_кг_м_ch_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_ch_вр_и_кг_м_ch_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2)
                        elif ((alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_ch_вр_и_кг_м_ch_бк_ст_рас)
                            meinss2 =float(alum_teks.заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2)
                            
                    elif nakleyka_code =='I01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                            elif alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)+float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                        elif ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                            meinss2 =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                            
                    elif nakleyka_code =='NB1':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                            elif alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                        elif ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                            meinss2 =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                            
                    elif nakleyka_code =='E01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            elif alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                        elif ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                            meinss2 =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                        
                    elif nakleyka_code =='E02':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты and alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты !='0') or ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)and((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)
                                meinss =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            elif alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)+float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                        elif ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)[:1].get()
                            meinss1 =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                            meinss2 =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                        
                    elif (nakleyka_code =='NT1') :
                        qatorlar_soni = 3
                
                    if its_lamination:
                        
                        if nakleyka_code =='A01' :
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм == alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм != alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0')or(alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni = 5
                                if alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                                elif alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)+float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                            elif ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni = 6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,тип_клея__in=['HL','HM'])[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,тип_клея__in=['HL','HM'])[:1].get()
                                meinss1 =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                                meinss2 =float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                                
                        elif nakleyka_code =='R05':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм=='0'))) 
                            log2 = ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм == '0'))
                            
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                                elif alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                            elif log2:
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,тип_клея__in=['HL','HM'])[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,тип_клея__in=['HL','HM'])[:1].get()
                                meinss1 =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                                    
                        elif nakleyka_code =='B01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                                elif alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,тип_клея__in=['HL','HM'])[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,тип_клея__in=['HL','HM'])[:1].get()
                                meinss1 =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                                
                        elif nakleyka_code =='I02':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni = 5
                                if alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2)
                                elif alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.кг_м_ch_вр_и_кг_м_ch_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.кг_м_ch_вр_и_кг_м_ch_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2)
                            elif ((alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм,тип_клея__in=['HL','HM'])[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм,тип_клея__in=['HL','HM'])[:1].get()
                                meinss1 =float(alum_teks.кг_м_ch_вр_и_кг_м_ch_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2)
                                
                        elif nakleyka_code =='I01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                                elif alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)+float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,тип_клея__in=['HL','HM'])[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,тип_клея__in=['HL','HM'])[:1].get()
                                meinss1 =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                                meinss2 =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                                
                        elif nakleyka_code =='NB1':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                                elif alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,тип_клея__in=['HL','HM'])[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,тип_клея__in=['HL','HM'])[:1].get()
                                meinss1 =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                                
                        elif nakleyka_code =='E01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                                elif alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            elif ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм,тип_клея__in=['HL','HM'])[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм,тип_клея__in=['HL','HM'])[:1].get()
                                meinss1 =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            
                        elif nakleyka_code =='E02':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты and alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты !='0') or ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)and((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                                elif alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,тип_клея__in=['HL','HM'])
                                    meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)+float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,тип_клея__in=['HL','HM'])[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты,тип_клея__in=['HL','HM'])[:1].get()
                                meinss1 =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                                meinss2 =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            
                        elif (nakleyka_code =='NT1') :
                            qatorlar_soni = 4
                        
                        
                    ############Laminatsiya
                    
                    
                        
                        
                        
                    
                    if ((not '_' in df[i][9]) or ('7777' in ddd.split('_')[1]) or ('8888' in ddd.split('_')[1]) or ('3701' in ddd.split('_')[1]) or ('3702' in ddd.split('_')[1])):
                        
                        if qatorlar_soni == 3:
                            j+=1
                            df_new['ID'].append('1')
                            df_new['MATNR'].append(df[i][8])
                            df_new['WERKS'].append('1101')
                            df_new['TEXT1'].append(df[i][9])
                            df_new['STLAL'].append('1')
                            df_new['STLAN'].append('1')
                            ztekst = 'Упаковка'
                            df_new['ZTEXT'].append(ztekst)
                            df_new['STKTX'].append(ztekst)
                            df_new['BMENG'].append( '1000')
                            df_new['BMEIN'].append('ШТ')
                            df_new['STLST'].append('1')
                            df_new['POSNR'].append('')
                            df_new['POSTP'].append('')
                            df_new['MATNR1'].append('')
                            df_new['TEXT2'].append('')
                            df_new['MEINS'].append('')
                            df_new['MENGE'].append('')
                            df_new['DATUV'].append('01012021')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('')
                            length = df[i][8].split('-')[0]
                            for k in range(0,qatorlar_soni):
                                j+=1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                
                                
                                if k == 0 :
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new['MATNR1'].append('1000001016')
                                    df_new['TEXT2'].append('Пленка П1 NS12см 60мк Ncolor')
                                    df_new['MENGE'].append('КГ')
                                    df_new['MEINS'].append( "{:0f}".format(float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==2:
                                    df_new['MATNR1'].append('1900000069')
                                    df_new['TEXT2'].append('Скотч 36мм/300м')
                                    df_new['MENGE'].append("ШТ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.рас_скотча_рас_скотча_на_1000_штук_шт)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                df_new['LGORT'].append('PS10')
                        if qatorlar_soni == 4:
                            jjj =0
                            for nakleykaa in nakleyka_results:
                                jjj += 1
                                j+=1
                                df_new['ID'].append('1')
                                df_new['MATNR'].append(df[i][8])
                                df_new['WERKS'].append('1101')
                                df_new['TEXT1'].append(df[i][9])
                                df_new['STLAL'].append(f'{jjj}')
                                df_new['STLAN'].append('1')
                                ztekst = 'Упаковка'
                                df_new['ZTEXT'].append(ztekst)
                                df_new['STKTX'].append(ztekst+' '+nakleykaa.ширина+nakleykaa.еи_ширины+' '+nakleykaa.тип_клея)
                                df_new['BMENG'].append( '1000')
                                df_new['BMEIN'].append('ШТ')
                                df_new['STLST'].append('1')
                                df_new['POSNR'].append('')
                                df_new['POSTP'].append('')
                                df_new['MATNR1'].append('')
                                df_new['TEXT2'].append('')
                                df_new['MEINS'].append('')
                                df_new['MENGE'].append('')
                                df_new['DATUV'].append('01012021')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('')
                                length = df[i][8].split('-')[0]
                                for k in range(0,qatorlar_soni):
                                    j+=1
                                    df_new['ID'].append('2')
                                    df_new['MATNR'].append('')
                                    df_new['WERKS'].append('')
                                    df_new['TEXT1'].append('')
                                    df_new['STLAL'].append('')
                                    df_new['STLAN'].append('')
                                    df_new['ZTEXT'].append('')
                                    df_new['STKTX'].append('')
                                    df_new['BMENG'].append('')
                                    df_new['BMEIN'].append('')
                                    df_new['STLST'].append('')
                                    df_new['POSNR'].append(k+1)
                                    df_new['POSTP'].append('L')
                                    
                                    
                                    if k == 0 :
                                        df_new['MATNR1'].append(older_process['sapcode'])
                                        df_new['TEXT2'].append(older_process['kratkiy'])
                                        df_new['MEINS'].append('1000')
                                        df_new['MENGE'].append('ШТ')
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==1:
                                        df_new['MATNR1'].append('1000001016')
                                        df_new['TEXT2'].append('Пленка П1 NS12см 60мк Ncolor')
                                        df_new['MENGE'].append('КГ')
                                        df_new['MEINS'].append( "{:0f}".format(float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==2:
                                        skotch = Skotch.objects.get(id=1)
                                        df_new['MATNR1'].append('1900000069')
                                        df_new['TEXT2'].append('Скотч 36мм/300м')
                                        df_new['MENGE'].append("ШТ")
                                        df_new['MEINS'].append("{:0f}".format(float(alum_teks.рас_скотча_рас_скотча_на_1000_штук_шт)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==3:
                                        df_new['MATNR1'].append(nakleykaa.sap_code_s4q100)
                                        df_new['TEXT2'].append(nakleykaa.название)
                                        df_new['MENGE'].append("М2")
                                        df_new['MEINS'].append("{:0f}".format((meinss)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    df_new['LGORT'].append('PS10')
                    
                        if qatorlar_soni == 5:
                            j += 1
                            df_new['ID'].append('1')
                            df_new['MATNR'].append(df[i][8])
                            df_new['WERKS'].append('1101')
                            df_new['TEXT1'].append(df[i][9])
                            df_new['STLAL'].append('1')
                            df_new['STLAN'].append('1')
                            ztekst = 'Упаковка'
                            df_new['ZTEXT'].append(ztekst)
                            df_new['STKTX'].append(ztekst)
                            df_new['BMENG'].append( '1000')
                            df_new['BMEIN'].append('ШТ')
                            df_new['STLST'].append('1')
                            df_new['POSNR'].append('')
                            df_new['POSTP'].append('')
                            df_new['MATNR1'].append('')
                            df_new['TEXT2'].append('')
                            df_new['MEINS'].append('')
                            df_new['MENGE'].append('')
                            df_new['DATUV'].append('01012021')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('')
                            length = df[i][8].split('-')[0]
                            for k in range(0,qatorlar_soni):
                                j+=1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                
                                
                                if k == 0 :
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new['MATNR1'].append('1000001016')
                                    df_new['TEXT2'].append('Пленка П1 NS12см 60мк Ncolor')
                                    df_new['MENGE'].append('КГ')
                                    df_new['MEINS'].append( "{:0f}".format(float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==2:
                                    skotch = Skotch.objects.get(id=1)
                                    df_new['MATNR1'].append('1900000069')
                                    df_new['TEXT2'].append('Скотч 36мм/300м')
                                    df_new['MENGE'].append("ШТ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.рас_скотча_рас_скотча_на_1000_штук_шт)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==3:
                                    df_new['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result1.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinss1)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==4:
                                    df_new['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result2.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinss2)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                df_new['LGORT'].append('PS10')
                    
                    else:
                        
                        laminatsiya_code = ddd.split('_')[1].split('/')
                        laminatsiya_code1 = laminatsiya_code[0]
                        laminatsiya_code2 = laminatsiya_code[1]
                        
                        if ((laminatsiya_code1 == laminatsiya_code2) or (laminatsiya_code1 =='XXXX' or laminatsiya_code2 == 'XXXX')):
                            qatorlar_soni +=1
                            
                            if laminatsiya_code1 =='XXXX':
                                meinsL = alum_teks.лам_низ_b_рас_ленты_на_1000_пр_м2
                                laminatsiya =Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code2)[:1].get() 
                            elif laminatsiya_code2 =='XXXX':
                                
                                meinsL = alum_teks.лам_верх_a_рас_ленты_на_1000_пр_м2
                                laminatsiya =Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code1)[:1].get() 
                            elif laminatsiya_code1 == laminatsiya_code2:
                                meinsL = float(alum_teks.лам_верх_a_рас_ленты_на_1000_пр_м2)+float(alum_teks.лам_низ_b_рас_ленты_на_1000_пр_м2)
                                print('lanination kode <<<<< ',laminatsiya_code1,' >>>>>>')
                                laminatsiya =Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code1)[:1].get() 
                                
                        else:
                            qatorlar_soni +=2
                            laminatsiya_result1 = Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code1)[:1].get() 
                            laminatsiya_result2 = Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code2)[:1].get() 
                            meinsL1 = float(alum_teks.лам_верх_a_рас_ленты_на_1000_пр_м2)
                            meinsL2 = float(alum_teks.лам_низ_b_рас_ленты_на_1000_пр_м2)
                            
                        
                        if qatorlar_soni == 5:
                            j+=1
                            df_new['ID'].append('1')
                            df_new['MATNR'].append(df[i][8])
                            df_new['WERKS'].append('1101')
                            df_new['TEXT1'].append(df[i][9])
                            df_new['STLAL'].append('1')
                            df_new['STLAN'].append('1')
                            ztekst = 'Ламинация + Наклейка + Упаковка'
                            df_new['ZTEXT'].append(ztekst)
                            df_new['STKTX'].append(ztekst)
                            df_new['BMENG'].append( '1000')
                            df_new['BMEIN'].append('ШТ')
                            df_new['STLST'].append('1')
                            df_new['POSNR'].append('')
                            df_new['POSTP'].append('')
                            df_new['MATNR1'].append('')
                            df_new['TEXT2'].append('')
                            df_new['MEINS'].append('')
                            df_new['MENGE'].append('')
                            df_new['DATUV'].append('01012021')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('')
                            length = df[i][8].split('-')[0]
                            for k in range(0,qatorlar_soni):
                                j+=1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                
                                
                                if k == 0 :
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new['MATNR1'].append('1300000064')
                                    df_new['TEXT2'].append('KLEIBERIT 704,5')
                                    df_new['MENGE'].append('КГ')
                                    df_new['MEINS'].append( "{:0f}".format(float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==2:
                                    df_new['MATNR1'].append('1300000068')
                                    df_new['TEXT2'].append('KLEIBERIT Primer 831,0')
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==3:
                                    df_new['MATNR1'].append('1000001020')
                                    df_new['TEXT2'].append('Пленка П2 NS35см 140мк Grey1')
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==4:
                                    df_new['MATNR1'].append(laminatsiya.sap_code_s4q100)
                                    df_new['TEXT2'].append(laminatsiya.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinsL)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                df_new['LGORT'].append('PS11')
                        if qatorlar_soni == 6:
                            print('ichida',laminatsiya)
                            jjj =0
                            for nakleykaa in nakleyka_results:
                                jjj += 1
                                j+=1
                                df_new['ID'].append('1')
                                df_new['MATNR'].append(df[i][8])
                                df_new['WERKS'].append('1101')
                                df_new['TEXT1'].append(df[i][9])
                                df_new['STLAL'].append(f'{jjj}')
                                df_new['STLAN'].append('1')
                                ztekst = 'Ламинация + Наклейка + Упаковка'
                                df_new['ZTEXT'].append(ztekst)
                                df_new['STKTX'].append(ztekst+' '+nakleykaa.тип_клея)
                                df_new['BMENG'].append( '1000')
                                df_new['BMEIN'].append('ШТ')
                                df_new['STLST'].append('1')
                                df_new['POSNR'].append('')
                                df_new['POSTP'].append('')
                                df_new['MATNR1'].append('')
                                df_new['TEXT2'].append('')
                                df_new['MEINS'].append('')
                                df_new['MENGE'].append('')
                                df_new['DATUV'].append('01012021')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('')
                                length = df[i][8].split('-')[0]
                                for k in range(0,qatorlar_soni):
                                    j+=1
                                    df_new['ID'].append('2')
                                    df_new['MATNR'].append('')
                                    df_new['WERKS'].append('')
                                    df_new['TEXT1'].append('')
                                    df_new['STLAL'].append('')
                                    df_new['STLAN'].append('')
                                    df_new['ZTEXT'].append('')
                                    df_new['STKTX'].append('')
                                    df_new['BMENG'].append('')
                                    df_new['BMEIN'].append('')
                                    df_new['STLST'].append('')
                                    df_new['POSNR'].append(k+1)
                                    df_new['POSTP'].append('L')
                                    
                                    
                                    if k == 0 :
                                        df_new['MATNR1'].append(older_process['sapcode'])
                                        df_new['TEXT2'].append(older_process['kratkiy'])
                                        df_new['MEINS'].append('1000')
                                        df_new['MENGE'].append('ШТ')
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==1:
                                        df_new['MATNR1'].append('1300000064')
                                        df_new['TEXT2'].append('KLEIBERIT 704,5')
                                        df_new['MENGE'].append('КГ')
                                        df_new['MEINS'].append( "{:0f}".format(float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==2:
                                        df_new['MATNR1'].append('1300000068')
                                        df_new['TEXT2'].append('KLEIBERIT Primer 831,0')
                                        df_new['MENGE'].append("КГ")
                                        df_new['MEINS'].append("{:0f}".format(float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==3:
                                        df_new['MATNR1'].append('1000001020')
                                        df_new['TEXT2'].append('Пленка П2 NS35см 140мк Grey1')
                                        df_new['MENGE'].append("КГ")
                                        df_new['MEINS'].append("{:0f}".format(float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==4:
                                        
                                        df_new['MATNR1'].append(nakleykaa.sap_code_s4q100)
                                        df_new['TEXT2'].append(nakleykaa.название)
                                        df_new['MENGE'].append("М2")
                                        df_new['MEINS'].append("{:0f}".format((meinss*mein_percent)))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==5:
                                        
                                        df_new['MATNR1'].append(laminatsiya.sap_code_s4q100)
                                        df_new['TEXT2'].append(laminatsiya.название)
                                        df_new['MENGE'].append("М2")
                                        df_new['MEINS'].append(float(meinsL)*mein_percent)
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    df_new['LGORT'].append('PS11')
                    
                        if qatorlar_soni == 7:
                            j+=1
                            df_new['ID'].append('1')
                            df_new['MATNR'].append(df[i][8])
                            df_new['WERKS'].append('1101')
                            df_new['TEXT1'].append(df[i][9])
                            df_new['STLAL'].append(f'1')
                            df_new['STLAN'].append('1')
                            ztekst = 'Ламинация + Наклейка + Упаковка'
                            df_new['ZTEXT'].append(ztekst)
                            df_new['STKTX'].append(ztekst)
                            df_new['BMENG'].append( '1000')
                            df_new['BMEIN'].append('ШТ')
                            df_new['STLST'].append('1')
                            df_new['POSNR'].append('')
                            df_new['POSTP'].append('')
                            df_new['MATNR1'].append('')
                            df_new['TEXT2'].append('')
                            df_new['MEINS'].append('')
                            df_new['MENGE'].append('')
                            df_new['DATUV'].append('01012021')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('')
                            length = df[i][8].split('-')[0]
                            for k in range(0,qatorlar_soni):
                                j+=1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                
                                
                                if k == 0 :
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new['MATNR1'].append('1300000064')
                                    df_new['TEXT2'].append('KLEIBERIT 704,5')
                                    df_new['MENGE'].append('КГ')
                                    df_new['MEINS'].append( "{:0f}".format(float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==2:
                                    df_new['MATNR1'].append('1300000068')
                                    df_new['TEXT2'].append('KLEIBERIT Primer 831,0')
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==3:
                                    df_new['MATNR1'].append('1000001020')
                                    df_new['TEXT2'].append('Пленка П2 NS35см 140мк Grey1')
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==4:
                                    df_new['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result1.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinss1)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k==5:
                                    df_new['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result2.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinss2)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==6:
                                    
                                    df_new['MATNR1'].append(laminatsiya.sap_code_s4q100)
                                    df_new['TEXT2'].append(laminatsiya.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinsL)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                df_new['LGORT'].append('PS11')
                    
                        if qatorlar_soni == 8:
                            j += 1
                            df_new['ID'].append('1')
                            df_new['MATNR'].append(df[i][8])
                            df_new['WERKS'].append('1101')
                            df_new['TEXT1'].append(df[i][9])
                            df_new['STLAL'].append('1')
                            df_new['STLAN'].append('1')
                            ztekst = 'Ламинация + Наклейка + Упаковка'
                            df_new['ZTEXT'].append(ztekst)
                            df_new['STKTX'].append(ztekst)
                            df_new['BMENG'].append( '1000')
                            df_new['BMEIN'].append('ШТ')
                            df_new['STLST'].append('1')
                            df_new['POSNR'].append('')
                            df_new['POSTP'].append('')
                            df_new['MATNR1'].append('')
                            df_new['TEXT2'].append('')
                            df_new['MEINS'].append('')
                            df_new['MENGE'].append('')
                            df_new['DATUV'].append('01012021')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('')
                            length = df[i][8].split('-')[0]
                            for k in range(0,qatorlar_soni):
                                j+=1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                
                                
                                if k == 0 :
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new['MATNR1'].append('1300000064')
                                    df_new['TEXT2'].append('KLEIBERIT 704,5')
                                    df_new['MENGE'].append('КГ')
                                    df_new['MEINS'].append( "{:0f}".format(float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==2:
                                    df_new['MATNR1'].append('1300000068')
                                    df_new['TEXT2'].append('KLEIBERIT Primer 831,0')
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==3:
                                    df_new['MATNR1'].append('1000001020')
                                    df_new['TEXT2'].append('Пленка П2 NS35см 140мк Grey1')
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==4:
                                    df_new['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result1.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinss1)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k==5:
                                    df_new['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result2.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinss1)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k == 6:
                                    df_new['MATNR1'].append(laminatsiya_result1.sap_code_s4q100)
                                    df_new['TEXT2'].append(laminatsiya_result1.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinsL1)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k == 7:
                                    df_new['MATNR1'].append(laminatsiya_result2.sap_code_s4q100)
                                    df_new['TEXT2'].append(laminatsiya_result2.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinsL2)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                df_new['LGORT'].append('PS11')
                    
                    
                    
                older_process['sapcode'] =df[i][8]
                older_process['kratkiy'] =df[i][9]
                
                        
                        
        
    # for key,val in df_new.items():
    #     print(key,len(val)) 
    # print(df_new)
    dff =pd.DataFrame(df_new)
    path =os.path.join(os.path.expanduser("~/Desktop"),'new_base.xlsx')
    
    dff.to_excel(path)
    return JsonResponse({'a':'b'})
    
######### Integratsiya 2 ########
def kombinirovaniy_process(request,id):
    file = NormaExcelFiles.objects.get(id=id).file
    file_path =f'{MEDIA_ROOT}\\{file}'
    df_exell = pd.read_excel(file_path)
    df_exell = df_exell.fillna('')
    df_exell =df_exell.astype(str)
    
    
    product_type = request.GET.get('type','termo')
        
    df = []
    
    norma_list,kraska_list = norma_for_list()
    
    check_for_existing =[]
    for key,row in df_exell.iterrows():
        df.append([
            row['SAP код E'],row['Экструзия холодная резка'],
            row['SAP код Z'],row['Печь старения'],
            row['SAP код P'],row['Покраска автомат'],
            row['SAP код S'],row['Сублимация'],
            row['SAP код N'],row['Наклейка'],
            row['SAP код K'],row['K-Комбинирования'],
            row['SAP код 7'],row['U-Упаковка + Готовая Продукция']
        ])
        
    norma = []
    alumniy_silindr = []
    
    subdekor = []
    kraska =[]
    nakleyka_N = []
    kombinirovanniy = []
    isklyucheniye_ids = []
    k = -1
    for fullsapkod in df:
        k += 1
        for i in range(0,7):
            t= fullsapkod[i * 2]
            length = fullsapkod[i * 2].split('-')
            
            if fullsapkod[i * 2]!='':
                if length[0] not in  norma_list:
                    isklyucheniye_ids.append(k)
                    if length[0] not in norma:
                        norma.append(length[0])
                
                if (('-E' in t) or ('-P' in t) and (length[0] not in norma)):
                    if '-P' in t:
                        kraska_code = fullsapkod[i*2+1].split()[-1]
                        if kraska_code!='MF':
                            if kraska_code not in kraska_list:
                                isklyucheniye_ids.append(k) 
                                if kraska_code not in  kraska:                                  
                                    kraska.append(kraska_code) 
                                    
                    alum_teks_all = Norma.objects.filter(Q(компонент_1=length[0])|Q(компонент_2=length[0])|Q(компонент_3=length[0])|Q(артикул=length[0]))
                    alum_teks = alum_teks_all[:1].get()
                    if '178' in alum_teks.алю_сплав_биллетов_102_178:
                        if not AlyuminniysilindrEkstruziya1.objects.filter(тип =alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064,название__icontains='178').exists():
                            isklyucheniye_ids.append(k)
                            if [length[0],alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064,{'norma soni':len(alum_teks_all)}] not in alumniy_silindr:
                                alumniy_silindr.append([length[0],alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064,{'norma soni':len(alum_teks_all)}])
                    elif '102' in alum_teks.алю_сплав_биллетов_102_178:
                        if not AlyuminniysilindrEkstruziya1.objects.filter(тип =alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064,название__icontains='102').exists():
                            isklyucheniye_ids.append(k)
                            if [length[0],alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064,{'norma soni':len(alum_teks_all)}] not in alumniy_silindr:
                                alumniy_silindr.append([length[0],alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064,{'norma soni':len(alum_teks_all)}])
                    else:
                        if [length[0],alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064,{'norma soni':len(alum_teks_all)}] not in alumniy_silindr:
                            isklyucheniye_ids.append(k)
                            alumniy_silindr.append([length[0],alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064,{'norma soni':len(alum_teks_all)}])
                
                if (('-S' in t) and (length[0] not in norma)) :
                    sublimatsiya_code = fullsapkod[i * 2+1].split('_')[1]
                    if sublimatsiya_code =='7777':
                        code_ss = alum_teks.суб_ширина_декор_пленки_мм_зол_дуб
                        
                    elif sublimatsiya_code =='8888':
                        code_ss = alum_teks.суб_ширина_декор_пленки_мм_дуб_мокко

                    elif sublimatsiya_code =='3701':
                        code_ss = alum_teks.суб_ширина_декор_пленки_мм_3д_313701
                        
                    elif sublimatsiya_code =='3702':
                        code_ss = alum_teks.суб_ширина_декор_пленки_мм_3д_313702
                    if not SubDekorPlonka.objects.filter(код_декор_пленки = sublimatsiya_code, ширина_декор_пленки_мм = code_ss).exists():
                        isklyucheniye_ids.append(k) 
                        if [sublimatsiya_code,code_ss,length[0]] not in subdekor:
                            subdekor.append([sublimatsiya_code,code_ss,length[0]])
                
                if ((('-N' in t) or ('-7' in t)) and (length[0] not in norma)):
                    norma_1 = Norma.objects.filter(Q(компонент_1=length[0])|Q(компонент_2=length[0])|Q(компонент_3=length[0])|Q(артикул=length[0]))[:1].get()
                    nakleyka_code = fullsapkod[i * 2+1].split()[-1]
                    
                    ###############
                    if nakleyka_code =='A01':
                        aluminiy_norma_log = (norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм == norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм and norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм != '0') or ((norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм != norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)and((norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0')or(norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм=='0')))
                        if aluminiy_norma_log:
                            if norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'A01',ширина= norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,'niz':True,'verx':False} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,'niz':True,'verx':False})
                            elif norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'A01',ширина= norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,'niz':False,'verx':True} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,'niz':False,'verx':True})
                            else:
                                if not Nakleyka.objects.filter(код_наклейки = 'A01',ширина= norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,'niz':True,'verx':True} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,'niz':True,'verx':True})
                        elif ((norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0') and (norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм == '0')):
                            isklyucheniye_ids.append(k)
                            if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,'niz':True,'verx':True} not in nakleyka_N:
                                nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,'niz':True,'verx':True})
                        else:
                            if ((not Nakleyka.objects.filter(код_наклейки = 'A01',ширина= norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм).exists()) and (not Nakleyka.objects.filter(код_наклейки = 'A01',ширина= norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм).exists())):
                                isklyucheniye_ids.append(k)
                                if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,'niz':True,'verx':True} not in nakleyka_N:
                                    nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_akfa_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_akfa_верх_ширина_ленты_мм,'niz':True,'verx':True})
                    
                    elif nakleyka_code =='R05':
                        aluminiy_norma_log = (norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм == norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм and norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм != '0') or ((norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм != norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)and((norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм =='0')or(norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм=='0')))
                        if aluminiy_norma_log:
                            if norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'R05',ширина= norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,'niz':True,'verx':False} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,'niz':True,'verx':False})
                            elif norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'R05',ширина= norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,'niz':False,'verx':True} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,'niz':False,'verx':True})
                            else:
                                if not Nakleyka.objects.filter(код_наклейки = 'R05',ширина= norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,'niz':True,'verx':True} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,'niz':True,'verx':True})
                        elif ((norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм =='0') and (norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм == '0')):
                            isklyucheniye_ids.append(k)
                            if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,'niz':True,'verx':True} not in nakleyka_N:
                                nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,'niz':True,'verx':True})
                        else:
                            if ((not Nakleyka.objects.filter(код_наклейки = 'R05',ширина= norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм).exists()) and (not Nakleyka.objects.filter(код_наклейки = 'R05',ширина= norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм).exists())):
                                isklyucheniye_ids.append(k)
                                if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,'niz':True,'verx':True} not in nakleyka_N:
                                    nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_retpen_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_retpen_верх_ширина_ленты_мм,'niz':True,'verx':True})
                        
                    elif nakleyka_code =='B01':
                        aluminiy_norma_log = (norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм == norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм and norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм != '0') or ((norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм != norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)and((norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм =='0')or(norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            if norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'B01',ширина= norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,'niz':True,'verx':False} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,'niz':True,'verx':False})
                            elif norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'B01',ширина= norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,'niz':False,'verx':True} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,'niz':False,'verx':True})
                            else:
                                if not Nakleyka.objects.filter(код_наклейки = 'B01',ширина= norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,'niz':True,'verx':True} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,'niz':True,'verx':True})
                        elif ((norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм =='0') and (norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм == '0')):
                            isklyucheniye_ids.append(k)
                            if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,'niz':True,'verx':True} not in nakleyka_N:
                                nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,'niz':True,'verx':True})
                        else:
                            if ((not Nakleyka.objects.filter(код_наклейки = 'B01',ширина= norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм).exists()) and (not Nakleyka.objects.filter(код_наклейки = 'B01',ширина= norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм).exists())):
                                isklyucheniye_ids.append(k)
                                if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,'niz':True,'verx':True} not in nakleyka_N:
                                    nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм,'niz':True,'verx':True})
                     
                    elif nakleyka_code =='I02':
                        aluminiy_norma_log = (norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм == norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм and norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм != '0') or ((norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм != norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм)and((norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм =='0')or(norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            if norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'I02',ширина= norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм,'niz':True,'verx':False} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм,'niz':True,'verx':False})
                            elif norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'I02',ширина= norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм,'niz':False,'verx':True} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм,'niz':False,'verx':True})
                            else:
                                if not Nakleyka.objects.filter(код_наклейки = 'I02',ширина= norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм,'niz':True,'verx':True} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм,'niz':True,'verx':True})
                        elif ((norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм =='0') and (norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм == '0')):
                            isklyucheniye_ids.append(k)
                            if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм,'niz':True,'verx':True} not in nakleyka_N:
                                nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм,'niz':True,'verx':True})
                        else:
                            if ((not Nakleyka.objects.filter(код_наклейки = 'I02',ширина= norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм).exists()) and (not Nakleyka.objects.filter(код_наклейки = 'I02',ширина= norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм).exists())):
                                isklyucheniye_ids.append(k)
                                if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм,'niz':True,'verx':True} not in nakleyka_N:
                                    nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_ch_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_ch_вр_ширина_лн_мм,'niz':True,'verx':True})
                         
                    elif nakleyka_code =='I01':
                        aluminiy_norma_log = (norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм == norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм and norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм != '0') or ((norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм != norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)and((norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =='0')or(norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            if norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'I01',ширина= norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,'niz':True,'verx':False} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,'niz':True,'verx':False})
                            elif norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'I01',ширина= norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,'niz':False,'verx':True} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,'niz':False,'verx':True})
                            else:
                                if not Nakleyka.objects.filter(код_наклейки = 'I01',ширина= norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,'niz':True,'verx':True} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,'niz':True,'verx':True})
                        elif ((norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =='0') and (norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм == '0')):
                            isklyucheniye_ids.append(k)
                            if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,'niz':True,'verx':True} not in nakleyka_N:
                                nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,'niz':True,'verx':True})
                        else:
                            if ((not Nakleyka.objects.filter(код_наклейки = 'I01',ширина= norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм).exists()) and (not Nakleyka.objects.filter(код_наклейки = 'I01',ширина= norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм).exists())):
                                isklyucheniye_ids.append(k)
                                if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,'niz':True,'verx':True} not in nakleyka_N:
                                    nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм,'niz':True,'verx':True})
                                     
                    elif nakleyka_code =='NB1':
                        aluminiy_norma_log = (norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм == norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм and norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм != '0') or ((norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм != norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)and((norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм =='0')or(norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            if norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,'niz':True,'verx':False} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,'niz':True,'verx':False})
                            elif norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,'niz':False,'verx':True} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,'niz':False,'verx':True})
                            else:
                                if not Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,'niz':True,'verx':True} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,'niz':True,'verx':True})
                        elif ((norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм =='0') and (norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм == '0')):
                            isklyucheniye_ids.append(k)
                            if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,'niz':True,'verx':True} not in nakleyka_N:
                                nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,'niz':True,'verx':True})
                        else:
                            if ((not Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм).exists()) and (not Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм).exists())):
                                isklyucheniye_ids.append(k)
                                if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,'niz':True,'verx':True} not in nakleyka_N:
                                    nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_без_бр_низ_ширина_лн_мм,'shirina_verx':norma_1.заш_пл_кг_м_без_бр_вр_ширина_лн_мм,'niz':True,'verx':True})
                    
                    elif nakleyka_code =='E01':
                        aluminiy_norma_log = (norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм == norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм and norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм != '0') or ((norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм != norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм)and((norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм =='0')or(norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм=='0')))
                        if aluminiy_norma_log:
                            if norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'E01',ширина= norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,'niz':True,'verx':False} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,'niz':True,'verx':False})
                            elif norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'E01',ширина= norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,'niz':False,'verx':True} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,'niz':False,'verx':True})
                            else:
                                if not Nakleyka.objects.filter(код_наклейки = 'E01',ширина= norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,'niz':True,'verx':True} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,'niz':True,'verx':True})
                        elif ((norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм =='0') and (norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм == '0')):
                            isklyucheniye_ids.append(k)
                            if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,'niz':True,'verx':True} not in nakleyka_N:
                                nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,'niz':True,'verx':True})
                        else:
                            if ((not Nakleyka.objects.filter(код_наклейки = 'E01',ширина= norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм).exists()) and (not Nakleyka.objects.filter(код_наклейки = 'E01',ширина= norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм).exists())):
                                isklyucheniye_ids.append(k)
                                if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,'niz':True,'verx':True} not in nakleyka_N:
                                    nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_низ_ширина_ленты_мм,'shirina_verx':norma_1.заш_пл_кг_м_eng_верх_ширина_ленты_мм,'niz':True,'verx':True})
                          
                    elif nakleyka_code =='E02':
                        aluminiy_norma_log = (norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм == norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты and norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты != '0') or ((norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм != norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты)and((norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =='0')or(norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты=='0')))
                        if aluminiy_norma_log:
                            if norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'E02',ширина= norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,'shirina_verx':norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,'niz':True,'verx':False} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,'shirina_verx':norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,'niz':True,'verx':False})
                            elif norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты =='0':
                                if not Nakleyka.objects.filter(код_наклейки = 'E02',ширина= norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,'shirina_verx':norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,'niz':False,'verx':True} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,'shirina_verx':norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,'niz':False,'verx':True})
                            else:
                                if not Nakleyka.objects.filter(код_наклейки = 'E02',ширина= norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм).exists():
                                    isklyucheniye_ids.append(k)
                                    if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,'shirina_verx':norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,'niz':True,'verx':True} not in nakleyka_N:
                                        nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,'shirina_verx':norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,'niz':True,'verx':True})
                        elif ((norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =='0') and (norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты == '0')):
                            isklyucheniye_ids.append(k)
                            if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,'shirina_verx':norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,'niz':True,'verx':True} not in nakleyka_N:
                                nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,'shirina_verx':norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,'niz':True,'verx':True})
                        else:
                            if ((not Nakleyka.objects.filter(код_наклейки = 'E02',ширина= norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм).exists()) and (not Nakleyka.objects.filter(код_наклейки = 'E02',ширина= norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты).exists())):
                                isklyucheniye_ids.append(k)
                                if {'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,'shirina_verx':norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,'niz':True,'verx':True} not in nakleyka_N:
                                    nakleyka_N.append({'sap_code':length[0],'nakleyka_code':nakleyka_code,'shirina_niz':norma_1.заш_пл_кг_м_eng_qora_низ_ширина_ленты,'shirina_verx':norma_1.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм,'niz':True,'verx':True})
                
                if (('-K' in t) and (length[0] not in norma)):
                    
                    if not KombinirovaniyUtilsInformation.objects.filter(artikul=length[0]):
                        isklyucheniye_ids.append(k)
                        if length[0] not in kombinirovanniy:
                            kombinirovanniy.append(length[0])
                            
                              
    existing = norma + alumniy_silindr + subdekor + kraska + nakleyka_N + kombinirovanniy
    
    if len(existing) > 0 : 
        create_csv_file(norma,alumniy_silindr,subdekor,kraska,nakleyka_N,kombinirovanniy,str(product_type))                          
        # return JsonResponse({'norma':norma,'aluminiy silindr':alumniy_silindr,'subdecor':subdekor,'kraska':kraska,'nakleyka':nakleyka_N,'kombinirovanniy':kombinirovanniy})
    
    df_new ={
        'ID':[],
        'MATNR': [],
        'WERKS':[],
        'TEXT1':[],
        'STLAL':[],
        'STLAN':[],
        'ZTEXT':[],
        'STKTX':[],
        'BMENG':[],
        'BMEIN':[],
        'STLST':[],
        'POSNR':[],
        'POSTP':[],
        'MATNR1':[],
        'TEXT2':[],
        'MEINS':[],
        'MENGE':[],
        'DATUV':[],
        'PUSTOY':[],
        'LGORT':[]
    }
    
    j = 0
    
    print(isklyucheniye_ids)
    for i in range(0,len(df)):
        print('created i= ',i)
        if i in isklyucheniye_ids:
            continue
        older_process ={'sapcode':'','kratkiy':''}
        norma_existsE = CheckNormaBase.objects.filter(artikul=df[i][0],kratkiytekst=df[i][1]).exists()
        if not norma_existsE:
            if df[i][0] !="":
                CheckNormaBase(artikul=df[i][0],kratkiytekst=df[i][1]).save()
                older_process['sapcode'] =df[i][0]
                older_process['kratkiy'] =df[i][1]
                if df[i][0].split('-')[1][:1]=='E':
                    df_new['ID'].append('1')
                    df_new['MATNR'].append(df[i][0])
                    df_new['WERKS'].append('1101')
                    df_new['TEXT1'].append(df[i][1])
                    df_new['STLAL'].append('1')
                    df_new['STLAN'].append('1')
                    if df[i][0].split('-')[1][:1]=='E':
                        ztekst ='Экструзия (пресс) + Пила'
                    df_new['ZTEXT'].append(ztekst)
                    length = df[i][0].split('-')[0]
                    alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                    
                    if '178' in alum_teks.алю_сплав_биллетов_102_178:
                        aliminisi = AlyuminniysilindrEkstruziya1.objects.filter(тип =alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064,название__icontains='178')[:1].get()
                    elif '102' in alum_teks.алю_сплав_биллетов_102_178:
                        aliminisi = AlyuminniysilindrEkstruziya1.objects.filter(тип =alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064,название__icontains='102')[:1].get()
                    
                    mein_percent =((get_legth(df[i][1]))/float(alum_teks.длина_профиля_м))
                    df_new['STKTX'].append(aliminisi.название)
                    df_new['BMENG'].append( '1000')
                    df_new['BMEIN'].append('ШТ')
                    df_new['STLST'].append('1')
                    df_new['POSNR'].append('')
                    df_new['POSTP'].append('')
                    df_new['MATNR1'].append('')
                    df_new['TEXT2'].append('')
                    df_new['MEINS'].append('')
                    df_new['MENGE'].append('')
                    df_new['DATUV'].append('01012021')
                    df_new['PUSTOY'].append('')
                    df_new['LGORT'].append('')
                    for k in range(1,6):
                        j+=1
                        df_new['ID'].append('2')
                        df_new['MATNR'].append('')
                        df_new['WERKS'].append('')
                        df_new['TEXT1'].append('')
                        df_new['STLAL'].append('')
                        df_new['STLAN'].append('')
                        df_new['ZTEXT'].append('')
                        df_new['STKTX'].append('')
                        df_new['BMENG'].append('')
                        df_new['BMEIN'].append('')
                        df_new['STLST'].append('')
                        df_new['POSNR'].append(k)
                        df_new['POSTP'].append('L')
                        
                        
                        if k == 1 :
                            
                            df_new['MATNR1'].append(aliminisi.sap_code_s4q100)
                            df_new['TEXT2'].append(aliminisi.название)
                            df_new['MEINS'].append("{:0f}".format(float(alum_teks.алю_сп_6063_рас_спа_на_1000_шт_пр_кг)*mein_percent))
                            df_new['MENGE'].append('КГ')
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        
                        if k==2:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=1)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append( "{:0f}".format(float(alum_teks.смазка_для_пресса_кг_графитовая)*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k==3:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=2)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append("{:0f}".format((float(alum_teks.смазка_для_пресса_кг_пилы_хл_резки_сол) + float(alum_teks.смазка_для_пресса_кг_горячей_резки_сол))*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k == 4:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=3)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append("{:0f}".format(float(alum_teks.смазка_для_пресса_кг_графитовые_плиты)*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k == 5:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=4)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append("{:0f}".format(((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода1)+float(alum_teks.алю_сплав_6063_при_этом_тех_отхода2)))*mein_percent)) 
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                            
                        df_new['LGORT'].append('PS01')
                    
                    # j+=1
                    # df_new['ID'].append('1')
                    # df_new['MATNR'].append( df[i][0])
                    # df_new['WERKS'].append('1101')
                    # df_new['TEXT1'].append(df[i][1])
                    # df_new['STLAL'].append('2')
                    # df_new['STLAN'].append('1')
                
                    # if df[i][0].split('-')[1][:1]=='E':
                    #     ztekst='Экструзия (пресс) + Пила'
                    # df_new['ZTEXT'].append( ztekst)
                    # length = df[i][0].split('-')[0]
                    
                    # alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                    # aliminisi =AlyuminniysilindrEkstruziya1.objects.filter(тип =alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064)[1:2].get()       
                    # df_new['STKTX'].append(aliminisi.название)
                    # df_new['BMENG'].append( '1000')
                    # df_new['BMEIN'].append('ШТ')
                    # df_new['STLST'].append('1')
                    # df_new['POSNR'].append('')
                    # df_new['POSTP'].append('')
                    # df_new['MATNR1'].append('')
                    # df_new['TEXT2'].append('')
                    # df_new['MEINS'].append('')
                    # df_new['MENGE'].append('')
                    # df_new['DATUV'].append('01012021')
                    # df_new['PUSTOY'].append('')
                    # df_new['LGORT'].append('')
                    # for k in range(1,6):
                    #     j+=1
                    #     df_new['ID'].append( '2')
                    #     df_new['MATNR'].append( '')
                    #     df_new['WERKS'].append( '')
                    #     df_new['TEXT1'].append( '')
                    #     df_new['STLAL'].append( '')
                    #     df_new['STLAN'].append( '')
                    #     df_new['ZTEXT'].append( '')
                    #     df_new['STKTX'].append( '')
                    #     df_new['BMENG'].append( '')
                    #     df_new['BMEIN'].append('')
                    #     df_new['STLST'].append('')
                    #     df_new['POSNR'].append(k)
                    #     df_new['POSTP'].append('L')
                    #     if k == 1 :
                    #         df_new['MATNR1'].append(aliminisi.sap_code_s4q100)
                    #         df_new['TEXT2'].append(aliminisi.название)
                    #         df_new['MEINS'].append( "{:0f}".format(float(alum_teks.алю_сп_6063_рас_спа_на_1000_шт_пр_кг)*mein_percent))
                    #         df_new['MENGE'].append( 'КГ')
                    #         df_new['DATUV'].append('')
                    #         df_new['PUSTOY'].append('')
                        
                    #     if k==2:
                    #         alummm = AlyuminniysilindrEkstruziya2.objects.first()
                    #         df_new['MATNR1'].append(alummm.sap_code_s4q100)
                    #         df_new['TEXT2'].append(alummm.название)
                    #         df_new['MENGE'].append(alummm.еи)
                    #         df_new['MEINS'].append( "{:0f}".format(float(alum_teks.смазка_для_пресса_кг_графитовая)*mein_percent))
                    #         df_new['DATUV'].append('')
                    #         df_new['PUSTOY'].append('')
                    #     if k==3:
                    #         alummm = AlyuminniysilindrEkstruziya2.objects.get(id=2)
                    #         df_new['MATNR1'].append(alummm.sap_code_s4q100)
                    #         df_new['TEXT2'].append(alummm.название)
                    #         df_new['MENGE'].append(alummm.еи)
                    #         df_new['MEINS'].append( "{:0f}".format((float(alum_teks.смазка_для_пресса_кг_пилы_хл_резки_сол) + float(alum_teks.смазка_для_пресса_кг_горячей_резки_сол))*mein_percent))
                    #         df_new['DATUV'].append('')
                    #         df_new['PUSTOY'].append('')
                    #     if k == 4:
                    #         alummm = AlyuminniysilindrEkstruziya2.objects.get(id=3)
                    #         df_new['MATNR1'].append(alummm.sap_code_s4q100)
                    #         df_new['TEXT2'].append(alummm.название)
                    #         df_new['MENGE'].append(alummm.еи)
                    #         df_new['MEINS'].append( "{:0f}".format(float(alum_teks.смазка_для_пресса_кг_графитовые_плиты)*mein_percent))
                    #         df_new['DATUV'].append('')
                    #         df_new['PUSTOY'].append('')
                    #     if k == 5:
                    #         alummm = AlyuminniysilindrEkstruziya2.objects.get(id=4)
                    #         df_new['MATNR1'].append(alummm.sap_code_s4q100)
                    #         df_new['TEXT2'].append(alummm.название)
                    #         df_new['MENGE'].append(alummm.еи)
                    #         df_new['MEINS'].append( "{:0f}".format(((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода1)+float(alum_teks.алю_сплав_6063_при_этом_тех_отхода2)))*mein_percent))
                    #         df_new['DATUV'].append('')
                    #         df_new['PUSTOY'].append('')
                    #     df_new['LGORT'].append('PS01')
        else:
            normaexist = CheckNormaBase.objects.filter(artikul=df[i][0],kratkiytekst=df[i][1])[:1].get()
            older_process['sapcode'] =normaexist.artikul
            older_process['kratkiy'] =normaexist.kratkiytekst
                    
                
        norma_existsZ = CheckNormaBase.objects.filter(artikul=df[i][2],kratkiytekst=df[i][3]).exists()
        if not norma_existsZ:
            if df[i][2] !="":
                print(df[i][2])
                CheckNormaBase(artikul=df[i][2],kratkiytekst=df[i][3]).save()
                older_process['sapcode'] =df[i][2]
                older_process['kratkiy'] =df[i][3]  
                j+=1
                if (df[i][2].split('-')[1][:1]=='Z'):
                    df_new['ID'].append('1')
                    df_new['MATNR'].append(df[i][2])
                    df_new['WERKS'].append('1101')
                    df_new['TEXT1'].append(df[i][3])
                    df_new['STLAL'].append('1')
                    df_new['STLAN'].append('1')
                    if df[i][2].split('-')[1][:1]=='Z':
                        ztekst ='Экструзия (пресс) + Пила + Старение'
                    df_new['ZTEXT'].append(ztekst)
                    length = df[i][2].split('-')[0]
                    
                    alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                    
                    if '178' in alum_teks.алю_сплав_биллетов_102_178:
                        aliminisi =AlyuminniysilindrEkstruziya1.objects.filter(тип =alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064,название__icontains='178')[:1].get()
                    elif '102' in alum_teks.алю_сплав_биллетов_102_178:
                        aliminisi =AlyuminniysilindrEkstruziya1.objects.filter(тип =alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064,название__icontains='102')[:1].get()
                    
                    
                    mein_percent =((get_legth(df[i][3]))/float(alum_teks.длина_профиля_м))
                    df_new['STKTX'].append(aliminisi.название)
                    df_new['BMENG'].append( '1000')
                    df_new['BMEIN'].append('ШТ')
                    df_new['STLST'].append('1')
                    df_new['POSNR'].append('')
                    df_new['POSTP'].append('')
                    df_new['MATNR1'].append('')
                    df_new['TEXT2'].append('')
                    df_new['MEINS'].append('')
                    df_new['MENGE'].append('')
                    df_new['DATUV'].append('01012021')
                    df_new['PUSTOY'].append('')
                    df_new['LGORT'].append('')
                    
                    for k in range(1,6):
                        j+=1
                        df_new['ID'].append('2')
                        df_new['MATNR'].append('')
                        df_new['WERKS'].append('')
                        df_new['TEXT1'].append('')
                        df_new['STLAL'].append('')
                        df_new['STLAN'].append('')
                        df_new['ZTEXT'].append('')
                        df_new['STKTX'].append('')
                        df_new['BMENG'].append('')
                        df_new['BMEIN'].append('')
                        df_new['STLST'].append('')
                        df_new['POSNR'].append(k)
                        df_new['POSTP'].append('L')
                        
                        
                        if k == 1 :
                            df_new['MATNR1'].append(aliminisi.sap_code_s4q100)
                            df_new['TEXT2'].append(aliminisi.название)
                            df_new['MEINS'].append("{:0f}".format(float(alum_teks.алю_сп_6063_рас_спа_на_1000_шт_пр_кг)*mein_percent))
                            df_new['MENGE'].append('КГ')
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        
                        if k==2:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=1)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append( "{:0f}".format(float(alum_teks.смазка_для_пресса_кг_графитовая)*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k==3:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=2)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append("{:0f}".format((float(alum_teks.смазка_для_пресса_кг_пилы_хл_резки_сол) + float(alum_teks.смазка_для_пресса_кг_горячей_резки_сол))*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k == 4:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=3)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append("{:0f}".format(float(alum_teks.смазка_для_пресса_кг_графитовые_плиты)*mein_percent))
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                        if k == 5:
                            alummm = AlyuminniysilindrEkstruziya2.objects.get(id=4)
                            df_new['MATNR1'].append(alummm.sap_code_s4q100)
                            df_new['TEXT2'].append(alummm.название)
                            df_new['MENGE'].append(alummm.еи)
                            df_new['MEINS'].append("{:0f}".format(((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода1)+float(alum_teks.алю_сплав_6063_при_этом_тех_отхода2)))*mein_percent)) 
                            df_new['DATUV'].append('')
                            df_new['PUSTOY'].append('')
                            
                        df_new['LGORT'].append('PS01')

                    
                    
                    # j+=1
                    # df_new['ID'].append('1')
                    # df_new['MATNR'].append( df[i][2])
                    # df_new['WERKS'].append('1101')
                    # df_new['TEXT1'].append(df[i][3])
                    # df_new['STLAL'].append('2')
                    # df_new['STLAN'].append('1')
                
                    # length = df[i][2].split('-')[0]
                    
                    # alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                    # if df[i][2].split('-')[1][:1]=='E':
                    #     ztekst='Экструзия (пресс) + Пила'
                    # df_new['ZTEXT'].append( ztekst)
                    # aliminisi =AlyuminniysilindrEkstruziya1.objects.filter(тип =alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064)[1:2].get()
                    # df_new['STKTX'].append(aliminisi.название)
                    # df_new['BMENG'].append( '1000')
                    # df_new['BMEIN'].append('ШТ')
                    # df_new['STLST'].append('1')
                    # df_new['POSNR'].append('')
                    # df_new['POSTP'].append('')
                    # df_new['MATNR1'].append('')
                    # df_new['TEXT2'].append('')
                    # df_new['MEINS'].append('')
                    # df_new['MENGE'].append('')
                    # df_new['DATUV'].append('01012021')
                    # df_new['PUSTOY'].append('')
                    # df_new['LGORT'].append('')
                    # for k in range(1,6):
                    #     j+=1
                    #     df_new['ID'].append( '2')
                    #     df_new['MATNR'].append( '')
                    #     df_new['WERKS'].append( '')
                    #     df_new['TEXT1'].append( '')
                    #     df_new['STLAL'].append( '')
                    #     df_new['STLAN'].append( '')
                    #     df_new['ZTEXT'].append( '')
                    #     df_new['STKTX'].append( '')
                    #     df_new['BMENG'].append( '')
                    #     df_new['BMEIN'].append('')
                    #     df_new['STLST'].append('')
                    #     df_new['POSNR'].append(k)
                    #     df_new['POSTP'].append('L')
                    #     if k == 1 :
                            
                    #         df_new['MATNR1'].append(aliminisi.sap_code_s4q100)
                    #         df_new['TEXT2'].append(aliminisi.название)
                    #         df_new['MEINS'].append( "{:0f}".format(float(alum_teks.алю_сп_6063_рас_спа_на_1000_шт_пр_кг)*mein_percent))
                    #         df_new['MENGE'].append( 'КГ')
                    #         df_new['DATUV'].append('')
                    #         df_new['PUSTOY'].append('')
                        
                    #     if k==2:
                    #         alummm = AlyuminniysilindrEkstruziya2.objects.first()
                    #         df_new['MATNR1'].append(alummm.sap_code_s4q100)
                    #         df_new['TEXT2'].append(alummm.название)
                    #         df_new['MENGE'].append(alummm.еи)
                    #         df_new['MEINS'].append( "{:0f}".format(float(alum_teks.смазка_для_пресса_кг_графитовая)*mein_percent))
                    #         df_new['DATUV'].append('')
                    #         df_new['PUSTOY'].append('')
                    #     if k==3:
                    #         alummm = AlyuminniysilindrEkstruziya2.objects.get(id=2)
                    #         df_new['MATNR1'].append(alummm.sap_code_s4q100)
                    #         df_new['TEXT2'].append(alummm.название)
                    #         df_new['MENGE'].append(alummm.еи)
                    #         df_new['MEINS'].append( "{:0f}".format((float(alum_teks.смазка_для_пресса_кг_пилы_хл_резки_сол) + float(alum_teks.смазка_для_пресса_кг_горячей_резки_сол))*mein_percent))
                    #         df_new['DATUV'].append('')
                    #         df_new['PUSTOY'].append('')
                    #     if k == 4:
                    #         alummm = AlyuminniysilindrEkstruziya2.objects.get(id=3)
                    #         df_new['MATNR1'].append(alummm.sap_code_s4q100)
                    #         df_new['TEXT2'].append(alummm.название)
                    #         df_new['MENGE'].append(alummm.еи)
                    #         df_new['MEINS'].append( "{:0f}".format(float(alum_teks.смазка_для_пресса_кг_графитовые_плиты)*mein_percent))
                    #         df_new['DATUV'].append('')
                    #         df_new['PUSTOY'].append('')
                    #     if k == 5:
                    #         alummm = AlyuminniysilindrEkstruziya2.objects.get(id=4)
                    #         df_new['MATNR1'].append(alummm.sap_code_s4q100)
                    #         df_new['TEXT2'].append(alummm.название)
                    #         df_new['MENGE'].append(alummm.еи)
                    #         df_new['MEINS'].append( "{:0f}".format(((-1)*(float(alum_teks.алю_сплав_6063_при_этом_тех_отхода1)+float(alum_teks.алю_сплав_6063_при_этом_тех_отхода2)))*mein_percent))
                    #         df_new['DATUV'].append('')
                    #         df_new['PUSTOY'].append('')
                    #     df_new['LGORT'].append('PS01')
        else:
            normaexist = CheckNormaBase.objects.filter(artikul=df[i][2],kratkiytekst=df[i][3])[:1].get()
            older_process['sapcode'] =normaexist.artikul
            older_process['kratkiy'] =normaexist.kratkiytekst            
        
        sklad ={
            'sklad_pokraski':['SKM - SKM покраска','SAT - SAT покраска','ГР - ГР покраска','SKM - Ручная покраска','SAT - Ручная покраска','ГР - Ручная покраска'],
            'number_sklad':[
                ['PS04','PS04','PS04','PS04','PS04','PS04'],
                ['PS05','PS05','PS05','PS05','PS05','PS05'],
                ['PS06','PS06','PS06','PS06','PS06','PS06'],
                ['PS07','PS07','PS07','PS04','PS04','PS04'],
                ['PS07','PS07','PS07','PS05','PS05','PS05'],
                ['PS07','PS07','PS07','PS06','PS06','PS06']
                ]
        }
        
        norma_existsP = CheckNormaBase.objects.filter(artikul=df[i][4],kratkiytekst=df[i][5]).exists()
        if not norma_existsP:
            if df[i][4] !="":
                CheckNormaBase(artikul=df[i][4],kratkiytekst=df[i][5]).save()
                if (df[i][4].split('-')[1][:1]=='P'):
                    for p in range(0,6):    
                        j+=1
                        
                        if (df[i][4].split('-')[1][:1]=='P'):
                            df_new['ID'].append('1')
                            df_new['MATNR'].append(df[i][4])
                            df_new['WERKS'].append('1101')
                            df_new['TEXT1'].append(df[i][5])
                            df_new['STLAL'].append(f'{p+1}')
                            df_new['STLAN'].append('1')
                            ztekst = sklad['sklad_pokraski'][p]
                            df_new['ZTEXT'].append(ztekst)
                            df_new['STKTX'].append(ztekst)
                            df_new['BMENG'].append( '1000')
                            df_new['BMEIN'].append('ШТ')
                            df_new['STLST'].append('1')
                            df_new['POSNR'].append('')
                            df_new['POSTP'].append('')
                            df_new['MATNR1'].append('')
                            df_new['TEXT2'].append('')
                            df_new['MEINS'].append('')
                            df_new['MENGE'].append('')
                            df_new['DATUV'].append('01012021')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('')
                            length = df[i][4].split('-')[0]
                            
                            alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                            
                            
                            mein_percent =((get_legth(df[i][5]))/float(alum_teks.длина_профиля_м))
                            
                            for k in range(0,6):
                                j+=1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                
                                
                                if k == 0 :
                                    print('tip kleyaaa --->>>> ',alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064)
                                    aliminisi =AlyuminniysilindrEkstruziya1.objects.filter(тип =alum_teks.ala7_oddiy_ala8_qora_алю_сплав_6064)[:1].get()
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    alummm = AlyuminniysilindrEkstruziya2.objects.get(id=1)
                                    kraska_code = df[i][5].split()[-1]
                                    print('kraskaaa======= ',kraska_code)                                    
                                    kraska =Kraska.objects.filter(код_краски_в_профилях = kraska_code)[:1].get()
                                    df_new['MATNR1'].append(kraska.sap_code_s4q100)
                                    df_new['TEXT2'].append(kraska.название)
                                    df_new['MENGE'].append('КГ')
                                    df_new['MEINS'].append( "{:0f}".format(float(alum_teks.порошковый_краситель_рас_кг_на_1000_пр)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k == 2:
                                    himikat_kraska = Ximikat.objects.get(id=4)
                                    df_new['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                    df_new['TEXT2'].append(himikat_kraska.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format((-1)*float(alum_teks.пр_краситель_при_этом_тех_отхода)*mein_percent)) 
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==3:
                                    himikat_kraska = Ximikat.objects.get(id=1)
                                    df_new['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                    df_new['TEXT2'].append(himikat_kraska.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.хим_пг_к_окр_politeknik_кг_alupol_сr_51)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k == 4:
                                    himikat_kraska = Ximikat.objects.get(id=2)
                                    df_new['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                    df_new['TEXT2'].append(himikat_kraska.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.хим_пг_к_окр_politeknik_кг_alupol_ac_52)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k == 5:
                                    himikat_kraska = Ximikat.objects.get(id=3)
                                    df_new['MATNR1'].append(himikat_kraska.sap_code_s4q100)
                                    df_new['TEXT2'].append(himikat_kraska.название)
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.хим_пг_к_окр_politeknik_кг_pol_ac_25p)*mein_percent)) 
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                    
                                df_new['LGORT'].append(sklad['number_sklad'][p][k])
                        
                            # df_new['STKTX'][j-6+i]=(df_new['TEXT2'][j-4+i])
                            
                older_process['sapcode'] =df[i][4]
                older_process['kratkiy'] =df[i][5]
        else:
            normaexist = CheckNormaBase.objects.filter(artikul=df[i][4],kratkiytekst=df[i][5])[:1].get()
            older_process['sapcode'] =normaexist.artikul
            older_process['kratkiy'] =normaexist.kratkiytekst
            
        norma_existsS = CheckNormaBase.objects.filter(artikul=df[i][6],kratkiytekst=df[i][7]).exists()
        if not norma_existsS:
            if df[i][6] !="":
                CheckNormaBase(artikul=df[i][6],kratkiytekst=df[i][7]).save()
                if (df[i][6].split('-')[1][:1]=='S'):
                    j+=1
                    if (df[i][6].split('-')[1][:1]=='S'):
                        df_new['ID'].append('1')
                        df_new['MATNR'].append(df[i][6])
                        df_new['WERKS'].append('1101')
                        df_new['TEXT1'].append(df[i][7])
                        df_new['STLAL'].append(f'1')
                        df_new['STLAN'].append('1')
                        ztekst = 'Сублимация - Декоративное покрытие'
                        ateks2='Сублимация - '+df[i][7].split('_')[1]
                        df_new['ZTEXT'].append(ztekst)
                        df_new['STKTX'].append(ateks2)
                        df_new['BMENG'].append( '1000')
                        df_new['BMEIN'].append('ШТ')
                        df_new['STLST'].append('1')
                        df_new['POSNR'].append('')
                        df_new['POSTP'].append('')
                        df_new['MATNR1'].append('')
                        df_new['TEXT2'].append('')
                        df_new['MEINS'].append('')
                        df_new['MENGE'].append('')
                        df_new['DATUV'].append('01012021')
                        df_new['PUSTOY'].append('')
                        df_new['LGORT'].append('')
                        length = df[i][6].split('-')[0]
                        
                        alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                        
                        mein_percent =((get_legth(df[i][7]))/float(alum_teks.длина_профиля_м))
                        
                        sublimatsiya_code = df[i][7].split('_')[1]
                        if sublimatsiya_code =='7777':
                            code_ss = alum_teks.суб_ширина_декор_пленки_мм_зол_дуб
                            mein =alum_teks.сублимация_расход_на_1000_профиль_м21
                            
                        elif sublimatsiya_code =='8888':
                            
                            code_ss = alum_teks.суб_ширина_декор_пленки_мм_дуб_мокко
                            mein =alum_teks.сублимация_расход_на_1000_профиль_м23
                        elif sublimatsiya_code =='3701':
                            
                            code_ss = alum_teks.суб_ширина_декор_пленки_мм_3д_313701
                            mein =alum_teks.сублимация_расход_на_1000_профиль_м22
                        elif sublimatsiya_code =='3702':
                            
                            code_ss = alum_teks.суб_ширина_декор_пленки_мм_3д_313702
                            mein =alum_teks.сублимация_расход_на_1000_профиль_м24
                        
                        
                        for k in range(0,4):
                            j+=1
                            df_new['ID'].append('2')
                            df_new['MATNR'].append('')
                            df_new['WERKS'].append('')
                            df_new['TEXT1'].append('')
                            df_new['STLAL'].append('')
                            df_new['STLAN'].append('')
                            df_new['ZTEXT'].append('')
                            df_new['STKTX'].append('')
                            df_new['BMENG'].append('')
                            df_new['BMEIN'].append('')
                            df_new['STLST'].append('')
                            df_new['POSNR'].append(k+1)
                            df_new['POSTP'].append('L')
                            
                            
                            if k == 0 :
                                df_new['MATNR1'].append(older_process['sapcode'])
                                df_new['TEXT2'].append(older_process['kratkiy'])
                                df_new['MEINS'].append('1000')
                                df_new['MENGE'].append('ШТ')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            
                            if k==1:
                                
                                subdecor = SubDekorPlonka.objects.get(код_декор_пленки = sublimatsiya_code, ширина_декор_пленки_мм = code_ss)
                                df_new['MATNR1'].append(subdecor.sap_code_s4q100)
                                df_new['TEXT2'].append(subdecor.название)
                                df_new['MENGE'].append('М2')
                                df_new['MEINS'].append( "{:0f}".format(float(mein)*mein_percent))
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            
                            if k==2:
                                skotch = Skotch.objects.get(id=1)
                                df_new['MATNR1'].append(skotch.sap_code_s4q100)
                                df_new['TEXT2'].append(skotch.название)
                                df_new['MENGE'].append("ШТ")
                                df_new['MEINS'].append("{:0f}".format(float(alum_teks.молярный_скотч_рас_на_1000_пр_шт1)*mein_percent))
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            if k == 3:
                                skotch = Skotch.objects.get(id=2)
                                df_new['MATNR1'].append(skotch.sap_code_s4q100)
                                df_new['TEXT2'].append(skotch.название)
                                df_new['MENGE'].append("ШТ")
                                df_new['MEINS'].append("{:0f}".format(float(alum_teks.молярный_скотч_рас_на_1000_пр_шт2)*mein_percent))
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                            
                                
                            df_new['LGORT'].append('PS08')
                            
                older_process['sapcode'] =df[i][6]
                older_process['kratkiy'] =df[i][7]
        else:
            normaexist = CheckNormaBase.objects.filter(artikul=df[i][6],kratkiytekst=df[i][7])[:1].get()
            older_process['sapcode'] =normaexist.artikul
            older_process['kratkiy'] =normaexist.kratkiytekst
        
            
        norma_existsN = CheckNormaBase.objects.filter(artikul=df[i][8],kratkiytekst=df[i][9]).exists()
        if not norma_existsN:
            if df[i][8] !="":
                CheckNormaBase(artikul=df[i][8],kratkiytekst=df[i][9]).save()
                if (df[i][8].split('-')[1][:1]=='N'):
                    
                        length = df[i][8].split('-')[0]
                        
                        alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                        
                        mein_percent =((get_legth(df[i][9]))/float(alum_teks.длина_профиля_м))
                        
                        nakleyka_code = df[i][9].split()[-1]
                        
                        qatorlar_soni = 0
                        
                        if nakleyka_code =='A01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм == alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм != alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0')or(alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni = 4
                                if alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)
                                    meinss = float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                                elif alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                    meinss = float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)+float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                            elif ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni = 5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                                meinss2 =float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                                
                        elif nakleyka_code =='R05':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм=='0'))) 
                            log2 = ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм == '0'))
                            
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                
                                if alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)
                                    meinss = float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                                elif alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                            elif log2:
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)[:1].get()
                                meinss1 = float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                                meinss2 = float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                                
                        elif nakleyka_code =='B01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4        
                                if alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                                elif alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                                
                        elif nakleyka_code =='I02':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                if alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2)
                                elif alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_ch_вр_и_кг_м_ch_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_ch_вр_и_кг_м_ch_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2)
                            elif ((alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_ch_вр_и_кг_м_ch_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2)
                                
                        elif nakleyka_code =='I01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                if alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                                elif alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)+float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                                meinss2 =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                                
                        elif nakleyka_code =='NB1':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                if alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                                elif alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                                
                        elif nakleyka_code =='E01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                if alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                                elif alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            elif ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            
                        elif nakleyka_code =='E02':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты and alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты !='0') or ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)and((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =4
                                if alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)
                                    meinss =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                                elif alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)+float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты == '0')):
                                qatorlar_soni = 3
                            else:
                                qatorlar_soni =5
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)[:1].get()
                                meinss1 =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                                meinss2 =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            
                        elif (nakleyka_code =='NT1') :
                            qatorlar_soni = 0

                        if qatorlar_soni == 4 :
                            for nakleykaa in nakleyka_results:
                                j+=1
                                if (df[i][8].split('-')[1][:1]=='N'):
                                    df_new['ID'].append('1')
                                    df_new['MATNR'].append(df[i][8])
                                    df_new['WERKS'].append('1101')
                                    df_new['TEXT1'].append(df[i][9])
                                    df_new['STLAL'].append(f'1')
                                    df_new['STLAN'].append('1')
                                    ztekst = 'Упаковка'
                                    df_new['ZTEXT'].append(ztekst)
                                    df_new['STKTX'].append(ztekst)
                                    df_new['BMENG'].append( '1000')
                                    df_new['BMEIN'].append('ШТ')
                                    df_new['STLST'].append('1')
                                    df_new['POSNR'].append('')
                                    df_new['POSTP'].append('')
                                    df_new['MATNR1'].append('')
                                    df_new['TEXT2'].append('')
                                    df_new['MEINS'].append('')
                                    df_new['MENGE'].append('')
                                    df_new['DATUV'].append('01012021')
                                    df_new['PUSTOY'].append('')
                                    df_new['LGORT'].append('')
                                for k in range(0,2):
                                    j+=1
                                    df_new['ID'].append('2')
                                    df_new['MATNR'].append('')
                                    df_new['WERKS'].append('')
                                    df_new['TEXT1'].append('')
                                    df_new['STLAL'].append('')
                                    df_new['STLAN'].append('')
                                    df_new['ZTEXT'].append('')
                                    df_new['STKTX'].append('')
                                    df_new['BMENG'].append('')
                                    df_new['BMEIN'].append('')
                                    df_new['STLST'].append('')
                                    df_new['POSNR'].append(k+1)
                                    df_new['POSTP'].append('L')
                                    
                                    
                                    if k == 0 :
                                        df_new['MATNR1'].append(older_process['sapcode'])
                                        df_new['TEXT2'].append(older_process['kratkiy'])
                                        df_new['MEINS'].append('1000')
                                        df_new['MENGE'].append('ШТ')
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==1:
                                        df_new['MATNR1'].append(nakleykaa.sap_code_s4q100)
                                        df_new['TEXT2'].append(nakleykaa.название)
                                        df_new['MENGE'].append('М2')
                                        df_new['MEINS'].append( "{:0f}".format(float(meinss)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    
                                        
                                    df_new['LGORT'].append('PS10')
                        elif qatorlar_soni == 5:
                            j+=1
                            if (df[i][8].split('-')[1][:1]=='N'):
                                df_new['ID'].append('1')
                                df_new['MATNR'].append(df[i][8])
                                df_new['WERKS'].append('1101')
                                df_new['TEXT1'].append(df[i][9])
                                df_new['STLAL'].append(f'1')
                                df_new['STLAN'].append('1')
                                ztekst = 'Упаковка'
                                df_new['ZTEXT'].append(ztekst)
                                df_new['STKTX'].append(ztekst)
                                df_new['BMENG'].append( '1000')
                                df_new['BMEIN'].append('ШТ')
                                df_new['STLST'].append('1')
                                df_new['POSNR'].append('')
                                df_new['POSTP'].append('')
                                df_new['MATNR1'].append('')
                                df_new['TEXT2'].append('')
                                df_new['MEINS'].append('')
                                df_new['MENGE'].append('')
                                df_new['DATUV'].append('01012021')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('')
                            for k in range(0,2):
                                j+=1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                
                                
                                if k == 0 :
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result1.название)
                                    df_new['MENGE'].append('М2')
                                    df_new['MEINS'].append( "{:0f}".format(float(meinss1)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS10') 
                                
                            j+=1
                            if (df[i][8].split('-')[1][:1]=='N'):
                                df_new['ID'].append('1')
                                df_new['MATNR'].append(df[i][8])
                                df_new['WERKS'].append('1101')
                                df_new['TEXT1'].append(df[i][9])
                                df_new['STLAL'].append(f'1')
                                df_new['STLAN'].append('1')
                                ztekst = 'Упаковка'
                                df_new['ZTEXT'].append(ztekst)
                                df_new['STKTX'].append(ztekst)
                                df_new['BMENG'].append( '1000')
                                df_new['BMEIN'].append('ШТ')
                                df_new['STLST'].append('1')
                                df_new['POSNR'].append('')
                                df_new['POSTP'].append('')
                                df_new['MATNR1'].append('')
                                df_new['TEXT2'].append('')
                                df_new['MEINS'].append('')
                                df_new['MENGE'].append('')
                                df_new['DATUV'].append('01012021')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('')
                            for k in range(0,2):
                                j+=1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                
                                
                                if k == 0 :
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result2.название)
                                    df_new['MENGE'].append('М2')
                                    df_new['MEINS'].append( "{:0f}".format(float(meinss2)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS10') 
                                
                                       
                older_process['sapcode'] =df[i][8]
                older_process['kratkiy'] =df[i][9]
        else:
            normaexist = CheckNormaBase.objects.filter(artikul=df[i][8],kratkiytekst=df[i][9])[:1].get()
            older_process['sapcode'] =normaexist.artikul
            older_process['kratkiy'] =normaexist.kratkiytekst
            
        norma_existsK = CheckNormaBase.objects.filter(artikul=df[i][10],kratkiytekst=df[i][11]).exists()
        if not norma_existsK:
            if df[i][10] !="":
                CheckNormaBase(artikul=df[i][10],kratkiytekst=df[i][11]).save()
                if (df[i][10].split('-')[1][:1]=='K'):
                    
                    older_process_kombinirovanniy = {'s1':None,'k1':None,'s2':None,'k2':None,'s3':None,'k3':None}
                    ###############  Nakleyka   ###################
                    if df[i+1][8] !='':
                        older_process_kombinirovanniy['s1'] = df[i+1][8]
                        older_process_kombinirovanniy['k1'] = df[i+1][9]
                        if df[i+2][8] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][8]
                            older_process_kombinirovanniy['k2'] = df[i+2][9]
                        try:
                            if df[i+3][8] !='':
                                older_process_kombinirovanniy['s3'] = df[i+3][8]
                                older_process_kombinirovanniy['k3'] = df[i+3][9]
                        except:
                            older_process_kombinirovanniy['s3'] = None
                            older_process_kombinirovanniy['k3'] = None
                            
                    elif df[i+1][6] !='':
                        older_process_kombinirovanniy['s1'] = df[i+1][6]
                        older_process_kombinirovanniy['k1'] = df[i+1][7]
                        if df[i+2][6] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][6]
                            older_process_kombinirovanniy['k2'] = df[i+2][7]
                        try:
                            if df[i+3][6] !='':
                                older_process_kombinirovanniy['s3'] = df[i+3][6]
                                older_process_kombinirovanniy['k3'] = df[i+3][7]
                        except:
                            older_process_kombinirovanniy['s3'] = None
                            older_process_kombinirovanniy['k3'] = None
                        
                    elif df[i+1][4] !='':
                        older_process_kombinirovanniy['s1'] = df[i+1][4]
                        older_process_kombinirovanniy['k1'] = df[i+1][5]
                        if df[i+2][4] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][4]
                            older_process_kombinirovanniy['k2'] = df[i+2][5]
                        try:
                            if df[i+3][4] !='':
                                older_process_kombinirovanniy['s3'] = df[i+3][4]
                                older_process_kombinirovanniy['k3'] = df[i+3][5]
                        except:
                            older_process_kombinirovanniy['s3'] = None
                            older_process_kombinirovanniy['k3'] = None   
                        
                    elif df[i+1][2] !='':
                        older_process_kombinirovanniy['s1'] = df[i+1][2]
                        older_process_kombinirovanniy['k1'] = df[i+1][3]
                        if df[i+2][2] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][2]
                            older_process_kombinirovanniy['k2'] = df[i+2][3]
                        try:
                            if df[i+3][2] !='':
                                older_process_kombinirovanniy['s3'] = df[i+3][2]
                                older_process_kombinirovanniy['k3'] = df[i+3][3]
                        except:
                            older_process_kombinirovanniy['s3'] = None
                            older_process_kombinirovanniy['k3'] = None
                        
                    elif df[i+1][0] !='':
                        older_process_kombinirovanniy['s1'] = df[i+1][0]
                        older_process_kombinirovanniy['k1'] = df[i+1][1]
                        if df[i+2][0] !='':
                            older_process_kombinirovanniy['s2'] = df[i+2][0]
                            older_process_kombinirovanniy['k2'] = df[i+2][1]
                        try:
                            if df[i+3][0] !='':
                                older_process_kombinirovanniy['s3'] = df[i+3][0]
                                older_process_kombinirovanniy['k3'] = df[i+3][1]
                        except:
                            older_process_kombinirovanniy['s3'] = None
                            older_process_kombinirovanniy['k3'] = None
                        
                    
                    j+=1
                    if (df[i][10].split('-')[1][:1]=='K'):
                        df_new['ID'].append('1')
                        df_new['MATNR'].append(df[i][10])
                        df_new['WERKS'].append('1101')
                        df_new['TEXT1'].append(df[i][11])
                        df_new['STLAL'].append(f'1')
                        df_new['STLAN'].append('1')
                        ztekst = 'Комбинированный'
                        ateks2='Комбинированный'
                        df_new['ZTEXT'].append(ztekst)
                        df_new['STKTX'].append(ateks2)
                        df_new['BMENG'].append( '1000')
                        df_new['BMEIN'].append('ШТ')
                        df_new['STLST'].append('1')
                        df_new['POSNR'].append('')
                        df_new['POSTP'].append('')
                        df_new['MATNR1'].append('')
                        df_new['TEXT2'].append('')
                        df_new['MEINS'].append('')
                        df_new['MENGE'].append('')
                        df_new['DATUV'].append('01012021')
                        df_new['PUSTOY'].append('')
                        df_new['LGORT'].append('')
                        length = df[i][10].split('-')[0]
                        
                        alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                        
                        mein_percent =((get_legth(df[i][11]))/float(alum_teks.длина_профиля_м))
                        
                        artikul = df[i][10].split('-')[0]
                        kombininovanniy_utils = KombinirovaniyUtilsInformation.objects.get(artikul=artikul)
                        dddd =[
                                    {
                                        'sap_code':kombininovanniy_utils.sap_code1,
                                        'bridge':kombininovanniy_utils.termal_bridge1
                                    },
                                    {
                                        'sap_code':kombininovanniy_utils.sap_code1,
                                        'bridge':kombininovanniy_utils.termal_bridge2
                                    },
                                    {
                                        'sap_code':kombininovanniy_utils.sap_code3,
                                        'bridge':kombininovanniy_utils.termal_bridge3
                                    },
                                    {
                                        'sap_code':kombininovanniy_utils.sap_code4,
                                        'bridge':kombininovanniy_utils.termal_bridge4
                                    }
                                    ]
                        length_of_profile = get_legth(df[i][11]) * 1000
                        if older_process_kombinirovanniy['s3'] != None:
                            for k in range(0,3):
                                j+=1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append(f'{k+1}')
                                df_new['POSTP'].append('L')
                                df_new['MATNR1'].append(older_process_kombinirovanniy[f's{k+1}'])
                                df_new['TEXT2'].append(older_process_kombinirovanniy[f'k{k+1}'])
                                df_new['MEINS'].append('1000')
                                df_new['MENGE'].append('ШТ')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS10')
                            
                            new_list_for_com = []
                            sap_code_new ={}
                            
                            for ii in range(0,4):
                            
                                if not dddd[ii]['bridge'] in sap_code_new:
                                    sap_code_new[dddd[ii]['bridge']] ={'sum':length_of_profile,'sap_code':dddd[ii]['sap_code']}
                                    
                                    
                                if not dddd[ii]['bridge'] in new_list_for_com:
                                    for jj in range(ii + 1 , 4):
                                        if dddd[ii]['bridge'] == dddd[jj]['bridge']:
                                            sap_code_new[dddd[ii]['bridge']]['sum']+=length_of_profile
                                        
                                new_list_for_com.append(dddd[ii]['bridge'])
                            ttt = 4
                            for key,val in sap_code_new.items(): 
                                j += 1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append(f'{ttt}')
                                df_new['POSTP'].append('L')
                                df_new['MATNR1'].append(val['sap_code'])
                                df_new['TEXT2'].append(key)
                                df_new['MEINS'].append(f"{val['sum']}")
                                df_new['MENGE'].append('М')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS10')
                                ttt +=1
                        
                                
                        else:
                            for k in range(0,2):
                                j+=1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append(f'{k+1}')
                                df_new['POSTP'].append('L')
                                df_new['MATNR1'].append(older_process_kombinirovanniy[f's{k+1}'])
                                df_new['TEXT2'].append(older_process_kombinirovanniy[f'k{k+1}'])
                                df_new['MEINS'].append('1000')
                                df_new['MENGE'].append('ШТ')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS10')
                            
                            
                            if kombininovanniy_utils.termal_bridge1 == kombininovanniy_utils.termal_bridge2:
                                j += 1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append('3')
                                df_new['POSTP'].append('L')
                                df_new['MATNR1'].append(kombininovanniy_utils.sap_code1)
                                df_new['TEXT2'].append(kombininovanniy_utils.termal_bridge1)
                                df_new['MEINS'].append( f'{length_of_profile * 2}' )
                                df_new['MENGE'].append('М')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS10')
                            else:
                                j += 1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append('3')
                                df_new['POSTP'].append('L')
                                df_new['MATNR1'].append(kombininovanniy_utils.sap_code1)
                                df_new['TEXT2'].append(kombininovanniy_utils.termal_bridge1)
                                df_new['MEINS'].append(f'{length_of_profile}')
                                df_new['MENGE'].append('М')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS10')
                                
                                j += 1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append('4')
                                df_new['POSTP'].append('L')
                                df_new['MATNR1'].append(kombininovanniy_utils.sap_code2)
                                df_new['TEXT2'].append(kombininovanniy_utils.termal_bridge2)
                                df_new['MEINS'].append(f'{length_of_profile}')
                                df_new['MENGE'].append('М')
                                df_new['DATUV'].append('')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('PS10')
                                
                            
                            
                older_process['sapcode'] =df[i][10]
                older_process['kratkiy'] =df[i][11]
        else:
            normaexist = CheckNormaBase.objects.filter(artikul=df[i][10],kratkiytekst=df[i][11])[:1].get()
            older_process['sapcode'] =normaexist.artikul
            older_process['kratkiy'] =normaexist.kratkiytekst
            
         
        
                           
        norma_exists7 = CheckNormaBase.objects.filter(artikul=df[i][12],kratkiytekst=df[i][13]).exists()
        if not norma_exists7:
            
            if df[i][12] !="":
                CheckNormaBase(artikul=df[i][12],kratkiytekst=df[i][13]).save()
                if (df[i][12].split('-')[1][:1]=='7'):
                    
                    
                    if '_' in df[i][13]:
                        ddd = df[i][13].split()[2]
                    
                    nakleyka_code = df[i][13].split()[-1]
                    length = df[i][12].split('-')[0]
                    
                    alum_teks = Norma.objects.filter(Q(компонент_1=length)|Q(компонент_2=length)|Q(компонент_3=length)|Q(артикул=length))[:1].get()
                    
                    mein_percent =((get_legth(df[i][13]))/float(alum_teks.длина_профиля_м))
                    
                    its_lamination = not ((not '_' in df[i][13]) or ('7777' in ddd.split('_')[1]) or ('8888' in ddd.split('_')[1]) or ('3701' in ddd.split('_')[1]) or ('3702' in ddd.split('_')[1]))
                    
                    if nakleyka_code =='A01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм == alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм != alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0')or(alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)
                                meinss = float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                            elif alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                meinss = float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)+float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                        elif ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni = 5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                            meinss2 =float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                            
                    elif nakleyka_code =='R05':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм=='0'))) 
                        log2 = ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм == '0'))
                        
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            
                            if alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)
                                meinss = float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                            elif alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                        elif log2:
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)[:1].get()
                            meinss1 = float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                            meinss2 = float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                            
                    elif nakleyka_code =='B01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4        
                            if alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                            elif alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                        elif ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                            meinss2 =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                            
                    elif nakleyka_code =='I02':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2)
                            elif alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_ch_вр_и_кг_м_ch_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_ch_вр_и_кг_м_ch_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2)
                        elif ((alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_ch_вр_и_кг_м_ch_бк_ст_рас)
                            meinss2 =float(alum_teks.заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2)
                            
                    elif nakleyka_code =='I01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                            elif alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)+float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                        elif ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                            meinss2 =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                            
                    elif nakleyka_code =='NB1':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                            elif alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                        elif ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                            meinss2 =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                            
                    elif nakleyka_code =='E01':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)
                                meinss =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            elif alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                        elif ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)[:1].get()
                            meinss1 =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                            meinss2 =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                        
                    elif nakleyka_code =='E02':
                        aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты and alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты !='0') or ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)and((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты=='0')))
                        if aluminiy_norma_log:
                            qatorlar_soni =4
                            if alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)
                                meinss =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            elif alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты =='0':
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                            else:
                                nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)+float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                        elif ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты == '0')):
                            qatorlar_soni = 3
                        else:
                            qatorlar_soni =5
                            nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)[:1].get()
                            nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)[:1].get()
                            meinss1 =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                            meinss2 =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                        
                    elif (nakleyka_code =='NT1') :
                        qatorlar_soni = 3
                
                    if its_lamination:
                        
                        if nakleyka_code =='A01' :
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм == alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм != alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0')or(alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni = 5
                                if alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                                elif alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)+float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                            elif ((alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni = 6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'A01',ширина= alum_teks.заш_пл_кг_м_akfa_низ_ширина_ленты_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_ak_вр_и_кг_м_ak_бк_ст_рас_лн)
                                meinss2 =float(alum_teks.заш_пл_кг_м_ak_низ_рас_лн_на_1000_пр_м2)
                                
                        elif nakleyka_code =='R05':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм=='0'))) 
                            log2 = ((alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм == '0'))
                            
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                                elif alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                            elif log2:
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'R05',ширина= alum_teks.заш_пл_кг_м_retpen_низ_ширина_ленты_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_retpen_вр_и_кг_м_retpen_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_retpen_низ_рас)
                                    
                        elif nakleyka_code =='B01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                                elif alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'B01',ширина= alum_teks.заш_пл_кг_м_benkam_жл_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_bn_жл_вр_и_кг_м_bn_жл_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_bn_жл_низ_рас)
                                
                        elif nakleyka_code =='I02':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni = 5
                                if alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2)
                                elif alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_ch_вр_и_кг_м_ch_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_ch_вр_и_кг_м_ch_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2)
                            elif ((alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'I02',ширина= alum_teks.заш_пл_кг_м_ch_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_ch_вр_и_кг_м_ch_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_ch_низ_рас_лн_на_1000_пр_м2)
                                
                        elif nakleyka_code =='I01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                                elif alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)+float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'I01',ширина= alum_teks.заш_пл_кг_м_imzo_akfa_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_imzo_ak_вр_и_кг_м_imzo_ak_бк_ст)
                                meinss2 =float(alum_teks.заш_пл_кг_м_imzo_ak_низ_рас)
                                
                        elif nakleyka_code =='NB1':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм and alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм != '0') or ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)and((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                                elif alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'NB1',ширина= alum_teks.заш_пл_кг_м_без_бр_низ_ширина_лн_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_без_бр_вр_и_кг_м_без_бр_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_без_бр_низ_рас)
                                
                        elif nakleyka_code =='E01':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм== alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм and alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм != '0') or ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм!= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)and((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0')or(alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)
                                    meinss =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                                elif alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)
                                    meinss =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)+float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            elif ((alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм =='0') and (alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_верх_ширина_ленты_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E01',ширина= alum_teks.заш_пл_кг_м_eng_низ_ширина_ленты_мм)[:1].get()
                                meinss1 =float(alum_teks.кг_м_eng_вр_и_кг_м_eng_бк_ст_рас)
                                meinss2 =float(alum_teks.заш_пл_кг_м_eng_низ_рас_лн_на_1000_пр)
                            
                        elif nakleyka_code =='E02':
                            aluminiy_norma_log = (alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм== alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты and alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты !='0') or ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм!= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)and((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0')or(alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты=='0')))
                            if aluminiy_norma_log:
                                qatorlar_soni =5
                                if alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм=='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)
                                    meinss =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                                elif alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты =='0':
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                                else:
                                    nakleyka_results = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)
                                    meinss =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)+float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            elif ((alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм =='0') and (alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты == '0')):
                                qatorlar_soni = 4
                            else:
                                qatorlar_soni =6
                                nakleyka_result1 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_вр_ширина_лн_мм)[:1].get()
                                nakleyka_result2 = Nakleyka.objects.filter(код_наклейки = 'E02',ширина= alum_teks.заш_пл_кг_м_eng_qora_низ_ширина_ленты)[:1].get()
                                meinss1 =float(alum_teks.кг_м_eng_qora_вр_и_кг_м_eng_qora_бк_ст)
                                meinss2 =float(alum_teks.заш_пл_кг_м_eng_qora_низ_рас)
                            
                        elif (nakleyka_code =='NT1') :
                            qatorlar_soni = 4
                        
                        
                    ############Laminatsiya
                    
                    
                        
                        
                    its_kombinirovanniy ='-K' in df[i][10]
                    
                    if ((not '_' in df[i][13]) or ('7777' in ddd.split('_')[1]) or ('8888' in ddd.split('_')[1]) or ('3701' in ddd.split('_')[1]) or ('3702' in ddd.split('_')[1])):
                        
                        if its_kombinirovanniy:
                            if qatorlar_soni == 3:
                                j+=1
                                df_new['ID'].append('1')
                                df_new['MATNR'].append(df[i][12])
                                df_new['WERKS'].append('1101')
                                df_new['TEXT1'].append(df[i][13])
                                df_new['STLAL'].append('1')
                                df_new['STLAN'].append('1')
                                ztekst = 'Упаковка'
                                df_new['ZTEXT'].append(ztekst)
                                df_new['STKTX'].append(ztekst)
                                df_new['BMENG'].append( '1000')
                                df_new['BMEIN'].append('ШТ')
                                df_new['STLST'].append('1')
                                df_new['POSNR'].append('')
                                df_new['POSTP'].append('')
                                df_new['MATNR1'].append('')
                                df_new['TEXT2'].append('')
                                df_new['MEINS'].append('')
                                df_new['MENGE'].append('')
                                df_new['DATUV'].append('01012021')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('')
                                length = df[i][12].split('-')[0]
                                for k in range(0,qatorlar_soni):
                                    j+=1
                                    df_new['ID'].append('2')
                                    df_new['MATNR'].append('')
                                    df_new['WERKS'].append('')
                                    df_new['TEXT1'].append('')
                                    df_new['STLAL'].append('')
                                    df_new['STLAN'].append('')
                                    df_new['ZTEXT'].append('')
                                    df_new['STKTX'].append('')
                                    df_new['BMENG'].append('')
                                    df_new['BMEIN'].append('')
                                    df_new['STLST'].append('')
                                    df_new['POSNR'].append(k+1)
                                    df_new['POSTP'].append('L')
                                    
                                    
                                    if k == 0 :
                                        df_new['MATNR1'].append(older_process['sapcode'])
                                        df_new['TEXT2'].append(older_process['kratkiy'])
                                        df_new['MEINS'].append('1000')
                                        df_new['MENGE'].append('ШТ')
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==1:
                                        df_new['MATNR1'].append('1000001016')
                                        df_new['TEXT2'].append('Пленка П1 NS12см 60мк Ncolor')
                                        df_new['MENGE'].append('КГ')
                                        df_new['MEINS'].append( "{:0f}".format(float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==2:
                                        df_new['MATNR1'].append('1900000069')
                                        df_new['TEXT2'].append('Скотч 36мм/300м')
                                        df_new['MENGE'].append("ШТ")
                                        df_new['MEINS'].append("{:0f}".format(float(alum_teks.рас_скотча_рас_скотча_на_1000_штук_шт)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    df_new['LGORT'].append('PS10')
                            if ((qatorlar_soni == 4) or (qatorlar_soni == 5)):
                                j+=1
                                df_new['ID'].append('1')
                                df_new['MATNR'].append(df[i][12])
                                df_new['WERKS'].append('1101')
                                df_new['TEXT1'].append(df[i][13])
                                df_new['STLAL'].append(f'1')
                                df_new['STLAN'].append('1')
                                ztekst = 'Упаковка'
                                df_new['ZTEXT'].append(ztekst)
                                df_new['STKTX'].append(ztekst+' Комбинированный')
                                df_new['BMENG'].append( '1000')
                                df_new['BMEIN'].append('ШТ')
                                df_new['STLST'].append('1')
                                df_new['POSNR'].append('')
                                df_new['POSTP'].append('')
                                df_new['MATNR1'].append('')
                                df_new['TEXT2'].append('')
                                df_new['MEINS'].append('')
                                df_new['MENGE'].append('')
                                df_new['DATUV'].append('01012021')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('')
                                length = df[i][12].split('-')[0]
                                for k in range(0,3):
                                    j+=1
                                    df_new['ID'].append('2')
                                    df_new['MATNR'].append('')
                                    df_new['WERKS'].append('')
                                    df_new['TEXT1'].append('')
                                    df_new['STLAL'].append('')
                                    df_new['STLAN'].append('')
                                    df_new['ZTEXT'].append('')
                                    df_new['STKTX'].append('')
                                    df_new['BMENG'].append('')
                                    df_new['BMEIN'].append('')
                                    df_new['STLST'].append('')
                                    df_new['POSNR'].append(k+1)
                                    df_new['POSTP'].append('L')
                                    
                                    
                                    if k == 0 :
                                        df_new['MATNR1'].append(older_process['sapcode'])
                                        df_new['TEXT2'].append(older_process['kratkiy'])
                                        df_new['MEINS'].append('1000')
                                        df_new['MENGE'].append('ШТ')
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==1:
                                        df_new['MATNR1'].append('1000001016')
                                        df_new['TEXT2'].append('Пленка П1 NS12см 60мк Ncolor')
                                        df_new['MENGE'].append('КГ')
                                        df_new['MEINS'].append( "{:0f}".format(float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==2:
                                        skotch = Skotch.objects.get(id=1)
                                        df_new['MATNR1'].append('1900000069')
                                        df_new['TEXT2'].append('Скотч 36мм/300м')
                                        df_new['MENGE'].append("ШТ")
                                        df_new['MEINS'].append("{:0f}".format(float(alum_teks.рас_скотча_рас_скотча_на_1000_штук_шт)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    df_new['LGORT'].append('PS10')
                        else:
                            if qatorlar_soni == 3:
                                j+=1
                                df_new['ID'].append('1')
                                df_new['MATNR'].append(df[i][12])
                                df_new['WERKS'].append('1101')
                                df_new['TEXT1'].append(df[i][13])
                                df_new['STLAL'].append('1')
                                df_new['STLAN'].append('1')
                                ztekst = 'Упаковка'
                                df_new['ZTEXT'].append(ztekst)
                                df_new['STKTX'].append(ztekst)
                                df_new['BMENG'].append( '1000')
                                df_new['BMEIN'].append('ШТ')
                                df_new['STLST'].append('1')
                                df_new['POSNR'].append('')
                                df_new['POSTP'].append('')
                                df_new['MATNR1'].append('')
                                df_new['TEXT2'].append('')
                                df_new['MEINS'].append('')
                                df_new['MENGE'].append('')
                                df_new['DATUV'].append('01012021')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('')
                                length = df[i][12].split('-')[0]
                                for k in range(0,qatorlar_soni):
                                    j+=1
                                    df_new['ID'].append('2')
                                    df_new['MATNR'].append('')
                                    df_new['WERKS'].append('')
                                    df_new['TEXT1'].append('')
                                    df_new['STLAL'].append('')
                                    df_new['STLAN'].append('')
                                    df_new['ZTEXT'].append('')
                                    df_new['STKTX'].append('')
                                    df_new['BMENG'].append('')
                                    df_new['BMEIN'].append('')
                                    df_new['STLST'].append('')
                                    df_new['POSNR'].append(k+1)
                                    df_new['POSTP'].append('L')
                                    
                                    
                                    if k == 0 :
                                        df_new['MATNR1'].append(older_process['sapcode'])
                                        df_new['TEXT2'].append(older_process['kratkiy'])
                                        df_new['MEINS'].append('1000')
                                        df_new['MENGE'].append('ШТ')
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==1:
                                        df_new['MATNR1'].append('1000001016')
                                        df_new['TEXT2'].append('Пленка П1 NS12см 60мк Ncolor')
                                        df_new['MENGE'].append('КГ')
                                        df_new['MEINS'].append( "{:0f}".format(float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==2:
                                        df_new['MATNR1'].append('1900000069')
                                        df_new['TEXT2'].append('Скотч 36мм/300м')
                                        df_new['MENGE'].append("ШТ")
                                        df_new['MEINS'].append("{:0f}".format(float(alum_teks.рас_скотча_рас_скотча_на_1000_штук_шт)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    df_new['LGORT'].append('PS10')
                            if qatorlar_soni == 4:
                                jjj =0
                                for nakleykaa in nakleyka_results:
                                    jjj += 1
                                    j+=1
                                    df_new['ID'].append('1')
                                    df_new['MATNR'].append(df[i][12])
                                    df_new['WERKS'].append('1101')
                                    df_new['TEXT1'].append(df[i][13])
                                    df_new['STLAL'].append(f'{jjj}')
                                    df_new['STLAN'].append('1')
                                    ztekst = 'Упаковка'
                                    df_new['ZTEXT'].append(ztekst)
                                    df_new['STKTX'].append(ztekst)
                                    df_new['BMENG'].append( '1000')
                                    df_new['BMEIN'].append('ШТ')
                                    df_new['STLST'].append('1')
                                    df_new['POSNR'].append('')
                                    df_new['POSTP'].append('')
                                    df_new['MATNR1'].append('')
                                    df_new['TEXT2'].append('')
                                    df_new['MEINS'].append('')
                                    df_new['MENGE'].append('')
                                    df_new['DATUV'].append('01012021')
                                    df_new['PUSTOY'].append('')
                                    df_new['LGORT'].append('')
                                    length = df[i][12].split('-')[0]
                                    for k in range(0,qatorlar_soni):
                                        j+=1
                                        df_new['ID'].append('2')
                                        df_new['MATNR'].append('')
                                        df_new['WERKS'].append('')
                                        df_new['TEXT1'].append('')
                                        df_new['STLAL'].append('')
                                        df_new['STLAN'].append('')
                                        df_new['ZTEXT'].append('')
                                        df_new['STKTX'].append('')
                                        df_new['BMENG'].append('')
                                        df_new['BMEIN'].append('')
                                        df_new['STLST'].append('')
                                        df_new['POSNR'].append(k+1)
                                        df_new['POSTP'].append('L')
                                        
                                        
                                        if k == 0 :
                                            df_new['MATNR1'].append(older_process['sapcode'])
                                            df_new['TEXT2'].append(older_process['kratkiy'])
                                            df_new['MEINS'].append('1000')
                                            df_new['MENGE'].append('ШТ')
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        if k==1:
                                            df_new['MATNR1'].append('1000001016')
                                            df_new['TEXT2'].append('Пленка П1 NS12см 60мк Ncolor')
                                            df_new['MENGE'].append('КГ')
                                            df_new['MEINS'].append( "{:0f}".format(float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent))
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        if k==2:
                                            skotch = Skotch.objects.get(id=1)
                                            df_new['MATNR1'].append('1900000069')
                                            df_new['TEXT2'].append('Скотч 36мм/300м')
                                            df_new['MENGE'].append("ШТ")
                                            df_new['MEINS'].append("{:0f}".format(float(alum_teks.рас_скотча_рас_скотча_на_1000_штук_шт)*mein_percent))
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        if k==3:
                                            df_new['MATNR1'].append(nakleykaa.sap_code_s4q100)
                                            df_new['TEXT2'].append(nakleykaa.название)
                                            df_new['MENGE'].append("М2")
                                            df_new['MEINS'].append("{:0f}".format((meinss)*mein_percent))
                                            df_new['DATUV'].append('')
                                            df_new['PUSTOY'].append('')
                                        
                                        df_new['LGORT'].append('PS10')
                            if qatorlar_soni == 5:
                                j += 1
                                df_new['ID'].append('1')
                                df_new['MATNR'].append(df[i][12])
                                df_new['WERKS'].append('1101')
                                df_new['TEXT1'].append(df[i][13])
                                df_new['STLAL'].append('1')
                                df_new['STLAN'].append('1')
                                ztekst = 'Упаковка'
                                df_new['ZTEXT'].append(ztekst)
                                df_new['STKTX'].append(ztekst)
                                df_new['BMENG'].append( '1000')
                                df_new['BMEIN'].append('ШТ')
                                df_new['STLST'].append('1')
                                df_new['POSNR'].append('')
                                df_new['POSTP'].append('')
                                df_new['MATNR1'].append('')
                                df_new['TEXT2'].append('')
                                df_new['MEINS'].append('')
                                df_new['MENGE'].append('')
                                df_new['DATUV'].append('01012021')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('')
                                length = df[i][12].split('-')[0]
                                for k in range(0,qatorlar_soni):
                                    j+=1
                                    df_new['ID'].append('2')
                                    df_new['MATNR'].append('')
                                    df_new['WERKS'].append('')
                                    df_new['TEXT1'].append('')
                                    df_new['STLAL'].append('')
                                    df_new['STLAN'].append('')
                                    df_new['ZTEXT'].append('')
                                    df_new['STKTX'].append('')
                                    df_new['BMENG'].append('')
                                    df_new['BMEIN'].append('')
                                    df_new['STLST'].append('')
                                    df_new['POSNR'].append(k+1)
                                    df_new['POSTP'].append('L')
                                    
                                    
                                    if k == 0 :
                                        df_new['MATNR1'].append(older_process['sapcode'])
                                        df_new['TEXT2'].append(older_process['kratkiy'])
                                        df_new['MEINS'].append('1000')
                                        df_new['MENGE'].append('ШТ')
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==1:
                                        df_new['MATNR1'].append('1000001016')
                                        df_new['TEXT2'].append('Пленка П1 NS12см 60мк Ncolor')
                                        df_new['MENGE'].append('КГ')
                                        df_new['MEINS'].append( "{:0f}".format(float(alum_teks.уп_пол_лн_рас_уп_лн_на_1000_штук_кг)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==2:
                                        skotch = Skotch.objects.get(id=1)
                                        df_new['MATNR1'].append('1900000069')
                                        df_new['TEXT2'].append('Скотч 36мм/300м')
                                        df_new['MENGE'].append("ШТ")
                                        df_new['MEINS'].append("{:0f}".format(float(alum_teks.рас_скотча_рас_скотча_на_1000_штук_шт)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==3:
                                        df_new['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                        df_new['TEXT2'].append(nakleyka_result1.название)
                                        df_new['MENGE'].append("М2")
                                        df_new['MEINS'].append(float(meinss1)*mein_percent)
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==4:
                                        df_new['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                                        df_new['TEXT2'].append(nakleyka_result2.название)
                                        df_new['MENGE'].append("М2")
                                        df_new['MEINS'].append(float(meinss2)*mein_percent)
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    df_new['LGORT'].append('PS10')
                        
                    else:
                        
                        laminatsiya_code = ddd.split('_')[1].split('/')
                        laminatsiya_code1 = laminatsiya_code[0]
                        laminatsiya_code2 = laminatsiya_code[1]
                        
                        if ((laminatsiya_code1 == laminatsiya_code2) or (laminatsiya_code1 =='XXXX' or laminatsiya_code2 == 'XXXX')):
                            qatorlar_soni +=1
                            
                            if laminatsiya_code1 =='XXXX':
                                meinsL = alum_teks.лам_низ_b_рас_ленты_на_1000_пр_м2
                                laminatsiya =Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code2)[:1].get() 
                            elif laminatsiya_code2 =='XXXX':
                                
                                meinsL = alum_teks.лам_верх_a_рас_ленты_на_1000_пр_м2
                                laminatsiya =Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code1)[:1].get() 
                            elif laminatsiya_code1 == laminatsiya_code2:
                                meinsL = float(alum_teks.лам_верх_a_рас_ленты_на_1000_пр_м2)+float(alum_teks.лам_низ_b_рас_ленты_на_1000_пр_м2)
                                print('lanination kode <<<<< ',laminatsiya_code1,' >>>>>>')
                                laminatsiya =Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code1)[:1].get() 
                                
                        else:
                            qatorlar_soni +=2
                            laminatsiya_result1 = Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code1)[:1].get() 
                            laminatsiya_result2 = Lamplonka.objects.filter(код_лам_пленки =laminatsiya_code2)[:1].get() 
                            meinsL1 = float(alum_teks.лам_верх_a_рас_ленты_на_1000_пр_м2)
                            meinsL2 = float(alum_teks.лам_низ_b_рас_ленты_на_1000_пр_м2)
                            
                        
                        if qatorlar_soni == 5:
                            j+=1
                            df_new['ID'].append('1')
                            df_new['MATNR'].append(df[i][12])
                            df_new['WERKS'].append('1101')
                            df_new['TEXT1'].append(df[i][13])
                            df_new['STLAL'].append('1')
                            df_new['STLAN'].append('1')
                            ztekst = 'Ламинация + Наклейка + Упаковка'
                            df_new['ZTEXT'].append(ztekst)
                            df_new['STKTX'].append(ztekst)
                            df_new['BMENG'].append( '1000')
                            df_new['BMEIN'].append('ШТ')
                            df_new['STLST'].append('1')
                            df_new['POSNR'].append('')
                            df_new['POSTP'].append('')
                            df_new['MATNR1'].append('')
                            df_new['TEXT2'].append('')
                            df_new['MEINS'].append('')
                            df_new['MENGE'].append('')
                            df_new['DATUV'].append('01012021')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('')
                            length = df[i][12].split('-')[0]
                            for k in range(0,qatorlar_soni):
                                j+=1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                
                                
                                if k == 0 :
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new['MATNR1'].append('1300000064')
                                    df_new['TEXT2'].append('KLEIBERIT 704,5')
                                    df_new['MENGE'].append('КГ')
                                    df_new['MEINS'].append( "{:0f}".format(float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==2:
                                    df_new['MATNR1'].append('1300000068')
                                    df_new['TEXT2'].append('KLEIBERIT Primer 831,0')
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==3:
                                    df_new['MATNR1'].append('1000001020')
                                    df_new['TEXT2'].append('Пленка П2 NS35см 140мк Grey1')
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==4:
                                    df_new['MATNR1'].append(laminatsiya.sap_code_s4q100)
                                    df_new['TEXT2'].append(laminatsiya.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinsL)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                df_new['LGORT'].append('PS11')
                        if qatorlar_soni == 6:
                            print('ichida',laminatsiya)
                            jjj =0
                            for nakleykaa in nakleyka_results:
                                jjj += 1
                                j+=1
                                df_new['ID'].append('1')
                                df_new['MATNR'].append(df[i][12])
                                df_new['WERKS'].append('1101')
                                df_new['TEXT1'].append(df[i][13])
                                df_new['STLAL'].append(f'{jjj}')
                                df_new['STLAN'].append('1')
                                ztekst = 'Ламинация + Наклейка + Упаковка'
                                df_new['ZTEXT'].append(ztekst)
                                df_new['STKTX'].append(ztekst)
                                df_new['BMENG'].append( '1000')
                                df_new['BMEIN'].append('ШТ')
                                df_new['STLST'].append('1')
                                df_new['POSNR'].append('')
                                df_new['POSTP'].append('')
                                df_new['MATNR1'].append('')
                                df_new['TEXT2'].append('')
                                df_new['MEINS'].append('')
                                df_new['MENGE'].append('')
                                df_new['DATUV'].append('01012021')
                                df_new['PUSTOY'].append('')
                                df_new['LGORT'].append('')
                                length = df[i][12].split('-')[0]
                                for k in range(0,qatorlar_soni):
                                    j+=1
                                    df_new['ID'].append('2')
                                    df_new['MATNR'].append('')
                                    df_new['WERKS'].append('')
                                    df_new['TEXT1'].append('')
                                    df_new['STLAL'].append('')
                                    df_new['STLAN'].append('')
                                    df_new['ZTEXT'].append('')
                                    df_new['STKTX'].append('')
                                    df_new['BMENG'].append('')
                                    df_new['BMEIN'].append('')
                                    df_new['STLST'].append('')
                                    df_new['POSNR'].append(k+1)
                                    df_new['POSTP'].append('L')
                                    
                                    
                                    if k == 0 :
                                        df_new['MATNR1'].append(older_process['sapcode'])
                                        df_new['TEXT2'].append(older_process['kratkiy'])
                                        df_new['MEINS'].append('1000')
                                        df_new['MENGE'].append('ШТ')
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==1:
                                        df_new['MATNR1'].append('1300000064')
                                        df_new['TEXT2'].append('KLEIBERIT 704,5')
                                        df_new['MENGE'].append('КГ')
                                        df_new['MEINS'].append( "{:0f}".format(float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==2:
                                        df_new['MATNR1'].append('1300000068')
                                        df_new['TEXT2'].append('KLEIBERIT Primer 831,0')
                                        df_new['MENGE'].append("КГ")
                                        df_new['MEINS'].append("{:0f}".format(float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==3:
                                        df_new['MATNR1'].append('1000001020')
                                        df_new['TEXT2'].append('Пленка П2 NS35см 140мк Grey1')
                                        df_new['MENGE'].append("КГ")
                                        df_new['MEINS'].append("{:0f}".format(float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==4:
                                        
                                        df_new['MATNR1'].append(nakleykaa.sap_code_s4q100)
                                        df_new['TEXT2'].append(nakleykaa.название)
                                        df_new['MENGE'].append("М2")
                                        df_new['MEINS'].append("{:0f}".format((meinss*mein_percent)))
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    if k==5:
                                        
                                        df_new['MATNR1'].append(laminatsiya.sap_code_s4q100)
                                        df_new['TEXT2'].append(laminatsiya.название)
                                        df_new['MENGE'].append("М2")
                                        df_new['MEINS'].append(float(meinsL)*mein_percent)
                                        df_new['DATUV'].append('')
                                        df_new['PUSTOY'].append('')
                                    
                                    df_new['LGORT'].append('PS11')
                    
                        if qatorlar_soni == 7:
                            j+=1
                            df_new['ID'].append('1')
                            df_new['MATNR'].append(df[i][12])
                            df_new['WERKS'].append('1101')
                            df_new['TEXT1'].append(df[i][13])
                            df_new['STLAL'].append(f'1')
                            df_new['STLAN'].append('1')
                            ztekst = 'Ламинация + Наклейка + Упаковка'
                            df_new['ZTEXT'].append(ztekst)
                            df_new['STKTX'].append(ztekst)
                            df_new['BMENG'].append( '1000')
                            df_new['BMEIN'].append('ШТ')
                            df_new['STLST'].append('1')
                            df_new['POSNR'].append('')
                            df_new['POSTP'].append('')
                            df_new['MATNR1'].append('')
                            df_new['TEXT2'].append('')
                            df_new['MEINS'].append('')
                            df_new['MENGE'].append('')
                            df_new['DATUV'].append('01012021')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('')
                            length = df[i][12].split('-')[0]
                            for k in range(0,qatorlar_soni):
                                j+=1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                
                                
                                if k == 0 :
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new['MATNR1'].append('1300000064')
                                    df_new['TEXT2'].append('KLEIBERIT 704,5')
                                    df_new['MENGE'].append('КГ')
                                    df_new['MEINS'].append( "{:0f}".format(float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==2:
                                    df_new['MATNR1'].append('1300000068')
                                    df_new['TEXT2'].append('KLEIBERIT Primer 831,0')
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==3:
                                    df_new['MATNR1'].append('1000001020')
                                    df_new['TEXT2'].append('Пленка П2 NS35см 140мк Grey1')
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==4:
                                    df_new['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result1.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinss1)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k==5:
                                    df_new['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result2.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinss2)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==6:
                                    
                                    df_new['MATNR1'].append(laminatsiya.sap_code_s4q100)
                                    df_new['TEXT2'].append(laminatsiya.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinsL)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                df_new['LGORT'].append('PS11')
                    
                        if qatorlar_soni == 8:
                            j += 1
                            df_new['ID'].append('1')
                            df_new['MATNR'].append(df[i][12])
                            df_new['WERKS'].append('1101')
                            df_new['TEXT1'].append(df[i][13])
                            df_new['STLAL'].append('1')
                            df_new['STLAN'].append('1')
                            ztekst = 'Ламинация + Наклейка + Упаковка'
                            df_new['ZTEXT'].append(ztekst)
                            df_new['STKTX'].append(ztekst)
                            df_new['BMENG'].append( '1000')
                            df_new['BMEIN'].append('ШТ')
                            df_new['STLST'].append('1')
                            df_new['POSNR'].append('')
                            df_new['POSTP'].append('')
                            df_new['MATNR1'].append('')
                            df_new['TEXT2'].append('')
                            df_new['MEINS'].append('')
                            df_new['MENGE'].append('')
                            df_new['DATUV'].append('01012021')
                            df_new['PUSTOY'].append('')
                            df_new['LGORT'].append('')
                            length = df[i][12].split('-')[0]
                            for k in range(0,qatorlar_soni):
                                j+=1
                                df_new['ID'].append('2')
                                df_new['MATNR'].append('')
                                df_new['WERKS'].append('')
                                df_new['TEXT1'].append('')
                                df_new['STLAL'].append('')
                                df_new['STLAN'].append('')
                                df_new['ZTEXT'].append('')
                                df_new['STKTX'].append('')
                                df_new['BMENG'].append('')
                                df_new['BMEIN'].append('')
                                df_new['STLST'].append('')
                                df_new['POSNR'].append(k+1)
                                df_new['POSTP'].append('L')
                                
                                
                                if k == 0 :
                                    df_new['MATNR1'].append(older_process['sapcode'])
                                    df_new['TEXT2'].append(older_process['kratkiy'])
                                    df_new['MEINS'].append('1000')
                                    df_new['MENGE'].append('ШТ')
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==1:
                                    df_new['MATNR1'].append('1300000064')
                                    df_new['TEXT2'].append('KLEIBERIT 704,5')
                                    df_new['MENGE'].append('КГ')
                                    df_new['MEINS'].append( "{:0f}".format(float(alum_teks.лам_рас_клея_на_1000_штук_пр_кг)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==2:
                                    df_new['MATNR1'].append('1300000068')
                                    df_new['TEXT2'].append('KLEIBERIT Primer 831,0')
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.лам_рас_праймера_на_1000_штук_пр_кг)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==3:
                                    df_new['MATNR1'].append('1000001020')
                                    df_new['TEXT2'].append('Пленка П2 NS35см 140мк Grey1')
                                    df_new['MENGE'].append("КГ")
                                    df_new['MEINS'].append("{:0f}".format(float(alum_teks.лам_рас_уп_материала_мешок_на_1000_пр)*mein_percent))
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                if k==4:
                                    df_new['MATNR1'].append(nakleyka_result1.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result1.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinss1)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k==5:
                                    df_new['MATNR1'].append(nakleyka_result2.sap_code_s4q100)
                                    df_new['TEXT2'].append(nakleyka_result2.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinss1)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k == 6:
                                    df_new['MATNR1'].append(laminatsiya_result1.sap_code_s4q100)
                                    df_new['TEXT2'].append(laminatsiya_result1.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinsL1)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                if k == 7:
                                    df_new['MATNR1'].append(laminatsiya_result2.sap_code_s4q100)
                                    df_new['TEXT2'].append(laminatsiya_result2.название)
                                    df_new['MENGE'].append("М2")
                                    df_new['MEINS'].append(float(meinsL2)*mein_percent)
                                    df_new['DATUV'].append('')
                                    df_new['PUSTOY'].append('')
                                
                                df_new['LGORT'].append('PS11')
                    
                    
                    
                older_process['sapcode'] =df[i][12]
                older_process['kratkiy'] =df[i][13]
                
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR")
    minut =now.strftime("%M-%S")    
                 
            
    create_folder(f'{MEDIA_ROOT}\\uploads\\','norma')
    create_folder(f'{MEDIA_ROOT}\\uploads\\norma\\',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\norma\\{year}\\',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\norma\\{year}\\{month}\\',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\norma\\{year}\\{month}\\{day}\\',hour)
            
            
    
    path =f'{MEDIA_ROOT}\\uploads\\norma\\{year}\\{month}\\{day}\\{hour}\\norma-{product_type}-{minut}.xlsx'
    
    
    dff =pd.DataFrame(df_new)
    # path =os.path.join(os.path.expanduser("~/Desktop"),'new_base_cominirovaniy.xlsx')
    
    dff.to_excel(path)
    return redirect('norma_file_upload')
  

def generatenewexceldata(request):
    path1 =os.path.join(os.path.expanduser("~/Desktop/generate"),'data.xlsx')
    df0 = pd.read_excel(path1,'baza1')
    
    df =excelgenerate(df0)
    path2 =os.path.join(os.path.expanduser("~/Desktop/generate"),'generated_data.xlsx')
    df.to_excel(path2)
    
    return JsonResponse({'File':'Genarated!!'})

def remove_whitespace(request):
    normas = Norma.objects.all()
    
    for norma in normas:
        print(norma.id)
        norma.компонент_1 = norma.компонент_1.strip()
        norma.компонент_2 = norma.компонент_1.strip()
        norma.компонент_3 = norma.компонент_1.strip()
        norma.артикул = norma.артикул.strip()
        norma.save()
        
    return JsonResponse({'a':'b'})


def nakleyka_duplicate_del(request):
    nakleykas = Nakleyka.objects.all()
      
    for nakleyka in nakleykas:
        nak =Nakleyka.objects.filter(код_наклейки =nakleyka.код_наклейки,ширина=nakleyka.ширина)
        if len(nak)>1:
            i=1
            for n in nak:
                if i ==1:
                    i+=1
                    continue
                n.delete()
                i+=1
              
    return JsonResponse({'a':'b'})


def norma_for_list():
        normas = Norma.objects.all().values_list("компонент_1","компонент_2","компонент_3",'артикул')
        normass =[]
        for norm in normas:
            for n in norm:
                if n !='0' and n!='nan':
                    normass.append(n)
        norma_unique =set(normass)
        
        kraskas = Kraska.objects.all().values_list('код_краски_в_профилях',flat=True)
        
        return norma_unique,kraskas