from django.shortcuts import render
from django.http import HttpResponse
from staff.models import Videojuegos
from staff.forms import BuscarJuegoForm
# Create your views here.
def inicio(request):
    return HttpResponse("Esta es la pagina de inicio")

def index(request):
    return render(request, 'staff/index.html')

def verJuegos(request):
    return render(request, 'staff/ver-juegos.html')


def hacerPubli(request):
    return render(request, 'staff/hacer-publicacion.html')


def sobreMi(request):
    return render(request, 'staff/sobre-mi.html')

def buscarJuegos(request):

    if request.method == "POST":
        nombre = request.POST["juego"]
        compania = request.POST["compania"]
        consola = request.POST["consola"]
        juego = Videojuegos(nombre=nombre, compania=compania, consola=consola)
        juego.save()

    return render(request, 'staff/buscar-juegos.html')


def guardar_juegos(request):

    if request.method == "POST":

        formulario = BuscarJuegoForm(request.POST)

        if formulario.is_valid():
            infojuego = formulario.cleaned_data
            videojuego = Videojuegos(nombre=infojuego["nombre"], compania=infojuego["compania"], consola=infojuego["consola"])
            videojuego.save()
            return render(request, 'staff/index.html') 
        
    else:
        formulario = BuscarJuegoForm()

    return render(request, 'staff/guardar-juegos.html', {"formulario": formulario})



