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
    filterset_fields = ['name','continent']


    
