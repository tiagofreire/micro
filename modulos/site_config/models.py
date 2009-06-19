#-*- coding: utf-8 -*-
from django.db import models

class HomePage(models.Model):
    area_i_imagem = models.ImageField("Imagem", upload_to = "img", blank = True, null = True, help_text = "")
    area_i_titulo = models.CharField("Titulo", max_length = 96, blank = True, null = True, help_text = "")
    area_i_texto = models.CharField("Texto", max_length = 255, blank = True, null = True, help_text = "")
    area_ii_imagem = models.ImageField("Imagem", upload_to = "img", blank = True, null = True, help_text = "")
    area_ii_titulo = models.CharField("Titulo", max_length = 96, blank = True, null = True, help_text = "")
    area_ii_texto = models.CharField("Texto", max_length = 255, blank = True, null = True, help_text = "")
    area_iii_imagem = models.ImageField("Imagem", upload_to = "img", blank = True, null = True, help_text = "")
    area_iii_titulo = models.CharField("Titulo", max_length = 96, blank = True, null = True, help_text = "")
    area_iii_texto = models.CharField("Texto", max_length = 255, blank = True, null = True, help_text = "")
    video_imagem = models.ImageField("Imagem", upload_to = "img", blank = True, null = True, help_text = "")
    video_titulo = models.CharField("Titulo", max_length = 96, blank = True, null = True, help_text = "")
    blog_imagem = models.ImageField("Imagem", upload_to = "img", blank = True, null = True, help_text = "")
    blog_titulo = models.CharField("Titulo", max_length = 96, blank = True, null = True, help_text = "")
    newslleter_imagem = models.ImageField("Imagem", upload_to = "img", blank = True, null = True, help_text = "")
    newslleter_titulo = models.CharField("Titulo", max_length = 96, blank = True, null = True, help_text = "")
    newslleter_texto = models.CharField("Texto", max_length = 255, blank = True, null = True, help_text = "")
    banner = models.FileField("Banner", upload_to = "swf", blank = True, null = True, help_text = "Arquivo .swf")
    noticias_listadas = models.IntegerField("Últimas Notícias", max_length = 12, default = 5, blank = True, null = True, help_text = "Quantidadas de notícias exibidas.")
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")
    
    def __str__(self):
        return ""
    
    def __unicode__(self):
        return ""


class SiteConfig(models.Model):
    google_analytics_user = models.CharField(max_length = 96, blank = True, null = True, help_text = "")
    
    class Meta:
        verbose_name = u"Configurar Site"
        verbose_name_plural = u"Configurar Site"
    
    def __str__(self) :
        return "%s" % ""

    def __unicode__(self) :
        return "%s" % ""