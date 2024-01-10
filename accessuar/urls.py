from django.urls import path,re_path
from . import views
from aluminiy import views as aluview
from aluminiytermo import views as alutermoview

urlpatterns = [
    path('upload-norma',views.full_update_norm,name='full_update_norm_accessuar'), 
    path('get-norma',views.get_accessuar_sapcode,name='get_accessuar_sapcode'), 

]

