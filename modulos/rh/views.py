#-*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from models import PaginaRecursosHumanos, Curriculo
from forms import FormCurriculo, FormCurriculoFoto
from micro.modulos.site_config.models import SiteConfig
from datetime import date
import random
import Image

#Sombreamento do Admin
def sombreamento_pagina_rh(request):
    pagina, criado = PaginaRecursosHumanos.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/rh/paginarecursoshumanos/1/')

#VIews do site
def cropar_foto_view(request, id_curriculo = False):
    curriculo = Curriculo.objects.get(codigo_cadastro = id_curriculo)
    imagem_cropada = False
    if request.method == "POST":
        crop_dimensao = (int(request.POST['x']), int(request.POST['y']), int(request.POST['x2']), int(request.POST['y2']))
        imagem_caminho = "%s/%s" % (settings.MEDIA_ROOT, curriculo.foto)
        imagem = Image.open(imagem_caminho)       
        imagem_crop = imagem.crop(crop_dimensao)
        imagem_crop.save(imagem_caminho, imagem.format)
        imagem_cropada = True
    variaveis = RequestContext(request, {'curriculo': curriculo, 'imagem_cropada': imagem_cropada})
    return render_to_response('rh_crop.html', variaveis)

def editar_foto_view(request, id_curriculo = False):
    if id_curriculo:
        try:
            curriculo = Curriculo.objects.get(codigo_cadastro = id_curriculo)
        except Curriculo.DoesNotExist:    
            try:
                curriculo = Curriculo.objects.get(codigo_cadastro = "curriculo-cadastro")
            except Curriculo.DoesNotExist:
                curriculo = Curriculo()
                curriculo.codigo_cadastro = "curriculo-cadastro"
                curriculo.save()    
        formulario = FormCurriculoFoto(instance = curriculo)
    if request.method == "POST":
        formulario = FormCurriculoFoto(request.POST, request.FILES, instance = curriculo)
        if formulario.is_valid():
            instancia = formulario.save()
            return HttpResponseRedirect('/rh/cropar/%s/' % instancia.codigo_cadastro)
    variaveis = RequestContext(request, {'curriculo': curriculo, 'formulario': formulario})
    return render_to_response('rh_upload_foto.html', variaveis)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/rh/")    

def rh_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaRecursosHumanos.objects.get(id = 1)
    mensagem = ""
    usuario = request.user
    if usuario.is_authenticated:
        try:
            curriculo = Curriculo.objects.get(usuario = usuario)
        except Curriculo.DoesNotExist:
            curriculo = None
    else:
        curriculo = None
    if request.method == "POST":
        usuario = authenticate(username = request.POST['usuario'], password = request.POST['senha'])
        if usuario:
            if usuario.is_active:
                login(request, usuario)
                curriculo = Curriculo.objects.get(usuario = usuario)
                return HttpResponseRedirect("/rh/curriculo/%s/" % curriculo.codigo_cadastro)
            else:
                mensagem = "Sua conta esta bloqueada."
        else:
            mensagem = "Dados de login invalidos."
    variaveis = RequestContext(request, {'pagina': pagina, 'config': config, 'mensagem': mensagem, 'curriculo': curriculo})
    return render_to_response('rh.html', variaveis)

def rh_curriculo_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaRecursosHumanos.objects.get(id = 1)
    cadastrado = False
    novo_cadastro = FormCurriculo()
    if request.method == "POST":
        novo_usuario = User()
        novo_usuario.username = request.POST['login']
        novo_usuario.set_password(request.POST['senha'])
        novo_usuario.save()
        nascimento = date(int(request.POST['ano']), int(request.POST['mes']), int(request.POST['dia']))
        telefone = "%s%s" % (request.POST['ddd_telefone'], request.POST['telefone'])
        celular = "%s%s" % (request.POST['ddd_celular'], request.POST['celular'])  
        novo_cadastro = FormCurriculo(request.POST)
        if novo_cadastro.is_valid():
            novo_objeto = novo_cadastro.save()
            novo_objeto.telefone = telefone
            novo_objeto.nascimento = nascimento
            novo_objeto.celular = celular
            novo_objeto.usuario = novo_usuario
            caracteres = "abcdefghijklmnopqrstuvxzwy1234567890ABCDEFGHIJKLMNOPQRSTUVXZKWY"
            codigo_cadastro = ""
            for letra in range(1, 16):
                codigo_cadastro += caracteres[random.randint(0, 60)]
            novo_objeto.codigo_cadastro = codigo_cadastro
            novo_objeto.save()
            cadastrado = True        
    variaveis = RequestContext(request, {'formulario': novo_cadastro, 'pagina': pagina, 'config': config, 'cadastrado': cadastrado})
    return render_to_response('rh_form.html', variaveis)

def rh_curriculo_editar_view(request, id_curriculo = False):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaRecursosHumanos.objects.get(id = 1)
    curriculo = Curriculo.objects.get(codigo_cadastro = id_curriculo)
    formulario = FormCurriculo(instance = curriculo)                                                      
    editado = False
    if request.method == "POST":        
        nascimento = date(int(request.POST['ano']), int(request.POST['mes']), int(request.POST['dia']))
        telefone = "%s%s" % (request.POST['ddd_telefone'], request.POST['telefone'])
        celular = "%s%s" % (request.POST['ddd_celular'], request.POST['celular'])
        formulario = FormCurriculo(request.POST, instance = curriculo)
        if formulario.is_valid():
            novo_objeto = formulario.save()
            novo_objeto.telefone = telefone
            novo_objeto.nascimento = nascimento
            novo_objeto.celular = celular
            novo_objeto.save()
            editado = True        
    variaveis = RequestContext(request, {'formulario': formulario, 'pagina': pagina, 'config': config, 'editado': editado, 'curriculo': curriculo})
    return render_to_response('rh_form_editar.html', variaveis)    


