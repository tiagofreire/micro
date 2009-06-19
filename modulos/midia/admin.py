#-*- coding: utf-8 -*-
from django.contrib import admin
from models import PaginaHotsites, PaginaManualDaMarca, PaginaMidia, PaginaPublicidade, Publicidade, ManualDaMarca, Noticia, PaginaInformativo, Hotsite

class PaginaMidiaAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem', 'texto_publicidade', 'texto_hotsites', 'texto_manual_da_marca', )}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )

class PaginaPublicidadeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )
    
class PaginaInformativoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )    

class PaginaHotsitesAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )

class PaginaManualDaMarcaAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto', 'imagem')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )
    
class PublicidadeAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data', 'autor', 'admin_thumbnail']
    search_fields = ['titulo']
    exclude = ['data', 'autor']   
    
    def response_add(self, request, obj, post_url_continue="../%s/") :
        redirect = super(PublicidadeAdmin, self).response_add(request, obj) 
        obj.criar_miniaturas()
        obj.autor = request.user 
        obj.save()
        return redirect

    def response_change(self, request, obj) :
        redirect = super(PublicidadeAdmin, self).response_change(request, obj)
        obj.criar_miniaturas()
        return redirect
    
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data', 'autor']
    search_fields = ['titulo']
    exclude = ['data', 'autor'] 
    prepopulated_fields = {'titulo_slug': ('titulo', )}
    
    def response_add(self, request, obj, post_url_continue="../%s/") :
        redirect = super(NoticiaAdmin, self).response_add(request, obj) 
        obj.criar_miniaturas()
        obj.autor = request.user 
        obj.save()
        return redirect

    def response_change(self, request, obj) :
        redirect = super(NoticiaAdmin, self).response_change(request, obj)
        obj.criar_miniaturas()
        return redirect
    
class HotsiteAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data', 'autor', 'admin_thumbnail']
    search_fields = ['titulo']
    exclude = ['data', 'autor'] 
    
    def response_add(self, request, obj, post_url_continue="../%s/") :
        redirect = super(HotsiteAdmin, self).response_add(request, obj) 
        obj.criar_miniaturas()
        obj.autor = request.user 
        obj.save()
        return redirect

    def response_change(self, request, obj) :
        redirect = super(HotsiteAdmin, self).response_change(request, obj)
        obj.criar_miniaturas()
        return redirect      
    
class ManualDaMarcaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'data', 'autor']
    search_fields = ['titulo']
    exclude = ['data', 'autor']   
    
    def response_add(self, request, obj, post_url_continue="../%s/") :
        redirect = super(ManualDaMarcaAdmin, self).response_add(request, obj) 
        obj.autor = request.user 
        obj.save()
        return redirect
    

admin.site.register(PaginaMidia, PaginaMidiaAdmin)
admin.site.register(PaginaPublicidade, PaginaPublicidadeAdmin)
admin.site.register(PaginaHotsites, PaginaHotsitesAdmin)
admin.site.register(PaginaManualDaMarca, PaginaManualDaMarcaAdmin)
admin.site.register(Publicidade, PublicidadeAdmin)
admin.site.register(ManualDaMarca, ManualDaMarcaAdmin)
admin.site.register(PaginaInformativo, PaginaInformativoAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Hotsite, HotsiteAdmin)