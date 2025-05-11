from django.contrib import admin
from .models import Link
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    # Si en el panel admin entra un usuario del grupo Personal, no podrá editar
    # los campos 'created', 'updated', 'key' y 'name'
    def get_readonly_fields(self, request, obj = None):
        if request.user.groups.filter(name="Personal").exists():
            return ('updated', 'key', 'name')
        else:
            return ('created', 'updated')


admin.site.register(Link, LinkAdmin)
