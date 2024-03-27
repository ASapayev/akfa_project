
text =""

for (let i = 1; i <= 5; i++) {
    text +=`
    <tr id='table_tr` +String(i)+`' >
                                
    <td >
        <div class="input-group input-group-sm mb-1">
            <div>
                <button type="button" class="btn btn-warning" onclick="artukil_clear(`+String(i)+`)" style="font-size: 12px;">Очистить</button>     
            </div>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            <div><span class ='nazvaniye_system` +String(i)+`'style="text-transform: uppercase;" style="font-size: 12px;"></span></div>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            <select class=" form-control" style="background-color:#ddebf7; width: 140px; font-size:10px" id="artikul`+String(i)+`"  onchange='clear_artikul(`+String(i)+`)'></select>
        </div>
    </td>
    
    
    <td >
        <div class="input-group input-group-sm mb-1">
            <input type="text" class="form-control "  style='width:50px' onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled aria-describedby="inputGroup-sizing-sm" name ='length`+String(i)+`' id="length`+String(i)+`"  >
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 165px;text-transform: uppercase; font-size:12px; padding-right:0px;" onchange="tip_pokritiya_selected(`+String(i)+`,this.value)" disabled id='tip_pokritiya`+String(i)+`' required>
                <option  selected></option>
                <option value="1" >Неокрашенный</option>
                <option value="2">Белый</option>
                <option value="3">Окрашенный</option>
                <option value="4">Ламинированный</option>
                <option value="5">Сублимированный</option>
                <option value="6">Анодированный</option>
              </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1" style="width: 60px;">
       
        <select class="form-select" aria-label="" style="width: 50px;"  disabled id='splav`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)">
            
            <option value="" selected  ></option>
            <option value="60" >60</option>
            <option value="63" >63</option>
            <option value="82" >82</option>
        </select>
        
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1"  style="width: 60px;">
        <select class="form-select" aria-label="" style="width: 50px;!important" disabled  id='tip_zakalyonnosti`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)">
            <option value="" selected ></option>
            <option value="T4" >T4</option>
            <option value="T5" >T5</option>
            <option value="T6" >T6</option>
            <option value="T66" >T66</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1" style="font-size: small; text-transform: uppercase; width:130px">
            <div>
                <span class =' text-center pl-1' style="font-size: small; text-transform: uppercase;" id ='combination` +String(i)+`'></span>
            </div>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1" >
        <div>
            <span class =' text-center' style="font-size: small;font-weight: bold; text-transform: uppercase;" id ='brand_kraski_snaruji` +String(i)+`'></span>
        </div>
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1" style="width: 100px;">
        <div>
            <span class =' text-center' style="font-size: small; font-weight: bold; text-transform: uppercase;width: 100px;" id ='code_kraski_snaruji` +String(i)+`'></span>
        </div>
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1">
        <div>
            <span class =' text-center' style="font-size: small;font-weight: bold; text-transform: uppercase;" id ='brand_kraski_vnutri` +String(i)+`'></span>
        </div>
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1" style="width: 100px;">
        <div>
            <span class =' text-center' style="font-size: small; font-weight: bold; text-transform: uppercase; width:100px" id ='code_kraski_vnutri` +String(i)+`' ></span>
        </div>
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1">    
        <select class="form-select" aria-label="" style="width: 75px;" onchange="svet_dekplonka_snaruji_selected(`+String(i)+`,this.value)"  id='svet_dekplonka_snaruji`+String(i)+`' disabled>
            <option  value="" selected></option>
            <option value="Золотой Дуб 7777" >7777</option>
            <option value="Махагон 3701">3701</option>
            <option value="3D 3702">3702</option>
            <option value="Дуб мокко">8888</option>
            <option value="Шеф. сер. дуб">9999</option>
            <option value="XXXX">XXXX</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            <div>
                <em><span class =' text-center ' style="font-size: 10px;  font-weight: bold; text-transform: uppercase;" id ='code_dekplonka_snaruji` +String(i)+`' disabled ></span></em>
            </div>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1"  >    
        <select class="form-select" aria-label="" style="width: 75px;" onchange="svet_dekplonka_vnutri_selected(`+String(i)+`,this.value)"  id='svet_dekplonka_vnutri`+String(i)+`' disabled>
            <option  value="" selected></option>
            <option value="Золотой Дуб 7777" >7777</option>
            <option value="Махагон 3701">3701</option>
            <option value="3D 3702">3702</option>
            <option value="Дуб мокко">8888</option>
            <option value="Шеф. сер. дуб">9999</option>
            <option value="XXXX">XXXX</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            <div>
            <em><span class =' text-center ' style="font-size: 10px; font-weight: bold; text-transform: uppercase;" id ='code_dekplonka_vnutri` +String(i)+`' disabled></span></em>
            </div>
        </div>
    </td>

    

    <td >
        <div class="input-group input-group-sm mb-1">    
        <select class="form-select" aria-label="" style="width: 220px;" onchange="svet_lamplonka_snaruji_selected(`+String(i)+`,this.value)" disabled id='svet_lamplonka_snaruji`+String(i)+`'>
            <option  value="" selected></option>
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
    
    <td >
        <div class="input-group input-group-sm mb-1">
            <div>
                <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;padding-left:35%;" id ='code_lamplonka_snaruji` +String(i)+`'></span>
            </div>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 220px;" onchange="svet_lamplonka_vnutri_selected(`+String(i)+`,this.value)" disabled id='svet_lamplonka_vnutri`+String(i)+`'>
                <option  value="" selected></option>
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
    <td >
        <div class="input-group input-group-sm mb-1">
            <div>
                <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;padding-left:35%" id='code_lamplonka_vnutri`+String(i)+`'></span>
            </div>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1" style="width: 75px;">
        <div id='anod`+String(i)+`' class='anood'  style="width: 75px;" ></div>            
        </div>
    </td> 
    <td >
        <div class="input-group input-group-sm mb-1" style="width: 75px;">
        <div id='anod_vnutr`+String(i)+`'  style="width: 75px;"></div>            
        </div>
        </div>
    </td> 
    <td >
        <div class="input-group input-group-sm mb-1" style="width: 60px;">
        <select class="form-select" aria-label=""   disabled id='contactnost_anodirovki`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)">
            <option  value=""></option>
            <option value="YC" >YC</option>
            <option value="NC">NC</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <div>
            <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;" id='tip_anodirovki`+String(i)+`'></span>
        </div>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <div>
            <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='sposob_anodirovki`+String(i)+`'></span>
        </div>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1" id="nakleyka`+String(i)+`">
        <span id='nakleyka_nt`+String(i)+`' style='display:none;padding-left:35%'>NT1</span>
        <span id='nakleyka_org`+String(i)+`' style='display:none;padding-left:35%'></span>
        <div id='nakleyka_select`+String(i)+`' style='display:none;padding-left:35%'>
            <select class ='kod_nakleyki`+String(i)+`'  style='text-transform: uppercase; width: 70px;padding-left:35%' onchange="create_kratkiy_tekst(`+String(i)+`)"></select>
        </div>
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
        <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='kratkiy_tekst`+String(i)+`'></span>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type="text" class="form-control "  style='width:90px;display:none;'   aria-describedby="inputGroup-sizing-sm"  id="sap_code_ruchnoy`+String(i)+`"  >           
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type="text" class="form-control "  style='width:220px;display:none;'   aria-describedby="inputGroup-sizing-sm"  id="kratkiy_text_ruchnoy`+String(i)+`"  >
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




