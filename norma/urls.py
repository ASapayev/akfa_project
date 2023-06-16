from django.urls import path,re_path
from . import views

urlpatterns = [
 path('norma-base',views.norma_excel,name='norma_excel'),
 path('receipt-all',views.receipt_all,name='receipt_all'),
#  path('process/<int:id>',views.process,name='process'),
 path('process-combinirovanniy/<int:id>',views.kombinirovaniy_process,name='kombinirovaniy_process'),
 path('',views.index,name='norma_index'),
 path('file-upload',views.file_upload,name='norma_file_upload'),
 path('file-list',views.file_list,name='norma_file_list'),
 path('generate',views.generatenewexceldata,name ='excellgenerate'),
 path('remove-whitespace',views.remove_whitespace,name ='remove_whitespace'),
 path('norma-utils',views.norma_add,name ='norma_utils'),
 path('nakleyka-delete',views.nakleyka_duplicate_del,name ='nakleyka_delete'),
 path('norma-update',views.norma_update,name='norma_update')
 
]

