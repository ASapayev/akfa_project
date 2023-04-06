from django.urls import path,re_path
from . import views

urlpatterns = [
 path('norma-base',views.norma_excel,name='norma_excel'),
 path('receipt-all',views.receipt_all,name='receipt_all'),
 path('process/<int:id>',views.process,name='process'),
 path('',views.index,name='norma_index'),
 path('file-upload',views.file_upload,name='norma_file_upload'),
 path('file-list',views.file_list,name='norma_file_list'),
 path('generate',views.generatenewexceldata,name ='excellgenerate')
]