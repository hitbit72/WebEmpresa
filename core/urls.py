from django.urls import path
from . import views # Importamos las vistas de la aplicación core 'views.py'

urlpatterns = [
    # Path del core
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
]
