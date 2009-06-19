#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import PaginaAplicativos, PaginaCatalogos, PaginaManuais, PaginaSuporte, Manuais, Pergunta
from micro.modulos.site_config.models import SiteConfig
from micro.modulos.produtos.models import Categoria

#Sombreamento do Admin
def sombreamento_pagina_aplicativos(request):
    pagina, criado = PaginaAplicativos.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/suporte/paginaaplicativos/1/')

def sombreamento_pagina_catalogos(request):
    pagina, criado = PaginaCatalogos.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/suporte/paginacatalogos/1/')

def sombreamento_pagina_manuais(request):
    pagina, criado = PaginaManuais.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/suporte/paginamanuais/1/')

def sombreamento_pagina_suporte(request):
    pagina, criado = PaginaSuporte.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/suporte/paginasuporte/1/')

#VIews do site
def catalogos_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaSuporte.objects.get(id = 1)
    perguntas = Pergunta.objects.order_by('-data').all()[:10]
    categorias = Categoria.objects.all()
    variaveis = RequestContext(request, {'config': config, 'pagina': pagina, 'perguntas': perguntas, 'categorias': categorias})
    return render_to_response('suporte_catalogos.html', variaveis)

def manuais_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaSuporte.objects.get(id = 1)
    perguntas = Pergunta.objects.order_by('-data').all()[:10]
    categorias = Categoria.objects.all()
    variaveis = RequestContext(request, {'config': config, 'pagina': pagina, 'perguntas': perguntas, 'categorias': categorias})
    return render_to_response('suporte_manuais.html', variaveis)

def suporte_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaSuporte.objects.get(id = 1)
    perguntas = Pergunta.objects.order_by('-data').all()[:10]
    variaveis = RequestContext(request, {'config': config, 'pagina': pagina, 'perguntas': perguntas})
    return render_to_response('suporte.html', variaveis)

def perguntas_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaSuporte.objects.get(id = 1)
    perguntas = Pergunta.objects.order_by('-data').all()
    variaveis = RequestContext(request, {'config': config, 'pagina': pagina, 'perguntas': perguntas})
    return render_to_response('suporte_faq.html', variaveis)


    
