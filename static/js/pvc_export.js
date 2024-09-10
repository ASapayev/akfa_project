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
        artikul=NaN,//done
        is_iklyuch=false,
        is_special = false
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
            this.is_special=is_special;

    }
    get_kratkiy_tekst(){
        switch(this.id){
            case 1: if(this.is_iklyuch){
                if(this.dlina && this.kod_svet_zames && this.kod_nakleyki){
                    if(this.sena_export){
                        return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' ' +this.kod_nakleyki,'accept':true}
                    }else{
                        return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' ' +this.kod_nakleyki,'accept':false}
                    }
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
    
                }else{
        
                    if(this.kod_svet_rezini && this.dlina && this.kod_svet_zames && this.kod_nakleyki){
                        if(this.sena_export){
                            return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' '+this.kod_svet_rezini +' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' '+this.kod_svet_rezini +' ' +this.kod_nakleyki,'accept':false}
                        }
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }break;
            case 2: if(this.is_iklyuch){
                if(this.dlina && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki && this.kod_svet_zames){
                    if(this.sena_export){
                        return {'text':this.artikul + ' '+this.kod_svet_zames + ' L' + this.dlina +' ' + this.kod_lam_sn+'/'+this.kod_lam_vn + ' '+this.kod_nakleyki,'accept':true}
                    }else{
                        return {'text':this.artikul + ' '+this.kod_svet_zames + ' L' + this.dlina +' ' + this.kod_lam_sn+'/'+this.kod_lam_vn + ' '+this.kod_nakleyki,'accept':false}
                    }
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
        
                    if(this.dlina && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki && this.kod_svet_rezini && this.kod_svet_zames){
                        if(this.sena_export){
                            return {'text':this.artikul + ' '+this.kod_svet_zames + ' L' + this.dlina +' ' + this.kod_lam_sn+'/'+this.kod_lam_vn + ' '+this.kod_svet_rezini +' '+this.kod_nakleyki,'accept':true} 
                        }else{
                            return {'text':this.artikul + ' '+this.kod_svet_zames + ' L' + this.dlina +' ' + this.kod_lam_sn+'/'+this.kod_lam_vn + ' '+this.kod_svet_rezini +' '+this.kod_nakleyki,'accept':false} 
                        }
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }break;
        }
       
    }
  }




function front_piece(start=1,end=6){
    text =""

    for (let i = start; i < end; i++) {
        text +=`
        <tr id='table_tr` +String(i)+`' style='padding-bottom:0!important;margin-bottom:0!important;'>                   
        <td class="sticky-col"   style='left:0; padding-right:5px; background-color:white!important;' >
                    <div class="btn-group" role="group" aria-label="Basic example">
                            <button type="button" class="btn btn-outline-secondary btn-sm" id='clear_btn`+String(i)+`' onclick="artukil_clear(`+String(i)+`)" data-bs-toggle='popover' title='Yangi sozdaniya qilish uchun ishlatiladi'><i class="bi bi-x-circle"></i></button>
                            <button type="button" class="btn btn-outline-secondary btn-sm"  onclick="copy_tr(`+String(i)+`)" data-bs-toggle='popover' title='Yangi sozdaniya qilish uchun ishlatiladi'><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-copy" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M4 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 5a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-1h1v1a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h1v1z"/></svg></button>
                    </div>
                    
                    

        </td>
        <td style='display:none;'>
            <div class="input-group input-group-sm mb-1" style='width:150px;'>
                <span class ='nazvaniye_system` +String(i)+`'style="text-transform: uppercase;font-size: 10px; font-weight:700;padding:5px;width:150px" ></span>
            </div>
        </td>
        <td style='display:none;' >
            <div class="input-group input-group-sm mb-1">
                <b><span id='camera` +String(i)+`'style="text-transform: uppercase; font-size:12px;padding-left:5px"></span></b>
            </div>
        </td>
        <td class="sticky-col" style=' left: 73.5px;background-color:white!important'  >
            <div class="input-group input-group-sm mb-1">
                <select class=" form-control basic_artikul" style="background-color:#ddebf7; width: 140px; font-size:10px " id="artikul`+String(i)+`" ></select>
            </div>
            <span style='display:none' id='artikul_pvc` +String(i)+`'></span>
            <span style='display:none' id='iskyucheniye` +String(i)+`'></span>
            <span style='display:none' id='is_special` +String(i)+`'></span>
            <span style='display:none' id='nakleyka_nt1` +String(i)+`'></span>
        </td>
        
        
        <td style='display:none;'>
            <div class="input-group input-group-sm mb-1">
                <b><span  id ='kod_komponent` +String(i)+`'style="text-transform: uppercase;font-size: 12px;padding-left:5px;"></span></b>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 177px;text-transform: uppercase; font-size:12px; padding-right:0px;height:27px!important;z-index:0" onchange="tip_pokritiya_selected(`+String(i)+`,this.value)" disabled id='tip_pokritiya`+String(i)+`' required>
                    <option  selected ></option>
                    <option value="1" >Неламинированный</option>
                    <option value="2" >Ламинированный</option>
                </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 70px;">
        
            <select class="form-select" aria-label="" style="width: 70px;height:27px!important;z-index:0"  disabled id='kod_svet_zames`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option  value="" selected ></option>
                <option value="F8" >F8</option>
                <option value="PE" >PE</option>
                <option value="EG1" >EG1</option>
                <option value="LE" >LE</option>
                <option value="BR1" >BR1</option>
                <option value="WT7" >WT7</option>
                <option value="BR10" >BR10</option>
                <option value="N2" >N2</option>
            </select>
            
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type="text"  class="form-control " style='width:50px;height:27px!important;z-index:0' onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled aria-describedby="inputGroup-sizing-sm" name ='length`+String(i)+`' id="length`+String(i)+`"  maxlength="4" >
            </div>
        </td>

        <td >
            <div class="input-group input-group-sm mb-1">    
            <select class="form-select" aria-label="" style="width: 220px; height:27px!important;z-index:0" onchange="svet_lamplonka_snaruji_selected(`+String(i)+`,this.value)" disabled id='svet_lamplonka_snaruji`+String(i)+`'>
                <option  value="" selected></option>
                <option value="0027">Золотой дуб IW</option>
                <option value="0300">Дуб мокко IW</option>
                <option value="0549">Красный Орех IW</option>
                <option value="0550">Орех IW</option>
                <option value="1004">Мет платин</option>
                <option value="1005">Мет серый кварц</option>
                <option value="1006">Мет серый антрацит</option>
                <option value="1012">Алюкс антрацит</option>
                <option value="1015">Алюкс алюмин</option>
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
                <option value="3058">Грец орех амаретто</option>
                <option value="3059">Орех терра</option>
                <option value="3062">Грецкий орех</option>
                <option value="3077">Винчестер</option>
                <option value="3081">Шеф дуб светлый</option>
                <option value="3083">Сантана</option>
                <option value="3086">ШЕФ ДУБ СЕРЫЙ</option>
                <option value="3091">Шеф дуб</option>
                <option value="3094">Орех Ребраун</option>
                <option value="4687">Кенсингтон серый</option>
                <option value="5053">Алтвейс</option>
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
                <option value="XXXX">XXXX</option>
                <option value="S513">Красный орех ADO</option>
                <option value="S540">Золотой дуб S540</option>
                <option value="1022">Ocean Blue</option>
                <option value="5F01">Шеф дуб сер 5F01</option>
                <option value="1027">GOLD BRUSH</option>
                <option value="ASA1128">ASA1128</option>
                <option value="ASA8028">ASA8028</option>
                <option value="ASA5003">ASA5003</option>
                <option value="6030">Матовый белый</option>
                <option value="6062">Матовый черный</option>
                <option value="2509">АНТРАЦИТ СЕРЫЙ LG</option>
                <option value="9252">Винчестер Renolit</option>
                <option value="1001">Метбраш Алюмин</option>
                <option value="5001">Кремвейс</option>
                <option value="6003">Маттекс антрацит</option>
                <option value="3007">Тропик дуб</option>
                <option value="9026">Маттекс темный сер</option>
                <option value="9036">Терновый орех</option>
            </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
                <div>
                    <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;padding-left:35%;z-index:0" id ='code_lamplonka_snaruji` +String(i)+`'></span>
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 220px;height:27px!important;z-index:0" onchange="svet_lamplonka_vnutri_selected(`+String(i)+`,this.value)" disabled id='svet_lamplonka_vnutri`+String(i)+`'>
                    <option  value="" selected></option>
                    <option value="0027">Золотой дуб IW</option>
                    <option value="0300">Дуб мокко IW</option>
                    <option value="0549">Красный Орех IW</option>
                    <option value="0550">Орех IW</option>
                    <option value="1004">Мет платин</option>
                    <option value="1005">Мет серый кварц</option>
                    <option value="1006">Мет серый антрацит</option>
                    <option value="1012">Алюкс антрацит</option>
                    <option value="1015">Алюкс алюмин</option>
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
                    <option value="3058">Грец орех амаретто</option>
                    <option value="3059">Орех терра</option>
                    <option value="3062">Грецкий орех</option>
                    <option value="3077">Винчестер</option>
                    <option value="3081">Шеф дуб светлый</option>
                    <option value="3083">Сантана</option>
                    <option value="3086">ШЕФ ДУБ СЕРЫЙ</option>
                    <option value="3091">Шеф дуб</option>
                    <option value="3094">Орех Ребраун</option>
                    <option value="4687">Кенсингтон серый</option>
                    <option value="5053">Алтвейс</option>
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
                    <option value="XXXX">XXXX</option>
                    <option value="S513">Красный орех ADO</option>
                    <option value="S540">Золотой дуб S540</option>
                    <option value="1022">Ocean Blue</option>
                    <option value="5F01">Шеф дуб сер 5F01</option>
                    <option value="1027">GOLD BRUSH</option>
                    <option value="ASA1128">ASA1128</option>
                    <option value="ASA8028">ASA8028</option>
                    <option value="ASA5003">ASA5003</option>
                    <option value="6030">Матовый белый</option>
                    <option value="6062">Матовый черный</option>
                    <option value="2509">АНТРАЦИТ СЕРЫЙ LG</option>
                    <option value="9252">Винчестер Renolit</option>
                    <option value="1001">Метбраш Алюмин</option>
                    <option value="5001">Кремвейс</option>
                    <option value="6003">Маттекс антрацит</option>
                    <option value="3007">Тропик дуб</option>
                    <option value="9026">Маттекс темный сер</option>
                    <option value="9036">Терновый орех</option>
                </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <div>
                    <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;padding-left:35%;z-index:0" id='code_lamplonka_vnutri`+String(i)+`'></span>
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 60px;">
            <select class="form-select" aria-label="" style="width: 50px;border-color:red;display:none;height:27px!important;z-index:0"   id='kod_svet_rezini`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option  value="" selected ></option>
                <option value="Чёрная резина" >BR</option>
                <option value="Серая резина" >GR</option>
                <option value="Без резины" >NR</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" id='svet_text`+String(i)+`'>
                
                    <span class =' text-center ' style="font-size:10px; font-weight: bold; text-transform: uppercase;z-index:0;white-space: nowrap;" id='svet_rezin`+String(i)+`'></span>
                
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" id="nakleyka`+String(i)+`">
            <div id='nakleyka_select`+String(i)+`' class='nak_select`+String(i)+`' style='display:none;'>
                <select class ='kod_nakleyki`+String(i)+`'  style='text-transform: uppercase; width: 70px;padding-left:35%;height:27px!important;z-index:0' onchange="create_kratkiy_tekst(`+String(i)+`)" data-placeholder="..."></select>
            </div>
            </div>
        </td>
         <td  style='width:100px'>
            <div class="input-group input-group-sm mb-1" style='width:100%'>
                
                    <span class ='text-center ' style="width:100px;font-size:12px;  text-transform: uppercase;padding:5px;z-index:0" id='nadpis_nakleyki`+String(i)+`'></span>
                
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <div>
                    <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;z-index:0" >PVCGP</span>
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <span  style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;z-index:0;white-space: nowrap;" id='kratkiy_tekst`+String(i)+`'></span>
            </div>
        </td>

        <td >
            <div class="input-group input-group-sm mb-1">
        
            <input type='text' class=" form-control " style=" width: 150px; font-size:10px;  height:27px!important;z-index:0" id='sap_code_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        
            </div>
        </td> 
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 250px; font-size:10px;  height:27px!important;z-index:0"  id='kratkiy_tekst_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 220px; font-size:10px; display:none; height:27px!important;z-index:0;border-color:red;"  id='sena_export`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 250px; font-size:10px; height:27px!important;z-index:0"  id='comment`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
            
        </td>
    `
    }
    return text
}

text = front_piece()

var table = $('#table-artikul')

table.append(text)

// function request_piece(start = 1, end = 6) {
//     // Fetch all necessary data in one request
//     $.ajax({
//         type: 'GET',
//         url: "/client/pvc-artikul-list",
//         dataType: 'json'
//     }).then(function (data) {
//         // Data is now an array of objects
//         var dataMap = {};
//         data.forEach(function (item) {
//             dataMap[item.id] = item;
//         });

//         for (let i = start; i <= end; i++) {
//             // Initialize Select2
//             $('#artikul' + i).select2({
//                 ajax: {
//                     url: "/client/pvc-artikul-list",
//                     dataType: 'json',
//                     processResults: function(data) {
//                         return {
//                             results: $.map(data, function(item) {
//                                 return { 
//                                     id: item.id,
//                                     text: item.artikul,
//                                     component: item.component2,
//                                     system: item.nazvaniye_sistem,
//                                     camera: item.camera,
//                                     kod_k_component: item.kod_k_component,
//                                     iskyucheniye: item.iskyucheniye,
//                                     is_special: item.is_special,
//                                     nakleyka_nt1: item.nakleyka_nt1
//                                 };
//                             })
//                         };
//                     }
//                 }
//             });

//             // Handle select2 select event
//             $('#artikul' + i).on('select2:select', function(e) {
//                 var selectedId = e.params.data.id;
//                 var item = dataMap[selectedId];

//                 if (item) {
//                     var nazvaniye_system = $('.nazvaniye_system' + i);
//                     var camera = $('#camera' + i);
//                     var kod_komponent = $('#kod_komponent' + i);
//                     var artikul_pvc = $('#artikul_pvc' + i);
//                     var iskyucheniye = $('#iskyucheniye' + i);
//                     var is_special = $('#is_special' + i);
//                     var nakleyka_nt1 = $('#nakleyka_nt1' + i);
//                     var nadpis_nakleyki = $('#nadpis_nakleyki' + i);
//                     var tip_pokritiya = $('#tip_pokritiya' + i);

//                     tip_pokritiya.attr("disabled", false);
//                     nazvaniye_system.text(item.system);
//                     artikul_pvc.text(item.component);
//                     iskyucheniye.text(item.iskyucheniye);
//                     camera.text(item.camera);
//                     kod_komponent.text(item.kod_k_component);
//                     is_special.text(item.is_special);

//                     var select_nak = $('.kod_nakleyki' + i);
//                     var hasOption_snar = select_nak.find('option').length > 0;

//                     if (item.nakleyka_nt1 === '1') {
//                         set_nakleyka(nakleyka_list, '.kod_nakleyki' + i, 'NT1', !hasOption_snar);
//                         nakleyka_nt1.text('1');
//                         nadpis_nakleyki.text('Без наклейки');
//                     } else {
//                         set_nakleyka(nakleyka_list, '.kod_nakleyki' + i, '', !hasOption_snar);
//                         nakleyka_nt1.text('');
//                         nadpis_nakleyki.text('');
//                     }

//                     var nakleyka_select = $('#nakleyka_select' + i);
//                     var length = $('#length' + i);
//                     length.attr('required', true);
//                     nakleyka_select.css('display', 'block');
//                     nakleyka_select.attr('required', true);

//                     if (data_base[i]) {
//                         clear_artikul(i);
//                     }
//                 }
//             });
//         }
//     });
// }

function request_piece(start=1,end=6){

    for (let i = start; i <= end; i++) {
        $('#artikul'+String(i)).select2({
            ajax: {
                url: "/client/pvc-artikul-list",
                dataType: 'json',
                processResults: function(data){
                    return {results: $.map(data, function(item){
                        return {id:item.id,text:item.artikul,component:item.component2,system:item.nazvaniye_sistem,camera:item.camera,kod_k_component:item.kod_k_component,iskyucheniye:item.iskyucheniye,is_special:item.is_special,nakleyka_nt1:item.nakleyka_nt1}
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
            var is_special = $('#is_special'+String(i));
            var nakleyka_nt1 = $('#nakleyka_nt1'+String(i));
            var nadpis_nakleyki = $('#nadpis_nakleyki'+String(i));
            tip_pokritiya.attr("disabled",false);
            nazvaniye_system.text(e.params.data.system);
            artikul_pvc.text(e.params.data.component);
            iskyucheniye.text(e.params.data.iskyucheniye);
            camera.text(e.params.data.camera)
            kod_komponent.text(e.params.data.kod_k_component)
            is_special.text(e.params.data.is_special)
            

            var select_nak = $('.kod_nakleyki'+String(i))
            var hasOption_snar = select_nak.find('option').length > 0;

            if(e.params.data.nakleyka_nt1 =='1'){
                if(hasOption_snar){
                    set_nakleyka(nakleyka_list,'.kod_nakleyki'+i,value='NT1',add=false)
                }else{
                    set_nakleyka(nakleyka_list,'.kod_nakleyki'+i,value='NT1',add=true)
                }
                nakleyka_nt1.text('1')

                nadpis_nakleyki.text('Без наклейки')
            }else{
                if(hasOption_snar){
                    set_nakleyka(nakleyka_list,'.kod_nakleyki'+i,value='',add=false)
                }else{
                    set_nakleyka(nakleyka_list,'.kod_nakleyki'+i,value='',add=true)
                }
                nakleyka_nt1.text('')
                nadpis_nakleyki.text('')
            }
        
            var nakleyka_select = $('#nakleyka_select'+String(i));

            var length = $('#length'+String(i));
            length.attr('required',true)
            nakleyka_select.css('display','block')
            nakleyka_select.attr('required',true)
           


            if(data_base[i]){
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
        
        var s = size+1

        var id = data.id;
        var nazvaniye_system = data.nazvaniye_system;
        var camera = data.camera
        var base_artikul = data.base_artikul;
        var kod_k_component = data.kod_k_component
        var tip_pokritiya = data.tip_pokritiya
        var kod_svet_zames = data.kod_svet_zames
        var dlina = data.dlina;
        var svet_lamplonka_snaruji = data.svet_lamplonka_snaruji;
        var kod_lam_sn = data.kod_lam_sn;
        var svet_lamplonka_vnutri = data.svet_lamplonka_vnutri;
        var kod_lam_vn = data.kod_lam_vn;
        var kod_svet_rezini = data.kod_svet_rezini
        var svet_rezin = data.svet_rezin
        var nadpis_nakleyki = data.nadpis_nakleyki;
        var kod_nakleyki = data.kod_nakleyki;
    

        var kratkiy_tekst = data.kratkiy_tekst;
        var sap_code_ruchnoy = data.sap_code;
        var kratkiy_text_ruchnoy = data.krat;
        var comment = data.comment;
        var sena_export = data.sena_export;
        var artikul = data.artikul;

       
        var is_iklyuch = data.is_iklyuch
        var is_special = data.is_special
        


        var iskyucheniye =$('#iskyucheniye'+id)
        if(is_iklyuch){
            iskyucheniye.text('1')
        }else{
            iskyucheniye.text('')

        }
        var is_special_text =$('#is_special'+id)
        if(is_special){
            is_special_text.text('1')
        }else{
            is_special_text.text('')
        }


        check_text_and_change_simple(artikul,'#artikul_pvc'+s)
        check_text_and_change_simple(nazvaniye_system,'.nazvaniye_system'+s)
        check_text_and_change_simple(camera,'#camera'+s)

        check_text_and_change_simple(kod_k_component,'#kod_komponent'+s)
    
        
        check_text_and_change(nazvaniye_system,'.nazvaniye_system'+s)
        check_input_and_change(id,'#tip_pokritiya'+s)


        
        if(id ==2){
            
            check_input_and_change(kod_lam_sn,'#svet_lamplonka_snaruji'+s,dis=false,is_req=true)
            check_text_and_change(kod_lam_sn,'#code_lamplonka_snaruji'+s,dis=false,is_req=true)

            check_input_and_change(kod_lam_vn,'#svet_lamplonka_vnutri'+s,dis=false,is_req=true)
            check_text_and_change(kod_lam_vn,'#code_lamplonka_vnutri'+s,dis=false,is_req=true)


        }

       
        check_input_and_change(dlina,'#length'+s,dis=false,is_req=true)
        
        $('#artikul'+ s).attr('disabled',false)
        check_for_valid_and_set_val_select(base_artikul,'artikul'+ s,is_req=true)
        check_input_and_change(kod_svet_zames,'#kod_svet_zames'+s,dis=false,is_req=true)
        // check_text_and_change(kod_svet_zames,'#kod_svet_zames'+s)

        if(!is_iklyuch){
            check_input_and_change(kod_svet_rezini,'#kod_svet_rezini'+s,dis=false,is_req=true)
            check_text_and_change(kod_svet_rezini,'#svet_rezin'+s)
        }

        var nakleyka_select = $('#nakleyka_select'+String(s));

       
        nakleyka_select.css('display','block')
        nakleyka_select.attr('required',true)
        set_nakleyka(nakleyka_list,'.kod_nakleyki'+s,value=kod_nakleyki)
        check_text_and_change(nadpis_nakleyki,'#nadpis_nakleyki'+s)
       

        

       
        check_text_and_change(kratkiy_tekst,'#kratkiy_tekst'+s)

        check_input_and_change(sap_code_ruchnoy,'#sap_code_ruchnoy'+s)
        check_input_and_change(kratkiy_text_ruchnoy,'#kratkiy_tekst_ruchnoy'+s)
        check_input_and_change(comment,'#comment'+s)
        check_input_and_change(sena_export,'#sena_export'+s,dis=false,is_req=true,is_req_simple=false)


       
        
        
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



function artukil_clear(id){
    $('#artikul'+id).val(null).trigger('change');
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


function clear_artikul(id){
    if(data_base[id]){

        var base_artikul =$('#select2-artikul'+id+'-container').text()
        var nazvaniye_system = $('.nazvaniye_system'+id).text()
        var camera = $('#camera'+String(id)).text();
        var kod_komponent = $('#kod_komponent'+String(id)).text();
        var artikul_pvc = $('#artikul_pvc'+String(id)).text();
        var iskyucheniye = $('#iskyucheniye'+String(id)).text();
        var is_special = $('#is_special'+String(id)).text();
        var kod_svet_rezini = $('#kod_svet_rezini'+id)
        var svet_lamplonka_vnutri = $('#svet_lamplonka_vnutri'+id)
        var svet_rezini = $('#svet_text'+String(id));
        
        if(iskyucheniye == '1'){
            svet_rezini.children('span').remove()
            kod_svet_rezini.val('')
            data_base[id].svet_rezin = NaN
            data_base[id].kod_svet_rezini = NaN
            var iklyuch =true
            kod_svet_rezini.css('display','none')
        }else{
            svet_rezini.append('<span class =" text-center " style="font-size:10px; font-weight: bold; text-transform: uppercase;" id="svet_rezin'+id+'"></span>')
            kod_svet_rezini.css('display','block')
            var iklyuch =false
            
        }

        if(is_special=='1'){
            var is_spec =true
            svet_lamplonka_vnutri.val('XXXX')
            
        }else{
            var is_spec =false
            svet_lamplonka_vnutri.val('')
            
        }

        data_base[id].base_artikul = base_artikul
        data_base[id].nazvaniye_system = nazvaniye_system
        data_base[id].camera = camera
        data_base[id].kod_k_component = kod_komponent
        data_base[id].artikul = artikul_pvc
        data_base[id].is_iklyuch = iklyuch
        data_base[id].is_special = is_spec

    }
   
   
    create_kratkiy_tekst(id) 
   
    
}

function tip_pokritiya_selected(id,val){

    var element33 = document.getElementById("table_tr"+id);
    element33.style.backgroundColor='white';
    

    var dlina =$('#length'+String(id));
    dlina.attr("disabled",false);
    dlina.css("border-color",'#fc2003');

    

    
   
    var kratkiy_tekst = $('#kratkiy_tekst'+String(id));
    var kod_nakleyki =$('.kod_nakleyki'+id)
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
    var nakleyka_nt1 = $('#nakleyka_nt1'+String(id));
    if(nakleyka_nt1.text()==''){
        set_nakleyka(nakleyka_list,'.kod_nakleyki'+id,value='',add=false)
        nadpis_nakleyki.text('')
    }else{
        set_nakleyka(nakleyka_list,'.kod_nakleyki'+id,value='NT1',add=false)
        nadpis_nakleyki.text('Без наклейки')
    }

    
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
        kod_nakleyki.css('border-color','red')
        
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
        kod_nakleyki.css('border-color','red')

        var kod_svet_rezini = $('#kod_svet_rezini'+String(id));
        kod_svet_rezini.val('')

        var svet_lamplonka_snaruji = $('#svet_lamplonka_snaruji'+String(id));
        svet_lamplonka_snaruji.attr("disabled",false);
        svet_lamplonka_snaruji.attr("required",true);
        svet_lamplonka_snaruji.css("border-color",'#fc2003');
        
        var is_special = $('#is_special'+String(id)).text();
        var svet_lamplonka_vnutri = $('#svet_lamplonka_vnutri'+String(id));
        var code_lamplonka_vnutri = $('#code_lamplonka_vnutri'+String(id));
        if(is_special =='1'){
            svet_lamplonka_vnutri.val('XXXX')
            code_lamplonka_vnutri.text('XXXX')

        }else{
            svet_lamplonka_vnutri.css("border-color",'#fc2003');
        }
        svet_lamplonka_vnutri.attr("disabled",false);
        svet_lamplonka_vnutri.attr("required",true);

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
        console.log(kod_komponent,'dddddddd')
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


var zapros_count =[]


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


    var value_nak = $('.kod_nakleyki'+String(id))
    var nadpis_nakleyki = $('#nadpis_nakleyki'+String(id));
    
    var value_nak_1 = $('.kod_nakleyki'+String(id) +' option:selected')
    var nadpiss_ = value_nak_1.attr('data-nadpis')
  
    if(value_nak.val() !=''){
        value_nak.css('border-color','#dedad9');
        data_base[id].kod_nakleyki = value_nak.val();
        data_base[id].nadpis_nakleyki = nadpiss_
        nadpis_nakleyki.text(nadpiss_)
        
    }else{
        nadpis_nakleyki.text('')
        value_nak.css('border-color','red');
        data_base[id].kod_nakleyki = NaN
        data_base[id].nadpis_nakleyki = NaN;
    }

    if(String(val) == '2'){

        
            
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

    if(data.text !='XXXXXXXX' ){
        var artikul_bass = data_base[id].base_artikul
        var art_krat_dict = artikul_bass + data.text

        if(zapros_count.indexOf(art_krat_dict) === -1){
            sap_codes = get_sapcode(id,data_base[id].base_artikul,data.text)
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
            var art_krat =artikul+kratkiy_tekst
            zapros_count.push(art_krat)

            data_base[id].sap_code=res.artikul
            data_base[id].krat=res.kratkiy_tekst
            var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
            var kratkiy_text_ruchnoy = $('#kratkiy_tekst_ruchnoy'+id)
            sap_code_ruchnoy.val(res.artikul)
            kratkiy_text_ruchnoy.val(res.kratkiy_tekst)
            sap_code_ruchnoy.css('background-color','orange')
            kratkiy_text_ruchnoy.css('background-color','orange')
        }else{
            var art_krat =artikul+kratkiy_tekst
            zapros_count.push(art_krat)
            data_base[id].sap_code=NaN
            data_base[id].krat=NaN
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

function add_column(){
        
    text =""
    var sizeee = $('#table-artikul tr').length;
    
    text = front_piece(start = sizeee+1, end = sizeee+2)

    
    var table = $('#table-artikul')
    table.append(text)
    
    

    request_piece(start = sizeee+1, end = sizeee+2)


}






