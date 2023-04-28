from django.urls import path,re_path
from . import views

urlpatterns = [
path('index-alumin', views.index, name='sardorbek'),
path('aluminiy',views.artikul_and_companent,name='aluminiy'),
path('upload-product',views.upload_product,name='upload_product'),
path('aluminiy-files',views.aluminiy_files,name='aluminiy_files'),
path('aluminiy-files-char-title',views.aluminiy_files_simple_char_title,name='aluminiy_files_simple_char_title'),
path('product-base',views.alu_product_base,name='alu_product_base'),
path('product-alu',views.aluminiy_productbases,name='alu_product_alu'),
path('aluminiy/gr',views.aluminiy_group,name='aluminiy_group'),
path('alum/add/<int:id>',views.product_add_second,name='aluminiy_add'),
path('alum/update-char-title/<int:id>',views.update_char_title,name='update_char_title_simple'),
path('add-to-char-utils-two',views.add_char_utils_two,name='add_char_utils_two_simple'),
path('add-to-char-utils-one',views.add_char_utils_one,name='add_char_utils_one_simple'),
path('baza-profile',views.baza_profile,name='baza_profile_simple'),
path('artikul-component',views.artikul_component,name='artikul_component_aluminiy'),
path('excel-does-not-exists-add',views.excel_does_not_exists_add,name='excel_does_not_exists_add_simple'),
path('duplicate-save',views.duplicate_correct,name='duplicate_save')
]