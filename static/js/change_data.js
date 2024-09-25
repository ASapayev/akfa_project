class BasePokritiya{
    constructor(
        full=false,//done
        id=NaN, //done
        vid_zayavki=NaN,
        id_savdo=NaN,
        naz_savdo=NaN,
        sapcode=NaN,
        bei =NaN,
        aei=NaN,
        koefitsiyent=NaN,
        sena_c_ndc=NaN,
        sena_bez_ndc=NaN,
        ed_izm=NaN,
        group=NaN,
        group_zakupok=NaN,
        zavod=NaN,
        segment=NaN,
        bux_naz=NaN,
        tip_clienta=NaN,
        svet_product=NaN,
        diller=NaN,


        comment=NaN,
        
        
        ) {
      
        this.full=full;
        this.id=id;
        this.vid_zayavki=vid_zayavki;
        this.id_savdo=id_savdo;
        this.naz_savdo=naz_savdo;
        this.sapcode=sapcode;
        this.bei=bei;
        this.aei=aei;
        this.koefitsiyent=koefitsiyent;
        this.sena_c_ndc=sena_c_ndc;
        this.sena_bez_ndc=sena_bez_ndc;
        this.ed_izm=ed_izm;
        this.group=group;
        this.group_zakupok=group_zakupok;
        this.zavod=zavod;
        this.segment=segment;
        this.bux_naz=bux_naz;
        this.tip_clienta=tip_clienta;
        this.svet_product=svet_product;
        this.diller=diller;
        this.comment=comment;
        
    }
    get_kratkiy_tekst(){
            switch(this.id){
                case 1:
            
                        if (this.id_savdo && this.naz_savdo&& this.sena_c_ndc&&this.sena_bez_ndc&&this.ed_izm&&this.tip_clienta){
        
                            return {'text':'','accept':true}
                        }else{
                            return {'text':'','accept':false}
                        }
                        break;
                case 2:
            
                        if (this.id_savdo && this.naz_savdo&& this.bei&&this.aei&&this.koefitsiyent){
        
                            return {'text':'','accept':true}
                        }else{
                            return {'text':'','accept':false}
                        }
                        break;
                case 3:
            
                        if (this.id_savdo && this.naz_savdo&& this.group){
        
                            return {'text':'','accept':true}
                        }else{
                            return {'text':'','accept':false}
                        }
                        break;
                case 4:
            
                        if (this.id_savdo && this.naz_savdo&& this.group_zakupok){
        
                            return {'text':'','accept':true}
                        }else{
                            return {'text':'','accept':false}
                        }
                        break;
                case 5:
            
                        if (this.id_savdo && this.naz_savdo&& this.segment){
        
                            return {'text':'','accept':true}
                        }else{
                            return {'text':'','accept':false}
                        }
                        break;
                case 6:
            
                        if (this.id_savdo && this.naz_savdo&& this.bux_naz){
        
                            return {'text':'','accept':true}
                        }else{
                            return {'text':'','accept':false}
                        }
                        break;
                case 7:
            
                        if (this.id_savdo && this.naz_savdo&& this.zavod){
        
                            return {'text':'','accept':true}
                        }else{
                            return {'text':'','accept':false}
                        }
                        break;
                case 8:
            
                        if (this.id_savdo && this.naz_savdo&& this.svet_product){
        
                            return {'text':'','accept':true}
                        }else{
                            return {'text':'','accept':false}
                        }
                        break;
                case 9:
            
                        if (this.id_savdo && this.naz_savdo&& this.diller){
        
                            return {'text':'','accept':true}
                        }else{
                            return {'text':'','accept':false}
                        }
                        break;
            }
        }
  }




var data_base = {}

