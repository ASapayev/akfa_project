class BasePokritiya{
    constructor(
        full=false,//done
        id=NaN,//done
        nazvaniye_system=NaN,//done
        base_artikul=NaN,//done
        dlina=NaN,//done
        tip_pokritiya=NaN,//done
        splav=NaN,//done
        tip_zak=NaN,//done
        combination=NaN,//done
        brend_kraska_sn=NaN,//done
        kod_kraska_sn=NaN,//done
        brend_kraska_vn=NaN,//done
        kod_kraska_vn=NaN,//done
        kod_dekor_sn=NaN,//done
        svet_dekplonka_snaruji=NaN,//done
        kod_dekor_vn=NaN,//done
        svet_dekplonka_vnutri=NaN,//done
        svet_lamplonka_snaruji=NaN,//done
        kod_lam_sn=NaN,//done
        svet_lamplonka_vnutri=NaN,//done
        kod_lam_vn=NaN,//done
        kod_anod_sn=NaN,//done 1425
        kod_anod_vn=NaN,//done
        contactnost_anod=NaN,//done
        tip_anod=NaN,//done
        sposob_anod=NaN,//done
        kod_nakleyki=NaN,//done
        nadpis_nakleyki=NaN,
        baza_profiley=NaN,
        gruppa_materialov=NaN,
        kratkiy_tekst=NaN,//done
        sap_code=NaN,//done
        krat=NaN,//done
        nazvaniye_ruchnoy =NaN,
        comment=NaN,
        dilina_pressa =NaN,
        is_termo=false
        ) {

        this.full=full;
        this.id=id;
        this.nazvaniye_system=nazvaniye_system;
        this.base_artikul=base_artikul;
        this.dlina=dlina;
        this.tip_pokritiya=tip_pokritiya;
        this.splav=splav;
        this.tip_zak=tip_zak;
        this.combination=combination;
        this.brend_kraska_sn=brend_kraska_sn;
        this.kod_kraska_sn=kod_kraska_sn;
        this.brend_kraska_vn=brend_kraska_vn;
        this.kod_kraska_vn=kod_kraska_vn;
        this.kod_dekor_sn=kod_dekor_sn;
        this.svet_dekplonka_snaruji=svet_dekplonka_snaruji;
        this.kod_dekor_vn=kod_dekor_vn;
        this.svet_dekplonka_vnutri=svet_dekplonka_vnutri;
        this.svet_lamplonka_snaruji=svet_lamplonka_snaruji;
        this.kod_lam_sn=kod_lam_sn;
        this.svet_lamplonka_vnutri=svet_lamplonka_vnutri;
        this.kod_lam_vn=kod_lam_vn;
        this.kod_anod_sn=kod_anod_sn;
        this.kod_anod_vn=kod_anod_vn;
        this.contactnost_anod=contactnost_anod;
        this.tip_anod=tip_anod;
        this.sposob_anod=sposob_anod;
        this.kod_nakleyki=kod_nakleyki;
        this.nadpis_nakleyki=nadpis_nakleyki;
        this.baza_profiley=baza_profiley;
        this.gruppa_materialov=gruppa_materialov;
        this.kratkiy_tekst=kratkiy_tekst;
        this.sap_code=sap_code;
        this.krat=krat;
        this.nazvaniye_ruchnoy=nazvaniye_ruchnoy;
        this.comment=comment;
        this.dilina_pressa =dilina_pressa;
        this.is_termo=is_termo;
        this.result=''
      
    }
    get_kratkiy_tekst(){
        if(this.splav){
            this.result = this.splav.slice(2);
        }else{
            this.result =''
        }
        switch(this.id){
            case 1:if(!this.is_termo){
           
                    if(this.splav && this.tip_zak && this.dlina && this.kod_kraska_sn && this.kod_nakleyki ){
                        if(this.nazvaniye_ruchnoy && this.dilina_pressa){

                            return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':false}
                        }
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }else{
                    if(this.splav && this.tip_zak && this.dlina && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki){
                        if(this.nazvaniye_ruchnoy && this.dilina_pressa){

                            return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.kod_kraska_sn +'/'+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.kod_kraska_sn +'/'+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':false}

                        }
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }break;
            case 2:if(!this.is_termo){

                if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_nakleyki ){
                    if(this.nazvaniye_ruchnoy && this.dilina_pressa){

                        return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':true}
                    }else{
                        return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':false}
                        
                    }
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
        
                    if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki ){
                        if(this.nazvaniye_ruchnoy && this.dilina_pressa){
                            return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':true}
                            
                        }else{
                            return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':false}
                            
                        }
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }break;
            case 3: if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_nakleyki){
                    if(this.nazvaniye_ruchnoy && this.dilina_pressa){

                        return  {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':true}
                    }else{
                        return  {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':false}
                        
                    }
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
                
                    if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki){
                        if(this.nazvaniye_ruchnoy && this.dilina_pressa){

                            return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn+'/'+this.brend_kraska_vn+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn+'/'+this.brend_kraska_vn+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':false}
                            
                        }
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }break;
            case 4: if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki ){
                    if(this.nazvaniye_ruchnoy && this.dilina_pressa){

                        return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':true}
                    }else{
                        return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':false}
                        
                    }
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
                    if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki ){
                        if(this.nazvaniye_ruchnoy && this.dilina_pressa){

                            return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn + this.kod_kraska_vn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn + this.kod_kraska_vn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':false}
                            
                        }
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }break;
            case 5:if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_dekor_sn && this.kod_nakleyki){
                    if(this.nazvaniye_ruchnoy && this.dilina_pressa){
                        return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_dekor_sn + ' ' +this.kod_nakleyki,'accept':true}
                        
                    }else{
                        return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_dekor_sn + ' ' +this.kod_nakleyki,'accept':false}
                        
                    }
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
                    if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_dekor_sn && this.kod_dekor_vn){
                        if(this.nazvaniye_ruchnoy && this.dilina_pressa){

                            return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+'_'+this.kod_dekor_sn+'/'+this.kod_dekor_vn + ' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+'_'+this.kod_dekor_sn+'/'+this.kod_dekor_vn + ' ' +this.kod_nakleyki,'accept':false}
                            
                        }
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }break;
            case 6:if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.kod_anod_sn && this.kod_nakleyki && this.contactnost_anod){
                    if(this.nazvaniye_ruchnoy && this.dilina_pressa){

                        return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.kod_anod_sn + ' ' + this.contactnost_anod + ' ' + this.kod_nakleyki,'accept':true}
                    }else{
                        return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.kod_anod_sn + ' ' + this.contactnost_anod + ' ' + this.kod_nakleyki,'accept':false}
                        
                    }
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
                    if(this.splav && this.tip_zak && this.dlina && this.kod_anod_sn && this.kod_anod_vn && this.kod_nakleyki && this.contactnost_anod){
                        if(this.nazvaniye_ruchnoy && this.dilina_pressa){

                            return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.kod_anod_sn +'/'+this.kod_anod_vn+ ' ' + this.contactnost_anod + ' ' + this.kod_nakleyki,'accept':true}
                        }else{
                            
                            return {'text':this.result + this.tip_zak + ' L' + this.dlina +' ' + this.kod_anod_sn +'/'+this.kod_anod_vn+ ' ' + this.contactnost_anod + ' ' + this.kod_nakleyki,'accept':false}
                        }
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
        
                }break;
        }
    }
  }

  



var nakleyka_list = document.getElementById('nakleyka_list').outerHTML

