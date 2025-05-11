from django.contrib import admin
from .models import Post, Caterory


class CateroryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #list_display = ('name', 'created', 'updated')
    #search_fields = ('name',)
    #ordering = ('-created',)

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('-published',)
    
    search_fields = ('title', 'content','author__username', 'categories__name')
    # __name para acceder al campo name del modelo Caterory
    # __username, en campos relacionados hay que usar __ para acceder al campo de la relación
    
    date_hierarchy = 'published'
    # Muestra una barra para agrupar las entrads por fecha en el panel de administración
    
    list_filter = ('author__username', 'categories__name')
    # Crea un panel lateral para agrupar las entradas por autor y categoría

    #prepopulated_fields = {'slug': ('title',)}
    #list_editable = ('published',)

    # Recorremos las categorías de cada entrada y las mostramos en el panel de administración
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = 'Categorías' # Nombre que se mostrará en el panel de administración

admin.site.register(Caterory, CateroryAdmin)
admin.site.register(Post, PostAdmin)


