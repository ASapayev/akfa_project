class BasePokritiya{
    constructor(
        full=false, 
        id=NaN,
        nazvaniye_system=NaN,
        base_artikul=NaN,
        dlina=NaN,
        tip_pokritiya=NaN,
        splav=NaN,
        tip_zak=NaN,
        combination=NaN,
        brend_kraska_sn=NaN,
        kod_kraska_sn=NaN,
        brend_kraska_vn=NaN,
        kod_kraska_vn=NaN,
        kod_dekor_sn=NaN,
        svet_dekplonka_snaruji=NaN,
        kod_dekor_vn=NaN,
        svet_dekplonka_vnutri=NaN,
        svet_lamplonka_snaruji=NaN,
        kod_lam_sn=NaN,
        svet_lamplonka_vnutri=NaN,
        kod_lam_vn=NaN,
        kod_anod_sn=NaN,
        kod_anod_vn=NaN,
        contactnost_anod=NaN,
        tip_anod=NaN,
        sposob_anod=NaN,
        kod_nakleyki=NaN,
        nadpis_nakleyki=NaN,
        baza_profiley=NaN,
        goods_group=NaN,
        tex_name=NaN,
        gruppa_materialov=NaN,
        kratkiy_tekst=NaN,
        sap_code_ruchnoy=NaN,
        kratkiy_text_ruchnoy=NaN,
        klaes_id=NaN,
        klaes_nazvaniye=NaN,
        kod_sveta=NaN,
        kratkiy_klaes=NaN,
        comment=NaN,
        is_termo=false) {
            this.full=full;
            this.id =id;
            this.nazvaniye_system =nazvaniye_system;
            this.base_artikul =base_artikul;
            this.dlina =dlina;
            this.tip_pokritiya =tip_pokritiya;
            this.splav =splav;
            this.tip_zak =tip_zak;
            this.combination =combination;
            this.brend_kraska_sn =brend_kraska_sn;
            this.kod_kraska_sn =kod_kraska_sn;
            this.brend_kraska_vn =brend_kraska_vn;
            this.kod_kraska_vn =kod_kraska_vn;
            this.kod_dekor_sn =kod_dekor_sn;
            this.svet_dekplonka_snaruji =svet_dekplonka_snaruji;
            this.kod_dekor_vn =kod_dekor_vn;
            this.svet_dekplonka_vnutri =svet_dekplonka_vnutri;
            this.svet_lamplonka_snaruji =svet_lamplonka_snaruji;
            this.kod_lam_sn =kod_lam_sn;
            this.svet_lamplonka_vnutri =svet_lamplonka_vnutri;
            this.kod_lam_vn =kod_lam_vn;
            this.kod_anod_sn =kod_anod_sn;
            this.kod_anod_vn =kod_anod_vn;
            this.contactnost_anod =contactnost_anod;
            this.tip_anod =tip_anod;
            this.sposob_anod =sposob_anod;
            this.kod_nakleyki =kod_nakleyki;
            this.nadpis_nakleyki =nadpis_nakleyki;
            this.baza_profiley =baza_profiley;
            this.goods_group =goods_group;
            this.tex_name =tex_name;
            this.gruppa_materialov =gruppa_materialov;
            this.kratkiy_tekst =kratkiy_tekst;
            this.sap_code_ruchnoy =sap_code_ruchnoy;
            this.kratkiy_text_ruchnoy =kratkiy_text_ruchnoy;
            this.klaes_id =klaes_id;
            this.klaes_nazvaniye =klaes_nazvaniye;
            this.kod_sveta =kod_sveta;
            this.kratkiy_klaes =kratkiy_klaes;
            this.comment =comment;
            this.is_termo= is_termo;
    }


    get_kratkiy_tekst(){
        switch(this.id){
            case 1: if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.kod_kraska_sn && this.kod_nakleyki ){
                    if( this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){

                        return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':true}
                    }else{
                        return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':false}
                    }
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
                    if(this.splav && this.tip_zak && this.dlina && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki ){
                        if(this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){

                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_kraska_sn +'/'+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_kraska_sn +'/'+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':false}
                        }
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }
                break;
            case 2: if(!this.is_termo){

                if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_nakleyki ){
                    if(this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){

                        return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':true}
                    }else{
                        return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':false}
                    }
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
        
                    if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki){
                        if(this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){

                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':false}
                        }
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                } break;
            case 3:if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_nakleyki){
                    if(this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){

                        return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':true}
                    }else{
                        return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':false}
                    }
                    
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
                   if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki){
                    if(this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){

                        return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn+'/'+this.brend_kraska_vn+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':true}
                    }else{
                        return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn+'/'+this.brend_kraska_vn+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':false}
                    }
                        
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }break;
            case 4:if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki){
                    if(this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){

                        return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':true}
                    }else{
                        return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':false}
                    }
                    
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
                    if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki){
                        if(this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){

                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn + this.kod_kraska_vn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn + this.kod_kraska_vn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':false}
                        }
                        
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }break;
            case 5:if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_dekor_sn && this.kod_nakleyki){
                    if(this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){

                        return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_dekor_sn + ' ' +this.kod_nakleyki,'accept':true}
                    }else{
                        return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_dekor_sn + ' ' +this.kod_nakleyki,'accept':false}
                    }
                    
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
                    if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_dekor_sn && this.kod_dekor_vn && this.kod_nakleyki){
                        if(this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){

                            return {'text': this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+'_'+this.kod_dekor_sn+'/'+this.kod_dekor_vn + ' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text': this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+'_'+this.kod_dekor_sn+'/'+this.kod_dekor_vn + ' ' +this.kod_nakleyki,'accept':false}
                        }
                        
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }break;
            case 6:if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.kod_anod_sn && this.kod_nakleyki && this.contactnost_anod){
                    if(this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){

                        return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_anod_sn + ' ' + this.contactnost_anod + ' ' + this.kod_nakleyki,'accept':true}
                    }else{
                        return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_anod_sn + ' ' + this.contactnost_anod + ' ' + this.kod_nakleyki,'accept':false}
                    }
                    
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
                    if(this.splav && this.tip_zak && this.dlina && this.kod_anod_sn && this.kod_anod_vn && this.kod_nakleyki && this.contactnost_anod){
                        if(this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){

                            return {'text': this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_anod_sn +'/'+this.kod_anod_vn+ ' ' + this.contactnost_anod + ' ' + this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text': this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_anod_sn +'/'+this.kod_anod_vn+ ' ' + this.contactnost_anod + ' ' + this.kod_nakleyki,'accept':false}
                        }
                        
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
        
                }break;
        }
        
    }
  }

