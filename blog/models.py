from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User # Importa todos los usuarios del panel administrador de Django


# Create your models here.
class Caterory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha actualización')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['-created']

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha publicación', default=now)
    image = models.ImageField(upload_to='blog/', verbose_name='Imagen', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)    # Relación con el modelo User
    categories = models.ManyToManyField(Caterory, verbose_name='Categorías', related_name='get_posts')  # Relación con el modelo Caterory
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha actualización')

    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title