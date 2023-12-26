
text =""

for (let i = 1; i <= 5; i++) {
    text +=`
    <tr >
                                
    <td style=";">
        <div class="input-group input-group-sm mb-1">
            <div>
                <button type="button" class="btn btn-warning" onclick="clear_artikul(`+String(i)+`)">Очистить</button>     
            </div>
        </div>
    </td>
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
            <div><span class ='nazvaniye_system` +String(i)+`'style="text-transform: uppercase;"></span></div>
        </div>
    </td>
    <td style="background-color:#ddebf7;">
        <div class="input-group input-group-sm mb-1">
            <select class=" form-control" style="background-color:#ddebf7; width: 200px;" id="artikul`+String(i)+`"></select>
        </div>
    </td>
    
    
    <td >
        <div class="input-group input-group-sm mb-1">
            <input type="text" class="form-control " aria-describedby="inputGroup-sizing-sm">
        </div>
    </td>
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 200px;text-transform: uppercase;" onchange="tip_pokritiya_selected(`+String(i)+`,this.value)" disabled id='tip_pokritiya`+String(i)+`' required>
                <option  value="0" selected></option>
                <option value="1" >Неокрашенный</option>
                <option value="2">Белый</option>
                <option value="3">Окрашенный</option>
                <option value="4">Ламинированный</option>
                <option value="5">Сублимированный</option>
                <option value="6">Анодированный</option>
              </select>
        </div>
    </td>
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
            
        </div>
    </td>
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
            
        </div>
    </td>
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1" style="font-size: small; text-transform: uppercase; width:130px">
            <div>
                <span class =' text-center pl-1' style="font-size: small; text-transform: uppercase;" id ='combination` +String(i)+`'></span>
            </div>
        </div>
    </td>
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
        <div>
            <span class =' text-center' style="font-size: small;font-weight: bold; text-transform: uppercase;" id ='brand_kraski_snaruji` +String(i)+`'></span>
        </div>
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1">
        <div>
            <span class =' text-center' style="font-size: small; font-weight: bold; text-transform: uppercase;" id ='code_kraski_snaruji` +String(i)+`'></span>
        </div>
        </div>
    </td>
    
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
        <div>
            <span class =' text-center' style="font-size: small;font-weight: bold; text-transform: uppercase;" id ='brand_kraski_vnutri` +String(i)+`'></span>
        </div>
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1">
        <div>
            <span class =' text-center' style="font-size: small; font-weight: bold; text-transform: uppercase;" id ='code_kraski_vnutri` +String(i)+`'></span>
        </div>
        </div>
    </td>
    
    <td style="background-color:#ddebf7;">
        <div class="input-group input-group-sm mb-1">    
        <select class="form-select" aria-label="" style="width: 245px;" onchange="svet_dekplonka_snaruji_selected(`+String(i)+`,this.value)"  id='svet_dekplonka_snaruji`+String(i)+`' disabled>
            <option  value="0" selected></option>
            <option value="Золотой Дуб 7777" >7777</option>
            <option value="Махагон 3701">3701</option>
            <option value="3D 3702">3702</option>
            <option value="Дуб мокко">8888</option>
            <option value="Шеф. сер. дуб">9999</option>
            <option value="XXXX">XXXX</option>
        </select>
        </div>
    </td>
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
            <div>
                <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;" id ='code_dekplonka_snaruji` +String(i)+`' disabled ></span>
            </div>
        </div>
    </td>
    <td style="background-color:#ddebf7;">
        <div class="input-group input-group-sm mb-1">    
        <select class="form-select" aria-label="" style="width: 245px;" onchange="svet_dekplonka_vnutri_selected(`+String(i)+`,this.value)"  id='svet_dekplonka_vnutri`+String(i)+`'>
            <option  value="0" selected></option>
            <option value="Золотой Дуб 7777" >7777</option>
            <option value="Махагон 3701">3701</option>
            <option value="3D 3702">3702</option>
            <option value="Дуб мокко">8888</option>
            <option value="Шеф. сер. дуб">9999</option>
            <option value="XXXX">XXXX</option>
        </select>
        </div>
    </td>
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
            <div>
                <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;" id ='code_dekplonka_vnutri` +String(i)+`'></span>
            </div>
        </div>
    </td>

    

    <td style="background-color:#ddebf7;">
        <div class="input-group input-group-sm mb-1">    
        <select class="form-select" aria-label="" style="width: 245px;" onchange="svet_lamplonka_snaruji_selected(`+String(i)+`,this.value)" disabled id='svet_lamplonka_snaruji`+String(i)+`'>
            <option  value="0" selected></option>
            <option value="2036" >Золотой дуб</option>
            <option value="2048">Дуб мокко</option>
            <option value="2007">Красный орех</option>
            <option value="2012">Орех</option>
            <option value="3086">Шеффелдский дуб серый</option>
            <option value="1012">Алюкс антрацит</option>
            <option value="3001">Терновый дуб</option>
            <option value="3002">Шеф Альпийский дуб</option>
            <option value="3003">Гранитовый шеф дуб</option>
            <option value="3042">Дерево бальза</option>
            <option value="3062">Грецкий орех</option>
            <option value="3043">Вишня амаретто</option>
            <option value="3059">Орех терра</option>
            <option value="3058">Грецкий орех амаретто</option>
            <option value="3077">Винчестер</option>
            <option value="3081">Шеффелдский дуб светлый</option>
            <option value="3094">Орех Ребраун</option>
            <option value="1004">Метбраш платин</option>
            <option value="1005">Метбраш серый кварц</option>
            <option value="1006">Метбраш серый антрацит</option>
            <option value="XXXX">XXXX</option>
        </select>
        </div>
    </td>
    
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
            <div>
                <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;" id ='code_lamplonka_snaruji` +String(i)+`'></span>
            </div>
        </div>
    </td>
    <td style="background-color:#ddebf7;">
        <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 245px;" onchange="svet_lamplonka_vnutri_selected(`+String(i)+`,this.value)" disabled id='svet_lamplonka_vnutri`+String(i)+`'>
                <option  value="0" selected></option>
                <option value="2036" >Золотой дуб</option>
            <option value="2048">Дуб мокко</option>
            <option value="2007">Красный орех</option>
            <option value="2012">Орех</option>
            <option value="3086">Шеффелдский дуб серый</option>
            <option value="1012">Алюкс антрацит</option>
            <option value="3001">Терновый дуб</option>
            <option value="3002">Шеф Альпийский дуб</option>
            <option value="3003">Гранитовый шеф дуб</option>
            <option value="3042">Дерево бальза</option>
            <option value="3062">Грецкий орех</option>
            <option value="3043">Вишня амаретто</option>
            <option value="3059">Орех терра</option>
            <option value="3058">Грецкий орех амаретто</option>
            <option value="3077">Винчестер</option>
            <option value="3081">Шеффелдский дуб светлый</option>
            <option value="3094">Орех Ребраун</option>
            <option value="1004">Метбраш платин</option>
            <option value="1005">Метбраш серый кварц</option>
            <option value="1006">Метбраш серый антрацит</option>
            <option value="XXXX">XXXX</option>
            </select>
        </div>
    </td>
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
            <div>
                <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;" id='code_lamplonka_vnutri`+String(i)+`'></span>
            </div>
        </div>
    </td>
    <td style="background-color:#ddebf7;">
        <div class="input-group input-group-sm mb-1">
            
        </div>
    </td> 
    <td style="background-color:#ddebf7;">
        <div class="input-group input-group-sm mb-1">
            
        </div>
    </td> 
    <td style="background-color:#ddebf7;">
        <div class="input-group input-group-sm mb-1">
           
        </div>
    </td>
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
            
        </div>
    </td>
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
            
        </div>
    </td>
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1" id="nakleyka`+String(i)+`">
            
        </div>
    </td>
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
            
        </div>
    </td>
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
            
        </div>
    </td>
    <td style="background-color:#ddebf7;">
        <div class="input-group input-group-sm mb-1">
            
        </div>
    </td> 
    <td style="background-color:#ddebf7;">
        <div class="input-group input-group-sm mb-1">
            
        </div>
    </td> 
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
           
        </div>
    </td>
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
           
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
           
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
           
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
           
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
           
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
           
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
           
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
           
        </div>
    </td>
    </tr>`
  }



