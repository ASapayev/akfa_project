class BasePokritiya{
    constructor(
        id = NaN,//done 
        full = false,//done
        model = NaN,
        base_artikul = NaN,
        kol_section = NaN,
        svet = NaN,
        brend = NaN,
        kratkiy_tekst = NaN,
        comment = NaN,
        pickupdate = NaN,
        sena_c_nds = NaN,
        sena_bez_nds = NaN,

        online_id = NaN,
        nazvaniye_ruchnoy = NaN,
        svet_product = NaN,
        group_zakup = NaN,
        group = NaN,
        tip = NaN,
        segment = NaN,
        buxgalter_tovar = NaN,
        buxgalter_sena = NaN,
        buxgalter_uchot = NaN,
        bazoviy_edin = NaN,
        alter_edin = NaN,
        stoimost_baza = NaN,
        stoimost_alter = NaN,
        status_online = NaN,
        zavod_name = NaN,
        tip_clenta = NaN,
        is_active = false,

        ) {
            this.id = id;//done 
            this.full = full;//done
            this.base_artikul = base_artikul;
            this.model = model;
            this.kol_section = kol_section;
            this.svet = svet;
            this.brend = brend;
            this.kratkiy_tekst = kratkiy_tekst;
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
            this.segment = segment;
            this.buxgalter_tovar = buxgalter_tovar;
            this.buxgalter_sena = buxgalter_sena;
            this.buxgalter_uchot = buxgalter_uchot;
            this.bazoviy_edin = bazoviy_edin;//done
            this.alter_edin = alter_edin;
            this.stoimost_baza = stoimost_baza;
            this.stoimost_alter = stoimost_alter;
            this.status_online = status_online;//done
            this.zavod_name = zavod_name;//done
            this.tip_clenta = tip_clenta;//done
            this.is_active = is_active;//done
    
    }
    get_kratkiy_tekst(){
        switch(this.id){
            case 1: 
                if(this.model && this.kol_section && this.svet && this.brend){
                    if(this.is_active){
                        if (this.online_id && this.nazvaniye_ruchnoy){
        
                           
                            return {'text':this.model + '-'+ this.kol_section + ' ' + this.svet +' ' +this.brend,'accept':true}
                        }else{
                            
                            return {'text':this.model + '-'+ this.kol_section + ' ' + this.svet +' ' +this.brend,'accept':false}
                        }
                        
                    }else{
                        console.log('####>>>>> ',this.tip_clenta , this.sena_bez_nds , this.sena_c_nds , this.pickupdate , this.nazvaniye_ruchnoy , this.svet_product , this.group_zakup , this.group , this.tip , this.bazoviy_edin , this.status_online)
                        if (this.tip_clenta && this.sena_bez_nds && this.sena_c_nds && this.pickupdate && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online){
                            
                            
                            return {'text':this.model + '-'+ this.kol_section + ' ' + this.svet +' ' +this.brend,'accept':true}
                        }else{
                            
                            return {'text':this.model + '-'+ this.kol_section + ' ' + this.svet +' ' +this.brend,'accept':false}
                        }
                    } 
        
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                } break;
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
        
        <td class="sticky-col" style=' left: 139.6px;background-color:white!important' >
            <div class="input-group input-group-sm mb-1">
                <select class=" form-control basic_model" style="background-color:#ddebf7; width: 140px; font-size:10px " disabled id="model`+String(i)+`" ></select>
            </div>
            <span style='display:none' id='artikul_radiator` +String(i)+`'></span>
        </td>
        
        
        
        <td  >
            <div class="input-group input-group-sm mb-1 text-center" id ='base_artikul` +String(i)+`'>
                   
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 70px;">
        
            <select class="form-select" aria-label="" style="width: 70px;height:27px!important;z-index:0;border-color:red;display:none;"  id='kol_section`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option  value="" selected ></option>
                <option value="01">01</option>
                <option value="02">02</option>
                <option value="03">03</option>
                <option value="04">04</option>
                <option value="05">05</option>
                <option value="06">06</option>
                <option value="07">07</option>
                <option value="08">08</option>
                <option value="09">09</option>
                <option value="10">10</option>
                <option value="11">11</option>
                <option value="12">12</option>
                <option value="13">13</option>
                <option value="14">14</option>
                <option value="15">15</option>
                <option value="16">16</option>
                <option value="17">17</option>
                <option value="18">18</option>
                <option value="19">19</option>
                <option value="20">20</option>
                
            </select>
            
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">    
            <select class="form-select" aria-label="" style="width: 90px;height:27px!important;z-index:0;border-color:red;display:none;" onchange="create_kratkiy_tekst(`+String(i)+`)"  id='svet`+String(i)+`'>
                <option  value="" selected></option>
                <option value="9016">9016</option>
                <option value="1376">1376</option>
                <option value="840M">840M</option>
                <option value="YW383I">YW383I</option>
                <option value="YX353F">YX353F</option>
                <option value="YW370F">YW370F</option>
                <option value="Y2303I">Y2303I</option>
                <option value="7011">7011</option>

                
            </select>
            </div>
        </td>

        <td >
            <div class="input-group input-group-sm mb-1">    
            <select class="form-select" aria-label="" style="width: 100px;height:27px!important;z-index:0;border-color:red;display:none;" onchange="create_kratkiy_tekst(`+String(i)+`)"  id='brend`+String(i)+`'>
                <option  value="" selected></option>
                <option value="BK">BK</option>
                <option value="LIDER">LIDER</option>
                <option value="AKFA">AKFA</option>
                <option value="MILANO">MILANO</option>
                <option value="Perfetto">Perfetto</option>
                <option value="Florence">Florence</option>
                <option value="Piuma">Piuma</option>
                <option value="LIDER-PERFETTO">LIDER-PERFETTO</option>

                
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <span  class='text-center' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;z-index:0" id='kratkiy_tekst`+String(i)+`'></span>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
        <textarea   rows='1' class=" form-control " style="width: 220px; font-size:10px;height:27px!important;z-index:0;" id='comment`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></textarea >
        </div>
        </td>
        <td >
            <input  style='display:none;border-color:red; line-height:15px;height:27px!important;z-index:0' type="date" class="form-control" id="pickupdate`+String(i)+`" onchange='create_kratkiy_tekst(`+String(i)+`)'>      
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px; display:none;height:27px!important;z-index:0" id='sena_c_nds`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px; display:none; height:27px!important;z-index:0;" id='sena_bez_nds`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
       
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px;display:none;height:27px!important;z-index:0; " id='online_savdo_id`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <textarea   rows='1' class=" form-control " style="border-color:red; width: 220px; font-size:10px; display:none; height:27px!important;z-index:0;" id='nazvaniye_ruchnoy`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></textarea >
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 110px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;height:27px!important;z-index:0"  id='svet_product`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  value='' selected></option>
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
            <select class="form-select" aria-label="" style="width: 230px;text-transform: uppercase; font-size:12px; padding-right:0px;  border-color:red;display:none;height:27px!important;z-index:0" id='group_zakup`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option value="Butilchita">Butilchita</option>
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
            <option value="Granit">Granit</option>
            <option value="Radiator SAP (IMPORT)">Radiator SAP (IMPORT)</option>
            <option value="Radiator (Panel) Lider Line (UZ)">Radiator (Panel) Lider Line (UZ)</option>
            <option value="Rezina Tpv">Rezina Tpv</option>
            <option value="Aksessuar UZ Tapoich">Aksessuar UZ Tapoich</option>
            <option value="Aksessuar Import (SAP) keremas">Aksessuar Import (SAP) keremas</option>
            <option value="Radiator (Panel) AKFA (UZ)">Radiator (Panel) AKFA (UZ)</option>
            <option value="Kraska">Kraska</option>
            <option value="Gazoblok">Gazoblok</option>
            <option value="Paket">Paket</option>
            <option value="Radiator (Panel) ROYAL (UZ)">Radiator (Panel) ROYAL (UZ)</option>


            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1"  >
            <select class="form-select" aria-label="" id='group`+String(i)+`' style="width: 240px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;height:27px!important;z-index:0"  id='tipr`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)'required>
                <option  selected></option>
                <option value="5200 QVT PVC (NAVOIY)">5200 QVT PVC (NAVOIY)</option>
                <option value="5200 QVT PVC RETPEN (NAVOIY)">5200 QVT PVC RETPEN (NAVOIY)</option>
                
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;height:27px!important;z-index:0"  id='tip`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)'required>
                <option selected value="Готовый продукт">Готовый продукт</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 145px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;height:27px!important;z-index:0" id='segment`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="Aldoks">Aldoks</option>
                <option value="Стандарт">Стандарт</option>
                <option value="Премиум">Премиум</option>
                <option value="Аксессуар">Аксессуар</option>
                <option value="Falcon">Falcon</option>
                <option value="Аксессуар 2">Аксессуар 2</option>
                <option value="Podokonnik EKO">Podokonnik EKO</option>
                
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 520px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;height:27px!important;z-index:0" id='buxgalter_tovar`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value='Профиль из ПВХ ламинированный'>Профиль из ПВХ ламинированный</option>
                <option value='Otvetka 153 (oq)'>Otvetka 153 (oq)</option>
                <option value='Ламбри из ПВХ'>Ламбри из ПВХ</option>
                <option value='Soedinitel OP.40.J05 L=10mm'>Soedinitel OP.40.J05 L=10mm</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;display:none;height:27px!important;z-index:0" id='buxgalter_sena`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;display:none;height:27px!important;z-index:0" id='buxgalter_uchot`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;height:27px!important;z-index:0" id='bazoviy_edin`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;display:none;height:27px!important;z-index:0" id='alter_edin`+ String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
            <input type='text' class=" form-control " style="width: 75px; font-size:10px; display:none;height:27px!important;z-index:0" id='stoimost_baza`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)' ></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 75px; font-size:10px; display:none;height:27px!important;z-index:0;" id='stoimost_alter`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)' ></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;height:27px!important;z-index:0" id='status`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="Активный">Активный</option>
                <option value="Пассивный">Пассивный</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <span class =' text-center ' style="font-size: small; width:190px; font-weight: bold; text-transform: uppercase;z-index:0" id='zavod_name`+String(i)+`'>ZAVOD PVS NAVOIY</span>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;height:27px!important;z-index:0" id='tip_clenta`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
    return text
}

text = front_piece()


var table = $('#table-artikul')

table.append(text)


function request_piece(start=1,end=6){

    for (let i = start; i <= end; i++) {
        $('#model'+String(i)).select2({
            ajax: {
                url: "/client/radiator-artikul-list",
                dataType: 'json',
                processResults: function(data){
                    return {results: $.map(data, function(item){
                        return {id:item.id,text:item.model_radiator,artikul:item.artikul}
                    })
                };
                }
            }
            });
        
        
        
        var artikulSelect = $('#model'+String(i));
        $.ajax({
            type: 'GET',
            url: "/client/radiator-artikul-list"
        }).then(function (data) {
            var option = new Option(data.model_radiator, data.id, true, true);
            artikulSelect.append(option).trigger('change');
        
            artikulSelect.trigger({
                type: 'select2:select',
                params: {
                    data: data
                }
            });
        });
        
        
        $("#model"+String(i)).on("select2:select", function (e) { 
            
            var artikul_radiator =$('#artikul_radiator'+String(i));
            var base_artikul =$('#base_artikul'+String(i));
            
            artikul_radiator.text(e.params.data.artikul);
            base_artikul.text(e.params.data.artikul)
            
            var kol_section =$('#kol_section'+i);
            var svet =$('#svet'+i);
            var brend =$('#brend'+i);

            kol_section.css('display','block')
            svet.css('display','block')
            brend.css('display','block')

            kol_section.css('border-color','#red')
            svet.css('border-color','#red')
            brend.css('border-color','#red')

            if(data_base[i]){
                clear_artikul(i)
            }


            var is_active =$('#is_active'+i)
        
            if(is_active.text()=='Активный'){
                var online_savdo_id =$('#online_savdo_id'+i);
                var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+i);
                var svet_product =$('#svet_product'+i);
                var group_zakup =$('#group_zakup'+i);
                var group =$('#group'+i);
                var tip =$('#tip'+i);
                var bazoviy_edin =$('#bazoviy_edin'+i);
                var status =$('#status'+i);
                var zavod =$('#zavod'+i);
                var buxgalter_uchot =$('#buxgalter_uchot'+i);
                var buxgalter_sena =$('#buxgalter_sena'+i);
                var alter_edin =$('#alter_edin'+i);
                var stoimost_baza =$('#stoimost_baza'+i);
                var stoimost_alter =$('#stoimost_alter'+i);
                var segment =$('#segment'+i);
                var buxgalter_tovar =$('#buxgalter_tovar'+i);
                var comment =$('#comment'+i);
                var pickupdate =$('#pickupdate'+i);
                var sena_c_nds =$('#sena_c_nds'+i);
                var sena_bez_nds =$('#sena_bez_nds'+i);
                var tip_clenta =$('#tip_clenta'+i);
                comment.css('display','block')
                pickupdate.css('display','block')
                sena_c_nds.css('display','block')
                sena_bez_nds.css('display','block')
                tip_clenta.css('display','block')
                buxgalter_sena.css('display','block')
                
                
                
                
                
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
            
                
                online_savdo_id.css('border-color','red')
                nazvaniye_ruchnoy.css('border-color','red')
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
            
                

            }else{
                var online_savdo_id =$('#online_savdo_id'+i);
                var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+i);
                var svet_product =$('#svet_product'+i);
                var group_zakup =$('#group_zakup'+i);
                var group =$('#group'+i);
                var tip =$('#tip'+i);
                var bazoviy_edin =$('#bazoviy_edin'+i);
                var tip_clenta =$('#tip_clenta'+i);
                var status =$('#status'+i);
                var zavod =$('#zavod'+i);
                var buxgalter_uchot =$('#buxgalter_uchot'+i);
                var alter_edin =$('#alter_edin'+i);
                var stoimost_baza =$('#stoimost_baza'+i);
                var stoimost_alter =$('#stoimost_alter'+i);
                var segment =$('#segment'+i);
                var buxgalter_tovar =$('#buxgalter_tovar'+i);
                var buxgalter_sena =$('#buxgalter_sena'+i);
                var comment =$('#comment'+i);
                var obshiy_ves_shtuku =$('#obshiy_ves_shtuku'+i);
                var pickupdate =$('#pickupdate'+i);
                var sena_c_nds =$('#sena_c_nds'+i);
                var sena_bez_nds =$('#sena_bez_nds'+i);
                comment.css('display','block')
                obshiy_ves_shtuku.css('display','block')
                pickupdate.css('display','block')
                sena_c_nds.css('display','block')
                sena_bez_nds.css('display','block')
                tip_clenta.css('display','block')
                
                
                
                buxgalter_uchot.val('Килограмм')
                bazoviy_edin.val('Штука')
                alter_edin.val('Килограмм')
                stoimost_baza.val('1')
                
                
            
                
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
                buxgalter_sena.css('display','block')
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
            

            }







            
        });

    }
}

