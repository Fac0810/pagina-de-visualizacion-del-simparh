from django.shortcuts import render
from django.views import View
from django.db.models import Sum

# ENVIRONMENT
from django.conf import settings

### MODELS ###
from .models import Estacion, Contacto, EstadoMantenimiento, Usuario

### FORMS ###
from .forms import LoginForm
from .forms import FormularioContacto

# API
from rest_framework.decorators import api_view
from rest_framework import status

# RESPONSE API
from rest_framework.response import Response

# TOKEN
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.middleware.csrf import get_token

# RESPONSE
from django.http import JsonResponse, HttpResponse, HttpResponseServerError
from django.contrib import messages

# EXCEPTIONS
from django.db import IntegrityError
from django.core.exceptions import ValidationError

# VALIDATIONS
import re
from django.core.validators import validate_email

# HASH
from django.contrib.auth.hashers import make_password

# DECORATORS
from django.views.decorators.http import require_POST

from datetime import datetime, timedelta


### HOME ###
def index(request):
    return render(request, "index.html")


### LOGIN ###
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, "index.html")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


### SIGNUP ###
def signup(request):
    return render(request, "signup.html")


def validar_datos_registro(username, nombre, apellido, email, password):
    # Validación de username
    if not re.match(r"^[a-zA-Z0-9]+$", username):
        return "El nombre de usuario debe ser alfanumérico sin espacios"

    # Validación de nombre y apellido
    if not re.match(r"^[a-zA-Z]+$", nombre):
        return "El nombre debe contener solo letras"

    if not re.match(r"^[a-zA-Z]+$", apellido):
        return "El apellido debe contener solo letras"

    # Validación de email
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        return "Ingrese un email válido"

    # Validación de password
    if not re.match(r'^[a-zA-Z0-9!@#$%^&*()_+=\-[\]{};:\'",.<>/?]+$', password):
        return "La contraseña debe ser alfanumérica con símbolos sin espacios"

    if len(password) < 8:
        return "La contraseña debe tener al menos 8 caracteres"

    if len(password) > 15:
        return "La contraseña debe tener menos de 15 caracteres"

    return None


@csrf_protect
@require_POST
def crearUsuario(request):
        try:
            nombre_usuario = request.POST.get("nombreUsuario")
            nombre = request.POST.get("nombre")
            apellido = request.POST.get("apellido")
            email = request.POST.get("email")
            password = request.POST.get("password")
            

            # Validación
            error_message = validar_datos_registro(
                nombre_usuario, nombre, apellido, email, password
            )
            if error_message:
                messages.error(request, error_message)
                return JsonResponse({"error": error_message}, status=400)

            if (
                Usuario.objects.filter(nombre_usuario=nombre_usuario).exists()
                or Usuario.objects.filter(email=email).exists()
            ):
                messages.error(request, "El usuario o email ya existen")
                return JsonResponse(
                    {"error": "El usuario o email ya existen"}, status=400
                )

            usuario = Usuario.objects.create(
                username=username,
                nombre=nombre,
                apellido=apellido,
                email=email,
                password=make_password(password),
                superuser=False,
                activo=True,
                tipo_usuario_id=1,
                fecha_inicio = datetime.now(),
                ultima_conexion = datetime.now(),
                
            )
            usuario.save()
            return JsonResponse({"message": "Usuario creado correctamente"}, status=201)

        except IntegrityError:
            return JsonResponse({"error": "El usuario o email ya existen"}, status=500)

        except ValidationError as e:
            return JsonResponse({"error": e.message}, status=400)





### TOKEN ###
# OBTENCION DE TOKEN CSRF
@csrf_exempt
def getcsrf(request):
    try:
        csrf_token = get_token(request)
        return JsonResponse({"csrfToken": csrf_token})
    except Exception as e:
        return HttpResponseServerError(
            "Error al obtener el token CSRF: {}".format(str(e))
        )


### CONTACTO ###
def contacto(request):
    if request.method == "POST":
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            contactoParaGuardar = Contacto(
                asunto=informacion["asunto"],
                nombre=informacion["nombre"],
                localidad=informacion["localidad"],
                partido=informacion["partido"],
                email=informacion["email"],
                telefono=informacion["telefono"],
                mensaje=informacion["mensaje"],
            )
            contactoParaGuardar.transformador()
            contactoParaGuardar.save()
            return render(request, "exito.html")
    else:
        formulario = FormularioContacto()
    return render(request, "contacto.html", {"form": formulario})


### EMA'S ###
# Hago el json de las estaciones
class EstacionesView(View):
    def get(self, request):
        estaciones = list(Estacion.objects.values())
        if len(estaciones) > 0:
            datos = {"estaciones": estaciones}
        else:
            datos = {"message": "estaciones not found..."}
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
    return render(request, "graficos.html", {"id": str(id)})


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


# esto se utiliza para mostrar las mediciones de una estacion en particular (si tiene)
"""
def mostrarMediciones(request, id):
    mediciones=Medicion.objects.filter(estacion_id=id).order_by('fecha')
    return render(request, 'mediciones.html',{"mediciones":mediciones}) 
"""


def mapakml(request):
    return render(request, "mapakml.html")


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


@api_view(["POST"])
def check_mantenimiento_post(request):
    id_estacion = request.data.get("idEstacion", None)

    if id_estacion is not None:
        try:
            estacion = Estacion.objects.get(id=id_estacion)
            mantenimiento = estacion.estado_mantenimiento

            response_data = {
                "nombre": estacion.nombre,
                "ultimo_mantenimiento": estacion.ultimo_mantenimiento,
                "estado_mantenimiento_id": mantenimiento.id,
                "estado_mantenimiento": mantenimiento.nombre,
            }

            return Response(response_data)
        except Estacion.DoesNotExist:
            return Response(
                {"error": "Estación no encontrada"}, status=status.HTTP_404_NOT_FOUND
            )
        except EstadoMantenimiento.DoesNotExist:
            return Response(
                {"error": "Mantenimiento no encontrado"},
                status=status.HTTP_404_NOT_FOUND,
            )
    else:
        return Response(
            {"error": "Se requiere el parámetro idEstacion"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
def estaciones_mantenimiento_reciente(request):

    fecha_actual = datetime.now()
    fecha_hace_tres_meses = fecha_actual - timedelta(days=90)
    # estaciones_recientes = Estacion.objects.filter(ultimo_mantenimiento__gte=fecha_hace_tres_meses) # mayor igual
    estaciones_recientes = Estacion.objects.filter(
        ultimo_mantenimiento__lte=fecha_hace_tres_meses
    )  # menor igual

    resultados = [
        {
            "nombre": estacion.nombre,
            "ultimo_mantenimiento": estacion.ultimo_mantenimiento,
            "estado_mantenimiento": estacion.estado_mantenimiento.nombre,
        }
        for estacion in estaciones_recientes
    ]

    return Response(resultados)
