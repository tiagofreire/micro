#-*- coding: utf-8 -*-
from django.contrib import admin
from models import TipoAplicacao, Modelo, Produto, Categoria, Software, Cor, Caracteristica

class TipoAplicacaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data', 'autor', 'admin_thumbnail']
    search_fields = ['nome']
    exclude = ['data', 'autor']
   
    
    def response_add(self, request, obj, post_url_continue="../%s/") :
        redirect = super(TipoAplicacaoAdmin, self).response_add(request, obj) 
        obj.criar_miniaturas()
        obj.autor = request.user 
        obj.save()
        return redirect

    def response_change(self, request, obj) :
        redirect = super(TipoAplicacaoAdmin, self).response_change(request, obj)
        obj.criar_miniaturas()
        return redirect

class CaracteristicaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data', 'autor', 'admin_thumbnail']
    search_fields = ['titulo']
    exclude = ['data', 'autor']   
    
    def response_add(self, request, obj, post_url_continue="../%s/") :
        redirect = super(CaracteristicaAdmin, self).response_add(request, obj) 
        obj.criar_miniaturas()
        obj.autor = request.user 
        obj.save()
        return redirect

    def response_change(self, request, obj) :
        redirect = super(CaracteristicaAdmin, self).response_change(request, obj)
        obj.criar_miniaturas()
        return redirect    
    
class ModeloAdmin(admin.ModelAdmin):
    list_display = ['nome', 'potencia','tipo_potencia', 'data', 'autor']
    search_fields = ['nome']
    exclude = ['data', 'autor']
    filter_horizontal = ['aplicacoes']
    
    def response_add(self, request, obj, post_url_continue="../%s/") :
        redirect = super(ModeloAdmin, self).response_add(request, obj) 
        obj.autor = request.user 
        obj.save()
        return redirect
    
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'admin_logo', 'categoria', 'sgm', 'admin_hotsite', 'data', 'autor', 'admin_thumbnail']
    search_fields = ['nome']
    exclude = ['data', 'autor']
    filter_horizontal = ['modelos', 'caracteristicas', 'produtos_semelhantes']
    fieldsets = (
        (None, {'fields': ['nome', 'nome_slug', 'categoria', 'logo', 'potencia', 'imagem', 'miniatura', 'galeria', 'descricao', 'modelos', 'caracteristicas', 'sgm', 'hotsite', 'modulo_de_comunicacao', 
                           'funcoes_e_beneficios', 'manual', 'catalogo', 'tour_360', 'produtos_semelhantes']}),
        ("Item Extra", {'classes': ('collapse',), 'fields': ['extra_i_nome', 'extra_i_texto']}),
        ("Item Extra", {'classes': ('collapse',), 'fields': ['extra_ii_nome', 'extra_ii_texto']}),
        ("Item Extra", {'classes': ('collapse',), 'fields': ['extra_iii_nome', 'extra_iii_texto']})
    )
    prepopulated_fields = {'nome_slug': ('nome',)}
    
    def response_add(self, request, obj, post_url_continue="../%s/") :
        redirect = super(ProdutoAdmin, self).response_add(request, obj) 
        obj.criar_miniaturas()
        obj.autor = request.user 
        obj.save()
        return redirect

    def response_change(self, request, obj) :
        redirect = super(ProdutoAdmin, self).response_change(request, obj)
        obj.criar_miniaturas()
        return redirect   
    
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ['nome', 'admin_logo', 'data', 'autor']
    search_fields = ['nome']
    exclude = ['data', 'autor']
    prepopulated_fields = {'nome_slug': ('nome',)}
    filter_horizontal = ['caracteristicas']
    
    def response_add(self, request, obj, post_url_continue="../%s/") :
        redirect = super(SoftwareAdmin, self).response_add(request, obj) 
        obj.autor = request.user 
        obj.save()
        return redirect
        
admin.site.register(TipoAplicacao, TipoAplicacaoAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Caracteristica, CaracteristicaAdmin)
admin.site.register(Categoria)
admin.site.register(Cor)