request_piece()

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
        request_piece(start = size+1, end = size+2)
        
        var data = new BasePokritiya()

        for(key in data_base[id]){
            data[key] = data_base[id][key]
        }
       

        data_base[size+1] = data
        
        var s = size+1

        var id = data.id;
        var model =  data.model
        var base_artikul =  data.base_artikul 
        var kol_section =  data.kol_section 
        var svet =  data.svet 
        var brend =  data.brend  
        var kratkiy_tekst =  data.kratkiy_tekst 
        var comment =  data.comment 
        var pickupdate =  data.pickupdate 
        var sena_c_nds =  data.sena_c_nds  
        var sena_bez_nds =  data.sena_bez_nds  

        var online_id =  data.online_id 
        var nazvaniye_ruchnoy =  data.nazvaniye_ruchnoy 
        var svet_product =  data.svet_product 
        var group_zakup =  data.group_zakup 
        var group =  data.group 
        var tip =  data.tip 
        var segment =  data.segment 
        var buxgalter_tovar =  data.buxgalter_tovar 
        var buxgalter_sena =  data.buxgalter_sena 
        var buxgalter_uchot =  data.buxgalter_uchot 
        var bazoviy_edin =  data.bazoviy_edin 
        var alter_edin =  data.alter_edin 
        var stoimost_baza =  data.stoimost_baza  
        var stoimost_alter =  data.stoimost_alter  
        var status_online =  data.status_online 
        var zavod_name =  data.zavod_name 
        var tip_clenta =  data.tip_clenta  

        var is_active = data.is_active
        


        check_text_and_change_simple(base_artikul,'#base_artikul'+s)
        
         
        
      
        var activate_btn =$('#activate_btn'+s);
        var create_btn =$('#create_btn'+s);
        activate_btn.attr('disabled',true)
        create_btn.attr('disabled',true)



        
        
       
        check_input_and_change(kol_section,'#kol_section'+s,dis=false,is_req=true)
        check_input_and_change(svet,'#svet'+s,dis=false,is_req=true)
        check_input_and_change(brend,'#brend'+s,dis=false,is_req=true)


        
        $('#model'+ s).attr('disabled',false)
        check_for_valid_and_set_val_select(model,'model'+ s,is_req=true)


       
        check_text_and_change(kratkiy_tekst,'#kratkiy_tekst'+s)
        check_input_and_change(comment,'#comment'+s)
        


       
        
        if(!is_active){
            create_btn.css('background-color','green')
            create_btn.css('color','white')
            check_input_and_change(pickupdate,'#pickupdate'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(sena_c_nds,'#sena_c_nds'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(sena_bez_nds,'#sena_bez_nds'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(online_id,'#online_savdo_id'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(svet_product,'#svet_product'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(group_zakup,'#group_zakup'+s,dis=false,is_req=true,is_req_simple=false)

            check_input_and_change(group,'#group'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(tip,'#tip'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(segment,'#segment'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(buxgalter_tovar,'#buxgalter_tovar'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(buxgalter_sena,'#buxgalter_sena'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(buxgalter_uchot,'#buxgalter_uchot'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(bazoviy_edin,'#bazoviy_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(alter_edin,'#alter_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_baza,'#stoimost_baza'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_alter,'#stoimost_alter'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(status_online,'#status'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(zavod_name,'#zavod_name'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip_clenta,'#tip_clenta'+s,dis=false,is_req=true,is_req_simple=false)
            var is_active =$('#is_active'+s)
            is_active.text('Пассивный')

        }else{
            
            activate_btn.css('background-color','orange')
            activate_btn.css('color','white')
            check_input_and_change(pickupdate,'#pickupdate'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sena_c_nds,'#sena_c_nds'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sena_bez_nds,'#sena_bez_nds'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(online_id,'#online_savdo_id'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(svet_product,'#svet_product'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(group_zakup,'#group_zakup'+s,dis=false,is_req=false,is_req_simple=true)

            check_input_and_change(group,'#group'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip,'#tip'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(segment,'#segment'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(buxgalter_sena,'#buxgalter_sena'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(buxgalter_tovar,'#buxgalter_tovar'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(buxgalter_uchot,'#buxgalter_uchot'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(bazoviy_edin,'#bazoviy_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(alter_edin,'#alter_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_baza,'#stoimost_baza'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_alter,'#stoimost_alter'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(status_online,'#status'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(zavod_name,'#zavod_name'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip_clenta,'#tip_clenta'+s,dis=false,is_req=false,is_req_simple=true)
            
            var is_active =$('#is_active'+s)
            is_active.text('Активный')
        }
        

        
        
    }


}

function check_for_valid_and_set_val_select(val,selector,is_req=false){
    if(is_req){
        var span = $('#select2-'+selector+'-container')
        span.css('display','block')
        span.css('border-color','red')

    }
    if(val !=NaN && val !='' && String(val) != 'NaN'){
        ////// selec2 value change \\\\\\\
        var span = $('#select2-'+selector+'-container')
        span.attr('title',val);
        span.text(val);

        //////end ////////////
        
    }
}

function check_input_and_change(val,selector,dis=false,is_req=false,is_req_simple=false){
    if(is_req){
        
        $(selector).attr('disabled',false)
        $(selector).css('display','block')
        $(selector).css('border-color','red')

    }
    if(is_req_simple){
        
        $(selector).attr('disabled',false)
        $(selector).css('display','block')
        $(selector).css('border-color','#dedad9')

    }
    if(val !=NaN && val !='' && String(val) != 'NaN'){
        var sel = $(selector)
        sel.attr('disabled',dis)
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
function check_text_and_change_simple(val,selector){
    if(val !=NaN && val !='' && String(val) != 'NaN'){
        var sel = $(selector)
        sel.text(val)
    }
}

function add_column(){
        
    text =""
    var sizeee = $('#table-artikul tr').length;
    
    text = front_piece(start = sizeee+1, end = sizeee+2)

    
    var table = $('#table-artikul')
    table.append(text)
    
    

    request_piece(start = sizeee+1, end = sizeee+2)


}



function create(i){
    
    var model = $('#model'+i)
    
    model.attr('disabled',false)

    var status_first =$('#status'+i);
    status_first.val('Активный')

    var is_active =$('#is_active'+i);
    is_active.text('Пассивный')
    // status_first.attr('disabled',true)

    var tip =$('#tip'+i);
    tip.val('Готовый продукт')
    

    var activate_btn =$('#activate_btn'+i);
    var create_btn =$('#create_btn'+i);
    create_btn.css('background-color','green')
    create_btn.css('color','white')
    activate_btn.attr('disabled',true)
    create_btn.attr('disabled',true)
    
    data_base[i] = new BasePokritiya()
    data_base[i].id = 1;
    
    data_base[i].is_active = false
    var svet_product =$('#svet_product'+i);


    
   

}

function activate(i){
    data_base[i] = new BasePokritiya()
    data_base[i].id = 1;

    var model = $('#model'+i)
    
    model.attr('disabled',false)


    var activate_btn =$('#activate_btn'+i);
    var create_btn =$('#create_btn'+i);
    activate_btn.css('background-color','orange')
    activate_btn.css('color','white')
    activate_btn.attr('disabled',true)
    create_btn.attr('disabled',true)


    var status_first =$('#status'+i);
    status_first.val('Активный')

    var is_active =$('#is_active'+i);
    is_active.text('Активный')
    // status_first.attr('disabled',true)
    var svet_product =$('#svet_product'+i);
        
    
    data_base[i].is_active=true

    

   
}


function clear_artikul(id){
    if(data_base[id]){

        var model =$('#select2-model'+id+'-container').text()
        
        var artikul_radiator = $('#artikul_radiator'+String(id)).text();
       
        

        

        data_base[id].model = model
        data_base[id].base_artikul = artikul_radiator
        


    }
   
//    console.log(data_base[id],'lllllllllllllll')
   
    create_kratkiy_tekst(id)
}

function artukil_clear(id){
    $('#model'+id).val(null).trigger('change');
    $('#model'+id).attr('disabled',true)
    var table_tr =$('#table_tr'+id);
    
   
    
    
    delete data_base[id]

    


    
    
    table_tr.css('background-color','white')
    




    var base_artikul =$('#base_artikul'+String(id));
    base_artikul.text('');

    var kol_section =$('#kol_section'+String(id));
    kol_section.val('');
    kol_section.css("display",'none');
    kol_section.css("border-color",'red');

    var svet =$('#svet'+String(id));
    svet.val('');
    svet.css("display",'none');
    svet.css("border-color",'red');

    var brend =$('#brend'+String(id));
    brend.val('');
    brend.css("display",'none');
    brend.css("border-color",'red');

    var kratkiy_tekst = document.getElementById('kratkiy_tekst'+String(id));
    kratkiy_tekst.innerText="";
    
    var status_first = $('#status'+String(id))
   
    status_first.val('Активный')

    
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
    var buxgalter_sena =$('#buxgalter_sena'+id);
    var alter_edin =$('#alter_edin'+id);
    var stoimost_baza =$('#stoimost_baza'+id);
    var stoimost_alter =$('#stoimost_alter'+id);
    var segment =$('#segment'+id);
    var buxgalter_tovar =$('#buxgalter_tovar'+id);
    var comment =$('#comment'+id);
    var pickupdate =$('#pickupdate'+id);
    var sena_c_nds =$('#sena_c_nds'+id);
    var sena_bez_nds =$('#sena_bez_nds'+id);
    var diller =$('#diller'+id);
    var tip_clenta =$('#tip_clenta'+id);
    
    // comment.css('display','none')
    pickupdate.css('display','none')
    sena_c_nds.css('display','none')
    sena_bez_nds.css('display','none')
    diller.css('display','none')
    tip_clenta.css('display','none')
    // var zavod_name =$('#zavod_name'+id)
    // zavod_name.text('')


    svet_product.css('display','none')
    group_zakup.css('display','none')
    group.css('display','none')
    tip.css('display','none')
    bazoviy_edin.css('display','none')
    status.css('display','none')
    zavod.css('display','none')
    buxgalter_uchot.css('display','none')
    buxgalter_sena.css('display','none')
    alter_edin.css('display','none')
    stoimost_baza.css('display','none')
    stoimost_alter.css('display','none')
    segment.css('display','none')
    buxgalter_tovar.css('display','none')
    
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
    sena_c_nds.css('border-color','red')
    sena_bez_nds.css('border-color','red')
    tip_clenta.css('border-color','red')

    
    diller.val('')
    tip_clenta.val('')
    
    online_savdo_id.val('')
    nazvaniye_ruchnoy.val('')
    svet_product.val('')
    group_zakup.val('')
    group.val('')
    tip.val('')
    bazoviy_edin.val('')
    status.val('Активный')
    // zavod.val('')
    buxgalter_uchot.val('')
    buxgalter_sena.val('')
    alter_edin.val('')
    stoimost_baza.val('')
    stoimost_alter.val('')
    segment.val('')
    buxgalter_tovar.val('')
    comment.val('')
   
    pickupdate.val('')
    sena_c_nds.val('')
    sena_bez_nds.val('')
    
    var create_btn =$('#create_btn'+id);
    var activate_btn =$('#activate_btn'+id);

    activate_btn.attr('disabled',false)
    create_btn.attr('disabled',false)

    activate_btn.css('background-color','')
    activate_btn.css('color','')
    create_btn.css('background-color','')
    create_btn.css('color','')

}





var zapros_count =[]


function create_kratkiy_tekst(id){
    if(!data_base[id]){
        console.log(data_base)
        console.log('salom')
    }else{
    var kratkiy_tekst = $('#kratkiy_tekst'+String(id));
    
    var base_artikul= $('#base_artikul'+String(id));
    var kol_section= $('#kol_section'+String(id));
    var svet= $('#svet'+String(id));
    var brend= $('#brend'+String(id));
        
        console.log(svet,brend,'lddddddd')
    var comment= $('#comment'+String(id));
    comment = comment.val();
    

    if(comment!=''){
        data_base[id].comment = comment;
    }else{
        data_base[id].comment = NaN;
    }
   
    if(base_artikul.text()!=''){
        base_artikul.css("border-color",'#dedad9');
        data_base[id].base_artikul = base_artikul.text();
    }else{
        base_artikul.css("border-color",'red');
        data_base[id].base_artikul = NaN;
    }
    console.log(kol_section.val(),'kol-sec')
    if(kol_section.val()!=''){
        console.log(kol_section.val(),'section')
        kol_section.css("border-color",'#dedad9');
        data_base[id].kol_section = kol_section.val();
    }else{
        kol_section.css("border-color",'red');
        data_base[id].kol_section = NaN;
    }
    if(svet.val()!=''){
        console.log(svet.val(),'svet')
        svet.css("border-color",'#dedad9');
        data_base[id].svet = svet.val();
    }else{
        svet.css("border-color",'red');
        data_base[id].svet = NaN;
    }
    if(brend.val()!=''){
        console.log(brend.val(),'brend')
        brend.css("border-color",'#dedad9');
        data_base[id].brend = brend.val();
    }else{
        brend.css("border-color",'red');
        data_base[id].brend = NaN;
    }
    
    
    
    
    



    

    
    var online_savdo_id =$('#online_savdo_id'+id);
    var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);
    var svet_product =$('#svet_product'+id);
    var group_zakup =$('#group_zakup'+id);
    var group =$('#group'+id);
    var tip =$('#tip'+id);
    var bazoviy_edin =$('#bazoviy_edin'+id);
    var status =$('#status'+id);
    var zavod =$('#zavod_name'+id);
    var nazvaniye_system =$('.nazvaniye_system'+id).text();
    
    var segment =$('#segment'+id).val();
    var buxgalter_tovar =$('#buxgalter_tovar'+id).val();
    var buxgalter_uchot =$('#buxgalter_uchot'+id).val();
    var alter_edin =$('#alter_edin'+id).val();
    var stoimost_baza =$('#stoimost_baza'+id).val();
    var stoimost_alter =$('#stoimost_alter'+id).val();
    
    if(nazvaniye_system!=''){
        data_base[id].nazvaniye_system = nazvaniye_system;
    }else{
        data_base[id].nazvaniye_system = NaN;
    }
    if(stoimost_alter!=''){
        data_base[id].stoimost_alter = stoimost_alter;
    }else{
        data_base[id].stoimost_alter = NaN;
    }
    if(stoimost_baza!=''){
        data_base[id].stoimost_baza = stoimost_baza;
    }else{
        data_base[id].stoimost_baza = NaN;
    }
    if(alter_edin!=''){
        data_base[id].alter_edin = alter_edin;
    }else{
        data_base[id].alter_edin = NaN;
    }
    if(buxgalter_uchot!=''){
        data_base[id].buxgalter_uchot = buxgalter_uchot;
    }else{
        data_base[id].buxgalter_uchot = NaN;
    }
    if(segment!=''){
        data_base[id].segment = segment;
    }else{
        data_base[id].segment = NaN;
    }
    if(buxgalter_tovar!=''){
        data_base[id].buxgalter_tovar = buxgalter_tovar;
    }else{
        data_base[id].buxgalter_tovar = NaN;
    }


    var comment =$('#comment'+id);
    var pickupdate =$('#pickupdate'+id);
    var sena_c_nds =$('#sena_c_nds'+id);
    var sena_bez_nds =$('#sena_bez_nds'+id);
    var diller =$('#diller'+id)
    var tip_clenta =$('#tip_clenta'+id)
    
    
    var is_active =$('#is_active'+id)
    
    if(is_active.text()=='Активный'){

        if(tip_clenta.val()!=''){
            data_base[id].tip_clenta = tip_clenta.val();
            tip_clenta.css('border-color','#dedad9')
        }else{
            tip_clenta.css('border-color','#dedad9')
            data_base[id].tip_clenta = NaN;
        }
        if(diller.val()!=''){
            data_base[id].diller = diller.val();
            diller.css('border-color','#dedad9')
        }else{
            data_base[id].diller = NaN;
        }

        if(sena_bez_nds.val()!=''){
            data_base[id].sena_bez_nds = sena_bez_nds.val();
            sena_bez_nds.css('border-color','#dedad9')
        }else{
            data_base[id].sena_bez_nds = NaN;
        }
        if(sena_c_nds.val()!=''){
            data_base[id].sena_c_nds = sena_c_nds.val();
            sena_c_nds.css('border-color','#dedad9')
        }else{
            data_base[id].sena_c_nds = NaN;
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
        
        data_base[id].zavod_name = 'ZAVOD PVS NAVOIY';
        
    }else{
        if(tip_clenta.val()!=''){
            data_base[id].tip_clenta = tip_clenta.val();
            tip_clenta.css('border-color','#dedad9')
        }else{
            tip_clenta.css('border-color','red')
            data_base[id].tip_clenta = NaN;
        }
        if(diller.val()!=''){
            data_base[id].diller = diller.val();
            diller.css('border-color','#dedad9')
        }else{
            data_base[id].diller = NaN;
        }
        if(sena_bez_nds.val()!=''){
            data_base[id].sena_bez_nds = sena_bez_nds.val();
            sena_bez_nds.css('border-color','#dedad9')
        }else{
            sena_bez_nds.css('border-color','red')
            data_base[id].sena_bez_nds = NaN;
        }

        if(sena_c_nds.val()!=''){
            data_base[id].sena_c_nds = sena_c_nds.val();
            sena_c_nds.css('border-color','#dedad9')
        }else{
            sena_c_nds.css('border-color','red')
            data_base[id].sena_c_nds = NaN;
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
        data_base[id].zavod_name = 'ZAVOD PVS NAVOIY';
        
        
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
    
    if(data.text !='XXXXXXXX' ){
        var art_krat = data_base[id].base_artikul + data.text
        if(zapros_count.indexOf(art_krat) === -1){
            sap_codes = get_sapcode(id,data_base[id].base_artikul,data.text)
            zapros_count.push(art_krat)
        }
        data_base[id].kratkiy_tekst= data.text
    } 

  
    kratkiy_tekst.text(data.text)

    }
}
function get_sapcode(id,artikul,kratkiy_tekst){
    var url = '/client/get-sapcodes-pvc'
   

    $.ajax({
        type: 'GET',
        url: url,
        data: {'artikul':artikul,'kratkiy_tekst':kratkiy_tekst},
    }).done(function (res) {
        if (res.status ==201){
            var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
            var kratkiy_text_ruchnoy = $('#kratkiy_tekst_ruchnoy'+id)
            sap_code_ruchnoy.val(res.artikul)
            kratkiy_text_ruchnoy.val(res.kratkiy_tekst)
            sap_code_ruchnoy.css('background-color','orange')
            kratkiy_text_ruchnoy.css('background-color','orange')
        }else{
            var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
            var kratkiy_text_ruchnoy = $('#kratkiy_tekst_ruchnoy'+id)
            sap_code_ruchnoy.val('')
            kratkiy_text_ruchnoy.val('')
            sap_code_ruchnoy.css('background-color','white')
            kratkiy_text_ruchnoy.css('background-color','white')
            console.log('aa')
        }
        // WON'T REDIRECT
    });
}








