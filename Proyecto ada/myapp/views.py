from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.db.models import Sum

from datetime import datetime, timedelta

### MODELS ###
from .models import Estacion, Contacto, EstadoMantenimiento

### FORMS ###
from .forms import LoginForm  # Ajusta esto según tu estructura de archivos
from .forms import FormularioContacto

#API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#RESPONSES
from django.http import JsonResponse
import json

#TOKEN  
from django.contrib.auth.models import Usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

### HOME ###

def index(request):
    return render(request, 'index.html')

### LOGIN ###

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, 'index.html')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

### SIGNUP ###

def signup(request):
    if request.method == 'POST':
        data = request.POST
        print(data)  
        return JsonResponse({'message': 'Registro exitoso'})  
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)  

### CONTACTO ###
def contacto(request):
    if request.method== "POST":
        formulario=FormularioContacto(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            contactoParaGuardar=Contacto(asunto=informacion['asunto'],nombre=informacion['nombre'],localidad=informacion['localidad'],partido=informacion['partido'],email=informacion['email'],telefono=informacion['telefono'],mensaje=informacion['mensaje'])
            contactoParaGuardar.transformador()
            contactoParaGuardar.save()
            return render(request, 'exito.html')
    else:
        formulario=FormularioContacto()
    return render(request,'contacto.html',{"form":formulario})


### EMA'S ###
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
    """
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
"""


### GRAFICOS ###
def graficos(request, id):
    return render(request, 'graficos.html',{"id":str(id)})
"""
def datos_graficos(request, id):
    labels = []
    data = []

    queryset = Medicion.objects.filter(estacion_id=id).values('fecha').annotate(temita=Sum('tmax')).order_by('fecha')
    for entry in queryset:
        labels.append(entry['fecha'])
        data.append(entry['temita'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
"""
"""
def datos_graficos(request):
    labels = []
    data = []

    queryset = Medicion.objects.values('fecha').annotate(tmedia=Sum('tmax')).order_by('fecha')
    for entry in queryset:
        labels.append(entry['fecha'])
        data.append(entry['tmax'])
    #print(labels)
    print(data)
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })    

    queryset = Medicion.objects.order_by('fecha')
    for medicion in queryset:
        labels.append(medicion.fecha)
        data.append(medicion.tmedia)

    return render(request, 'graficos.html', {
        'labels': labels,
        'data': data,
    })
"""


#esto se utiliza para mostrar las mediciones de una estacion en particular (si tiene)
"""
def mostrarMediciones(request, id):
    mediciones=Medicion.objects.filter(estacion_id=id).order_by('fecha')
    return render(request, 'mediciones.html',{"mediciones":mediciones}) 
"""
def mapakml(request):
    return render(request, 'mapakml.html')


# def datos_graficos1(request, id):
#     labels = []
#     data = []

#     queryset = Medicion.objects.filter(estacion_id=id).values('fecha').annotate(temita=Sum('pp_mm')).order_by('fecha')
#     for entry in queryset:
#         labels.append(entry['fecha'])
#         data.append(entry['temita'])

#     return JsonResponse(data={
#         'labels': labels,
#         'data': data,
#     })


### MANTENIMIENTO ###



### API ###

@api_view(['POST'])
def check_mantenimiento_post(request):
    id_estacion = request.data.get('idEstacion', None)

    if id_estacion is not None:
        try:
            estacion = Estacion.objects.get(id=id_estacion)
            mantenimiento = estacion.estado_mantenimiento
            
            response_data = {
                'nombre': estacion.nombre,
                'ultimo_mantenimiento': estacion.ultimo_mantenimiento,
                'estado_mantenimiento_id': mantenimiento.id,
                'estado_mantenimiento': mantenimiento.nombre,  
            }

            return Response(response_data)
        except Estacion.DoesNotExist:
            return Response({'error': 'Estación no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        except EstadoMantenimiento.DoesNotExist:
            return Response({'error': 'Mantenimiento no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'Se requiere el parámetro idEstacion'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def estaciones_mantenimiento_reciente(request):
    
    fecha_actual = datetime.now()
    fecha_hace_tres_meses = fecha_actual - timedelta(days=90)
    # estaciones_recientes = Estacion.objects.filter(ultimo_mantenimiento__gte=fecha_hace_tres_meses) # mayor igual
    estaciones_recientes = Estacion.objects.filter(ultimo_mantenimiento__lte=fecha_hace_tres_meses) # menor igual

    resultados = [
        {
            'nombre': estacion.nombre,
            'ultimo_mantenimiento': estacion.ultimo_mantenimiento,
            'estado_mantenimiento': estacion.estado_mantenimiento.nombre,
        }
        for estacion in estaciones_recientes
    ]

    return Response(resultados)