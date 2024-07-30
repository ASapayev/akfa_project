
from django.urls import path
from . import views

urlpatterns = [
    
    path('upload-product-pvc-org',views.upload_product_org,name='upload_product_pvc_org'),
    path('upload-product-pvc-detail/<int:id>',views.product_add_second_org,name='upload_product_pvc__detail_org'),
    path('upload-char-pvc',views.upload_product_char_pvc,name='upload_char_pvc'),
    path('update-char-title-org/<int:id>',views.update_char_title_pvc,name='update_char_title_org_pvc'),
    path('show-sapcodes',views.show_list_simple_sapcodes_pvc,name='show_sapcodes_pvc'),
    path('bulk-delete-sapcodes',views.sap_code_bulk_delete,name='sap_code_bulk_delete_pvc'),
    path('delete-sapcode/<int:id>',views.delete_sap_code,name='delete_sap_code_pvc'),
    path('edit-sapcode/<int:id>',views.edit_sapcode,name='edit_sapcode_pvc'),
    path('create-artikul',views.create_artikul,name='create_artikul_pvc'),
    path('pvc-history',views.show_list_history,name='show_list_history_pvc'),
    path('get-razlovki',views.get_razlovka_pvc,name='get_razlovka_pvc'),
    path('get-all-razlovki',views.download_all_razlovki,name='download_all_razlovki_pvc'),
    path('show-all-artikules',views.show_all_artikules,name='show_all_artikules'),

    path('get-all-characteristiki',views.download_all_characteristiki,name='download_all_characteristiki_pvc'),

    ###1
    path('upload-pvc',views.upload_product_org_pvc,name='upload_online_savdo_pvc'),
    path('generate-pvc-file/<int:id>',views.create_online,name='generate_online_savdo_pvc'),

    ###2ha
    path('upload-sozd-pvc',views.upload_sozdaniye,name='upload_sozdaniye_pvc'),
    path('generate-sozdaniyepvc-file/<int:id>',views.sozdaniya_online_savdo,name='generate_sozdaniye_pvc'),

    ###3
    path('upload-sozdanipvc-sena',views.upload_sozdaniye_sena,name='upload_sozdaniye_sena_pvc'),
    path('generate-sozdaniyepvc-sena/<int:id>',views.sozdaniye_sena,name='generate_sozdaniye_sena_pvc'),

    ###4
    path('upload-sozdanipvc-format',views.upload_sozdaniye_format,name='upload_sozdaniye_format_pvc'),
    path('generate-sozdaniyepvc-format/<int:id>',views.sozdaniye_sap_format_sena,name='generate_sozdaniye_format_pvc'),

    ###5
    path('upload-fopvc-proverka',views.upload_for_proverka,name='upload_for_proverka_pvc'),
    path('generate-proverkapvc-files/<int:id>',views.proverka,name='generate_proverka_files_pvc'),
   
    ]