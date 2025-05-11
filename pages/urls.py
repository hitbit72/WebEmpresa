from django.urls import path
from . import views

# page_title es un slug, que es una cadena de texto que representa una URL amigable
# page_id es un entero que representa el id de la página
# page_title es un nombre inventado, puedes ponerle cualquier nombre

urlpatterns = [
    # Path de pages
    path('<int:page_id>/<slug:page_title>', views.page, name='page'),
]
