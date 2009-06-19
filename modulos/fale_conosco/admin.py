#-*- coding: utf-8 -*-
from django.contrib import admin
from models import PaginaContato, PaginaDepartamentos, PaginaFaleConosco, PaginaSAM

class PaginaFaleConoscoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem', 'texto_sam', 'texto_departamentos', 'texto_contato')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )

class PaginaSAMAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )

class PaginaContatoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )

class PaginaDepartamentosAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )
    

admin.site.register(PaginaFaleConosco, PaginaFaleConoscoAdmin)
admin.site.register(PaginaSAM, PaginaSAMAdmin)
admin.site.register(PaginaContato, PaginaContatoAdmin)
admin.site.register(PaginaDepartamentos, PaginaDepartamentosAdmin)
