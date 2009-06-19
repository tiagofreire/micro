#-*- coding: utf-8 -*-
from django.contrib import admin
from models import Noticia
from micro.modulos.utils import cropar_imagem_view
   
class NoticiaAdmin(admin.ModelAdmin) :
    list_display = ['titulo', 'chamada', 'data', 'autor', 'publicada', 'admin_thumbnail']
    search_fields = ['titulo']
    prepopulated_fields = {'titulo_slug':('titulo',)}
    exclude = ['data', 'autor']
    
    def response_add(self, request, obj, post_url_continue="../%s/") :
        redirect = super(NoticiaAdmin, self).response_add(request, obj) 
        obj.criar_miniaturas()
        obj.autor = request.user 
        obj.save()
        request.method = "GET"    
        request.session['obj_crop'] = obj
        return cropar_imagem_view(request, obj.imagem.name, redirect)


    def response_change(self, request, obj) :
        redirect = super(NoticiaAdmin, self).response_change(request, obj)
        obj.criar_miniaturas()
        request.method = "GET"    
        request.session['obj_crop'] = obj
        return cropar_imagem_view(request, obj.imagem.name, redirect)
    
    def queryset(self, request):
        if request.user.is_superuser:
            qs = self.model._default_manager.get_query_set().all()
        else:   
            qs = self.model._default_manager.get_query_set().filter(autor = request.user)
        return qs

admin.site.register(Noticia, NoticiaAdmin)