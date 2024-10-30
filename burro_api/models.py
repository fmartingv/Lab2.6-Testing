from django.db import models

class Burro(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    color = models.CharField(max_length=50)
    peso = models.FloatField()
    
    def __str__(self): 
        return self.nombre