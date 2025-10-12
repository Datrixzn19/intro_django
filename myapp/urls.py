from django.urls import path
from . import views #de esta carpeta importa donde estan mis vistas

urlpatterns = [
    path('', views.hello), #vacio indica que sera la raiz 
    path("about/", views.about)
]