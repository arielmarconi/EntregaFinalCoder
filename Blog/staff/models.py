from django.db import models


# Create your models here.

class Persona:
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()

class UsuarioComun(models.Model):
    usuario = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.id} - {self.usuario} - {self.email}"


class Administrador(models.Model):
    adm = models.CharField(max_length=20)
    email = models.EmailField()
