from django.db import models
# Create your models here.


class Continent(models.Model):
    name = models.CharField(max_length=30)
    descripten = models.TextField(blank=True)
    def __str__ (self):
        return self.name


    
class Climat (models.Model):
    name = models.CharField(max_length=50)
    descripten = models.TextField(blank=True)
    def __str__ (self):
        return self.name
    

class Country(models.Model):
    name = models.CharField(max_length=30)
    capital = models.CharField(max_length=30)
    population = models.BigIntegerField()
    area = models.FloatField()
    language = models.CharField(max_length=30)
    currency = models.CharField(max_length=30)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    climat = models.ForeignKey(Climat, on_delete=models.CASCADE)




