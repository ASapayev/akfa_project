from django.urls import path,re_path
from . import views

urlpatterns = [
path('alum/update-char-title/<int:id>',views.update_char_title,name='update_char_title'),
path('excel-does-not-exists-add',views.excel_does_not_exists_add,name='excel_does_not_exists_add'),
path('upload-product',views.upload_product,name='upload_product_termo'),
path('aluminiy-files',views.aluminiy_files,name='aluminiy_files_termo'),
path('aluminiy-files-char-title',views.aluminiy_files_termo_char_title,name='aluminiy_files_termo_char_title'),
path('product-base',views.alu_product_base,name='alu_product_base_termo'),
path('product-alu',views.aluminiy_productbases,name='alu_product_alu_termo'),
path('aluminiy/gr',views.aluminiy_group,name='aluminiy_group_termo'),
path('razlovka-termo',views.razlovkatermo_save,name='razlovka-save'),
path('character-force/<int:id>',views.create_characteristika_force, name='cretecharacteristika'),

path('update-artikul-component',views.full_artikul_component,name='update_artikul_component'),#artikul component download


path('upload-product-termo-org',views.upload_product_org,name='upload_product_termo_org'),
path('upload-char',views.upload_product_char,name='upload_char'),
path('alum/update-char-title-org/<int:id>',views.update_char_title,name='update_char_title_org'),
path('aluminiy-files-termo-org',views.aluminiy_files_org,name='aluminiy_files_termo_org'),
path('aluminiy-files-char-org',views.aluminiy_files_char_org,name='aluminiy_files_char_org'),
path('alumtermo/add/<int:id>',views.product_add_second_org,name='aluminiy_add_termo_org'),
path('character-extras/',views.character_extras,name ='character_extras'),
path('show-list-termo/',views.show_list_simple_sapcodes,name ='show_list_termo'),
path('downloading-characteristika/',views.downloading_characteristika,name ='downloading_character'),
path('create-txt',views.create_txt_for_1101,name='create_txt_for_1101'),
path('get-raube',views.get_raube,name='get_raube'),
path('get-sapcodes',views.get_sapcodes,name='get_sapcodes'),
path('upload-character-force',views.upload_for_char_termo,name='upload_for_char_termo'),
path('termo-files-org-force',views.char_files_org_termo,name='char_files_org_termo'),
path('for-three-factory',views.upload_for_1301,name='upload_for_1301'),
path('upload-razlovka-termo',views.upload_razlovka_termo,name='upload_razlovka_termo'),
path('new',views.upload_for_1301_v22,name='sdf'),
path('create-construction-v2',views.upload_for_1301_v22, name ='mmmmmmmm' ),

#####################################
path('sms-list',views.sms_list,name='sms_list'),
path('sms-detail/<uuid>',views.sms_detail,name='sms_detail'),
path('create-fake-sms',views.create_fake,name='create_new_sms'),
path('sms-save',views.sms_save,name='sms_save'),
path('lobby',views.lobby,name='lobby')

]