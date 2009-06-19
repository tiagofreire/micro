#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils.html import strip_tags
from models import Email

def cadastrar_newsletter_ajax(request):
    try:
        email = strip_tags(request.POST['email'])
        nome = strip_tags(request.POST['nome'])
        try:
            cadastro = Email.objects.get(email = email)
            resposta = "email_existente"
        except Email.DoesNotExist:    
            novo_cadastro = Email()
            novo_cadastro.email = email
            novo_cadastro.nome = nome
            novo_cadastro.save()
            resposta = "sucesso" 
    except Exception:
        resposta = "falha" 
        pass
    return HttpResponse(resposta)
    
