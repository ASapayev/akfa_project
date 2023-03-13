from django.urls import path,re_path
from . import views

urlpatterns = [
#  path('')
path('aluminiy',views.artikul_and_companent,name='aluminiy'),
path('upload-product',views.upload_product,name='upload_product'),
path('aluminiy-files',views.aluminiy_files,name='aluminiy_files'),
path('product-base',views.alu_product_base,name='alu_product_base'),
  
]