from django.urls import path
from staff.views import inicio, index, verBlogs, hacerPubli, sobreMi


urlpatterns = [
    path('', index, name="index"),
    path('ver-blogs/', verBlogs, name="ver-blogs"),
    path('hacer-publicacion/', hacerPubli, name="hacer-publicacion"),
    path('sobre-mi/', sobreMi, name="sobre-mi"),
    
    

]
