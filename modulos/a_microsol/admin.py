#-*- coding: utf-8 -*-
from django.contrib import admin
from models import PaginaAMicrosol, PaginaAEmpresa, PaginaConheca, PaginaQualidadeEPremios

class PaginaAMicrosolAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem', 'texto_a_empresa', 'texto_conheca', 'texto_qualidade_e_premios')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )
    
class PaginaAEmpresaAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem', 'texto_filiais', 'imagem_filiais')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )    

class PaginaConhecaAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem', 'galeria', 'arquivo')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )

class PaginaQualidadeEPremiosAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem', 'galeria')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )     
admin.site.register(PaginaAMicrosol, PaginaAMicrosolAdmin)
admin.site.register(PaginaAEmpresa, PaginaAEmpresaAdmin)
admin.site.register(PaginaConheca, PaginaConhecaAdmin)
admin.site.register(PaginaQualidadeEPremios, PaginaQualidadeEPremiosAdmin)

