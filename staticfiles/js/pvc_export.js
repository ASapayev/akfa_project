class BasePokritiya{
    constructor(
        full=false,//done
        id=NaN,//done
        nazvaniye_system=NaN,//done
        camera=NaN,//done
        base_artikul=NaN,//done
        kod_k_component=NaN,//done
        tip_pokritiya=NaN,//done
        kod_svet_zames=NaN,
        dlina=NaN,//done
        svet_lamplonka_snaruji=NaN,//done
        kod_lam_sn=NaN,//done
        svet_lamplonka_vnutri=NaN,//done
        kod_lam_vn=NaN,//done
        kod_svet_rezini=NaN,//done
        svet_rezin=NaN,//done
        kod_nakleyki=NaN,//done
        nadpis_nakleyki=NaN,//done
        gruppa_materialov='PVCGP',//done
        kratkiy_tekst=NaN,//done
        sap_code=NaN,//done
        krat=NaN,//done
        sena_export=NaN,//done
        comment=NaN,//done
        artikul=NaN,
        is_iklyuch=false
        ) {
      
            this.full=full;
            this.id=id;
            this.nazvaniye_system=nazvaniye_system;
            this.camera=camera;
            this.base_artikul=base_artikul;
            this.kod_k_component=kod_k_component;
            this.tip_pokritiya=tip_pokritiya;
            this.kod_svet_zames=kod_svet_zames;
            this.dlina=dlina;
            this.svet_lamplonka_snaruji=svet_lamplonka_snaruji;
            this.kod_lam_sn=kod_lam_sn;
            this.svet_lamplonka_vnutri=svet_lamplonka_vnutri;
            this.kod_lam_vn=kod_lam_vn;
            this.kod_svet_rezini=kod_svet_rezini;
            this.svet_rezin=svet_rezin;
            this.kod_nakleyki=kod_nakleyki;
            this.nadpis_nakleyki=nadpis_nakleyki;
            this.gruppa_materialov=gruppa_materialov;
            this.kratkiy_tekst=kratkiy_tekst;
            this.sap_code=sap_code;
            this.krat=krat;
            this.sena_export=sena_export;
            this.comment=comment;
            this.artikul=artikul;
            this.is_iklyuch=is_iklyuch;

    }
    get_kratkiy_tekst(){
        switch(this.id){
            case 1: if(this.is_iklyuch){
                if(this.dlina && this.kod_svet_zames && this.kod_nakleyki){
                    if(this.sena_export){
                        return {'text':this.artikul + '  '+ this.kod_svet_zames + ' L' + this.dlina +'  ' +this.kod_nakleyki,'accept':true}
                    }else{
                        return {'text':this.artikul + '  '+ this.kod_svet_zames + ' L' + this.dlina +'  ' +this.kod_nakleyki,'accept':false}
                    }
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
    
                }else{
        
                    if(this.kod_svet_rezini && this.dlina && this.kod_svet_zames && this.kod_nakleyki){
                        if(this.sena_export){
                            return {'text':this.artikul + '  '+ this.kod_svet_zames + ' L' + this.dlina +'  '+this.kod_svet_rezini +'  ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.artikul + '  '+ this.kod_svet_zames + ' L' + this.dlina +'  '+this.kod_svet_rezini +'  ' +this.kod_nakleyki,'accept':false}
                        }
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }break;
            case 2: if(this.is_iklyuch){
                if(this.dlina && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki && this.kod_svet_zames){
                    if(this.sena_export){
                        return {'text':this.artikul + '  '+this.kod_svet_zames + ' L' + this.dlina +'  ' + this.kod_lam_sn+'/'+this.kod_lam_vn + '  '+this.kod_nakleyki,'accept':true}
                    }else{
                        return {'text':this.artikul + '  '+this.kod_svet_zames + ' L' + this.dlina +'  ' + this.kod_lam_sn+'/'+this.kod_lam_vn + '  '+this.kod_nakleyki,'accept':false}
                    }
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
        
                    if(this.dlina && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki && this.kod_svet_rezini && this.kod_svet_zames){
                        if(this.sena_export){
                            return {'text':this.artikul + '  '+this.kod_svet_zames + ' L' + this.dlina +'  ' + this.kod_lam_sn+'/'+this.kod_lam_vn + '  '+this.kod_svet_rezini +'  '+this.kod_nakleyki,'accept':true} 
                        }else{
                            return {'text':this.artikul + '  '+this.kod_svet_zames + ' L' + this.dlina +'  ' + this.kod_lam_sn+'/'+this.kod_lam_vn + '  '+this.kod_svet_rezini +'  '+this.kod_nakleyki,'accept':false} 
                        }
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }break;
        }
       
    }
  }





text =""

for (let i = 1; i <= 5; i++) {
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
        <div class="input-group input-group-sm mb-1" style='width:150px;'>
            <span class ='nazvaniye_system` +String(i)+`'style="text-transform: uppercase;font-size: 10px; font-weight:700;padding:5px;width:150px" ></span>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            <b><span id='camera` +String(i)+`'style="text-transform: uppercase; font-size:12px;padding-left:5px"></span></b>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            <select class=" form-control basic_artikul" style="background-color:#ddebf7; width: 140px; font-size:10px " id="artikul`+String(i)+`" onchange='clear_artikul(`+String(i)+`)'></select>
        </div>
        <span style='display:none' id='artikul_pvc` +String(i)+`'></span>
        <span style='display:none' id='iskyucheniye` +String(i)+`'></span>
    </td>
    
    
    <td >
        <div class="input-group input-group-sm mb-1">
            <b><span  id ='kod_komponent` +String(i)+`'style="text-transform: uppercase;font-size: 12px;padding-left:5px;"></span></b>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 177px;text-transform: uppercase; font-size:12px; padding-right:0px;" onchange="tip_pokritiya_selected(`+String(i)+`,this.value)" disabled id='tip_pokritiya`+String(i)+`' required>
                <option  selected ></option>
                <option value="1" >Неламинированный</option>
                <option value="2" >Ламинированный</option>
              </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1" style="width: 70px;">
       
        <select class="form-select" aria-label="" style="width: 70px;"  disabled id='kod_svet_zames`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)">
            <option  value="" selected ></option>
            <option value="F8" >F8</option>
            <option value="PE" >PE</option>
            <option value="N1" >N1</option>
            <option value="EG1" >EG1</option>
            <option value="LE" >LE</option>
            <option value="BR1" >BR1</option>
            <option value="WT7" >WT7</option>
            <option value="BR10" >BR10</option>
            <option value="W6" >W6</option>
            <option value="N2" >N2</option>
        </select>
        
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            <input type="text" class="form-control " style='width:50px' onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled aria-describedby="inputGroup-sizing-sm" name ='length`+String(i)+`' id="length`+String(i)+`"  >
        </div>
    </td>

    <td >
        <div class="input-group input-group-sm mb-1">    
        <select class="form-select" aria-label="" style="width: 220px;" onchange="svet_lamplonka_snaruji_selected(`+String(i)+`,this.value)" disabled id='svet_lamplonka_snaruji`+String(i)+`'>
            <option  value="" selected></option>
            <option value="0027">Золотой дуб IW</option>
            <option value="0300">Дуб мокко IW</option>
            <option value="0549">Красный Орех IW</option>
            <option value="0550">Орех IW</option>
            <option value="1004">Мет платин</option>
            <option value="1005">Мет серый кварц</option>
            <option value="1006">Мет серый антрацит</option>
            <option value="1012">Алюкс антрацит</option>
            <option value="1015">АЛЮКС БЕЛЫЙ АЛЮМИН</option>
            <option value="1016">Алюкс серый алюмин</option>
            <option value="2007">Красный орех</option>
            <option value="2012">Орех</option>
            <option value="2025">Светлый дуб</option>
            <option value="2036">Золотой дуб</option>
            <option value="2048">Дуб мокко</option>
            <option value="3001">Терновый дуб солод</option>
            <option value="3002">Шеф Альпийский дуб</option>
            <option value="3003">Гранитовый шеф дуб</option>
            <option value="3042">Дерево бальза</option>
            <option value="3043">Вишня амаретто</option>
            <option value="3059">Орех терра</option>
            <option value="3062">Грецкий орех</option>
            <option value="3077">Винчестер</option>
            <option value="3081">Шеф дуб светлый</option>
            <option value="3083">Сантана</option>
            <option value="3086">ШЕФ ДУБ СЕРЫЙ</option>
            <option value="3091">Шеф дуб</option>
            <option value="3094">Орех Ребраун</option>
            <option value="4687">Кенсингтон серый</option>
            <option value="5057">Бриллиантвейс</option>
            <option value="6700">Темный дуб</option>
            <option value="5F00">Шеф дуб серый LG</option>
            <option value="A508">Антрацит сер ADO п</option>
            <option value="EL01">Золотой дуб Элезго</option>
            <option value="EL02">Горный Элезго</option>
            <option value="KC01">Горный KCC</option>
            <option value="S103">Красный орех ADO п</option>
            <option value="S141">Дуб мокко ADO п</option>
            <option value="S150">Золотой дуб ADO п</option>
            <option value="S500">Золотой дуб ADO</option>
            <option value="S508">Антрацит серый ADO</option>
            <option value="S541">Дуб мокко ADO</option>
            <option value="5003">Темный Антрацит</option>
            <option value="S513">Красный орех ADO</option>
            <option value="S540">Золотой дуб S540</option>
            <option value="5F01">Шеф дуб сер 5F01</option>
            <option value="1022">Ocean Blue</option>
            <option value="ASA1128">ASA1128</option>
            <option value="6030">МАТОВЫЙ БЕЛЫЙ</option>
            <option value="6062">МАТОВЫЙ ЧЁРНЫЙ</option>
            <option value="2509">АНТРАЦИТ СЕРЫЙ LG</option>
            <option value="9252">Винчестер Renolit</option>
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
                <option value="0027">Золотой дуб IW</option>
                <option value="0300">Дуб мокко IW</option>
                <option value="0549">Красный Орех IW</option>
                <option value="0550">Орех IW</option>
                <option value="1004">Мет платин</option>
                <option value="1005">Мет серый кварц</option>
                <option value="1006">Мет серый антрацит</option>
                <option value="1012">Алюкс антрацит</option>
                <option value="1015">АЛЮКС БЕЛЫЙ АЛЮМИН</option>
                <option value="1016">Алюкс серый алюмин</option>
                <option value="2007">Красный орех</option>
                <option value="2012">Орех</option>
                <option value="2025">Светлый дуб</option>
                <option value="2036">Золотой дуб</option>
                <option value="2048">Дуб мокко</option>
                <option value="3001">Терновый дуб солод</option>
                <option value="3002">Шеф Альпийский дуб</option>
                <option value="3003">Гранитовый шеф дуб</option>
                <option value="3042">Дерево бальза</option>
                <option value="3043">Вишня амаретто</option>
                <option value="3059">Орех терра</option>
                <option value="3062">Грецкий орех</option>
                <option value="3077">Винчестер</option>
                <option value="3081">Шеф дуб светлый</option>
                <option value="3083">Сантана</option>
                <option value="3086">ШЕФ ДУБ СЕРЫЙ</option>
                <option value="3091">Шеф дуб</option>
                <option value="3094">Орех Ребраун</option>
                <option value="4687">Кенсингтон серый</option>
                <option value="5057">Бриллиантвейс</option>
                <option value="6700">Темный дуб</option>
                <option value="5F00">Шеф дуб серый LG</option>
                <option value="A508">Антрацит сер ADO п</option>
                <option value="EL01">Золотой дуб Элезго</option>
                <option value="EL02">Горный Элезго</option>
                <option value="KC01">Горный KCC</option>
                <option value="S103">Красный орех ADO п</option>
                <option value="S141">Дуб мокко ADO п</option>
                <option value="S150">Золотой дуб ADO п</option>
                <option value="S500">Золотой дуб ADO</option>
                <option value="S508">Антрацит серый ADO</option>
                <option value="S541">Дуб мокко ADO</option>
                <option value="5003">Темный Антрацит</option>
                <option value="S513">Красный орех ADO</option>
                <option value="S540">Золотой дуб S540</option>
                <option value="5F01">Шеф дуб сер 5F01</option>
                <option value="1022">Ocean Blue</option>
                <option value="ASA1128">ASA1128</option>
                <option value="6030">МАТОВЫЙ БЕЛЫЙ</option>
                <option value="6062">МАТОВЫЙ ЧЁРНЫЙ</option>
                <option value="2509">АНТРАЦИТ СЕРЫЙ LG</option>
                <option value="9252">Винчестер Renolit</option>
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
        <div class="input-group input-group-sm mb-1" style="width: 60px;">
        <select class="form-select" aria-label="" style="width: 50px;border-color:red;display:none"   id='kod_svet_rezini`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)">
            <option  value="" selected ></option>
            <option value="Чёрная резина" >BR</option>
            <option value="Серая резина" >GR</option>
            <option value="Без резины" >NR</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            
                <span class =' text-center ' style="font-size:10px; font-weight: bold; text-transform: uppercase;" id='svet_rezin`+String(i)+`'></span>
            
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1" id="nakleyka`+String(i)+`">
        <div id='nakleyka_select`+String(i)+`' class='nak_select`+String(i)+`' style='display:none;'>
            <select class ='kod_nakleyki`+String(i)+`'  style='text-transform: uppercase; width: 70px;padding-left:35%' onchange="create_kratkiy_tekst(`+String(i)+`)"></select>
        </div>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            
                <span class ='text-center ' style="font-size:10px; font-weight: bold; text-transform: uppercase;padding:5px" id='nadpis_nakleyki`+String(i)+`'></span>
            
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            <div>
                <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;" >PVCGP</span>
            </div>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='kratkiy_tekst`+String(i)+`'></span>
        </div>
    </td>

    <td >
        <div class="input-group input-group-sm mb-1">
       
        <input type='text' class=" form-control " style=" width: 110px; font-size:10px; display:none; height:32px" id='sap_code_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
    
        </div>
    </td> 
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style=" width: 220px; font-size:10px; display:none; height:32px"  id='kratkiy_tekst_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style=" width: 220px; font-size:10px; display:none; height:32px;border-color:red;"  id='sena_export`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
       </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
       <textarea   rows='1' class=" form-control " style="width: 220px; font-size:10px;display:none;height:32px" id='comment`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></textarea >
       </div>
    </td>
   `
  }



var table = $('#table-artikul')

table.append(text)




for (let i = 1; i <= 6; i++) {
    $('#artikul'+String(i)).select2({
        ajax: {
            url: "/client/pvc-artikul-list",
            dataType: 'json',
            processResults: function(data){
                return {results: $.map(data, function(item){
                    return {id:item.id,text:item.artikul,component:item.component2,system:item.nazvaniye_sistem,camera:item.camera,kod_k_component:item.kod_k_component,iskyucheniye:item.iskyucheniye}
                })
            };
            }
        }
        });
    
    
    
    var artikulSelect = $('#artikul'+String(i));
    $.ajax({
        type: 'GET',
        url: "/client/pvc-artikul-list"
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
        var camera = $('#camera'+String(i));
        var kod_komponent = $('#kod_komponent'+String(i));
        var artikul_pvc = $('#artikul_pvc'+String(i));
        var iskyucheniye = $('#iskyucheniye'+String(i));
        var tip_pokritiya = $('#tip_pokritiya'+String(i));
        tip_pokritiya.attr("disabled",false);
        nazvaniye_system.text(e.params.data.system);
        artikul_pvc.text(e.params.data.component);
        iskyucheniye.text(e.params.data.iskyucheniye);
        camera.text(e.params.data.camera)
        kod_komponent.text(e.params.data.kod_k_component)
        
       
        var nakleyka_select = $('#nakleyka_select'+String(i));

        var length = $('#length'+String(i));
        length.attr('required',true)
        nakleyka_select.css('display','block')
        nakleyka_select.attr('required',true)
        get_nakleyka(String(i))
        
    });

}



data_base = {}


function get_nakleyka(i){
    $('.kod_nakleyki'+i).select2({
        ajax: {
            url: "/client/nakleyka-list-pvc",
            dataType: 'json',
            processResults: function(data){
                return {results: $.map(data, function(item){
                    return {id:item.id,text:item.name,nadpis:item.nadpis}
                })
            };
            }
        }
        });
        $(".kod_nakleyki"+String(i)).on("select2:select", function (e) { 
            var nadpis_nakleyki = $('#nadpis_nakleyki'+String(i));
            nadpis_nakleyki.text(e.params.data.nadpis);
            
            })
}





function artukil_clear(id){
    $('#artikul'+id).val(null).trigger('change');
    clear_artikul(id)
}



function clear_artikul(id){
    var table_tr =$('#table_tr'+id);
    $('.nazvaniye_system'+id).text('');
    var tip_pokritiya = $('#tip_pokritiya'+String(id));
    tip_pokritiya.val('0').change();
    tip_pokritiya.attr("disabled",true);
    var camera = $('#camera'+String(id));
    var kod_komponent = $('#kod_komponent'+String(id));
    var kod_svet_zames = $('#kod_svet_zames'+String(id));
    var kod_svet_rezini = $('#kod_svet_rezini'+String(id));
    var svet_rezini = $('#svet_rezin'+String(id));
    var nakleyka_select = $('.kod_nakleyki'+String(id))
    nakleyka_select.val(null).trigger('change');
    var nakleyka_select_org = document.getElementById('nakleyka_select'+String(id))
    nakleyka_select_org.style.display='none';

    camera.text('')
    kod_komponent.text('')
    svet_rezini.text('')
    kod_svet_zames.val('')
    kod_svet_zames.attr('disabled',true)
    kod_svet_zames.css('border-color','#dedad9')
    
    kod_svet_rezini.val('')
    kod_svet_rezini.css('display','none')

    delete data_base[id]

    var kratkiy_tekst = document.getElementById('kratkiy_tekst'+String(id));
    kratkiy_tekst.innerText="";


    
    
    table_tr.css('background-color','white')
    




    var dlina =$('#length'+String(id));
    dlina.val('');
    dlina.attr("disabled",true);
    dlina.css("border-color",'#dedad9');

    var combination= $('#combination'+String(id));
    combination.text("");

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

    var sap_code_ruchnoy =$('#sap_code_ruchnoy'+String(id));
    sap_code_ruchnoy.val('');
    sap_code_ruchnoy.css('display','none');
    var kratkiy_tekst_ruchnoy =$('#kratkiy_tekst_ruchnoy'+String(id));
    kratkiy_tekst_ruchnoy.val('');
    kratkiy_tekst_ruchnoy.css('display','none');
    var sena_export =$('#sena_export'+String(id));
    sena_export.val('');
    sena_export.css('border-color','red');
    sena_export.css('display','none');
   
   
   
    
}



function tip_pokritiya_selected(id,val){

    var element33 = document.getElementById("table_tr"+id);
    element33.style.backgroundColor='white';
    

    var dlina =$('#length'+String(id));
    dlina.attr("disabled",false);
    dlina.css("border-color",'#fc2003');

    

    
   
    var kratkiy_tekst = $('#kratkiy_tekst'+String(id));
    kratkiy_tekst.text("");


    
  

    var nadpis_nakleyki = $('#nadpis_nakleyki'+String(id));
    nadpis_nakleyki.text('');
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

    var sap_code_ruchnoy =$('#sap_code_ruchnoy'+String(id));
    sap_code_ruchnoy.css('display','block');
    sap_code_ruchnoy.val('');
    var kratkiy_tekst_ruchnoy =$('#kratkiy_tekst_ruchnoy'+String(id));
    kratkiy_tekst_ruchnoy.css('display','block');
    kratkiy_tekst_ruchnoy.val('');
    var sena_export =$('#sena_export'+String(id));
    sena_export.css('display','block');;
    sena_export.val('');

    var nakleyka_select = $('#nakleyka_select'+String(id));
    nakleyka_select.css('display','block');
    get_nakleyka(id)

    
    var svet_product_val =''
    var gruppa_zakupok =''
    
    var iskyucheniye =$('#iskyucheniye'+id).text()
    
    if(String(val) == '1'){
        var kod_svet_zames = $('#kod_svet_zames'+String(id));
        kod_svet_zames.attr("disabled",false);
        kod_svet_zames.css("border-color",'#fc2003');
        data_base[id] = new BasePokritiya();
        data_base[id].id = 1;
        data_base[id].tip_pokritiya = 'Неламинированный';
        var artikul_pvc = $('#artikul_pvc'+String(id));
        data_base[id].artikul= artikul_pvc.text()

        svet_product_val = 'WHITE' 
        gruppa_zakupok ='PVX OQ (Navoiy)' 
        var kod_svet_rezini = $('#kod_svet_rezini'+String(id));
        kod_svet_rezini.val('')
        kod_svet_rezini.css('display','block');
        const spanss =document.querySelector('.nak_select' +id+ ' .select2-container .select2-selection--single')
        spanss.style.borderColor='red';
        
        if(iskyucheniye =='1'){
            data_base[id].is_iklyuch=true
            kod_svet_rezini.css('display','none');
            kod_svet_rezini.css('border-color','#dedad9')
        }else{
            data_base[id].is_iklyuch=false
        }
        
    }else if(String(val) == '2'){
        
        data_base[id] = new BasePokritiya()
        data_base[id].id = 2;
        data_base[id].tip_pokritiya = 'Ламинированный';
        var artikul_pvc = $('#artikul_pvc'+String(id));
        data_base[id].artikul= artikul_pvc.text()

        svet_product_val ='LAM'
        gruppa_zakupok ='PVX LAM (Navoiy)' 
        
        var kod_svet_zames = $('#kod_svet_zames'+String(id));
        kod_svet_zames.attr("disabled",false);
        kod_svet_zames.css("border-color",'#fc2003');
        const spanss =document.querySelector('.nak_select' +id+ ' .select2-container .select2-selection--single')
        spanss.style.borderColor='red';

        var kod_svet_rezini = $('#kod_svet_rezini'+String(id));
        kod_svet_rezini.val('')

        var svet_lamplonka_snaruji = $('#svet_lamplonka_snaruji'+String(id));
        svet_lamplonka_snaruji.attr("disabled",false);
        svet_lamplonka_snaruji.attr("required",true);
        svet_lamplonka_snaruji.css("border-color",'#fc2003');
        var svet_lamplonka_vnutri = $('#svet_lamplonka_vnutri'+String(id));
        svet_lamplonka_vnutri.attr("disabled",false);
        svet_lamplonka_vnutri.attr("required",true);
        svet_lamplonka_vnutri.css("border-color",'#fc2003');

        if(iskyucheniye =='1'){
            data_base[id].is_iklyuch=true
            kod_svet_rezini.css('display','none');
        }else{
            data_base[id].is_iklyuch=false
            kod_svet_rezini.css('display','block');
        }
    }
    if(String(val) != ''){
        var base_artikul =$('#select2-artikul'+id+'-container')
        data_base[id].base_artikul = base_artikul.text()
        var nazvaniye_system = $('.nazvaniye_system'+id).text()
        var camera =$('#camera'+id).text()
        var kod_komponent =$('#kod_komponent'+id).text()
        data_base[id].nazvaniye_system = nazvaniye_system;
        data_base[id].camera = camera;
        data_base[id].kod_k_component = kod_komponent;
    }
    
    create_kratkiy_tekst(id);
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





function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
    
    var kratkiy_tekst = $('#kratkiy_tekst'+String(id));
    var combination= $('#combination'+String(id));
    combination_text = combination.text();
    var val = $('#tip_pokritiya'+String(id)).val();
    var dlina = $('#length'+String(id));
    var sena_export = $('#sena_export'+String(id));
    var sap_code_ruchnoy = $('#sap_code_ruchnoy'+String(id));
    var kratkiy_tekst_ruchnoy = $('#kratkiy_tekst_ruchnoy'+String(id));
    var comment = $('#comment'+String(id));

    if(comment.val()!=''){
        data_base[id].comment = comment.val();
    }else{
        data_base[id].comment = NaN;
    }
    if(kratkiy_tekst_ruchnoy.val()!=''){
        data_base[id].krat = kratkiy_tekst_ruchnoy.val();
    }else{
        data_base[id].krat = NaN;
    }
    if(sap_code_ruchnoy.val()!=''){
        data_base[id].sap_code = sap_code_ruchnoy.val();
    }else{
        data_base[id].sap_code = NaN;
    }
    if(dlina.val()!=''){
        dlina.css("border-color",'#dedad9');
        data_base[id].dlina = dlina.val();
    }else{
        dlina.css("border-color",'red');
        data_base[id].dlina = NaN;
    }

    if(sena_export.val()!=''){
        sena_export.css("border-color",'#dedad9');
        data_base[id].sena_export = sena_export.val();
    }else{
        sena_export.css("border-color",'red');
        data_base[id].sena_export = NaN;
    }
    
    var kod_svet_zames = $('#kod_svet_zames'+String(id));
    if(kod_svet_zames){
        if(kod_svet_zames.val()!='0' && kod_svet_zames.val()!='' && kod_svet_zames.val()!=null){
            kod_svet_zames.css("border-color",'#dedad9');
            data_base[id].kod_svet_zames = kod_svet_zames.val()
        }else{
            data_base[id].kod_svet_zames = NaN;
            kod_svet_zames.css("border-color",'red');
        }
    }
    
    
    var iskyucheniye =$('#iskyucheniye' +id).text()

    if(iskyucheniye =='1'){

        var kod_svet_rezini =$('#kod_svet_rezini' + id);
        if(kod_svet_rezini.val()!=''){
            var svet_rezin =$('#svet_rezin' + id);
            var selectedText = $("#kod_svet_rezini"+id + " option:selected").text();
            svet_rezin.text(kod_svet_rezini.val())
            kod_svet_rezini.css('border-color','#dedad9')
            data_base[id].svet_rezin =kod_svet_rezini.val();
            data_base[id].kod_svet_rezini =selectedText;
        }else{
            var svet_rezin =$('#svet_rezin' + id);
            svet_rezin.text('')
            data_base[id].svet_rezin =NaN;
            data_base[id].kod_svet_rezini = NaN
        }
        
    }else{
        
        var kod_svet_rezini =$('#kod_svet_rezini' + id);
        if(kod_svet_rezini.val()!=''){
            var svet_rezin =$('#svet_rezin' + id);
            var selectedText = $("#kod_svet_rezini"+id + " option:selected").text();
            svet_rezin.text(kod_svet_rezini.val())
            kod_svet_rezini.css('border-color','#dedad9')
            data_base[id].svet_rezin =kod_svet_rezini.val();
            data_base[id].kod_svet_rezini =selectedText;
        }else{
            var svet_rezin =$('#svet_rezin' + id);
            svet_rezin.text('')
            data_base[id].svet_rezin =NaN;
            kod_svet_rezini.css('border-color','red')
            data_base[id].kod_svet_rezini = NaN
        }
    }


    

    if(String(val) == '1'){
       
       var nakleyka_select = document.getElementById('nakleyka_select'+String(id))
        
        const spanTextbox = nakleyka_select.querySelector('span[role="textbox"]');
        const spanss =document.querySelector('.nak_select' +id+ ' .select2-container .select2-selection--single')
        var nadpis_nak= $('#nadpis_nakleyki1'+String(id)).text()
        
        if(spanTextbox.innerText !=''){
            spanss.style.borderColor='#dedad9';
            // nakleyka_select.style.borderBlockColor='#dedad9'
            data_base[id].kod_nakleyki = spanTextbox.innerText;
            data_base[id].nadpis_nakleyki = nadpis_nak;
            
        }else{
            // spanss.style.borderColor='red';
            // nakleyka_select.style.borderBlockColor='red'
            data_base[id].nadpis_nakleyki = NaN;
            data_base[id].kod_nakleyki = NaN

        }

       
    }
    else if(String(val) == '2'){
       


       var nakleyka_select = document.getElementById('nakleyka_select'+String(id))
       const spanTextbox = nakleyka_select.querySelector('span[role="textbox"]');
       const spanss =document.querySelector('.nak_select' +id+ ' .select2-container .select2-selection--single')
       var nadpis_nak= $('#nadpis_nakleyki1'+String(id)).text()
        
       if(spanTextbox.innerText !=''){
            
            spanss.style.borderColor='#dedad9';
            // nakleyka_select.style.borderBlockColor='#dedad9'
            data_base[id].kod_nakleyki = spanTextbox.innerText;
            data_base[id].nadpis_nakleyki = nadpis_nak;
        
        }else{
            spanss.style.borderColor='red';
            data_base[id].kod_nakleyki = NaN
            data_base[id].nadpis_nakleyki = NaN;
            // nakleyka_select.style.borderBlockColor='red'

        }

        
            
        var code_lamplonka_snaruji = document.getElementById('code_lamplonka_snaruji'+String(id))//.innerText;
        
        if(code_lamplonka_snaruji.innerText !=''){
            var svet_lamplonka_snaruji = document.getElementById('svet_lamplonka_snaruji'+String(id))//.innerText;
            var svet_lamplonka_snaruji1 = $('#svet_lamplonka_snaruji'+String(id)+' option:selected').text()//.innerText;
            svet_lamplonka_snaruji.style.borderColor='#dedad9';
            data_base[id].kod_lam_sn =code_lamplonka_snaruji.innerText;
            data_base[id].svet_lamplonka_snaruji = svet_lamplonka_snaruji1;
        }else{
            data_base[id].kod_lam_sn =NaN;
            data_base[id].svet_lamplonka_snaruji = NaN;
        }
        
        var code_lamplonka_vnutri = document.getElementById('code_lamplonka_vnutri'+String(id));
        

        if(code_lamplonka_vnutri.innerText !=''){
            var svet_lamplonka_vnutri = document.getElementById('svet_lamplonka_vnutri'+String(id))//.innerText;
            var svet_lamplonka_vnutri1 = $('#svet_lamplonka_vnutri'+String(id)+' option:selected').text()//.innerText;
           
            svet_lamplonka_vnutri.style.borderColor='#dedad9';
            
            data_base[id].kod_lam_vn =code_lamplonka_vnutri.innerText;
            data_base[id].svet_lamplonka_vnutri =svet_lamplonka_vnutri1;
        }else{
            data_base[id].kod_lam_vn =NaN;
            data_base[id].svet_lamplonka_vnutri =NaN;
        }

        
        

    }






    



    var data =data_base[id].get_kratkiy_tekst()
    if(data.accept){
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','#2de319')
        data_base[id].full =true
        data_base[id].kratkiy_tekst = data.text
    }else{
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','white')
        data_base[id].full =false
        data_base[id].kratkiy_tekst = NaN;

    }
    
    kratkiy_tekst.text(data.text)

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
                
                <div class="btn-group" role="group" aria-label="Basic example">
                <button type="button" class="btn btn-warning btn-sm gradient-buttons" onclick="artukil_clear(`+String(i)+`)"  id='clear_btn`+String(i)+`'>Очистить</button>
                </div>
                    
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" style='width:150px;'>
                <span class ='nazvaniye_system` +String(i)+`'style="text-transform: uppercase;font-size: 10px; font-weight:700;padding:5px;width:150px" ></span>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <b><span id='camera` +String(i)+`'style="text-transform: uppercase; font-size:12px;padding-left:5px"></span></b>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class=" form-control basic_artikul" style="background-color:#ddebf7; width: 140px; font-size:10px " id="artikul`+String(i)+`" onchange='clear_artikul(`+String(i)+`)'></select>
            </div>
            <span style='display:none' id='artikul_pvc` +String(i)+`'></span>
            <span style='display:none' id='iskyucheniye` +String(i)+`'></span>
        </td>
        
        
        <td >
            <div class="input-group input-group-sm mb-1">
                <b><span  id ='kod_komponent` +String(i)+`'style="text-transform: uppercase;font-size: 12px;padding-left:5px;"></span></b>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 177px;text-transform: uppercase; font-size:12px; padding-right:0px;" onchange="tip_pokritiya_selected(`+String(i)+`,this.value)" disabled id='tip_pokritiya`+String(i)+`' required>
                    <option  selected ></option>
                    <option value="1" >Неламинированный</option>
                    <option value="2" >Ламинированный</option>
                  </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 70px;">
           
            <select class="form-select" aria-label="" style="width: 70px;"  disabled id='kod_svet_zames`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option  value="" selected ></option>
                <option value="F8" >F8</option>
                <option value="PE" >PE</option>
                <option value="N1" >N1</option>
                <option value="EG1" >EG1</option>
                <option value="LE" >LE</option>
                <option value="BR1" >BR1</option>
                <option value="WT7" >WT7</option>
                <option value="BR10" >BR10</option>
                <option value="W6" >W6</option>
                <option value="N2" >N2</option>
            </select>
            
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type="text" class="form-control " style='width:50px' onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled aria-describedby="inputGroup-sizing-sm" name ='length`+String(i)+`' id="length`+String(i)+`"  >
            </div>
        </td>
    
        <td >
            <div class="input-group input-group-sm mb-1">    
            <select class="form-select" aria-label="" style="width: 220px;" onchange="svet_lamplonka_snaruji_selected(`+String(i)+`,this.value)" disabled id='svet_lamplonka_snaruji`+String(i)+`'>
                <option  value="" selected></option>
                <option value="0027">Золотой дуб IW</option>
                <option value="0300">Дуб мокко IW</option>
                <option value="0549">Красный Орех IW</option>
                <option value="0550">Орех IW</option>
                <option value="1004">Мет платин</option>
                <option value="1005">Мет серый кварц</option>
                <option value="1006">Мет серый антрацит</option>
                <option value="1012">Алюкс антрацит</option>
                <option value="1015">АЛЮКС БЕЛЫЙ АЛЮМИН</option>
                <option value="1016">Алюкс серый алюмин</option>
                <option value="2007">Красный орех</option>
                <option value="2012">Орех</option>
                <option value="2025">Светлый дуб</option>
                <option value="2036">Золотой дуб</option>
                <option value="2048">Дуб мокко</option>
                <option value="3001">Терновый дуб солод</option>
                <option value="3002">Шеф Альпийский дуб</option>
                <option value="3003">Гранитовый шеф дуб</option>
                <option value="3042">Дерево бальза</option>
                <option value="3043">Вишня амаретто</option>
                <option value="3059">Орех терра</option>
                <option value="3062">Грецкий орех</option>
                <option value="3077">Винчестер</option>
                <option value="3081">Шеф дуб светлый</option>
                <option value="3083">Сантана</option>
                <option value="3086">ШЕФ ДУБ СЕРЫЙ</option>
                <option value="3091">Шеф дуб</option>
                <option value="3094">Орех Ребраун</option>
                <option value="4687">Кенсингтон серый</option>
                <option value="5057">Бриллиантвейс</option>
                <option value="6700">Темный дуб</option>
                <option value="5F00">Шеф дуб серый LG</option>
                <option value="A508">Антрацит сер ADO п</option>
                <option value="EL01">Золотой дуб Элезго</option>
                <option value="EL02">Горный Элезго</option>
                <option value="KC01">Горный KCC</option>
                <option value="S103">Красный орех ADO п</option>
                <option value="S141">Дуб мокко ADO п</option>
                <option value="S150">Золотой дуб ADO п</option>
                <option value="S500">Золотой дуб ADO</option>
                <option value="S508">Антрацит серый ADO</option>
                <option value="S541">Дуб мокко ADO</option>
                <option value="5003">Темный Антрацит</option>
                <option value="S513">Красный орех ADO</option>
                <option value="S540">Золотой дуб S540</option>
                <option value="5F01">Шеф дуб сер 5F01</option>
                <option value="1022">Ocean Blue</option>
                <option value="ASA1128">ASA1128</option>
                <option value="6030">МАТОВЫЙ БЕЛЫЙ</option>
                <option value="6062">МАТОВЫЙ ЧЁРНЫЙ</option>
                <option value="2509">АНТРАЦИТ СЕРЫЙ LG</option>
                <option value="9252">Винчестер Renolit</option>
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
                    <option value="0027">Золотой дуб IW</option>
                    <option value="0300">Дуб мокко IW</option>
                    <option value="0549">Красный Орех IW</option>
                    <option value="0550">Орех IW</option>
                    <option value="1004">Мет платин</option>
                    <option value="1005">Мет серый кварц</option>
                    <option value="1006">Мет серый антрацит</option>
                    <option value="1012">Алюкс антрацит</option>
                    <option value="1015">АЛЮКС БЕЛЫЙ АЛЮМИН</option>
                    <option value="1016">Алюкс серый алюмин</option>
                    <option value="2007">Красный орех</option>
                    <option value="2012">Орех</option>
                    <option value="2025">Светлый дуб</option>
                    <option value="2036">Золотой дуб</option>
                    <option value="2048">Дуб мокко</option>
                    <option value="3001">Терновый дуб солод</option>
                    <option value="3002">Шеф Альпийский дуб</option>
                    <option value="3003">Гранитовый шеф дуб</option>
                    <option value="3042">Дерево бальза</option>
                    <option value="3043">Вишня амаретто</option>
                    <option value="3059">Орех терра</option>
                    <option value="3062">Грецкий орех</option>
                    <option value="3077">Винчестер</option>
                    <option value="3081">Шеф дуб светлый</option>
                    <option value="3083">Сантана</option>
                    <option value="3086">ШЕФ ДУБ СЕРЫЙ</option>
                    <option value="3091">Шеф дуб</option>
                    <option value="3094">Орех Ребраун</option>
                    <option value="4687">Кенсингтон серый</option>
                    <option value="5057">Бриллиантвейс</option>
                    <option value="6700">Темный дуб</option>
                    <option value="5F00">Шеф дуб серый LG</option>
                    <option value="A508">Антрацит сер ADO п</option>
                    <option value="EL01">Золотой дуб Элезго</option>
                    <option value="EL02">Горный Элезго</option>
                    <option value="KC01">Горный KCC</option>
                    <option value="S103">Красный орех ADO п</option>
                    <option value="S141">Дуб мокко ADO п</option>
                    <option value="S150">Золотой дуб ADO п</option>
                    <option value="S500">Золотой дуб ADO</option>
                    <option value="S508">Антрацит серый ADO</option>
                    <option value="S541">Дуб мокко ADO</option>
                    <option value="5003">Темный Антрацит</option>
                    <option value="S513">Красный орех ADO</option>
                    <option value="S540">Золотой дуб S540</option>
                    <option value="5F01">Шеф дуб сер 5F01</option>
                    <option value="1022">Ocean Blue</option>
                    <option value="ASA1128">ASA1128</option>
                    <option value="6030">МАТОВЫЙ БЕЛЫЙ</option>
                    <option value="6062">МАТОВЫЙ ЧЁРНЫЙ</option>
                    <option value="2509">АНТРАЦИТ СЕРЫЙ LG</option>
                    <option value="9252">Винчестер Renolit</option>
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
            <div class="input-group input-group-sm mb-1" style="width: 60px;">
            <select class="form-select" aria-label="" style="width: 50px;border-color:red;display:none"   id='kod_svet_rezini`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option  value="" selected ></option>
                <option value="Чёрная резина" >BR</option>
                <option value="Серая резина" >GR</option>
                <option value="Без резины" >NR</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                
                    <span class =' text-center ' style="font-size:10px; font-weight: bold; text-transform: uppercase;" id='svet_rezin`+String(i)+`'></span>
                
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" id="nakleyka`+String(i)+`">
            <div id='nakleyka_select`+String(i)+`' class='nak_select`+String(i)+`' style='display:none;'>
                <select class ='kod_nakleyki`+String(i)+`'  style='text-transform: uppercase; width: 70px;padding-left:35%' onchange="create_kratkiy_tekst(`+String(i)+`)"></select>
            </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                
                    <span class ='text-center ' style="font-size:10px; font-weight: bold; text-transform: uppercase;padding:5px" id='nadpis_nakleyki`+String(i)+`'></span>
                
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <div>
                    <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;" >PVCGP</span>
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='kratkiy_tekst`+String(i)+`'></span>
            </div>
        </td>
    
        <td >
            <div class="input-group input-group-sm mb-1">
           
            <input type='text' class=" form-control " style=" width: 110px; font-size:10px; display:none; height:32px" id='sap_code_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        
            </div>
        </td> 
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 220px; font-size:10px; display:none; height:32px"  id='kratkiy_tekst_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 220px; font-size:10px; display:none; height:32px;border-color:red;"  id='sena_export`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
           </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
           <textarea   rows='1' class=" form-control " style="width: 220px; font-size:10px;display:none;height:32px" id='comment`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></textarea >
           </div>
        </td>`
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






