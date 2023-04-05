from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("Esta es la pagina de inicio")

def index(request):
    return render(request, 'staff/index.html')
