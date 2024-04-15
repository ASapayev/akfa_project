from django.urls import path,re_path
from . import views
from aluminiy import views as aluview
from aluminiytermo import views as alutermoview

urlpatterns = [
    path('upload-norma',views.full_update_norm,name='full_update_norm_accessuar'), 
    path('upload-siryo',views.full_update_siryo,name='full_update_siryo_accessuar'),
    path('upload-texcarta',views.full_update_texcarta,name='full_update_texcarta_accessuar'),
    path('upload-text-base',views.update_text_base,name='update_text_base'),


    

    path('get-norma',views.get_accessuar_sapcode,name='get_accessuar_sapcode'), 
    path('get-price',views.get_accessuar_sapcode_narx,name='get_accessuar_sapcode_narx'),

    path('get-texcarta',views.get_accessuar_sapcode_texcarta,name='get_accessuar_sapcode_texcarta'), 
    path('get-delete',views.texcarta_delete,name='texcarta_delete'), 



    path('generating-text',views.texcarta_delete,name='texcarta_delete'), 

    ###################new ##############
    path('create-new',views.create_new_norma,name='create_new'),
    path('create-post',views.create_norma_post,name='create_new_post'),
    path('show-sapcodes',views.show_sapcodes,name='show_sapcodes_acs'),
    path('edit-sapcode/<int:id>',views.edit_sapcode,name='edit_sapcode_acs'),
    path('copy-sapcode/<int:id>',views.copy_sapcode,name='copy_sapcode_acs'),
    path('check-sapcode',views.check_sapcode,name='check_acs'),

    path('siryo-list',views.siryo_list,name='siryo_acs'),
    path('delete-siryo/<int:id>',views.delete_siryo,name='delete_siryo_acs'),
    path('new-siryo',views.new_siryo,name='new_siryo_acs'),
    path('update-siryo/<int:id>',views.update_siryo,name='update_siryo_acs'),



    path('delete-sapcode/<int:id>',views.delete_sapcode,name='delete_sapcode_acs'),


]

