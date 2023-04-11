from django.db import models
from django.contrib.auth.models import User, Permission
from django.utils import timezone
from django.contrib.auth import get_user_model



# Create your models here.
class Videojuegos(models.Model):
        nombre = models.CharField(max_length=30)
        compania = models.CharField(max_length=20)
        consola = models.CharField(max_length=20)
        anio = models.IntegerField(null=True)
        descripcion = models.TextField(max_length=5000, null=True, blank=True)
        autor = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
        imagen = models.ImageField(upload_to='videojuegos', null=True, blank= True)

        class Meta:
                permissions = [
                        ("can_edit_own_post", "Can edit own post"),

                ]


        def __str__(self):
                return f"{self.id} - {self.nombre} - {self.compania} - {self.consola} - {self.descripcion} - {self.anio} - {self.imagen}"
        



class Avatar(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        imagen = models.ImageField(upload_to='avatares', null=True, blank= True)

        def __str__(self):
                return f'Usuario: {self.user} - Imagen: {self.imagen}'
        
class Imagen(models.Model):
                titulo = models.CharField(max_length=100)
                imagen = models.ImageField(upload_to='videojuegos')
# class Posts(models.Model):
#         title = models.CharField(max_length=250, verbose_name="Titulo")
#         excerpt = models.TextField(verbose_name="Bajada")
#         content = models.TextField(verbose_name="Contenido")
#         image = models.ImageField(upload_to="posts", null=True, blank=True, verbose_name="Imagen")
#         published = models.BooleanField(default=False, verbose_name="Publicado")

#         created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacioon")
#         updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
        



