from rest_framework import routers
from .viewsets import EstacionViewSet, MedicionPluviometricaViewSet

router = routers.SimpleRouter()
router.register('estaciones', EstacionViewSet)
router.register('mediciones_pluviometricas', MedicionPluviometricaViewSet)

urlpatterns = router.urls