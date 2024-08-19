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
                if (this.zavod && this.nazvaniye_tovarov && this.polnoye_nazvaniye && this.sena_materiala && this.bazoviy_edinitsa && this.vid_materiala && this.vid_zagotovki && this.prodayot){
                    return {'text':'','accept':true}
                }else{
                    return {'text':'','accept':false}
                }
        }
  }


data_base = {}

function front_piece(start=1,end=6){
    text =""

    for (let i = start; i < end; i++) {
        data_base[i] = new BasePokritiya()
        text +=`
        <tr id='table_tr` +String(i)+`' style='padding-bottom:0!important;margin-bottom:0!important;'>                   
        <td class="sticky-col"   style='left:0; padding-right:5px; background-color:white!important;' >
                    <div class="btn-group" role="group" aria-label="Basic example">
                            <button type="button" class="btn btn-outline-secondary btn-sm" id='clear_btn`+String(i)+`' onclick="artukil_clear(`+String(i)+`)" data-bs-toggle='popover' title='Yangi sozdaniya qilish uchun ishlatiladi'><i class="bi bi-x-circle"></i></button>
                            <button type="button" class="btn btn-outline-secondary btn-sm"  onclick="copy_tr(`+String(i)+`)" data-bs-toggle='popover' title='Yangi sozdaniya qilish uchun ishlatiladi'><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-copy" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M4 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 5a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-1h1v1a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h1v1z"/></svg></button>
                    </div>
                    
                    

        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 115px;text-transform: uppercase; font-size:12px; padding-right:0px;z-index:0" id='vid_zayavki`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                    <option  selected></option>
                    <option vlaue="Создание">Создание</div>
                    <option vlaue="Изменение">Изменение</div>
                    <option vlaue="Расширение">Расширение</div>
                </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 450px;text-transform: uppercase; font-size:12px; padding-right:0px;z-index:0;border-color:red" id='zavod`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
                    <option value="1305 - AKFA Projects">1305 - AKFA Projects</option>
                    <option value="5101 - AKFA Radiators">5101 - AKFA Radiators</option>
                    <option value="4501 - Сектор оконно-дверных аксессуаров">4501 - Сектор оконно-дверных аксессуаров</option>
                    <option value="4601 - Завод производства Композитных панелей из Алюминия">4601 - Завод производства Композитных панелей из Алюминия</option>
                    <option value="9001 - RADIATOR ">9001 - RADIATOR </option>
                    <option value="9002 - Акссеуар Technology">9002 - Акссеуар Technology</option>
                    <option value="9003 - Дорожная краска">9003 - Дорожная краска</option>
                    <option value="9004 - ПОРОШКОВАЯ КРАСКА">9004 - ПОРОШКОВАЯ КРАСКА</option>
                    <option value="9004 - Матрица">9004 - Матрица</option>
                    <option value="9005 - EPDM_WTS">9005 - EPDM_WTS</option>
                </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 100px; font-size:10px;z-index:0 " id='sapcode`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 175px; font-size:10px; z-index:0" id='nazvaniye_tovarov`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 175px; font-size:10px;z-index:0 " id='polnoye_nazvaniye`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px; z-index:0" id='sena_materiala`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="border-color:red;height:27px;width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;z-index:0" id='bazoviy_edinitsa`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                    <option  selected></option>
                    <option vlaue="Штука">Штука</div>
                    <option vlaue="Килограмм">Килограмм</div>
                    <option vlaue="Квадратный метр">Квадратный метр</div>
                    <option vlaue="Метр">Метр</div>
                    <option vlaue="КМП">КМП</div>
                    <option vlaue="Пачка">Пачка</div>
                    <option vlaue="Секция">Секция</div>
                    <option  value="Коробка">Коробка</div>
                    <option  value="Грам">Грам</div>
                </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 75px; font-size:10px;z-index:0 " id='koefitsiyent`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 75px; font-size:10px;z-index:0 " id='alternativ_edin`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="border-color:red;width: 500px;text-transform: uppercase; font-size:12px; padding-right:0px;z-index:0" id='vid_materiala`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
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
                <select class="form-select" aria-label="" style="width: 120px;text-transform: uppercase; font-size:12px; padding-right:0px;z-index:0;border-color:red;" id='vid_zagotovki`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                    <option  selected></option>
                    <option value="Закупается">Закупается</option>
                    <option value="Производится">Производится</option>
                </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 30px;text-transform: uppercase; font-size:12px; padding-right:0px;z-index:0;border-color:red;" id='prodayot`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                    <option  selected value=''></option>
                    <option value="X">X</option>
                </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 200px;text-transform: uppercase; font-size:12px; padding-right:0px;z-index:0" id='gruppa_zakupok`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                    <option  selected></option>
                    <option value="100 - Импорт/Сырьё/Усл.">100 - Импорт/Сырьё/Усл.</option>
                    <option value="101 - Импорт/Оборудов/ЗЧ">101 - Импорт/Оборудов/ЗЧ</option>
                    <option value="120 - Местный/ТМЦ/Усл.">120 - Местный/ТМЦ/Усл.</option>
                </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 100px; font-size:10px;z-index:0 " id='gruppa_materialov`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type='text' class=" form-control " style="width: 250px; font-size:10px; height:27px!important;z-index:0"  id='comment`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
            
        </td>
        
        </tr>`
    }
    return text
}

text = front_piece()

var table = $('#table-artikul')

table.append(text)

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
        
        
        var data = new BasePokritiya()
        for(key in data_base[id]){
            data[key] = data_base[id][key]
        }
            
        
        data_base[size+1] = data
        
        var s = size+1

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
        
      
        
        check_input_and_change(vid_zayavki,'#vid_zayavki'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(zavod,'#zavod'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(sapcode,'#sapcode'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(nazvaniye_tovarov,'#nazvaniye_tovarov'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(polnoye_nazvaniye,'#polnoye_nazvaniye'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(sena_materiala,'#sena_materiala'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(bazoviy_edinitsa,'#bazoviy_edinitsa'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(koefitsiyent,'#koefitsiyent'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(alternativ_edin,'#alternativ_edin'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(vid_materiala,'#vid_materiala'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(vid_zagotovki,'#vid_zagotovki'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(prodayot,'#prodayot'+s,dis=false,is_req=true,is_req_simple=false)
        check_input_and_change(gruppa_zakupok,'#gruppa_zakupok'+s,dis=false,is_req=false,is_req_simple=true)
        check_input_and_change(gruppa_materialov,'#gruppa_materialov'+s,dis=false,is_req=false,is_req_simple=true)
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
    
    for(key in data_base[id]){
        data_base[id][key] = NaN
    }

    
    table_tr.css('background-color','white')

  
    var vid_zayavki =$('#vid_zayavki'+id);
    vid_zayavki.val('')
    var zavod =$('#zavod'+id);
    zavod.val('')


    var sapcode =$('#sapcode'+id);
    sapcode.val('')


    var nazvaniye_tovarov =$('#nazvaniye_tovarov'+id);
    nazvaniye_tovarov.val('')

    var polnoye_nazvaniye =$('#polnoye_nazvaniye'+id);
    polnoye_nazvaniye.val('')
    polnoye_nazvaniye.css('border-color','red')
    var sena_materiala =$('#sena_materiala'+id);
    sena_materiala.val('')
    sena_materiala.css('border-color','red')
    var bazoviy_edinitsa =$('#bazoviy_edinitsa'+id);
    bazoviy_edinitsa.val('')
    bazoviy_edinitsa.css('border-color','red')
    
    var koefitsiyent =$('#koefitsiyent'+id);
    koefitsiyent.val('')
    var alternativ_edin =$('#alternativ_edin'+id);
    alternativ_edin.val('')
    var vid_materiala =$('#vid_materiala'+id);
    vid_materiala.val('')
    var vid_zagotovki =$('#vid_zagotovki'+id);
    vid_zagotovki.val('')
    var prodayot =$('#prodayot'+id);
    prodayot.val('')


    var gruppa_zakupok =$('#gruppa_zakupok'+id);
    gruppa_zakupok.val('')
    
    var gruppa_materialov =$('#gruppa_materialov'+id);
    gruppa_materialov.val('')
    var comment =$('#comment'+id);
    comment.val('')
    

}





function create_kratkiy_tekst(id){
    
    if(!data_base[id]){
        console.log('salom')
    }else{
    
    console.log(data_base[id])
        
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
    var id_klaes =$('#id_klaes'+id);
    var gruppa_materialov =$('#gruppa_materialov'+id);
    var comment =$('#comment'+id);
    
    if(gruppa_materialov.val()!=''){
        data_base[id].gruppa_materialov = gruppa_materialov.val();
    }else{
        data_base[id].gruppa_materialov =NaN;
    }
    if(vid_zayavki.val()!=''){
        data_base[id].vid_zayavki = vid_zayavki.val();
    }else{
        data_base[id].vid_zayavki =NaN;
    }
    if(zavod.val()!=''){
        zavod.css('border-color','#dedad9')
        data_base[id].zavod = zavod.val();
    }else{
        zavod.css('border-color','red')
        data_base[id].zavod =NaN;
    }
    if(vid_zagotovki.val()!=''){
        vid_zagotovki.css('border-color','#dedad9')
        data_base[id].vid_zagotovki = vid_zagotovki.val();
    }else{
        vid_zagotovki.css('border-color','red')
        data_base[id].vid_zagotovki =NaN;
    }
    if(prodayot.val()!=''){
        prodayot.css('border-color','#dedad9')
        data_base[id].prodayot = prodayot.val();
    }else{
        prodayot.css('border-color','red')
        data_base[id].prodayot =NaN;
    }
    if(vid_materiala.val()!=''){
        vid_materiala.css('border-color','#dedad9')
        data_base[id].vid_materiala = vid_materiala.val();
    }else{
        vid_materiala.css('border-color','red')
        data_base[id].vid_materiala =NaN;
    }
    if(gruppa_zakupok.val()!=''){
        data_base[id].gruppa_zakupok = gruppa_zakupok.val();
    }else{
        data_base[id].gruppa_zakupok =NaN;
    }
    if(id_klaes.val()!=''){
        data_base[id].id_klaes = id_klaes.val();
    }else{
        data_base[id].id_klaes =NaN;
    }
    
    if(alternativ_edin.val()!=''){
        data_base[id].alternativ_edin = alternativ_edin.val();
    }else{
        data_base[id].alternativ_edin =NaN;
    }
    if(koefitsiyent.val()!=''){
        data_base[id].koefitsiyent = koefitsiyent.val();
    }else{
        data_base[id].koefitsiyent =NaN;
    }
    if(nazvaniye_tovarov.val()!=''){
        nazvaniye_tovarov.css('border-color','#dedad9')
        data_base[id].nazvaniye_tovarov = nazvaniye_tovarov.val();
    }else{
        nazvaniye_tovarov.css('border-color','red')
        data_base[id].nazvaniye_tovarov =NaN;
    }
    if(sapcode.val()!=''){
        data_base[id].sapcode = sapcode.val();
    }else{
        data_base[id].sapcode =NaN;
    }
    if(comment.val()!=''){
        data_base[id].comment = comment.val();
    }else{
        data_base[id].comment =NaN;
    }
        
    var polnoye_nazvaniye =$('#polnoye_nazvaniye'+id)
    if(polnoye_nazvaniye.val()!=''){
        polnoye_nazvaniye.css('border-color','#dedad9')
        data_base[id].polnoye_nazvaniye = polnoye_nazvaniye.val();
    }else{
        polnoye_nazvaniye.css('border-color','red')
        data_base[id].polnoye_nazvaniye =NaN;
        
        
    }
    var sena_materiala =$('#sena_materiala'+id)
    if(sena_materiala.val()!=''){
        sena_materiala.css('border-color','#dedad9')
        data_base[id].sena_materiala = sena_materiala.val();
    }else{
        sena_materiala.css('border-color','red')
        data_base[id].sena_materiala =NaN;
        
        
    }
    var bazoviy_edinitsa =$('#bazoviy_edinitsa'+id)
    if(bazoviy_edinitsa.val()!=''){
        bazoviy_edinitsa.css('border-color','#dedad9')
        data_base[id].bazoviy_edinitsa = bazoviy_edinitsa.val();
    }else{
        bazoviy_edinitsa.css('border-color','red')
        data_base[id].bazoviy_edinitsa =NaN;
        
        
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






