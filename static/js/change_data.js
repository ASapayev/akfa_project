class BasePokritiya{
    constructor(
        full=false,//done
        id=NaN, //done
        vid_zayavki=NaN,
        id_savdo=NaN,
        naz_savdo=NaN,
        sapcode=NaN,
        bei =NaN,
        aei=NaN,
        koefitsiyent=NaN,
        sena_c_ndc=NaN,
        sena_bez_ndc=NaN,
        ed_izm=NaN,
        group=NaN,
        group_zakupok=NaN,
        zavod=NaN,
        segment=NaN,
        bux_naz=NaN,
        tip_clienta=NaN,
        svet_product=NaN,
        diller=NaN,


        comment=NaN,
        
        
        ) {
      
        this.full=full;
        this.id=id;
        this.vid_zayavki=vid_zayavki;
        this.id_savdo=id_savdo;
        this.naz_savdo=naz_savdo;
        this.sapcode=sapcode;
        this.bei=bei;
        this.aei=aei;
        this.koefitsiyent=koefitsiyent;
        this.sena_c_ndc=sena_c_ndc;
        this.sena_bez_ndc=sena_bez_ndc;
        this.ed_izm=ed_izm;
        this.group=group;
        this.group_zakupok=group_zakupok;
        this.zavod=zavod;
        this.segment=segment;
        this.bux_naz=bux_naz;
        this.tip_clienta=tip_clienta;
        this.svet_product=svet_product;
        this.diller=diller;
        this.comment=comment;
        
    }
    get_kratkiy_tekst(){
            switch(this.id){
                case 1:
            
                        if (this.id_savdo && this.naz_savdo){
        
                            return {'text':'','accept':true}
                        }else{
                            return {'text':'','accept':false}
                        }
                        break;
            }
        }
  }




var data_base = {}

