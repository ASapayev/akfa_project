
from django.urls import path
from . import views

urlpatterns = [
    path('upload-product-pvc-org',views.upload_product_org,name='upload_product_pvc_org'),
    path('upload-product-pvc-detail/<int:id>',views.product_add_second_org,name='upload_product_pvc__detail_org'),
    path('upload-char-pvc',views.upload_product_char_pvc,name='upload_char_pvc'),
    path('update-char-title-org/<int:id>',views.update_char_title_pvc,name='update_char_title_org_pvc'),
   
    ]