for (let i = 1; i <= 6; i++) {
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
    // tip_pokritiya.val('').change();
    tip_pokritiya.attr("disabled",false);
    nazvaniye_system.text(e.params.data.system);
    combination.text(e.params.data.combination)

    var nakleyka_kode = e.params.data.code_nakleyka
    
    $('.select2-selection__rendered').css('font-size', '15px');
    
    
    
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

data_base = {}


function get_nakleyka(i){
    $('.kod_nakleyki'+i).select2({
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


function get_anod(termo=false){
    $('.kod_anod_snar').select2({
        ajax: {
            url: "/client/anod-list",
            dataType: 'json',
            processResults: function(data){
                return {results: $.map(data, function(item){
                    return {id:item.id,text:item.code_sveta,tip_anod:item.tip_anod,sposob_anod:item.sposob_anod}
                })
            };
            }
        }
        });
    if (termo){
        $('.kod_anod_vnutri').select2({
            ajax: {
                url: "/client/anod-list",
                dataType: 'json',
                processResults: function(data){
                    return {results: $.map(data, function(item){
                        return {id:item.id,text:item.code_sveta,tip_anod:item.tip_anod,sposob_anod:item.sposob_anod}
                    })
                };
                }
            }
            });
    }
}



function clear_artikul(id){
    var table_tr =$('#table_tr'+id);
    // table_tr.remove()
    // $('#artikul'+id).val(null).trigger('change');
    $('.nazvaniye_system'+id).text('');
    var tip_pokritiya = $('#tip_pokritiya'+String(id));
    tip_pokritiya.val('0').change();
    tip_pokritiya.attr("disabled",true);
    // var select_nakleyka = $('#nakleyka'+String(id));
    // select_nakleyka.children("span").remove();
    // select_nakleyka.children("select").remove();
    delete data_base[id]

    var kratkiy_tekst = document.getElementById('kratkiy_tekst'+String(id));
    kratkiy_tekst.innerText="";


    
    
    table_tr.css('background-color','white')
    

    var code_kraski_snaruji = $('#code_kraski_snaruji'+String(id));
    var code_kraski_vnutri = $('#code_kraski_vnutri'+String(id));
    var brand_kraski_vnutri = $('#brand_kraski_vnutri'+String(id))
    var brand_kraski_snaruji = $('#brand_kraski_snaruji'+String(id))
    code_kraski_snaruji.text("");
    code_kraski_vnutri.text("");
    brand_kraski_vnutri.text("");
    brand_kraski_snaruji.text("");

    code_kraski_snaruji.css("border-color",'#dedad9');
    code_kraski_vnutri.css("border-color",'#dedad9');
    brand_kraski_vnutri.css("border-color",'#dedad9');
    brand_kraski_snaruji.css("border-color",'#dedad9');



    var dlina =$('#length'+String(id));
    dlina.val('');
    dlina.attr("disabled",true);
    dlina.css("border-color",'#dedad9');

    var combination= document.getElementById('combination'+String(id));
    console.log(combination,'dddd',combination.innerText)
    combination.innerText='';
    // combination.text("");

    var svet_lamplonka_snaruji = $('#svet_lamplonka_snaruji'+String(id));
    svet_lamplonka_snaruji.val('0').change();
    svet_lamplonka_snaruji.attr("disabled",true);
    svet_lamplonka_snaruji.css("border-color",'#dedad9');
    var code_lamplonka_snaruji = $('#code_lamplonka_snaruji'+String(id));
    code_lamplonka_snaruji.text("")
    

    var svet_lamplonka_vnutri = $('#svet_lamplonka_vnutri'+String(id));
    svet_lamplonka_vnutri.val('0').change();
    svet_lamplonka_vnutri.attr("disabled",true);
    svet_lamplonka_vnutri.css("border-color",'#dedad9');
    var code_lamplonka_vnutri = $('#code_lamplonka_vnutri'+String(id));
    code_lamplonka_vnutri.text("")

    var nakleyka_nt1 = $('#nakleyka_nt'+String(id))
    var nakleyka_org =$('#nakleyka_org'+String(id));
    var nakleyka_select = $('#nakleyka_select'+String(id));
    nakleyka_nt1.css('display','none');
    nakleyka_org.css('display','none');
    nakleyka_select.css('display','none');


    var splav = $('#splav'+String(id));
    // splav.val('0').change();
    splav.attr("disabled",true);
    splav.css("border-color",'#dedad9');
    var tip_zakalyonnosti = $('#tip_zakalyonnosti'+String(id));
    // tip_zakalyonnosti.val('0').change();
    tip_zakalyonnosti.attr("disabled",true);
    tip_zakalyonnosti.css("border-color",'#dedad9');
    // console.log(data_base)
    // console.log(typeof(data_base))
    
}

function artukil_clear(id){
    $('#artikul'+id).val(null).trigger('change');
    clear_artikul(id)
    var goods_group = $('#goods_group'+String(id));
    var tex_name = $('#tex_name'+String(id));
    var id_klaes =$('#id_klaes'+String(id))
    var klaes_nazvaniye =$('#klaes_nazvaniye'+String(id))
    var code_sveta =$('#code_sveta'+String(id))
    var klaes_kratkiy =$('#klaes_kratkiy'+String(id))
    var sap_code_ruchnoy =$('#sap_code_ruchnoy'+String(id))
    var kratkiy_text_ruchnoy =$('#kratkiy_text_ruchnoy'+String(id))

    tex_name.text('')
    kratkiy_text_ruchnoy.val('')
    sap_code_ruchnoy.val('')
    goods_group.val('0').change();
    id_klaes.val('')
    klaes_nazvaniye.val('')
    code_sveta.val('')
    klaes_kratkiy.val('')
    goods_group.css('border-color','red')
    id_klaes.css('border-color','red')
    klaes_nazvaniye.css('border-color','red')
    code_sveta.css('border-color','red')
    klaes_kratkiy.css('border-color','red')
    kratkiy_text_ruchnoy.css('display','none')
    sap_code_ruchnoy.css('display','none')
    goods_group.css('display','none')
    id_klaes.css('display','none')
    klaes_nazvaniye.css('display','none')
    code_sveta.css('display','none')
    klaes_kratkiy.css('display','none')
}


function tip_pokritiya_selected(id,val){

    var element33 = document.getElementById("table_tr"+id);
    element33.style.backgroundColor='white';

    
    
    var select_anod_snar = $('#anod'+String(id));
    select_anod_snar.children("span").css('display','none');
    select_anod_snar.children("select").remove();

    var dlina =$('#length'+String(id));
    dlina.attr("disabled",false);
    dlina.css("border-color",'#fc2003');

    var select_anod_vnut = $('#anod_vnutr'+String(id));
    select_anod_vnut.children("span").css('display','none');
    select_anod_vnut.children("select").remove();
    
    var code_kraski_snaruji = $('#code_kraski_snaruji'+String(id));
    var code_kraski_vnutri = $('#code_kraski_vnutri'+String(id));
    var brand_kraski_vnutri = $('#brand_kraski_vnutri'+String(id))
    var brand_kraski_snaruji = $('#brand_kraski_snaruji'+String(id))
    var kratkiy_tekst = $('#kratkiy_tekst'+String(id));
    kratkiy_tekst.text("");
    code_kraski_snaruji.text("");
    code_kraski_vnutri.text("");
    brand_kraski_vnutri.text("");
    brand_kraski_snaruji.text("");

    code_kraski_snaruji.css("border-color",'#dedad9');
    code_kraski_vnutri.css("border-color",'#dedad9');
    brand_kraski_vnutri.css("border-color",'#dedad9');
    brand_kraski_snaruji.css("border-color",'#dedad9');


    var combination= $('#combination'+String(id));
    combination_text = combination.text();
  

    



    var svet_lamplonka_snaruji = $('#svet_lamplonka_snaruji'+String(id));
    svet_lamplonka_snaruji.val('0').change();
    svet_lamplonka_snaruji.attr("disabled",true);
    svet_lamplonka_snaruji.css("border-color",'#dedad9');
    var code_lamplonka_snaruji = $('#code_lamplonka_snaruji'+String(id));
    code_lamplonka_snaruji.text("")
    code_lamplonka_snaruji.css("border-color",'#dedad9');

    var svet_lamplonka_vnutri = $('#svet_lamplonka_vnutri'+String(id));
    svet_lamplonka_vnutri.val('0').change();
    svet_lamplonka_vnutri.attr("disabled",true);
    svet_lamplonka_vnutri.css("border-color",'#dedad9');
    var code_lamplonka_vnutri = $('#code_lamplonka_vnutri'+String(id));
    code_lamplonka_vnutri.text("")
    code_lamplonka_vnutri.css("border-color",'#dedad9');

    var svet_dekplonka_snaruji = $('#svet_dekplonka_snaruji'+String(id));
    svet_dekplonka_snaruji.val('0').change();
    svet_dekplonka_snaruji.attr("disabled",true);
    svet_dekplonka_snaruji.css("border-color",'#dedad9');

    var code_dekplonka_snaruji = $('#code_dekplonka_snaruji'+String(id));
    code_dekplonka_snaruji.text("");
    code_dekplonka_snaruji.css("border-color",'#dedad9');

    var svet_dekplonka_vnutri = $('#svet_dekplonka_vnutri'+String(id));
    svet_dekplonka_vnutri.val('0').change();
    svet_dekplonka_vnutri.attr("disabled",true);
    svet_dekplonka_vnutri.css("border-color",'#dedad9');
    var code_dekplonka_vnutri = $('#code_dekplonka_vnutri'+String(id));
    code_dekplonka_vnutri.text("");
    code_dekplonka_vnutri.css("border-color",'#dedad9');

    var code_svet_anodirovki_vnutri = $('#code_svet_anodirovki_vnutri'+String(id));
    code_svet_anodirovki_vnutri.val('0').change();
    code_svet_anodirovki_vnutri.attr("disabled",true);
    code_svet_anodirovki_vnutri.css("border-color",'#dedad9');

    // console.log(,'eeeee')
    if(String(val) !=''){

        
        var sap_code_ruchnoy =$('#sap_code_ruchnoy'+String(id))
        var kratkiy_text_ruchnoy =$('#kratkiy_text_ruchnoy'+String(id))
    
        kratkiy_text_ruchnoy.val('')
        sap_code_ruchnoy.val('')
        sap_code_ruchnoy.css('display','block')
        kratkiy_text_ruchnoy.css('display','block')
    }
    
    var contactnost_anodirovki = $('#contactnost_anodirovki'+String(id));
    if(data_base[id]){
        contactnost_anodirovki.val('0').change();
    }
    contactnost_anodirovki.attr("disabled",true);
    contactnost_anodirovki.css("border-color",'#dedad9');


    var splav = $('#splav'+String(id));
    // console.log(splav,'splavvvv')
    splav.attr("disabled",false);
    splav.val('');
    splav.css("border-color","#fc2003");
    var tip_zakalyonnosti = $('#tip_zakalyonnosti'+String(id));
    tip_zakalyonnosti.attr("disabled",false);
    tip_zakalyonnosti.val("");
    tip_zakalyonnosti.css("border-color","#fc2003");





    var tip_anodirovki =$('#tip_anodirovki'+String(id));
    var sposob_anodirovki = $('#sposob_anodirovki'+String(id));
    
    tip_anodirovki.text("");
    sposob_anodirovki.text("")
    var nakleyka_nt1 = $('#nakleyka_nt'+String(id))
    var nakleyka_org =$('#nakleyka_org'+String(id));
    var nakleyka_select = $('#nakleyka_select'+String(id));

    if(String(val) == '1'){
        data_base[id] = new Neokrashenniy()
        nakleyka_nt1.css('display','block');
        nakleyka_org.css('display','none');
        nakleyka_select.css('display','none');

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
        data_base[id] = new Beliy()
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

        
        
        var nakleyka_kode = nakleyka_org.text()
        if (nakleyka_kode !=''){
            nakleyka_nt1.css('display','none');
            nakleyka_org.css('display','block');
            nakleyka_select.css('display','none');
        }else{
            nakleyka_nt1.css('display','none');
            nakleyka_org.css('display','none');
            nakleyka_select.css('display','block');
            get_nakleyka(id)
        }
            
    }else if(String(val) == '3' || String(val) == '4'|| String(val) == '5'){

        if(String(val) == '3'){
            data_base[id] = new Okrashenniy()
        }else if(String(val) == '4'){
            data_base[id] = new Laminatsiya()
        }else if(String(val) == '5'){
            data_base[id] = new Sublimatsiya()
        } 
        
        var brands =`<select class="form-select form-select-sm text-center"  style="width:55px;border-color:#fc2003" id='brand_k_snaruji`+String(id)+`'  onchange="create_kratkiy_tekst(`+String(id)+`)" required>
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
        var code_kras_snaruji =`<input type="text"  class="form-control " id ='code_kraski_snar`+String(id)+`' aria-describedby="inputGroup-sizing-sm" style="width: 65px;border-color: red;height:30px"  onkeyup="create_kratkiy_tekst(`+String(id)+`)" required>`
        // var code_kraski_snaruji = $('#code_kraski_snaruji'+String(id));
        code_kraski_snaruji.append(code_kras_snaruji);
        code_kraski_snaruji.css("border-color",'#fc2003')
        
        // var code_kraski_snaruji = document.getElementById('code_kraski_snaruji'+String(id));
        // console.log(code_kraski_snaruji)
        // if(code_kraski_snaruji){
        //     code_kraski_snaruji.style.borderColor='red';
        // } 
        // var code_kraski_snar =$('#code_kraski_snaruji'+String(id))
        // code_kraski_snar.css("border-color",'#fc2003');
        
        var nakleyka_kode = nakleyka_org.text()
        if (nakleyka_kode !=''){
            nakleyka_nt1.css('display','none');
            nakleyka_org.css('display','block');
            nakleyka_select.css('display','none');
        }else{
            nakleyka_nt1.css('display','none');
            nakleyka_org.css('display','none');
            nakleyka_select.css('display','block');
            get_nakleyka(id)
        }
       

        if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА'){
            var brands =`<select class="form-select form-select-sm text-center"  style="width:55px;border-color:#fc2003" id='brand_k_vnutri`+String(id)+`' onchange="create_kratkiy_tekst(`+String(id)+`)" required>
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

            var code_kras_vnut =`<input type="text" class="form-control " style='border-color:#fc2003;width:65px; height:30px' id ='code_kraski_vnut`+String(id)+`' aria-describedby="inputGroup-sizing-sm"  onkeyup="create_kratkiy_tekst(`+String(id)+`)" required>`
            var code_kraski_vnutri = $('#code_kraski_vnutri'+String(id));
            code_kraski_vnutri.append(code_kras_vnut)


        }

        if (String(val) == '4'){
            var svet_lamplonka_snaruji = $('#svet_lamplonka_snaruji'+String(id));
            svet_lamplonka_snaruji.attr("disabled",false);
            svet_lamplonka_snaruji.attr("required",true);
            svet_lamplonka_snaruji.css("border-color",'#fc2003');
            var svet_lamplonka_vnutri = $('#svet_lamplonka_vnutri'+String(id));
            svet_lamplonka_vnutri.attr("disabled",false);
            svet_lamplonka_vnutri.attr("required",true);
            svet_lamplonka_vnutri.css("border-color",'#fc2003');

            
        }

        if (String(val) == '5'){
            
            var svet_dekplonka_snaruji = $('#svet_dekplonka_snaruji'+String(id));
            svet_dekplonka_snaruji.attr("disabled",false);
            svet_dekplonka_snaruji.attr("required",true);
            svet_dekplonka_snaruji.css("border-color",'#fc2003');
           
            if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА'){
                var svet_dekplonka_vnutri = $('#svet_dekplonka_vnutri'+String(id));
                svet_dekplonka_vnutri.attr("disabled",false);
                svet_dekplonka_vnutri.attr("required",true);
                svet_dekplonka_vnutri.css("border-color",'#fc2003');
            }
            
        }
        

    }else if(String(val) == '6'){
        data_base[id] = new Anodirovka()
        const newDiv = `<select class="form-select kod_anod_snar" aria-label="" style="width: 100px; border-color:#fc2003;!important" onchange="code_svet_anodirovki_snaruji_selected(`+String(id)+`,this.value)"  id='code_svet_anodirovki_snaruji`+String(id)+`' required></select>`
        select_anod_snar.append(newDiv) 

        if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА'){
            const newDiv = `<select class="form-select kod_anod_vnutri" aria-label="" style="width: 100px;border-color:#fc2003" onchange="create_kratkiy_tekst(`+String(id)+`)"  id='code_svet_anodirovki_vnutr`+String(id)+`' required></select>`
            select_anod_vnut.append(newDiv) 
            get_anod(termo=true)

            var code_svet_anodirovki_vnutri = $('#code_svet_anodirovki_vnutri'+String(id));
            code_svet_anodirovki_vnutri.attr("disabled",false);
            code_svet_anodirovki_vnutri.attr("required",true);
            code_svet_anodirovki_vnutri.css("border-color",'#fc2003');

        }else{
            get_anod()
            
        }

        

        var contactnost_anodirovki = $('#contactnost_anodirovki'+String(id));
        console.log(contactnost_anodirovki)
        contactnost_anodirovki.attr("disabled",false);
        contactnost_anodirovki.attr("required",true);
        contactnost_anodirovki.css("border-color",'red');

        
        var nakleyka_kode = nakleyka_org.text()
        if (nakleyka_kode !=''){
            nakleyka_nt1.css('display','none');
            nakleyka_org.css('display','block');
            nakleyka_select.css('display','none');
        }else{
            nakleyka_nt1.css('display','none');
            nakleyka_org.css('display','none');
            nakleyka_select.css('display','block');
            get_nakleyka(id)
        }
        
        
        
    }
    
    create_kratkiy_tekst(id);
}










function code_svet_anodirovki_snaruji_selected(id,val){
    $("#code_svet_anodirovki_snaruji"+String(id)).on("select2:select", function (e) { 
    
        var tip_anodirovki =$('#tip_anodirovki'+String(id));
        var sposob_anodirovki = $('#sposob_anodirovki'+String(id));
        console.log(e.params.data.text);
        tip_anodirovki.text(e.params.data.tip_anod);
        sposob_anodirovki.text(e.params.data.sposob_anod);

        var selectedOption = $(this).find(':selected');
            $(this).siblings('.select2-container').find('.select2-selection--single').css('border-color', '#000');
    
    
    });
    if (val !=''){
        create_kratkiy_tekst(id);
    }

}

function svet_lamplonka_snaruji_selected(id,val){
    var code_lamplonka_snaruji = $('#code_lamplonka_snaruji'+String(id));
    code_lamplonka_snaruji.text(String(val))
    
    var svet_lamplonka_snaruji = document.getElementById('svet_lamplonka_snaruji'+String(id))
    svet_lamplonka_snaruji.style.borderColor='red';
    // data_base[id].kod_lam_sn =NaN;
    create_kratkiy_tekst(id);
    

}
function svet_lamplonka_vnutri_selected(id,val){
    var code_lamplonka_vnutri = $('#code_lamplonka_vnutri'+String(id));
    code_lamplonka_vnutri.text(String(val));
    var svet_lamplonka_vnutri = document.getElementById('svet_lamplonka_vnutri'+String(id))
    svet_lamplonka_vnutri.style.borderColor='red';
    create_kratkiy_tekst(id);
    
}


function svet_dekplonka_snaruji_selected(id,val){
    var code_dekplonka_snaruji = $('#code_dekplonka_snaruji'+String(id));
    code_dekplonka_snaruji.text(String(val))
    var selectElement = document.getElementById('svet_dekplonka_snaruji'+String(id));
    selectElement.style.borderColor='red';
    create_kratkiy_tekst(id);
    
}
function svet_dekplonka_vnutri_selected(id,val){
    var code_dekplonka_vnutri = $('#code_dekplonka_vnutri'+String(id));
    code_dekplonka_vnutri.text(String(val));
    var selectElement = document.getElementById('svet_dekplonka_vnutri'+String(id));
    selectElement.style.borderColor='red';
    console.log(selectElement)
    create_kratkiy_tekst(id);
}



class Neokrashenniy{
    constructor(
                id=NaN, 
                full=false, 
                splav=NaN,
                tip_zak=NaN,
                dlina=NaN,
                kod_kraska_sn=NaN,
                kod_nakleyki=NaN,
                kod_kraska_vn=NaN,
                is_termo=false
                ) 
        {
        this.id = id;
        this.full = full;
        this.splav = splav;
        this.tip_zak = tip_zak;
        this.dlina = dlina;
        this.kod_kraska_sn = kod_kraska_sn;
        this.kod_kraska_vn = kod_kraska_vn;
        this.kod_nakleyki = kod_nakleyki;
        this.is_termo = is_termo;
        }

    get_kratkiy_tekst(){
        if(!this.is_termo){
           
            if(this.splav && this.tip_zak && this.dlina && this.kod_kraska_sn && this.kod_nakleyki ){
                return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.kod_kraska_sn +'  ' +this.kod_nakleyki
            }else{
                return 'XXXXXXXX'
            }
        }else{
            if(this.splav && this.tip_zak && this.dlina && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki){
                return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.kod_kraska_sn +'/'+this.kod_kraska_vn+'  ' +this.kod_nakleyki
            }else{
                return 'XXXXXXXX'
            }
        }
    }
  }

class Beliy{
    constructor(id=NaN, full=false,splav=NaN,tip_zak=NaN,tex_name=NaN,dlina=NaN,brend_kraska_sn=NaN,brend_kraska_vn=NaN,kod_kraska_sn=NaN,kod_kraska_vn=NaN,kod_nakleyki=NaN,
        
        is_termo=false) {
        this.id = id;
        this.full = full;
        this.splav = splav;
        this.tip_zak = tip_zak;
        this.dlina = dlina;
        this.brend_kraska_sn = brend_kraska_sn;
        this.brend_kraska_vn = brend_kraska_vn;
        this.kod_kraska_sn = kod_kraska_sn;
        this.kod_kraska_vn = kod_kraska_vn;
        this.kod_nakleyki = kod_nakleyki;
        this.is_termo = is_termo;
       
    }

    get_kratkiy_tekst(){
        if(!this.is_termo){

            if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_nakleyki ){
                return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'  ' +this.kod_nakleyki
            }else{
                return 'XXXXXXXX'
            }
        }else{

            if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki ){
                return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+'  ' +this.kod_nakleyki
            }else{
                return 'XXXXXXXX'
            }
        }
    }
  }

