
text =""
var jsonData = JSON.parse(document.getElementById('items-data').textContent).data;
console.log(jsonData,'eeeeeeeeeeeeeeeee')

i = 0
var order_type =$('#order_type').text()

var order ={
            'alu_imzo':[ 'nazvaniye_system','base_artikul','dlina','tip_pokritiya','splav','tip_zak','combination','brend_kraska_sn','kod_kraska_sn','brend_kraska_vn','kod_kraska_vn','kod_dekor_sn','svet_dekplonka_snaruji','kod_dekor_vn','svet_dekplonka_vnutri','svet_lamplonka_snaruji','kod_lam_sn','svet_lamplonka_vnutri','kod_lam_vn','kod_anod_sn','kod_anod_vn','contactnost_anod','tip_anod','sposob_anod','kod_nakleyki','nadpis_nakleyki','baza_profiley','goods_group','tex_name','gruppa_materialov','kratkiy_tekst','sap_code_ruchnoy','kratkiy_text_ruchnoy','klaes_id','klaes_nazvaniye','kod_sveta','kratkiy_klaes','comment',],
            'alu_savdo':['nazvaniye_system','base_artikul','dlina','tip_pokritiya','splav','tip_zak','combination','brend_kraska_sn','kod_kraska_sn','brend_kraska_vn','kod_kraska_vn','kod_dekor_sn','svet_dekplonka_snaruji','kod_dekor_vn','svet_dekplonka_vnutri','kod_lam_sn','svet_lamplonka_snaruji','kod_lam_vn','svet_lamplonka_vnutri','kod_anod_sn','kod_anod_vn','contactnost_anod','tip_anod','sposob_anod','kod_nakleyki','nadpis_nakleyki','baza_profiley','gruppa_materialov','kratkiy_tekst','sap_code','krat','comment','zavod','online_id','nazvaniye_ruchnoy','svet_product','group_zakup','group','tip','segment','buxgalter_tovar','buxgalter_uchot','bazoviy_edin','alter_edin','stoimost_baza','stoimost_alter','status_online','zavod_name','diller','tip_clienta'],
            'alu_export':['nazvaniye_system','base_artikul','dlina','tip_pokritiya','splav','tip_zak','combination','brend_kraska_sn','kod_kraska_sn','brend_kraska_vn','kod_kraska_vn','kod_dekor_sn','svet_dekplonka_snaruji','kod_dekor_vn','svet_dekplonka_vnutri','svet_lamplonka_snaruji','kod_lam_sn','svet_lamplonka_vnutri','kod_lam_vn','kod_anod_sn','kod_anod_vn','contactnost_anod','tip_anod','sposob_anod','kod_nakleyki','nadpis_nakleyki','baza_profiley','gruppa_materialov','kratkiy_tekst','sap_code_ruchnoy','kratkiy_text_ruchnoy','comment',],
            'pvc_imzo':['nazvaniye_sistem','camera','base_artikul','kod_k_component','tip_pokritiya','kod_svet_zames','dlina','svet_lamplonka_snaruji','kod_lam_sn','svet_lamplonka_vnutri','kod_lam_vn','svet_rezin','kod_svet_rezini','nadpis_nakleyki','kod_nakleyki','goods_group','tex_name','kratkiy_tekst','sap_code','krat','comment','sena','klaes_id'],
            'pvc_savdo':['comment','pickupdate','diller','tip_clenta','sena_c_nds','sena_bez_nds','artikul','sap_code','krat','online_id','nazvaniye_ruchnoy','svet_product','group_zakup','group','tip','bazoviy_edin','status_online','zavod','kod_svet_zames','dlina','kod_lam_sn','kod_lam_vn','kod_nakleyki','kod_svet_rezini'],
            'pvc_export':['nazvaniye_sistem','camera','base_artikul','kod_k_component','tip_pokritiya','kod_svet_zames','dlina','svet_lamplonka_snaruji','kod_lam_sn','svet_lamplonka_vnutri','kod_lam_vn','kod_svet_rezini','svet_rezin','kod_nakleyki','nadpis_nakleyki','gruppa_materialov','kratkiy_tekst','sap_code','krat','sena_export','nazvaniye_ruchnoy'],
            'acs_imzo':['sapcode','nazvaniye_tovarov','polnoye_nazvaniye','sena_materiala','bazoviy_edinitsa','goods_group','tex_name','koefitsiyent','alternativ_edin','id_klaes','gruppa_materialov','comment'],
            'acs_savdo':['pickupdate','sena_za_bei','online_id','nazvaniye_ruchnoy','svet_product','group_zakup','group','tip','segment','buxgalter_tovar','buxgalter_uchot','bazoviy_edin','alter_edin','stoimost_baza','stoimost_alter','status_online','zavod','tip_clenta'],
            'acs_export':[ 'sapcode','nazvaniye_tovarov','polnoye_nazvaniye','sena_materiala','bazoviy_edinitsa','koefitsiyent','alternativ_edin','gruppa_materialov','comment']
            }
console.log(order_type)
for (var key in jsonData) {
    i += 1
        text2=''
        for (var j = 0; j < order[order_type].length; j++) {
            var key2 = order[order_type][j];
            if(key2 =='kratkiy_tekst'){
                text2+=`<td class="text-center" width='500' >
                            
                               <span class ='custom-width `+key2 +String(i)+String(j)+` text-center'style="text-transform: uppercase;font-size: 16px; width:200px!important" ></span>
                            
                        </td>
                        `
            }else{
                text2+=`<td class="text-center" style='background-color:white' >
                            
                               <span class ='`+key2 +String(i)+` text-center'style="text-transform: uppercase;font-size: 16px; width:auto" ></span>
                            
                        </td>
                        `
            }
        }
        text +=`
                <tr id='table_tr` +String(i)+`'  >
                                            
                    `+text2+`
                </tr>`
 
    
}



var table = $('#table-artikul')

table.append(text)
i=0
console.log(jsonData)
for (var key in jsonData) {
    i += 1
    set_values(jsonData[key],String(i),order[order_type])
    
}


function set_values(base,i,order){
    for (var j = 0; j < order.length; j++) {
        var key = order[j];
        if(base[key]){
            var va2 =$('.'+key+i+j)
            va2.text(base[key])
        }
    }
}








