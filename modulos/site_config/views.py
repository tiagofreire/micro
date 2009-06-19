#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import SiteConfig, HomePage
from micro.modulos.midia.models import Noticia

def teste_pdf_view(request):
    raise Exception("TESTE")

#Views de sombreamento do admin
def sombreamento_siteconfig(request):
    SiteConfig.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/site_config/siteconfig/1/')

def sombreamento_homepage(request):
    HomePage.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/site_config/homepage/1/')

#Views do front-end do site
def home_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = HomePage.objects.get(id = 1)
    noticias = Noticia.objects.order_by('-data').all()[:pagina.noticias_listadas]
    variaveis = RequestContext(request, {'config': config, 'pagina': pagina, 'noticias': noticias})
    return render_to_response('index.html', variaveis)

def microsol_e_voce_view(request):
    variaveis = RequestContext(request, {})
    return render_to_response('microsol_e_voce.html', variaveis)
    
