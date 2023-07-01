from django.urls import path,re_path,include
from . import views 

urlpatterns = [
    # path('', views.myAccount),
    # path('registerVendor',views.registerVendor,name='registerVendor'),
    path('registerUser',views.registerUser,name='registerUser'),

    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    # path('myAccount/',views.myAccount,name='myAccount'),
    # path('customerDashboard/',views.customerDashboard,name='customerDashboard'),
    # path('vendorDashboard/',views.vendorDashboard,name='vendorDashboard'),

    # path('activate/<uidb64>/<token>/', views.activate,name='activate'),

    
    # path('forgot_password/',views.forgot_password,name='forgot_password'),
    # path('reset_password_validate/<uidb64>/<token>/',views.reset_password_validate,name='reset_password_validate'),
    # path('reset_password/',views.reset_password,name='reset_password'),

   
    
]