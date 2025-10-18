#Este archivo fue creado a mano 
#es para que cada aplicacion tenga sus propias urls y luego se las pase a urls.py principal usando include 
from django.urls import path
from . import views #de esta carpeta importa donde estan mis vistas

urlpatterns = [
    path("", views.index), #vacio indica que sera la raiz 

    path('hello/<str:nombreUsuario>', views.hello),#parametros por url
    
    path("about/", views.about),
]