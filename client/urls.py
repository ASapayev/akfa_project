from django.urls import path,include
from . import views

urlpatterns = [
    path('index',views.index,name='client_index'),
    ######Aluminiy############
    path('shablon-imzo-detail',views.shablon_imzo_detail,name='shablon_imzo_detail'),
    path('shablon-savdo-detail',views.shablon_savdo_detail,name='shablon_savdo_detail'),
    path('shablon-export-detail',views.shablon_export_detail,name='shablon_export_detail'),

    ######PVC############
    path('shablon-pvc-imzo-detail',views.shablon_pvc_export_detail,name='shablon_pvc_export_detail'),
    path('shablon-pvc-savdo-detail',views.shablon_pvc_savdo_detail,name='shablon_pvc_savdo_detail'),
    path('shablon-pvc-export-detail',views.shablon_pvc_export_savdo_detail,name='shablon_pvc_export_savdo_detail'),

    ######Accessuar############
    path('shablon-acs-imzo-detail',views.shablon_acs_export_detail,name='shablon_acs_imzo_detail'),
    path('shablon-acs-savdo-detail',views.shablon_acs_savdo_detail,name='shablon_acs_savdo_detail'),
    path('shablon-acs-export-detail',views.shablon_acs_export_savdo_detail,name='shablon_acs_export_savdo_detail'),


    ######AKP###############
    path('shablon-akp-savdo-detail',views.shablon_akp_savdo_detail,name='shablon_akp_savdo_detail'),

    ################## APIS ################
    path('imzo-artikul-list',views.imzo_artikul_list,name='imzo_artikul_list'),
    path('pvc-artikul-list',views.pvc_artikul_list,name='pvc_artikul_list'),
    path('nakleyka-list',views.nakleyka_list,name='nakleyka_list'),
    path('nakleyka-list-pvc',views.nakleyka_list_pvc,name='nakleyka_list_pvc'),

    path('client-anod-list',views.anod_list,name='client_anod_list'),

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
    path('detail-order-update/<int:id>',views.detail_order_update,name='detail_order_update'),
    path('order-update-all/<int:id>',views.order_update_all,name='order_update_all'),
    path('order-update/<int:id>',views.order_update,name='order_update'),
    path('customer-order-detail/<int:id>',views.order_detail,name='customer_order_detail'),
    path('order-list',views.order_list,name='client_order_list'),
    path('get-sapcodes',views.get_sapcodes,name='get_sapcodes_for_client'),
    path('get-sapcodes-pvc',views.get_sapcodes_pvc,name='get_sapcodes_pvc'),


   
    path('check',views.test,name='test')
]