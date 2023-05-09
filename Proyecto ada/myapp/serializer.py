#aca se serializan los models para hacerlos API
from rest_framework import serializers
from .models import Estacion, Medicion

class EstacionSerializer(serializers.ModelSerializer):

    mediciones= serializers.SerializerMethodField()

    class Meta:
        model = Estacion
        fields = '__all__'

    def get_mediciones(self, obj):
        try:
            meds = Medicion.objects.filter(estacion_id=obj.id).order_by("fecha")
            prim = meds.first().fecha
            ulti = meds.last().fecha
            return {"primera":prim, "ultima":ulti}
        except:
            return {"primera":"", "ultima":""}

class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = '__all__'
