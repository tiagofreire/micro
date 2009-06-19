#-*-coding: utf-8 -*-
from django.conf import settings
from django import template
from django.template import Context
from micro.modulos.index_gallery.models import Tamanho, Galeria

register = template.Library()

#Devolve o caminho que aponta para a miniatura indicada da foto.
def pegar_miniatura(foto, nome_miniatura):
    miniatura = Tamanho.objects.get(nome = nome_miniatura)
    nome_foto = foto.arquivo.name[len(settings.INDEX_GALLERY_ROOT):]
    return "%s%sthumbnails/%sx%s_%s" % (settings.MEDIA_URL, settings.INDEX_GALLERY_ROOT, miniatura.largura, miniatura.altura, nome_foto)
register.simple_tag(pegar_miniatura)

def pegar_galeria(nome_galeria):
    galeria = Galeria.objects.get(nome = nome_galeria)
    variaveis = Context({'MEDIA_URL': settings.MEDIA_URL, 'galeria': galeria})
    return variaveis
register.inclusion_tag('galeria.html')(pegar_galeria)
    