from django.urls import path,re_path
from . import views
from aluminiy import views as aluview
from aluminiytermo import views as alutermoview

urlpatterns = [
    ########## SAPCODE GENERATING #########
    # path('file-upload-kraska',views.file_upload_for_kraska,name='file_upload_kraska'),
    # path('kraska-file-list',views.file_list_org_kraska,name='kraska_file_list'),
    # path('generate-sapcode/<int:id>',views.product_add_second_org_kraska,name='generate_sapcode_kraska'),
    ##########END ##########

    ######## NORMA ############
    path('file-upload-matrix-norma',views.upload_razlovka_file,name='norma_file_upload_matrix'),
    path('kombinirovaniy-process-matrix/<int:id>',views.create_norma_for_matrix,name='kombinirovaniy_process_matrix'),

    # path('show-siryo',views.show_siryo,name='show_siryo_kraska'),
    # path('add-sapcode-from-file',views.create_siryo_from_file, name='create_siryo_kraska_from_file'),
    # path('add-sapcode',views.create_siryo, name='create_siryo_kraska'),
    # path('edit-sapcode/<int:id>',views.edit_siryo, name='edit_siryo_kraska'),
    # path('delete-siryo/<int:id>',views.delete_siryo,name='delete_siryo'),
    # path('siryo-bulk-delete',views.siryo_bulk_delete,name='siryo_bulk_delete_kraska'),

    # ######## END NORMA ############

    ######### TEXCARTA #######
    path('file-matrix-texcarta',views.file_upload_matrix_tex,name='file_upload_matrix_tex'),
    path('generate-matrix-texcarta/<int:id>',views.lenght_generate_texcarta,name='lenght_generate_texcarta_matrix'),
    ######### END TEXCARTA #######


    # ####### vi files #############

    # ############# end vi #############

    ############ API ###########
    # path('get-or-add-option-kraska/', views.get_or_add_option, name='get_or_add_option_kraska'),

    

    


    
]

