from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
#cosas que se envian al navegador para que las vea el usuario 
def index(response):
    return HttpResponse("Hola esta es la pagina de inicio")

def hello(response, nombreUsuario):
    return HttpResponse(f"<h1>Hola {nombreUsuario} </h1>")
    #return HttpResponse("Hola mundo!") 

def about(response):
    print()#imprimiendo un parametro de url 
    return HttpResponse("Esta es la pagina de about")