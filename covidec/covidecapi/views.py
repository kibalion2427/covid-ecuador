from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics,mixins,viewsets
from .models import Pais,Provincia,CasoCovid
from .serializers import PaisSerializer,ProvinciaSerializer,CovidSerializer,HistorySerializer

class ProvinceHistoryViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = HistorySerializer.objects.all()
        serializer = HistorySerializer(queryset, many=True)
        return Response(serializer.data)

class PaisViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Pais.objects.all()
        serializer =PaisSerializer(queryset,many = True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        queryset = Pais.objects.all()
        pais = get_object_or_404(queryset,pk=pk)
        serializer =  PaisSerializer(pais)
        return Response(serializer.data)
class ProvinciaViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Provincia.objects.all()
        serializer =ProvinciaSerializer(queryset,many = True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        queryset = Provincia.objects.all()
        pais = get_object_or_404(queryset,pk=pk)
        serializer =  ProvinciaSerializer(pais)
        return Response(serializer.data)

class CovidCaseViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = CasoCovid.objects.all()
        serializer =CovidSerializer(queryset,many = True)
        return Response(serializer.data)
    def retrieve(self,request):
        paiss = Pais.objects.only('codigo').get(codigo="EC")
        provincia = Provincia.objects.only('codigo').get(codigo="PICH")
        pass
        # print("REQUEST-->",self.kwargs['pais'])
        # print("REQUEST-->", self.kwargs['provincia'])
        # queryset = CasoCovid.objects.select_related('fk_pais').get(fk_pais=pk)
        # # queryset = CasoCovid.objects.all()
        # covid = get_object_or_404(queryset)
        # serializer =  CovidSerializer(covid)
        # print(serializer.data)
        # return Response(serializer.data)