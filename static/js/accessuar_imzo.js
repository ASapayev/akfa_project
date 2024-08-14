class BasePokritiya{
    constructor(
        full=false,//done
        id=NaN, //done
        sapcode=NaN,//done
        nazvaniye_tovarov=NaN,//done
        polnoye_nazvaniye=NaN,//done
        sena_materiala=NaN,//done
        bazoviy_edinitsa=NaN,//done
        goods_group=NaN,//done
        tex_name=NaN,//done
        koefitsiyent=NaN,//done
        alternativ_edin=NaN,//done
        id_klaes=NaN,//done
        gruppa_materialov=NaN,//done
        comment=NaN,//done
        
        ) {
      
        this.id = id;
        this.sapcode=sapcode;
        this.nazvaniye_tovarov=nazvaniye_tovarov;
        this.polnoye_nazvaniye=polnoye_nazvaniye;
        this.sena_materiala=sena_materiala;
        this.bazoviy_edinitsa=bazoviy_edinitsa;
        this.goods_group=goods_group;
        this.koefitsiyent=koefitsiyent;
        this.alternativ_edin=alternativ_edin;
        this.id_klaes=id_klaes;
        this.gruppa_materialov=gruppa_materialov;
        this.comment=comment; 
        this.full = full; 
        this.tex_name=tex_name;
      

    }
    get_kratkiy_tekst(){
                if (this.polnoye_nazvaniye && this.sena_materiala && this.bazoviy_edinitsa && this.goods_group&& this.id_klaes && this.nazvaniye_tovarov){
                    return {'text':'','accept':true}
                }else{
                    return {'text':'','accept':false}
                }
        }
  }



data_base = {}

