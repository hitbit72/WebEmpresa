from django.apps import AppConfig


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'
    verbose_name = 'Gestor de servicios'  # Nombre de la aplicación que se mostrará en el panel de administración de Django

