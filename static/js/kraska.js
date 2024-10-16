class BasePokritiya{
    constructor(
        full=false,
        id=NaN, 
        combination=NaN,
        tip_kraski=NaN,
        tip_kraski_full=NaN,
        kraska=NaN,
        brend_kraska=NaN,
        artikul=NaN,
        dop_info=NaN,
        kratkiy_tekst=NaN,
        comment=NaN,



        pickupdate=NaN,
        sena_c_nds=NaN,
        sena_bez_nds=NaN,
        edi_izm=NaN,

        online_id=NaN,
        nazvaniye_ruchnoy=NaN,
        svet_product=NaN,
        group_zakup=NaN,
        group=NaN,
        tip=NaN,
        
        bazoviy_edin=NaN,
        alter_edin=NaN,
        stoimost_baza=NaN,
        stoimost_alter=NaN,
        status_online=NaN,
        zavod=NaN,
        tip_clenta=NaN,
        is_active=false,
        ) {
      
            this.full=full;
            this.id=id;
            this.combination=combination;
            this.tip_kraski=tip_kraski;
            this.tip_kraski_full=tip_kraski_full;
            this.kraska=kraska;
            this.brend_kraska=brend_kraska;
            this.artikul=artikul;
            this.dop_info=dop_info;
            this.kratkiy_tekst=kratkiy_tekst;
            this.comment=comment;
            this.pickupdate=pickupdate;
            this.sena_c_nds=sena_c_nds;
            this.sena_bez_nds=sena_bez_nds;
            this.edi_izm=edi_izm;
            this.online_id=online_id;
            this.nazvaniye_ruchnoy=nazvaniye_ruchnoy;
            this.svet_product=svet_product;
            this.group_zakup=group_zakup;
            this.group=group;
            this.tip=tip;
            // this.segment=segment;
            // this.buxgalter_tovar=buxgalter_tovar;
            // this.buxgalter_sena=buxgalter_sena;
            // this.buxgalter_uchot=buxgalter_uchot;
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
                            if(this.tip_kraski && this.kraska){
                                console.log(this.pickupdate ,this.sena_c_nds, this.sena_bez_nds,this.edi_izm, this.online_id , this.nazvaniye_ruchnoy)
                                // if (this.base_artikul && this.kratkiy_tekst && this.bei && this.tip_clenta && this.zavod &&this.sena_c_nds&&this.sena_bez_nds && this.pickupdate && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.sistema){
                                if (this.pickupdate &&this.sena_c_nds&& this.sena_bez_nds&&this.edi_izm&& this.online_id && this.nazvaniye_ruchnoy){
                                    if(this.dop_info){
                                        return {'text':'RAINBOW RAL '+this.kraska+' '+this.dop_info +' ' +this.tip_kraski_full,'accept':true}
                                    }else{
                                        return {'text':'RAINBOW RAL '+this.kraska+' ' +this.tip_kraski_full,'accept':true}
                                    }
                                }else{
                                    if(this.dop_info){
                                        return {'text':'RAINBOW RAL '+this.kraska+' '+this.dop_info +' ' +this.tip_kraski_full,'accept':false}
                                    }else{
                                        return {'text':'RAINBOW RAL '+this.kraska+' ' +this.tip_kraski_full,'accept':false}
                                    }
                                }
                            }else{
                                return {'text':'XXXXXXXX','accept':false}
                            }
                    
                        }else{
                            if(this.tip_kraski && this.kraska){
                                console.log(this.pickupdate ,this.sena_c_nds, this.sena_bez_nds,this.edi_izm , this.nazvaniye_ruchnoy , this.zavod_name , this.svet_product , this.group_zakup , this.group , this.tip , this.bazoviy_edin)
                                if (this.pickupdate &&this.sena_c_nds&& this.sena_bez_nds&&this.edi_izm && this.nazvaniye_ruchnoy && this.zavod_name && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin){
                                    if(this.dop_info){
                                        return {'text':'RAINBOW RAL '+this.kraska+' '+this.dop_info +' ' +this.tip_kraski_full,'accept':true}
                                    }else{
                                        return {'text':'RAINBOW RAL '+this.kraska+' ' +this.tip_kraski_full,'accept':true}
                                    }
                                }else{
                                    if(this.dop_info){
                                        return {'text':'RAINBOW RAL '+this.kraska+' '+this.dop_info +' ' +this.tip_kraski_full,'accept':false}
                                    }else{
                                        return {'text':'RAINBOW RAL '+this.kraska+' ' +this.tip_kraski_full,'accept':false}
                                    }
                                }
                            }else{
                                return {'text':'XXXXXXXX','accept':false}
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
                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1">
                            <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px; display:none;z-index:0"  id='combination`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                                <option  selected ></option>
                                <option   value="Гибрид">Гибрид</option>
                                <option   value="Обычный">Обычный</option>
                            </select>
                        </div>
                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1">
                            <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px; display:none;z-index:0"  id='tip_kraski`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                                <option  selected ></option>
                                <option   value="GLS" data-krat = "GLOSS">GLS</option>
                                <option   value="EPS" data-krat = "Epoxide">EPS</option>
                                <option   value="TEX" data-krat = "TEX">TEX</option>
                                <option   value="MAT" data-krat = "MAT">MAT</option>
                                <option   value="SW" data-krat = "SW">SW</option>
                            </select>
                        </div>
                    </td>
                    <td  style='display:none;' id="kraska_div`+String(i)+`">
                        <div class="input-group input-group-sm mb-1">
                            <select class=" form-control basic_artikul" style="background-color:#ddebf7; width: 75px; padding-right:150px!important; font-size:10px; z-index:0"  id="kraska`+String(i)+`" onchange='create_kratkiy_tekst(`+String(i)+`)'></select>
                
                        </div>
                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1" style="font-size: small; width:130px">
                            <div>
                                <span class =' text-center pl-1' style="font-size: small; z-index:0" id ='brend_kraska` +String(i)+`'></span>
                            </div>
                        </div>
                    </td>
                    <td class="sticky-col" style="left: 139.6px;background-color:white!important" >
                        <div class="mb-1" style="font-size: small; width:130px">
                            <div>
                                <span class =' text-center pl-1' style="font-size: small;" id ='artikul` +String(i)+`'></span>
                            </div>
                        </div>
                    </td>
                    
                    `
        }else{
            buttons=`
            <td >
                <div class="input-group input-group-sm mb-1">
                    <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px; display:none;z-index:0"  id='combination`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                        <option  selected ></option>
                        <option   value="Гибрид">Гибрид</option>
                        <option   value="Обычный">Обычный</option>
                    </select>
                </div>
            </td>
            <td >
                <div class="input-group input-group-sm mb-1">
                    <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px; display:none;z-index:0"  id='tip_kraski`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                        <option  selected ></option>
                        <option   value="GLS" data-krat = "GLOSS">GLS</option>
                        <option   value="EPS" data-krat = "Epoxide">EPS</option>
                        <option   value="TEX" data-krat = "TEX">TEX</option>
                        <option   value="MAT" data-krat = "MAT">MAT</option>
                        <option   value="SW" data-krat = "SW">SW</option>
                    </select>
                </div>
            </td>
            <td  style='display:none;' id="kraska_div`+String(i)+`">
                <div class="input-group input-group-sm mb-1">
                    <select class=" form-control basic_artikul" style="background-color:#ddebf7; width: 75px; padding-right:150px!important; font-size:10px; z-index:0"  id="kraska`+String(i)+`" onchange='create_kratkiy_tekst(`+String(i)+`)'></select>
        
                </div>
            </td>
            <td >
                <div class="input-group input-group-sm mb-1" style="font-size: small; width:130px">
                    <div>
                        <span class =' text-center pl-1' style="font-size: small; z-index:0" id ='brend_kraska` +String(i)+`'></span>
                    </div>
                </div>
            </td>
            <td class="sticky-col" style="left:0;background-color:white!important" >
                <div class="mb-1" style="font-size: small; width:130px">
                    <div>
                        <span class =' text-center pl-1' style="font-size: small;" id ='artikul` +String(i)+`'></span>
                    </div>
                </div>
            </td>
            `
        }
        text +=`
        <tr id='table_tr` +String(i)+`' style='padding-bottom:0!important;margin-bottom:0!important;'>                   
        `+buttons+
         `
        
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;display:none;height:27px;z-index:0 " id='dop_info`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class=" mb-1" style="font-size: small; width:250px">
                <div>
                    <span class =' text-center pl-1' style="font-size: small; z-index:0;white-space:nowrap;" id ='kratkiy_tekst` +String(i)+`'></span>
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;display:none;height:27px;z-index:0 " id='comment`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>


        <td >
        <input  style='display:none; line-height:15px;z-index:0' type="date" class="form-control" id="pickupdate`+String(i)+`" onchange='create_kratkiy_tekst(`+String(i)+`)'> 
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 75px; font-size:10px;display:none;height:32px;z-index:0 " id='sena_c_nds`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 75px; font-size:10px;display:none;height:32px;z-index:0 " id='sena_bez_nds`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px; display:none;z-index:0"  id='edi_izm`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                    <option  selected value="КГ">КГ</option>
                </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 75px; font-size:10px;display:none;height:32px;z-index:0 " id='online_id`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type='text' class=" form-control " style=" width: 250px; font-size:10px; height:27px!important;z-index:0;display:none;"  id='nazvaniye_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
            
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px; display:none;z-index:0"  id='svet_product`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                    <option  selected></option>
                    <option   value="COLOUR">COLOUR</option>
                    <option   value="WHITE">WHITE</option>
                </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 230px; font-size:12px; padding-right:0px;  display:none;z-index:0" id='group_zakup`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  ></option>
            <option  selected value='Kraska'>Kraska</option>
            
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1"  >
            <select class="form-select" aria-label="" id='group`+String(i)+`' style="width: 240px; font-size:12px; padding-right:0px; display:none;z-index:0"    onchange='create_kratkiy_tekst(`+String(i)+`)'required>
                <option  ></option>
                <option selected value="PIGMENT POROSHKOVIY">PIGMENT POROSHKOVIY</option>
                
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px; display:none;z-index:0"  id='tip`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)'required>
                <option  ></option>
                <option value="Сырье">Сырье</option>
                <option selected value="Готовый продукт">Готовый продукт</option>
            </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px; display:none;z-index:0" id='bazoviy_edin`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  ></option>
                <option value="Штука">Штука</div>
                <option selected value="Килограмм">Килограмм</div>
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
            <select class="form-select" disabled  aria-label="" style="width: 155px; font-size:12px; padding-right:0px; display:none;z-index:0" id='status`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="Активный">Активный</option>
                <option value="Пассивный">Пассивный</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px; display:none;z-index:0" id='zavod_name`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option selected value="ZAVOD KRASKA">ZAVOD KRASKA</option>
                
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

var csrfToken = getCSRFToken();

function request_piece(start = 1, end = 7) {
    for (let i = start; i <= end; i++) {
        var $selectElement = $('#kraska' + i);  // Cache the selector
        // console.log(i)
        $selectElement.select2({
            tags: true,
            placeholder: "Код краски",
            ajax: {
                url: url_kraska,
                dataType: 'json',
                delay: 250,
                data: function (params) {
                    return {
                        term: params.term  // search term
                    };
                },
                processResults: function (data) {

                    return {
                        results: data.results.map(function (item) {
                            return {
                                id: item.name,  // Ensure your API returns 'id'
                                text: item.name  // Ensure your API returns 'text'
                            };
                        })
                    };
                },
                cache: true
            },
            createTag: function (params) {
                var term = $.trim(params.term);

                if (term === '') {
                    return null;
                }

                return {
                    id: term,
                    text: term,
                    newOption: true
                };
            },
            insertTag: function (data, tag) {
                data.push(tag);
            }
        });

        
        // Handle the event when a new option is added
        $selectElement.on('select2:select', function (e) {
            var data = e.params.data;
            // console.log(data)
            if (data.newOption) {
                // Make a POST request to add the new option
                var newOption = new Option(data.text, data.text, true, true);
                $selectElement.append(newOption).trigger('change');
                // $.post(url_kraska, {
                //     new_option: data.text,
                //     csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()  // Properly get the CSRF token
                // }).done(function (response) {
                //     // Update the select2 with the new option
                //     var newOption = new Option(response.name, response.id, true, true);
                //     $selectElement.append(newOption).trigger('change');
                // }).fail(function () {
                //     alert("There was an error adding the new option.");
                // });
            }
        });
    }
}


var table = $('#table-artikul')

// table.append(text)
data_base = {}

if(status_proccess1 == 'new'){
    table.append(text)
    request_piece()

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
            request_piece(start = s, end = s+1)
        }else{
            var data = data_base[id]
            var s = ii
            // artikul_list_add(start = s, end = s+1)
            request_piece(start = s, end = s+1)
        }

        
        var combination = data.combination;
        var tip_kraski = data.tip_kraski;
        var kraska = data.kraska;
        var brend_kraska = data.brend_kraska;
        var artikul = data.artikul;
        var dop_info = data.dop_info;
        var kratkiy_tekst = data.kratkiy_tekst;
        var comment = data.comment;
    
        
        var comment = data.comment;
        
        
        var pickupdate = data.pickupdate;
        var sena_c_nds = data.sena_c_nds;
        var sena_bez_nds = data.sena_bez_nds;
        var edi_izm = data.edi_izm;

        var online_id = data.online_id;
        var nazvaniye_ruchnoy = data.nazvaniye_ruchnoy;
        var svet_product = data.svet_product;
        var group_zakup = data.group_zakup;
        var group = data.group;
        var tip = data.tip;
       
        var bazoviy_edin = data.bazoviy_edin;
        var alter_edin = data.alter_edin;
        var stoimost_baza = data.stoimost_baza;
        var stoimost_alter = data.stoimost_alter;
        var status_online = data.status_online;
        var zavod = data.zavod;
        var tip_clenta = data.tip_clenta;
        
        var is_active = data.is_active;
        
        var activate_btn =$('#activate_btn'+s);
        var create_btn =$('#create_btn'+s);
        activate_btn.attr('disabled',true)
        create_btn.attr('disabled',true)
        var kraska_div =$('#kraska_div'+s);
        kraska_div.css('display','block')
        console.log(artikul,'llllssd')
        
        if(!is_active){
            create_btn.css('background-color','green')
            create_btn.css('color','white')
            $('#is_active'+s).text('')
            
            check_input_and_change(combination,'#combination'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(tip_kraski,'#tip_kraski'+s,dis=false,is_req=true,is_req_simple=false)

            // #kraska
            check_text_and_change('RAINBOW RAL','#brend_kraska'+s)
            check_text_and_change(artikul,'#artikul'+s)
            check_input_and_change(dop_info,'#dop_info'+s,dis=false,is_req=false,is_req_simple=true)
            check_text_and_change(kratkiy_tekst,'#kratkiy_tekst'+s)
            
            check_input_and_change(comment,'#comment'+s,dis=false,is_req=false,is_req_simple=true)

           

            check_input_and_change(pickupdate,'#pickupdate'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(sena_c_nds ,'#sena_c_nds'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(sena_bez_nds ,'#sena_bez_nds'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(edi_izm ,'#edi_izm'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(online_id,'#online_id'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(svet_product,'#svet_product'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(group_zakup,'#group_zakup'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(group,'#group'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip,'#tip'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(bazoviy_edin,'#bazoviy_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(alter_edin,'#alter_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_baza,'#stoimost_baza'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_alter,'#stoimost_alter'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(status_online,'#status'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(zavod,'#zavod_name'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip_clenta,'#tip_clenta'+s,dis=false,is_req=false,is_req_simple=true)
            }
        else{
            // console.log(status_online,'kkkk')
            activate_btn.css('background-color','orange')
            activate_btn.css('color','white')
            $('#is_active'+s).text('Активный')
            check_input_and_change(combination,'#combination'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(tip_kraski,'#tip_kraski'+s,dis=false,is_req=true,is_req_simple=false)

            // #kraska
            check_text_and_change('RAINBOW RAL','#brend_kraska'+s)
            check_text_and_change(artikul,'#artikul'+s)
            check_input_and_change(dop_info,'#dop_info'+s,dis=false,is_req=false,is_req_simple=true)
            check_text_and_change(kratkiy_tekst,'#kratkiy_tekst'+s)
            
            check_input_and_change(comment,'#comment'+s,dis=false,is_req=false,is_req_simple=true)

           

            check_input_and_change(pickupdate,'#pickupdate'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(sena_c_nds ,'#sena_c_nds'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(sena_bez_nds ,'#sena_bez_nds'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(edi_izm ,'#edi_izm'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(online_id,'#online_id'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(svet_product,'#svet_product'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(group_zakup,'#group_zakup'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(group,'#group'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip,'#tip'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(bazoviy_edin,'#bazoviy_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(alter_edin,'#alter_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_baza,'#stoimost_baza'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_alter,'#stoimost_alter'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(status_online,'#status'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(zavod,'#zavod_name'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip_clenta,'#tip_clenta'+s,dis=false,is_req=false,is_req_simple=true)
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
    data_base[id].zavod_name = 'ZAVOD KRASKA';
    data_base[id].status_online = 'Пассивный';
    var status_first =$('#status'+id);
    status_first.val('Пассивный')
    status_first.css('display','block')

    var is_active =$('#is_active'+id);
    is_active.text('Пассивный')

    
    

    var activate_btn =$('#activate_btn'+id);
    var create_btn =$('#create_btn'+id);
    create_btn.css('background-color','green')
    create_btn.css('color','white')
    activate_btn.attr('disabled',true)
    create_btn.attr('disabled',true)


    var combination=$('#combination'+id)
    var tip_kraski=$('#tip_kraski'+id)
    var kraska_div=$('#kraska_div'+id)
    var brend_kraska=$('#brend_kraska'+id)
    var artikul=$('#artikul'+id)
    var dop_info=$('#dop_info'+id)
    var kratkiy_tekst=$('#kratkiy_tekst'+id)
    var comment=$('#comment'+id)
    var pickupdate=$('#pickupdate'+id)
    var sena_c_nds=$('#sena_c_nds'+id)
    var sena_bez_nds=$('#sena_bez_nds'+id)
    var edi_izm=$('#edi_izm'+id)
    var online_id=$('#online_id'+id)
    var nazvaniye_ruchnoy=$('#nazvaniye_ruchnoy'+id)
    var svet_product=$('#svet_product'+id)
    var group_zakup=$('#group_zakup'+id)
    var group=$('#group'+id)
    var tip=$('#tip'+id)
    // var segment=$('#segment'+id)
    // var buxgalter_tovar=$('#buxgalter_tovar'+id)
    // var buxgalter_sena=$('#buxgalter_sena'+id)
    // var buxgalter_uchot=$('#buxgalter_uchot'+id)
    var bazoviy_edin=$('#bazoviy_edin'+id)
    // var alter_edin=$('#alter_edin'+id)
    // var stoimost_baza=$('#stoimost_baza'+id)
    // var stoimost_alter=$('#stoimost_alter'+id)
    var status_online=$('#status_online'+id)
    var zavod=$('#zavod_name'+id)
    var tip_clenta=$('#tip_clenta'+id)
    
    
    combination.css('display','block')
    tip_kraski.css('display','block')
    kraska_div.css('display','block')
    brend_kraska.css('display','block')
    artikul.css('display','block')
    dop_info.css('display','block')
    kratkiy_tekst.css('display','block')
    comment.css('display','block')
    pickupdate.css('display','block')
    sena_c_nds.css('display','block')
    sena_bez_nds.css('display','block')
    edi_izm.css('display','block')
    online_id.css('display','block')
    nazvaniye_ruchnoy.css('display','block')
    svet_product.css('display','block')
    group_zakup.css('display','block')
    group.css('display','block')
    tip.css('display','block')
    // segment.css('display','block')
    // buxgalter_tovar.css('display','block')
    // buxgalter_sena.css('display','block')
    // buxgalter_uchot.css('display','block')
    bazoviy_edin.css('display','block')
    // alter_edin.css('display','block')
    // stoimost_baza.css('display','block')
    // stoimost_alter.css('display','block')
    status_online.css('display','block')
    zavod.css('display','block')
    tip_clenta.css('display','block')
    brend_kraska.text('RAINBOW RAL')


    combination.css('border-color','red')
    tip_kraski.css('border-color','red')
    
    online_id.css('border-color','#dedad9')
    

    pickupdate.css('border-color','red')
    sena_c_nds.css('border-color','red')
    sena_bez_nds.css('border-color','red')
    // edi_izm.css('border-color','red')
    nazvaniye_ruchnoy.css('border-color','red')
    svet_product.css('border-color','red')
    // group_zakup.css('border-color','red')
    // group.css('border-color','red')
    
    // tip.css('border-color','red')
    // bazoviy_edin.css('border-color','red')

    
  
   
        
   

}

function activate(id){
    // data_base[i] = new OnlineSavdo()

    data_base[id] = new BasePokritiya()
    data_base[id].id = 1;
    data_base[id].status_online = 'Активный';
    data_base[id].zavod_name = 'ZAVOD KRASKA';

    var activate_btn =$('#activate_btn'+id);
    var create_btn =$('#create_btn'+id);
    activate_btn.css('background-color','orange')
    activate_btn.css('color','white')
    activate_btn.attr('disabled',true)
    create_btn.attr('disabled',true)



    // console.log('activateeee')
    var status_first =$('#status'+id);
    status_first.val('Активный')
    status_first.css('display','block')

    var is_active =$('#is_active'+id);
    is_active.text('Активный')



    // var status_first =$('#status'+id);
    // status_first.val('Пассивный')
    // status_first.css('display','block')

    // var is_active =$('#is_active'+id);
    // is_active.text('Пассивный')


    data_base[id].is_active=true
   

    var combination=$('#combination'+id)
    var tip_kraski=$('#tip_kraski'+id)
    var kraska_div=$('#kraska_div'+id)
    var brend_kraska=$('#brend_kraska'+id)
    var artikul=$('#artikul'+id)
    var dop_info=$('#dop_info'+id)
    var kratkiy_tekst=$('#kratkiy_tekst'+id)
    var comment=$('#comment'+id)
    var pickupdate=$('#pickupdate'+id)
    var sena_c_nds=$('#sena_c_nds'+id)
    var sena_bez_nds=$('#sena_bez_nds'+id)
    var edi_izm=$('#edi_izm'+id)
    var online_id=$('#online_id'+id)
    var nazvaniye_ruchnoy=$('#nazvaniye_ruchnoy'+id)
    var svet_product=$('#svet_product'+id)
    var group_zakup=$('#group_zakup'+id)
    var group=$('#group'+id)
    var tip=$('#tip'+id)
    // var segment=$('#segment'+id)
    // var buxgalter_tovar=$('#buxgalter_tovar'+id)
    // var buxgalter_sena=$('#buxgalter_sena'+id)
    // var buxgalter_uchot=$('#buxgalter_uchot'+id)
    var bazoviy_edin=$('#bazoviy_edin'+id)
    // var alter_edin=$('#alter_edin'+id)
    // var stoimost_baza=$('#stoimost_baza'+id)
    // var stoimost_alter=$('#stoimost_alter'+id)
    var status=$('#status'+id)
    var zavod=$('#zavod_name'+id)
    var tip_clenta=$('#tip_clenta'+id)
    
    
    combination.css('display','block')
    tip_kraski.css('display','block')
    kraska_div.css('display','block')
    brend_kraska.css('display','block')
    artikul.css('display','block')
    dop_info.css('display','block')
    kratkiy_tekst.css('display','block')
    comment.css('display','block')
    pickupdate.css('display','block')
    sena_c_nds.css('display','block')
    sena_bez_nds.css('display','block')
    edi_izm.css('display','block')
    online_id.css('display','block')
    nazvaniye_ruchnoy.css('display','block')
    svet_product.css('display','block')
    group_zakup.css('display','block')
    group.css('display','block')
    tip.css('display','block')
    // segment.css('display','block')
    // buxgalter_tovar.css('display','block')
    // buxgalter_sena.css('display','block')
    // buxgalter_uchot.css('display','block')
    bazoviy_edin.css('display','block')
    // alter_edin.css('display','block')
    // stoimost_baza.css('display','block')
    // stoimost_alter.css('display','block')
    status.css('display','block')
    zavod.css('display','block')
    tip_clenta.css('display','block')
    status.val('Активный')

    brend_kraska.text('RAINBOW RAL')
    
    combination.css('border-color','red')
    tip_kraski.css('border-color','red')

    pickupdate.css('border-color','red')
    sena_c_nds.css('border-color','red')
    sena_bez_nds.css('border-color','red')
    // edi_izm.css('border-color','red')
    online_id.css('border-color','red')
    nazvaniye_ruchnoy.css('border-color','red')

    svet_product.css('border-color','#dedad9')
    group_zakup.css('border-color','#dedad9')
    group.css('border-color','#dedad9')
    tip.css('border-color','#dedad9')
    bazoviy_edin.css('border-color','#dedad9')
    // sena_c_nds.css('border-color','#dedad9')
    // sena_bez_nds.css('border-color','#dedad9')

    

}





function artukil_clear(id){
    
    var table_tr =$('#table_tr'+id);
    
    delete data_base[id]

    
    table_tr.css('background-color','white')
    

    var status_first = $('#status'+String(id))
   
    status_first.val('Активный')

    
    var combination=$('#combination'+id)
    var tip_kraski=$('#tip_kraski'+id)
    var kraska_div=$('#kraska_div'+id)
    var kraska=$('#kraska'+id)
    var brend_kraska=$('#brend_kraska'+id)
    var artikul=$('#artikul'+id)
    var dop_info=$('#dop_info'+id)
    var kratkiy_tekst=$('#kratkiy_tekst'+id)
    var comment=$('#comment'+id)
    var pickupdate=$('#pickupdate'+id)
    var sena_c_nds=$('#sena_c_nds'+id)
    var sena_bez_nds=$('#sena_bez_nds'+id)
    var edi_izm=$('#edi_izm'+id)
    var online_id=$('#online_id'+id)
    var nazvaniye_ruchnoy=$('#nazvaniye_ruchnoy'+id)
    var svet_product=$('#svet_product'+id)
    var group_zakup=$('#group_zakup'+id)
    var group=$('#group'+id)
    var tip=$('#tip'+id)
    var bazoviy_edin=$('#bazoviy_edin'+id)
    // var alter_edin=$('#alter_edin'+id)
    // var stoimost_baza=$('#stoimost_baza'+id)
    // var stoimost_alter=$('#stoimost_alter'+id)
    var status=$('#status'+id)
    var zavod=$('#zavod_name'+id)
    var tip_clenta=$('#tip_clenta'+id)

    

    sena_bez_nds.val('')
    combination.val('')
    tip_kraski.val('')
    kraska.val('')
    brend_kraska.val('')
    artikul.val('')
    dop_info.val('')
    kratkiy_tekst.val('')
    comment.val('')
    pickupdate.val('')
    sena_c_nds.val('')
    sena_bez_nds.val('')
    // edi_izm.val('')
    online_id.val('')
    nazvaniye_ruchnoy.val('')
    svet_product.val('')
    group_zakup.val('')
    group.val('')
    tip.val('')
    bazoviy_edin.val('')
    // alter_edin.val('')
    // stoimost_baza.val('')
    // stoimost_alter.val('')
    status.val('')
    // zavod.val('')
    // tip_clenta.val('')

    combination.css('display','none')
    tip_kraski.css('display','none')
    kraska_div.css('display','none')
    brend_kraska.css('display','none')
    artikul.css('display','none')
    dop_info.css('display','none')
    kratkiy_tekst.css('display','none')
    comment.css('display','none')
    pickupdate.css('display','none')
    sena_c_nds.css('display','none')
    sena_bez_nds.css('display','none')
    edi_izm.css('display','none')
    online_id.css('display','none')
    nazvaniye_ruchnoy.css('display','none')
    svet_product.css('display','none')
    group_zakup.css('display','none')
    group.css('display','none')
    tip.css('display','none')
    bazoviy_edin.css('display','none')
    // alter_edin.css('display','none')
    // stoimost_baza.css('display','none')
    // stoimost_alter.css('display','none')
    status.css('display','none')
    zavod.css('display','none')
    tip_clenta.css('display','none')
    
    
    
    var create_btn =$('#create_btn'+id);
    var activate_btn =$('#activate_btn'+id);

    activate_btn.attr('disabled',false)
    create_btn.attr('disabled',false)

    activate_btn.css('background-color','')
    activate_btn.css('color','')
    create_btn.css('background-color','')
    create_btn.css('color','')


}

var zapros_count ={}

function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
    
    
        var combination=$('#combination'+id)
        var tip_kraski=$('#tip_kraski'+id)
        var kraska_div=$('#kraska_div'+id)
        var kraska=$('#kraska'+id)
        var brend_kraska=$('#brend_kraska'+id)
        var artikul=$('#artikul'+id)
        var dop_info=$('#dop_info'+id)
        var kratkiy_tekst=$('#kratkiy_tekst'+id)
        var comment=$('#comment'+id)
        var pickupdate=$('#pickupdate'+id)
        var sena_c_nds=$('#sena_c_nds'+id)
        var sena_bez_nds=$('#sena_bez_nds'+id)
        var edi_izm=$('#edi_izm'+id)
        var online_id=$('#online_id'+id)
        var nazvaniye_ruchnoy=$('#nazvaniye_ruchnoy'+id)
        var svet_product=$('#svet_product'+id)
        var group_zakup=$('#group_zakup'+id)
        var group=$('#group'+id)
        var tip=$('#tip'+id)
        var bazoviy_edin=$('#bazoviy_edin'+id)
        // var alter_edin=$('#alter_edin'+id)
        // var stoimost_baza=$('#stoimost_baza'+id)
        // var stoimost_alter=$('#stoimost_alter'+id)
        var status=$('#status'+id)
        var zavod=$('#zavod'+id)
        var tip_clenta=$('#tip_clenta'+id)
        var is_active =$('#is_active'+id)


        if(combination.val()!=''){
            data_base[id].combination = combination.val();
            combination.css('border-color','#dedad9')
        }else{
            combination.css('border-color','red')
            data_base[id].combination = NaN;
        }
        var tip_kraski_ful =$('#tip_kraski'+id+' option:selected').attr('data-krat')
        if(tip_kraski.val()!=''){
            data_base[id].tip_kraski = tip_kraski.val();
            
            data_base[id].tip_kraski_full = tip_kraski_ful;
            
            tip_kraski.css('border-color','#dedad9')
        }else{
            data_base[id].tip_kraski_full = NaN;
            tip_kraski.css('border-color','red')
            data_base[id].tip_kraski = NaN;
        }

        if(kraska.val()!=''){
            data_base[id].kraska = kraska.val();
            kraska_div.css('border-color','#dedad9')
        }else{
            kraska_div.css('border-color','red')
            data_base[id].kraska = NaN;
        }
        data_base[id].brend_kraska = 'RAINBOW RAL';
        
        // console.log(kraska.val(),'lllllll')
        if(kraska.val()!='' && tip_kraski.val()!='' && kraska.val()!=null && kraska.val()!=undefined){
            var atr ='PNT.'+kraska.val()+'.'+tip_kraski.val()
            artikul.text(atr)
            data_base[id].artikul = atr;
        }else{
            artikul.text('')
            data_base[id].artikul = NaN;
        }

        if(dop_info.val()!=''){
            data_base[id].dop_info = dop_info.val();
            dop_info.css('border-color','#dedad9')
        }else{
            dop_info.css('border-color','#dedad9')
            // dop_info.css('border-color','red')
            data_base[id].dop_info = NaN;
        }
        if(comment.val()!=''){
            data_base[id].comment = comment.val();
            comment.css('border-color','#dedad9')
        }else{
            comment.css('border-color','#dedad9')
            data_base[id].comment = NaN;
        }

        
        if(is_active.text()=='Активный'){

           
            if(pickupdate.val()!=''){
                data_base[id].pickupdate = pickupdate.val();
                pickupdate.css('border-color','#dedad9')
            }else{
                pickupdate.css('border-color','red')
                data_base[id].pickupdate = NaN;
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
            if(edi_izm.val()!=''){
                edi_izm.css('border-color','#dedad9')
                data_base[id].edi_izm = edi_izm.val();
            }else{
                data_base[id].edi_izm = NaN;
                edi_izm.css('border-color','red')
            }
            
            
           

           
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
                data_base[id].nazvaniye_ruchnoy =NaN;
                nazvaniye_ruchnoy.css('border-color','red')
            }
    
    
            if(svet_product.val()!=''){
                svet_product.css('border-color','#dedad9')
                data_base[id].svet_product = svet_product.val();
            }else{
                data_base[id].svet_product =NaN;
                svet_product.css('border-color','#dedad9')
            }
            if(group_zakup.val()!=''){
                group_zakup.css('border-color','#dedad9')
                data_base[id].group_zakup = group_zakup.val();
            }else{
                data_base[id].group_zakup =NaN;
                group_zakup.css('border-color','#dedad9')
            }
            if(group.val()!=''){
                group.css('border-color','#dedad9')
                data_base[id].group = group.val();
            }else{
                data_base[id].group =NaN;
                group.css('border-color','#dedad9')
            }
            if(tip.val()!=''){
                tip.css('border-color','#dedad9')
                data_base[id].tip = tip.val();
            }else{
                data_base[id].tip =NaN;
                tip.css('border-color','#dedad9')
            }
            if(bazoviy_edin.val()!=''){
                bazoviy_edin.css('border-color','#dedad9')
                data_base[id].bazoviy_edin = bazoviy_edin.val();
            }else{
                data_base[id].bazoviy_edin =NaN;
                bazoviy_edin.css('border-color','#dedad9')
            }
            
            
            if(status.val()!=''){
                status.css('border-color','#dedad9')
                data_base[id].status_online = status.val();
            }else{
                data_base[id].status_online =NaN;
                status.css('border-color','#dedad9')
            }

            var zavod_name =$('#zavod_name'+id)
            if(zavod_name.val()!=''){
                zavod_name.css('border-color','#dedad9')
               
                data_base[id].zavod = zavod_name.val();
            }else{
                data_base[id].zavod =NaN;
                zavod_name.css('border-color','#dedad9')
            }

            if(tip_clenta.val()!=''){
                data_base[id].tip_clenta = tip_clenta.val();
                tip_clenta.css('border-color','#dedad9')
            }else{
                tip_clenta.css('border-color','red')
                data_base[id].tip_clenta = NaN;
            }
        }else{
            
            
            
            if(pickupdate.val()!=''){
                data_base[id].pickupdate = pickupdate.val();
                pickupdate.css('border-color','#dedad9')
            }else{
                pickupdate.css('border-color','red')
                data_base[id].pickupdate = NaN;
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
            if(edi_izm.val()!=''){
                edi_izm.css('border-color','#dedad9')
                data_base[id].edi_izm = edi_izm.val();
            }else{
                data_base[id].edi_izm = NaN;
                edi_izm.css('border-color','red')
            }
            
            
           

           
            if(online_id.val()!=''){
                
                data_base[id].online_id = online_id.val();
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
            // 
            
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
                zavod_name.css('border-color','#dedad9')
            }

            if(tip_clenta.val()!=''){
                data_base[id].tip_clenta = tip_clenta.val();
                tip_clenta.css('border-color','#dedad9')
            }else{
                tip_clenta.css('border-color','red')
                data_base[id].tip_clenta = NaN;
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

    if(data.text !='XXXXXXXX' ){
        var artikul_bass = data_base[id].base_artikul
        var art_krat_dict = artikul_bass + data.text
        var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
        var kratkiy_text_ruchnoy = $('#kratkiy_tekst_ruchnoy'+id)
        

        if(art_krat_dict in zapros_count){
            if(zapros_count[art_krat_dict]){
                var sap_code = zapros_count[art_krat_dict]
                sap_code_ruchnoy.val(sap_code)
                kratkiy_text_ruchnoy.val(data.text)
                sap_code_ruchnoy.css('background-color','#eaecef')
                kratkiy_text_ruchnoy.css('background-color','#eaecef')
                // sap_code_ruchnoy.attr('disabled',true)
                // kratkiy_text_ruchnoy.attr('disabled',true)
            }else{
                
                sap_code_ruchnoy.val('')
                kratkiy_text_ruchnoy.val('')
             
                sap_code_ruchnoy.css('background-color','#eaecef')
                kratkiy_text_ruchnoy.css('background-color','#eaecef')
                // sap_code_ruchnoy.attr('disabled',false)
                // kratkiy_text_ruchnoy.attr('disabled',false)
            }
            
        }else{
            
                sap_codes = get_sapcode(id,data_base[id].base_artikul,data.text,data_base[id].is_termo)
            
        }


        data_base[id].kratkiy_tekst= data.text
        
    }else{
        var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
        var kratkiy_text_ruchnoy = $('#kratkiy_tekst_ruchnoy'+id)
        sap_code_ruchnoy.val('')
        kratkiy_text_ruchnoy.val('')
        sap_code_ruchnoy.css('background-color','#eaecef')
        kratkiy_text_ruchnoy.css('background-color','#eaecef')
    }
    
    kratkiy_tekst.text(data.text)



    }
}

function add_column(){
        
    text =""
    var sizeee = $('#table-artikul tr').length;
    
    text = front_piece(start = sizeee+1, end = sizeee+2)

    
    var table = $('#table-artikul')
    table.append(text)
    


}
function get_sapcode(){

}

// function get_sapcode(id,artikul,kratkiy_tekst,is_termo){
//     var url = '/client/get-sapcodes'
   
//     console.log('get sapcode process'+id)
//     $.ajax({
//         type: 'GET',
//         url: url,
//         data: {'artikul':artikul,'kratkiy_tekst':kratkiy_tekst,'is_termo':is_termo},
//     }).done(function (res) {
//         if (res.status ==201){
//             // console.log(res,'$$$$$')
//             var art_krat =artikul+kratkiy_tekst
//             zapros_count[art_krat]=res.artikul
//             var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
//             var kratkiy_text_ruchnoy = $('#kratkiy_tekst_ruchnoy'+id)
            
//             data_base[id].sap_code=res.artikul
//             data_base[id].krat=res.kratkiy_tekst
//             sap_code_ruchnoy.val(res.artikul)
//             kratkiy_text_ruchnoy.val(res.kratkiy_tekst)
//             sap_code_ruchnoy.css('background-color','#eaecef')
//             kratkiy_text_ruchnoy.css('background-color','#eaecef')
//             // sap_code_ruchnoy.attr('disabled',true)
//             // kratkiy_text_ruchnoy.attr('disabled',true)
//         }else{
//             var art_krat =artikul+kratkiy_tekst
//             zapros_count[art_krat]=NaN
//             var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
//             var kratkiy_text_ruchnoy = $('#kratkiy_tekst_ruchnoy'+id)
//             data_base[id].sap_code=NaN
//             data_base[id].krat=NaN
//             sap_code_ruchnoy.val('')
//             kratkiy_text_ruchnoy.val('')
//             sap_code_ruchnoy.css('background-color','#eaecef')
//             kratkiy_text_ruchnoy.css('background-color','#eaecef')
//             // sap_code_ruchnoy.attr('disabled',false)
//             // kratkiy_text_ruchnoy.attr('disabled',false)
//             console.log('aa')
//         }
//         // WON'T REDIRECT
//     });
// }