function front_piece(start=1,end=6){
    var text =""

    for (let i = start; i < end; i++) {
       

        var buttons =''
        if(status_proccess == 'new'){
            data_base[i] = new BasePokritiya()
            data_base[i].id = 1
            buttons=`<td class="sticky-col"   style='left:0; padding-right:5px; background-color:white!important;' >
                    <div class="btn-group" role="group" aria-label="Basic example">
                            <button type="button" class="btn btn-outline-secondary btn-sm" id='clear_btn`+String(i)+`' onclick="artukil_clear(`+String(i)+`)" data-bs-toggle='popover' title='Tozalab tashlash'><i class="bi bi-x-circle"></i></button>
                            <button type="button" class="btn btn-outline-secondary btn-sm"  onclick="copy_tr(`+String(i)+`)" data-bs-toggle='popover' title='Dubl qilish'><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-copy" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M4 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 5a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-1h1v1a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h1v1z"/></svg></button>
                    </div>
                    </td>`
        }else{
            buttons=``

        }

        text +=`
        <tr id='table_tr` +String(i)+`' style='padding-bottom:0!important;margin-bottom:0!important;'>                   
        `+buttons+
         `
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 270px; font-size:12px; padding-right:0px;z-index:0" id='vid_zayavki`+String(i)+`' onchange='select_condition(`+String(i)+`)' required>
                <option  selected></option>
                <option  value="Изменения цена">Изменения цена</div>
                <option  value="Изменения веса">Изменения веса</div>
                <option  value="Изменения группа">Изменения группа</div>
                <option  value="Изменения группа закупок">Изменения группа закупок</div>
                <option  value="Изменения сегмент">Изменения сегмент</div>
                <option  value="Изменения бухгалтерская названия">Изменения бухгалтерская названия</div>
                <option  value="Изменения завода">Изменения завода</div>
                <option  value="Изменения цвет продукта">Изменения цвет продукта</div>
                <option  value="Изменения вид клиента">Изменения вид клиента</div>
            </select>
            </div>
        </td>
       <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 100px; font-size:10px;height:27px;z-index:0;display:none; " id='id_savdo`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 200px; font-size:10px;height:27px;z-index:0;display:none; " id='naz_savdo`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 200px; font-size:10px;height:27px;z-index:0 ;display:none;" id='sapcode`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px;z-index:0;display:none;" id='bei`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option  value="Штука">Штука</div>
                <option  value="Килограмм">Килограмм</div>
                <option  value="Квадратный метр">Квадратный метр</div>
                <option  value="Метр">Метр</div>
                <option  value="КМП">КМП</div>
                <option  value="Пачка">Пачка</div>
                <option  value="Секция">Секция</div>
                <option  value="Коробка">Коробка</div>
                <option  value="Грам">Грам</div>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px;z-index:0;display:none;" id='aei`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option  value="Штука">Штука</div>
                <option  value="Килограмм">Килограмм</div>
                <option  value="Квадратный метр">Квадратный метр</div>
                <option  value="Метр">Метр</div>
                <option  value="КМП">КМП</div>
                <option  value="Пачка">Пачка</div>
                <option  value="Секция">Секция</div>
                <option  value="Коробка">Коробка</div>
                <option  value="Грам">Грам</div>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 75px; font-size:10px;height:27px;z-index:0;display:none; " id='koefitsiyent`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 75px; font-size:10px;height:27px;z-index:0;display:none; " id='sena_c_ndc`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 75px; font-size:10px;height:27px;z-index:0 ;display:none;" id='sena_bez_ndc`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px;z-index:0;display:none;" id='ed_izm`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option  value="Штука">Штука</div>
                <option  value="Килограмм">Килограмм</div>
                <option  value="Квадратный метр">Квадратный метр</div>
                <option  value="Метр">Метр</div>
                <option  value="КМП">КМП</div>
                <option  value="Пачка">Пачка</div>
                <option  value="Секция">Секция</div>
                <option  value="Коробка">Коробка</div>
                <option  value="Грам">Грам</div>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1"  >
            <select class="form-select" aria-label="" id='group`+String(i)+`' style="width: 240px; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0"   onchange='create_kratkiy_tekst(`+String(i)+`)'required>
                <option  selected></option>
                <option value="AKSESSUAR (B) ALUTEX">AKSESSUAR (B) ALUTEX</option>
                <option value="AKSESSUAR BUTIL">AKSESSUAR BUTIL</option>
                <option value="AKSESSUAR BUTIL (B.N)">AKSESSUAR BUTIL (B.N)</option>
                <option value="AKSESSUAR (R) ALUTEX">AKSESSUAR (R) ALUTEX</option>
                <option value="Pvc. EPDM (UZ)">Pvc. EPDM (UZ)</option>
                <option value="REZINA PROF. & TPV">REZINA PROF. & TPV</option>
                <option value="REZINA PROF. & TPV (B.N)">REZINA PROF. & TPV (B.N)</option>
                <option value="AKSESSUAR (T) ALUTEX">AKSESSUAR (T) ALUTEX</option>
                <option value="TIOKOL">TIOKOL</option>
                <option value="Metall Prof. ALUTEX">Metall Prof. ALUTEX</option>
                <option value="Metall Profil (..)">Metall Profil (..)</option>
                <option value="Metall Profil (Engelberg)">Metall Profil (Engelberg)</option>
                <option value="Metall Profil (..) (B.N)">Metall Profil (..) (B.N)</option>
                <option value="Avt. SEKSIONNIE VOROTO">Avt. SEKSIONNIE VOROTO</option>
                <option value="ALUCOBOND">ALUCOBOND</option>
                <option value="ALUCOBOND (KG)">ALUCOBOND (KG)</option>
                <option value="EKO KABINA">EKO KABINA</option>
                <option value="GRANULA">GRANULA</option>
                <option value="KOTEL">KOTEL</option>
                <option value="KOTEL (AIRFEL)">KOTEL (AIRFEL)</option>
                <option value="KOTEL (AKFA)">KOTEL (AKFA)</option>
                <option value="KOTEL (AKFA) GOST AAA">KOTEL (AKFA) GOST AAA</option>
                <option value="KOTEL (FAHRENEIT)">KOTEL (FAHRENEIT)</option>
                <option value="KOTEL AKSSESSUAR">KOTEL AKSSESSUAR</option>
                <option value="KOTEL (AIRFEL) AKSESSUAR">KOTEL (AIRFEL) AKSESSUAR</option>
                <option value="KOTEL (AKFA) AKSESSUAR">KOTEL (AKFA) AKSESSUAR</option>
                <option value="KRASKA">KRASKA</option>
                <option value="MEBEL PROF&AKS.">MEBEL PROF&AKS.</option>
                <option value="MEBEL 3D (56/55)">MEBEL 3D (56/55)</option>
                <option value="MEBEL AKSESSUAR (ANOD)">MEBEL AKSESSUAR (ANOD)</option>
                <option value="MEBEL ANADIROVKA">MEBEL ANADIROVKA</option>
                <option value="MEBEL SVETNOY">MEBEL SVETNOY</option>
                <option value="MEBEL VAKUM">MEBEL VAKUM</option>
                <option value="RADIATOR AKSESSUAR">RADIATOR AKSESSUAR</option>
                <option value="SETKA">SETKA</option>
                <option value="SUVOQ PROFIL">SUVOQ PROFIL</option>
                <option value="VITYAJNOY USTROYSTVA">VITYAJNOY USTROYSTVA</option>
                <option value="GRANIT">GRANIT</option>
                <option value="RADIATORI PANEL (IMPORT)">RADIATORI PANEL (IMPORT)</option>
                <option value="PIGMENT POROSHKOVIY">PIGMENT POROSHKOVIY</option>
                <option value="GAZOBLOK">GAZOBLOK</option>
                <option value="PAKET">PAKET</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 230px; font-size:12px; padding-right:0px;  border-color:red;display:none;z-index:0;display:none;" id='group_zakupok`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option value="Butilchita">Butilchita</option>
            <option value="Aksessuar Import">Aksessuar Import</option>
            <option value="Aksessuar Rezina">Aksessuar Rezina</option>
            <option value="Aksessuar UZ">Aksessuar UZ</option>
            <option value="Tiokol">Tiokol</option>
            <option value="Alumin Lam">Alumin Lam</option>
            <option value="Alumin Anod (Navoiy)">Alumin Anod (Navoiy)</option>
            <option value="PVX LAM">PVX LAM</option>
            <option value="PVX OQ">PVX OQ</option>
            <option value="Metal">Metal</option>
            <option value="Alucobond">Alucobond</option>
            <option value="Alumin WHITE">Alumin WHITE</option>
            <option value="Radiator">Radiator</option>
            <option value="Kabina">Kabina</option>
            <option value="Granula">Granula</option>
            <option value="Radiator (IMPORT)">Radiator (IMPORT)</option>
            <option value="Alumin COLOUR">Alumin COLOUR</option>
            <option value="Alumin VAKUM">Alumin VAKUM</option>
            <option value="Kotel (AIRFEL)">Kotel (AIRFEL)</option>
            <option value="Kotel (AKFA)">Kotel (AKFA)</option>
            <option value="Alumin WHITE (Navoiy)">Alumin WHITE (Navoiy)</option>
            <option value="Alumin VAKUM (Navoiy)">Alumin VAKUM (Navoiy)</option>
            <option value="Alumin COLOUR (Navoiy)">Alumin COLOUR (Navoiy)</option>
            <option value="PVX LAM (Navoiy)">PVX LAM (Navoiy)</option>
            <option value="PVX OQ (Navoiy)">PVX OQ (Navoiy)</option>
            <option value="VITYAJNOYE USTROYSTVA">VITYAJNOYE USTROYSTVA</option>
            <option value="Setka">Setka</option>
            <option value="Granit">Granit</option>
            <option value="Radiator SAP (IMPORT)">Radiator SAP (IMPORT)</option>
            <option value="Radiator (Panel) Lider Line (UZ)">Radiator (Panel) Lider Line (UZ)</option>
            <option value="Rezina Tpv">Rezina Tpv</option>
            <option value="Alumin WHITE (B.N)">Alumin WHITE (B.N)</option>
            <option value="Alumin VAKUM (B.N)">Alumin VAKUM (B.N)</option>
            <option value="Aksessuar UZ Tapoich">Aksessuar UZ Tapoich</option>
            <option value="Aksessuar Import (SAP) keremas">Aksessuar Import (SAP) keremas</option>
            <option value="Radiator (Panel) AKFA (UZ)">Radiator (Panel) AKFA (UZ)</option>
            <option value="Kraska">Kraska</option>
            <option value="Gazoblok">Gazoblok</option>
            <option value="Paket">Paket</option>
            <option value="Radiator (Panel) ROYAL (UZ)">Radiator (Panel) ROYAL (UZ)</option>
           
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0" id='zavod`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="ZAVOD BUTIL">ZAVOD BUTIL</option>
                <option value="IMPORT">IMPORT</option>
                <option value="ZAVOD REZINA">ZAVOD REZINA</option>
                <option value="ZAVOD TIOKOL">ZAVOD TIOKOL</option>
                <option value="ZAVOD METAL">ZAVOD METAL</option>
                <option value="ZAVOD GRANULA">ZAVOD GRANULA</option>
                <option value="ZAVOD REZINA TPV">ZAVOD REZINA TPV</option>
                <option value="ZAVOD KRASKA">ZAVOD KRASKA</option>
                <option value="ZAVOD TAPOICH AKS UZ">ZAVOD TAPOICH AKS UZ</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 145px; font-size:12px; padding-right:0px; display:none;z-index:0" id='segment`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="Aldoks">Aldoks</option>
                <option value="Стандарт">Стандарт</option>
                <option value="Премиум">Премиум</option>
                <option value="Аксессуар">Аксессуар</option>
                <option value="Аксессуар 2">Аксессуар 2</option>
                <option value="Аксессуар 3">Аксессуар 3</option>
                <option value="Falcon">Falcon</option>
                <option value="Эконом">Эконом</option>
                <option value="Mebel">Mebel</option>
                <option value="LAMBRI">LAMBRI</option>
                <option value="RETPEN 10%">RETPEN 10%</option>
                <option value="RETPEN 15%">RETPEN 15%</option>
            </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none; " id='bux_naz`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px; font-size:12px; padding-right:0px; display:none;z-index:0" id='tip_clienta`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  ></option>
                <option value="AKFA">AKFA</option>
                <option value="IMZO">IMZO</option>
                <option value="FRANCHISING">FRANCHISING</option>
                <option value="AKFA-IMZO-FRANCHISING">AKFA-IMZO-FRANCHISING</option>
                <option value="IMZO-FRANCHISING">IMZO-FRANCHISING</option>
            </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0"  id='svet_product`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
            <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px; border-color:red;display:none;z-index:0"  id='diller`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option   value="Да">Да</option>
                <option   value="Нет">Нет</option>
               
            </select>
            </div>
        </td>

        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;" id='comment`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>

        </tr>`
        
    }
    return text
}

text = front_piece()


var table = $('#table-artikul')

// table.append(text)



if(status_proccess == 'new'){
    table.append(text)

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

function removeQuotesFromStartAndEnd(str) {
    // Remove double quotes from the beginning and end of the string
    return str.replace(/^"+|"+$/g, '');
}

function select_condition(id){
    var vid_zayavki = $('#vid_zayavki'+id).val()
    var id_savdo =$('#id_savdo'+id)
    var naz_savdo =$('#naz_savdo'+id)
    var sapcode =$('#sapcode'+id)
    var bei =$('#bei'+id)
    var aei =$('#aei'+id)
    var koefitsiyent =$('#koefitsiyent'+id)
    var sena_c_ndc =$('#sena_c_ndc'+id)
    var sena_bez_ndc =$('#sena_bez_ndc'+id)
    var ed_izm =$('#ed_izm'+id)
    var group =$('#group'+id)
    var group_zakupok =$('#group_zakupok'+id)
    var zavod =$('#zavod'+id)
    var segment =$('#segment'+id)
    var bux_naz =$('#bux_naz'+id)
    var tip_clienta =$('#tip_clienta'+id)
    var svet_product =$('#svet_product'+id)
    var diller =$('#diller'+id)
    var comment =$('#comment'+id)

    id_savdo.css('display','block')
    naz_savdo.css('display','block')

    id_savdo.css('border-color','red')
    naz_savdo.css('border-color','red')

    id_savdo.val('')
    naz_savdo.val('')
    sapcode.val('')
    bei.val('')
    aei.val('')
    koefitsiyent.val('')
    sena_c_ndc.val('')
    sena_bez_ndc.val('')
    ed_izm.val('')
    group.val('')
    group_zakupok.val('')
    zavod.val('')
    segment.val('')
    bux_naz.val('')
    tip_clienta.val('')
    svet_product.val('')
    diller.val('')
    comment.val('')

    sapcode.css('display','none')
    bei.css('display','none')
    aei.css('display','none')
    koefitsiyent.css('display','none')
    sena_c_ndc.css('display','none')
    sena_bez_ndc.css('display','none')
    ed_izm.css('display','none')
    group.css('display','none')
    group_zakupok.css('display','none')
    zavod.css('display','none')
    segment.css('display','none')
    bux_naz.css('display','none')
    tip_clienta.css('display','none')
    svet_product.css('display','none')
    diller.css('display','none')

   

    if(vid_zayavki =='Изменения цена'){
        sena_c_ndc.css('display','block')
        sena_bez_ndc.css('display','block')
        ed_izm.css('display','block')
        tip_clienta.css('display','block')

        sena_c_ndc.css('border-color','red')
        sena_bez_ndc.css('border-color','red')
        ed_izm.css('border-color','red')
        tip_clienta.css('border-color','red')

        data_base[id] = new BasePokritiya()
        data_base[id].id =1
        data_base[id].vid_zayavki ='Изменения цена'
    }
    if(vid_zayavki =='Изменения веса'){
        bei.css('display','block')
        aei.css('display','block')
        koefitsiyent.css('display','block')

        bei.css('border-color','red')
        aei.css('border-color','red')
        koefitsiyent.css('border-color','red')
        data_base[id] = new BasePokritiya()
        data_base[id].id =2
        data_base[id].vid_zayavki ='Изменения веса'
    }
    if(vid_zayavki =='Изменения группа'){
        group.css('display','block')
        group.css('border-color','red')

        data_base[id] = new BasePokritiya()
        data_base[id].id =3
        data_base[id].vid_zayavki ='Изменения группа'
    }
    if(vid_zayavki =='Изменения группа закупок'){
        console.log(group_zakupok,'vidddd')
        group_zakupok.css('display','block')
        group_zakupok.css('border-color','red')

        data_base[id] = new BasePokritiya()
        data_base[id].id =4
        data_base[id].vid_zayavki ='Изменения группа закупок'
    }
    if(vid_zayavki =='Изменения сегмент'){
        segment.css('display','block')
        segment.css('border-color','red')

        data_base[id] = new BasePokritiya()
        data_base[id].id =5
        data_base[id].vid_zayavki ='Изменения сегмент'
    }
    if(vid_zayavki =='Изменения бухгалтерская названия'){
        bux_naz.css('display','block')
        bux_naz.css('border-color','red')

        data_base[id] = new BasePokritiya()
        data_base[id].id =6
        data_base[id].vid_zayavki ='Изменения бухгалтерская названия'
    }
    if(vid_zayavki =='Изменения завода'){
        zavod.css('display','block')
        zavod.css('border-color','red')

        data_base[id] = new BasePokritiya()
        data_base[id].id =7
        data_base[id].vid_zayavki ='Изменения завода'
    }
    if(vid_zayavki =='Изменения цвет продукта'){
        svet_product.css('display','block')
        svet_product.css('border-color','red')

        data_base[id] = new BasePokritiya()
        data_base[id].id =8
        data_base[id].vid_zayavki ='Изменения цвет продукта'
    }
    if(vid_zayavki =='Изменения вид клиента'){
        diller.css('display','block')
        diller.css('border-color','red')

        data_base[id] = new BasePokritiya()
        data_base[id].id =9
        data_base[id].vid_zayavki ='Изменения вид клиента'
    }




}





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
            
            
            var data = new BasePokritiya()
            for(key in data_base[id]){
                data[key] = data_base[id][key]
            }
                
            

            

            data_base[size+1] = data
            
            var s = size+1
        }else{
            var data = data_base[id]
            var s = ii
        }

        var vid_zayavki = data.vid_zayavki;
        var id_savdo = data.id_savdo;
        var naz_savdo = data.naz_savdo;
        var sapcode = data.sapcode;
        var bei = data.bei;
        var aei = data.aei;
        var koefitsiyent = data.koefitsiyent;
        var sena_c_ndc = data.sena_c_ndc;
        var sena_bez_ndc = data.sena_bez_ndc;
        var ed_izm = data.ed_izm;
        var group = data.group;
        var group_zakupok = data.group_zakupok;
        var zavod = data.zavod;
        var segment = data.segment;
        var bux_naz = data.bux_naz;
        var tip_clienta = data.tip_clienta;
        var svet_product = data.svet_product;
        var diller = data.diller;
        var comment = data.comment;
        
        check_input_and_change(vid_zayavki,'#vid_zayavki'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(id_savdo,'#id_savdo'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(naz_savdo,'#naz_savdo'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(sapcode,'#sapcode'+s,dis=false,is_req=false,is_req_simple=true)


        if(vid_zayavki =='Изменения цена'){
            check_input_and_change(sena_c_ndc,'#sena_c_ndc'+s,dis=false,is_req=true,is_req_simple=false) 
            check_input_and_change(sena_bez_ndc,'#sena_bez_ndc'+s,dis=false,is_req=true,is_req_simple=false) 
            check_input_and_change(ed_izm,'#ed_izm'+s,dis=false,is_req=true,is_req_simple=false) 
            check_input_and_change(tip_clienta,'#tip_clienta'+s,dis=false,is_req=true,is_req_simple=false) 
            
        }
        if(vid_zayavki =='Изменения веса'){
            check_input_and_change(bei,'#bei'+s,dis=false,is_req=true,is_req_simple=false) 
            check_input_and_change(aei,'#aei'+s,dis=false,is_req=true,is_req_simple=false) 
            check_input_and_change(koefitsiyent,'#koefitsiyent'+s,dis=false,is_req=true,is_req_simple=false) 
            
        }
        if(vid_zayavki =='Изменения группа'){
            check_input_and_change(group,'#group'+s,dis=false,is_req=true,is_req_simple=false) 
        }
        if(vid_zayavki =='Изменения группа закупок'){
            check_input_and_change(group_zakupok,'#group_zakupok'+s,dis=false,is_req=true,is_req_simple=false) 
        }
        if(vid_zayavki =='Изменения сегмент'){
            check_input_and_change(segment,'#segment'+s,dis=false,is_req=true,is_req_simple=false)    
        }
        if(vid_zayavki =='Изменения бухгалтерская названия'){
            check_input_and_change(bux_naz,'#bux_naz'+s,dis=false,is_req=true,is_req_simple=false)  
        }
        if(vid_zayavki =='Изменения завода'){
            check_input_and_change(zavod,'#zavod'+s,dis=false,is_req=true,is_req_simple=false) 
        }
        if(vid_zayavki =='Изменения цвет продукта'){
            check_input_and_change(svet_product,'#svet_product'+s,dis=false,is_req=true,is_req_simple=false) 
        }
        if(vid_zayavki =='Изменения вид клиента'){
            check_input_and_change(diller,'#diller'+s,dis=false,is_req=true,is_req_simple=false) 
        }

        
        check_input_and_change(comment,'#comment'+s,dis=false,is_req=false,is_req_simple=true)
        
        
    }


}



function check_input_and_change(val,selector,dis=false,is_req=false,is_req_simple=false){
    if(is_req){
        
        // $(selector).attr('disabled',false)
        $(selector).css('display','block')
        $(selector).css('border-color','red')

    }
    if(is_req_simple){
        
        // $(selector).attr('disabled',false)
        $(selector).css('display','block')
        $(selector).css('border-color','#dedad9')

    }
    if(val !=NaN && val !='' && String(val) != 'NaN'){
        var sel = $(selector)
        // sel.attr('disabled',dis)
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





function artukil_clear(id){
    
    var table_tr =$('#table_tr'+id);
    
    data_base[id].vid_zayavki=NaN
    data_base[id].id_savdo=NaN
    data_base[id].naz_savdo=NaN
    data_base[id].sapcode=NaN
    data_base[id].bei=NaN
    data_base[id].aei=NaN
    data_base[id].koefitsiyent=NaN
    data_base[id].sena_c_ndc=NaN
    data_base[id].sena_bez_ndc=NaN
    data_base[id].ed_izm=NaN
    data_base[id].group=NaN
    data_base[id].group_zakupok=NaN
    data_base[id].zavod=NaN
    data_base[id].segment=NaN
    data_base[id].bux_naz=NaN
    data_base[id].tip_clienta=NaN
    data_base[id].svet_product=NaN
    data_base[id].diller=NaN
    data_base[id].comment=NaN

    
    table_tr.css('background-color','white')
    

    var vid_zayavki = $('#vid_zayavki'+id)
    var id_savdo =$('#id_savdo'+id)
    var naz_savdo =$('#naz_savdo'+id)
    var sapcode =$('#sapcode'+id)
    var bei =$('#bei'+id)
    var aei =$('#aei'+id)
    var koefitsiyent =$('#koefitsiyent'+id)
    var sena_c_ndc =$('#sena_c_ndc'+id)
    var sena_bez_ndc =$('#sena_bez_ndc'+id)
    var ed_izm =$('#ed_izm'+id)
    var group =$('#group'+id)
    var group_zakupok =$('#group_zakupok'+id)
    var zavod =$('#zavod'+id)
    var segment =$('#segment'+id)
    var bux_naz =$('#bux_naz'+id)
    var tip_clienta =$('#tip_clienta'+id)
    var svet_product =$('#svet_product'+id)
    var diller =$('#diller'+id)
    var comment =$('#comment'+id)

    
    vid_zayavki.val('')
    id_savdo.val('')
    naz_savdo.val('')
    sapcode.val('')
    bei.val('')
    aei.val('')
    koefitsiyent.val('')
    sena_c_ndc.val('')
    sena_bez_ndc.val('')
    ed_izm.val('')
    group.val('')
    group_zakupok.val('')
    zavod.val('')
    segment.val('')
    bux_naz.val('')
    tip_clienta.val('')
    svet_product.val('')
    diller.val('')
    comment.val('')

    id_savdo.css('display','none')
    naz_savdo.css('display','none')
    sapcode.css('display','none')
    bei.css('display','none')
    aei.css('display','none')
    koefitsiyent.css('display','none')
    sena_c_ndc.css('display','none')
    sena_bez_ndc.css('display','none')
    ed_izm.css('display','none')
    group.css('display','none')
    group_zakupok.css('display','none')
    zavod.css('display','none')
    segment.css('display','none')
    bux_naz.css('display','none')
    tip_clienta.css('display','none')
    svet_product.css('display','none')
    diller.css('display','none')


}


function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
        
        var vid_zayavki = $('#vid_zayavki'+id).val()
        var id_savdo =$('#id_savdo'+id)
        var naz_savdo =$('#naz_savdo'+id)
        var sapcode =$('#sapcode'+id)
        var bei =$('#bei'+id)
        var aei =$('#aei'+id)
        var koefitsiyent =$('#koefitsiyent'+id)
        var sena_c_ndc =$('#sena_c_ndc'+id)
        var sena_bez_ndc =$('#sena_bez_ndc'+id)
        var ed_izm =$('#ed_izm'+id)
        var group =$('#group'+id)
        var group_zakupok =$('#group_zakupok'+id)
        var zavod =$('#zavod'+id)
        var segment =$('#segment'+id)
        var bux_naz =$('#bux_naz'+id)
        var tip_clienta =$('#tip_clienta'+id)
        var svet_product =$('#svet_product'+id)
        var diller =$('#diller'+id)
        var comment =$('#comment'+id)
        
        
        
        if(id_savdo.val()!=''){
            data_base[id].id_savdo = id_savdo.val();
            id_savdo.css('border-color','#dedad9')
        }else{
            id_savdo.css('border-color','red')
            data_base[id].id_savdo = NaN;
        }
        if(naz_savdo.val()!=''){
            data_base[id].naz_savdo = removeQuotesFromStartAndEnd(naz_savdo.val());
            naz_savdo.css('border-color','#dedad9')
        }else{
            naz_savdo.css('border-color','red')
            data_base[id].naz_savdo = NaN;
        }

        if(sapcode.val()!=''){
            data_base[id].sapcode = sapcode.val();
            sapcode.css('border-color','#dedad9')
        }else{
            sapcode.css('border-color','#dedad9')
            data_base[id].sapcode = NaN;
        }


        if(vid_zayavki =='Изменения цена'){
            if(sena_c_ndc.val()!=''){
                data_base[id].sena_c_ndc = sena_c_ndc.val();
                sena_c_ndc.css('border-color','#dedad9')
            }else{
                sena_c_ndc.css('border-color','red')
                data_base[id].sena_c_ndc = NaN;
            }
            if(sena_bez_ndc.val()!=''){
                data_base[id].sena_bez_ndc = sena_bez_ndc.val();
                sena_bez_ndc.css('border-color','#dedad9')
            }else{
                sena_bez_ndc.css('border-color','red')
                data_base[id].sena_bez_ndc = NaN;
            }
            if(ed_izm.val()!=''){
                data_base[id].ed_izm = ed_izm.val();
                ed_izm.css('border-color','#dedad9')
            }else{
                ed_izm.css('border-color','red')
                data_base[id].ed_izm = NaN;
            }
            if(tip_clienta.val()!=''){
                data_base[id].tip_clienta = tip_clienta.val();
                tip_clienta.css('border-color','#dedad9')
            }else{
                tip_clienta.css('border-color','red')
                data_base[id].tip_clienta = NaN;
            }
           
        }
        if(vid_zayavki =='Изменения веса'){
            if(bei.val()!=''){
                data_base[id].bei = bei.val();
                bei.css('border-color','#dedad9')
            }else{
                bei.css('border-color','red')
                data_base[id].bei = NaN;
            }
            if(aei.val()!=''){
                data_base[id].aei = aei.val();
                aei.css('border-color','#dedad9')
            }else{
                aei.css('border-color','red')
                data_base[id].aei = NaN;
            }
            if(koefitsiyent.val()!=''){
                data_base[id].koefitsiyent = koefitsiyent.val();
                koefitsiyent.css('border-color','#dedad9')
            }else{
                koefitsiyent.css('border-color','red')
                data_base[id].koefitsiyent = NaN;
            }
        }
        if(vid_zayavki =='Изменения группа'){
            if(group.val()!=''){
                data_base[id].group = group.val();
                group.css('border-color','#dedad9')
            }else{
                group.css('border-color','red')
                data_base[id].group = NaN;
            }
            
        }
        if(vid_zayavki =='Изменения группа закупок'){
            if(group_zakupok.val()!=''){
                data_base[id].group_zakupok = group_zakupok.val();
                group_zakupok.css('border-color','#dedad9')
            }else{
                group_zakupok.css('border-color','red')
                data_base[id].group_zakupok = NaN;
            }
        }
        if(vid_zayavki =='Изменения сегмент'){
            if(segment.val()!=''){
                data_base[id].segment = segment.val();
                segment.css('border-color','#dedad9')
            }else{
                segment.css('border-color','red')
                data_base[id].segment = NaN;
            }
            
        }
        if(vid_zayavki =='Изменения бухгалтерская названия'){
            if(bux_naz.val()!=''){
                data_base[id].bux_naz = bux_naz.val();
                bux_naz.css('border-color','#dedad9')
            }else{
                bux_naz.css('border-color','red')
                data_base[id].bux_naz = NaN;
            }
           
        }
        if(vid_zayavki =='Изменения завода'){
            if(zavod.val()!=''){
                data_base[id].zavod = zavod.val();
                zavod.css('border-color','#dedad9')
            }else{
                zavod.css('border-color','red')
                data_base[id].zavod = NaN;
            }
            
        }
        if(vid_zayavki =='Изменения цвет продукта'){
            if(svet_product.val()!=''){
                data_base[id].svet_product = svet_product.val();
                svet_product.css('border-color','#dedad9')
            }else{
                svet_product.css('border-color','red')
                data_base[id].svet_product = NaN;
            }
        }
        if(vid_zayavki =='Изменения вид клиента'){
            if(diller.val()!=''){
                data_base[id].diller = diller.val();
                diller.css('border-color','#dedad9')
            }else{
                diller.css('border-color','red')
                data_base[id].diller = NaN;
            }
            
        }
    


        
        
        if(comment.val()!=''){
            data_base[id].comment = comment.val();
            comment.css('border-color','#dedad9')
        }else{
            comment.css('border-color','#dedad9')
            data_base[id].comment = NaN;
        }


    var data = data_base[id].get_kratkiy_tekst()
    
    if(data.accept){
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','#2de319')
        data_base[id].full =true
    }else{
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','white')
        data_base[id].full =false

    }
    }
}

function add_column(){
        
    text =""
    var sizeee = $('#table-artikul tr').length;
    
    text = front_piece(start = sizeee+1, end = sizeee+2)

    
    var table = $('#table-artikul')
    table.append(text)
    


}




