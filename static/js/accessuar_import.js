class BasePokritiya{
    constructor(
        full=false,
        id=NaN,
        artikul=NaN,
        group_tovarov=NaN,
        categoriya=NaN,
        nazvaniye_materiala=NaN,
        bei=NaN,
        aei=NaN,
        koefitsiyent=NaN,
        sap_code=NaN,
        pickupdate=NaN,
        sena_c_nds=NaN,
        sena_bez_nds=NaN,
        edizm =NaN,
        online_id=NaN,
        nazvaniye_ruchnoy=NaN,
        svet_product=NaN,
        group_zakup=NaN,
        group=NaN,
        tip=NaN,
        segment=NaN,
        bazoviy_edin=NaN,
        alter_edin=NaN,
        stoimost_baza=NaN,
        stoimost_alter=NaN,
        status_online=NaN,
        zavod=NaN,
        tip_clenta=NaN,
        comment=NaN,
        is_active=false,
        ) {
      
        this.full=full;
        this.id=id;
        this.artikul=artikul;
        this.group_tovarov=group_tovarov;
        this.categoriya=categoriya;
        this.nazvaniye_materiala=nazvaniye_materiala;
        this.bei=bei;
        this.aei=aei;
        this.koefitsiyent=koefitsiyent;
        this.sap_code=sap_code;

        this.pickupdate=pickupdate;
        this.sena_c_nds=sena_c_nds;
        this.sena_bez_nds=sena_bez_nds;
        this.edizm=edizm;

        this.online_id=online_id;
        this.nazvaniye_ruchnoy=nazvaniye_ruchnoy;
        this.svet_product=svet_product;
        this.group_zakup=group_zakup;
        this.group=group;
        this.tip=tip;
        this.segment=segment;
        this.bazoviy_edin=bazoviy_edin;
        this.alter_edin=alter_edin;
        this.stoimost_baza=stoimost_baza;
        this.stoimost_alter=stoimost_alter;
        this.status_online=status_online;
        this.zavod=zavod;
        this.tip_clenta=tip_clenta;
        this.comment=comment;
        this.is_active=is_active;
    }
    get_kratkiy_tekst(){
            switch(this.id){
                case 1: if(this.is_active){
                    if (this.group_tovarov && this.categoriya && this.nazvaniye_materiala && this.svet_product&& this.bei&&  this.online_id && this.nazvaniye_ruchnoy){
                        
                        return {'text':'','accept':true}
                    }else{
                        return {'text':'','accept':false}
                    }
                    
                    }else{
                        if (this.group_tovarov && this.categoriya && this.nazvaniye_materiala && this.svet_product&& this.bei &&  this.tip_clenta && this.zavod &&this.sena_c_nds &&this.sena_bez_nds && this.pickupdate && this.nazvaniye_ruchnoy && this.svet_product_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online){
        
                            return {'text':'','accept':true}
                        }else{
                            return {'text':'','accept':false}
                        }
                    }break;
                }
        }
  }





