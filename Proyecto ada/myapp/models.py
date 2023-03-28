from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


#creamos los modelos de las clases que necesitamos para trabajar el mapa



class Estacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    estacion = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100, null=True)
    ubicacion = models.CharField(max_length=100, null=True)
    desde = models.DateField(null=True)
    hasta = models.DateField(null=True)
    fuente = models.CharField(max_length=10, null=True)
    longitud = models.DecimalField(max_digits=15,decimal_places=12, null=True, blank=True)
    latitud = models.DecimalField(max_digits=15,decimal_places=12, null=True, blank=True)


    def __str__(self):
        return self.nombre


 
class Medicion(models.Model):
    id = models.BigAutoField(primary_key=True)
    estacion = models.CharField(max_length=100, default="0000")
    fecha = models.DateField(null=True, blank=True)
    tmax = models.DecimalField(max_digits=5,decimal_places=3, null=True, blank=True)
    tmin = models.DecimalField(max_digits=5,decimal_places=3, null=True, blank=True)
    tmedia = models.DecimalField(max_digits=5,decimal_places=3, null=True, blank=True)
    pp_mm = models.DecimalField(max_digits=7,decimal_places=3, null=True, blank=True)
    heliofania = models.DecimalField(max_digits=10,decimal_places=6, null=True, blank=True)
    viento_max_direccion = models.DecimalField(max_digits=5,decimal_places=3, null=True, blank=True)
    viento_max_intensidad = models.DecimalField(max_digits=5,decimal_places=3, null=True, blank=True)
    viento_medi = models.DecimalField(max_digits=5,decimal_places=3, null=True, blank=True)
    temp_rocio_media = models.DecimalField(max_digits=5,decimal_places=3, null=True, blank=True)
    presion_nivel_estacion = models.DecimalField(max_digits=10,decimal_places=5, null=True, blank=True)
    humedad_relativa = models.DecimalField(max_digits=10,decimal_places=5, null=True, blank=True)
    cant_datos_promedio = models.DecimalField(max_digits=5,decimal_places=3, null=True, blank=True)
    estacion_id = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1)
    
    

    def __str__(self):
        return 'Medicion de '+ self.estacion + ' en la fecha ' + str(self.fecha)
    


class Asunto(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.CharField(max_length=100, null=False)
   
    def __str__(self):
        return self.tipo
    



class Contacto(models.Model):
    id = models.BigAutoField(primary_key=True)
    asunto = models.ForeignKey(Asunto, on_delete=models.CASCADE, blank=False)
    nombre = models.CharField(max_length=100, null=True, blank=False)
    localidad= models.CharField(max_length=100, null=True, blank=False)
    partido= models.CharField(max_length=100, null=True, blank=False)
    email = models.EmailField(max_length=100, null=True, blank=False)
    telefono = PhoneNumberField(null =True, blank=False)
    mensaje = models.TextField(null =True, blank=False)

    def __str__(self):
        return self.nombre + " :" + self.asunto.tipo
    
    def transformador(self):
        self.localidad= self.localidad.lower().title()
        self.partido= self.partido.lower().title()
        self.nombre= self.nombre.lower().title()


    



   