from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet, basename='profiles')
router.register(r'ves-profiles', views.LengthProfileViewSet, basename='ves_profiles')
urlpatterns = router.urls
