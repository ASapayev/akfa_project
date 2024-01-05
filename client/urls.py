from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='client_index'),
    path('shablon-imzo-detail',views.shablon_imzo_detail,name='shablon_imzo_detail'),
    path('shablon-savdo-detail',views.shablon_savdo_detail,name='shablon_savdo_detail'),
    path('shablon-export-detail',views.shablon_export_detail,name='shablon_export_detail'),
    path('shablon-pvc-imzo-detail',views.shablon_pvc_export_detail,name='shablon_pvc_export_detail'),
    path('shablon-pvc-savdo-detail',views.shablon_pvc_savdo_detail,name='shablon_pvc_savdo_detail'),
    path('shablon-pvc-export-detail',views.shablon_pvc_export_savdo_detail,name='shablon_pvc_export_savdo_detail'),

    ################## APIS ################
    path('imzo-artikul-list',views.imzo_artikul_list,name='imzo_artikul_list'),
    path('nakleyka-list',views.nakleyka_list,name='nakleyka_list'),

    path('anod-list',views.anod_list,name='anod_list'),
    
]