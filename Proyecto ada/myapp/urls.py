from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('listaEstaciones/', views.EstacionesView.as_view(),name='lista de estaciones'),
    path('listaMediciones/', views.MedicionesView.as_view(),name='lista de mediciones'),
    path('contacto/', views.contacto),
    path('datos_graficos/', views.datos_graficos , name='myChart'),
    path('graficos/',views.graficos),
    path('exito/', views.contacto),
    path('mediciones/<int:id>', views.mostrarMediciones),
]
