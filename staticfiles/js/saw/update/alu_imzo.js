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
        dilina_pressa =NaN,
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
            this.dilina_pressa =dilina_pressa;
            this.is_termo= is_termo;
    }


    get_kratkiy_tekst(){
        switch(this.id){
            case 1: if(!this.is_termo){
                // console.log('termoooo')
                if(this.splav && this.tip_zak && this.dlina && this.kod_kraska_sn && this.kod_nakleyki && this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){
                    return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.kod_kraska_sn +'  ' +this.kod_nakleyki
                }else{
                    return 'XXXXXXXX'
                }
                }else{
                    console.log('termooooooem3444')
                    console.log(this.splav ,this.tip_zak ,this.dlina ,this.kod_kraska_sn ,this.kod_kraska_vn ,this.kod_nakleyki ,this.tex_name ,this.klaes_id ,this.klaes_nazvaniye ,this.kod_sveta ,this.kratkiy_klaes)
                    if(this.splav && this.tip_zak && this.dlina && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki && this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){
                        return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.kod_kraska_sn +'/'+this.kod_kraska_vn+'  ' +this.kod_nakleyki
                    }else{
                        return 'XXXXXXXX'
                    }
                }
                break;
            case 2: if(!this.is_termo){

                if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_nakleyki && this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){
                    return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'  ' +this.kod_nakleyki
                }else{
                    return 'XXXXXXXX'
                }
                }else{
        
                    if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki && this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){
                        return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+'  ' +this.kod_nakleyki
                    }else{
                        return 'XXXXXXXX'
                    }
                } break;
            case 3:if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_nakleyki && this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){
                    return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'  ' +this.kod_nakleyki
                }else{
                    return 'XXXXXXXX'
                }
                }else{
                   if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki && this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){
                        return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn+'/'+this.brend_kraska_vn+this.kod_kraska_vn+'  ' +this.kod_nakleyki
                    }else{
                        return 'XXXXXXXX'
                    }
                }break;
            case 4:if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki && this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){
                    return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + '  ' +this.kod_nakleyki
                }else{
                    return 'XXXXXXXX'
                }
                }else{
                    if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki && this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){
                        return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn + this.kod_kraska_vn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + '  ' +this.kod_nakleyki
                    }else{
                        return 'XXXXXXXX'
                    }
                }break;
            case 5:if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_dekor_sn && this.kod_nakleyki && this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){
                    return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_dekor_sn + '  ' +this.kod_nakleyki
                }else{
                    return 'XXXXXXXX'
                }
                }else{
                    if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_dekor_sn && this.kod_dekor_vn && this.tex_name && this.kod_nakleyki && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){
                        return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+'_'+this.kod_dekor_sn+'/'+this.kod_dekor_vn + '  ' +this.kod_nakleyki
                    }else{
                        return 'XXXXXXXX'
                    }
                }break;
            case 6:if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.kod_anod_sn && this.kod_nakleyki && this.contactnost_anod && this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){
                    return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.kod_anod_sn + '  ' + this.contactnost_anod + '  ' + this.kod_nakleyki
                }else{
                    return 'XXXXXXXX'
                }
                }else{
                    if(this.splav && this.tip_zak && this.dlina && this.kod_anod_sn && this.kod_anod_vn && this.kod_nakleyki && this.contactnost_anod && this.tex_name && this.klaes_id && this.klaes_nazvaniye && this.kod_sveta && this.kratkiy_klaes){
                        return this.splav + this.tip_zak + ' L' + this.dlina +'  ' + this.kod_anod_sn +'/'+this.kod_anod_vn+ '  ' + this.contactnost_anod + '  ' + this.kod_nakleyki
                    }else{
                        return 'XXXXXXXX'
                    }
        
                }break;
        }
        
    }
  }

text =""

var jsonData = JSON.parse(JSON.parse(document.getElementById('items-data').textContent)).data;

data_base = {}

