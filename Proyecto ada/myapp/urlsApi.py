from rest_framework import routers
from .viewsets import EstacionViewSet
from django.urls import path

from .views import check_mantenimiento_post, estaciones_mantenimiento_reciente

router = routers.SimpleRouter()
router.register('estaciones', EstacionViewSet)
#router.register('mediciones', MedicionViewSet)

urlpatterns = [
    path('checkMantenimiento/', check_mantenimiento_post, name='check-mantenimiento-post'),
    path('checkMantenimientoReciente/', estaciones_mantenimiento_reciente, name='check-mantenimiento-reciente'),
]

urlpatterns += router.urls
