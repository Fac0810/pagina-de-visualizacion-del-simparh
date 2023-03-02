from django.contrib import admin
from .models import Estacion, Medicion, Prueba



# Register your models here.
admin.site.register(Estacion)
admin.site.register(Medicion)
admin.site.register(Prueba)