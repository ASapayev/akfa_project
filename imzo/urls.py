from django.urls import path,re_path
from . import views

urlpatterns = [
  path('abduvali/',views.index, name='abduvali'),
  path('file-upload-imzo/',views.file_uploadImzo, name='imzo_file_upload'),
  path('imzo/file',views.imzo_file, name='imzo_file'),
  path('imzo/<int:id>',views.lenght_generate_imzo,name='imzo_gen'),
  path('texcartabaseupload',views.texcartaupload,name='texcartaupload'),
  path('remove',views.delete_tex,name='remove'),
  path('tex-delete',views.tex_delete,name='tex-delete'),
  path('tex-delete-org',views.tex_delete_org,name='tex-delete-org'),

  path('file-upload-texcart/',views.file_uploadTexcarta_org, name='texcart_file_upload'),
  path('texcarta/file-list-texcart',views.texcart_file, name='texcart_files'),
  path('texcarta/<int:id>',views.lenght_generate_texcarta,name='texcarta_gen'),

]