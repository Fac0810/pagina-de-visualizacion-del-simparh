#se usa para traer los datos de las API
from rest_framework import viewsets
from .models import Estacion, Medicion, Asunto, Contacto
from .serializer import EstacionSerializer, MedicionSerializer, AsuntoSerializer, ContactoSerializer

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

class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

#Funcionalidades Api especificas