class Okrashenniy{
    constructor(id=NaN, full=false,splav=NaN,tip_zak=NaN,tex_name=NaN,dlina=NaN,brend_kraska_sn=NaN,brend_kraska_vn=NaN,kod_kraska_sn=NaN,
       
        kod_kraska_vn=NaN,kod_nakleyki=NaN,is_termo=false) {
      this.id = id;
      this.full = full;
      this.splav = splav;
      this.tip_zak = tip_zak;
      this.dlina = dlina;
      this.brend_kraska_sn = brend_kraska_sn;
      this.brend_kraska_vn = brend_kraska_vn;
      this.kod_kraska_sn = kod_kraska_sn;
      this.kod_kraska_vn = kod_kraska_vn;
      this.kod_nakleyki = kod_nakleyki;
      this.is_termo = is_termo;
    }
    get_kratkiy_tekst(){
        if(!this.is_termo){
            if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_nakleyki){
                return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'  ' +this.kod_nakleyki
            }else{
                return 'XXXXXXXX'
            }
        }else{
           
            if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki){
                return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn+'/'+this.brend_kraska_vn+this.kod_kraska_vn+'  ' +this.kod_nakleyki
            }else{
                return 'XXXXXXXX'
            }
        }
    }
  }

  
class Sublimatsiya{
    constructor(id=NaN, full=false,splav=NaN,tip_zak=NaN,tex_name=NaN,
        
        dlina=NaN,brend_kraska_sn=NaN,brend_kraska_vn=NaN,kod_kraska_sn=NaN,kod_kraska_vn=NaN,kod_dekor_sn=NaN,kod_dekor_vn=NaN,kod_nakleyki=NaN,is_termo=false) {
      this.id = id;
      this.full = full;
      this.splav = splav;
      this.tip_zak = tip_zak;
      this.dlina = dlina;
      this.brend_kraska_sn = brend_kraska_sn;
      this.brend_kraska_vn = brend_kraska_vn;
      this.kod_kraska_sn = kod_kraska_sn;
      this.kod_kraska_vn = kod_kraska_vn;
      this.kod_dekor_sn = kod_dekor_sn;
      this.kod_dekor_vn = kod_dekor_vn;
      this.kod_nakleyki = kod_nakleyki;
      this.is_termo = is_termo;
    }

