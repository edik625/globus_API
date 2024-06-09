from django.contrib import admin
from .models import Climat, Continent, Country
# Register your models here.

admin.site.register([Climat,Continent,Country])