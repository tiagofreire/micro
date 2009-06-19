#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import PaginaCatalogos
from micro.modulos.site_config.models import SiteConfig
from django.template.defaultfilters import slugify
from micro.modulos.index_gallery.models import Galeria

#Sombreamento do Admin
def sombreamento_pagina_catalogos(request):
    pagina, criado = PaginaCatalogos.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/catalogo/paginacatalogos/1/')

#VIews do site
def catalogo_view(request, id_galeria = None):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaCatalogos.objects.get(id = 1)
    if id_galeria:
        catalogo = Galeria.objects.get(nome_slug = id_galeria)
        xml = "%s.xml" % slugify(catalogo.nome)
        titulo = catalogo.nome
    else:
        xml = "%s.xml" % slugify(pagina.catalogo_destaque.nome)
        titulo = pagina.catalogo_destaque.nome
    variaveis = RequestContext(request, {'config': config, 'pagina': pagina, 'titulo': titulo, 'xml': xml})
    return render_to_response('catalogo.html', variaveis)
    