function front_piece(start=1,end=6){
    text =""
    for (let i = start; i < end; i++) {

        nakleyki = nakleyka_list.replace('nakleyka_list',"nakleyka"+String(i))
        nakleyki = nakleyki.replace('onchange=""','onchange="create_kratkiy_tekst('+String(i)+')"')
    

        text +=`
        <tr id='table_tr` +String(i)+`' style='padding-bottom:0!important;margin-bottom:0!important;'>
                                    
         <td  class="sticky-col"   style='left:0; padding-right:5px; background-color:white!important;'>
                    <div class="btn-group" role="group" aria-label="Basic example">
                            <button type="button" class="btn btn-outline-secondary btn-sm" id='clear_btn`+String(i)+`' onclick="artukil_clear(`+String(i)+`)" data-bs-toggle='popover' title='Tozalab tashlash'><i class="bi bi-x-circle"></i></button>
                            <button type="button" class="btn btn-outline-secondary btn-sm"  onclick="copy_tr(`+String(i)+`)" data-bs-toggle='popover' title='Dubl qilish'><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-copy" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M4 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 5a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-1h1v1a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h1v1z"/></svg></button>
                    </div>
                    
                    

        </td>
        <td class="sticky-col" style=' left: 73.5px;background-color:white!important;width:100px!important'>
            <div class="input-group input-group-sm mb-1" style='width:100%'>
                <span class ='text-center nazvaniye_system` +String(i)+`'style="text-transform: uppercase;font-size: 14px;width:100px!important;white-space: nowrap;"></span>
            </div>
        </td>
        <td class="sticky-col"  style=' left: 183.2px; background-color:white!important' >
            <div class="input-group input-group-sm mb-1">
                <select class=" form-control" style="background-color:#ddebf7; width: 140px; font-size:10px;padding-right:150px!important;" id="artikul`+String(i)+`" ></select>
                <span style='display:none' id ='nakleyka_codd` +String(i)+`'></span>
            </div>
        </td>
        
        
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type="text" pattern="\d{0,4}"  maxlength="4"  class="form-control " style='width:70px;height:27px!important;z-index:0' oninput="restrictToFourDigits(event,`+String(i)+`)"  disabled aria-describedby="inputGroup-sizing-sm" name ='length`+String(i)+`' id="length`+String(i)+`"  >
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 165px;text-transform: uppercase; font-size:12px; padding-right:0px;height:27px!important;z-index:0" onchange="tip_pokritiya_selected(`+String(i)+`,this.value)" disabled id='tip_pokritiya`+String(i)+`' required>
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
            <div class="input-group input-group-sm mb-1" style="width: 70px;">
        
            <select class="form-select" aria-label="" style="width: 70px;height:27px!important;z-index:0"  disabled id='splav`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)">
                
                <option value="" selected  ></option>
                <option value="6060" >6060</option>
                <option value="6063" >6063</option>
                <option value="6082" >6082</option>
                <option value="6005" >6005</option>
                <option value="6005A" >6005A</option>
                <option value="6061" >6061</option>
            </select>
            
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1"  style="width: 60px;">
            <select class="form-select" aria-label="" style="width: 50px;!important;height:27px!important;z-index:0" disabled  id='tip_zakalyonnosti`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option value="" selected ></option>
                <option value="T4" >T4</option>
                <option value="T5" >T5</option>
                <option value="T6" >T6</option>
                <option value="T42" >T42</option>
                <option value="T52" >T52</option>
                <option value="T61" >T61</option>
                <option value="T66" >T66</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" style="font-size: small; text-transform: uppercase; width:130px">
                <div>
                    <span class =' text-center pl-1' style="font-size: small; text-transform: uppercase;z-index:0" id ='combination` +String(i)+`'></span>
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" >
            <select class="form-select form-select-sm text-center"  style="width:65px;border-color:#fc2003;display:none;height:27px!important;z-index:0" id='brand_k_snaruji`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)" required>
                <option  value="" selected></option>
                <option value="A">A</option>
                <option value="B">B</option>
                <option value="R">R</option>
                <option value="T">T</option>
                <option value="J">J</option>
                <option value="P">P</option>
                <option value="M">M</option>
                <option value="X">X</option>
            </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 100px;display:none" id='div_kras_sn`+String(i)+`'>
            <select class="form-select form-select-sm text-center code_kraski_snar_sel`+String(i)+`"  style="width:150px;border-color:#fc2003;height:27px!important;z-index:0"  id='code_kraski_snar`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)" required data-placeholder="..."></select>
           
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select form-select-sm text-center"  style="width:65px;border-color:#fc2003;display:none;height:27px!important;z-index:0" id='brand_k_vnutri`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)" required>
                <option  value="" selected></option>
                <option value="A">A</option>
                <option value="B">B</option>
                <option value="R">R</option>
                <option value="T">T</option>
                <option value="J">J</option>
                <option value="P">P</option>
                <option value="M">M</option>
                <option value="X">X</option>
            </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 100px;display:none" id='div_kras_vn`+String(i)+`'>
             <select class="form-select form-select-sm text-center code_kraski_vnut_sel`+String(i)+`"  style="width:100px;border-color:#fc2003;display:none;height:27px!important;z-index:0" id='code_kraski_vnut`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)" data-placeholder="..." required> </select>
            
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">    
            <select class="form-select" aria-label="" style="width: 75px;height:27px!important;z-index:0" onchange="svet_dekplonka_snaruji_selected(`+String(i)+`,this.value)"  id='svet_dekplonka_snaruji`+String(i)+`' disabled>
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
                    <em><span class =' text-center ' style="font-size: 10px;  font-weight: bold; text-transform: uppercase;z-index:0" id ='code_dekplonka_snaruji` +String(i)+`' disabled ></span></em>
                </div>
            </div>
        </td>
       

        

        <td >
            <div class="input-group input-group-sm mb-1"  >    
            <select class="form-select" aria-label="" style="width: 75px;height:27px!important;z-index:0" onchange="svet_dekplonka_vnutri_selected(`+String(i)+`,this.value)"  id='svet_dekplonka_vnutri`+String(i)+`' disabled>
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
                <em><span class =' text-center ' style="font-size: 10px;  font-weight: bold; text-transform: uppercase;z-index:0" id ='code_dekplonka_vnutri` +String(i)+`' disabled ></span></em>
                </div>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">    
            <select class="form-select" aria-label="" style="width: 220px;height:27px!important;z-index:0" onchange="svet_lamplonka_snaruji_selected(`+String(i)+`,this.value)" disabled id='svet_lamplonka_snaruji`+String(i)+`'>
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
                <option value="1001">Метбраш Алюмин</option>
                <option value="5001">Кремвейс</option>
                <option value="6062">Матовый чёрный</option>
                <option value="6030">Матовый белый</option>
                <option value="1015">Алюкс алюмин</option>
                <option value="2025">Светлый дуб</option>
                <option value="1022">Ocean Blue</option>
                <option value="XXXX">XXXX</option>
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
                    <option value="1001">Метбраш Алюмин</option>
                    <option value="5001">Кремвейс</option>
                    <option value="6062">Матовый чёрный</option>
                    <option value="6030">Матовый белый</option>
                    <option value="1015">Алюкс алюмин</option>
                    <option value="2025">Светлый дуб</option>
                    <option value="1022">Ocean Blue</option>
                    <option value="XXXX">XXXX</option>
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
            <div class="input-group input-group-sm mb-1" style="width: 75px;">
            <div id='anod`+String(i)+`' class='anood'  style="width: 75px;border-color:red; display:none;" >
                <select class="form-select kod_anod_snar`+String(i)+`" aria-label="" style=" width: 100px; border-color:#fc2003;!important;height:27px!important;z-index:0" onchange="code_svet_anodirovki_snaruji_selected(`+String(i)+`,this.value)"  id='code_svet_anodirovki_snaruji`+String(i)+`' required></select>         
            </div>            
            </div>
        </td> 
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 75px;">
            <div id='anod_vnutr`+String(i)+`'  style="width: 75px;display:none;border-color:red;">
                <select class="form-select kod_anod_vnutri`+String(i)+`" aria-label="" style="width: 75px;border-color:#fc2003;margin-right:15px;height:27px!important;z-index:0" onchange="create_kratkiy_tekst(`+String(i)+`)"  id='code_svet_anodirovki_vnutr`+String(i)+`' required></select>       
            </div>
            </div>
        </td> 
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 60px;">
            <select class="form-select" aria-label=""  style='height:27px!important;z-index:0' disabled id='contactnost_anodirovki`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option  value=""></option>
                <option value="YC" >YC</option>
                <option value="NC">NC</option>
            </select>
            </div>
        </td>
        <td style='display:none' >
            <div class="input-group input-group-sm mb-1">
            <div>
                <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;z-index:0" id='tip_anodirovki`+String(i)+`'></span>
            </div>
            </div>
        </td>
        <td style='display:none' >
            <div class="input-group input-group-sm mb-1">
            <div>
                <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;z-index:0" id='sposob_anodirovki`+String(i)+`'></span>
            </div>
            </div>
        </td>
        <td >`
        text +=nakleyki

        text += `
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <span  class='text-center' style="font-size: small; width:150px; font-weight: bold; text-transform: uppercase;z-index:0" id='nadpis_nakleyki`+String(i)+`'></span>
            </div>
        </td>
        <td >
        <span  style="font-size: small; width:150px; font-weight: bold; text-transform: uppercase;z-index:0;white-space:nowrap;" id='baza_profiley`+String(i)+`'></span>
        </td>
        <td >
            <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;z-index:0" id='gruppa_materialov`+String(i)+`'>ALUGP</span>   
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <span  style="font-size: small; width:300px; font-weight: bold; text-transform: uppercase;z-index:0;white-space: nowrap;" id='kratkiy_tekst`+String(i)+`'></span>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type="text" class="form-control "  style='width:150px;height:27px!important;z-index:0'   aria-describedby="inputGroup-sizing-sm" disabled  id="sap_code`+String(i)+`"  onchange="create_kratkiy_tekst(`+String(i)+`)">           
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type="text" class="form-control "  style='width:250px;height:27px!important;z-index:0'   aria-describedby="inputGroup-sizing-sm" disabled  id="krat`+String(i)+`" onchange="create_kratkiy_tekst(`+String(i)+`)" >
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type='text' class=" form-control " style="border-color:red; width: 250px; font-size:10px; height:27px!important;z-index:0;display:none;"  id='nazvaniye_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type='text' class=" form-control " style="width: 250px; font-size:10px; height:27px!important;z-index:0"  id='comment`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type="text" pattern="\d{0,4}"  maxlength="4"  class="form-control " style='width:90px;height:27px!important;z-index:0;border-color:red;display:none;' oninput="restrictToFourDigits(event,`+String(i)+`)"   aria-describedby="inputGroup-sizing-sm" name ='dilina_pressa`+String(i)+`' id="dilina_pressa`+String(i)+`"  >
     
            </div>
        </td>
        </tr>`
    }
    return text
}

