from django.shortcuts import render
# Importamos models para poder acceder a los modelos de la aplicación, la base de datos.
from .models import Service

# Create your views here.
def services(request):
    services = Service.objects.all()  # Obtiene todos los servicios de la base de datos
    return render(request, 'services/services.html', {'services': services})