function front_piece(start=1,end=6){
    text =""

    for (let i = start; i < end; i++) {
        text +=`
        <tr id='table_tr` +String(i)+`' style='padding-bottom:0!important;margin-bottom:0!important;'>                   
        <td class="sticky-col"   style='left:0; padding-right:5px; background-color:white!important;' >
                    <div class="btn-group" role="group" aria-label="Basic example">
                            <button type="button" class="btn btn-outline-secondary btn-sm" id='clear_btn`+String(i)+`' onclick="artukil_clear(`+String(i)+`)" data-bs-toggle='popover' title='Yangi sozdaniya qilish uchun ishlatiladi'><i class="bi bi-x-circle"></i></button>
                            <button type="button" class="btn btn-outline-secondary btn-sm"  onclick="copy_tr(`+String(i)+`)" data-bs-toggle='popover' title='Yangi sozdaniya qilish uchun ishlatiladi'><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-copy" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M4 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 5a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-1h1v1a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h1v1z"/></svg></button>
                            <button type="button" class="btn btn-outline-secondary btn-sm" id='create_btn`+String(i)+`' onclick="create(`+String(i)+`)" data-bs-toggle='popover' title='Yangi sozdaniya qilish uchun ishlatiladi' style='font-size:16px; width:34px'>С</button>
                            <button type="button" class="btn btn-outline-secondary btn-sm" id='activate_btn`+String(i)+`' onclick="activate(`+String(i)+`)" data-bs-toggle='popover' title='Activatsiya qilish uchun ishlatiladi' style='font-size:16px;width:34px'>А</button>
                    </div>      
        </td>

        <td class="sticky-col" style=' left: 139.6px;background-color:white!important;width:100px!important'>
            <div class="input-group input-group-sm mb-1">
            <div><span  id ='artikul` +String(i)+`'style="font-weight:600;text-transform: uppercase;white-space: nowrap!important;font-size: 12px;z-index:0"></span></div>
            </div>
        </td>
        <td >
            <div id='group_tovarov_select`+String(i)+`'  style='display:none;'>
                <select class ='form-select' id='group_tovarov`+String(i)+`'  style='text-transform: uppercase; padding-left:35%;height:27px!important;z-index:0;border-color:red' onchange="create_kratkiy_tekst(`+String(i)+`)" data-placeholder="..."></select>
            </div>
        </td>
        
        <td >
            <div id='categoriya_select`+String(i)+`'  style='display:none;'>
                <select class ='form-select' id='categoriya`+String(i)+`'  style='text-transform: uppercase; padding-left:35%;height:27px!important;z-index:0;border-color:red' onchange="create_kratkiy_tekst(`+String(i)+`)" data-placeholder="..."></select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 200px; font-size:10px;display:none;height:27px;z-index:0 " id='nazvaniye_materiala`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)' maxlength="40"></input>
            </div>
        </td>

         
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;border-color:red;display:none;z-index:0" id='bei`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option  value="Штука">Штука</div>
                <option  value="Килограмм">Килограмм</div>
                <option  value="Квадратный метр">Квадратный метр</div>
                <option  value="Метр">Метр</div>
                <option  value="КМП">КМП</div>
                <option  value="Пачка">Пачка</div>
                <option  value="Секция">Секция</div>
                <option  value="Коробка">Коробка</div>
                <option  value="Грам">Грам</div>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;display:none;z-index:0" id='aei`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option  value="Штука">Штука</div>
                <option  value="Килограмм">Килограмм</div>
                <option  value="Квадратный метр">Квадратный метр</div>
                <option  value="Метр">Метр</div>
                <option  value="КМП">КМП</div>
                <option  value="Пачка">Пачка</div>
                <option  value="Секция">Секция</div>
                <option  value="Коробка">Коробка</div>
                <option  value="Грам">Грам</div>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 75px; font-size:10px;display:none;height:27px;z-index:0 " id='koefitsiyent`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 75px; font-size:10px;display:none;height:27px;z-index:0 " id='sap_code`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
        <input  style='display:none;border-color:red; line-height:15px;z-index:0;height:27px;' type="date" class="form-control" id="pickupdate`+String(i)+`" onchange='create_kratkiy_tekst(`+String(i)+`)'> 
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px;display:none;height:27px;z-index:0 " id='sena_c_nds`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px;display:none;height:27px;z-index:0 " id='sena_bez_nds`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0" id='edizm`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option vlaue="Штука">Штука</div>
                <option vlaue="Килограмм">Килограмм</div>
                <option vlaue="Квадратный метр">Квадратный метр</div>
                <option vlaue="Метр">Метр</div>
                <option vlaue="КМП">КМП</div>
                <option vlaue="Пачка">Пачка</div>
                <option vlaue="Секция">Секция</div>
                <option  value="Коробка">Коробка</div>
                <option  value="Грам">Грам</div>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px;display:none;height:27px;z-index:0 " id='online_id`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type='text' class=" form-control " style="border-color:red; width: 250px; font-size:10px; height:27px!important;z-index:0;display:none;"  id='nazvaniye_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
            
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 110px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0"  id='svet_product`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option   value="LAM">LAM</option>
            <option   value="Anod">Anod</option>
            <option   value="COLOUR">COLOUR</option>
            <option   value="VAKUM &amp; 3D">VAKUM &amp; 3D</option>
            <option   value="WHITE">WHITE</option>
            <option   value="Без цвета">Без цвета</option>
        </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 230px;text-transform: uppercase; font-size:12px; padding-right:0px;  border-color:red;display:none;z-index:0" id='group_zakup`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option value="RADIATORI (IMPORT)">RADIATORI (IMPORT)</option>
            <option value="Aksessuar Import">Aksessuar Import</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1"  >
            <select class="form-select" aria-label="" id='group`+String(i)+`' style="width: 240px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0"    onchange='create_kratkiy_tekst(`+String(i)+`)'required>
                <option  selected></option>
                <option value="Alu. AKSESSUAR (TR)">Alu. AKSESSUAR (TR)</option>
                <option value="Alu. AKSESSUAR (TR) ALUTEX">Alu. AKSESSUAR (TR) ALUTEX</option>
                <option value="Alu. ALUMIN (OQ JP TURKEY)">Alu. ALUMIN (OQ JP TURKEY)</option>
                <option value="Avt. AKSESSUAR AVTO.GARAJ">Avt. AKSESSUAR AVTO.GARAJ</option>
                <option value="Avt. AKSESSUAR RUCHNOY. GARAJ">Avt. AKSESSUAR RUCHNOY. GARAJ</option>
                <option value="Pvc. AKSESSUAR (TR)">Pvc. AKSESSUAR (TR)</option>
                <option value="Pvc. Dvoy.Otk. ACCADO">Pvc. Dvoy.Otk. ACCADO</option>
                <option value="Pvc. Dvoy.Otk. EURO_JET">Pvc. Dvoy.Otk. EURO_JET</option>
                <option value="Pvc. Dvoy.Otk. FORNAX">Pvc. Dvoy.Otk. FORNAX</option>
                <option value="Pvc. Dvoy.Otk. KIN LONG">Pvc. Dvoy.Otk. KIN LONG</option>
                <option value="Pvc. Dvoy.Otk. ROTO">Pvc. Dvoy.Otk. ROTO</option>
                <option value="Pvc. Dvoy.Otk. SIEGENIA">Pvc. Dvoy.Otk. SIEGENIA</option>
                <option value="Pvc. Dvoy.Otk. UNIJET">Pvc. Dvoy.Otk. UNIJET</option>
                <option value="Pvc. FAB & FIX Aksessuar">Pvc. FAB & FIX Aksessuar</option>
                <option value="Pvc. STUBLINA">Pvc. STUBLINA</option>
                <option value="STANOK_CHAX">STANOK_CHAX</option>
                <option value="STANOK">STANOK</option>
                <option value="STANOK_ZAPCHASTI">STANOK_ZAPCHASTI</option>
                <option value="T. MASTER">T. MASTER</option>
                <option value="Alu. AKSESSUAR (SlideMaster)">Alu. AKSESSUAR (SlideMaster)</option>
                <option value="Alu. AKSESSUAR (Markiza)">Alu. AKSESSUAR (Markiza)</option>
                <option value="Alu. AKSESSUAR (Gilyotina)">Alu. AKSESSUAR (Gilyotina)</option>
                <option value="Alu. AKSESSUAR (Perilla)">Alu. AKSESSUAR (Perilla)</option>
                <option value="Alu. AKSESSUAR (Jaluzi)">Alu. AKSESSUAR (Jaluzi)</option>
                <option value="GENERATOR">GENERATOR</option>
                <option value="Pvc. Dvoy.Otk. WINKHAUS">Pvc. Dvoy.Otk. WINKHAUS</option>
                <option value="Alu. AKSESSUAR PENA (TR)">Alu. AKSESSUAR PENA (TR)</option>
                <option value="Alu. AKSESSUAR (Polycon)">Alu. AKSESSUAR (Polycon)</option>
                <option value="Alu. AKSESSUAR (Pergola)">Alu. AKSESSUAR (Pergola)</option>
                <option value="TIOKOL (TR)">TIOKOL (TR)</option>
                <option value="Alu. AKSESSUAR (BKS)">Alu. AKSESSUAR (BKS)</option>
                <option value="Avt. SEKSIONNIE VOROTO">Avt. SEKSIONNIE VOROTO</option>
                <option value="ALUCOBOND">ALUCOBOND</option>
                <option value="Bez Nakleyka">Bez Nakleyka</option>
                <option value="Bez Nakleyka TR">Bez Nakleyka TR</option>
                <option value="EKO KABINA">EKO KABINA</option>
                <option value="GRANULA">GRANULA</option>
                <option value="KOTEL">KOTEL</option>
                <option value="KOTEL (AIRFEL)">KOTEL (AIRFEL)</option>
                <option value="KOTEL (AKFA)">KOTEL (AKFA)</option>
                <option value="KOTEL (AKFA) GOST AAA">KOTEL (AKFA) GOST AAA</option>
                <option value="KOTEL (FAHRENEIT)">KOTEL (FAHRENEIT)</option>
                <option value="KOTEL AKSSESSUAR">KOTEL AKSSESSUAR</option>
                <option value="KOTEL (AIRFEL) AKSESSUAR">KOTEL (AIRFEL) AKSESSUAR</option>
                <option value="KOTEL (AKFA) AKSESSUAR">KOTEL (AKFA) AKSESSUAR</option>
                <option value="RADIATORI (IMPORT)">RADIATORI (IMPORT)</option>
                <option value="RADIATORI PANEL (IMPORT)">RADIATORI PANEL (IMPORT)</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0"  id='tip`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)'required>
                <option  ></option>
                <option value="Готовый продукт" selected>Готовый продукт</option>
                <option value="Сырье">Сырье</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 145px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;z-index:0" id='segment`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  ></option>
                <option value="Аксессуар" selected >Аксессуар</option>
            </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0" id='bazoviy_edin`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option vlaue="Штука">Штука</div>
                <option vlaue="Килограмм">Килограмм</div>
                <option vlaue="Квадратный метр">Квадратный метр</div>
                <option vlaue="Метр">Метр</div>
                <option vlaue="КМП">КМП</div>
                <option vlaue="Пачка">Пачка</div>
                <option vlaue="Секция">Секция</div>
                <option  value="Коробка">Коробка</div>
                <option  value="Грам">Грам</div>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;display:none;z-index:0" id='alter_edin`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option vlaue="Штука">Штука</div>
                <option vlaue="Килограмм">Килограмм</div>
                <option vlaue="Квадратный метр">Квадратный метр</div>
                <option vlaue="Метр">Метр</div>
                <option vlaue="КМП">КМП</div>
                <option vlaue="Пачка">Пачка</div>
                <option vlaue="Секция">Секция</div>
                <option  value="Коробка">Коробка</div>
                <option  value="Грам">Грам</div>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 75px; font-size:10px; display:none;height:27px;z-index:0" id='stoimost_baza`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)' ></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 75px; font-size:10px; display:none;height:27px;z-index:0" id='stoimost_alter`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)' ></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0" id='status`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="Активный">Активный</option>
                <option value="Пассивный">Пассивный</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0" id='zavod_name`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="IMPORT" >IMPORT</option>
                <option value="IMPORT Airfel"  >IMPORT Airfel</option>
            </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0" id='tip_clenta`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="AKFA">AKFA</option>
                <option value="IMZO">IMZO</option>
                <option value="Q-Q">Q-Q</option>
                <option value="FRANCHISING">FRANCHISING</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type='text' class=" form-control " style=" width: 250px; font-size:10px; height:27px!important;z-index:0"  id='comment`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
            
        </td>
        <td style="display: none;" >
            <div class="input-group input-group-sm mb-1">
            <span id="is_active`+String(i)+`" style="display: none;"></span>
            </div>
        </td>
        
        </tr>`
    }
    return text
}

text = front_piece()


var table = $('#table-artikul')

table.append(text)


function removeQuotesFromStartAndEnd(str) {
    // Remove double quotes from the beginning and end of the string
    return str.replace(/^"+|"+$/g, '');
}

data_base = {}


function copy_tr(id){
    if(!data_base[id]){
        console.log('salom2222 copy')
    }else{
        
        text =""
        var size = $('#table-artikul tr').length;
        text = front_piece(start = size+1, end = size+2)
        var table = $('#table_tr'+id)
        var new_tr =$(text)

        table.after(new_tr)
        
        
        var data = new BasePokritiya()
        for(key in data_base[id]){
            data[key] = data_base[id][key]
        }
            
        

        

        data_base[size+1] = data
        
        var s = size+1

        var artikul = data.artikul;
        var group_tovarov = data.group_tovarov;
        var categoriya = data.categoriya;
        var nazvaniye_materiala = data.nazvaniye_materiala;
        var svet = data.svet;
        var bei = data.bei;
        var aei = data.aei;
        var koefitsiyent = data.koefitsiyent;
        var sap_code = data.sap_code;


        var pickupdate = data.pickupdate;
        var sena_c_nds = data.sena_c_nds;
        var sena_bez_nds = data.sena_bez_nds;
        var edizm = data.edizm;
        var online_id = data.online_id;
        var nazvaniye_ruchnoy = data.nazvaniye_ruchnoy;
        var svet_product = data.svet_product;
        var group_zakup = data.group_zakup;
        var group = data.group;
        var tip = data.tip;
        var segment = data.segment;
        var bazoviy_edin = data.bazoviy_edin;
        var alter_edin = data.alter_edin;
        var stoimost_baza = data.stoimost_baza;
        var stoimost_alter = data.stoimost_alter;
        var status_online = data.status_online;
        var zavod = data.zavod;
        var tip_clenta = data.tip_clenta;
        var is_active = data.is_active;
        var comment = data.comment;
        
        var activate_btn =$('#activate_btn'+s);
        var create_btn =$('#create_btn'+s);
        activate_btn.attr('disabled',true)
        create_btn.attr('disabled',true)
        
        
        
        check_text_and_change(artikul,'#artikul'+s)
        $('#categoriya_select'+s).css('display','block')
        $('#group_tovarov_select'+s).css('display','block')
        console.log(categoriya,category_list,'llllll')
        set_val_category(category_list,'#categoriya'+s,val=categoriya)
        set_val_group(group_product_list,'#group_tovarov'+s,val=group_tovarov)

        check_input_and_change(nazvaniye_materiala,'#nazvaniye_materiala'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(svet,'#svet'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(bei,'#bei'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(aei,'#aei'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(koefitsiyent,'#koefitsiyent'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(sap_code,'#sap_code'+s,dis=false,is_req=false,is_req_simple=true)

        if(!is_active){
            create_btn.css('background-color','green')
            create_btn.css('color','white')
            $('#is_active'+s).text('')
            check_input_and_change(pickupdate,'#pickupdate'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(sena_c_nds,'#sena_c_nds'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(sena_bez_nds,'#sena_bez_nds'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(edizm,'#edizm'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(online_id,'#online_id'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(svet_product,'#svet_product'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(group_zakup,'#group_zakup'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(group,'#group'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(tip,'#tip'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(segment,'#segment'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(bazoviy_edin,'#bazoviy_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(alter_edin,'#alter_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_baza,'#stoimost_baza'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_alter,'#stoimost_alter'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(status_online,'#status'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(zavod,'#zavod_name'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(tip_clenta,'#tip_clenta'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(comment,'#tip_clenta'+s,dis=false,is_req=false,is_req_simple=true)
            }
        else{
            activate_btn.css('background-color','orange')
            activate_btn.css('color','white')
            $('#is_active'+s).text('Активный')
            check_input_and_change(pickupdate,'#pickupdate'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sena_c_nds,'#sena_c_nds'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(edizm,'#edizm'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sena_bez_nds,'#sena_bez_nds'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(online_id,'#online_id'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(svet_product,'#svet_product'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(group_zakup,'#group_zakup'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(group,'#group'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip,'#tip'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(segment,'#segment'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(bazoviy_edin,'#bazoviy_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(alter_edin,'#alter_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_baza,'#stoimost_baza'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_alter,'#stoimost_alter'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(status_online,'#status'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(zavod,'#zavod_name'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip_clenta,'#tip_clenta'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(comment,'#tip_clenta'+s,dis=false,is_req=false,is_req_simple=true)

        }


        
      
        
        
        
    }


}



function check_input_and_change(val,selector,dis=false,is_req=false,is_req_simple=false){
    if(is_req){
        
        // $(selector).attr('disabled',false)
        $(selector).css('display','block')
        $(selector).css('border-color','red')

    }
    if(is_req_simple){
        
        // $(selector).attr('disabled',false)
        $(selector).css('display','block')
        $(selector).css('border-color','#dedad9')

    }
    if(val !=NaN && val !='' && String(val) != 'NaN'){
        var sel = $(selector)
        // sel.attr('disabled',dis)
        sel.css('display','block')
        sel.css('border-color','#dedad9')
        sel.val(val)
        // console.log(val,typeof(val),selector)
    }
    
}

function check_text_and_change(val,selector){
    if(val !=NaN && val !='' && String(val) != 'NaN'){
        var sel = $(selector)
        sel.css('display','block')
        sel.text(val)
    }
}


function create(id){

    data_base[id] = new BasePokritiya()
    data_base[id].id = 1;
    var status_first =$('#status'+id);
    status_first.val('Активный')

    var is_active =$('#is_active'+id);
    is_active.text('Пассивный')

    var tip =$('#tip'+id);
    tip.val('Готовый продукт')
    

    var activate_btn =$('#activate_btn'+id);
    var create_btn =$('#create_btn'+id);
    create_btn.css('background-color','green')
    create_btn.css('color','white')
    activate_btn.attr('disabled',true)
    create_btn.attr('disabled',true)


    var group_tovarov =$('#group_tovarov_select'+id);
    var categoriya =$('#categoriya_select'+id);

    var nazvaniye_materiala =$('#nazvaniye_materiala'+id);
    var svet =$('#svet'+id);
    var bei =$('#bei'+id);
    var aei =$('#aei'+id);
    var koefitsiyent =$('#koefitsiyent'+id);
    var sap_code =$('#sap_code'+id);
    
    var pickupdate =$('#pickupdate'+id);
    var sena_c_nds =$('#sena_c_nds'+id);
    var sena_bez_nds =$('#sena_bez_nds'+id);

    var edizm =$('#edizm'+id);

    var online_savdo_id =$('#online_id'+id);
    var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);
    var svet_product =$('#svet_product'+id);
    var group_zakup =$('#group_zakup'+id);
    var group =$('#group'+id);
    var tip =$('#tip'+id);
    var segment =$('#segment'+id);
    var bazoviy_edin =$('#bazoviy_edin'+id);
    var alter_edin =$('#alter_edin'+id);
    var stoimost_baza =$('#stoimost_baza'+id);
    var stoimost_alter =$('#stoimost_alter'+id);
    var status =$('#status'+id);
    var zavod_name =$('#zavod_name'+id);
    var tip_clenta =$('#tip_clenta'+id);
    var comment =$('#comment'+id);

    
    
    comment.css('display','block')
    pickupdate.css('display','block')
    sena_c_nds.css('display','block')
    sena_bez_nds.css('display','block')
    group_tovarov.css('display','block')
    categoriya.css('display','block')
    nazvaniye_materiala.css('display','block')
    svet.css('display','block')
    bei.css('display','block')
    aei.css('display','block')
    koefitsiyent.css('display','block')
    sap_code.css('display','block')
    edizm.css('display','block')
    
    
    
    
    bazoviy_edin.val('Штука')
    alter_edin.val('Килограмм')
    stoimost_baza.val('1')
    
    

    zavod_name.css('display','block')
    tip_clenta.css('display','block')
    online_savdo_id.css('display','block')
    nazvaniye_ruchnoy.css('display','block')
    svet_product.css('display','block')
    group_zakup.css('display','block')
    group.css('display','block')
    tip.css('display','block')
    bazoviy_edin.css('display','block')
    status.css('display','block')
    alter_edin.css('display','block')
    stoimost_baza.css('display','block')
    stoimost_alter.css('display','block')
    segment.css('display','block')
    
    svet_product.val('')
    tip.val('Готовый продукт')
    group_zakup.val('')
    status.val('Активный')
    // status.attr('disabled',true)

    online_savdo_id.css('border-color','#dedad9')
    // tip_clenta.css('border-color','#dedad9')
    tip.css('border-color','#dedad9')
    bazoviy_edin.css('border-color','#dedad9')
    status.css('border-color','#dedad9')

    set_val_category(category_list,'#categoriya'+id,val='')
    set_val_group(group_product_list,'#group_tovarov'+id,val='')
   

}

function activate(id){
    // data_base[i] = new OnlineSavdo()

    data_base[id] = new BasePokritiya()
    data_base[id].id = 1;

    var activate_btn =$('#activate_btn'+id);
    var create_btn =$('#create_btn'+id);
    activate_btn.css('background-color','orange')
    activate_btn.css('color','white')
    activate_btn.attr('disabled',true)
    create_btn.attr('disabled',true)



    var status_first =$('#status'+id);
    status_first.val('Активный')

    var is_active =$('#is_active'+id);
    is_active.text('Активный')

   
   
        
    var svet_product =$('#svet_product'+id);
    
    
    data_base[id].is_active=true

    var group_tovarov =$('#group_tovarov_select'+id);
    var categoriya =$('#categoriya_select'+id);
    var nazvaniye_materiala =$('#nazvaniye_materiala'+id);
    var svet =$('#svet'+id);
    var bei =$('#bei'+id);
    var aei =$('#aei'+id);
    var koefitsiyent =$('#koefitsiyent'+id);
    var sap_code =$('#sap_code'+id);
    
    var pickupdate =$('#pickupdate'+id);
    var sena_c_nds =$('#sena_c_nds'+id);
    var sena_bez_nds =$('#sena_bez_nds'+id);

    var edizm =$('#edizm'+id);

    var online_savdo_id =$('#online_id'+id);
    var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);
    var svet_product =$('#svet_product'+id);
    var group_zakup =$('#group_zakup'+id);
    var group =$('#group'+id);
    var tip =$('#tip'+id);
    var segment =$('#segment'+id);
    var bazoviy_edin =$('#bazoviy_edin'+id);
    var alter_edin =$('#alter_edin'+id);
    var stoimost_baza =$('#stoimost_baza'+id);
    var stoimost_alter =$('#stoimost_alter'+id);
    var status =$('#status'+id);
    var zavod_name =$('#zavod_name'+id);
    var tip_clenta =$('#tip_clenta'+id);
    var comment =$('#comment'+id);

    comment.css('display','block')
    pickupdate.css('display','block')
    sena_c_nds.css('display','block')
    sena_bez_nds.css('display','block')
    group_tovarov.css('display','block')
    categoriya.css('display','block')
    nazvaniye_materiala.css('display','block')
    svet.css('display','block')
    bei.css('display','block')
    aei.css('display','block')
    koefitsiyent.css('display','block')
    sap_code.css('display','block')
    edizm.css('display','block')
    
    
    zavod_name.css('display','block')
    tip_clenta.css('display','block')
    online_savdo_id.css('display','block')
    nazvaniye_ruchnoy.css('display','block')
    svet_product.css('display','block')
    group_zakup.css('display','block')
    group.css('display','block')
    tip.css('display','block')
    bazoviy_edin.css('display','block')
    status.css('display','block')
    alter_edin.css('display','block')
    stoimost_baza.css('display','block')
    stoimost_alter.css('display','block')
    segment.css('display','block')


    status.val('Активный')
    // status.attr('disabled',true)

    edizm.css('border-color','#dedad9')
    zavod_name.css('border-color','#dedad9')
    tip_clenta.css('border-color','#dedad9')
    svet_product.css('border-color','#dedad9')
    group_zakup.css('border-color','#dedad9')
    group.css('border-color','#dedad9')
    tip.css('border-color','#dedad9')
    bazoviy_edin.css('border-color','#dedad9')
    status.css('border-color','#dedad9')
    alter_edin.css('border-color','#dedad9')
    stoimost_baza.css('border-color','#dedad9')
    stoimost_alter.css('border-color','#dedad9')
    segment.css('border-color','#dedad9')
    comment.css('border-color','#dedad9')
    pickupdate.css('border-color','#dedad9')
    sena_c_nds.css('border-color','#dedad9')
    sena_bez_nds.css('border-color','#dedad9')

    set_val_category(category_list,'#categoriya'+id,val='')
    set_val_group(group_product_list,'#group_tovarov'+id,val='')

}





function artukil_clear(id){
    
    var table_tr =$('#table_tr'+id);
    
    delete data_base[id]

    
    table_tr.css('background-color','white')
    

    var status_first = $('#status'+String(id))
   
    status_first.val('Активный')

    var group_tovarov =$('#group_tovarov_select'+id);
    var categoriya =$('#categoriya_select'+id);
    var artikul =$('#artikul'+id);

    var nazvaniye_materiala =$('#nazvaniye_materiala'+id);
    var svet =$('#svet'+id);
    var bei =$('#bei'+id);
    var aei =$('#aei'+id);
    var koefitsiyent =$('#koefitsiyent'+id);
    var sap_code =$('#sap_code'+id);
    
    var pickupdate =$('#pickupdate'+id);
    var sena_c_nds =$('#sena_c_nds'+id);
    var sena_bez_nds =$('#sena_bez_nds'+id);

    var edizm =$('#edizm'+id);

    var online_savdo_id =$('#online_id'+id);
    var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);
    var svet_product =$('#svet_product'+id);
    var group_zakup =$('#group_zakup'+id);
    var group =$('#group'+id);
    var tip =$('#tip'+id);
    var segment =$('#segment'+id);
    var bazoviy_edin =$('#bazoviy_edin'+id);
    var alter_edin =$('#alter_edin'+id);
    var stoimost_baza =$('#stoimost_baza'+id);
    var stoimost_alter =$('#stoimost_alter'+id);
    var status =$('#status'+id);
    var zavod_name =$('#zavod_name'+id);
    var tip_clenta =$('#tip_clenta'+id);
    var comment =$('#comment'+id);
   
    
    pickupdate.css('display','none')
    sena_c_nds.css('display','none')
    sena_bez_nds.css('display','none')
    group_tovarov.css('display','none')
    categoriya.css('display','none')
    nazvaniye_materiala.css('display','none')
    svet.css('display','none')
    bei.css('display','none')
    aei.css('display','none')
    koefitsiyent.css('display','none')
    sap_code.css('display','none')
    edizm.css('display','none')
    tip_clenta.css('display','none')
    
    


    svet_product.css('display','none')
    group_zakup.css('display','none')
    group.css('display','none')
    tip.css('display','none')
    zavod_name.css('display','none')
    bazoviy_edin.css('display','none')
    status.css('display','none')
    alter_edin.css('display','none')
    stoimost_baza.css('display','none')
    stoimost_alter.css('display','none')
    segment.css('display','none')
    online_savdo_id.css('display','none')
    online_savdo_id.css('border-color','red')
    nazvaniye_ruchnoy.css('display','none')
    nazvaniye_ruchnoy.css('border-color','red')


    nazvaniye_materiala.css('border-color','red')
    svet.css('border-color','red')
    bei.css('border-color','red')
    aei.css('border-color','red')
    koefitsiyent.css('border-color','red')


    svet_product.css('border-color','red')
    group_zakup.css('border-color','red')
    group.css('border-color','red')
    tip.css('border-color','red')
    bazoviy_edin.css('border-color','red')
    status.css('border-color','red')
    zavod_name.css('border-color','red')
    pickupdate.css('border-color','red')
    tip_clenta.css('border-color','red')
    sena_c_nds.css('border-color','red')
    sena_bez_nds.css('border-color','red')

    
    group_tovarov.val('')
    categoriya.val('')
    nazvaniye_materiala.val('')
    svet.val('')
    bei.val('')
    aei.val('')
    koefitsiyent.val('')
    sap_code.val('')
    edizm.val('')

    artikul.text('')
    tip_clenta.val('')
    online_savdo_id.val('')
    nazvaniye_ruchnoy.val('')
    svet_product.val('')
    group_zakup.val('')
    group.val('')
    tip.val('')
    zavod_name.val('')
    bazoviy_edin.val('')
    status.val('Активный')
    sena_c_nds.val('')
    sena_bez_nds.val('')
    alter_edin.val('')
    stoimost_baza.val('')
    stoimost_alter.val('')
    segment.val('')
    comment.val('')
    pickupdate.val('')
    
    
    var create_btn =$('#create_btn'+id);
    var activate_btn =$('#activate_btn'+id);

    activate_btn.attr('disabled',false)
    create_btn.attr('disabled',false)

    activate_btn.css('background-color','')
    activate_btn.css('color','')
    create_btn.css('background-color','')
    create_btn.css('color','')


}


function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
        
       
    
        var artikul =$('#artikul'+id);
        var group_tovarov =$('#group_tovarov'+id);
        var categoriya =$('#categoriya'+id);

        var nazvaniye_materiala =$('#nazvaniye_materiala'+id);
        var svet =$('#svet'+id);
        var bei =$('#bei'+id);
        var aei =$('#aei'+id);
        var koefitsiyent =$('#koefitsiyent'+id);
        var sap_code =$('#sap_code'+id);
        
        var pickupdate =$('#pickupdate'+id);
        var sena_c_nds =$('#sena_c_nds'+id);
        var sena_bez_nds =$('#sena_bez_nds'+id);

        var edizm =$('#edizm'+id);

        var online_savdo_id =$('#online_id'+id);
        var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);
        var svet_product =$('#svet_product'+id);
        var group_zakup =$('#group_zakup'+id);
        var group =$('#group'+id);
        var tip =$('#tip'+id);
        var segment =$('#segment'+id);
        var bazoviy_edin =$('#bazoviy_edin'+id);
        var alter_edin =$('#alter_edin'+id);
        var stoimost_baza =$('#stoimost_baza'+id);
        var stoimost_alter =$('#stoimost_alter'+id);
        var status =$('#status'+id);
        var zavod_name =$('#zavod_name'+id);
        var tip_clenta =$('#tip_clenta'+id);
        var comment =$('#comment'+id);

        if(group_tovarov.val()!=''){
            group_tovarov.css('border-color','#dedad9')
            data_base[id].group_tovarov = group_tovarov.val();
        }else{
            data_base[id].group_tovarov = NaN;
            group_tovarov.css('border-color','red')
        }
        if(categoriya.val()!=''){
            categoriya.css('border-color','#dedad9')
            data_base[id].categoriya = categoriya.val();
        }else{
            data_base[id].categoriya = NaN;
            categoriya.css('border-color','red')
        }
        var group_sel = $('#group_tovarov'+id +' option:selected');
        var categoriya_sel = $('#categoriya'+id +' option:selected');
        console.log(group_tovarov.val())
        if(group_tovarov.val()!='' && group_tovarov.val()!=null && categoriya.val()!='' && categoriya.val()!=null){
            var group_text = group_sel.attr('data-group-tovarov')
            var categoriya_text = categoriya_sel.attr('data-category')
            var artikul_text = 'ACS.'+group_text+'.'+categoriya_text+'-75'
            artikul.text(artikul_text)
            data_base[id].artikul = artikul_text;
        }else{
            artikul.text('')
            data_base[id].artikul = NaN;
        }

        if(nazvaniye_materiala.val()!=''){
            nazvaniye_materiala.css('border-color','#dedad9')
            data_base[id].nazvaniye_materiala = removeQuotesFromStartAndEnd(nazvaniye_materiala.val());
        }else{
            data_base[id].nazvaniye_materiala = NaN;
            nazvaniye_materiala.css('border-color','red')
        }
        if(svet.val()!=''){
            svet.css('border-color','#dedad9')
            data_base[id].svet = svet.val();
        }else{
            data_base[id].svet = NaN;
            svet.css('border-color','red')
        }
        if(bei.val()!=''){
            bei.css('border-color','#dedad9')
            data_base[id].bei = bei.val();
        }else{
            data_base[id].bei = NaN;
            bei.css('border-color','red')
        }
        if(aei.val()!=''){
            aei.css('border-color','#dedad9')
            data_base[id].aei = aei.val();
        }else{
            data_base[id].aei = NaN;
            
        }
        if(koefitsiyent.val()!=''){
            koefitsiyent.css('border-color','#dedad9')
            data_base[id].koefitsiyent = koefitsiyent.val();
        }else{
            data_base[id].koefitsiyent = NaN;
            
        }
        
        if(sap_code.val()!=''){
            data_base[id].sap_code = sap_code.val();
        }else{
            data_base[id].sap_code = NaN;
            
        }






        if(stoimost_alter.val()!=''){
            data_base[id].stoimost_alter = stoimost_alter.val();
        }else{
            data_base[id].stoimost_alter = NaN;
        }
        if(stoimost_baza.val()!=''){
            data_base[id].stoimost_baza = stoimost_baza.val();
        }else{
            data_base[id].stoimost_baza = NaN;
        }
        if(alter_edin.val()!=''){
            data_base[id].alter_edin = alter_edin.val();
        }else{
            data_base[id].alter_edin = NaN;
        }
        
        if(segment.val()!=''){
            data_base[id].segment = segment.val();
        }else{
            data_base[id].segment = NaN;
        }



        var is_active =$('#is_active'+id)
        
        if(is_active.text()=='Активный'){
            if(edizm.val()!=''){
                edizm.css('border-color','#dedad9')
                data_base[id].edizm = edizm.val();
            }else{
                data_base[id].edizm = NaN;
            }
            if(tip_clenta.val()!=''){
                data_base[id].tip_clenta = tip_clenta.val();
                tip_clenta.css('border-color','#dedad9')
            }else{
                tip_clenta.css('border-color','#dedad9')
                data_base[id].tip_clenta = NaN;
            }
            if(sena_c_nds.val()!=''){
                data_base[id].sena_c_nds = sena_c_nds.val();
                sena_c_nds.css('border-color','#dedad9')
            }else{
                data_base[id].sena_c_nds = NaN;
            }
            if(sena_bez_nds.val()!=''){
                data_base[id].sena_bez_nds = sena_bez_nds.val();
                sena_bez_nds.css('border-color','#dedad9')
            }else{
                data_base[id].sena_bez_nds = NaN;
            }
            
            if(pickupdate.val()!=''){
                data_base[id].pickupdate = pickupdate.val();
                pickupdate.css('border-color','#dedad9')
            }else{
                data_base[id].pickupdate = NaN;
            }
            
            if(comment.val()!=''){
                data_base[id].comment = comment.val();
                comment.css('border-color','#dedad9')
            }else{
                data_base[id].comment = NaN;
            }
            
            
            if(online_savdo_id.val()!=''){
                online_savdo_id.css('border-color','#dedad9')
                data_base[id].online_id = online_savdo_id.val();
            }else{
                data_base[id].online_id = NaN;
                online_savdo_id.css('border-color','red')
            }
            if(nazvaniye_ruchnoy.val()!=''){
                nazvaniye_ruchnoy.css('border-color','#dedad9')
                data_base[id].nazvaniye_ruchnoy = nazvaniye_ruchnoy.val();
            }else{
                data_base[id].nazvaniye_ruchnoy =NaN;
                nazvaniye_ruchnoy.css('border-color','red')
            }
    
    
            if(svet_product.val()!=''){
                
                data_base[id].svet_product = svet_product.val();
            }else{
                data_base[id].svet_product =NaN;
               
            }
            if(group_zakup.val()!=''){
                
                data_base[id].group_zakup = group_zakup.val();
            }else{
                data_base[id].group_zakup =NaN;
                
            }
            if(group.val()!=''){
                
                data_base[id].group = group.val();
            }else{
                data_base[id].group =NaN;
                
            }
            if(tip.val()!=''){
                
                data_base[id].tip = tip.val();
            }else{
                data_base[id].tip =NaN;
                
            }
            if(bazoviy_edin.val()!=''){
                
                data_base[id].bazoviy_edin = bazoviy_edin.val();
            }else{
                data_base[id].bazoviy_edin =NaN;
                
            }
            
            if(status.val()!=''){
                
                data_base[id].status_online = status.val();
            }else{
                data_base[id].status_online =NaN;
                
            }
            var zavod_name =$('#zavod_name'+id)
            if(zavod_name.val()!=''){
                data_base[id].zavod = zavod_name.val();
            }else{
                data_base[id].zavod =zavod_name.val();
                
                
            }
        }else{
            if(edizm.val()!=''){
                edizm.css('border-color','#dedad9')
                data_base[id].edizm = edizm.val();
            }else{
                data_base[id].edizm = NaN;
                edizm.css('border-color','red')
            }
            if(tip_clenta.val()!=''){
                data_base[id].tip_clenta = tip_clenta.val();
                tip_clenta.css('border-color','#dedad9')
            }else{
                tip_clenta.css('border-color','red')
                data_base[id].tip_clenta = NaN;
            }
            if(sena_c_nds.val()!=''){
                data_base[id].sena_c_nds = sena_c_nds.val();
                sena_c_nds.css('border-color','#dedad9')
            }else{
                data_base[id].sena_c_nds = NaN;
            }
            if(sena_bez_nds.val()!=''){
                data_base[id].sena_bez_nds = sena_bez_nds.val();
                sena_bez_nds.css('border-color','#dedad9')
            }else{
                data_base[id].sena_bez_nds = NaN;
            }
            if(pickupdate.val()!=''){
                data_base[id].pickupdate = pickupdate.val();
                pickupdate.css('border-color','#dedad9')
            }else{
                pickupdate.css('border-color','red')
                data_base[id].pickupdate = NaN;
            }
            
            if(comment.val()!=''){
                data_base[id].comment = comment.val();
                comment.css('border-color','#dedad9')
            }else{
                data_base[id].comment = NaN;
            }

           
            if(online_savdo_id.val()!=''){
                
                data_base[id].online_id = online_savdo_id.val();
            }else{
                data_base[id].online_id = NaN;
                
            }
            if(nazvaniye_ruchnoy.val()!=''){
                nazvaniye_ruchnoy.css('border-color','#dedad9')
                data_base[id].nazvaniye_ruchnoy = nazvaniye_ruchnoy.val();
            }else{
                data_base[id].nazvaniye_ruchnoy =NaN;
                nazvaniye_ruchnoy.css('border-color','red')
            }
    
    
            if(svet_product.val()!=''){
                svet_product.css('border-color','#dedad9')
                data_base[id].svet_product = svet_product.val();
            }else{
                data_base[id].svet_product =NaN;
                svet_product.css('border-color','red')
            }
            if(group_zakup.val()!=''){
                group_zakup.css('border-color','#dedad9')
                data_base[id].group_zakup = group_zakup.val();
            }else{
                data_base[id].group_zakup =NaN;
                group_zakup.css('border-color','red')
            }
            if(group.val()!=''){
                group.css('border-color','#dedad9')
                data_base[id].group = group.val();
            }else{
                data_base[id].group =NaN;
                group.css('border-color','red')
            }
            if(tip.val()!=''){
                tip.css('border-color','#dedad9')
                data_base[id].tip = tip.val();
            }else{
                data_base[id].tip =NaN;
                tip.css('border-color','red')
            }
            if(bazoviy_edin.val()!=''){
                bazoviy_edin.css('border-color','#dedad9')
                data_base[id].bazoviy_edin = bazoviy_edin.val();
            }else{
                data_base[id].bazoviy_edin =NaN;
                bazoviy_edin.css('border-color','red')
            }
            
            if(status.val()!=''){
                status.css('border-color','#dedad9')
                data_base[id].status_online = status.val();
            }else{
                data_base[id].status_online =NaN;
                status.css('border-color','red')
            }
            var zavod_name =$('#zavod_name'+id)
            if(zavod_name.val()!=''){
                zavod_name.css('border-color','#dedad9')
               
                data_base[id].zavod = zavod_name.val();
            }else{
                data_base[id].zavod =NaN;
                zavod_name.css('border-color','red')
            }

        
        
    }




    



    var data = data_base[id].get_kratkiy_tekst()
    
    if(data.accept){
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','#2de319')
        data_base[id].full =true
    }else{
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','white')
        data_base[id].full =false

    }
    }
}

function add_column(){
        
    text =""
    var sizeee = $('#table-artikul tr').length;
    
    text = front_piece(start = sizeee+1, end = sizeee+2)

    
    var table = $('#table-artikul')
    table.append(text)
    


}




