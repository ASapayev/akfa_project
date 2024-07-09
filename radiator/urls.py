from django.urls import path,re_path
from . import views
from aluminiy import views as aluview
from aluminiytermo import views as alutermoview

urlpatterns = [

    path('file-upload-termo-org',views.full_update_norm,name='norma_file_upload_radiator'),
    path('file-upload-siryo',views.full_update_siryo,name='upload_siryo_radiator'),
    path('norma-radiator-upload',views.file_upload_org,name='file_upload_radiator'),
    path('norma-radiator-file-list',views.file_list_org,name='file_list_radiator'),
    path('kombinirovaniy-process/<int:id>',views.kombinirovaniy_process,name='kombinirovaniy_process_radiator'),
    
]

