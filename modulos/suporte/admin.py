#-*- coding: utf-8 -*-
from django.contrib import admin
from models import PaginaAplicativos, PaginaCatalogos, PaginaManuais, PaginaSuporte, Manuais, Pergunta

class PaginaSuporteAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem', 'texto_manuais', 'texto_catalogos', 'texto_aplicativos', )}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )

class PaginaManuaisAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )

class PaginaCatalogosAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'catalogos', 'catalogo_destaque')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )
    
    def response_add(self, request, obj, post_url_continue="../%s/") :
        redirect = super(PaginaCatalogosAdmin, self).response_add(request, obj) 
        for catalogo in obj.catalogos.all():
            catalogo.gerar_xml_catalogo()
        if obj.catalogo_destaque:
            obj.catalogo_destaque.gerar_xml_catalogo()
        return redirect
    
    def response_change(self, request, obj) :
        redirect = super(PaginaCatalogosAdmin, self).response_add(request, obj) 
        for catalogo in obj.catalogos.all():
            catalogo.gerar_xml_catalogo()
        if obj.catalogo_destaque:
            obj.catalogo_destaque.gerar_xml_catalogo()
        return redirect

class PaginaAplicativosAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )
    
class ManuaisAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data', 'autor']
    search_fields = ['titulo']
    exclude = ['data', 'autor']   
    
    def response_add(self, request, obj, post_url_continue="../%s/") :
        redirect = super(ManualDaMarcaAdmin, self).response_add(request, obj) 
        obj.autor = request.user 
        obj.save()
        return redirect
    
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ['pergunta', 'data', 'autor']
    search_fields = ['pergunta']
    prepopulated_fields = {'pergunta_slug': ('pergunta', )}
    exclude = ['data', 'autor']   
    
    def response_add(self, request, obj, post_url_continue="../%s/") :
        redirect = super(PerguntaAdmin, self).response_add(request, obj) 
        obj.autor = request.user 
        obj.save()
        return redirect

admin.site.register(PaginaAplicativos, PaginaAplicativosAdmin)
admin.site.register(PaginaCatalogos, PaginaCatalogosAdmin)
admin.site.register(PaginaManuais, PaginaManuaisAdmin)
admin.site.register(PaginaSuporte, PaginaSuporteAdmin)
admin.site.register(Manuais, ManuaisAdmin)
admin.site.register(Pergunta, PerguntaAdmin)