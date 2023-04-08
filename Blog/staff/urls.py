from django.urls import path
from staff.views import index, verJuegos, hacerPubli, sobreMi, buscarJuegos, guardar_juegos, eliminar_juego, editarJuego


urlpatterns = [
    path('', index, name="index"),
    path('ver-juegos/', verJuegos, name="ver-juegos"),
    path('hacer-publicacion/', hacerPubli, name="hacer-publicacion"),
    path('sobre-mi/', sobreMi, name="sobre-mi"),
    path('buscar-juegos/', buscarJuegos, name="buscar-juegos"),
    path('guardar-juegos/', guardar_juegos, name="guardar-juegos"),
    path('eliminar-juego/<int:id_juego>/', eliminar_juego, name="eliminar-juego"),
    path('editar-juego/<int:id_juego>/', editarJuego, name="editar-juego")
    
    

]
