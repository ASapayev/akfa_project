from django.urls import path,re_path
from . import views

urlpatterns = [
  path('abduvali/',views.index, name='abduvali'),
  path('file-upload-imzo/',views.file_uploadImzo, name='imzo_file_upload'),
  path('imzo/file',views.imzo_file, name='imzo_file'),
  path('imzo/<int:id>',views.lenght_generate_imzo,name='imzo_gen'),
  path('texcartabaseupload',views.texcartaupload,name='texcartaupload'),

]