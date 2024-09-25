from django.urls import path,include
from . import views

urlpatterns = [
    path('index',views.index,name='client_index'),
    ######Aluminiy############
    path('shablon-imzo-detail',views.shablon_imzo_detail,name='shablon_imzo_detail'),
    path('shablon-savdo-detail',views.shablon_savdo_detail,name='shablon_savdo_detail'),
    path('shablon-export-detail',views.shablon_export_detail,name='shablon_export_detail'),

    ######PVC############
    path('shablon-pvc-imzo-detail',views.shablon_pvc_export_detail,name='shablon_pvc_imzo_detail'),
    path('shablon-pvc-savdo-detail',views.shablon_pvc_savdo_detail,name='shablon_pvc_savdo_detail'),
    path('shablon-pvc-export-detail',views.shablon_pvc_export_savdo_detail,name='shablon_pvc_export_detail'),

    ######Accessuar############
    path('shablon-acs-imzo-detail',views.shablon_acs_export_detail,name='shablon_acs_imzo_detail'),
    path('shablon-acs-savdo-detail',views.shablon_acs_savdo_detail,name='shablon_acs_savdo_detail'),
    path('shablon-acs-export-detail',views.shablon_acs_export_savdo_detail,name='shablon_acs_export_detail'),
    path('shablon-acs-zavod-detail',views.shablon_acs_zavod_savdo_detail,name='shablon_acs_zavod_detail'),
    path('shablon-acs-texnopark-detail',views.shablon_accessuar_texnopark_detail,name='shablon_acs_texnopark_detail'),


    ######AKP###############
    path('shablon-akp-savdo-detail',views.shablon_akp_savdo_detail,name='shablon_akp_savdo_detail'),

    #######RADIATOR##############
    path('shablon-radiator-detail',views.shablon_radiator_detail,name='shablon_radiator_detail'),
    path('shablon-radiator-export-detail',views.shablon_radiator_export_detail,name='shablon_radiator_export_detail'),

    ####### Prochiye #########
    path('shablon-prochiye-detail',views.shablon_prochiye_detail,name='shablon_prochie_detail'),
    path('shablon-prochiye-tms-detail',views.shablon_prochiye_tms_detail,name='shablon_prochie_tms_detail'),


    ####### Accessuar Import #########
    path('shablon-accessuar-import-detail',views.shablon_accessuar_import_detail,name='shablon_accessuar_import_detail'),

    ####### Change Data #########
    path('change-data-detail',views.shablon_change_data_detail,name='shablon_change_data_detail'),



    ########### bussines partner #############
    path('bussines-partner-detail',views.bussines_partner,name='bussines_partner'),





    ################## APIS ################
        ######## ALU #####
    path('imzo-artikul-list',views.imzo_artikul_list,name='imzo_artikul_list'),
    path('nakleyka-list',views.nakleyka_list,name='nakleyka_list'),
    path('client-anod-list',views.anod_list,name='client_anod_list'),

        ######### PVC ######
    path('pvc-artikul-list',views.pvc_artikul_list,name='pvc_artikul_list'),
    path('nakleyka-list-pvc',views.nakleyka_list_pvc,name='nakleyka_list_pvc'),

        ######## Radiator ########
    path('radiator-artikul-list',views.radiator_artikul_list,name='radiator_artikul_list'),


    ################ Order ###########

    ###### Moderator #####
    path('order-list-check',views.order_list_for_moderator,name='order_list_for_moderator'),
    path('order-check/<int:id>',views.moderator_check,name='order_check'),
    path('order-check-zavod/<int:id>',views.moderator_check_zavod,name='order_check_zavod'),
    path('order-convert/<int:id>',views.moderator_convert,name='order_convert'),
    path('save-ves-of-profile',views.save_ves_of_profile,name='save_ves_of_profile'),
    path('save-ves-of-profile-single',views.save_ves_of_profile_single,name='save_ves_of_profile_single'),
    


    ####### Customer ######
    path('order-save',views.OrderSaveView.as_view(),name='order_save'),



    # path('detail-order-update/<int:id>',views.detail_order_update,name='detail_order_update'),
    path('detail-order-update/<int:id>',views.order_update_all,name='order_update_all'),
    path('order-update/<int:id>',views.order_update,name='order_update'),






    path('customer-order-detail/<int:id>',views.order_detail,name='customer_order_detail'),
    path('order-list',views.order_list,name='client_order_list'),
    path('order-list-test',views.order_list_test,name='client_order_list_test'),
    path('get-sapcodes',views.get_sapcodes,name='get_sapcodes_for_client'),
    path('get-sapcodes-pvc',views.get_sapcodes_pvc,name='get_sapcodes_pvc'),


   
    path('check',views.test,name='test')
]