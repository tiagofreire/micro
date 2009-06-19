#-*- coding: utf-8 -*-
from django.contrib import admin
from models import PaginaCatalogos

class PaginaCatalogosAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'catalogos', 'catalogo_destaque')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )
    
    def response_add(self, request, obj, post_url_continue="../%s/") :
        redirect = super(PaginaCatalogosAdmin, self).response_add(request, obj) 
        for catalogo in obj.catalogos.all():
            catalogo.adicionarArquivo()
            catalogo.gerar_xml_catalogo()
        if obj.catalogo_destaque:
            obj.catalogo_destaque.gerar_xml_catalogo()
        return redirect
    
    def response_change(self, request, obj) :
        redirect = super(PaginaCatalogosAdmin, self).response_add(request, obj) 
        for catalogo in obj.catalogos.all():
            catalogo.adicionarArquivo()
            catalogo.gerar_xml_catalogo()
        if obj.catalogo_destaque:
            obj.catalogo_destaque.gerar_xml_catalogo()
        return redirect

admin.site.register(PaginaCatalogos, PaginaCatalogosAdmin)