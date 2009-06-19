#-*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.db.models import signals
from django.contrib.auth.models import User
from micro.modulos.index_gallery.models import Galeria
import os

try:
    import Image
except ImportError:
    try:
        from modulos.PIL import Image
    except ImportError:
        raise ImportError((u"Suporte não conseguiu importar a biblioteca de imagem do Python (Python Imaging Library)."))


class PaginaSuporte(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = False, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = False, null = True, help_text = "")
    texto_manuais = models.CharField(u"Texto Manuais", max_length = 255, blank = False, null = True, help_text = "")
    texto_catalogos = models.CharField(u"Texto Catalogos", max_length = 255, blank = False, null = True, help_text = "")
    texto_aplicativos = models.CharField(u"Texto Aplicativos", max_length = 255, blank = False, null = True, help_text = "")
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Suporte"
        verbose_name_plural = "Pagina Suporte"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""
    
class PaginaManuais(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = False, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = False, null = True, help_text = "")    
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Manuais"
        verbose_name_plural = "Pagina Manuais"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""    
    
class PaginaCatalogos(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    catalogos = models.ManyToManyField(Galeria, verbose_name = u"Catalógos", related_name = "catalogo_galerias", blank = True, null = True)  
    catalogo_destaque = models.ForeignKey(Galeria, verbose_name = u"Catalógo Principal", related_name = "catalogo_galeria", blank = True, null = True)
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Catálogos"
        verbose_name_plural = "Pagina Catálogos"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u"" 
    
class PaginaAplicativos(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = False, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = False, null = True, help_text = "")    
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Aplicativos"
        verbose_name_plural = "Pagina Aplicativos"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""     
            
class Manuais(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    arquivo = models.FileField(u"Arquivo", upload_to = "manual", blank = False, null = True, help_text = "")
    data = models.DateTimeField("Adicionado em", auto_now_add = True, blank = True, null = True)
    autor = models.ForeignKey(User, blank = True, null = True, related_name = "manual_user")
    
    class Meta:
        verbose_name = u"Manuais"
        verbose_name_plural = u"Manuais"
        
    def __str__(self):
        return u"%s" % self.titulo
    
    def __unicode__(self):
        return u"%s" % self.titulo
    
class Pergunta(models.Model):
    pergunta = models.CharField(u"Pergunta", max_length = 196, blank = False, null = True, help_text = "")
    pergunta_slug = models.SlugField(u"Pergunta Slug", blank = False, null = True, help_text = "")
    resposta = models.TextField(u"Resposta", blank = False, null = True, help_text = "")
    data = models.DateTimeField("Adicionado em", auto_now_add = True, blank = True, null = True)
    autor = models.ForeignKey(User, blank = True, null = True, related_name = "pergunta_user")
    
    class Meta:
        verbose_name = u"Pergunta"
        verbose_name_plural = u"Perguntas"
        
    def __str__(self):
        return u"%s" % self.pergunta
    
    def __unicode__(self):
        return u"%s" % self.pergunta


