#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import PaginaAMicrosol, PaginaAEmpresa, PaginaConheca, PaginaQualidadeEPremios
from micro.modulos.site_config.models import SiteConfig

#Sombreamento do Admin
def sombreamento_pagina_a_microsol(request):
    pagina, criado = PaginaAMicrosol.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/a_microsol/paginaamicrosol/1/')

def sombreamento_pagina_a_empresa(request):
    pagina, criado = PaginaAEmpresa.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/a_microsol/paginaaempresa/1/')

def sombreamento_pagina_conheca(request):
    pagina, criado = PaginaConheca.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/a_microsol/paginaconheca/1/')

def sombreamento_pagina_qualidade_e_premios(request):
    pagina, criado = PaginaQualidadeEPremios.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/a_microsol/paginaqualidadeepremios/1/')

#VIews do site
def a_microsol_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaAMicrosol.objects.get(id = 1)
    variaveis = RequestContext(request, {'pagina': pagina, 'config': config})
    return render_to_response('a_microsol.html', variaveis)

def a_empresa_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaAEmpresa.objects.get(id = 1)
    variaveis = RequestContext(request, {'pagina': pagina, 'config': config})
    return render_to_response('a_microsol_empresa.html', variaveis)

def conheca_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaConheca.objects.get(id = 1)
    variaveis = RequestContext(request, {'pagina': pagina, 'config': config})
    return render_to_response('a_microsol_conheca.html', variaveis)

def qualidade_e_premios_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaQualidadeEPremios.objects.get(id = 1)
    variaveis = RequestContext(request, {'pagina': pagina, 'config': config})
    return render_to_response('a_microsol_qualidadepremios.html', variaveis)

def aplicativo_view(request):
    config = SiteConfig.objects.get(id = 1)
    variaveis = RequestContext(request, {'config': config})
    return render_to_response('microsol_e_voce.html', variaveis)
    
