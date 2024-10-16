class BasePokritiya{
    constructor(
        id=NaN, //done

        vid_zayavki=NaN,//done
        zavod=NaN,//done
        sapcode=NaN,//done
        nazvaniye_tovarov=NaN,//done
        polnoye_nazvaniye=NaN,//done
        sena_materiala=NaN,//done
        bazoviy_edinitsa=NaN,//done
        koefitsiyent=NaN,//done
        alternativ_edin=NaN,//done
        vid_materiala=NaN,//done
        vid_zagotovki=NaN,//done
        prodayot=NaN,//done
        gruppa_zakupok=NaN,//done
        gruppa_materialov=NaN,//done
        comment=NaN,//done
        full=false//done
        ) {
      
        this.id = id;
        this.vid_zayavki=vid_zayavki;
        this.zavod=zavod;
        this.sapcode=sapcode;
        this.nazvaniye_tovarov=nazvaniye_tovarov;
        this.polnoye_nazvaniye=polnoye_nazvaniye;
        this.sena_materiala=sena_materiala;
        this.bazoviy_edinitsa=bazoviy_edinitsa;
        this.koefitsiyent=koefitsiyent;
        this.alternativ_edin=alternativ_edin;
        this.vid_materiala=vid_materiala;
        this.vid_zagotovki=vid_zagotovki;
        this.prodayot=prodayot;
        this.gruppa_zakupok=gruppa_zakupok;
        this.gruppa_materialov=gruppa_materialov;
        this.comment=comment 
        this.full = full; 
      

    }
    get_kratkiy_tekst(){

        switch(this.id){
            case 1: if(this.zavod && this.nazvaniye_tovarov && this.polnoye_nazvaniye && this.sena_materiala && this.bazoviy_edinitsa && this.vid_materiala && this.gruppa_zakupok){
                return {'text':'','accept':true}
            }else{
                return {'text':'','accept':false}
            } break;
            case 2: if(this.sapcode && this.nazvaniye_tovarov){
                return {'text':'','accept':true}
            }else{
                return {'text':'','accept':false}
            } break;
            case 3: if(this.zavod && this.sapcode && this.nazvaniye_tovarov && this.sena_materiala && this.bazoviy_edinitsa){
                return {'text':'','accept':true}
            }else{
                return {'text':'','accept':false}
            } break;
            }
            
        }
  }


