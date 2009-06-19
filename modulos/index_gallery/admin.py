#-*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib import databrowse
from django.db.models import Q
from models import Tamanho, Foto, Galeria, UploadArquivo, Categoria
from forms import FormGaleria, FormAdminArquivo
from django.conf import settings

class GaleriaAdmin(admin.ModelAdmin) :
    form = FormGaleria
    list_display = ['nome', 'categoria', 'data', 'publico', 'autor' ]
    fieldsets = (
        (None, {'fields':('nome', 'nome_slug', 'ordem', 'categoria', 'capa', 'fotos', 'arquivo', 'publico')}),
        )
    filter_horizontal = ['fotos', 'arquivo']
    prepopulated_fields = {'nome_slug':('nome',)}
    search_fields = ['nome']

    def response_add(self, request, obj, post_url_continue = "../%s/"):
        retorno = super(GaleriaAdmin, self).response_add(request, obj)
        obj.adicionarArquivo()
        obj.autor = request.user
        obj.save()
        if obj.capa:
            obj.criar_miniatura_capa()
        return retorno
    
    def response_change(self, request, obj):
        retorno = super(GaleriaAdmin, self).response_change(request, obj)
        obj.adicionarArquivo()
        if obj.capa:
            obj.criar_miniatura_capa()
        return retorno
    
    #Ixibirá apenas as galerias que o usuario criou caso ele não seja um superusuario.
    def queryset(self, request):
        if request.user.is_superuser:
            qs = self.model._default_manager.get_query_set().all()
        else:           
            qs = self.model._default_manager.get_query_set().filter(Q(autor = request.user) | Q(publico = True))
        return qs


class FotoAdmin(admin.ModelAdmin) :
    list_display = ['nome', 'data', 'publico', 'admin_tamanho', 'autor', 'admin_thumbnail']
    list_display_links = ['nome']
    search_fields = ['nome']
    prepopulated_fields = {'nome_slug':('nome',)}
    actions_on_bottom = False
    exclude = ['autor', 'upload']
    fieldsets = (
        (None, {'fields':('nome', 'nome_slug', 'descricao', 'ordem', 'arquivo', 'thumbnails', 'publico')}),
        )
    
    def response_add(self, request, obj, post_url_continue="../%s/") :
        redirect = super(FotoAdmin, self).response_add(request, obj)        
        obj.criar_miniaturas()
        obj.criar_miniatura_admin()
        obj.autor = request.user
        obj.adicionar_miniaturas_padrao()
        obj.save()
        return redirect    

    def response_change(self, request, obj) :
        redirect = super(FotoAdmin, self).response_change(request, obj)
        obj.criar_miniaturas()
        return redirect
    
    #Ixibirá apenas as fotos que o usuario criou caso ele não seja um superusuario.
    def queryset(self, request):
        if request.user.is_superuser:
            qs = self.model._default_manager.get_query_set().all()
        else:   
            qs = self.model._default_manager.get_query_set().filter(Q(autor = request.user) | Q(publico = True))
        return qs


class ArquivoUploadAdmin(admin.ModelAdmin):
    exclude = ['autor']  
    list_display = ['nome', 'data', 'publico', 'admin_tamanho', 'autor']
    form = FormAdminArquivo
    fieldsets = (
        (None, {'fields':('nome', 'usar_nome', 'arquivo', 'thumbnails', 'publico')}),
        )
    
    def response_add(self, request, obj, post_url_continur="../%s/") :
        redirect = super(ArquivoUploadAdmin, self).response_add(request, obj)    
        for tamanho in Tamanho.objects.filter(padrao = True).all():
            if not tamanho in obj.thumbnails.all():
                obj.thumbnails.add(tamanho)
        obj.processar_zip(request.user)
        obj.autor = request.user
        obj.save()
        return redirect

    def response_change(self, request, obj) :
        redirect = super(ArquivoUploadAdmin, self).response_change(request, obj)
        obj.processar_zip(request.user)
        obj.autor = request.user
        obj.save()
        return redirect
    
    #Ixibirá apenas os uploads que o usuario criou caso ele não seja um superusuario.
    def queryset(self, request):
        if request.user.is_superuser:
            qs = self.model._default_manager.get_query_set().all()
        else:   
            qs = self.model._default_manager.get_query_set().filter(autor = request.user)
        return qs


class TamanhoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'largura', 'altura', 'proporcional', 'padrao']
    
    def response_add(self, request, obj, post_url_continue = "../%s/"):
        redirect = super(TamanhoAdmin, self).response_add(request, obj)
        obj.adicionar_para_fotos()
        return redirect   
    

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'nome_slug':('nome',)}  


admin.site.register(Tamanho, TamanhoAdmin)
admin.site.register(UploadArquivo, ArquivoUploadAdmin)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Foto, FotoAdmin)
admin.site.register(Categoria, CategoriaAdmin)

databrowse.site.register(Foto)
databrowse.site.register(Categoria)
databrowse.site.register(Galeria)
databrowse.site.register(UploadArquivo)