from django.shortcuts import render
from django.http import JsonResponse
from .models import Estacion, Contacto, MedicionPluviometrica
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

class MedicionPluviometricaView(View):
    def get(self, request):
        mediciones = list(MedicionPluviometrica.objects.values())
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


def datos_graficos_pluviometricos(request, id):
# Es especifico de la estacion que se pasa por "id".
    labels = []
    data = []

    queryset = MedicionPluviometrica.objects.filter(estacion_id=id).values('fecha_hora').annotate(temita=Sum('tmax')).order_by('fecha_hora')
    for entry in queryset:
        labels.append(entry['fecha_hora'])
        data.append(entry['temita'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def datos_graficos(request):
# No es especifico de una estación.
    labels = []
    data = []

    queryset = MedicionPluviometrica.objects.values('fecha_hora').annotate(tmedia=Sum('tmax')).order_by('fecha_hora')
    for entry in queryset:
        labels.append(entry['fecha_hora'])
        data.append(entry['tmax'])
    #print(labels)
    print(data)
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })    

"""
# probar si se puede borrar
    queryset = Medicion.objects.order_by('fecha_hora')
    for medicion in queryset:
        labels.append(medicion.fecha_hora)
        data.append(medicion.tmedia)

    return render(request, 'graficos.html', {
        'labels': labels,
        'data': data,
    })
"""


#esto se utiliza para mostrar las mediciones de una estacion en particular (si tiene)

def mostrarMedicionPluviometrica(request, id):
    mediciones=MedicionPluviometrica.objects.filter(estacion_id=id).order_by('fecha_hora')
    return render(request, 'mediciones.html',{"mediciones":mediciones}) 

def mapakml(request):
    return render(request, 'mapakml.html')

# Esto lo había hecho seba en su momento, se deberia arreglar para que sea estandar con los ottros mostrar graficos
def datos_graficos1(request, id):
    labels = []
    data = []

    queryset = MedicionPluviometrica.objects.filter(estacion_id=id).values('fecha_hora').annotate(temita=Sum('pp_mm')).order_by('fecha_hora')
    for entry in queryset:
        labels.append(entry['fecha_hora'])
        data.append(entry['temita'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
