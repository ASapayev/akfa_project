from django.urls import path,re_path
from . import views

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
    path('file-upload-org',views.file_upload_org,name='norma_file_upload_org'),
    path('file-list-org',views.file_list_org,name='norma_file_list_org'),
    path('file-list-termo-org',views.file_list_termo_org,name='norma_file_list_termo_org'),
    path('process-combinirovanniy/<int:id>',views.kombinirovaniy_process,name='kombinirovaniy_process'),
    path('find-chaarcteristics_org',views.find_characteristics_org,name='find_characteristics_org'),
    
]

