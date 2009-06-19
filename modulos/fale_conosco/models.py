#-*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.db.models import signals
from django.contrib.auth.models import User
import os

try:
    import Image
except ImportError:
    try:
        from micro.modulos.PIL import Image
    except ImportError:
        raise ImportError((u"Fale Conosco não conseguiu importar a biblioteca de imagem do Python (Python Imaging Library)."))


class PaginaFaleConosco(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = True, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = True, null = True, help_text = "")
    texto_sam = models.CharField(u"Texto SAM", max_length = 255, blank = False, null = True, help_text = "")
    texto_departamentos = models.CharField(u"Texto Departamentos", max_length = 255, blank = False, null = True, help_text = "")
    texto_contato = models.CharField(u"Texto Contato", max_length = 255, blank = False, null = True, help_text = "")
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Fale Conosco"
        verbose_name_plural = "Pagina Fale Conosco"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""
    
class PaginaSAM(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = True, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = True, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = True, null = True, help_text = "")    
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina SAM"
        verbose_name_plural = "Pagina SAM"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""    
    
class PaginaContato(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = True, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = True, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = True, null = True, help_text = "")    
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Contato"
        verbose_name_plural = "Pagina Contato"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u"" 
    
class PaginaDepartamentos(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = True, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = True, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank =True, null = True, help_text = "")    
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Departamentos"
        verbose_name_plural = "Pagina Departamentos"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""  
    
   