var table = $('#table-artikul')

table.append(text)




for (let i = 1; i <= 5; i++) {
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
    var nazvaniye_system =$('.nazvaniye_system'+String(i));
    var combination = $('#combination'+String(i));
    var tip_pokritiya = $('#tip_pokritiya'+String(i));
    tip_pokritiya.val('0').change();
    tip_pokritiya.attr("disabled",false);
    nazvaniye_system.text(e.params.data.system);
    combination.text(e.params.data.combination)

    var nakleyka_kode = e.params.data.code_nakleyka
    
    var select_nakleyka = $('#nakleyka'+String(i))
  
    
    
    if (nakleyka_kode =='NT1'){
        select_nakleyka.children("span").remove();
        select_nakleyka.children("select").remove();
        var newDiv = "<span>NT1</span>"; 
        select_nakleyka.append(newDiv)
    }
    else if( nakleyka_kode !=''){
        select_nakleyka.children("span").remove();
        select_nakleyka.children("select").remove();
        if (nakleyka_kode ==undefined){
            var newDiv = "<span></span>"; 
        }else{
            var newDiv = "<span>" + nakleyka_kode + "</span>"; 

        }
        select_nakleyka.append(newDiv)
    }        
    else{
        select_nakleyka.children("span").remove();
        select_nakleyka.children("select").remove();
        const newDiv = "<select class ='kod_nakleyki' style='text-transform: uppercase; width: 70px;'' required></select>"
        select_nakleyka.append(newDiv)
        get_nakleyka()
    }
    
    
    
    // console.log(e.params.data.system)
    });

}



