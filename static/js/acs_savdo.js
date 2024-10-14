class BasePokritiya{
    constructor(
        full=false,//done
        id=NaN, //done
        base_artikul=NaN,
        kratkiy_tekst=NaN,
        gruppa_materialov=NaN,
        bei =NaN,
        aei=NaN,
        koefitsiyent=NaN,
        comment=NaN,
        pickupdate=NaN,//done
        sena_c_nds=NaN,
        sena_bez_nds=NaN,

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
        sistema=NaN,//done
        is_active=false,
        ) {
      
        this.full=full;
        this.id=id;
        this.base_artikul=base_artikul;
        this.kratkiy_tekst=kratkiy_tekst;
        this.gruppa_materialov=gruppa_materialov;
        this.bei=bei;
        this.aei=aei;
        this.koefitsiyent=koefitsiyent;
        this.comment=comment,
        this.pickupdate=pickupdate;
        this.sena_c_nds=sena_c_nds;
        this.sena_bez_nds=sena_bez_nds;
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
        this.sistema=sistema;
        this.is_active=is_active;
    }
    get_kratkiy_tekst(){
            switch(this.id){
                case 1: if(this.is_active){
                    if (this.online_id && this.nazvaniye_ruchnoy&&this.sena_c_nds&&this.sena_bez_nds){
                        
                        return {'text':'','accept':true}
                    }else{
                        return {'text':'','accept':false}
                    }
                    
                    }else{
                        if (this.base_artikul && this.kratkiy_tekst && this.bei && this.tip_clenta && this.zavod &&this.sena_c_nds&&this.sena_bez_nds && this.pickupdate && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.sistema){
        
                            return {'text':'','accept':true}
                        }else{
                            return {'text':'','accept':false}
                        }
                    }break;
                case 2:if(this.is_active){
                    if (this.online_id && this.nazvaniye_ruchnoy&&this.sena_c_nds&&this.sena_bez_nds){
        
                        
                        return {'text':'','accept':true}
                    }else{
                        
                        return {'text':'','accept':false}
                    }
                    
                    }else{
                        
                        if (this.base_artikul && this.kratkiy_tekst && this.bei && this.tip_clenta &&this.zavod &&this.sena_c_nds&&this.sena_bez_nds && this.pickupdate && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online&& this.sistema){
                            
                            
                            return {'text':'','accept':true}
                        }else{
                            
                            return {'text':'','accept':false}
                        }
                    }break;
            }
        }
  }





