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
        raise ImportError((u"Midia não conseguiu importar a biblioteca de imagem do Python (Python Imaging Library)."))


class PaginaMidia(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = False, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = False, null = True, help_text = "")
    texto_publicidade = models.CharField(u"Texto Publicidade", max_length = 255, blank = False, null = True, help_text = "")
    texto_hotsites = models.CharField(u"Texto Publicidade", max_length = 255, blank = False, null = True, help_text = "")
    texto_manual_da_marca = models.CharField(u"Texto Publicidade", max_length = 255, blank = False, null = True, help_text = "")
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Mídia"
        verbose_name_plural = "Pagina Mídia"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""
    
class PaginaPublicidade(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = True, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = True, null = True, help_text = "")    
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Publicidade"
        verbose_name_plural = "Pagina Publicidade"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""    
    
class PaginaHotsites(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = True, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = True, null = True, help_text = "")    
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Hotsites"
        verbose_name_plural = "Pagina Hotsites"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u"" 
    
class PaginaManualDaMarca(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = True, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = True, null = True, help_text = "")    
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Manual da Marca"
        verbose_name_plural = "Pagina Manual da Marca"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""     
    
class PaginaInformativo(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = True, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = True, null = True, help_text = "")    
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Informativo"
        verbose_name_plural = "Pagina Informativo"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""     
    
class Publicidade(models.Model):
    titulo = models.CharField("Nome", max_length = 96, blank = True, null = True, help_text = "") 
    video = models.TextField("Video", blank = True, null = True, help_text = u"Embbed do youtube.") 
    imagem = models.ImageField("Imagem", upload_to = "img/publicidade", blank = True, null = True, help_text = "")
    data = models.DateTimeField("Adicionado em", auto_now_add = True, blank = True, null = True)
    autor = models.ForeignKey(User, blank = True, null = True, related_name = "publicidade_user")
    
    class Meta:
        verbose_name = u"Publicidade"
        verbose_name_plural = u"Publicidades"
        
    def __str__(self):
        return u"%s" % self.titulo
    
    def __unicode__(self):
        return u"%s" % self.titulo
    
    def criar_miniaturas(self):
        if self.imagem:
            self.criar_miniatura_admin()
            self.criar_miniatura_padrao()
    
    def criar_miniatura_admin(self):
        foto = Image.open(self.imagem.path)
        thumbnail_path = "%simg/publicidade/thumbnails/admin_%s" % (settings.MEDIA_ROOT, self.imagem.name[16:]) 
        dimensoes = (32, 32)
        thumbnail = foto.resize(dimensoes, Image.ANTIALIAS)
        thumbnail.save(thumbnail_path, foto.format)
        
    def criar_miniatura_padrao(self):
        foto = Image.open(self.imagem.path)
        thumbnail_path = "%simg/publicidade/thumbnails/padrao_%s" % (settings.MEDIA_ROOT, self.imagem.name[16:]) 
        dimensoes = (64, 64)
        thumbnail = foto.resize(dimensoes, Image.ANTIALIAS)
        thumbnail.save(thumbnail_path, foto.format)    
        
    def padrao_thumbnail(self) :
        return u'%simg/publicidade/thumbnails/padrao_%s' % (settings.MEDIA_URL, self.imagem.name[16:])  
        
    def admin_thumbnail(self) :
        return u'<a href="%simg/publicidade/%s" class="fancy_trigger"><img src="%simg/publicidade/thumbnails/admin_%s"/></a>' % (settings.MEDIA_URL, self.imagem.name[16:], settings.MEDIA_URL, self.imagem.name[16:])
    admin_thumbnail.short_description = 'Imagem'
    admin_thumbnail.allow_tags = True
    
    def deletar_miniaturas(self):
        try:
            thumbnail_dir = "%simg/publicidade/thumbnails/" % settings.MEDIA_ROOT
            thumbnail_file = "%admin_%s" % (32, 32, self.imagem.name[16:])
            os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
            thumbnail_file = "%padrao_%s" % (64, 128, self.imagem.name[16:])
            os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
        except Exception:
            pass  

class Noticia(models.Model):
    titulo = models.CharField(u"Título", max_length = 96, blank = False, null = True, help_text = "")    
    titulo_slug = models.SlugField(u"Título Slug", blank = False, null = True, help_text = "")    
    imagem = models.ImageField("Imagem", upload_to = "img/noticia", blank = True, null = True, help_text = "")
    texto = models.TextField("Texto", blank = True, null = False, help_text = "")
    data = models.DateTimeField("Adicionado em", auto_now_add = True, blank = True, null = True)
    autor = models.ForeignKey(User, blank = True, null = True, related_name = "noticia_user")
    
    class Meta:
        verbose_name = u"Noticia"
        verbose_name_plural = u"Noticias"
        
    def __str__(self):
        return u"%s" % self.titulo
    
    def __unicode__(self):
        return u"%s" % self.titulo
    
    def criar_miniaturas(self):
        if self.imagem:
            self.criar_miniatura_admin()
            self.criar_miniatura_padrao()
    
    def criar_miniatura_admin(self):
        foto = Image.open(self.imagem.path)
        thumbnail_path = "%simg/noticia/thumbnails/admin_%s" % (settings.MEDIA_ROOT, self.imagem.name[12:]) 
        dimensoes = (32, 32)
        thumbnail = foto.resize(dimensoes, Image.ANTIALIAS)
        thumbnail.save(thumbnail_path, foto.format)
        
    def criar_miniatura_padrao(self):
        foto = Image.open(self.imagem.path)
        thumbnail_path = "%simg/noticia/thumbnails/padrao_%s" % (settings.MEDIA_ROOT, self.imagem.name[12:]) 
        dimensoes = (64, 64)
        thumbnail = foto.resize(dimensoes, Image.ANTIALIAS)
        thumbnail.save(thumbnail_path, foto.format)    
        
    def padrao_thumbnail(self) :
        return u'%simg/noticia/thumbnails/padrao_%s' % (settings.MEDIA_URL, self.imagem.name[12:])  
        
    def admin_thumbnail(self) :
        return u'<a href="%simg/noticia/%s" class="fancy_trigger"><img src="%simg/noticia/thumbnails/admin_%s"/></a>' % (settings.MEDIA_URL, self.imagem.name[11:], settings.MEDIA_URL, self.imagem.name[11:])
    admin_thumbnail.short_description = 'Imagem'
    admin_thumbnail.allow_tags = True
    
    def deletar_miniaturas(self):
        try:
            thumbnail_dir = "%s/img/noticia/thumbnails/" % settings.MEDIA_ROOT
            thumbnail_file = "%admin_%s" % (32, 32, self.imagem.name[11:])
            os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
            thumbnail_file = "%padrao_%s" % (64, 128, self.imagem.name[11:])
            os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
        except Exception:
            pass   
        
