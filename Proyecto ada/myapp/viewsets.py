#se usa para traer los datos de las API
from rest_framework import viewsets
from .models import Estacion, Medicion, Asunto
from .serializer import EstacionSerializer, MedicionSerializer, AsuntoSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

class EstacionViewSet(viewsets.ModelViewSet):
    queryset = Estacion.objects.all()
    serializer_class = EstacionSerializer

class MedicionViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer

class AsuntoViewSet(viewsets.ModelViewSet):
    queryset = Asunto.objects.all()
    serializer_class = AsuntoSerializer


#Funcionalidades Api especificas


