from django.shortcuts import render
from .models import Climat, Continent, Country
from .serializers import ClimatSerializer, ContinetSerializer, CountrySerializer
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.


class ClimatViewSet(viewsets.ModelViewSet):
    queryset = Climat.objects.all()
    serializer_class = ClimatSerializer


class ContinentViewSet(viewsets.ModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = ContinetSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


# def gets(request,name):
#     if request.method == 'GET':
#         country = Country.objects.get(name=name)
#         serializer = CountrySerializer(country)
#         return Response(serializer.data)
#     else:
#         return Response({'error':'country not found'})

    
