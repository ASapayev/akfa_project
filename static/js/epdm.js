class BasePokritiya{
    constructor(
        full=false,
        id=NaN, 
        tip_zayavka=NaN,
        dop_info=NaN,
        artikul=NaN,
        svet=NaN,
        ves=NaN,
        kratkiy_tekst=NaN,
        sap_code=NaN,
        bei=NaN,
        aei=NaN,
        koefitsiyent=NaN,
        comment=NaN,

        online_id=NaN,
        nazvaniye_ruchnoy=NaN,
        svet_product=NaN,//done
        group_zakup=NaN,
        group=NaN,
        tip=NaN,//done
        segment=NaN,
        buxgalter_tovar=NaN,
        bazoviy_edin=NaN,//done
        alter_edin=NaN,//done
        stoimost_baza=NaN,//done
        stoimost_alter=NaN,
        zavod_name=NaN,
        tip_clienta=NaN, 
        status_name =NaN,
        is_active =NaN


        ) {
      
            this.full=full;
            this.id=id;
            this.tip_zayavka=tip_zayavka;
            this.dop_info= dop_info;
            this.artikul= artikul;
            this.svet = svet;
            this.ves = ves;
            this.kratkiy_tekst = kratkiy_tekst;
            this.bei = bei;
            this.aei = aei;
            this.koefitsiyent = koefitsiyent;
            this.sap_code=sap_code;
            this.comment = comment;

            this.online_id=online_id;
            this.nazvaniye_ruchnoy=nazvaniye_ruchnoy;
            this.svet_product=svet_product;
            this.group_zakup=group_zakup;
            this.group=group;
            this.tip=tip;
            this.segment=segment;
            this.buxgalter_tovar=buxgalter_tovar;
            this.bazoviy_edin=bazoviy_edin;
            this.alter_edin=alter_edin;
            this.stoimost_baza=stoimost_baza;
            this.stoimost_alter=stoimost_alter;
            this.zavod_name=zavod_name;
            this.tip_clienta=tip_clienta;
            this.status_name=status_name;
            this.is_active=is_active;
    }
    get_kratkiy_tekst(){
            switch(this.id){
                case 1: 
                        if(this.tip_zayavka =='EPDM'){
                            if(this.is_active){
                                if(this.tip_zayavka && this.artikul && this.ves){
                                    if (this.koefitsiyent && this.online_id && this.nazvaniye_ruchnoy&& this.tip_clienta){
                                        return {'text':'Рез.упл. '+this.artikul+' чёрный '+this.ves +' кг','accept':true}     
                                    }
                                    else{
                                        return {'text':'Рез.упл. '+this.artikul+' чёрный '+this.ves +' кг','accept':false}
                                        
                                    }
                                }else{
                                    return {'text':'XXXXXXXX','accept':false}
                                }
                        
                            }else{
                                if(this.tip_zayavka && this.artikul && this.ves){
                                    if (this.koefitsiyent && this.nazvaniye_ruchnoy&&this.svet_product&& this.group_zakup && this.group && this.tip && this.segment && this.buxgalter_tovar && this.bazoviy_edin && this.alter_edin && this.stoimost_baza&& this.stoimost_alter&& this.tip_clienta){
                                         return {'text':'Рез.упл. '+this.artikul+' чёрный '+this.ves +' кг','accept':true}
                                             
                                    }
                                    else{
                                         return {'text':'Рез.упл. '+this.artikul+' чёрный '+this.ves +' кг','accept':false}
                                     }
                                 }else{
                                     return {'text':'XXXXXXXX','accept':false}
                                 }
                                
                            }
                            
                        }else{
                            // console.log(this.is_active,this.dop_info,'sssd')
                            if(this.is_active){
                                if(this.dop_info){
                                    if (this.online_id && this.nazvaniye_ruchnoy&& this.tip_clienta && this.ves && this.koefitsiyent){
                                        return {'text':'ИДН '+this.dop_info,'accept':true}     
                                    }
                                    else{
                                        return {'text':'ИДН '+this.dop_info,'accept':false}
                                        
                                    }
                                }else{
                                    return {'text':'XXXXXXXX','accept':false}
                                }
                        
                            }else{
                                if(this.dop_info){
                                    if (this.ves && this.koefitsiyent && this.nazvaniye_ruchnoy&&this.svet_product&& this.group_zakup && this.group && this.tip && this.segment && this.buxgalter_tovar && this.bazoviy_edin && this.alter_edin && this.stoimost_baza&& this.stoimost_alter&& this.tip_clienta){
                                         return {'text':'ИДН '+this.dop_info,'accept':true}
                                             
                                    }
                                    else{
                                         return {'text':'ИДН '+this.dop_info,'accept':false}
                                     }
                                 }else{
                                     return {'text':'XXXXXXXX','accept':false}
                                 }
                                
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
                            <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px;z-index:0"  id='tip_zayavka`+String(i)+`'  onchange='select_tip(`+String(i)+`)' required disabled>
                                <option  selected ></option>
                                <option   value="EPDM">EPDM</option>
                                <option   value="IDN">IDN</option>
                            </select>
                        </div>
                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1">
                            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0 " id='dop_info`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled></input>
                        </div>
                    </td>
                    <td  class="sticky-col" style="left: 139.6px;background-color:white!important" id="epdm_div`+String(i)+`" >
                        <div class="input-group input-group-sm mb-1">
                            <select class=" form-control basic_artikul" style="background-color:#ddebf7; width: 120px; padding-right:130px!important; font-size:10px; z-index:0"  id="artikul`+String(i)+`" onchange='create_kratkiy_tekst(`+String(i)+`)' disabled>
                            </select>
                
                        </div>
                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1" style="font-size: small; width:130px">
                            <div>
                                <span class =' text-center pl-1' style="font-size: small; z-index:0" id ='svet` +String(i)+`'></span>
                            </div>
                        </div>
                    </td>
                    
                    <td >
                        <div class="input-group input-group-sm mb-1">
                            <input type='text' class=" form-control " style=" width: 75px; font-size:10px;height:27px;z-index:0 " id='ves`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled></input>
                        </div>
                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1" style="font-size: small; width:250px">
                            <div>
                                <span class =' text-center pl-1' style="font-size: small; z-index:0;white-space:nowrap" id ='kratkiy_tekst` +String(i)+`'></span>
                            </div>
                        </div>
                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1">
                            <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px; z-index:0"  id='bei`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required disabled>
                               
                                <option ></option>
                                <option selected value="ШТ">ШТ</div>
                               
                            </select>
                        </div>
                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1">
                            <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px; z-index:0"  id='aei`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required disabled>
                                <option  ></option>
                              
                                <option selected value="КГ">КГ</div>
                                
                            </select>
                        </div>
                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1">
                            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0 " id='koefitsiyent`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled></input>
                        </div>
                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1">
                            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0 " id='comment`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled></input>
                        </div>
                    </td>
                    
                    `
        }else{
            buttons=`
                    <td >
                        <div class="input-group input-group-sm mb-1">
                            <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px;z-index:0"  id='tip_zayavka`+String(i)+`'  onchange='select_tip(`+String(i)+`)' required disabled>
                                <option  selected ></option>
                                <option   value="EPDM">EPDM</option>
                                <option   value="IDN">IDN</option>
                            </select>
                        </div>
                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1">
                            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0 " id='dop_info`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled></input>
                        </div>
                    </td>
                    <td  class="sticky-col" style="left: 139.6px;background-color:white!important" id="epdm_div`+String(i)+`" >
                        <div class="input-group input-group-sm mb-1">
                            <select class=" form-control basic_artikul" style="background-color:#ddebf7; width: 120px; padding-right:130px!important; font-size:10px; z-index:0"  id="artikul`+String(i)+`" onchange='create_kratkiy_tekst(`+String(i)+`)' disabled>
                            </select>
                
                        </div>
                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1" style="font-size: small; width:130px">
                            <div>
                                <span class =' text-center pl-1' style="font-size: small; z-index:0" id ='svet` +String(i)+`'></span>
                            </div>
                        </div>
                    </td>
                    
                    <td >
                        <div class="input-group input-group-sm mb-1">
                            <input type='text' class=" form-control " style=" width: 75px; font-size:10px;height:27px;z-index:0 " id='ves`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled></input>
                        </div>
                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1" style="font-size: small; width:250px">
                            <div>
                                <span class =' text-center pl-1' style="font-size: small; z-index:0;white-space:nowrap" id ='kratkiy_tekst` +String(i)+`'></span>
                            </div>
                        </div>
                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1">
                            <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px; z-index:0"  id='bei`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required disabled>
                               
                                <option ></option>
                                <option selected value="ШТ">ШТ</div>
                               
                            </select>
                        </div>
                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1">
                            <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px; z-index:0"  id='aei`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required disabled>
                                <option  ></option>
                              
                                <option selected value="КГ">КГ</div>
                                
                            </select>
                        </div>
                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1">
                            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0 " id='koefitsiyent`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled></input>
                        </div>
                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1">
                            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0 " id='comment`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled></input>
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
            <input type="number" class="form-control " style=' width:75px;height:27px!important;z-index:0;display:none;' oninput="create_kratkiy_tekst(`+String(i)+`); limitLength(this, 7);"    aria-describedby="inputGroup-sizing-sm" name ='online_savdo_id`+String(i)+`' id="online_savdo_id`+String(i)+`"  >
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 250px; font-size:10px; height:27px!important;z-index:0;display:none;"  id='nazvaniye_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
            
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 110px;font-size:12px; padding-right:0px; height:27px!important;z-index:0;display:none;"  id='svet_product`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected ></option>
            <option    value="Без цвета">Без цвета</option>
        </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 130px;font-size:12px; padding-right:0px;  height:27px!important;z-index:0;display:none;" id='group_zakup`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option value="Aksessuar Rezina">Aksessuar Rezina</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1"  >
            <select class="form-select" aria-label="" style="width: 150px;font-size:12px; padding-right:0px; height:27px!important;z-index:0;display:none;"  id='group`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)'required>
                <option  selected></option>
                <option value="Pvc. EPDM (UZ)">Pvc. EPDM (UZ)</option>
                
                
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;font-size:12px; padding-right:0px; height:27px!important;z-index:0;display:none;"  id='tip`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)'required>
                <option  selected></option>
                <option value="Готовый продукт">Готовый продукт</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style=" width: 145px;font-size:12px; padding-right:0px; height:27px!important;z-index:0;display:none;" id='segment`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected value="" ></option>
                <option value="Нет сегмента">Нет сегмента</option>
                <option value="Аксессуар">Аксессуар</option>
                
            </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 150px;font-size:12px; padding-right:0px; height:27px!important;z-index:0;display:none;" id='buxgalter_tovar`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                    <option  selected></option>
                    <option value="EPDM уплотнитель">EPDM уплотнитель</option>
                    

            </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;font-size:12px; padding-right:0px; height:27px!important;z-index:0;display:none;" id='bazoviy_edin`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
            <select class="form-select" aria-label="" style="width: 155px;font-size:12px; padding-right:0px;height:27px!important;z-index:0;display:none;" id='alter_edin`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
            <input type='text' class=" form-control " style="width: 75px; font-size:10px; height:27px!important;z-index:0;display:none;" id='stoimost_baza`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type="number"  class="form-control " style='width:75px;height:27px!important;z-index:0;display:none;' oninput="create_kratkiy_tekst(`+String(i)+`); limitLength(this, 4);"   aria-describedby="inputGroup-sizing-sm" name ='stoimost_alter`+String(i)+`' id="stoimost_alter`+String(i)+`"  >
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;font-size:12px; padding-right:0px; height:27px!important;z-index:0;display:none;" id='status`+String(i)+`' disabled onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="Активный">Активный</option>
                <option value="Пассивный">Пассивный</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <span class =' text-center ' style="font-size: small; width:190px; font-weight: bold; height:27px!important;z-index:0;" id='zavod_name`+String(i)+`'>ZAVOD REZINA</span>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 180px;font-size:12px;height:27px!important;z-index:0; padding-right:0px;display:none;border-color:red" id='tip_clienta`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option selected value=""></option>
                <option value="AKFA">AKFA</option>
                <option value="IMZO">IMZO</option>
                <option value="FRANCHISING">FRANCHISING</option>
                <option value="AKFA-IMZO-FRANCHISING">AKFA-IMZO-FRANCHISING</option>
                <option value="IMZO-FRANCHISING">IMZO-FRANCHISING</option>
            </select>
            </div>
            
        </td>
        
        </tr>
        
        `
        
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
        var $selectElement = $('#artikul' + i);  // Cache the selector
        // console.log(i)
        $selectElement.select2({
            tags: true,
            placeholder: "",
            ajax: {
                url: '/epdm/get-or-add-option-epdm-artikul',
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

data_base = {}

if(status_proccess1 == 'new'){
    table.append(text)
    request_piece()

}else{
    var jsonData = JSON.parse(jsonData);

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

        
        
        var tip_zayavka = data.tip_zayavka;
        var dop_info = data.dop_info;
        var artikul = data.artikul;
        var svet = data.svet;
        var ves = data.ves;
        var kratkiy_tekst = data.kratkiy_tekst;
        var sap_code = data.sap_code;
        var bei = data.bei;
        var aei = data.aei;
        var koefitsiyent = data.koefitsiyent;
        var comment = data.comment;
        var online_id = data.online_id;
        var nazvaniye_ruchnoy = data.nazvaniye_ruchnoy;
        var svet_product = data.svet_product;
        var group_zakup = data.group_zakup;
        var group = data.group;
        var tip = data.tip;
        var segment = data.segment;
        var buxgalter_tovar = data.buxgalter_tovar;
        var bazoviy_edin = data.bazoviy_edin;
        var alter_edin = data.alter_edin;
        var stoimost_baza = data.stoimost_baza;
        var stoimost_alter = data.stoimost_alter;
        var zavod_name = data.zavod_name;
        var tip_clienta = data.tip_clienta;
        var status_name = data.status_name;


        var is_active = data.is_active;
        
        var activate_btn =$('#activate_btn'+s);
        var create_btn =$('#create_btn'+s);
        activate_btn.attr('disabled',true)
        create_btn.attr('disabled',true)

        var status =$('#status'+s)
        status.val(status_name)
        status.css('display','block')


        if(tip_zayavka =='EPDM'){

            var epdm_div =$('#epdm_div'+s);
            // kraska_div.css('display','block')
    
            var  epdm_div = $('#epdm_div'+s +' .select2 .selection .select2-selection--single')
            var  epdm_val = $('#select2-artikul'+s+'-container')
            var epdm_val_org=$('#artikul'+s)
    
            const newOption = document.createElement('option');
    
            if(artikul){
                epdm_val.text(artikul)
                epdm_val_org.val(artikul)
                epdm_val_org.attr('disabled',false)
                epdm_div.css('border-color','')
                newOption.value = artikul;
                newOption.text = artikul;
                newOption.selected = true;
                epdm_val_org.append(newOption) 
            }else{
                epdm_val.text('')
                epdm_val_org.val('')
                epdm_val_org.attr('disabled',false)
                epdm_div.css('border-color','red')
            }
    
            check_input_and_change(tip_zayavka,'#tip_zayavka'+s,dis=false,is_req=true,is_req_simple=false)
            $('#tip_zayavka'+s).attr('disabled',false)
            check_input_and_change(dop_info,'#dop_info'+s,dis=false,is_req=false,is_req_simple=true)
            $('#dop_info'+s).attr('disabled',false)
            check_text_and_change(svet,'#svet'+s)
            check_input_and_change(ves,'#ves'+s,dis=false,is_req=true,is_req_simple=false)
            $('#ves'+s).attr('disabled',false)
            check_text_and_change(kratkiy_tekst,'#kratkiy_tekst'+s)
            check_input_and_change(bei,'#bei'+s,dis=true,is_req=false,is_req_simple=true)
            check_input_and_change(aei,'#aei'+s,dis=true,is_req=false,is_req_simple=true)
            check_input_and_change(koefitsiyent,'#koefitsiyent'+s,dis=false,is_req=true,is_req_simple=false)
            $('#koefitsiyent'+s).attr('disabled',false)
            check_input_and_change(comment,'#comment'+s,dis=false,is_req=false,is_req_simple=true)
            $('#comment'+s).attr('disabled',false)
    
            if(!is_active){
                create_btn.css('background-color','green')
                create_btn.css('color','white')
                $('#is_active'+s).text('')
    
                
                check_input_and_change(online_id,'#online_savdo_id'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(svet_product,'#svet_product'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(group_zakup,'#group_zakup'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(group,'#group'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(tip,'#tip'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(segment,'#segment'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(buxgalter_tovar,'#buxgalter_tovar'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(bazoviy_edin,'#bazoviy_edin'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(alter_edin,'#alter_edin'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(stoimost_baza,'#stoimost_baza'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(stoimost_alter,'#stoimost_alter'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(tip_clienta,'#tip_clienta'+s,dis=false,is_req=true,is_req_simple=false)
                
                
                }
            else{

                activate_btn.css('background-color','orange')
                activate_btn.css('color','white')
                $('#is_active'+s).text('Активный')
                check_input_and_change(online_id,'#online_savdo_id'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s,dis=false,is_req=true,is_req_simple=false)
    
                check_input_and_change(svet_product,'#svet_product'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(group_zakup,'#group_zakup'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(group,'#group'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(tip,'#tip'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(segment,'#segment'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(buxgalter_tovar,'#buxgalter_tovar'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(bazoviy_edin,'#bazoviy_edin'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(alter_edin,'#alter_edin'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(stoimost_baza,'#stoimost_baza'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(stoimost_alter,'#stoimost_alter'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(tip_clienta,'#tip_clienta'+s,dis=false,is_req=true,is_req_simple=false)
                
                }
        }else{
                var epdm_div =$('#epdm_div'+s);
        
                var  epdm_div = $('#epdm_div'+s +' .select2 .selection .select2-selection--single')
                var  epdm_val = $('#select2-artikul'+s+'-container')
                var epdm_val_org=$('#artikul'+s)
        
                const newOption = document.createElement('option');
        
                if(artikul){
                    epdm_val.text(artikul)
                    epdm_val_org.val(artikul)
                    epdm_val_org.attr('disabled',false)
                    epdm_div.css('border-color','')
                    newOption.value = artikul;
                    newOption.text = artikul;
                    newOption.selected = true;
                    epdm_val_org.append(newOption) 
                }else{
                    epdm_val.text('')
                    epdm_val_org.val('')
                    epdm_val_org.attr('disabled',false)
                    // epdm_div.css('border-color','red')
                }
        
                check_input_and_change(tip_zayavka,'#tip_zayavka'+s,dis=false,is_req=true,is_req_simple=false)
                $('#tip_zayavka'+s).attr('disabled',false)
                check_input_and_change(dop_info,'#dop_info'+s,dis=false,is_req=true,is_req_simple=false)
                $('#dop_info'+s).attr('disabled',false)
                check_text_and_change(svet,'#svet'+s)
                check_input_and_change(ves,'#ves'+s,dis=false,is_req=true,is_req_simple=false)
                $('#ves'+s).attr('disabled',false)
                check_text_and_change(kratkiy_tekst,'#kratkiy_tekst'+s)
                check_input_and_change(bei,'#bei'+s,dis=true,is_req=false,is_req_simple=true)
                check_input_and_change(aei,'#aei'+s,dis=true,is_req=false,is_req_simple=true)
                check_input_and_change(koefitsiyent,'#koefitsiyent'+s,dis=false,is_req=true,is_req_simple=false)
                $('#koefitsiyent'+s).attr('disabled',false)
                check_input_and_change(comment,'#comment'+s,dis=false,is_req=false,is_req_simple=true)
                $('#comment'+s).attr('disabled',false)
        
                if(!is_active){
                    create_btn.css('background-color','green')
                    create_btn.css('color','white')
                    $('#is_active'+s).text('')
        
                    
                    check_input_and_change(online_id,'#online_savdo_id'+s,dis=false,is_req=false,is_req_simple=true)
                    check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s,dis=false,is_req=true,is_req_simple=false)
                    check_input_and_change(svet_product,'#svet_product'+s,dis=false,is_req=true,is_req_simple=false)
                    check_input_and_change(group_zakup,'#group_zakup'+s,dis=false,is_req=true,is_req_simple=false)
                    check_input_and_change(group,'#group'+s,dis=false,is_req=true,is_req_simple=false)
                    check_input_and_change(tip,'#tip'+s,dis=false,is_req=true,is_req_simple=false)
                    check_input_and_change(segment,'#segment'+s,dis=false,is_req=true,is_req_simple=false)
                    check_input_and_change(buxgalter_tovar,'#buxgalter_tovar'+s,dis=false,is_req=true,is_req_simple=false)
                    check_input_and_change(bazoviy_edin,'#bazoviy_edin'+s,dis=false,is_req=true,is_req_simple=false)
                    check_input_and_change(alter_edin,'#alter_edin'+s,dis=false,is_req=true,is_req_simple=false)
                    check_input_and_change(stoimost_baza,'#stoimost_baza'+s,dis=false,is_req=true,is_req_simple=false)
                    check_input_and_change(stoimost_alter,'#stoimost_alter'+s,dis=false,is_req=true,is_req_simple=false)
                    check_input_and_change(tip_clienta,'#tip_clienta'+s,dis=false,is_req=true,is_req_simple=false)
                    
                    
                    }
                else{
                    // console.log(status_online,'kkkk')
                    activate_btn.css('background-color','orange')
                    activate_btn.css('color','white')
                    $('#is_active'+s).text('Активный')
                    check_input_and_change(online_id,'#online_savdo_id'+s,dis=false,is_req=true,is_req_simple=false)
                    check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s,dis=false,is_req=true,is_req_simple=false)
        
                    check_input_and_change(svet_product,'#svet_product'+s,dis=false,is_req=false,is_req_simple=true)
                    check_input_and_change(group_zakup,'#group_zakup'+s,dis=false,is_req=false,is_req_simple=true)
                    check_input_and_change(group,'#group'+s,dis=false,is_req=false,is_req_simple=true)
                    check_input_and_change(tip,'#tip'+s,dis=false,is_req=false,is_req_simple=true)
                    check_input_and_change(segment,'#segment'+s,dis=false,is_req=false,is_req_simple=true)
                    check_input_and_change(buxgalter_tovar,'#buxgalter_tovar'+s,dis=false,is_req=false,is_req_simple=true)
                    check_input_and_change(bazoviy_edin,'#bazoviy_edin'+s,dis=false,is_req=false,is_req_simple=true)
                    check_input_and_change(alter_edin,'#alter_edin'+s,dis=false,is_req=false,is_req_simple=true)
                    check_input_and_change(stoimost_baza,'#stoimost_baza'+s,dis=false,is_req=false,is_req_simple=true)
                    check_input_and_change(stoimost_alter,'#stoimost_alter'+s,dis=false,is_req=false,is_req_simple=true)
                    check_input_and_change(tip_clienta,'#tip_clienta'+s,dis=false,is_req=true,is_req_simple=false)
                    
                    }

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
    data_base[id].zavod_name = 'ZAVOD REZINA';
    data_base[id].status_name = 'Пассивный';
    data_base[id].is_active = false;
     
    

    var status_first =$('#status'+id);
    status_first.val('Пассивный')
    status_first.css('display','block')    

    var activate_btn =$('#activate_btn'+id);
    var create_btn =$('#create_btn'+id);
    create_btn.css('background-color','green')
    create_btn.css('color','white')
    activate_btn.attr('disabled',true)
    create_btn.attr('disabled',true)

    // var  kraska = $('#kraska_div'+id +' .select2 .selection .select2-selection--single')
    // kraska.css('border-color','red')

    var tip_zayavka=$('#tip_zayavka'+id)

 
   
    tip_zayavka.attr('disabled',false);
    tip_zayavka.val('')
    tip_zayavka.css('border-color','red')
    
    


}

function activate(id){
    // data_base[i] = new OnlineSavdo()

    data_base[id] = new BasePokritiya()
    data_base[id].id = 1;
    data_base[id].status_name = 'Активный';
    data_base[id].zavod_name = 'ZAVOD REZINA';
    data_base[id].is_active = true;

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

    

    var tip_zayavka=$('#tip_zayavka'+id)
    tip_zayavka.attr('disabled',false);
    tip_zayavka.val('')
    tip_zayavka.css('border-color','red')
    
    

    

}





function artukil_clear(id){
    
    var table_tr =$('#table_tr'+id);
    
    delete data_base[id]

    
    table_tr.css('background-color','white')
    

    var status_first = $('#status_name'+String(id))
    status_first.val('')
    status_first.css('display','none')

    var tip_zayavka=$('#tip_zayavka'+id)
    tip_zayavka.attr('disabled',true);
    tip_zayavka.val('')
    tip_zayavka.css('border-color','#dedad9')

    var dop_info=$('#dop_info'+id)
    dop_info.attr('disabled',true);
    dop_info.val('')
    dop_info.css('border-color','#dedad9')

    var artikul=$('#artikul'+id)
    artikul.attr('disabled',true);
    artikul.val('')
    artikul.css('border-color','#dedad9')
    
    var  epdm = $('#epdm_div'+id +' .select2 .selection .select2-selection--single')
    epdm.css('border-color','#dedad9')
    
    var svet=$('#svet'+id)
    svet.text('')
    
    
    var ves=$('#ves'+id)
    ves.attr('disabled',true);
    ves.val('')
    ves.css('border-color','#dedad9')
    
    var kratkiy_tekst=$('#kratkiy_tekst'+id)
    kratkiy_tekst.text('')
    
    var koefitsiyent=$('#koefitsiyent'+id)
    koefitsiyent.attr('disabled',true);
    koefitsiyent.val('')
    koefitsiyent.css('border-color','#dedad9')
    
    var comment=$('#comment'+id)
    comment.attr('disabled',true);
    comment.val('')
    comment.css('border-color','#dedad9')
    
    var online_id=$('#online_savdo_id'+id)
    online_id.css('display','none');
    online_id.val('')

    var nazvaniye_ruchnoy=$('#nazvaniye_ruchnoy'+id)
    nazvaniye_ruchnoy.css('display','none');
    nazvaniye_ruchnoy.val('')

    var svet_product=$('#svet_product'+id)
    svet_product.css('display','none');
    svet_product.val('')

    var group_zakup=$('#group_zakup'+id)
    group_zakup.css('display','none');
    group_zakup.val('')

    var group=$('#group'+id)
    group.css('display','none');
    group.val('')

    var tip=$('#tip'+id)
    tip.css('display','none');
    tip.val('')
    

    var segment=$('#segment'+id)
    segment.css('display','none');
    segment.val('')

    var buxgalter_tovar=$('#buxgalter_tovar'+id)
    buxgalter_tovar.css('display','none');
    buxgalter_tovar.val('')

    var bazoviy_edin=$('#bazoviy_edin'+id)
    bazoviy_edin.css('display','none');
    bazoviy_edin.val('')

    var alter_edin=$('#alter_edin'+id)
    alter_edin.css('display','none');
    alter_edin.val('')

    var stoimost_baza=$('#stoimost_baza'+id)
    stoimost_baza.css('display','none');
    stoimost_baza.val('')

    var stoimost_alter=$('#stoimost_alter'+id)
    stoimost_alter.css('display','none');
    stoimost_alter.val('')

    var status_name=$('#status'+id)
    status_name.css('display','none');
    status_name.val('')

    var tip_clienta=$('#tip_clienta'+id)
    tip_clienta.css('display','none');
    tip_clienta.val('')
    
    
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

function select_tip(id){
    var status_org =$('#status'+id)
    var tip_zayavki =$('#tip_zayavka'+id).val()

    
    if(tip_zayavki =='EPDM'){
        data_base[id].svet = 'чёрный';
        if(status_org.val()=='Активный'){
    
            var dop_info=$('#dop_info'+id)
            dop_info.attr('disabled',false);
            dop_info.val('')
            dop_info.css('border-color','#dedad9')
            
            var artikul=$('#artikul'+id)
            artikul.attr('disabled',false);
            artikul.val('')
            
    
            var  epdm = $('#epdm_div'+id +' .select2 .selection .select2-selection--single')
            epdm.css('border-color','red')
            var  epdm_val = $('#select2-artikul'+id+'-container')
            epdm_val.text('')
    
            artikul.css('border-color','red')
    
            var ves=$('#ves'+id)
            ves.attr('disabled',false);
            ves.val('')
            ves.css('border-color','red')
    
            var koefitsiyent=$('#koefitsiyent'+id)
            koefitsiyent.attr('disabled',false);
            koefitsiyent.val('')
            koefitsiyent.css('border-color','red')
    
            var comment=$('#comment'+id)
            comment.attr('disabled',false);
            comment.val('')
            // comment.css('border-color','red')
    
            var online_id=$('#online_savdo_id'+id)
            online_id.css('display','block');
            online_id.val('')
            online_id.css('border-color','red')
    
            var nazvaniye_ruchnoy=$('#nazvaniye_ruchnoy'+id)
            nazvaniye_ruchnoy.css('display','block');
            nazvaniye_ruchnoy.val('')
            nazvaniye_ruchnoy.css('border-color','red')
    
            var svet_product=$('#svet_product'+id)
            svet_product.css('display','block');
            svet_product.val('')
            svet_product.css('border-color','#dedad9')
            // data_base[id].svet_product ='Без цвета'
            // svet_product.css('border-color','red')
    
            var group_zakup=$('#group_zakup'+id)
            group_zakup.css('display','block');
            group_zakup.val('')
            group_zakup.css('border-color','#dedad9')
            // data_base[id].group_zakup='Aksessuar Rezina'
            // group_zakup.css('border-color','red')
    
            var group=$('#group'+id)
            group.css('display','block');
            group.val('')
            group.css('border-color','#dedad9')
            // data_base[id].group='Pvc. EPDM (UZ)'
            // group.css('border-color','red')
    
            var tip=$('#tip'+id)
            tip.css('display','block');
            tip.val('')
            tip.css('border-color','#dedad9')
            // data_base[id].tip='Готовый продукт'
            // tip.css('border-color','red')
    
            var segment=$('#segment'+id)
            segment.css('display','block');
            segment.val('')
            segment.css('border-color','#dedad9')
            // data_base[id].segment ='Аксессуар'
            // segment.css('border-color','red')
    
            var buxgalter_tovar=$('#buxgalter_tovar'+id)
            buxgalter_tovar.css('display','block');
            buxgalter_tovar.val('')
            buxgalter_tovar.css('border-color','#dedad9')
            // data_base[id].buxgalter_tovar='EPDM уплотнитель'
            // buxgalter_tovar.css('border-color','red')
    
            var bazoviy_edin=$('#bazoviy_edin'+id)
            bazoviy_edin.css('display','block');
            bazoviy_edin.val('')
            bazoviy_edin.css('border-color','#dedad9')
            // data_base[id].bazoviy_edin='Штука'
            // bazoviy_edin.css('border-color','red')
    
            var alter_edin=$('#alter_edin'+id)
            alter_edin.css('display','block');
            alter_edin.val('')
            alter_edin.css('border-color','#dedad9')
            // data_base[id].alter_edin='Килограмм'
            // alter_edin.css('border-color','red')
    
            var stoimost_baza=$('#stoimost_baza'+id)
            stoimost_baza.css('display','block');
            stoimost_baza.val('')
            stoimost_baza.css('border-color','#dedad9')
            // stoimost_baza.css('border-color','red')
    
            var stoimost_alter=$('#stoimost_alter'+id)
            stoimost_alter.css('display','block');
            stoimost_alter.val('')
            stoimost_alter.css('border-color','#dedad9')
            // stoimost_alter.css('border-color','red')
    
        
    
            var tip_clienta=$('#tip_clienta'+id)
            tip_clienta.css('display','block');
            tip_clienta.val('')
            tip_clienta.css('border-color','red!important')
        }else{
            var dop_info=$('#dop_info'+id)
            dop_info.attr('disabled',false);
            dop_info.val('')
            dop_info.css('border-color','#dedad9')
    
            var artikul=$('#artikul'+id)
            artikul.attr('disabled',false);
            artikul.val('')
    
            var  epdm = $('#epdm_div'+id +' .select2 .selection .select2-selection--single')
            epdm.css('border-color','red')
            var  epdm_val = $('#select2-artikul'+id+'-container')
            epdm_val.text('')
    
            var ves=$('#ves'+id)
            ves.attr('disabled',false);
            ves.css('border-color','red')
            ves.val('')

    
            var koefitsiyent=$('#koefitsiyent'+id)
            koefitsiyent.attr('disabled',false);
            koefitsiyent.css('border-color','red')
            koefitsiyent.val('')
    
            var comment=$('#comment'+id)
            comment.attr('disabled',false);
            comment.val('')

            var online_id=$('#online_savdo_id'+id)
            online_id.css('display','block');
            // online_id.css('border-color','red')
            online_id.val('')
            online_id.css('border-color','#dedad9')
    
            var nazvaniye_ruchnoy=$('#nazvaniye_ruchnoy'+id)
            nazvaniye_ruchnoy.css('display','block');
            nazvaniye_ruchnoy.css('border-color','red')
            nazvaniye_ruchnoy.val('')
    
            var svet_product=$('#svet_product'+id)
            svet_product.css('display','block');
            svet_product.val('Без цвета')
            data_base[id].svet_product ='Без цвета'
            svet_product.css('border-color','red')
    
            var group_zakup=$('#group_zakup'+id)
            group_zakup.css('display','block');
            group_zakup.val('Aksessuar Rezina')
            data_base[id].group_zakup='Aksessuar Rezina'
            group_zakup.css('border-color','red')
    
            var group=$('#group'+id)
            group.css('display','block');
            group.val('Pvc. EPDM (UZ)')
            data_base[id].group='Pvc. EPDM (UZ)'
            group.css('border-color','red')
    
            var tip=$('#tip'+id)
            tip.css('display','block');
            tip.val('Готовый продукт')
            data_base[id].tip = 'Готовый продукт'
            tip.css('border-color','red')
    
            var segment=$('#segment'+id)
            segment.css('display','block');
            segment.val('Аксессуар')
            data_base[id].segment ='Аксессуар'
            segment.css('border-color','red')
    
            var buxgalter_tovar=$('#buxgalter_tovar'+id)
            buxgalter_tovar.css('display','block');
            buxgalter_tovar.val('EPDM уплотнитель')
            data_base[id].buxgalter_tovar='EPDM уплотнитель'
            buxgalter_tovar.css('border-color','red')
    
            var bazoviy_edin=$('#bazoviy_edin'+id)
            bazoviy_edin.css('display','block');
            bazoviy_edin.val('Штука')
            data_base[id].bazoviy_edin='Штука'
            bazoviy_edin.css('border-color','red')
    
            var alter_edin=$('#alter_edin'+id)
            alter_edin.css('display','block');
            alter_edin.val('Килограмм')
            data_base[id].alter_edin='Килограмм'
            alter_edin.css('border-color','red')
    
            var stoimost_baza=$('#stoimost_baza'+id)
            stoimost_baza.css('display','block');
            stoimost_baza.val('')
            stoimost_baza.css('border-color','red')
    
            var stoimost_alter=$('#stoimost_alter'+id)
            stoimost_alter.css('display','block');
            stoimost_alter.val('')
            stoimost_alter.css('border-color','red')
    
        
    
            var tip_clienta=$('#tip_clienta'+id)
            tip_clienta.css('display','block');
            tip_clienta.val('')
            tip_clienta.css('border-color','red!important')
        }
    }else{
        data_base[id].svet = NaN;
        if(status_org.val()=='Активный'){
    
            var dop_info=$('#dop_info'+id)
            dop_info.attr('disabled',false);
            dop_info.val('')
            dop_info.css('border-color','red')
    
            var artikul=$('#artikul'+id)
            artikul.attr('disabled',false);
            artikul.val('')
    
            // var  epdm = $('#epdm_div'+id +' .select2 .selection .select2-selection--single')
            // epdm.css('border-color','red')
    
            // artikul.css('border-color','red')
            var  epdm_val = $('#select2-artikul'+id+'-container')
            epdm_val.text('')
    
            var svet=$('#svet'+id)
            svet.text('')
    
            var ves=$('#ves'+id)
            ves.attr('disabled',false);
            ves.val('')
            // ves.css('border-color','#dedad9')
            ves.css('border-color','red')
    
            var koefitsiyent=$('#koefitsiyent'+id)
            koefitsiyent.attr('disabled',false);
            koefitsiyent.val('')
            // koefitsiyent.css('border-color','#dedad9')
            koefitsiyent.css('border-color','red')
    
            var comment=$('#comment'+id)
            comment.attr('disabled',false);
            comment.val('')
            // comment.css('border-color','red')
    
            var online_id=$('#online_savdo_id'+id)
            online_id.css('display','block');
            online_id.val('')
            online_id.css('border-color','red')
    
            var nazvaniye_ruchnoy=$('#nazvaniye_ruchnoy'+id)
            nazvaniye_ruchnoy.css('display','block');
            nazvaniye_ruchnoy.val('')
            nazvaniye_ruchnoy.css('border-color','red')
    
            var svet_product=$('#svet_product'+id)
            svet_product.css('display','block');
            svet_product.val('')
            svet_product.css('border-color','#dedad9')
            // data_base[id].svet_product ='Без цвета'
            // svet_product.css('border-color','red')
    
            var group_zakup=$('#group_zakup'+id)
            group_zakup.css('display','block');
            group_zakup.val('')
            group_zakup.css('border-color','#dedad9')
            // data_base[id].group_zakup='Aksessuar Rezina'
            // group_zakup.css('border-color','red')
    
            var group=$('#group'+id)
            group.css('display','block');
            group.val('')
            group.css('border-color','#dedad9')
            // data_base[id].group='Pvc. EPDM (UZ)'
            // group.css('border-color','red')
    
            var tip=$('#tip'+id)
            tip.css('display','block');
            tip.val('')
            tip.css('border-color','#dedad9')
            // data_base[id].tip='Готовый продукт'
            // tip.css('border-color','red')
    
            var segment=$('#segment'+id)
            segment.css('display','block');
            segment.val('')
            segment.css('border-color','#dedad9')
            // data_base[id].segment ='Аксессуар'
            // segment.css('border-color','red')
    
            var buxgalter_tovar=$('#buxgalter_tovar'+id)
            buxgalter_tovar.css('display','block');
            buxgalter_tovar.val('')
            buxgalter_tovar.css('border-color','#dedad9')
            // data_base[id].buxgalter_tovar='EPDM уплотнитель'
            // buxgalter_tovar.css('border-color','red')
    
            var bazoviy_edin=$('#bazoviy_edin'+id)
            bazoviy_edin.css('display','block');
            bazoviy_edin.val('')
            bazoviy_edin.css('border-color','#dedad9')
            // data_base[id].bazoviy_edin='Штука'
            // bazoviy_edin.css('border-color','red')
    
            var alter_edin=$('#alter_edin'+id)
            alter_edin.css('display','block');
            alter_edin.val('')
            alter_edin.css('border-color','#dedad9')
            // data_base[id].alter_edin='Килограмм'
            // alter_edin.css('border-color','red')
    
            var stoimost_baza=$('#stoimost_baza'+id)
            stoimost_baza.css('display','block');
            stoimost_baza.val('')
            stoimost_baza.css('border-color','red')
    
            var stoimost_alter=$('#stoimost_alter'+id)
            stoimost_alter.css('display','block');
            stoimost_alter.val('')
            stoimost_alter.css('border-color','red')
    
        
    
            var tip_clienta=$('#tip_clienta'+id)
            tip_clienta.css('display','block');
            tip_clienta.val('')
            tip_clienta.css('border-color','red!important')
        }else{
            var dop_info=$('#dop_info'+id)
            dop_info.attr('disabled',false);
            dop_info.val('')
            dop_info.css('border-color','red')
    
            var artikul=$('#artikul'+id)
            artikul.attr('disabled',false);
            artikul.val('')
            
            var svet=$('#svet'+id)
            svet.text('')
            // var  epdm = $('#epdm_div'+id +' .select2 .selection .select2-selection--single')
            
            var  epdm_val = $('#select2-artikul'+id+'-container')
            epdm_val.text('')

            var ves=$('#ves'+id)
            ves.attr('disabled',false);
            // ves.css('border-color','red')
            ves.val('')
            ves.css('border-color','#dedad9')

    
            var koefitsiyent=$('#koefitsiyent'+id)
            koefitsiyent.attr('disabled',false);
            // koefitsiyent.css('border-color','red')
            koefitsiyent.val('')
            koefitsiyent.css('border-color','#dedad9')
    
            var comment=$('#comment'+id)
            comment.attr('disabled',false);
            comment.val('')

            var online_id=$('#online_savdo_id'+id)
            online_id.css('display','block');
            // online_id.css('border-color','red')
            online_id.val('')
            
    
            var nazvaniye_ruchnoy=$('#nazvaniye_ruchnoy'+id)
            nazvaniye_ruchnoy.css('display','block');
            nazvaniye_ruchnoy.css('border-color','red')
            nazvaniye_ruchnoy.val('')
    
            var svet_product=$('#svet_product'+id)
            svet_product.css('display','block');
            svet_product.val('')
            // data_base[id].svet_product ='Без цвета'
            svet_product.css('border-color','red')
    
            var group_zakup=$('#group_zakup'+id)
            group_zakup.css('display','block');
            group_zakup.val('')
            // data_base[id].group_zakup='Aksessuar Rezina'
            group_zakup.css('border-color','red')
    
            var group=$('#group'+id)
            group.css('display','block');
            group.val('')
            // data_base[id].group='Pvc. EPDM (UZ)'
            group.css('border-color','red')
    
            var tip=$('#tip'+id)
            tip.css('display','block');
            tip.val('')
            // data_base[id].tip = 'Готовый продукт'
            tip.css('border-color','red')
    
            var segment=$('#segment'+id)
            segment.css('display','block');
            segment.val('')
            // data_base[id].segment ='Аксессуар'
            segment.css('border-color','red')
    
            var buxgalter_tovar=$('#buxgalter_tovar'+id)
            buxgalter_tovar.css('display','block');
            buxgalter_tovar.val('')
            // data_base[id].buxgalter_tovar='EPDM уплотнитель'
            buxgalter_tovar.css('border-color','red')
    
            var bazoviy_edin=$('#bazoviy_edin'+id)
            bazoviy_edin.css('display','block');
            bazoviy_edin.val('')
            // data_base[id].bazoviy_edin='Штука'
            bazoviy_edin.css('border-color','red')
    
            var alter_edin=$('#alter_edin'+id)
            alter_edin.css('display','block');
            alter_edin.val('')
            // data_base[id].alter_edin='Килограмм'
            alter_edin.css('border-color','red')
    
            var stoimost_baza=$('#stoimost_baza'+id)
            stoimost_baza.css('display','block');
            stoimost_baza.val('')
            stoimost_baza.css('border-color','red')
    
            var stoimost_alter=$('#stoimost_alter'+id)
            stoimost_alter.css('display','block');
            stoimost_alter.val('')
            stoimost_alter.css('border-color','red')
    
        
    
            var tip_clienta=$('#tip_clienta'+id)
            tip_clienta.css('display','block');
            tip_clienta.val('')
            tip_clienta.css('border-color','red!important')
        }

    }

    create_kratkiy_tekst(id)

}


function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
    
        var kratkiy_tekst=$('#kratkiy_tekst'+id)

        var tip_zayavka=$('#tip_zayavka'+id)
        var online_id=$('#online_savdo_id'+id)
        var nazvaniye_ruchnoy=$('#nazvaniye_ruchnoy'+id)
        var svet_product=$('#svet_product'+id)
        var group_zakup=$('#group_zakup'+id)
        var group=$('#group'+id)
        var tip=$('#tip'+id)
        var segment=$('#segment'+id)
        var buxgalter_tovar=$('#buxgalter_tovar'+id)
        var bazoviy_edin=$('#bazoviy_edin'+id)
        var alter_edin=$('#alter_edin'+id)
        var stoimost_baza=$('#stoimost_baza'+id)
        var stoimost_alter=$('#stoimost_alter'+id)
        var tip_clienta=$('#tip_clienta'+id)

        if(tip_zayavka.val()!=''){
            data_base[id].tip_zayavka = tip_zayavka.val()
            tip_zayavka.css('border-color','#dedad9')
        }else{
            data_base[id].tip_zayavka = NaN;
            tip_zayavka.css('border-color','red')
        }

        if(tip_zayavka.val()=='EPDM'){
            var dop_info=$('#dop_info'+id)
            if(dop_info.val()!=''){
                data_base[id].dop_info = dop_info.val()
                dop_info.css('border-color','#dedad9')
            }else{
                data_base[id].dop_info = NaN;
                // dop_info.css('border-color','red')
            }

            var artikul=$('#artikul'+id)
            // console.log(artikul.val(),'4444')
            if(artikul.val()!='' && artikul.val()!=null){
                data_base[id].artikul = artikul.val()
                var  epdm = $('#epdm_div'+id +' .select2 .selection .select2-selection--single')
                epdm.css('border-color','#dedad9')
            }else{
                data_base[id].artikul = NaN;
                var  epdm = $('#epdm_div'+id +' .select2 .selection .select2-selection--single')
                epdm.css('border-color','red')
            }
            
            var ves = $('#ves'+id)
            if(ves.val()!=''){
                data_base[id].ves = ves.val()
                ves.css('border-color','#dedad9')
            }else{
                data_base[id].ves = NaN;
                ves.css('border-color','red')
            }
            var bei = $('#bei'+id)
            if(bei.val()!=''){
                data_base[id].bei = bei.val()
            }else{
                data_base[id].bei = NaN;
            }
            var aei = $('#aei'+id)
            if(aei.val()!=''){
                data_base[id].aei = aei.val()
            }else{
                data_base[id].aei = NaN;
            }
            var koefitsiyent = $('#koefitsiyent'+id)
            if(koefitsiyent.val()!=''){
                data_base[id].koefitsiyent = koefitsiyent.val()
                koefitsiyent.css('border-color','#dedad9')
            }else{
                data_base[id].koefitsiyent = NaN;
                koefitsiyent.css('border-color','red')
            }
            var comment = $('#comment'+id)
            if(comment.val()!=''){
                data_base[id].comment = comment.val()
                comment.css('border-color','#dedad9')
            }else{
                data_base[id].comment = NaN;
                // comment.css('border-color','red')
            }
        
            if(data_base[id].status_name=='Активный'){

           
                // if(pickupdate.val()!=''){
                //     data_base[id].pickupdate = pickupdate.val();
                //     pickupdate.css('border-color','#dedad9')
                // }else{
                //     pickupdate.css('border-color','red')
                //     data_base[id].pickupdate = NaN;
                // }
                
                
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
                if(segment.val()!=''){
                    segment.css('border-color','#dedad9')
                    data_base[id].segment = segment.val();
                }else{
                    data_base[id].segment =NaN;
                    segment.css('border-color','#dedad9')
                }
                if(buxgalter_tovar.val()!=''){
                    buxgalter_tovar.css('border-color','#dedad9')
                    data_base[id].buxgalter_tovar = buxgalter_tovar.val();
                }else{
                    data_base[id].buxgalter_tovar =NaN;
                    buxgalter_tovar.css('border-color','#dedad9')
                }
    
                if(bazoviy_edin.val()!=''){
                    bazoviy_edin.css('border-color','#dedad9')
                    data_base[id].bazoviy_edin = bazoviy_edin.val();
                }else{
                    data_base[id].bazoviy_edin =NaN;
                    bazoviy_edin.css('border-color','#dedad9')
                }
                if(alter_edin.val()!=''){
                    alter_edin.css('border-color','#dedad9')
                    data_base[id].alter_edin = alter_edin.val();
                }else{
                    data_base[id].alter_edin =NaN;
                    alter_edin.css('border-color','#dedad9')
                }
                if(stoimost_baza.val()!=''){
                    stoimost_baza.css('border-color','#dedad9')
                    data_base[id].stoimost_baza = stoimost_baza.val();
                }else{
                    data_base[id].stoimost_baza =NaN;
                    stoimost_baza.css('border-color','#dedad9')
                }
                if(stoimost_alter.val()!=''){
                    stoimost_alter.css('border-color','#dedad9')
                    data_base[id].stoimost_alter = stoimost_alter.val();
                }else{
                    data_base[id].stoimost_alter =NaN;
                    stoimost_alter.css('border-color','#dedad9')
                }
                
                if(tip_clienta.val()!=''){
                    data_base[id].tip_clienta = tip_clienta.val();
                    tip_clienta.css('border-color','#dedad9')
                }else{
                    tip_clienta.css('border-color','red!important')
                    data_base[id].tip_clienta = NaN;
                }
            }else{
                
                
                
                if(online_id.val()!=''){
                    online_id.css('border-color','#dedad9')
                    data_base[id].online_id = online_id.val();
                }else{
                    online_id.css('border-color','#dedad9')
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
                if(segment.val()!=''){
                    segment.css('border-color','#dedad9')
                    data_base[id].segment = segment.val();
                }else{
                    data_base[id].segment =NaN;
                    segment.css('border-color','red')
                }
                if(buxgalter_tovar.val()!=''){
                    buxgalter_tovar.css('border-color','#dedad9')
                    data_base[id].buxgalter_tovar = buxgalter_tovar.val();
                }else{
                    data_base[id].buxgalter_tovar =NaN;
                    buxgalter_tovar.css('border-color','red')
                }
    
                if(bazoviy_edin.val()!=''){
                    bazoviy_edin.css('border-color','#dedad9')
                    data_base[id].bazoviy_edin = bazoviy_edin.val();
                }else{
                    data_base[id].bazoviy_edin =NaN;
                    bazoviy_edin.css('border-color','red')
                }
                if(alter_edin.val()!=''){
                    alter_edin.css('border-color','#dedad9')
                    data_base[id].alter_edin = alter_edin.val();
                }else{
                    data_base[id].alter_edin =NaN;
                    alter_edin.css('border-color','red')
                }
                if(stoimost_baza.val()!=''){
                    stoimost_baza.css('border-color','#dedad9')
                    data_base[id].stoimost_baza = stoimost_baza.val();
                }else{
                    data_base[id].stoimost_baza =NaN;
                    stoimost_baza.css('border-color','red')
                }
                if(stoimost_alter.val()!=''){
                    stoimost_alter.css('border-color','#dedad9')
                    data_base[id].stoimost_alter = stoimost_alter.val();
                }else{
                    data_base[id].stoimost_alter =NaN;
                    stoimost_alter.css('border-color','red')
                }
                
                if(tip_clienta.val()!=''){
                    data_base[id].tip_clienta = tip_clienta.val();
                    tip_clienta.css('border-color','#dedad9')
                }else{
                    tip_clienta.css('border-color','red!important')
                    data_base[id].tip_clienta = NaN;
                }
            
        
        
            }
    

        }else{

            var dop_info=$('#dop_info'+id)

            console.log(dop_info.val(),'sfsdfsd')

            if(dop_info.val()!=''){
                data_base[id].dop_info = dop_info.val()
                dop_info.css('border-color','#dedad9')
            }else{
                data_base[id].dop_info = NaN;
                dop_info.css('border-color','red')
            }

            var artikul=$('#artikul'+id)
            // console.log(artikul.val(),'4444')
            if(artikul.val()!='' && artikul.val()!=null){
                data_base[id].artikul = artikul.val()
                var  epdm = $('#epdm_div'+id +' .select2 .selection .select2-selection--single')
                epdm.css('border-color','#dedad9')
            }else{
                data_base[id].artikul = NaN;
                var  epdm = $('#epdm_div'+id +' .select2 .selection .select2-selection--single')
                epdm.css('border-color','#dedad9')
                // epdm.css('border-color','red')
            }
            
            var svet = $('#svet'+id)
            if(svet.text()!=''){
                data_base[id].svet = svet.text()
                svet.css('border-color','#dedad9')
            }else{
                data_base[id].svet = NaN;
                svet.css('border-color','#dedad9')
            }
            var ves = $('#ves'+id)
            if(ves.val()!=''){
                data_base[id].ves = ves.val()
                ves.css('border-color','#dedad9')
            }else{
                data_base[id].ves = NaN;
                ves.css('border-color','red')
            }
            var bei = $('#bei'+id)
            if(bei.val()!=''){
                bei.css('border-color','#dedad9')
                data_base[id].bei = bei.val()
            }else{
                bei.css('border-color','#dedad9')
                data_base[id].bei = NaN;
            }
            var aei = $('#aei'+id)
            if(aei.val()!=''){
                aei.css('border-color','#dedad9')
                data_base[id].aei = aei.val()
            }else{
                aei.css('border-color','#dedad9')
                data_base[id].aei = NaN;
            }
            var koefitsiyent = $('#koefitsiyent'+id)
            if(koefitsiyent.val()!=''){
                data_base[id].koefitsiyent = koefitsiyent.val()
                koefitsiyent.css('border-color','#dedad9')
            }else{
                data_base[id].koefitsiyent = NaN;
                koefitsiyent.css('border-color','red')
            }
            var comment = $('#comment'+id)
            if(comment.val()!=''){
                data_base[id].comment = comment.val()
                comment.css('border-color','#dedad9')
            }else{
                data_base[id].comment = NaN;
                comment.css('border-color','#dedad9')
            }
        
            if(data_base[id].status_name=='Активный'){

           
                // if(pickupdate.val()!=''){
                //     data_base[id].pickupdate = pickupdate.val();
                //     pickupdate.css('border-color','#dedad9')
                // }else{
                //     pickupdate.css('border-color','red')
                //     data_base[id].pickupdate = NaN;
                // }
                
                
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
                if(segment.val()!=''){
                    segment.css('border-color','#dedad9')
                    data_base[id].segment = segment.val();
                }else{
                    data_base[id].segment =NaN;
                    segment.css('border-color','#dedad9')
                }
                if(buxgalter_tovar.val()!=''){
                    buxgalter_tovar.css('border-color','#dedad9')
                    data_base[id].buxgalter_tovar = buxgalter_tovar.val();
                }else{
                    data_base[id].buxgalter_tovar =NaN;
                    buxgalter_tovar.css('border-color','#dedad9')
                }
    
                if(bazoviy_edin.val()!=''){
                    bazoviy_edin.css('border-color','#dedad9')
                    data_base[id].bazoviy_edin = bazoviy_edin.val();
                }else{
                    data_base[id].bazoviy_edin =NaN;
                    bazoviy_edin.css('border-color','#dedad9')
                }
                if(alter_edin.val()!=''){
                    alter_edin.css('border-color','#dedad9')
                    data_base[id].alter_edin = alter_edin.val();
                }else{
                    data_base[id].alter_edin =NaN;
                    alter_edin.css('border-color','#dedad9')
                }
                if(stoimost_baza.val()!=''){
                    stoimost_baza.css('border-color','#dedad9')
                    data_base[id].stoimost_baza = stoimost_baza.val();
                }else{
                    data_base[id].stoimost_baza =NaN;
                    stoimost_baza.css('border-color','#dedad9')
                }
                if(stoimost_alter.val()!=''){
                    stoimost_alter.css('border-color','#dedad9')
                    data_base[id].stoimost_alter = stoimost_alter.val();
                }else{
                    data_base[id].stoimost_alter =NaN;
                    stoimost_alter.css('border-color','#dedad9')
                }
                
                if(tip_clienta.val()!=''){
                    data_base[id].tip_clienta = tip_clienta.val();
                    tip_clienta.css('border-color','#dedad9')
                }else{
                    tip_clienta.css('border-color','red!important')
                    data_base[id].tip_clienta = NaN;
                }
            }else{
                
                
                
                if(online_id.val()!=''){
                    online_id.css('border-color','#dedad9')
                    data_base[id].online_id = online_id.val();
                }else{
                    online_id.css('border-color','#dedad9')
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
                if(segment.val()!=''){
                    segment.css('border-color','#dedad9')
                    data_base[id].segment = segment.val();
                }else{
                    data_base[id].segment =NaN;
                    segment.css('border-color','red')
                }
                if(buxgalter_tovar.val()!=''){
                    buxgalter_tovar.css('border-color','#dedad9')
                    data_base[id].buxgalter_tovar = buxgalter_tovar.val();
                }else{
                    data_base[id].buxgalter_tovar =NaN;
                    buxgalter_tovar.css('border-color','red')
                }
    
                if(bazoviy_edin.val()!=''){
                    bazoviy_edin.css('border-color','#dedad9')
                    data_base[id].bazoviy_edin = bazoviy_edin.val();
                }else{
                    data_base[id].bazoviy_edin =NaN;
                    bazoviy_edin.css('border-color','red')
                }
                if(alter_edin.val()!=''){
                    alter_edin.css('border-color','#dedad9')
                    data_base[id].alter_edin = alter_edin.val();
                }else{
                    data_base[id].alter_edin =NaN;
                    alter_edin.css('border-color','red')
                }
                if(stoimost_baza.val()!=''){
                    stoimost_baza.css('border-color','#dedad9')
                    data_base[id].stoimost_baza = stoimost_baza.val();
                }else{
                    data_base[id].stoimost_baza =NaN;
                    stoimost_baza.css('border-color','red')
                }
                if(stoimost_alter.val()!=''){
                    stoimost_alter.css('border-color','#dedad9')
                    data_base[id].stoimost_alter = stoimost_alter.val();
                }else{
                    data_base[id].stoimost_alter =NaN;
                    stoimost_alter.css('border-color','red')
                }
                
                if(tip_clienta.val()!=''){
                    data_base[id].tip_clienta = tip_clienta.val();
                    tip_clienta.css('border-color','#dedad9')
                }else{
                    tip_clienta.css('border-color','red!important')
                    data_base[id].tip_clienta = NaN;
                }
            
        
        
            }
    
        }

        

        
        // console.log(data_base[id].status_name,'llll')
        

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
    console.log(data)

    if(data.text !='XXXXXXXX' ){

        var artikul_bass = data_base[id].base_artikul
        var art_krat_dict = artikul_bass + data.text
        var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
        var kratkiy_text_ruchnoy = $('#kratkiy_tekst_ruchnoy'+id)
        var svet = $('#svet'+id)
        svet.text('чёрный')

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
        var svet = $('#svet'+id)
        svet.text('')

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

