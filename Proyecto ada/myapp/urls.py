from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index),
    path('listaEstaciones/', views.EstacionesView.as_view(),name='lista de estaciones'),
    path('listaMediciones/', views.MedicionesView.as_view(),name='lista de mediciones'),
    path('contacto/', views.contacto),
    path('graficos/', views.graficos),
    path('exito/', views.contacto),
    
]
