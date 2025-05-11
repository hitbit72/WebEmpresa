from django.shortcuts import render, get_object_or_404
# Importamos models para poder acceder a los modelos de la aplicación, la base de datos.
from .models import Post, Caterory

# Create your views here.
def blog(request):
    posts = Post.objects.all()  # Obtiene todos los post de la base de datos
    return render(request, 'blog/blog.html', {'posts': posts})

def category(request, category_id):
    #No usaremos esta linea, lo cambiamos por get_object_or_404
    #category = Caterory.objects.get(id=category_id)  # Obtiene la categoría de la base de datos

    category = get_object_or_404(Caterory, id=category_id)  # Obtiene la categoría de la base de datos o devuelve un error 404 si no existe
    
    #Esta es la forma tradicional de opbtener los posts de la categoria
    #posts = Post.objects.filter(categories=category)  # Obtiene todos los post de la categoría
    # Pero no paseremos 'posts' a la plantilla, ya que no lo usaremos
    # En su lugar usaremos 'category' directamente en la platilla, ya que tenemos una relacion de muchos a muchos entre Post y Caterory
    return render(request, 'blog/category.html', {'category': category})  # Renderiza la plantilla de la categoría
