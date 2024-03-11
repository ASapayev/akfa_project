
class OnlineSavdo{
    constructor(id=NaN, sap_code=NaN,krat=NaN,online_id=NaN,nazvaniye_ruchnoy=NaN,svet_product=NaN,group_zakup=NaN,group=NaN,tip=NaN,bazoviy_edin=NaN,status_online=NaN,zavod=NaN) {
        this.id = id;
        this.sap_code = sap_code;
        this.krat = krat;
        this.online_id = online_id;
        this.nazvaniye_ruchnoy = nazvaniye_ruchnoy;

        this.svet_product = svet_product;
        this.group_zakup = group_zakup;
        this.group = group;
        this.tip = tip;
        this.bazoviy_edin = bazoviy_edin;
        this.status_online = status_online;
        this.zavod = zavod;
      }
      get_kratkiy_tekst(){
        if(this.sap_code && this.krat && this.online_id && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod){
            return this.sap_code + this.krat + ' L' + this.online_id +'  ' + this.nazvaniye_ruchnoy
        }else{    
            return 'XXXXXXXX'
        }
    }

}

class Neokrashenniy{
    constructor(id=NaN, 
        sap_code=NaN,krat=NaN,online_id=NaN,nazvaniye_ruchnoy=NaN,svet_product=NaN,group_zakup=NaN,group=NaN,tip=NaN,bazoviy_edin=NaN,status_online=NaN,zavod=NaN,
        splav=NaN,tip_zak=NaN,dlina=NaN,kod_kraska_sn=NaN,kod_nakleyki=NaN,kod_kraska_vn=NaN,is_termo=false) {
      this.id = id;
      this.splav = splav;
      this.tip_zak = tip_zak;
      this.dlina = dlina;
      this.kod_kraska_sn = kod_kraska_sn;
      this.kod_kraska_vn = kod_kraska_vn;
      this.kod_nakleyki = kod_nakleyki;
      this.is_termo = is_termo;

      
      this.sap_code = sap_code;
      this.krat = krat;
      this.online_id = online_id;
      this.nazvaniye_ruchnoy = nazvaniye_ruchnoy;

      this.svet_product = svet_product;
      this.group_zakup = group_zakup;
      this.group = group;
      this.tip = tip;
      this.bazoviy_edin = bazoviy_edin;
      this.status_online = status_online;
      this.zavod = zavod;
    }

    get_kratkiy_tekst(){
        if(!this.is_termo){
            if(this.splav && this.tip_zak && this.dlina && this.kod_kraska_sn && this.kod_nakleyki){
                if (this.sap_code && this.krat && this.online_id && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod){
                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.kod_kraska_sn +'  ' +this.kod_nakleyki,'accept':true}
                }else{
                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.kod_kraska_sn +'  ' +this.kod_nakleyki,'accept':false}
                }
            }else{
                return {'text':'XXXXXXXX','accept':false}
            }
        }else{
            if(this.splav && this.tip_zak && this.dlina && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki){
                if (this.sap_code && this.krat && this.online_id && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod){

                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.kod_kraska_sn +'/'+this.kod_kraska_vn+'  ' +this.kod_nakleyki,'accept':true}
                }else{
                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.kod_kraska_sn +'/'+this.kod_kraska_vn+'  ' +this.kod_nakleyki,'accept':false}

                }
            }else{
                return {'text':'XXXXXXXX','accept':false}
            }
        }
    }
  }

class Beliy{
    constructor(id=NaN, 
        sap_code=NaN,krat=NaN,online_id=NaN,nazvaniye_ruchnoy=NaN,svet_product=NaN,group_zakup=NaN,group=NaN,tip=NaN,bazoviy_edin=NaN,status_online=NaN,zavod=NaN,
        splav=NaN,tip_zak=NaN,dlina=NaN,brend_kraska_sn=NaN,brend_kraska_vn=NaN,kod_kraska_sn=NaN,kod_kraska_vn=NaN,kod_nakleyki=NaN,is_termo=false) {
      this.id = id;
      this.splav = splav;
      this.tip_zak = tip_zak;
      this.dlina = dlina;
      this.brend_kraska_sn = brend_kraska_sn;
      this.brend_kraska_vn = brend_kraska_vn;
      this.kod_kraska_sn = kod_kraska_sn;
      this.kod_kraska_vn = kod_kraska_vn;
      this.kod_nakleyki = kod_nakleyki;
      this.is_termo = is_termo;

      
      this.sap_code = sap_code;
      this.krat = krat;
      this.online_id = online_id;
      this.nazvaniye_ruchnoy = nazvaniye_ruchnoy;

      this.svet_product = svet_product;
      this.group_zakup = group_zakup;
      this.group = group;
      this.tip = tip;
      this.bazoviy_edin = bazoviy_edin;
      this.status_online = status_online;
      this.zavod = zavod;
    }

    get_kratkiy_tekst(){
        if(!this.is_termo){

            if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_nakleyki){
                if (this.sap_code && this.krat && this.online_id && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod){

                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'  ' +this.kod_nakleyki,'accept':true}
                }else{
                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'  ' +this.kod_nakleyki,'accept':false}

                }
            }else{
                return {'text':'XXXXXXXX','accept':false}
            }
        }else{

            if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki){
                if (this.sap_code && this.krat && this.online_id && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod){

                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+'  ' +this.kod_nakleyki,'accept':true}
                }else{
                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+'  ' +this.kod_nakleyki,'accept':false}

                }
            }else{
                return {'text':'XXXXXXXX','accept':false}
            }
        }
    }
  }

class Okrashenniy{
    constructor(id=NaN, 
        sap_code=NaN,krat=NaN,online_id=NaN,nazvaniye_ruchnoy=NaN,svet_product=NaN,group_zakup=NaN,group=NaN,tip=NaN,bazoviy_edin=NaN,status_online=NaN,zavod=NaN,
        splav=NaN,tip_zak=NaN,dlina=NaN,brend_kraska_sn=NaN,brend_kraska_vn=NaN,kod_kraska_sn=NaN,kod_kraska_vn=NaN,kod_nakleyki=NaN,is_termo=false) {
      this.id = id;
      this.splav = splav;
      this.tip_zak = tip_zak;
      this.dlina = dlina;
      this.brend_kraska_sn = brend_kraska_sn;
      this.brend_kraska_vn = brend_kraska_vn;
      this.kod_kraska_sn = kod_kraska_sn;
      this.kod_kraska_vn = kod_kraska_vn;
      this.kod_nakleyki = kod_nakleyki;
      this.is_termo = is_termo;

      
      this.sap_code = sap_code;
      this.krat = krat;
      this.online_id = online_id;
      this.nazvaniye_ruchnoy = nazvaniye_ruchnoy;

      this.svet_product = svet_product;
      this.group_zakup = group_zakup;
      this.group = group;
      this.tip = tip;
      this.bazoviy_edin = bazoviy_edin;
      this.status_online = status_online;
      this.zavod = zavod;
    }
    get_kratkiy_tekst(){
        if(!this.is_termo){
            if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_nakleyki){
                if (this.sap_code && this.krat && this.online_id && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod){

                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'  ' +this.kod_nakleyki,'accept':true}
                }else{
                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'  ' +this.kod_nakleyki,'accept':false}

                }
            }else{
                return {'text':'XXXXXXXX','accept':false}
            }
        }else{
            console.log(this.splav,this.tip_zak,this.dlina,this.brend_kraska_sn,this.brend_kraska_vn,this.kod_kraska_sn,this.kod_kraska_vn,this.kod_nakleyki)
            if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki){
                if (this.sap_code && this.krat && this.online_id && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod){

                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn+'/'+this.brend_kraska_vn+this.kod_kraska_vn+'  ' +this.kod_nakleyki,'accept':true}
                }else{
                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn+'/'+this.brend_kraska_vn+this.kod_kraska_vn+'  ' +this.kod_nakleyki,'accept':false}

                }
            }else{
                return {'text':'XXXXXXXX','accept':false}
            }
        }
    }
  }


class Sublimatsiya{
    constructor(id=NaN, 
        sap_code=NaN,krat=NaN,online_id=NaN,nazvaniye_ruchnoy=NaN,svet_product=NaN,group_zakup=NaN,group=NaN,tip=NaN,bazoviy_edin=NaN,status_online=NaN,zavod=NaN,
        splav=NaN,tip_zak=NaN,dlina=NaN,brend_kraska_sn=NaN,brend_kraska_vn=NaN,kod_kraska_sn=NaN,kod_kraska_vn=NaN,kod_dekor_sn=NaN,kod_dekor_vn=NaN,kod_nakleyki=NaN,is_termo=false) {
      this.id = id;
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

      this.sap_code = sap_code;
      this.krat = krat;
      this.online_id = online_id;
      this.nazvaniye_ruchnoy = nazvaniye_ruchnoy;

      this.svet_product = svet_product;
      this.group_zakup = group_zakup;
      this.group = group;
      this.tip = tip;
      this.bazoviy_edin = bazoviy_edin;
      this.status_online = status_online;
      this.zavod = zavod;
    }

    get_kratkiy_tekst(){
        if(!this.is_termo){
            if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_dekor_sn && this.kod_nakleyki){
                if (this.sap_code && this.krat && this.online_id && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod){

                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_dekor_sn + '  ' +this.kod_nakleyki,'accept':true}
                }else{
                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_dekor_sn + '  ' +this.kod_nakleyki,'accept':false}

                }
            }else{
                return {'text':'XXXXXXXX','accept':false}
            }
        }else{
            if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_dekor_sn && this.kod_dekor_vn  && this.kod_nakleyki){
                if (this.sap_code && this.krat && this.online_id && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod){

                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+'_'+this.kod_dekor_sn+'/'+this.kod_dekor_vn + '  ' +this.kod_nakleyki,'accept':true}
                }else{
                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+'_'+this.kod_dekor_sn+'/'+this.kod_dekor_vn + '  ' +this.kod_nakleyki,'accept':false}

                }
            }else{
                return {'text':'XXXXXXXX','accept':false}
            }
        }
    }
  }