function front_piece(start=1,end=6){
    var text =""

    for (let i = start; i < end; i++) {
        var buttons =''
        if(status_proccess1 == 'new'){
            buttons=`<td class="sticky-col"   style='left:0; padding-right:5px; background-color:white!important;' >
                    <div class="btn-group" role="group" aria-label="Basic example">
                            <button type="button" class="btn btn-outline-secondary btn-sm" id='clear_btn`+String(i)+`' onclick="artukil_clear(`+String(i)+`)" data-bs-toggle='popover' title='Tozalab tashlash'><i class="bi bi-x-circle"></i></button>
                            <button type="button" class="btn btn-outline-secondary btn-sm"  onclick="copy_tr(`+String(i)+`)" data-bs-toggle='popover' title='Dubl qilish'><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-copy" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M4 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 5a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-1h1v1a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h1v1z"/></svg></button>
                            <button type="button" class="btn btn-outline-secondary btn-sm" id='create_btn`+String(i)+`' onclick="create(`+String(i)+`)" data-bs-toggle='popover' title='Yangi sozdaniya qilish uchun ishlatiladi' style='font-size:16px; width:34px'>С</button>
                            <button type="button" class="btn btn-outline-secondary btn-sm" id='activate_btn`+String(i)+`' onclick="activate(`+String(i)+`)" data-bs-toggle='popover' title='Activatsiya qilish uchun ishlatiladi' style='font-size:16px;width:34px'>А</button>
                    </div>
                    </td>`
        }else{
            buttons=``
        }
        text +=`
        <tr id='table_tr` +String(i)+`' style='padding-bottom:0!important;margin-bottom:0!important;'>                   
        `+buttons+
         `
        <td >
            <div id='div_artikul`+String(i)+`' style='display:none'>
                <select class ='form-select base_artikul_org`+String(i)+`' id='base_artikul`+String(i)+`'  style=' padding-left:35%;height:27px!important;z-index:0;border-color:red' onchange="create_kratkiy_tekst(`+String(i)+`)" data-placeholder="..."></select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 200px; font-size:10px;display:none;height:27px;z-index:0 " id='kratkiy_tekst`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px; display:none;z-index:0"  id='gruppa_materialov`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                    <option  ></option>
                    <option  selected value="ACSUZGP">ACSUZGP</option>
                </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px;border-color:red;display:none;z-index:0" id='bei`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px;display:none;z-index:0" id='aei`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;display:none;height:27px;z-index:0 " id='comment`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>


        <td >
        <input  style='display:none;border-color:red; line-height:15px;z-index:0' type="date" class="form-control" id="pickupdate`+String(i)+`" onchange='create_kratkiy_tekst(`+String(i)+`)'> 
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px;display:none;height:32px;z-index:0 " id='sena_c_nds`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px;display:none;height:32px;z-index:0 " id='sena_bez_nds`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px;display:none;height:32px;z-index:0 " id='online_savdo_id`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type='text' class=" form-control " style="border-color:red; width: 250px; font-size:10px; height:27px!important;z-index:0;display:none;"  id='nazvaniye_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
            
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0"  id='svet_product`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                    <option  selected></option>
                    <option   value="COLOUR">COLOUR</option>
                    <option   value="Без цвета">Без цвета</option>
                </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 230px; font-size:12px; padding-right:0px;  border-color:red;display:none;z-index:0" id='group_zakup`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
            <select class="form-select" aria-label="" id='group`+String(i)+`' style="width: 240px; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0"  id='tipr`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)'required>
                <option  selected></option>
                <option value="Alu. AKSESSUAR (UZ)">Alu. AKSESSUAR (UZ)</option>
                <option value="Pvc. AKSESSUAR (UZ)">Pvc. AKSESSUAR (UZ)</option>
                
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0"  id='tip`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)'required>
                <option  selected></option>
                <option value="Сырье">Сырье</option>
                <option value="Готовый продукт">Готовый продукт</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 145px; font-size:12px; padding-right:0px; display:none;z-index:0" id='segment`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                
                <option value="Аксессуар">Аксессуар</option>
                <option value="Аксессуар 2">Аксессуар 2</option>
                <option value="Аксессуар 3">Аксессуар 3</option>
                
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 520px; font-size:12px; padding-right:0px; display:none;z-index:0" id='buxgalter_tovar`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value='Профиль из ПВХ ламинированный'>Профиль из ПВХ ламинированный</option>
                <option value='Термоуплотненный алюминиевый профиль (N)'>Термоуплотненный алюминиевый профиль (N)</option>
                <option value='Мебельный профиль из алюминия анодированный матовое серебро (N)'>Мебельный профиль из алюминия анодированный матовое серебро (N)</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px;display:none;z-index:0" id='buxgalter_uchot`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0" id='bazoviy_edin`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="Штука">Штука</div>
                <option value="Килограмм">Килограмм</div>
                <option value="Квадратный метр">Квадратный метр</div>
                <option value="Метр">Метр</div>
                <option value="КМП">КМП</div>
                <option value="Пачка">Пачка</div>
                <option value="Секция">Секция</div>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px;display:none;z-index:0" id='alter_edin`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="Штука">Штука</div>
                <option value="Килограмм">Килограмм</div>
                <option value="Квадратный метр">Квадратный метр</div>
                <option value="Метр">Метр</div>
                <option value="КМП">КМП</div>
                <option value="Пачка">Пачка</div>
                <option value="Секция">Секция</div>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 75px; font-size:10px; display:none;height:32px;z-index:0" id='stoimost_baza`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)' ></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 75px; font-size:10px; display:none;height:32px;z-index:0" id='stoimost_alter`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)' ></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0" id='status`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="Активный">Активный</option>
                <option value="Пассивный">Пассивный</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0" id='zavod_name`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="ZAVOD AKS UZ">ZAVOD AKS UZ</option>
                
            </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px; display:none;z-index:0" id='tip_clenta`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  ></option>
                <option selected value="AKFA">AKFA</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 280px;font-size:12px; padding-right:0px; display:none;z-index:0" id='sistema`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected ></option>
                <option  value="Online savdo">Online savdo</option>
                <option  value="Akfa diller">Akfa diller</option>
                <option  value="Akfa diller comfort">Akfa diller comfort</option>
                <option  value="Online savdo - Akfa diller">Online savdo - Akfa diller</option>
                <option  value="Online savdo - Akfa diller comfort">Online savdo - Akfa diller comfort</option>
                <option  value="Akfa diller - Akfa diller comfort">Akfa diller - Akfa diller comfort</option>
                <option  value="Online savdo - Akfa diller - Akfa diller comfort">Online savdo - Akfa diller - Akfa diller comfort</option>


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
    return text
}

function removeQuotesFromStartAndEnd(str) {
    // Remove double quotes from the beginning and end of the string
    return str.replace(/^"+|"+$/g, '');
}

text = front_piece()


var table = $('#table-artikul')

// table.append(text)
data_base = {}

if(status_proccess1 == 'new'){
    table.append(text)
    artikul_list_add()

}else{
    var jsonData = JSON.parse(jsonData);
    // var jsonData ='{{order}}'

    // var ii= 1

    for(var key1 in jsonData){
        data_base[key1] = new BasePokritiya()
        for(var key2 in jsonData[key1]){
            data_base[key1][key2] = jsonData[key1][key2]
        }
        // ii += 1
    }

    console.log(data_base,'daatatatata')

    var text2 =''
    for(var key1 in jsonData){
        // console.log(key1,'lllsdsafasfads')
        text2 += front_piece( parseInt(key1),parseInt(key1)+1)
    }



    var table = $('#table-artikul')

    table.append(text2)

    // var i = 1
    for(key2 in data_base){
        copy_tr(key2,key2)
        // i += 1
    }
}

function artikul_list_add(start=1,end=6){

    for (let i = start; i < end; i++) {
        set_base_artikul(artikul_list,'.base_artikul_org'+i,value='')
    }
}




function copy_tr(id,ii=1){
    if(!data_base[id]){
        console.log('salom2222 copy')
    }else{
        if(status_proccess1 == 'new'){
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
        }else{
            var data = data_base[id]
            var s = ii
            artikul_list_add(start = s, end = s+1)
        }

        var base_artikul = data.base_artikul;
        var kratkiy_tekst = data.kratkiy_tekst;
        var gruppa_materialov = data.gruppa_materialov;
        var bei = data.bei;
        var aei = data.aei;
        var koefitsiyent = data.koefitsiyent;
        var comment = data.comment;
        
        
        var pickupdate = data.pickupdate;
        var sena_c_nds = data.sena_c_nds;
        var sena_bez_nds = data.sena_bez_nds;
        var online_id = data.online_id;
        var nazvaniye_ruchnoy = data.nazvaniye_ruchnoy;
        var svet_product = data.svet_product;
        var group_zakup = data.group_zakup;
        var group = data.group;
        var tip = data.tip;
        var segment = data.segment;
        var buxgalter_tovar = data.buxgalter_tovar;
        var buxgalter_uchot = data.buxgalter_uchot;
        var bazoviy_edin = data.bazoviy_edin;
        var alter_edin = data.alter_edin;
        var stoimost_baza = data.stoimost_baza;
        var stoimost_alter = data.stoimost_alter;
        var status_online = data.status_online;
        var zavod = data.zavod;
        var tip_clenta = data.tip_clenta;
        var sistema = data.sistema;
        var is_active = data.is_active;
        
        var activate_btn =$('#activate_btn'+s);
        var create_btn =$('#create_btn'+s);
        activate_btn.attr('disabled',true)
        create_btn.attr('disabled',true)
        var div_artikul =$('#div_artikul'+s);
        div_artikul.css('display','block')
        
        if(!is_active){
            create_btn.css('background-color','green')
            create_btn.css('color','white')
            $('#is_active'+s).text('')
            set_base_artikul(artikul_list,'.base_artikul_org'+s,value=base_artikul)
            check_input_and_change(kratkiy_tekst,'#kratkiy_tekst'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(gruppa_materialov,'#gruppa_materialov'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(bei,'#bei'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(aei,'#aei'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(koefitsiyent,'#koefitsiyent'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(comment,'#comment'+s,dis=false,is_req=false,is_req_simple=true)

            console.log(sena_c_nds,sena_bez_nds,'bez ndsssss')

            check_input_and_change(pickupdate,'#pickupdate'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(sena_c_nds ,'#sena_c_nds'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(sena_bez_nds ,'#sena_bez_nds'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(online_id,'#online_savdo_id'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(svet_product,'#svet_product'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(group_zakup,'#group_zakup'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(group,'#group'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(tip,'#tip'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(segment,'#segment'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(buxgalter_tovar,'#buxgalter_tovar'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(buxgalter_uchot,'#buxgalter_uchot'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(bazoviy_edin,'#bazoviy_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(alter_edin,'#alter_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_baza,'#stoimost_baza'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_alter,'#stoimost_alter'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(status_online,'#status'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(zavod,'#zavod_name'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(tip_clenta,'#tip_clenta'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sistema,'#sistema'+s,dis=false,is_req=true,is_req_simple=false)
            }
        else{
            activate_btn.css('background-color','orange')
            activate_btn.css('color','white')
            $('#is_active'+s).text('Активный')
            set_base_artikul(artikul_list,'.base_artikul_org'+s,value=base_artikul)
            check_input_and_change(kratkiy_tekst,'#kratkiy_tekst'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(gruppa_materialov,'#gruppa_materialov'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(bei,'#bei'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(aei,'#aei'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(koefitsiyent,'#koefitsiyent'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(comment,'#comment'+s,dis=false,is_req=false,is_req_simple=true)

            check_input_and_change(pickupdate,'#pickupdate'+s,dis=false,is_req=false,is_req_simple=true)
            
            check_input_and_change(sena_c_nds ,'#sena_c_nds'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(sena_bez_nds ,'#sena_bez_nds'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(online_id,'#online_savdo_id'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(svet_product,'#svet_product'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(group_zakup,'#group_zakup'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(group,'#group'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip,'#tip'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(segment,'#segment'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(buxgalter_tovar,'#buxgalter_tovar'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(buxgalter_uchot,'#buxgalter_uchot'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(bazoviy_edin,'#bazoviy_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(alter_edin,'#alter_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_baza,'#stoimost_baza'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_alter,'#stoimost_alter'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(status_online,'#status'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(zavod,'#zavod_name'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip_clenta,'#tip_clenta'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sistema,'#sistema'+s,dis=false,is_req=false,is_req_simple=true)

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

    var zavod_name =$('#zavod_name'+id);
    var tip_clenta =$('#tip_clenta'+id);

    var div_artikul =$('#div_artikul'+id);
    var kratkiy_tekst =$('#kratkiy_tekst'+id);
    var gruppa_materialov =$('#gruppa_materialov'+id);
    var bei =$('#bei'+id);
    var aei =$('#aei'+id);
    var koefitsiyent =$('#koefitsiyent'+id);
    
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
    var sistema =$('#sistema'+id);
    comment.css('display','block')
    obshiy_ves_shtuku.css('display','block')
    pickupdate.css('display','block')
    sena_c_nds.css('display','block')
    sena_bez_nds.css('display','block')
    sistema.css('display','block')
    
    
    
    buxgalter_uchot.val('Килограмм')
    bazoviy_edin.val('Штука')
    alter_edin.val('Килограмм')
    stoimost_baza.val('1')
    
    

    div_artikul.css('display','block')
    kratkiy_tekst.css('display','block')
    gruppa_materialov.css('display','block')
    bei.css('display','block')
    aei.css('display','block')
    koefitsiyent.css('display','block')
    comment.css('display','block')

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
    // tip_clenta.css('border-color','#dedad9')
    tip.css('border-color','#dedad9')
    bazoviy_edin.css('border-color','#dedad9')
    status.css('border-color','#dedad9')
    sistema.css('border-color','red')

        
   

}

function activate(id){
    // data_base[i] = new OnlineSavdo()

    data_base[id] = new BasePokritiya()
    data_base[id].id = 2;

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

    var div_artikul =$('#div_artikul'+id);
    var kratkiy_tekst =$('#kratkiy_tekst'+id);
    var gruppa_materialov =$('#gruppa_materialov'+id);
    var bei =$('#bei'+id);
    var aei =$('#aei'+id);
    var koefitsiyent =$('#koefitsiyent'+id);

  

    var zavod_name =$('#zavod_name'+id);
    var tip_clenta =$('#tip_clenta'+id);

    
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
    var sistema =$('#sistema'+id);
    
    comment.css('display','block')
    pickupdate.css('display','block')
    sena_c_nds.css('display','block')
    sena_bez_nds.css('display','block')
    sistema.css('display','block')
    
    div_artikul.css('display','block')
    kratkiy_tekst.css('display','block')
    gruppa_materialov.css('display','block')
    bei.css('display','block')
    aei.css('display','block')
    koefitsiyent.css('display','block')
    comment.css('display','block')

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

    kratkiy_tekst.css('border-color','#dedad9')
    bei.css('border-color','#dedad9')

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
    sistema.css('border-color','#dedad9')
    // sena_c_nds.css('border-color','#dedad9')
    // sena_bez_nds.css('border-color','#dedad9')

    

}





function artukil_clear(id){
    
    var table_tr =$('#table_tr'+id);
    
    delete data_base[id]

    
    table_tr.css('background-color','white')
    

    var status_first = $('#status'+String(id))
   
    status_first.val('Активный')

    var sap_code_ruchnoy =$('#sap_code_ruchnoy'+id);
    var kratkiy_tekst_ruchnoy =$('#kratkiy_tekst_ruchnoy'+id);

    var online_savdo_id =$('#online_savdo_id'+id);
    var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);

    set_base_artikul(artikul_list,'.base_artikul_org'+id,value='',add=false)

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
    var div_artikul =$('#div_artikul'+id);
    var kratkiy_tekst =$('#kratkiy_tekst'+id);
    var gruppa_materialov =$('#gruppa_materialov'+id);
    var bei =$('#bei'+id);
    var aei =$('#aei'+id);
    var koefitsiyent =$('#koefitsiyent'+id);
    var sena_c_nds =$('#sena_c_nds'+id);
    var sena_bez_nds =$('#sena_bez_nds'+id);
    var sistema =$('#sistema'+id);
    
    div_artikul.css('display','none')
    kratkiy_tekst.css('display','none')
    gruppa_materialov.css('display','none')
    bei.css('display','none')
    aei.css('display','none')
    koefitsiyent.css('display','none')

    comment.css('display','none')
    obshiy_ves_shtuku.css('display','none')
    pickupdate.css('display','none')
    diller.css('display','none')
    tip_clenta.css('display','none')
    sena_c_nds.css('display','none')
    sena_bez_nds.css('display','none')
    sistema.css('display','none')


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

    sena_bez_nds.css('border-color','red')
    sena_c_nds.css('border-color','red')
    sistema.css('border-color','red')

    // base_artikul.css('border-color','red')
    kratkiy_tekst.css('border-color','red')
    // gruppa_materialov.css('border-color','red')
    bei.css('border-color','red')
    // aei.css('border-color','red')
    // koefitsiyent.css('border-color','red')

    

    sena_bez_nds.val('')
    sena_c_nds.val('')
    // base_artikul.val('')
    kratkiy_tekst.val('')
    gruppa_materialov.val('')
    bei.val('')
    aei.val('')
    koefitsiyent.val('')

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
    buxgalter_uchot.val('')
    alter_edin.val('')
    stoimost_baza.val('')
    stoimost_alter.val('')
    segment.val('')
    buxgalter_tovar.val('')
    comment.val('')
    obshiy_ves_shtuku.val('')
    pickupdate.val('')
    sistema.val('')
    
    
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


        var base_artikul =$('#base_artikul'+id)
        var kratkiy_tekst =$('#kratkiy_tekst'+id)
        var gruppa_materialov =$('#gruppa_materialov'+id)
        var bei =$('#bei'+id)
        var aei =$('#aei'+id)
        var koefitsiyent =$('#koefitsiyent'+id)
        var sena_c_nds =$('#sena_c_nds'+id)
        var sena_bez_nds =$('#sena_bez_nds'+id)
        
        
        var is_active =$('#is_active'+id)
        var segment =$('#segment'+id)
        var buxgalter_tovar =$('#buxgalter_tovar'+id)
        var buxgalter_uchot =$('#buxgalter_uchot'+id)
        var alter_edin =$('#alter_edin'+id)
        var stoimost_baza =$('#stoimost_baza'+id)
        var stoimost_alter =$('#stoimost_alter'+id)
        var sistema =$('#sistema'+id)

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

            if(base_artikul.val()!=''){
                data_base[id].base_artikul = base_artikul.val();
                base_artikul.css('border-color','#dedad9')
            }else{
                base_artikul.css('border-color','#dedad9')
                data_base[id].base_artikul = NaN;
            }
            if(kratkiy_tekst.val()!=''){
                data_base[id].kratkiy_tekst = kratkiy_tekst.val();
                kratkiy_tekst.css('border-color','#dedad9')
            }else{
                kratkiy_tekst.css('border-color','#dedad9')
                data_base[id].kratkiy_tekst = NaN;
            }
            if(gruppa_materialov.val()!=''){
                data_base[id].gruppa_materialov = gruppa_materialov.val();
                gruppa_materialov.css('border-color','#dedad9')
            }else{
                gruppa_materialov.css('border-color','#dedad9')
                data_base[id].gruppa_materialov = NaN;
            }
            if(bei.val()!=''){
                data_base[id].bei = bei.val();
                bei.css('border-color','#dedad9')
            }else{
                bei.css('border-color','#dedad9')
                data_base[id].bei = NaN;
            }
            if(aei.val()!=''){
                data_base[id].aei = aei.val();
                aei.css('border-color','#dedad9')
            }else{
                aei.css('border-color','#dedad9')
                data_base[id].aei = NaN;
            }
            if(koefitsiyent.val()!=''){
                data_base[id].koefitsiyent = koefitsiyent.val();
                koefitsiyent.css('border-color','#dedad9')
            }else{
                koefitsiyent.css('border-color','#dedad9')
                data_base[id].koefitsiyent = NaN;
            }

            if(tip_clenta.val()!=''){
                data_base[id].tip_clenta = tip_clenta.val();
                tip_clenta.css('border-color','#dedad9')
            }else{
                tip_clenta.css('border-color','#dedad9')
                data_base[id].tip_clenta = NaN;
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
            if(sistema.val()!=''){
                data_base[id].sistema = sistema.val();
                sistema.css('border-color','#dedad9')
            }else{
                sistema.css('border-color','#dedad9')
                data_base[id].sistema = NaN;
            }
            
            
            if(sena_c_nds.val()!=''){
                sena_c_nds.css('border-color','#dedad9')
                data_base[id].sena_c_nds = sena_c_nds.val();
            }else{
                data_base[id].sena_c_nds = NaN;
                sena_c_nds.css('border-color','red')
            }
            if(sena_bez_nds.val()!=''){
                sena_bez_nds.css('border-color','#dedad9')
                data_base[id].sena_bez_nds = sena_bez_nds.val();
            }else{
                data_base[id].sena_bez_nds = NaN;
                sena_bez_nds.css('border-color','red')
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
                data_base[id].nazvaniye_ruchnoy = removeQuotesFromStartAndEnd(nazvaniye_ruchnoy.val());
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
            
            if(base_artikul.val()!=''){
                data_base[id].base_artikul = base_artikul.val();
                base_artikul.css('border-color','#dedad9')
            }else{
                base_artikul.css('border-color','red')
                data_base[id].base_artikul = NaN;
            }
            if(kratkiy_tekst.val()!=''){
                data_base[id].kratkiy_tekst = kratkiy_tekst.val();
                kratkiy_tekst.css('border-color','#dedad9')
            }else{
                kratkiy_tekst.css('border-color','red')
                data_base[id].kratkiy_tekst = NaN;
            }
            if(gruppa_materialov.val()!=''){
                data_base[id].gruppa_materialov = gruppa_materialov.val();
                gruppa_materialov.css('border-color','#dedad9')
            }else{
                gruppa_materialov.css('border-color','#dedad9')
                data_base[id].gruppa_materialov = NaN;
            }
            if(bei.val()!=''){
                data_base[id].bei = bei.val();
                bei.css('border-color','#dedad9')
            }else{
                bei.css('border-color','red')
                data_base[id].bei = NaN;
            }
            if(aei.val()!=''){
                data_base[id].aei = aei.val();
                aei.css('border-color','#dedad9')
            }else{
                aei.css('border-color','#dedad9')
                data_base[id].aei = NaN;
            }
            if(koefitsiyent.val()!=''){
                data_base[id].koefitsiyent = koefitsiyent.val();
                koefitsiyent.css('border-color','#dedad9')
            }else{
                koefitsiyent.css('border-color','#dedad9')
                data_base[id].koefitsiyent = NaN;
            }
            if(sistema.val()!=''){
                data_base[id].sistema = sistema.val();
                sistema.css('border-color','#dedad9')
            }else{
                sistema.css('border-color','red')
                data_base[id].sistema = NaN;
            }

            if(tip_clenta.val()!=''){
                data_base[id].tip_clenta = tip_clenta.val();
                tip_clenta.css('border-color','#dedad9')
            }else{
                tip_clenta.css('border-color','red')
                data_base[id].tip_clenta = NaN;
            }
            if(sena_c_nds.val()!=''){
                sena_c_nds.css('border-color','#dedad9')
                data_base[id].sena_c_nds = sena_c_nds.val();
            }else{
                data_base[id].sena_c_nds = NaN;
                sena_c_nds.css('border-color','red')
            }
            if(sena_bez_nds.val()!=''){
                sena_bez_nds.css('border-color','#dedad9')
                data_base[id].sena_bez_nds = sena_bez_nds.val();
            }else{
                data_base[id].sena_bez_nds = NaN;
                sena_bez_nds.css('border-color','red')
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




