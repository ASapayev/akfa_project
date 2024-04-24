class BasePokritiya{
    constructor(
        full=false,//done
        id=NaN, //done
        pickupdate=NaN,//done
        sena_za_bei=NaN,//done
        online_id=NaN,//done
        nazvaniye_ruchnoy=NaN,//done
        svet_product=NaN,//done
        group_zakup=NaN,//done
        group=NaN,//done
        tip=NaN,//done
        segment=NaN,//done
        buxgalter_tovar=NaN,//done
        buxgalter_uchot=NaN,//done
        bazoviy_edin=NaN,//done
        alter_edin=NaN,//done
        stoimost_baza=NaN,//done
        stoimost_alter=NaN,//done
        status_online=NaN,//done
        zavod=NaN,//done
        tip_clenta=NaN,//done
        is_active=false,
        ) {
      
        this.full=full;
        this.id=id;
        this.pickupdate=pickupdate;
        this.sena_za_bei=sena_za_bei;
        this.online_id=online_id;
        this.nazvaniye_ruchnoy=nazvaniye_ruchnoy;
        this.svet_product=svet_product;
        this.group_zakup=group_zakup;
        this.group=group;
        this.tip=tip;
        this.segment=segment;
        this.buxgalter_tovar=buxgalter_tovar;
        this.buxgalter_uchot=buxgalter_uchot;
        this.bazoviy_edin=bazoviy_edin;
        this.alter_edin=alter_edin;
        this.stoimost_baza=stoimost_baza;
        this.stoimost_alter=stoimost_alter;
        this.status_online=status_online;
        this.zavod=zavod;
        this.tip_clenta=tip_clenta;
        this.is_active=is_active;
    }
    get_kratkiy_tekst(){
            switch(this.id){
                case 1: if(this.is_active){
                    if (this.online_id && this.nazvaniye_ruchnoy){
                        
                        return {'text':'','accept':true}
                    }else{
                        return {'text':'','accept':false}
                    }
                    
                    }else{
                        if (this.tip_clenta && this.zavod &&this.sena_za_bei && this.pickupdate && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online){
        
                            return {'text':'','accept':true}
                        }else{
                            return {'text':'','accept':false}
                        }
                    }break;
                case 2:if(this.is_active){
                    if (this.online_id && this.nazvaniye_ruchnoy){
        
                        
                        return {'text':'','accept':true}
                    }else{
                        
                        return {'text':'','accept':false}
                    }
                    
                    }else{
                        
                        if (this.tip_clenta &&this.zavod && this.sena_za_bei && this.pickupdate && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online){
                            
                            
                            return {'text':'','accept':true}
                        }else{
                            
                            return {'text':'','accept':false}
                        }
                    }break;
            }
        }
  }



  text =""
  var jsonData = JSON.parse(JSON.parse(document.getElementById('items-data').textContent)).data;
  
  i = 0
  var order_type =$('#order_type').text()
  for (var key in jsonData) {
    i += 1
    text +=`
    <tr id='table_tr` +String(i)+`' >                   
    <td >
    <input  style='display:none;border-color:red; line-height:15px' type="date" class="form-control" id="pickupdate`+String(i)+`" onchange='create_kratkiy_tekst(`+String(i)+`)'> 
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px;display:none;height:32px " id='sena_za_bei`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px;display:none;height:32px " id='online_savdo_id`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <textarea   rows='1' class=" form-control " style="border-color:red; width: 220px; font-size:10px; display:none; height:32px" id='nazvaniye_ruchnoy`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></textarea >
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 110px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;"  id='svet_product`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
        <select class="form-select" aria-label="" style="width: 230px;text-transform: uppercase; font-size:12px; padding-right:0px;  border-color:red;display:none;" id='group_zakup`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
        <option  selected></option>
        <option value="Granit">Granit</option>
        <option value="Radiator SAP (IMPORT)">Radiator SAP (IMPORT)</option>
        <option value="Rezina Tpv">Rezina Tpv</option>
        <option value="Aksessuar Import (SAP)">Aksessuar Import (SAP)</option>
        <option value="Kraska">Kraska</option>
        <option value="Gazoblok">Gazoblok</option>
        <option value="Butilchita">Butilchita</option>
        <option value="Aksessuar Import">Aksessuar Import</option>
        <option value="Aksessuar Rezina">Aksessuar Rezina</option>
        <option value="Aksessuar UZ">Aksessuar UZ</option>
        <option value="Tiokol">Tiokol</option>
        <option value="Metal">Metal</option>
        <option value="Alucobond">Alucobond</option>
        <option value="Radiator">Radiator</option>
        <option value="Kabina">Kabina</option>
        <option value="Granula">Granula</option>
        <option value="Radiator (IMPORT)">Radiator (IMPORT)</option>
        <option value="Kotel (AIRFEL)">Kotel (AIRFEL)</option>
        <option value="Kotel (AKFA)">Kotel (AKFA)</option>
        <option value="VITYAJNOYE USTROYSTVA">VITYAJNOYE USTROYSTVA</option>
        <option value="Setka">Setka</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1"  >
        <select class="form-select" aria-label="" id='group`+String(i)+`' style="width: 240px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;"  id='tipr`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)'required>
            <option  selected></option>
            <option value="5200 QVT PVC (NAVOIY)">5200 QVT PVC (NAVOIY)</option>
            <option value="5200 QVT PVC RETPEN (NAVOIY)">5200 QVT PVC RETPEN (NAVOIY)</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;"  id='tip`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)'required>
            <option  selected></option>
            <option value="Сырье">Сырье</option>
            <option value="Готовый продукт">Готовый продукт</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 145px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;" id='segment`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option value="Aldoks">Aldoks</option>
            <option value="Стандарт">Стандарт</option>
            <option value="Премиум">Премиум</option>
            <option value="Аксессуар">Аксессуар</option>
            <option value="Аксессуар 2">Аксессуар 2</option>
            <option value="Аксессуар 3">Аксессуар 3</option>
            <option value="Falcon">Falcon</option>
            <option value="Эконом">Эконом</option>
            <option value="Mebel">Mebel</option>
            <option value="LAMBRI">LAMBRI</option>
            <option value="RETPEN 10%">RETPEN 10%</option>
            <option value="RETPEN 15%">RETPEN 15%</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 520px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;" id='buxgalter_tovar`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option value='Профиль из ПВХ ламинированный'>Профиль из ПВХ ламинированный</option>
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
        <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;" id='bazoviy_edin`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
        <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;display:none" id='alter_edin`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
        <input type='text' class=" form-control " style="width: 75px; font-size:10px; display:none;height:32px" id='stoimost_baza`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)' ></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="width: 75px; font-size:10px; display:none;height:32px" id='stoimost_alter`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)' ></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;" id='status`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option value="Активный">Активный</option>
            <option value="Пассивный">Пассивный</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;" id='zavod_name`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option value="ZAVOD BUTIL">ZAVOD BUTIL</option>
            <option value="IMPORT">IMPORT</option>
            <option value="ZAVOD REZINA">ZAVOD REZINA</option>
            <option value="ZAVOD AKS UZ">ZAVOD AKS UZ</option>
            <option value="ZAVOD TIOKOL">ZAVOD TIOKOL</option>
            <option value="ZAVOD METAL">ZAVOD METAL</option>
            <option value="ZAVOD ALUCOBOND">ZAVOD ALUCOBOND</option>
            <option value="ZAVOD RADIATOR">ZAVOD RADIATOR</option>
            <option value="Akfa Savdo">Akfa Savdo</option>
            <option value="ZAVOD GRANULA">ZAVOD GRANULA</option>
            <option value="ZAVOD GRANIT">ZAVOD GRANIT</option>
            <option value="РЦ Зенит">РЦ Зенит</option>
            <option value="РЦ Наманган">РЦ Наманган</option>
            <option value="РЦ Бухара">РЦ Бухара</option>
            <option value="РЦ Самарканд">РЦ Самарканд</option>
            <option value="РЦ Хорезм">РЦ Хорезм</option>
            <option value="ZAVOD REZINA TPV">ZAVOD REZINA TPV</option>
            <option value="ZAVOD KRASKA">ZAVOD KRASKA</option>
        </select>
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;" id='tip_clenta`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option value="AKFA">AKFA</option>
            <option value="IMZO">IMZO</option>
            <option value="Q-Q">Q-Q</option>
            <option value="FRANCHISING">FRANCHISING</option>
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





data_base = {}

for(var key1 in jsonData){
    data_base[key1] = new BasePokritiya()
    for(var key2 in jsonData[key1]){
        data_base[key1][key2] = jsonData[key1][key2]
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
    activate_btn.attr('disabled',true)
    var create_btn =$('#create_btn'+id);
    create_btn.attr('disabled',true)

    var zavod_name =$('#zavod_name'+id);
    var tip_clenta =$('#tip_clenta'+id);
    var sena_za_bei =$('#sena_za_bei'+id);
    
    var svet_product =$('#svet_product'+id);
    var online_savdo_id =$('#online_savdo_id'+id);
    var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);
    var svet_product =$('#svet_product'+id);
    var group_zakup =$('#group_zakup'+id);
    var group =$('#group'+id);
    var tip =$('#tip'+id);
    var bazoviy_edin =$('#bazoviy_edin'+id);
    var status =$('#status'+id);
    var zavod =$('#zavod'+id);
    var buxgalter_uchot =$('#buxgalter_uchot'+id);
    var alter_edin =$('#alter_edin'+id);
    var stoimost_baza =$('#stoimost_baza'+id);
    var stoimost_alter =$('#stoimost_alter'+id);
    var segment =$('#segment'+id);
    var buxgalter_tovar =$('#buxgalter_tovar'+id);
    var comment =$('#comment'+id);
    var obshiy_ves_shtuku =$('#obshiy_ves_shtuku'+id);
    var pickupdate =$('#pickupdate'+id);
    var sena_c_nds =$('#sena_c_nds'+id);
    var sena_bez_nds =$('#sena_bez_nds'+id);
    comment.css('display','block')
    obshiy_ves_shtuku.css('display','block')
    pickupdate.css('display','block')
    sena_c_nds.css('display','block')
    sena_bez_nds.css('display','block')
    sena_za_bei.css('display','block')
    
    
    
    buxgalter_uchot.val('Килограмм')
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
    zavod.css('display','block')
    buxgalter_uchot.css('display','block')
    alter_edin.css('display','block')
    stoimost_baza.css('display','block')
    stoimost_alter.css('display','block')
    segment.css('display','block')
    buxgalter_tovar.css('display','block')
    
    svet_product.val('')
    tip.val('Готовый продукт')
    group_zakup.val('')
    status.val('Активный')
    // status.attr('disabled',true)

    online_savdo_id.css('border-color','#dedad9')
    tip_clenta.css('border-color','#dedad9')
    tip.css('border-color','#dedad9')
    bazoviy_edin.css('border-color','#dedad9')
    status.css('border-color','#dedad9')

        
   

}

function activate(id){
    // data_base[i] = new OnlineSavdo()

    data_base[id] = new BasePokritiya()
    data_base[id].id = 2;

    var activate_btn =$('#activate_btn'+id);
    var create_btn =$('#create_btn'+id);
    activate_btn.attr('disabled',true)
    create_btn.attr('disabled',true)
    var status_first =$('#status'+id);
    status_first.val('Активный')

    var is_active =$('#is_active'+id);
    is_active.text('Активный')
   
        
    var svet_product =$('#svet_product'+id);
    
    
    data_base[id].is_active=true

    var zavod_name =$('#zavod_name'+id);
    var tip_clenta =$('#tip_clenta'+id);
    var sena_za_bei =$('#sena_za_bei'+id);

    
    var online_savdo_id =$('#online_savdo_id'+id);
    var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);
    var svet_product =$('#svet_product'+id);
    var group_zakup =$('#group_zakup'+id);
    var group =$('#group'+id);
    var tip =$('#tip'+id);
    var bazoviy_edin =$('#bazoviy_edin'+id);
    var status =$('#status'+id);
    var zavod =$('#zavod'+id);
    var buxgalter_uchot =$('#buxgalter_uchot'+id);
    var alter_edin =$('#alter_edin'+id);
    var stoimost_baza =$('#stoimost_baza'+id);
    var stoimost_alter =$('#stoimost_alter'+id);
    var segment =$('#segment'+id);
    var buxgalter_tovar =$('#buxgalter_tovar'+id);
    var comment =$('#comment'+id);
    var pickupdate =$('#pickupdate'+id);
    var sena_c_nds =$('#sena_c_nds'+id);
    var sena_bez_nds =$('#sena_bez_nds'+id);

    comment.css('display','block')
    pickupdate.css('display','block')
    sena_c_nds.css('display','block')
    sena_bez_nds.css('display','block')
    sena_za_bei.css('display','block')
    
    
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
    zavod.css('display','block')
    buxgalter_uchot.css('display','block')
    alter_edin.css('display','block')
    stoimost_baza.css('display','block')
    stoimost_alter.css('display','block')
    segment.css('display','block')
    buxgalter_tovar.css('display','block')


    status.val('Активный')
    // status.attr('disabled',true)

    sena_za_bei.css('border-color','#dedad9')
    zavod_name.css('border-color','#dedad9')
    tip_clenta.css('border-color','#dedad9')
    svet_product.css('border-color','#dedad9')
    group_zakup.css('border-color','#dedad9')
    group.css('border-color','#dedad9')
    tip.css('border-color','#dedad9')
    bazoviy_edin.css('border-color','#dedad9')
    status.css('border-color','#dedad9')
    zavod.css('border-color','#dedad9')
    buxgalter_uchot.css('border-color','#dedad9')
    alter_edin.css('border-color','#dedad9')
    stoimost_baza.css('border-color','#dedad9')
    stoimost_alter.css('border-color','#dedad9')
    segment.css('border-color','#dedad9')
    buxgalter_tovar.css('border-color','#dedad9')
    comment.css('border-color','#dedad9')
    pickupdate.css('border-color','#dedad9')
    sena_c_nds.css('border-color','#dedad9')
    sena_bez_nds.css('border-color','#dedad9')

    

}




