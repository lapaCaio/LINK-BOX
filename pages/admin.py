from django.contrib import admin
from pages.models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descricao', 'imagem_box', 'data_criacao', 'data_atualizacao']
    list_filter = ['data_criacao', 'data_atualizacao']
    search_fields = ['titulo']

admin.site.register(Page, PageAdmin)