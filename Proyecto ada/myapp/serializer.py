#aca se serializan los models para hacerlos API
from rest_framework import serializers
from .models import Estacion, Medicion

class EstacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacion
        fields = '__all__'

class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = '__all__'