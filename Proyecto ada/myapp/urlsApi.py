from rest_framework import routers
from .viewsets import EstacionViewSet, MedicionViewSet, AsuntoViewSet

router = routers.SimpleRouter()
router.register('estaciones', EstacionViewSet)
router.register('mediciones', MedicionViewSet)
router.register('asuntos', AsuntoViewSet)

urlpatterns = router.urls