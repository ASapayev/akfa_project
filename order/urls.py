
from django.urls import path
from . import views

urlpatterns = [
    #aluminiy
    path('aluminiy-zayavki',views.index,name='order'),
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
    ]