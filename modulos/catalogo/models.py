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
        raise ImportError((u"Catálogo não conseguiu importar a biblioteca de imagem do Python (Python Imaging Library)."))

class PaginaCatalogos(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    catalogos = models.ManyToManyField(Galeria, verbose_name = u"Catalógos", related_name = "catalogoi_galerias", blank = True, null = True)  
    catalogo_destaque = models.ForeignKey(Galeria, verbose_name = u"Catalógo Principal", related_name = "catalogoi_galeria", blank = True, null = True)
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
    
    def catalogos_ordenados(self):
        return self.catalogos.order_by('ordem').all()
    