function front_piece(start=1,end=6){
    text =""
    for (let i = start; i < end; i++) {
        data_base[i] = new BasePokritiya()
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
            <input type='text' class=" form-control " style=" width: 125px; font-size:10px;z-index:0 " id='sapcode`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 175px; font-size:10px; border-color:red;z-index:0" id='nazvaniye_tovarov`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)' maxlength="40"></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 175px; font-size:10px;z-index:0 " id='polnoye_nazvaniye`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px;z-index:0 " id='sena_materiala`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;display:none;z-index:0" id='bazoviy_edinitsa`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
            <select class="form-select" aria-label="" style="border-color:red; width: 165px;text-transform: uppercase; font-size:12px; padding-right:0px;z-index:0" onchange="create_kratkiy_tekst(`+String(i)+`)" id='goods_group`+String(i)+`' required>
                    <option  selected></option>
                    <option value="ACS_RAW_ALU">Сырье аксессуары алюминий</option>
                    <option value="ACS_RAW_PVC">Сырье аксессуары ПВХ</option>
                    <option value="GLASS_RAW_MATERIAL">Стекло сырье</option>
                    <option value="OTHER_RAW">Прочее сырье</option>
                    <option value="PVC_RAW_MATERIAL">ПВХ сырье</option>
                    <option value="ALU_RAW_MATERIAL">Алюминиевое сырье</option>
                    <option value="SVR_FINISH_PROD">ГП секционные ворота</option>
                    <option value="SGLS_FINISH_PROD">ГП стекло одинарное</option>
                    <option value="GLS_FINISH_PROD">ГП стеклопакеты</option>
                    <option value="ALU_FINISH_PROD">ГП алюминий</option>
                    <option value="PVC_FINISH_PROD">ГП ПВХ</option>
                    <option value="QLIK_ALU_PROF">Алюминиевый профиль</option>
                    <option value="QLIK_PVC_PROF">ПВХ профиль</option>
                    <option value="QLIK_RLS">Рольставни</option>
                    <option value="QLIK_MSQ">Москитка</option>
                    <option value="QLIK_FSD">Фасад</option>
                    <option value="QLIK_ACS">Аксессуар</option>
                    <option value="QLIK_GLS">Стекло</option>
                    <option value="QLIK_PDF">Подоконник</option>
                    <option value="QLIK_CLR">Метал</option>
                    <option value="QLIK_MDF">МДФ</option>
                    <option value="RAWMAT_TYPE_PVC">Сырьё ПВХ</option>
                    <option value="RAWMAT_TYPE_LAM">Сырьё Ламинации</option>
                    <option value="QLIK_PVC_DO">Деловод отход ПВХ</option>
                    <option value="QLIK_ALU_DO">Деловод отход Алю</option>
                    <option value="QLIK_OTH_MAT">Прочие материалы</option>
                    <option value="OTH_FINISH_PROD">ГП другие</option>
                </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <div><span class ='tex_name` +String(i)+`' id ='tex_name` +String(i)+`'style="text-transform: uppercase;font-size: 12px;z-index:0"></span></div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 75px; font-size:10px;z-index:0 " id='koefitsiyent`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 75px; font-size:10px; z-index:0" id='alternativ_edin`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 75px; font-size:10px; border-color:red; z-index:0" id='id_klaes`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 75px; font-size:10px; z-index:0" id='gruppa_materialov`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)' value='AKSUZGP'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type='text' class=" form-control " style="width: 250px; font-size:10px; height:27px!important;z-index:0"  id='comment`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
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

        var sapcode = data.sapcode;
        var nazvaniye_tovarov = data.nazvaniye_tovarov;
        var polnoye_nazvaniye = data.polnoye_nazvaniye;
        var sena_materiala = data.sena_materiala;
        var bazoviy_edinitsa = data.bazoviy_edinitsa;
        var goods_group = data.goods_group;
        var tex_name = data.tex_name;
        var koefitsiyent = data.koefitsiyent;
        var alternativ_edin = data.alternativ_edin;
        var id_klaes = data.id_klaes;
        var gruppa_materialov = data.gruppa_materialov;
        var comment = data.comment;
        
      
        
        check_input_and_change(sapcode,'#sapcode'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(nazvaniye_tovarov,'#nazvaniye_tovarov'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(polnoye_nazvaniye,'#polnoye_nazvaniye'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(sena_materiala,'#sena_materiala'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(bazoviy_edinitsa,'#bazoviy_edinitsa'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(tex_name,'#goods_group'+s,dis=false,is_req=true,is_req_simple=false)
        check_text_and_change(tex_name,'#tex_name'+s)
        check_input_and_change(koefitsiyent,'#koefitsiyent'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(alternativ_edin,'#alternativ_edin'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(id_klaes,'#id_klaes'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(gruppa_materialov,'#gruppa_materialov'+s,dis=false,is_req=false,is_req_simple=true)
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


function add_column(){
        
    text =""
    var sizeee = $('#table-artikul tr').length;
    
    text = front_piece(start = sizeee+1, end = sizeee+2)

    
    var table = $('#table-artikul')
    table.append(text)
    


}





function artukil_clear(id){
    
    var table_tr =$('#table_tr'+id);
    
    for(key in data_base[id]){
        data_base[id][key] = NaN
    }

    
    table_tr.css('background-color','white')

  
    var sapcode =$('#sapcode'+id);
    sapcode.val('')
    var nazvaniye_tovarov =$('#nazvaniye_tovarov'+id);
    nazvaniye_tovarov.css('border-color','red')
    nazvaniye_tovarov.val('')

    var polnoye_nazvaniye =$('#polnoye_nazvaniye'+id);
    polnoye_nazvaniye.val('')
    polnoye_nazvaniye.css('border-color','red')
    var sena_materiala =$('#sena_materiala'+id);
    sena_materiala.val('')
    sena_materiala.css('border-color','red')
    var bazoviy_edinitsa =$('#bazoviy_edinitsa'+id);
    bazoviy_edinitsa.val('')
    bazoviy_edinitsa.css('border-color','red')
    var goods_group =$('#goods_group'+id);
    goods_group.val('')
    goods_group.css('border-color','red')
    
    var tex_name =$('#tex_name'+id);
    tex_name.text('')
    var koefitsiyent =$('#koefitsiyent'+id);
    koefitsiyent.val('')
    var alternativ_edin =$('#alternativ_edin'+id);
    alternativ_edin.val('')
    var id_klaes =$('#id_klaes'+id);
    id_klaes.val('')
    id_klaes.css('border-color','red')
    var gruppa_materialov =$('#gruppa_materialov'+id);
    gruppa_materialov.val('')
    var comment =$('#comment'+id);
    comment.val('')
    

}





function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
    

    var polnoye_nazvaniye =$('#polnoye_nazvaniye'+id);
    var sena_materiala =$('#sena_materiala'+id);
    var bazoviy_edinitsa =$('#bazoviy_edinitsa'+id);
    var goods_group =$('#goods_group'+id);

    var sapcode =$('#sapcode'+id);
    var nazvaniye_tovarov =$('#nazvaniye_tovarov'+id);
    var koefitsiyent =$('#koefitsiyent'+id);
    var alternativ_edin =$('#alternativ_edin'+id);
    var id_klaes =$('#id_klaes'+id);
    var gruppa_materialov =$('#gruppa_materialov'+id);
    var comment =$('#comment'+id);
    
   
        
        
    if(comment.val()!=''){
        data_base[id].comment = comment.val();
    }else{
        data_base[id].comment =NaN;
    }
    if(gruppa_materialov.val()!=''){
        data_base[id].gruppa_materialov = gruppa_materialov.val();
    }else{
        data_base[id].gruppa_materialov =NaN;
    }
    
    if(alternativ_edin.val()!=''){
        data_base[id].alternativ_edin = alternativ_edin.val();
    }else{
        data_base[id].alternativ_edin =NaN;
    }
    if(koefitsiyent.val()!=''){
        data_base[id].koefitsiyent = koefitsiyent.val();
    }else{
        data_base[id].koefitsiyent =NaN;
    }
    
    if(sapcode.val()!=''){
        data_base[id].sapcode = sapcode.val();
    }else{
        data_base[id].sapcode =NaN;
    }


    

    if(nazvaniye_tovarov.val()!=''){
        nazvaniye_tovarov.css('border-color','#dedad9')
        data_base[id].nazvaniye_tovarov = nazvaniye_tovarov.val();
    }else{
        nazvaniye_tovarov.css('border-color','red')
        data_base[id].nazvaniye_tovarov =NaN;
    }

    if(id_klaes.val()!=''){
        id_klaes.css('border-color','#dedad9')
        data_base[id].id_klaes = id_klaes.val();
    }else{
        id_klaes.css('border-color','red')
        data_base[id].id_klaes =NaN;
    }

    var polnoye_nazvaniye =$('#polnoye_nazvaniye'+id)

    if(polnoye_nazvaniye.val()!=''){
        polnoye_nazvaniye.css('border-color','#dedad9')
        data_base[id].polnoye_nazvaniye = polnoye_nazvaniye.val();
    }else{
        polnoye_nazvaniye.css('border-color','red')
        data_base[id].polnoye_nazvaniye =NaN;
    }

    var sena_materiala =$('#sena_materiala'+id)
    if(sena_materiala.val()!=''){
        sena_materiala.css('border-color','#dedad9')
        data_base[id].sena_materiala = sena_materiala.val();
    }else{
        sena_materiala.css('border-color','red')
        data_base[id].sena_materiala =NaN;
        
        
    }
    var bazoviy_edinitsa =$('#bazoviy_edinitsa'+id)
    if(bazoviy_edinitsa.val()!=''){
        bazoviy_edinitsa.css('border-color','#dedad9')
        data_base[id].bazoviy_edinitsa = bazoviy_edinitsa.val();
    }else{
        bazoviy_edinitsa.css('border-color','red')
        data_base[id].bazoviy_edinitsa =NaN;
        
        
    }
    var goods_group =$('#goods_group'+id)
    if(goods_group.val()!=''){
        var goods_group_sel =$('#goods_group'+id +' option:selected').text()
        goods_group.css('border-color','#dedad9')
        data_base[id].goods_group = goods_group_sel;
        data_base[id].tex_name = goods_group.val();
        var tex_name =$('#tex_name'+id);
        tex_name.text(goods_group.val())
    }else{
        var tex_name =$('#tex_name'+id);
        tex_name.text('')
        goods_group.css('border-color','red')
        data_base[id].goods_group =NaN;
        data_base[id].tex_name =NaN;
        
        
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








