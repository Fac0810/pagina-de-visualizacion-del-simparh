#se usa para traer los datos de las API
from rest_framework import viewsets
from .models import Estacion, Medicion
from .serializer import EstacionSerializer, MedicionSerializer

class EstacionViewSet(viewsets.ModelViewSet):
    queryset = Estacion.objects.all()
    serializer_class = EstacionSerializer

class MedicionViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer