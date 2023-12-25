from django.urls import path,re_path
from . import views
from aluminiy import views as aluview
from aluminiytermo import views as alutermoview

urlpatterns = [

    path('file-upload-termo-org',views.file_upload_termo_org,name='norma_file_upload_termo_org_benkam'),
    path('file-upload-org-norma',views.file_upload_org,name='norma_file_upload_org_benkam'),
    path('vifile-upload-org',views.file_vi_upload_org,name='vi_file_upload_org_benkam'),
    path('file-list-org',views.file_list_org,name='norma_file_list_org_benkam'),
    path('file-list-termo-org',views.file_list_termo_org,name='norma_file_list_termo_org_benkam'),
    path('process-combinirovanniy/<int:id>',views.kombinirovaniy_process,name='kombinirovaniy_process_benkam'),
    path('find-chaarcteristics_org',views.find_characteristics_org,name='find_characteristics_org_benkam'),
    path('show-norma-base',views.show_norm_base,name='show_norm_base_benkam'),
    path('show-sikl-base',views.show_sikl_base,name='show_sikl_base_benkam'),
    path('add-norm',views.add_norm,name = 'add_norm_benkam'),
    path('full-update-norma',views.full_update_norm,name = 'full_update_norm_benkam'),
    path('full-update-termomost',views.full_update_termomost,name = 'full_update_termomost_benkam'),
    path('add-norm-post',views.add_norm_post,name = 'add_norm_post_benkam'),
    path('edit-norm/<int:id>',views.edit_norm,name = 'edit_norm_benkam'),
    path('edit-sikl/<int:id>',views.edit_sikl,name = 'edit_sikl_benkam'),
    path('delete-norm/<int:id>',views.delete_norm,name = 'delete_norm_benkam'),
    path('vi-file-list',views.vi_file,name='vi_file_list_benkam'),
    path('vi-generate/<int:id>',views.vi_generate,name='vi_generate_benkam'),
    path('downloading-files',views.download, name='download_vi_benkam'),
    path('downloading-zip-file',views.download_zip_file, name='download_zip_file_benkam'),
    path('norma-delete-all',views.norma_delete_all,name='norma_delete_all_benkam'),
    path('termomost-delete-all',views.termomost_delete_all,name='termomost_delete_all_benkam'),
    path('full-update',views.full_update_norma,name='full_update_norma_base_benkam'),
    path('simple-razlovka',aluview.upload_razlovka_simple,name='alu_simple_raz_benkam'),
    path('norma-delete-org',views.norma_delete_org,name='norma-delete-org_benkam'),
    path('termo-razlovka',alutermoview.upload_razlovka_termo,name='alu_termo_raz_benkam'),
    
    
    
    path('ximikat',views.ximikat,name ='ximikat'),
    path('ximikat-save',views.ximikat_save,name='ximikat_save'),
    path('anod-list',views.anod_list,name='anod_list'),
    path('add-anod',views.add_anod,name='add_anod'),
    path('download-txt',views.download_txt,name='download_txt'),
    path('generate-texcarta/<int:id>',views.lenght_generate_texcarta,name='generate_texcarta'),
    path('delete-texcarta',views.delete_texcarta,name='delete_texcarta'),
    path('bulk-delete-texcarta',views.bulk_delete_texcarta,name='bulk_delete_texcarta'),
    path('delete-texcarta/<int:id>',views.delete_texcarta_one,name='delete_texcarta_one'),
    path('deletele-anod/<int:id>',views.delete_anod,name='delete_anod'),


    path('kraska-list',views.kraska_list,name='kraska_list'),
    path('add-kraska',views.add_kraska,name ='add_kraska_benkam'),
    path('deletele-kraska/<int:id>',views.kraska_anod,name='delete_kraska'),

    path('nakleyka-list',views.nakleyka_list,name ='nakleyka_list_benkam'),
    path('add-nakleyka',views.add_nakleyka,name ='add_nakleyka_benkam'),
    path('deletele-nakleyka/<int:id>',views.nakleyka_del,name='delete_nakleyka'),
   
    path('sublimatsiya-list',views.sublimatsiya_list,name ='sublimatsiya_list_benkam'),
    path('add-sublimation',views.add_sublimation_benkam,name ='add_sublimation_benkam'),
     path('deletele-sublimatsiya/<int:id>',views.sublimatsiya_del,name='delete_sublimatsiya'),



    
]

