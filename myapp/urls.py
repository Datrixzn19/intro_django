#Este archivo fue creado a mano 
#es para que cada aplicacion tenga sus propias urls y luego se las pase a urls.py principal usando include 
from django.urls import path
from . import views #de esta carpeta importa donde estan mis vistas

urlpatterns = [
    path("", views.index, name="index"), #vacio indica que sera la raiz 

    path('hello/<str:nombreUsuario>', views.hello, name="hello"),#parametros por url
    
    path("about/", views.about, name="about"),

    path("proyecto/", views.proyecto, name="proyecto"),

    #path("tareas/<int:id>", views.tareas), #pedia un int para buscar por id
    path("tareas/", views.tareas, name="tareas"),

    path("crearTareas/", views.crearTareas, name="crearTareas"),

    path("crearProyecto/", views.crearProyecto, name="crearProyecto"),

]