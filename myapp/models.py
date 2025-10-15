from django.db import models

# Create your models here.

class Proyecto(models.Model): 
    nombre = models.CharField(max_length=20)

class Tareas(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    proyeto = models.ForeignKey(Proyecto, on_delete=models.CASCADE) #Relacion a otra tabla, eliminar cuando se borre un proyecto se borren las tareas que estaban con el 

