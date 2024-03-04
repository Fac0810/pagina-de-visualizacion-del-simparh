#aca se serializan los models para hacerlos API
from rest_framework import serializers
from .models import Estacion, MedicionPluviometrica
""
class EstacionSerializer(serializers.ModelSerializer):

#    mediciones= serializers.SerializerMethodField()

    class Meta:
        model = Estacion
        fields = '__all__'

    def get_mediciones_pluviometricas(self, obj):
        try:
            meds = MedicionPluviometrica.objects.filter(estacion_id=obj.id).order_by("fecha")
            prim = meds.first().fecha
            ulti = meds.last().fecha
            return {"primera":prim, "ultima":ulti}
        except:
            return {"primera":"", "ultima":""}
            
class MedicionPluviometricaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicionPluviometrica
        fields = '__all__'
