from django.urls import path,re_path
from . import views

urlpatterns = [
path('upload-product',views.upload_product,name='upload_product_termo'),
path('aluminiy-files',views.aluminiy_files,name='aluminiy_files_termo'),
path('aluminiy-files-char-title',views.aluminiy_files_termo_char_title,name='aluminiy_files_termo_char_title'),
path('product-base',views.alu_product_base,name='alu_product_base_termo'),
path('product-alu',views.aluminiy_productbases,name='alu_product_alu_termo'),
path('aluminiy/gr',views.aluminiy_group,name='aluminiy_group_termo'),
path('alum/add/<int:id>',views.product_add_second,name='aluminiy_add_termo'),
path('alum/update-char-title/<int:id>',views.update_char_title,name='update_char_title'),
path('char-utils',views.add_characteristika_utils,name='charutils'),
path('base-profile',views.base_profile,name='base_profile'),
path('add-to-char-utils-two',views.add_char_utils_two,name='add_char_utils_two'),
path('add-to-char-utils-one',views.add_char_utils_one,name='add_char_utils_one'),
path('baza-profile',views.baza_profile,name='baza_profile'),
path('excel-does-not-exists-add',views.excel_does_not_exists_add,name='excel_does_not_exists_add'),
]