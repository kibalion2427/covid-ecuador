from rest_framework import serializers
from .models import Pais,Provincia,CasoCovid

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ["codigo","nombre","latitud","longitud","urlImagen"]

class PaisSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Pais
    #     fields = '__all__'
    # provincias = ProvinciaSerializer(many=True)
    class Meta:
        model = Pais
        fields = ["codigo","nombre","latitud","longitud","urlImagen"]



class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CasoCovid
        fields = ("fk_pais", "fk_provincia", "fecha", "confirmados", "recuperados", "muertos", "activos", "nuevos", "total")

class CovidSerializer(serializers.ModelSerializer):
    # pais = PaisSerializer(read_only = True)
    # provincia = ProvinciaSerializer(read_only= True)
    # pais = PaisSerializer(read_only = True,source="fk_pais")
    # provincia = ProvinciaSerializer(read_only= True,source="fk_provincia")
    pais = serializers.CharField(source="fk_pais")
    provincia = serializers.CharField(source="fk_provincia")
    class Meta:
        model = CasoCovid
        fields = ("pais","provincia","fecha","confirmados","recuperados","muertos","activos","nuevos","total")
        # depth = 1