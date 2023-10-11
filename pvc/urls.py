
from django.urls import path
from . import views

urlpatterns = [
    path('upload-product-pvc-org',views.upload_product_org,name='upload_product_pvc_org'),
    path('upload-product-pvc-detail/<int:id>',views.product_add_second_org,name='upload_product_pvc__detail_org'),

    ]