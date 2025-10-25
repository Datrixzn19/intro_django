#Este archivo fue creado a mano 
#es para que cada aplicacion tenga sus propias urls y luego se las pase a urls.py principal usando include 
from django.urls import path
from . import views #de esta carpeta importa donde estan mis vistas

urlpatterns = [
    path("", views.index, name="index"), #vacio indica que sera la raiz 

    path('hello/<str:nombreUsuario>', views.hello),#parametros por url
    
    path("about/", views.about),

    path("proyecto/", views.proyecto),

    #path("tareas/<int:id>", views.tareas), #pedia un int para buscar por id
    path("tareas/", views.tareas),

    path("crearTareas/", views.crearTareas),

    path("crearProyecto/", views.crearProyecto),

]