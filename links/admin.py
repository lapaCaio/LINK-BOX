from django.contrib import admin
from links.models import Link

class LinkAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'link_ativo', 'url', 'data_criacao', 'data_atualizacao', 'ordem_link']
    list_filter = ['link_ativo', 'data_criacao', 'data_atualizacao']
    search_fields = ['titulo']

admin.site.register(Link, LinkAdmin)