class Laminatsiya{
    constructor(id=NaN, 
        sap_code=NaN,krat=NaN,online_id=NaN,nazvaniye_ruchnoy=NaN,svet_product=NaN,group_zakup=NaN,group=NaN,tip=NaN,bazoviy_edin=NaN,status_online=NaN,zavod=NaN,
        splav=NaN,tip_zak=NaN,dlina=NaN,brend_kraska_sn=NaN,brend_kraska_vn=NaN,kod_kraska_sn=NaN,kod_kraska_vn=NaN,kod_lam_sn=NaN,kod_lam_vn=NaN,kod_nakleyki=NaN,is_termo=false) {
      this.id = id;
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

      this.sap_code = sap_code;
      this.krat = krat;
      this.online_id = online_id;
      this.nazvaniye_ruchnoy = nazvaniye_ruchnoy;

      this.svet_product = svet_product;
      this.group_zakup = group_zakup;
      this.group = group;
      this.tip = tip;
      this.bazoviy_edin = bazoviy_edin;
      this.status_online = status_online;
      this.zavod = zavod;
    }
    get_kratkiy_tekst(){
        if(!this.is_termo){
            if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki){
                if (this.sap_code && this.krat && this.online_id && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod){

                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + '  ' +this.kod_nakleyki,'accept':true}
                }else{
                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + '  ' +this.kod_nakleyki,'accept':false}
                }
            }else{
                return {'text':'XXXXXXXX','accept':false}
            }
        }else{
            if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki){
                if (this.sap_code && this.krat && this.online_id && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod){

                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn + this.kod_kraska_vn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + '  ' +this.kod_nakleyki,'accept':true}
                }else{
                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn + this.kod_kraska_vn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + '  ' +this.kod_nakleyki,'accept':false}

                }
            }else{
                return {'text':'XXXXXXXX','accept':false}
            }
        }
    }
  }
class Anodirovka {
    constructor(id=NaN, 
        sap_code=NaN,krat=NaN,online_id=NaN,nazvaniye_ruchnoy=NaN,svet_product=NaN,group_zakup=NaN,group=NaN,tip=NaN,bazoviy_edin=NaN,status_online=NaN,zavod=NaN,
        splav=NaN,tip_zak=NaN,dlina=NaN,kod_anod_sn=NaN,kod_anod_vn=NaN,kod_nakleyki=NaN,contactnost_anod=NaN,is_termo=false) {
        
      this.id = id;
      this.splav = splav;
      this.tip_zak = tip_zak;
      this.dlina = dlina;
      this.kod_anod_sn = kod_anod_sn;
      this.kod_anod_vn = kod_anod_vn;
      this.kod_nakleyki = kod_nakleyki;
      this.contactnost_anod = contactnost_anod;
      this.is_termo = is_termo;

      this.sap_code = sap_code;
      this.krat = krat;
      this.online_id = online_id;
      this.nazvaniye_ruchnoy = nazvaniye_ruchnoy;

      this.svet_product = svet_product;
      this.group_zakup = group_zakup;
      this.group = group;
      this.tip = tip;
      this.bazoviy_edin = bazoviy_edin;
      this.status_online = status_online;
      this.zavod = zavod;
    }
   