    get_kratkiy_tekst(){
        if(!this.is_termo){
            if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_dekor_sn && this.kod_nakleyki){
                return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_dekor_sn + '  ' +this.kod_nakleyki
            }else{
                return 'XXXXXXXX'
            }
        }else{
            if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_dekor_sn && this.kod_dekor_vn){
                return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+'_'+this.kod_dekor_sn+'/'+this.kod_dekor_vn + '  ' +this.kod_nakleyki
            }else{
                return 'XXXXXXXX'
            }
        }
    }
  }
class Laminatsiya{
    constructor(id=NaN, full=false,splav=NaN,tip_zak=NaN,tex_name=NaN,
       
        dlina=NaN,brend_kraska_sn=NaN,brend_kraska_vn=NaN,kod_kraska_sn=NaN,kod_kraska_vn=NaN,kod_lam_sn=NaN,kod_lam_vn=NaN,kod_nakleyki=NaN,is_termo=false) {
      this.id = id;
      this.full = full;
      this.splav = splav;
      this.tip_zak = tip_zak;
      this.dlina = dlina;
      this.brend_kraska_sn = brend_kraska_sn;
      this.brend_kraska_vn = brend_kraska_vn;
      this.kod_kraska_sn = kod_kraska_sn;
      this.kod_kraska_vn = kod_kraska_vn;
      this.kod_lam_sn = kod_lam_sn;
      this.kod_lam_vn = kod_lam_vn;
      this.kod_nakleyki = kod_nakleyki;
      this.is_termo = is_termo;
      
    }
    get_kratkiy_tekst(){
        if(!this.is_termo){
            if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki ){
                return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + '  ' +this.kod_nakleyki
            }else{
                return 'XXXXXXXX'
            }
        }else{
            if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki ){
                return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn + this.kod_kraska_vn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + '  ' +this.kod_nakleyki
            }else{
                return 'XXXXXXXX'
            }
        }
    }
  }
