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
            
    
    }
    get_kratkiy_tekst(){
        switch(this.id){
            case 1: 
            console.log(this.model , this.kol_section , this.svet , this.brend)
                if(this.model && this.kol_section && this.svet && this.brend){       
                    return {'text':this.model + '-'+ this.kol_section + ' ' + this.svet +' ' +this.brend,'accept':true}
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
         <td   style='  background-color:white!important;' >
                    <div class="btn-group" role="group" aria-label="Basic example">
                            <button type="button" class="btn btn-outline-secondary btn-sm" id='clear_btn`+String(i)+`' onclick="artukil_clear(`+String(i)+`)" data-bs-toggle='popover' title='Tozalab tashlash'><i class="bi bi-x-circle"></i></button>
                            <button type="button" class="btn btn-outline-secondary btn-sm"  onclick="copy_tr(`+String(i)+`)" data-bs-toggle='popover' title='Dubl qilish'><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-copy" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M4 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 5a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-1h1v1a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h1v1z"/></svg></button>
                    </div>
                    
                    

        </td>
        
        <td  style=' background-color:white!important;'>
            <div class="input-group input-group-sm mb-1">
                <select class=" form-control basic_model" style="background-color:#ddebf7; width: 140px; font-size:10px "  id="model`+String(i)+`" ></select>
            </div>
            <span style='display:none' id='artikul_radiator` +String(i)+`'></span>
        </td>
        
        
        
        <td  >
            <div class="input-group input-group-sm mb-1 text-center" id ='base_artikul` +String(i)+`'>
                   
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm " style="width: 70px;" >
        
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
            <select class="form-select" aria-label="" style="width: 150px;height:27px!important;z-index:0;border-color:red;display:none;" onchange="create_kratkiy_tekst(`+String(i)+`)"  id='brend`+String(i)+`'>
                <option  value="" selected></option>
                <option value="BK">BK</option>
                <option value="LIDER">LIDER</option>
                <option value="AKFA">AKFA</option>
                <option value="MILANO">MILANO</option>
                <option value="Perfetto">Perfetto</option>
                <option value="Florence">Florence</option>
                <option value="Piuma">Piuma</option>
                <option value="LIDER-PERFETTO">LIDER-PERFETTO</option>
                <option value="SIRA">SIRA</option>

                
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
                <input type='text' class=" form-control " style=" width: 250px; font-size:10px; height:27px!important;z-index:0"  id='comment`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
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
                        return {id:item.model_radiator,text:item.model_radiator,artikul:item.artikul}
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
            var option = new Option(data.model_radiator, data.model_radiator, true, true);
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
            }else{
                data_base[i] = new BasePokritiya()
                data_base[i].id = 1
                clear_artikul(i)
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
        
        console.log(data_base,'databaseee')
        var s = size+1

        var id = data.id;
        var model =  data.model
        var base_artikul =  data.base_artikul 
        var kol_section =  data.kol_section 
        var svet =  data.svet 
        var brend =  data.brend  
        var kratkiy_tekst =  data.kratkiy_tekst 
        var comment =  data.comment 
        


        check_text_and_change_simple(base_artikul,'#base_artikul'+s)
        
        

        
        
       
        check_input_and_change(kol_section,'#kol_section'+s,dis=false,is_req=true)
        check_input_and_change(svet,'#svet'+s,dis=false,is_req=true)
        check_input_and_change(brend,'#brend'+s,dis=false,is_req=true)


        $('#model'+ s).attr('disabled',false)
        check_for_valid_and_set_val_select(model,'model'+ s,is_req=true)


       
        check_text_and_change(kratkiy_tekst,'#kratkiy_tekst'+s)
        check_input_and_change(comment,'#comment'+s)
      

        
        
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








