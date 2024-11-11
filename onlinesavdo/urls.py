
from django.urls import path
from . import views

urlpatterns = [
    ###1
    path('upload-online-savdo',views.upload_product_org,name='upload_online_savdo'),
    path('generate-online-file/<int:id>',views.create_online,name='generate_online_savdo'),

    ###5
    path('upload-for-proverka',views.upload_for_proverka,name='upload_for_proverka'),
    path('generate-proverka-files/<int:id>',views.proverka,name='generate_proverka_files'),

    ###online savdo 
    path('upload-for-merging',views.upload_file_for_preparing,name='upload_file_for_preparing'),
    path('generate-merging-files/<int:id>',views.merging_files,name='merging_files'),

    ]