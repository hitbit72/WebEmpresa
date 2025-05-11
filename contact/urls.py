from django.urls import path
from . import views # Importamos las vistas de la aplicación core 'views.py'

urlpatterns = [
    # Path del contact
    path('', views.contact, name='contact'),
]
