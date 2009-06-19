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
        from micro.modulos.PIL import Image
    except ImportError:
        raise ImportError((u"A Microsol não conseguiu importar a biblioteca de imagem do Python (Python Imaging Library)."))


class PaginaAMicrosol(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = False, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = False, null = True, help_text = "")
    texto_a_empresa = models.CharField(u"Texto A Empresa", max_length = 255, blank = False, null = True, help_text = "")
    texto_conheca = models.CharField(u"Texto Conheça", max_length = 255, blank = False, null = True, help_text = "")
    texto_qualidade_e_premios = models.CharField(u"Texto Qualidade e Prêmios", max_length = 255, blank = False, null = True, help_text = "")
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina A Microsol"
        verbose_name_plural = "Pagina A Microsol"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""
    
class PaginaAEmpresa(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = False, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = True, null = True, help_text = "")
    texto_filiais = models.TextField(u"Texto Filiais", blank = True, null = True, help_text = "")
    imagem_filiais = models.ImageField(u"Imagem Filiais", upload_to = "img", blank = True, null = True, help_text = "")    
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina A Empresa"
        verbose_name_plural = "Pagina A Empresa"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""   
    
class PaginaConheca(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = False, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = True, null = True, help_text = "")
    galeria = models.ForeignKey(Galeria, verbose_name = "Galeria", related_name = "conheca_galeria", blank = True, null = True)
    arquivo = models.FileField(u"Arquivo", upload_to = "arquivos", blank = True, null = True, help_text = "")
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Conheça"
        verbose_name_plural = "Pagina Conheça"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""      
    
class PaginaQualidadeEPremios(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = False, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = True, null = True, help_text = "")
    galeria = models.ForeignKey(Galeria, verbose_name = "Galeria", related_name = "qualidade_galeria", blank = True, null = True)    
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")
    
    class Meta:
        verbose_name = "Pagina Qualidade e Prêmios"
        verbose_name_plural = "Pagina Qualidade e Prêmios"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""     
    
