#-*- coding: utf-8 -*-
from django.contrib import admin
from django.http import HttpResponseRedirect
from models import Parceiro
from modulos.batchadmin.admin import BatchModelAdmin
from modulos.utils import cropar_imagem_view
  
class ParceiroAdmin(BatchModelAdmin) :
    list_display = ['nome', 'link', 'admin_thumbnail']
    search_fields = ['nome']
    actions_on_bottom = False
    
    def response_add(self, request, obj, post_url_continue="../%s/") :
        redirect = super(ParceiroAdmin, self).response_add(request, obj) 
        if obj.imagem:
            obj.criar_miniatura()
            obj.criar_miniatura_admin()
        request.method = "GET"    
        request.session['obj_crop'] = obj
        return cropar_imagem_view(request, obj.imagem.name, redirect)    

    def response_change(self, request, obj) :
        redirect = super(ParceiroAdmin, self).response_change(request, obj)
        if obj.imagem:
            obj.criar_miniatura()
            obj.criar_miniatura_admin()
        request.method = "GET"    
        request.session['obj_crop'] = obj
        return cropar_imagem_view(request, obj.imagem.name, redirect)
    
admin.site.register(Parceiro, ParceiroAdmin)