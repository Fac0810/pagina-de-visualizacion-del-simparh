#se usa para traer los datos de las API
from rest_framework import viewsets
from .models import Estacion, MedicionPluviometrica
from .serializer import EstacionSerializer, MedicionPluviometricaSerializer

class EstacionViewSet(viewsets.ModelViewSet):
    queryset = Estacion.objects.all()
    serializer_class = EstacionSerializer

    #para terminar rapido con el refactoring se va a tomar Medicion = MedicionPluviometrica


class MedicionPluviometricaViewSet(viewsets.ModelViewSet):
    queryset = MedicionPluviometrica.objects.all()
    serializer_class = MedicionPluviometricaSerializer



