from django.db import models

# Create your models here.
class Residente(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    familiar_cargo = models.CharField(max_length=100)
    medicamentos = models.CharField(max_length=50)
    situacion_salud = models.CharField(max_length=25)
    cuidados_especiales = models.TextField()
    def __str__(self) -> str:
        return self.rut