    get_kratkiy_tekst(){
        console.log(this)
        if(!this.is_termo){
            if(this.splav && this.tip_zak && this.dlina && this.kod_anod_sn && this.kod_nakleyki && this.contactnost_anod){
                if (this.sap_code && this.krat && this.online_id && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod){
                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.kod_anod_sn + '  ' + this.contactnost_anod + '  ' + this.kod_nakleyki,'accept':true}
                }else{
                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.kod_anod_sn + '  ' + this.contactnost_anod + '  ' + this.kod_nakleyki,'accept':false}
                }
            }else{
                return {'text':'XXXXXXXX','accept':false}
            }
        }else{
            if(this.splav && this.tip_zak && this.dlina && this.kod_anod_sn && this.kod_anod_vn && this.kod_nakleyki && this.contactnost_anod){
                if (this.sap_code && this.krat && this.online_id && this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod){
                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.kod_anod_sn +'/'+this.kod_anod_vn+ '  ' + this.contactnost_anod + '  ' + this.kod_nakleyki,'accept':true}
                }else{
                    return {'text':this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.kod_anod_sn +'/'+this.kod_anod_vn+ '  ' + this.contactnost_anod + '  ' + this.kod_nakleyki,'accept':false}
                }

            }else{
                return {'text':'XXXXXXXX','accept':false}
            }

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
            <button type="button" class="btn btn-secondary btn-sm" onclick="create(`+String(i)+`)" id='create_btn`+String(i)+`' >Создание</button>
            <button type="button" class="btn btn-info btn-sm" onclick="activate(`+String(i)+`)" id='activate_btn`+String(i)+`'>Активация</button>
            <button type="button" class="btn btn-warning btn-sm gradient-buttons" onclick="artukil_clear(`+String(i)+`)"  id='clear_btn`+String(i)+`'>Очистить</button>
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
            <select class=" form-control basic_artikul" style="background-color:#ddebf7; width: 140px; font-size:10px " disabled id="artikul`+String(i)+`" onchange='clear_artikul(`+String(i)+`)'></select>
        </div>
    </td>
    
    
    <td >
        <div class="input-group input-group-sm mb-1">
            <input type="text" class="form-control " style='width:50px' onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled aria-describedby="inputGroup-sizing-sm" name ='length`+String(i)+`' id="length`+String(i)+`"  >
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
            <option  value="" selected ></option>
            <option value="63" >63</option>
        </select>
        
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1"  style="width: 60px;">
        <select class="form-select" aria-label="" style="width: 50px;!important"  disabled id='tip_zakalyonnosti`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)">
            <option  value="" selected></option>
            <option value="T4" >T4</option>
            <option value="T6" >T6</option>
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
            <span class =' text-center' style="font-size: small; font-weight: bold; text-transform: uppercase; width:100px" id ='code_kraski_vnutri` +String(i)+`'></span>
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
            <em><span class =' text-center ' style="font-size: 10px;  font-weight: bold; text-transform: uppercase;" id ='code_dekplonka_vnutri` +String(i)+`' disabled></span></em>
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
       
        <input type='text' class=" form-control " style="  border-color:red;width: 110px; font-size:10px; display:none; " id='sap_code_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
    
        </div>
    </td> 
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="border-color:red; width: 220px; font-size:10px; display:none; "  id='kratkiy_tekst_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1">
           
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 90px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;border-color:red;" onchange="create_kratkiy_tekst(`+String(i)+`)"  id='zavod`+String(i)+`' required>
            <option  selected></option>
            <option value="ZAVOD ALUMIN NAVOIY" >Benkam</option>
            <option value="ZAVOD ALUMIN">Jomiy</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 113px;text-transform: uppercase; font-size:12px; padding-right:0px;" onchange="create_kratkiy_tekst(`+String(i)+`)"  id='status_first`+String(i)+`' required>
        <option value="Активный" selected >Активный</option>
        <option value="Пассивный">Пассивный</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px; display:none;" id='online_savdo_id`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <textarea   rows='1' class=" form-control " style="border-color:red; width: 220px; font-size:10px; display:none; " id='nazvaniye_ruchnoy`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></textarea >
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 110px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;"  id='svet_product`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
        <option  selected></option>
        <option   value="LAM">LAM</option>
        <option   value="Anod">Anod</option>
        <option   value="COLOUR">COLOUR</option>
        <option   value="VAKUM &amp; 3D">VAKUM &amp; 3D</option>
        <option   value="WHITE">WHITE</option>
        <option   value="Без цвета">Без цвета</option>
      </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 230px;text-transform: uppercase; font-size:12px; padding-right:0px;  border-color:red;display:none;" id='group_zakup`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
        <option  selected></option>
        <option value="Kabina">Kabina</option>
        <option value="Alumin WHITE (B.N)">Alumin WHITE (B.N)</option>
        <option value="Aksessuar Import (SAP)">Aksessuar Import (SAP)</option>
        <option value="Alumin VAKUM (B.N)">Alumin VAKUM (B.N)</option>
        <option value="Metal">Metal</option>
        <option value="Aksessuar UZ Tapoich">Aksessuar UZ Tapoich</option>
        <option value="Alumin COLOUR (Navoiy)">Alumin COLOUR (Navoiy)</option>
        <option value="Alumin VAKUM (Navoiy)">Alumin VAKUM (Navoiy)</option>
        <option value="Alumin WHITE (Navoiy)">Alumin WHITE (Navoiy)</option>
        <option value="Alumin Anod (Navoiy)">Alumin Anod (Navoiy)</option>
        <option value="PVX OQ (Navoiy)">PVX OQ (Navoiy)</option>
        <option value="Butilchita">Butilchita</option>
        <option value="Aksessuar Rezina">Aksessuar Rezina</option>
        <option value="Radiator">Radiator</option>
        <option value="Aksessuar UZ">Aksessuar UZ</option>
        <option value="Alucobond">Alucobond</option>
        <option value="VITYAJNOYE USTROYSTVA">VITYAJNOYE USTROYSTVA</option>
        <option value="Aksessuar Import">Aksessuar Import</option>
        <option value="Radiator (IMPORT)">Radiator (IMPORT)</option>
        <option value="Radiator SAP (IMPORT)">Radiator SAP (IMPORT)</option>
        <option value="PVX LAM (Navoiy)">PVX LAM (Navoiy)</option>
        <option value="Rezina Tpv">Rezina Tpv</option>
        <option value="Granula">Granula</option>
        <option value="Granit">Granit</option>
        <option value="Setka">Setka</option>
        <option value="Kraska">Kraska</option>
        <option value="Gazoblok">Gazoblok</option>
        <option value="Paket">Paket</option>
        <option value="Alumin Lam">Alumin Lam</option>
        <option value="Alumin COLOUR">Alumin COLOUR</option>
        <option value="Alumin VAKUM">Alumin VAKUM</option>
        <option value="Alumin WHITE">Alumin WHITE</option>
        <option value="Radiator (Panel) AKFA (UZ)">Radiator (Panel) AKFA (UZ)</option>
        <option value="Radiator (Panel) ROYAL (UZ)">Radiator (Panel) ROYAL (UZ)</option>
        <option value="Radiator (Panel) Lider Line (UZ)" >Radiator (Panel) Lider Line (UZ)"</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1" id='group`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)'>
        <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;"  id='tipr`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)'required>
            <option  selected></option>
            <option value="Сырье">Сырье</option>
            <option value="Готовый продукт">Готовый продукт</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;"  id='tip`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)'required>
            <option  selected></option>
            <option value="Сырье">Сырье</option>
            <option value="Готовый продукт">Готовый продукт</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 145px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;" id='segment`+String(i)+`' required>
            <option  selected></option>
            <option value="Aldoks">Aldoks</option>
            <option value="Стандарт">Стандарт</option>
            <option value="Премиум">Премиум</option>
            <option value="Аксессуар">Аксессуар</option>
            <option value="Falcon">Falcon</option>
            <option value="Mebel">Mebel</option>
            <option value="RETPEN 8-10%">RETPEN 8-10%</option>
            <option value="RETPEN 10-12%">RETPEN 10-12%</option>
            <option value="RETPEN 17%">RETPEN 17%</option>
            <option value="Аксессуар 2">Аксессуар 2</option>
            <option value="Podokonnik EKO">Podokonnik EKO</option>
            <option value="Alumin arzon">Alumin arzon</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 520px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;" id='buxgalter_tovar`+String(i)+`' required>
            <option  selected></option>
            <option value='Профиль из ПВХ ламинированный'>Профиль из ПВХ ламинированный</option>
            <option value='Otvetka 153 (oq)'>Otvetka 153 (oq)</option>
            <option value='Ламбри из ПВХ'>Ламбри из ПВХ</option>
            <option value='Soedinitel OP.40.J05 L=10mm'>Soedinitel OP.40.J05 L=10mm</option>
            <option value='Soedinitel CL.X.W 14 (5mm)'>Soedinitel CL.X.W 14 (5mm)</option>
            <option value='BKT 78 Soed. (M11427-15.8mm)'>BKT 78 Soed. (M11427-15.8mm)</option>
            <option value='Soedinitel CL.X.W 14 (38mm)'>Soedinitel CL.X.W 14 (38mm)</option>
            <option value='BKT 70 Soed. W 02 (1=7.8)'>BKT 70 Soed. W 02 (1=7.8)</option>
            <option value='Otvetka 155 (rangli)'>Otvetka 155 (rangli)</option>
            <option value='Ruchka Dvernaya Fornaks (28mm) (rangli)'>Ruchka Dvernaya Fornaks (28mm) (rangli)</option>
            <option value='Petlya Dvernaya 2SK MASTER (rangli)'>Petlya Dvernaya 2SK MASTER (rangli)</option>
            <option value='Petlya (rangli)'>Petlya (rangli)</option>
            <option value='Soedinitel Chovush'>Soedinitel Chovush</option>
            <option value='Soedinitel (Bolshoy) CHEMPION'>Soedinitel (Bolshoy) CHEMPION</option>
            <option value='Petlya Dvernaya Chempion (rangli)'>Petlya Dvernaya Chempion (rangli)</option>
            <option value='Soedinitel (Bolshoy) (ALD-2)'>Soedinitel (Bolshoy) (ALD-2)</option>
            <option value='Krishka Podokonnik (ALYUMIN) (oq)'>Krishka Podokonnik (ALYUMIN) (oq)</option>
            <option value='Soedinitel Universal'>Soedinitel Universal</option>
            <option value='Ogranichitel (rangli)'>Ogranichitel (rangli)</option>
            <option value='Otvetka Mini 153 (rangli)'>Otvetka Mini 153 (rangli)</option>
            <option value='Ruchka Elegant (rangli)'>Ruchka Elegant (rangli)</option>
            <option value='Ruchka LUX Fortuna O (rangli)'>Ruchka LUX Fortuna O (rangli)</option>
            <option value='Petlya 100 mm (rangli)'>Petlya 100 mm (rangli)</option>
            <option value='Ruchka dvernaya "BELLA" (700) mm (rangli)'>Ruchka dvernaya "BELLA" (700) mm (rangli)</option>
            <option value='Soedinitel CL.X.W 34 (43mm)'>Soedinitel CL.X.W 34 (43mm)</option>
            <option value='Ruchka dvernaya "BELLA" (500) mm (oq)'>Ruchka dvernaya "BELLA" (500) mm (oq)</option>
            <option value='Ruchka dvernaya "BELLA" (600) mm (rangli)'>Ruchka dvernaya "BELLA" (600) mm (rangli)</option>
            <option value='Ruchka LUX Fortuna O (oq)'>Ruchka LUX Fortuna O (oq)</option>
            <option value='Otvetka Mini 155 (oq)'>Otvetka Mini 155 (oq)</option>
            <option value='Soedinitel CL.X.W 10 (25.8mm)'>Soedinitel CL.X.W 10 (25.8mm)</option>
            <option value='Termo soedinitel 19 mm'>Termo soedinitel 19 mm</option>
            <option value='Petlya 100 mm (oq)'>Petlya 100 mm (oq)</option>
            <option value='Petlya (ALD-2) (oq)'>Petlya (ALD-2) (oq)</option>
            <option value='Otvetnaya chast zamka A0275-K (155) (rangli)'>Otvetnaya chast zamka A0275-K (155) (rangli)</option>
            <option value='Petlya (ALD-2) (rangli)'>Petlya (ALD-2) (rangli)</option>
            <option value='Petlya Dvernaya 3SK MASTER (rangli)'>Petlya Dvernaya 3SK MASTER (rangli)</option>
            <option value='Petlya Dvernaya Alyumin (rangli)'>Petlya Dvernaya Alyumin (rangli)</option>
            <option value='Ruchka Kvadrat (rangli)'>Ruchka Kvadrat (rangli)</option>
            <option value='Chit-Chit PVH.uz (rangli)'>Chit-Chit PVH.uz (rangli)</option>
            <option value='Otvetka 153 (rangli)'>Otvetka 153 (rangli)</option>
            <option value='Ruchka LUX Fortuna Mini O (rangli)'>Ruchka LUX Fortuna Mini O (rangli)</option>
            <option value='Zashyolka Narujnyaya (rangli)'>Zashyolka Narujnyaya (rangli)</option>
            <option value='Shpingalet (rangli)'>Shpingalet (rangli)</option>
            <option value='Ruchka DELFIN (rangli)'>Ruchka DELFIN (rangli)</option>
            <option value='Otvetka Mini 155 (rangli)'>Otvetka Mini 155 (rangli)</option>
            <option value='Otvetnaya chast zamka A0275-K (153) (rangli)'>Otvetnaya chast zamka A0275-K (153) (rangli)</option>
            <option value='BKT 70 Soed. Impost (J01-52.5mm)'>BKT 70 Soed. Impost (J01-52.5mm)</option>
            <option value='BKT 70 Soed. Impost (J01-66.5mm)'>BKT 70 Soed. Impost (J01-66.5mm)</option>
            <option value='BKT 70 Soed. Impost (J02-13.6mm)'>BKT 70 Soed. Impost (J02-13.6mm)</option>
            <option value='BKT 70 Soed. Impost (J02-43.6mm)'>BKT 70 Soed. Impost (J02-43.6mm)</option>
            <option value='BKT 70 Soed. Impost (J03-66.6mm)'>BKT 70 Soed. Impost (J03-66.6mm)</option>
            <option value='BKT 70 Soed. Impost (J06-43.6mm)'>BKT 70 Soed. Impost (J06-43.6mm)</option>
            <option value='BKT 70 Soed. Impost (J06-66.5mm)'>BKT 70 Soed. Impost (J06-66.5mm)</option>
            <option value='BKT 70 Soed. W 01 (1=21.7)'>BKT 70 Soed. W 01 (1=21.7)</option>
            <option value='BKT 70 Soed. W 01 (1=5.1)'>BKT 70 Soed. W 01 (1=5.1)</option>
            <option value='BKT 70 Soed. W 01 (1=8.5)'>BKT 70 Soed. W 01 (1=8.5)</option>
            <option value='Krishka Podokonnik (ALYUMIN) (rangli)'>Krishka Podokonnik (ALYUMIN) (rangli)</option>
            <option value='Kreplenie moskitnoy setki (rangli)'>Kreplenie moskitnoy setki (rangli)</option>
            <option value='BKT 70 Soed. W 01 (1=8)'>BKT 70 Soed. W 01 (1=8)</option>
            <option value='BKT 78 Soed. (M11427-19.5mm)'>BKT 78 Soed. (M11427-19.5mm)</option>
            <option value='Kreplenie moskitnoy setki (oq)'>Kreplenie moskitnoy setki (oq)</option>
            <option value='BKT 78 Soed. (M11427-27mm)'>BKT 78 Soed. (M11427-27mm)</option>
            <option value='Ruchka LUX Pol (oq)'>Ruchka LUX Pol (oq)</option>
            <option value='Ruchka Sos. VENTURO (oq)'>Ruchka Sos. VENTURO (oq)</option>
            <option value='Montajnaya Planka 5200 (Metal)'>Montajnaya Planka 5200 (Metal)</option>
            <option value='Ламинированный термоуплотненный алюминиевый профиль'>Ламинированный термоуплотненный алюминиевый профиль</option>
            <option value='Термоуплотненный анодированный алюминиевый профиль (N)'>Термоуплотненный анодированный алюминиевый профиль (N)</option>
            <option value='Профиль из ПВХ с уплотнителем'>Профиль из ПВХ с уплотнителем</option>
            <option value='Алюминиевый профиль с декоративным покрытием'>Алюминиевый профиль с декоративным покрытием</option>
            <option value='Подоконник из ПВХ'>Подоконник из ПВХ</option>
            <option value='Дистанционная рамка'>Дистанционная рамка</option>
            <option value='Профиль из ПВХ ламинированный (Engelberg)'>Профиль из ПВХ ламинированный (Engelberg)</option>
            <option value='Профиль из ПВХ ламинированный с уплотнителем'>Профиль из ПВХ ламинированный с уплотнителем</option>
            <option value='Ламинированный алюминиевый профиль'>Ламинированный алюминиевый профиль</option>
            <option value='Неокрашенный алюминиевый профиль'>Неокрашенный алюминиевый профиль</option>
            <option value='Подоконник из ПВХ ламинированный'>Подоконник из ПВХ ламинированный</option>
            <option value='Уплотнитель для алюминиевых и ПВХ профилей'>Уплотнитель для алюминиевых и ПВХ профилей</option>
            <option value='Профиль из ПВХ'>Профиль из ПВХ</option>
            <option value='Алюминиевый профиль'>Алюминиевый профиль</option>
            <option value='Ламинированный термоуплотненный алюминиевый профиль (N)'>Ламинированный термоуплотненный алюминиевый профиль (N)</option>
            <option value='Металлический усилитель'>Металлический усилитель</option>
            <option value='Ламбри из ПВХ ламинированный'>Ламбри из ПВХ ламинированный</option>
            <option value='Профиль из ПВХ (Engelberg)'>Профиль из ПВХ (Engelberg)</option>
            <option value='Ламинированный алюминиевый профиль (N)'>Ламинированный алюминиевый профиль (N)</option>
            <option value='Алюминиевый профиль с декоративным покрытием (N)'>Алюминиевый профиль с декоративным покрытием (N)</option>
            <option value='Chit-Chit PVH.uz (oq)'>Chit-Chit PVH.uz (oq)</option>
            <option value='BKT 70 Soed. (M11148-13.6mm)'>BKT 70 Soed. (M11148-13.6mm)</option>
            <option value='Ruchka D (oq)'>Ruchka D (oq)</option>
            <option value='Ruchka Kvadrat Mini (oq)'>Ruchka Kvadrat Mini (oq)</option>
            <option value='Ruchka LUX (oq)'>Ruchka LUX (oq)</option>
            <option value='Soedinitel 114 D 400 (13mm)'>Soedinitel 114 D 400 (13mm)</option>
            <option value='Soedinitel 114 D 400 (52mm)'>Soedinitel 114 D 400 (52mm)</option>
            <option value='Petlya Dvernaya Chempion (oq)'>Petlya Dvernaya Chempion (oq)</option>
            <option value='Soedinitel BKH-001 (38mm)'>Soedinitel BKH-001 (38mm)</option>
            <option value='Soedinitel 5507 (6,5mm)'>Soedinitel 5507 (6,5mm)</option>
            <option value='Soedinitel BKH-001 (16mm)'>Soedinitel BKH-001 (16mm)</option>
            <option value='Soedinitel BKH-001 (5mm)'>Soedinitel BKH-001 (5mm)</option>
            <option value='Soedinitel AKF-107 (40mm)'>Soedinitel AKF-107 (40mm)</option>
            <option value='Soedinitel AKF-106 (37.5mm)'>Soedinitel AKF-106 (37.5mm)</option>
            <option value='Vstavka Dlya Zamka (rangli)'>Vstavka Dlya Zamka (rangli)</option>
            <option value='Soedinitel JP2186 (60mm)'>Soedinitel JP2186 (60mm)</option>
            <option value='T 6 Soed. (ST 10 255) C 9.5 Qanot Mal.'>T 6 Soed. (ST 10 255) C 9.5 Qanot Mal.</option>
            <option value='T 6 Soed. (ST 10 366) C 29.0 Qanot Bol.'>T 6 Soed. (ST 10 366) C 29.0 Qanot Bol.</option>
            <option value='T 6 Soed. (ST 10 366) P 27.5 Kosa Bol.'>T 6 Soed. (ST 10 366) P 27.5 Kosa Bol.</option>
            <option value='T 6 Soed. (ST 10 366) P 9.2 Kosa Mal.'>T 6 Soed. (ST 10 366) P 9.2 Kosa Mal.</option>
            <option value='T 6 Soed. (ST 10 565) B 26.0 Balkon Qanot Bol.'>T 6 Soed. (ST 10 565) B 26.0 Balkon Qanot Bol.</option>
            <option value='T 6 Soed. (ST 10 565) B 5.1 Balkon Qanot Mal.'>T 6 Soed. (ST 10 565) B 5.1 Balkon Qanot Mal.</option>
            <option value='Soedinitel AKF-107 (43.5mm)'>Soedinitel AKF-107 (43.5mm)</option>
            <option value='Vstavka Dlya Zamka (oq)'>Vstavka Dlya Zamka (oq)</option>
            <option value='Soedinitel 5505 (45mm)'>Soedinitel 5505 (45mm)</option>
            <option value='Zashyolka Narujnyaya (oq)'>Zashyolka Narujnyaya (oq)</option>
            <option value='Zashyolka Narujnyaya Mini (oq)'>Zashyolka Narujnyaya Mini (oq)</option>
            <option value='Ruchka Dvernaya Fornaks (35mm) (rangli)'>Ruchka Dvernaya Fornaks (35mm) (rangli)</option>
            <option value='Krishka Podokonnik 300 (rangli)'>Krishka Podokonnik 300 (rangli)</option>
            <option value='Ogranichitel PVH (rangli)'>Ogranichitel PVH (rangli)</option>
            <option value='Petlya Dvernaya 3D (rangli)'>Petlya Dvernaya 3D (rangli)</option>
            <option value='Petlya Dvernaya 3D (oq)'>Petlya Dvernaya 3D (oq)</option>
            <option value='Porog Soedinitel 7000 (1kom.) (L;P) (rangli)'>Porog Soedinitel 7000 (1kom.) (L;P) (rangli)</option>
            <option value='Petlya 100 mm (oq)'>Petlya 100 mm (oq)</option>
            <option value='Krishka Shtulp Dlya Adap 7000 (oq)'>Krishka Shtulp Dlya Adap 7000 (oq)</option>
            <option value='Krishka Shtulp Dlya Adap dvernaya 6000 (13 AKS) (rangli)'>Krishka Shtulp Dlya Adap dvernaya 6000 (13 AKS) (rangli)</option>
            <option value='Ruchka Dvernaya Fornaks (28mm) fiksator (rangli)'>Ruchka Dvernaya Fornaks (28mm) fiksator (rangli)</option>
            <option value='Ruchka Dvernaya Fornaks (35mm) fiksator (rangli)'>Ruchka Dvernaya Fornaks (35mm) fiksator (rangli)</option>
            <option value='Chit-Chit (aldocks).uz (rangli)'>Chit-Chit (aldocks).uz (rangli)</option>
            <option value='Ruchka Okonaya Roto (rangli)'>Ruchka Okonaya Roto (rangli)</option>
            <option value='Petlya 75 mm (rangli)'>Petlya 75 mm (rangli)</option>
            <option value='Soedinitel AKF-106 (36.5mm)'>Soedinitel AKF-106 (36.5mm)</option>
            <option value='Soedinitel 114 D 300 (13,2 mm)'>Soedinitel 114 D 300 (13,2 mm)</option>
            <option value='Soedinitel JP2002 (40mm)'>Soedinitel JP2002 (40mm)</option>
            <option value='Ruchka Kvadrat Mini (rangli)'>Ruchka Kvadrat Mini (rangli)</option>
            <option value='Shpingalet (oq)'>Shpingalet (oq)</option>
            <option value='Krishka Shtulp Dlya Adap dvernaya 6000 (13 AKS) (oq)'>Krishka Shtulp Dlya Adap dvernaya 6000 (13 AKS) (oq)</option>
            <option value='Krishka Shtulp Dlya Adap 7000 (rangli)'>Krishka Shtulp Dlya Adap 7000 (rangli)</option>
            <option value='(A0286) Petlya (Chempion) (rangli)'>(A0286) Petlya (Chempion) (rangli)</option>
            <option value='Otvetka 155 (oq)'>Otvetka 155 (oq)</option>
            <option value='(A0286) Petlya (Chempion) (oq)'>(A0286) Petlya (Chempion) (oq)</option>
            <option value='BKT 70 Soed. Impost (J01-66.6mm)'>BKT 70 Soed. Impost (J01-66.6mm)</option>
            <option value='Petlya Dvernaya MDF (oq)'>Petlya Dvernaya MDF (oq)</option>
            <option value='Petlya Dvernaya MDF (rangli)'>Petlya Dvernaya MDF (rangli)</option>
            <option value='Petlya Dvernaya PVH (rangli)'>Petlya Dvernaya PVH (rangli)</option>
            <option value='Soedinitel A 00018 (21mm)'>Soedinitel A 00018 (21mm)</option>
            <option value='Soedinitel CL.X.W 14 (18mm)'>Soedinitel CL.X.W 14 (18mm)</option>
            <option value='Soedinitel CL.X.W 14 (8mm)'>Soedinitel CL.X.W 14 (8mm)</option>
            <option value='Soedinitel CL.X.W 14 (9mm)'>Soedinitel CL.X.W 14 (9mm)</option>
            <option value='Soedinitel WDT 67 J 02 (44mm)'>Soedinitel WDT 67 J 02 (44mm)</option>
            <option value='Soedinitel CL.X.W 34 (25.6mm)'>Soedinitel CL.X.W 34 (25.6mm)</option>
            <option value='Soedinitel CL.X.W 14 (12.5mm)'>Soedinitel CL.X.W 14 (12.5mm)</option>
            <option value='Petlya Dvernaya 3SK MASTER (rangli)'>Petlya Dvernaya 3SK MASTER (rangli)</option>
            <option value='Klipsa 13mm JP'>Klipsa 13mm JP</option>
            <option value='Zaglushka (PVCC 031) (rangli)'>Zaglushka (PVCC 031) (rangli)</option>
            <option value='Zaglushka (PVCC 032) (rangli)'>Zaglushka (PVCC 032) (rangli)</option>
            <option value='Soedinitel CL.X.W 20 (25.8mm)'>Soedinitel CL.X.W 20 (25.8mm)</option>
            <option value='Krishka Podokonnik 350 (Ovolniy) (rangli)'>Krishka Podokonnik 350 (Ovolniy) (rangli)</option>
            <option value='Soedinitel CL.X.W 34 (17,7mm)'>Soedinitel CL.X.W 34 (17,7mm)</option>
            <option value='Soedinitel CL.X.W 34 (10mm)'>Soedinitel CL.X.W 34 (10mm)</option>
            <option value='Ruchka dvernaya "BELLA" (1000) mm (rangli)'>Ruchka dvernaya "BELLA" (1000) mm (rangli)</option>
            <option value='Petlya dvernaya Jocker (rangli)'>Petlya dvernaya Jocker (rangli)</option>
            <option value='Soedinitel CL.X.W 34 (6mm)'>Soedinitel CL.X.W 34 (6mm)</option>
            <option value='Soedinitel CL.X.W 10 (5mm)'>Soedinitel CL.X.W 10 (5mm)</option>
            <option value='Soedinitel CL.X.W 34 (18mm)'>Soedinitel CL.X.W 34 (18mm)</option>
            <option value='Soedinitel CL.X.W 34 (15,8mm)'>Soedinitel CL.X.W 34 (15,8mm)</option>
            <option value='Soedinitel A 00018 (25 mm)'>Soedinitel A 00018 (25 mm)</option>
            <option value='Petlya dvernaya Jocker (oq)'>Petlya dvernaya Jocker (oq)</option>
            <option value='Ruchka Dvernaya mini (rangli)'>Ruchka Dvernaya mini (rangli)</option>
            <option value='Ruchka Dvernaya Fornaks (30mm) (rangli)'>Ruchka Dvernaya Fornaks (30mm) (rangli)</option>
            <option value='Soedinitel WDT 67 J 03 (44mm)'>Soedinitel WDT 67 J 03 (44mm)</option>
            <option value='Soedinitel 114 D 300 (10mm)'>Soedinitel 114 D 300 (10mm)</option>
            <option value='Soedinitel 114 D 400 (14mm)'>Soedinitel 114 D 400 (14mm)</option>
            <option value='Soedinitel CL.X.W 10 (14mm)'>Soedinitel CL.X.W 10 (14mm)</option>
            <option value='Krishka Podokonnik 300 (Trapetsiya) (rangli)'>Krishka Podokonnik 300 (Trapetsiya) (rangli)</option>
            <option value='Soedinitel 148х125хх (60mm)'>Soedinitel 148х125хх (60mm)</option>
            <option value='Soedinitel CL.X.W 16 (10.8mm)'>Soedinitel CL.X.W 16 (10.8mm)</option>
            <option value='Soedinitel FST 50 JR 001 (30mm)'>Soedinitel FST 50 JR 001 (30mm)</option>
            <option value='Soedinitel FST 50 G 003 (100 mm)'>Soedinitel FST 50 G 003 (100 mm)</option>
            <option value='Soedinitel CL.X.W 40 (7.4mm)'>Soedinitel CL.X.W 40 (7.4mm)</option>
            <option value='Soedinitel 8000'>Soedinitel 8000</option>
            <option value='Soedinitel CL.X.W 20 (20,7mm)'>Soedinitel CL.X.W 20 (20,7mm)</option>
            <option value='Soedinitel CL.X.W 20 (20,6mm)'>Soedinitel CL.X.W 20 (20,6mm)</option>
            <option value='Soedinitel OP.40.J04 L=10mm'>Soedinitel OP.40.J04 L=10mm</option>
            <option value='Soedinitel CL.X.W 34 (7,4mm)'>Soedinitel CL.X.W 34 (7,4mm)</option>
            <option value='Ruchka dvernaya "BELLA" (800) mm (rangli)'>Ruchka dvernaya "BELLA" (800) mm (rangli)</option>
            <option value='Soedinitel CL.X.W 40 (5mm)'>Soedinitel CL.X.W 40 (5mm)</option>
            <option value='Ruchka dvernaya "BELLA" (2000) mm (oq)'>Ruchka dvernaya "BELLA" (2000) mm (oq)</option>
            <option value='Ruchka Dvernaya (28mm) Slim fiksator (rangli)'>Ruchka Dvernaya (28mm) Slim fiksator (rangli)</option>
            <option value='Soedinitel CL.X.W 40 (19mm)'>Soedinitel CL.X.W 40 (19mm)</option>
            <option value='Ruchka dvernaya "BELLA" (1800) mm (rangli)'>Ruchka dvernaya "BELLA" (1800) mm (rangli)</option>
            <option value='Soedinitel CLSW 16'>Soedinitel CLSW 16</option>
            <option value='Soedinitel CL.X.W 40 (18.9mm)'>Soedinitel CL.X.W 40 (18.9mm)</option>
            <option value='Soedinitel 148х125хх (90mm)'>Soedinitel 148х125хх (90mm)</option>
            <option value='BKT 70 Soed. List (A10-001)'>BKT 70 Soed. List (A10-001)</option>
            <option value='Soedinitel CL.X.W 40 (19.6mm)'>Soedinitel CL.X.W 40 (19.6mm)</option>
            <option value='Soedinitel AKF-106 (44mm)'>Soedinitel AKF-106 (44mm)</option>
            <option value='Soedinitel AKF-107 (37mm)'>Soedinitel AKF-107 (37mm)</option>
            <option value='Soedinitel 7000 ECO'>Soedinitel 7000 ECO</option>
            <option value='Ruchka dvernaya "Comfort" (oq)'>Ruchka dvernaya "Comfort" (oq)</option>
            <option value='Soedinitel 148х125хх (140mm)'>Soedinitel 148х125хх (140mm)</option>
            <option value='Soedinitel BKH-010 (38mm)'>Soedinitel BKH-010 (38mm)</option>
            <option value='Ruchka Dvernaya (28mm) Slim (rangli)'>Ruchka Dvernaya (28mm) Slim (rangli)</option>
            <option value='Ruchka dvernaya "Comfort" (rangli)'>Ruchka dvernaya "Comfort" (rangli)</option>
            <option value='Soedinitel BKH-010 (56mm)'>Soedinitel BKH-010 (56mm)</option>
            <option value='Soedinitel CLSW 12'>Soedinitel CLSW 12</option>
            <option value='Ruchka dvernaya "BELLA" (1500) mm (rangli)'>Ruchka dvernaya "BELLA" (1500) mm (rangli)</option>
            <option value='Soedinitel FST 50 G 004 (100 mm)'>Soedinitel FST 50 G 004 (100 mm)</option>
            <option value='Ruchka Okonnaya PVH (rangli)'>Ruchka Okonnaya PVH (rangli)</option>
            <option value='Soedinitel 110049 (20mm)'>Soedinitel 110049 (20mm)</option>
            <option value='Soedinitel 110048 (20mm)'>Soedinitel 110048 (20mm)</option>
            <option value='Soedinitel CL.X.W 38 (28.7mm)'>Soedinitel CL.X.W 38 (28.7mm)</option>
            <option value='Soedinitel FST 50 JR 001 (33mm)'>Soedinitel FST 50 JR 001 (33mm)</option>
            <option value='Soedinitel FST 50 JR 001 (97,5mm)'>Soedinitel FST 50 JR 001 (97,5mm)</option>
            <option value='Ruchka Dvernaya (28mm) Slim (oq)'>Ruchka Dvernaya (28mm) Slim (oq)</option>
            <option value='Zaglushka (PVCC 033) (rangli)'>Zaglushka (PVCC 033) (rangli)</option>
            <option value='Zaglushka (PVCC 036) (rangli)'>Zaglushka (PVCC 036) (rangli)</option>
            <option value='Soedinitel moskitnoy setki (rangli)'>Soedinitel moskitnoy setki (rangli)</option>
            <option value='Ruchka dvernaya "BELLA" (700) mm (oq)'>Ruchka dvernaya "BELLA" (700) mm (oq)</option>
            <option value='Soedinitel CL.X.W 14 (43.5mm)'>Soedinitel CL.X.W 14 (43.5mm)</option>
            <option value='Soedinitel A 00018 (44mm)'>Soedinitel A 00018 (44mm)</option>
            <option value='Ruchka Elegant (oq)'>Ruchka Elegant (oq)</option>
            <option value='Krishka Shtulp Dlya Adap 6000 (rangli)'>Krishka Shtulp Dlya Adap 6000 (rangli)</option>
            <option value='Ruchka Dvernaya Fornaks (30mm) fiksator (rangli)'>Ruchka Dvernaya Fornaks (30mm) fiksator (rangli)</option>
            <option value='Krishka Shtulp Dlya Adap 8000 (rangli)'>Krishka Shtulp Dlya Adap 8000 (rangli)</option>
            <option value='Soedinitel CL.X.W 20 (25.6mm)'>Soedinitel CL.X.W 20 (25.6mm)</option>
            <option value='BKT 70 Soed. W 01 (1=5)'>BKT 70 Soed. W 01 (1=5)</option>
            <option value='Soedinitel moskitnoy setki (oq)'>Soedinitel moskitnoy setki (oq)</option>
            <option value='Замок для профиля москитной сетки серии 10х20цветной'>Замок для профиля москитной сетки серии 10х20цветной</option>
            <option value='Замок для профиля москитной сетки серии 10х20'>Замок для профиля москитной сетки серии 10х20</option>
            <option value='Soedinitel CLSW 0243'>Soedinitel CLSW 0243</option>
            <option value='Klipsa 10.5 mm'>Klipsa 10.5 mm</option>
            <option value='BKT 70 Soed. Impost (J01-26.3mm)'>BKT 70 Soed. Impost (J01-26.3mm)</option>
            <option value='BKT 70 Soed. Impost (J02-23.6mm)'>BKT 70 Soed. Impost (J02-23.6mm)</option>
            <option value='BKT 70 Soed. Impost (J06-13.6mm)'>BKT 70 Soed. Impost (J06-13.6mm)</option>
            <option value='BKT 70 Soed. Impost (J06-23.6mm)'>BKT 70 Soed. Impost (J06-23.6mm)</option>
            <option value='BKT 70 Soed. W 01 (1=18.4)'>BKT 70 Soed. W 01 (1=18.4)</option>
            <option value='BKT 70 Soed. W 01 (1=26.3)'>BKT 70 Soed. W 01 (1=26.3)</option>
            <option value='BKT 70 Soed. W 01 (1=26.8)'>BKT 70 Soed. W 01 (1=26.8)</option>
            <option value='BKT 70 Soed. W 01 (1=7.8)'>BKT 70 Soed. W 01 (1=7.8)</option>
            <option value='BKT 78 Soed. (M11227-19.5mm)'>BKT 78 Soed. (M11227-19.5mm)</option>
            <option value='BKT 70 Soed. W 01 (1=10.8)'>BKT 70 Soed. W 01 (1=10.8)</option>
            <option value='BKT 70 Soed. W 02 (1=10.8)'>BKT 70 Soed. W 02 (1=10.8)</option>
            <option value='BKT 70 Soed. W 02 (1=23.6)'>BKT 70 Soed. W 02 (1=23.6)</option>
            <option value='BKT 70 Soed. W 03 (1=7.8)'>BKT 70 Soed. W 03 (1=7.8)</option>
            <option value='BKT 70 Soed. W 03 (1=10.8)'>BKT 70 Soed. W 03 (1=10.8)</option>
            <option value='BKT 70 Soed. (M11535-7.8mm)'>BKT 70 Soed. (M11535-7.8mm)</option>
            <option value='BKT 70 Soed. Impost (J01-13.6mm)'>BKT 70 Soed. Impost (J01-13.6mm)</option>
            <option value='BKT 70 Soed. W 02 (1=18.4)'>BKT 70 Soed. W 02 (1=18.4)</option>
            <option value='BKT 70 Soed. (M11055-13.6mm)'>BKT 70 Soed. (M11055-13.6mm)</option>
            <option value='BKT 70 Soed. Impost (J01-43.6mm)'>BKT 70 Soed. Impost (J01-43.6mm)</option>
            <option value='BKT 70 Soed. Impost (J05-43.6mm)'>BKT 70 Soed. Impost (J05-43.6mm)</option>
            <option value='BKT 78 Soed. (M11227-22.7mm)'>BKT 78 Soed. (M11227-22.7mm)</option>
            <option value='Chit-Chit (aldocks).uz (oq)'>Chit-Chit (aldocks).uz (oq)</option>
            <option value='Klipsa 12 mm'>Klipsa 12 mm</option>
            <option value='BKT 70 Soed. Impost (J05-23.6mm)'>BKT 70 Soed. Impost (J05-23.6mm)</option>
            <option value='Ogranichitel (oq)'>Ogranichitel (oq)</option>
            <option value='Otvetniy Plast. (rangli)'>Otvetniy Plast. (rangli)</option>
            <option value='Otvetniy Plast. (oq)'>Otvetniy Plast. (oq)</option>
            <option value='Petlya Dvernaya Alyumin (oq)'>Petlya Dvernaya Alyumin (oq)</option>
            <option value='Ruchka Kvadrat (oq)'>Ruchka Kvadrat (oq)</option>
            <option value='Soedinitel 114 D 300 (13mm)'>Soedinitel 114 D 300 (13mm)</option>
            <option value='Soedinitel 114 D 300 (6mm)'>Soedinitel 114 D 300 (6mm)</option>
            <option value='Soedinitel 114 D 400 (38mm)'>Soedinitel 114 D 400 (38mm)</option>
            <option value='Soedinitel 114 D 400 (46mm)'>Soedinitel 114 D 400 (46mm)</option>
            <option value='Soedinitel BKH-001 (6mm)'>Soedinitel BKH-001 (6mm)</option>
            <option value='Soedinitel BKH-002 (38mm)'>Soedinitel BKH-002 (38mm)</option>
            <option value='Soedinitel (Inja)'>Soedinitel (Inja)</option>
            <option value='Zashyolka Narujnyaya (new) (oq)'>Zashyolka Narujnyaya (new) (oq)</option>
            <option value='Soedinitel (Bolshoy)'>Soedinitel (Bolshoy)</option>
            <option value='Otvetniy Plast. (ALD-2) (rangli)'>Otvetniy Plast. (ALD-2) (rangli)</option>
            <option value='Otvetniy Plast. (ALD-2) (oq)'>Otvetniy Plast. (ALD-2) (oq)</option>
            <option value='BKT 70 Soed. List (A10-002)'>BKT 70 Soed. List (A10-002)</option>
            <option value='Montajnaya Planka 7000 (Metal)'>Montajnaya Planka 7000 (Metal)</option>
            <option value='Petlya (oq)'>Petlya (oq)</option>
            <option value='BKT 78 Soed. (M11227-26.9mm)'>BKT 78 Soed. (M11227-26.9mm)</option>
            <option value='Ruchka LUX Fortuna Mini O (oq)'>Ruchka LUX Fortuna Mini O (oq)</option>
            <option value='BKT 70 Soed. List (A10-003)'>BKT 70 Soed. List (A10-003)</option>
            <option value='Otvetnaya chast zamka A0275-K (155) (oq)'>Otvetnaya chast zamka A0275-K (155) (oq)</option>
            <option value='Soedinitel 114 D 400 (10mm)'>Soedinitel 114 D 400 (10mm)</option>
            <option value='Soedinitel 5505 (35mm)'>Soedinitel 5505 (35mm)</option>
            <option value='Soedinitel BKH-008 (14mm)'>Soedinitel BKH-008 (14mm)</option>
            <option value='Soedinitel BKH-008 (15mm)'>Soedinitel BKH-008 (15mm)</option>
            <option value='Soedinitel BKH-010 (6mm)'>Soedinitel BKH-010 (6mm)</option>
            <option value='Krishka Podokonnik 300 (Trapetsiya) (oq)'>Krishka Podokonnik 300 (Trapetsiya) (oq)</option>
            <option value='Ogranichitel PVH (oq)'>Ogranichitel PVH (oq)</option>
            <option value='Petlya 75 mm (oq)'>Petlya 75 mm (oq)</option>
            <option value='Petlya Dvernaya PVH (oq)'>Petlya Dvernaya PVH (oq)</option>
            <option value='Porog Soedinitel 6000 (1kom.) (L;P) (rangli)'>Porog Soedinitel 6000 (1kom.) (L;P) (rangli)</option>
            <option value='Porog Soedinitel 7000 (1kom.) (L;P) (oq)'>Porog Soedinitel 7000 (1kom.) (L;P) (oq)</option>
            <option value='Krishka Shtulp Dlya Adap 6000 (oq)'>Krishka Shtulp Dlya Adap 6000 (oq)</option>
            <option value='Krishka Podokonnik 300 (oq)'>Krishka Podokonnik 300 (oq)</option>
            <option value='Ruchka Dvernaya Fornaks (35mm) fiksator (oq)'>Ruchka Dvernaya Fornaks (35mm) fiksator (oq)</option>
            <option value='BKT 70 Soed. (M11535-22mm)'>BKT 70 Soed. (M11535-22mm)</option>
            <option value='Ruchka DELFIN (oq)'>Ruchka DELFIN (oq)</option>
            <option value='Zatsepka 5200'>Zatsepka 5200</option>
            <option value='Zatsepka 7000'>Zatsepka 7000</option>
            <option value='Zatsepka 6000'>Zatsepka 6000</option>
            <option value='Ruchka Okonaya Roto (oq)'>Ruchka Okonaya Roto (oq)</option>
            <option value='Ruchka Okonnaya PVH (oq)'>Ruchka Okonnaya PVH (oq)</option>
            <option value='Soedinitel 5200'>Soedinitel 5200</option>
            <option value='Soedinitel 6000 (TRIO)'>Soedinitel 6000 (TRIO)</option>
            <option value='Soedinitel 7000'>Soedinitel 7000</option>
            <option value='Ruchka Dvernaya Fornaks (35mm) (oq)'>Ruchka Dvernaya Fornaks (35mm) (oq)</option>
            <option value='Soedinitel 5800'>Soedinitel 5800</option>
            <option value='Soedinitel CL.X.W 38 (5.5 mm)'>Soedinitel CL.X.W 38 (5.5 mm)</option>
            <option value='Petlya Dvernaya 2SK MASTER (oq)'>Petlya Dvernaya 2SK MASTER (oq)</option>
            <option value='Soedinitel A 00018 (37mm)'>Soedinitel A 00018 (37mm)</option>
            <option value='Soedinitel CL.X.W 14 (40mm)'>Soedinitel CL.X.W 14 (40mm)</option>
            <option value='Ruchka Okonaya Rotto Swing (oq)'>Ruchka Okonaya Rotto Swing (oq)</option>
            <option value='BKT 70 Soed. Impost (J03-23.6mm)'>BKT 70 Soed. Impost (J03-23.6mm)</option>
            <option value='Ruchka Okonaya Rotto Swing (rangli)'>Ruchka Okonaya Rotto Swing (rangli)</option>
            <option value='Soedinitel CL.X.W 10 (27mm)'>Soedinitel CL.X.W 10 (27mm)</option>
            <option value='Soedinitel A 00018 (9mm)'>Soedinitel A 00018 (9mm)</option>
            <option value='Soedinitel A 00018 (25.8mm)'>Soedinitel A 00018 (25.8mm)</option>
            <option value='Soedinitel A 00018 (18mm)'>Soedinitel A 00018 (18mm)</option>
            <option value='Soedinitel CL.X.W 38 (5mm)'>Soedinitel CL.X.W 38 (5mm)</option>
            <option value='Soedinitel CL.X.W 28 (9mm)'>Soedinitel CL.X.W 28 (9mm)</option>
            <option value='Soedinitel CL.X.W 28 (25.8mm)'>Soedinitel CL.X.W 28 (25.8mm)</option>
            <option value='Soedinitel CL.X.W 28 (18mm)'>Soedinitel CL.X.W 28 (18mm)</option>
            <option value='Soedinitel CL.X.W 24 (5mm)'>Soedinitel CL.X.W 24 (5mm)</option>
            <option value='Soedinitel CL.X.W 38 (5.8mm)'>Soedinitel CL.X.W 38 (5.8mm)</option>
            <option value='Soedinitel CL.X.W 38 (6.8mm)'>Soedinitel CL.X.W 38 (6.8mm)</option>
            <option value='Soedinitel CL.X.W 14 (22.5mm)'>Soedinitel CL.X.W 14 (22.5mm)</option>
            <option value='Soedinitel CL.X.W 34 (34.3mm)'>Soedinitel CL.X.W 34 (34.3mm)</option>
            <option value='BKT 70 Soed. Impost (J01-16mm)'>BKT 70 Soed. Impost (J01-16mm)</option>
            <option value='Soedinitel CL.X.W 05 (13mm)'>Soedinitel CL.X.W 05 (13mm)</option>
            <option value='Soedinitel CL.X.W 20 (27mm)'>Soedinitel CL.X.W 20 (27mm)</option>
            <option value='Soedinitel CL.X.W 20 (18,8mm)'>Soedinitel CL.X.W 20 (18,8mm)</option>
            <option value='Soedinitel CL.X.W 20 (6mm)'>Soedinitel CL.X.W 20 (6mm)</option>
            <option value='Soedinitel CL.X.W 34 (18,8mm)'>Soedinitel CL.X.W 34 (18,8mm)</option>
            <option value='BKT 70 Soed. Impost (J01-23.6mm)'>BKT 70 Soed. Impost (J01-23.6mm)</option>
            <option value='Ruchka Dvernaya Fornaks (30mm) (oq)'>Ruchka Dvernaya Fornaks (30mm) (oq)</option>
            <option value='Ruchka Dvernaya mini (oq)'>Ruchka Dvernaya mini (oq)</option>
            <option value='Ruchka dvernaya "BELLA" (2250) mm (rangli)'>Ruchka dvernaya "BELLA" (2250) mm (rangli)</option>
            <option value='Otvetka Mini 153 (oq)'>Otvetka Mini 153 (oq)</option>
            <option value='Soedinitel CL.X.W 14 (6mm)'>Soedinitel CL.X.W 14 (6mm)</option>
            <option value='Soedinitel CLSW 22'>Soedinitel CLSW 22</option>
            <option value='Ruchka "Simple" (oq)'>Ruchka "Simple" (oq)</option>
            <option value='Soedinitel CL.X.W 10 (18,8mm)'>Soedinitel CL.X.W 10 (18,8mm)</option>
            <option value='Soedinitel CL.X.W 10 (6mm)'>Soedinitel CL.X.W 10 (6mm)</option>
            <option value='Ruchka "Simple"(rangli)'>Ruchka "Simple"(rangli)</option>
            <option value='Vstavka (PVCC 005) (rangli)'>Vstavka (PVCC 005) (rangli)</option>
            <option value='Zaglushka (PVCC 002) (rangli)'>Zaglushka (PVCC 002) (rangli)</option>
            <option value='Soedinitel (PVCC 022)'>Soedinitel (PVCC 022)</option>
            <option value='Krishka (PVCC 001) (rangli)'>Krishka (PVCC 001) (rangli)</option>
            <option value='Termo vstavka (PVCC 003) (rangli)'>Termo vstavka (PVCC 003) (rangli)</option>
            <option value='Termo vstavka (PVCC 004) (rangli)'>Termo vstavka (PVCC 004) (rangli)</option>
            <option value='Ruchka Dvernaya Fornaks (30mm) fiksator (oq)'>Ruchka Dvernaya Fornaks (30mm) fiksator (oq)</option>
            <option value='Soedinitel CL.X.W 10 (17mm)'>Soedinitel CL.X.W 10 (17mm)</option>
            <option value='Zaglushka (PVCC 035) (rangli)'>Zaglushka (PVCC 035) (rangli)</option>
            <option value='Ruchka dvernaya "BELLA" (750) mm (rangli)'>Ruchka dvernaya "BELLA" (750) mm (rangli)</option>
            <option value='Soedinitel CL.X.W 38 (44.4mm)'>Soedinitel CL.X.W 38 (44.4mm)</option>
            <option value='Soedinitel CL.X.W 16 (44.4mm)'>Soedinitel CL.X.W 16 (44.4mm)</option>
            <option value='Ruchka dvernaya "BELLA" (500) mm (rangli)'>Ruchka dvernaya "BELLA" (500) mm (rangli)</option>
            <option value='Krishka Podokonnik 350 (Ovolniy) (oq)'>Krishka Podokonnik 350 (Ovolniy) (oq)</option>
            <option value='Soedinitel CL.X.W 14 (21.5mm)'>Soedinitel CL.X.W 14 (21.5mm)</option>
            <option value='Ruchka dvernaya "BELLA" (2350) mm (rangli)'>Ruchka dvernaya "BELLA" (2350) mm (rangli)</option>
            <option value='Zaglushka (PVCC 034) (rangli)'>Zaglushka (PVCC 034) (rangli)</option>
            <option value='Ruchka dvernaya "BELLA" (2000) mm (rangli)'>Ruchka dvernaya "BELLA" (2000) mm (rangli)</option>
            <option value='Soedinitel CL.X.W 34 (28.7mm)'>Soedinitel CL.X.W 34 (28.7mm)</option>
            <option value='Ruchka dvernaya "BELLA" (1200) mm (rangli)'>Ruchka dvernaya "BELLA" (1200) mm (rangli)</option>
            <option value='Ruchka Dvernaya (28mm) Slim fiksator (oq)'>Ruchka Dvernaya (28mm) Slim fiksator (oq)</option>
            <option value='BKT 70 Soed. W 02 (1=25.8)'>BKT 70 Soed. W 02 (1=25.8)</option>
            <option value='Derjatel i ruchka-koltso dlya moskitnoy setki (rangli)'>Derjatel i ruchka-koltso dlya moskitnoy setki (rangli)</option>
            <option value='Ручка к конструкции москитной сетки серии 10х20. "AKBULUT" цветной'>Ручка к конструкции москитной сетки серии 10х20. "AKBULUT" цветной</option>
            <option value='Ручка к конструкции москитной сетки серии 10х20 "AKBULUT"белый'>Ручка к конструкции москитной сетки серии 10х20 "AKBULUT"белый</option>
            <option value='Ruchka dvernaya "BELLA" (2300) mm (rangli)'>Ruchka dvernaya "BELLA" (2300) mm (rangli)</option>
            <option value='Takos PVH'>Takos PVH</option>
            <option value='BKT 70 Soed. W 02 (1=26.3)'>BKT 70 Soed. W 02 (1=26.3)</option>
            <option value='BKT 70 Soed. W 02 (1=5.1)'>BKT 70 Soed. W 02 (1=5.1)</option>
            <option value='BKT 70 Soed. W 03 (1=18.4)'>BKT 70 Soed. W 03 (1=18.4)</option>
            <option value='BKT 70 Soed. W 03 (1=26.3)'>BKT 70 Soed. W 03 (1=26.3)</option>
            <option value='BKT 70 Soed. W 03 (1=5.1)'>BKT 70 Soed. W 03 (1=5.1)</option>
            <option value='Derjatel i ruchka-koltso dlya moskitnoy setki (oq)'>Derjatel i ruchka-koltso dlya moskitnoy setki (oq)</option>
            <option value='BKT 70 Soed. Impost (J03-13.6mm)'>BKT 70 Soed. Impost (J03-13.6mm)</option>
            <option value='Porog Soedinitel 6000 (1kom.) (L;P) (oq)'>Porog Soedinitel 6000 (1kom.) (L;P) (oq)</option>
            <option value='Montajnaya Planka 6000 (Metal)'>Montajnaya Planka 6000 (Metal)</option>
            <option value='BKT 70 Soed. Impost (J05-13.6mm)'>BKT 70 Soed. Impost (J05-13.6mm)</option>
            <option value='Soedinitel BKH-010 (42mm)'>Soedinitel BKH-010 (42mm)</option>
            <option value='Ruchka Dvernaya Fornaks (28mm) (oq)'>Ruchka Dvernaya Fornaks (28mm) (oq)</option>
            <option value='Otvetnaya chast zamka A0275-K (153) (oq)'>Otvetnaya chast zamka A0275-K (153) (oq)</option>
            <option value='Soedinitel CL.X.W 14 (25.8mm)'>Soedinitel CL.X.W 14 (25.8mm)</option>
            <option value='Soedinitel 114 D 300 (35mm)'>Soedinitel 114 D 300 (35mm)</option>
            <option value='Ruchka Dvernaya Fornaks (28mm) fiksator (oq)'>Ruchka Dvernaya Fornaks (28mm) fiksator (oq)</option>
            <option value='BKT 70 Soed. (M11535-18.4mm)'>BKT 70 Soed. (M11535-18.4mm)</option>
            <option value='Soedinitel CL.X.W 10 (10mm)'>Soedinitel CL.X.W 10 (10mm)</option>
            <option value='Soedinitel CL.X.W 20 (20mm)'>Soedinitel CL.X.W 20 (20mm)</option>
            <option value='EPDM L-65 угловой соединитель для уплотнителей'>EPDM L-65 угловой соединитель для уплотнителей</option>
            <option value='EPDM заглушка для штульпа "Чемпион"'>EPDM заглушка для штульпа "Чемпион"</option>
            <option value='EPDM адаптер крышка для Термо 78'>EPDM адаптер крышка для Термо 78</option>
            <option value='EPDM А01 105 угловой соединитель для уплотнителей'>EPDM А01 105 угловой соединитель для уплотнителей</option>
            <option value='EPDM ССЕР 0057 адаптер крышка'>EPDM ССЕР 0057 адаптер крышка</option>
            <option value='EPDM ССЕР 0058 адаптер крышка'>EPDM ССЕР 0058 адаптер крышка</option>
            <option value='EPDM D 017500 Decor Zaglushka'>EPDM D 017500 Decor Zaglushka</option>
            <option value='EPDM адаптер крышка для Термо 70 (BKT-70)'>EPDM адаптер крышка для Термо 70 (BKT-70)</option>
            <option value='EPDM крышка для штульпа АК-40'>EPDM крышка для штульпа АК-40</option>
            <option value='EPDM адаптер крышка 012'>EPDM адаптер крышка 012</option>
            <option value='EPDM epdc 004 дренажный носик'>EPDM epdc 004 дренажный носик</option>
            <option value='EPDM 5108 угловой соединитель для уплотнителей'>EPDM 5108 угловой соединитель для уплотнителей</option>
            <option value='Термоуплотненный окрашенный алюминиевый профиль'>Термоуплотненный окрашенный алюминиевый профиль</option>
            <option value='Неокрашенный алюминиевый профиль (N)'>Неокрашенный алюминиевый профиль (N)</option>
            <option value='Алюминиевый профиль (N)'>Алюминиевый профиль (N)</option>
            <option value='EPDM уплотнитель'>EPDM уплотнитель</option>
            <option value='Анодированный алюминиевый профиль (N)'>Анодированный алюминиевый профиль (N)</option>
            <option value='Термоуплотненный алюминиевый профиль (N)'>Термоуплотненный алюминиевый профиль (N)</option>
            <option value='Мебельный профиль из алюминия анодированный матовое серебро (N)'>Мебельный профиль из алюминия анодированный матовое серебро (N)</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;display:none" id='buxgalter_uchot`+String(i)+`' required>
            <option  selected></option>
            <option  value="Штука">Штука</div>
            <option  value="Килограмм">Килограмм</div>
            <option  value="Квадратный метр">Квадратный метр</div>
            <option  value="Метр">Метр</div>
            <option  value="КМП">КМП</div>
            <option  value="Пачка">Пачка</div>
            <option  value="Секция">Секция</div>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;" id='bazoviy_edin`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option vlaue="Штука">Штука</div>
            <option vlaue="Килограмм">Килограмм</div>
            <option vlaue="Квадратный метр">Квадратный метр</div>
            <option vlaue="Метр">Метр</div>
            <option vlaue="КМП">КМП</div>
            <option vlaue="Пачка">Пачка</div>
            <option vlaue="Секция">Секция</div>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;display:none" id='alter_edin`+ String(i)+`'  required>
            <option  selected></option>
            <option vlaue="Штука">Штука</div>
            <option vlaue="Килограмм">Килограмм</div>
            <option vlaue="Квадратный метр">Квадратный метр</div>
            <option vlaue="Метр">Метр</div>
            <option vlaue="КМП">КМП</div>
            <option vlaue="Пачка">Пачка</div>
            <option vlaue="Секция">Секция</div>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="width: 75px; font-size:10px; display:none;" id='stoimost_baza`+String(i)+`'  ></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style="width: 75px; font-size:10px; display:none" id='stoimost_alter`+String(i)+`'  ></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;" id='status`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option value="Активный">Активный</option>
            <option value="Пассивный">Пассивный</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <span class =' text-center ' style="font-size: small; width:190px; font-weight: bold; text-transform: uppercase;" id='zavod_name`+String(i)+`'></span>
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
    
    $('.select2-selection__rendered').css('font-size', '15 px');
    
    
    
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
data_base['columns']= 5


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


