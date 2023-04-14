from rest_framework import routers
from .viewsets import EstacionViewSet

router = routers.SimpleRouter()
router.register('estaciones', EstacionViewSet)

urlpatterns = router.urls