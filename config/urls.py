from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
import django_eventstream
# from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('',include('main.urls')),
    path('texcart/',include('imzo.urls')),
    path('alu/',include('aluminiy.urls')),
    path('termo/',include('aluminiytermo.urls')),
    path('norma/',include('norma.urls')),
    path('norma-benkam/',include('normabenkam.urls')),
    path('order/',include('order.urls')),
    path('pvc/',include('pvc.urls')),
    path('online-savdo/',include('onlinesavdo.urls')),
    path('client/',include('client.urls')),
    path('accessuar/',include('accessuar.urls')),
    path('accessuar-import/',include('accessuar_import.urls')),
    path('radiator/',include('radiator.urls')),
    path('api/v1/',include('apis.urls')),
    

   path("events/", include(django_eventstream.urls), {"channels": ["orders"]}),
    # path('__debug__/', include('debug_toolbar.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# if settings.DEBUG:
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler404 = 'aluminiy.views.handler404'