function create(i){
    
    var artikul = $('#artikul'+i)
    
    artikul.attr('disabled',false)

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
    
    var activate_btn =$('#activate_btn'+i);
    activate_btn.attr('disabled',true)
    var create_btn =$('#create_btn'+i);
    create_btn.attr('disabled',true)
    
   

}

function activate(i){
    // data_base[i] = new OnlineSavdo()

    var artikul = $('#artikul'+i)
    
    artikul.attr('disabled',false)

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





    var activate_btn =$('#activate_btn'+i);
    var create_btn =$('#create_btn'+i);
    activate_btn.attr('disabled',true)
    create_btn.attr('disabled',true)




    // scrollToTd()


}


function scrollToTd(tdIndex=30) {
    var table = document.getElementById("my-table");
        var td = table.rows[0].cells[tdIndex];
        var container = document.getElementById("table-container");
        var targetScrollX = td.offsetLeft;
        var currentScrollX = container.scrollLeft;
        var distance = Math.abs(targetScrollX - currentScrollX);
        var step = 250; 

        function scroll() {
            if (currentScrollX < targetScrollX) {
                currentScrollX += step;
                if (currentScrollX >= targetScrollX) {
                    currentScrollX = targetScrollX;
                }
            } else {
                currentScrollX -= step;
                if (currentScrollX <= targetScrollX) {
                    currentScrollX = targetScrollX;
                }
            }
            container.scrollLeft = currentScrollX;
            if (currentScrollX !== targetScrollX) {
                window.requestAnimationFrame(scroll);
            }
        }

        scroll();
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

    var nakleyka_nt1 = $('#nakleyka_nt'+String(id))
    var nakleyka_org =$('#nakleyka_org'+String(id));
    var nakleyka_select = $('#nakleyka_select'+String(id));
    nakleyka_nt1.css('display','none');
    nakleyka_org.css('display','none');
    nakleyka_select.css('display','none');


    var splav = $('#splav'+String(id));
    splav.val('0').change();
    splav.attr("disabled",true);
    splav.css("border-color",'#dedad9');
    var tip_zakalyonnosti = $('#tip_zakalyonnosti'+String(id));
    tip_zakalyonnosti.val('0').change();
    tip_zakalyonnosti.attr("disabled",true);
    tip_zakalyonnosti.css("border-color",'#dedad9');
    // console.log(data_base)
    // console.log(typeof(data_base))
    
}

