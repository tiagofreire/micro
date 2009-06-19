#-*- coding: utf-8 -*-
from django.contrib import admin
from models import PaginaRecursosHumanos, Curriculo

class PaginaRecursosHumanosAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('texto', 'imagem', 'texto_primeiro_acesso')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )  
    
class CurriculoAdmin(admin.ModelAdmin):
    exclude = ['data', ]
    list_display = ['nome', 'email', 'sexo', 'estado', 'data']
    search_fields = ['nome', 'cidade', 'estado']

admin.site.register(PaginaRecursosHumanos, PaginaRecursosHumanosAdmin)
admin.site.register(Curriculo, CurriculoAdmin)

