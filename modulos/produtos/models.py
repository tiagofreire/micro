#-*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.db.models import signals
from django.contrib.auth.models import User
from micro.modulos.index_gallery.models import Galeria
import os

#Importa a biblioteca grafica do Python (PIL - Python Imaging Library)
try:
    import Image
except ImportError:
    try:
        from micro.modulos.PIL import Image
    except ImportError:
        raise ImportError((u"Produtos não conseguiu importar a biblioteca de imagem do Python (Python Imaging Library)."))

class TipoAplicacao(models.Model):
    nome = models.CharField("Nome", max_length = 96, blank = True, null = True, help_text = "")    
    imagem = models.ImageField("Icone", upload_to = "img/produtos/aplicacoes", blank = True, null = True, help_text = "")
    data = models.DateTimeField(auto_now_add = True, blank = True, null = True)
    autor = models.ForeignKey(User, blank = True, null = True, related_name = "tipoaplicacao_user")
    
    class Meta:
        verbose_name = u"Tipo de Aplicação"
        verbose_name_plural = u"Tipos de Aplicações"
        
    def __str__(self):
        return u"%s" % self.nome
    
    def __unicode__(self):
        return u"%s" % self.nome
    
    def criar_miniaturas(self):
        if self.imagem:
            self.criar_miniatura_admin()
            self.criar_miniatura_padrao()
    
    def criar_miniatura_admin(self):
        foto = Image.open(self.imagem.path)
        thumbnail_path = "%s/img/produtos/aplicacoes/thumbnails/admin_%s" % (settings.MEDIA_ROOT, self.imagem.name[25:]) 
        dimensoes = (32, 32)
        thumbnail = foto.resize(dimensoes, Image.ANTIALIAS)
        thumbnail.save(thumbnail_path, foto.format)
        
    def criar_miniatura_padrao(self):
        foto = Image.open(self.imagem.path)
        thumbnail_path = "%s/img/produtos/aplicacoes/thumbnails/padrao_%s" % (settings.MEDIA_ROOT, self.imagem.name[25:]) 
        dimensoes = (64, 64)
        thumbnail = foto.resize(dimensoes, Image.ANTIALIAS)
        thumbnail.save(thumbnail_path, foto.format)    
        
    def padrao_thumbnail(self) :
        return u'%simg/produtos/aplicacoes/thumbnails/padrao_%s' % (settings.MEDIA_URL, self.imagem.name[25:])  
        
    def admin_thumbnail(self) :
        return u'<a href="%simg/produtos/aplicacoes/%s" class="fancy_trigger"><img src="%simg/produtos/aplicacoes/thumbnails/admin_%s"/></a>' % (settings.MEDIA_URL, self.imagem.name[25:], settings.MEDIA_URL, self.imagem.name[25:])
    admin_thumbnail.short_description = 'Imagem'
    admin_thumbnail.allow_tags = True
    
    def deletar_miniaturas(self):
        try:
            thumbnail_dir = "%s/img/produtos/aplicacoes/thumbnails/" % settings.MEDIA_ROOT
            thumbnail_file = "%admin_%s" % (32, 32, self.imagem.name[25:])
            os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
            thumbnail_file = "%padrao_%s" % (64, 128, self.imagem.name[25:])
            os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
        except Exception:
            pass
        
class Cor(models.Model):
    nome = models.CharField("Cor", max_length = 196, blank = False, null = True, help_text = "")
    
    class Meta:
        verbose_name = u"Cor"
        verbose_name_plural = u"Cores"
        
    def __str__(self):
        return u"%s" % self.nome
    
    def __unicode__(self):
        return u"%s" % self.nome
        
