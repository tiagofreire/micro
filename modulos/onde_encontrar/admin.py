#-*- coding: utf-8 -*-
from django.contrib import admin
from models import PaginaAssitenciaTecnica, PaginaLojasOnline, PaginaOndeEncontrar, PaginaRevendas, LojaOnline

class PaginaOndeEncontrarAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem', 'texto_revenda', 'texto_lojas_online', 'texto_assitencia_tecnica', )}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )

class PaginaAssitenciaTecnicaAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )

class PaginaLojasOnlineAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )

class PaginaRevendasAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )

class LojaOnlineAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data', 'autor', 'admin_thumbnail']
    search_fields = ['titulo']
    exclude = ['data', 'autor']   
    
    def response_add(self, request, obj, post_url_continue="../%s/") :
        redirect = super(LojaOnlineAdmin, self).response_add(request, obj) 
        obj.criar_miniaturas()
        obj.autor = request.user 
        obj.save()
        return redirect

    def response_change(self, request, obj) :
        redirect = super(LojaOnlineAdmin, self).response_change(request, obj)
        obj.criar_miniaturas()
        return redirect    

admin.site.register(PaginaOndeEncontrar, PaginaOndeEncontrarAdmin)
admin.site.register(PaginaAssitenciaTecnica, PaginaAssitenciaTecnicaAdmin)
admin.site.register(PaginaLojasOnline, PaginaLojasOnlineAdmin)
admin.site.register(PaginaRevendas, PaginaRevendasAdmin)
admin.site.register(LojaOnline, LojaOnlineAdmin)