text =""

var jsonData = JSON.parse(JSON.parse(document.getElementById('items-data').textContent)).data;

data_base = {}

var ii = 1

for(var key1 in jsonData){
    data_base[ii] = new BasePokritiya()
    for(var key2 in jsonData[key1]){
        data_base[ii][key2] = jsonData[key1][key2]
    }
    ii += 1 
}


const lengthOfObject = Object.keys(jsonData).length;

i = 0
var order_type =$('#order_type').text()


var nakleyka_list = document.getElementById('nakleyka_list').outerHTML


function front_piece(start=1,end=6){
    text =""
    for (let i = start; i < end; i++) {

        nakleyki = nakleyka_list.replace('nakleyka_list',"nakleyka"+String(i))
        nakleyki = nakleyki.replace('onchange=""','onchange="create_kratkiy_tekst('+String(i)+')"')
       
    
        text +=`
        <tr id='table_tr` +String(i)+`' >
                                    
        <td >
            <div class="input-group input-group-sm mb-1">
                <div><span class ='nazvaniye_system` +String(i)+`'style="text-transform: uppercase;" style="font-size: 12px;"></span></div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class=" form-control" style="background-color:#ddebf7; width: 140px; font-size:10px" id="artikul`+String(i)+`" ></select>
                <span style='display:none' id ='nakleyka_codd` +String(i)+`'></span>
            </div>
        </td>
        
        
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type="text" class="form-control "  style='width:50px' onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled aria-describedby="inputGroup-sizing-sm"  name ='length`+String(i)+`' id="length`+String(i)+`"  maxlength="4" >
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
            <select class="form-select form-select-sm text-center"  style="width:65px;border-color:#fc2003;display:none" id='brand_k_snaruji`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)" required>
                <option  value="0" selected></option>
                <option value="NT1">NT1</option>
                <option value="A">A</option>
                <option value="B">B</option>
                <option value="R">R</option>
                <option value="T">T</option>
                <option value="J">J</option>
                <option value="P">P</option>
                <option value="M">M</option>
            </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 100px;">
            <select class="form-select form-select-sm text-center"  style="width:100px;border-color:#fc2003;display:none" id='code_kraski_snar`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)" required>
                                    <option  value="0" selected></option>
                                    <option value="MF">MF</option>
                                    <option value="8M01">8M01</option>
                                    <option value="6029">6029</option>
                                    <option value="1013">1013</option>
                                    <option value="7M43">7M43</option>
                                    <option value="8002">8002</option>
                                    <option value="7M24">7M24</option>
                                    <option value="7M16">7M16</option>
                                    <option value="7043">7043</option>
                                    <option value="7021">7021</option>
                                    <option value="7015">7015</option>
                                    <option value="7039">7039</option>
                                    <option value="7011">7011</option>
                                    <option value="7M47">7M47</option>
                                    <option value="9016">9016</option>
                                    <option value="7016">7016</option>
                                    <option value="2654">2654</option>
                                    <option value="9010">9010</option>
                                    <option value="9M05">9M05</option>
                                    <option value="9005">9005</option>
                                    <option value="3884">3884</option>
                                    <option value="3774">3774</option>
                                    <option value="235G">235G</option>
                                    <option value="7M21">7M21</option>
                                    <option value="355F">355F</option>
                                    <option value="8001">8001</option>
                                    <option value="8019">8019</option>
                                    <option value="8017">8017</option>
                                    <option value="9006">9006</option>
                                    <option value="306G">306G</option>
                                    <option value="9011">9011</option>
                                    <option value="2M06">2M06</option>
                                    <option value="8M19">8M19</option>
                                    <option value="8003">8003</option>
                                    <option value="2900">2900</option>
                                    <option value="7037">7037</option>
                                    <option value="281F">281F</option>
                                    <option value="1019">1019</option>
                                    <option value="7M22">7M22</option>
                                    <option value="7M31">7M31</option>
                                    <option value="9M07">9M07</option>
                                    <option value="9M16">9M16</option>
                                    <option value="7M35">7M35</option>
                                    <option value="9007">9007</option>
                                    <option value="5002">5002</option>
                                    <option value="7024">7024</option>
                                    <option value="2604">2604</option>
                                    <option value="7035">7035</option>
                                    <option value="7M36">7M36</option>
                                    <option value="7042">7042</option>
                                    <option value="9M03">9M03</option>
                                    <option value="7006">7006</option>
                                    <option value="9M04">9M04</option>
                                    <option value="9003">9003</option>
                                    <option value="2M04">2M04</option>
                                    <option value="283F">283F</option>
                                    <option value="7038">7038</option>
                                    <option value="1035">1035</option>
                                    <option value="7M39">7M39</option>
                                    <option value="2303">2303</option>
                                    <option value="3020">3020</option>
                                    <option value="8M24">8M24</option>
                                    <option value="7M12">7M12</option>
                                    <option value="9001">9001</option>
                                    <option value="7M06">7M06</option>
                                    <option value="8000">8000</option>
                                    <option value="1015">1015</option>
                                    <option value="7030">7030</option>
                                    <option value="8024">8024</option>
                                    <option value="1376">1376</option>
                                    <option value="S352">S352</option>
                                    <option value="8077">8077</option>
                                </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select form-select-sm text-center"  style="width:65px;border-color:#fc2003;display:none" id='brand_k_vnutri`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)" required>
                <option  value="0" selected></option>
                <option value="A">A</option>
                <option value="B">B</option>
                <option value="R">R</option>
                <option value="T">T</option>
                <option value="J">J</option>
                <option value="P">P</option>
                <option value="M">M</option>
            </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 100px;">
            <select class="form-select form-select-sm text-center"  style="width:100px;border-color:#fc2003;display:none" id='code_kraski_vnut`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)" required>
                                    <option  value="0" selected></option>
                                    <option value="MF">MF</option>
                                    <option value="8M01">8M01</option>
                                    <option value="6029">6029</option>
                                    <option value="1013">1013</option>
                                    <option value="7M43">7M43</option>
                                    <option value="8002">8002</option>
                                    <option value="7M24">7M24</option>
                                    <option value="7M16">7M16</option>
                                    <option value="7043">7043</option>
                                    <option value="7021">7021</option>
                                    <option value="7015">7015</option>
                                    <option value="7039">7039</option>
                                    <option value="7011">7011</option>
                                    <option value="7M47">7M47</option>
                                    <option value="9016">9016</option>
                                    <option value="7016">7016</option>
                                    <option value="2654">2654</option>
                                    <option value="9010">9010</option>
                                    <option value="9M05">9M05</option>
                                    <option value="9005">9005</option>
                                    <option value="3884">3884</option>
                                    <option value="3774">3774</option>
                                    <option value="235G">235G</option>
                                    <option value="7M21">7M21</option>
                                    <option value="355F">355F</option>
                                    <option value="8001">8001</option>
                                    <option value="8019">8019</option>
                                    <option value="8017">8017</option>
                                    <option value="9006">9006</option>
                                    <option value="306G">306G</option>
                                    <option value="9011">9011</option>
                                    <option value="2M06">2M06</option>
                                    <option value="8M19">8M19</option>
                                    <option value="8003">8003</option>
                                    <option value="2900">2900</option>
                                    <option value="7037">7037</option>
                                    <option value="281F">281F</option>
                                    <option value="1019">1019</option>
                                    <option value="7M22">7M22</option>
                                    <option value="7M31">7M31</option>
                                    <option value="9M07">9M07</option>
                                    <option value="9M16">9M16</option>
                                    <option value="7M35">7M35</option>
                                    <option value="9007">9007</option>
                                    <option value="5002">5002</option>
                                    <option value="7024">7024</option>
                                    <option value="2604">2604</option>
                                    <option value="7035">7035</option>
                                    <option value="7M36">7M36</option>
                                    <option value="7042">7042</option>
                                    <option value="9M03">9M03</option>
                                    <option value="7006">7006</option>
                                    <option value="9M04">9M04</option>
                                    <option value="9003">9003</option>
                                    <option value="2M04">2M04</option>
                                    <option value="283F">283F</option>
                                    <option value="7038">7038</option>
                                    <option value="1035">1035</option>
                                    <option value="7M39">7M39</option>
                                    <option value="2303">2303</option>
                                    <option value="3020">3020</option>
                                    <option value="8M24">8M24</option>
                                    <option value="7M12">7M12</option>
                                    <option value="9001">9001</option>
                                    <option value="7M06">7M06</option>
                                    <option value="8000">8000</option>
                                    <option value="1015">1015</option>
                                    <option value="7030">7030</option>
                                    <option value="8024">8024</option>
                                    <option value="1376">1376</option>
                                    <option value="S352">S352</option>
                                    <option value="8077">8077</option>
                                </select>
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
                
                    <em><span class =' text-center ' style="font-size: 10px;  font-weight: bold; text-transform: uppercase;" id ='code_dekplonka_snaruji` +String(i)+`' disabled ></span></em>
                
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
                
                <em><span class =' text-center ' style="font-size: 10px; font-weight: bold; text-transform: uppercase;" id ='code_dekplonka_vnutri` +String(i)+`' disabled></span></em>
                
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
            <div id='anod`+String(i)+`' class='anood'  style="width: 75px;border-color:red; display:none;" >
                <select class="form-select kod_anod_snar" aria-label="" style=" width: 100px; border-color:#fc2003;!important; display:none" onchange="code_svet_anodirovki_snaruji_selected(`+String(i)+`,this.value)"  id='code_svet_anodirovki_snaruji`+String(i)+`' required></select>         
            </div>   
            </div>
        </td> 
        <td class='mr-2'>
            <div class="input-group input-group-sm mr-1 pr-5 mr-1" style="width: 75px;">
            <div id='anod_vnutr`+String(i)+`'  style="width: 75px;display:none;border-color:red;">
                <select class="form-select kod_anod_vnutri" aria-label="" style="width: 75px;border-color:#fc2003;margin-right:15px;" onchange="create_kratkiy_tekst(`+String(i)+`)"  id='code_svet_anodirovki_vnutr`+String(i)+`' required></select>       
            </div>     
            </div>
            </div>
        </td> 
        <td >
            <div class="input-group input-group-sm " style="width: 60px;">
            <select class="form-select" aria-label=""   disabled id='contactnost_anodirovki`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option  value=""></option>
                <option value="YC" >YC</option>
                <option value="NC">NC</option>
            </select>
            </div>
        </td>
        <td style='display:none' >
            <div class="input-group input-group-sm mb-1">
            <div>
                <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;" id='tip_anodirovki`+String(i)+`'></span>
            </div>
            </div>
        </td>
        <td style='display:none' >
            <div class="input-group input-group-sm mb-1">
            <div>
                <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='sposob_anodirovki`+String(i)+`'></span>
            </div>
            </div>
        </td>
        <td >`
        text +=nakleyki
    
        text += `
        </td>
        <td >
            
            <span  style="font-size: small; width:150px; font-weight: bold; text-transform: uppercase;" id='nadpis_nakleyki`+String(i)+`'></span>
            
        </td>
        <td >
            <span  style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='baza_profiley`+String(i)+`'></span>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label=""    style="width:200px; border-color:red" id='goods_group`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option  value=""></option>
                <option value="QLIK_ALU_PROF" >Алюминиевый профиль</option>
                <option value="QLIK_RLS">Рольставни</option>
                <option value="QLIK_MSQ">Москитка</option>
                <option value="QLIK_FSD">Фасад</option>
                <option value="QLIK_ACS">Аксессуар</option>
                <option value="QLIK_GLS">Стекло</option>
                <option value="QLIK_PDF">Подоконник</option>
                <option value="QLIK_CLR">Металл</option>
                <option value="QLIK_MDF">МДФ</option>
            </select>
            </div>
        </td> 
        <td >
            <div class="input-group input-group-sm mb-1">
            <span class ='text-center ' style="font-size: small;  font-weight: bold; text-transform: uppercase;" id='tex_name`+String(i)+`'></span>
            </div>
        </td> 
        <td >
            <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='gruppa_materialov`+String(i)+`'>ALUGP</span>
           
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='kratkiy_tekst`+String(i)+`'></span>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type="text" class="form-control "  style='width:150px;'   aria-describedby="inputGroup-sizing-sm"  id="sap_code_ruchnoy`+String(i)+`" onkeyup='create_kratkiy_tekst(`+String(i)+`)' >           
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type="text" class="form-control "  style='width:250px;'   aria-describedby="inputGroup-sizing-sm"  id="kratkiy_text_ruchnoy`+String(i)+`"  onkeyup='create_kratkiy_tekst(`+String(i)+`)'>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type="text" class="form-control "  style='width:90px;border-color:red;'   aria-describedby="inputGroup-sizing-sm" onkeyup='create_kratkiy_tekst(`+String(i)+`)' id="id_klaes`+String(i)+`"  >    
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type="text" class="form-control "  style='width:90px;border-color:red;'   aria-describedby="inputGroup-sizing-sm" onkeyup='create_kratkiy_tekst(`+String(i)+`)' id="klaes_nazvaniye`+String(i)+`"  >    
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type="text" class="form-control "  style='width:90px;border-color:red;'   aria-describedby="inputGroup-sizing-sm" onkeyup='create_kratkiy_tekst(`+String(i)+`)' id="code_sveta`+String(i)+`"  >    
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type="text" class="form-control "  style='width:90px;border-color:red;'   aria-describedby="inputGroup-sizing-sm" onkeyup='create_kratkiy_tekst(`+String(i)+`)' id="klaes_kratkiy`+String(i)+`"  >    
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <textarea   rows='1' class=" form-control " style="width: 220px; font-size:10px;height:32px" id='comment`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></textarea >
            </div>
        </td>
        
        </tr>`
      }

    return text
}

text = front_piece(start=1,end=lengthOfObject+1)



var table = $('#table-artikul')

table.append(text)



function request_piece(start=1,end=lengthOfObject+1){

    for (let i = start; i <=end; i++) {
        $('#artikul'+String(i)).select2({
            ajax: {
                url: "/client/imzo-artikul-list",
                dataType: 'json',
                processResults: function(data){
                    return {results: $.map(data, function(item){
                        return {id:item.data['Артикул'],text:item.data['Артикул'],system:item.data['Система'],combination:item.data['Комбинация'],code_nakleyka:item.data['Код наклейки'],baza_profiley:item.data['BAZA']}
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
        baza_profiley.text(e.params.data.baza_profiley)
        
        
        // tip_pokritiya.val('').change();
        tip_pokritiya.attr("disabled",false);
        nazvaniye_system.text(e.params.data.system);
        combination.text(e.params.data.combination)
    
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

    var i = 1
    for(key in data_base){
        copy_tr(key,i)
        i += 1
    }
}

request_piece()

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
            // $('.nazvaniye_system'+id).text('');
            var tip_pokritiya = $('#tip_pokritiya'+String(id));
            tip_pokritiya.val('0').change();
            // tip_pokritiya.attr("disabled",true);
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
            // // console.log(combination,'dddd',combination.innerText)
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

function copy_tr(id,i){
    if(!data_base[id]){
        console.log('salom2222 copy')
    }else{
        
        var data = data_base[id]
        var s = i

        var id = data.id;
        var nazvaniye_system = data.nazvaniye_system;
        var dlina = data.dlina;
        var base_artikul = data.base_artikul;
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
        var goods_group = data.goods_group;
        var tex_name = data.tex_name;
        var gruppa_materialov = data.gruppa_materialov;

        var kratkiy_tekst = data.kratkiy_tekst;

        var sap_code_ruchnoy = data.sap_code_ruchnoy;
        var kratkiy_text_ruchnoy = data.kratkiy_text_ruchnoy;
        var klaes_id = data.klaes_id;
        var klaes_nazvaniye = data.klaes_nazvaniye;
        var kod_sveta = data.kod_sveta;
        var kratkiy_klaes = data.kratkiy_klaes;
        var comment = data.comment;
        var is_termo = data.is_termo;

        
      
        
        check_input_and_change(id,'#tip_pokritiya'+s)


        

        if(id ==1){
            check_input_and_change(kod_kraska_sn,'#code_kraski_snar'+s,dis=true)
            check_input_and_change(kod_nakleyki,'#nakleyka'+s,dis=true)
            if(is_termo){
                check_input_and_change(kod_kraska_vn,'#code_kraski_vnut'+s,dis=true)
            }
        }else if(id == 2){    
                check_input_and_change(brend_kraska_sn,'#brand_k_snaruji'+s,dis=true)
                check_input_and_change(kod_kraska_sn,'#code_kraski_snar'+s,dis=true)
                check_input_and_change(kod_nakleyki,'#nakleyka'+s)
                if(is_termo){
                    check_input_and_change(brend_kraska_vn,'#brand_k_vnutri'+s,dis=true)
                    check_input_and_change(kod_kraska_vn,'#code_kraski_vnut'+s,dis=true)
                }
        }else if(id ==3){
            
            check_input_and_change(brend_kraska_sn,'#brand_k_snaruji'+s,dis=false,is_req=true)
            check_input_and_change(kod_kraska_sn,'#code_kraski_snar'+s,dis=false,is_req=true)
            check_input_and_change(kod_nakleyki,'#nakleyka'+s)

            if(is_termo){
                check_input_and_change(brend_kraska_vn,'#brand_k_vnutri'+s,dis=false,is_req=true)
                check_input_and_change(kod_kraska_vn,'#code_kraski_vnut'+s,dis=false,is_req=true)
            }
        }
        else if(id ==4){
            
            check_input_and_change(brend_kraska_sn,'#brand_k_snaruji'+s,dis=false,is_req=true)
            check_input_and_change(kod_kraska_sn,'#code_kraski_snar'+s,dis=false,is_req=true)

            check_input_and_change(kod_lam_sn,'#svet_lamplonka_snaruji'+s,dis=false,is_req=true)
            check_text_and_change(kod_lam_sn,'#code_lamplonka_snaruji'+s,dis=false,is_req=true)

            check_input_and_change(kod_lam_vn,'#svet_lamplonka_vnutri'+s,dis=false,is_req=true)
            check_text_and_change(kod_lam_vn,'#code_lamplonka_vnutri'+s,dis=false,is_req=true)
            check_input_and_change(kod_nakleyki,'#nakleyka'+s)
            if(is_termo){
                check_input_and_change(brend_kraska_vn,'#brand_k_vnutri'+s,dis=false,is_req=true)
                check_input_and_change(kod_kraska_vn,'#code_kraski_vnut'+s,dis=false,is_req=true)
            }

        }
        else if(id ==5){
            
            check_input_and_change(brend_kraska_sn,'#brand_k_snaruji'+s,dis=false,is_req=true)
            check_input_and_change(kod_kraska_sn,'#code_kraski_snar'+s,dis=false,is_req=true)

            check_input_and_change(svet_dekplonka_snaruji,'#svet_dekplonka_snaruji'+s,dis=false,is_req=true)
            check_text_and_change(svet_dekplonka_snaruji,'#code_dekplonka_snaruji'+s,dis=false,is_req=true)

            check_input_and_change(kod_nakleyki,'#nakleyka'+s)

            if(is_termo){
                check_input_and_change(brend_kraska_vn,'#brand_k_vnutri'+s,dis=false,is_req=true)
                check_input_and_change(kod_kraska_vn,'#code_kraski_vnut'+s,dis=false,is_req=true)

                check_input_and_change(svet_dekplonka_vnutri,'#svet_dekplonka_vnutri'+s,dis=false,is_req=true)
                check_text_and_change(svet_dekplonka_vnutri,'#code_dekplonka_vnutri'+s,dis=false,is_req=true)
            }

        }
        else if(id ==6){
            

            
            check_for_valid_and_set_val_select(kod_anod_sn,'code_svet_anodirovki_snaruji'+ s)

            check_input_and_change(contactnost_anod,'#contactnost_anodirovki'+s,dis=false,is_req=true)

            check_input_and_change(kod_nakleyki,'#nakleyka'+s)

            get_anod(s)
            if(is_termo){
                check_for_valid_and_set_val_select(kod_anod_sn,'code_svet_anodirovki_vnutri'+ s)
                get_anod(s,is_termo=true)
            }



        }

       
        check_input_and_change(dlina,'#length'+s,dis=false,is_req=true)
        check_for_valid_and_set_val_select(base_artikul,'artikul'+ s)
        check_input_and_change(splav,'#splav'+s)
        check_input_and_change(tip_zak,'#tip_zakalyonnosti'+s)
        check_text_and_change(combination,'#combination'+s)
        check_text_and_change(nazvaniye_system,'.nazvaniye_system'+s)
        
        
        check_text_and_change(nadpis_nakleyki,'#nadpis_nakleyki'+s)
        check_text_and_change(baza_profiley,'#baza_profiley'+s)
        

        check_input_and_change(tex_name,'#goods_group'+s)
        check_text_and_change(tex_name,'#tex_name'+s)
        
        check_text_and_change(kratkiy_tekst,'#kratkiy_tekst'+s)

        check_input_and_change(sap_code_ruchnoy,'#sap_code_ruchnoy'+s)
        check_input_and_change(kratkiy_text_ruchnoy,'#kratkiy_text_ruchnoy'+s)


        check_input_and_change(klaes_id,'#id_klaes'+s)
        check_input_and_change(klaes_nazvaniye,'#klaes_nazvaniye'+s)
        check_input_and_change(kod_sveta,'#code_sveta'+s)
        check_input_and_change(kratkiy_klaes,'#klaes_kratkiy'+s)
        check_input_and_change(comment,'#comment'+s)
        
        
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


function get_anod(id,termo=false){
    $('#anod'+id).css('display','block')
    $('.kod_anod_snar').select2({
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
        $('.kod_anod_vnutri').select2({
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
   
    
    var code_kraski_snaruji = $('#code_kraski_snar'+String(id));
    var code_kraski_vnutri = $('#code_kraski_vnut'+String(id));
    var brand_kraski_vnutri = $('#brand_k_vnutri'+String(id))
    var brand_kraski_snaruji = $('#brand_k_snaruji'+String(id))
    var kratkiy_tekst = $('#kratkiy_tekst'+String(id));
    kratkiy_tekst.text("");
    code_kraski_snaruji.val("");
    code_kraski_vnutri.val("");
    brand_kraski_vnutri.val("");
    brand_kraski_snaruji.val("");

    code_kraski_snaruji.css("border-color",'#dedad9');
    code_kraski_vnutri.css("border-color",'#dedad9');
    brand_kraski_vnutri.css("border-color",'#dedad9');
    brand_kraski_snaruji.css("border-color",'#dedad9');

    code_kraski_snaruji.css("display",'none');
    code_kraski_vnutri.css("display",'none');
    brand_kraski_vnutri.css("display",'none');
    brand_kraski_snaruji.css("display",'none');


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
    var nakleyka = $('#nakleyka'+String(id))

    if(String(val) == '1'){
        
        data_base[id] = new BasePokritiya()
        data_base[id].id = 1 
        data_base[id].tip_pokritiya = 'Неокрашенный' 
        
        nakleyka.css('display','block');
        nakleyka.val("NT1");

        if (combination_text.toUpperCase() == 'БЕЗ ТЕРМОМОСТА'){
            var code_kraski_snaruji = $('#code_kraski_snar'+String(id))
            code_kraski_snaruji.val('MF')
            code_kraski_snaruji.attr('disabled',true)
            code_kraski_snaruji.css('display','block')
            code_kraski_snaruji.css('border-color','#dedad9')
        }else{
            var code_kraski_snaruji = $('#code_kraski_snar'+String(id));
            var code_kraski_vnutri = $('#code_kraski_vnut'+String(id));
            code_kraski_snaruji.val('MF');
            code_kraski_snaruji.attr('disabled',true)
            code_kraski_snaruji.css('display','block')
            code_kraski_snaruji.css('border-color','#dedad9')
            
            code_kraski_vnutri.val('MF');
            code_kraski_vnutri.attr('disabled',true)
            code_kraski_vnutri.css('display','block')
            code_kraski_vnutri.css('border-color','#dedad9')
           

        }

    }else if(String(val) == '2'){
        
        data_base[id] = new BasePokritiya()
        data_base[id].id = 2 
        data_base[id].tip_pokritiya = 'Белый'
        
        if (combination_text.toUpperCase() == 'БЕЗ ТЕРМОМОСТА'){
            var code_kraski_snaruji = $('#code_kraski_snar'+String(id))
            var brand_kraski_snaruji = $('#brand_k_snaruji'+String(id))
        
            code_kraski_snaruji.val('9016');
            code_kraski_snaruji.attr('disabled',true)
            code_kraski_snaruji.css('display','block')
            code_kraski_snaruji.css('border-color','#dedad9')

            brand_kraski_snaruji.val('R');
            brand_kraski_snaruji.attr('disabled',true)
            brand_kraski_snaruji.css('display','block')
            brand_kraski_snaruji.css('border-color','#dedad9')
        }else{
            var code_kraski_snaruji = $('#code_kraski_snar'+String(id));
            var code_kraski_vnutri = $('#code_kraski_vnut'+String(id));
            var brand_kraski_vnutri = $('#brand_k_vnutri'+String(id))
            var brand_kraski_snaruji = $('#brand_k_snaruji'+String(id))

            brand_kraski_snaruji.val('R');
            brand_kraski_snaruji.attr('disabled',true)
            brand_kraski_snaruji.css('display','block')
            brand_kraski_snaruji.css('border-color','#dedad9')

            code_kraski_snaruji.val('9016');
            code_kraski_snaruji.attr('disabled',true)
            code_kraski_snaruji.css('display','block')
            code_kraski_snaruji.css('border-color','#dedad9')

            brand_kraski_vnutri.val('R');
            brand_kraski_vnutri.attr('disabled',true)
            brand_kraski_vnutri.css('display','block')
            brand_kraski_vnutri.css('border-color','#dedad9')

            code_kraski_vnutri.val('9016');
            code_kraski_vnutri.attr('disabled',true)
            code_kraski_vnutri.css('display','block')
            code_kraski_vnutri.css('border-color','#dedad9')

        }

        var nakleyka_codd = $('#nakleyka_codd'+String(id)).text()
        if(nakleyka_codd!=''){
            nakleyka.val(nakleyka_codd)
        }
            
    }else if(String(val) == '3' || String(val) == '4'|| String(val) == '5'){

        var nakleyka_codd = $('#nakleyka_codd'+String(id)).text()
        if(nakleyka_codd!=''){
            nakleyka.val(nakleyka_codd)
        }

        if(String(val) == '3'){
            
            data_base[id] = new BasePokritiya()
            data_base[id].id = 3 
            data_base[id].tip_pokritiya = 'Окрашенный'
            
        }else if(String(val) == '4'){
            
            data_base[id] = new BasePokritiya()
            data_base[id].id = 4 
            data_base[id].tip_pokritiya = 'Ламинированный'
            
        }else if(String(val) == '5'){
            
            data_base[id] = new BasePokritiya()
            data_base[id].id = 5 
            data_base[id].tip_pokritiya = 'Сублимированный'
            
        } 
        
        
        var brand_k_snaruji = $('#brand_k_snaruji'+String(id));
        brand_k_snaruji.attr('disabled',false)
        brand_k_snaruji.css('display','block')
        var code_kraski_snar = $('#code_kraski_snar'+String(id));
        code_kraski_snar.attr('disabled',false)
        code_kraski_snar.css('display','block')

        // code_kraski_snaruji.css("border-color",'#fc2003')
    
       

        if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА'){
            
            var brand_kraski_vnutri = $('#brand_k_vnutri'+String(id));
            brand_kraski_vnutri.attr('disabled',false)
            brand_kraski_vnutri.css('display','block')
            var code_kraski_vnutri = $('#code_kraski_vnut'+String(id));
            code_kraski_vnutri.attr('disabled',false)
            code_kraski_vnutri.css('display','block')
            


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
        
        data_base[id] = new BasePokritiya()
        data_base[id].id = 6 
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
        data_base[id].tip_zak = tip_zakalyonnosti.val()
        data_base[id].combination = combination.text()
        

        var goods_group = $('#goods_group'+String(id));
        goods_group.val('0').change();
        goods_group.css('display','block')
        var id_klaes =$('#id_klaes'+String(id))
        var klaes_nazvaniye =$('#klaes_nazvaniye'+String(id))
        var code_sveta =$('#code_sveta'+String(id))
        var klaes_kratkiy =$('#klaes_kratkiy'+String(id))
        var sap_code_ruchnoy =$('#sap_code_ruchnoy'+String(id))
        var kratkiy_text_ruchnoy =$('#kratkiy_text_ruchnoy'+String(id))
    
        kratkiy_text_ruchnoy.val('')
        sap_code_ruchnoy.val('')
        id_klaes.val('')
        klaes_nazvaniye.val('')
        code_sveta.val('')
        klaes_kratkiy.val('')
        id_klaes.css('border-color','red')
        klaes_nazvaniye.css('border-color','red')
        code_sveta.css('border-color','red')
        klaes_kratkiy.css('border-color','red')
        id_klaes.css('display','block')
        klaes_nazvaniye.css('display','block')
        code_sveta.css('display','block')
        klaes_kratkiy.css('display','block')
        sap_code_ruchnoy.css('display','block')
        kratkiy_text_ruchnoy.css('display','block')
    }
    create_kratkiy_tekst(id);
}





function code_svet_anodirovki_snaruji_selected(id,val){
    $("#code_svet_anodirovki_snaruji"+String(id)).on("select2:select", function (e) { 
    
        var tip_anodirovki =$('#tip_anodirovki'+String(id));
        var sposob_anodirovki = $('#sposob_anodirovki'+String(id));
        // console.log(e.params.data.text);
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
    // console.log(selectElement)
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
    if(dlina.val()!=''){
        dlina.css("border-color",'#dedad9');
        data_base[id].dlina = dlina.val();
    }else{
        dlina.css("border-color",'red');
        data_base[id].dlina = NaN;
    }
   

    var id_klaes =$('#id_klaes'+String(id))
    var klaes_nazvaniye =$('#klaes_nazvaniye'+String(id))
    var code_sveta =$('#code_sveta'+String(id))
    var klaes_kratkiy =$('#klaes_kratkiy'+String(id))
   
    if(id_klaes.val()!=''){
        id_klaes.css("border-color",'#dedad9');
        data_base[id].klaes_id = id_klaes.val();
    }else{
        id_klaes.css("border-color",'red');
        data_base[id].klaes_id = NaN;
    }
    if(klaes_nazvaniye.val()!=''){
        klaes_nazvaniye.css("border-color",'#dedad9');
        data_base[id].klaes_nazvaniye = klaes_nazvaniye.val();
    }else{
        klaes_nazvaniye.css("border-color",'red');
        data_base[id].klaes_nazvaniye = NaN;
    }
    if(code_sveta.val()!=''){
        code_sveta.css("border-color",'#dedad9');
        data_base[id].kod_sveta = code_sveta.val();
    }else{
        code_sveta.css("border-color",'red');
        data_base[id].kod_sveta = NaN;
    }
    if(klaes_kratkiy.val()!=''){
        klaes_kratkiy.css("border-color",'#dedad9');
        data_base[id].kratkiy_klaes = klaes_kratkiy.val();
    }else{
        klaes_kratkiy.css("border-color",'red');
        data_base[id].kratkiy_klaes = NaN;
    }

     var goods_group = $('#goods_group'+String(id));
    if(goods_group.val()!=''&&goods_group.val()!=null){
        
        var tex_name = $('#tex_name'+String(id));
        tex_name.text(goods_group.val())
        goods_group.css("border-color",'#dedad9');
        var goods_text = $('#goods_group'+String(id)+' option:selected').text();
        data_base[id].goods_group = goods_text;
        data_base[id].tex_name = goods_group.val();
    }else{
        var tex_name = $('#tex_name'+String(id));
        tex_name.text('')
        goods_group.css("border-color",'red');
        data_base[id].tex_name = NaN;
    }
    
    var sap_code_ruchnoy = $('#sap_code_ruchnoy'+String(id));
    
    if(sap_code_ruchnoy.val()!='0' && sap_code_ruchnoy.val()!='' && sap_code_ruchnoy.val()!=null){
        
        data_base[id].sap_code_ruchnoy = sap_code_ruchnoy.val();
    }else{
        
        data_base[id].sap_code_ruchnoy = NaN;
    }
    
    var kratkiy_text_ruchnoy = $('#kratkiy_text_ruchnoy'+String(id));
    if(kratkiy_text_ruchnoy.val()!='0' && kratkiy_text_ruchnoy.val()!='' && kratkiy_text_ruchnoy.val()!=null){
        
        data_base[id].kratkiy_text_ruchnoy = kratkiy_text_ruchnoy.val();
    }else{
        
        data_base[id].kratkiy_text_ruchnoy = NaN;
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
            var nadpis_nakleyki = $('#nadpis_nakleyki'+String(id))
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
                // console.log(a1,a2,a3)
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
                data_base[id].kod_lam_sn =code_lamplonka_snaruji.innerText;
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
                data_base[id].svet_lamplonka_vnutri= NaN;
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
                    var svet_dekplonka_snaruji = $('#code_dekplonka_snaruji'+id).text()
                    data_base[id].kod_dekor_sn =selectedText;
                    data_base[id].svet_dekplonka_snaruji =svet_dekplonka_snaruji;
                }else{
                    selectElement.style.borderColor='red';
                    data_base[id].svet_dekplonka_snaruji =NaN;
                    data_base[id].kod_dekor_sn =NaN;
                }
            }else{
                data_base[id].svet_dekplonka_snaruji =NaN;
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
                var tip_anodirovki = $('#tip_anodirovki'+String(id)).text()
                var sposob_anodirovki = $('#sposob_anodirovki'+String(id)).text()
                spanss.style.borderColor='#dedad9';
                data_base[id].kod_anod_sn = spanTextbox1.innerText;
                data_base[id].tip_anod = tip_anodirovki;
                data_base[id].sposob_anod = sposob_anodirovki;
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
        var art_krat = data_base[id].base_artikul + data.text
        if(zapros_count.indexOf(art_krat) === -1){
            sap_codes = get_sapcode(id,data_base[id].base_artikul,data.text,data_base[id].is_termo)
            zapros_count.push(art_krat)
        }
        data_base[id].kratkiy_tekst= data.text
    }
    
    kratkiy_tekst.text(data.text)
    }

    // console.log(data_base,'create_text')
}





function get_sapcode(id,artikul,kratkiy_tekst,is_termo){
    var url = '/client/get-sapcodes'
   

    $.ajax({
        type: 'GET',
        url: url,
        data: {'artikul':artikul,'kratkiy_tekst':kratkiy_tekst,'is_termo':is_termo},
    }).done(function (res) {
        if (res.status ==201){
            var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
            var kratkiy_text_ruchnoy = $('#kratkiy_text_ruchnoy'+id)
            sap_code_ruchnoy.val(res.artikul)
            kratkiy_text_ruchnoy.val(res.kratkiy_tekst)
            sap_code_ruchnoy.css('background-color','orange')
            kratkiy_text_ruchnoy.css('background-color','orange')
        }else{
            var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
            var kratkiy_text_ruchnoy = $('#kratkiy_text_ruchnoy'+id)
            sap_code_ruchnoy.val('')
            kratkiy_text_ruchnoy.val('')
            sap_code_ruchnoy.css('background-color','white')
            kratkiy_text_ruchnoy.css('background-color','white')
            // console.log('aa')
        }
        // WON'T REDIRECT
    });
}
