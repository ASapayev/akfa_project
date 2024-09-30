class BasePokritiya{
    constructor(
        full=false,//done
        id=NaN, //done
        vid_zayavki=NaN,
        balance_ed=NaN,
        rol_bp=NaN,
        group_del_partner=NaN,
        nomer_del_partner=NaN,
        imya_org=NaN,
        imya=NaN,
        familiya=NaN,
        ulitsa=NaN,
        nomer_doma=NaN,
        pochta_index=NaN,
        gorod=NaN,
        kod_stran=NaN,
        region=NaN,
        rayon=NaN,
        nomer_tel=NaN,
        nomer_mob=NaN,
        inn=NaN,
        ndc=NaN,
        nalog=NaN,
        oked=NaN,
        okpo=NaN,
        coato=NaN,
        coogu=NaN,
        kod_stran_bank=NaN,
        klyuch_banka=NaN,
        bank_schot=NaN,
        valyuta_zakaz=NaN,

        usloviya_plateja=NaN,
        sbitovoy_organ=NaN,
        kanal_sbita=NaN,
        sektor=NaN,
        rayon_sbita=NaN,
        gruppa_sena=NaN,

        sxema_kliyenta=NaN,
        status_gruppa_kliyent=NaN,
        usloviya_otgruz=NaN,
        sbit_debitora=NaN,
        sbit_nalog=NaN,
        kontrol_schot=NaN,
        kontrol_debitora=NaN,
        
        
        ){
      
        this.full = full;
        this.id = id;
        this.vid_zayavki = vid_zayavki;
        this.balance_ed = balance_ed
        this.rol_bp = rol_bp
        this.group_del_partner = group_del_partner
        this.nomer_del_partner = nomer_del_partner
        this.imya_org = imya_org
        this.imya = imya
        this.familiya = familiya
        this.ulitsa = ulitsa
        this.nomer_doma = nomer_doma
        this.pochta_index = pochta_index
        this.gorod = gorod
        this.kod_stran = kod_stran
        this.region = region
        this.rayon = rayon
        this.nomer_tel = nomer_tel
        this.nomer_mob = nomer_mob
        this.inn = inn
        this.ndc = ndc
        this.nalog = nalog
        this.oked = oked
        this.okpo = okpo
        this.coato = coato
        this.coogu = coogu
        this.kod_stran_bank = kod_stran_bank
        this.klyuch_banka = klyuch_banka
        this.bank_schot = bank_schot
        this.valyuta_zakaz = valyuta_zakaz
        this.usloviya_plateja = usloviya_plateja
        this.sbitovoy_organ = sbitovoy_organ
        this.kanal_sbita = kanal_sbita
        this.sektor = sektor
        this.rayon_sbita = rayon_sbita
        this.gruppa_sena = gruppa_sena
        this.sxema_kliyenta = sxema_kliyenta
        this.status_gruppa_kliyent = status_gruppa_kliyent
        this.usloviya_otgruz = usloviya_otgruz
        this.sbit_debitora = sbit_debitora
        this.sbit_nalog = sbit_nalog
        this.kontrol_schot = kontrol_schot
        this.kontrol_debitora = kontrol_debitora
        
        
    }
    get_kratkiy_tekst(){
            switch(this.id){
                case 1:
            
                        if (this.balance_ed && this.rol_bp&& this.group_del_partner&&this.imya_org&&this.gorod){
                            
                            if(this.rol_bp =='Клиент' || this.rol_bp =='Поставщик и Клиент'){
                                if(this.group_del_partner=='B001 - Локальные Юридические Лица'){
                                        
                                    if(this.inn&&this.kod_stran && this.klyuch_banka&&this.bank_schot&&this.valyuta_zakaz&&this.usloviya_plateja&&this.sbitovoy_organ&&this.kanal_sbita&&this.sektor&&this.rayon_sbita&&this.gruppa_sena&&this.sxema_kliyenta&&this.status_gruppa_kliyent&&this.usloviya_otgruz&&this.sbit_debitora&&this.sbit_nalog){
                                        return {'text':'','accept':true}
                                    }else{
                                        return {'text':'','accept':false}
                                    }
                                }else{
                                    if(this.kod_stran && this.klyuch_banka&&this.bank_schot&&this.valyuta_zakaz&&this.usloviya_plateja&&this.sbitovoy_organ&&this.kanal_sbita&&this.sektor&&this.rayon_sbita&&this.gruppa_sena&&this.sxema_kliyenta&&this.status_gruppa_kliyent&&this.usloviya_otgruz&&this.sbit_debitora&&this.sbit_nalog){
                                        return {'text':'','accept':true}
                                    }else{
                                        return {'text':'','accept':false}
                                    }

                                }

                            }else if(this.rol_bp == 'Поставщик'){
                                if(this.group_del_partner=='B001 - Локальные Юридические Лица'){
                                        
                                    if(this.kod_stran && this.klyuch_banka&&this.bank_schot&&this.valyuta_zakaz&&this.inn){
                                        return {'text':'','accept':true}
                                    }else{
                                        return {'text':'','accept':false}
                                    }
                                }else{
                                    if(this.kod_stran && this.klyuch_banka&&this.bank_schot&&this.valyuta_zakaz){
                                        return {'text':'','accept':true}
                                    }else{
                                        return {'text':'','accept':false}
                                    }

                                }

                            }else{
                                return {'text':'','accept':false}
                            }



                        }else{
                            return {'text':'','accept':false}
                        }
                        break;
                case 2:
            
                        if (this.balance_ed && this.nomer_del_partner&& this.imya_org){
        
                            return {'text':'','accept':true}
                        }else{
                            return {'text':'','accept':false}
                        }
                        break;
                case 3:
            
                        if (this.balance_ed &&this.rol_bp&& this.group_del_partner&&this.nomer_del_partner&& this.imya_org){
        
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
        
        if(status_proccess1 == 'new'){
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
            <select class="form-select" aria-label="" style="width: 120px; font-size:12px; padding-right:0px;z-index:0" id='vid_zayavki`+String(i)+`' onchange='select_condition(`+String(i)+`)' required>
                <option  selected></option>
                <option  value="Создание">Создание</div>
                <option  value="Изменения">Изменения</div>
                <option  value="Расширение">Расширение</div>
            </select>
            </div>
        </td>
       <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 280px; font-size:12px; padding-right:0px; z-index:0;display:none;"  id='balance_ed`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="1000 - AKFA Engineering&Management">1000 - AKFA Engineering&Management</option>
                <option value="1100 - AKFA Building Materials">1100 - AKFA Building Materials</option>
                <option value="1200 - AKFA Extrusions">1200 - AKFA Extrusions</option>
                <option value="1300 - AKFA Assembly">1300 - AKFA Assembly</option>
                <option value="1310 - AKFA Project">1310 - AKFA Project</option>
                <option value="1400 - AKFA Logistics">1400 - AKFA Logistics</option>
                <option value="1500 - AKFA Food Service">1500 - AKFA Food Service</option>
                <option value="4500 - AKFA ACCESSORIES">4500 - AKFA ACCESSORIES</option>
                <option value="4600 - AKFA AKP">4600 - AKFA AKP</option>
                <option value="5100 - AKFA Radiators">5100 - AKFA Radiators</option>
               
            </select>
            </div>
        </td>
       <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 200px; font-size:12px; padding-right:0px; z-index:0;display:none;"  id='rol_bp`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="Клиент">Клиент</option>
                <option value="Поставщик">Поставщик</option>
                <option value="Поставщик и Клиент">Поставщик и Клиент</option>
            </select>
            </div>
        </td>
       <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 290px; font-size:12px; padding-right:0px; z-index:0;display:none;"  id='group_del_partner`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="B001 - Локальные Юридические Лица">B001 - Локальные Юридические Лица</option>
                <option value="B002 - Иностранные Юридические Лица">B002 - Иностранные Юридические Лица</option>
                <option value="B003 - Кредитные организации">B003 - Кредитные организации</option>
                <option value="B004 - Сотрудники">B004 - Сотрудники</option>
                <option value="B005 - Физ.Лица Конкуренты ИП">B005 - Физ.Лица Конкуренты ИП</option>
                <option value="B006 - Гос. органы, расчет с бюджет. Орг">B006 - Гос. органы, расчет с бюджет. Орг</option>
                <option value="B007 - Налоговые органы">B007 - Налоговые органы</option>
                <option value="B008 - Счет разных лиц">B008 - Счет разных лиц</option>
                <option value="B009 - Технические контрагенты ">B009 - Технические контрагенты </option>
                <option value="B010 - Внутригрупповые партнеры">B010 - Внутригрупповые партнеры</option>
                <option value="B011 - Учредители">B011 - Учредители</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='nomer_del_partner`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='imya_org`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='imya`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='familiya`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='ulitsa`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='nomer_doma`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='pochta_index`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='gorod`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='kod_stran`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='region`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='rayon`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='nomer_tel`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='nomer_mob`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='inn`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='ndc`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='nalog`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='oked`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='okpo`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='coato`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='coogu`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='kod_stran_bank`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='klyuch_banka`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 170px; font-size:10px;height:27px;z-index:0;display:none;" id='bank_schot`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 195px; font-size:12px; padding-right:0px; z-index:0;display:none;"  id='valyuta_zakaz`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="UZS - Узбекский сум">UZS - Узбекский сум</option>
                <option value="USD - Доллар США">USD - Доллар США</option>
                <option value="RUB - Российский рубль">RUB - Российский рубль</option>
                <option value="TRL - Турецкая лира (стар.)">TRL - Турецкая лира (стар.)</option>
                <option value="TRY - Турецкая лира">TRY - Турецкая лира</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 360px; font-size:12px; padding-right:0px; z-index:0;display:none;"  id='usloviya_plateja`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="A100  100% предоплата">A100  100% предоплата</option>
                <option value="A103  100% до отгрузки">A103  100% до отгрузки</option>
                <option value="A109  10% предоплата, 90% до отгрузки">A109  10% предоплата, 90% до отгрузки</option>
                <option value="A303  30% предоплата, 70% до отгрузки">A303  30% предоплата, 70% до отгрузки</option>
                <option value="A305  30% до отгрузки, 70% после">A305  30% до отгрузки, 70% после</option>
                <option value="A405  40% до отгрузки, 60% после">A405  40% до отгрузки, 60% после</option>
                <option value="A503  50% предоплата, 50% до отгрузки">A503  50% предоплата, 50% до отгрузки</option>
                <option value="A560  50% предоплата, 50% в течение 60 дней">A560  50% предоплата, 50% в течение 60 дней</option>
                <option value="A575  50% предоплата, 50% в течение 75 дней">A575  50% предоплата, 50% в течение 75 дней</option>
                <option value="P020  В течение 20 дней">P020  В течение 20 дней</option>
                <option value="P026  в течение 20 дней - 50%, в течение 60 дней - 50%">P026  в течение 20 дней - 50%, в течение 60 дней - 50%</option>
                <option value="P030  В течение 30 дней">P030  В течение 30 дней</option>
                <option value="P040  В течение 40 дней">P040  В течение 40 дней</option>
                <option value="P045  В течение 45 дней">P045  В течение 45 дней</option>
                <option value="P060  В течение 60 дней">P060  В течение 60 дней</option>
                <option value="P090  В течение 90 дней">P090  В течение 90 дней</option>
                <option value="P180  В течение 180 дней">P180  В течение 180 дней</option>
            </select>
            </div>
        </td>
         <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 270px; font-size:12px; padding-right:0px; z-index:0;display:none;"  id='sbitovoy_organ`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="1000 - AKFA Engineering&Management">1000 - AKFA Engineering&Management</option>
                <option value="1100 - AKFA Building Materials">1100 - AKFA Building Materials</option>
                <option value="1200 - AKFA Extrusions">1200 - AKFA Extrusions</option>
                <option value="1300 - AKFA Assembly">1300 - AKFA Assembly</option>
                <option value="1310 - AKFA Project">1310 - AKFA Project</option>
                <option value="1400 - AKFA Logistics">1400 - AKFA Logistics</option>
                <option value="1500 - AKFA Food Service">1500 - AKFA Food Service</option>
                <option value="4500 - AKFA ACCESSORIES">4500 - AKFA ACCESSORIES</option>
                <option value="4600 - AKFA AKP">4600 - AKFA AKP</option>
                <option value="4700 - AKFA EPDM & PAINT">4700 - AKFA EPDM & PAINT</option>
                <option value="5100 - AKFA Radiators">5100 - AKFA Radiators</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 195px; font-size:12px; padding-right:0px; z-index:0;display:none;"  id='kanal_sbita`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="10 - Локальные продажи">10 - Локальные продажи</option>
                <option value="20 - Экспорт">20 - Экспорт</option>
                <option value="99 - Перемещение">99 - Перемещение</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 250px; font-size:12px; padding-right:0px; z-index:0;display:none;"  id='sektor`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="01 - Алюминиевый профиль">01 - Алюминиевый профиль</option>
                <option value="20 - Услуги">20 - Услуги</option>
                <option value="27 - Прочее">27 - Прочее</option>
                <option value="99 - Перемещение запасов">99 - Перемещение запасов</option>
                <option value="18 - Аксессуары Импорт">18 - Аксессуары Импорт</option>
                <option value="15 - АКП">15 - АКП</option>
                <option value="10 - ACS UZ">10 - ACS UZ</option>
                <option value="09 - Радиатор">09 - Радиатор</option>
                <option value="08 - Резина EPDM">08 - Резина EPDM</option>
                <option value="37 - Порошковая краска">37 - Порошковая краска</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 190px; font-size:12px; padding-right:0px; z-index:0;display:none;"  id='rayon_sbita`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="000001 - Представители">000001 - Представители</option>
                <option value="000002 - Дилеры">000002 - Дилеры</option>
                <option value="000003 - Шоурум">000003 - Шоурум</option>
                <option value="000004 - Третьи лица">000004 - Третьи лица</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 210px; font-size:12px; padding-right:0px; z-index:0;display:none;"  id='gruppa_sena`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="01 - Дилер">01 - Дилер</option>
                <option value="02 - Оптовик">02 - Оптовик</option>
                <option value="03 - Бюджет. организация">03 - Бюджет. организация</option>
                <option value="04 - Благотвор и менценат">04 - Благотвор и менценат</option>
                <option value="05 - Девелоп. организ. 1">05 - Девелоп. организ. 1</option>
                <option value="06 - Девелоп. организ. 1">06 - Девелоп. организ. 1</option>
                <option value="E1 - Валюта Евро">E1 - Валюта Евро</option>
                <option value="E2 - Валюта Доллар">E2 - Валюта Доллар</option>
            </select>
            </div>
        </td>
         <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 190px; font-size:12px; padding-right:0px; z-index:0;display:none;"  id='sxema_kliyenta`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="01 - Схема 01">01 - Схема 01</option>
                <option value="02 - Схема 02">02 - Схема 02</option>
                <option value="1 - Стандарт">1 - Стандарт</option>
                <option value="2 - Стандарт вкл. НДС">2 - Стандарт вкл. НДС</option>
                <option value="3">3</option>
                <option value="5">5</option>
                <option value="6 - Р-т по конт. по усл.">6 - Р-т по конт. по усл.</option>
                <option value="G - Клнт-станд. (ISHTSW)">G - Клнт-станд. (ISHTSW)</option>
                <option value="M - ЦМ в завис. от веса">M - ЦМ в завис. от веса</option>
                <option value="N - ЦМ стандарт">N - ЦМ стандарт</option>
                <option value="R - УДР: клиент">R - УДР: клиент</option>
                <option value="W - AECMA-клиент">W - AECMA-клиент</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 130px; font-size:12px; padding-right:0px; z-index:0;display:none;"  id='status_gruppa_kliyent`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected value=""></option>
                <option value="+  маскирован.">+  маскирован.</option>
                <option value="1 - A-материал">1 - A-материал</option>
                <option value="2 - Группа 2">2 - Группа 2</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 135px; font-size:12px; padding-right:0px; z-index:0;display:none;"  id='usloviya_otgruz`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="01 - Стандарт">01 - Стандарт</option>
                <option value="02 - Самовывоз">02 - Самовывоз</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 175px; font-size:12px; padding-right:0px; z-index:0;display:none;"  id='sbit_debitora`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="01 - Третьи стороны">01 - Третьи стороны</option>
                <option value="02 - Интеркомпани">02 - Интеркомпани</option>
                <option value="03 - Физические лица">03 - Физические лица</option>
                <option value="04 - Сотрудники">04 - Сотрудники</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 210px; font-size:12px; padding-right:0px; z-index:0;display:none;"  id='sbit_nalog`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="0 - Необлагаемый налогом">0 - Необлагаемый налогом</option>
                <option value="1 - Облагаемый налогом">1 - Облагаемый налогом</option>
                <option value="2 - Освобожденный">2 - Освобожденный</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px; z-index:0;display:none;"  id='kontrol_schot`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="3300101200">3300101200</option>
                <option value="4600110200">4600110200</option>
                <option value="3700300000">3700300000</option>
                <option value="3309900200">3309900200</option>
                <option value="3400100000">3400100000</option>
                <option value="3300101100">3300101100</option>
                <option value="3750100000">3750100000</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 110px; font-size:12px; padding-right:0px; z-index:0;display:none;"  id='kontrol_debitora`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="2200100200">2200100200</option>
                <option value="1600110200">1600110200</option>
                <option value="2200100100">2200100100</option>
            </select>
            </div>
        </td>




        </tr>`
        
    }
    return text
}

text = front_piece()


var table = $('#table-artikul')

// table.append(text)


if(status_proccess1 == 'new'){
    table.append(text)

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

function select_condition(id){
    var vid_zayavki = $('#vid_zayavki'+id).val()
    var balance_ed =$('#balance_ed'+id)
    var rol_bp =$('#rol_bp'+id)
    var group_del_partner =$('#group_del_partner'+id)
    var nomer_del_partner =$('#nomer_del_partner'+id)
    var imya_org =$('#imya_org'+id)
    var imya =$('#imya'+id)
    var familiya =$('#familiya'+id)
    var ulitsa =$('#ulitsa'+id)
    var nomer_doma =$('#nomer_doma'+id)
    var pochta_index =$('#pochta_index'+id)
    var gorod =$('#gorod'+id)
    var kod_stran =$('#kod_stran'+id)
    var region =$('#region'+id)
    var rayon =$('#rayon'+id)
    var nomer_tel =$('#nomer_tel'+id)
    var nomer_mob =$('#nomer_mob'+id)
    var inn =$('#inn'+id)
    var ndc =$('#ndc'+id)
    var nalog =$('#nalog'+id)
    var oked =$('#oked'+id)
    var okpo =$('#okpo'+id)
    var coato =$('#coato'+id)
    var coogu =$('#coogu'+id)
    var kod_stran_bank =$('#kod_stran_bank'+id)
    var klyuch_banka =$('#klyuch_banka'+id)
    var bank_schot =$('#bank_schot'+id)
    var valyuta_zakaz =$('#valyuta_zakaz'+id)
    var usloviya_plateja =$('#usloviya_plateja'+id)
    var sbitovoy_organ =$('#sbitovoy_organ'+id)
    var kanal_sbita =$('#kanal_sbita'+id)
    var sektor =$('#sektor'+id)
    var rayon_sbita =$('#rayon_sbita'+id)
    var gruppa_sena =$('#gruppa_sena'+id)
    var sxema_kliyenta =$('#sxema_kliyenta'+id)
    var status_gruppa_kliyent =$('#status_gruppa_kliyent'+id)
    var usloviya_otgruz =$('#usloviya_otgruz'+id)
    var sbit_debitora =$('#sbit_debitora'+id)
    var sbit_nalog =$('#sbit_nalog'+id)
    var kontrol_schot =$('#kontrol_schot'+id)
    var kontrol_debitora =$('#kontrol_debitora'+id)
   



    balance_ed.css('display','block')
    rol_bp.css('display','block')
    group_del_partner.css('display','block')
    nomer_del_partner.css('display','block')
    imya_org.css('display','block')
    imya.css('display','block')
    familiya.css('display','block')
    ulitsa.css('display','block')
    nomer_doma.css('display','block')
    pochta_index.css('display','block')
    gorod.css('display','block')
    kod_stran.css('display','block')
    region.css('display','block')
    rayon.css('display','block')
    nomer_tel.css('display','block')
    nomer_mob.css('display','block')
    inn.css('display','block')
    ndc.css('display','block')
    nalog.css('display','block')
    oked.css('display','block')
    okpo.css('display','block')
    coogu.css('display','block')
    coato.css('display','block')
    kod_stran_bank.css('display','block')
    klyuch_banka.css('display','block')
    bank_schot.css('display','block')
    valyuta_zakaz.css('display','block')
    kontrol_schot.css('display','block')
    kontrol_debitora.css('display','block')

    balance_ed.css('border-color','#dedad9')
    rol_bp.css('border-color','#dedad9')
    group_del_partner.css('border-color','#dedad9')
    nomer_del_partner.css('border-color','#dedad9')
    imya_org.css('border-color','#dedad9')
    imya.css('border-color','#dedad9')
    familiya.css('border-color','#dedad9')
    ulitsa.css('border-color','#dedad9')
    nomer_doma.css('border-color','#dedad9')
    pochta_index.css('border-color','#dedad9')
    gorod.css('border-color','#dedad9')
    kod_stran.css('border-color','#dedad9')
    region.css('border-color','#dedad9')
    rayon.css('border-color','#dedad9')
    nomer_tel.css('border-color','#dedad9')
    nomer_mob.css('border-color','#dedad9')
    inn.css('border-color','#dedad9')
    ndc.css('border-color','#dedad9')
    nalog.css('border-color','#dedad9')
    oked.css('border-color','#dedad9')
    okpo.css('border-color','#dedad9')
    coogu.css('border-color','#dedad9')
    coato.css('border-color','#dedad9')
    kod_stran_bank.css('border-color','#dedad9')
    klyuch_banka.css('border-color','#dedad9')
    bank_schot.css('border-color','#dedad9')
    valyuta_zakaz.css('border-color','#dedad9')
    usloviya_plateja.css('border-color','#dedad9')
    sbitovoy_organ.css('border-color','#dedad9')
    kanal_sbita.css('border-color','#dedad9')
    sektor.css('border-color','#dedad9')
    rayon_sbita.css('border-color','#dedad9')
    gruppa_sena.css('border-color','#dedad9')
    sxema_kliyenta.css('border-color','#dedad9')
    status_gruppa_kliyent.css('border-color','#dedad9')
    usloviya_otgruz.css('border-color','#dedad9')
    sbit_debitora.css('border-color','#dedad9')
    sbit_nalog.css('border-color','#dedad9')
    kontrol_schot.css('border-color','#dedad9')
    kontrol_debitora.css('border-color','#dedad9')
   

    if(vid_zayavki =='Создание'){
        // console.log(vid_zayavki,'ddddd')
        if(balance_ed.val()!=''){
            balance_ed.css('border-color','#dedad9')
        }else{
            balance_ed.css('border-color','red')
        }
        if(rol_bp.val()!=''){
            rol_bp.css('border-color','#dedad9')
        }else{
            rol_bp.css('border-color','red')
        }
        if(group_del_partner.val()!=''){
            group_del_partner.css('border-color','#dedad9')
        }else{
            group_del_partner.css('border-color','red')
        }
        if(imya_org.val()!=''){
            imya_org.css('border-color','#dedad9')
        }else{
            imya_org.css('border-color','red')
        }
        if(gorod.val()!=''){
            gorod.css('border-color','#dedad9')
        }else{
            gorod.css('border-color','red')
        }
        if(kod_stran.val()!=''){
            kod_stran.css('border-color','#dedad9')
        }else{
            kod_stran.css('border-color','red')
        }
        if(inn.val()!=''){
            inn.css('border-color','#dedad9')
        }else{
            inn.css('border-color','#dedad9')
            // inn.css('border-color','red')
        }
        // if(kod_stran_bank.val()!=''){
        //     kod_stran_bank.css('border-color','#dedad9')
        // }else{
        //     kod_stran_bank.css('border-color','red')
        // }
        if(klyuch_banka.val()!=''){
            klyuch_banka.css('border-color','#dedad9')
        }else{
            klyuch_banka.css('border-color','red')
        }
        if(bank_schot.val()!=''){
            bank_schot.css('border-color','#dedad9')
        }else{
            bank_schot.css('border-color','red')
        }
        if(valyuta_zakaz.val()!=''){
            valyuta_zakaz.css('border-color','#dedad9')
        }else{
            valyuta_zakaz.css('border-color','red')
        }
        // console.log(rol_bp.val(),'rolllll')
        if(rol_bp.val() == 'Клиент' || rol_bp.val() == 'Поставщик и Клиент'){
           
            usloviya_plateja.css('border-color','red')
            sbitovoy_organ.css('border-color','red')
            kanal_sbita.css('border-color','red')
            sektor.css('border-color','red')
            rayon_sbita.css('border-color','red')
            gruppa_sena.css('border-color','red')
            sxema_kliyenta.css('border-color','red')
            status_gruppa_kliyent.css('border-color','red!important')
            usloviya_otgruz.css('border-color','red')
            sbit_debitora.css('border-color','red')
            sbit_nalog.css('border-color','red')
        }

        data_base[id] = new BasePokritiya()
        data_base[id].id =1
        data_base[id].vid_zayavki ='Создание'
    }
    if(vid_zayavki =='Изменения'){
        usloviya_plateja.css('display','block')
        sbitovoy_organ.css('display','block')
        kanal_sbita.css('display','block')
        sektor.css('display','block')
        rayon_sbita.css('display','block')
        gruppa_sena.css('display','block')
        sxema_kliyenta.css('display','block')
        status_gruppa_kliyent.css('display','block')
        usloviya_otgruz.css('display','block')
        sbit_debitora.css('display','block')
        sbit_nalog.css('display','block')

        if(balance_ed.val()!=''){
            balance_ed.css('border-color','#dedad9')
        }else{
            balance_ed.css('border-color','red')
        }
        if(nomer_del_partner.val()!=''){
            nomer_del_partner.css('border-color','#dedad9')
        }else{
            nomer_del_partner.css('border-color','red')
        }
        if(imya_org.val()!=''){
            imya_org.css('border-color','#dedad9')
        }else{
            imya_org.css('border-color','red')
        }


        data_base[id] = new BasePokritiya()
        data_base[id].id =2
        data_base[id].vid_zayavki ='Изменения'
    }
    if(vid_zayavki =='Расширение'){
        usloviya_plateja.css('display','block')
        sbitovoy_organ.css('display','block')
        kanal_sbita.css('display','block')
        sektor.css('display','block')
        rayon_sbita.css('display','block')
        gruppa_sena.css('display','block')
        sxema_kliyenta.css('display','block')
        status_gruppa_kliyent.css('display','block')
        usloviya_otgruz.css('display','block')
        sbit_debitora.css('display','block')
        sbit_nalog.css('display','block')
        if(balance_ed.val()!=''){
            balance_ed.css('border-color','#dedad9')
        }else{
            balance_ed.css('border-color','red')
        }
        if(rol_bp.val()!=''){
            rol_bp.css('border-color','#dedad9')
        }else{
            rol_bp.css('border-color','red')
        }
        if(group_del_partner.val()!=''){
            group_del_partner.css('border-color','#dedad9')
        }else{
            group_del_partner.css('border-color','red')
        }
        if(nomer_del_partner.val()!=''){
            nomer_del_partner.css('border-color','#dedad9')
        }else{
            nomer_del_partner.css('border-color','red')
        }
        if(imya_org.val()!=''){
            imya_org.css('border-color','#dedad9')
        }else{
            imya_org.css('border-color','red')
        }

        data_base[id] = new BasePokritiya()
        data_base[id].id =3
        data_base[id].vid_zayavki ='Расширение'
    }
    




}





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
        var balance_ed=data.balance_ed;
        var rol_bp=data.rol_bp;
        var group_del_partner=data.group_del_partner;
        var nomer_del_partner=data.nomer_del_partner;
        var imya_org=data.imya_org;
        var imya=data.imya;
        var familiya=data.familiya;
        var ulitsa=data.ulitsa;
        var nomer_doma=data.nomer_doma;
        var pochta_index=data.pochta_index;
        var gorod=data.gorod;
        var kod_stran=data.kod_stran;
        var region=data.region;
        var rayon=data.rayon;
        var nomer_tel=data.nomer_tel;
        var nomer_mob=data.nomer_mob;
        var inn=data.inn;
        var ndc=data.ndc;
        var nalog=data.nalog;
        var oked=data.oked;
        var okpo=data.okpo;
        var coato=data.coato;
        var coogu=data.coogu;
        var kod_stran_bank=data.kod_stran_bank;
        var klyuch_banka=data.klyuch_banka;
        var bank_schot=data.bank_schot;
        var valyuta_zakaz=data.valyuta_zakaz;
        var usloviya_plateja=data.usloviya_plateja;
        var sbitovoy_organ=data.sbitovoy_organ;
        var kanal_sbita=data.kanal_sbita;
        var sektor=data.sektor;
        var rayon_sbita=data.rayon_sbita;
        var gruppa_sena=data.gruppa_sena;
        var sxema_kliyenta=data.sxema_kliyenta;
        var status_gruppa_kliyent=data.status_gruppa_kliyent;
        var usloviya_otgruz=data.usloviya_otgruz;
        var sbit_debitora=data.sbit_debitora;
        var sbit_nalog=data.sbit_nalog;
        var kontrol_schot=data.kontrol_schot;
        var kontrol_debitora=data.kontrol_debitora;
         
        
        check_input_and_change(vid_zayavki,'#vid_zayavki'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(balance_ed,'#balance_ed'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(imya_org,'#imya_org'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(imya,'#imya'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(familiya,'#familiya'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(ulitsa,'#ulitsa'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(nomer_doma,'#nomer_doma'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(pochta_index,'#pochta_index'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(region,'#region'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(rayon,'#rayon'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(nomer_tel,'#nomer_tel'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(nomer_mob,'#nomer_mob'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(ndc,'#ndc'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(nalog,'#nalog'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(oked,'#oked'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(okpo,'#okpo'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(coato,'#coato'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(coogu,'#coogu'+s,dis=false,is_req=false,is_req_simple=true)

        
      
        
        check_input_and_change(kontrol_schot,'#kontrol_schot'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(kontrol_debitora,'#kontrol_debitora'+s,dis=false,is_req=false,is_req_simple=true)
       


        if(vid_zayavki =='Создание'){
            check_input_and_change(rol_bp,'#rol_bp'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(group_del_partner,'#group_del_partner'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(nomer_del_partner,'#nomer_del_partner'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(gorod,'#gorod'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(kod_stran,'#kod_stran'+s,dis=false,is_req=true,is_req_simple=false)
            if(this.group_del_partner=='B001 - Локальные Юридические Лица'){
                check_input_and_change(inn,'#inn'+s,dis=false,is_req=true,is_req_simple=false)
            }else{
                check_input_and_change(inn,'#inn'+s,dis=false,is_req=false,is_req_simple=true)
            }
            check_input_and_change(kod_stran_bank,'#kod_stran_bank'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(klyuch_banka,'#klyuch_banka'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(bank_schot,'#bank_schot'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(valyuta_zakaz,'#valyuta_zakaz'+s,dis=false,is_req=true,is_req_simple=false)
            
            if(rol_bp == 'Клиент' || rol_bp == 'Поставщик и Клиент'){
                check_input_and_change(usloviya_plateja,'#usloviya_plateja'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(sbitovoy_organ,'#sbitovoy_organ'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(kanal_sbita,'#kanal_sbita'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(sektor,'#sektor'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(rayon_sbita,'#rayon_sbita'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(gruppa_sena,'#gruppa_sena'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(sxema_kliyenta,'#sxema_kliyenta'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(status_gruppa_kliyent,'#status_gruppa_kliyent'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(usloviya_otgruz,'#usloviya_otgruz'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(sbit_debitora,'#sbit_debitora'+s,dis=false,is_req=true,is_req_simple=false)
                check_input_and_change(sbit_nalog,'#sbit_nalog'+s,dis=false,is_req=true,is_req_simple=false)
            }else{
                
                check_input_and_change(usloviya_plateja,'#usloviya_plateja'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(sbitovoy_organ,'#sbitovoy_organ'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(kanal_sbita,'#kanal_sbita'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(sektor,'#sektor'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(rayon_sbita,'#rayon_sbita'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(gruppa_sena,'#gruppa_sena'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(sxema_kliyenta,'#sxema_kliyenta'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(status_gruppa_kliyent,'#status_gruppa_kliyent'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(usloviya_otgruz,'#usloviya_otgruz'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(sbit_debitora,'#sbit_debitora'+s,dis=false,is_req=false,is_req_simple=true)
                check_input_and_change(sbit_nalog,'#sbit_nalog'+s,dis=false,is_req=false,is_req_simple=true)
            }
        
        }
        if(vid_zayavki =='Изменения'){
            check_input_and_change(rol_bp,'#rol_bp'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(group_del_partner,'#group_del_partner'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(nomer_del_partner,'#nomer_del_partner'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(gorod,'#gorod'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(kod_stran,'#kod_stran'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(inn,'#inn'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(kod_stran_bank,'#kod_stran_bank'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(klyuch_banka,'#klyuch_banka'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(bank_schot,'#bank_schot'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(valyuta_zakaz,'#valyuta_zakaz'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(usloviya_plateja,'#usloviya_plateja'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sbitovoy_organ,'#sbitovoy_organ'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(kanal_sbita,'#kanal_sbita'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sektor,'#sektor'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(rayon_sbita,'#rayon_sbita'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(gruppa_sena,'#gruppa_sena'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sxema_kliyenta,'#sxema_kliyenta'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(status_gruppa_kliyent,'#status_gruppa_kliyent'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(usloviya_otgruz,'#usloviya_otgruz'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sbit_debitora,'#sbit_debitora'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sbit_nalog,'#sbit_nalog'+s,dis=false,is_req=false,is_req_simple=true)
        
        
        }
        if(vid_zayavki =='Расширение'){
            check_input_and_change(rol_bp,'#rol_bp'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(group_del_partner,'#group_del_partner'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(nomer_del_partner,'#nomer_del_partner'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(gorod,'#gorod'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(kod_stran,'#kod_stran'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(inn,'#inn'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(kod_stran_bank,'#kod_stran_bank'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(klyuch_banka,'#klyuch_banka'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(bank_schot,'#bank_schot'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(valyuta_zakaz,'#valyuta_zakaz'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(usloviya_plateja,'#usloviya_plateja'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sbitovoy_organ,'#sbitovoy_organ'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(kanal_sbita,'#kanal_sbita'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sektor,'#sektor'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(rayon_sbita,'#rayon_sbita'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(gruppa_sena,'#gruppa_sena'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sxema_kliyenta,'#sxema_kliyenta'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(status_gruppa_kliyent,'#status_gruppa_kliyent'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(usloviya_otgruz,'#usloviya_otgruz'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sbit_debitora,'#sbit_debitora'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sbit_nalog,'#sbit_nalog'+s,dis=false,is_req=false,is_req_simple=true)
        }
        

        
        
        
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
    
    delete data_base[id]

    
    table_tr.css('background-color','white')
    

    var vid_zayavki = $('#vid_zayavki'+id)
    var balance_ed =$('#balance_ed'+id)
    var rol_bp =$('#rol_bp'+id)
    var group_del_partner =$('#group_del_partner'+id)
    var nomer_del_partner =$('#nomer_del_partner'+id)
    var imya_org =$('#imya_org'+id)
    var imya =$('#imya'+id)
    var familiya =$('#familiya'+id)
    var ulitsa =$('#ulitsa'+id)
    var nomer_doma =$('#nomer_doma'+id)
    var pochta_index =$('#pochta_index'+id)
    var gorod =$('#gorod'+id)
    var kod_stran =$('#kod_stran'+id)
    var region =$('#region'+id)
    var rayon =$('#rayon'+id)
    var nomer_tel =$('#nomer_tel'+id)
    var nomer_mob =$('#nomer_mob'+id)
    var inn =$('#inn'+id)
    var ndc =$('#ndc'+id)
    var nalog =$('#nalog'+id)
    var oked =$('#oked'+id)
    var okpo =$('#okpo'+id)
    var coato =$('#coato'+id)
    var coogu =$('#coogu'+id)
    var kod_stran_bank =$('#kod_stran_bank'+id)
    var klyuch_banka =$('#klyuch_banka'+id)
    var bank_schot =$('#bank_schot'+id)
    var valyuta_zakaz =$('#valyuta_zakaz'+id)
    var usloviya_plateja =$('#usloviya_plateja'+id)
    var sbitovoy_organ =$('#sbitovoy_organ'+id)
    var kanal_sbita =$('#kanal_sbita'+id)
    var sektor =$('#sektor'+id)
    var rayon_sbita =$('#rayon_sbita'+id)
    var gruppa_sena =$('#gruppa_sena'+id)
    var sxema_kliyenta =$('#sxema_kliyenta'+id)
    var status_gruppa_kliyent =$('#status_gruppa_kliyent'+id)
    var usloviya_otgruz =$('#usloviya_otgruz'+id)
    var sbit_debitora =$('#sbit_debitora'+id)
    var sbit_nalog =$('#sbit_nalog'+id)
    var kontrol_schot =$('#kontrol_schot'+id)
    var kontrol_debitora =$('#kontrol_debitora'+id)

    
    vid_zayavki.val('')
    balance_ed.val('')
    rol_bp.val('')
    group_del_partner.val('')
    nomer_del_partner.val('')
    imya_org.val('')
    imya.val('')
    familiya.val('')
    ulitsa.val('')
    nomer_doma.val('')
    pochta_index.val('')
    gorod.val('')
    kod_stran.val('')
    region.val('')
    rayon.val('')
    nomer_tel.val('')
    nomer_mob.val('')
    inn.val('')
    ndc.val('')
    nalog.val('')
    oked.val('')
    okpo.val('')
    coato.val('')
    coogu.val('')
    kod_stran_bank.val('')
    klyuch_banka.val('')
    bank_schot.val('')
    valyuta_zakaz.val('')
    usloviya_plateja.val('')
    sbitovoy_organ.val('')
    kanal_sbita.val('')
    sektor.val('')
    rayon_sbita.val('')
    gruppa_sena.val('')
    sxema_kliyenta.val('')
    status_gruppa_kliyent.val('')
    usloviya_otgruz.val('')
    sbit_debitora.val('')
    sbit_nalog.val('')
    kontrol_schot.val('')
    kontrol_debitora.val('')

    balance_ed.css('display','none')
    rol_bp.css('display','none')
    group_del_partner.css('display','none')
    nomer_del_partner.css('display','none')
    imya_org.css('display','none')
    imya.css('display','none')
    familiya.css('display','none')
    ulitsa.css('display','none')
    nomer_doma.css('display','none')
    pochta_index.css('display','none')
    gorod.css('display','none')
    kod_stran.css('display','none')
    region.css('display','none')
    rayon.css('display','none')
    nomer_tel.css('display','none')
    nomer_mob.css('display','none')
    inn.css('display','none')
    ndc.css('display','none')
    nalog.css('display','none')
    oked.css('display','none')
    okpo.css('display','none')
    coato.css('display','none')
    coogu.css('display','none')
    kod_stran_bank.css('display','none')
    klyuch_banka.css('display','none')
    bank_schot.css('display','none')
    valyuta_zakaz.css('display','none')
    usloviya_plateja.css('display','none')
    sbitovoy_organ.css('display','none')
    kanal_sbita.css('display','none')
    sektor.css('display','none')
    rayon_sbita.css('display','none')
    gruppa_sena.css('display','none')
    sxema_kliyenta.css('display','none')
    status_gruppa_kliyent.css('display','none')
    usloviya_otgruz.css('display','none')
    sbit_debitora.css('display','none')
    sbit_nalog.css('display','none')
    kontrol_schot.css('display','none')
    kontrol_debitora.css('display','none')


}


function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
        
        var vid_zayavki = $('#vid_zayavki'+id).val()
        var balance_ed =$('#balance_ed'+id)
        var rol_bp =$('#rol_bp'+id)
        var group_del_partner =$('#group_del_partner'+id)
        var nomer_del_partner =$('#nomer_del_partner'+id)
        var imya_org =$('#imya_org'+id)
        var imya =$('#imya'+id)
        var familiya =$('#familiya'+id)
        var ulitsa =$('#ulitsa'+id)
        var nomer_doma =$('#nomer_doma'+id)
        var pochta_index =$('#pochta_index'+id)
        var gorod =$('#gorod'+id)
        var kod_stran =$('#kod_stran'+id)
        var region =$('#region'+id)
        var rayon =$('#rayon'+id)
        var nomer_tel =$('#nomer_tel'+id)
        var nomer_mob =$('#nomer_mob'+id)
        var inn =$('#inn'+id)
        var ndc =$('#ndc'+id)
        var nalog =$('#nalog'+id)
        var oked =$('#oked'+id)
        var okpo =$('#okpo'+id)
        var coato =$('#coato'+id)
        var coogu =$('#coogu'+id)
        var kod_stran_bank =$('#kod_stran_bank'+id)
        var klyuch_banka =$('#klyuch_banka'+id)
        var bank_schot =$('#bank_schot'+id)
        var valyuta_zakaz =$('#valyuta_zakaz'+id)
        var usloviya_plateja =$('#usloviya_plateja'+id)
        var sbitovoy_organ =$('#sbitovoy_organ'+id)
        var kanal_sbita =$('#kanal_sbita'+id)
        var sektor =$('#sektor'+id)
        var rayon_sbita =$('#rayon_sbita'+id)
        var gruppa_sena =$('#gruppa_sena'+id)
        var sxema_kliyenta =$('#sxema_kliyenta'+id)
        var status_gruppa_kliyent =$('#status_gruppa_kliyent'+id)
        var usloviya_otgruz =$('#usloviya_otgruz'+id)
        var sbit_debitora =$('#sbit_debitora'+id)
        var sbit_nalog =$('#sbit_nalog'+id)
        var kontrol_schot =$('#kontrol_schot'+id)
        var kontrol_debitora =$('#kontrol_debitora'+id)
        
        if(balance_ed.val()!=''){
            data_base[id].balance_ed = balance_ed.val();
        }else{
            data_base[id].balance_ed = NaN;
        }
        if(rol_bp.val()!=''){
            data_base[id].rol_bp = rol_bp.val();
        }else{
            data_base[id].rol_bp = NaN;
        }
        if(group_del_partner.val()!=''){
            data_base[id].group_del_partner = group_del_partner.val();
        }else{
            data_base[id].group_del_partner = NaN;
        }
        if(nomer_del_partner.val()!=''){
            data_base[id].nomer_del_partner = nomer_del_partner.val();
        }else{
            data_base[id].nomer_del_partner = NaN;
        }
        if(imya_org.val()!=''){
            data_base[id].imya_org = imya_org.val();
        }else{
            data_base[id].imya_org = NaN;
        }
        if(imya.val()!=''){
            data_base[id].imya = imya.val();
        }else{
            data_base[id].imya = NaN;
        }
        if(familiya.val()!=''){
            data_base[id].familiya = familiya.val();
        }else{
            data_base[id].familiya = NaN;
        }
        if(ulitsa.val()!=''){
            data_base[id].ulitsa = ulitsa.val();
        }else{
            data_base[id].ulitsa = NaN;
        }
        if(nomer_doma.val()!=''){
            data_base[id].nomer_doma = nomer_doma.val();
        }else{
            data_base[id].nomer_doma = NaN;
        }
        if(pochta_index.val()!=''){
            data_base[id].pochta_index = pochta_index.val();
        }else{
            data_base[id].pochta_index = NaN;
        }
        if(gorod.val()!=''){
            data_base[id].gorod = gorod.val();
        }else{
            data_base[id].gorod = NaN;
        }
        if(kod_stran.val()!=''){
            data_base[id].kod_stran = kod_stran.val();
        }else{
            data_base[id].kod_stran = NaN;
        }
        if(region.val()!=''){
            data_base[id].region = region.val();
        }else{
            data_base[id].region = NaN;
        }
        if(rayon.val()!=''){
            data_base[id].rayon = rayon.val();
        }else{
            data_base[id].rayon = NaN;
        }
        if(nomer_tel.val()!=''){
            data_base[id].nomer_tel = nomer_tel.val();
        }else{
            data_base[id].nomer_tel = NaN;
        }
        if(nomer_mob.val()!=''){
            data_base[id].nomer_mob = nomer_mob.val();
        }else{
            data_base[id].nomer_mob = NaN;
        }
        if(inn.val()!=''){
            data_base[id].inn = inn.val();
        }else{
            data_base[id].inn = NaN;
        }
        if(ndc.val()!=''){
            data_base[id].ndc = ndc.val();
        }else{
            data_base[id].ndc = NaN;
        }
        if(nalog.val()!=''){
            data_base[id].nalog = nalog.val();
        }else{
            data_base[id].nalog = NaN;
        }
        if(oked.val()!=''){
            data_base[id].oked = oked.val();
        }else{
            data_base[id].oked = NaN;
        }
        if(okpo.val()!=''){
            data_base[id].okpo = okpo.val();
        }else{
            data_base[id].okpo = NaN;
        }
        if(coato.val()!=''){
            data_base[id].coato = coato.val();
        }else{
            data_base[id].coato = NaN;
        }
        if(coogu.val()!=''){
            data_base[id].coogu = coogu.val();
        }else{
            data_base[id].coogu = NaN;
        }
        if(kod_stran_bank.val()!=''){
            data_base[id].kod_stran_bank = kod_stran_bank.val();
        }else{
            data_base[id].kod_stran_bank = NaN;
        }
        if(klyuch_banka.val()!=''){
            data_base[id].klyuch_banka = klyuch_banka.val();
        }else{
            data_base[id].klyuch_banka = NaN;
        }
        if(bank_schot.val()!=''){
            data_base[id].bank_schot = bank_schot.val();
        }else{
            data_base[id].bank_schot = NaN;
        }
        if(valyuta_zakaz.val()!=''){
            data_base[id].valyuta_zakaz = valyuta_zakaz.val();
        }else{
            data_base[id].valyuta_zakaz = NaN;
        }
        if(usloviya_plateja.val()!=''){
            data_base[id].usloviya_plateja = usloviya_plateja.val();
        }else{
            data_base[id].usloviya_plateja = NaN;
        }
        if(sbitovoy_organ.val()!=''){
            data_base[id].sbitovoy_organ = sbitovoy_organ.val();
        }else{
            data_base[id].sbitovoy_organ = NaN;
        }
        if(kanal_sbita.val()!=''){
            data_base[id].kanal_sbita = kanal_sbita.val();
        }else{
            data_base[id].kanal_sbita = NaN;
        }
        if(sektor.val()!=''){
            data_base[id].sektor = sektor.val();
        }else{
            data_base[id].sektor = NaN;
        }
        if(rayon_sbita.val()!=''){
            data_base[id].rayon_sbita = rayon_sbita.val();
        }else{
            data_base[id].rayon_sbita = NaN;
        }
        if(gruppa_sena.val()!=''){
            data_base[id].gruppa_sena = gruppa_sena.val();
        }else{
            data_base[id].gruppa_sena = NaN;
        }
        if(sxema_kliyenta.val()!=''){
            data_base[id].sxema_kliyenta = sxema_kliyenta.val();
        }else{
            data_base[id].sxema_kliyenta = NaN;
        }
        if(status_gruppa_kliyent.val()!=''){
            data_base[id].status_gruppa_kliyent = status_gruppa_kliyent.val();
        }else{
            data_base[id].status_gruppa_kliyent = NaN;
        }
        if(usloviya_otgruz.val()!=''){
            data_base[id].usloviya_otgruz = usloviya_otgruz.val();
        }else{
            data_base[id].usloviya_otgruz = NaN;
        }
        if(sbit_debitora.val()!=''){
            data_base[id].sbit_debitora = sbit_debitora.val();
        }else{
            data_base[id].sbit_debitora = NaN;
        }
        if(sbit_nalog.val()!=''){
            data_base[id].sbit_nalog = sbit_nalog.val();
        }else{
            data_base[id].sbit_nalog = NaN;
        }
        if(kontrol_schot.val()!=''){
            data_base[id].kontrol_schot = kontrol_schot.val();
        }else{
            data_base[id].kontrol_schot = NaN;
        }
        if(kontrol_debitora.val()!=''){
            data_base[id].kontrol_debitora = kontrol_debitora.val();
        }else{
            data_base[id].kontrol_debitora = NaN;
        }
        
        
        

        console.log(vid_zayavki)
        console.log(status_gruppa_kliyent.val(),'kliyent&&&')

        if(vid_zayavki =='Создание'){
            if(balance_ed.val()!=''){
                balance_ed.css('border-color','#dedad9')
            }else{
                balance_ed.css('border-color','red')
            }
            if(rol_bp.val()!=''){
                rol_bp.css('border-color','#dedad9')
            }else{
                rol_bp.css('border-color','red')
            }
            if(group_del_partner.val()!=''){
                if(group_del_partner.val()=='B001 - Локальные Юридические Лица'){
                    if(inn.val()!=''){
                        inn.css('border-color','#dedad9')
                    }else{
                        inn.css('border-color','red')
                    }
                }else{
                    if(inn.val()!=''){
                        inn.css('border-color','#dedad9')
                    }else{
                        inn.css('border-color','#dedad9')
                    }
                }
                group_del_partner.css('border-color','#dedad9')
            }else{
                group_del_partner.css('border-color','red')
            }
            if(imya_org.val()!=''){
                imya_org.css('border-color','#dedad9')
            }else{
                imya_org.css('border-color','red')
            }
            if(gorod.val()!=''){
                gorod.css('border-color','#dedad9')
            }else{
                gorod.css('border-color','red')
            }
            if(kod_stran.val()!=''){
                kod_stran.css('border-color','#dedad9')
            }else{
                kod_stran.css('border-color','red')
            }
            
            if(kod_stran_bank.val()!=''){
                kod_stran_bank.css('border-color','#dedad9')
            }else{
                kod_stran_bank.css('border-color','#dedad9')
                // kod_stran_bank.css('border-color','red')
            }
            if(klyuch_banka.val()!=''){
                klyuch_banka.css('border-color','#dedad9')
            }else{
                klyuch_banka.css('border-color','red')
            }
            if(bank_schot.val()!=''){
                bank_schot.css('border-color','#dedad9')
            }else{
                bank_schot.css('border-color','red')
            }
            if(valyuta_zakaz.val()!=''){
                valyuta_zakaz.css('border-color','#dedad9')
            }else{
                valyuta_zakaz.css('border-color','red')
            }

            if(rol_bp.val() == 'Клиент' || rol_bp.val() == 'Поставщик и Клиент'){
                usloviya_plateja.css('display','block')
                sbitovoy_organ.css('display','block')
                kanal_sbita.css('display','block')
                sektor.css('display','block')
                rayon_sbita.css('display','block')
                gruppa_sena.css('display','block')
                sxema_kliyenta.css('display','block')
                status_gruppa_kliyent.css('display','block')
                usloviya_otgruz.css('display','block')
                sbit_debitora.css('display','block')
                sbit_nalog.css('display','block')
                if(sbit_nalog.val()!=''){
                    sbit_nalog.css('border-color','#dedad9')
                }else{
                    sbit_nalog.css('border-color','red')
                }
                if(sbit_debitora.val()!=''){
                    sbit_debitora.css('border-color','#dedad9')
                }else{
                    sbit_debitora.css('border-color','red')
                }
                if(usloviya_otgruz.val()!=''){
                    usloviya_otgruz.css('border-color','#dedad9')
                }else{
                    usloviya_otgruz.css('border-color','red')
                }
                if(status_gruppa_kliyent.val()!=''){
                    status_gruppa_kliyent.css('border-color','#dedad9')
                }else{
                    status_gruppa_kliyent.css('border-color','red')
                }
                if(sxema_kliyenta.val()!=''){
                    sxema_kliyenta.css('border-color','#dedad9')
                }else{
                    sxema_kliyenta.css('border-color','red')
                }
                if(gruppa_sena.val()!=''){
                    gruppa_sena.css('border-color','#dedad9')
                }else{
                    gruppa_sena.css('border-color','red')
                }
                if(rayon_sbita.val()!=''){
                    rayon_sbita.css('border-color','#dedad9')
                }else{
                    rayon_sbita.css('border-color','red')
                }
                if(sektor.val()!=''){
                    sektor.css('border-color','#dedad9')
                }else{
                    sektor.css('border-color','red')
                }
                if(usloviya_plateja.val()!=''){
                    usloviya_plateja.css('border-color','#dedad9')
                }else{
                    usloviya_plateja.css('border-color','red')
                }
                if(sbitovoy_organ.val()!=''){
                    sbitovoy_organ.css('border-color','#dedad9')
                }else{
                    sbitovoy_organ.css('border-color','red')
                }
                if(kanal_sbita.val()!=''){
                    kanal_sbita.css('border-color','#dedad9')
                }else{
                    kanal_sbita.css('border-color','red')
                }
            }else if(rol_bp.val() == 'Поставщик'){
                usloviya_plateja.css('display','block')
                sbitovoy_organ.css('display','block')
                kanal_sbita.css('display','block')
                sektor.css('display','block')
                rayon_sbita.css('display','block')
                gruppa_sena.css('display','block')
                sxema_kliyenta.css('display','block')
                status_gruppa_kliyent.css('display','block')
                usloviya_otgruz.css('display','block')
                sbit_debitora.css('display','block')
                sbit_nalog.css('display','block')
                
                sbit_nalog.css('border-color','#dedad9')
                sbit_debitora.css('border-color','#dedad9')
                usloviya_otgruz.css('border-color','#dedad9')
                status_gruppa_kliyent.css('border-color','#dedad9')
                sxema_kliyenta.css('border-color','#dedad9')
                gruppa_sena.css('border-color','#dedad9')
                rayon_sbita.css('border-color','#dedad9')
                sektor.css('border-color','#dedad9')
                usloviya_plateja.css('border-color','#dedad9')
                sbitovoy_organ.css('border-color','#dedad9')
                kanal_sbita.css('border-color','#dedad9')
                
                
            }

           
        }
        if(vid_zayavki =='Изменения'){
            
            if(balance_ed.val()!=''){
                balance_ed.css('border-color','#dedad9')
            }else{
                balance_ed.css('border-color','red')
            }
            if(nomer_del_partner.val()!=''){
                nomer_del_partner.css('border-color','#dedad9')
            }else{
                nomer_del_partner.css('border-color','red')
            }
            if(imya_org.val()!=''){
                imya_org.css('border-color','#dedad9')
            }else{
                imya_org.css('border-color','red')
            }
        }
        if(vid_zayavki =='Расширение'){
            
            if(balance_ed.val()!=''){
                balance_ed.css('border-color','#dedad9')
            }else{
                balance_ed.css('border-color','red')
            }
            if(rol_bp.val()!=''){
                rol_bp.css('border-color','#dedad9')
            }else{
                rol_bp.css('border-color','red')
            }
            if(group_del_partner.val()!=''){
                group_del_partner.css('border-color','#dedad9')
            }else{
                group_del_partner.css('border-color','red')
            }
            if(nomer_del_partner.val()!=''){
                nomer_del_partner.css('border-color','#dedad9')
            }else{
                nomer_del_partner.css('border-color','red')
            }
            if(imya_org.val()!=''){
                imya_org.css('border-color','#dedad9')
            }else{
                imya_org.css('border-color','red')
            }
            
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




