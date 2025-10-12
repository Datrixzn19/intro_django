from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def hello(response):
    return HttpResponse("<h1>Hola mundo!</h1>")
    #return HttpResponse("Hola mundo!") 
def about(response):
    return HttpResponse("Esta es la pagina de about")