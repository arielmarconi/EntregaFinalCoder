from django.shortcuts import render
from django.http import HttpResponse
from staff.models import Videojuegos
from staff.forms import BuscarJuegoForm
from django.db.models import Q
# Create your views here.
def inicio(request):
    return HttpResponse("Esta es la pagina de inicio")

def index(request):
    return render(request, 'staff/index.html')

def verJuegos(request):

    juegoss = Videojuegos.objects.all()

    return render(request, 'staff/ver-juegos.html', {'juegos': juegoss})



def hacerPubli(request):

    if request.method == "POST":
        
        juegos_form = BuscarJuegoForm(request.POST)

        if juegos_form.is_valid():
            datos = juegos_form.cleaned_data
            juego = Videojuegos(nombre=datos["nombre"], compania=datos["compania"], consola=datos["consola"])
            juego.save()
            return render(request, 'staff/index.html')
        
    juegos_form = BuscarJuegoForm()
        
    return render(request, 'staff/hacer-publicacion.html', {"form":juegos_form})


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

def eliminar_juego(request, id_juego):

    juego = Videojuegos.objects.get(id=id_juego)
    name = juego.nombre
    juego.delete()

    return render(request, 'staff/eliminar-juego.html', {"juego_eliminado":name})

def editarJuego(request, id_juego):

    juego = Videojuegos.objects.get(id=id_juego)

    if request.method == "POST":
        juego_form = BuscarJuegoForm(request.POST)
        if juego_form.is_valid():
            datos = juego_form.cleaned_data
            juego.nombre = datos["nombre"]
            juego.compania = datos["compania"]
            juego.consola = datos["consola"]
            juego.save()
            return render(request, 'staff/index.html')
    else:
        juego_form = BuscarJuegoForm(initial={'nombre': juego.nombre, 'compania': juego.compania, 'consola': juego.consola})
        
    return render(request, 'staff/editar-juego.html', {'form': juego_form})


def busqueda_articulo(request):
    return render(request,'staff/buscar-nombre.html')

def buscarNombre(request):
    
    
    if request.POST['nombre']:

        juego = request.POST['nombre']
        juegos = Videojuegos.objects.filter(nombre__icontains=juego)

        return render(request, 'staff/resultado-busqueda.html', {"juegos":juegos})
    
    else:
        respuesta = "No enviaste datos"


    return HttpResponse(respuesta)

