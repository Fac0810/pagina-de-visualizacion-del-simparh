#aca se serializan los models para hacerlos API
from rest_framework import serializers
from .models import Estacion

class EstacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacion
        fields = '__all__'