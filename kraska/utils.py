import modin.pandas as pd
from datetime import datetime
from kraska.models import OrderKraska 
from aluminiy.utils import zip,create_folder
from config.settings import MEDIA_ROOT
import os
import numpy as np


def characteristika_created_txt_create(datas):
    now = datetime.now()
    year =now.strftime("%Y")
    month =now.strftime("%B")
    day =now.strftime("%a%d")
    hour =now.strftime("%H HOUR %M %S")
    minut =now.strftime("%M-%S MINUT")
    
    parent_dir =f'{MEDIA_ROOT}\\uploads\\kraska'
    if not os.path.isdir(parent_dir):
        create_folder(f'{MEDIA_ROOT}\\uploads','kraska')
        
    create_folder(f'{MEDIA_ROOT}\\uploads\\kraska',f'{year}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\kraska\\{year}',f'{month}')
    create_folder(f'{MEDIA_ROOT}\\uploads\\kraska\\{year}\\{month}',day)
    create_folder(f'{MEDIA_ROOT}\\uploads\\kraska\\{year}\\{month}\\{day}',f'{hour}')
    pathzip =f'{MEDIA_ROOT}\\uploads\\kraska\\{year}\\{month}\\{day}\\{hour}'

     
    obyekt = ExcelToTxt(sapcode=datas['sapcode'], kratkiy=datas['kratkiy'], narx=datas['narx'])
    kraska = obyekt.kraska  
    obyekt.generate_txt_files(frame=kraska, path=pathzip) 

    file_path =f'{pathzip}.zip'
    
    zip(pathzip, pathzip)

    return [file_path,]