class Anodirovka{
    constructor(id=NaN, full=false,splav=NaN,tip_zak=NaN,tex_name=NaN,
        dlina=NaN,kod_anod_sn=NaN,kod_anod_vn=NaN,kod_nakleyki=NaN,contactnost_anod=NaN,is_termo=false) {
      this.id = id;
      this.full = full;
      this.splav = splav;
      this.tip_zak = tip_zak;
      this.dlina = dlina;
      this.kod_anod_sn = kod_anod_sn;
      this.kod_anod_vn = kod_anod_vn;
      this.kod_nakleyki = kod_nakleyki;
      this.contactnost_anod = contactnost_anod;
      this.is_termo = is_termo;
      
    }

    get_kratkiy_tekst(){
        if(!this.is_termo){
            if(this.splav && this.tip_zak && this.dlina && this.kod_anod_sn && this.kod_nakleyki && this.contactnost_anod){
                return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.kod_anod_sn + '  ' + this.contactnost_anod + '  ' + this.kod_nakleyki
            }else{
                return 'XXXXXXXX'
            }
        }else{
            if(this.splav && this.tip_zak && this.dlina && this.kod_anod_sn && this.kod_anod_vn && this.kod_nakleyki && this.contactnost_anod){
                return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.kod_anod_sn +'/'+this.kod_anod_vn+ '  ' + this.contactnost_anod + '  ' + this.kod_nakleyki
            }else{
                return 'XXXXXXXX'
            }

        }
    }
  }