function clear_artikul(id){
    var table_tr =$('#table_tr'+id);
    
    delete data_base[id]

    
    table_tr.css('background-color','white')
    
    
}

function artukil_clear(id){
    
    clear_artikul(id)

    var status_first = $('#status'+String(id))
   
    status_first.val('Активный')

    var sap_code_ruchnoy =$('#sap_code_ruchnoy'+id);
    var kratkiy_tekst_ruchnoy =$('#kratkiy_tekst_ruchnoy'+id);

    var online_savdo_id =$('#online_savdo_id'+id);
    var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);


    var svet_product =$('#svet_product'+id);
    var group_zakup =$('#group_zakup'+id);
    var group =$('#group'+id);
    var tip =$('#tip'+id);
    var bazoviy_edin =$('#bazoviy_edin'+id);
    var status =$('#status'+id);
    var zavod =$('#zavod_name'+id);
    var buxgalter_uchot =$('#buxgalter_uchot'+id);
    var alter_edin =$('#alter_edin'+id);
    var stoimost_baza =$('#stoimost_baza'+id);
    var stoimost_alter =$('#stoimost_alter'+id);
    var segment =$('#segment'+id);
    var buxgalter_tovar =$('#buxgalter_tovar'+id);
    var comment =$('#comment'+id);
    var obshiy_ves_shtuku =$('#obshiy_ves_shtuku'+id);
    var pickupdate =$('#pickupdate'+id);
    var diller =$('#diller'+id);
    var tip_clenta =$('#tip_clenta'+id);
    var sena_za_bei =$('#sena_za_bei'+id);
    
    comment.css('display','none')
    obshiy_ves_shtuku.css('display','none')
    pickupdate.css('display','none')
    diller.css('display','none')
    tip_clenta.css('display','none')
    sena_za_bei.css('display','none')


    svet_product.css('display','none')
    group_zakup.css('display','none')
    group.css('display','none')
    tip.css('display','none')
    bazoviy_edin.css('display','none')
    status.css('display','none')
    zavod.css('display','none')
    buxgalter_uchot.css('display','none')
    alter_edin.css('display','none')
    stoimost_baza.css('display','none')
    stoimost_alter.css('display','none')
    segment.css('display','none')
    buxgalter_tovar.css('display','none')
    sap_code_ruchnoy.css('display','none')
    kratkiy_tekst_ruchnoy.css('display','none')
    online_savdo_id.css('display','none')
    online_savdo_id.css('border-color','red')
    nazvaniye_ruchnoy.css('display','none')
    nazvaniye_ruchnoy.css('border-color','red')


    svet_product.css('border-color','red')
    group_zakup.css('border-color','red')
    group.css('border-color','red')
    tip.css('border-color','red')
    bazoviy_edin.css('border-color','red')
    status.css('border-color','red')
    zavod.css('border-color','red')
    pickupdate.css('border-color','red')
    tip_clenta.css('border-color','red')
    sena_za_bei.css('border-color','red')

    
    diller.val('')
    tip_clenta.val('')
    online_savdo_id.val('')
    nazvaniye_ruchnoy.val('')
    svet_product.val('')
    group_zakup.val('')
    group.val('')
    tip.val('')
    zavod.val('')
    bazoviy_edin.val('')
    status.val('Активный')
    sena_za_bei.val('')
    buxgalter_uchot.val('')
    alter_edin.val('')
    stoimost_baza.val('')
    stoimost_alter.val('')
    segment.val('')
    buxgalter_tovar.val('')
    comment.val('')
    obshiy_ves_shtuku.val('')
    pickupdate.val('')
    
    
    var create_btn =$('#create_btn'+id);
    var activate_btn =$('#activate_btn'+id);

    create_btn.attr('disabled',false)
    activate_btn.attr('disabled',false)



}





