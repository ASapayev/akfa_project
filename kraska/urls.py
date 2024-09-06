from django.urls import path,re_path
from . import views
from aluminiy import views as aluview
from aluminiytermo import views as alutermoview

urlpatterns = [


    ######## NORMA ############
    path('file-upload-kraska-7',views.full_update_norm7,name='norma_file_upload_kraska7'),
    path('file-upload-kraska-75',views.full_update_norm75,name='norma_file_upload_kraska75'),
    # path('file-upload-radiator-texcarta',views.file_upload_radiator_tex,name='file_upload_radiator_tex'),
    # path('file-upload-siryo',views.full_update_siryo,name='upload_siryo_radiator'),
    # path('file-upload-korobka',views.full_update_korobka,name='upload_korobka_radiator'),
    # path('file-upload-kraska',views.full_update_kraska,name='upload_kraska_radiator'),
    # path('norma-radiator-upload',views.file_upload_org,name='file_upload_radiator'),
    # path('norma-radiator-file-list',views.file_list_org,name='file_list_radiator'),
    path('kombinirovaniy-process-7/<int:id>',views.generate_norma_7,name='kombinirovaniy_process_kraska7'),
    path('kombinirovaniy-process-75/<int:id>',views.generate_norma_75,name='kombinirovaniy_process_kraska75'),
    # path('get-razlovka-radiator',views.get_razlovka_radiator,name='get_razlovka_radiator'),

    # ######## END NORMA ############

    # ######## texcarta #######
    path('generate-kraska-texcarta/<int:id>',views.lenght_generate_texcarta,name='lenght_generate_texcarta_kraska'),


    # ####### vi files #############
    # path('vifile-upload-radiator',views.file_vi_upload_org,name='vi_file_upload_radiator'),
    # path('vifile-mo-upload-radiator',views.file_vi_mo_upload_org,name='vi_mo_file_upload_radiator'),
    # path('vi-file-list',views.vi_file,name='vi_file_list_radiator'),
    # path('vi-mo-file-list',views.vi_mo_file,name='vi_mo_file_list_radiator'),
    # path('vi-generate/<int:id>',views.vi_generate,name='vi_generate_radiator'),
    # path('vi-generate-mo/<int:id>',views.vi_generate_mo,name='vi_generate_mo_radiator'),
    # ############# end vi #############

    

    # path('radiator-generate-sapcode/<int:id>',views.product_add_second_org_radiator,name='radiator_add_org'),

    
]

