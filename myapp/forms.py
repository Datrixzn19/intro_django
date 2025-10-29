#archivo creado a mano 
from django import forms 

class CrearNuevaTarea(forms.Form):
    # CharField es para texto
    nombre = forms.CharField(label='Nombre:', max_length=50) 
    
    # Textarea se usa para campos de texto largos como parrafos
    descripcion = forms.CharField(
        label='Descripcion:', 
        widget=forms.Textarea,
        max_length=500  
    )

class CrearNuevoProyecto(forms.Form):
    # CharField usa TextInput por defecto
    # Se usa 'class':'input'. es para dar estilos, el nombre input lo ponemos en el .css, no hay que poner nada en el html para esto
    nombre = forms.CharField(
        label='Nombre del proyecto: ',
        max_length=30, 
        widget=forms.TextInput(
            attrs={'class':'input'} # attrs para atributos HTML como class, id, placeholder
        )
    )