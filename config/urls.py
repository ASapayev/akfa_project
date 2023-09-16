from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
# from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('',include('main.urls')),
    path('texcart/',include('imzo.urls')),
    path('alu/',include('aluminiy.urls')),
    path('termo/',include('aluminiytermo.urls')),
    path('norma/',include('norma.urls')),
    path('order/',include('order.urls')),
    path('pvc/',include('pvc.urls')),
    
    # path('__debug__/', include('debug_toolbar.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# if settings.DEBUG:
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler404 = 'aluminiy.views.handler404'
