from django.db import models

# Create your models here.
#son para crear clases que luego seran tablas 

class Proyecto(models.Model): 
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre #con esto ya no va a aparecer Proyecto Object. sino el nombre real que tengan 



class Tareas(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    proyeto = models.ForeignKey(Proyecto, on_delete=models.CASCADE) #Relacion a otra tabla, eliminar cuando se borre un proyecto se borren las tareas que estaban con el 
    tareaRealizada = models.BooleanField(default=False)
    
    def __str__(self):
        #return 'Tarea: '+ self.nombre + 'royecto: '+ self.proyeto.nombre #como proyecto es un objeto entonces podemos acceder a sus propiedades 
        return f"TAREA: {self.nombre}    PROYECTO: {self.proyeto.nombre}" #ambas maneras funcionarion 