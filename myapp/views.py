from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import Proyecto, Tareas # importando los models que creé 

from django.shortcuts import get_object_or_404 #es una funciona de django, lo uso para que no caiga el server al buscar un registro en model
from django.shortcuts import render #para renderizar html


# Create your views here.

#cosas que se envian al navegador para que las vea el usuario 
def index(response):
    return render(response, 'index.html')

def hello(response, nombreUsuario):
    return HttpResponse(f"<h1>Hola {nombreUsuario} </h1>")
    #return HttpResponse("Hola mundo!") 

def about(response):
    print()#imprimiendo un parametro de url 
    return HttpResponse("Esta es la pagina de about")


def proyecto(response):
    proyecto = list(Proyecto.objects.values()) 
    return JsonResponse(proyecto, safe=False)

def tareas(response, id):
    #antes 
    #tareas = Tareas.objects.get(id=id) #propiedad de la clase, parametro de la funcion 
    #despues
    tareas = get_object_or_404(Tareas, id=id)
    return HttpResponse(f"Tarea: {tareas.nombre}") #ahora es en minuscula pq asi se habia guardado 