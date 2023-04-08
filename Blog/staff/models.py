from django.db import models


# Create your models here.
class Videojuegos(models.Model):
        nombre = models.CharField(max_length=30)
        compania = models.CharField(max_length=20)
        consola = models.CharField(max_length=20)

        def __str__(self):
                return f"{self.id} - {self.nombre} - {self.compania} - {self.consola}"
        



