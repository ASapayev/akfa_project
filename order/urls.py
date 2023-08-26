
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='order'),
    path('order-detail/<int:id>',views.order_detail,name='order_detail'),
    path('order-delete/<int:id>',views.order_delete,name='order_delete')
    ]