function get_nakleyka(){
    $('.kod_nakleyki').select2({
        ajax: {
            url: "/client/nakleyka-list",
            dataType: 'json',
            processResults: function(data){
                return {results: $.map(data, function(item){
                    return {id:item.id,text:item.код_наклейки}
                })
            };
            }
        }
        });
}


function clear_artikul(id){
    $('#artikul'+id).val(null).trigger('change');
    $('.nazvaniye_system'+id).text('');
    var tip_pokritiya = $('#tip_pokritiya'+String(id));
    tip_pokritiya.val('0').change();
    tip_pokritiya.attr("disabled",true);
    var select_nakleyka = $('#nakleyka'+String(id));
    select_nakleyka.children("span").remove();
    select_nakleyka.children("select").remove();

    var code_kraski_snaruji = $('#code_kraski_snaruji'+String(id));
    var code_kraski_vnutri = $('#code_kraski_vnutri'+String(id));
    var brand_kraski_vnutri = $('#brand_kraski_vnutri'+String(id))
    var brand_kraski_snaruji = $('#brand_kraski_snaruji'+String(id))
    code_kraski_snaruji.text("");
    code_kraski_vnutri.text("");
    brand_kraski_vnutri.text("");
    brand_kraski_snaruji.text("");

    var combination= $('#combination'+String(id));
    combination.text("");

    var svet_lamplonka_snaruji = $('#svet_lamplonka_snaruji'+String(id));
    svet_lamplonka_snaruji.val('0').change();
    svet_lamplonka_snaruji.attr("disabled",true);
    var code_lamplonka_snaruji = $('#code_lamplonka_snaruji'+String(id));
    code_lamplonka_snaruji.text("")

    var svet_lamplonka_vnutri = $('#svet_lamplonka_vnutri'+String(id));
    svet_lamplonka_vnutri.val('0').change();
    svet_lamplonka_vnutri.attr("disabled",true);
    var code_lamplonka_vnutri = $('#code_lamplonka_vnutri'+String(id));
    code_lamplonka_vnutri.text("")


}


