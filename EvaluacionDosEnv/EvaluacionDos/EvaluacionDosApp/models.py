from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Automovil(models.Model):
    Marca = models.CharField(max_length = 40)
    Modelo = models.CharField(max_length = 40)
    Anio = models.IntegerField(default = 1000, validators = [
        MaxValueValidator(2018),
        MinValueValidator(1000)
    ])
    Color = models.CharField(max_length = 40)
    NumeroPuertas = models.IntegerField(default = 2, validators = [
        MaxValueValidator(5),
        MinValueValidator(2)
    ])
    Descripcion = models.TextField(max_length = 200)
    FechaPublicacion = models.DateTimeField(default = timezone.now)
    Precio = models.IntegerField(default = 500000, validators = [
        MaxValueValidator(20000000),
        MinValueValidator(500000)
    ])