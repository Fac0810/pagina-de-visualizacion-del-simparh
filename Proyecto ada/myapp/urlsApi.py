from rest_framework import routers
from .viewsets import EstacionViewSet, MedicionViewSet, AsuntoViewSet, ContactoViewSet

router = routers.SimpleRouter()
router.register('estaciones', EstacionViewSet)
router.register('mediciones', MedicionViewSet)
router.register('asuntos', AsuntoViewSet)
router.register('contactos', ContactoViewSet)

urlpatterns = router.urls