function front_piece(start=1,end=6){
    text =""

    for (let i = start; i < end; i++) {
        data_base[i] = new BasePokritiya()
        data_base[i].id = 1
        text +=`
        <tr id='table_tr` +String(i)+`' style='padding-bottom:0!important;margin-bottom:0!important;'>                   
        <td class="sticky-col"   style='left:0; padding-right:5px; background-color:white!important;' >
                    <div class="btn-group" role="group" aria-label="Basic example">
                            <button type="button" class="btn btn-outline-secondary btn-sm" id='clear_btn`+String(i)+`' onclick="artukil_clear(`+String(i)+`)" data-bs-toggle='popover' title='Yangi sozdaniya qilish uchun ishlatiladi'><i class="bi bi-x-circle"></i></button>
                            <button type="button" class="btn btn-outline-secondary btn-sm"  onclick="copy_tr(`+String(i)+`)" data-bs-toggle='popover' title='Yangi sozdaniya qilish uchun ishlatiladi'><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-copy" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M4 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 5a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-1h1v1a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h1v1z"/></svg></button>
                    </div>
                    
                    

        </td>
       <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 100px; font-size:10px;height:27px;z-index:0 " id='id_savdo`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 200px; font-size:10px;height:27px;z-index:0 " id='naz_savdo`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 200px; font-size:10px;height:27px;z-index:0 " id='sapcode`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;z-index:0" id='bei`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;z-index:0" id='aei`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
            <input type='text' class=" form-control " style=" width: 75px; font-size:10px;height:27px;z-index:0 " id='koefitsiyent`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 75px; font-size:10px;height:27px;z-index:0 " id='sena_c_ndc`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 75px; font-size:10px;height:27px;z-index:0 " id='sena_bez_ndc`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;z-index:0" id='ed_izm`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0 " id='comment`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>

        </tr>`
        
    }
    return text
}

text = front_piece()


var table = $('#table-artikul')

table.append(text)





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

        var id_savdo = data.id_savdo;
        var naz_savdo = data.naz_savdo;
        var sapcode = data.sapcode;
        var bei = data.bei;
        var aei = data.aei;
        var koefitsiyent = data.koefitsiyent;
        var sena_c_ndc = data.sena_c_ndc;
        var sena_bez_ndc = data.sena_bez_ndc;
        var ed_izm = data.ed_izm;
        var comment = data.comment;
        
        check_input_and_change(id_savdo,'#id_savdo'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(naz_savdo,'#naz_savdo'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(sapcode,'#sapcode'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(bei,'#bei'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(aei,'#aei'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(koefitsiyent,'#koefitsiyent'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(sena_c_ndc,'#sena_c_ndc'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(sena_bez_ndc,'#sena_bez_ndc'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(ed_izm,'#ed_izm'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(comment,'#comment'+s,dis=false,is_req=false,is_req_simple=true)
        
        
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





function artukil_clear(id){
    
    var table_tr =$('#table_tr'+id);
    
    data_base[id].id_savdo=NaN
    data_base[id].naz_savdo=NaN
    data_base[id].sapcode=NaN
    data_base[id].bei=NaN
    data_base[id].aei=NaN
    data_base[id].koefitsiyent=NaN
    data_base[id].sena_c_ndc=NaN
    data_base[id].sena_bez_ndc=NaN
    data_base[id].ed_izm=NaN
    data_base[id].comment=NaN

    
    table_tr.css('background-color','white')
    

    var id_savdo =$('#id_savdo'+id);
    var naz_savdo =$('#naz_savdo'+id);
    var sapcode =$('#sapcode'+id);
    var bei =$('#bei'+id);
    var aei =$('#aei'+id);
    var koefitsiyent =$('#koefitsiyent'+id);
    var sena_c_ndc =$('#sena_c_ndc'+id);
    var sena_bez_ndc =$('#sena_bez_ndc'+id);
    var ed_izm =$('#ed_izm'+id);
    var comment =$('#comment'+id);

  
    id_savdo.css('border-color','red')
    naz_savdo.css('border-color','red')
    
    id_savdo.val('')
    naz_savdo.val('')
    sapcode.val('')
    bei.val('')
    aei.val('')
    koefitsiyent.val('')
    sena_c_ndc.val('')
    sena_bez_ndc.val('')
    ed_izm.val('')
    comment.val('')


}


function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
        
        var id_savdo =$('#id_savdo'+id)
        var naz_savdo =$('#naz_savdo'+id)
        var sapcode =$('#sapcode'+id)
        var bei =$('#bei'+id)
        var aei =$('#aei'+id)
        var koefitsiyent =$('#koefitsiyent'+id)
        var sena_c_ndc =$('#sena_c_ndc'+id)
        var sena_bez_ndc =$('#sena_bez_ndc'+id)
        var ed_izm =$('#ed_izm'+id)
        var comment =$('#comment'+id);
        
        
        
        if(id_savdo.val()!=''){
            data_base[id].id_savdo = id_savdo.val();
            id_savdo.css('border-color','#dedad9')
        }else{
            id_savdo.css('border-color','red')
            data_base[id].id_savdo = NaN;
        }
        if(naz_savdo.val()!=''){
            data_base[id].naz_savdo = naz_savdo.val();
            naz_savdo.css('border-color','#dedad9')
        }else{
            naz_savdo.css('border-color','red')
            data_base[id].naz_savdo = NaN;
        }
        if(sapcode.val()!=''){
            data_base[id].sapcode = sapcode.val();
            sapcode.css('border-color','#dedad9')
        }else{
            sapcode.css('border-color','#dedad9')
            data_base[id].sapcode = NaN;
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
        if(sena_c_ndc.val()!=''){
            data_base[id].sena_c_ndc = sena_c_ndc.val();
            sena_c_ndc.css('border-color','#dedad9')
        }else{
            sena_c_ndc.css('border-color','#dedad9')
            data_base[id].sena_c_ndc = NaN;
        }
        if(sena_bez_ndc.val()!=''){
            data_base[id].sena_bez_ndc = sena_bez_ndc.val();
            sena_bez_ndc.css('border-color','#dedad9')
        }else{
            sena_bez_ndc.css('border-color','#dedad9')
            data_base[id].sena_bez_ndc = NaN;
        }
        if(ed_izm.val()!=''){
            data_base[id].ed_izm = ed_izm.val();
            ed_izm.css('border-color','#dedad9')
        }else{
            ed_izm.css('border-color','#dedad9')
            data_base[id].ed_izm = NaN;
        }
        if(comment.val()!=''){
            data_base[id].comment = comment.val();
            comment.css('border-color','#dedad9')
        }else{
            comment.css('border-color','#dedad9')
            data_base[id].comment = NaN;
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




