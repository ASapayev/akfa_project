class BasePokritiya{
    constructor(
        id = NaN,//done 
        full = false,//done
        nazvaniye_system = NaN,//done
        camera = NaN,//done
        
        base_artikul = NaN,//done
        kod_k_component = NaN,//done
        tip_pokritiya = NaN,//done
        kod_svet_zames = NaN,//done
        dlina = NaN,//done
        svet_lamplonka_snaruji = NaN,//done
        kod_lam_sn = NaN,//done
        svet_lamplonka_vnutri = NaN,//done
        kod_lam_vn = NaN,//done
       
        kod_svet_rezini = NaN,//done
        svet_rezin = NaN,//done
        kod_nakleyki = NaN,//done
        
        nadpis_nakleyki = NaN,//done
        gruppa_materialov = NaN,//done
        kratkiy_tekst = NaN,//done
        
        sap_code = NaN,//done
        krat = NaN,//done
        comment = NaN,//done
        pickupdate = NaN,//done
        sena_c_nds = NaN,//done
        sena_bez_nds = NaN,//done
        online_id = NaN,//done
        nazvaniye_ruchnoy = NaN,//done
        svet_product=NaN,//done
        group_zakup=NaN,//done
        group=NaN,//done
        tip=NaN,//done
        segment = NaN,//done
        buxgalter_tovar = NaN,//done
        buxgalter_uchot = NaN,//done
        bazoviy_edin = NaN,//done
        alter_edin = NaN,//done
        stoimost_baza = NaN,//done
        stoimost_alter = NaN,//done
        obshiy_ves_shtuku = NaN,//done
        status_online = NaN,//done
        zavod_name = NaN,//done
        diller = NaN,//done
        tip_clenta = NaN,//done
        artikul = NaN,//done

        is_iklyuch = false,//done
        is_special = false,//done
        is_active = false
        ) {
            this.id = id;//done 
            this.full = full;//done
            this.nazvaniye_system = nazvaniye_system;
            this.camera = camera;
            this.base_artikul = base_artikul;
            this.kod_k_component = kod_k_component;
            this.tip_pokritiya = tip_pokritiya;
            this.kod_svet_zames = kod_svet_zames;//done
            this.dlina = dlina;//done
            this.svet_lamplonka_snaruji = svet_lamplonka_snaruji;
            this.kod_lam_sn = kod_lam_sn;//done
            this.svet_lamplonka_vnutri = svet_lamplonka_vnutri;
            this.kod_lam_vn = kod_lam_vn;//done
            this.kod_svet_rezini = kod_svet_rezini;//done
            this.svet_rezin = svet_rezin;
            this.kod_nakleyki = kod_nakleyki;//done
            this.nadpis_nakleyki = nadpis_nakleyki;
            this.gruppa_materialov = 'PVCGP';
            this.kratkiy_tekst = kratkiy_tekst;
            this.sap_code = sap_code;//done
            this.krat = krat;//done
            this.comment = comment;//done
            this.pickupdate = pickupdate;//done
            this.sena_c_nds = sena_c_nds;//done
            this.sena_bez_nds = sena_bez_nds;//done
            this.online_id = online_id;//done
            this.nazvaniye_ruchnoy = nazvaniye_ruchnoy;//done
            this.svet_product = svet_product;//done
            this.group_zakup = group_zakup;//done
            this.group = group;//done
            this.tip = tip;//done
            this.segment = segment;
            this.buxgalter_tovar = buxgalter_tovar;
            this.buxgalter_uchot = buxgalter_uchot;
            this.bazoviy_edin = bazoviy_edin;//done
            this.alter_edin = alter_edin;
            this.stoimost_baza = stoimost_baza;
            this.stoimost_alter = stoimost_alter;
            this.obshiy_ves_shtuku = obshiy_ves_shtuku;
            this.status_online = status_online;//done
            this.zavod_name = zavod_name;//done
            this.diller = diller;//done
            this.tip_clenta = tip_clenta;//done
            this.artikul = artikul;//done
    
            this.is_iklyuch = is_iklyuch;//done
            this.is_special = is_special;//done
            this.is_active = is_active;
    }
    get_kratkiy_tekst(){
        switch(this.id){
            case 1: 
            if(this.is_active){
                if(this.sap_code && this.krat && this.online_id && this.nazvaniye_ruchnoy){
                    if(this.artikul && this.dlina && this.kod_svet_zames && this.kod_nakleyki){
                        return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' ' +this.kod_nakleyki,'accept':true}
                    }else{
                        return {'text':'XXXXXXXX','accept':true}
                    }
                }else{
                    if(this.artikul && this.dlina && this.kod_svet_zames && this.kod_nakleyki){
                        return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' ' +this.kod_nakleyki,'accept':false}
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }
            }else{
                if(this.is_iklyuch){
                    if(this.dlina && this.kod_svet_zames && this.kod_nakleyki){
                        if(this.is_active){
                            if (this.online_id && this.nazvaniye_ruchnoy ){
            
                               
                                return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' ' +this.kod_nakleyki,'accept':true}
                            }else{
                                
                                return {'text':this.artikul+ ' ' + this.kod_svet_zames + ' L' + this.dlina +' ' +this.kod_nakleyki,'accept':false}
                            }
                            
                        }else{
                            if (this.tip_clenta && this.sena_bez_nds && this.sena_c_nds && this.pickupdate && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online&& this.segment){
                                
                                
                                return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' ' +this.kod_nakleyki,'accept':true}
                            }else{
                                
                                return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' ' +this.kod_nakleyki,'accept':false}
                            }
                        } 
            
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
        
                    }else{
                        
                        if(this.kod_svet_rezini && this.dlina && this.kod_svet_zames && this.kod_nakleyki){
                
                            if(this.is_active){
                                if (this.online_id && this.nazvaniye_ruchnoy){
                
                                
                                    return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' '+this.kod_svet_rezini +' ' +this.kod_nakleyki,'accept':true}
                                }else{
                                    
                                    return {'text':this.artikul+ ' ' + this.kod_svet_zames + ' L' + this.dlina +' '+this.kod_svet_rezini +' ' +this.kod_nakleyki,'accept':false}
                                }
                                
                            }else{
                                
                                if (this.tip_clenta && this.sena_bez_nds && this.sena_c_nds && this.pickupdate && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online&& this.segment){
                                    
                                    
                                    return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' '+this.kod_svet_rezini +' ' +this.kod_nakleyki,'accept':true}
                                }else{
                                    
                                    return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' '+this.kod_svet_rezini +' ' +this.kod_nakleyki,'accept':false}
                                }
                            } 
                
                        }else{
                            return {'text':'XXXXXXXX','accept':false}
                        }
                    }
                } break;
            case 2:if(this.is_iklyuch){
                if(this.dlina && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki && this.kod_svet_zames){
        
                    if(this.is_active){
                        if (this.online_id && this.nazvaniye_ruchnoy){
        
                            return {'text':this.artikul + ' '+this.kod_svet_zames + ' L' + this.dlina +' ' + this.kod_lam_sn+'/'+this.kod_lam_vn + ' '+this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.artikul+ ' ' + this.kod_svet_zames + ' L' + this.dlina +' ' + this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':false}
                        }
        
                    }else{
                        if (this.tip_clenta && this.sena_bez_nds && this.sena_c_nds && this.pickupdate && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online&& this.segment){
        
                            return {'text':this.artikul+ ' ' + this.kod_svet_zames + ' L' + this.dlina +' ' + this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' ' + this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':false}
                        }
                    } 
        
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
        
                    if(this.dlina && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki && this.kod_svet_rezini && this.kod_svet_zames){
            
                        if(this.is_active){
                            if (this.online_id && this.nazvaniye_ruchnoy){
            
                                return {'text':this.artikul + ' '+this.kod_svet_zames + ' L' + this.dlina +' ' + this.kod_lam_sn+'/'+this.kod_lam_vn + ' '+this.kod_svet_rezini +' '+this.kod_nakleyki,'accept':true}
                            }else{
                                return {'text':this.artikul+ ' ' + this.kod_svet_zames + ' L' + this.dlina +' ' + this.kod_lam_sn+'/'+this.kod_lam_vn + ' '+this.kod_svet_rezini +' ' +this.kod_nakleyki,'accept':false}
                            }
            
                        }else{
                        if (this.tip_clenta && this.sena_bez_nds && this.sena_c_nds && this.pickupdate && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online&& this.segment){
            
                                return {'text':this.artikul+ ' ' + this.kod_svet_zames + ' L' + this.dlina +' ' + this.kod_lam_sn+'/'+this.kod_lam_vn + ' '+this.kod_svet_rezini +' ' +this.kod_nakleyki,'accept':true}
                            }else{
                                return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' ' + this.kod_lam_sn+'/'+this.kod_lam_vn + ' '+this.kod_svet_rezini +' ' +this.kod_nakleyki,'accept':false}
                            }
                        } 
            
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }break;
            case 3:
                if(this.is_active){
                    if(this.sap_code && this.krat && this.online_id && this.nazvaniye_ruchnoy){
                        if(this.artikul && this.dlina && this.kod_svet_zames && this.kod_nakleyki){
                            return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':'XXXXXXXX','accept':true}
                        }
                    }else{
                        if(this.artikul && this.dlina && this.kod_svet_zames && this.kod_nakleyki){
                            return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' ' +this.kod_nakleyki,'accept':false}
                        }else{
                            return {'text':'XXXXXXXX','accept':false}
                        }
                    }
                }else{
                    if(this.is_iklyuch){
                        if(this.dlina && this.kod_svet_zames && this.kod_nakleyki){
                            if(this.is_active){
                                if (this.online_id && this.nazvaniye_ruchnoy&& this.segment){
                
                                   
                                    return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' ' +this.kod_nakleyki,'accept':true}
                                }else{
                                    
                                    return {'text':this.artikul+ ' ' + this.kod_svet_zames + ' L' + this.dlina +' ' +this.kod_nakleyki,'accept':false}
                                }
                                
                            }else{
                                if (this.tip_clenta && this.sena_bez_nds && this.sena_c_nds && this.pickupdate && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online&& this.segment){
                                    
                                    
                                    return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' ' +this.kod_nakleyki,'accept':true}
                                }else{
                                    
                                    return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' ' +this.kod_nakleyki,'accept':false}
                                }
                            } 
                
                        }else{
                            return {'text':'XXXXXXXX','accept':false}
                        }
            
                        }else{
                            
                            if(this.kod_svet_rezini && this.dlina && this.kod_svet_zames && this.kod_nakleyki){
                    
                                if(this.is_active){
                                    if (this.online_id && this.nazvaniye_ruchnoy && this.segment){
                    
                                    
                                        return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' '+this.kod_svet_rezini +' ' +this.kod_nakleyki,'accept':true}
                                    }else{
                                        
                                        return {'text':this.artikul+ ' ' + this.kod_svet_zames + ' L' + this.dlina +' '+this.kod_svet_rezini +' ' +this.kod_nakleyki,'accept':false}
                                    }
                                    
                                }else{
                                    
                                    if (this.tip_clenta && this.sena_bez_nds && this.sena_c_nds && this.pickupdate && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.segment){
                                        
                                        
                                        return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' '+this.kod_svet_rezini +' ' +this.kod_nakleyki,'accept':true}
                                    }else{
                                        
                                        return {'text':this.artikul + ' '+ this.kod_svet_zames + ' L' + this.dlina +' '+this.kod_svet_rezini +' ' +this.kod_nakleyki,'accept':false}
                                    }
                                } 
                    
                            }else{
                                return {'text':'XXXXXXXX','accept':false}
                            }
                        }
                    } break;
            }
            
       
       
    }
  }

