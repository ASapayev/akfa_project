from django.urls import path,re_path
from . import views

urlpatterns = [
 path('norma-base',views.norma_excel,name='norma_excel')
]