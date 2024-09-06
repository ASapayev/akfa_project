from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet, basename='profiles')
router.register(r'ves-profiles', views.LengthProfileViewSet, basename='ves_profiles')
router.register(r'master-group', views.MasterGroupViewSet, basename='master_group')
router.register(r'buxgalter-nazvaniye', views.BuxgalterNazvaniyeViewSet, basename='buxgalter_nazvaniye')
urlpatterns = router.urls
