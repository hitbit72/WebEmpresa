from django.urls import path
from . import views

urlpatterns = [
    # Path de servbicios
    path('', views.services, name='services'),
]
