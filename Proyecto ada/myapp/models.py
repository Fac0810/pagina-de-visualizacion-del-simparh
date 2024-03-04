from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime , date

# Aca se encuentran los modelos de los objetos de datos. Django los utiliza para hacer las migraciones
# haciendo que estos modelos se reflejen en la base de datos


# Mantenimiento (se repite abajo, pero se necesita para la estacion)

class EstadoMantenimiento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=40)



# Estaciones
    
class Estacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_externo_estacion = models.IntegerField(default=0)
    nombre = models.CharField(max_length=60, null=False, blank=False)
    fuente = models.CharField(max_length=25, default="No se sabe")
    latitud = models.DecimalField(max_digits=15,decimal_places=12, null=False, blank=False)
    longitud = models.DecimalField(max_digits=15,decimal_places=12, null=False, blank=False)
    numero_serie = models.CharField(max_length=35, default="No tiene")
    descripcion_lugar = models.TextField(default="")
    ultimo_mantenimiento = models.DateTimeField(default=datetime.now,)
    estado_mantenimiento= models.ForeignKey(EstadoMantenimiento, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre



# Mediciones

#Presion atmosferica. Con valores entre 500 y 1100 hPa (hectopascales). Resolucion: 0.1 hPA
class MedicionBarometrica(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1, null=False, blank=False)
    valor_presion = models.DecimalField(max_digits=7,decimal_places=5, null=False, blank=False)
    validacion_presion = models.BooleanField()
    discreto = models.BooleanField() #define si es discreto (True) o telemetrico (False)
    fecha_hora = models.DateTimeField(null=False, blank=False) 

    def __str__(self):
        return 'Medicion barometrica de la estacion: '+ self.estacion + ' en la fecha ' + str(self.fecha_hora)

#Direcion del viento. Con valores entre 0 y 359 ° (grados). Resolucion: 0.1 °
class MedicionDireccionViento(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1, null=False, blank=False)
    valor_direccion = models.DecimalField(max_digits=5,decimal_places=3, null=False, blank=False)
    validacion_direccion = models.BooleanField()
    discreto = models.BooleanField() #define si es discreto (True) o telemetrico (False)
    fecha_hora = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return 'Medicion de la direccion del viento de la estacion: '+ self.estacion + ' en la fecha ' + str(self.fecha_hora)

#Velocidad del Viento. Con valores entre 0 y 60 m/s (metros por segundo). Resolucion: 0.1 m/s
class MedicionAnemometrica(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1, null=False, blank=False)
    valor_velocidad = models.DecimalField(max_digits=5,decimal_places=3, null=False, blank=False)
    validacion_velocidad = models.BooleanField()
    discreto = models.BooleanField() #define si es discreto (True) o telemetrico (False)
    fecha_hora = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return 'Medicion anemometrica de la estacion: '+ self.estacion + ' en la fecha ' + str(self.fecha_hora)

#Presion en nivel. Con valores entre 0 y 200 mH2O (metros de agua). Resolucion: 0.1
class MedicionFreatimetrica(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1, null=False, blank=False)
    valor_presion = models.DecimalField(max_digits=7,decimal_places=5, null=False, blank=False)
    validacion_presion = models.BooleanField()
    discreto = models.BooleanField() #define si es discreto (True) o telemetrico (False)
    fecha_hora = models.DateTimeField(null=False, blank=False) 

    def __str__(self):
        return 'Medicion freatimetrica de la estacion: '+ self.estacion + ' en la fecha ' + str(self.fecha_hora)

#Radacion solar. Con valores entre 0 y 4000 W/m² (Watt por metro cuadrado). Resolucion: 0.5 W/m²
class MedicionPiranometrica(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1, null=False, blank=False)
    valor_radiacion = models.DecimalField(max_digits=7,decimal_places=5, null=False, blank=False)
    validacion_radiacion = models.BooleanField()
    discreto = models.BooleanField() #define si es discreto (True) o telemetrico (False)
    fecha_hora = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return 'Medicion piranometrica de la estacion: '+ self.estacion + ' en la fecha ' + str(self.fecha_hora)

#Profundidad. Con valores entre 0 y 25 (o 100/200) m (metros) . Resolucion: 0.01 m
class MedicionLimnigrafica(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1, null=False, blank=False)
    valor_nivel = models.DecimalField(max_digits=6,decimal_places=4, null=False, blank=False)
    validacion_nivel = models.BooleanField()
    discreto = models.BooleanField() #define si es discreto (True) o telemetrico (False)
    fecha_hora = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return 'Medicion limnigrafica de la estacion: '+ self.estacion + ' en la fecha ' + str(self.fecha_hora)

#Precepitacion. Con valores entre 0 y 500 mm (milimietros), con un maximo de intensidad de 10mm/min. Resolucion: 0.2 mm
class MedicionPluviometrica(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1, null=False, blank=False)
    valor_precipitacion = models.DecimalField(max_digits=6,decimal_places=4, null=False, blank=False)
    validacion_precipitacion = models.BooleanField()
    discreto = models.BooleanField() #define si es discreto (True) o telemetrico (False)
    fecha_hora = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return 'Medicion pluviometrica de la estacion: '+ self.estacion + ' en la fecha ' + str(self.fecha_hora)

#Punto rocio. Con valores entre -40 y 80 °C (grados centigrados)
class MedicionPuntoRocio(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1, null=False, blank=False)
    valor_punto_rocio = models.DecimalField(max_digits=6,decimal_places=4, null=False, blank=False)
    validacion_punto_rocio = models.BooleanField()
    discreto = models.BooleanField() #define si es discreto (True) o telemetrico (False)
    fecha_hora = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return 'Medicion del punto rocio de la estacion: '+ self.estacion + ' en la fecha ' + str(self.fecha_hora)

#Humedad relativa. Con valores entre 0 y 100 % hr (humedad relativa). Resolucion: 0.1 %hr
class MedicionHumedad(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1, null=False, blank=False)
    valor_humedad = models.DecimalField(max_digits=5,decimal_places=3, null=False, blank=False)
    validacion_humedad = models.BooleanField()
    discreto = models.BooleanField() #define si es discreto (True) o telemetrico (False)
    fecha_hora = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return 'Medicion de la humedad de la estacion: '+ self.estacion + ' en la fecha ' + str(self.fecha_hora)

#Temperatura ambiente. Con valores entre -40 y 80 °C (grados centigrados). Resolucion: 0.01 °C    
class MedicionTemperaturaAtmosferica(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1, null=False, blank=False)
    valor_teperatura = models.DecimalField(max_digits=6,decimal_places=4, null=False, blank=False)
    validacion_teperatura = models.BooleanField()
    discreto = models.BooleanField() #define si es discreto (True) o telemetrico (False)
    fecha_hora = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return 'Medicion de la temperatura atmosferica de la estacion: '+ self.estacion + ' en la fecha ' + str(self.fecha_hora)

#Temperatura del curso. Con valores entre -5 y 50 °C (grados centigrados). Resolucion: 0.01 °
class MedicionTemperaturaDelCurso(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1, null=False, blank=False)
    valor_teperatura = models.DecimalField(max_digits=7,decimal_places=5, null=False, blank=False)
    validacion_teperatura = models.BooleanField()
    discreto = models.BooleanField() #define si es discreto (True) o telemetrico (False)
    fecha_hora = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return 'Medicion de la temperatura del curso de la estacion: '+ self.estacion + ' en la fecha ' + str(self.fecha_hora)

#Nivel de batería. Con valores entre 0 y 100 %(porciento). Resolucion: 1%
class MedicionBateria(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1, null=False, blank=False)
    valor_bateria = models.DecimalField(max_digits=7,decimal_places=5, null=False, blank=False)
    validacion_bateria = models.BooleanField()
    discreto = models.BooleanField() #define si es discreto (True) o telemetrico (False)
    fecha_hora = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return 'Medicion de la bateria de la estacion: '+ self.estacion + ' en la fecha ' + str(self.fecha_hora)

#Conductividad especifica. Con valores entre 0 y 200,000 uS/cm (microsiemens por centimetro). Resolucion: 0.1 uS/cm
class MedicionConductividad(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1, null=False, blank=False)
    valor_conductividad = models.DecimalField(max_digits=15,decimal_places=13, null=False, blank=False)
    validacion_conductividad = models.BooleanField()
    discreto = models.BooleanField() #define si es discreto (True) o telemetrico (False)
    fecha_hora = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return 'Medicion de conductividad de la estacion: '+ self.estacion + ' en la fecha ' + str(self.fecha_hora)

#PH. Con valores entre 0 y 14 ph (Nivel de ph). Resolucion: 0.01 ph
class MedicionPH(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1, null=False, blank=False)
    valor_ph = models.DecimalField(max_digits=7,decimal_places=5, null=False, blank=False)
    validacion_ph = models.BooleanField()
    discreto = models.BooleanField() #define si es discreto (True) o telemetrico (False)
    fecha_hora = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return 'Medicion del PH de la estacion: '+ self.estacion + ' en la fecha ' + str(self.fecha_hora)

#Turbidez. Formazin Nephelometric Unit (FNU) o Unidad Nefelométrica de Formacina (tambien se puede calibrar para NTU). Con valores entre 0 y 1000 o 1000 y 4000 FNU o NTU. Resolucion: 0.01
class MedicionTurbidimetrica(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1, null=False, blank=False)
    valor_turbiedad = models.DecimalField(max_digits=7,decimal_places=5, null=False, blank=False)
    validacion_turbiedad = models.BooleanField()
    discreto = models.BooleanField() #define si es discreto (True) o telemetrico (False)
    fecha_hora = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return 'Medicion de la estacion: '+ self.estacion + ' en la fecha ' + str(self.fecha_hora)    



# Eventos

class Evento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=40, null=False, blank=False)
    descripcion = models.TextField(default="")
    
