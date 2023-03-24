from django.urls import path,re_path
from . import views

urlpatterns = [
  path('',views.index, name='index'),
  path('home',views.home, name='home'),
  path('exel_to_sql',views.excel,name='excel'),
  path('list',views.show_list,name='show_list'),
  path('json',views.experiment_json,name='json'),
  path('new',views.counter_set,name='new'),
  path('gr',views.group,name='gr'),
  path('sz',views.size_product,name='size'),
  path('file-upload',views.file_upload,name='file-upload'),
  path('file-list',views.file_list,name='file_list'),
  path('import-and-merge/<int:id>',views.import_file,name='import_and_merge'),
  path('get-counter',views.counter_exist_data,name='get_counter'),
  path('add-data/<int:id>',views.read_and_write,name='add_data'),
  path('download/<int:id>',views.download,name='download'),
  path('len-gen/<int:id>',views.lenght_generate,name='lenght_generate'),
  path('delete-file/<int:id>',views.delete_file,name='delete_file'),
  
]