function tip_pokritiya_selected(id,val){
    
    var select_nakleyka = $('#nakleyka'+String(id));
    select_nakleyka.children("span").remove();
    select_nakleyka.children("select").remove();
    
    var code_kraski_snaruji = $('#code_kraski_snaruji'+String(id));
    var code_kraski_vnutri = $('#code_kraski_vnutri'+String(id));
    var brand_kraski_vnutri = $('#brand_kraski_vnutri'+String(id))
    var brand_kraski_snaruji = $('#brand_kraski_snaruji'+String(id))
    code_kraski_snaruji.text("");
    code_kraski_vnutri.text("");
    brand_kraski_vnutri.text("");
    brand_kraski_snaruji.text("");
    var combination= $('#combination'+String(id));
    combination_text = combination.text();

    var svet_lamplonka_snaruji = $('#svet_lamplonka_snaruji'+String(id));
    svet_lamplonka_snaruji.val('0').change();
    svet_lamplonka_snaruji.attr("disabled",true);
    var code_lamplonka_snaruji = $('#code_lamplonka_snaruji'+String(id));
    code_lamplonka_snaruji.text("")

    var svet_lamplonka_vnutri = $('#svet_lamplonka_vnutri'+String(id));
    svet_lamplonka_vnutri.val('0').change();
    svet_lamplonka_vnutri.attr("disabled",true);
    var code_lamplonka_vnutri = $('#code_lamplonka_vnutri'+String(id));
    code_lamplonka_vnutri.text("")

    if(String(val) == '1'){
        var newDiv = "<span>NT1</span>"; 
        select_nakleyka.append(newDiv);
        if (combination_text.toUpperCase() == 'БЕЗ ТЕРМОМОСТА'){

            var code_kraski_snaruji = $('#code_kraski_snaruji'+String(id))
            code_kraski_snaruji.text('MF')
        }else{
            var code_kraski_snaruji = $('#code_kraski_snaruji'+String(id));
            var code_kraski_vnutri = $('#code_kraski_vnutri'+String(id));
            code_kraski_snaruji.text('MF');
            code_kraski_vnutri.text('MF');

        }

    }else if(String(val) == '2'){
        
        if (combination_text.toUpperCase() == 'БЕЗ ТЕРМОМОСТА'){
            var code_kraski_snaruji = $('#code_kraski_snaruji'+String(id))
            var brand_kraski_snaruji = $('#brand_kraski_snaruji'+String(id))
            code_kraski_snaruji.text('9016')
            brand_kraski_snaruji.text('R')
        }else{
            var code_kraski_snaruji = $('#code_kraski_snaruji'+String(id));
            var code_kraski_vnutri = $('#code_kraski_vnutri'+String(id));
            var brand_kraski_vnutri = $('#brand_kraski_vnutri'+String(id))
            var brand_kraski_snaruji = $('#brand_kraski_snaruji'+String(id))
            brand_kraski_snaruji.text('R');
            code_kraski_snaruji.text('9016');
            brand_kraski_vnutri.text('R');
            code_kraski_vnutri.text('9016');

        }

        select_nakleyka.children("span").remove();
        select_nakleyka.children("select").remove();
        const newDiv = "<select class ='kod_nakleyki' style='text-transform: uppercase; width: 70px;' required></select>"
        select_nakleyka.append(newDiv)
        get_nakleyka()
    }else if(String(val) == '3' || String(val) == '4'){
        
        var brands =`<select required class="form-select form-select-sm text-center"  style="width:55px;" id='brand_k_snaruji`+String(id)+`' >
        <option  value="0" selected></option>
        <option value="A">A</option>
        <option value="B">B</option>
        <option value="R">R</option>
        <option value="T">T</option>
        <option value="J">J</option>
        <option value="P">P</option>
        <option value="M">M</option>
        </select>` 
        var brand_kraski_snaruji = $('#brand_kraski_snaruji'+String(id))
        brand_kraski_snaruji.append(brands)
        var code_kras_snaruji =`<input type="text" class="form-control " id ='code_kraski_snar' aria-describedby="inputGroup-sizing-sm" style="width:100px;" required>`
        var code_kraski_snaruji = $('#code_kraski_snaruji'+String(id));
        code_kraski_snaruji.append(code_kras_snaruji);
        select_nakleyka.children("span").remove();
        select_nakleyka.children("select").remove();
        const newDiv = "<select class ='kod_nakleyki' style='text-transform: uppercase; width: 70px;' required></select>"
        select_nakleyka.append(newDiv)
        get_nakleyka()

        if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА'){
            var brands =`<select class="form-select form-select-sm text-center"  style="width:55px;" id='brand_k_vnutri`+String(id)+`' required>
                <option  value="0" selected></option>
                <option value="A">A</option>
                <option value="B">B</option>
                <option value="R">R</option>
                <option value="T">T</option>
                <option value="J">J</option>
                <option value="P">P</option>
                <option value="M">M</option>
            </select>`
            var brand_kraski_vnutri = $('#brand_kraski_vnutri'+String(id));
            brand_kraski_vnutri.append(brands)

            var code_kras_vnut =`<input type="text" class="form-control " id ='code_kraski_vnut' aria-describedby="inputGroup-sizing-sm" style="width:100px;" required>`
            var code_kraski_vnutri = $('#code_kraski_vnutri'+String(id));
            code_kraski_vnutri.append(code_kras_vnut)


        }

        if (String(val) == '4'){
            var svet_lamplonka_snaruji = $('#svet_lamplonka_snaruji'+String(id));
            svet_lamplonka_snaruji.attr("disabled",false);

            if(combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА'){
                var svet_lamplonka_vnutri = $('#svet_lamplonka_vnutri'+String(id));
                svet_lamplonka_vnutri.attr("disabled",false);

            }
        }


    }else if(String(val) == '5'){
        var brands =`<select required class="form-select form-select-sm text-center"  style="width:55px;" id='brand_k_snaruji`+String(id)+`' >
        <option  value="0" selected></option>
        <option value="A">A</option>
        <option value="B">B</option>
        <option value="R">R</option>
        <option value="T">T</option>
        <option value="J">J</option>
        <option value="P">P</option>
        <option value="M">M</option>
        </select>` 
        var brand_kraski_snaruji = $('#brand_kraski_snaruji'+String(id))
        brand_kraski_snaruji.append(brands)
        var code_kras_snaruji =`<input type="text" class="form-control " id ='code_kraski_snar' aria-describedby="inputGroup-sizing-sm" style="width:100px;" required>`
        var code_kraski_snaruji = $('#code_kraski_snaruji'+String(id));
        code_kraski_snaruji.append(code_kras_snaruji);
        select_nakleyka.children("span").remove();
        select_nakleyka.children("select").remove();
        const newDiv = "<select class ='kod_nakleyki' style='text-transform: uppercase; width: 70px;' required></select>"
        select_nakleyka.append(newDiv)
        get_nakleyka()

        if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА'){
            var brands =`<select class="form-select form-select-sm text-center"  style="width:55px;" id='brand_k_vnutri`+String(id)+`' required>
                <option  value="0" selected></option>
                <option value="A">A</option>
                <option value="B">B</option>
                <option value="R">R</option>
                <option value="T">T</option>
                <option value="J">J</option>
                <option value="P">P</option>
                <option value="M">M</option>
            </select>`
            var brand_kraski_vnutri = $('#brand_kraski_vnutri'+String(id));
            brand_kraski_vnutri.append(brands)

            var code_kras_vnut =`<input type="text" class="form-control " id ='code_kraski_vnut' aria-describedby="inputGroup-sizing-sm" style="width:100px;" required>`
            var code_kraski_vnutri = $('#code_kraski_vnutri'+String(id));
            code_kraski_vnutri.append(code_kras_vnut)


        }else{

        }

        if (String(val) == '5'){
            var svet_lamplonka_snaruji = $('#svet_dekplonka_snaruji'+String(id));
            svet_lamplonka_snaruji.attr("disabled",false);

            if(combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА'){
                var svet_lamplonka_vnutri = $('#svet_dekplonka_vnutri'+String(id));
                svet_lamplonka_vnutri.attr("disabled",false);

            }
        } 
    }
}


function svet_lamplonka_snaruji_selected(id,val){
    var code_lamplonka_snaruji = $('#code_lamplonka_snaruji'+String(id));
    code_lamplonka_snaruji.text(String(val))
}
function svet_lamplonka_vnutri_selected(id,val){
    var code_lamplonka_vnutri = $('#code_lamplonka_vnutri'+String(id));
    code_lamplonka_vnutri.text(String(val))
}