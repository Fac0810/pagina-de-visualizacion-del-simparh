from django.shortcuts import render
from django.http import JsonResponse
from .models import Estacion, Medicion, Contacto
from django.views import View
from .forms import FormularioContacto
from django.db.models import Sum





# Create your views here.

def index(request):
    return render(request, 'index.html')

#Se utiliza para el fromulario de contacto
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

def graficos(request, id):
    return render(request, 'graficos.html',{"id":str(id)})

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
def mostrarMediciones(request, id):
    mediciones=Medicion.objects.filter(estacion_id=id).order_by('fecha')
    return render(request, 'mediciones.html',{"mediciones":mediciones}) 

def mapakml(request):
    return render(request, 'mapakml.html')
