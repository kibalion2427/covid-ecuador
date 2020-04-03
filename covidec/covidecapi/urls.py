from django.urls import include,path
from .views import PaisViewSet,ProvinciaViewSet,CovidCaseViewSet,ProvinceHistoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('pais',PaisViewSet,basename='pais')
router.register('provincia',ProvinciaViewSet,basename='provincia')
router.register('covid',CovidCaseViewSet,basename='covid')
router.register('history',ProvinceHistoryViewSet,basename='history')
urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/covid/<int:fk_pais>/<int:fk_provincia>/',CovidCaseViewSet)
]