class Modelo(models.Model):
    TIPO_POTENCIA = (
        ('VA', 'VA'),
        ('W', 'W'),
        ('KVA', 'KVA'),
        ('AH', 'AH')
    )
    nome = models.CharField(u"Nome", max_length = 96, blank = True, null = True, help_text = "")
    potencia = models.FloatField(u"Potência", blank = True, null = True)
    tipo_potencia = models.CharField(u"Tipo da Potência", max_length = 96, choices = TIPO_POTENCIA, blank = True, null = True, help_text = "")
    fator_potencia = models.CharField(u"Fator de potência", max_length = 96, blank = True, null = True, help_text = "")
    entrada = models.CharField(u"Entrada", max_length = 96, blank = True, null = True, help_text = "(V)")
    saida = models.CharField(u"Saida", max_length = 96, blank = True, null = True, help_text = "(V)")
    sgm = models.BooleanField(u"SGM",blank = True, null = True, help_text = "")
    usb = models.BooleanField(u"USB",blank = True, null = True, help_text = "")
    protecao_fax_modem = models.BooleanField(u"Proteção Fax/Modem",blank = True, null = True, help_text = "")
    aplicacoes = models.ManyToManyField(TipoAplicacao, verbose_name = u"Aplicações", related_name = "modelo_aplicacao", blank = True, null = True, help_text = "")
    cores = models.ManyToManyField(Cor, verbose_name = "Cores", related_name = "modelo_cor", blank = True, null = True)
    data = models.DateTimeField(auto_now_add = True, blank = True, null = True)
    autor = models.ForeignKey(User, blank = True, null = True, related_name = "modelo_user")
    
    class Meta:
        verbose_name = u"Modelo de produto"
        verbose_name_plural = u"Modelos de produtos"
        
    def __str__(self):
        return u"%s" % self.nome
    
    def __unicode__(self):
        return u"%s" % self.nome
    
class Categoria(models.Model):
    nome = models.CharField("Nome", max_length = 98, blank = True, null = True)
    nome_slug = models.CharField("Nome Slug", max_length = 98, blank = True, null = True)
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return "%s" % self.nome
    
    def __unicode__(self):
        return "%s" % self.nome
    
class Caracteristica(models.Model):
    titulo = models.CharField("Título", max_length = 96, blank = False, null = True, help_text = "")    
    texto = models.TextField(u"Texto", blank = False, null = True, help_text = "")
    imagem = models.ImageField("Icone", upload_to = "img/produtos/caracteristica", blank = True, null = True, help_text = "")
    data = models.DateTimeField(auto_now_add = True, blank = True, null = True)
    autor = models.ForeignKey(User, blank = True, null = True, related_name = "caracteristica_user")
    
    class Meta:
        verbose_name = u"Caracteristica do Produto"
        verbose_name_plural = u"Caracteristicas dos Produtos"
        
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
        thumbnail_path = "%simg/produtos/caracteristica/thumbnails/admin_%s" % (settings.MEDIA_ROOT, self.imagem.name[28:]) 
        dimensoes = (32, 32)
        thumbnail = foto.resize(dimensoes, Image.ANTIALIAS)
        thumbnail.save(thumbnail_path, foto.format)
        
    def criar_miniatura_padrao(self):
        foto = Image.open(self.imagem.path)
        thumbnail_path = "%simg/produtos/caracteristica/thumbnails/padrao_%s" % (settings.MEDIA_ROOT, self.imagem.name[28:]) 
        dimensoes = (76, 79)
        thumbnail = foto.resize(dimensoes, Image.ANTIALIAS)
        thumbnail.save(thumbnail_path, foto.format)    
        
    def padrao_thumbnail(self) :
        return u'%simg/produtos/caracteristica/thumbnails/padrao_%s' % (settings.MEDIA_URL, self.imagem.name[28:])  
        
    def admin_thumbnail(self) :
        return u'<a href="%simg/produtos/caracteristica/%s" class="fancy_trigger"><img src="%simg/produtos/caracteristica/thumbnails/admin_%s"/></a>' % (settings.MEDIA_URL, self.imagem.name[28:], settings.MEDIA_URL, self.imagem.name[28:])
    admin_thumbnail.short_description = 'Imagem'
    admin_thumbnail.allow_tags = True
    
    def deletar_miniaturas(self):
        try:
            thumbnail_dir = "%simg/produtos/caracteristica/thumbnails/" % settings.MEDIA_ROOT
            thumbnail_file = "%admin_%s" % (32, 32, self.imagem.name[28:])
            os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
            thumbnail_file = "%padrao_%s" % (64, 128, self.imagem.name[28:])
            os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
        except Exception:
            pass
    
