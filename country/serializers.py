from .models import Climat,Continent,Country
from rest_framework import serializers


class ClimatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climat
        fields = ["name"]


class ContinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ["name"]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"