function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
    
    
        var online_savdo_id =$('#online_savdo_id'+id);
        var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);
        var svet_product =$('#svet_product'+id);
        var group_zakup =$('#group_zakup'+id);
        var group =$('#group'+id);
        var tip =$('#tip'+id);
        var bazoviy_edin =$('#bazoviy_edin'+id);
        var status =$('#status'+id);
        var zavod =$('#zavod'+id);

        var comment =$('#comment'+id);
        var pickupdate =$('#pickupdate'+id);
        var tip_clenta =$('#tip_clenta'+id)
        var sena_za_bei =$('#sena_za_bei'+id)
        
        
        var is_active =$('#is_active'+id)
        var segment =$('#segment'+id)
        var buxgalter_tovar =$('#buxgalter_tovar'+id)
        var buxgalter_uchot =$('#buxgalter_uchot'+id)
        var alter_edin =$('#alter_edin'+id)
        var stoimost_baza =$('#stoimost_baza'+id)
        var stoimost_alter =$('#stoimost_alter'+id)

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
        if(buxgalter_uchot.val()!=''){
            data_base[id].buxgalter_uchot = buxgalter_uchot.val();
        }else{
            data_base[id].buxgalter_uchot = NaN;
        }
        if(buxgalter_tovar.val()!=''){
            data_base[id].buxgalter_tovar = buxgalter_tovar.val();
        }else{
            data_base[id].buxgalter_tovar = NaN;
        }
        if(segment.val()!=''){
            data_base[id].segment = segment.val();
        }else{
            data_base[id].segment = NaN;
        }




        
        if(is_active.text()=='Активный'){

            if(tip_clenta.val()!=''){
                data_base[id].tip_clenta = tip_clenta.val();
                tip_clenta.css('border-color','#dedad9')
            }else{
                tip_clenta.css('border-color','#dedad9')
                data_base[id].tip_clenta = NaN;
            }
            if(sena_za_bei.val()!=''){
                data_base[id].sena_za_bei = sena_za_bei.val();
                sena_za_bei.css('border-color','#dedad9')
            }else{
                data_base[id].sena_za_bei = NaN;
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
            if(zavod.val()!=''){
                
                var zavod_name =$('#zavod_name'+id)
                zavod_name.text(zavod.val())
                data_base[id].zavod = zavod.val();
            }else{
                var zavod_name =$('#zavod_name'+id)
                zavod_name.text('')
                data_base[id].zavod =NaN;
                
                
            }
        }else{
            if(tip_clenta.val()!=''){
                data_base[id].tip_clenta = tip_clenta.val();
                tip_clenta.css('border-color','#dedad9')
            }else{
                tip_clenta.css('border-color','red')
                data_base[id].tip_clenta = NaN;
            }
            if(sena_za_bei.val()!=''){
                data_base[id].sena_za_bei = sena_za_bei.val();
                sena_za_bei.css('border-color','#dedad9')
            }else{
                sena_za_bei.css('border-color','red')
                data_base[id].sena_za_bei = NaN;
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






