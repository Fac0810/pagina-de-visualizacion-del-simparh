from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index),
    path('ListaEstaciones/', views.EstacionesView.as_view(),name='lista de estaciones'),
    path('ListaMediciones/', views.MedicionesView.as_view(),name='lista de mediciones'),
    path('Contacto/', views.contacto),
    path('Graficos/', views.Graficos),
    
]
