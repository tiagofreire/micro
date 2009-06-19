#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import PaginaHotsites, PaginaManualDaMarca, ManualDaMarca, PaginaMidia, PaginaPublicidade, PaginaInformativo, Noticia, Hotsite, Publicidade
from micro.modulos.site_config.models import SiteConfig
from django.core.paginator import Paginator, EmptyPage, InvalidPage

#Sombreamento do Admin
def sombreamento_pagina_hotsites(request):
    pagina, criado = PaginaHotsites.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/midia/paginahotsites/1/')

def sombreamento_pagina_manual_da_marca(request):
    pagina, criado = PaginaManualDaMarca.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/midia/paginamanualdamarca/1/')

def sombreamento_pagina_midia(request):
    pagina, criado = PaginaMidia.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/midia/paginamidia/1/')

def sombreamento_pagina_publicidade(request):
    pagina, criado = PaginaPublicidade.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/midia/paginapublicidade/1/')

def sombreamento_pagina_informativo(request):
    pagina, criado = PaginaInformativo.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/midia/paginainformativo/1/')

#VIews do site
def midia_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaMidia.objects.get(id = 1)
    noticias = Noticia.objects.order_by('-data').all()[:10]
    variaveis = RequestContext(request, {'pagina': pagina, 'noticias': noticias, 'config': config})
    return render_to_response('midia.html', variaveis)

def informativo_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaInformativo.objects.get(id = 1)
    noticias = Noticia.objects.order_by('-data').all()[:10]
    variaveis = RequestContext(request, {'pagina': pagina, 'noticias': noticias, 'config': config})
    return render_to_response('informativo.html', variaveis)

def noticias_view(request, pagina):
    config = SiteConfig.objects.get(id = 1)
    noticias_all = Noticia.objects.order_by('-data').all()[:10]
    POR_PAGINA = 4
    paginacao = Paginator(noticias_all, POR_PAGINA)
    try:
        noticias = paginacao.page(int(pagina))
    except (EmptyPage, InvalidPage):
        noticias = paginacao.page(paginacao.num_pages)
    if paginacao.num_pages > 1:
        paginar = True
    else:
        paginar = False
        
    paginas = paginacao.page_range
    if (int(pagina) + 2) <= (len(paginas)):
        paginas_apos = int(pagina) + 2
    else:
        paginas_apos = int(pagina)
    if (int(pagina) - 2) >= 1:
        paginas_antes = int(pagina) - 2
    else:
        paginas_antes = 1
    variaveis = RequestContext(request, {'pagina_atual': int(pagina), 'paginas_apos': paginas_apos, 'paginas_antes': paginas_antes, 'noticias': noticias, 'config': config, 'paginar': paginar, 'paginas':paginas})
    return render_to_response('noticias.html', variaveis)

def noticia_view(request, titulo_slug):
    config = SiteConfig.objects.get(id = 1)
    noticia = Noticia.objects.get(titulo_slug = titulo_slug)
    noticias = Noticia.objects.order_by('-data').all()
    variaveis = RequestContext(request, {'noticias': noticias, 'noticia': noticia, 'config': config})
    return render_to_response('noticia.html', variaveis)

def hotsites_view(request):
    config = SiteConfig.objects.get(id = 1)
    hotsites = Hotsite.objects.order_by('-data').all()
    pagina = PaginaHotsites.objects.get(id = 1)
    variaveis = RequestContext(request, {'hotsites': hotsites, 'pagina': pagina})
    return render_to_response('hotsites.html', variaveis)

def manual_da_marca_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaManualDaMarca.objects.get(id = 1)
    manuais_da_marca = ManualDaMarca.objects.order_by('-data').all()
    variaveis = RequestContext(request, {'manuais_da_marca': manuais_da_marca, 'pagina': pagina})
    return render_to_response('manual_da_marca.html', variaveis)

def publicidade_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaPublicidade.objects.get(id = 1)
    publicidades = Publicidade.objects.order_by('-data').all()
    variaveis = RequestContext(request, {'publicidades': publicidades, 'pagina': pagina})
    return render_to_response('publicidade.html', variaveis)

def teste_aplicativo(request):
    variaveis = RequestContext(request, {})
    return render_to_response('teste_aplicativo.html', variaveis)
    