function front_piece(start=1,end=6){
    var text =""

    for (let i = start; i < end; i++) {
        var buttons =''
        if(status_proccess1 == 'new'){
            buttons=`<td class="sticky-col"   style='left:0; padding-right:5px; background-color:white!important;' >
                    <div class="btn-group" role="group" aria-label="Basic example">
                            <button type="button" class="btn btn-outline-secondary btn-sm" id='clear_btn`+String(i)+`' onclick="artukil_clear(`+String(i)+`)" data-bs-toggle='popover' title='Tozalab tashlash'><i class="bi bi-x-circle"></i></button>
                            <button type="button" class="btn btn-outline-secondary btn-sm"  onclick="copy_tr(`+String(i)+`)" data-bs-toggle='popover' title='Dubl qilish'><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-copy" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M4 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 5a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-1h1v1a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h1v1z"/></svg></button>
                            <button type="button" class="btn btn-outline-secondary btn-sm" id='create_btn`+String(i)+`' onclick="create(`+String(i)+`)" data-bs-toggle='popover' title='Yangi sozdaniya qilish uchun ishlatiladi' style='font-size:16px; width:34px'>С</button>
                            <button type="button" class="btn btn-outline-secondary btn-sm" id='activate_btn`+String(i)+`' onclick="activate(`+String(i)+`)" data-bs-toggle='popover' title='Activatsiya qilish uchun ishlatiladi' style='font-size:16px;width:34px'>А</button>
                    </div>
                
                    </td>
                    <td style='display:none;'>
                        <div class="input-group input-group-sm mb-1" style='width:150px;'>
                            <span class ='nazvaniye_system` +String(i)+`'style="font-size: 10px; font-weight:700;padding:5px;width:150px" ></span>
                        </div>
                    </td>
                    <td style='display:none;'>
                        <div class="input-group input-group-sm mb-1">
                            <b><span id='camera` +String(i)+`'style=" font-size:12px;padding-left:5px"></span></b>
                        </div>
                    </td>
                    <td class="sticky-col" style=' left: 139.6px;background-color:white!important' >
                        <div class="input-group input-group-sm mb-1">
                            <select class=" form-control basic_artikul" style="background-color:#ddebf7; width: 140px; font-size:10px " disabled id="artikul`+String(i)+`" ></select>
                        </div>
                        <span style='display:none' id='artikul_pvc` +String(i)+`'></span>
                        <span style='display:none' id='iskyucheniye` +String(i)+`'></span>
                        <span style='display:none' id='is_special` +String(i)+`'></span>
                        <span style='display:none' id='nakleyka_nt1` +String(i)+`'></span>
                    </td>`
        }else{
            buttons=`
                    <td style='display:none;'>
                        <div class="input-group input-group-sm mb-1" style='width:150px;'>
                            <span class ='nazvaniye_system` +String(i)+`'style="font-size: 10px; font-weight:700;padding:5px;width:150px" ></span>
                        </div>
                    </td>
                    <td style='display:none;'>
                        <div class="input-group input-group-sm mb-1">
                            <b><span id='camera` +String(i)+`'style=" font-size:12px;padding-left:5px"></span></b>
                        </div>
                    </td>
                    <td class="sticky-col" style=' left:0;background-color:white!important' >
                        <div class="input-group input-group-sm mb-1">
                            <select class=" form-control basic_artikul" style="background-color:#ddebf7; width: 140px; font-size:10px " disabled id="artikul`+String(i)+`" ></select>
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
        
        <td style='display:none;' >
            <div class="input-group input-group-sm mb-1">
                <b><span  id ='kod_komponent` +String(i)+`'style="font-size: 12px;padding-left:5px;"></span></b>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 177px; font-size:12px; padding-right:0px;height:27px!important;z-index:0" onchange="tip_pokritiya_selected(`+String(i)+`,this.value)" disabled id='tip_pokritiya`+String(i)+`' required>
                    <option  selected disabled></option>
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
                <option value="N1" >N1</option>
                <option value="W6" >W6</option>
            </select>
            
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type="number"   class="form-control " style='width:70px;height:27px!important;z-index:0' oninput="create_kratkiy_tekst(`+String(i)+`); limitLength(this, 4);"  disabled aria-describedby="inputGroup-sizing-sm" name ='length`+String(i)+`' id="length`+String(i)+`"  >
            </div>
        </td>

        <td >
            <div class="input-group input-group-sm mb-1">    
            <select class="form-select" aria-label="" style="width: 220px;height:27px!important;z-index:0" onchange="svet_lamplonka_snaruji_selected(`+String(i)+`,this.value)" disabled id='svet_lamplonka_snaruji`+String(i)+`'>
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
            <div class="input-group input-group-sm mb-1" style="width: 60px;">
            <select class="form-select" aria-label="" style="width: 50px;border-color:red;display:none;height:27px!important;z-index:0"   id='kod_svet_rezini`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option  value="" selected disabled ></option>
                <option value="Чёрная резина" >BR</option>
                <option value="Серая резина" >GR</option>
                <option value="Без резины" >NR</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" id='svet_text`+String(i)+`'>
                
                    <span class =' text-center ' style="font-size:10px; font-weight: bold; z-index:0;white-space: nowrap;" id='svet_rezin`+String(i)+`'></span>
                
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" id="nakleyka`+String(i)+`">
            <div id='nakleyka_select`+String(i)+`' class='nak_select`+String(i)+`' style='display:none;'>
                <select class ='kod_nakleyki`+String(i)+`'  style=' width: 70px;padding-left:35%;height:27px!important;z-index:0' onchange="create_kratkiy_tekst(`+String(i)+`)" data-placeholder="..."></select>
            </div>
            </div>
        </td>
         <td  style='width:100px'>
            <div class="input-group input-group-sm mb-1" style='width:100%'>
                
                    <span class ='text-center ' style="width:100px;font-size:12px;  padding:5px;z-index:0;whitespace:nowrap;" id='nadpis_nakleyki`+String(i)+`'></span>
                
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <div>
                    <span class =' text-center ' style="font-size: small; font-weight: bold; z-index:0" >PVCGP</span>
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <span  style="font-size: small; width:250px; font-weight: bold; z-index:0;white-space: nowrap;" id='kratkiy_tekst`+String(i)+`'></span>
            </div>
        </td>

        <td >
            <div class="input-group input-group-sm mb-1">
        
            <input type='text' class=" form-control " style=" width: 150px; font-size:10px; height:27px!important;z-index:0;" disabled id='sap_code_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        
            </div>
        </td> 
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 250px; font-size:10px; height:27px!important;z-index:0;" disabled id='kratkiy_tekst_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 250px; font-size:10px; height:27px!important;z-index:0;display:none"  id='comment`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
            
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 75px; font-size:10px; display:none;height:27px!important;z-index:0;" id='obshiy_ves_shtuku`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)' ></input>
            </div>
        </td>
        <td >
            <input  style='display:none;border-color:red; line-height:15px;height:27px!important;z-index:0' type="date" class="form-control" id="pickupdate`+String(i)+`" onchange='create_kratkiy_tekst(`+String(i)+`)'>      
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px; display:none;height:27px!important;z-index:0" id='sena_c_nds`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            
            <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px; display:none; height:27px!important;z-index:0;" id='sena_bez_nds`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type="number"   class="form-control " style='border-color:red;width:75px;height:27px!important;z-index:0;display:none;' oninput="create_kratkiy_tekst(`+String(i)+`); limitLength(this, 7);"  aria-describedby="inputGroup-sizing-sm" name ='online_savdo_id`+String(i)+`' id="online_savdo_id`+String(i)+`"  >
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
             <input type='text' class=" form-control " style="border-color:red; width: 250px; font-size:10px; height:27px!important;z-index:0;display:none;"  id='nazvaniye_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
            
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px; border-color:red;display:none;height:27px!important;z-index:0"  id='svet_product`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  value='' selected></option>
            <option   value="LAM">LAM</option>
            <option   value="WHITE">WHITE</option>
        </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 230px; font-size:12px; padding-right:0px;  border-color:red;display:none;height:27px!important;z-index:0" id='group_zakup`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option value="PVX OQ (Navoiy)">PVX OQ (Navoiy)</option>
            <option value="PVX LAM (Navoiy)">PVX LAM (Navoiy)</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1"  >
            <select class="form-select" aria-label="" id='group`+String(i)+`' style="width: 240px; font-size:12px; padding-right:0px; border-color:red;display:none;height:27px!important;z-index:0"    onchange='create_kratkiy_tekst(`+String(i)+`)'required>
                <option  selected></option>
                <option value="5200 QVT PVC (NAVOIY)">5200 QVT PVC (NAVOIY)</option>
                <option value="5200 QVT PVC RETPEN (NAVOIY)">5200 QVT PVC RETPEN (NAVOIY)</option>
                <option value="5200 TRIO PVC (NAVOIY)">5200 TRIO PVC (NAVOIY)</option>
                <option value="5800 ENGELBERG PVC (NAVOIY)">5800 ENGELBERG PVC (NAVOIY)</option>
                <option value="5800 QVT PVC (NAVOIY)">5800 QVT PVC (NAVOIY)</option>
                <option value="5800 TRIO PVC (NAVOIY)">5800 TRIO PVC (NAVOIY)</option>
                <option value="6000 AGROMIR (NAVOIY)">6000 AGROMIR (NAVOIY)</option>
                <option value="6000 EKO PVC (NAVOIY)">6000 EKO PVC (NAVOIY)</option>
                <option value="6000 EKO PVC RETPEN (NAVOIY)">6000 EKO PVC RETPEN (NAVOIY)</option>
                <option value="6000 QVT ALUTEX (NAVOIY)">6000 QVT ALUTEX (NAVOIY)</option>
                <option value="6000 QVT PVC (NAVOIY)">6000 QVT PVC (NAVOIY)</option>
                <option value="6000 QVT PVC RETPEN (NAVOIY)">6000 QVT PVC RETPEN (NAVOIY)</option>
                <option value="6000 TRIO PVC (NAVOIY)">6000 TRIO PVC (NAVOIY)</option>
                <option value="7000 AKFA (NAVOIY)">7000 AKFA (NAVOIY)</option>
                <option value="7000 ENGELBERG PVC (NAVOIY)">7000 ENGELBERG PVC (NAVOIY)</option>
                <option value="KONYUSHNYA">KONYUSHNYA</option>
                <option value="LAM 5200 TRIO PVC (NAVOIY)">LAM 5200 TRIO PVC (NAVOIY)</option>
                <option value="LAM 5800 ENGELBERG PVC">LAM 5800 ENGELBERG PVC</option>
                <option value="LAM 5800 TRIO PVC (NAVOIY)">LAM 5800 TRIO PVC (NAVOIY)</option>
                <option value="LAM 6000 QVT ALUTEX">LAM 6000 QVT ALUTEX</option>
                <option value="LAM 6000 QVT PVC (NAVOIY)">LAM 6000 QVT PVC (NAVOIY)</option>
                <option value="LAM 6000 QVT PVC RETPEN (NAVOIY)">LAM 6000 QVT PVC RETPEN (NAVOIY)</option>
                <option value="LAM 6000 TRIO ALUTEX">LAM 6000 TRIO ALUTEX</option>
                <option value="LAM 6000 TRIO PVC (NAVOIY)">LAM 6000 TRIO PVC (NAVOIY)</option>
                <option value="LAM 7000 AKFA (NAVOIY)">LAM 7000 AKFA (NAVOIY)</option>
                <option value="LAM 7000 ENGELBERG PVC (NAVOIY)">LAM 7000 ENGELBERG PVC (NAVOIY)</option>
                <option value="LAM 7600 ENGELBERG PVC (NAVOIY)">LAM 7600 ENGELBERG PVC (NAVOIY)</option>
                <option value="LAM LAMBRI PVC (NAVOIY)">LAM LAMBRI PVC (NAVOIY)</option>
                <option value="LAM OTKOS Prof. (NAVOIY)">LAM OTKOS Prof. (NAVOIY)</option>
                <option value="LAM Sendvich Panel">LAM Sendvich Panel</option>
                <option value="LAMBRI PVC (NAVOIY)">LAMBRI PVC (NAVOIY)</option>
                <option value="PODOKONNIK (LAM) (NAVOIY)">PODOKONNIK (LAM) (NAVOIY)</option>
                <option value="PODOKONNIK (LAM) (RETPEN)">PODOKONNIK (LAM) (RETPEN)</option>
                <option value="PODOKONNIK (OQ) (NAVOIY)">PODOKONNIK (OQ) (NAVOIY)</option>
                <option value="PODOKONNIK (OQ) (RETPEN)">PODOKONNIK (OQ) (RETPEN)</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px; border-color:red;display:none;height:27px!important;z-index:0"  id='tip`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)'required>
                <option  selected></option>
                <option value="Сырье">Сырье</option>
                <option value="Готовый продукт">Готовый продукт</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 145px; font-size:12px; padding-right:0px; display:none;height:27px!important;z-index:0;border-color:red;" id='segment`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                
                <option value="Стандарт">Стандарт</option>
                <option value="Премиум">Премиум</option>
                
                <option value="RETPEN 8-10%">RETPEN 8-10%</option>
                <option value="RETPEN 10-12%">RETPEN 10-12%</option>
                <option value="RETPEN 25%">RETPEN 25%</option>
                
                <option value="Podokonnik EKO">Podokonnik EKO</option>
                
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 520px; font-size:12px; padding-right:0px; display:none;height:27px!important;z-index:0" id='buxgalter_tovar`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="Профиль из ПВХ">Профиль из ПВХ</option>
                <option value="Профиль ПВХ с уплотнителем">Профиль ПВХ с уплотнителем</option>
                <option value="Профиль из ПВХ (Engelberg)">Профиль из ПВХ (Engelberg)</option>
                <option value="Подоконник из ПВХ">Подоконник из ПВХ</option>
                <option value="Ламбри из ПВХ">Ламбри из ПВХ</option>
                <option value="Профиль из ПВХ ламинированный">Профиль из ПВХ ламинированный</option>
                <option value="Профиль из ПВХ ламинированный с уплотнителем">Профиль из ПВХ ламинированный с уплотнителем</option>
                <option value="Профиль из ПВХ ламинированный (Engelberg)">Профиль из ПВХ ламинированный (Engelberg)</option>
                <option value="Подоконник из ПВХ ламинированный">Подоконник из ПВХ ламинированный</option>
                <option value="Ламбри из ПВХ ламинированный">Ламбри из ПВХ ламинированный</option>
                <option value="Профиль из ПВХ (Retpen)">Профиль из ПВХ (Retpen)</option>
                <option value="Профиль из ПВХ с акриловым покрытием">Профиль из ПВХ с акриловым покрытием</option>
                <option value="Профиль из ПВХ с односторонним ламинированным покрытием">Профиль из ПВХ с односторонним ламинированным покрытием</option>
                <option value="Профиль из ПВХ ламинированный с уплотнителем (Retpen)">Профиль из ПВХ ламинированный с уплотнителем (Retpen)</option>
                <option value="Профиль из ПВХ ламинированный (Retpen)">Профиль из ПВХ ламинированный (Retpen)</option>
                <option value="Подоконник из ПВХ ламинированный (Retpen)">Подоконник из ПВХ ламинированный (Retpen)</option>
                <option value="Подоконник из ПВХ (Retpen)">Подоконник из ПВХ (Retpen)</option>           
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px;display:none;height:27px!important;z-index:0" id='buxgalter_uchot`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
               
                <option  value="Килограмм">Килограмм</div>
                
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px; border-color:red;display:none;height:27px!important;z-index:0" id='bazoviy_edin`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option vlaue="Штука">Штука</div>
                
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px;display:none;height:27px!important;z-index:0" id='alter_edin`+ String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                
                <option vlaue="Килограмм">Килограмм</div>
                
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 75px; font-size:10px; display:none;height:27px!important;z-index:0" id='stoimost_baza`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)' ></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 75px; font-size:10px; display:none;height:27px!important;z-index:0;" id='stoimost_alter`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)' ></input>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px; display:none;height:27px!important;z-index:0" id='status`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="Активный">Активный</option>
                <option value="Пассивный">Пассивный</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <span class =' text-center ' style="font-size: small; width:190px; font-weight: bold; z-index:0" id='zavod_name`+String(i)+`'>ZAVOD PVS NAVOIY</span>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            
            <select class="form-select" aria-label="" style="width: 75px; font-size:12px; padding-right:0px;display:none;height:27px!important;z-index:0" id='diller`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="1">Да</option>
                <option value="0">Нет</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px; border-color:red;display:none;height:27px!important;z-index:0" id='tip_clenta`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="AKFA">AKFA</option>
                <option value="IMZO">IMZO</option>
                <option value="Q-Q">Q-Q</option>
                <option value="FRANCHISING">FRANCHISING</option>
                <option value="AKFA-IMZO-FRANCHISING">AKFA-IMZO-FRANCHISING</option>
                <option value="IMZO-FRANCHISING">IMZO-FRANCHISING</option>
            </select>
            </div>
        </td>
        <td style="display: none;" >
            <div class="input-group input-group-sm mb-1">
            <span id="is_active`+String(i)+`" style="display: none;"></span>
            </div>
        </td>
        
        </tr>`
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
        
        
            if(status_proccess1 == 'new'){
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
                    var is_special = $('#is_special'+String(i));
                    var nakleyka_nt1 = $('#nakleyka_nt1'+String(i));
                    var nadpis_nakleyki = $('#nadpis_nakleyki'+String(i));
                    var tip_pokritiya = $('#tip_pokritiya'+String(i));
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
                            $('#nakleyka'+i).find('.chosen-container').find('.chosen-single').css('border-color', 'red');
                        }else{
                            set_nakleyka(nakleyka_list,'.kod_nakleyki'+i,value='',add=true)
                            $('#nakleyka'+i).find('.chosen-container').find('.chosen-single').css('border-color', 'red');
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

if(status_proccess1 == 'new'){
    table.append(text)
    request_piece()

}else{
    var jsonData = JSON.parse(jsonData);
    // var jsonData ='{{order}}'

    // var ii= 1

    for(var key1 in jsonData){
        data_base[key1] = new BasePokritiya()
        for(var key2 in jsonData[key1]){
            data_base[key1][key2] = jsonData[key1][key2]
        }
        // ii += 1
    }



    var text2 =''
    for(var key1 in jsonData){
        // console.log(key1,'lllsdsafasfads')
        text2 += front_piece( parseInt(key1),parseInt(key1)+1)
    }


    var table = $('#table-artikul')

    table.append(text2)

    // var i = 1
    for(key2 in data_base){
        copy_tr(key2,key2)
        // i += 1
    }
}



// request_piece()




function copy_tr(id,ii=1){
    if(!data_base[id]){
        console.log('salom2222 copy')
    }else{
        if(status_proccess1 == 'new'){
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
        var kod_nakleyki = data.kod_nakleyki;
        var nadpis_nakleyki = data.nadpis_nakleyki;
        var kratkiy_tekst = data.kratkiy_tekst;
        var sap_code_ruchnoy = data.sap_code;
        var kratkiy_text_ruchnoy = data.krat;
        var comment = data.comment;
        var pickupdate = data.pickupdate
        var sena_c_nds = data.sena_c_nds
        var sena_bez_nds = data.sena_bez_nds
        var online_id = data.online_id
        var nazvaniye_ruchnoy = data.nazvaniye_ruchnoy
        var svet_product = data.svet_product
        var group_zakup = data.group_zakup
        var group = data.group
        var tip= data.tip
        var segment = data.segment
        var buxgalter_tovar = data.buxgalter_tovar
        var buxgalter_uchot = data.buxgalter_uchot
        var bazoviy_edin = data.bazoviy_edin
        var alter_edin = data.alter_edin
        var stoimost_baza = data.stoimost_baza
        var stoimost_alter = data.stoimost_alter
        var obshiy_ves_shtuku = data.obshiy_ves_shtuku
        var status_online = data.status_online
        var zavod_name = data.zavod_name
        var diller = data.diller
        var tip_clenta = data.tip_clenta 
        var artikul = data.artikul
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


        
         
        
      
        var activate_btn =$('#activate_btn'+s);
        var create_btn =$('#create_btn'+s);
        activate_btn.attr('disabled',true)
        create_btn.attr('disabled',true)

        


        
        

        check_input_and_change(comment,'#comment'+s,dis=false,is_req=false,is_req_simple=true)
        


       
        check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s)
        
        if(!is_active){
            create_btn.css('background-color','green')
            create_btn.css('color','white')
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
    
            if(!is_iklyuch){
                check_input_and_change(svet_rezin,'#kod_svet_rezini'+s,dis=false,is_req=true)
                check_text_and_change(svet_rezin,'#svet_rezin'+s)
            }
    
            var nakleyka_select = $('#nakleyka_select'+String(s));
    
           
            nakleyka_select.css('display','block')
            nakleyka_select.attr('required',true)
    
            set_nakleyka(nakleyka_list,'.kod_nakleyki'+s,value=kod_nakleyki)
           
            if(kod_nakleyki){
                $('#nakleyka'+s).find('.chosen-container').find('.chosen-single').css('border-color', '#dedad9');
            }else{
                $('#nakleyka'+s).find('.chosen-container').find('.chosen-single').css('border-color', 'red');
            }
            check_text_and_change(nadpis_nakleyki,'#nadpis_nakleyki'+s)
    
    
           
            check_text_and_change(kratkiy_tekst,'#kratkiy_tekst'+s)

            check_input_and_change(sap_code_ruchnoy,'#sap_code_ruchnoy'+s,dis=true)
            check_input_and_change(kratkiy_text_ruchnoy,'#kratkiy_tekst_ruchnoy'+s,dis=true)
    
    

            check_input_and_change(pickupdate,'#pickupdate'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(sena_c_nds,'#sena_c_nds'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(sena_bez_nds,'#sena_bez_nds'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(online_id,'#online_savdo_id'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(svet_product,'#svet_product'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(group_zakup,'#group_zakup'+s,dis=false,is_req=false,is_req_simple=true)

            check_input_and_change(group,'#group'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(tip,'#tip'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(segment,'#segment'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(buxgalter_tovar,'#buxgalter_tovar'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(buxgalter_uchot,'#buxgalter_uchot'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(bazoviy_edin,'#bazoviy_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(alter_edin,'#alter_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_baza,'#stoimost_baza'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_alter,'#stoimost_alter'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(obshiy_ves_shtuku,'#obshiy_ves_shtuku'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(status_online,'#status'+s,dis=true,is_req=false,is_req_simple=true)
            check_input_and_change(zavod_name,'#zavod_name'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(diller,'#diller'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip_clenta,'#tip_clenta'+s,dis=false,is_req=true,is_req_simple=false)
            var is_active =$('#is_active'+s)
            is_active.text('Пассивный')

        }else{
            
            activate_btn.css('background-color','orange')
            activate_btn.css('color','white')
            check_input_and_change(sap_code_ruchnoy,'#sap_code_ruchnoy'+s,dis=false,is_req=true)
            check_input_and_change(kratkiy_text_ruchnoy,'#kratkiy_tekst_ruchnoy'+s,dis=false,is_req=true)
            check_input_and_change(pickupdate,'#pickupdate'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sena_c_nds,'#sena_c_nds'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sena_bez_nds,'#sena_bez_nds'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(online_id,'#online_savdo_id'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(svet_product,'#svet_product'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(group_zakup,'#group_zakup'+s,dis=false,is_req=false,is_req_simple=true)

            check_input_and_change(group,'#group'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip,'#tip'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(segment,'#segment'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(buxgalter_tovar,'#buxgalter_tovar'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(buxgalter_uchot,'#buxgalter_uchot'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(bazoviy_edin,'#bazoviy_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(alter_edin,'#alter_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_baza,'#stoimost_baza'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_alter,'#stoimost_alter'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(obshiy_ves_shtuku,'#obshiy_ves_shtuku'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(status_online,'#status'+s,dis=true,is_req=false,is_req_simple=true)
            check_input_and_change(zavod_name,'#zavod_name'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(diller,'#diller'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip_clenta,'#tip_clenta'+s,dis=false,is_req=false,is_req_simple=true)
            
            var is_active =$('#is_active'+s)
            is_active.text('Активный')
        }
        

        
        
    }


}
function removeQuotesFromStartAndEnd(str) {
    // Remove double quotes from the beginning and end of the string
    return str.replace(/^"+|"+$/g, '');
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



function create(i){
    
    var artikul = $('#artikul'+i)
    
    artikul.attr('disabled',false)

    var status_first =$('#status'+i);
    status_first.val('Пассивный')
    status_first.attr('disabled',true)

    var is_active =$('#is_active'+i);
    is_active.text('Пассивный')

    var tip =$('#tip'+i);
    tip.val('Готовый продукт')
    

    var activate_btn =$('#activate_btn'+i);
    var create_btn =$('#create_btn'+i);
    create_btn.css('background-color','green')
    create_btn.css('color','white')
    activate_btn.attr('disabled',true)
    create_btn.attr('disabled',true)
   

}

function activate(i){
    // data_base[i] = new OnlineSavdo()

    var artikul = $('#artikul'+i)
    
    // artikul.attr('disabled',false)


    var activate_btn =$('#activate_btn'+i);
    var create_btn =$('#create_btn'+i);
    activate_btn.css('background-color','orange')
    activate_btn.css('color','white')
    activate_btn.attr('disabled',true)
    create_btn.attr('disabled',true)


    var status_first =$('#status'+i);
    status_first.val('Активный')

    var is_active =$('#is_active'+i);
    is_active.text('Активный')
    status_first.attr('disabled',true)

    var svet_product =$('#svet_product'+i);
    
    data_base[i] = new BasePokritiya()
    data_base[i].id = 3
    
        
    data_base[i].is_active = true

    var obshiy_ves_shtuku =$('#obshiy_ves_shtuku'+i);
    var sap_code_ruchnoy =$('#sap_code_ruchnoy'+i);
    var kratkiy_tekst_ruchnoy =$('#kratkiy_tekst_ruchnoy'+i);
    var online_savdo_id =$('#online_savdo_id'+i);
    var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+i);
    var svet_product =$('#svet_product'+i);
    var group_zakup =$('#group_zakup'+i);
    var group =$('#group'+i);
    var tip =$('#tip'+i);
    var bazoviy_edin =$('#bazoviy_edin'+i);
    var status =$('#status'+i);
    var zavod =$('#zavod'+i);
    var buxgalter_uchot =$('#buxgalter_uchot'+i);
    var alter_edin =$('#alter_edin'+i);
    var stoimost_baza =$('#stoimost_baza'+i);
    var stoimost_alter =$('#stoimost_alter'+i);
    var segment =$('#segment'+i);
    var buxgalter_tovar =$('#buxgalter_tovar'+i);
    var comment =$('#comment'+i);
    var pickupdate =$('#pickupdate'+i);
    var sena_c_nds =$('#sena_c_nds'+i);
    var sena_bez_nds =$('#sena_bez_nds'+i);
    var diller =$('#diller'+i)
    var tip_clenta =$('#tip_clenta'+i)

    diller.css('display','block')
    tip_clenta.css('display','block')
    comment.css('display','block')
    pickupdate.css('display','block')
    sena_c_nds.css('display','block')
    sena_bez_nds.css('display','block')
    
    
    
    
    sap_code_ruchnoy.css('display','block')
    kratkiy_tekst_ruchnoy.css('display','block')
    online_savdo_id.css('display','block')
    nazvaniye_ruchnoy.css('display','block')
    svet_product.css('display','block')
    group_zakup.css('display','block')
    group.css('display','block')
    tip.css('display','block')
    bazoviy_edin.css('display','block')
    status.css('display','block')
    zavod.css('display','block')
    buxgalter_uchot.css('display','block')
    alter_edin.css('display','block')
    stoimost_baza.css('display','block')
    stoimost_alter.css('display','block')
    obshiy_ves_shtuku.css('display','block')
    segment.css('display','block')
    buxgalter_tovar.css('display','block')


    status.val('Активный')
    status.attr('disabled',true)

    sap_code_ruchnoy.css('border-color','red')
    kratkiy_tekst_ruchnoy.css('border-color','red')
    sap_code_ruchnoy.attr('disabled',false)
    kratkiy_tekst_ruchnoy.attr('disabled',false)
    online_savdo_id.css('border-color','red')
    nazvaniye_ruchnoy.css('border-color','red')
    svet_product.css('border-color','#dedad9')
    group_zakup.css('border-color','#dedad9')
    group.css('border-color','#dedad9')
    tip.css('border-color','#dedad9')
    bazoviy_edin.css('border-color','#dedad9')
    status.css('border-color','#dedad9')
    zavod.css('border-color','#dedad9')
    buxgalter_uchot.css('border-color','#dedad9')
    alter_edin.css('border-color','#dedad9')
    stoimost_baza.css('border-color','#dedad9')
    stoimost_alter.css('border-color','#dedad9')
    segment.css('border-color','#dedad9')
    buxgalter_tovar.css('border-color','#dedad9')
    comment.css('border-color','#dedad9')
    pickupdate.css('border-color','#dedad9')
    sena_c_nds.css('border-color','#dedad9')
    sena_bez_nds.css('border-color','#dedad9')
    tip_clenta.css('border-color','#dedad9')

    
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
   
   console.log(id,'idddddddd')
    create_kratkiy_tekst(id)
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

    set_nakleyka(nakleyka_list,'.kod_nakleyki'+id,value='',add=false)
    $('#nakleyka'+id).find('.chosen-container').find('.chosen-single').css('border-color', '#dedad9');

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
    $('#artikul'+id).attr('disabled',true)

    var status_first = $('#status'+String(id))
   
    status_first.val('')

    var sap_code_ruchnoy =$('#sap_code_ruchnoy'+id);
    var kratkiy_tekst_ruchnoy =$('#kratkiy_tekst_ruchnoy'+id);
    var online_savdo_id =$('#online_savdo_id'+id);
    var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);


    var svet_product =$('#svet_product'+id);
    var group_zakup =$('#group_zakup'+id);
    var group =$('#group'+id);
    var tip =$('#tip'+id);
    var bazoviy_edin =$('#bazoviy_edin'+id);
    var status =$('#status'+id);
    var zavod =$('#zavod'+id);
    var buxgalter_uchot =$('#buxgalter_uchot'+id);
    var alter_edin =$('#alter_edin'+id);
    var stoimost_baza =$('#stoimost_baza'+id);
    var stoimost_alter =$('#stoimost_alter'+id);
    var obshiy_ves_shtuku =$('#obshiy_ves_shtuku'+id);
    var segment =$('#segment'+id);
    var buxgalter_tovar =$('#buxgalter_tovar'+id);
    var comment =$('#comment'+id);
    var obshiy_ves_shtuku =$('#obshiy_ves_shtuku'+id);
    var pickupdate =$('#pickupdate'+id);
    var sena_c_nds =$('#sena_c_nds'+id);
    var sena_bez_nds =$('#sena_bez_nds'+id);
    var diller =$('#diller'+id);
    var tip_clenta =$('#tip_clenta'+id);
    
    comment.css('display','none')
    obshiy_ves_shtuku.css('display','none')
    pickupdate.css('display','none')
    sena_c_nds.css('display','none')
    sena_bez_nds.css('display','none')
    diller.css('display','none')
    tip_clenta.css('display','none')
    // var zavod_name =$('#zavod_name'+id)
    // zavod_name.text('')


    svet_product.css('display','none')
    group_zakup.css('display','none')
    group.css('display','none')
    tip.css('display','none')
    bazoviy_edin.css('display','none')
    status.css('display','none')
    zavod.css('display','none')
    buxgalter_uchot.css('display','none')
    alter_edin.css('display','none')
    stoimost_baza.css('display','none')
    stoimost_alter.css('display','none')
    segment.css('display','none')
    buxgalter_tovar.css('display','none')
    sap_code_ruchnoy.css('border-color','#dedad9')
    kratkiy_tekst_ruchnoy.css('border-color','#dedad9')
    sap_code_ruchnoy.attr('disabled',true)
    kratkiy_tekst_ruchnoy.attr('disabled',true)
    online_savdo_id.css('display','none')
    online_savdo_id.css('border-color','red')
    obshiy_ves_shtuku.css('display','none')
    nazvaniye_ruchnoy.css('display','none')
    nazvaniye_ruchnoy.css('border-color','red')


    svet_product.css('border-color','red')
    group_zakup.css('border-color','red')
    group.css('border-color','red')
    tip.css('border-color','red')
    bazoviy_edin.css('border-color','red')
    status.css('border-color','red')
    zavod.css('border-color','red')
    pickupdate.css('border-color','red')
    sena_c_nds.css('border-color','red')
    sena_bez_nds.css('border-color','red')
    tip_clenta.css('border-color','red')
    segment.css('border-color','red')

    
    diller.val('')
    tip_clenta.val('')
    sap_code_ruchnoy.val('')
    kratkiy_tekst_ruchnoy.val('')
    online_savdo_id.val('')
    nazvaniye_ruchnoy.val('')
    svet_product.val('')
    group_zakup.val('')
    group.val('')
    tip.val('')
    bazoviy_edin.val('')
    status.val('')
    // zavod.val('')
    buxgalter_uchot.val('')
    alter_edin.val('')
    stoimost_baza.val('')
    stoimost_alter.val('')
    obshiy_ves_shtuku.val('')
    segment.val('')
    buxgalter_tovar.val('')
    comment.val('')
    obshiy_ves_shtuku.val('')
    pickupdate.val('')
    sena_c_nds.val('')
    sena_bez_nds.val('')
    
    var create_btn =$('#create_btn'+id);
    var activate_btn =$('#activate_btn'+id);

    activate_btn.attr('disabled',false)
    create_btn.attr('disabled',false)

    activate_btn.css('background-color','')
    activate_btn.css('color','')
    create_btn.css('background-color','')
    create_btn.css('color','')

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

    

    var nakleyka_select = $('#nakleyka_select'+String(id));
    nakleyka_select.css('display','block');
    var nakleyka_nt1 = $('#nakleyka_nt1'+String(id));
    if(nakleyka_nt1.text()==''){
        set_nakleyka(nakleyka_list,'.kod_nakleyki'+id,value='',add=false)
        nadpis_nakleyki.text('')
        // nakleyka1
        $('#nakleyka'+id).find('.chosen-container').find('.chosen-single').css('border-color', 'red');
    }else{
        set_nakleyka(nakleyka_list,'.kod_nakleyki'+id,value='NT1',add=false)
        nadpis_nakleyki.text('Без наклейки')
        $('#nakleyka'+id).find('.chosen-container').find('.chosen-single').css('border-color', '#dedad9');
    }

    
    var is_active = $('#is_active'+String(id))
    
    var svet_product_val =''
    var gruppa_zakupok =''
    var diller =$('#diller'+id)
    var tip_clenta =$('#tip_clenta'+id)
    diller.css('display','block')
    tip_clenta.css('display','block')
    
  
    var iskyucheniye =$('#iskyucheniye'+id).text()
    
    if(String(val) == '1'){
        var kod_svet_zames = $('#kod_svet_zames'+String(id));
        kod_svet_zames.attr("disabled",false);
        kod_svet_zames.css("border-color",'#fc2003');
        if(is_active.text()!='Активный'){
            data_base[id] = new BasePokritiya()
        }
        data_base[id].id = 1;
        data_base[id].tip_pokritiya = 'Неламинированный';
        
        var artikul_pvc = $('#artikul_pvc'+String(id));
        data_base[id].artikul= artikul_pvc.text()

        svet_product_val = 'WHITE' 
        gruppa_zakupok ='PVX OQ (Navoiy)' 
        var kod_svet_rezini = $('#kod_svet_rezini'+String(id));
        kod_svet_rezini.val('')

       

        // $('#nakleyka'+id).find('.chosen-container').find('.chosen-single').css('border-color', 'red');
        
        if(iskyucheniye =='1'){
            data_base[id].is_iklyuch=true
            kod_svet_rezini.css('display','none');
            kod_svet_rezini.css('border-color','#dedad9')
        }else{
            data_base[id].is_iklyuch=false
            kod_svet_rezini.css('display','block');
        }
        
    }else if(String(val) == '2'){
        if(is_active.text()!='Активный'){
            data_base[id] = new BasePokritiya()
        }
        // data_base[id] = new BasePokritiya()
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
        // svet_lamplonka_vnutri.css("border-color",'#fc2003');

        if(iskyucheniye =='1'){
            kod_svet_rezini.css('display','none');
            data_base[id].is_iklyuch=true
        }else{
            kod_svet_rezini.css('display','block');
            data_base[id].is_iklyuch=false
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

    if(is_active.text()=='Активный' && String(val) != ''){
        
        var svet_product =$('#svet_product'+id);
        
        
        data_base[id].is_active=true

        var sap_code_ruchnoy =$('#sap_code_ruchnoy'+id);
        var kratkiy_tekst_ruchnoy =$('#kratkiy_tekst_ruchnoy'+id);
        var online_savdo_id =$('#online_savdo_id'+id);
        var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);
        var svet_product =$('#svet_product'+id);
        var group_zakup =$('#group_zakup'+id);
        var group =$('#group'+id);
        var tip =$('#tip'+id);
        var bazoviy_edin =$('#bazoviy_edin'+id);
        var status =$('#status'+id);
        var zavod =$('#zavod'+id);
        var buxgalter_uchot =$('#buxgalter_uchot'+id);
        var alter_edin =$('#alter_edin'+id);
        var stoimost_baza =$('#stoimost_baza'+id);
        var stoimost_alter =$('#stoimost_alter'+id);
        var obshiy_ves_shtuku =$('#obshiy_ves_shtuku'+id);
        var segment =$('#segment'+id);
        var buxgalter_tovar =$('#buxgalter_tovar'+id);
        var comment =$('#comment'+id);
        var pickupdate =$('#pickupdate'+id);
        var sena_c_nds =$('#sena_c_nds'+id);
        var sena_bez_nds =$('#sena_bez_nds'+id);
        comment.css('display','block')
        pickupdate.css('display','block')
        sena_c_nds.css('display','block')
        sena_bez_nds.css('display','block')
        
        
        
        
        sap_code_ruchnoy.css('display','block')
        kratkiy_tekst_ruchnoy.css('display','block')
        online_savdo_id.css('display','block')
        nazvaniye_ruchnoy.css('display','block')
        svet_product.css('display','block')
        group_zakup.css('display','block')
        group.css('display','block')
        tip.css('display','block')
        bazoviy_edin.css('display','block')
        status.css('display','block')
        zavod.css('display','block')
        buxgalter_uchot.css('display','block')
        alter_edin.css('display','block')
        stoimost_baza.css('display','block')
        stoimost_alter.css('display','block')
        segment.css('display','block')
        buxgalter_tovar.css('display','block')


        status.val('Активный')
        // status.attr('disabled',true)

        sap_code_ruchnoy.css('border-color','#dedad9')
        kratkiy_tekst_ruchnoy.css('border-color','#dedad9')
        online_savdo_id.css('border-color','#dedad9')
        nazvaniye_ruchnoy.css('border-color','#dedad9')
        svet_product.css('border-color','#dedad9')
        group_zakup.css('border-color','#dedad9')
        group.css('border-color','#dedad9')
        tip.css('border-color','#dedad9')
        bazoviy_edin.css('border-color','#dedad9')
        status.css('border-color','#dedad9')
        zavod.css('border-color','#dedad9')
        buxgalter_uchot.css('border-color','#dedad9')
        alter_edin.css('border-color','#dedad9')
        stoimost_baza.css('border-color','#dedad9')
        stoimost_alter.css('border-color','#dedad9')
        obshiy_ves_shtuku.css('border-color','#dedad9')
        segment.css('border-color','#dedad9')
        buxgalter_tovar.css('border-color','#dedad9')
        comment.css('border-color','#dedad9')
        pickupdate.css('border-color','#dedad9')
        sena_c_nds.css('border-color','#dedad9')
        sena_bez_nds.css('border-color','#dedad9')

    }else if(is_active.text()=='Пассивный' && String(val) != ''){
        
        data_base[id].is_active = false
        var svet_product =$('#svet_product'+id);
        var sap_code_ruchnoy =$('#sap_code_ruchnoy'+id);
        var kratkiy_tekst_ruchnoy =$('#kratkiy_tekst_ruchnoy'+id);
        var online_savdo_id =$('#online_savdo_id'+id);
        var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);
        var svet_product =$('#svet_product'+id);
        var group_zakup =$('#group_zakup'+id);
        var group =$('#group'+id);
        var tip =$('#tip'+id);
        var bazoviy_edin =$('#bazoviy_edin'+id);
        var status =$('#status'+id);
        var zavod =$('#zavod'+id);
        var buxgalter_uchot =$('#buxgalter_uchot'+id);
        var alter_edin =$('#alter_edin'+id);
        var stoimost_baza =$('#stoimost_baza'+id);
        var stoimost_alter =$('#stoimost_alter'+id);
        var obshiy_ves_shtuku =$('#obshiy_ves_shtuku'+id);
        var segment =$('#segment'+id);
        var buxgalter_tovar =$('#buxgalter_tovar'+id);
        var comment =$('#comment'+id);
        var obshiy_ves_shtuku =$('#obshiy_ves_shtuku'+id);
        var pickupdate =$('#pickupdate'+id);
        var sena_c_nds =$('#sena_c_nds'+id);
        var sena_bez_nds =$('#sena_bez_nds'+id);
        comment.css('display','block')
        obshiy_ves_shtuku.css('display','block')
        pickupdate.css('display','block')
        sena_c_nds.css('display','block')
        sena_bez_nds.css('display','block')
        
        
        
        buxgalter_uchot.val('Килограмм')
        bazoviy_edin.val('Штука')
        alter_edin.val('Килограмм')
        stoimost_baza.val('1')
        
        

        sap_code_ruchnoy.css('display','block')
        kratkiy_tekst_ruchnoy.css('display','block')
        online_savdo_id.css('display','block')
        nazvaniye_ruchnoy.css('display','block')
        svet_product.css('display','block')
        group_zakup.css('display','block')
        group.css('display','block')
        tip.css('display','block')
        bazoviy_edin.css('display','block')
        status.css('display','block')
        zavod.css('display','block')
        buxgalter_uchot.css('display','block')
        alter_edin.css('display','block')
        stoimost_baza.css('display','block')
        stoimost_alter.css('display','block')
        obshiy_ves_shtuku.css('display','block')
        segment.css('display','block')
        buxgalter_tovar.css('display','block')
        
        svet_product.val(svet_product_val)
        tip.val('Готовый продукт')
        group_zakup.val(gruppa_zakupok)
        status.val('Пассивный')
        // status.attr('disabled',true)

        online_savdo_id.css('border-color','#dedad9')
        tip_clenta.css('border-color','#dedad9')

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


var zapros_count ={}


function create_kratkiy_tekst(id){
    if(!data_base[id]){
        console.log('salom')
    }else{
    
        // console.log(id,'sssssss')
    var kratkiy_tekst = $('#kratkiy_tekst'+String(id));
    var combination= $('#combination'+String(id));
    combination_text = combination.text();
    var comment= $('#comment'+String(id));
    comment = comment.val();
    var is_active =$('#is_active'+id)
    var val = $('#tip_pokritiya'+String(id)).val();
    var dlina = $('#length'+String(id));

    if(comment!=''){
        data_base[id].comment = comment;
    }else{
        data_base[id].comment = NaN;
    }
   
    if(dlina.val()!=''&& dlina.val()!=0 && dlina.val()!='0'){
        dlina.css("border-color",'#dedad9');
        data_base[id].dlina = dlina.val().slice(0,4);
    }else{
        if(is_active.text()=='Активный'){
            dlina.css("border-color",'#dedad9');
        }else{
            dlina.css("border-color",'red');
        }
        data_base[id].dlina = NaN;
    }
    
    var kod_svet_zames = $('#kod_svet_zames'+String(id));
    if(kod_svet_zames){
        if(kod_svet_zames.val()!='0' && kod_svet_zames.val()!='' && kod_svet_zames.val()!=null){
            kod_svet_zames.css("border-color",'#dedad9');
            data_base[id].kod_svet_zames = kod_svet_zames.val()
        }else{
            data_base[id].kod_svet_zames = NaN;
            if(is_active.text()=='Активный'){
                kod_svet_zames.css("border-color",'#dedad9');
            }else{

                kod_svet_zames.css("border-color",'red');
            }
        }
    }
    
    
    var iskyucheniye =$('#iskyucheniye' +id).text()

    if(iskyucheniye =='1'){

        var kod_svet_rezini =$('#kod_svet_rezini' + id);
        if(kod_svet_rezini.val()!=''&&kod_svet_rezini.val()){
            var svet_rezin =$('#svet_rezin' + id);
            var selectedText = $("#kod_svet_rezini"+id + " option:selected").text();
            svet_rezin.text(kod_svet_rezini.val())
            kod_svet_rezini.css('border-color','#dedad9')
            data_base[id].kod_svet_rezini =selectedText;
            data_base[id].svet_rezin =kod_svet_rezini.val();
        }else{
            var svet_rezin =$('#svet_rezin' + id);
            svet_rezin.text('')
            data_base[id].kod_svet_rezini = NaN
            data_base[id].svet_rezin = NaN;
        }
        
    }else{
        
        var kod_svet_rezini =$('#kod_svet_rezini' + id);
        if(kod_svet_rezini.val()!=''&&kod_svet_rezini.val()){
            var svet_rezin =$('#svet_rezin' + id);
            var selectedText = $("#kod_svet_rezini"+id + " option:selected").text();
            svet_rezin.text(kod_svet_rezini.val())
            kod_svet_rezini.css('border-color','#dedad9')
            data_base[id].kod_svet_rezini =selectedText;
            data_base[id].svet_rezin =kod_svet_rezini.val();
        }else{
            var svet_rezin =$('#svet_rezin' + id);
            svet_rezin.text('')
            kod_svet_rezini.css('border-color','red')
            data_base[id].kod_svet_rezini = NaN
            data_base[id].svet_rezin = NaN;
        }
    }


    var value_nak = $('.kod_nakleyki'+String(id))
    var nadpis_nakleyki = $('#nadpis_nakleyki'+String(id));
    
    var value_nak_1 = $('.kod_nakleyki'+String(id) +' option:selected')
    var nadpiss_ = value_nak_1.attr('data-nadpis')
    console.log('nakkkkkk >>>>> ',value_nak.val())
    if(value_nak.val() !='' && value_nak.val()!=null && value_nak.val()!=undefined ){
        // value_nak.css('border-color','#dedad9');
        $('#nakleyka'+id).find('.chosen-container').find('.chosen-single').css('border-color', '#dedad9');
        data_base[id].kod_nakleyki = value_nak.val();
        data_base[id].nadpis_nakleyki = nadpiss_
        nadpis_nakleyki.text(nadpiss_)
        
    }else{
        nadpis_nakleyki.text('')
        // value_nak.css('border-color','red');
        $('#nakleyka'+id).find('.chosen-container').find('.chosen-single').css('border-color', 'red');
        data_base[id].kod_nakleyki = NaN
        data_base[id].nadpis_nakleyki = NaN;
    }

    if(String(val) == '2'){     
        var code_lamplonka_snaruji = document.getElementById('code_lamplonka_snaruji'+String(id))//.innerText;
        
        if(code_lamplonka_snaruji.innerText !=''){
            $('#svet_lamplonka_snaruji'+String(id)).css('border-color','#dedad9');//.innerText;
            var svet_lamplonka_snaruji = $('#svet_lamplonka_snaruji'+String(id)+' option:selected')//.innerText;
            data_base[id].kod_lam_sn = code_lamplonka_snaruji.innerText;
            data_base[id].svet_lamplonka_snaruji = svet_lamplonka_snaruji.text();
        }else{
            if(is_active.text()=='Активный'){
                $('#svet_lamplonka_snaruji'+String(id)).css('border-color','#dedad9');//.innerText;
            }else{
                $('#svet_lamplonka_snaruji'+String(id)).css('border-color','red');//.innerText;
            }
            data_base[id].kod_lam_sn = NaN;
            data_base[id].svet_lamplonka_snaruji = NaN;
        }
        
        var code_lamplonka_vnutri = document.getElementById('code_lamplonka_vnutri'+String(id));
        

        if(code_lamplonka_vnutri.innerText !=''){
            $('#svet_lamplonka_vnutri'+String(id)).css('border-color','#dedad9');//.innerText;
            var svet_lamplonka_vnutri = $('#svet_lamplonka_vnutri'+String(id)+' option:selected')//.innerText;
            data_base[id].kod_lam_vn =code_lamplonka_vnutri.innerText;
            data_base[id].svet_lamplonka_vnutri =svet_lamplonka_vnutri.text();
        }else{
            if(is_active.text()=='Активный'){
                $('#svet_lamplonka_vnutri'+String(id)).css('border-color','#dedad9');//.innerText;
            }else{
                $('#svet_lamplonka_vnutri'+String(id)).css('border-color','red');//.innerText;
            }
            data_base[id].kod_lam_vn =NaN;
        }

        
        

    }

    if(is_active.text()=='Активный'){
        val = 3
    }

    if(String(val) != ''){

        var sap_code_ruchnoy =$('#sap_code_ruchnoy'+id);
        var kratkiy_tekst_ruchnoy =$('#kratkiy_tekst_ruchnoy'+id);
        var online_savdo_id =$('#online_savdo_id'+id);
        var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);
        var svet_product =$('#svet_product'+id);
        var group_zakup =$('#group_zakup'+id);
        var group =$('#group'+id);
        var tip =$('#tip'+id);
        var bazoviy_edin =$('#bazoviy_edin'+id);
        var status =$('#status'+id);
        var zavod =$('#zavod_name'+id);
        var nazvaniye_system =$('.nazvaniye_system'+id).text();
        
        var segment =$('#segment'+id)
        var buxgalter_tovar =$('#buxgalter_tovar'+id).val();
        var buxgalter_uchot =$('#buxgalter_uchot'+id).val();
        var alter_edin =$('#alter_edin'+id).val();
        var stoimost_baza =$('#stoimost_baza'+id).val();
        var stoimost_alter =$('#stoimost_alter'+id).val();
        var obshiy_ves_shtuku =$('#obshiy_ves_shtuku'+id).val();
       
        if(obshiy_ves_shtuku!=''){
            data_base[id].obshiy_ves_shtuku = obshiy_ves_shtuku;
        }else{
            data_base[id].obshiy_ves_shtuku = NaN;
        }
        if(nazvaniye_system!=''){
            data_base[id].nazvaniye_system = nazvaniye_system;
        }else{
            data_base[id].nazvaniye_system = NaN;
        }
        if(stoimost_alter!=''){
            data_base[id].stoimost_alter = stoimost_alter;
        }else{
            data_base[id].stoimost_alter = NaN;
        }
        if(stoimost_baza!=''){
            data_base[id].stoimost_baza = stoimost_baza;
        }else{
            data_base[id].stoimost_baza = NaN;
        }
        if(alter_edin!=''){
            data_base[id].alter_edin = alter_edin;
        }else{
            data_base[id].alter_edin = NaN;
        }
        if(buxgalter_uchot!=''){
            data_base[id].buxgalter_uchot = buxgalter_uchot;
        }else{
            data_base[id].buxgalter_uchot = NaN;
        }
        
        if(buxgalter_tovar!=''){
            data_base[id].buxgalter_tovar = buxgalter_tovar;
        }else{
            data_base[id].buxgalter_tovar = NaN;
        }


        var comment =$('#comment'+id);
        var pickupdate =$('#pickupdate'+id);
        var sena_c_nds =$('#sena_c_nds'+id);
        var sena_bez_nds =$('#sena_bez_nds'+id);
        var diller =$('#diller'+id)
        var tip_clenta =$('#tip_clenta'+id)
        
        
        
        
        if(is_active.text()=='Активный'){
            if(segment.val()!=''){
                segment.css('border-color','#dedad9')
                data_base[id].segment = segment.val();
            }else{
                segment.css('border-color','#dedad9')
                data_base[id].segment = NaN;
            }

            if(tip_clenta.val()!=''){
                data_base[id].tip_clenta = tip_clenta.val();
                tip_clenta.css('border-color','#dedad9')
            }else{
                tip_clenta.css('border-color','#dedad9')
                data_base[id].tip_clenta = NaN;
            }
            if(diller.val()!=''){
                data_base[id].diller = diller.val();
                diller.css('border-color','#dedad9')
            }else{
                data_base[id].diller = NaN;
            }

            if(sena_bez_nds.val()!=''){
                data_base[id].sena_bez_nds = sena_bez_nds.val();
                sena_bez_nds.css('border-color','#dedad9')
            }else{
                data_base[id].sena_bez_nds = NaN;
            }
            if(sena_c_nds.val()!=''){
                data_base[id].sena_c_nds = sena_c_nds.val();
                sena_c_nds.css('border-color','#dedad9')
            }else{
                data_base[id].sena_c_nds = NaN;
            }
            if(pickupdate.val()!=''){
                data_base[id].pickupdate = pickupdate.val();
                pickupdate.css('border-color','#dedad9')
            }else{
                data_base[id].pickupdate = NaN;
            }
            
            if(comment.val()!=''){
                data_base[id].comment = comment.val();
                comment.css('border-color','#dedad9')
            }else{
                data_base[id].comment = NaN;
            }
   
            if(sap_code_ruchnoy.val()!=''){
                data_base[id].sap_code = sap_code_ruchnoy.val();
                sap_code_ruchnoy.css('border-color','#dedad9')
            }else{
                sap_code_ruchnoy.css('border-color','red')
                data_base[id].sap_code = NaN;
                
            }
            if(kratkiy_tekst_ruchnoy.val()!=''){
                data_base[id].krat = kratkiy_tekst_ruchnoy.val();
                kratkiy_tekst_ruchnoy.css('border-color','#dedad9')
                
            }else{
                kratkiy_tekst_ruchnoy.css('border-color','red')
                data_base[id].krat = NaN;
                
            }
            if(online_savdo_id.val()!=''&& online_savdo_id.val()!=0 && online_savdo_id.val()!='0'){
                online_savdo_id.css('border-color','#dedad9')
                data_base[id].online_id = online_savdo_id.val();
            }else{
                data_base[id].online_id = NaN;
                online_savdo_id.css('border-color','red')
            }
            if(nazvaniye_ruchnoy.val()!=''){
                nazvaniye_ruchnoy.css('border-color','#dedad9')
                data_base[id].nazvaniye_ruchnoy = removeQuotesFromStartAndEnd(nazvaniye_ruchnoy.val());
            }else{
                data_base[id].nazvaniye_ruchnoy =NaN;
                nazvaniye_ruchnoy.css('border-color','red')
            }
    
    
            if(svet_product.val()!=''){
                
                data_base[id].svet_product = svet_product.val();
            }else{
                data_base[id].svet_product =NaN;
               
            }
            if(group_zakup.val()!=''){
                
                data_base[id].group_zakup = group_zakup.val();
            }else{
                data_base[id].group_zakup =NaN;
            }
            if(group.val()!=''){
                
                data_base[id].group = group.val();
            }else{
                data_base[id].group =NaN;
                
            }
            if(tip.val()!=''){
                
                data_base[id].tip = tip.val();
            }else{
                data_base[id].tip =NaN;
                
            }
            if(bazoviy_edin.val()!=''){
                
                data_base[id].bazoviy_edin = bazoviy_edin.val();
            }else{
                data_base[id].bazoviy_edin =NaN;
                
            }
            
            if(status.val()!=''){
                
                data_base[id].status_online = status.val();
            }else{
                data_base[id].status_online =NaN;
                
            }
            
            data_base[id].zavod_name = 'ZAVOD PVS NAVOIY';
            
        }else{
            if(segment.val()!=''){
                segment.css('border-color','#dedad9')
                data_base[id].segment = segment.val();
            }else{
                segment.css('border-color','red')
                data_base[id].segment = NaN;
            }
            if(tip_clenta.val()!=''){
                data_base[id].tip_clenta = tip_clenta.val();
                tip_clenta.css('border-color','#dedad9')
            }else{
                tip_clenta.css('border-color','red')
                data_base[id].tip_clenta = NaN;
            }
            if(diller.val()!=''){
                data_base[id].diller = diller.val();
                diller.css('border-color','#dedad9')
            }else{
                data_base[id].diller = NaN;
            }
            if(sena_bez_nds.val()!=''){
                data_base[id].sena_bez_nds = sena_bez_nds.val();
                sena_bez_nds.css('border-color','#dedad9')
            }else{
                sena_bez_nds.css('border-color','red')
                data_base[id].sena_bez_nds = NaN;
            }

            if(sena_c_nds.val()!=''){
                data_base[id].sena_c_nds = sena_c_nds.val();
                sena_c_nds.css('border-color','#dedad9')
            }else{
                sena_c_nds.css('border-color','red')
                data_base[id].sena_c_nds = NaN;
            }
            if(pickupdate.val()!=''){
                data_base[id].pickupdate = pickupdate.val();
                pickupdate.css('border-color','#dedad9')
            }else{
                pickupdate.css('border-color','red')
                data_base[id].pickupdate = NaN;
            }
            
            if(comment.val()!=''){
                data_base[id].comment = comment.val();
                comment.css('border-color','#dedad9')
            }else{
                data_base[id].comment = NaN;
            }

            if(sap_code_ruchnoy.val()!=''){
                data_base[id].sap_code = sap_code_ruchnoy.val();
                sap_code_ruchnoy.css('border-color','#dedad9')
            }else{
                data_base[id].sap_code = NaN;
            }


            if(kratkiy_tekst_ruchnoy.val()!=''){
                data_base[id].krat = kratkiy_tekst_ruchnoy.val();
                kratkiy_tekst_ruchnoy.css('border-color','#dedad9')
            }else{
                data_base[id].krat = NaN;
            }
            if(online_savdo_id.val()!=''&& online_savdo_id.val()!=0 && online_savdo_id.val()!='0'){
                
                data_base[id].online_id = online_savdo_id.val();
            }else{
                data_base[id].online_id = NaN;
                
            }
            if(nazvaniye_ruchnoy.val()!=''){
                nazvaniye_ruchnoy.css('border-color','#dedad9')
                data_base[id].nazvaniye_ruchnoy = removeQuotesFromStartAndEnd(nazvaniye_ruchnoy.val());
            }else{
                data_base[id].nazvaniye_ruchnoy =NaN;
                nazvaniye_ruchnoy.css('border-color','red')
            }
    
    
            if(svet_product.val()!=''){
                svet_product.css('border-color','#dedad9')
                data_base[id].svet_product = svet_product.val();
            }else{
                data_base[id].svet_product =NaN;
                svet_product.css('border-color','red')
            }
            if(group_zakup.val()!=''){
                group_zakup.css('border-color','#dedad9')
                data_base[id].group_zakup = group_zakup.val();
            }else{
                data_base[id].group_zakup =NaN;
                group_zakup.css('border-color','red')
            }
            if(group.val()!=''){
                group.css('border-color','#dedad9')
                data_base[id].group = group.val();
            }else{
                data_base[id].group =NaN;
                group.css('border-color','red')
            }
            if(tip.val()!=''){
                tip.css('border-color','#dedad9')
                data_base[id].tip = tip.val();
            }else{
                data_base[id].tip =NaN;
                tip.css('border-color','red')
            }
            if(bazoviy_edin.val()!=''){
                bazoviy_edin.css('border-color','#dedad9')
                data_base[id].bazoviy_edin = bazoviy_edin.val();
            }else{
                data_base[id].bazoviy_edin =NaN;
                bazoviy_edin.css('border-color','red')
            }
            
            if(status.val()!=''){
                status.css('border-color','#dedad9')
                data_base[id].status_online = status.val();
            }else{
                data_base[id].status_online =NaN;
                status.css('border-color','red')
            }
            data_base[id].zavod_name = 'ZAVOD PVS NAVOIY';
        }
        
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
        var artikul_bass = data_base[id].base_artikul
        var art_krat_dict = artikul_bass + data.text
        var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
        var kratkiy_text_ruchnoy = $('#kratkiy_tekst_ruchnoy'+id)
        

        if(art_krat_dict in zapros_count){
            if(zapros_count[art_krat_dict]){
                var sap_code = zapros_count[art_krat_dict]
                sap_code_ruchnoy.val(sap_code)
                kratkiy_text_ruchnoy.val(data.text)
                sap_code_ruchnoy.css('background-color','#eaecef')
                kratkiy_text_ruchnoy.css('background-color','#eaecef')
                // sap_code_ruchnoy.attr('disabled',true)
                // kratkiy_text_ruchnoy.attr('disabled',true)
            }else{
                
                sap_code_ruchnoy.val('')
                kratkiy_text_ruchnoy.val('')
                sap_code_ruchnoy.css('background-color','#eaecef')
                kratkiy_text_ruchnoy.css('background-color','#eaecef')
                // sap_code_ruchnoy.attr('disabled',false)
                // kratkiy_text_ruchnoy.attr('disabled',false)
            }
            
        }else{
            sap_codes = get_sapcode(id,data_base[id].base_artikul,data.text)
        }
        data_base[id].kratkiy_tekst= data.text
    }else{
        if(is_active.text()!='Активный'){
            var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
            var kratkiy_text_ruchnoy = $('#kratkiy_tekst_ruchnoy'+id)
            sap_code_ruchnoy.val('')
            kratkiy_text_ruchnoy.val('')
            sap_code_ruchnoy.css('background-color','#eaecef')
            kratkiy_text_ruchnoy.css('background-color','#eaecef')
        }
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
            // sap_code_ruchnoy.attr('disabled',true)
            // kratkiy_text_ruchnoy.attr('disabled',true)
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
            // sap_code_ruchnoy.attr('disabled',false)
            // kratkiy_text_ruchnoy.attr('disabled',false)
        }
        // WON'T REDIRECT
    });
}








