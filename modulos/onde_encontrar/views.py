#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import PaginaAssitenciaTecnica, PaginaLojasOnline, PaginaOndeEncontrar, PaginaRevendas, LojaOnline
from micro.modulos.site_config.models import SiteConfig

#Sombreamento do Admin
def sombreamento_pagina_assistencia_tecnica(request):
    pagina, criado = PaginaAssitenciaTecnica.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/onde_encontrar/paginaassitenciatecnica/1/')

def sombreamento_pagina_lojas_online(request):
    pagina, criado = PaginaLojasOnline.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/onde_encontrar/paginalojasonline/1/')

def sombreamento_pagina_onde_encontrar(request):
    pagina, criado = PaginaOndeEncontrar.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/onde_encontrar/paginaondeencontrar/1/')

def sombreamento_pagina_revendas(request):
    pagina, criado = PaginaRevendas.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/onde_encontrar/paginarevendas/1/')

#VIews do site
def onde_encontrar_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaOndeEncontrar.objects.get(id = 1)
    variaveis = RequestContext(request, {'pagina': pagina, 'config': config})
    return render_to_response('onde_encontrar.html', variaveis)

def lojas_online_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaLojasOnline.objects.get(id = 1)
    lojas = LojaOnline.objects.order_by('-data').all()
    variaveis = RequestContext(request, {'pagina': pagina, 'lojas': lojas, 'config': config})
    return render_to_response('onde_encontrar_lojas_online.html', variaveis)
