from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from .models import Estacion, Asunto, Contacto

# Register your models here.
# Se utiliza para mostrar y tener registro sobre los distintos elementos de la base de datos.
# Si se utiliza "list_ display" se mostraran estos atributos en un listado.
"""
@admin.register(Estacion)
class EstacionAdmin(admin.ModelAdmin):
    list_display = (
        'estacion',
        'nombre',
        'ubicacion',
        'fuente',
    )
    """
"""
class MedicionesResources(resources.ModelResource):
    fields = (
        'estacion',
        'fecha',
        'tmax',
        'tmin',
        'pp_mm',
    )
    class Meta:
        model = Medicion
    
@admin.register(Medicion)
class EstacionAdmin(ImportExportModelAdmin):
    resource_class = MedicionesResources
    list_display = (
        'estacion',
        'fecha',
        'tmax',
        'tmin',
        'pp_mm',
    )
"""
admin.site.register(Asunto)
admin.site.register(Contacto)
