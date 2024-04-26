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
        is_active=false//done

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
    }
    get_kratkiy_tekst(){
        switch(this.id){
            case 1: if(this.is_iklyuch){
                if(this.dlina && this.kod_svet_zames && this.kod_nakleyki){
                    if(this.goods_group && this.sena && this.klaes_id){
                        return {'text':this.artikul + '  '+ this.kod_svet_zames + ' L' + this.dlina +'  ' +this.kod_nakleyki,'accept':true} 
                    }else{
                        return {'text':this.artikul + '  '+ this.kod_svet_zames + ' L' + this.dlina +'  ' +this.kod_nakleyki,'accept':false} 
    
                    }
        
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
    
                }else{
        
                    if(this.kod_svet_rezini && this.dlina && this.kod_svet_zames && this.kod_nakleyki){
                        if(this.goods_group && this.sena && this.klaes_id){
                            return {'text':this.artikul + '  '+ this.kod_svet_zames + ' L' + this.dlina +'  '+this.kod_svet_rezini +'  ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.artikul + '  '+ this.kod_svet_zames + ' L' + this.dlina +'  '+this.kod_svet_rezini +'  ' +this.kod_nakleyki,'accept':false}
        
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
                        return {'text':this.artikul + '  '+this.kod_svet_zames + ' L' + this.dlina +'  ' + this.kod_lam_sn+'/'+this.kod_lam_vn + '  '+this.kod_nakleyki,'accept':true} 
                    }else{
                        console.log(this.dlina , this.kod_lam_vn , this.kod_lam_sn , this.kod_nakleyki , this.kod_svet_zames,this.kod_svet_rezini,'isklyuch3')
                        return {'text':this.artikul + '  '+this.kod_svet_zames + ' L' + this.dlina +'  ' + this.kod_lam_sn+'/'+this.kod_lam_vn + '  '+this.kod_nakleyki,'accept':false} 
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
                            return {'text':this.artikul + '  '+this.kod_svet_zames + ' L' + this.dlina +'  ' + this.kod_lam_sn+'/'+this.kod_lam_vn + '  '+this.kod_svet_rezini +'  '+this.kod_nakleyki,'accept':true} 
                        }else{
                            console.log(this.dlina , this.kod_lam_vn , this.kod_lam_sn , this.kod_nakleyki , this.kod_svet_zames,this.kod_svet_rezini,'77777777')
                            return {'text':this.artikul + '  '+this.kod_svet_zames + ' L' + this.dlina +'  ' + this.kod_lam_sn+'/'+this.kod_lam_vn + '  '+this.kod_svet_rezini +'  '+this.kod_nakleyki,'accept':false} 
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

    for(var key1 in jsonData){
        data_base[key1] = new BasePokritiya();
        Object.assign( data_base[key1] , jsonData[key1]);
    }
  i = 0

  var order_type =$('#order_type').text()
  for (var key in jsonData) {
     i+=1
    text +=`
    <tr id='table_tr` +String(i)+`' >                   
    
    <td >
        <div class="input-group input-group-sm mb-1" style='width:150px;'>
            <span id ='nazvaniye_system` +String(i)+`'style="text-transform: uppercase;font-size: 10px; font-weight:700;padding:5px;width:150px" ></span>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            <b><span id='camera` +String(i)+`'style="text-transform: uppercase; font-size:12px;padding-left:5px"></span></b>
        </div>
    </td>
    <td >
        <input type="text" id="searchInput` +String(i)+`" class=" form-control pb-1" style='width:150px' placeholder="Search for options">
        <div class="input-group input-group-sm mb-1">
        <select id="mySelect` +String(i)+`"  class=" form-control" style='display:none' multiple="multiple" ></select>
        </div>
        <span style='display:none' id='artikul_pvc` +String(i)+`'></span>
        <span style='display:none' id='iskyucheniye` +String(i)+`'></span>
        <span style='display:none' id='component` +String(i)+`'></span>
    </td>
    
    
    <td >
        <div class="input-group input-group-sm mb-1">
            <b><span  id ='kod_komponent` +String(i)+`'style="text-transform: uppercase;font-size: 12px;padding-left:5px;"></span></b>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 177px;text-transform: uppercase; font-size:12px; padding-right:0px;" onchange="tip_pokritiya_selected(`+String(i)+`,this.value)" disabled id='tip_pokritiya`+String(i)+`' required>
                <option  selected ></option>
                <option value="1" >Неламинированный</option>
                <option value="2" >Ламинированный</option>
              </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1" style="width: 190px;">
       
        <select class="form-select" aria-label="" style="width: 190px;"  disabled id='nazvaniye_svet_zames`+String(i)+`' onchange="nazvaniye_svet_zames_selected(`+String(i)+`,this.value)">
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
            <b><span  id ='kod_svet_zames` +String(i)+`'style="text-transform: uppercase;font-size: 12px;padding-left:5px;"></span></b>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            <input type="text" class="form-control " style='width:50px' onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled aria-describedby="inputGroup-sizing-sm" name ='length`+String(i)+`' id="length`+String(i)+`"  >
        </div>
    </td>

    <td >
        <div class="input-group input-group-sm mb-1">    
        <select class="form-select" aria-label="" style="width: 220px;" onchange="svet_lamplonka_snaruji_selected(`+String(i)+`,this.value)" disabled id='svet_lamplonka_snaruji`+String(i)+`'>
            <option  value="" selected></option>
            <option value="0027">Золотой дуб IW</option>
            <option value="0300">Дуб мокко IW</option>
            <option value="0549">Красный Орех IW</option>
            <option value="0550">Орех IW</option>
            <option value="1004">Мет платин</option>
            <option value="1005">Мет серый кварц</option>
            <option value="1006">Мет серый антрацит</option>
            <option value="1012">Алюкс антрацит</option>
            <option value="1015">АЛЮКС БЕЛЫЙ АЛЮМИН</option>
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
            <option value="3059">Орех терра</option>
            <option value="3062">Грецкий орех</option>
            <option value="3077">Винчестер</option>
            <option value="3081">Шеф дуб светлый</option>
            <option value="3083">Сантана</option>
            <option value="3086">ШЕФ ДУБ СЕРЫЙ</option>
            <option value="3091">Шеф дуб</option>
            <option value="3094">Орех Ребраун</option>
            <option value="4687">Кенсингтон серый</option>
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
            <option value="S513">Красный орех ADO</option>
            <option value="S540">Золотой дуб S540</option>
            <option value="5F01">Шеф дуб сер 5F01</option>
            <option value="1022">Ocean Blue</option>
            <option value="ASA1128">ASA1128</option>
            <option value="6030">МАТОВЫЙ БЕЛЫЙ</option>
            <option value="6062">МАТОВЫЙ ЧЁРНЫЙ</option>
            <option value="2509">АНТРАЦИТ СЕРЫЙ LG</option>
            <option value="9252">Винчестер Renolit</option>
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
                <option value="0027">Золотой дуб IW</option>
                <option value="0300">Дуб мокко IW</option>
                <option value="0549">Красный Орех IW</option>
                <option value="0550">Орех IW</option>
                <option value="1004">Мет платин</option>
                <option value="1005">Мет серый кварц</option>
                <option value="1006">Мет серый антрацит</option>
                <option value="1012">Алюкс антрацит</option>
                <option value="1015">АЛЮКС БЕЛЫЙ АЛЮМИН</option>
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
                <option value="3059">Орех терра</option>
                <option value="3062">Грецкий орех</option>
                <option value="3077">Винчестер</option>
                <option value="3081">Шеф дуб светлый</option>
                <option value="3083">Сантана</option>
                <option value="3086">ШЕФ ДУБ СЕРЫЙ</option>
                <option value="3091">Шеф дуб</option>
                <option value="3094">Орех Ребраун</option>
                <option value="4687">Кенсингтон серый</option>
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
                <option value="S513">Красный орех ADO</option>
                <option value="S540">Золотой дуб S540</option>
                <option value="5F01">Шеф дуб сер 5F01</option>
                <option value="1022">Ocean Blue</option>
                <option value="ASA1128">ASA1128</option>
                <option value="6030">МАТОВЫЙ БЕЛЫЙ</option>
                <option value="6062">МАТОВЫЙ ЧЁРНЫЙ</option>
                <option value="2509">АНТРАЦИТ СЕРЫЙ LG</option>
                <option value="9252">Винчестер Renolit</option>
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
        <div class="input-group input-group-sm mb-1" style="width: 150px;">
        <select class="form-select" aria-label="" style="width: 150px;border-color:red;display:none"   id='kod_svet_rezini`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)">
            <option  value="" selected ></option>
            <option value="BR" >Чёрная резина</option>
            <option value="GR" >Серая резина</option>
            <option value="NR" >Без резины</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            
                <span class =' text-center ' style="font-size:12px; font-weight: 700; text-transform: uppercase; padding:5px" id='svet_rezin`+String(i)+`'></span>
            
        </div>
    </td>
    <td >
        <input type="text" id="nakleykaInput` +String(i)+`" class=" form-control pb-1" style='width:150px' placeholder="Search for options">
        <div class="input-group input-group-sm mb-1">
        <select id="nakleykaSelect` +String(i)+`"  class=" form-control" style='display:none' multiple="multiple" ></select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
            
                <span class ='text-center ' style="font-size:12px; font-weight: bold; text-transform: uppercase;padding:5px" id='nadpis_nakleyki`+String(i)+`'></span>
            
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <select class="form-select" aria-label="" style="width: 150px;border-color:red;display:none"   id='goods_group`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)">
            <option  value="" selected ></option>
            <option value="QLIK_PVC_PROF" >ПВХ профиль</option>
            <option value="QLIK_PDF" >Подоконник</option>
        </select>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;" id='tex_name`+String(i)+`'></span>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='kratkiy_tekst`+String(i)+`'></span>
        </div>
    </td>

    <td >
        <div class="input-group input-group-sm mb-1">
       
        <input type='text' class=" form-control " style=" width: 110px; font-size:10px; display:none; height:32px" id='sap_code_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
    
        </div>
    </td> 
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style=" width: 220px; font-size:10px; display:none; height:32px"  id='kratkiy_tekst_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    
    <td >
        <div class="input-group input-group-sm mb-1">
       <textarea   rows='1' class=" form-control " style="width: 220px; font-size:10px;display:none;height:32px" id='comment`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></textarea >
       </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style=" width: 220px; font-size:10px; display:none; height:32px; border-color:red"  id='sena`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
    <td >
        <div class="input-group input-group-sm mb-1">
        <input type='text' class=" form-control " style=" width: 220px; font-size:10px; display:none; height:32px; border-color:red"  id='klaes_id`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        </div>
    </td>
   `
  }




var table = $('#table-artikul')

table.append(text)





function custom_select2(type_selection=NaN,older_val=NaN,i,nam=NaN,selector=NaN,input_selector=NaN,url=NaN,data=NaN){
    if(older_val!=NaN){
        $(input_selector).val(older_val)
        for(var key in data){
           $('#'+key +i).text(data[key])
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
                        
                        $(selector).append($(`<option>`, {
                            value: JSON.stringify(item),
                            text: item[nam]
                        }));
                    });
                },
                error: function(xhr, status, error) {
                    console.error('Failed to fetch search results:', error);
                }
            });
    
        });
        
        $(selector).on('change', function() {
            // console.log('onchangeddddddd')
            var selectedValue = $(this).find('option:selected').text();
            var value = JSON.parse($(this).val())
            console.log(value)
            $(this).css('display', 'none');
            if (type_selection.indexOf('artikul_alu') !== -1) {
                data_base[i].base_artikul =selectedValue
            }
            if (type_selection.indexOf('artikul_imzo') !== -1) {
                console.log()
                data_base[i].base_artikul =selectedValue
                data_base[i].nazvaniye_system = value['nazvaniye_sistem']
                data_base[i].camera = value['camera']
                data_base[i].kod_k_component = value['kod_k_component']
                data_base[i].artikul = value['component2']
    
                $('#artikul_pvc'+i).text(value['artikul'])
                $('#iskyucheniye'+i).text(value['iskyucheniye'])
                $('#component'+i).text(value['component2'])


                $('#nazvaniye_system'+i).text(value['nazvaniye_sistem'])
                $('#camera'+i).text(value['camera'])
                $('#kod_komponent'+i).text(value['kod_k_component'])
            }
            if (type_selection.indexOf('nak') !== -1) {
                data_base[i].kod_nakleyki = selectedValue
                data_base[i].nadpis_nakleyki = value['nadpis']
                $('#nadpis_nakleyki'+i).text(value['nadpis'])
            }
            // ######## dovomi bor
            $(input_selector).val(selectedValue)

            var data = data_base[i].get_kratkiy_tekst()
            console.log(data)
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


for(var key in jsonData){
    i+=1
    data ={
        'component':jsonData[key]['artikul'],
        'artikul_pvc':jsonData[key]['base_artikul'],
        'nazvaniye_system':jsonData[key]['nazvaniye_system'],
        'camera':jsonData[key]['camera'],
        'kod_komponent':jsonData[key]['kod_k_component'],
        'iskyucheniye':jsonData[key]['is_iklyuch']
    }
    custom_select2(type_selection='artikul_imzo',jsonData[i]['base_artikul'],i,nam='artikul','#mySelect'+i,'#searchInput'+i, url= '/client/pvc-artikul-list',data=data)    

    if(jsonData[i]['id']){
        $('#tip_pokritiya' +i).val(jsonData[i]['id'])
    }
    if(jsonData[i]['nazvaniye_svet_zames']){
        $('#nazvaniye_svet_zames' +i).attr('disabled',false)
        $('#nazvaniye_svet_zames' +i).val(jsonData[i]['kod_svet_zames'])
    }
    if(jsonData[i]['kod_svet_zames']){
        $('#kod_svet_zames' +i).attr('disabled',false)
        $('#kod_svet_zames' +i).text(jsonData[i]['kod_svet_zames'])
    }
    if(jsonData[i]['dlina']){
        $('#length' +i).attr('disabled',false)
        $('#length' +i).val(jsonData[i]['dlina'])
    }
    if(jsonData[i]['svet_lamplonka_snaruji']){
        $('#svet_lamplonka_snaruji' +i).attr('disabled',false)
        $('#svet_lamplonka_snaruji' +i).val(jsonData[i]['kod_lam_sn'])
        $('#code_lamplonka_snaruji' +i).text(jsonData[i]['kod_lam_sn'])
    }
    if(jsonData[i]['svet_lamplonka_vnutri']){
        $('#svet_lamplonka_vnutri' +i).attr('disabled',false)
        $('#svet_lamplonka_vnutri' +i).val(jsonData[i]['kod_lam_vn'])
        $('#code_lamplonka_vnutri' +i).text(jsonData[i]['kod_lam_vn'])
    }
    if(jsonData[i]['kod_svet_rezini']){
        $('#kod_svet_rezini' +i).css('display','block')
        $('#kod_svet_rezini' +i).css('border-color','#dedad9')
        $('#kod_svet_rezini' +i).val(jsonData[i]['kod_svet_rezini'])
        $('#svet_rezin' +i).text(jsonData[i]['kod_svet_rezini'])
    }
    data ={
        'nadpis_nakleyki':jsonData[i]['nadpis_nakleyki']
    }
    custom_select2(type_selection='nakleyka',jsonData[i]['kod_nakleyki'],i,nam='name','#nakleykaSelect'+i,'#nakleykaInput'+i, url= '/client/nakleyka-list-pvc',data=data)

    if(jsonData[i]['kratkiy_tekst']){
        $('#kratkiy_tekst' +i).text(jsonData[i]['kratkiy_tekst'])
    }
    if(jsonData[i]['goods_group']){
        $('#goods_group' +i).css('display','block')
        $('#goods_group' +i).css('border-color','#dedad9')
        $('#goods_group' +i).val(jsonData[i]['tex_name'])
        $('#tex_name' +i).text(jsonData[i]['tex_name'])
    }
    $('#sap_code_ruchnoy' +i).css('display','block')
    $('#sap_code_ruchnoy' +i).val(jsonData[i]['sap_code'])

    $('#kratkiy_tekst_ruchnoy' +i).css('display','block')
    $('#kratkiy_tekst_ruchnoy' +i).val(jsonData[i]['krat'])

    $('#comment' +i).css('display','block')
    $('#comment' +i).val(jsonData[i]['comment'])

    $('#sena' +i).css('display','block')
    $('#sena' +i).css('border-color','#dedad9')
    $('#sena' +i).val(jsonData[i]['sena'])

    $('#klaes_id' +i).css('display','block')
    $('#klaes_id' +i).css('border-color','#dedad9')
    $('#klaes_id' +i).val(jsonData[i]['klaes_id'])

       // create_kratkiy_tekst(i)
}


function get_nakleyka(i){
    $('.kod_nakleyki'+i).select2({
        ajax: {
            url: "/client/nakleyka-list-pvc",
            dataType: 'json',
            processResults: function(data){
                return {results: $.map(data, function(item){
                    return {id:item.name,text:item.nadpis,nadpis:item.name}
                })
            };
            }
        }
        });
        $(".kod_nakleyki"+String(i)).on("select2:select", function (e) { 
            var nadpis_nakleyki = $('#nadpis_nakleyki'+String(i));
            nadpis_nakleyki.text(e.params.data.nadpis);
            
            })
}





function artukil_clear(id){
    $('#artikul'+id).val(null).trigger('change');
    clear_artikul(id)
}



function clear_artikul(id){
    var table_tr =$('#table_tr'+id);
    $('#nazvaniye_system'+id).text('');
    var tip_pokritiya = $('#tip_pokritiya'+String(id));
    tip_pokritiya.val('0').change();
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
    sap_code_ruchnoy.css('display','none');
    var kratkiy_tekst_ruchnoy =$('#kratkiy_tekst_ruchnoy'+String(id));
    kratkiy_tekst_ruchnoy.val('');
    kratkiy_tekst_ruchnoy.css('display','none');
    var comment =$('#comment'+String(id));
    comment.val('');
    comment.css('display','none');
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

    

    // var nakleyka_select = $('#nakleyka_select'+String(id));
    // nakleyka_select.css('display','block');
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

        var kod_svet_rezini = $('#kod_svet_rezini'+String(id));
        kod_svet_rezini.val('')
        kod_svet_rezini.css('display','block');
        var goods_group = $('#goods_group'+String(id));
        goods_group.val('')
        goods_group.css('display','block');

        const spanss =document.querySelector('.nak_select' +id+ ' .select2-container .select2-selection--single')
        spanss.style.borderColor='red';
        
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
        const spanss =document.querySelector('.nak_select' +id+ ' .select2-container .select2-selection--single')
        spanss.style.borderColor='red';

        var kod_svet_rezini = $('#kod_svet_rezini'+String(id));
        kod_svet_rezini.val('')
        

        var svet_lamplonka_snaruji = $('#svet_lamplonka_snaruji'+String(id));
        svet_lamplonka_snaruji.attr("disabled",false);
        svet_lamplonka_snaruji.attr("required",true);
        svet_lamplonka_snaruji.css("border-color",'#fc2003');
        var svet_lamplonka_vnutri = $('#svet_lamplonka_vnutri'+String(id));
        svet_lamplonka_vnutri.attr("disabled",false);
        svet_lamplonka_vnutri.attr("required",true);
        svet_lamplonka_vnutri.css("border-color",'#fc2003');

        if(iskyucheniye =='1'){
            data_base[id].is_iklyuch=true
            kod_svet_rezini.css('display','none')
        }else{
            data_base[id].is_iklyuch=false
            kod_svet_rezini.css('display','block');
        }
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
    if(dlina.val()!=''){
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
        if(kod_svet_rezini.val()!=''){
            var svet_rezin =$('#svet_rezin' + id);
            var selectedText = $("#kod_svet_rezini"+id + " option:selected");
            svet_rezin.text(kod_svet_rezini.val())
            kod_svet_rezini.css('border-color','#dedad9')
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
        if(kod_svet_rezini.val()!=''){
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


    

    if(String(val) == '1'){

        var nakleyka_select = $('#nakleykaInput'+String(id))
        
        if(nakleyka_select.val() !=''){
            var nadpis_nakleyki = $('#nadpis_nakleyki'+id)
            nadpis_nakleyki.css('border-color','#dedad9');
            // nakleyka_select.style.borderBlockColor='#dedad9'
            data_base[id].kod_nakleyki = nakleyka_select.val()
            data_base[id].nadpis_nakleyki = nadpis_nakleyki.text();
            
        }else{
            // spanss.style.borderColor='red';
            // nakleyka_select.style.borderBlockColor='red'
            data_base[id].nadpis_nakleyki = NaN;
            data_base[id].kod_nakleyki = NaN

        }

       
    }
    else if(String(val) == '2'){
       

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
    
    kratkiy_tekst.text(data.text)

    }
}







