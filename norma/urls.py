from django.urls import path,re_path
from . import views
from aluminiy import views as aluview
from aluminiytermo import views as alutermoview

urlpatterns = [
    path('norma-base',views.norma_excel,name='norma_excel'),
    path('receipt-all',views.receipt_all,name='receipt_all'),
    path('',views.index,name='norma_index'),
    path('file-upload',views.file_upload,name='norma_file_upload'),
    path('file-list',views.file_list,name='norma_file_list'),
    path('generate',views.generatenewexceldata,name ='excellgenerate'),
    path('remove-whitespace',views.remove_whitespace,name ='remove_whitespace'),
    path('norma-utils',views.norma_add,name ='norma_utils'),
    path('nakleyka-delete',views.nakleyka_duplicate_del,name ='nakleyka_delete'),
    path('norma-update',views.norma_update,name='norma_update'),
    path('norma-delete',views.norma_delete,name='norma-delete'),
    path('norma-delete-org',views.norma_delete_org,name='norma-delete-org'),
    path('find-chaarcteristics',views.find_characteristics,name='find-characteristics'),
    
    path('file-upload-termo-org',views.file_upload_termo_org,name='norma_file_upload_termo_org'),
    path('file-upload-org-norma',views.file_upload_org,name='norma_file_upload_org'),
    path('vifile-upload-org',views.file_vi_upload_org,name='vi_file_upload_org'),
    path('file-list-org',views.file_list_org,name='norma_file_list_org'),
    path('file-list-termo-org',views.file_list_termo_org,name='norma_file_list_termo_org'),
    path('process-combinirovanniy/<int:id>',views.kombinirovaniy_process,name='kombinirovaniy_process'),
    path('find-chaarcteristics_org',views.find_characteristics_org,name='find_characteristics_org'),
    path('show-norma-base',views.show_norm_base,name='show_norm_base'),
    path('show-sikl-base',views.show_sikl_base,name='show_sikl_base'),
    path('add-norm',views.add_norm,name = 'add_norm'),
    path('full-update-norma',views.full_update_norm,name = 'full_update_norm'),
    path('add-norm-post',views.add_norm_post,name = 'add_norm_post'),
    path('edit-norm/<int:id>',views.edit_norm,name = 'edit_norm'),
    path('edit-sikl/<int:id>',views.edit_sikl,name = 'edit_sikl'),
    path('delete-norm/<int:id>',views.delete_norm,name = 'delete_norm'),
    path('vi-file-list',views.vi_file,name='vi_file_list'),
    path('vi-generate/<int:id>',views.vi_generate,name='vi_generate'),
    path('downloading-files',views.download, name='download_vi'),
    path('downloading-zip-file',views.download_zip_file, name='download_zip_file'),
    path('norma-delete-all',views.norma_delete_all,name='norma_delete_all'),
    path('full-update',views.full_update_norma,name='full_update_norma_base'),
    path('simple-razlovka',aluview.upload_razlovka_simple,name='alu_simple_raz'),
    path('termo-razlovka',alutermoview.upload_razlovka_termo,name='alu_termo_raz'),


    
]

