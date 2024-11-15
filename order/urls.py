
from django.urls import path
from . import views

urlpatterns = [
    #aluminiy
    path('aluminiy-zayavki',views.index,name='order'),
    path('aluminiy-zayavki-zavod',views.index_zavod,name='order_zavod_alum'),
    path('order-detail-zavod/<int:id>',views.order_detail_zavod,name='order_detail_zavod'),
    path('order-detail/<int:id>',views.order_detail,name='order_detail'),
    path('order-delete/<int:id>',views.order_delete,name='order_delete'),
    path('order-status/<int:id>',views.status_change_to_done,name ='status_change_to_done'),



    #pvc
    path('order-pvc',views.index_pvc,name='order_pvc'),
    path('order-pvc-delete/<int:id>',views.order_delete_pvc,name='order_delete_pvc'),
    path('order-detail-pvc/<int:id>',views.order_detail_pvc,name='order_detail_pvc'),
    path('order-status-pvc/<int:id>',views.status_change_to_done_pvc,name ='status_change_to_done_pvc'),
    
    #radiator
    path('order-radiator',views.index_radiator,name='order_radiator'),
    path('order-radiator-delete/<int:id>',views.order_delete_radiator,name='order_delete_radiator'),
    path('order-detail-radiator/<int:id>',views.order_detail_radiator,name='order_detail_radiator'),
    path('order-status-radiator/<int:id>',views.status_change_to_done_radiator,name ='status_change_to_done_radiator'),
    
    #accessuar
    path('order-accessuar',views.index_accessuar,name='order_accessuar'),
    path('order-accessuar-delete/<int:id>',views.order_delete_accessuar,name='order_delete_accessuar'),
    path('order-detail-accessuar/<int:id>',views.order_detail_accessuar,name='order_detail_accessuar'),
    path('order-status-accessuar/<int:id>',views.status_change_to_done_accessuar,name ='status_change_to_done_accessuar'),
    
    #akp
    path('order-akp',views.index_akp,name='order_akp'),
    path('order-akp-delete/<int:id>',views.order_delete_akp,name='order_delete_akp'),
    path('order-detail-akp/<int:id>',views.order_detail_akp,name='order_detail_akp'),
    path('order-status-akp/<int:id>',views.status_change_to_done_akp,name ='status_change_to_done_akp'),
    
    #prochiye
    path('order-prochiye',views.index_prochiye,name='order_prochiye'),
    path('order-prochiye-delete/<int:id>',views.order_delete_prochiye,name='order_delete_prochiye'),
    path('order-detail-prochiye/<int:id>',views.order_detail_prochiye,name='order_detail_prochiye'),
    path('order-status-prochiye/<int:id>',views.status_change_to_done_prochiye,name ='status_change_to_done_prochiye'),


    #kraska
    path('order-kraska',views.index_kraska,name='order_client_kraska'),
    path('order-detail-kraska/<int:id>',views.order_detail_kraska,name='order_detail_kraska'),
    path('order-kraska-delete/<int:id>',views.order_delete_radiator,name='order_delete_kraska'),

    ##### epdm 
    path('order-epdm',views.index_epdm,name='order_client_epdm'),
    path('order-detail-epdm/<int:id>',views.order_detail_epdm,name='order_detail_epdm'),
    path('order-epdm-delete/<int:id>',views.order_delete_epdm,name='order_delete_epdm'),

    ]