class Produto(models.Model):   
    nome = models.CharField(u"Nome", max_length = 96, blank = True, null = True, help_text = "")
    nome_slug = models.SlugField(u"Nome slug", blank = True, null = True, help_text = "")
    categoria = models.ForeignKey(Categoria,verbose_name = "Categoria", related_name = "produto_categoria", blank = True, null = True)
    logo = models.ImageField(u"Logomarca", upload_to = 'img/produtos', blank = True, null = True)
    potencia = models.IntegerField(u"Potência", default = 0, blank = True, null = False, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = 'img/produtos', blank = True, null = True)
    miniatura = models.ImageField(u"Miniatura", upload_to = 'img/produtos', blank = True, null = True)
    descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    modelos = models.ManyToManyField(Modelo, verbose_name = u"Modelos", related_name = "produto_modelo", blank = True, null = True, help_text = "")
    caracteristicas = models.ManyToManyField(Caracteristica, verbose_name = "Caracteristicas", related_name = "produto_caracteristica", blank = True, null = True, help_text = "")
    sgm = models.BooleanField(u"SGM",blank = True, null = True, help_text = "")
    hotsite = models.URLField(u"Hotsite", blank = True, null = True, help_text = "http://www.meusite.com")
    modulo_de_comunicacao = models.TextField(u"Modulo de comunicação", blank = True, null = True, help_text = "")
    funcoes_e_beneficios = models.TextField(u"Funções e Beneficios", blank = True, null = True, help_text = "") 
    manual = models.FileField(u"Manual", upload_to = "manuais", blank = True, null = True, help_text = "")
    catalogo = models.FileField(u"Catalogos", upload_to = "catalogos", blank = True, null = True, help_text = "")
    tour_360 = models.FileField(u"Tour 360", upload_to = "tour", blank = True, null = True, help_text = "")
    galeria = models.ForeignKey(Galeria, verbose_name = "Galeria", related_name = "produto_galeria", blank = True, null = True)
    produtos_semelhantes = models.ManyToManyField("Produto", verbose_name = "Produtos semelhantes", related_name = "produto_produto",blank = True, null = True)
    extra_i_nome = models.CharField('Nome', max_length = "96", blank = True, null = True, help_text = "")
    extra_i_texto = models.TextField('Texto', blank = True, null = True, help_text = "")
    extra_ii_nome = models.CharField('Nome', max_length = "96", blank = True, null = True, help_text = "")
    extra_ii_texto = models.TextField('Texto', blank = True, null = True, help_text = "")
    extra_iii_nome = models.CharField('Nome', max_length = "96", blank = True, null = True, help_text = "")
    extra_iii_texto = models.TextField('Texto', blank = True, null = True, help_text = "")
    data = models.DateTimeField("Adicionado em", auto_now_add = True, blank = True, null = True)
    autor = models.ForeignKey(User, blank = True, null = True, related_name = "produto_user")
    
    class Meta:
        verbose_name = u"Produto"
        verbose_name_plural = u"Produtos"
        
    def __str__(self):
        return u"%s" % self.nome
    
    def __unicode__(self):
        return u"%s" % self.nome
    
    def pegar_potencias(self):
        modelos_filtrados = []
        consta = False
        for modelo in self.modelos.all():
            for modelo_filtrado in modelos_filtrados:
                if modelo_filtrado.potencia == modelo.potencia:
                    consta = True
                    break
            if not consta:
                modelos_filtrados.append(modelo)
            consta = False
        return modelos_filtrados    
    
    def criar_miniaturas(self):
        if self.imagem:
            self.criar_miniatura_admin()
            self.criar_miniatura_padrao()
    
    def criar_miniatura_admin(self):
        foto = Image.open(self.imagem.path)
        thumbnail_path = "%s/img/produtos/thumbnails/admin_%s" % (settings.MEDIA_ROOT, self.imagem.name[13:]) 
        dimensoes = (32, 32)
        thumbnail = foto.resize(dimensoes, Image.ANTIALIAS)
        thumbnail.save(thumbnail_path, foto.format)
        
    def criar_miniatura_padrao(self):
        foto = Image.open(self.imagem.path)
        thumbnail_path = "%s/img/produtos/thumbnails/padrao_%s" % (settings.MEDIA_ROOT, self.imagem.name[13:]) 
        dimensoes = (76, 76)
        thumbnail = foto.resize(dimensoes, Image.ANTIALIAS)
        thumbnail.save(thumbnail_path, foto.format)    
        
    def padrao_thumbnail(self) :
        return u'%simg/produtos/thumbnails/padrao_%s' % (settings.MEDIA_URL, self.imagem.name[13:])  
        
    def admin_thumbnail(self) :
        return u'<a href="%simg/produtos/%s" class="fancy_trigger"><img src="%simg/produtos/thumbnails/admin_%s"/></a>' % (settings.MEDIA_URL, self.imagem.name[13:], settings.MEDIA_URL, self.imagem.name[13:])
    admin_thumbnail.short_description = 'Imagem'
    admin_thumbnail.allow_tags = True
    
    def admin_logo(self):
        if self.logo:
            return u"<img src='%s%s' />" % (settings.MEDIA_URL, self.logo) 
        else:
            return u"<img src='%simg/sem_imagem.jpg' />" % settings.MEDIA_URL 
    admin_logo.short_description = "Logomarca"
    admin_logo.allow_tags = True
    
    def admin_hotsite(self):
        return u"<a href='%s'>Visitar hostsite</a>" % self.hotsite
    admin_hotsite.short_description = "Hotsite"
    admin_hotsite.allow_tags = True
    
    def deletar_miniaturas(self):
        try:
            thumbnail_dir = "%s/img/produtos/thumbnails/" % settings.MEDIA_ROOT
            thumbnail_file = "%admin_%s" % (32, 32, self.imagem.name[13:])
            os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
            thumbnail_file = "%padrao_%s" % (64, 128, self.imagem.name[13:])
            os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
        except Exception:
            pass     
        
