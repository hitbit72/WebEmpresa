"""
URL configuration for webempresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# setting para el manejo de archivos estáticos media en modo de desarrollo
# En un entorno de producción no es necesario, ya que se manejan de forma diferente.
# En producción, los archivos estáticos y media se sirven a través de un servidor web como Nginx o Apache.
from django.conf import settings

urlpatterns = [
    # Path del core
    path('', include('core.urls')),
    # Servicios
    path('services/', include('services.urls')),
    # Blog
    path('blog/', include('blog.urls')),
    # Pages legal
    path('page/', include('pages.urls')),
    # Pages contact
    path('contact/', include('contact.urls')),
    # Path para la administración
    path('admin/', admin.site.urls),
]

# Manejo de archivos estáticos media en modo de desarrollo
# En un entorno de producción no es necesario, ya que se manejan de forma diferente.
if  settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Manejo de archivos media en modo de desarrollo


# Titulos customizados para Administrador
admin.site.site_header = "La Caffetiera"
admin.site.index_title = "Panal de administrador"
admin.site.site_title = "La Caffetiera"
