from .models import Link
# Archivo de contexto
# Permite transferirir variables a todas las plantillas del proyecto
# Se usa en el settings.py en 'TEMPLATES' para cargarlo en el contexto de las plantillas

def ctx_dict(request):
    social_ctx = {}
    links = Link.objects.all()
    for link in links:
        social_ctx[link.key] = link.url
    return social_ctx
