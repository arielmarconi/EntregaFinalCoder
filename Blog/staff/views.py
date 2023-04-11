from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse
from staff.models import Videojuegos, Avatar
from staff.forms import BuscarJuegoForm
from .forms import CustomUserCreationForm, CustomUserEditForm
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, View
from django.core.paginator import Paginator

# Create your views here.
def inicio(request):
    return HttpResponse("Esta es la pagina de inicio")

# @login_required
def index(request):
        return render(request, 'staff/index.html')

@login_required
def verJuegos(request):

    juegoss = Videojuegos.objects.all()

    return render(request, 'staff/ver-juegos.html', {'juegos': juegoss})


@login_required
def hacerPubli(request):

    if request.method == "POST":
        
        juegos_form = BuscarJuegoForm(request.POST)

        if juegos_form.is_valid():
            datos = juegos_form.cleaned_data
            juego = Videojuegos(nombre=datos["nombre"], compania=datos["compania"], consola=datos["consola"], anio=datos["anio"], autor=datos["autor"], imagen=datos['imagen'])
            juego.save()
            return render(request, 'staff/index.html')
        
    juegos_form = BuscarJuegoForm()
        
    return render(request, 'staff/hacer-publicacion.html', {"form":juegos_form})

@login_required
def sobreMi(request):
    return render(request, 'staff/sobre-mi.html')

@login_required
def buscarJuegos(request):

    if request.method == "POST":
        nombre = request.POST["juego"]
        compania = request.POST["compania"]
        consola = request.POST["consola"]
        juego = Videojuegos(nombre=nombre, compania=compania, consola=consola)
        juego.save()

    return render(request, 'staff/buscar-juegos.html')

@login_required
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
            juego.anio = datos["anio"]
            juego.descripcion = datos["descripcion"]
            juego.imagen = datos["imagen"]
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

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "staff/index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "staff/index.html", {"mensaje":"Datos incorrectos"})

        else:

            return render(request, "staff/index.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "staff/login.html", {"form": form})

def exit(request):
    logout(request)
    return redirect('index')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == "POST":
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('index')
        


    return render(request, 'registration/register.html', data)


def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = CustomUserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data

            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            
            password1 = informacion['password1']
            password2 = informacion['password2']
            if password1 and password2 and password1 == password2:
                usuario.set_password(password1)

            usuario.save()


            return render(request, "staff/index.html", {"mensaje": "Se edito el usuario correctamente"})
        
    else:
        form = CustomUserEditForm(initial={'email': usuario.email})
        

    return render(request, "staff/editar-perfil.html", {"form":form, "usuario":usuario})


class HomeView(View):
    def get(self, request, *args, **kwargs):

        context={


        }
        return render(request, 'staff/index.html', context)