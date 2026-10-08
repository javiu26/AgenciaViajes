from django.db import models

class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    precio = models.IntegerField()
    cupos = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre