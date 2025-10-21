from django.contrib import admin

from .models import Tareas, Proyecto
#desde aqui podemos agregar modelos al panel de administracion 

# Register your models here.
admin.site.register(Proyecto)
admin.site.register(Tareas)