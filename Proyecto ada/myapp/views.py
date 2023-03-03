import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Estacion, Medicion
from django.views import View




# Create your views here.

def index(request):
    return render(request, 'index.html')


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