function artukil_clear(id){
    $('#artikul'+id).val(null).trigger('change');
    clear_artikul(id)
    $('#artikul'+id).attr('disabled',true)

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
    var segment =$('#segment'+id);
    var buxgalter_tovar =$('#buxgalter_tovar'+id);
    var zavod_name =$('#zavod_name'+id)
    zavod_name.text('')


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
    sap_code_ruchnoy.css('display','none')
    sap_code_ruchnoy.css('border-color','red')
    kratkiy_tekst_ruchnoy.css('display','none')
    kratkiy_tekst_ruchnoy.css('border-color','red')
    online_savdo_id.css('display','none')
    online_savdo_id.css('border-color','red')
    nazvaniye_ruchnoy.css('display','none')
    nazvaniye_ruchnoy.css('border-color','red')


    svet_product.css('border-color','red')
    group_zakup.css('border-color','red')
    group.css('border-color','red')
    tip.css('border-color','red')
    bazoviy_edin.css('border-color','red')
    status.css('border-color','red')
    zavod.css('border-color','red')

    
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
    zavod.val('')
    buxgalter_uchot.val('')
    alter_edin.val('')
    stoimost_baza.val('')
    stoimost_alter.val('')
    segment.val('')
    buxgalter_tovar.val('')
    
    var create_btn =$('#create_btn'+id);
    var activate_btn =$('#activate_btn'+id);

    create_btn.attr('disabled',false)
    activate_btn.attr('disabled',false)



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
    
    var contactnost_anodirovki = $('#contactnost_anodirovki'+String(id));
    if(data_base[id]){
        contactnost_anodirovki.val('0').change();
    }
    contactnost_anodirovki.attr("disabled",true);
    contactnost_anodirovki.css("border-color",'#dedad9');


    var splav = $('#splav'+String(id));
    // console.log(splav,'splavvvv')
    splav.attr("disabled",false);
    splav.css("border-color","#fc2003");
    var tip_zakalyonnosti = $('#tip_zakalyonnosti'+String(id));
    tip_zakalyonnosti.attr("disabled",false);
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
        var code_kras_snaruji =`<input type="text"  class="form-control " id ='code_kraski_snar`+String(id)+`' aria-describedby="inputGroup-sizing-sm" style="border-color: red;width:65px; height:30px"  onkeyup="create_kratkiy_tekst(`+String(id)+`)" required>`
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
    create_kratkiy_tekst(id);
}





