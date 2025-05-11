from django import template
from pages.models import Page

# Registrar este templatetag en la libreria de templates para poder utilizarla
register = template.Library()

@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages
