
from django.urls import path
from . import views

urlpatterns = [
    ###1
    path('upload-online-savdo',views.upload_product_org,name='upload_online_savdo'),
    path('generate-online-file/<int:id>',views.create_online,name='generate_online_savdo'),

    ###2
    path('upload-sozdaniye',views.upload_sozdaniye,name='upload_sozdaniye'),
    path('generate-sozdaniye-file/<int:id>',views.sozdaniya_online_savdo,name='generate_sozdaniye'),

    ###3
    path('upload-sozdani-sena',views.upload_sozdaniye_sena,name='upload_sozdaniye_sena'),
    path('generate-sozdaniye-sena/<int:id>',views.sozdaniye_sena,name='generate_sozdaniye_sena'),

    ###4
    path('upload-sozdani-format',views.upload_sozdaniye_format,name='upload_sozdaniye_format'),
    path('generate-sozdaniye-format/<int:id>',views.sozdaniye_sap_format_sena,name='generate_sozdaniye_format'),

    ###5
    path('upload-for-proverka',views.upload_for_proverka,name='upload_for_proverka'),
    path('generate-proverka-files/<int:id>',views.proverka,name='generate_proverka_files'),

    ###online savdo 
    path('upload-for-proverka',views.upload_file_for_preparing,name='upload_for_proverka'),
    # path('generate-proverka-files/<int:id>',views.proverka,name='generate_proverka_files'),

    ]