class BasePokritiya{
    constructor(
        id=NaN, //done
        sapcode=NaN,//done
        nazvaniye_tovarov=NaN,//done
        polnoye_nazvaniye=NaN,//done
        sena_materiala=NaN,//done
        bazoviy_edinitsa=NaN,//done
        koefitsiyent=NaN,//done
        alternativ_edin=NaN,//done
        gruppa_materialov=NaN,//done
        comment=NaN,//done
        full=false//done
        ) {
      
        this.id = id;
        this.sapcode=sapcode;
        this.nazvaniye_tovarov=nazvaniye_tovarov;
        this.polnoye_nazvaniye=polnoye_nazvaniye;
        this.sena_materiala=sena_materiala;
        this.bazoviy_edinitsa=bazoviy_edinitsa;
        this.koefitsiyent=koefitsiyent;
        this.alternativ_edin=alternativ_edin;
        this.gruppa_materialov=gruppa_materialov;
        this.comment=comment 
        this.full = full; 
      

    }
    get_kratkiy_tekst(){
                if (this.polnoye_nazvaniye && this.sena_materiala && this.bazoviy_edinitsa){
                    return {'text':'','accept':true}
                }else{
                    return {'text':'','accept':false}
                }
        }
  }


text =""
data_base = {}

for (let i = 1; i <= 10; i++) {
    data_base[i] = new BasePokritiya()
    text +=`
    <tr id='table_tr` +String(i)+`' >                   
    <td >
        <div class="input-group input-group-sm mb-1">
            
            <div class="btn-group" role="group" aria-label="Basic example">
            <button type="button" class="btn btn-warning btn-sm gradient-buttons" onclick="artukil_clear(`+String(i)+`)"  id='clear_btn`+String(i)+`'>Очистить</button>
            </div>
                
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style=" width: 75px; font-size:10px;height:32px " id='sapcode`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style=" width: 175px; font-size:10px;height:32px " id='nazvaniye_tovarov`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="border-color:red; width: 175px; font-size:10px;height:32px " id='polnoye_nazvaniye`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px;height:32px " id='sena_materiala`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px;height:32px " id='bazoviy_edinitsa`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="width: 75px; font-size:10px;height:32px " id='koefitsiyent`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="width: 75px; font-size:10px;height:32px " id='alternativ_edin`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="width: 75px; font-size:10px;height:32px " id='gruppa_materialov`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <textarea   rows='1' class=" form-control " style="width: 220px; font-size:10px;height:32px" id='comment`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></textarea >
        </div>
    </td>
    
    </tr>`
  }



var table = $('#table-artikul')

table.append(text)














function clear_artikul(id){
    var table_tr =$('#table_tr'+id);
    
    delete data_base[id]

    
    table_tr.css('background-color','white')
    
    
}

function artukil_clear(id){
    
    clear_artikul(id)

  
    var sapcode =$('#sapcode'+id);
    sapcode.val('')
    var nazvaniye_tovarov =$('#nazvaniye_tovarov'+id);
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
    
    var koefitsiyent =$('#koefitsiyent'+id);
    koefitsiyent.val('')
    var alternativ_edin =$('#alternativ_edin'+id);
    alternativ_edin.val('')
    
    var gruppa_materialov =$('#gruppa_materialov'+id);
    gruppa_materialov.val('')
    var comment =$('#comment'+id);
    comment.val('')
    

}





function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
    
    console.log(data_base[id])
        
    var sapcode =$('#sapcode'+id);
    var nazvaniye_tovarov =$('#nazvaniye_tovarov'+id);

    var polnoye_nazvaniye =$('#polnoye_nazvaniye'+id);
    var sena_materiala =$('#sena_materiala'+id);
    var bazoviy_edinitsa =$('#bazoviy_edinitsa'+id);
    

    var koefitsiyent =$('#koefitsiyent'+id);
    var alternativ_edin =$('#alternativ_edin'+id);
    var id_klaes =$('#id_klaes'+id);
    var gruppa_materialov =$('#gruppa_materialov'+id);
    var comment =$('#comment'+id);
    
    if(gruppa_materialov.val()!=''){
        data_base[id].gruppa_materialov = gruppa_materialov.val();
    }else{
        data_base[id].gruppa_materialov =NaN;
    }
    if(id_klaes.val()!=''){
        data_base[id].id_klaes = id_klaes.val();
    }else{
        data_base[id].id_klaes =NaN;
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
    if(nazvaniye_tovarov.val()!=''){
        data_base[id].nazvaniye_tovarov = nazvaniye_tovarov.val();
    }else{
        data_base[id].nazvaniye_tovarov =NaN;
    }
    if(sapcode.val()!=''){
        data_base[id].sapcode = sapcode.val();
    }else{
        data_base[id].sapcode =NaN;
    }
    if(comment.val()!=''){
        data_base[id].comment = comment.val();
    }else{
        data_base[id].comment =NaN;
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
    var sizee = Object.keys(data_base).length;
    var sizeee = $('#table-artikul tr').length;
    
    for (let i = sizeee + 1; i < sizeee+2; i++) {
        text +=`
        <tr id='table_tr` +String(i)+`' >                   
    <td >
        <div class="input-group input-group-sm mb-1">
            
            <div class="btn-group" role="group" aria-label="Basic example">
            <button type="button" class="btn btn-warning btn-sm gradient-buttons" onclick="artukil_clear(`+String(i)+`)"  id='clear_btn`+String(i)+`'>Очистить</button>
            </div>
                
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style=" width: 75px; font-size:10px;height:32px " id='sapcode`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style=" width: 175px; font-size:10px;height:32px " id='nazvaniye_tovarov`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="border-color:red; width: 175px; font-size:10px;height:32px " id='polnoye_nazvaniye`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px;height:32px " id='sena_materiala`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px;height:32px " id='bazoviy_edinitsa`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="width: 75px; font-size:10px;height:32px " id='koefitsiyent`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="width: 75px; font-size:10px;height:32px " id='alternativ_edin`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="width: 75px; font-size:10px;height:32px " id='gruppa_materialov`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <textarea   rows='1' class=" form-control " style="width: 220px; font-size:10px;height:32px" id='comment`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></textarea >
        </div>
    </td>
    
    </tr>
        `
    }



    
    var table = $('#table-artikul')
    table.append(text)




    for (let i = sizeee + 1; i < sizeee+2; i++) {
        $('#artikul'+String(i)).select2({
            ajax: {
                url: "/client/imzo-artikul-list",
                dataType: 'json',
                processResults: function(data){
                    return {results: $.map(data, function(item){
                        return {id:item.id,text:item.artikul,system:item.system,combination:item.combination,code_nakleyka:item.code_nakleyka}
                    })
                };
                }
            }
            });
        
        
        
        var artikulSelect = $('#artikul'+String(i));
        $.ajax({
            type: 'GET',
            url: "/client/imzo-artikul-list"
        }).then(function (data) {
            var option = new Option(data.artikul, data.id, true, true);
            artikulSelect.append(option).trigger('change');
        
            artikulSelect.trigger({
                type: 'select2:select',
                params: {
                    data: data
                }
            });
        });
        
        
        $("#artikul"+String(i)).on("select2:select", function (e) { 
        var select_val = $(e.currentTarget).val();
        console.log(select_val)
        var nazvaniye_system =$('.nazvaniye_system'+String(i));
        var combination = $('#combination'+String(i));
        var tip_pokritiya = $('#tip_pokritiya'+String(i));
        // tip_pokritiya.val('').change();
        console.log(tip_pokritiya)
        if(select_val!=''){

            tip_pokritiya.attr("disabled",false);
            
        }
        nazvaniye_system.text(e.params.data.system);
        combination.text(e.params.data.combination)

        var nakleyka_kode = e.params.data.code_nakleyka
        
        
        
        
        
        var nakleyka_nt1 = $('#nakleyka_nt'+String(i))
        var nakleyka_org =$('#nakleyka_org'+String(i));
        var nakleyka_select = $('#nakleyka_select'+String(i));

        var length = $('#length'+String(i));
        length.attr('required',true)
        var splav = $('#splav'+String(i));
        splav.attr('required',true)
        var tip_zakalyonnosti = $('#tip_zakalyonnosti'+String(i));
        tip_zakalyonnosti.attr('required',true)

        nakleyka_org.text("")
        if (nakleyka_kode =='NT1'){
            nakleyka_nt1.css('display','block')
            nakleyka_org.css('display','none')
            nakleyka_select.css('display','none')
        }
        else if( nakleyka_kode !=''){
            nakleyka_org.text(nakleyka_kode)
            nakleyka_nt1.css('display','none')
            nakleyka_org.css('display','block')
            nakleyka_select.css('display','none')
        }        
        else{
            nakleyka_nt1.css('display','none')
            nakleyka_org.css('display','none')
            nakleyka_select.css('display','block')
            nakleyka_select.attr('required',true)
            get_nakleyka(String(i))
        }
        
        
        
        // console.log(e.params.data.system)
        });

    }
    // clear_artikul(sizeee + 1);
}






