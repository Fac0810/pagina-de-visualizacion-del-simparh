import json
from django import forms
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from .models import Estacion, Medicion, Contacto
from .models import Asunto
from django.views import View





# Create your views here.

def index(request):
    return render(request, 'index.html')

def contacto(request):
    asunto = Asunto.objects.values()
    return render(request, 'contacto.html', {'asunto':asunto})

# Hago el json de las estaciones 
class EstacionesView(View):
    def get(self, request):
        estaciones = list(Estacion.objects.values())
        if len(estaciones) > 0:
            datos={'estaciones':estaciones}
        else:
            datos={'message':"estaciones not found..."}
        return JsonResponse(datos)
    def post(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass
# Hago el json de las mediciones 
class MedicionesView(View):
    def get(self, request):
        mediciones = list(Medicion.objects.values())
        if len(mediciones) > 0:
            datos={'mediciones':mediciones}
        else:
            datos={'message':"estaciones not found..."}
        return JsonResponse(datos)
    def post(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass


def Graficos(request):
    return render(request, 'prueba.html')
