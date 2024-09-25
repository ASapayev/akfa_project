class BasePokritiya{
    constructor(
        full=false,//done
        id=NaN, //done
        nazvaniye_system=NaN,//done
        camera=NaN,//done
        base_artikul=NaN,//done
        kod_k_component=NaN,//done
        tip_pokritiya=NaN,//done
        nazvaniye_svet_zames=NaN,//done
        kod_svet_zames=NaN,//done
        dlina=NaN,//done
        svet_lamplonka_snaruji=NaN,//done
        kod_lam_sn=NaN,//done
        svet_lamplonka_vnutri=NaN,//done
        kod_lam_vn=NaN,//done
        svet_rezin=NaN,//done
        kod_svet_rezini=NaN,//done
        nadpis_nakleyki=NaN,
        kod_nakleyki=NaN,//done
        goods_group=NaN,//done
        tex_name=NaN,//done
        kratkiy_tekst=NaN,//done
        sap_code=NaN,//done
        krat=NaN,//done
        comment=NaN,//done
        sena=NaN,//done
        klaes_id=NaN,//done
        artikul=NaN,//done
        is_iklyuch=false,//done
        is_active=false,//done
        is_special = false

        ) {
      
        this.full=full;
        this.id=id;
        this.nazvaniye_system=nazvaniye_system;
        this.camera=camera;
        this.base_artikul=base_artikul;
        this.nazvaniye_svet_zames=nazvaniye_svet_zames;
        this.kod_k_component=kod_k_component;
        this.tip_pokritiya=tip_pokritiya;
        this.kod_svet_zames=kod_svet_zames;
        this.dlina=dlina;
        this.svet_lamplonka_snaruji=svet_lamplonka_snaruji;
        this.kod_lam_sn=kod_lam_sn;
        this.svet_lamplonka_vnutri=svet_lamplonka_vnutri;
        this.kod_lam_vn=kod_lam_vn;
        this.svet_rezin=svet_rezin;
        this.kod_svet_rezini=kod_svet_rezini;
        this.nadpis_nakleyki=nadpis_nakleyki;
        this.kod_nakleyki=kod_nakleyki;
        this.goods_group=goods_group;
        this.tex_name=tex_name;
        this.kratkiy_tekst=kratkiy_tekst;
        this.sap_code=sap_code;
        this.krat=krat;
        this.comment=comment;
        this.sena=sena;
        this.klaes_id=klaes_id;
        this.artikul=artikul;
        this.is_iklyuch=is_iklyuch;
        this.is_active=is_active;
        this.is_special=is_special;
    }
    get_kratkiy_tekst(){
        switch(this.id){
            case 1: if(this.is_iklyuch){
                if(this.dlina && this.kod_svet_zames && this.kod_nakleyki){
                    if(this.goods_group && this.sena && this.klaes_id){
                        return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' ' +this.kod_nakleyki,'accept':true} 
                    }else{
                        return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' ' +this.kod_nakleyki,'accept':false} 
    
                    }
        
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
    
                }else{
        
                    if(this.kod_svet_rezini && this.dlina && this.kod_svet_zames && this.kod_nakleyki){
                        if(this.goods_group && this.sena && this.klaes_id){
                            return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' '+this.kod_svet_rezini +' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' '+this.kod_svet_rezini +' ' +this.kod_nakleyki,'accept':false}
        
                        }
            
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }break;
            case 2:if(this.is_iklyuch){
            
                console.log(this.dlina , this.kod_lam_vn , this.kod_lam_sn , this.kod_nakleyki , this.kod_svet_zames,this.kod_svet_rezini,'isklyuch')
                if(this.dlina && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki && this.kod_svet_zames){
                    console.log(this.dlina , this.kod_lam_vn , this.kod_lam_sn , this.kod_nakleyki , this.kod_svet_zames,this.kod_svet_rezini,'isklyuch1')
                    if(this.goods_group && this.sena && this.klaes_id){
                        console.log(this.dlina , this.kod_lam_vn , this.kod_lam_sn , this.kod_nakleyki , this.kod_svet_zames,this.kod_svet_rezini,'isklyuch2')
                        return {'text':this.artikul + ' '+this.kod_svet_zames + ' L' + this.dlina +' ' + this.kod_lam_sn+'/'+this.kod_lam_vn + ' '+this.kod_nakleyki,'accept':true} 
                    }else{
                        console.log(this.dlina , this.kod_lam_vn , this.kod_lam_sn , this.kod_nakleyki , this.kod_svet_zames,this.kod_svet_rezini,'isklyuch3')
                        return {'text':this.artikul + ' '+this.kod_svet_zames + ' L' + this.dlina +' ' + this.kod_lam_sn+'/'+this.kod_lam_vn + ' '+this.kod_nakleyki,'accept':false} 
                    }
        
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
                    console.log(this.dlina , this.kod_lam_vn , this.kod_lam_sn , this.kod_nakleyki , this.kod_svet_zames,this.kod_svet_rezini,'000000')
                    if(this.dlina && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki && this.kod_svet_rezini && this.kod_svet_zames){
                        console.log(this.dlina , this.kod_lam_vn , this.kod_lam_sn , this.kod_nakleyki , this.kod_svet_zames,this.kod_svet_rezini,'ee1')
                        if(this.goods_group && this.sena && this.klaes_id){
                            console.log(this.dlina , this.kod_lam_vn , this.kod_lam_sn , this.kod_nakleyki , this.kod_svet_zames,this.kod_svet_rezini,'ffsdfs33333sfffff')
                            return {'text':this.artikul + ' '+this.kod_svet_zames + ' L' + this.dlina +' ' + this.kod_lam_sn+'/'+this.kod_lam_vn + ' '+this.kod_svet_rezini +' '+this.kod_nakleyki,'accept':true} 
                        }else{
                            console.log(this.dlina , this.kod_lam_vn , this.kod_lam_sn , this.kod_nakleyki , this.kod_svet_zames,this.kod_svet_rezini,'77777777')
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
    var text =""

    for (let i = start; i < end; i++) {
        var buttons =''
        if(status_proccess == 'new'){
            buttons=`<td class="sticky-col"   style='left:0; padding-right:5px; background-color:white!important;' >
                    <div class="btn-group" role="group" aria-label="Basic example">
                            <button type="button" class="btn btn-outline-secondary btn-sm" id='clear_btn`+String(i)+`' onclick="artukil_clear(`+String(i)+`)" data-bs-toggle='popover' title='Tozalab tashlash'><i class="bi bi-x-circle"></i></button>
                            <button type="button" class="btn btn-outline-secondary btn-sm"  onclick="copy_tr(`+String(i)+`)" data-bs-toggle='popover' title='Dubl qilish'><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-copy" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M4 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 5a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-1h1v1a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h1v1z"/></svg></button>
                    </div>
                    
                    

                        </td>
                        <td style='display:none;' >
                            <div class="input-group input-group-sm mb-1" style='width:150px;'>
                                <span id ='nazvaniye_system` +String(i)+`'style="font-size: 10px; font-weight:700;padding:5px;width:150px" ></span>
                            </div>
                        </td>
                        <td style='display:none;' >
                            <div class="input-group input-group-sm mb-1">
                                <b><span id='camera` +String(i)+`'style=" font-size:12px;padding-left:5px"></span></b>
                            </div>
                        </td>
                        <td class="sticky-col" style=' left: 73.5px;background-color:white!important' >
                            <div class="input-group input-group-sm mb-1">
                                <select class=" form-control basic_artikul" style="background-color:#ddebf7; width: 140px; font-size:10px " id="artikul`+String(i)+`" ></select>
                            </div>
                            <span style='display:none' id='artikul_pvc` +String(i)+`'></span>
                            <span style='display:none' id='iskyucheniye` +String(i)+`'></span>
                            <span style='display:none' id='is_special` +String(i)+`'></span>
                            <span style='display:none' id='nakleyka_nt1` +String(i)+`'></span>
                        </td>`
        }else{
            buttons=`
                        <td style='display:none;' >
                            <div class="input-group input-group-sm mb-1" style='width:150px;'>
                                <span id ='nazvaniye_system` +String(i)+`'style="font-size: 10px; font-weight:700;padding:5px;width:150px" ></span>
                            </div>
                        </td>
                        <td style='display:none;' >
                            <div class="input-group input-group-sm mb-1">
                                <b><span id='camera` +String(i)+`'style=" font-size:12px;padding-left:5px"></span></b>
                            </div>
                        </td>
                        <td class="sticky-col" style=' left:0;background-color:white!important' >
                            <div class="input-group input-group-sm mb-1">
                                <select class=" form-control basic_artikul" style="background-color:#ddebf7; width: 140px; font-size:10px " id="artikul`+String(i)+`" ></select>
                            </div>
                            <span style='display:none' id='artikul_pvc` +String(i)+`'></span>
                            <span style='display:none' id='iskyucheniye` +String(i)+`'></span>
                            <span style='display:none' id='is_special` +String(i)+`'></span>
                            <span style='display:none' id='nakleyka_nt1` +String(i)+`'></span>
                        </td>`
        }
        text +=`
        <tr id='table_tr` +String(i)+`' style='padding-bottom:0!important;margin-bottom:0!important;'>                   
        
        `+buttons+
         `
        
        <td style='display:none;'>
            <div class="input-group input-group-sm mb-1">
                <b><span  id ='kod_komponent` +String(i)+`'style="font-size: 12px;padding-left:5px;height:27px!important;z-index:0;"></span></b>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 177px; font-size:12px; padding-right:0px;height:27px!important;z-index:0" onchange="tip_pokritiya_selected(`+String(i)+`,this.value)" disabled id='tip_pokritiya`+String(i)+`' required>
                    <option  selected value='' ></option>
                    <option value="1" >Неламинированный</option>
                    <option value="2" >Ламинированный</option>
                </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 190px;">
        
            <select class="form-select" aria-label="" style="width: 190px;height:27px!important;z-index:0"  disabled id='nazvaniye_svet_zames`+String(i)+`' onchange="nazvaniye_svet_zames_selected(`+String(i)+`,this.value)">
                <option  value="" selected ></option>
                <option value="F8" >Белый стандарт</option>
                <option value="PE" >Подоконник</option>
                <option value="EG1" >Белый ENGELBERG</option>
                <option value="LE" >Ламбри</option>
                <option value="BR1" >Тёмный коричневый</option>
                <option value="WT7" >Серый</option>
                <option value="BR10" >Светлый коричневый</option>
                <option value="N2" >Белый 6000 ECO</option>
            </select>
            
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <b><span  id ='kod_svet_zames` +String(i)+`'style="font-size: 12px;padding-left:5px;z-index:0"></span></b>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type="number"   class="form-control " style='width:70px;height:27px!important;z-index:0' oninput="create_kratkiy_tekst(`+String(i)+`); limitLength(this, 4);"  disabled aria-describedby="inputGroup-sizing-sm" name ='length`+String(i)+`' id="length`+String(i)+`"  >
            </div>
        </td>

        <td >
            <div class="input-group input-group-sm mb-1">    
            <select class="form-select " aria-label="" style="width: 220px;height:27px!important;z-index:0" onchange="svet_lamplonka_snaruji_selected(`+String(i)+`,this.value)" disabled id='svet_lamplonka_snaruji`+String(i)+`'>
                <option  value="" selected></option>
                <option value="0027">Золотой дуб IW</option>
                <option value="0300">Дуб мокко IW</option>
                <option value="0549">Красный Орех IW</option>
                <option value="0550">Орех IW</option>
                <option value="1004">Мет платин</option>
                <option value="1005">Мет серый кварц</option>
                <option value="1006">Мет серый антрацит</option>
                <option value="1012">Алюкс антрацит</option>
                <option value="1015">Алюкс белый алюмин</option>
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
                    <span class =' text-center ' style="font-size: small; font-weight: bold; padding-left:35%;z-index:0" id ='code_lamplonka_snaruji` +String(i)+`'></span>
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
                <option value="1015">Алюкс белый алюмин</option>
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
                    <span class =' text-center ' style="font-size: small; font-weight: bold; padding-left:35%;z-index:0" id='code_lamplonka_vnutri`+String(i)+`'></span>
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 150px;">
            <select class="form-select" aria-label="" style="width: 150px;border-color:red;display:none;height:27px!important;z-index:0"   id='kod_svet_rezini`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option  value="" selected disabled></option>
                <option value="BR" >Чёрная резина</option>
                <option value="GR" >Серая резина</option>
                <option value="NR" >Без резины</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1"  id='svet_text`+String(i)+`'>
                
                    <span class =' text-center ' style="font-size:12px; font-weight: 700;  padding:5px;z-index:0;white-space: nowrap;" id='svet_rezin`+String(i)+`'></span>
                
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" id="nakleyka`+String(i)+`">
            <div id='nakleyka_select`+String(i)+`' class='nak_select`+String(i)+`' style='display:none;'>
                <select class ='kod_nakleyki`+String(i)+`'  style=' width: 145px;padding-left:35%;height:27px!important;z-index:0' onchange="create_kratkiy_tekst(`+String(i)+`)" data-placeholder="..."></select>
            </div>
            </div>
        </td>
        <td  style='width:100px'>
            <div class="input-group input-group-sm mb-1" style='width:100%'>
                
                    <span class ='text-center ' style="width:100px;font-size:12px;  padding:5px;z-index:0" id='nadpis_nakleyki`+String(i)+`'></span>
                
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 150px;border-color:red;display:none;height:27px!important;z-index:0"   id='goods_group`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option  value="" selected ></option>
                <option value="QLIK_PVC_PROF" >ПВХ профиль</option>
                <option value="QLIK_PDF" >Подоконник</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <span class =' text-center ' style="font-size: small; font-weight: bold; z-index:0" id='tex_name`+String(i)+`'></span>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <span  style="font-size: small; width:250px; font-weight: bold; z-index:0;white-space: nowrap;" id='kratkiy_tekst`+String(i)+`'></span>
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
            <input type='text' class=" form-control " style="width: 250px; font-size:10px; height:27px!important;z-index:0"  id='comment`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
            
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 220px; font-size:10px; display:none; height:27px!important;z-index:0; border-color:red"  id='sena`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 220px; font-size:10px; display:none; height:27px!important;z-index:0; border-color:red"  id='klaes_id`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
    `
    }
    return text
}

text = front_piece()


var table = $('#table-artikul')

// table.append(text)


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
        
        
        if(status_proccess == 'new'){
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
                var nazvaniye_system =$('#nazvaniye_system'+String(i));
                var camera = $('#camera'+String(i));
                var kod_komponent = $('#kod_komponent'+String(i));
                var artikul_pvc = $('#artikul_pvc'+String(i));
                var iskyucheniye = $('#iskyucheniye'+String(i));
                var tip_pokritiya = $('#tip_pokritiya'+String(i));
                var is_special = $('#is_special'+String(i));
                var nakleyka_nt1 = $('#nakleyka_nt1'+String(i));
                var nadpis_nakleyki = $('#nadpis_nakleyki'+String(i));
                tip_pokritiya.attr("disabled",false);
                is_special.text(e.params.data.is_special);
                nazvaniye_system.text(e.params.data.system);
                artikul_pvc.text(e.params.data.component);
                iskyucheniye.text(e.params.data.iskyucheniye);
                camera.text(e.params.data.camera)
                kod_komponent.text(e.params.data.kod_k_component)
                
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
}
data_base = {}

if(status_proccess == 'new'){
    table.append(text)
    request_piece()

}else{
    var jsonData = JSON.parse(jsonData);
    // var jsonData ='{{order}}'

    var ii= 1

    for(var key1 in jsonData){
        data_base[ii] = new BasePokritiya()
        for(var key2 in jsonData[key1]){
            data_base[ii][key2] = jsonData[key1][key2]
        }
        ii += 1
    }



    const lengthOfObject = Object.keys(jsonData).length;

    var text = front_piece(1,lengthOfObject+1)



    var table = $('#table-artikul')

    table.append(text)

    var i = 1
    for(key2 in data_base){
        copy_tr(key2,i)
        i += 1
    }
}





// request_piece()



function copy_tr(id,ii=1){
    if(!data_base[id]){
        console.log('salom2222 copy')
    }else{
        if(status_proccess == 'new'){
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
        }else{
            var data = data_base[id]
            var s = ii
            request_piece(start = s, end = s+1)
        }

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
        var goods_group = data.goods_group;
        var tex_name = data.tex_name;

        var kratkiy_tekst = data.kratkiy_tekst;
        var sap_code_ruchnoy = data.sap_code;
        var kratkiy_text_ruchnoy = data.krat;
        var comment = data.comment;
        var sena = data.sena;
        var klaes_id = data.klaes_id;
        var artikul = data.artikul;

       
        var is_iklyuch = data.is_iklyuch
        var is_special = data.is_special
        var is_active = data.is_active


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
        check_input_and_change(kod_svet_zames,'#nazvaniye_svet_zames'+s,dis=false,is_req=true)
        check_text_and_change(kod_svet_zames,'#kod_svet_zames'+s)

        if(!is_iklyuch){
            check_input_and_change(kod_svet_rezini,'#kod_svet_rezini'+s,dis=false,is_req=true)
            check_text_and_change(kod_svet_rezini,'#svet_rezin'+s)
        }

        var nakleyka_select = $('#nakleyka_select'+String(s));

       
        nakleyka_select.css('display','block')
        nakleyka_select.attr('required',true)
        set_nakleyka(nakleyka_list,'.kod_nakleyki'+s,value=kod_nakleyki)
        check_text_and_change(nadpis_nakleyki,'#nadpis_nakleyki'+s)

        // get_nakleyka(String(s))

        check_input_and_change(tex_name,'#goods_group'+s,dis=false,is_req=true,is_req_simple=false)
        check_text_and_change(tex_name,'#tex_name'+s)

       
        check_text_and_change(kratkiy_tekst,'#kratkiy_tekst'+s)

        check_input_and_change(sap_code_ruchnoy,'#sap_code_ruchnoy'+s,dis=true)
        check_input_and_change(kratkiy_text_ruchnoy,'#kratkiy_tekst_ruchnoy'+s,dis=true)
        check_input_and_change(comment,'#comment'+s)
        check_input_and_change(sena,'#sena'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(klaes_id,'#klaes_id'+s,dis=false,is_req=true,is_req_simple=false)
        


       
        // check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s)

      
        
        
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

        var base_artikul =$('#select2-artikul'+id+'-container').text()
        var nazvaniye_system = $('.nazvaniye_system'+id).text()
        var camera = $('#camera'+String(id)).text();
        var kod_komponent = $('#kod_komponent'+String(id)).text();
        var artikul_pvc = $('#artikul_pvc'+String(id)).text();
        var iskyucheniye = $('#iskyucheniye'+String(id)).text();
        var is_special = $('#is_special'+String(id)).text();
        var kod_svet_rezini = $('#kod_svet_rezini'+id)
        var svet_lamplonka_vnutri = $('#svet_lamplonka_vnutri'+id)
        var code_lamplonka_vnutri = $('#code_lamplonka_vnutri'+id)
        var svet_rezini = $('#svet_text'+String(id));
        
        if(iskyucheniye == '1'){
            svet_rezini.children('span').remove()
            kod_svet_rezini.val('')
            data_base[id].svet_rezin = NaN
            data_base[id].kod_svet_rezini = NaN
            var iklyuch =true
            kod_svet_rezini.css('display','none')
        }else{
            svet_rezini.append('<span class =" text-center " style="font-size:10px; font-weight: bold; " id="svet_rezin'+id+'"></span>')
            kod_svet_rezini.css('display','block')
            var iklyuch =false
            
        }

        if(is_special=='1'){
            var is_spec =true
            if(data_base[id].id == 2){
                svet_lamplonka_vnutri.val('XXXX')
                code_lamplonka_vnutri.text('XXXX')
            }
            
        }else{
            var is_spec =false
            svet_lamplonka_vnutri.val('')
            if(data_base[id].id == 2){
                svet_lamplonka_vnutri.css('border-color','red')
            }
            code_lamplonka_vnutri.text('')
            
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

function artukil_clear(id){
    $('#artikul'+id).val(null).trigger('change');
    var table_tr =$('#table_tr'+id);
    $('#nazvaniye_system'+id).text('');
    var tip_pokritiya = $('#tip_pokritiya'+String(id));
    tip_pokritiya.val('').change();
    tip_pokritiya.attr("disabled",true);

    var camera = $('#camera'+String(id));
    var kod_komponent = $('#kod_komponent'+String(id));
    var nazvaniye_svet_zames = $('#nazvaniye_svet_zames'+String(id));
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
    kod_svet_zames.text('')
    kod_svet_zames.attr('disabled',true)
    kod_svet_zames.css('border-color','#dedad9')
    
    nazvaniye_svet_zames.val('')
    nazvaniye_svet_zames.attr('disabled',true)
    nazvaniye_svet_zames.css('border-color','#dedad9')
    kod_svet_rezini.val('')
    kod_svet_rezini.css('display','none')
       
    // var select_nakleyka = $('#nakleyka'+String(id));
    // select_nakleyka.children("span").remove();
    // select_nakleyka.children("select").remove();
    delete data_base[id]

    var kratkiy_tekst = document.getElementById('kratkiy_tekst'+String(id));
    kratkiy_tekst.innerText="";

    
    
    table_tr.css('background-color','white')
    




    
    var sena =$('#sena'+String(id));
    sena.val('');
    sena.css('display','none');
    var klaes_id =$('#klaes_id'+String(id));
    klaes_id.val('');
    klaes_id.css('display','none');

    var sap_code_ruchnoy =$('#sap_code_ruchnoy'+String(id));
    sap_code_ruchnoy.val('');
    // sap_code_ruchnoy.css('display','none');
    var kratkiy_tekst_ruchnoy =$('#kratkiy_tekst_ruchnoy'+String(id));
    kratkiy_tekst_ruchnoy.val('');
    // kratkiy_tekst_ruchnoy.css('display','none');
    var comment =$('#comment'+String(id));
    comment.val('');
    // comment.css('display','none');
    var goods_group =$('#goods_group'+String(id));
    goods_group.val('');
    goods_group.css('display','none');
    var tex_name =$('#tex_name'+String(id));
    tex_name.text('');
    tex_name.css('display','none');


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

   
   
   
}

function tip_pokritiya_selected(id,val){

    var element33 = document.getElementById("table_tr"+id);
    element33.style.backgroundColor='white';
    

    var dlina =$('#length'+String(id));
    dlina.attr("disabled",false);
    dlina.css("border-color",'#fc2003');

    var sap_code_ruchnoy =$('#sap_code_ruchnoy'+String(id));
    sap_code_ruchnoy.css('display','block');
    sap_code_ruchnoy.val('');
    var kratkiy_tekst_ruchnoy =$('#kratkiy_tekst_ruchnoy'+String(id));
    kratkiy_tekst_ruchnoy.css('display','block');
    kratkiy_tekst_ruchnoy.val('');
    var comment =$('#comment'+String(id));
    comment.css('display','block');;
    comment.val('');
    var sena =$('#sena'+String(id));
    sena.css('display','block');;
    sena.val('');
    var klaes_id =$('#klaes_id'+String(id));
    klaes_id.css('display','block');;
    klaes_id.val('');

    
   
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

    

    // get_nakleyka(id)

    
    var iskyucheniye =$('#iskyucheniye'+id).text()
    
    if(String(val) == '1'){
        var goods_group = $('#goods_group'+String(id));
        goods_group.val('')
        goods_group.css('display','block');
        var tex_name = $('#tex_name'+String(id));
        tex_name.val('')
        tex_name.css('display','block');

        var nazvaniye_svet_zames = $('#nazvaniye_svet_zames'+String(id));
        nazvaniye_svet_zames.attr("disabled",false);
        nazvaniye_svet_zames.css("border-color",'#fc2003');
        data_base[id] = new BasePokritiya()
        data_base[id].id = 1;
        data_base[id].tip_pokritiya = 'Неламинированный';
        var artikul_pvc = $('#artikul_pvc'+String(id));
        data_base[id].artikul= artikul_pvc.text()

        var svet_lamplonka_vnutri = $('#svet_lamplonka_vnutri'+String(id));
        svet_lamplonka_vnutri.css('border-color','#dedad9')
        var svet_lamplonka_snaruji = $('#svet_lamplonka_snaruji'+String(id));
        svet_lamplonka_snaruji.css('border-color','#dedad9')

        var kod_svet_rezini = $('#kod_svet_rezini'+String(id));
        kod_svet_rezini.val('')
        kod_svet_rezini.css('display','block');
        var goods_group = $('#goods_group'+String(id));
        goods_group.val('')
        goods_group.css('display','block');

        // const spanss =document.querySelector('.nak_select' +id+ ' .select2-container .select2-selection--single')
        // spanss.style.borderColor='red';
        kod_nakleyki.css('border-color','red')

        
        if(iskyucheniye =='1'){
            data_base[id].is_iklyuch=true
            kod_svet_rezini.css('display','none')
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

        
        var goods_group = $('#goods_group'+String(id));
        goods_group.val('')
        goods_group.css('display','block');
        var tex_name = $('#tex_name'+String(id));
        tex_name.val('')
        tex_name.css('display','block');

        var nazvaniye_svet_zames = $('#nazvaniye_svet_zames'+String(id));
        nazvaniye_svet_zames.attr("disabled",false);
        nazvaniye_svet_zames.css("border-color",'#fc2003');
        // const spanss =document.querySelector('.nak_select' +id+ ' .select2-container .select2-selection--single')
        // spanss.style.borderColor='red';
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
        // svet_lamplonka_vnutri.css("border-color",'#fc2003');

        if(iskyucheniye =='1'){
            data_base[id].is_iklyuch=true
            kod_svet_rezini.css('display','none')
        }else{
            data_base[id].is_iklyuch=false
            kod_svet_rezini.css('display','block');
        }
    }

    if(String(val) != ''){
        var base_artikul =$('#select2-artikul'+id+'-container')
        data_base[id].base_artikul = base_artikul.text()
        var nazvaniye_system = $('#nazvaniye_system'+id).text()
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

function nazvaniye_svet_zames_selected(id,val){
    var kod_svet_zames = $('#kod_svet_zames'+String(id));
    kod_svet_zames.text(String(val));
    create_kratkiy_tekst(id);
}

var zapros_count ={}



function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
    
    var kratkiy_tekst = $('#kratkiy_tekst'+String(id));
    var combination= $('#combination'+String(id));
    combination_text = combination.text();
    var val = $('#tip_pokritiya'+String(id)).val();
    var dlina = $('#length'+String(id));
    var sena = $('#sena'+String(id));
    var klaes_id = $('#klaes_id'+String(id));
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
    if(dlina.val()!=''&& dlina.val()!=0 && dlina.val()!='0'){
        dlina.css("border-color",'#dedad9');
        data_base[id].dlina = dlina.val();
    }else{
        dlina.css("border-color",'red');
        data_base[id].dlina = NaN;
    }
    if(sena.val()!=''){
        sena.css("border-color",'#dedad9');
        data_base[id].sena = sena.val();
    }else{
        sena.css("border-color",'red');
        data_base[id].sena = NaN;
    }
    if(klaes_id.val()!=''){
        klaes_id.css("border-color",'#dedad9');
        data_base[id].klaes_id = klaes_id.val();
    }else{
        klaes_id.css("border-color",'red');
        data_base[id].klaes_id = NaN;
    }
    
    var nazvaniye_svet_zames = $('#nazvaniye_svet_zames'+String(id));
    if(nazvaniye_svet_zames){
        if(nazvaniye_svet_zames.val()!='0' && nazvaniye_svet_zames.val()!='' && nazvaniye_svet_zames.val()!=null){
            var nazvaniye_svet_zames1 = $('#nazvaniye_svet_zames' +id +' option:selected').text()
            nazvaniye_svet_zames.css("border-color",'#dedad9');
            data_base[id].kod_svet_zames = nazvaniye_svet_zames.val()
            data_base[id].nazvaniye_svet_zames = nazvaniye_svet_zames1
        }else{
            data_base[id].nazvaniye_svet_zames = NaN
            data_base[id].kod_svet_zames = NaN;
            nazvaniye_svet_zames.css("border-color",'red');
        }
    }
    var goods_group = $('#goods_group'+String(id));
    if(goods_group.val()!='0' && goods_group.val()!='' && goods_group.val()!=null){
        goods_group.css("border-color",'#dedad9');
        var goods_group1 = $('#goods_group'+String(id)+' option:selected').text();
        var tex_name = $('#tex_name'+String(id));
        tex_name.text(goods_group.val())
        data_base[id].tex_name = goods_group.val()
        data_base[id].goods_group = goods_group1
    }else{
        data_base[id].tex_name = NaN;
        data_base[id].goods_group = NaN;
        var tex_name = $('#tex_name'+String(id));
        tex_name.text('')
        goods_group.css("border-color",'red');
    }
    
    
    
    var iskyucheniye =$('#iskyucheniye' +id).text()

    if(iskyucheniye =='1'){

        var kod_svet_rezini =$('#kod_svet_rezini' + id);
        if(kod_svet_rezini.val()!=''&&kod_svet_rezini.val()){
            var svet_rezin =$('#svet_rezin' + id);
            var selectedText = $("#kod_svet_rezini"+id + " option:selected");
            svet_rezin.text(kod_svet_rezini.val())
            kod_svet_rezini.css('border-color','#dedad9')
            
            console.log(kod_svet_rezini.val(),'iskyucheniye')
            data_base[id].kod_svet_rezini =kod_svet_rezini.val();
            data_base[id].svet_rezin =selectedText;
        }else{
            var svet_rezin =$('#svet_rezin' + id);
            svet_rezin.text('')
            data_base[id].svet_rezin = NaN;
            data_base[id].kod_svet_rezini = NaN
        }
        
    }else{
        
        var kod_svet_rezini =$('#kod_svet_rezini' + id);
        if(kod_svet_rezini.val()!=''&&kod_svet_rezini.val()){
            var svet_rezin =$('#svet_rezin' + id);
            var selectedText = $("#kod_svet_rezini"+id + " option:selected").text();
            svet_rezin.text(kod_svet_rezini.val())
            kod_svet_rezini.css('border-color','#dedad9')
            console.log(kod_svet_rezini.val(),selectedText,'rezzz')
            data_base[id].kod_svet_rezini =kod_svet_rezini.val();
            data_base[id].svet_rezin = selectedText;
        }else{
            var svet_rezin =$('#svet_rezin' + id);
            data_base[id].svet_rezin = NaN;
            svet_rezin.text('')
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
        data_base[id].full=true
        data_base[id].kratkiy_tekst = data.text
    }else{
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','white')
        data_base[id].kratkiy_tekst=NaN
        data_base[id].full=false

    }
    
    if(data.text !='XXXXXXXX' ){
        var artikul_bass = data_base[id].base_artikul
        var art_krat_dict = artikul_bass + data.text
        var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
        var kratkiy_text_ruchnoy = $('#kratkiy_tekst_ruchnoy'+id)
        

        // console.log(zapros_count,art_krat_dict,'+++++')
        if(art_krat_dict in zapros_count){
            if(zapros_count[art_krat_dict]){
                var sap_code = zapros_count[art_krat_dict]
                sap_code_ruchnoy.val(sap_code)
                kratkiy_text_ruchnoy.val(data.text)
                sap_code_ruchnoy.css('background-color','#eaecef')
                kratkiy_text_ruchnoy.css('background-color','#eaecef')
                sap_code_ruchnoy.attr('disabled',true)
                kratkiy_text_ruchnoy.attr('disabled',true)
            }else{
                
                sap_code_ruchnoy.val('')
                kratkiy_text_ruchnoy.val('')
                sap_code_ruchnoy.css('background-color','white')
                kratkiy_text_ruchnoy.css('background-color','white')
                sap_code_ruchnoy.attr('disabled',false)
                kratkiy_text_ruchnoy.attr('disabled',false)
            }
            
        }else{
            sap_codes = get_sapcode(id,data_base[id].base_artikul,data.text)
        }
        // else{
        //     var krat = zapros_count[art_krat_dict]
        //     var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
        //     var kratkiy_text_ruchnoy = $('#kratkiy_tekst_ruchnoy'+id)
            

        //     sap_code_ruchnoy.val(artikul_bass)
        //     kratkiy_text_ruchnoy.val(krat)
        //     sap_code_ruchnoy.css('background-color','#eaecef')
        //     kratkiy_text_ruchnoy.css('background-color','#eaecef')
        //     sap_code_ruchnoy.attr('disabled',true)
        //     kratkiy_text_ruchnoy.attr('disabled',true)
        // }
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
            zapros_count[art_krat]=res.artikul

            data_base[id].sap_code=res.artikul
            data_base[id].krat=res.kratkiy_tekst

            var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
            var kratkiy_text_ruchnoy = $('#kratkiy_tekst_ruchnoy'+id)
            sap_code_ruchnoy.val(res.artikul)
            kratkiy_text_ruchnoy.val(res.kratkiy_tekst)
            sap_code_ruchnoy.css('background-color','#eaecef')
            kratkiy_text_ruchnoy.css('background-color','#eaecef')
        }else{
            var art_krat =artikul+kratkiy_tekst
            zapros_count[art_krat]=NaN
            data_base[id].sap_code=NaN
            data_base[id].krat=NaN
            var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
            var kratkiy_text_ruchnoy = $('#kratkiy_tekst_ruchnoy'+id)
            sap_code_ruchnoy.val('')
            kratkiy_text_ruchnoy.val('')
            sap_code_ruchnoy.css('background-color','#eaecef')
            kratkiy_text_ruchnoy.css('background-color','#eaecef')
            console.log('aa')
        }
        // WON'T REDIRECT
    });
}







