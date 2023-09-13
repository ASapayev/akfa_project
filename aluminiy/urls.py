from django.urls import path,re_path
from . import views

urlpatterns = [
path('index-alumin', views.index, name='sardorbek'),
path('aluminiy',views.artikul_and_companent,name='aluminiy'),
path('upload-product',views.upload_product,name='upload_product'),
path('aluminiy-files',views.aluminiy_files,name='aluminiy_files'),
path('aluminiy-files-char-title',views.aluminiy_files_simple_char_title,name='aluminiy_files_simple_char_title'),
path('product-base',views.alu_product_base,name='alu_product_base'),
path('product-alu',views.aluminiy_productbases,name='alu_product_alu'),
path('aluminiy/gr',views.aluminiy_group,name='aluminiy_group'),
path('alum/add/<int:id>',views.product_add_second,name='aluminiy_add'),
path('alum/update-char-title/<int:id>',views.update_char_title,name='update_char_title_simple'),
path('add-to-char-utils-two',views.add_char_utils_two,name='add_char_utils_two_simple'),
path('add-to-char-utils-one',views.add_char_utils_one,name='add_char_utils_one_simple'),
path('baza-profile',views.baza_profile,name='baza_profile_simple'),
path('artikul-component',views.artikul_component,name='artikul_component_aluminiy'),
path('excel-does-not-exists-add',views.excel_does_not_exists_add,name='excel_does_not_exists_add_simple'),
path('duplicate-save',views.duplicate_correct,name='duplicate_save'),
path('razlovka-simple',views.razlovka_save,name='razlovka_save'),

path('alum/update-char-title-org/<int:id>',views.update_char_title,name='update_char_title_org'),
path('upload-product-org',views.upload_product_org,name='upload_product_org'),
path('aluminiy-files-org',views.aluminiy_files_org,name='aluminiy_files_org'),
path('char-files-org',views.char_files_org,name='char_files_org'),
path('alum-org/add/<int:id>',views.product_add_second_org,name='aluminiy_add_org'),
path('save-razlovka-org',views.save_razlovka2,name='aluminiy_add_org2'),
path('show-simple-sap-list',views.show_list_simple_sapcodes,name='show_simple_sapcodes'),
path('delete-sapcode/<int:id>',views.delete_sap_code, name='delete_sapkode'),
path('bulk-delete-sapcode',views.sap_code_bulk_delete, name='bulk_delete_sapkode'),
path('show-razlovki',views.show_razlovki,name='show_razlovki'),
path('show-termo-razlovki',views.show_razlovki_termo,name='show_razlovki_termo'),
path('download-razlovki',views.download_all_razlovki,name='download_razlovki_all'),
path('upload-for-character',views.upload_for_char,name='upload_for_char'),
path('upload-razlovka-simple',views.upload_razlovka_simple,name='upload_razlovka_simple'),
path('show-price-profile', views.show_price_profile,name='show_profile'),
path('delete-length-profile/<int:id>',views.delete_length_profile,name='delete_length_profile'), 
path('bulk-delete-length-profile',views.bulk_delete_length_profile,name='bulk_delete_length_profile'), 
path('length-profile-edit/<int:id>',views.profile_edit,name='edit_profile_length'),
path('add-length-profile',views.add_length_profile,name='add_length_profile'),
path('edit-currency',views.edit_currency,name='edit_currency')

]