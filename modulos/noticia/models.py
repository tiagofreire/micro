#-*- coding: utf-8 -*-
from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from django.conf import settings
import os

#Importa a biblioteca grafica do Python (PIL - Python Imaging Library)
try:
    import Image
except ImportError:
    try:
        from micro.modulos.PIL import Image
    except ImportError:
        raise ImportError(("Noticia n\u00E3o conseguiu importar a biblioteca de imagem do Python (Python Imaging Library)."))
   
class Noticia(models.Model):   
    titulo = models.CharField(u"Titulo", max_length = 32, blank = False, null = False)
    titulo_slug = models.SlugField(u"Slug titulo",blank = False, null = False, help_text = "Slug devem ser composto apenas de letras minusculas, '_' e numeros.")
    chamada = models.CharField(u"Chamada", max_length = 255, blank = True, null = True)
    imagem = models.ImageField(u"Imagem", upload_to = 'img/noticias', blank = True, null = True)
    texto = models.TextField(u"Texto", blank = False, null = False)
    data = models.DateTimeField(auto_now_add = True, blank = True, null = True)
    autor = models.ForeignKey(User, blank = True, null = True, related_name = "Noticia-User")
    publicada = models.BooleanField(blank = True, null = True, default = True, help_text = "Apenas noticias publicadas ser\u00E3o mostradas no site.")

    class Meta:
        verbose_name = u"Notícia"
        verbose_name_plural = u"Notícias"    
    
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
        thumbnail_path = "%s/img/noticias/thumbnails/admin_%s" % (settings.MEDIA_ROOT, self.imagem.name[13:]) 
        dimensoes = (32, 32)
        thumbnail = foto.resize(dimensoes, Image.ANTIALIAS)
        thumbnail.save(thumbnail_path, foto.format)
        
    def criar_miniatura_padrao(self):
        foto = Image.open(self.imagem.path)
        thumbnail_path = "%s/img/noticias/thumbnails/padrao_%s" % (settings.MEDIA_ROOT, self.imagem.name[13:]) 
        dimensoes = (64, 128)
        thumbnail = foto.resize(dimensoes, Image.ANTIALIAS)
        thumbnail.save(thumbnail_path, foto.format)    
        
    def padrao_thumbnail(self) :
        return u'%simg/noticias/thumbnails/padrao_%s' % (settings.MEDIA_URL, self.imagem.name[13:])  
        
    def admin_thumbnail(self) :
        return u'<a href="%simg/noticias/%s" class="fancy_trigger"><img src="%simg/noticias/thumbnails/admin_%s"/></a>' % (settings.MEDIA_URL, self.imagem.name[13:], settings.MEDIA_URL, self.imagem.name[13:])
    admin_thumbnail.short_description = 'Imagem'
    admin_thumbnail.allow_tags = True
    
    def deletar_miniaturas(self):
        try:
            thumbnail_dir = "%s/img/noticias/thumbnails/" % settings.MEDIA_ROOT
            thumbnail_file = "%admin_%s" % (32, 32, self.imagem.name[13:])
            os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
            thumbnail_file = "%padrao_%s" % (64, 128, self.imagem.name[13:])
            os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
        except Exception:
            pass
        
#===================================== Signals ====================================================================================
def post_delete_noticia(signal, instance, sender, **kwargs):
    instance.deletar_miniaturas()    
signals.pre_delete.connect(post_delete_noticia, sender = Noticia)

        

