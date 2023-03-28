from django.urls import path,re_path
from . import views

urlpatterns = [
 path('index-alumin', views.index, name='sardorbek'),
path('aluminiy',views.artikul_and_companent,name='aluminiy'),
path('upload-product',views.upload_product,name='upload_product'),
path('aluminiy-files',views.aluminiy_files,name='aluminiy_files'),
path('product-base',views.alu_product_base,name='alu_product_base'),
path('product-alu',views.aluminiy_productbases,name='alu_product_alu'),
path('aluminiy/gr',views.aluminiy_group,name='aluminiy_group'),
path('alum/add/<int:id>',views.product_add,name='aluminiy_add'),

  
]