data_base = {}

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
                <select class="form-select" aria-label="" style="width: 115px; font-size:12px; padding-right:0px;z-index:0" id='vid_zayavki`+ String(i)+`' onchange='select_vid_zayavki(`+String(i)+`,this.value)' required>
                    <option  selected></option>
                    <option value="Создание">Создание</div>
                    <option value="Изменение">Изменение</div>
                    <option value="Расширение">Расширение</div>
                </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="display:none;width: 60px; font-size:12px; padding-right:0px;z-index:0;border-color:red" id='zavod`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                    <option  selected></option>
                    <option value="1101 - Производство алюминиевых профилей - Джами">1101 - Производство алюминиевых профилей - Джами</option>
                    <option value="1201 - Производство алюминиевых профилей - BENKAM">1201 - Производство алюминиевых профилей - BENKAM</option>
                    <option value="1202 - Литейный цех и переработка втор.cырья">1202 - Литейный цех и переработка втор.cырья</option>
                    <option value="1203 - Производство ПВХ профилей - AKFA Plast">1203 - Производство ПВХ профилей - AKFA Plast</option>
                    <option value="1204 - Производство защитной наклейки">1204 - Производство защитной наклейки</option>
                    <option value="1205 - Производство полиэтиленовой пленки и стрейч">1205 - Производство полиэтиленовой пленки и стрейч</option>
                    <option value="1206 - Производство гранул ПВХ">1206 - Производство гранул ПВХ</option>
                    <option value="1207 - Производство металлических усилителей">1207 - Производство металлических усилителей</option>
                    <option value="1208 - Производство дистанционной рамки">1208 - Производство дистанционной рамки</option>
                    <option value="1209 - Производство резиновых уплотнителей">1209 - Производство резиновых уплотнителей</option>
                    <option value="1301 - Фабрика сборки оконно-дверных систем Имзо">1301 - Фабрика сборки оконно-дверных систем Имзо</option>
                    <option value="1311 - AKFA Projects">1311 - AKFA Projects</option>
                    <option value="5101 - AKFA Radiators">5101 - AKFA Radiators</option>
                    <option value="4501 - Сектор оконно-дверных аксессуаров">4501 - Сектор оконно-дверных аксессуаров</option>
                    <option value="4601 - Завод производства Композитных панелей из Алюминия">4601 - Завод производства Композитных панелей из Алюминия</option>
                    <option value="4701 - Завод EPDM резины">4701 - Завод EPDM резины</option>
                    
                </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="display:none; width: 100px; font-size:10px;z-index:0 " id='sapcode`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)' ></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="display:none; border-color:red; width: 175px; font-size:10px; z-index:0" id='nazvaniye_tovarov`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)' maxlength="40"></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="display:none; border-color:red; width: 175px; font-size:10px;z-index:0 " id='polnoye_nazvaniye`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='number' class=" form-control " style="display:none; border-color:red; width: 75px; font-size:10px; z-index:0" id='sena_materiala`+String(i)+`'  oninput="create_kratkiy_tekst(`+String(i)+`); limitLength(this, 15);"></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="display:none;border-color:red;height:27px;width: 55px; font-size:12px; padding-right:0px;z-index:0" id='bazoviy_edinitsa`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                    <option  selected></option>
                    <option value="ШТ">ШТ</div>
                    <option value="КГ">КГ</div>
                    <option value="М2">М2</div>
                    <option value="М">М</div>
                    <option value="Л">Л</div>
                    <option value="КМП">КМП</div>
                    <option value="ПАЧ">ПАЧ</div>
                    <option value="ПАРА">ПАРА</div>
                    <option value="СКЦ">СКЦ</div>
                    <option  value="КОР">КОР</div>
                    <option  value="КУБ">КУБ</div>
                    <option  value="Т">Т</div>
                </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="display:none;width: 75px; font-size:10px;z-index:0 " id='koefitsiyent`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="display:none;width: 75px; font-size:10px;z-index:0 " id='alternativ_edin`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="display:none;border-color:red;width: 500px; font-size:12px; padding-right:0px;z-index:0" id='vid_materiala`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                    <option  selected></option>
                    <option value="Сырье и материалы - Сырье и материалы">Сырье и материалы - Сырье и материалы</option>
                    <option value="Вспомогательные материалы - Вспомогательное сырье и материалы">Вспомогательные материалы - Вспомогательное сырье и материалы</option>
                    <option value="ГСМ (масла) - Бензин">ГСМ (масла) - Бензин</option>
                    <option value="ГСМ (масла) - Дизельное топливо">ГСМ (масла) - Дизельное топливо</option>
                    <option value="ГСМ (масла) - Сжатый природный газ">ГСМ (масла) - Сжатый природный газ</option>
                    <option value="Запасные части - Запасные части">Запасные части - Запасные части</option>
                    <option value="Тара и тарные материалы - Тара и тарные материалы">Тара и тарные материалы - Тара и тарные материалы</option>
                    <option value="Строительные материалы - Строительные материалы">Строительные материалы - Строительные материалы</option>
                    <option value="Инвентарь, ИХП, спецодежда и СИЗ - Инвентарь, ИХП, СИЗ и спецодежда">Инвентарь, ИХП, спецодежда и СИЗ - Инвентарь, ИХП, СИЗ и спецодежда</option>
                    <option value="Прочие материалы, товары - Сменные материалы">Прочие материалы, товары - Сменные материалы</option>
                    <option value="Прочие материалы, товары - Электрические приборы">Прочие материалы, товары - Электрические приборы</option>
                    <option value="Прочие материалы, товары - Сантехнические приборы">Прочие материалы, товары - Сантехнические приборы</option>
                    <option value="Прочие материалы, товары - Продукты для буфетного обслуживания">Прочие материалы, товары - Продукты для буфетного обслуживания</option>
                    <option value="Прочие материалы, товары - Продукты для столовой">Прочие материалы, товары - Продукты для столовой</option>
                    <option value="Прочие материалы, товары - Медикаменты для медпункта">Прочие материалы, товары - Медикаменты для медпункта</option>
                    <option value="Прочие материалы, товары - Другие материалы">Прочие материалы, товары - Другие материалы</option>
                    <option value="Прочие материалы, товары - Товары">Прочие материалы, товары - Товары</option>
                    <option value="Прочие материалы, товары - Тех.отход">Прочие материалы, товары - Тех.отход</option>
                    <option value="Полуфабрикат покупные (3-стороны) - Покупные полуфабр.и комплект.изделия,констр.детали">Полуфабрикат покупные (3-стороны) - Покупные полуфабр.и комплект.изделия,констр.детали</option>
                    <option value="Производимые/покупные внутри группы AKFA - Покупные полуфабр.и комплект.изделия,констр.детали">Производимые/покупные внутри группы AKFA - Покупные полуфабр.и комплект.изделия,констр.детали</option>
                    <option value="Производимые/покупные внутри группы AKFA - Полуфабрикаты (производимые)">Производимые/покупные внутри группы AKFA - Полуфабрикаты (производимые)</option>
                    <option value="Производимые/покупные внутри группы AKFA - Готовая продукция">Производимые/покупные внутри группы AKFA - Готовая продукция</option>
                    <option value="Производимые/покупные внутри группы AKFA - Сырье и материалы">Производимые/покупные внутри группы AKFA - Сырье и материалы</option>
                    <option value="Производимые/покупные внутри группы AKFA - Товары">Производимые/покупные внутри группы AKFA - Товары</option>
                    <option value="Профили - Готовая продукция">Профили - Готовая продукция</option>
                    <option value="Профили - Сырье и материалы">Профили - Сырье и материалы</option>
                    <option value="Профили - Полуфабрикаты (производимые)">Профили - Полуфабрикаты (производимые)</option>
                    <option value="Профили - Брак">Профили - Брак</option>
                    <option value="ОС на складе (оборуд, техника) - Основное средство без НЗС">ОС на складе (оборуд, техника) - Основное средство без НЗС</option>
                    <option value="ОС на складе (оборуд, техника) - Основное средство под НЗС">ОС на складе (оборуд, техника) - Основное средство под НЗС</option>
                    <option value="Нескладируемый материал (Все виды НМА) - НМА">Нескладируемый материал (Все виды НМА) - НМА</option>


                </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="display:none;width: 120px; font-size:12px; padding-right:0px;z-index:0;border-color:red;" id='vid_zagotovki`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                    <option  selected></option>
                    <option value="Закупается">Закупается</option>
                    <option value="Производится">Производится</option>
                </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="display:none;width: 30px; font-size:12px; padding-right:0px;z-index:0;border-color:red;" id='prodayot`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)'  required>
                    <option  selected value='0' disabled>...</option>
                    <option value="X">X</option>
                    <option value=""></option>
                </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="display:none;width: 200px; font-size:12px; padding-right:0px;z-index:0" id='gruppa_zakupok`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                    <option  selected></option>
                    <option value="100 - Импорт/Сырьё/Усл.">100 - Импорт/Сырьё/Усл.</option>
                    <option value="101 - Импорт/Оборудов/ЗЧ">101 - Импорт/Оборудов/ЗЧ</option>
                    <option value="120 - Местный/ТМЦ/Усл.">120 - Местный/ТМЦ/Усл.</option>
                    <option value="540 - Akfa Project">540 - Akfa Project</option>
                </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="display:none;width: 100px; font-size:10px;z-index:0 " id='gruppa_materialov`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type='text' class=" form-control " style="display:none;width: 250px; font-size:10px; height:27px!important;z-index:0"  id='comment`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)' placeholder='Складини тулдиринг'></input>
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

        var data_id = data.id;
        var vid_zayavki = data.vid_zayavki;
        var zavod = data.zavod;
        var sapcode = data.sapcode;
        var nazvaniye_tovarov = data.nazvaniye_tovarov;
        var polnoye_nazvaniye = data.polnoye_nazvaniye;
        var sena_materiala = data.sena_materiala;
        var bazoviy_edinitsa = data.bazoviy_edinitsa;
        var koefitsiyent = data.koefitsiyent;
        var alternativ_edin = data.alternativ_edin;
        var vid_materiala = data.vid_materiala;
        var vid_zagotovki = data.vid_zagotovki;
        var prodayot = data.prodayot;
        var gruppa_zakupok = data.gruppa_zakupok;
        var gruppa_materialov = data.gruppa_materialov;
        var comment = data.comment;
        

        // console.log(sena_materiala,'senaaa materiala')
        check_input_and_change(vid_zayavki,'#vid_zayavki'+s,dis=false,is_req=false,is_req_simple=true)
        // console.log('sss',prodayot,'mmm')
        if(data_id == 1){
            check_input_and_change(zavod,'#zavod'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(sapcode,'#sapcode'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(nazvaniye_tovarov,'#nazvaniye_tovarov'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(polnoye_nazvaniye,'#polnoye_nazvaniye'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(sena_materiala,'#sena_materiala'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(bazoviy_edinitsa,'#bazoviy_edinitsa'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(koefitsiyent,'#koefitsiyent'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(alternativ_edin,'#alternativ_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(vid_materiala,'#vid_materiala'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(vid_zagotovki,'#vid_zagotovki'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(prodayot,'#prodayot'+s,dis=false,is_req=false,is_req_simple=true)
            if(prodayot ==' '){
                $('#prodayot'+s).val('')
            }
            check_input_and_change(gruppa_zakupok,'#gruppa_zakupok'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(gruppa_materialov,'#gruppa_materialov'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(comment,'#comment'+s,dis=false,is_req=false,is_req_simple=true)
        }else if(data_id == 2){
            check_input_and_change(zavod,'#zavod'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sapcode,'#sapcode'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(nazvaniye_tovarov,'#nazvaniye_tovarov'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(polnoye_nazvaniye,'#polnoye_nazvaniye'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sena_materiala,'#sena_materiala'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(bazoviy_edinitsa,'#bazoviy_edinitsa'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(koefitsiyent,'#koefitsiyent'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(alternativ_edin,'#alternativ_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(vid_materiala,'#vid_materiala'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(vid_zagotovki,'#vid_zagotovki'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(prodayot,'#prodayot'+s,dis=false,is_req=false,is_req_simple=true)
            if(prodayot ==' '){
                $('#prodayot'+s).val('')
            }
            check_input_and_change(gruppa_zakupok,'#gruppa_zakupok'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(gruppa_materialov,'#gruppa_materialov'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(comment,'#comment'+s,dis=false,is_req=false,is_req_simple=true)
        }else if(data_id == 3){
            check_input_and_change(zavod,'#zavod'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(sapcode,'#sapcode'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(nazvaniye_tovarov,'#nazvaniye_tovarov'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(polnoye_nazvaniye,'#polnoye_nazvaniye'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(sena_materiala,'#sena_materiala'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(bazoviy_edinitsa,'#bazoviy_edinitsa'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(koefitsiyent,'#koefitsiyent'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(alternativ_edin,'#alternativ_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(vid_materiala,'#vid_materiala'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(vid_zagotovki,'#vid_zagotovki'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(prodayot,'#prodayot'+s,dis=false,is_req=false,is_req_simple=true)
            if(prodayot ==' '){
                $('#prodayot'+s).val('')
            }
            check_input_and_change(gruppa_zakupok,'#gruppa_zakupok'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(gruppa_materialov,'#gruppa_materialov'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(comment,'#comment'+s,dis=false,is_req=false,is_req_simple=true)

        }
        
        
        
        
    }


}

function removeQuotesFromStartAndEnd(str) {
    // Remove double quotes from the beginning and end of the string
    return str.replace(/^"+|"+$/g, '');
}

function select_vid_zayavki(id,val){

    var element33 = document.getElementById("table_tr"+id);
    element33.style.backgroundColor='white';

    var vid_zayavki =$('#vid_zayavki'+id);
    var zavod =$('#zavod'+id);
    var sapcode =$('#sapcode'+id);
    var nazvaniye_tovarov =$('#nazvaniye_tovarov'+id);
    var polnoye_nazvaniye =$('#polnoye_nazvaniye'+id);
    var sena_materiala =$('#sena_materiala'+id);
    var bazoviy_edinitsa =$('#bazoviy_edinitsa'+id);
    var koefitsiyent =$('#koefitsiyent'+id);
    var alternativ_edin =$('#alternativ_edin'+id);
    var vid_materiala =$('#vid_materiala'+id);
    var vid_zagotovki =$('#vid_zagotovki'+id);
    var prodayot =$('#prodayot'+id);
    var gruppa_zakupok =$('#gruppa_zakupok'+id);
    var gruppa_materialov =$('#gruppa_materialov'+id);
    var comment =$('#comment'+id);

    zavod.val('')
    sapcode.val('')
    nazvaniye_tovarov.val('')
    polnoye_nazvaniye.val('')
    sena_materiala.val('')
    bazoviy_edinitsa.val('')
    koefitsiyent.val('')
    alternativ_edin.val('')
    vid_materiala.val('')
    vid_zagotovki.val('')
    prodayot.val('')
    gruppa_zakupok.val('')
    gruppa_materialov.val('')
    comment.val('')


    // vid_zayavki.css('display','none')
    zavod.css('display','none')
    sapcode.css('display','none')
    nazvaniye_tovarov.css('display','none')
    polnoye_nazvaniye.css('display','none')
    sena_materiala.css('display','none')
    bazoviy_edinitsa.css('display','none')
    koefitsiyent.css('display','none')
    alternativ_edin.css('display','none')
    vid_materiala.css('display','none')
    vid_zagotovki.css('display','none')
    prodayot.css('display','none')
    gruppa_zakupok.css('display','none')
    gruppa_materialov.css('display','none')
    comment.css('display','none')

    vid_zayavki.css('border-color','#dedad9')
    zavod.css('border-color','#dedad9')
    sapcode.css('border-color','#dedad9')
    nazvaniye_tovarov.css('border-color','#dedad9')
    polnoye_nazvaniye.css('border-color','#dedad9')
    sena_materiala.css('border-color','#dedad9')
    bazoviy_edinitsa.css('border-color','#dedad9')
    koefitsiyent.css('border-color','#dedad9')
    alternativ_edin.css('border-color','#dedad9')
    vid_materiala.css('border-color','#dedad9')
    vid_zagotovki.css('border-color','#dedad9')
    prodayot.css('border-color','#dedad9')
    gruppa_zakupok.css('border-color','#dedad9')
    gruppa_materialov.css('border-color','#dedad9')
    comment.css('border-color','#dedad9')

    if(val!=''){
        vid_zayavki.css('display','block')
        zavod.css('display','block')
        sapcode.css('display','block')
        nazvaniye_tovarov.css('display','block')
        polnoye_nazvaniye.css('display','block')
        sena_materiala.css('display','block')
        bazoviy_edinitsa.css('display','block')
        koefitsiyent.css('display','block')
        alternativ_edin.css('display','block')
        vid_materiala.css('display','block')
        vid_zagotovki.css('display','block')
        prodayot.css('display','block')
        gruppa_zakupok.css('display','block')
        gruppa_materialov.css('display','block')
        comment.css('display','block')
    }

    if(val =='Создание'){
        data_base[id] = new BasePokritiya()
        data_base[id].id = 1
        data_base[id].vid_zayavki = 'Создание'
        zavod.css('border-color','red')
        nazvaniye_tovarov.css('border-color','red')
        polnoye_nazvaniye.css('border-color','red')
        sena_materiala.css('border-color','red')
        bazoviy_edinitsa.css('border-color','red')
        vid_materiala.css('border-color','red')
        // prodayot.css('border-color','red')
        gruppa_zakupok.css('border-color','red')
        vid_zagotovki.val('Закупается')
        prodayot.val('')
    }else if(val =='Изменение'){
        data_base[id] = new BasePokritiya()
        data_base[id].id = 2
        data_base[id].vid_zayavki = 'Изменение'
        sapcode.css('border-color','red')
        nazvaniye_tovarov.css('border-color','red')
        
    }else if(val =='Расширение'){
        data_base[id] = new BasePokritiya()
        data_base[id].id = 3
        data_base[id].vid_zayavki = 'Расширение'

        zavod.css('border-color','red')
        sapcode.css('border-color','red')
        nazvaniye_tovarov.css('border-color','red')
        sena_materiala.css('border-color','red')
        bazoviy_edinitsa.css('border-color','red')

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

    
    var vid_zayavki =$('#vid_zayavki'+id);
    var zavod =$('#zavod'+id);
    var sapcode =$('#sapcode'+id);
    var nazvaniye_tovarov =$('#nazvaniye_tovarov'+id);
    var polnoye_nazvaniye =$('#polnoye_nazvaniye'+id);
    var sena_materiala =$('#sena_materiala'+id);
    var bazoviy_edinitsa =$('#bazoviy_edinitsa'+id);
    var koefitsiyent =$('#koefitsiyent'+id);
    var alternativ_edin =$('#alternativ_edin'+id);
    var vid_materiala =$('#vid_materiala'+id);
    var vid_zagotovki =$('#vid_zagotovki'+id);
    var prodayot =$('#prodayot'+id);
    var gruppa_zakupok =$('#gruppa_zakupok'+id);
    var gruppa_materialov =$('#gruppa_materialov'+id);
    var comment =$('#comment'+id);

    vid_zayavki.val('')
    zavod.val('')
    sapcode.val('')
    nazvaniye_tovarov.val('')
    polnoye_nazvaniye.val('')
    sena_materiala.val('')
    bazoviy_edinitsa.val('')
    koefitsiyent.val('')
    alternativ_edin.val('')
    vid_materiala.val('')
    vid_zagotovki.val('')
    prodayot.val('')
    gruppa_zakupok.val('')
    gruppa_materialov.val('')
    comment.val('')


    zavod.css('display','none')
    sapcode.css('display','none')
    nazvaniye_tovarov.css('display','none')
    polnoye_nazvaniye.css('display','none')
    sena_materiala.css('display','none')
    bazoviy_edinitsa.css('display','none')
    koefitsiyent.css('display','none')
    alternativ_edin.css('display','none')
    vid_materiala.css('display','none')
    vid_zagotovki.css('display','none')
    prodayot.css('display','none')
    gruppa_zakupok.css('display','none')
    gruppa_materialov.css('display','none')
    comment.css('display','none')
   
    

}

function  get_and_set_data(id,selector,is_req){
    var data = $('#'+selector+id)
    if(data.val() != '' && data.val() !=NaN && data.val() !=null){
        data_base[id][selector] = removeQuotesFromStartAndEnd(data.val())
        data.css('border-color','#dedad9')
    }else{
        if(is_req){
            data.css('border-color','red')
        }else{
            data.css('border-color','#dedad9')
        }
        data_base[id][selector] = NaN;
    }
}



function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
    
    var vid_zayavki =$('#vid_zayavki'+id);
    var prodayot =$('#prodayot'+id);
    if(prodayot.val()=='' || prodayot.val()=='X'){
        // console.log('dddd11',prodayot.val(),'lllll')
        prodayot.css('border-color','#dedad9')
        if(prodayot.val()==''){
            data_base[id].prodayot = ' ';
        }else{
            data_base[id].prodayot = prodayot.val();
        }
    }else{
        // console.log('dddd2222',prodayot.val(),'lllll')
        prodayot.css('border-color','#dedad9')
        data_base[id].prodayot =NaN;
    }
    
    if(vid_zayavki.val()=='Создание'){
        get_and_set_data(id,'zavod',is_req=true)
        get_and_set_data(id,'sapcode',is_req=false)
        get_and_set_data(id,'nazvaniye_tovarov',is_req=true)
        get_and_set_data(id,'polnoye_nazvaniye',is_req=true)
        // get_and_set_data(id,'sena_materiala',is_req=true)
        var sena_materiala =$('#sena_materiala'+String(id))
        if(sena_materiala.val()!='' && sena_materiala.val()!=0 && sena_materiala.val()!='0'){
            sena_materiala.css("border-color",'#dedad9');
            data_base[id].sena_materiala = sena_materiala.val()
        }else{
            sena_materiala.css("border-color",'red');
            data_base[id].sena_materiala = NaN;
        }

        get_and_set_data(id,'bazoviy_edinitsa',is_req=true)
        get_and_set_data(id,'koefitsiyent',is_req=false)
        get_and_set_data(id,'alternativ_edin',is_req=false)
        get_and_set_data(id,'vid_materiala',is_req=true)
        get_and_set_data(id,'vid_zagotovki',is_req=false)

        

        get_and_set_data(id,'gruppa_zakupok',is_req=true)
        get_and_set_data(id,'gruppa_materialov',is_req=false)
        get_and_set_data(id,'comment',is_req=false)

    }else if(vid_zayavki.val()=='Изменение'){
        get_and_set_data(id,'zavod',is_req=false)
        get_and_set_data(id,'sapcode',is_req=true)
        get_and_set_data(id,'nazvaniye_tovarov',is_req=true)
        get_and_set_data(id,'polnoye_nazvaniye',is_req=false)
        // get_and_set_data(id,'sena_materiala',is_req=false)
        var sena_materiala =$('#sena_materiala'+String(id))
        if(sena_materiala.val()!='' && sena_materiala.val()!=0 && sena_materiala.val()!='0'){
            sena_materiala.css("border-color",'#dedad9');
            data_base[id].sena_materiala = sena_materiala.val()
        }else{
            sena_materiala.css("border-color",'#dedad9');
            data_base[id].sena_materiala = NaN;
        }
        get_and_set_data(id,'bazoviy_edinitsa',is_req=false)
        get_and_set_data(id,'koefitsiyent',is_req=false)
        get_and_set_data(id,'alternativ_edin',is_req=false)
        get_and_set_data(id,'vid_materiala',is_req=false)
        get_and_set_data(id,'vid_zagotovki',is_req=false)

        

        get_and_set_data(id,'gruppa_zakupok',is_req=false)
        get_and_set_data(id,'gruppa_materialov',is_req=false)
        get_and_set_data(id,'comment',is_req=false)

    }else if(vid_zayavki.val()=='Расширение'){
        get_and_set_data(id,'zavod',is_req=true)
        get_and_set_data(id,'sapcode',is_req=true)
        get_and_set_data(id,'nazvaniye_tovarov',is_req=true)
        get_and_set_data(id,'polnoye_nazvaniye',is_req=false)
        // get_and_set_data(id,'sena_materiala',is_req=true)
        var sena_materiala =$('#sena_materiala'+String(id))
        if(sena_materiala.val()!='' && sena_materiala.val()!=0 && sena_materiala.val()!='0'){
            sena_materiala.css("border-color",'#dedad9');
            data_base[id].sena_materiala = sena_materiala.val()
        }else{
            sena_materiala.css("border-color",'red');
            data_base[id].sena_materiala = NaN;
        }
        get_and_set_data(id,'bazoviy_edinitsa',is_req=true)
        get_and_set_data(id,'koefitsiyent',is_req=false)
        get_and_set_data(id,'alternativ_edin',is_req=false)
        get_and_set_data(id,'vid_materiala',is_req=false)
        get_and_set_data(id,'vid_zagotovki',is_req=false)

        // get_and_set_data(id,'prodayot',is_req=false)
        

        get_and_set_data(id,'gruppa_zakupok',is_req=false)
        get_and_set_data(id,'gruppa_materialov',is_req=false)
        get_and_set_data(id,'comment',is_req=false)

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






