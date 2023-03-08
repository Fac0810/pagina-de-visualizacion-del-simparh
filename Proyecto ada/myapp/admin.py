from django.contrib import admin
from .models import Estacion, Medicion, Asunto, Contacto

# Register your models here.
admin.site.register(Estacion)
admin.site.register(Medicion)
admin.site.register(Asunto)
admin.site.register(Contacto)
