from django.urls import path,re_path
from . import views
from aluminiy import views as aluview
from aluminiytermo import views as alutermoview

urlpatterns = [


    ######## NORMA ############
    path('file-upload-kraska',views.full_update_norm,name='norma_file_upload_kraska7'),
    path('kombinirovaniy-process/<int:id>',views.generate_norma,name='kombinirovaniy_process_kraska7'),
    # ######## END NORMA ############

    ######### TEXCARTA #######
    path('generate-kraska-texcarta/<int:id>',views.lenght_generate_texcarta,name='lenght_generate_texcarta_kraska'),
    ######### END TEXCARTA #######


    # ####### vi files #############

    # ############# end vi #############

    

    # path('radiator-generate-sapcode/<int:id>',views.product_add_second_org_radiator,name='radiator_add_org'),

    
]