function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
    var obj_name = data_base[id].constructor.name
    
    var kratkiy_tekst = $('#kratkiy_tekst'+String(id));
    var combination= $('#combination'+String(id));
    combination_text = combination.text();
    var val = $('#tip_pokritiya'+String(id)).val();
    var dlina = $('#length'+String(id));

    if(obj_name != 'OnlineSavdo'){
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
                if(code_kraski_vnut.val() != '0' && code_kraski_vnut.val()  != undefined && code_kraski_vnut.val()  != ''){
                    code_kraski_vnut.css("border-color",'#dedad9');
                    data_base[id].kod_kraska_vn =code_kraski_vnut.val();
                }else{
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
        var zavod =$('#zavod'+id);
        
        
    
    
        
        if(sap_code_ruchnoy.val()!=''){
            data_base[id].sap_code = sap_code_ruchnoy.val();
            sap_code_ruchnoy.css('border-color','#dedad9')
        }else{
            data_base[id].sap_code = NaN;
            sap_code_ruchnoy.css('border-color','red')
        }
        if(kratkiy_tekst_ruchnoy.val()!=''){
            data_base[id].krat = kratkiy_tekst_ruchnoy.val();
            kratkiy_tekst_ruchnoy.css('border-color','#dedad9')
        }else{
            data_base[id].krat = NaN;
            kratkiy_tekst_ruchnoy.css('border-color','red')
        }
        if(online_savdo_id.val()!=''){
            online_savdo_id.css('border-color','#dedad9')
            data_base[id].online_id = online_savdo_id.val();
        }else{
            data_base[id].online_id = NaN;
            online_savdo_id.css('border-color','red')
        }
        if(nazvaniye_ruchnoy.val()!=''){
            nazvaniye_ruchnoy.css('border-color','#dedad9')
            data_base[id].nazvaniye_ruchnoy = nazvaniye_ruchnoy.val();
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
        console.log(data_base[id])
        if(status.val()!=''){
            status.css('border-color','#dedad9')
            data_base[id].status_online = status.val();
        }else{
            data_base[id].status_online =NaN;
            status.css('border-color','red')
        }
        if(zavod.val()!=''){
            zavod.css('border-color','#dedad9')
            var zavod_name =$('#zavod_name'+id)
            zavod_name.text(zavod.val())
            data_base[id].zavod = zavod.val();
        }else{
            var zavod_name =$('#zavod_name'+id)
            zavod_name.text('')
            data_base[id].zavod =NaN;
            
            zavod.css('border-color','red')
        }
    }




    



    var data =data_base[id].get_kratkiy_tekst()
    console.log(data.text,data.accept)
    if(data.accept){
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','#2de319')
    }else{
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','white')

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
                <button type="button" class="btn btn-secondary btn-sm" onclick="create(`+String(i)+`)" id='create_btn`+String(i)+`' >Создание</button>
                <button type="button" class="btn btn-info btn-sm" onclick="activate(`+String(i)+`)" id='activate_btn`+String(i)+`'>Активация</button>
                <button type="button" class="btn btn-warning btn-sm gradient-buttons" onclick="artukil_clear(`+String(i)+`)"  id='clear_btn`+String(i)+`'>Очистить</button>
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
                <select class=" form-control basic_artikul" style="background-color:#ddebf7; width: 140px; font-size:10px " disabled id="artikul`+String(i)+`" onchange='clear_artikul(`+String(i)+`)'></select>
            </div>
        </td>
        
        
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type="text" class="form-control " style='width:50px' onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled aria-describedby="inputGroup-sizing-sm" name ='length`+String(i)+`' id="length`+String(i)+`"  >
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
                <option  value="" selected ></option>
                <option value="63" >63</option>
            </select>
            
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1"  style="width: 60px;">
            <select class="form-select" aria-label="" style="width: 50px;!important"  disabled id='tip_zakalyonnosti`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option  value="" selected></option>
                <option value="T4" >T4</option>
                <option value="T6" >T6</option>
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
                <span class =' text-center' style="font-size: small; font-weight: bold; text-transform: uppercase; width:100px" id ='code_kraski_vnutri` +String(i)+`'></span>
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
                <em><span class =' text-center ' style="font-size: 10px;  font-weight: bold; text-transform: uppercase;" id ='code_dekplonka_vnutri` +String(i)+`' disabled></span></em>
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
           
            <input type='text' class=" form-control " style="  border-color:red;width: 110px; font-size:10px; display:none; " id='sap_code_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        
            </div>
        </td> 
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 220px; font-size:10px; display:none; "  id='kratkiy_tekst_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
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
            <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px; display:none;" id='online_savdo_id`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <textarea   rows='1' class=" form-control " style="border-color:red; width: 220px; font-size:10px; display:none; " id='nazvaniye_ruchnoy`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></textarea >
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