class ExcelToTxt:
    
    """
    SAP tizimiga yuklash uchun .txt fayllarni tayyorlashga mo'ljallangan klass.

    Ushbu klass berilgan parametrlar asosida SAP tizimiga yuklash uchun tayyor .txt fayllar yaratadi.

    ### Parametrlar:
    - **sapcode**: `str` | `Majburiy` 
        Materialning SAP kodini (`MATNR`) ifodalaydi. Bu SAP tizimida materiallarni unikal tarzda aniqlash uchun ishlatiladigan 18 belgidan iborat identifikator.
      
    - **kratkiy**: `str` | `Majburiy`
        Materialning qisqa tavsifi (`MAKTX`). Odatda mahsulotlar nomi yoki qisqa tavsifini ko'rsatadigan 40 belgili maydon.
      
    - **narx**: `float` | `Majburiy`
        Materialning standart narxi (`STPRS`). Materialning asosiy narxini ko'rsatadi va raqamli formatda bo'ladi.
      
    - **brutto**: `float` | `Default=1` 
        Materialning umumiy og'irligi (`BRGEW`). Qadoqlash bilan birga bo'lgan umumiy og'irlikni ifodalaydi, odatda bu raqamli formatdagi maydon.
    
    ### Metodlar:
    - **__init__(self, sapcode, kratkiy, narx, brutto)**: 
        Ob'ektni berilgan parametrlar bilan boshlaydi.
      
    - **excel_to_txt(self)**: 
        Kiruvchi parametrlar asosida asosiy DataFrame yaratadi va SAP tizimiga yuklash uchun zarur bo'lgan maydonlarni standart qiymatlar bilan to'ldiradi.
      
    - **txt_1(self, frame, path)**: 
        Materialning asosiy ma'lumotlarini o'z ichiga olgan `.txt` faylni yaratadi va ko'rsatilgan manzilga saqlaydi.
      
    - **txt_2(self, frame, path)**: 
        Ta'minot va material boshqaruvi bo'yicha ma'lumotlarni o'z ichiga olgan `.txt` faylni yaratadi va ko'rsatilgan manzilga saqlaydi.
      
    - **txt_3(self, frame, path)**: 
        Sotish va tarqatish bo'yicha ma'lumotlarni o'z ichiga olgan `.txt` faylni yaratadi va ko'rsatilgan manzilga saqlaydi.
      
    - **txt_4(self, frame, path)**: 
        Saqlash joyi bo'yicha ma'lumotlarni o'z ichiga olgan `.txt` faylni yaratadi va ko'rsatilgan manzilga saqlaydi.
      
    Ushbu klass SAP tizimiga kerakli bo'lgan .txt fayllarni yaratishni osonlashtiradi va unumdorlikni oshiradi.
    """

    def __init__(self, sapcode, kratkiy, narx, brutto=1): 
        if type(sapcode) == str:
            self.sapcode = [sapcode]
            self.kratkiy = [kratkiy]
        else:
            self.sapcode = sapcode
            self.kratkiy = kratkiy

        self.price = narx
        if type(brutto) != list:
            self.brutto = [1] * len(sapcode)
        else:
            self.brutto = brutto

        werks_kraska = [4702, '47D1', '47D2', '47D3', '47D4', '47D5']
        werks_epdm = [4701, '47D1', '47D2', '47D3', '47D4', '47D5']
        
        
        self.kraska = self.excel_to_txt(werks=werks_kraska, BEI='КГ', spart=30, dispo='KR1', tex_karta='Z0ZKPK')
        self.epdm = self.excel_to_txt(werks=werks_epdm, BEI='ШТ', spart=8, dispo='EP1')

    def excel_to_txt(self, werks, BEI, spart, dispo, tex_karta=None):
        columns_all = ['MATNR', 'MAKTX', 'WERKS', 'MATKL', 'LGFSB', 'SCM_STRA1', 'KONDM', 'LADGR', 'MTPOS_MARA', 'GEWEI', 'STRGR', 'SBDKZ', 'VKORG', 'PEINH', 'LGPRO',
                       'VRKME', 'LOSGR', 'NTGEW', 'XCHPF', 'VRMOD', 'LGORT', 'DISGR', 'VTWEG', 'DISLS', 'PERKZ', 'SFCPF', 'DISPO', 'SOBSL', 'MTPOS', 'TAXKM', 'SCM_RRP_TYPE',
                       'VERSG', 'BRGEW', 'DISMM', 'EKGRP', 'HKMAT', 'UEETK', 'TATYP', 'ALAND', 'VPRSV', 'SCM_PROFID', 'PRCTR', 'TRAGR', 'SCM_HEUR_ID',
                       'MLAST', 'BWKEY', 'BESKZ', 'MEINS', 'BKLAS', 'MTART', 'PPSKZ', 'MTVFP', 'STPRS', 'SCM_WHATBOM', 'KTGRM', 'PLIFZ', 'BISMT', 'SPART', 'EKALR', 'WEBAZ']

        result = pd.DataFrame(columns=columns_all)
        ind = 0
        for code in self.sapcode:
            if 'PDM' in code.upper():
                tex_karta = 'Z0ZEEU'
            elif ('IDN' in code.upper()) or ('PDS' in code.upper()):
                tex_karta = 'Z0ZEPU'
            df = pd.DataFrame(columns=columns_all)
            df['WERKS'] = werks
            df['SFCPF'][0] = tex_karta
            df[['MATNR', 'BISMT']] = code
            df['MAKTX'] = self.kratkiy[ind]
            df['NTGEW'] = self.brutto[ind]
            df['BRGEW'] = self.brutto[ind]
            df['STPRS'] = self.price[ind]
            ind += 1
            result = pd.concat([result, df], ignore_index=True)

        result['MEINS'] = BEI
        result['SPART'] = spart
        result['PRCTR'] = werks[0]
        result['BWKEY'] = result['WERKS']
        result.loc[result['WERKS'].apply(lambda x: isinstance(x, int)), 'DISPO'] = dispo
        result['XCHPF'] = 'X'
        result['EKALR'] = 'X'
        result['UEETK'] = 'X'
        result['HKMAT'] = 'X'
        result['PERKZ'] = 'M'
        result['VPRSV'] = 'S'
        result['ALAND'] = 'UZ'
        result['GEWEI'] = 'КГ'
        result['DISMM'] = 'PD'
        result['DISLS'] = 'MB'
        result['MTART'] = 'ZPRF'
        result['TATYP'] = 'MWST'
        result['MATKL'] = 'ACSUZGP'
        result['MTPOS_MARA'] = 'NORM'
        result['MTPOS'] = 'NORM'
        result['LADGR'] = '0001'
        result['TRAGR'] = '0001'
        result['KTGRM'] = '01'
        result['KONDM'] = '01'
        result['MTVFP'] = '02'
        result['BKLAS'] = '0100'
        result['WEBAZ'] = 0
        result['LOSGR'] = 1
        result['PEINH'] = 1
        result['TAXKM'] = 1
        result['VERSG'] = 1
        result['SBDKZ'] = 2
        result['MLAST'] = 3
        result['VTWEG'] = 10
        result['SOBSL'] = 20
        result['SCM_STRA1'] = 26
        result['EKGRP'] = 999
        result['VKORG'] = 4700

        result.loc[result['WERKS'].apply(lambda x: isinstance(x, int)), 'BESKZ'] = 'E'
        result.loc[result['WERKS'].apply(lambda x: isinstance(x, int)), 'SCM_PROFID'] = 'SAP999'
        result.loc[result['WERKS'].apply(lambda x: isinstance(x, int)), 'SCM_HEUR_ID'] = 'Z_SAP_PP_002'
        result.loc[result['WERKS'].apply(lambda x: isinstance(x, int)), 'STRGR'] = 10
        result.loc[result['WERKS'].apply(lambda x: isinstance(x, int)), 'SCM_RRP_TYPE'] = 4
        result.loc[result['WERKS'].apply(lambda x: isinstance(x, int)), ['VRMOD', 'SCM_WHATBOM']] = 5
        result['BESKZ'] = result['BESKZ'].fillna('F')
        result['DISPO'] = result['DISPO'].fillna('001')

        return result

    def txt_1(self, frame, path='1.txt'):
        columns_1 = ['MATNR', 'BISMT', 'MAKTX', 'MEINS', 'MTART', 'MATKL', 'WERKS', 'BESKZ', 'SPART', 'BRGEW', 'NTGEW', 'GEWEI', 'MTPOS_MARA']
        header1 ='MATNR\tBISMT\tMAKTX\tMEINS\tMTART\tMATKL\tWERKS\tBESKZ\tSPART\tBRGEW\tNTGEW\tGEWEI\tMTPOS_MARA'
        result_txt = frame[columns_1]
        np.savetxt(path, result_txt.values, fmt='%s', delimiter="\t",header=header1,comments='',encoding='ansi')
        return 

    def txt_2(self, frame, path='2.txt'):
        columns_2 = [
            'MAKTX', 'MEINS', 'MTART', 'MATNR', 'WERKS', 'EKGRP', 'XCHPF', 'DISGR',
            'DISMM', 'DISPO', 'DISLS', 'WEBAZ', 'BESKZ', 'LGFSB', 'PLIFZ', 'PERKZ',
            'MTVFP', 'SCM_STRA1', 'VRMOD', 'PPSKZ', 'SCM_WHATBOM', 'SCM_HEUR_ID',
            'SCM_RRP_TYPE', 'SCM_PROFID', 'STRGR', 'BWKEY', 'MLAST', 'BKLAS', 'VPRSV',
            'PEINH', 'STPRS', 'PRCTR', 'EKALR', 'HKMAT', 'LOSGR', 'SFCPF', 'UEETK',
            'LGPRO', 'SBDKZ', 'SOBSL']
        header2 ='MAKTX\tMEINS\tMTART\tMATNR\tWERKS\tEKGRP\tXCHPF\tDISGR\tDISMM\tDISPO\tDISLS\tWEBAZ\tBESKZ\tLGFSB\tPLIFZ\tPERKZ\tMTVFP\tSCM_STRA1\tVRMOD\tPPSKZ\tSCM_WHATBOM\tSCM_HEUR_ID\tSCM_RRP_TYPE\tSCM_PROFID\tSTRGR\tBWKEY\tMLAST\tBKLAS\tVPRSV\tPEINH\tSTPRS\tPRCTR\tEKALR\tHKMAT\tLOSGR\tSFCPF\tUEETK\tLGPRO\tSBDKZ\tSOBSL'

        result_txt = frame[columns_2]
        np.savetxt(path, result_txt.values, fmt='%s', delimiter="\t",header=header2,comments='',encoding='ansi')
        return 

    def txt_3(self, frame, path='3.txt'):
        vtweg = [10, 20, 99]
        columns_3 = [
            'MAKTX', 'MEINS', 'MTART', 'SPART', 'MATNR', 'WERKS', 'VKORG', 'MTPOS',
            'VTWEG', 'PRCTR', 'MTVFP', 'ALAND', 'TATYP', 'TAXKM', 'VERSG', 'KTGRM',
            'KONDM', 'LADGR', 'TRAGR']
        header3 ='MAKTX\tMEINS\tMTART\tSPART\tMATNR\tWERKS\tVKORG\tMTPOS\tVTWEG\tPRCTR\tMTVFP\tALAND\tTATYP\tTAXKM\tVERSG\tKTGRM\tKONDM\tLADGR\tTRAGR'
        result_txt = pd.DataFrame(columns=columns_3)
        frame = frame[columns_3]
        for vt in vtweg:
            frame_copy = frame.copy()  
            frame_copy.loc[:, 'VTWEG'] = vt  
            result_txt = pd.concat([result_txt, frame_copy])
        # result_txt.to_csv(path, sep='\t', index=False)
        np.savetxt(path, result_txt.values, fmt='%s', delimiter="\t",header=header3,comments='',encoding='ansi')
        return 

    def txt_4(self, frame, path='4.txt'):
        sapcode = frame['MATNR'].unique()
        header4='MATNR\tWERKS\tLGORT'
        df = pd.DataFrame(columns=['MATNR', 'WERKS', 'LGORT'])
        result_txt = pd.DataFrame(columns=['MATNR', 'WERKS', 'LGORT'])
        
        for code in sapcode:
            if 'PDM' in code.upper():
                lgort = ['PS02', 'S400']
            elif ('IDN' in code.upper()) or ('PDS' in code.upper()):
                lgort = ['PS03 ', 'S400']
            else:
                lgort = ['PS01', 'S400']
    
            df['LGORT'] = lgort
            df['MATNR'] = code
            df['WERKS'] = int(frame['WERKS'][0])
            result_txt = pd.concat([result_txt, df])
        result_txt = result_txt.copy()
        np.savetxt(path, result_txt.values, fmt='%s', delimiter="\t",header=header4,comments='',encoding='ansi')
        return 

    def generate_txt_files(self, frame, path):
        """
            - **generate_txt_files(self, frame, path)**: 
        Yuqoridagi `txt` metodlarini hammasini birdaniga ishga tushirib, yaratgan `.txt` fayllarni ko'rsatilgan manzilga saqlaydi va tegishli DataFramelarni qaytaradi.

    ### Foydalanish Misoli:
    ```python
    # Klassga argumentlar berish
    sapcode = ['ACS.502.PDM-7001', 'PNT.7034.GLS-7001']
    kratkiy = ['Mahsulot A', 'Mahsulot B']
    narx = [100, 200]
    brutto = [1.5, 2.0]
    
    # Obyekt yaratish
    obyekt = ExcelToTxt(sapcode, kratkiy, narx, brutto)
    
    # Kerakli metodga murojaat qilish
    kraska = obyekt.kraska | epdm = obyekt.epdm
    Yuqoridagi metodlar DataFrame qaytaradi
    
    # .txt fayllarni ko'rsatilgan manzilga saqlash
    txt_files = obyekt.generate_txt_files(frame=kraska, path='saqlash/manzili')
    ```
    

        """
        result_1 = self.txt_1(frame, f"{path}/1.txt")
        result_2 = self.txt_2(frame, f"{path}/2.txt")
        result_3 = self.txt_3(frame, f"{path}/3.txt")
        result_4 = self.txt_4(frame, f"{path}/4.txt")
        
        return 






   