text = front_piece()

var table = $('#table-artikul')

table.append(text)



function request_piece(start=1,end=6){
    for (let i = start; i <=end; i++) {
        $('#artikul'+String(i)).select2({
            ajax: {
                url: "/client/imzo-artikul-list",
                dataType: 'json',
                processResults: function(data){
                    return {results: $.map(data, function(item){
                        return {id:item.id,text:item.data['Артикул'],system:item.data['Система'],combination:item.data['Комбинация'],code_nakleyka:item.data['Код наклейки'],baza_profiley:item.data['BAZA']}
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
            data.forEach(function(dataItem) {

                var option = new Option(dataItem['Артикул'], data['id'], true, true);
                artikulSelect.append(option).trigger('change');
            
                artikulSelect.trigger({
                    type: 'select2:select',
                    params: {
                        data: dataItem
                    }
                });
            })
        });
        
        
        $("#artikul"+String(i)).on("select2:select", function (e) { 
        var select_val = $(e.currentTarget).val();
        var nazvaniye_system =$('.nazvaniye_system'+String(i));
        var combination = $('#combination'+String(i));
        var tip_pokritiya = $('#tip_pokritiya'+String(i));
        var baza_profiley = $('#baza_profiley'+String(i));
        // tip_pokritiya.val('').change();
        tip_pokritiya.attr("disabled",false);
        nazvaniye_system.text(e.params.data.system);
        combination.text(e.params.data.combination)
        baza_profiley.text(e.params.data.baza_profiley)

        var nakleyka_kode = e.params.data.code_nakleyka
        
        $('.select2-selection__rendered').css('font-size', '15px');
        
        
        var length = $('#length'+String(i));
        length.attr('required',true)
        var splav = $('#splav'+String(i));
        splav.attr('required',true)
        var tip_zakalyonnosti = $('#tip_zakalyonnosti'+String(i));
        tip_zakalyonnosti.attr('required',true)

        var nakleyka = $('#nakleyka'+String(i))
        var nadpis_nakleyki = $('#nadpis_nakleyki'+String(i))
    
        if (nakleyka_kode =='NT1'){
            nakleyka.css('display','block')
            nakleyka.val('NT1')
            nadpis_nakleyki.text('Без наклейки')
        }
        else if( nakleyka_kode !=''){
            var nakleyka_codd = $('#nakleyka_codd'+String(i))
            nakleyka_codd.text(nakleyka_kode)
            if(!data_base[i]){
               
                nakleyka.css('display','block')
                nakleyka.val(nakleyka_kode)
                var selectedOption = $('#nakleyka'+String(i)).find('option:selected');

                var nadpisValue = selectedOption.data('nadpis');
                nadpis_nakleyki.text(nadpisValue)
            }else{
                console.log('222 com')
                var pokritiya = data_base[i].id
                if(pokritiya == 1 || pokritiya =='1'){
                    console.log('222 com 222','pokrrr1')
                    nakleyka.css('display','block')
                    nakleyka.val('NT1')
                    nadpis_nakleyki.text('БЕЗ НАКЛЕЙКИ')
                }else{
                    nakleyka.css('display','block')
                    nakleyka.val(nakleyka_kode)
                    var selectedOption = $('#nakleyka'+String(i)).find('option:selected');
        
                    var nadpisValue = selectedOption.data('nadpis');
                    nadpis_nakleyki.text(nadpisValue)
                }
            }


        }        
        else{

            nakleyka.val('')
        }
        
        if(data_base[i]){
            clear_artikul(i)
        }
        
        // console.log(e.params.data.system)
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
        var base_artikul = data.base_artikul;
        var dlina = data.dlina;
        var splav = data.splav;
        var tip_zak = data.tip_zak;
        var combination = data.combination;
        var brend_kraska_sn = data.brend_kraska_sn;
        var kod_kraska_sn = data.kod_kraska_sn;
        var brend_kraska_vn = data.brend_kraska_vn;
        var kod_kraska_vn = data.kod_kraska_vn;
        var kod_dekor_sn = data.kod_dekor_sn;
        var svet_dekplonka_snaruji = data.svet_dekplonka_snaruji;
        var kod_dekor_vn = data.kod_dekor_vn;
        var svet_dekplonka_vnutri = data.svet_dekplonka_vnutri;

        var svet_lamplonka_snaruji = data.svet_lamplonka_snaruji;
        var kod_lam_sn = data.kod_lam_sn;
        var svet_lamplonka_vnutri = data.svet_lamplonka_vnutri;
        var kod_lam_vn = data.kod_lam_vn;


        var kod_anod_sn = data.kod_anod_sn;
        var kod_anod_vn = data.kod_anod_vn;


        var contactnost_anod = data.contactnost_anod;
        var tip_anod = data.tip_anod;
        var sposob_anod = data.sposob_anod;

        var kod_nakleyki = data.kod_nakleyki;
        var nadpis_nakleyki = data.nadpis_nakleyki;
        var baza_profiley = data.baza_profiley;
        
        

        var kratkiy_tekst = data.kratkiy_tekst;

        var sap_code = data.sap_code;
        var krat = data.krat;
        
        var nazvaniye_ruchnoy = data.nazvaniye_ruchnoy
        var dilina_pressa = data.dilina_pressa

        var comment = data.comment;

        var is_termo_bas = data.is_termo;

       
      
      
        
      
        
        check_input_and_change(id,'#tip_pokritiya'+s)

        var div_kras_sn = $('#div_kras_sn'+String(s))
        var div_kras_vn = $('#div_kras_vn'+String(s))

        

        if(id ==1){
            chosen_update('.code_kraski_snar_sel'+String(s),val_=kod_kraska_sn,disabled=true)
            div_kras_sn.css('display','block')
            check_input_and_change(kod_nakleyki,'#nakleyka'+s,dis=true)
            if(is_termo_bas){
                chosen_update('.code_kraski_vnut_sel'+String(s),val_=kod_kraska_vn,disabled=true)
                div_kras_vn.css('display','block')
            }
        }else if(id == 2){    
                check_input_and_change(brend_kraska_sn,'#brand_k_snaruji'+s,dis=true)
                chosen_update('.code_kraski_snar_sel'+String(s),val_=kod_kraska_sn,disabled=true)
                div_kras_sn.css('display','block')
                check_input_and_change(kod_nakleyki,'#nakleyka'+s)
                if(is_termo_bas){
                    check_input_and_change(brend_kraska_vn,'#brand_k_vnutri'+s,dis=true)
                    chosen_update('.code_kraski_vnut_sel'+String(s),val_=kod_kraska_vn,disabled=true)
                    div_kras_vn.css('display','block')
                }
        }else if(id ==3){
            
            check_input_and_change(brend_kraska_sn,'#brand_k_snaruji'+s,dis=false,is_req=true)
            chosen_update('.code_kraski_snar_sel'+String(s),val_=kod_kraska_sn,disabled=false)
            div_kras_sn.css('display','block')
            check_input_and_change(kod_nakleyki,'#nakleyka'+s)

            if(is_termo_bas){
                check_input_and_change(brend_kraska_vn,'#brand_k_vnutri'+s,dis=false,is_req=true)
                chosen_update('.code_kraski_vnut_sel'+String(s),val_=kod_kraska_vn,disabled=false)
                div_kras_vn.css('display','block')
            }
        }
        else if(id ==4){
            
            check_input_and_change(brend_kraska_sn,'#brand_k_snaruji'+s,dis=false,is_req=true)
            chosen_update('.code_kraski_snar_sel'+String(s),val_=kod_kraska_sn,disabled=false)
            div_kras_sn.css('display','block')

            check_input_and_change(kod_lam_sn,'#svet_lamplonka_snaruji'+s,dis=false,is_req=true)
            check_text_and_change(kod_lam_sn,'#code_lamplonka_snaruji'+s,dis=false,is_req=true)

            check_input_and_change(kod_lam_vn,'#svet_lamplonka_vnutri'+s,dis=false,is_req=true)
            check_text_and_change(kod_lam_vn,'#code_lamplonka_vnutri'+s,dis=false,is_req=true)
            check_input_and_change(kod_nakleyki,'#nakleyka'+s)
            if(is_termo_bas){
                check_input_and_change(brend_kraska_vn,'#brand_k_vnutri'+s,dis=false,is_req=true)
                chosen_update('.code_kraski_vnut_sel'+String(s),val_=kod_kraska_vn,disabled=false)
                div_kras_vn.css('display','block')
            }

        }
        else if(id ==5){
            
            check_input_and_change(brend_kraska_sn,'#brand_k_snaruji'+s,dis=false,is_req=true)
            chosen_update('.code_kraski_snar_sel'+String(s),val_=kod_kraska_sn,disabled=false)
            div_kras_sn.css('display','block')

            check_input_and_change(svet_dekplonka_snaruji,'#svet_dekplonka_snaruji'+s,dis=false,is_req=true)
            check_text_and_change(svet_dekplonka_snaruji,'#code_dekplonka_snaruji'+s,dis=false,is_req=true)

            check_input_and_change(kod_nakleyki,'#nakleyka'+s)

            if(is_termo_bas){
                check_input_and_change(brend_kraska_vn,'#brand_k_vnutri'+s,dis=false,is_req=true)
                chosen_update('.code_kraski_vnut_sel'+String(s),val_=kod_kraska_vn,disabled=false)
                div_kras_vn.css('display','block')

                check_input_and_change(svet_dekplonka_vnutri,'#svet_dekplonka_vnutri'+s,dis=false,is_req=true)
                check_text_and_change(svet_dekplonka_vnutri,'#code_dekplonka_vnutri'+s,dis=false,is_req=true)
            }

        }
        else if(id ==6){
            
            get_anod(s)

            
            check_for_valid_and_set_val_select(s,kod_anod_sn,'code_svet_anodirovki_snaruji'+ s,is_req=true,is_anod=true,is_termo=false)

            check_input_and_change(contactnost_anod,'#contactnost_anodirovki'+s,dis=false,is_req=true)

            check_input_and_change(kod_nakleyki,'#nakleyka'+s)

            if(is_termo_bas){
                get_anod(s,is_termo=true,copy=true)
                check_for_valid_and_set_val_select2(s,kod_anod_vn,'code_svet_anodirovki_vnutri'+ s,is_req=true)
            }


        }

       
        check_input_and_change(dlina,'#length'+s,dis=false,is_req=true)
        check_for_valid_and_set_val_select(s,base_artikul,'artikul'+ s,is_req=true,is_anod=false)
        check_input_and_change(splav,'#splav'+s,dis=false,is_req=true)
        check_input_and_change(tip_zak,'#tip_zakalyonnosti'+s,dis=false,is_req=true)
        check_text_and_change(combination,'#combination'+s)
        check_text_and_change(nazvaniye_system,'.nazvaniye_system'+s)
        
        
        check_text_and_change(nadpis_nakleyki,'#nadpis_nakleyki'+s)
        check_text_and_change(baza_profiley,'#baza_profiley'+s)
        

        // check_input_and_change(tex_name,'#goods_group'+s)
        // check_text_and_change(tex_name,'#tex_name'+s)
        
        check_text_and_change(kratkiy_tekst,'#kratkiy_tekst'+s)

        check_input_and_change(sap_code,'#sap_code'+s,dis=true)
        check_input_and_change(krat,'#krat'+s,dis=true)



       
        check_input_and_change(comment,'#comment'+s)
        check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s,dis=false,is_req=true)
        check_input_and_change(dilina_pressa,'#dilina_pressa'+s,dis=false,is_req=true)
        
        
    }


}

function removeQuotesFromStartAndEnd(str) {
    // Remove double quotes from the beginning and end of the string
    return str.replace(/^"+|"+$/g, '');
}

function chosen_update(selector,val_,disabled=false){

    set_brend_kraska(brend_kaska,selector,val_=val_)
    if(disabled){
        $(selector).prop('disabled', true).trigger('chosen:updated')
    }else{
        $(selector).prop('disabled', false).trigger('chosen:updated')
    }
}


function check_for_valid_and_set_val_select(i,val,selector,is_req=false,is_anod=false){
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

        if(is_anod){
            const spanss =document.querySelector('#anod'+String(i) +' .select2-container .select2-selection--single')
            spanss.style.borderColor='#dedad9'
        }

        //////end ////////////
        
    }
}

function check_for_valid_and_set_val_select2(i,val,selector,is_req=false){
    if(is_req){
        var span = $('#select2-'+selector+'-container')
        span.css('display','block')
        span.css('border-color','red')

    }
    if(is_anod){
        console.log(val,selector)
    }
    
    if(val !=NaN && val !='' && String(val) != 'NaN'){
        ////// selec2 value change \\\\\\\
        var span = $('#select2-'+selector+'-container')
        span.attr('title',val);
        span.text(val);
        console.log(val,'anodddddd22222')
        const spanss =document.querySelector('#anod_vnutr'+String(i) +' .select2-container .select2-selection--single')
        spanss.style.borderColor='#dedad9'
        
        //////end ////////////
        
    }
}

function check_input_and_change(val,selector,dis=false,is_req=false){
    if(is_req){
        
        $(selector).attr('disabled',false)
        $(selector).css('display','block')
        $(selector).css('border-color','red')

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

function add_column(){
        
    text =""
    var sizeee = $('#table-artikul tr').length;
    
    text = front_piece(start = sizeee+1, end = sizeee+2)

    
    var table = $('#table-artikul')
    table.append(text)
    
    

    request_piece(start = sizeee+1, end = sizeee+2)


}


function get_anod(id,termo=false,copy=false){
    $('#anod'+id).css('display','block')
    if(copy){
        if(termo){
            $('#anod_vnutr'+id).css('display','block')
            $('.kod_anod_vnutri'+id).select2({
                ajax: {
                    url: "/client/client-anod-list",
                    dataType: 'json',
                    processResults: function(data){
                        return {results: $.map(data, function(item){
                            return {id:item.id,text:item.code_sveta,tip_anod:item.tip_anod,sposob_anod:item.sposob_anod}
                        })
                    };
                    }
                }
                });
        }else{
            $('.kod_anod_snar'+id).select2({
                ajax: {
                    url: "/client/client-anod-list",
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
    }else{
        $('.kod_anod_snar'+id).select2({
            ajax: {
                url: "/client/client-anod-list",
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
            $('#anod_vnutr'+id).css('display','block')
            $('.kod_anod_vnutri'+id).select2({
                ajax: {
                    url: "/client/client-anod-list",
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
}


function clear_artikul(id){
    if(data_base[id]){
        var is_termo = data_base[id].is_termo
        var base_artikul =$('#select2-artikul'+id+'-container').text()
        var nazvaniye_system = $('.nazvaniye_system'+id).text()
        var combination =$('#combination'+id).text()
        var baza_profiley =$('#baza_profiley'+id).text()
       
        
        console.log(combination,'ggggg')

        data_base[id].base_artikul = base_artikul
        data_base[id].nazvaniye_system = nazvaniye_system
        data_base[id].combination = combination
        data_base[id].baza_profiley = baza_profiley

        
        var sss= combination.toUpperCase() == 'БЕЗ ТЕРМОМОСТА'
    
        if (sss){
            var second_is_termo = false
        }else{
            var second_is_termo = true
        }

        if(is_termo != second_is_termo){


            var table_tr =$('#table_tr'+id);
            // table_tr.remove()
            // $('#artikul'+id).val(null).trigger('change');
            // $('.nazvaniye_system'+id).text('');
            var tip_pokritiya = $('#tip_pokritiya'+String(id));
            tip_pokritiya.val('0').change();
            // var select_nakleyka = $('#nakleyka'+String(id));
            // select_nakleyka.children("span").remove();
            // select_nakleyka.children("select").remove();
            delete data_base[id]

            var kratkiy_tekst = document.getElementById('kratkiy_tekst'+String(id));
            kratkiy_tekst.innerText="";


            
            
            table_tr.css('background-color','white')
            

            var code_kraski_snaruji = $('#code_kraski_snar'+String(id));
            var code_kraski_vnutri = $('#code_kraski_vnut'+String(id));
            var brand_kraski_vnutri = $('#brand_k_vnutri'+String(id))
            var brand_kraski_snaruji = $('#brand_k_snaruji'+String(id))
            code_kraski_snaruji.val("");
            code_kraski_vnutri.val("");
            brand_kraski_vnutri.val("");
            brand_kraski_snaruji.val("");

            code_kraski_snaruji.css("border-color",'#dedad9');
            code_kraski_vnutri.css("border-color",'#dedad9');
            brand_kraski_vnutri.css("border-color",'#dedad9');
            brand_kraski_snaruji.css("border-color",'#dedad9');



            var dlina =$('#length'+String(id));
            dlina.val('');
            dlina.attr("disabled",true);
            dlina.css("border-color",'#dedad9');

            // var combination= document.getElementById('combination'+String(id));
            // console.log(combination,'dddd',combination.innerText)
            // combination.innerText='';
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

            var nakleyka_codd = $('#nakleyka_codd'+String(id)).text()
            var nadpis_nakleyki = $('#nadpis_nakleyki'+String(id))

            if(nakleyka_codd != ''){
                var nakleyka = $('#nakleyka'+String(id))
                nakleyka.css('display','block')
                nakleyka.attr('disabled',false)
                nakleyka.val(nakleyka_codd)

                var selectedOption = $('#nakleyka'+String(id)).find('option:selected');
                var nadpisValue = selectedOption.data('nadpis');
                nadpis_nakleyki.text(nadpisValue)
            }else{
                var nakleyka = $('#nakleyka'+String(id))
                nakleyka.css('display','block')
                nakleyka.attr('disabled',false)
                nakleyka.val('')

                var selectedOption = $('#nakleyka'+String(id)).find('option:selected');
                var nadpisValue = selectedOption.data('nadpis');
                nadpis_nakleyki.text(nadpisValue)

            }
            


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
    }
}

function artukil_clear(id){
    $('#artikul'+id).val(null).trigger('change');
    var table_tr =$('#table_tr'+id);
    $('.nazvaniye_system'+id).text('');
    var tip_pokritiya = $('#tip_pokritiya'+String(id));
    tip_pokritiya.val('0').change();
    tip_pokritiya.attr("disabled",true);
    delete data_base[id]

    var kratkiy_tekst = document.getElementById('kratkiy_tekst'+String(id));
    kratkiy_tekst.innerText="";

    
    
    table_tr.css('background-color','white')
    

    var code_kraski_snaruji = $('#code_kraski_snar'+String(id));
    var code_kraski_vnutri = $('#code_kraski_vnut'+String(id));
    var brand_kraski_vnutri = $('#brand_k_vnutri'+String(id))
    var brand_kraski_snaruji = $('#brand_k_snaruji'+String(id))
    code_kraski_snaruji.val("");
    code_kraski_vnutri.val("");
    brand_kraski_vnutri.val("");
    brand_kraski_snaruji.val("");

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

    var nakleyka = $('#nakleyka'+String(id))
    nakleyka.css('display','none')
    nakleyka.val('')
    


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
    var goods_group = $('#goods_group'+String(id));
    var tex_name = $('#tex_name'+String(id));
    var id_klaes =$('#id_klaes'+String(id))
    var klaes_nazvaniye =$('#klaes_nazvaniye'+String(id))
    var code_sveta =$('#code_sveta'+String(id))
    var klaes_kratkiy =$('#klaes_kratkiy'+String(id))
    var sap_code =$('#sap_code'+String(id))
    var krat =$('#krat'+String(id))
    var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+String(id))
    var dilina_pressa =$('#dilina_pressa'+String(id))


    sap_code.css('background-color','#eaecef')
    krat.css('background-color','#eaecef')
   

    nazvaniye_ruchnoy.text('')
    tex_name.text('')
    krat.val('')
    sap_code.val('')
    goods_group.val('0').change();
    id_klaes.val('')
    klaes_nazvaniye.val('')
    code_sveta.val('')
    klaes_kratkiy.val('')
    goods_group.css('border-color','red')
    nazvaniye_ruchnoy.css('display','none')
    dilina_pressa.css('display','none')
    id_klaes.css('border-color','red')
    klaes_nazvaniye.css('border-color','red')
    code_sveta.css('border-color','red')
    klaes_kratkiy.css('border-color','red')
}


function tip_pokritiya_selected(id,val){

    var element33 = document.getElementById("table_tr"+id);
    element33.style.backgroundColor='white';

    
    
    var select_anod_snar = $('#anod'+String(id));
    select_anod_snar.children("span").css('display','none');

    var dlina =$('#length'+String(id));
    dlina.attr("disabled",false);
    dlina.css("border-color",'#fc2003');

    var select_anod_vnut = $('#anod_vnutr'+String(id));
    select_anod_vnut.children("span").css('display','none');
    
    var select_snar = $('.code_kraski_snar_sel'+String(id))
    var select_vnut = $('.code_kraski_vnut_sel'+String(id))
    var hasOption_snar = select_snar.find('option').length > 0;
    var hasOption_vnut = select_vnut.find('option').length > 0;

    if(hasOption_snar){
        set_brend_kraska(brend_kaska,'.code_kraski_snar_sel'+String(id),val_='',add=false)
    }else{
        set_brend_kraska(brend_kaska,'.code_kraski_snar_sel'+String(id),val_='',add=true)
    }
    if(hasOption_vnut){
        set_brend_kraska(brend_kaska,'.code_kraski_vnut_sel'+String(id),val_='',add=false)
    }else{
        set_brend_kraska(brend_kaska,'.code_kraski_vnut_sel'+String(id),val_='',add=true)
    }

    var brand_k_snaruji = $('#brand_k_snaruji'+id)
    var brand_k_vnutri = $('#brand_k_vnutri'+id)

    brand_k_snaruji.val('')
    brand_k_vnutri.val('')

    brand_k_snaruji.css('display','none')
    brand_k_vnutri.css('display','none')



    
    var div_kras_sn = $('#div_kras_sn'+String(id))
    div_kras_sn.css('display','none')

    var div_kras_vn = $('#div_kras_vn'+String(id))
    div_kras_vn.css('display','none')


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


    var obj_exists = true

    if(data_base[id]){
        obj_exists =true
    }else{
        obj_exists =false
    }


    var tip_anodirovki =$('#tip_anodirovki'+String(id));
    var sposob_anodirovki = $('#sposob_anodirovki'+String(id));
    
    tip_anodirovki.text("");
    sposob_anodirovki.text("")
    var nakleyka = $('#nakleyka'+String(id))


    if(String(val) == '1'){
         

        nakleyka.css('display','block');
        nakleyka.val("NT1");

        if (combination_text.toUpperCase() == 'БЕЗ ТЕРМОМОСТА'){
            set_brend_kraska(brend_kaska,'.code_kraski_snar_sel'+String(id),val_='MF',add=false)
            
            $('.code_kraski_snar_sel'+String(id)).prop('disabled', true).trigger('chosen:updated')
            var div_kras = $('#div_kras_sn'+String(id))
            div_kras.css('display','block')
            brand_k_snaruji.val('')
            // code_kraski_snaruji.css('border-color','#dedad9')
        }else{
            set_brend_kraska(brend_kaska,'.code_kraski_snar_sel'+String(id),val_='MF',add=false)
            set_brend_kraska(brend_kaska,'.code_kraski_vnut_sel'+String(id),val_='MF',add=false)
            
            $('.code_kraski_snar_sel'+String(id)).prop('disabled', true).trigger('chosen:updated')
            var div_kras = $('#div_kras_sn'+String(id))
            div_kras.css('display','block')

            $('.code_kraski_vnut_sel'+String(id)).prop('disabled', true).trigger('chosen:updated')
            var div_kras = $('#div_kras_vn'+String(id))
            div_kras.css('display','block')
            
            brand_k_snaruji.val('')
            brand_k_vnutri.val('')
        }

        data_base[id] = new BasePokritiya()
        data_base[id].id = 1;
        data_base[id].tip_pokritiya = 'Неокрашенный'

    }else if(String(val) == '2'){
        
        if (combination_text.toUpperCase() == 'БЕЗ ТЕРМОМОСТА'){
            
            var brand_kraski_snaruji = $('#brand_k_snaruji'+String(id))
            set_brend_kraska(brend_kaska,'.code_kraski_snar_sel'+String(id),val_='9016',add=false)
            
        
            $('.code_kraski_snar_sel'+String(id)).prop('disabled', true).trigger('chosen:updated')
            var div_kras = $('#div_kras_sn'+String(id))
            div_kras.css('display','block')

            brand_kraski_snaruji.val('R');
            brand_kraski_snaruji.attr('disabled',true)
            brand_kraski_snaruji.css('display','block')
            brand_kraski_snaruji.css('border-color','#dedad9')
        }else{

            set_brend_kraska(brend_kaska,'.code_kraski_snar_sel'+String(id),val_='9016',add=false)
            set_brend_kraska(brend_kaska,'.code_kraski_vnut_sel'+String(id),val_='9016',add=false)
            
            $('.code_kraski_snar_sel'+String(id)).prop('disabled', true).trigger('chosen:updated')
            var div_kras = $('#div_kras_sn'+String(id))
            div_kras.css('display','block')

            $('.code_kraski_vnut_sel'+String(id)).prop('disabled', true).trigger('chosen:updated')
            var div_kras = $('#div_kras_vn'+String(id))
            div_kras.css('display','block')

           
            var brand_kraski_vnutri = $('#brand_k_vnutri'+String(id))
            var brand_kraski_snaruji = $('#brand_k_snaruji'+String(id))

            brand_kraski_snaruji.val('R');
            brand_kraski_snaruji.attr('disabled',true)
            brand_kraski_snaruji.css('display','block')
            brand_kraski_snaruji.css('border-color','#dedad9')

            

            brand_kraski_vnutri.val('R');
            brand_kraski_vnutri.attr('disabled',true)
            brand_kraski_vnutri.css('display','block')
            brand_kraski_vnutri.css('border-color','#dedad9')

            

        }

        data_base[id] = new BasePokritiya()
        data_base[id].id = 2;
        data_base[id].tip_pokritiya = 'Белый'
        
        
        var nakleyka_codd = $('#nakleyka_codd'+String(id)).text()
        if(nakleyka_codd!=''){
            nakleyka.val(nakleyka_codd)
        }
            
    }else if(String(val) == '3' || String(val) == '4'|| String(val) == '5'){

        
        var brand_kraski_vnutri = $('#brand_k_snaruji'+String(id));
        brand_kraski_vnutri.attr('disabled',false)
        brand_kraski_vnutri.css('display','block')
        
        set_brend_kraska(brend_kaska,'.code_kraski_snar_sel'+String(id),val_='',add=false)
        

        $('.code_kraski_snar_sel'+String(id)).prop('disabled', false).trigger('chosen:updated')
        var div_kras = $('#div_kras_sn'+String(id))
        div_kras.css('display','block')
       
        
        
        
        var nakleyka_codd = $('#nakleyka_codd'+String(id)).text()
        if(nakleyka_codd!=''){
            nakleyka.val(nakleyka_codd)
        }
       

        if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА'){
            
            var brand_kraski_vnutri = $('#brand_k_vnutri'+String(id));
            brand_kraski_vnutri.attr('disabled',false)
            brand_kraski_vnutri.css('display','block')
            set_brend_kraska(brend_kaska,'.code_kraski_vnut_sel'+String(id),val_='',add=false)
            
            $('.code_kraski_vnut_sel'+String(id)).prop('disabled', false).trigger('chosen:updated')
            var div_kras = $('#div_kras_vn'+String(id))
            div_kras.css('display','block')


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
        

        if(String(val) == '3'){
            data_base[id] = new BasePokritiya()
            data_base[id].id = 3;
            data_base[id].tip_pokritiya = 'Окрашенный'
        }else if(String(val) == '4'){
            data_base[id] = new BasePokritiya()
            data_base[id].id = 4;
            data_base[id].tip_pokritiya = 'Ламинированный'
        }else if(String(val) == '5'){
            data_base[id] = new BasePokritiya()
            data_base[id].id = 5;
            data_base[id].tip_pokritiya = 'Сублимированный'
        } 
        
    }else if(String(val) == '6'){
        data_base[id] = new BasePokritiya()
        data_base[id].id = 6;
        data_base[id].tip_pokritiya = 'Анодированный'
        

        if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА'){
           
            get_anod(id,termo=true)

            var code_svet_anodirovki_vnutri = $('#code_svet_anodirovki_vnutri'+String(id));
            code_svet_anodirovki_vnutri.attr("disabled",false);
            code_svet_anodirovki_vnutri.attr("required",true);
            code_svet_anodirovki_vnutri.css("border-color",'#fc2003');

        }else{
            get_anod(id,termo=false)
            
        }

        

        var contactnost_anodirovki = $('#contactnost_anodirovki'+String(id));
        console.log(contactnost_anodirovki)
        contactnost_anodirovki.attr("disabled",false);
        contactnost_anodirovki.attr("required",true);
        contactnost_anodirovki.css("border-color",'red');

        
        var nakleyka_codd = $('#nakleyka_codd'+String(id)).text()
        if(nakleyka_codd!=''){
            nakleyka.val(nakleyka_codd)
        }
        
        
        
    }
    if(String(val) !=''){

        var nazvaniye_system =$('.nazvaniye_system'+id)
        var splav =$('#splav'+id)
        var tip_zakalyonnosti =$('#tip_zakalyonnosti'+id)
        var combination =$('#combination'+id)
        var base_artikul =$('#select2-artikul'+id+'-container')
        var baza_profiley =$('#baza_profiley'+id)
        var gruppa_materialov =$('#gruppa_materialov'+id)
        var dilina_pressa =$('#dilina_pressa'+id)
        var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id)
        var comment =$('#comment'+id)
        data_base[id].baza_profiley = baza_profiley.text()
        data_base[id].gruppa_materialov = gruppa_materialov.text()
        data_base[id].comment = comment.val()
        
        var nadpis_nakleyki =$('#nadpis_nakleyki'+id)
        
        if(nadpis_nakleyki!=''){
            data_base[id].nadpis_nakleyki = nadpis_nakleyki.text()
        }
        
        data_base[id].base_artikul = base_artikul.text()
        data_base[id].nazvaniye_system = nazvaniye_system.text()
        data_base[id].splav = splav.val()
        data_base[id].tip_zakalyonnosti = tip_zakalyonnosti.val()
        data_base[id].combination = combination.text()

        var sap_code =$('#sap_code'+String(id))
        var krat =$('#krat'+String(id))
    
        krat.val('')
        sap_code.val('')
        sap_code.css('display','block')
        krat.css('display','block')
        nazvaniye_ruchnoy.val('')
        dilina_pressa.val('')
        dilina_pressa.css('display','block')
        nazvaniye_ruchnoy.css('display','block')
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


var zapros_count ={}

function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
    var kratkiy_tekst = $('#kratkiy_tekst'+String(id));
    var combination= $('#combination'+String(id));
    var comment= $('#comment'+String(id));
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
    if(comment.val()!=''){
        data_base[id].comment = comment.val();
    }else{
        data_base[id].comment = NaN;
    }
    var dilina_pressa = $('#dilina_pressa'+String(id));
    if(dilina_pressa.val()!=''){
        dilina_pressa.css("border-color",'#dedad9');
        data_base[id].dilina_pressa = dilina_pressa.val();
    }else{
        data_base[id].dilina_pressa = NaN;
        dilina_pressa.css("border-color",'red');
    }
    var nazvaniye_ruchnoy = $('#nazvaniye_ruchnoy'+String(id));
    if(nazvaniye_ruchnoy.val()!=''){
        nazvaniye_ruchnoy.css("border-color",'#dedad9');
        data_base[id].nazvaniye_ruchnoy = removeQuotesFromStartAndEnd(nazvaniye_ruchnoy.val());
    }else{
        data_base[id].nazvaniye_ruchnoy = NaN;
        nazvaniye_ruchnoy.css("border-color",'red');
    }

    var sap_code = $('#sap_code'+String(id));
   
    
    if(sap_code.val()!='0' && sap_code.val()!='' && sap_code.val()!=null){
        
        data_base[id].sap_code = sap_code.val();
    }else{
        
        data_base[id].sap_code = NaN;
    }
    
    var krat = $('#krat'+String(id));
   
    if(krat.val()!='0' && krat.val()!='' && krat.val()!=null){
        
        data_base[id].krat = krat.val();
    }else{
        
        data_base[id].krat = NaN;
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

    var nadpis_nakleyki = $('#nadpis_nakleyki'+String(id))

    if(String(val) == '1'){
            
            data_base[id].kod_kraska_sn = 'MF'
            data_base[id].kod_nakleyki = 'NT1'
            data_base[id].nadpis_nakleyki = 'Без наклейки'
            var nakleyka = $('#nakleyka'+String(id))
            nadpis_nakleyki.text('Без наклейки')
            nakleyka.attr('disabled',true)
            nakleyka.val('NT1')
        
         if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА')
            {
                
                data_base[id].kod_kraska_vn = 'MF'
                data_base[id].is_termo = true;
                
            }

    }else if(String(val) == '2'){
        data_base[id].brend_kraska_sn ='R'
        data_base[id].kod_kraska_sn ='9016'

        var nakleyka = $('#nakleyka'+String(id))
        nakleyka.attr('disabled',false)
        if(nakleyka.val()!=''){
            data_base[id].kod_nakleyki = nakleyka.val();
            var selectedOption = $('#nakleyka'+String(id)).find('option:selected');

            var nadpisValue = selectedOption.data('nadpis');
            nadpis_nakleyki.text(nadpisValue)
            nakleyka.css('border-color','#dedad9')
        }else{
            data_base[id].kod_nakleyki = NaN;
            nadpis_nakleyki.text('')
            nakleyka.css('border-color','red')
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
        if(brend_kraska_sn.val() != '0' && brend_kraska_sn.val()  != undefined && brend_kraska_sn.val() != '' && brend_kraska_sn.val()  !=null){
            brend_kraska_sn.css("border-color",'#dedad9');
            data_base[id].brend_kraska_sn =brend_kraska_sn.val();
        }else{
            brend_kraska_sn.css("border-color",'red');
            data_base[id].brend_kraska_sn =NaN;
        }
        
        var code_kraski_snaruji = $('#code_kraski_snar'+String(id));
        if(code_kraski_snaruji.val() != '0' && code_kraski_snaruji.val()  != undefined && code_kraski_snaruji.val() != '' && code_kraski_snaruji.val()  !=null){
            code_kraski_snaruji.css("border-color",'#dedad9');
            data_base[id].kod_kraska_sn =code_kraski_snaruji.val();
        }else{
            code_kraski_snaruji.css("border-color",'red');
            data_base[id].kod_kraska_sn =NaN;
        }
       
       


        if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА')
            {

                var brend_kraska_vn = $('#brand_k_vnutri'+String(id))
                if(brend_kraska_vn.val() != '0' && brend_kraska_vn.val()  != undefined  && brend_kraska_vn.val()  != ''  && brend_kraska_vn.val()  != null){
                    brend_kraska_vn.css("border-color",'#dedad9');
                    data_base[id].brend_kraska_vn =brend_kraska_vn.val();
                }else{
                    brend_kraska_vn.css("border-color",'red');
                    data_base[id].brend_kraska_vn =NaN;
                }

                var code_kraski_vnut = $('#code_kraski_vnut'+String(id))
               
                if((code_kraski_vnut.val() != '0') && (code_kraski_vnut.val()  != undefined)&&code_kraski_vnut.val()!=''){
                    
                    code_kraski_vnut.css("border-color",'#dedad9');
                    data_base[id].kod_kraska_vn =code_kraski_vnut.val();
                }else{
                    code_kraski_vnut.css("border-color",'red');
                    data_base[id].kod_kraska_vn =NaN;
                }
                
                data_base[id].is_termo =true;
                
            }



            var nakleyka = $('#nakleyka'+String(id))
        nakleyka.attr('disabled',false)
        if(nakleyka.val()!=''){
            data_base[id].kod_nakleyki = nakleyka.val();
            var selectedOption = $('#nakleyka'+String(id)).find('option:selected');

            var nadpisValue = selectedOption.data('nadpis');
            nadpis_nakleyki.text(nadpisValue)
            nakleyka.css('border-color','#dedad9')
        }else{
            data_base[id].kod_nakleyki = NaN;
            nadpis_nakleyki.text('')
            nakleyka.css('border-color','red')
        }

       
        if(String(val) == '4'){
            
            var code_lamplonka_snaruji = document.getElementById('code_lamplonka_snaruji'+String(id))//.innerText;
            
            if(code_lamplonka_snaruji.innerText !=''){
                var svet_lamplonka_snaruji = document.getElementById('svet_lamplonka_snaruji'+String(id))//.innerText;
                svet_lamplonka_snaruji.style.borderColor='#dedad9';
                data_base[id].kod_lam_sn =code_lamplonka_snaruji.innerText;;
                var code_lamplonka_sn = $('#svet_lamplonka_snaruji'+String(id)+' option:selected').text()
                data_base[id].svet_lamplonka_snaruji= code_lamplonka_sn;
            }else{
                data_base[id].kod_lam_sn =NaN;
                data_base[id].svet_lamplonka_snaruji= NaN;
            }
            
            var code_lamplonka_vnutri = document.getElementById('code_lamplonka_vnutri'+String(id));
           

            if(code_lamplonka_vnutri.innerText !=''){
                var svet_lamplonka_vnutri = document.getElementById('svet_lamplonka_vnutri'+String(id))//.innerText;
                svet_lamplonka_vnutri.style.borderColor='#dedad9';
                var code_lamplonka_vn = $('#svet_lamplonka_vnutri'+String(id)+' option:selected').text()
                data_base[id].svet_lamplonka_vnutri= code_lamplonka_vn;
                data_base[id].kod_lam_vn =code_lamplonka_vnutri.innerText;
            }else{
                data_base[id].kod_lam_vn =NaN;
                data_base[id].svet_lamplonka_vnutri= NaN;
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
                    var svet_dekplonka_snaruji = $('#code_dekplonka_snaruji'+id).text()
                    data_base[id].kod_dekor_sn =selectedText;
                    data_base[id].svet_dekplonka_snaruji =svet_dekplonka_snaruji;
                }else{
                    selectElement.style.borderColor='red';
                    data_base[id].svet_dekplonka_snaruji =NaN;
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
                        var svet_dekplonka_vnutri = $('#code_dekplonka_vnutri'+id).text()
                        data_base[id].svet_dekplonka_vnutri =svet_dekplonka_vnutri;
                        data_base[id].kod_dekor_vn =selectedText;
                    }else{
                        selectElement.style.borderColor='red';
                        data_base[id].kod_dekor_vn =NaN;
                        data_base[id].svet_dekplonka_vnutri =NaN;
                    }
                }else{
                    selectElement.style.borderColor='red';
                    data_base[id].kod_dekor_vn =NaN;
                    data_base[id].svet_dekplonka_vnutri =NaN;
                }
            }
            // this.kod_dekor_sn && this.kod_dekor_vn

        }

    }else if(String(val) == '6'){
        var nakleyka = $('#nakleyka'+String(id))
        nakleyka.attr('disabled',false)

        if(nakleyka.val()!=''){
            data_base[id].kod_nakleyki = nakleyka.val();
            var selectedOption = $('#nakleyka'+String(id)).find('option:selected');

            var nadpisValue = selectedOption.data('nadpis');
            nadpis_nakleyki.text(nadpisValue)
            nakleyka.css('border-color','#dedad9')
        }else{
            data_base[id].kod_nakleyki = NaN;
            nadpis_nakleyki.text('')
            nakleyka.css('border-color','red')
        }

        var anod_sn = document.getElementById("anod"+String(id))
        const spanTextbox1 = anod_sn.querySelector('span[role="textbox"]');
        
        const spanss =document.querySelector('#anod'+String(id) +' .select2-container .select2-selection--single')
        if(spanTextbox1){
            if(spanTextbox1.innerText !='' ){
                spanss.style.borderColor='#dedad9';
                var tip_anodirovki = $('#tip_anodirovki'+String(id)).text()
                var sposob_anodirovki = $('#sposob_anodirovki'+String(id)).text()
                data_base[id].tip_anod = tip_anodirovki;
                data_base[id].sposob_anod = sposob_anodirovki;
                data_base[id].kod_anod_sn = spanTextbox1.innerText;
            }else{
                spanss.style.borderColor='red';
                data_base[id].kod_anod_sn = NaN;
                data_base[id].tip_anod = NaN;
                data_base[id].sposob_anod = NaN;
            }
        }
        if(combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА'){
            data_base[id].is_termo =true;
            var anod_sn = document.getElementById("anod_vnutr"+String(id))
            // anod_sn.style.borderColor='#dedad9';
            const spanss =document.querySelector('#anod_vnutr'+String(id) +' .select2-container .select2-selection--single')
            const spanTextbox2 = anod_sn.querySelector('span[role="textbox"]');
            if(spanTextbox2){
                if(spanTextbox2.innerText !=''){
                    spanss.style.borderColor='#dedad9';
                    spanTextbox2.style.borderColor='#dedad9';
                    data_base[id].kod_anod_vn = spanTextbox2.innerText;
                }else{
                    spanss.style.borderColor='red';
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

    var data =data_base[id].get_kratkiy_tekst()
    if(data.accept){
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','#2de319')
        data_base[id].full=true
        data_base[id].kratkiy_tekst=data.text
    }else{
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','white')
        data_base[id].full=false
        data_base[id].kratkiy_tekst=NaN

    }
    if(data.text !='XXXXXXXX' ){
        var artikul_bass = data_base[id].base_artikul
        var art_krat_dict = artikul_bass + data.text
        var sap_code_ruchnoy = $('#sap_code'+id)
        var kratkiy_text_ruchnoy = $('#krat'+id)
        

        // console.log(zapros_count,art_krat_dict,'+++++')
        if(art_krat_dict in zapros_count){
            if(zapros_count[art_krat_dict]){
                var sap_code = zapros_count[art_krat_dict]
                sap_code_ruchnoy.val(sap_code)
                kratkiy_text_ruchnoy.val(data.text)
                sap_code_ruchnoy.css('background-color','orange')
                kratkiy_text_ruchnoy.css('background-color','orange')
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
            sap_codes = get_sapcode(id,data_base[id].base_artikul,data.text,data_base[id].is_termo)
            
        }
        data_base[id].kratkiy_tekst= data.text
    }
    kratkiy_tekst.text(data.text)

    }
}


function get_sapcode(id,artikul,kratkiy_tekst,is_termo){
    var url = '/client/get-sapcodes'
   

    $.ajax({
        type: 'GET',
        url: url,
        data: {'artikul':artikul,'kratkiy_tekst':kratkiy_tekst,'is_termo':is_termo},
    }).done(function (res) {
        if (res.status ==201){
            var art_krat =artikul+kratkiy_tekst
            zapros_count[art_krat]=res.artikul

            var sap_code = $('#sap_code'+id)
            var krat = $('#krat'+id)
            data_base[id].sap_code=res.artikul
            data_base[id].krat=res.kratkiy_tekst

            sap_code.val(res.artikul)
            krat.val(res.kratkiy_tekst)
            sap_code.css('background-color','orange')
            krat.css('background-color','orange')
        }else{
            var art_krat =artikul+kratkiy_tekst
            zapros_count[art_krat]=NaN

            var sap_code = $('#sap_code'+id)
            var krat = $('#krat'+id)
            data_base[id].sap_code=NaN
            data_base[id].krat=NaN
            
            sap_code.val('')
            krat.val('')
            sap_code.css('background-color','#eaecef')
            krat.css('background-color','#eaecef')
            console.log('aa')
        }
        // WON'T REDIRECT
    });
}