class Software(models.Model):
    nome = models.CharField(u"Nome", max_length = 96, blank = True, null = True, help_text = "")
    nome_slug = models.SlugField(u"Nome slug", blank = True, null = True, help_text = "")
    logo = models.ImageField(u"Logomarca", upload_to = 'img/produtos', blank = True, null = True)
    imagem = models.ImageField(u"Imagem", upload_to = 'img/produtos', blank = True, null = True)
    miniatura = models.ImageField(u"Miniatura", upload_to = 'img/produtos', blank = True, null = True)
    galeria = models.ForeignKey(Galeria, verbose_name = "Galeria", related_name = "software_galeria", blank = True, null = True, help_text = "")
    graficos = models.TextField(u"Graficos", blank = True, null = True, help_text = "")
    descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    notificacao = models.TextField(u"Notificação", blank = True, null = True, help_text = "")
    manual = models.FileField(u"Manual", upload_to = "manuais", blank = True, null = True, help_text = "")    
    comandos = models.TextField(u"Comandos", blank = True, null = True, help_text = "") 
    monitoramento = models.TextField(u"Monitoramento", blank = True, null = True, help_text = "") 
    historico = models.TextField(u"Historico", blank = True, null = True, help_text = "")
    caracteristicas = models.ManyToManyField(Caracteristica, verbose_name = "Caracteristicas", related_name = "software_caracteristica", blank = True, null = True, help_text = "")
    data = models.DateTimeField("Adicionado em", auto_now_add = True, blank = True, null = True)
    autor = models.ForeignKey(User, blank = True, null = True, related_name = "software_user")
    
    class Meta:
        verbose_name = u"Software"
        verbose_name_plural = u"Softwares"
        
    def __str__(self):
        return u"%s" % self.nome
    
    def __unicode__(self):
        return u"%s" % self.nome
    
    def admin_logo(self):
        if self.logo:
            return u"<img src='%s%s' />" % (settings.MEDIA_URL, self.logo) 
        else:
            return u"<img src='%simg/sem_imagem.jpeg' />" % settings.MEDIA_URL 
    admin_logo.short_description = "Logomarca"
    admin_logo.allow_tags = True
        
#===================================== Signals ====================================================================================
def post_delete_tipoaplicacao(signal, instance, sender, **kwargs):
    instance.deletar_miniaturas()    
signals.pre_delete.connect(post_delete_tipoaplicacao, sender = TipoAplicacao)    

def post_delete_produto(signal, instance, sender, **kwargs):
    instance.deletar_miniaturas()    
signals.pre_delete.connect(post_delete_produto, sender = Produto)