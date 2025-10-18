from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
#es el equivalente al settings del principal
#se puede decir que son las configuraciones unicas para la app 