for(var key1 in jsonData){
    data_base[key1] = new BasePokritiya()
    for(var key2 in jsonData[key1]){
        data_base[key1][key2] = jsonData[key1][key2]
    }
}


i = 0
var order_type =$('#order_type').text()

for (var key in jsonData) {
    i+=1
    text +=`
    <tr id='table_tr` +String(i)+`' >
                                
    <td >
        <div class="input-group input-group-sm mb-1">
            <div><span id ='nazvaniye_system` +String(i)+`'style="text-transform: uppercase;" style="font-size: 12px;"></span></div>
        </div>
    </td>
    <td >
        <input type="text" id="searchInput` +String(i)+`" class=" form-control pb-1" style='width:150px' placeholder="Search for options">
        <div class="input-group input-group-sm mb-1">
        <select id="mySelect` +String(i)+`"  class=" form-control" style='display:none' multiple="multiple" ></select>
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
        <select class="form-select form-select-sm text-center"  style="width:55px;border-color:#fc2003;display:none" id='brand_k_snaruji`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)" required>
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
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1" style="width: 100px;">
        <input type="text"  class="form-control " id ='code_kraski_snar`+String(i)+`' aria-describedby="inputGroup-sizing-sm" style="border-color: red;width:65px; height:30px;display:none"  onkeyup="create_kratkiy_tekst(`+String(i)+`)" required>
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select form-select-sm text-center"  style="width:55px;border-color:#fc2003; display:none" id='brand_k_vnutri`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)" required>
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
        <input type="text"  class="form-control " id ='code_kraski_vnut`+String(i)+`' aria-describedby="inputGroup-sizing-sm" style="border-color: red;width:65px; height:30px;display:none"  onkeyup="create_kratkiy_tekst(`+String(i)+`)" required>
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
        <input type="text" id="searchInputanod_sn` +String(i)+`" class=" form-control pb-1" style='width:150px;display:none' placeholder="Search for options">
        <div class="input-group input-group-sm mb-1">
        <select id="mySelectanod_sn` +String(i)+`"  class=" form-control" style='display:none' multiple="multiple" ></select>
        </div>
    </td> 
    <td class='mr-2'>
        <input type="text" id="searchInputanod_vn` +String(i)+`" class=" form-control pb-1" style='width:150px;display:none' placeholder="Search for options">
        <div class="input-group input-group-sm mb-1">
        <select id="mySelectanod_vn` +String(i)+`"  class=" form-control" style='display:none' multiple="multiple" ></select>
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
    <td >
        <div class="input-group input-group-sm mb-1">
        <div>
            <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;display:none" id='tip_anodirovki`+String(i)+`'></span>
        </div>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <div>
            <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;display:none" id='sposob_anodirovki`+String(i)+`'></span>
        </div>
        </div>
    </td>
    <td >
        <input type="text" id="nakleykaInput` +String(i)+`" class=" form-control pb-1" style='width:150px;display:none' placeholder="Search for options">
        <div class="input-group input-group-sm mb-1">
        <select id="nakleykaSelect` +String(i)+`"  class=" form-control" style='display:none' multiple="multiple" ></select>
        </div>
    </td>
    <td >
     <div class="input-group input-group-sm mb-1">
        <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase; display:none" id='nadpis_nakleyki`+String(i)+`'></span>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='baza_profiley`+String(i)+`'></span>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label=""    style="width:200px; display:none; border-color:red" id='goods_group`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)">
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
        <input type="text" class="form-control "  style='width:90px;display:none;'   aria-describedby="inputGroup-sizing-sm"  id="sap_code_ruchnoy`+String(i)+`" onkeyup='create_kratkiy_tekst(`+String(i)+`)' >           
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type="text" class="form-control "  style='width:220px;display:none;'   aria-describedby="inputGroup-sizing-sm"  id="kratkiy_text_ruchnoy`+String(i)+`"  onkeyup='create_kratkiy_tekst(`+String(i)+`)'>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type="text" class="form-control "  style='width:90px;display:none;border-color:red;'   aria-describedby="inputGroup-sizing-sm" onkeyup='create_kratkiy_tekst(`+String(i)+`)' id="id_klaes`+String(i)+`"  >    
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type="text" class="form-control "  style='width:90px;display:none;border-color:red;'   aria-describedby="inputGroup-sizing-sm" onkeyup='create_kratkiy_tekst(`+String(i)+`)' id="klaes_nazvaniye`+String(i)+`"  >    
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type="text" class="form-control "  style='width:90px;display:none;border-color:red;'   aria-describedby="inputGroup-sizing-sm" onkeyup='create_kratkiy_tekst(`+String(i)+`)' id="code_sveta`+String(i)+`"  >    
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type="text" class="form-control "  style='width:90px;display:none;border-color:red;'   aria-describedby="inputGroup-sizing-sm" onkeyup='create_kratkiy_tekst(`+String(i)+`)' id="klaes_kratkiy`+String(i)+`"  >    
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
           
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type="text" class="form-control "  style='width:220px;display:none;'   aria-describedby="inputGroup-sizing-sm"  id="dilina_pressa`+String(i)+`" onchange="create_kratkiy_tekst(`+String(i)+`)" >
        </div>
    </td>
    </tr>`
}


var table = $('#table-artikul')

table.append(text)




function custom_select2(type_selection=NaN,older_val=NaN,i,nam=NaN,selector=NaN,input_selector=NaN,url=NaN,data=NaN){
    if(older_val!=NaN){
        $(input_selector).val(older_val)
        $(input_selector).css('display','block')
        for(var key in data){
           $('#'+key +i).text(data[key])
           $('#'+key +i).css('display','block')
        }
        $(input_selector).on('input', function() {
            var searchValue = $(this).val().trim();
            $(selector).css('display','block')
            $.ajax({
                url: url, 
                type: 'GET',
                dataType: 'json',
                data: { term: searchValue },
                success: function(data) {
                    $(selector).empty();
                    $.each(data, function(index, item) {
                        if (type_selection.indexOf('nak') !== -1) {
                            $(selector).append($(`<option>`, {
                                value: JSON.stringify(item),
                                text: item[nam]
                            }));
                        }else{
                            $(selector).append($(`<option>`, {
                                value: JSON.stringify(item),
                                text: item.data[nam]
                            }));
                        }
                    });
                },
                error: function(xhr, status, error) {
                    console.error('Failed to fetch search results:', error);
                }
            });
    
        });
        $(selector).on('change', function() {
            var selectedValue = $(this).find('option:selected').text();
            var value = JSON.parse($(this).val())
            console.log(value)
            $(this).css('display', 'none');
            
            if (type_selection.indexOf('artikul_alu') !== -1) {
                data_base[i].base_artikul =selectedValue
                data_base[i].nazvaniye_system = value.data['Система']
                data_base[i].combination = value.data['Комбинация']
                if(String(value.data['Комбинация']).toUpperCase() =='С ТЕРМОМОСТОМ'){
                    data_base[i].is_termo = true
                }else{
                    data_base[i].is_termo = false
                }

                data_base[i].baza_profiley = value.data['BAZA']
                $('#baza_profiley'+i).text(value.data['BAZA'])

                if(value.data['Код наклейки']!=''){
                    data_base[i].kod_nakleyki = value.data['Код наклейки']
                    $('#nakleykaInput'+i).val(value.data['Код наклейки'])
                }else{
                    data_base[i].kod_nakleyki = NaN
                    $('#nakleykaInput'+i).val('')
                }
                $('#nazvaniye_system'+i).text(value.data['Система'])
                $('#combination'+i).text(value.data['Комбинация'])

            }
            if (type_selection.indexOf('anod_sn') !== -1) {
                data_base[i].kod_anod_sn = selectedValue
            }
            if (type_selection.indexOf('anod_vn') !== -1) {
                data_base[i].kod_anod_vn = selectedValue
            }
            if (type_selection.indexOf('nak') !== -1) {
                data_base[i].kod_nakleyki = selectedValue
                data_base[i].nadpis_nakleyki = value['nadpis']
                $('#nadpis_nakleyki'+i).text(value['nadpis'])
            }
            // ######## dovomi bor
            $(input_selector).val(selectedValue)

            var data = data_base[i].get_kratkiy_tekst()
        
            if(data.accept){
                var table_tr =$('#table_tr'+i);
                table_tr.css('background-color','#2de319')
                data_base[i].full = true
                data_base[i].kratkiy_tekst = data.text
            }else{
                var table_tr = $('#table_tr'+i);
                table_tr.css('background-color','white')
                data_base[i].kratkiy_tekst = NaN;
                data_base[i].full = false
            }
            var kratkiy_tekst = $('#kratkiy_tekst'+String(i));
            kratkiy_tekst.text(data.text)
        });
    }
}

i=0

// 'id','artikul','system','combination','code_nakleyka'
for(var key in jsonData){
    i+=1
    data ={
        'searchInput':jsonData[key]['base_artikul'],
        'nazvaniye_system':jsonData[key]['nazvaniye_system'],
        'combination':jsonData[key]['combination'],
    }
    if(jsonData[i]['base_artikul']){
        custom_select2(type_selection='artikul_alu',jsonData[i]['base_artikul'],i,nam='Артикул','#mySelect'+i,'#searchInput'+i, url= '/client/imzo-artikul-list',data=data)    
    }

    if(jsonData[i]['dlina'] && jsonData[i]['dlina']!='null'){
        $('#length' +i).css('border-color','#dedad9')
        $('#length' +i).css('display','block')
        $('#length' +i).attr('disabled',false)
        $('#length' +i).val(jsonData[i]['dlina'])
    }

    if(jsonData[i]['id']  && jsonData[i]['id']!='null'){
        $('#tip_pokritiya' +i).val(jsonData[i]['id'])
    }
    
    if(jsonData[i]['splav'] && jsonData[i]['splav']!='null'){
        $('#splav' +i).css('border-color','#dedad9')
        $('#splav' +i).attr('disabled',false)
        $('#splav' +i).css('display','block')
        $('#splav' +i).val(jsonData[i]['splav'])
    }
    if(jsonData[i]['tip_zak'] && jsonData[i]['tip_zak']!='null'){
        $('#tip_zakalyonnosti' +i).css('border-color','#dedad9')
        $('#tip_zakalyonnosti' +i).attr('disabled',false)
        $('#tip_zakalyonnosti' +i).css('display','block')
        $('#tip_zakalyonnosti' +i).val(jsonData[i]['tip_zak'])
    }
    if(jsonData[i]['brend_kraska_sn']  && String(jsonData[i]['brend_kraska_sn'])!='null'){
        $('#brand_k_snaruji' +i).css('border-color','#dedad9')
        $('#brand_k_snaruji' +i).attr('disabled',false)
        $('#brand_k_snaruji' +i).css('display','block')
        $('#brand_k_snaruji' +i).val(jsonData[i]['brend_kraska_sn'])
    }
    console.log(jsonData[i]['kod_kraska_sn'],'kraskaaa')
    if(jsonData[i]['kod_kraska_sn'] && jsonData[i]['kod_kraska_sn']!='null'){
        $('#code_kraski_snar' +i).css('border-color','#dedad9')
        $('#code_kraski_snar' +i).attr('disabled',false)
        $('#code_kraski_snar' +i).css('display','block')
        $('#code_kraski_snar' +i).val(jsonData[i]['kod_kraska_sn'])
    }

    if(jsonData[i]['brend_kraska_vn'] && jsonData[i]['brend_kraska_vn']!='null'){
        $('#brand_k_vnutri' +i).css('border-color','#dedad9')
        $('#brand_k_vnutri' +i).attr('disabled',false)
        $('#brand_k_vnutri' +i).css('display','block')
        $('#brand_k_vnutri' +i).val(jsonData[i]['brend_kraska_vn'])
    }
    if(jsonData[i]['kod_kraska_vn'] && jsonData[i]['kod_kraska_vn']!='null'){
        $('#code_kraski_vnut' +i).css('border-color','#dedad9')
        $('#code_kraski_vnut' +i).attr('disabled',false)
        $('#code_kraski_vnut' +i).css('display','block')
        $('#code_kraski_vnut' +i).val(jsonData[i]['kod_kraska_vn'])
    }
    if(jsonData[i]['kod_dekor_sn'] && jsonData[i]['kod_dekor_sn']!='null'){
        $('#svet_dekplonka_snaruji' +i).css('border-color','#dedad9')
        $('#svet_dekplonka_snaruji' +i).attr('disabled',false)
        $('#svet_dekplonka_snaruji' +i).css('display','block')
        $('#svet_dekplonka_snaruji' +i).val(jsonData[i]['svet_dekplonka_snaruji'])
        $('#code_dekplonka_snaruji' +i).text(jsonData[i]['svet_dekplonka_snaruji'])
    }
    if(jsonData[i]['kod_dekor_vn'] && jsonData[i]['kod_dekor_vn']!='null'){
        $('#svet_dekplonka_vnutri' +i).css('border-color','#dedad9')
        $('#svet_dekplonka_vnutri' +i).attr('disabled',false)
        $('#svet_dekplonka_vnutri' +i).css('display','block')
        $('#svet_dekplonka_vnutri' +i).val(jsonData[i]['svet_dekplonka_vnutri'])
        $('#code_dekplonka_vnutri' +i).text(jsonData[i]['svet_dekplonka_snaruji'])
    }

    if(jsonData[i]['svet_lamplonka_snaruji'] && jsonData[i]['svet_lamplonka_snaruji']!='null'){
        $('#svet_lamplonka_snaruji' +i).attr('disabled',false)
        $('#svet_lamplonka_snaruji' +i).val(jsonData[i]['kod_lam_sn'])
        $('#svet_lamplonka_snaruji' +i).css('display','block')
        $('#code_lamplonka_snaruji' +i).text(jsonData[i]['kod_lam_sn'])
    }
    if(jsonData[i]['svet_lamplonka_vnutri'] && jsonData[i]['svet_lamplonka_vnutri']!='null'){
        $('#svet_lamplonka_vnutri' +i).attr('disabled',false)
        $('#svet_lamplonka_vnutri' +i).val(jsonData[i]['kod_lam_vn'])
        $('#svet_lamplonka_vnutri' +i).css('display','block')
        $('#code_lamplonka_vnutri' +i).text(jsonData[i]['kod_lam_vn'])
    }

    data ={
        'tip_anodirovki':jsonData[i]['tip_anod'],
        'sposob_anodirovki':jsonData[i]['sposob_anod'],
    }
    if(jsonData[i]['kod_anod_sn']){
        custom_select2(type_selection='anod_sn',jsonData[i]['kod_anod_sn'],i,nam='code_sveta','#mySelectanod_sn'+i,'#searchInputanod_sn'+i, url= '/client/client-anod-list',data=data)
    }
    data ={}
    if(jsonData[i]['kod_anod_vn']){
        custom_select2(type_selection='anod_vn',jsonData[i]['kod_anod_vn'],i,nam='code_sveta','#mySelectanod_vn'+i,'#searchInputanod_vn'+i, url= '/client/client-anod-list',data=data)
    }
    if(jsonData[i]['contactnost_anod']){
        $('#contactnost_anodirovki' +i).attr('disabled',false)
        $('#contactnost_anodirovki' +i).val(jsonData[i]['contactnost_anod'])
    }
    

    data ={
        'nadpis_nakleyki':jsonData[i]['nadpis_nakleyki']
    }
    if(jsonData[i]['kod_nakleyki']){
        custom_select2(type_selection='nakleyka',jsonData[i]['kod_nakleyki'],i,nam='name','#nakleykaSelect'+i,'#nakleykaInput'+i, url= '/client/nakleyka-list',data=data)
    }
    
    // usdifksjdfjskfjsjdf

    if(jsonData[i]['baza_profiley']){
        $('#gruppa_materialov' +i).css('display','block')
        $('#gruppa_materialov' +i).css('border-color','#dedad9')
        $('#baza_profiley' +i).attr('disabled',false)
        $('#baza_profiley' +i).text(jsonData[i]['baza_profiley'])
    }
    
    if(jsonData[i]['goods_group']){
        $('#goods_group' +i).css('display','block')
        $('#goods_group' +i).css('border-color','#dedad9')
        $('#goods_group' +i).attr('disabled',false)
        $('#goods_group' +i).val(jsonData[i]['tex_name'])
        $('#tex_name' +i).text(jsonData[i]['tex_name'])
    }

    if(jsonData[i]['gruppa_materialov']){
        $('#gruppa_materialov' +i).css('display','block')
        $('#gruppa_materialov' +i).css('border-color','#dedad9')
        $('#gruppa_materialov' +i).attr('disabled',false)
        $('#gruppa_materialov' +i).text(jsonData[i]['gruppa_materialov'])
    }


    if(jsonData[i]['kratkiy_tekst']){
        $('#kratkiy_tekst' +i).css('display','block')
        $('#kratkiy_tekst' +i).css('border-color','#dedad9')
        $('#kratkiy_tekst' +i).attr('disabled',false)
        $('#kratkiy_tekst' +i).text(jsonData[i]['kratkiy_tekst'])
    }
    if(jsonData[i]['sap_code_ruchnoy']){
        $('#sap_code_ruchnoy' +i).css('display','block')
        $('#sap_code_ruchnoy' +i).css('border-color','#dedad9')
        $('#sap_code_ruchnoy' +i).attr('disabled',false)
        $('#sap_code_ruchnoy' +i).val(jsonData[i]['sap_code_ruchnoy'])
    }
    if(jsonData[i]['kratkiy_text_ruchnoy']){
        $('#kratkiy_text_ruchnoy' +i).css('display','block')
        $('#kratkiy_text_ruchnoy' +i).css('border-color','#dedad9')
        $('#kratkiy_text_ruchnoy' +i).attr('disabled',false)
        $('#kratkiy_text_ruchnoy' +i).val(jsonData[i]['kratkiy_text_ruchnoy'])
    }
    
   
    
    if(jsonData[i]['klaes_id']){
        $('#id_klaes' +i).css('display','block')
        $('#id_klaes' +i).css('border-color','#dedad9')
        $('#id_klaes' +i).attr('disabled',false)
        $('#id_klaes' +i).val(jsonData[i]['klaes_id'])
    }
    if(jsonData[i]['klaes_nazvaniye']){
        $('#klaes_nazvaniye' +i).css('display','block')
        $('#klaes_nazvaniye' +i).css('border-color','#dedad9')
        $('#klaes_nazvaniye' +i).attr('disabled',false)
        $('#klaes_nazvaniye' +i).val(jsonData[i]['klaes_nazvaniye'])
    }
    
    if(jsonData[i]['kod_sveta']){
        $('#code_sveta' +i).css('display','block')
        $('#code_sveta' +i).css('border-color','#dedad9')
        $('#code_sveta' +i).attr('disabled',false)
        $('#code_sveta' +i).val(jsonData[i]['kod_sveta'])
    }
    if(jsonData[i]['kratkiy_klaes']){
        $('#klaes_kratkiy' +i).css('display','block')
        $('#klaes_kratkiy' +i).css('border-color','#dedad9')
        $('#klaes_kratkiy' +i).attr('disabled',false)
        $('#klaes_kratkiy' +i).val(jsonData[i]['kratkiy_klaes'])
    }
    if(jsonData[i]['comment']){
        $('#comment' +i).css('display','block')
        $('#comment' +i).css('border-color','#dedad9')
        $('#comment' +i).attr('disabled',false)
        $('#comment' +i).val(jsonData[i]['comment'])
    }
    if(jsonData[i]['dilina_pressa']){
        $('#dilina_pressa' +i).css('display','block')
        $('#dilina_pressa' +i).css('border-color','#dedad9')
        $('#dilina_pressa' +i).attr('disabled',false)
        $('#dilina_pressa' +i).val(jsonData[i]['dilina_pressa'])
    }
    
    // create_kratkiy_tekst(i)
}



function get_nakleyka(i){
    $('.kod_nakleyki'+i).select2({
        ajax: {
            url: "/client/nakleyka-list",
            dataType: 'json',
            processResults: function(data){
                return {results: $.map(data, function(item){
                    return {id:item.id,text:item.data['name']}
                })
            };
            }
        }
        });
}


function get_anod(termo=false){
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
    // var nakleyka_nt1 = $('#nakleyka_nt'+String(id))
    // var nakleyka_org =$('#nakleyka_org'+String(id));
    // var nakleyka_select = $('#nakleyka_select'+String(id));

    if(String(val) == '1'){
        data_base[id] = new BasePokritiya()
        data_base[id].id = 1 
        data_base[id].tip_pokritiya = 'Неокрашенный' 
        // nakleyka_nt1.css('display','block');
        // nakleyka_org.css('display','none');
        // nakleyka_select.css('display','none');

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
        data_base[id] = new BasePokritiya()
        data_base[id].id = 2 
        data_base[id].tip_pokritiya = 'Белый'
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

        
        
        // var nakleyka_kode = nakleyka_org.text()
        // if (nakleyka_kode !=''){
        //     nakleyka_nt1.css('display','none');
        //     nakleyka_org.css('display','block');
        //     nakleyka_select.css('display','none');
        // }else{
        //     nakleyka_nt1.css('display','none');
        //     nakleyka_org.css('display','none');
        //     nakleyka_select.css('display','block');
        //     get_nakleyka(id)
        // }
            
    }else if(String(val) == '3' || String(val) == '4'|| String(val) == '5'){

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
        
        // var nakleyka_kode = nakleyka_org.text()
        // if (nakleyka_kode !=''){
        //     nakleyka_nt1.css('display','none');
        //     nakleyka_org.css('display','block');
        //     nakleyka_select.css('display','none');
        // }else{
        //     nakleyka_nt1.css('display','none');
        //     nakleyka_org.css('display','none');
        //     nakleyka_select.css('display','block');
        //     get_nakleyka(id)
        // }
       

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
        data_base[id] = new BasePokritiya()
        data_base[id].id = 6 
        data_base[id].tip_pokritiya = 'Анодированный'
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

        
        // var nakleyka_kode = nakleyka_org.text()
        // if (nakleyka_kode !=''){
        //     nakleyka_nt1.css('display','none');
        //     nakleyka_org.css('display','block');
        //     nakleyka_select.css('display','none');
        // }else{
        //     nakleyka_nt1.css('display','none');
        //     nakleyka_org.css('display','none');
        //     nakleyka_select.css('display','block');
        //     get_nakleyka(id)
        // }
        
        
        
    }
    
    if(String(val) !=''){
        var nazvaniye_system =$('.nazvaniye_system'+id)
        var splav =$('#splav'+id)
        var tip_zakalyonnosti =$('#tip_zakalyonnosti'+id)
        var combination =$('#combination'+id)
        var base_artikul =$('#select2-artikul'+id+'-container')
        
        data_base[id].base_artikul = base_artikul.text()
        data_base[id].nazvaniye_system = nazvaniye_system.text()
        data_base[id].splav = splav.val()
        data_base[id].tip_zakalyonnosti = tip_zakalyonnosti.val()
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






function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
    var kratkiy_tekst = $('#kratkiy_tekst'+String(id));
    var combination= $('#combination'+String(id));
    combination_text = combination.text();
    var val = $('#tip_pokritiya'+String(id)).val();
    var dilina_pressa = $('#dilina_pressa'+String(id));

    
    if(dilina_pressa.val()!=''){
        dilina_pressa.css("border-color",'#dedad9');
        data_base[id].dilina_pressa = dilina_pressa.val();
    }else{
        data_base[id].dilina_pressa = NaN;
    }

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
    console.log(sap_code_ruchnoy.val())
    
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

        var nakleyka_select = $('#nakleykaInput'+String(id))
        
        if(nakleyka_select.val() !=''){
            var nadpis_nakleyki = $('#nadpis_nakleyki'+id)
            nadpis_nakleyki.css('border-color','#dedad9');
            data_base[id].kod_nakleyki = nakleyka_select.val()
            data_base[id].nadpis_nakleyki = nadpis_nakleyki.text();
            
        }else{
            data_base[id].nadpis_nakleyki = NaN;
            data_base[id].kod_nakleyki = NaN

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
    
                if((code_kraski_vnut.val() != '0') && (code_kraski_vnut.val()  != undefined)&&code_kraski_vnut.val()!=''){
                    code_kraski_vnut.css("border-color",'#dedad9');
                    data_base[id].kod_kraska_vn =code_kraski_vnut.val();
                }else{
                    code_kraski_vnut.css("border-color",'red');
                    data_base[id].kod_kraska_vn =NaN;
                }
                
                data_base[id].is_termo =true;
                
            }



            var nakleyka_select = $('#nakleykaInput'+String(id))
        
            if(nakleyka_select.val() !=''){
                var nadpis_nakleyki = $('#nadpis_nakleyki'+id)
                nadpis_nakleyki.css('border-color','#dedad9');
                data_base[id].kod_nakleyki = nakleyka_select.val()
                data_base[id].nadpis_nakleyki = nadpis_nakleyki.text();
                
            }else{
                data_base[id].nadpis_nakleyki = NaN;
                data_base[id].kod_nakleyki = NaN
    
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
            // this.kod_dekor_sn && this.kod_dekor_vn

        }

    }else if(String(val) == '6'){
        var nakleyka_select = $('#nakleykaInput'+String(id))
        
        if(nakleyka_select.val() !=''){
            var nadpis_nakleyki = $('#nadpis_nakleyki'+id)
            nadpis_nakleyki.css('border-color','#dedad9');
            data_base[id].kod_nakleyki = nakleyka_select.val()
            data_base[id].nadpis_nakleyki = nadpis_nakleyki.text();
            
        }else{
            data_base[id].nadpis_nakleyki = NaN;
            data_base[id].kod_nakleyki = NaN

        }

        var anod_sn = $('#searchInputanod_sn'+String(id))
        
        if(anod_sn.val() !=''){
            var anod_sn = $('#searchInputanod_sn'+id);
            var tip_anod = $('#tip_anodirovki'+id);
            var sposob_anod = $('#sposob_anodirovki'+id);
            // nadpis_nakleyki.css('border-color','#dedad9')
            data_base[id].kod_anod_sn = anod_sn.val()
            data_base[id].tip_anod = tip_anod.text();
            data_base[id].sposob_anod = sposob_anod.text();     
        }else{
            data_base[id].kod_anod_sn = NaN;
            data_base[id].tip_anod = NaN
            data_base[id].sposob_anod = NaN
            

        }

        if(combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА'){
            data_base[id].is_termo =true;
            var anod_vn = $('#searchInputanod_vn'+String(id))
        
            if(anod_vn.val() !=''){
                var anod_vn = $('#searchInputanod_vn'+id);
                
                // nadpis_nakleyki.css('border-color','#dedad9')
                data_base[id].kod_anod_vn = anod_vn.val()
                
                
            }else{
                data_base[id].kod_anod_vn = NaN;
                

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
        data_base[id].full =true
        data_base[id].kratkiy_tekst =text
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','#2de319')
    }else{
        data_base[id].full =false
        data_base[id].kratkiy_tekst =NaN
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','white')

    }
    kratkiy_tekst.text(text)

    }
}