function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
    var kratkiy_tekst = $('#kratkiy_tekst'+String(id));
    var combination= $('#combination'+String(id));
    combination_text = combination.text();
    var val = $('#tip_pokritiya'+String(id)).val();


    var dlina = $('#length'+String(id));
    if(dlina.val()!=''){
        dlina.css("border-color",'#dedad9');
        data_base[id].dlina = dlina.val();
    }else{
        dlina.css("border-color",'red');
        data_base[id].dlina = NaN;
    }

    
    
    var splav = $('#splav'+String(id));
    if(splav){
        if(splav.val()!='0' && splav.val()!='' && splav.val()!=null){
            splav.css("border-color",'#dedad9');
            data_base[id].splav = splav.val();
        }else{
            splav.css("border-color",'red');
            data_base[id].splav = NaN;
        }
    }

    var tip_zakalyonnosti = $('#tip_zakalyonnosti'+String(id));
    if(tip_zakalyonnosti){
        if(tip_zakalyonnosti.val()!='0' && tip_zakalyonnosti.val()!='' && tip_zakalyonnosti.val()!=null){
            tip_zakalyonnosti.css("border-color",'#dedad9');
            data_base[id].tip_zak = tip_zakalyonnosti.val();
        }else{
            tip_zakalyonnosti.css("border-color",'red');
            data_base[id].tip_zak = NaN;
        }
    }

    if(String(val) == '1'){
            
            data_base[id].kod_kraska_sn = 'MF'
            data_base[id].kod_nakleyki = 'NT1'
        
         if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА')
            {
                
                data_base[id].kod_kraska_vn = 'MF'
                data_base[id].is_termo = true;
                
            }

    }else if(String(val) == '2'){
        data_base[id].brend_kraska_sn ='R'
        data_base[id].kod_kraska_sn ='9016'

        var nakleyka_nt1 = document.getElementById('nakleyka_nt'+String(id))
        var nakleyka_org = document.getElementById('nakleyka_org'+String(id))
        var nakleyka_select = document.getElementById('nakleyka_select'+String(id))
        
        var style_nt1 = window.getComputedStyle(nakleyka_nt1);
        var style_org = window.getComputedStyle(nakleyka_org);
        var style_select = window.getComputedStyle(nakleyka_select);

        var displayValue_nt1 = style_nt1.getPropertyValue('display');
        var displayValue_org = style_org.getPropertyValue('display');
        var displayValue_select = style_select.getPropertyValue('display');
        
        if(displayValue_nt1 != 'none'){
            data_base[id].kod_nakleyki = nakleyka_nt1.innerText;
        }else if(displayValue_org != 'none'){
            data_base[id].kod_nakleyki = nakleyka_org.innerText;
        }else if(displayValue_select != 'none'){
           
            const spanTextbox = nakleyka_select.querySelector('span[role="textbox"]');

            if(spanTextbox.innerText !=''){
                data_base[id].kod_nakleyki = spanTextbox.innerText;
            }

        }
        

        if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА')
            {

                data_base[id].brend_kraska_vn = 'R';
                data_base[id].kod_kraska_vn = '9016';
                data_base[id].is_termo = true
            }
    }
    else if(String(val) == '3' || String(val) == '4'|| String(val) == '5'){
        
        var brend_kraska_sn = $('#brand_k_snaruji'+String(id))
        if(brend_kraska_sn.val() != '0' && brend_kraska_sn.val()  != undefined){
            brend_kraska_sn.css("border-color",'#dedad9');
            data_base[id].brend_kraska_sn =brend_kraska_sn.val();
        }else{
            brend_kraska_sn.css("border-color",'red');
            data_base[id].brend_kraska_sn =NaN;
        }
        
        var code_kraski_snaruji = $('#code_kraski_snar'+String(id));
        if(code_kraski_snaruji.val() != '0' && code_kraski_snaruji.val()  != undefined && code_kraski_snaruji.val() != ''){
            code_kraski_snaruji.css("border-color",'#dedad9');
            data_base[id].kod_kraska_sn =code_kraski_snaruji.val();
        }else{
            code_kraski_snaruji.css("border-color",'red');
            data_base[id].kod_kraska_sn =NaN;
        }
       
       


        if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА')
            {

                var brend_kraska_vn = $('#brand_k_vnutri'+String(id))
                if(brend_kraska_vn.val() != '0' && brend_kraska_vn.val()  != undefined){
                    brend_kraska_vn.css("border-color",'#dedad9');
                    data_base[id].brend_kraska_vn =brend_kraska_vn.val();
                }else{
                    brend_kraska_vn.css("border-color",'red');
                    data_base[id].brend_kraska_vn =NaN;
                }

                var code_kraski_vnut = $('#code_kraski_vnut'+String(id))
                a1=code_kraski_vnut.val() != '0'
                a2=code_kraski_vnut.val() != undefined
                a3=code_kraski_vnut.val() != ''
                console.log(a1,a2,a3)
                if((code_kraski_vnut.val() != '0') && (code_kraski_vnut.val()  != undefined)&&code_kraski_vnut.val()!=''){
                    console.log(code_kraski_vnut.val(),'vnuttttrrrr')
                    code_kraski_vnut.css("border-color",'#dedad9');
                    data_base[id].kod_kraska_vn =code_kraski_vnut.val();
                }else{
                    console.log(code_kraski_vnut.val(),'sssssssss')
                    code_kraski_vnut.css("border-color",'red');
                    data_base[id].kod_kraska_vn =NaN;
                }
                
                data_base[id].is_termo =true;
                
            }



        var nakleyka_nt1 = document.getElementById('nakleyka_nt'+String(id))
        var nakleyka_org = document.getElementById('nakleyka_org'+String(id))
        var nakleyka_select = document.getElementById('nakleyka_select'+String(id))
        
        var style_nt1 = window.getComputedStyle(nakleyka_nt1);
        var style_org = window.getComputedStyle(nakleyka_org);
        var style_select = window.getComputedStyle(nakleyka_select);

        var displayValue_nt1 = style_nt1.getPropertyValue('display');
        var displayValue_org = style_org.getPropertyValue('display');
        var displayValue_select = style_select.getPropertyValue('display');
        
        if(displayValue_nt1 != 'none'){
            data_base[id].kod_nakleyki = nakleyka_nt1.innerText;
        }else if(displayValue_org != 'none'){
            data_base[id].kod_nakleyki = nakleyka_org.innerText;
        }else if(displayValue_select != 'none'){
           
            const spanTextbox = nakleyka_select.querySelector('span[role="textbox"]');

            if(spanTextbox.innerText != ''){
                data_base[id].kod_nakleyki = spanTextbox.innerText;
            }
        }

       
        if(String(val) == '4'){
            
            var code_lamplonka_snaruji = document.getElementById('code_lamplonka_snaruji'+String(id))//.innerText;
            
            if(code_lamplonka_snaruji.innerText !=''){
                var svet_lamplonka_snaruji = document.getElementById('svet_lamplonka_snaruji'+String(id))//.innerText;
                svet_lamplonka_snaruji.style.borderColor='#dedad9';
                data_base[id].kod_lam_sn =code_lamplonka_snaruji.innerText;;
            }else{
                data_base[id].kod_lam_sn =NaN;
            }
            
            var code_lamplonka_vnutri = document.getElementById('code_lamplonka_vnutri'+String(id));
           

            if(code_lamplonka_vnutri.innerText !=''){
                var svet_lamplonka_vnutri = document.getElementById('svet_lamplonka_vnutri'+String(id))//.innerText;
                svet_lamplonka_vnutri.style.borderColor='#dedad9';
                
                data_base[id].kod_lam_vn =code_lamplonka_vnutri.innerText;
            }else{
                data_base[id].kod_lam_vn =NaN;
            }

        }
        if(String(val) == '5'){
            var selectElement = document.getElementById('svet_dekplonka_snaruji'+String(id));

            var selectedIndex = selectElement.selectedIndex;
            if(selectedIndex !=-1){
                selectElement.style.borderColor='#dedad9';
                var selectedOption = selectElement.options[selectedIndex];
                var selectedText = selectedOption.textContent;
                
                if (selectedText!=''){
                    data_base[id].kod_dekor_sn =selectedText;
                }else{
                    selectElement.style.borderColor='red';
                    data_base[id].kod_dekor_sn =NaN;
                }
            }else{
                data_base[id].kod_dekor_sn =NaN;
            }

            if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА')
            {
                var selectElement = document.getElementById('svet_dekplonka_vnutri'+String(id));

                var selectedIndex = selectElement.selectedIndex;
                if(selectedIndex !=-1){
                    selectElement.style.borderColor='#dedad9';
                    var selectedOption = selectElement.options[selectedIndex];
                    var selectedText = selectedOption.textContent;
                    data_base[id].kod_dekor_vn =selectedText;
                    if (selectedText!=''){
                        data_base[id].kod_dekor_vn =selectedText;
                    }else{
                        selectElement.style.borderColor='red';
                        data_base[id].kod_dekor_vn =NaN;
                    }
                }else{
                    selectElement.style.borderColor='red';
                    data_base[id].kod_dekor_vn =NaN;
                }
            }
            // this.kod_dekor_sn && this.kod_dekor_vn

        }

    }else if(String(val) == '6'){
        var nakleyka_nt1 = document.getElementById('nakleyka_nt'+String(id))
        var nakleyka_org = document.getElementById('nakleyka_org'+String(id))
        var nakleyka_select = document.getElementById('nakleyka_select'+String(id))
        
        var style_nt1 = window.getComputedStyle(nakleyka_nt1);
        var style_org = window.getComputedStyle(nakleyka_org);
        var style_select = window.getComputedStyle(nakleyka_select);

        var displayValue_nt1 = style_nt1.getPropertyValue('display');
        var displayValue_org = style_org.getPropertyValue('display');
        var displayValue_select = style_select.getPropertyValue('display');
        
        if(displayValue_nt1 != 'none'){
            data_base[id].kod_nakleyki = nakleyka_nt1.innerText;
        }else if(displayValue_org != 'none'){
            data_base[id].kod_nakleyki = nakleyka_org.innerText;
        }else if(displayValue_select != 'none'){
           
            const spanTextbox = nakleyka_select.querySelector('span[role="textbox"]');
            if(spanTextbox.innerText !=''){
                data_base[id].kod_nakleyki = spanTextbox.innerText;
            }

        }

        var anod_sn = document.getElementById("anod"+String(id))
        const spanTextbox1 = anod_sn.querySelector('span[role="textbox"]');
        
        const spanss =document.querySelector('.anood .select2-container .select2-selection--single')
        if(spanTextbox1){
            if(spanTextbox1.innerText !='' ){
                spanss.style.borderColor='#dedad9';
                data_base[id].kod_anod_sn = spanTextbox1.innerText;
            }else{
                spanss.style.borderColor='red';
                data_base[id].kod_anod_sn = NaN;
            }
        }
        if(combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА'){
            data_base[id].is_termo =true;
            var anod_sn = document.getElementById("anod_vnutr"+String(id))
            // anod_sn.style.borderColor='#dedad9';
            const spanTextbox2 = anod_sn.querySelector('span[role="textbox"]');
            if(spanTextbox2){
                if(spanTextbox2.innerText !=''){
                    spanTextbox2.style.borderColor='#dedad9';
                    data_base[id].kod_anod_vn = spanTextbox2.innerText;
                }else{
                    spanTextbox2.style.borderColor='red';
                    data_base[id].kod_anod_vn = NaN;
                }
            }
        }
        var contactnost_anodirovki = $('#contactnost_anodirovki'+String(id));
        if(contactnost_anodirovki.val()!='0' && contactnost_anodirovki.val()!=''&& contactnost_anodirovki.val()!=null){
            
            contactnost_anodirovki.css("border-color",'#dedad9');
            data_base[id].contactnost_anod = contactnost_anodirovki.val();
        }else{

            var contactnost_anodirovki = $('#contactnost_anodirovki'+String(id));
            contactnost_anodirovki.css("border-color",'red');
            console.log(contactnost_anodirovki)
            data_base[id].contactnost_anod = NaN;
        }

    }

    var text =data_base[id].get_kratkiy_tekst()
    if(text != 'XXXXXXXX'){
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','#2de319')
        data_base[id].full =true
    }else{
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','white')
        data_base[id].full =false

    }
    kratkiy_tekst.text(text)

    }
}

