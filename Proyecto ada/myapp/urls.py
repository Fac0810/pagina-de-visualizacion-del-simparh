from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index),
    path('ListaEstaciones/', views.EstacionesView.as_view(),name='lista de estaciones'),
   
]
