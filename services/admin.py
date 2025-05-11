from django.contrib import admin
from .models import Service

# Register your models here.
# Hay que registrar nuestros modelos aquí para que aparezcan en el panel de administración de Django.

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')  # Campos que solo se pueden leer, no se pueden editar.

admin.site.register(Service, ServiceAdmin)  # Registra el modelo Service en el panel de administración de Django.

