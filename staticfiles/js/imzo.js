
text =""

for (let i = 1; i <= 4; i++) {
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
            <select class="form-select" aria-label="" style="width: 200px;text-transform: uppercase;" onchange="tip_pokritiya_selected(`+String(i)+`,this.value)" disabled id='tip_pokritiya`+String(i)+`'>
                <option selected></option>
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
        <div class="input-group input-group-sm mb-1">
            <div>
                <span class =' text-center p-1' style="font-size: small; text-transform: uppercase;" id ='combination` +String(i)+`'></span>
            </div>
        </div>
    </td>
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
        <div>
            <span class =' text-center p-1' style="font-size: small; text-transform: uppercase;" id ='brand_kraski_snaruji` +String(i)+`'></span>
        </div>
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1">
        <div>
            <span class =' text-center p-1' style="font-size: small; text-transform: uppercase;" id ='code_kraski_snaruji` +String(i)+`'></span>
        </div>
        </div>
    </td>
    <td style="background-color:#92d050;">
        <div class="input-group input-group-sm mb-1">
        <div>
            <span class =' text-center p-1' style="font-size: small; text-transform: uppercase;" id ='brand_kraski_vnutri` +String(i)+`'></span>
        </div>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <div>
            <span class =' text-center p-1' style="font-size: small; text-transform: uppercase;" id ='code_kraski_vnutri` +String(i)+`'></span>
        </div>
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
    <td style="background-color:#ddebf7;">
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
    tip_pokritiya.attr("disabled",false);
    nazvaniye_system.text(e.params.data.system);
    combination.text(e.params.data.combination)
    // console.log(e.params.data.combination);
    var nakleyka_kode = e.params.data.code_nakleyka
    // console.log(nakleyka_kode)
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
        const newDiv = "<select class ='kod_nakleyki' style='text-transform: uppercase; width: 70px;''></select>"
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
    tip_pokritiya.attr("disabled",true);
    var select_nakleyka = $('#nakleyka'+String(id));
    select_nakleyka.children("span").remove();
    select_nakleyka.children("select").remove();

}


function tip_pokritiya_selected(id,val){
    var select_nakleyka = $('#nakleyka'+String(id));
    select_nakleyka.children("span").remove();
    select_nakleyka.children("select").remove();
    if(String(val) == '1'){
        var newDiv = "<span>NT1</span>"; 
        select_nakleyka.append(newDiv);
        var combination= $('#combination'+String(id));
        combination_text = combination.text();
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
        var combination= $('#combination'+String(id));
        combination_text = combination.text();
        if (combination_text.toUpperCase() == 'БЕЗ ТЕРМОМОСТА'){

            var code_kraski_snaruji = $('#code_kraski_snaruji'+String(id))
            var brand_kraski_vnutri = $('#brand_kraski_snaruji'+String(id))
            code_kraski_snaruji.text('MF')
            brand_kraski_vnutri.text('MF')
        }else{
            var code_kraski_snaruji = $('#code_kraski_snaruji'+String(id));
            var code_kraski_vnutri = $('#code_kraski_vnutri'+String(id));
            var brand_kraski_vnutri = $('#brand_kraski_vnutri'+String(id))
            var brand_kraski_snaruji = $('#brand_kraski_snaruji'+String(id))
            code_kraski_snaruji.text('MF');
            code_kraski_vnutri.text('MF');

        }
    }
}