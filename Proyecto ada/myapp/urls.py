from django.urls import path, include
from . import views
from .views import check_mantenimiento_post

DEVELOPMENT_URL = 'http://127.0.0.1:8000/'
PRODUCTION_URL = 'https://url-de-produccion.com/'

urlpatterns = [
    path('', views.index),
    path('listaEstaciones/', views.EstacionesView.as_view(),name='lista de estaciones'),
    #path('listaMediciones/', views.MedicionesView.as_view(),name='lista de mediciones'),
    path('contacto/', views.contacto),
    path('login/', views.login),
    #path('datos_graficos/<int:id>', views.datos_graficos , name='myChart'),
    #path('datos_graficos1/<int:id>', views.datos_graficos1 , name='myChart2'),
    path('graficos/<int:id>',views.graficos),
    path('exito/', views.contacto),
    #path('mediciones/<int:id>', views.mostrarMediciones),
    path('mapakml/', views.mapakml),

    # API
    path('api/', include('myapp.urlsApi')),
]
