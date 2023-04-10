from django.db import models


# Create your models here.
class Videojuegos(models.Model):
        nombre = models.CharField(max_length=30)
        compania = models.CharField(max_length=20)
        consola = models.CharField(max_length=20)

        def __str__(self):
                return f"{self.id} - {self.nombre} - {self.compania} - {self.consola}"
        



# class Posts(models.Model):
#         title = models.CharField(max_length=250, verbose_name="Titulo")
#         excerpt = models.TextField(verbose_name="Bajada")
#         content = models.TextField(verbose_name="Contenido")
#         image = models.ImageField(upload_to="posts", null=True, blank=True, verbose_name="Imagen")
#         published = models.BooleanField(default=False, verbose_name="Publicado")

#         created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacioon")
#         updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
        



