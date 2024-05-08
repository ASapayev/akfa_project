class BasePokritiya{
    constructor(
        id = NaN,//done 
        full = false,//done
        brend = NaN,//done
        mikron = NaN,//done
        storonnost = NaN,//done
        kod_sveta =NaN,
        naz_sveta =NaN,
        tip_paneli =NaN,
        dlina = NaN,//done
        shirina = NaN,//done
        gruppa_materialov = NaN,//done
        kratkiy_tekst = NaN,//done
        sap_code = NaN,//done
        krat = NaN,//done
        comment = NaN,//done
        pickupdate = NaN,//done
        sena_c_nds = NaN,//done
        sena_bez_nds = NaN,//done
        online_id = NaN,//done
        nazvaniye_ruchnoy = NaN,//done
        svet_product=NaN,//done
        group_zakup=NaN,//done
        group=NaN,//done
        tip=NaN,//done
        segment = NaN,//done
        buxgalter_tovar = NaN,//done
        buxgalter_uchot = NaN,//done
        bazoviy_edin = NaN,//done
        alter_edin = NaN,//done
        status_online = NaN,//done
        zavod_name = NaN,//done
        diller = NaN,//done
        tip_clenta = NaN,//done
        is_active = false
        ) {
        this.id = id;//done 
        this.full = full ;//done
        this.brend = brend;//done
        this.mikron = mikron;//done
        this.storonnost = storonnost;//done
        this.kod_sveta = kod_sveta;
        this.naz_sveta = naz_sveta;
        this.tip_paneli = tip_paneli;
        this.dlina = dlina;//done
        this.shirina = shirina;//done
        this.gruppa_materialov = gruppa_materialov;//done
        this.kratkiy_tekst = kratkiy_tekst;//done
        this.sap_code = sap_code;//done
        this.krat = krat;//done
        this.comment = comment;//done
        this.pickupdate = pickupdate;//done
        this.sena_c_nds = sena_c_nds;//done
        this.sena_bez_nds = sena_bez_nds;//done
        this.online_id = online_id;//done
        this.nazvaniye_ruchnoy = nazvaniye_ruchnoy;//done
        this.svet_product = svet_product;//done
        this.group_zakup = group_zakup;//done
        this.group = group;//done
        this.tip = tip;//done
        this.segment = segment;//done
        this.buxgalter_tovar = buxgalter_tovar;//done
        this.buxgalter_uchot = buxgalter_uchot;//done
        this.bazoviy_edin = bazoviy_edin;//done
        this.alter_edin = alter_edin;//done
        this.status_online = status_online;//done
        this.zavod_name = zavod_name;//done
        this.diller = diller;//done
        this.tip_clenta = tip_clenta;//done
        this.is_active = is_active 
    }
    get_kratkiy_tekst(){
        switch(this.id){
            case 1: if(this.brend && this.storonnost && this.mikron && this.kod_sveta && this.tip_paneli && this.dlina && this.shirina){
                
                    if(this.is_active){
                        
                        if (this.online_id && this.nazvaniye_ruchnoy){
        
                           
                            return {'text':this.brend + ' '+this.mikron+' '+ this.storonnost + ' ' + this.kod_sveta +'  ' +this.tip_paneli+'  ' +this.dlina +'x' +this.shirina,'accept':true}
                        }else{
                            
                            return {'text':this.brend + ' '+this.mikron+' '+ this.storonnost + ' ' + this.kod_sveta +'  ' +this.tip_paneli+'  ' +this.dlina +'x' +this.shirina,'accept':false}
                        }
                        
                    }else{
                        
                        if ( this.pickupdate && this.sena_bez_nds && this.sena_c_nds && this.group && this.buxgalter_tovar && this.diller && this.tip_clenta){
                            
                            
                            return {'text':this.brend + ' '+this.mikron+' '+ this.storonnost + ' ' + this.kod_sveta +'  ' +this.tip_paneli+'  ' +this.dlina +'x' +this.shirina,'accept':true}
                        }else{
                            
                            return {'text':this.brend + ' '+this.mikron+' '+ this.storonnost + ' ' + this.kod_sveta +'  ' +this.tip_paneli+'  ' +this.dlina +'x' +this.shirina,'accept':false}
                        }
                    } 
        
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
    
               
       
       
    }
    }
}


text =""

data_base = {}

for (let i = 1; i <= 10; i++) {
    
    text +=`
    <tr id='table_tr` +String(i)+`' >                   
    <td >
        <div class="input-group input-group-sm mb-1">
            <div class="btn-group" role="group" aria-label="Basic example">
                <button type="button" class="btn btn-secondary btn-sm" onclick="create(`+String(i)+`)" id='create_btn`+String(i)+`' >Создание</button>
                <button type="button" class="btn btn-info btn-sm" onclick="activate(`+String(i)+`)" id='activate_btn`+String(i)+`'>Активация</button>
                <button type="button" class="btn btn-warning btn-sm gradient-buttons" onclick="clear_artikul(`+String(i)+`)"  id='clear_btn`+String(i)+`'>Очистить</button>
            </div>
        </div>
    </td>
    <td >
    <select class="form-select" aria-label="" style="width: 177px;text-transform: uppercase; font-size:12px; padding-right:0px;" onchange="create_kratkiy_tekst(`+String(i)+`)" disabled id='brend`+String(i)+`' required>
        <option  selected ></option>
        <option value="AKFA" >AKFA</option>
        <option value="ROYAL" >ROYAL</option>
    </select>
    </td>
    <td >
    <select class="form-select" aria-label="" style="width: 177px;text-transform: uppercase; font-size:12px; padding-right:0px;" onchange="create_kratkiy_tekst(`+String(i)+`)" disabled id='mikron`+String(i)+`' required>
        <option  selected ></option>
        <option value="180" >180</option>
        <option value="210">210</option>
        <option value="250">250</option>
        <option value="400">400</option>
        <option value="700">700</option>
    </select>
    </td>
    <td >
    <select class="form-select" aria-label="" style="width: 177px;text-transform: uppercase; font-size:12px; padding-right:0px;" onchange="create_kratkiy_tekst(`+String(i)+`)" disabled id='storonnost`+String(i)+`' required>
        <option  selected ></option>
        <option value="X1">X1</option>
        <option value="X2">X2</option>
    </select>
    </td>
    
    
    <td >
        <select class="form-select" aria-label="" style="width: 177px;text-transform: uppercase; font-size:12px; padding-right:0px;" onchange="create_kratkiy_tekst(`+String(i)+`)" disabled id='kod_sveta`+String(i)+`' required>
            <option  selected ></option>
            <option value="Глянцево-Белый">771</option>
            <option value="Металлик">772</option>
            <option value="Глянцево-Молочный">773</option>
            <option value="Дуб Мокко">777</option>
            <option value="Золотой дуб ламинат">778</option>
            <option value="Глянцево-Коричневый">779</option>
            <option value="Белый матовый">780</option>
            <option value="Мокрый асфальт">782</option>
            <option value="Тёмно Серый">784</option>
            <option value="Жемчуг">806</option>
            <option value="Каштан">807</option>
            <option value="Орех">808</option>
            <option value="Светло-Зелёный">776</option>
            <option value="Глянцево-Чёрный">781</option>
            <option value="Тёмно-Синий">783</option>
            <option value="Красный">785</option>
            <option value="Мис">703</option>
            <option value="Травертин">803</option>
            <option value="З/Д Белый">800</option>
            <option value="З/Д Серый">801</option>
            <option value="Мрамор">802</option>
            <option value="Чёрный мрамор">804</option>
            <option value="Silver">809</option>
            <option value="Белый мрамор">810</option>
            <option value="Серый матовый">786</option>
            <option value="Чёрный матовый">787</option>
            <option value="Светло Серый">790</option>
            <option value="Жёлтый матовый">789</option>
            <option value="Cиний Mатовый">788</option>
            <option value="Светло Серый">790</option>
        
        </select>
    </td>
    
    <td >
        
        <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;" id ='naz_sveta` +String(i)+`'></span>
        
    </td>
    <td >
    <select class="form-select" aria-label="" style="width: 177px;text-transform: uppercase; font-size:12px; padding-right:0px;" onchange="create_kratkiy_tekst(`+String(i)+`)" disabled id='tip_paneli`+String(i)+`' required>
        <option  selected ></option>
        <option value="A1">A1</option>
        <option value="A2">A2</option>
    </select>
    </td>

    <td >
        <div class="input-group input-group-sm mb-1">
        
            <input type='text' class=" form-control " style=" width: 110px; font-size:10px; display:none; height:32px" id='dlina`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>

        </div>
       
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1">
        
            <input type='text' class=" form-control " style=" width: 110px; font-size:10px; display:none; height:32px" id='shirina`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>

        </div>
    </td>
    <td >
         <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;padding-left:35%" id='gruppa_materialov`+String(i)+`'>AKPGP</span>
    
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='kratkiy_tekst`+String(i)+`'></span>
        </div>
    </td>

    <td >
        <div class="input-group input-group-sm mb-1">
       
        <input type='text' class=" form-control " style=" width: 110px; font-size:10px; display:none; height:32px" id='sap_code`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
    
        </div>
    </td> 
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style=" width: 220px; font-size:10px; display:none; height:32px"  id='krat`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1">
       <textarea   rows='1' class=" form-control " style="width: 220px; font-size:10px;display:none;height:32px" id='comment`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></textarea >
       </div>
    </td>
    <td >
        <input  style='display:none; line-height:15px' type="date" class="form-control" id="pickupdate`+String(i)+`" onchange='create_kratkiy_tekst(`+String(i)+`)'>      
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style=" width: 75px; font-size:10px; display:none;height:32px" id='sena_c_nds`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style=" width: 75px; font-size:10px; display:none; height:32px" id='sena_bez_nds`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style=" width: 75px; font-size:10px;display:none;height:32px " id='online_id`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <textarea   rows='1' class=" form-control " style=" width: 220px; font-size:10px; display:none; height:32px" id='nazvaniye_ruchnoy`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></textarea >
        </div>
    </td>
    
    <td >
        <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='svet_product`+String(i)+`'>Colour</span>
        
    </td>
    <td >
        <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='group_zakup`+String(i)+`'>Alucobond</span>
    
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 230px;text-transform: uppercase; font-size:12px; padding-right:0px;  display:none;" id='group`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option value="Bez Nakleyka"> Nakleyka</option>
            <option value="Bez Nakleyka TR"> Nakleyka TR</option>
            <option value="Engelberg (40 MIKRON)">Engelberg (40 MIKRON)</option>
            <option value="IBOARD 35 (21mk) (1.22x2.44mm)">IBOARD 35 (21mk) (1.22x2.44mm)</option>
            <option value="IBOARD CH (18mk)">IBOARD CH (18mk)</option>
            <option value="Iboard (Negaryuchiy)">Iboard (Negaryuchiy)</option>
            <option value="IBOARD TR (25mk)">IBOARD TR (25mk)</option>
            <option value="Ne Standart Alucobond">Ne Standart Alucobond</option>
            <option value="ROYAL 33 (21mk) (1.22*2.44mm)">ROYAL 33 (21mk) (1.22*2.44mm)</option>
            <option value="ROYAL CH (25mk)">ROYAL CH (25mk)</option>
            <option value="ROYAL TR (25mk)">ROYAL TR (25mk)</option>
            <option value="IBOARD CH (21mk)">IBOARD CH (21mk)</option>
            <option value="IB_Nestandart (Kg)">IB_Nestandart (Kg)</option>
        </select>
        </div>
    </td>
    <td >
        <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='tip`+String(i)+`'>ГП</span>
        
    </td>
    <td >
            <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='segment`+String(i)+`'>Пустой</span>
        
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 520px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;" id='buxgalter_tovar`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option value='Профиль из ПВХ ламинированный'>Профиль из ПВХ ламинированный</option>
            <option value='Otvetka 153 (oq)'>Otvetka 153 (oq)</option>
            <option value='Ламбри из ПВХ'>Ламбри из ПВХ</option>
            <option value='Soedinitel OP.40.J05 L=10mm'>Soedinitel OP.40.J05 L=10mm</option>
            <option value='Soedinitel CL.X.W 14 (5mm)'>Soedinitel CL.X.W 14 (5mm)</option>
            <option value='BKT 78 Soed. (M11427-15.8mm)'>BKT 78 Soed. (M11427-15.8mm)</option>
            <option value='Soedinitel CL.X.W 14 (38mm)'>Soedinitel CL.X.W 14 (38mm)</option>
            <option value='BKT 70 Soed. W 02 (1=7.8)'>BKT 70 Soed. W 02 (1=7.8)</option>
            <option value='Otvetka 155 (rangli)'>Otvetka 155 (rangli)</option>
            <option value='Ruchka Dvernaya Fornaks (28mm) (rangli)'>Ruchka Dvernaya Fornaks (28mm) (rangli)</option>
            <option value='Petlya Dvernaya 2SK MASTER (rangli)'>Petlya Dvernaya 2SK MASTER (rangli)</option>
            <option value='Petlya (rangli)'>Petlya (rangli)</option>
            <option value='Soedinitel Chovush'>Soedinitel Chovush</option>
            <option value='Soedinitel (Bolshoy) CHEMPION'>Soedinitel (Bolshoy) CHEMPION</option>
            <option value='Petlya Dvernaya Chempion (rangli)'>Petlya Dvernaya Chempion (rangli)</option>
            <option value='Soedinitel (Bolshoy) (ALD-2)'>Soedinitel (Bolshoy) (ALD-2)</option>
            <option value='Krishka Podokonnik (ALYUMIN) (oq)'>Krishka Podokonnik (ALYUMIN) (oq)</option>
            <option value='Soedinitel Universal'>Soedinitel Universal</option>
            <option value='Ogranichitel (rangli)'>Ogranichitel (rangli)</option>
            <option value='Otvetka Mini 153 (rangli)'>Otvetka Mini 153 (rangli)</option>
            <option value='Ruchka Elegant (rangli)'>Ruchka Elegant (rangli)</option>
            <option value='Ruchka LUX Fortuna O (rangli)'>Ruchka LUX Fortuna O (rangli)</option>
            <option value='Petlya 100 mm (rangli)'>Petlya 100 mm (rangli)</option>
            <option value='Ruchka dvernaya "BELLA" (700) mm (rangli)'>Ruchka dvernaya "BELLA" (700) mm (rangli)</option>
            <option value='Soedinitel CL.X.W 34 (43mm)'>Soedinitel CL.X.W 34 (43mm)</option>
            <option value='Ruchka dvernaya "BELLA" (500) mm (oq)'>Ruchka dvernaya "BELLA" (500) mm (oq)</option>
            <option value='Ruchka dvernaya "BELLA" (600) mm (rangli)'>Ruchka dvernaya "BELLA" (600) mm (rangli)</option>
            <option value='Ruchka LUX Fortuna O (oq)'>Ruchka LUX Fortuna O (oq)</option>
            <option value='Otvetka Mini 155 (oq)'>Otvetka Mini 155 (oq)</option>
            <option value='Soedinitel CL.X.W 10 (25.8mm)'>Soedinitel CL.X.W 10 (25.8mm)</option>
            <option value='Termo soedinitel 19 mm'>Termo soedinitel 19 mm</option>
            <option value='Petlya 100 mm (oq)'>Petlya 100 mm (oq)</option>
            <option value='Petlya (ALD-2) (oq)'>Petlya (ALD-2) (oq)</option>
            <option value='Otvetnaya chast zamka A0275-K (155) (rangli)'>Otvetnaya chast zamka A0275-K (155) (rangli)</option>
            <option value='Petlya (ALD-2) (rangli)'>Petlya (ALD-2) (rangli)</option>
            <option value='Petlya Dvernaya 3SK MASTER (rangli)'>Petlya Dvernaya 3SK MASTER (rangli)</option>
            <option value='Petlya Dvernaya Alyumin (rangli)'>Petlya Dvernaya Alyumin (rangli)</option>
            <option value='Ruchka Kvadrat (rangli)'>Ruchka Kvadrat (rangli)</option>
            <option value='Chit-Chit PVH.uz (rangli)'>Chit-Chit PVH.uz (rangli)</option>
            <option value='Otvetka 153 (rangli)'>Otvetka 153 (rangli)</option>
            <option value='Ruchka LUX Fortuna Mini O (rangli)'>Ruchka LUX Fortuna Mini O (rangli)</option>
            <option value='Zashyolka Narujnyaya (rangli)'>Zashyolka Narujnyaya (rangli)</option>
            <option value='Shpingalet (rangli)'>Shpingalet (rangli)</option>
            <option value='Ruchka DELFIN (rangli)'>Ruchka DELFIN (rangli)</option>
            <option value='Otvetka Mini 155 (rangli)'>Otvetka Mini 155 (rangli)</option>
            <option value='Otvetnaya chast zamka A0275-K (153) (rangli)'>Otvetnaya chast zamka A0275-K (153) (rangli)</option>
            <option value='BKT 70 Soed. Impost (J01-52.5mm)'>BKT 70 Soed. Impost (J01-52.5mm)</option>
            <option value='BKT 70 Soed. Impost (J01-66.5mm)'>BKT 70 Soed. Impost (J01-66.5mm)</option>
            <option value='BKT 70 Soed. Impost (J02-13.6mm)'>BKT 70 Soed. Impost (J02-13.6mm)</option>
            <option value='BKT 70 Soed. Impost (J02-43.6mm)'>BKT 70 Soed. Impost (J02-43.6mm)</option>
            <option value='BKT 70 Soed. Impost (J03-66.6mm)'>BKT 70 Soed. Impost (J03-66.6mm)</option>
            <option value='BKT 70 Soed. Impost (J06-43.6mm)'>BKT 70 Soed. Impost (J06-43.6mm)</option>
            <option value='BKT 70 Soed. Impost (J06-66.5mm)'>BKT 70 Soed. Impost (J06-66.5mm)</option>
            <option value='BKT 70 Soed. W 01 (1=21.7)'>BKT 70 Soed. W 01 (1=21.7)</option>
            <option value='BKT 70 Soed. W 01 (1=5.1)'>BKT 70 Soed. W 01 (1=5.1)</option>
            <option value='BKT 70 Soed. W 01 (1=8.5)'>BKT 70 Soed. W 01 (1=8.5)</option>
            <option value='Krishka Podokonnik (ALYUMIN) (rangli)'>Krishka Podokonnik (ALYUMIN) (rangli)</option>
            <option value='Kreplenie moskitnoy setki (rangli)'>Kreplenie moskitnoy setki (rangli)</option>
            <option value='BKT 70 Soed. W 01 (1=8)'>BKT 70 Soed. W 01 (1=8)</option>
            <option value='BKT 78 Soed. (M11427-19.5mm)'>BKT 78 Soed. (M11427-19.5mm)</option>
            <option value='Kreplenie moskitnoy setki (oq)'>Kreplenie moskitnoy setki (oq)</option>
            <option value='BKT 78 Soed. (M11427-27mm)'>BKT 78 Soed. (M11427-27mm)</option>
            <option value='Ruchka LUX Pol (oq)'>Ruchka LUX Pol (oq)</option>
            <option value='Ruchka Sos. VENTURO (oq)'>Ruchka Sos. VENTURO (oq)</option>
            <option value='Montajnaya Planka 5200 (Metal)'>Montajnaya Planka 5200 (Metal)</option>
            <option value='Ламинированный термоуплотненный алюминиевый профиль'>Ламинированный термоуплотненный алюминиевый профиль</option>
            <option value='Термоуплотненный анодированный алюминиевый профиль (N)'>Термоуплотненный анодированный алюминиевый профиль (N)</option>
            <option value='Профиль из ПВХ с уплотнителем'>Профиль из ПВХ с уплотнителем</option>
            <option value='Алюминиевый профиль с декоративным покрытием'>Алюминиевый профиль с декоративным покрытием</option>
            <option value='Подоконник из ПВХ'>Подоконник из ПВХ</option>
            <option value='Дистанционная рамка'>Дистанционная рамка</option>
            <option value='Профиль из ПВХ ламинированный (Engelberg)'>Профиль из ПВХ ламинированный (Engelberg)</option>
            <option value='Профиль из ПВХ ламинированный с уплотнителем'>Профиль из ПВХ ламинированный с уплотнителем</option>
            <option value='Ламинированный алюминиевый профиль'>Ламинированный алюминиевый профиль</option>
            <option value='Неокрашенный алюминиевый профиль'>Неокрашенный алюминиевый профиль</option>
            <option value='Подоконник из ПВХ ламинированный'>Подоконник из ПВХ ламинированный</option>
            <option value='Уплотнитель для алюминиевых и ПВХ профилей'>Уплотнитель для алюминиевых и ПВХ профилей</option>
            <option value='Профиль из ПВХ'>Профиль из ПВХ</option>
            <option value='Алюминиевый профиль'>Алюминиевый профиль</option>
            <option value='Ламинированный термоуплотненный алюминиевый профиль (N)'>Ламинированный термоуплотненный алюминиевый профиль (N)</option>
            <option value='Металлический усилитель'>Металлический усилитель</option>
            <option value='Ламбри из ПВХ ламинированный'>Ламбри из ПВХ ламинированный</option>
            <option value='Профиль из ПВХ (Engelberg)'>Профиль из ПВХ (Engelberg)</option>
            <option value='Ламинированный алюминиевый профиль (N)'>Ламинированный алюминиевый профиль (N)</option>
            <option value='Алюминиевый профиль с декоративным покрытием (N)'>Алюминиевый профиль с декоративным покрытием (N)</option>
            <option value='Chit-Chit PVH.uz (oq)'>Chit-Chit PVH.uz (oq)</option>
            <option value='BKT 70 Soed. (M11148-13.6mm)'>BKT 70 Soed. (M11148-13.6mm)</option>
            <option value='Ruchka D (oq)'>Ruchka D (oq)</option>
            <option value='Ruchka Kvadrat Mini (oq)'>Ruchka Kvadrat Mini (oq)</option>
            <option value='Ruchka LUX (oq)'>Ruchka LUX (oq)</option>
            <option value='Soedinitel 114 D 400 (13mm)'>Soedinitel 114 D 400 (13mm)</option>
            <option value='Soedinitel 114 D 400 (52mm)'>Soedinitel 114 D 400 (52mm)</option>
            <option value='Petlya Dvernaya Chempion (oq)'>Petlya Dvernaya Chempion (oq)</option>
            <option value='Soedinitel BKH-001 (38mm)'>Soedinitel BKH-001 (38mm)</option>
            <option value='Soedinitel 5507 (6,5mm)'>Soedinitel 5507 (6,5mm)</option>
            <option value='Soedinitel BKH-001 (16mm)'>Soedinitel BKH-001 (16mm)</option>
            <option value='Soedinitel BKH-001 (5mm)'>Soedinitel BKH-001 (5mm)</option>
            <option value='Soedinitel AKF-107 (40mm)'>Soedinitel AKF-107 (40mm)</option>
            <option value='Soedinitel AKF-106 (37.5mm)'>Soedinitel AKF-106 (37.5mm)</option>
            <option value='Vstavka Dlya Zamka (rangli)'>Vstavka Dlya Zamka (rangli)</option>
            <option value='Soedinitel JP2186 (60mm)'>Soedinitel JP2186 (60mm)</option>
            <option value='T 6 Soed. (ST 10 255) C 9.5 Qanot Mal.'>T 6 Soed. (ST 10 255) C 9.5 Qanot Mal.</option>
            <option value='T 6 Soed. (ST 10 366) C 29.0 Qanot Bol.'>T 6 Soed. (ST 10 366) C 29.0 Qanot Bol.</option>
            <option value='T 6 Soed. (ST 10 366) P 27.5 Kosa Bol.'>T 6 Soed. (ST 10 366) P 27.5 Kosa Bol.</option>
            <option value='T 6 Soed. (ST 10 366) P 9.2 Kosa Mal.'>T 6 Soed. (ST 10 366) P 9.2 Kosa Mal.</option>
            <option value='T 6 Soed. (ST 10 565) B 26.0 Balkon Qanot Bol.'>T 6 Soed. (ST 10 565) B 26.0 Balkon Qanot Bol.</option>
            <option value='T 6 Soed. (ST 10 565) B 5.1 Balkon Qanot Mal.'>T 6 Soed. (ST 10 565) B 5.1 Balkon Qanot Mal.</option>
            <option value='Soedinitel AKF-107 (43.5mm)'>Soedinitel AKF-107 (43.5mm)</option>
            <option value='Vstavka Dlya Zamka (oq)'>Vstavka Dlya Zamka (oq)</option>
            <option value='Soedinitel 5505 (45mm)'>Soedinitel 5505 (45mm)</option>
            <option value='Zashyolka Narujnyaya (oq)'>Zashyolka Narujnyaya (oq)</option>
            <option value='Zashyolka Narujnyaya Mini (oq)'>Zashyolka Narujnyaya Mini (oq)</option>
            <option value='Ruchka Dvernaya Fornaks (35mm) (rangli)'>Ruchka Dvernaya Fornaks (35mm) (rangli)</option>
            <option value='Krishka Podokonnik 300 (rangli)'>Krishka Podokonnik 300 (rangli)</option>
            <option value='Ogranichitel PVH (rangli)'>Ogranichitel PVH (rangli)</option>
            <option value='Petlya Dvernaya 3D (rangli)'>Petlya Dvernaya 3D (rangli)</option>
            <option value='Petlya Dvernaya 3D (oq)'>Petlya Dvernaya 3D (oq)</option>
            <option value='Porog Soedinitel 7000 (1kom.) (L;P) (rangli)'>Porog Soedinitel 7000 (1kom.) (L;P) (rangli)</option>
            <option value='Petlya 100 mm (oq)'>Petlya 100 mm (oq)</option>
            <option value='Krishka Shtulp Dlya Adap 7000 (oq)'>Krishka Shtulp Dlya Adap 7000 (oq)</option>
            <option value='Krishka Shtulp Dlya Adap dvernaya 6000 (13 AKS) (rangli)'>Krishka Shtulp Dlya Adap dvernaya 6000 (13 AKS) (rangli)</option>
            <option value='Ruchka Dvernaya Fornaks (28mm) fiksator (rangli)'>Ruchka Dvernaya Fornaks (28mm) fiksator (rangli)</option>
            <option value='Ruchka Dvernaya Fornaks (35mm) fiksator (rangli)'>Ruchka Dvernaya Fornaks (35mm) fiksator (rangli)</option>
            <option value='Chit-Chit (aldocks).uz (rangli)'>Chit-Chit (aldocks).uz (rangli)</option>
            <option value='Ruchka Okonaya Roto (rangli)'>Ruchka Okonaya Roto (rangli)</option>
            <option value='Petlya 75 mm (rangli)'>Petlya 75 mm (rangli)</option>
            <option value='Soedinitel AKF-106 (36.5mm)'>Soedinitel AKF-106 (36.5mm)</option>
            <option value='Soedinitel 114 D 300 (13,2 mm)'>Soedinitel 114 D 300 (13,2 mm)</option>
            <option value='Soedinitel JP2002 (40mm)'>Soedinitel JP2002 (40mm)</option>
            <option value='Ruchka Kvadrat Mini (rangli)'>Ruchka Kvadrat Mini (rangli)</option>
            <option value='Shpingalet (oq)'>Shpingalet (oq)</option>
            <option value='Krishka Shtulp Dlya Adap dvernaya 6000 (13 AKS) (oq)'>Krishka Shtulp Dlya Adap dvernaya 6000 (13 AKS) (oq)</option>
            <option value='Krishka Shtulp Dlya Adap 7000 (rangli)'>Krishka Shtulp Dlya Adap 7000 (rangli)</option>
            <option value='(A0286) Petlya (Chempion) (rangli)'>(A0286) Petlya (Chempion) (rangli)</option>
            <option value='Otvetka 155 (oq)'>Otvetka 155 (oq)</option>
            <option value='(A0286) Petlya (Chempion) (oq)'>(A0286) Petlya (Chempion) (oq)</option>
            <option value='BKT 70 Soed. Impost (J01-66.6mm)'>BKT 70 Soed. Impost (J01-66.6mm)</option>
            <option value='Petlya Dvernaya MDF (oq)'>Petlya Dvernaya MDF (oq)</option>
            <option value='Petlya Dvernaya MDF (rangli)'>Petlya Dvernaya MDF (rangli)</option>
            <option value='Petlya Dvernaya PVH (rangli)'>Petlya Dvernaya PVH (rangli)</option>
            <option value='Soedinitel A 00018 (21mm)'>Soedinitel A 00018 (21mm)</option>
            <option value='Soedinitel CL.X.W 14 (18mm)'>Soedinitel CL.X.W 14 (18mm)</option>
            <option value='Soedinitel CL.X.W 14 (8mm)'>Soedinitel CL.X.W 14 (8mm)</option>
            <option value='Soedinitel CL.X.W 14 (9mm)'>Soedinitel CL.X.W 14 (9mm)</option>
            <option value='Soedinitel WDT 67 J 02 (44mm)'>Soedinitel WDT 67 J 02 (44mm)</option>
            <option value='Soedinitel CL.X.W 34 (25.6mm)'>Soedinitel CL.X.W 34 (25.6mm)</option>
            <option value='Soedinitel CL.X.W 14 (12.5mm)'>Soedinitel CL.X.W 14 (12.5mm)</option>
            <option value='Petlya Dvernaya 3SK MASTER (rangli)'>Petlya Dvernaya 3SK MASTER (rangli)</option>
            <option value='Klipsa 13mm JP'>Klipsa 13mm JP</option>
            <option value='Zaglushka (PVCC 031) (rangli)'>Zaglushka (PVCC 031) (rangli)</option>
            <option value='Zaglushka (PVCC 032) (rangli)'>Zaglushka (PVCC 032) (rangli)</option>
            <option value='Soedinitel CL.X.W 20 (25.8mm)'>Soedinitel CL.X.W 20 (25.8mm)</option>
            <option value='Krishka Podokonnik 350 (Ovolniy) (rangli)'>Krishka Podokonnik 350 (Ovolniy) (rangli)</option>
            <option value='Soedinitel CL.X.W 34 (17,7mm)'>Soedinitel CL.X.W 34 (17,7mm)</option>
            <option value='Soedinitel CL.X.W 34 (10mm)'>Soedinitel CL.X.W 34 (10mm)</option>
            <option value='Ruchka dvernaya "BELLA" (1000) mm (rangli)'>Ruchka dvernaya "BELLA" (1000) mm (rangli)</option>
            <option value='Petlya dvernaya Jocker (rangli)'>Petlya dvernaya Jocker (rangli)</option>
            <option value='Soedinitel CL.X.W 34 (6mm)'>Soedinitel CL.X.W 34 (6mm)</option>
            <option value='Soedinitel CL.X.W 10 (5mm)'>Soedinitel CL.X.W 10 (5mm)</option>
            <option value='Soedinitel CL.X.W 34 (18mm)'>Soedinitel CL.X.W 34 (18mm)</option>
            <option value='Soedinitel CL.X.W 34 (15,8mm)'>Soedinitel CL.X.W 34 (15,8mm)</option>
            <option value='Soedinitel A 00018 (25 mm)'>Soedinitel A 00018 (25 mm)</option>
            <option value='Petlya dvernaya Jocker (oq)'>Petlya dvernaya Jocker (oq)</option>
            <option value='Ruchka Dvernaya mini (rangli)'>Ruchka Dvernaya mini (rangli)</option>
            <option value='Ruchka Dvernaya Fornaks (30mm) (rangli)'>Ruchka Dvernaya Fornaks (30mm) (rangli)</option>
            <option value='Soedinitel WDT 67 J 03 (44mm)'>Soedinitel WDT 67 J 03 (44mm)</option>
            <option value='Soedinitel 114 D 300 (10mm)'>Soedinitel 114 D 300 (10mm)</option>
            <option value='Soedinitel 114 D 400 (14mm)'>Soedinitel 114 D 400 (14mm)</option>
            <option value='Soedinitel CL.X.W 10 (14mm)'>Soedinitel CL.X.W 10 (14mm)</option>
            <option value='Krishka Podokonnik 300 (Trapetsiya) (rangli)'>Krishka Podokonnik 300 (Trapetsiya) (rangli)</option>
            <option value='Soedinitel 148х125хх (60mm)'>Soedinitel 148х125хх (60mm)</option>
            <option value='Soedinitel CL.X.W 16 (10.8mm)'>Soedinitel CL.X.W 16 (10.8mm)</option>
            <option value='Soedinitel FST 50 JR 001 (30mm)'>Soedinitel FST 50 JR 001 (30mm)</option>
            <option value='Soedinitel FST 50 G 003 (100 mm)'>Soedinitel FST 50 G 003 (100 mm)</option>
            <option value='Soedinitel CL.X.W 40 (7.4mm)'>Soedinitel CL.X.W 40 (7.4mm)</option>
            <option value='Soedinitel 8000'>Soedinitel 8000</option>
            <option value='Soedinitel CL.X.W 20 (20,7mm)'>Soedinitel CL.X.W 20 (20,7mm)</option>
            <option value='Soedinitel CL.X.W 20 (20,6mm)'>Soedinitel CL.X.W 20 (20,6mm)</option>
            <option value='Soedinitel OP.40.J04 L=10mm'>Soedinitel OP.40.J04 L=10mm</option>
            <option value='Soedinitel CL.X.W 34 (7,4mm)'>Soedinitel CL.X.W 34 (7,4mm)</option>
            <option value='Ruchka dvernaya "BELLA" (800) mm (rangli)'>Ruchka dvernaya "BELLA" (800) mm (rangli)</option>
            <option value='Soedinitel CL.X.W 40 (5mm)'>Soedinitel CL.X.W 40 (5mm)</option>
            <option value='Ruchka dvernaya "BELLA" (2000) mm (oq)'>Ruchka dvernaya "BELLA" (2000) mm (oq)</option>
            <option value='Ruchka Dvernaya (28mm) Slim fiksator (rangli)'>Ruchka Dvernaya (28mm) Slim fiksator (rangli)</option>
            <option value='Soedinitel CL.X.W 40 (19mm)'>Soedinitel CL.X.W 40 (19mm)</option>
            <option value='Ruchka dvernaya "BELLA" (1800) mm (rangli)'>Ruchka dvernaya "BELLA" (1800) mm (rangli)</option>
            <option value='Soedinitel CLSW 16'>Soedinitel CLSW 16</option>
            <option value='Soedinitel CL.X.W 40 (18.9mm)'>Soedinitel CL.X.W 40 (18.9mm)</option>
            <option value='Soedinitel 148х125хх (90mm)'>Soedinitel 148х125хх (90mm)</option>
            <option value='BKT 70 Soed. List (A10-001)'>BKT 70 Soed. List (A10-001)</option>
            <option value='Soedinitel CL.X.W 40 (19.6mm)'>Soedinitel CL.X.W 40 (19.6mm)</option>
            <option value='Soedinitel AKF-106 (44mm)'>Soedinitel AKF-106 (44mm)</option>
            <option value='Soedinitel AKF-107 (37mm)'>Soedinitel AKF-107 (37mm)</option>
            <option value='Soedinitel 7000 ECO'>Soedinitel 7000 ECO</option>
            <option value='Ruchka dvernaya "Comfort" (oq)'>Ruchka dvernaya "Comfort" (oq)</option>
            <option value='Soedinitel 148х125хх (140mm)'>Soedinitel 148х125хх (140mm)</option>
            <option value='Soedinitel BKH-010 (38mm)'>Soedinitel BKH-010 (38mm)</option>
            <option value='Ruchka Dvernaya (28mm) Slim (rangli)'>Ruchka Dvernaya (28mm) Slim (rangli)</option>
            <option value='Ruchka dvernaya "Comfort" (rangli)'>Ruchka dvernaya "Comfort" (rangli)</option>
            <option value='Soedinitel BKH-010 (56mm)'>Soedinitel BKH-010 (56mm)</option>
            <option value='Soedinitel CLSW 12'>Soedinitel CLSW 12</option>
            <option value='Ruchka dvernaya "BELLA" (1500) mm (rangli)'>Ruchka dvernaya "BELLA" (1500) mm (rangli)</option>
            <option value='Soedinitel FST 50 G 004 (100 mm)'>Soedinitel FST 50 G 004 (100 mm)</option>
            <option value='Ruchka Okonnaya PVH (rangli)'>Ruchka Okonnaya PVH (rangli)</option>
            <option value='Soedinitel 110049 (20mm)'>Soedinitel 110049 (20mm)</option>
            <option value='Soedinitel 110048 (20mm)'>Soedinitel 110048 (20mm)</option>
            <option value='Soedinitel CL.X.W 38 (28.7mm)'>Soedinitel CL.X.W 38 (28.7mm)</option>
            <option value='Soedinitel FST 50 JR 001 (33mm)'>Soedinitel FST 50 JR 001 (33mm)</option>
            <option value='Soedinitel FST 50 JR 001 (97,5mm)'>Soedinitel FST 50 JR 001 (97,5mm)</option>
            <option value='Ruchka Dvernaya (28mm) Slim (oq)'>Ruchka Dvernaya (28mm) Slim (oq)</option>
            <option value='Zaglushka (PVCC 033) (rangli)'>Zaglushka (PVCC 033) (rangli)</option>
            <option value='Zaglushka (PVCC 036) (rangli)'>Zaglushka (PVCC 036) (rangli)</option>
            <option value='Soedinitel moskitnoy setki (rangli)'>Soedinitel moskitnoy setki (rangli)</option>
            <option value='Ruchka dvernaya "BELLA" (700) mm (oq)'>Ruchka dvernaya "BELLA" (700) mm (oq)</option>
            <option value='Soedinitel CL.X.W 14 (43.5mm)'>Soedinitel CL.X.W 14 (43.5mm)</option>
            <option value='Soedinitel A 00018 (44mm)'>Soedinitel A 00018 (44mm)</option>
            <option value='Ruchka Elegant (oq)'>Ruchka Elegant (oq)</option>
            <option value='Krishka Shtulp Dlya Adap 6000 (rangli)'>Krishka Shtulp Dlya Adap 6000 (rangli)</option>
            <option value='Ruchka Dvernaya Fornaks (30mm) fiksator (rangli)'>Ruchka Dvernaya Fornaks (30mm) fiksator (rangli)</option>
            <option value='Krishka Shtulp Dlya Adap 8000 (rangli)'>Krishka Shtulp Dlya Adap 8000 (rangli)</option>
            <option value='Soedinitel CL.X.W 20 (25.6mm)'>Soedinitel CL.X.W 20 (25.6mm)</option>
            <option value='BKT 70 Soed. W 01 (1=5)'>BKT 70 Soed. W 01 (1=5)</option>
            <option value='Soedinitel moskitnoy setki (oq)'>Soedinitel moskitnoy setki (oq)</option>
            <option value='Замок для профиля москитной сетки серии 10х20цветной'>Замок для профиля москитной сетки серии 10х20цветной</option>
            <option value='Замок для профиля москитной сетки серии 10х20'>Замок для профиля москитной сетки серии 10х20</option>
            <option value='Soedinitel CLSW 0243'>Soedinitel CLSW 0243</option>
            <option value='Klipsa 10.5 mm'>Klipsa 10.5 mm</option>
            <option value='BKT 70 Soed. Impost (J01-26.3mm)'>BKT 70 Soed. Impost (J01-26.3mm)</option>
            <option value='BKT 70 Soed. Impost (J02-23.6mm)'>BKT 70 Soed. Impost (J02-23.6mm)</option>
            <option value='BKT 70 Soed. Impost (J06-13.6mm)'>BKT 70 Soed. Impost (J06-13.6mm)</option>
            <option value='BKT 70 Soed. Impost (J06-23.6mm)'>BKT 70 Soed. Impost (J06-23.6mm)</option>
            <option value='BKT 70 Soed. W 01 (1=18.4)'>BKT 70 Soed. W 01 (1=18.4)</option>
            <option value='BKT 70 Soed. W 01 (1=26.3)'>BKT 70 Soed. W 01 (1=26.3)</option>
            <option value='BKT 70 Soed. W 01 (1=26.8)'>BKT 70 Soed. W 01 (1=26.8)</option>
            <option value='BKT 70 Soed. W 01 (1=7.8)'>BKT 70 Soed. W 01 (1=7.8)</option>
            <option value='BKT 78 Soed. (M11227-19.5mm)'>BKT 78 Soed. (M11227-19.5mm)</option>
            <option value='BKT 70 Soed. W 01 (1=10.8)'>BKT 70 Soed. W 01 (1=10.8)</option>
            <option value='BKT 70 Soed. W 02 (1=10.8)'>BKT 70 Soed. W 02 (1=10.8)</option>
            <option value='BKT 70 Soed. W 02 (1=23.6)'>BKT 70 Soed. W 02 (1=23.6)</option>
            <option value='BKT 70 Soed. W 03 (1=7.8)'>BKT 70 Soed. W 03 (1=7.8)</option>
            <option value='BKT 70 Soed. W 03 (1=10.8)'>BKT 70 Soed. W 03 (1=10.8)</option>
            <option value='BKT 70 Soed. (M11535-7.8mm)'>BKT 70 Soed. (M11535-7.8mm)</option>
            <option value='BKT 70 Soed. Impost (J01-13.6mm)'>BKT 70 Soed. Impost (J01-13.6mm)</option>
            <option value='BKT 70 Soed. W 02 (1=18.4)'>BKT 70 Soed. W 02 (1=18.4)</option>
            <option value='BKT 70 Soed. (M11055-13.6mm)'>BKT 70 Soed. (M11055-13.6mm)</option>
            <option value='BKT 70 Soed. Impost (J01-43.6mm)'>BKT 70 Soed. Impost (J01-43.6mm)</option>
            <option value='BKT 70 Soed. Impost (J05-43.6mm)'>BKT 70 Soed. Impost (J05-43.6mm)</option>
            <option value='BKT 78 Soed. (M11227-22.7mm)'>BKT 78 Soed. (M11227-22.7mm)</option>
            <option value='Chit-Chit (aldocks).uz (oq)'>Chit-Chit (aldocks).uz (oq)</option>
            <option value='Klipsa 12 mm'>Klipsa 12 mm</option>
            <option value='BKT 70 Soed. Impost (J05-23.6mm)'>BKT 70 Soed. Impost (J05-23.6mm)</option>
            <option value='Ogranichitel (oq)'>Ogranichitel (oq)</option>
            <option value='Otvetniy Plast. (rangli)'>Otvetniy Plast. (rangli)</option>
            <option value='Otvetniy Plast. (oq)'>Otvetniy Plast. (oq)</option>
            <option value='Petlya Dvernaya Alyumin (oq)'>Petlya Dvernaya Alyumin (oq)</option>
            <option value='Ruchka Kvadrat (oq)'>Ruchka Kvadrat (oq)</option>
            <option value='Soedinitel 114 D 300 (13mm)'>Soedinitel 114 D 300 (13mm)</option>
            <option value='Soedinitel 114 D 300 (6mm)'>Soedinitel 114 D 300 (6mm)</option>
            <option value='Soedinitel 114 D 400 (38mm)'>Soedinitel 114 D 400 (38mm)</option>
            <option value='Soedinitel 114 D 400 (46mm)'>Soedinitel 114 D 400 (46mm)</option>
            <option value='Soedinitel BKH-001 (6mm)'>Soedinitel BKH-001 (6mm)</option>
            <option value='Soedinitel BKH-002 (38mm)'>Soedinitel BKH-002 (38mm)</option>
            <option value='Soedinitel (Inja)'>Soedinitel (Inja)</option>
            <option value='Zashyolka Narujnyaya (new) (oq)'>Zashyolka Narujnyaya (new) (oq)</option>
            <option value='Soedinitel (Bolshoy)'>Soedinitel (Bolshoy)</option>
            <option value='Otvetniy Plast. (ALD-2) (rangli)'>Otvetniy Plast. (ALD-2) (rangli)</option>
            <option value='Otvetniy Plast. (ALD-2) (oq)'>Otvetniy Plast. (ALD-2) (oq)</option>
            <option value='BKT 70 Soed. List (A10-002)'>BKT 70 Soed. List (A10-002)</option>
            <option value='Montajnaya Planka 7000 (Metal)'>Montajnaya Planka 7000 (Metal)</option>
            <option value='Petlya (oq)'>Petlya (oq)</option>
            <option value='BKT 78 Soed. (M11227-26.9mm)'>BKT 78 Soed. (M11227-26.9mm)</option>
            <option value='Ruchka LUX Fortuna Mini O (oq)'>Ruchka LUX Fortuna Mini O (oq)</option>
            <option value='BKT 70 Soed. List (A10-003)'>BKT 70 Soed. List (A10-003)</option>
            <option value='Otvetnaya chast zamka A0275-K (155) (oq)'>Otvetnaya chast zamka A0275-K (155) (oq)</option>
            <option value='Soedinitel 114 D 400 (10mm)'>Soedinitel 114 D 400 (10mm)</option>
            <option value='Soedinitel 5505 (35mm)'>Soedinitel 5505 (35mm)</option>
            <option value='Soedinitel BKH-008 (14mm)'>Soedinitel BKH-008 (14mm)</option>
            <option value='Soedinitel BKH-008 (15mm)'>Soedinitel BKH-008 (15mm)</option>
            <option value='Soedinitel BKH-010 (6mm)'>Soedinitel BKH-010 (6mm)</option>
            <option value='Krishka Podokonnik 300 (Trapetsiya) (oq)'>Krishka Podokonnik 300 (Trapetsiya) (oq)</option>
            <option value='Ogranichitel PVH (oq)'>Ogranichitel PVH (oq)</option>
            <option value='Petlya 75 mm (oq)'>Petlya 75 mm (oq)</option>
            <option value='Petlya Dvernaya PVH (oq)'>Petlya Dvernaya PVH (oq)</option>
            <option value='Porog Soedinitel 6000 (1kom.) (L;P) (rangli)'>Porog Soedinitel 6000 (1kom.) (L;P) (rangli)</option>
            <option value='Porog Soedinitel 7000 (1kom.) (L;P) (oq)'>Porog Soedinitel 7000 (1kom.) (L;P) (oq)</option>
            <option value='Krishka Shtulp Dlya Adap 6000 (oq)'>Krishka Shtulp Dlya Adap 6000 (oq)</option>
            <option value='Krishka Podokonnik 300 (oq)'>Krishka Podokonnik 300 (oq)</option>
            <option value='Ruchka Dvernaya Fornaks (35mm) fiksator (oq)'>Ruchka Dvernaya Fornaks (35mm) fiksator (oq)</option>
            <option value='BKT 70 Soed. (M11535-22mm)'>BKT 70 Soed. (M11535-22mm)</option>
            <option value='Ruchka DELFIN (oq)'>Ruchka DELFIN (oq)</option>
            <option value='Zatsepka 5200'>Zatsepka 5200</option>
            <option value='Zatsepka 7000'>Zatsepka 7000</option>
            <option value='Zatsepka 6000'>Zatsepka 6000</option>
            <option value='Ruchka Okonaya Roto (oq)'>Ruchka Okonaya Roto (oq)</option>
            <option value='Ruchka Okonnaya PVH (oq)'>Ruchka Okonnaya PVH (oq)</option>
            <option value='Soedinitel 5200'>Soedinitel 5200</option>
            <option value='Soedinitel 6000 (TRIO)'>Soedinitel 6000 (TRIO)</option>
            <option value='Soedinitel 7000'>Soedinitel 7000</option>
            <option value='Ruchka Dvernaya Fornaks (35mm) (oq)'>Ruchka Dvernaya Fornaks (35mm) (oq)</option>
            <option value='Soedinitel 5800'>Soedinitel 5800</option>
            <option value='Soedinitel CL.X.W 38 (5.5 mm)'>Soedinitel CL.X.W 38 (5.5 mm)</option>
            <option value='Petlya Dvernaya 2SK MASTER (oq)'>Petlya Dvernaya 2SK MASTER (oq)</option>
            <option value='Soedinitel A 00018 (37mm)'>Soedinitel A 00018 (37mm)</option>
            <option value='Soedinitel CL.X.W 14 (40mm)'>Soedinitel CL.X.W 14 (40mm)</option>
            <option value='Ruchka Okonaya Rotto Swing (oq)'>Ruchka Okonaya Rotto Swing (oq)</option>
            <option value='BKT 70 Soed. Impost (J03-23.6mm)'>BKT 70 Soed. Impost (J03-23.6mm)</option>
            <option value='Ruchka Okonaya Rotto Swing (rangli)'>Ruchka Okonaya Rotto Swing (rangli)</option>
            <option value='Soedinitel CL.X.W 10 (27mm)'>Soedinitel CL.X.W 10 (27mm)</option>
            <option value='Soedinitel A 00018 (9mm)'>Soedinitel A 00018 (9mm)</option>
            <option value='Soedinitel A 00018 (25.8mm)'>Soedinitel A 00018 (25.8mm)</option>
            <option value='Soedinitel A 00018 (18mm)'>Soedinitel A 00018 (18mm)</option>
            <option value='Soedinitel CL.X.W 38 (5mm)'>Soedinitel CL.X.W 38 (5mm)</option>
            <option value='Soedinitel CL.X.W 28 (9mm)'>Soedinitel CL.X.W 28 (9mm)</option>
            <option value='Soedinitel CL.X.W 28 (25.8mm)'>Soedinitel CL.X.W 28 (25.8mm)</option>
            <option value='Soedinitel CL.X.W 28 (18mm)'>Soedinitel CL.X.W 28 (18mm)</option>
            <option value='Soedinitel CL.X.W 24 (5mm)'>Soedinitel CL.X.W 24 (5mm)</option>
            <option value='Soedinitel CL.X.W 38 (5.8mm)'>Soedinitel CL.X.W 38 (5.8mm)</option>
            <option value='Soedinitel CL.X.W 38 (6.8mm)'>Soedinitel CL.X.W 38 (6.8mm)</option>
            <option value='Soedinitel CL.X.W 14 (22.5mm)'>Soedinitel CL.X.W 14 (22.5mm)</option>
            <option value='Soedinitel CL.X.W 34 (34.3mm)'>Soedinitel CL.X.W 34 (34.3mm)</option>
            <option value='BKT 70 Soed. Impost (J01-16mm)'>BKT 70 Soed. Impost (J01-16mm)</option>
            <option value='Soedinitel CL.X.W 05 (13mm)'>Soedinitel CL.X.W 05 (13mm)</option>
            <option value='Soedinitel CL.X.W 20 (27mm)'>Soedinitel CL.X.W 20 (27mm)</option>
            <option value='Soedinitel CL.X.W 20 (18,8mm)'>Soedinitel CL.X.W 20 (18,8mm)</option>
            <option value='Soedinitel CL.X.W 20 (6mm)'>Soedinitel CL.X.W 20 (6mm)</option>
            <option value='Soedinitel CL.X.W 34 (18,8mm)'>Soedinitel CL.X.W 34 (18,8mm)</option>
            <option value='BKT 70 Soed. Impost (J01-23.6mm)'>BKT 70 Soed. Impost (J01-23.6mm)</option>
            <option value='Ruchka Dvernaya Fornaks (30mm) (oq)'>Ruchka Dvernaya Fornaks (30mm) (oq)</option>
            <option value='Ruchka Dvernaya mini (oq)'>Ruchka Dvernaya mini (oq)</option>
            <option value='Ruchka dvernaya "BELLA" (2250) mm (rangli)'>Ruchka dvernaya "BELLA" (2250) mm (rangli)</option>
            <option value='Otvetka Mini 153 (oq)'>Otvetka Mini 153 (oq)</option>
            <option value='Soedinitel CL.X.W 14 (6mm)'>Soedinitel CL.X.W 14 (6mm)</option>
            <option value='Soedinitel CLSW 22'>Soedinitel CLSW 22</option>
            <option value='Ruchka "Simple" (oq)'>Ruchka "Simple" (oq)</option>
            <option value='Soedinitel CL.X.W 10 (18,8mm)'>Soedinitel CL.X.W 10 (18,8mm)</option>
            <option value='Soedinitel CL.X.W 10 (6mm)'>Soedinitel CL.X.W 10 (6mm)</option>
            <option value='Ruchka "Simple"(rangli)'>Ruchka "Simple"(rangli)</option>
            <option value='Vstavka (PVCC 005) (rangli)'>Vstavka (PVCC 005) (rangli)</option>
            <option value='Zaglushka (PVCC 002) (rangli)'>Zaglushka (PVCC 002) (rangli)</option>
            <option value='Soedinitel (PVCC 022)'>Soedinitel (PVCC 022)</option>
            <option value='Krishka (PVCC 001) (rangli)'>Krishka (PVCC 001) (rangli)</option>
            <option value='Termo vstavka (PVCC 003) (rangli)'>Termo vstavka (PVCC 003) (rangli)</option>
            <option value='Termo vstavka (PVCC 004) (rangli)'>Termo vstavka (PVCC 004) (rangli)</option>
            <option value='Ruchka Dvernaya Fornaks (30mm) fiksator (oq)'>Ruchka Dvernaya Fornaks (30mm) fiksator (oq)</option>
            <option value='Soedinitel CL.X.W 10 (17mm)'>Soedinitel CL.X.W 10 (17mm)</option>
            <option value='Zaglushka (PVCC 035) (rangli)'>Zaglushka (PVCC 035) (rangli)</option>
            <option value='Ruchka dvernaya "BELLA" (750) mm (rangli)'>Ruchka dvernaya "BELLA" (750) mm (rangli)</option>
            <option value='Soedinitel CL.X.W 38 (44.4mm)'>Soedinitel CL.X.W 38 (44.4mm)</option>
            <option value='Soedinitel CL.X.W 16 (44.4mm)'>Soedinitel CL.X.W 16 (44.4mm)</option>
            <option value='Ruchka dvernaya "BELLA" (500) mm (rangli)'>Ruchka dvernaya "BELLA" (500) mm (rangli)</option>
            <option value='Krishka Podokonnik 350 (Ovolniy) (oq)'>Krishka Podokonnik 350 (Ovolniy) (oq)</option>
            <option value='Soedinitel CL.X.W 14 (21.5mm)'>Soedinitel CL.X.W 14 (21.5mm)</option>
            <option value='Ruchka dvernaya "BELLA" (2350) mm (rangli)'>Ruchka dvernaya "BELLA" (2350) mm (rangli)</option>
            <option value='Zaglushka (PVCC 034) (rangli)'>Zaglushka (PVCC 034) (rangli)</option>
            <option value='Ruchka dvernaya "BELLA" (2000) mm (rangli)'>Ruchka dvernaya "BELLA" (2000) mm (rangli)</option>
            <option value='Soedinitel CL.X.W 34 (28.7mm)'>Soedinitel CL.X.W 34 (28.7mm)</option>
            <option value='Ruchka dvernaya "BELLA" (1200) mm (rangli)'>Ruchka dvernaya "BELLA" (1200) mm (rangli)</option>
            <option value='Ruchka Dvernaya (28mm) Slim fiksator (oq)'>Ruchka Dvernaya (28mm) Slim fiksator (oq)</option>
            <option value='BKT 70 Soed. W 02 (1=25.8)'>BKT 70 Soed. W 02 (1=25.8)</option>
            <option value='Derjatel i ruchka-koltso dlya moskitnoy setki (rangli)'>Derjatel i ruchka-koltso dlya moskitnoy setki (rangli)</option>
            <option value='Ручка к конструкции москитной сетки серии 10х20. "AKBULUT" цветной'>Ручка к конструкции москитной сетки серии 10х20. "AKBULUT" цветной</option>
            <option value='Ручка к конструкции москитной сетки серии 10х20 "AKBULUT"белый'>Ручка к конструкции москитной сетки серии 10х20 "AKBULUT"белый</option>
            <option value='Ruchka dvernaya "BELLA" (2300) mm (rangli)'>Ruchka dvernaya "BELLA" (2300) mm (rangli)</option>
            <option value='Takos PVH'>Takos PVH</option>
            <option value='BKT 70 Soed. W 02 (1=26.3)'>BKT 70 Soed. W 02 (1=26.3)</option>
            <option value='BKT 70 Soed. W 02 (1=5.1)'>BKT 70 Soed. W 02 (1=5.1)</option>
            <option value='BKT 70 Soed. W 03 (1=18.4)'>BKT 70 Soed. W 03 (1=18.4)</option>
            <option value='BKT 70 Soed. W 03 (1=26.3)'>BKT 70 Soed. W 03 (1=26.3)</option>
            <option value='BKT 70 Soed. W 03 (1=5.1)'>BKT 70 Soed. W 03 (1=5.1)</option>
            <option value='Derjatel i ruchka-koltso dlya moskitnoy setki (oq)'>Derjatel i ruchka-koltso dlya moskitnoy setki (oq)</option>
            <option value='BKT 70 Soed. Impost (J03-13.6mm)'>BKT 70 Soed. Impost (J03-13.6mm)</option>
            <option value='Porog Soedinitel 6000 (1kom.) (L;P) (oq)'>Porog Soedinitel 6000 (1kom.) (L;P) (oq)</option>
            <option value='Montajnaya Planka 6000 (Metal)'>Montajnaya Planka 6000 (Metal)</option>
            <option value='BKT 70 Soed. Impost (J05-13.6mm)'>BKT 70 Soed. Impost (J05-13.6mm)</option>
            <option value='Soedinitel BKH-010 (42mm)'>Soedinitel BKH-010 (42mm)</option>
            <option value='Ruchka Dvernaya Fornaks (28mm) (oq)'>Ruchka Dvernaya Fornaks (28mm) (oq)</option>
            <option value='Otvetnaya chast zamka A0275-K (153) (oq)'>Otvetnaya chast zamka A0275-K (153) (oq)</option>
            <option value='Soedinitel CL.X.W 14 (25.8mm)'>Soedinitel CL.X.W 14 (25.8mm)</option>
            <option value='Soedinitel 114 D 300 (35mm)'>Soedinitel 114 D 300 (35mm)</option>
            <option value='Ruchka Dvernaya Fornaks (28mm) fiksator (oq)'>Ruchka Dvernaya Fornaks (28mm) fiksator (oq)</option>
            <option value='BKT 70 Soed. (M11535-18.4mm)'>BKT 70 Soed. (M11535-18.4mm)</option>
            <option value='Soedinitel CL.X.W 10 (10mm)'>Soedinitel CL.X.W 10 (10mm)</option>
            <option value='Soedinitel CL.X.W 20 (20mm)'>Soedinitel CL.X.W 20 (20mm)</option>
            <option value='EPDM L-65 угловой соединитель для уплотнителей'>EPDM L-65 угловой соединитель для уплотнителей</option>
            <option value='EPDM заглушка для штульпа "Чемпион"'>EPDM заглушка для штульпа "Чемпион"</option>
            <option value='EPDM адаптер крышка для Термо 78'>EPDM адаптер крышка для Термо 78</option>
            <option value='EPDM А01 105 угловой соединитель для уплотнителей'>EPDM А01 105 угловой соединитель для уплотнителей</option>
            <option value='EPDM ССЕР 0057 адаптер крышка'>EPDM ССЕР 0057 адаптер крышка</option>
            <option value='EPDM ССЕР 0058 адаптер крышка'>EPDM ССЕР 0058 адаптер крышка</option>
            <option value='EPDM D 017500 Decor Zaglushka'>EPDM D 017500 Decor Zaglushka</option>
            <option value='EPDM адаптер крышка для Термо 70 (BKT-70)'>EPDM адаптер крышка для Термо 70 (BKT-70)</option>
            <option value='EPDM крышка для штульпа АК-40'>EPDM крышка для штульпа АК-40</option>
            <option value='EPDM адаптер крышка 012'>EPDM адаптер крышка 012</option>
            <option value='EPDM epdc 004 дренажный носик'>EPDM epdc 004 дренажный носик</option>
            <option value='EPDM 5108 угловой соединитель для уплотнителей'>EPDM 5108 угловой соединитель для уплотнителей</option>
            <option value='Термоуплотненный окрашенный алюминиевый профиль'>Термоуплотненный окрашенный алюминиевый профиль</option>
            <option value='Неокрашенный алюминиевый профиль (N)'>Неокрашенный алюминиевый профиль (N)</option>
            <option value='Алюминиевый профиль (N)'>Алюминиевый профиль (N)</option>
            <option value='EPDM уплотнитель'>EPDM уплотнитель</option>
            <option value='Анодированный алюминиевый профиль (N)'>Анодированный алюминиевый профиль (N)</option>
            <option value='Термоуплотненный алюминиевый профиль (N)'>Термоуплотненный алюминиевый профиль (N)</option>
            <option value='Мебельный профиль из алюминия анодированный матовое серебро (N)'>Мебельный профиль из алюминия анодированный матовое серебро (N)</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;display:none" id='buxgalter_uchot`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option  value="Штука">Штука</div>
            <option  value="Килограмм">Килограмм</div>
            <option  value="Квадратный метр">Квадратный метр</div>
            <option  value="Метр">Метр</div>
            <option  value="КМП">КМП</div>
            <option  value="Пачка">Пачка</div>
            <option  value="Секция">Секция</div>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;" id='bazoviy_edin`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option vlaue="Штука">Штука</div>
            <option vlaue="Килограмм">Килограмм</div>
            <option vlaue="Квадратный метр">Квадратный метр</div>
            <option vlaue="Метр">Метр</div>
            <option vlaue="КМП">КМП</div>
            <option vlaue="Пачка">Пачка</div>
            <option vlaue="Секция">Секция</div>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;display:none" id='alter_edin`+ String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option vlaue="Штука">Штука</div>
            <option vlaue="Килограмм">Килограмм</div>
            <option vlaue="Квадратный метр">Квадратный метр</div>
            <option vlaue="Метр">Метр</div>
            <option vlaue="КМП">КМП</div>
            <option vlaue="Пачка">Пачка</div>
            <option vlaue="Секция">Секция</div>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;" id='status`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option value="Активный">Активный</option>
            <option value="Пассивный">Пассивный</option>
        </select>
        </div>
    </td>
    <td >
        
        <span class =' text-center ' style="font-size: small; width:190px; font-weight: bold; text-transform: uppercase;" id='zavod_name`+String(i)+`'>ZAVOD ALUCOBOND</span>
        
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="width: 75px; font-size:10px;display:none;height:32px " id='diller`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;" id='tip_clenta`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option value="AKFA">AKFA</option>
            <option value="IMZO">IMZO</option>
            <option value="FRANCHISING">FRANCHISING</option>
            <option value="AKFA-IMZO-FRANCHISING">AKFA-IMZO-FRANCHISING</option>
            <option value="IMZO-FRANCHISING">IMZO-FRANCHISING</option>
        </select>
        </div>
    </td>
    <td style="display: none;" >
        <div class="input-group input-group-sm mb-1">
        <span id="is_active`+String(i)+`" style="display: none;"></span>
        </div>
    </td>
    
    </tr>`
  }


var table = $('#table-artikul')

table.append(text)








function create(i){
    data_base[i] = new BasePokritiya() 
    data_base[i].id = 1 
    var brend = $('#brend'+i)
    brend.attr('disabled',false)
    brend.css('border-color','red')

    var mikron = $('#mikron'+i)
    mikron.attr('disabled',false)
    mikron.css('border-color','red')

    var storonnost = $('#storonnost'+i)
    storonnost.attr('disabled',false)
    storonnost.css('border-color','red')

    var kod_sveta = $('#kod_sveta'+i)
    kod_sveta.attr('disabled',false)
    kod_sveta.css('border-color','red')

    var tip_paneli = $('#tip_paneli'+i)
    tip_paneli.attr('disabled',false)
    tip_paneli.css('border-color','red')

    var dlina = $('#dlina'+i)
    dlina.css('display','block')
    dlina.css('border-color','red')

    var shirina = $('#shirina'+i)
    shirina.css('display','block')
    shirina.css('border-color','red')

    var sap_code = $('#sap_code'+i)
    sap_code.css('display','block')

    var krat = $('#krat'+i)
    krat.css('display','block')

    var comment = $('#comment'+i)
    comment.css('display','block')

    var pickupdate = $('#pickupdate'+i)
    pickupdate.css('display','block')
    pickupdate.css('border-color','red')

    var sena_c_nds = $('#sena_c_nds'+i)
    sena_c_nds.css('display','block')
    sena_c_nds.css('border-color','red')
    var sena_bez_nds = $('#sena_bez_nds'+i)
    sena_bez_nds.css('display','block')
    sena_bez_nds.css('border-color','red')

    var online_id = $('#online_id'+i)
    online_id.css('display','block')
    var nazvaniye_ruchnoy = $('#nazvaniye_ruchnoy'+i)
    nazvaniye_ruchnoy.css('display','block')
    var group = $('#group'+i)
    group.css('display','block')
    group.css('border-color','red')
    var buxgalter_tovar = $('#buxgalter_tovar'+i)
    buxgalter_tovar.css('display','block')
    buxgalter_tovar.css('border-color','red')
    var buxgalter_uchot = $('#buxgalter_uchot'+i)
    buxgalter_uchot.css('display','block')
    var bazoviy_edin = $('#bazoviy_edin'+i)
    bazoviy_edin.css('display','block')
    var alter_edin = $('#alter_edin'+i)
    alter_edin.css('display','block')
    var diller = $('#diller'+i)
    diller.css('display','block')
    diller.css('border-color','red')
    var tip_clenta = $('#tip_clenta'+i)
    tip_clenta.css('display','block')
    tip_clenta.css('border-color','red')
    






    var status_first =$('#status'+i);
    status_first.css('display','block')
    status_first.val('Активный')

    

    var is_active =$('#is_active'+i);
    is_active.text('Пассивный')
    // status_first.attr('disabled',true)

    var tip =$('#tip'+i);
    tip.val('Готовый продукт')
    

    var activate_btn =$('#activate_btn'+i);
    activate_btn.attr('disabled',true)
    var create_btn =$('#create_btn'+i);
    create_btn.attr('disabled',true)
    
   
    data_base[i].gruppa_materialov ='AKPGP'
    data_base[i].svet_product ='Colour'
    data_base[i].group_zakup ='Alucobond'
    data_base[i].tip ='ГП'
    data_base[i].segment ='Пустой'

    data_base[i].buxgalter_uchot ='Килограмм'
    data_base[i].bazoviy_edin ='Штука'
    data_base[i].alter_edin ='Квадратный метр'
    data_base[i].zavod_name ='ZAVOD ALUCOBOND'
    buxgalter_uchot.val('Килограмм')
    bazoviy_edin.val('Штука')
    alter_edin.val('Квадратный метр')

    data_base[i].zavod_name ='ZAVOD ALUCOBOND'


}

function activate(i){
    data_base[i] = new BasePokritiya() 
    data_base[i].id = 1 

    var brend = $('#brend'+i)
    brend.attr('disabled',false)
    brend.css('border-color','red')

    var mikron = $('#mikron'+i)
    mikron.attr('disabled',false)
    mikron.css('border-color','red')

    var storonnost = $('#storonnost'+i)
    storonnost.attr('disabled',false)
    storonnost.css('border-color','red')

    var kod_sveta = $('#kod_sveta'+i)
    kod_sveta.attr('disabled',false)
    kod_sveta.css('border-color','red')

    var tip_paneli = $('#tip_paneli'+i)
    tip_paneli.attr('disabled',false)
    tip_paneli.css('border-color','red')

    var dlina = $('#dlina'+i)
    dlina.css('display','block')
    dlina.css('border-color','red')

    var shirina = $('#shirina'+i)
    shirina.css('display','block')
    shirina.css('border-color','red')

    var sap_code = $('#sap_code'+i)
    sap_code.css('display','block')

    var krat = $('#krat'+i)
    krat.css('display','block')

    var comment = $('#comment'+i)
    comment.css('display','block')

    var pickupdate = $('#pickupdate'+i)
    pickupdate.css('display','block')

    var sena_c_nds = $('#sena_c_nds'+i)
    sena_c_nds.css('display','block')
    var sena_bez_nds = $('#sena_bez_nds'+i)
    sena_bez_nds.css('display','block')
    var online_id = $('#online_id'+i)
    online_id.css('display','block')
    online_id.css('border-color','red')
    var nazvaniye_ruchnoy = $('#nazvaniye_ruchnoy'+i)
    nazvaniye_ruchnoy.css('display','block')
    nazvaniye_ruchnoy.css('border-color','red')
    var group = $('#group'+i)
    group.css('display','block')
    var buxgalter_tovar = $('#buxgalter_tovar'+i)
    buxgalter_tovar.css('display','block')
    var buxgalter_uchot = $('#buxgalter_uchot'+i)
    buxgalter_uchot.css('display','block')
    var bazoviy_edin = $('#bazoviy_edin'+i)
    bazoviy_edin.css('display','block')
    var alter_edin = $('#alter_edin'+i)
    alter_edin.css('display','block')
    var diller = $('#diller'+i)
    diller.css('display','block')
    var tip_clenta = $('#tip_clenta'+i)
    tip_clenta.css('display','block')
    



    var status_first =$('#status'+i);
    status_first.css('display','block')
    status_first.val('Активный')



    var activate_btn =$('#activate_btn'+i);
    var create_btn =$('#create_btn'+i);
    activate_btn.attr('disabled',true)
    create_btn.attr('disabled',true)
    

    var is_active =$('#is_active'+i);
    is_active.text('Активный')
    // status_first.attr('disabled',true)
    data_base[i].gruppa_materialov ='AKPGP'
    data_base[i].svet_product ='Colour'
    data_base[i].group_zakup ='Alucobond'
    data_base[i].tip ='ГП'
    data_base[i].segment ='Пустой'
    data_base[i].is_active = true


    data_base[i].zavod_name ='ZAVOD ALUCOBOND'

}







function clear_artikul(id){
    var table_tr =$('#table_tr'+id);
    table_tr.css('background-color','white')

    var kratkiy_tekst = document.getElementById('kratkiy_tekst'+String(id));
    kratkiy_tekst.innerText="";    
    
   
    delete data_base[id];
    var brend = $('#brend'+id)
    brend.val("")
    brend.attr('disabled',true)

    var mikron = $('#mikron'+id)
    mikron.val("")
    mikron.attr('disabled',true)

    var storonnost = $('#storonnost'+id)
    storonnost.val("")
    storonnost.attr('disabled',true)

    var kod_sveta = $('#kod_sveta'+id)
    kod_sveta.val("")
    kod_sveta.attr('disabled',true)

    var naz_sveta = $('#naz_sveta'+id)
    naz_sveta.text("")
    naz_sveta.attr('disabled',true)

    var tip_paneli = $('#tip_paneli'+id)
    tip_paneli.val("")
    tip_paneli.attr('disabled',true)

    var dlina = $('#dlina'+id)
    dlina.val("")
    dlina.css('display','none')

    var shirina = $('#shirina'+id)
    shirina.val("")
    shirina.css('display','none')

    var sap_code = $('#sap_code'+id)
    sap_code.val("")
    sap_code.css('display','none')

    var krat = $('#krat'+id)
    krat.val("")
    krat.css('display','none')

    var comment = $('#comment'+id)
    comment.val("")
    comment.css('display','none')

    var pickupdate = $('#pickupdate'+id)
    pickupdate.val("")
    pickupdate.css('display','none')

    var sena_c_nds = $('#sena_c_nds'+id)
    sena_c_nds.val("")
    sena_c_nds.css('display','none')

    var sena_bez_nds = $('#sena_bez_nds'+id)
    sena_bez_nds.val("")
    sena_bez_nds.css('display','none')

    var online_id = $('#online_id'+id)
    online_id.val("")
    online_id.css('display','none')

    var nazvaniye_ruchnoy = $('#nazvaniye_ruchnoy'+id)
    nazvaniye_ruchnoy.val("")
    nazvaniye_ruchnoy.css('display','none')

    var group = $('#group'+id)
    group.val("")
    group.css('display','none')

    var buxgalter_tovar = $('#buxgalter_tovar'+id)
    buxgalter_tovar.val("")
    buxgalter_tovar.css('display','none')

    var buxgalter_uchot = $('#buxgalter_uchot'+id)
    buxgalter_uchot.val("")
    buxgalter_uchot.css('display','none')

    var bazoviy_edin = $('#bazoviy_edin'+id)
    bazoviy_edin.val("")
    bazoviy_edin.css('display','none')

    var alter_edin = $('#alter_edin'+id)
    alter_edin.val("")
    alter_edin.css('display','none')

    var status_first =$('#status'+id);
    status_first.css('display','none')
    status_first.val('')

    var diller = $('#diller'+id)
    diller.val("")
    diller.css('display','none')

    var tip_clenta = $('#tip_clenta'+id)
    tip_clenta.val("")
    tip_clenta.css('display','none')


    var activate_btn =$('#activate_btn'+id);
    var create_btn =$('#create_btn'+id);
    activate_btn.attr('disabled',false)
    create_btn.attr('disabled',false)
    
}











function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{

        var brend = $('#brend'+id)
        var mikron = $('#mikron'+id)
        var storonnost = $('#storonnost'+id)
        var kod_sveta = $('#kod_sveta'+id)
        var naz_sveta = $('#naz_sveta'+id)
        var tip_paneli = $('#tip_paneli'+id)
        var dlina = $('#dlina'+id)
        var shirina = $('#shirina'+id)
        var kratkiy_tekst = $('#kratkiy_tekst'+id)
        var sap_code = $('#sap_code'+id)
        var krat = $('#krat'+id)
        var comment = $('#comment'+id)
        var pickupdate = $('#pickupdate'+id)
        var sena_c_nds = $('#sena_c_nds'+id)
        var sena_bez_nds = $('#sena_bez_nds'+id)
        var online_id = $('#online_id'+id)
        var nazvaniye_ruchnoy = $('#nazvaniye_ruchnoy'+id)
        var group = $('#group'+id)
        var buxgalter_tovar = $('#buxgalter_tovar'+id)

        var buxgalter_uchot = $('#buxgalter_uchot'+id)
        var bazoviy_edin = $('#bazoviy_edin'+id)
        var alter_edin = $('#alter_edin'+id)
        var diller = $('#diller'+id)
        var tip_clenta = $('#tip_clenta'+id)
        var status_online =$('#status'+id);
        var is_active =$('#is_active'+id);
        console.log(mikron.val())
    
        if(brend.val()!=''){
            data_base[id].brend = brend.val();
            brend.css('border-color','#dedad9')
        }else{
            data_base[id].brend = NaN;
            brend.css('border-color','red')
        }
        if(mikron.val()!=''){
            mikron.css('border-color','#dedad9')
            data_base[id].mikron = mikron.val();
        }else{
            mikron.css('border-color','red')
            data_base[id].mikron = NaN;
        }
        if(storonnost.val()!=''){
            storonnost.css('border-color','#dedad9')
            data_base[id].storonnost = storonnost.val();
        }else{
            storonnost.css('border-color','red')
            data_base[id].storonnost = NaN;
        }
        if(kod_sveta.val()!=''){
            kod_sveta.css('border-color','#dedad9')
            kod_svet1 =$('#kod_sveta'+id +' option:selected').text()
            naz_sveta.text(kod_sveta.val())
            data_base[id].kod_sveta = kod_svet1;
            data_base[id].naz_sveta = kod_sveta.val();
        }else{
            kod_sveta.css('border-color','red')
            naz_sveta.text("")
            data_base[id].kod_sveta = NaN;
            data_base[id].naz_sveta = NaN;
        }
        

        if(tip_paneli.val()!=''){
            tip_paneli.css('border-color','#dedad9')
            data_base[id].tip_paneli = tip_paneli.val();
        }else{
            tip_paneli.css('border-color','red')
            data_base[id].tip_paneli = NaN;
        }
        if(dlina.val()!=''){
            dlina.css('border-color','#dedad9')
            data_base[id].dlina = dlina.val();
        }else{
            dlina.css('border-color','red')
            data_base[id].dlina = NaN;
        }
        if(shirina.val()!=''){
            shirina.css('border-color','#dedad9')
            data_base[id].shirina = shirina.val();
        }else{
            shirina.css('border-color','red')
            data_base[id].shirina = NaN;
        }
        if(sap_code.val()!=''){
            data_base[id].sap_code = sap_code.val();
        }else{
            data_base[id].sap_code = NaN;
        }
        if(krat.val()!=''){
            data_base[id].krat = krat.val();
        }else{
            data_base[id].krat = NaN;
        }
        if(comment.val()!=''){
            data_base[id].comment = comment.val();
        }else{
            data_base[id].comment = NaN;
        }
        
        var is_active =$('#is_active'+id)
        
        if(is_active.text()=='Активный'){

            if(online_id.val()!=''){
                online_id.css('border-color','#dedad9')
                data_base[id].online_id = online_id.val();
            }else{
                online_id.css('border-color','red')
                data_base[id].online_id = NaN;
            }
            if(nazvaniye_ruchnoy.val()!=''){
                nazvaniye_ruchnoy.css('border-color','#dedad9')
                data_base[id].nazvaniye_ruchnoy = nazvaniye_ruchnoy.val();
            }else{
                nazvaniye_ruchnoy.css('border-color','red')
                data_base[id].nazvaniye_ruchnoy = NaN;
            }
            
            if(pickupdate.val()!=''){
                data_base[id].pickupdate = pickupdate.val();
            }else{
                data_base[id].pickupdate = NaN;
            }
            if(sena_c_nds.val()!=''){
                data_base[id].sena_c_nds = sena_c_nds.val();
            }else{
                data_base[id].sena_c_nds = NaN;
            }
            if(sena_bez_nds.val()!=''){
                data_base[id].sena_bez_nds = sena_bez_nds.val();
            }else{
                data_base[id].sena_bez_nds = NaN;
            }
            
            if(group.val()!=''){
                data_base[id].group = group.val();
            }else{
                data_base[id].group = NaN;
            }
    
            if(buxgalter_tovar.val()!=''){
                data_base[id].buxgalter_tovar = buxgalter_tovar.val();
            }else{
                data_base[id].buxgalter_tovar = NaN;
            }
            
            if(buxgalter_uchot.val()!=''){
                data_base[id].buxgalter_uchot = buxgalter_uchot.val();
            }else{
                data_base[id].buxgalter_uchot = NaN;
            }
            
            if(bazoviy_edin.val()!=''){
                data_base[id].bazoviy_edin = bazoviy_edin.val();
            }else{
                data_base[id].bazoviy_edin = NaN;
            }
            if(alter_edin.val()!=''){
                data_base[id].alter_edin = alter_edin.val();
            }else{
                data_base[id].alter_edin = NaN;
            }
            if(diller.val()!=''){
                data_base[id].diller = diller.val();
            }else{
                data_base[id].diller = NaN;
            }
            if(tip_clenta.val()!=''){
                data_base[id].tip_clenta = tip_clenta.val();
            }else{
                data_base[id].tip_clenta = NaN;
            }
            if(status_online.val()!=''){
                data_base[id].status_online = status_online.val();
            }else{
                data_base[id].status_online = NaN;
            }
    
           

          
        }else{
           
            if(online_id.val()!=''){
                
                data_base[id].online_id = online_id.val();
            }else{
               
                data_base[id].online_id = NaN;
            }
            if(nazvaniye_ruchnoy.val()!=''){
                
                data_base[id].nazvaniye_ruchnoy = nazvaniye_ruchnoy.val();
            }else{
                
                data_base[id].nazvaniye_ruchnoy = NaN;
            }
            if(pickupdate.val()!=''){
                pickupdate.css('border-color','#dedad9')
                data_base[id].pickupdate = pickupdate.val();
            }else{
                pickupdate.css('border-color','red')
                data_base[id].pickupdate = NaN;
            }
            if(sena_c_nds.val()!=''){
                sena_c_nds.css('border-color','#dedad9')
                data_base[id].sena_c_nds = sena_c_nds.val();
            }else{
                sena_c_nds.css('border-color','red')
                data_base[id].sena_c_nds = NaN;
            }
            if(sena_bez_nds.val()!=''){
                sena_bez_nds.css('border-color','#dedad9')
                data_base[id].sena_bez_nds = sena_bez_nds.val();
            }else{
                sena_bez_nds.css('border-color','red')
                data_base[id].sena_bez_nds = NaN;
            }
            
            if(group.val()!=''){
                group.css('border-color','#dedad9')
                data_base[id].group = group.val();
            }else{
                group.css('border-color','red')
                data_base[id].group = NaN;
            }
            console.log(buxgalter_tovar.val(),'buxfddffff')
            if(buxgalter_tovar.val()!=''){
                buxgalter_tovar.css('border-color','#dedad9')
                data_base[id].buxgalter_tovar = buxgalter_tovar.val();
            }else{
                buxgalter_tovar.css('border-color','red')
                data_base[id].buxgalter_tovar = NaN;
            }
            
            if(buxgalter_uchot.val()!=''){
                data_base[id].buxgalter_uchot = buxgalter_uchot.val();
            }else{
                data_base[id].buxgalter_uchot = NaN;
            }
            
            if(bazoviy_edin.val()!=''){
                data_base[id].bazoviy_edin = bazoviy_edin.val();
            }else{
                data_base[id].bazoviy_edin = NaN;
            }
            if(alter_edin.val()!=''){
                data_base[id].alter_edin = alter_edin.val();
            }else{
                data_base[id].alter_edin = NaN;
            }
            if(diller.val()!=''){
                diller.css('border-color','#dedad9')
                data_base[id].diller = diller.val();
            }else{
                diller.css('border-color','red')
                data_base[id].diller = NaN;
            }
            if(tip_clenta.val()!=''){
                tip_clenta.css('border-color','#dedad9')
                data_base[id].tip_clenta = tip_clenta.val();
            }else{
                tip_clenta.css('border-color','red')
                data_base[id].tip_clenta = NaN;
            }
            if(status_online.val()!=''){
                data_base[id].status_online = status_online.val();
            }else{
                data_base[id].status_online = NaN;
            }
    
    
        }
        
    




    



    var data = data_base[id].get_kratkiy_tekst()

    
    if(data.accept){
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','#2de319')
        data_base[id].full=true
        data_base[id].kratkiy_tekst = data.text
    }else{
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','white')
        data_base[id].kratkiy_tekst = NaN;
        data_base[id].full=false

    }
    
    kratkiy_tekst.text(data.text)

    }
}