class Hotsite(models.Model):
    titulo = models.CharField(u"Título", max_length = 96, blank = True, null = True, help_text = "")    
    imagem = models.ImageField("Imagem", upload_to = "img/hotsite", blank = True, null = True, help_text = "")
    texto = models.TextField("Texto", blank = True, null = False, help_text = "")
    url = models.URLField("URL", blank = True, null = True, help_text = u"ex: http://www.hotsite.com")
    data = models.DateTimeField("Adicionado em", auto_now_add = True, blank = True, null = True)
    autor = models.ForeignKey(User, blank = True, null = True, related_name = "hotsite_user")
    
    class Meta:
        verbose_name = u"Hotsite"
        verbose_name_plural = u"Hotsites"
        
    def __str__(self):
        return u"%s" % self.titulo
    
    def __unicode__(self):
        return u"%s" % self.titulo
    
    def criar_miniaturas(self):
        if self.imagem:
            self.criar_miniatura_admin()
            self.criar_miniatura_padrao()
    
    def criar_miniatura_admin(self):
        foto = Image.open(self.imagem.path)
        thumbnail_path = "%simg/hotsite/thumbnails/admin_%s" % (settings.MEDIA_ROOT, self.imagem.name[12:]) 
        dimensoes = (32, 32)
        thumbnail = foto.resize(dimensoes, Image.ANTIALIAS)
        thumbnail.save(thumbnail_path, foto.format)
        
    def criar_miniatura_padrao(self):
        foto = Image.open(self.imagem.path)
        thumbnail_path = "%simg/hotsite/thumbnails/padrao_%s" % (settings.MEDIA_ROOT, self.imagem.name[12:]) 
        dimensoes = (378, 182)
        thumbnail = foto.resize(dimensoes, Image.ANTIALIAS)
        thumbnail.save(thumbnail_path, foto.format)    
        
    def padrao_thumbnail(self) :
        return u'%simg/hotsite/thumbnails/padrao_%s' % (settings.MEDIA_URL, self.imagem.name[12:])  
        
    def admin_thumbnail(self) :
        return u'<a href="%simg/hotsite/%s" class="fancy_trigger"><img src="%simg/hotsite/thumbnails/admin_%s"/></a>' % (settings.MEDIA_URL, self.imagem.name[12:], settings.MEDIA_URL, self.imagem.name[12:])
    admin_thumbnail.short_description = 'Imagem'
    admin_thumbnail.allow_tags = True
    
    def deletar_miniaturas(self):
        try:
            thumbnail_dir = "%s/img/hotsite/thumbnails/" % settings.MEDIA_ROOT
            thumbnail_file = "%admin_%s" % (32, 32, self.imagem.name[12:])
            os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
            thumbnail_file = "%padrao_%s" % (64, 128, self.imagem.name[12:])
            os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
        except Exception:
            pass                  
        
class ManualDaMarca(models.Model):
    CATEGORIA_MANUAL = (
        ("Marca", "Marca"),
        ("Download", "Download"),
    ) 
    titulo = models.CharField(u"Título", max_length = 196, blank = False, null = True, help_text = "")
    arquivo = models.FileField(u"Arquivo", upload_to = "manual_da_marca", blank = False, null = True, help_text = "")
    categoria = models.CharField(u"Categoria", max_length = 196, choices = CATEGORIA_MANUAL, blank = True, null = True)
    data = models.DateTimeField("Adicionado em", auto_now_add = True, blank = True, null = True)
    autor = models.ForeignKey(User, blank = True, null = True, related_name = "manual_da_marca_user")
    
    class Meta:
        verbose_name = u"Manual da Marca"
        verbose_name_plural = u"Manuais da Marca"
        
    def __str__(self):
        return u"%s" % self.titulo
    
    def __unicode__(self):
        return u"%s" % self.titulo

#===================================== Signals ====================================================================================
def post_delete_publicidade(signal, instance, sender, **kwargs):
    instance.deletar_miniaturas()    
signals.pre_delete.connect(post_delete_publicidade, sender = Publicidade) 

def post_delete_hotsite(signal, instance, sender, **kwargs):
    instance.deletar_miniaturas()    
signals.pre_delete.connect(post_delete_hotsite, sender = Hotsite) 
 