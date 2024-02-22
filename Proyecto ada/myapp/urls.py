from django.urls import path, include
from . import views
from .views import check_mantenimiento_post

urlpatterns = [
    #VISTAS
    path('', views.index),
    
    path('listaEstaciones/', views.EstacionesView.as_view(),name='lista de estaciones'),
    #path('listaMediciones/', views.MedicionesView.as_view(),name='lista de mediciones'),
    
    path('graficos/<int:id>',views.graficos),
    #path('datos_graficos/<int:id>', views.datos_graficos , name='myChart'),
    #path('datos_graficos1/<int:id>', views.datos_graficos1 , name='myChart2'),
    
    #path('mediciones/<int:id>', views.mostrarMediciones),
    
    #Leafllet map
    path('mapakml/', views.mapakml),
    
    path('exito/', views.contacto),

    path('login/', views.login),
    path('signup/', views.signup, name='signup'),
    path('contacto/', views.contacto),

    #CONTROLLER 
    path('crearUsuario/', views.crearUsuario, name='crearUsuario'),
    #TOKEN
    path('getcsrf', views.getcsrf, name='getcsrf'),

    # API
    path('api/', include('myapp.urlsApi')), 
]
