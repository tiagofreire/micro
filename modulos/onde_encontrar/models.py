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
        raise ImportError((u"Onde Encontrar não conseguiu importar a biblioteca de imagem do Python (Python Imaging Library)."))


class PaginaOndeEncontrar(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = False, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = False, null = True, help_text = "")
    texto_revenda = models.CharField(u"Texto Revenda", max_length = 255, blank = False, null = True, help_text = "")
    texto_lojas_online = models.CharField(u"Texto Lojas Online", max_length = 255, blank = False, null = True, help_text = "")
    texto_assitencia_tecnica = models.CharField(u"Texto Assistência Técnica", max_length = 255, blank = False, null = True, help_text = "")
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Onde Encontrar"
        verbose_name_plural = "Pagina Onde Encontrar"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""
    
class PaginaRevendas(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = False, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = False, null = True, help_text = "")    
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Revendas"
        verbose_name_plural = "Pagina Revendas"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""    
    
class PaginaLojasOnline(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = False, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = False, null = True, help_text = "")    
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Lojas Online"
        verbose_name_plural = "Pagina Lojas Online"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u"" 
    
class PaginaAssitenciaTecnica(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = False, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = False, null = True, help_text = "")    
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Assitência Técnica"
        verbose_name_plural = "Pagina Assitência Técnica"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""
    
class LojaOnline(models.Model):   
    titulo = models.CharField(u"Titulo", max_length = 196, blank = False, null = False, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = 'img/loja_online', blank = True, null = True, help_text = "")
    link = models.URLField(u"Link", blank = True, null = True, help_text = "Caminho absoluto para a website da loja virtual.")
    email = models.EmailField(u'Email', blank = True, null = True, help_text = u"")
    data = models.DateTimeField("Adicionado em", auto_now_add = True, blank = True, null = True)
    autor = models.ForeignKey(User, blank = True, null = True, related_name = "loja_online_user")
    
    class Meta:
        verbose_name = u"Loja Online"
        verbose_name_plural = u"Lojas Online"    
    
    def __str__(self) :
        return "%s" % self.titulo

    def __unicode__(self) :
        return "%s" % self.titulo
    
    def criar_miniaturas(self):
        if self.imagem:
            self.criar_miniatura_admin()
            self.criar_miniatura_padrao()

    def criar_miniatura_admin(self):
        foto = Image.open(self.imagem.path)
        thumbnail_path = "%simg/loja_online/thumbnails/admin_%s" % (settings.MEDIA_ROOT, self.imagem.name[16:]) 
        dimensoes = (32, 32)
        foto.thumbnail(dimensoes, Image.ANTIALIAS)
        foto.save(thumbnail_path, foto.format)
        
    def criar_miniatura_padrao(self):
        foto = Image.open(self.imagem.path)
        thumbnail_path = "%simg/loja_online/thumbnails/padrao_%s" % (settings.MEDIA_ROOT, self.imagem.name[16:]) 
        dimensoes = (64, 128)
        foto.thumbnail(dimensoes, Image.ANTIALIAS)
        foto.save(thumbnail_path, foto.format)    
        
    def admin_thumbnail(self) :
        return u'<a href="%simg/loja_online/%s" class="fancy_trigger"><img src="%simg/loja_online/thumbnails/admin_%s"/></a>' % (settings.MEDIA_URL, self.imagem.name[16:], settings.MEDIA_URL, self.imagem.name[16:])
    admin_thumbnail.short_description = 'Imagem'
    admin_thumbnail.allow_tags = True
    
    def padrao_thumbnail(self) :
        return u'%simg/loja_online/thumbnails/padrao_%s' % (settings.MEDIA_URL, self.imagem.name[16:])  
    
    def deletar_miniaturas(self):
        thumbnail_dir = "%s/img/loja_online/thumbnails/" % settings.MEDIA_ROOT
        thumbnail_file = "%admin_%s" % (self.imagem.name[16:])
        os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
        thumbnail_file = "%padrao_%s" % (self.imagem.name[16:])
        os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
                
#===================================== Signals ====================================================================================

def post_delete_loja_online(signal, instance, sender, **kwargs):
    try:
        instance.deletar_miniaturas()    
    except Exception:
        pass
signals.pre_delete.connect(post_delete_loja_online, sender = LojaOnline)
    