function add_column(){
        
    text =""
    var sizee = Object.keys(data_base).length;
    console.log(sizee)
    var sizeee = $('#table-artikul tr').length;
    
    for (let i = sizeee + 1; i < sizeee+2; i++) {
        text +=`
        <tr id='table_tr` +String(i)+`' >                   
        <td >
            <div class="input-group input-group-sm mb-1">
                <div class="btn-group" role="group" aria-label="Basic example">
                    <button type="button" class="btn btn-secondary btn-sm" onclick="create(`+String(i)+`)" id='create_btn`+String(i)+`' >Создание</button>
                    <button type="button" class="btn btn-info btn-sm" onclick="activate(`+String(i)+`)" id='activate_btn`+String(i)+`'>Активация</button>
                    <button type="button" class="btn btn-warning btn-sm gradient-buttons" onclick="clear_artikul(`+String(i)+`)"  id='clear_btn`+String(i)+`'>Очистить</button>
                </div>
            </div>
        </td>
        <td >
        <select class="form-select" aria-label="" style="width: 177px;text-transform: uppercase; font-size:12px; padding-right:0px;" onchange="create_kratkiy_tekst(`+String(i)+`)" disabled id='brend`+String(i)+`' required>
            <option  selected ></option>
            <option value="AKFA" >AKFA</option>
            <option value="ROYAL" >ROYAL</option>
        </select>
        </td>
        <td >
        <select class="form-select" aria-label="" style="width: 177px;text-transform: uppercase; font-size:12px; padding-right:0px;" onchange="create_kratkiy_tekst(`+String(i)+`)" disabled id='mikron`+String(i)+`' required>
            <option  selected ></option>
            <option value="180" >180</option>
            <option value="210">210</option>
            <option value="250">250</option>
            <option value="400">400</option>
            <option value="700">700</option>
        </select>
        </td>
        <td >
        <select class="form-select" aria-label="" style="width: 177px;text-transform: uppercase; font-size:12px; padding-right:0px;" onchange="create_kratkiy_tekst(`+String(i)+`)" disabled id='storonnost`+String(i)+`' required>
            <option  selected ></option>
            <option value="X1">X1</option>
            <option value="X2">X2</option>
        </select>
        </td>
        
        
        <td >
            <select class="form-select" aria-label="" style="width: 177px;text-transform: uppercase; font-size:12px; padding-right:0px;" onchange="create_kratkiy_tekst(`+String(i)+`)" disabled id='kod_sveta`+String(i)+`' required>
                <option  selected ></option>
                <option value="Глянцево-Белый">771</option>
                <option value="Металлик">772</option>
                <option value="Глянцево-Молочный">773</option>
                <option value="Дуб Мокко">777</option>
                <option value="Золотой дуб ламинат">778</option>
                <option value="Глянцево-Коричневый">779</option>
                <option value="Белый матовый">780</option>
                <option value="Мокрый асфальт">782</option>
                <option value="Тёмно Серый">784</option>
                <option value="Жемчуг">806</option>
                <option value="Каштан">807</option>
                <option value="Орех">808</option>
                <option value="Светло-Зелёный">776</option>
                <option value="Глянцево-Чёрный">781</option>
                <option value="Тёмно-Синий">783</option>
                <option value="Красный">785</option>
                <option value="Мис">703</option>
                <option value="Травертин">803</option>
                <option value="З/Д Белый">800</option>
                <option value="З/Д Серый">801</option>
                <option value="Мрамор">802</option>
                <option value="Чёрный мрамор">804</option>
                <option value="Silver">809</option>
                <option value="Белый мрамор">810</option>
                <option value="Серый матовый">786</option>
                <option value="Чёрный матовый">787</option>
                <option value="Светло Серый">790</option>
                <option value="Жёлтый матовый">789</option>
                <option value="Cиний Mатовый">788</option>
                <option value="Светло Серый">790</option>
            
            </select>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
                    <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;padding-left:35%;" id ='naz_sveta` +String(i)+`'></span>
            </div>
        </td>
        <td >
        <select class="form-select" aria-label="" style="width: 177px;text-transform: uppercase; font-size:12px; padding-right:0px;" onchange="create_kratkiy_tekst(`+String(i)+`)" disabled id='tip_paneli`+String(i)+`' required>
            <option  selected ></option>
            <option value="A1">A1</option>
            <option value="A2">A2</option>
        </select>
        </td>
    
        <td >
            <div class="input-group input-group-sm mb-1">
            
                <input type='text' class=" form-control " style=" width: 110px; font-size:10px; display:none; height:32px" id='dlina`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
    
            </div>
           
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            
                <input type='text' class=" form-control " style=" width: 110px; font-size:10px; display:none; height:32px" id='shirina`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
    
            </div>
        </td>
        <td >
             <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;padding-left:35%" id='gruppa_materialov`+String(i)+`'>AKPGP</span>
        
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='kratkiy_tekst`+String(i)+`'></span>
            </div>
        </td>
    
        <td >
            <div class="input-group input-group-sm mb-1">
           
            <input type='text' class=" form-control " style=" width: 110px; font-size:10px; display:none; height:32px" id='sap_code`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        
            </div>
        </td> 
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 220px; font-size:10px; display:none; height:32px"  id='krat`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
           <textarea   rows='1' class=" form-control " style="width: 220px; font-size:10px;display:none;height:32px" id='comment`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></textarea >
           </div>
        </td>
        <td >
            <input  style='display:none; line-height:15px' type="date" class="form-control" id="pickupdate`+String(i)+`" onchange='create_kratkiy_tekst(`+String(i)+`)'>      
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 75px; font-size:10px; display:none;height:32px" id='sena_c_nds`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 75px; font-size:10px; display:none; height:32px" id='sena_bez_nds`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 75px; font-size:10px;display:none;height:32px " id='online_id`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <textarea   rows='1' class=" form-control " style=" width: 220px; font-size:10px; display:none; height:32px" id='nazvaniye_ruchnoy`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></textarea >
            </div>
        </td>
        
        <td >
            <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='svet_product`+String(i)+`'>Colour</span>
            
        </td>
        <td >
            <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='group_zakup`+String(i)+`'>Alucobond</span>
        
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 230px;text-transform: uppercase; font-size:12px; padding-right:0px;  display:none;" id='group`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="Bez Nakleyka"> Nakleyka</option>
                <option value="Bez Nakleyka TR"> Nakleyka TR</option>
                <option value="Engelberg (40 MIKRON)">Engelberg (40 MIKRON)</option>
                <option value="IBOARD 35 (21mk) (1.22x2.44mm)">IBOARD 35 (21mk) (1.22x2.44mm)</option>
                <option value="IBOARD CH (18mk)">IBOARD CH (18mk)</option>
                <option value="Iboard (Negaryuchiy)">Iboard (Negaryuchiy)</option>
                <option value="IBOARD TR (25mk)">IBOARD TR (25mk)</option>
                <option value="Ne Standart Alucobond">Ne Standart Alucobond</option>
                <option value="ROYAL 33 (21mk) (1.22*2.44mm)">ROYAL 33 (21mk) (1.22*2.44mm)</option>
                <option value="ROYAL CH (25mk)">ROYAL CH (25mk)</option>
                <option value="ROYAL TR (25mk)">ROYAL TR (25mk)</option>
                <option value="IBOARD CH (21mk)">IBOARD CH (21mk)</option>
                <option value="IB_Nestandart (Kg)">IB_Nestandart (Kg)</option>
            </select>
            </div>
        </td>
        <td >
            <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='tip`+String(i)+`'>ГП</span>
            
        </td>
        <td >
                <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='segment`+String(i)+`'>Пустой</span>
            
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 520px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;" id='buxgalter_tovar`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value='Профиль из ПВХ ламинированный'>Профиль из ПВХ ламинированный</option>
                <option value='Otvetka 153 (oq)'>Otvetka 153 (oq)</option>
                <option value='Ламбри из ПВХ'>Ламбри из ПВХ</option>
                <option value='Soedinitel OP.40.J05 L=10mm'>Soedinitel OP.40.J05 L=10mm</option>
                <option value='Soedinitel CL.X.W 14 (5mm)'>Soedinitel CL.X.W 14 (5mm)</option>
                <option value='BKT 78 Soed. (M11427-15.8mm)'>BKT 78 Soed. (M11427-15.8mm)</option>
                <option value='Soedinitel CL.X.W 14 (38mm)'>Soedinitel CL.X.W 14 (38mm)</option>
                <option value='BKT 70 Soed. W 02 (1=7.8)'>BKT 70 Soed. W 02 (1=7.8)</option>
                <option value='Otvetka 155 (rangli)'>Otvetka 155 (rangli)</option>
                <option value='Ruchka Dvernaya Fornaks (28mm) (rangli)'>Ruchka Dvernaya Fornaks (28mm) (rangli)</option>
                <option value='Petlya Dvernaya 2SK MASTER (rangli)'>Petlya Dvernaya 2SK MASTER (rangli)</option>
                <option value='Petlya (rangli)'>Petlya (rangli)</option>
                <option value='Soedinitel Chovush'>Soedinitel Chovush</option>
                <option value='Soedinitel (Bolshoy) CHEMPION'>Soedinitel (Bolshoy) CHEMPION</option>
                <option value='Petlya Dvernaya Chempion (rangli)'>Petlya Dvernaya Chempion (rangli)</option>
                <option value='Soedinitel (Bolshoy) (ALD-2)'>Soedinitel (Bolshoy) (ALD-2)</option>
                <option value='Krishka Podokonnik (ALYUMIN) (oq)'>Krishka Podokonnik (ALYUMIN) (oq)</option>
                <option value='Soedinitel Universal'>Soedinitel Universal</option>
                <option value='Ogranichitel (rangli)'>Ogranichitel (rangli)</option>
                <option value='Otvetka Mini 153 (rangli)'>Otvetka Mini 153 (rangli)</option>
                <option value='Ruchka Elegant (rangli)'>Ruchka Elegant (rangli)</option>
                <option value='Ruchka LUX Fortuna O (rangli)'>Ruchka LUX Fortuna O (rangli)</option>
                <option value='Petlya 100 mm (rangli)'>Petlya 100 mm (rangli)</option>
                <option value='Ruchka dvernaya "BELLA" (700) mm (rangli)'>Ruchka dvernaya "BELLA" (700) mm (rangli)</option>
                <option value='Soedinitel CL.X.W 34 (43mm)'>Soedinitel CL.X.W 34 (43mm)</option>
                <option value='Ruchka dvernaya "BELLA" (500) mm (oq)'>Ruchka dvernaya "BELLA" (500) mm (oq)</option>
                <option value='Ruchka dvernaya "BELLA" (600) mm (rangli)'>Ruchka dvernaya "BELLA" (600) mm (rangli)</option>
                <option value='Ruchka LUX Fortuna O (oq)'>Ruchka LUX Fortuna O (oq)</option>
                <option value='Otvetka Mini 155 (oq)'>Otvetka Mini 155 (oq)</option>
                <option value='Soedinitel CL.X.W 10 (25.8mm)'>Soedinitel CL.X.W 10 (25.8mm)</option>
                <option value='Termo soedinitel 19 mm'>Termo soedinitel 19 mm</option>
                <option value='Petlya 100 mm (oq)'>Petlya 100 mm (oq)</option>
                <option value='Petlya (ALD-2) (oq)'>Petlya (ALD-2) (oq)</option>
                <option value='Otvetnaya chast zamka A0275-K (155) (rangli)'>Otvetnaya chast zamka A0275-K (155) (rangli)</option>
                <option value='Petlya (ALD-2) (rangli)'>Petlya (ALD-2) (rangli)</option>
                <option value='Petlya Dvernaya 3SK MASTER (rangli)'>Petlya Dvernaya 3SK MASTER (rangli)</option>
                <option value='Petlya Dvernaya Alyumin (rangli)'>Petlya Dvernaya Alyumin (rangli)</option>
                <option value='Ruchka Kvadrat (rangli)'>Ruchka Kvadrat (rangli)</option>
                <option value='Chit-Chit PVH.uz (rangli)'>Chit-Chit PVH.uz (rangli)</option>
                <option value='Otvetka 153 (rangli)'>Otvetka 153 (rangli)</option>
                <option value='Ruchka LUX Fortuna Mini O (rangli)'>Ruchka LUX Fortuna Mini O (rangli)</option>
                <option value='Zashyolka Narujnyaya (rangli)'>Zashyolka Narujnyaya (rangli)</option>
                <option value='Shpingalet (rangli)'>Shpingalet (rangli)</option>
                <option value='Ruchka DELFIN (rangli)'>Ruchka DELFIN (rangli)</option>
                <option value='Otvetka Mini 155 (rangli)'>Otvetka Mini 155 (rangli)</option>
                <option value='Otvetnaya chast zamka A0275-K (153) (rangli)'>Otvetnaya chast zamka A0275-K (153) (rangli)</option>
                <option value='BKT 70 Soed. Impost (J01-52.5mm)'>BKT 70 Soed. Impost (J01-52.5mm)</option>
                <option value='BKT 70 Soed. Impost (J01-66.5mm)'>BKT 70 Soed. Impost (J01-66.5mm)</option>
                <option value='BKT 70 Soed. Impost (J02-13.6mm)'>BKT 70 Soed. Impost (J02-13.6mm)</option>
                <option value='BKT 70 Soed. Impost (J02-43.6mm)'>BKT 70 Soed. Impost (J02-43.6mm)</option>
                <option value='BKT 70 Soed. Impost (J03-66.6mm)'>BKT 70 Soed. Impost (J03-66.6mm)</option>
                <option value='BKT 70 Soed. Impost (J06-43.6mm)'>BKT 70 Soed. Impost (J06-43.6mm)</option>
                <option value='BKT 70 Soed. Impost (J06-66.5mm)'>BKT 70 Soed. Impost (J06-66.5mm)</option>
                <option value='BKT 70 Soed. W 01 (1=21.7)'>BKT 70 Soed. W 01 (1=21.7)</option>
                <option value='BKT 70 Soed. W 01 (1=5.1)'>BKT 70 Soed. W 01 (1=5.1)</option>
                <option value='BKT 70 Soed. W 01 (1=8.5)'>BKT 70 Soed. W 01 (1=8.5)</option>
                <option value='Krishka Podokonnik (ALYUMIN) (rangli)'>Krishka Podokonnik (ALYUMIN) (rangli)</option>
                <option value='Kreplenie moskitnoy setki (rangli)'>Kreplenie moskitnoy setki (rangli)</option>
                <option value='BKT 70 Soed. W 01 (1=8)'>BKT 70 Soed. W 01 (1=8)</option>
                <option value='BKT 78 Soed. (M11427-19.5mm)'>BKT 78 Soed. (M11427-19.5mm)</option>
                <option value='Kreplenie moskitnoy setki (oq)'>Kreplenie moskitnoy setki (oq)</option>
                <option value='BKT 78 Soed. (M11427-27mm)'>BKT 78 Soed. (M11427-27mm)</option>
                <option value='Ruchka LUX Pol (oq)'>Ruchka LUX Pol (oq)</option>
                <option value='Ruchka Sos. VENTURO (oq)'>Ruchka Sos. VENTURO (oq)</option>
                <option value='Montajnaya Planka 5200 (Metal)'>Montajnaya Planka 5200 (Metal)</option>
                <option value='Ламинированный термоуплотненный алюминиевый профиль'>Ламинированный термоуплотненный алюминиевый профиль</option>
                <option value='Термоуплотненный анодированный алюминиевый профиль (N)'>Термоуплотненный анодированный алюминиевый профиль (N)</option>
                <option value='Профиль из ПВХ с уплотнителем'>Профиль из ПВХ с уплотнителем</option>
                <option value='Алюминиевый профиль с декоративным покрытием'>Алюминиевый профиль с декоративным покрытием</option>
                <option value='Подоконник из ПВХ'>Подоконник из ПВХ</option>
                <option value='Дистанционная рамка'>Дистанционная рамка</option>
                <option value='Профиль из ПВХ ламинированный (Engelberg)'>Профиль из ПВХ ламинированный (Engelberg)</option>
                <option value='Профиль из ПВХ ламинированный с уплотнителем'>Профиль из ПВХ ламинированный с уплотнителем</option>
                <option value='Ламинированный алюминиевый профиль'>Ламинированный алюминиевый профиль</option>
                <option value='Неокрашенный алюминиевый профиль'>Неокрашенный алюминиевый профиль</option>
                <option value='Подоконник из ПВХ ламинированный'>Подоконник из ПВХ ламинированный</option>
                <option value='Уплотнитель для алюминиевых и ПВХ профилей'>Уплотнитель для алюминиевых и ПВХ профилей</option>
                <option value='Профиль из ПВХ'>Профиль из ПВХ</option>
                <option value='Алюминиевый профиль'>Алюминиевый профиль</option>
                <option value='Ламинированный термоуплотненный алюминиевый профиль (N)'>Ламинированный термоуплотненный алюминиевый профиль (N)</option>
                <option value='Металлический усилитель'>Металлический усилитель</option>
                <option value='Ламбри из ПВХ ламинированный'>Ламбри из ПВХ ламинированный</option>
                <option value='Профиль из ПВХ (Engelberg)'>Профиль из ПВХ (Engelberg)</option>
                <option value='Ламинированный алюминиевый профиль (N)'>Ламинированный алюминиевый профиль (N)</option>
                <option value='Алюминиевый профиль с декоративным покрытием (N)'>Алюминиевый профиль с декоративным покрытием (N)</option>
                <option value='Chit-Chit PVH.uz (oq)'>Chit-Chit PVH.uz (oq)</option>
                <option value='BKT 70 Soed. (M11148-13.6mm)'>BKT 70 Soed. (M11148-13.6mm)</option>
                <option value='Ruchka D (oq)'>Ruchka D (oq)</option>
                <option value='Ruchka Kvadrat Mini (oq)'>Ruchka Kvadrat Mini (oq)</option>
                <option value='Ruchka LUX (oq)'>Ruchka LUX (oq)</option>
                <option value='Soedinitel 114 D 400 (13mm)'>Soedinitel 114 D 400 (13mm)</option>
                <option value='Soedinitel 114 D 400 (52mm)'>Soedinitel 114 D 400 (52mm)</option>
                <option value='Petlya Dvernaya Chempion (oq)'>Petlya Dvernaya Chempion (oq)</option>
                <option value='Soedinitel BKH-001 (38mm)'>Soedinitel BKH-001 (38mm)</option>
                <option value='Soedinitel 5507 (6,5mm)'>Soedinitel 5507 (6,5mm)</option>
                <option value='Soedinitel BKH-001 (16mm)'>Soedinitel BKH-001 (16mm)</option>
                <option value='Soedinitel BKH-001 (5mm)'>Soedinitel BKH-001 (5mm)</option>
                <option value='Soedinitel AKF-107 (40mm)'>Soedinitel AKF-107 (40mm)</option>
                <option value='Soedinitel AKF-106 (37.5mm)'>Soedinitel AKF-106 (37.5mm)</option>
                <option value='Vstavka Dlya Zamka (rangli)'>Vstavka Dlya Zamka (rangli)</option>
                <option value='Soedinitel JP2186 (60mm)'>Soedinitel JP2186 (60mm)</option>
                <option value='T 6 Soed. (ST 10 255) C 9.5 Qanot Mal.'>T 6 Soed. (ST 10 255) C 9.5 Qanot Mal.</option>
                <option value='T 6 Soed. (ST 10 366) C 29.0 Qanot Bol.'>T 6 Soed. (ST 10 366) C 29.0 Qanot Bol.</option>
                <option value='T 6 Soed. (ST 10 366) P 27.5 Kosa Bol.'>T 6 Soed. (ST 10 366) P 27.5 Kosa Bol.</option>
                <option value='T 6 Soed. (ST 10 366) P 9.2 Kosa Mal.'>T 6 Soed. (ST 10 366) P 9.2 Kosa Mal.</option>
                <option value='T 6 Soed. (ST 10 565) B 26.0 Balkon Qanot Bol.'>T 6 Soed. (ST 10 565) B 26.0 Balkon Qanot Bol.</option>
                <option value='T 6 Soed. (ST 10 565) B 5.1 Balkon Qanot Mal.'>T 6 Soed. (ST 10 565) B 5.1 Balkon Qanot Mal.</option>
                <option value='Soedinitel AKF-107 (43.5mm)'>Soedinitel AKF-107 (43.5mm)</option>
                <option value='Vstavka Dlya Zamka (oq)'>Vstavka Dlya Zamka (oq)</option>
                <option value='Soedinitel 5505 (45mm)'>Soedinitel 5505 (45mm)</option>
                <option value='Zashyolka Narujnyaya (oq)'>Zashyolka Narujnyaya (oq)</option>
                <option value='Zashyolka Narujnyaya Mini (oq)'>Zashyolka Narujnyaya Mini (oq)</option>
                <option value='Ruchka Dvernaya Fornaks (35mm) (rangli)'>Ruchka Dvernaya Fornaks (35mm) (rangli)</option>
                <option value='Krishka Podokonnik 300 (rangli)'>Krishka Podokonnik 300 (rangli)</option>
                <option value='Ogranichitel PVH (rangli)'>Ogranichitel PVH (rangli)</option>
                <option value='Petlya Dvernaya 3D (rangli)'>Petlya Dvernaya 3D (rangli)</option>
                <option value='Petlya Dvernaya 3D (oq)'>Petlya Dvernaya 3D (oq)</option>
                <option value='Porog Soedinitel 7000 (1kom.) (L;P) (rangli)'>Porog Soedinitel 7000 (1kom.) (L;P) (rangli)</option>
                <option value='Petlya 100 mm (oq)'>Petlya 100 mm (oq)</option>
                <option value='Krishka Shtulp Dlya Adap 7000 (oq)'>Krishka Shtulp Dlya Adap 7000 (oq)</option>
                <option value='Krishka Shtulp Dlya Adap dvernaya 6000 (13 AKS) (rangli)'>Krishka Shtulp Dlya Adap dvernaya 6000 (13 AKS) (rangli)</option>
                <option value='Ruchka Dvernaya Fornaks (28mm) fiksator (rangli)'>Ruchka Dvernaya Fornaks (28mm) fiksator (rangli)</option>
                <option value='Ruchka Dvernaya Fornaks (35mm) fiksator (rangli)'>Ruchka Dvernaya Fornaks (35mm) fiksator (rangli)</option>
                <option value='Chit-Chit (aldocks).uz (rangli)'>Chit-Chit (aldocks).uz (rangli)</option>
                <option value='Ruchka Okonaya Roto (rangli)'>Ruchka Okonaya Roto (rangli)</option>
                <option value='Petlya 75 mm (rangli)'>Petlya 75 mm (rangli)</option>
                <option value='Soedinitel AKF-106 (36.5mm)'>Soedinitel AKF-106 (36.5mm)</option>
                <option value='Soedinitel 114 D 300 (13,2 mm)'>Soedinitel 114 D 300 (13,2 mm)</option>
                <option value='Soedinitel JP2002 (40mm)'>Soedinitel JP2002 (40mm)</option>
                <option value='Ruchka Kvadrat Mini (rangli)'>Ruchka Kvadrat Mini (rangli)</option>
                <option value='Shpingalet (oq)'>Shpingalet (oq)</option>
                <option value='Krishka Shtulp Dlya Adap dvernaya 6000 (13 AKS) (oq)'>Krishka Shtulp Dlya Adap dvernaya 6000 (13 AKS) (oq)</option>
                <option value='Krishka Shtulp Dlya Adap 7000 (rangli)'>Krishka Shtulp Dlya Adap 7000 (rangli)</option>
                <option value='(A0286) Petlya (Chempion) (rangli)'>(A0286) Petlya (Chempion) (rangli)</option>
                <option value='Otvetka 155 (oq)'>Otvetka 155 (oq)</option>
                <option value='(A0286) Petlya (Chempion) (oq)'>(A0286) Petlya (Chempion) (oq)</option>
                <option value='BKT 70 Soed. Impost (J01-66.6mm)'>BKT 70 Soed. Impost (J01-66.6mm)</option>
                <option value='Petlya Dvernaya MDF (oq)'>Petlya Dvernaya MDF (oq)</option>
                <option value='Petlya Dvernaya MDF (rangli)'>Petlya Dvernaya MDF (rangli)</option>
                <option value='Petlya Dvernaya PVH (rangli)'>Petlya Dvernaya PVH (rangli)</option>
                <option value='Soedinitel A 00018 (21mm)'>Soedinitel A 00018 (21mm)</option>
                <option value='Soedinitel CL.X.W 14 (18mm)'>Soedinitel CL.X.W 14 (18mm)</option>
                <option value='Soedinitel CL.X.W 14 (8mm)'>Soedinitel CL.X.W 14 (8mm)</option>
                <option value='Soedinitel CL.X.W 14 (9mm)'>Soedinitel CL.X.W 14 (9mm)</option>
                <option value='Soedinitel WDT 67 J 02 (44mm)'>Soedinitel WDT 67 J 02 (44mm)</option>
                <option value='Soedinitel CL.X.W 34 (25.6mm)'>Soedinitel CL.X.W 34 (25.6mm)</option>
                <option value='Soedinitel CL.X.W 14 (12.5mm)'>Soedinitel CL.X.W 14 (12.5mm)</option>
                <option value='Petlya Dvernaya 3SK MASTER (rangli)'>Petlya Dvernaya 3SK MASTER (rangli)</option>
                <option value='Klipsa 13mm JP'>Klipsa 13mm JP</option>
                <option value='Zaglushka (PVCC 031) (rangli)'>Zaglushka (PVCC 031) (rangli)</option>
                <option value='Zaglushka (PVCC 032) (rangli)'>Zaglushka (PVCC 032) (rangli)</option>
                <option value='Soedinitel CL.X.W 20 (25.8mm)'>Soedinitel CL.X.W 20 (25.8mm)</option>
                <option value='Krishka Podokonnik 350 (Ovolniy) (rangli)'>Krishka Podokonnik 350 (Ovolniy) (rangli)</option>
                <option value='Soedinitel CL.X.W 34 (17,7mm)'>Soedinitel CL.X.W 34 (17,7mm)</option>
                <option value='Soedinitel CL.X.W 34 (10mm)'>Soedinitel CL.X.W 34 (10mm)</option>
                <option value='Ruchka dvernaya "BELLA" (1000) mm (rangli)'>Ruchka dvernaya "BELLA" (1000) mm (rangli)</option>
                <option value='Petlya dvernaya Jocker (rangli)'>Petlya dvernaya Jocker (rangli)</option>
                <option value='Soedinitel CL.X.W 34 (6mm)'>Soedinitel CL.X.W 34 (6mm)</option>
                <option value='Soedinitel CL.X.W 10 (5mm)'>Soedinitel CL.X.W 10 (5mm)</option>
                <option value='Soedinitel CL.X.W 34 (18mm)'>Soedinitel CL.X.W 34 (18mm)</option>
                <option value='Soedinitel CL.X.W 34 (15,8mm)'>Soedinitel CL.X.W 34 (15,8mm)</option>
                <option value='Soedinitel A 00018 (25 mm)'>Soedinitel A 00018 (25 mm)</option>
                <option value='Petlya dvernaya Jocker (oq)'>Petlya dvernaya Jocker (oq)</option>
                <option value='Ruchka Dvernaya mini (rangli)'>Ruchka Dvernaya mini (rangli)</option>
                <option value='Ruchka Dvernaya Fornaks (30mm) (rangli)'>Ruchka Dvernaya Fornaks (30mm) (rangli)</option>
                <option value='Soedinitel WDT 67 J 03 (44mm)'>Soedinitel WDT 67 J 03 (44mm)</option>
                <option value='Soedinitel 114 D 300 (10mm)'>Soedinitel 114 D 300 (10mm)</option>
                <option value='Soedinitel 114 D 400 (14mm)'>Soedinitel 114 D 400 (14mm)</option>
                <option value='Soedinitel CL.X.W 10 (14mm)'>Soedinitel CL.X.W 10 (14mm)</option>
                <option value='Krishka Podokonnik 300 (Trapetsiya) (rangli)'>Krishka Podokonnik 300 (Trapetsiya) (rangli)</option>
                <option value='Soedinitel 148х125хх (60mm)'>Soedinitel 148х125хх (60mm)</option>
                <option value='Soedinitel CL.X.W 16 (10.8mm)'>Soedinitel CL.X.W 16 (10.8mm)</option>
                <option value='Soedinitel FST 50 JR 001 (30mm)'>Soedinitel FST 50 JR 001 (30mm)</option>
                <option value='Soedinitel FST 50 G 003 (100 mm)'>Soedinitel FST 50 G 003 (100 mm)</option>
                <option value='Soedinitel CL.X.W 40 (7.4mm)'>Soedinitel CL.X.W 40 (7.4mm)</option>
                <option value='Soedinitel 8000'>Soedinitel 8000</option>
                <option value='Soedinitel CL.X.W 20 (20,7mm)'>Soedinitel CL.X.W 20 (20,7mm)</option>
                <option value='Soedinitel CL.X.W 20 (20,6mm)'>Soedinitel CL.X.W 20 (20,6mm)</option>
                <option value='Soedinitel OP.40.J04 L=10mm'>Soedinitel OP.40.J04 L=10mm</option>
                <option value='Soedinitel CL.X.W 34 (7,4mm)'>Soedinitel CL.X.W 34 (7,4mm)</option>
                <option value='Ruchka dvernaya "BELLA" (800) mm (rangli)'>Ruchka dvernaya "BELLA" (800) mm (rangli)</option>
                <option value='Soedinitel CL.X.W 40 (5mm)'>Soedinitel CL.X.W 40 (5mm)</option>
                <option value='Ruchka dvernaya "BELLA" (2000) mm (oq)'>Ruchka dvernaya "BELLA" (2000) mm (oq)</option>
                <option value='Ruchka Dvernaya (28mm) Slim fiksator (rangli)'>Ruchka Dvernaya (28mm) Slim fiksator (rangli)</option>
                <option value='Soedinitel CL.X.W 40 (19mm)'>Soedinitel CL.X.W 40 (19mm)</option>
                <option value='Ruchka dvernaya "BELLA" (1800) mm (rangli)'>Ruchka dvernaya "BELLA" (1800) mm (rangli)</option>
                <option value='Soedinitel CLSW 16'>Soedinitel CLSW 16</option>
                <option value='Soedinitel CL.X.W 40 (18.9mm)'>Soedinitel CL.X.W 40 (18.9mm)</option>
                <option value='Soedinitel 148х125хх (90mm)'>Soedinitel 148х125хх (90mm)</option>
                <option value='BKT 70 Soed. List (A10-001)'>BKT 70 Soed. List (A10-001)</option>
                <option value='Soedinitel CL.X.W 40 (19.6mm)'>Soedinitel CL.X.W 40 (19.6mm)</option>
                <option value='Soedinitel AKF-106 (44mm)'>Soedinitel AKF-106 (44mm)</option>
                <option value='Soedinitel AKF-107 (37mm)'>Soedinitel AKF-107 (37mm)</option>
                <option value='Soedinitel 7000 ECO'>Soedinitel 7000 ECO</option>
                <option value='Ruchka dvernaya "Comfort" (oq)'>Ruchka dvernaya "Comfort" (oq)</option>
                <option value='Soedinitel 148х125хх (140mm)'>Soedinitel 148х125хх (140mm)</option>
                <option value='Soedinitel BKH-010 (38mm)'>Soedinitel BKH-010 (38mm)</option>
                <option value='Ruchka Dvernaya (28mm) Slim (rangli)'>Ruchka Dvernaya (28mm) Slim (rangli)</option>
                <option value='Ruchka dvernaya "Comfort" (rangli)'>Ruchka dvernaya "Comfort" (rangli)</option>
                <option value='Soedinitel BKH-010 (56mm)'>Soedinitel BKH-010 (56mm)</option>
                <option value='Soedinitel CLSW 12'>Soedinitel CLSW 12</option>
                <option value='Ruchka dvernaya "BELLA" (1500) mm (rangli)'>Ruchka dvernaya "BELLA" (1500) mm (rangli)</option>
                <option value='Soedinitel FST 50 G 004 (100 mm)'>Soedinitel FST 50 G 004 (100 mm)</option>
                <option value='Ruchka Okonnaya PVH (rangli)'>Ruchka Okonnaya PVH (rangli)</option>
                <option value='Soedinitel 110049 (20mm)'>Soedinitel 110049 (20mm)</option>
                <option value='Soedinitel 110048 (20mm)'>Soedinitel 110048 (20mm)</option>
                <option value='Soedinitel CL.X.W 38 (28.7mm)'>Soedinitel CL.X.W 38 (28.7mm)</option>
                <option value='Soedinitel FST 50 JR 001 (33mm)'>Soedinitel FST 50 JR 001 (33mm)</option>
                <option value='Soedinitel FST 50 JR 001 (97,5mm)'>Soedinitel FST 50 JR 001 (97,5mm)</option>
                <option value='Ruchka Dvernaya (28mm) Slim (oq)'>Ruchka Dvernaya (28mm) Slim (oq)</option>
                <option value='Zaglushka (PVCC 033) (rangli)'>Zaglushka (PVCC 033) (rangli)</option>
                <option value='Zaglushka (PVCC 036) (rangli)'>Zaglushka (PVCC 036) (rangli)</option>
                <option value='Soedinitel moskitnoy setki (rangli)'>Soedinitel moskitnoy setki (rangli)</option>
                <option value='Ruchka dvernaya "BELLA" (700) mm (oq)'>Ruchka dvernaya "BELLA" (700) mm (oq)</option>
                <option value='Soedinitel CL.X.W 14 (43.5mm)'>Soedinitel CL.X.W 14 (43.5mm)</option>
                <option value='Soedinitel A 00018 (44mm)'>Soedinitel A 00018 (44mm)</option>
                <option value='Ruchka Elegant (oq)'>Ruchka Elegant (oq)</option>
                <option value='Krishka Shtulp Dlya Adap 6000 (rangli)'>Krishka Shtulp Dlya Adap 6000 (rangli)</option>
                <option value='Ruchka Dvernaya Fornaks (30mm) fiksator (rangli)'>Ruchka Dvernaya Fornaks (30mm) fiksator (rangli)</option>
                <option value='Krishka Shtulp Dlya Adap 8000 (rangli)'>Krishka Shtulp Dlya Adap 8000 (rangli)</option>
                <option value='Soedinitel CL.X.W 20 (25.6mm)'>Soedinitel CL.X.W 20 (25.6mm)</option>
                <option value='BKT 70 Soed. W 01 (1=5)'>BKT 70 Soed. W 01 (1=5)</option>
                <option value='Soedinitel moskitnoy setki (oq)'>Soedinitel moskitnoy setki (oq)</option>
                <option value='Замок для профиля москитной сетки серии 10х20цветной'>Замок для профиля москитной сетки серии 10х20цветной</option>
                <option value='Замок для профиля москитной сетки серии 10х20'>Замок для профиля москитной сетки серии 10х20</option>
                <option value='Soedinitel CLSW 0243'>Soedinitel CLSW 0243</option>
                <option value='Klipsa 10.5 mm'>Klipsa 10.5 mm</option>
                <option value='BKT 70 Soed. Impost (J01-26.3mm)'>BKT 70 Soed. Impost (J01-26.3mm)</option>
                <option value='BKT 70 Soed. Impost (J02-23.6mm)'>BKT 70 Soed. Impost (J02-23.6mm)</option>
                <option value='BKT 70 Soed. Impost (J06-13.6mm)'>BKT 70 Soed. Impost (J06-13.6mm)</option>
                <option value='BKT 70 Soed. Impost (J06-23.6mm)'>BKT 70 Soed. Impost (J06-23.6mm)</option>
                <option value='BKT 70 Soed. W 01 (1=18.4)'>BKT 70 Soed. W 01 (1=18.4)</option>
                <option value='BKT 70 Soed. W 01 (1=26.3)'>BKT 70 Soed. W 01 (1=26.3)</option>
                <option value='BKT 70 Soed. W 01 (1=26.8)'>BKT 70 Soed. W 01 (1=26.8)</option>
                <option value='BKT 70 Soed. W 01 (1=7.8)'>BKT 70 Soed. W 01 (1=7.8)</option>
                <option value='BKT 78 Soed. (M11227-19.5mm)'>BKT 78 Soed. (M11227-19.5mm)</option>
                <option value='BKT 70 Soed. W 01 (1=10.8)'>BKT 70 Soed. W 01 (1=10.8)</option>
                <option value='BKT 70 Soed. W 02 (1=10.8)'>BKT 70 Soed. W 02 (1=10.8)</option>
                <option value='BKT 70 Soed. W 02 (1=23.6)'>BKT 70 Soed. W 02 (1=23.6)</option>
                <option value='BKT 70 Soed. W 03 (1=7.8)'>BKT 70 Soed. W 03 (1=7.8)</option>
                <option value='BKT 70 Soed. W 03 (1=10.8)'>BKT 70 Soed. W 03 (1=10.8)</option>
                <option value='BKT 70 Soed. (M11535-7.8mm)'>BKT 70 Soed. (M11535-7.8mm)</option>
                <option value='BKT 70 Soed. Impost (J01-13.6mm)'>BKT 70 Soed. Impost (J01-13.6mm)</option>
                <option value='BKT 70 Soed. W 02 (1=18.4)'>BKT 70 Soed. W 02 (1=18.4)</option>
                <option value='BKT 70 Soed. (M11055-13.6mm)'>BKT 70 Soed. (M11055-13.6mm)</option>
                <option value='BKT 70 Soed. Impost (J01-43.6mm)'>BKT 70 Soed. Impost (J01-43.6mm)</option>
                <option value='BKT 70 Soed. Impost (J05-43.6mm)'>BKT 70 Soed. Impost (J05-43.6mm)</option>
                <option value='BKT 78 Soed. (M11227-22.7mm)'>BKT 78 Soed. (M11227-22.7mm)</option>
                <option value='Chit-Chit (aldocks).uz (oq)'>Chit-Chit (aldocks).uz (oq)</option>
                <option value='Klipsa 12 mm'>Klipsa 12 mm</option>
                <option value='BKT 70 Soed. Impost (J05-23.6mm)'>BKT 70 Soed. Impost (J05-23.6mm)</option>
                <option value='Ogranichitel (oq)'>Ogranichitel (oq)</option>
                <option value='Otvetniy Plast. (rangli)'>Otvetniy Plast. (rangli)</option>
                <option value='Otvetniy Plast. (oq)'>Otvetniy Plast. (oq)</option>
                <option value='Petlya Dvernaya Alyumin (oq)'>Petlya Dvernaya Alyumin (oq)</option>
                <option value='Ruchka Kvadrat (oq)'>Ruchka Kvadrat (oq)</option>
                <option value='Soedinitel 114 D 300 (13mm)'>Soedinitel 114 D 300 (13mm)</option>
                <option value='Soedinitel 114 D 300 (6mm)'>Soedinitel 114 D 300 (6mm)</option>
                <option value='Soedinitel 114 D 400 (38mm)'>Soedinitel 114 D 400 (38mm)</option>
                <option value='Soedinitel 114 D 400 (46mm)'>Soedinitel 114 D 400 (46mm)</option>
                <option value='Soedinitel BKH-001 (6mm)'>Soedinitel BKH-001 (6mm)</option>
                <option value='Soedinitel BKH-002 (38mm)'>Soedinitel BKH-002 (38mm)</option>
                <option value='Soedinitel (Inja)'>Soedinitel (Inja)</option>
                <option value='Zashyolka Narujnyaya (new) (oq)'>Zashyolka Narujnyaya (new) (oq)</option>
                <option value='Soedinitel (Bolshoy)'>Soedinitel (Bolshoy)</option>
                <option value='Otvetniy Plast. (ALD-2) (rangli)'>Otvetniy Plast. (ALD-2) (rangli)</option>
                <option value='Otvetniy Plast. (ALD-2) (oq)'>Otvetniy Plast. (ALD-2) (oq)</option>
                <option value='BKT 70 Soed. List (A10-002)'>BKT 70 Soed. List (A10-002)</option>
                <option value='Montajnaya Planka 7000 (Metal)'>Montajnaya Planka 7000 (Metal)</option>
                <option value='Petlya (oq)'>Petlya (oq)</option>
                <option value='BKT 78 Soed. (M11227-26.9mm)'>BKT 78 Soed. (M11227-26.9mm)</option>
                <option value='Ruchka LUX Fortuna Mini O (oq)'>Ruchka LUX Fortuna Mini O (oq)</option>
                <option value='BKT 70 Soed. List (A10-003)'>BKT 70 Soed. List (A10-003)</option>
                <option value='Otvetnaya chast zamka A0275-K (155) (oq)'>Otvetnaya chast zamka A0275-K (155) (oq)</option>
                <option value='Soedinitel 114 D 400 (10mm)'>Soedinitel 114 D 400 (10mm)</option>
                <option value='Soedinitel 5505 (35mm)'>Soedinitel 5505 (35mm)</option>
                <option value='Soedinitel BKH-008 (14mm)'>Soedinitel BKH-008 (14mm)</option>
                <option value='Soedinitel BKH-008 (15mm)'>Soedinitel BKH-008 (15mm)</option>
                <option value='Soedinitel BKH-010 (6mm)'>Soedinitel BKH-010 (6mm)</option>
                <option value='Krishka Podokonnik 300 (Trapetsiya) (oq)'>Krishka Podokonnik 300 (Trapetsiya) (oq)</option>
                <option value='Ogranichitel PVH (oq)'>Ogranichitel PVH (oq)</option>
                <option value='Petlya 75 mm (oq)'>Petlya 75 mm (oq)</option>
                <option value='Petlya Dvernaya PVH (oq)'>Petlya Dvernaya PVH (oq)</option>
                <option value='Porog Soedinitel 6000 (1kom.) (L;P) (rangli)'>Porog Soedinitel 6000 (1kom.) (L;P) (rangli)</option>
                <option value='Porog Soedinitel 7000 (1kom.) (L;P) (oq)'>Porog Soedinitel 7000 (1kom.) (L;P) (oq)</option>
                <option value='Krishka Shtulp Dlya Adap 6000 (oq)'>Krishka Shtulp Dlya Adap 6000 (oq)</option>
                <option value='Krishka Podokonnik 300 (oq)'>Krishka Podokonnik 300 (oq)</option>
                <option value='Ruchka Dvernaya Fornaks (35mm) fiksator (oq)'>Ruchka Dvernaya Fornaks (35mm) fiksator (oq)</option>
                <option value='BKT 70 Soed. (M11535-22mm)'>BKT 70 Soed. (M11535-22mm)</option>
                <option value='Ruchka DELFIN (oq)'>Ruchka DELFIN (oq)</option>
                <option value='Zatsepka 5200'>Zatsepka 5200</option>
                <option value='Zatsepka 7000'>Zatsepka 7000</option>
                <option value='Zatsepka 6000'>Zatsepka 6000</option>
                <option value='Ruchka Okonaya Roto (oq)'>Ruchka Okonaya Roto (oq)</option>
                <option value='Ruchka Okonnaya PVH (oq)'>Ruchka Okonnaya PVH (oq)</option>
                <option value='Soedinitel 5200'>Soedinitel 5200</option>
                <option value='Soedinitel 6000 (TRIO)'>Soedinitel 6000 (TRIO)</option>
                <option value='Soedinitel 7000'>Soedinitel 7000</option>
                <option value='Ruchka Dvernaya Fornaks (35mm) (oq)'>Ruchka Dvernaya Fornaks (35mm) (oq)</option>
                <option value='Soedinitel 5800'>Soedinitel 5800</option>
                <option value='Soedinitel CL.X.W 38 (5.5 mm)'>Soedinitel CL.X.W 38 (5.5 mm)</option>
                <option value='Petlya Dvernaya 2SK MASTER (oq)'>Petlya Dvernaya 2SK MASTER (oq)</option>
                <option value='Soedinitel A 00018 (37mm)'>Soedinitel A 00018 (37mm)</option>
                <option value='Soedinitel CL.X.W 14 (40mm)'>Soedinitel CL.X.W 14 (40mm)</option>
                <option value='Ruchka Okonaya Rotto Swing (oq)'>Ruchka Okonaya Rotto Swing (oq)</option>
                <option value='BKT 70 Soed. Impost (J03-23.6mm)'>BKT 70 Soed. Impost (J03-23.6mm)</option>
                <option value='Ruchka Okonaya Rotto Swing (rangli)'>Ruchka Okonaya Rotto Swing (rangli)</option>
                <option value='Soedinitel CL.X.W 10 (27mm)'>Soedinitel CL.X.W 10 (27mm)</option>
                <option value='Soedinitel A 00018 (9mm)'>Soedinitel A 00018 (9mm)</option>
                <option value='Soedinitel A 00018 (25.8mm)'>Soedinitel A 00018 (25.8mm)</option>
                <option value='Soedinitel A 00018 (18mm)'>Soedinitel A 00018 (18mm)</option>
                <option value='Soedinitel CL.X.W 38 (5mm)'>Soedinitel CL.X.W 38 (5mm)</option>
                <option value='Soedinitel CL.X.W 28 (9mm)'>Soedinitel CL.X.W 28 (9mm)</option>
                <option value='Soedinitel CL.X.W 28 (25.8mm)'>Soedinitel CL.X.W 28 (25.8mm)</option>
                <option value='Soedinitel CL.X.W 28 (18mm)'>Soedinitel CL.X.W 28 (18mm)</option>
                <option value='Soedinitel CL.X.W 24 (5mm)'>Soedinitel CL.X.W 24 (5mm)</option>
                <option value='Soedinitel CL.X.W 38 (5.8mm)'>Soedinitel CL.X.W 38 (5.8mm)</option>
                <option value='Soedinitel CL.X.W 38 (6.8mm)'>Soedinitel CL.X.W 38 (6.8mm)</option>
                <option value='Soedinitel CL.X.W 14 (22.5mm)'>Soedinitel CL.X.W 14 (22.5mm)</option>
                <option value='Soedinitel CL.X.W 34 (34.3mm)'>Soedinitel CL.X.W 34 (34.3mm)</option>
                <option value='BKT 70 Soed. Impost (J01-16mm)'>BKT 70 Soed. Impost (J01-16mm)</option>
                <option value='Soedinitel CL.X.W 05 (13mm)'>Soedinitel CL.X.W 05 (13mm)</option>
                <option value='Soedinitel CL.X.W 20 (27mm)'>Soedinitel CL.X.W 20 (27mm)</option>
                <option value='Soedinitel CL.X.W 20 (18,8mm)'>Soedinitel CL.X.W 20 (18,8mm)</option>
                <option value='Soedinitel CL.X.W 20 (6mm)'>Soedinitel CL.X.W 20 (6mm)</option>
                <option value='Soedinitel CL.X.W 34 (18,8mm)'>Soedinitel CL.X.W 34 (18,8mm)</option>
                <option value='BKT 70 Soed. Impost (J01-23.6mm)'>BKT 70 Soed. Impost (J01-23.6mm)</option>
                <option value='Ruchka Dvernaya Fornaks (30mm) (oq)'>Ruchka Dvernaya Fornaks (30mm) (oq)</option>
                <option value='Ruchka Dvernaya mini (oq)'>Ruchka Dvernaya mini (oq)</option>
                <option value='Ruchka dvernaya "BELLA" (2250) mm (rangli)'>Ruchka dvernaya "BELLA" (2250) mm (rangli)</option>
                <option value='Otvetka Mini 153 (oq)'>Otvetka Mini 153 (oq)</option>
                <option value='Soedinitel CL.X.W 14 (6mm)'>Soedinitel CL.X.W 14 (6mm)</option>
                <option value='Soedinitel CLSW 22'>Soedinitel CLSW 22</option>
                <option value='Ruchka "Simple" (oq)'>Ruchka "Simple" (oq)</option>
                <option value='Soedinitel CL.X.W 10 (18,8mm)'>Soedinitel CL.X.W 10 (18,8mm)</option>
                <option value='Soedinitel CL.X.W 10 (6mm)'>Soedinitel CL.X.W 10 (6mm)</option>
                <option value='Ruchka "Simple"(rangli)'>Ruchka "Simple"(rangli)</option>
                <option value='Vstavka (PVCC 005) (rangli)'>Vstavka (PVCC 005) (rangli)</option>
                <option value='Zaglushka (PVCC 002) (rangli)'>Zaglushka (PVCC 002) (rangli)</option>
                <option value='Soedinitel (PVCC 022)'>Soedinitel (PVCC 022)</option>
                <option value='Krishka (PVCC 001) (rangli)'>Krishka (PVCC 001) (rangli)</option>
                <option value='Termo vstavka (PVCC 003) (rangli)'>Termo vstavka (PVCC 003) (rangli)</option>
                <option value='Termo vstavka (PVCC 004) (rangli)'>Termo vstavka (PVCC 004) (rangli)</option>
                <option value='Ruchka Dvernaya Fornaks (30mm) fiksator (oq)'>Ruchka Dvernaya Fornaks (30mm) fiksator (oq)</option>
                <option value='Soedinitel CL.X.W 10 (17mm)'>Soedinitel CL.X.W 10 (17mm)</option>
                <option value='Zaglushka (PVCC 035) (rangli)'>Zaglushka (PVCC 035) (rangli)</option>
                <option value='Ruchka dvernaya "BELLA" (750) mm (rangli)'>Ruchka dvernaya "BELLA" (750) mm (rangli)</option>
                <option value='Soedinitel CL.X.W 38 (44.4mm)'>Soedinitel CL.X.W 38 (44.4mm)</option>
                <option value='Soedinitel CL.X.W 16 (44.4mm)'>Soedinitel CL.X.W 16 (44.4mm)</option>
                <option value='Ruchka dvernaya "BELLA" (500) mm (rangli)'>Ruchka dvernaya "BELLA" (500) mm (rangli)</option>
                <option value='Krishka Podokonnik 350 (Ovolniy) (oq)'>Krishka Podokonnik 350 (Ovolniy) (oq)</option>
                <option value='Soedinitel CL.X.W 14 (21.5mm)'>Soedinitel CL.X.W 14 (21.5mm)</option>
                <option value='Ruchka dvernaya "BELLA" (2350) mm (rangli)'>Ruchka dvernaya "BELLA" (2350) mm (rangli)</option>
                <option value='Zaglushka (PVCC 034) (rangli)'>Zaglushka (PVCC 034) (rangli)</option>
                <option value='Ruchka dvernaya "BELLA" (2000) mm (rangli)'>Ruchka dvernaya "BELLA" (2000) mm (rangli)</option>
                <option value='Soedinitel CL.X.W 34 (28.7mm)'>Soedinitel CL.X.W 34 (28.7mm)</option>
                <option value='Ruchka dvernaya "BELLA" (1200) mm (rangli)'>Ruchka dvernaya "BELLA" (1200) mm (rangli)</option>
                <option value='Ruchka Dvernaya (28mm) Slim fiksator (oq)'>Ruchka Dvernaya (28mm) Slim fiksator (oq)</option>
                <option value='BKT 70 Soed. W 02 (1=25.8)'>BKT 70 Soed. W 02 (1=25.8)</option>
                <option value='Derjatel i ruchka-koltso dlya moskitnoy setki (rangli)'>Derjatel i ruchka-koltso dlya moskitnoy setki (rangli)</option>
                <option value='Ручка к конструкции москитной сетки серии 10х20. "AKBULUT" цветной'>Ручка к конструкции москитной сетки серии 10х20. "AKBULUT" цветной</option>
                <option value='Ручка к конструкции москитной сетки серии 10х20 "AKBULUT"белый'>Ручка к конструкции москитной сетки серии 10х20 "AKBULUT"белый</option>
                <option value='Ruchka dvernaya "BELLA" (2300) mm (rangli)'>Ruchka dvernaya "BELLA" (2300) mm (rangli)</option>
                <option value='Takos PVH'>Takos PVH</option>
                <option value='BKT 70 Soed. W 02 (1=26.3)'>BKT 70 Soed. W 02 (1=26.3)</option>
                <option value='BKT 70 Soed. W 02 (1=5.1)'>BKT 70 Soed. W 02 (1=5.1)</option>
                <option value='BKT 70 Soed. W 03 (1=18.4)'>BKT 70 Soed. W 03 (1=18.4)</option>
                <option value='BKT 70 Soed. W 03 (1=26.3)'>BKT 70 Soed. W 03 (1=26.3)</option>
                <option value='BKT 70 Soed. W 03 (1=5.1)'>BKT 70 Soed. W 03 (1=5.1)</option>
                <option value='Derjatel i ruchka-koltso dlya moskitnoy setki (oq)'>Derjatel i ruchka-koltso dlya moskitnoy setki (oq)</option>
                <option value='BKT 70 Soed. Impost (J03-13.6mm)'>BKT 70 Soed. Impost (J03-13.6mm)</option>
                <option value='Porog Soedinitel 6000 (1kom.) (L;P) (oq)'>Porog Soedinitel 6000 (1kom.) (L;P) (oq)</option>
                <option value='Montajnaya Planka 6000 (Metal)'>Montajnaya Planka 6000 (Metal)</option>
                <option value='BKT 70 Soed. Impost (J05-13.6mm)'>BKT 70 Soed. Impost (J05-13.6mm)</option>
                <option value='Soedinitel BKH-010 (42mm)'>Soedinitel BKH-010 (42mm)</option>
                <option value='Ruchka Dvernaya Fornaks (28mm) (oq)'>Ruchka Dvernaya Fornaks (28mm) (oq)</option>
                <option value='Otvetnaya chast zamka A0275-K (153) (oq)'>Otvetnaya chast zamka A0275-K (153) (oq)</option>
                <option value='Soedinitel CL.X.W 14 (25.8mm)'>Soedinitel CL.X.W 14 (25.8mm)</option>
                <option value='Soedinitel 114 D 300 (35mm)'>Soedinitel 114 D 300 (35mm)</option>
                <option value='Ruchka Dvernaya Fornaks (28mm) fiksator (oq)'>Ruchka Dvernaya Fornaks (28mm) fiksator (oq)</option>
                <option value='BKT 70 Soed. (M11535-18.4mm)'>BKT 70 Soed. (M11535-18.4mm)</option>
                <option value='Soedinitel CL.X.W 10 (10mm)'>Soedinitel CL.X.W 10 (10mm)</option>
                <option value='Soedinitel CL.X.W 20 (20mm)'>Soedinitel CL.X.W 20 (20mm)</option>
                <option value='EPDM L-65 угловой соединитель для уплотнителей'>EPDM L-65 угловой соединитель для уплотнителей</option>
                <option value='EPDM заглушка для штульпа "Чемпион"'>EPDM заглушка для штульпа "Чемпион"</option>
                <option value='EPDM адаптер крышка для Термо 78'>EPDM адаптер крышка для Термо 78</option>
                <option value='EPDM А01 105 угловой соединитель для уплотнителей'>EPDM А01 105 угловой соединитель для уплотнителей</option>
                <option value='EPDM ССЕР 0057 адаптер крышка'>EPDM ССЕР 0057 адаптер крышка</option>
                <option value='EPDM ССЕР 0058 адаптер крышка'>EPDM ССЕР 0058 адаптер крышка</option>
                <option value='EPDM D 017500 Decor Zaglushka'>EPDM D 017500 Decor Zaglushka</option>
                <option value='EPDM адаптер крышка для Термо 70 (BKT-70)'>EPDM адаптер крышка для Термо 70 (BKT-70)</option>
                <option value='EPDM крышка для штульпа АК-40'>EPDM крышка для штульпа АК-40</option>
                <option value='EPDM адаптер крышка 012'>EPDM адаптер крышка 012</option>
                <option value='EPDM epdc 004 дренажный носик'>EPDM epdc 004 дренажный носик</option>
                <option value='EPDM 5108 угловой соединитель для уплотнителей'>EPDM 5108 угловой соединитель для уплотнителей</option>
                <option value='Термоуплотненный окрашенный алюминиевый профиль'>Термоуплотненный окрашенный алюминиевый профиль</option>
                <option value='Неокрашенный алюминиевый профиль (N)'>Неокрашенный алюминиевый профиль (N)</option>
                <option value='Алюминиевый профиль (N)'>Алюминиевый профиль (N)</option>
                <option value='EPDM уплотнитель'>EPDM уплотнитель</option>
                <option value='Анодированный алюминиевый профиль (N)'>Анодированный алюминиевый профиль (N)</option>
                <option value='Термоуплотненный алюминиевый профиль (N)'>Термоуплотненный алюминиевый профиль (N)</option>
                <option value='Мебельный профиль из алюминия анодированный матовое серебро (N)'>Мебельный профиль из алюминия анодированный матовое серебро (N)</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;display:none" id='buxgalter_uchot`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option  value="Штука">Штука</div>
                <option  value="Килограмм">Килограмм</div>
                <option  value="Квадратный метр">Квадратный метр</div>
                <option  value="Метр">Метр</div>
                <option  value="КМП">КМП</div>
                <option  value="Пачка">Пачка</div>
                <option  value="Секция">Секция</div>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;" id='bazoviy_edin`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option vlaue="Штука">Штука</div>
                <option vlaue="Килограмм">Килограмм</div>
                <option vlaue="Квадратный метр">Квадратный метр</div>
                <option vlaue="Метр">Метр</div>
                <option vlaue="КМП">КМП</div>
                <option vlaue="Пачка">Пачка</div>
                <option vlaue="Секция">Секция</div>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;display:none" id='alter_edin`+ String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option vlaue="Штука">Штука</div>
                <option vlaue="Килограмм">Килограмм</div>
                <option vlaue="Квадратный метр">Квадратный метр</div>
                <option vlaue="Метр">Метр</div>
                <option vlaue="КМП">КМП</div>
                <option vlaue="Пачка">Пачка</div>
                <option vlaue="Секция">Секция</div>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;" id='status`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="Активный">Активный</option>
                <option value="Пассивный">Пассивный</option>
            </select>
            </div>
        </td>
        <td >
            
            <span class =' text-center ' style="font-size: small; width:190px; font-weight: bold; text-transform: uppercase;" id='zavod_name`+String(i)+`'>ZAVOD ALUCOBOND</span>
            
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 75px; font-size:10px;display:none;height:32px " id='diller`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;" id='tip_clenta`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="AKFA">AKFA</option>
                <option value="IMZO">IMZO</option>
                <option value="FRANCHISING">FRANCHISING</option>
                <option value="AKFA-IMZO-FRANCHISING">AKFA-IMZO-FRANCHISING</option>
                <option value="IMZO-FRANCHISING">IMZO-FRANCHISING</option>
            </select>
            </div>
        </td>
        <td style="display: none;" >
            <div class="input-group input-group-sm mb-1">
            <span id="is_active`+String(i)+`" style="display: none;"></span>
            </div>
        </td>
        
        </tr>`
    }



    
    var table = $('#table-artikul')
    table.append(text)




    for (let i = sizeee + 1; i < sizeee+2; i++) {
        $('#artikul'+String(i)).select2({
            ajax: {
                url: "/client/imzo-artikul-list",
                dataType: 'json',
                processResults: function(data){
                    return {results: $.map(data, function(item){
                        return {id:item.id,text:item.artikul,system:item.system,combination:item.combination,code_nakleyka:item.code_nakleyka}
                    })
                };
                }
            }
            });
        
        
        
        var artikulSelect = $('#artikul'+String(i));
        $.ajax({
            type: 'GET',
            url: "/client/imzo-artikul-list"
        }).then(function (data) {
            var option = new Option(data.artikul, data.id, true, true);
            artikulSelect.append(option).trigger('change');
        
            artikulSelect.trigger({
                type: 'select2:select',
                params: {
                    data: data
                }
            });
        });
        
        
        $("#artikul"+String(i)).on("select2:select", function (e) { 
        var select_val = $(e.currentTarget).val();
        console.log(select_val)
        var nazvaniye_system =$('.nazvaniye_system'+String(i));
        var combination = $('#combination'+String(i));
        var tip_pokritiya = $('#tip_pokritiya'+String(i));
        // tip_pokritiya.val('').change();
        console.log(tip_pokritiya)
        if(select_val!=''){

            tip_pokritiya.attr("disabled",false);
            
        }
        nazvaniye_system.text(e.params.data.system);
        combination.text(e.params.data.combination)

        var nakleyka_kode = e.params.data.code_nakleyka
        
        
        
        
        
        var nakleyka_nt1 = $('#nakleyka_nt'+String(i))
        var nakleyka_org =$('#nakleyka_org'+String(i));
        var nakleyka_select = $('#nakleyka_select'+String(i));

        var length = $('#length'+String(i));
        length.attr('required',true)
        var splav = $('#splav'+String(i));
        splav.attr('required',true)
        var tip_zakalyonnosti = $('#tip_zakalyonnosti'+String(i));
        tip_zakalyonnosti.attr('required',true)

        nakleyka_org.text("")
        if (nakleyka_kode =='NT1'){
            nakleyka_nt1.css('display','block')
            nakleyka_org.css('display','none')
            nakleyka_select.css('display','none')
        }
        else if( nakleyka_kode !=''){
            nakleyka_org.text(nakleyka_kode)
            nakleyka_nt1.css('display','none')
            nakleyka_org.css('display','block')
            nakleyka_select.css('display','none')
        }        
        else{
            nakleyka_nt1.css('display','none')
            nakleyka_org.css('display','none')
            nakleyka_select.css('display','block')
            nakleyka_select.attr('required',true)
            get_nakleyka(String(i))
        }
        
        
        
        // console.log(e.params.data.system)
        });

    }
    // clear_artikul(sizeee + 1);
}






