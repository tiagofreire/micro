#-*- coding: utf-8 -*-
from django.db import models
from django.db.models import signals
from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import os

#Importa a biblioteca grafica do Python (PIL - Python Imaging Library)
try:
    import Image
except ImportError:
    try:
        from modulos.PIL import Image
    except ImportError:
        raise ImportError((u"Parceiros n\u00E3o conseguiu importar a biblioteca de imagem do Python (Python Imaging Library)."))
   
class Parceiro(models.Model):   
    nome = models.CharField(u"Titulo", max_length = 32, blank = False, null = False, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = 'img/parceiro', blank = True, null = True, help_text = "")
    link = models.URLField(u"Link", blank = True, null = True, help_text = "Caminho absoluto para a website do parceiro.")
    texto = models.TextField(u'Descri\u00E7\u00E3o', blank = True, null = True, help_text = u"Texto sobre a parceria.")

    class Meta:
        verbose_name = u"Parceiro"
        verbose_name_plural = u"Parceiros"    
    
    def __str__(self) :
        return "%s" % self.nome

    def __unicode__(self) :
        return "%s" % self.nome

    def criar_miniatura_admin(self):
        foto = Image.open(self.imagem.path)
        thumbnail_path = "%s/img/parceiro/thumbnails/%sx%s_%s" % (settings.MEDIA_ROOT, 32, 32, self.imagem.name[15:]) 
        dimensoes = (32, 32)
        foto.thumbnail(dimensoes, Image.ANTIALIAS)
        foto.save(thumbnail_path, foto.format)
        
    def criar_miniatura(self):
        foto = Image.open(self.imagem.path)
        thumbnail_path = "%s/img/parceiro/thumbnails/%sx%s_%s" % (settings.MEDIA_ROOT, 64, 128, self.imagem.name[15:]) 
        dimensoes = (64, 128)
        foto.thumbnail(dimensoes, Image.ANTIALIAS)
        foto.save(thumbnail_path, foto.format)    
        
    def admin_thumbnail(self) :
        return u'<a href="%simg/parceiro/%s" rel="lightbox"><img src="%simg/parceiro/thumbnails/32x32_%s"/></a>' % (settings.MEDIA_URL, self.imagem.name[15:], settings.MEDIA_URL, self.imagem.name[15:])
    admin_thumbnail.short_description = 'Imagem'
    admin_thumbnail.allow_tags = True
    
    def deletar_miniaturas(self):
        thumbnail_dir = "%s/img/parceiro/thumbnails/" % settings.MEDIA_ROOT
        thumbnail_file = "%sx%s_%s" % (32, 32, self.imagem.name[15:])
        os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
        thumbnail_file = "%sx%s_%s" % (64, 128, self.imagem.name[15:])
        os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
                
#===================================== Signals ====================================================================================

def post_delete_parceiro(signal, instance, sender, **kwargs):
    try:
        instance.deletar_miniaturas()    
    except WindowsError:
        pass
signals.pre_delete.connect(post_delete_parceiro, sender = Parceiro)

        

