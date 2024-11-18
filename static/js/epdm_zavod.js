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

            
    }
    get_kratkiy_tekst(){
            switch(this.id){
                case 1: if(this.tip_zayavka =='EPDM'){
                    if(this.tip_zayavka && this.artikul && this.ves){
                        if (this.koefitsiyent){
                            return {'text':'Рез.упл. '+this.artikul+' чёрный '+this.ves +' кг','accept':true}     
                        }
                        else{
                            return {'text':'Рез.упл. '+this.artikul+' чёрный '+this.ves +' кг','accept':false}
                            
                        }
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }else{

                    if(this.dop_info){
                        if (this.ves&& this.koefitsiyent){
                            return {'text':'ИДН '+this.dop_info,'accept':true}     
                        }
                        else{
                            return {'text':'ИДН '+this.dop_info,'accept':false}
                            
                        }
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }

                }
                    
                        break;
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
                    </div>
                    
                                

                    </td>
                    <td >
                        <div class="input-group input-group-sm mb-1">
                            <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px;z-index:0"  id='tip_zayavka`+String(i)+`'  onchange='create(`+String(i)+`)' required >
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
                    <td  class="sticky-col" style="left: 73.5px;background-color:white!important" id="epdm_div`+String(i)+`" >
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
                            <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px;z-index:0"  id='tip_zayavka`+String(i)+`'  onchange='create(`+String(i)+`)' required disabled>
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
        
        console.log(tip_zayavka,'llll')
       



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
    
            
        }
        else
        {
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

    var tip_zayavka=$('#tip_zayavka'+id)

    if(tip_zayavka =='EPDM'){

        var dop_info=$('#dop_info'+id)
        dop_info.attr('disabled',false);
        dop_info.val('')
        // dop_info.css('border-color','red')
    
        var artikul=$('#artikul'+id)
        artikul.attr('disabled',false);
        artikul.val('')
    
        var  epdm = $('#epdm_div'+id +' .select2 .selection .select2-selection--single')
        epdm.css('border-color','red')
    
    
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
        comment.css('border-color','red')
    }
    else{
        var dop_info=$('#dop_info'+id)
        dop_info.attr('disabled',false);
        dop_info.val('')
        dop_info.css('border-color','red')
    
        var artikul=$('#artikul'+id)
        artikul.attr('disabled',false);
        artikul.val('')
    
        var  epdm = $('#epdm_div'+id +' .select2 .selection .select2-selection--single')
        epdm.css('border-color','#dedad9')
    
        // artikul.css('border-color','red')
    
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
        comment.css('border-color','#dedad9')

    }
    // data_base[id].svet = 'чёрный';
  
    

    create_kratkiy_tekst(id)

}



function artukil_clear(id){
    
    var table_tr =$('#table_tr'+id);
    
    delete data_base[id]

    
    table_tr.css('background-color','white')


    var tip_zayavka=$('#tip_zayavka'+id)
    tip_zayavka.attr('disabled',false);
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
    var  epdm_val = $('#select2-artikul'+id+'-container')
    epdm_val.text('')
    
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
    
    


}

var zapros_count ={}



function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
    
        var kratkiy_tekst=$('#kratkiy_tekst'+id)

        var tip_zayavka=$('#tip_zayavka'+id)
        
        if(tip_zayavka.val()=='EPDM'){

            if(tip_zayavka.val()!=''){
                data_base[id].tip_zayavka = tip_zayavka.val()
                tip_zayavka.css('border-color','#dedad9')
            }else{
                data_base[id].tip_zayavka = NaN;
                tip_zayavka.css('border-color','red')
            }
    
            var dop_info=$('#dop_info'+id)
            if(dop_info.val()!=''){
                data_base[id].dop_info = dop_info.val()
                dop_info.css('border-color','#dedad9')
            }else{
                data_base[id].dop_info = NaN;
                dop_info.css('border-color','#dedad9')
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
        }
        else{
            if(tip_zayavka.val()!=''){
                data_base[id].tip_zayavka = tip_zayavka.val()
                tip_zayavka.css('border-color','#dedad9')
            }else{
                data_base[id].tip_zayavka = NaN;
                tip_zayavka.css('border-color','red')
            }
    
            var dop_info=$('#dop_info'+id)
            if(dop_info.val()!=''){
                data_base[id].dop_info = dop_info.val()
                dop_info.css('border-color','#dedad9')
            }else{
                data_base[id].dop_info = NaN;
                dop_info.css('border-color','red')
            }
    
            var artikul=$('#artikul'+id)
            console.log(artikul.val(),'4444')
            if(artikul.val()!='' && artikul.val()!=null){
                data_base[id].artikul = artikul.val()
                var  epdm = $('#epdm_div'+id +' .select2 .selection .select2-selection--single')
                epdm.css('border-color','#dedad9')
            }else{
                data_base[id].artikul = NaN;
                var  epdm = $('#epdm_div'+id +' .select2 .selection .select2-selection--single')
                epdm.css('border-color','#dedad9')
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
                comment.css('border-color','#dedad9')
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
        var svet = $('#svet'+id)
        if(tip_zayavka.val()=='EPDM'){
            svet.text('чёрный')
        }

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

