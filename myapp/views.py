from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import Proyecto, Tareas # importando los models que creé 

from django.shortcuts import get_object_or_404 #es una funciona de django, lo uso para que no caiga el server al buscar un registro en model
from django.shortcuts import render #para renderizar html
from django.shortcuts import redirect #redirigir a otro html

from .forms import CrearNuevaTarea, CrearNuevoProyecto #importamos nuestra clase, este nombre lo pasaremos como parametro en el render pero usando (), asi: CrearNuevaTarea()



# Create your views here.

#cosas que se envian al navegador para que las vea el usuario 
def index(request):
    nombre = 'David'
    return render(request, 'index.html', {'username': nombre}) #el '' es el que se le pone en el html

def hello(request, nombreUsuario):
    return HttpResponse(f"<h1>Hola {nombreUsuario} </h1>")
    #return HttpResponse("Hola mundo!") 

def about(request):
    print()#imprimiendo un parametro de url 
    return HttpResponse("Esta es la pagina de about")


def proyecto(request):
    #proyecto = list(Proyecto.objects.values()) 
    #return JsonResponse(proyecto, safe=False)

    #ahora renderizando en un html
    proyectos = Proyecto.objects.all()
    return render(request, 'proyecto/proyecto.html', {
        'proyecto': proyectos
        })

def tareas(request):
    #antes 
    #tareas = Tareas.objects.get(id=id) #propiedad de la clase, parametro de la funcion 
    #despues
    #tareas = get_object_or_404(Tareas, id=id)
    #return HttpResponse(f"Tarea: {tareas.nombre}") #ahora es en minuscula pq asi se habia guardado 

    #ahora renderizando en un html
    tareas = Tareas.objects.all()

    return render(request, 'tareas/tareas.html', {
        'tareas':tareas})


def crearTareas(request):
    if request.method=='GET':
        #interace
        return render(request, 'tareas/crearTareas.html', {
            'CrearNuevaTarea': CrearNuevaTarea()#el primer parametro va en el html dentro del form, {{ CrearNuevoProyecto }}
        })
    else:
        Tareas.objects.create(nombre=request.POST['nombre'], descripcion=request.POST['descripcion'], proyeto_id=1) # ['nombre'] -- va el nombre que le dimos en forms.py
        return redirect('/tareas/')

def crearProyecto(request):
    if request.method == 'GET':
        return render(request, 'proyecto/crearProyecto.html', {
            'CrearNuevoProyecto':CrearNuevoProyecto() 
        })
    else:
        Proyecto.objects.create(nombre=request.POST['nombre'])
        return redirect('/proyectos')