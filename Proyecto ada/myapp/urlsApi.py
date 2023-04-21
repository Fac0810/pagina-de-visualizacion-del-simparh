from rest_framework import routers
from .viewsets import EstacionViewSet, MedicionViewSet

router = routers.SimpleRouter()
router.register('estaciones', EstacionViewSet)
router.register('mediciones', MedicionViewSet)

urlpatterns = router.urls