class EventoOcurrido(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1)
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE, default=1)
    fecha_hora = models.DateTimeField(null=False, blank=False)



# Sensores

class Sensor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=60, null=False, blank=False)
    marca = models.CharField(max_length=60, null=False, blank=False)
    modelo = models.CharField(max_length=60, null=False, blank=False)
    descripcion = models.TextField(default="")
    ultimo_mantenimiento = models.DateTimeField(default=datetime.now)
    estado_mantenimiento= models.ForeignKey(EstadoMantenimiento, on_delete=models.CASCADE, default=1)

class EmaSensor(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1)
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, default=1)



# Usuarios, roles y permisos
    
class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=60, null=False, blank=False)
    nombre = models.CharField(max_length=60, null=False, blank=False)
    apellido = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    fecha_inicio = models.DateField(default=datetime.now)
    ultima_coneccion = models.DateTimeField(default=datetime.now)

class Rol(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=60, null=False, blank=False)

class Permiso(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=60, null=False, blank=False)

class UsuarioRol(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_usr = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)
    id_rol= models.ForeignKey(Rol, on_delete=models.CASCADE, default=1)

class RolPermiso(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_rol= models.ForeignKey(Rol, on_delete=models.CASCADE, default=1)
    id_perm =models.ForeignKey(Permiso, on_delete=models.CASCADE, default=1)



# Mantenimiento
    
class InformeMantenimientoEstacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_hora = models.DateTimeField(null=False, blank=False)
    descripcion = models.TextField(default="", null=False, blank=False)
    id_ema = models.ForeignKey(Estacion, on_delete=models.CASCADE, default=1)
    id_usr = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)

class InformeMantenimientoEstacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_hora = models.DateTimeField(null=False, blank=False)
    descripcion = models.TextField(default="", null=False, blank=False)
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, default=1)
    id_usr = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)



# Contacto

class Asunto(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.CharField(max_length=100, null=False, blank=False)
   
    def __str__(self):
        return self.tipo
    
class Contacto(models.Model):
    id = models.BigAutoField(primary_key=True)
    asunto = models.ForeignKey(Asunto, on_delete=models.CASCADE, blank=False)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    localidad= models.CharField(max_length=100, null=False, blank=False)
    partido= models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    telefono = PhoneNumberField(null=False, blank=False)
    mensaje = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.nombre + " :" + self.asunto.tipo
    
    def transformador(self):
        self.localidad= self.localidad.lower().title()
        self.partido= self.partido.lower().title()
        self.nombre= self.nombre.lower().title()
 