from django.urls import path,re_path
from . import views
from aluminiy import views as aluview
from aluminiytermo import views as alutermoview

urlpatterns = [


    ######## NORMA ############
    path('file-upload-epdm',views.full_update_norm,name='norma_file_upload_epdm'),
    # path('file-upload-kraska-75',views.full_update_norm75,name='norma_file_upload_kraska75'),
     path('show-siryo',views.show_siryo,name='show_siryo'),
    path('add-sapcode-from-file',views.create_siryo_from_file, name='create_siryo_from_file'),
    
    path('add-sapcode',views.create_siryo, name='create_siryo_epdm'),
    path('edit-sapcode/<int:id>',views.edit_siryo, name='edit_siryo_epdm'),
    path('delete-siryo/<int:id>',views.delete_siryo,name='delete_siryo'),
    path('siryo-bulk-delete',views.siryo_bulk_delete,name='siryo_bulk_delete_epdm'),

    path('kombinirovaniy-process-epdm',views.find_norma,name='kombinirovaniy_process_epdm'),
 
    # ######## END NORMA ############

    # ######## texcarta #######
    path('file-epdm-texcarta',views.file_upload_epdm_tex,name='file_upload_epdm_tex'),
    path('generate-epdm-texcarta/<int:id>',views.lenght_generate_texcarta,name='lenght_generate_texcarta_epdm'),


 
    path('get-or-add-option-epdm-artikul/', views.get_or_add_option, name='get_or_add_option_epd_artikul'),

    path('epdm-generate-sapcode/<int:id>',views.product_add_second_org_epdm,name='generate_sapcode_epdm'),

    
]

