#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import PaginaContato, PaginaDepartamentos, PaginaFaleConosco, PaginaSAM
from micro.modulos.site_config.models import SiteConfig

#Sombreamento do Admin
def sombreamento_pagina_fale_conosco(request):
    pagina, criado = PaginaFaleConosco.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/fale_conosco/paginafaleconosco/1/')

def sombreamento_pagina_contato(request):
    pagina, criado = PaginaContato.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/fale_conosco/paginacontato/1/')

def sombreamento_pagina_sam(request):
    pagina, criado = PaginaSAM.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/fale_conosco/paginasam/1/')

def sombreamento_pagina_departamentos(request):
    pagina, criado = PaginaDepartamentos.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/fale_conosco/paginadepartamentos/1/')

#VIews do site
def fale_conosco_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaFaleConosco.objects.get(id = 1)
    variaveis = RequestContext(request, {'pagina': pagina, 'config': config})
    return render_to_response('fale_conosco.html', variaveis)

def sam_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaSAM.objects.get(id = 1)
    enviado = False
    if request.method == "POST":
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = "%s%s" % (request.POST['ddd'], request.POST['telefone'])
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        sexo = request.POST['sexo']
        tipo = request.POST['tipo']
        mensagem = request.POST['mensagem']
        corpo_email = """
            Nome: %s
            Email: %s
            Telefone: %s
            Cidade: %s
            Estado: %s
            Sexo: %s
            Tipo: %s
            Mensagem: %s
        """ % (nome, email, telefone, cidade, estado, sexo, tipo, mensagem)
        send_mail("Serviço de Atendimento Microsol", corpo_email, "microsol@sam.com.br", ("ronaldo.moura@microsol.com.br", ), fail_silently = False)
        enviado = True
    variaveis = RequestContext(request, {'pagina': pagina, 'config': config, 'enviado': enviado})
    return render_to_response('fale_conosco_sam.html', variaveis)

def contato_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaContato.objects.get(id = 1)
    enviado = False
    if request.method == "POST":
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = "%s%s" % (request.POST['ddd'], request.POST['telefone'])
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        setor = request.POST['setor']
        mensagem = request.POST['mensagem']
        corpo_email = """
            Nome: %s
            Email: %s
            Telefone: %s
            Cidade: %s
            Estado: %s
            Setor: %s
            Mensagem: %s
        """ % (nome, email, telefone, cidade, estado, setor, mensagem)
        send_mail("Serviço de Atendimento Microsol", corpo_email, "microsol@sam.com.br", ("ronaldo.moura@microsol.com.br", ), fail_silently = False)
        enviado = True
    variaveis = RequestContext(request, {'pagina': pagina, 'config': config, 'enviado': enviado})
    return render_to_response('fale_conosco_contato.html', variaveis)
    