function add_column(){
        
    text =""
    var sizee = Object.keys(data_base).length;
    console.log(sizee)
    var sizeee = $('#table-artikul tr').length;
    
    for (let i = sizeee + 1; i < sizeee+2; i++) {
        text +=`
        <tr id='table_tr` +String(i)+`' >
                                    
        <td >
            <div class="input-group input-group-sm mb-1">
                <div>
                    <button type="button" class="btn btn-warning" onclick="artukil_clear(`+String(i)+`)" style="font-size: 12px;">Очистить</button>     
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <div><span class ='nazvaniye_system` +String(i)+`'style="text-transform: uppercase;" style="font-size: 12px;"></span></div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class=" form-control" style="background-color:#ddebf7; width: 140px; font-size:10px" id="artikul`+String(i)+`"  onchange='clear_artikul(`+String(i)+`)'></select>
            </div>
        </td>
        
        
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type="text" class="form-control "  style='width:50px' onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled aria-describedby="inputGroup-sizing-sm" name ='length`+String(i)+`' id="length`+String(i)+`"  >
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 165px;text-transform: uppercase; font-size:12px; padding-right:0px;" onchange="tip_pokritiya_selected(`+String(i)+`,this.value)" disabled id='tip_pokritiya`+String(i)+`' required>
                    <option  selected></option>
                    <option value="1" >Неокрашенный</option>
                    <option value="2">Белый</option>
                    <option value="3">Окрашенный</option>
                    <option value="4">Ламинированный</option>
                    <option value="5">Сублимированный</option>
                    <option value="6">Анодированный</option>
                  </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 60px;">
           
            <select class="form-select" aria-label="" style="width: 50px;"  disabled id='splav`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)">
                
                <option value="63" selected  >63</option>
            </select>
            
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1"  style="width: 60px;">
            <select class="form-select" aria-label="" style="width: 50px;!important"  disabled id='tip_zakalyonnosti`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option value="T6" selected >T6</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" style="font-size: small; text-transform: uppercase; width:130px">
                <div>
                    <span class =' text-center pl-1' style="font-size: small; text-transform: uppercase;" id ='combination` +String(i)+`'></span>
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" >
            <div>
                <span class =' text-center' style="font-size: small;font-weight: bold; text-transform: uppercase;" id ='brand_kraski_snaruji` +String(i)+`'></span>
            </div>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 100px;">
            <div>
                <span class =' text-center' style="font-size: small; font-weight: bold; text-transform: uppercase;width: 100px;" id ='code_kraski_snaruji` +String(i)+`'></span>
            </div>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <div>
                <span class =' text-center' style="font-size: small;font-weight: bold; text-transform: uppercase;" id ='brand_kraski_vnutri` +String(i)+`'></span>
            </div>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 100px;">
            <div>
                <span class =' text-center' style="font-size: small; font-weight: bold; text-transform: uppercase; width:100px" id ='code_kraski_vnutri` +String(i)+`' ></span>
            </div>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">    
            <select class="form-select" aria-label="" style="width: 75px;" onchange="svet_dekplonka_snaruji_selected(`+String(i)+`,this.value)"  id='svet_dekplonka_snaruji`+String(i)+`' disabled>
                <option  value="" selected></option>
                <option value="Золотой Дуб 7777" >7777</option>
                <option value="Махагон 3701">3701</option>
                <option value="3D 3702">3702</option>
                <option value="Дуб мокко">8888</option>
                <option value="Шеф. сер. дуб">9999</option>
                <option value="XXXX">XXXX</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <div>
                    <em><span class =' text-center ' style="font-size: 10px;  font-weight: bold; text-transform: uppercase;" id ='code_dekplonka_snaruji` +String(i)+`' disabled ></span></em>
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1"  >    
            <select class="form-select" aria-label="" style="width: 75px;" onchange="svet_dekplonka_vnutri_selected(`+String(i)+`,this.value)"  id='svet_dekplonka_vnutri`+String(i)+`' disabled>
                <option  value="" selected></option>
                <option value="Золотой Дуб 7777" >7777</option>
                <option value="Махагон 3701">3701</option>
                <option value="3D 3702">3702</option>
                <option value="Дуб мокко">8888</option>
                <option value="Шеф. сер. дуб">9999</option>
                <option value="XXXX">XXXX</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <div>
                <em><span class =' text-center ' style="font-size: 10px; font-weight: bold; text-transform: uppercase;" id ='code_dekplonka_vnutri` +String(i)+`' disabled></span></em>
                </div>
            </div>
        </td>
    
        
    
        <td >
            <div class="input-group input-group-sm mb-1">    
            <select class="form-select" aria-label="" style="width: 220px;" onchange="svet_lamplonka_snaruji_selected(`+String(i)+`,this.value)" disabled id='svet_lamplonka_snaruji`+String(i)+`'>
                <option  value="" selected></option>
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
        
        <td >
            <div class="input-group input-group-sm mb-1">
                <div>
                    <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;padding-left:35%;" id ='code_lamplonka_snaruji` +String(i)+`'></span>
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 220px;" onchange="svet_lamplonka_vnutri_selected(`+String(i)+`,this.value)" disabled id='svet_lamplonka_vnutri`+String(i)+`'>
                    <option  value="" selected></option>
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
        <td >
            <div class="input-group input-group-sm mb-1">
                <div>
                    <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;padding-left:35%" id='code_lamplonka_vnutri`+String(i)+`'></span>
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 75px;">
            <div id='anod`+String(i)+`' class='anood'  style="width: 75px;" ></div>            
            </div>
        </td> 
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 75px;">
            <div id='anod_vnutr`+String(i)+`'  style="width: 75px;"></div>            
            </div>
            </div>
        </td> 
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 60px;">
            <select class="form-select" aria-label=""   disabled id='contactnost_anodirovki`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option  value=""></option>
                <option value="YC" >YC</option>
                <option value="NC">NC</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <div>
                <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;" id='tip_anodirovki`+String(i)+`'></span>
            </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <div>
                <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='sposob_anodirovki`+String(i)+`'></span>
            </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" id="nakleyka`+String(i)+`">
            <span id='nakleyka_nt`+String(i)+`' style='display:none;padding-left:35%'>NT1</span>
            <span id='nakleyka_org`+String(i)+`' style='display:none;padding-left:35%'></span>
            <div id='nakleyka_select`+String(i)+`' style='display:none;padding-left:35%'>
                <select class ='kod_nakleyki`+String(i)+`'  style='text-transform: uppercase; width: 70px;padding-left:35%' onchange="create_kratkiy_tekst(`+String(i)+`)"></select>
            </div>
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
            <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='kratkiy_tekst`+String(i)+`'></span>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type="text" class="form-control "  style='width:90px;display:none;'   aria-describedby="inputGroup-sizing-sm"  id="sap_code_ruchnoy`+String(i)+`"  >           
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type="text" class="form-control "  style='width:220px;display:none;'   aria-describedby="inputGroup-sizing-sm"  id="kratkiy_text_ruchnoy`+String(i)+`"  >
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
        var nazvaniye_system =$('.nazvaniye_system'+String(i));
        var combination = $('#combination'+String(i));
        var tip_pokritiya = $('#tip_pokritiya'+String(i));
        // tip_pokritiya.val('').change();
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

function ready_all(){

    var form = document.getElementById('basic_form');
    var fields = form.querySelectorAll('[required]');
    var isValid = true;

    // fields.forEach(function(field) {
    //     if (!field.value.trim()) {
    //         isValid = false;
    //         return;
    //     }
    // });

    if (!isValid) {
        alert('Please fill in all required fields.');
    } else {

        var add_column_btn = $('#add_column_btn')
        add_column_btn.css('display','none')
        
        var ready_btn = $('#ready_btn')
        ready_btn.css('display','none') 


        var zagruzka_file = $('#zagruzka_file')
        zagruzka_file.css('display','block')
        // form.submit(); // Submit the form if all required fields are filled
    }



    
    //////////////////////////////////////
    
    // var edit_btn = $('#edit_btn')
    // edit_btn.css('display','block')
    
   
}