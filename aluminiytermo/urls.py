from django.urls import path,re_path
from . import views

urlpatterns = [
path('upload-product',views.upload_product,name='upload_product_termo'),
path('aluminiy-files',views.aluminiy_files,name='aluminiy_files_termo'),
path('product-base',views.alu_product_base,name='alu_product_base_termo'),
path('product-alu',views.aluminiy_productbases,name='alu_product_alu_termo'),
path('aluminiy/gr',views.aluminiy_group,name='aluminiy_group_termo'),
path('alum/add/<int:id>',views.product_add_second,name='aluminiy_add_termo'),
path('char-utils',views.add_characteristika_utils,name='charutils'),
path('base-profile',views.base_profile,name='base_profile')
]