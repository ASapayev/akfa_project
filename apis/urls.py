from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet, basename='profiles')
router.register(r'alu-razlovka-simple-1101', views.RazlovkaAluSimple1101ViewSet, basename='alu_razlovka_simple_1101')
router.register(r'alu-razlovka-simple-1201', views.RazlovkaAluSimple1201ViewSet, basename='alu_razlovka_simple_1201')
router.register(r'alu-razlovka-termo-1101', views.RazlovkaAluTermo1101ViewSet, basename='alu_razlovka_termo_1101')
router.register(r'alu-razlovka-termo-1201', views.RazlovkaAluTermo1201ViewSet, basename='alu_razlovka_termo_1201')
router.register(r'ves-profiles', views.LengthProfileViewSet, basename='ves_profiles')
router.register(r'master-group', views.MasterGroupViewSet, basename='master_group')
router.register(r'buxgalter-nazvaniye', views.BuxgalterNazvaniyeViewSet, basename='buxgalter_nazvaniye')
urlpatterns = router.urls
