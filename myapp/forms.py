#creado manualmente
from django import forms 
class CrearNuevaTarea(forms.Form):
    nombre = forms.CharField(label='Nombre:', max_length=50)
    descripcion = forms.CharField(label='Descripcion:', widget=forms.Textarea )

class CrearNuevoProyecto(forms.Form):
    nombre = forms.CharField(label='Nombre del proyecto: ',max_length=30)