#-*- coding: utf-8 -*-
from django.db import models
from django.db.models import signals
from django.conf import settings
from cStringIO import StringIO
from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
import os
import zipfile

#Importa a biblioteca grafica do Python (PIL - Python Imaging Library)
try:
    import Image
except ImportError:
    try:
        from micro.modulos.PIL import Image
    except ImportError:
        raise ImportError(u"Index Gallery n\u00E3o conseguiu importar a biblioteca de imagem do Pytho (Python Imaging Library).")

    
#Cada objeto desta classe representa um tamanho de thumbnail que pode ser gerado de cada foto.
class Tamanho(models.Model):
    """Classe que guardar os dados referentes as dimens\u00E3oes de thumbnail da foto, cada foto pode ter mais
    de um thumbnail"""
    nome = models.CharField(u"Nome", max_length = 32, help_text = "", blank = False, null = True, unique = True)
    largura = models.IntegerField(u"Largura", help_text = "", blank = False, null = True)
    altura = models.IntegerField(u"Altura", help_text = "", blank = False, null = True)
    proporcional = models.BooleanField(u"Proporcional", help_text = u"Mantem a propor\u00E7\u00E3o da imagem original.")
    padrao = models.BooleanField(u"Padr\u00E3o", help_text = u"Tamanhos padr\u00e3o ser\u00E3o aplicados em todas as fotos.")
    
    class Meta:
        verbose_name = "Tamanho"
        verbose_name_plural = "Tamanhos"
        
    def __str__(self) :
        return "%s" % self.nome

    def __unicode__(self) :
        return "%s" % self.nome

    #Usado para adicionar uma miniatura padrão a todas as fotos adicionadas a index gallery. 
    def adicionar_para_fotos(self):
        for foto in Foto.objects.all():
            if foto.thumbnails:
                if not self in foto.thumbnails.all():
                    foto.thumbnails.add(self)    


#Cada objeto desta classe representa um arquivo de imagem e esta associado a um arquivo no disco.
class Foto(models.Model) :
    """Classe que guardar os dados referentes a um arquivo de imagem tal como nome, caminho, thumbnails e damais
    dados pertinentes a uma foto."""
    nome = models.CharField(u"Nome", max_length = 32, unique = True)
    nome_slug = models.SlugField(u"Slug", max_length = 32, help_text = "", unique = True, blank = False, null = True)
    descricao = models.TextField(u"Descri\u00E7\u00E3o", help_text = u"Pequeno texto descritivo da foto.", blank = True, null = True)
    ordem = models.IntegerField(help_text=u"Indica a ordem da foto dentro da galeria.", blank = True, null = True)
    arquivo = models.ImageField("Imagem", upload_to = settings.INDEX_GALLERY_ROOT, help_text = "", blank = False, null = True)
    data = models.DateTimeField(auto_now_add = True, blank = True, null = True)
    thumbnails = models.ManyToManyField(Tamanho, help_text = "", related_name = "Foto-Tamanho", verbose_name = u"Tamanhos", blank = True, null = True)
    publico = models.BooleanField(blank = True, null = True, help_text = "")
    autor = models.ForeignKey(User, related_name = "Foto-User", blank = True, null = True)
    upload = models.ForeignKey("UploadArquivo", related_name = "Foto-UploadArquivo", blank = True, null = True)

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"
        ordering = ['ordem']

    def __str__(self) :
        return "%s" % self.nome

    def __unicode__(self) :
        return "%s" % self.nome

    def get_absolute_url(self) :
        return "%s%s" % (settings.MEDIA_URL, self.arquivo)
     
    #Mostra a miniatura da foto no admin. 
    def admin_thumbnail(self) :
        try:
            self.arquivo.size #Verifica se o arquivo de imagem da foto ainda existe no servidor
            caminho_thumbnail =  u'<a href="%s%s%s" class="fancy_trigger"><img src="%s%sthumbnails/32x32_%s"/></a>' % \
    (settings.MEDIA_URL, settings.INDEX_GALLERY_ROOT, self.arquivo.name[len(settings.INDEX_GALLERY_ROOT):], \
     settings.MEDIA_URL, settings.INDEX_GALLERY_ROOT, self.arquivo.name[len(settings.INDEX_GALLERY_ROOT):])
        except Exception:
            caminho_thumbnail = u'<a href="%s%s%s" class="fancy_trigger"><img src="%s%sthumbnails/32x32_%s"/></a>' %\
            (settings.MEDIA_URL, settings.INDEX_GALLERY_ROOT, 'sem_foto.jpg', settings.MEDIA_URL, settings.INDEX_GALLERY_ROOT, 'sem_foto.jpg')
        return caminho_thumbnail
    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True
    
    #Calcula o tamanho da imagem para ser mostrada no admin.
    def admin_tamanho(self):
        tamanho = ""
        try:
            if self.arquivo.size < 1000:
                tamanho = str(self.arquivo.size) + "&nbsp;B"
            elif self.arquivo.size >= 1000 and self.arquivo.size < 1000000:
                tamanho = str(self.arquivo.size/1000) + "&nbsp;kB"
            elif self.arquivo.size >= 1000000:
                tamanho = str(self.arquivo.size/1000000) + "&nbsp;MB"
        except Exception:
            tamanho = "Arquivo deletado do servidor."
        return mark_safe(tamanho)
    admin_tamanho.short_description = "Tamanho do arquivo"
    admin_tamanho.allow_tags = True

    #Cria todas as miniaturas com base nos objetos do tipo Tamanho selecionados no admin.
    def criar_miniaturas_tamanho(self):        
        for tamanho in self.thumbnails.all() :
            foto = Image.open(self.arquivo.path)
            thumbnail_path = "%s/%sthumbnails/%sx%s_%s" % (settings.MEDIA_ROOT, settings.INDEX_GALLERY_ROOT, tamanho.largura, tamanho.altura, self.arquivo.name[len(settings.INDEX_GALLERY_ROOT):]) 
            if tamanho.proporcional :
                foto_largura, foto_altura = foto.size
                ratio = min(float(tamanho.largura) / foto_largura, float(tamanho.altura) / foto_altura)
                dimensoes = (int(round(foto_largura * ratio)), int(round(foto_altura * ratio)))
            else:
                foto_largura, foto_altura = foto.size
                if foto_largura > foto_altura:
                    nova_altura = foto_altura * tamanho.largura / foto_largura
                    dimensoes = (tamanho.largura, nova_altura)
                elif foto_largura < foto_altura:
                    nova_largura = foto_largura * tamanho.altura / foto_altura
                    dimensoes = (nova_largura, tamanho.altura)
                else:    
                    dimensoes = (tamanho.largura, tamanho.altura)
            foto.thumbnail(dimensoes, Image.ANTIALIAS)
            thumbnail = foto.crop((0, 0, dimensoes[0], dimensoes[1]))
            thumbnail.save(thumbnail_path, foto.format)

    #Cria a miniatura usada no admin.        
    def criar_miniatura_admin(self):
        foto = Image.open(self.arquivo.path)
        thumbnail_path = "%s/%sthumbnails/%sx%s_%s" % (settings.MEDIA_ROOT, settings.INDEX_GALLERY_ROOT, 32, 32, self.arquivo.name[len(settings.INDEX_GALLERY_ROOT):]) 
        dimensoes = (32, 32)
        thumbnail = foto.resize(dimensoes, Image.ANTIALIAS)
        thumbnail.save(thumbnail_path, foto.format)
        
    def criar_miniaturas(self):
        self.criar_miniaturas_tamanho()
        self.criar_miniatura_admin()

    #Deleta todas as miniaturas criadas para a foto    
    def deletar_miniaturas(self):
        try:
            for tamanho in self.thumbnails.all() :
                thumbnail_dir = "%s/%sthumbnails/" % (settings.MEDIA_ROOT, settings.INDEX_GALLERY_ROOT)
                thumbnail_file = "%sx%s_%s" % (tamanho.largura, tamanho.altura, self.arquivo.name[len(settings.INDEX_GALLERY_ROOT):])
                for arquivo in os.listdir(thumbnail_dir) :
                    if arquivo == thumbnail_file :
                        os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
            thumbnail_dir = "%s/%sthumbnails/" % (settings.MEDIA_ROOT, settings.INDEX_GALLERY_ROOT)
            thumbnail_file = "%sx%s_%s" % (32, 32, self.arquivo.name[len(settings.INDEX_GALLERY_ROOT):])
            os.unlink("%s%s" % (thumbnail_dir, thumbnail_file))
        except:
            pass
    
    #Adiciona todas a miniaturas marcadas como padr\u00E7o a foto.    
    def adicionar_miniaturas_padrao(self):
        for padrao in Tamanho.objects.filter(padrao = True):
            if not padrao in self.thumbnails.all():
                self.thumbnails.add(padrao)
        self.save()
        self.criar_miniaturas()
        
#Signal post delete para apagar do disco rigido os arquivos de miniatura da foto
def post_delete_foto(signal, instance, sender, **kwargs):
    try:
        instance.deletar_miniaturas()    
    except Exception:
        pass
signals.pre_delete.connect(post_delete_foto, sender = Foto)       

#Classe usada para representar uma categoria para uma galeria
class Categoria(models.Model):
    nome = models.CharField(max_length = 96, unique = True, blank = False, null = True, help_text = "")
    nome_slug = models.SlugField(unique = True, blank = False, null = True, help_text = "")
    descricao = models.TextField(u"Descri\u00E7\u00E3o", blank = True, null = True)

    def __str__(self):
        return u"%s" % self.nome

    def __unicode(self):
        return u"%s" % self.nome



#Cada objeto desta classe representa uma galeria de fotos.
class Galeria(models.Model) :
    """Descricao da classe Galeria"""
    nome = models.CharField("Nome", max_length = 96, help_text = "", unique = True, blank = False, null = True)
    nome_slug = models.SlugField("Nome Slug", blank = True, null = True)
    ordem = models.IntegerField("Ordem", blank = True, null = True)
    descricao = models.TextField(u"Descri\u00E7\u00E3o", help_text = u"Pequeno texto descritivo da galeria.", blank = True, null = True)
    categoria = models.ForeignKey(Categoria, related_name = "Galeria-Categoria", blank = True, null = True)
    publico = models.BooleanField(help_text = u"Galerias publicas s\u00E3o visiveis para todos os usuarios.")
    capa = models.ImageField("Capa", upload_to = settings.INDEX_GALLERY_ROOT + 'capas', help_text = "", blank = True, null = True)
    fotos = models.ManyToManyField(Foto, related_name="Galeria-Foto", verbose_name = "Fotos", blank = True, null = True, help_text = "Digite no campo busca para filtrar os resultados.")
    arquivo = models.ManyToManyField("UploadArquivo", blank = True, null = True, verbose_name = "Arquivos", help_text = "Digite no campo busca para filtrar os resultados.")
    data = models.DateTimeField(auto_now_add = True, blank = True, null = True)
    autor = models.ForeignKey(User, related_name = "Galeria-User", blank = True, null = True)

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galerias"    
    
    def adicionarArquivo(self):
        if self.arquivo.all():
            for arquivoUpload in self.arquivo.all():
                for foto in Foto.objects.filter(upload = arquivoUpload):
                    self.fotos.add(foto)
            self.save()        

    def __str__(self) :
        return "%s" % self.nome

    def __unicode__(self) :
        return "%s" % self.nome
    
    def criar_miniaturas(self):
        self.criar_miniatura_capa()
    
    def criar_miniatura_capa(self):
        foto = Image.open(self.capa.path)
        dimensoes = (128, 128)
        thumbnail = foto.resize(dimensoes, Image.ANTIALIAS)
        thumbnail.save(self.capa.path, foto.format)
        
    def gerar_xml_catalogo(self):    
        xml_content = u"""
            <FlippingBook>
                <width>750</width>
                <height>560</height>
        
                <scaleContent>true</scaleContent>
                <firstPage>0</firstPage>
                <alwaysOpened> false </alwaysOpened>
                <autoFlip> 50 </autoFlip>
                <flipOnClick> false </flipOnClick>
        
                <shadowsDepth> 1 </shadowsDepth>
        
                <moveSpeed> 2 </moveSpeed>
                <closeSpeed> 3 </closeSpeed>
                <gotoSpeed> 3 </gotoSpeed>
        
                <flipSound> mp3/01.mp3</flipSound>
                <pageBack> 0xFFFFFF </pageBack>
        
                <loadOnDemand> true </loadOnDemand>
                <cachePages> true </cachePages>
                <usePreloader> true </usePreloader>
        
                <pages>
        """ 
        for foto in self.fotos.order_by('-ordem').all():
            xml_content += u"                 <page>%s%s</page> \n" % (settings.MEDIA_URL, foto.arquivo)
        xml_content += u"""    </pages>
        </FlippingBook>"""
        nomeXML = u"%sxml/%s.xml" % (settings.MEDIA_ROOT, slugify(self.nome))
        arquivo = open(nomeXML, "w")
        arquivo.write(unicode(xml_content).encode('latin-1'))
        arquivo.close()     


#Classe para envior de arquivos zip contendo fotos.        
class UploadArquivo(models.Model) :
    nome = models.CharField(u"Nome", max_length = 96, help_text = "", unique = True, blank = False, null = True)
    usar_nome = models.BooleanField(u"Modificar nome", help_text=u"Caso marcado, as fotos ter\u00E3o o nome do upload seguido de um valor n\u00FAmerico sequencial.")
    data = models.DateTimeField(auto_now_add = True, blank = True, null = True)
    arquivo = models.FileField("Arquivo (zip)", upload_to = settings.INDEX_GALLERY_ROOT + 'capas')
    thumbnails = models.ManyToManyField(Tamanho, related_name = "Upload_Tamanho", verbose_name = "Tamanhos", blank = True, null = True)
    publico = models.BooleanField(u"Publico", help_text = u"Arquivos publicos ser\u00E3o visiveis para todos os usuarios.")
    autor = models.ForeignKey(User, related_name = "UploadArquivo-User", blank = True, null = True)
    
    class Meta:
        verbose_name = "Arquivo"
        verbose_name_plural = "Arquivos"
    
    #Calcula o tamanho do arquivo para se ser mostrado no admin.
    def admin_tamanho(self):
        tamanho = ""
        try:        
            if self.arquivo.size < 1000:
                tamanho = str(self.arquivo.size) + "&nbsp;B"
            elif self.arquivo.size >= 1000 and self.arquivo.size < 1000000:
                tamanho = str(self.arquivo.size/1000) + "&nbsp;kB"
            elif self.arquivo.size >= 1000000:
                tamanho = str(self.arquivo.size/1000000) + "&nbsp;MB"
        except Exception:
            tamanho = "Arquivo deletado do servidor."
        return mark_safe(tamanho)
    admin_tamanho.short_description = "Tamanho do arquivo"
    admin_tamanho.allow_tags = True
    
    #Processa o arquivo zip e criar objetos do tipo Foto para cada arquivo de imagem
    def processar_zip(self, usuario):
        if os.path.isfile(self.arquivo.path): #Verifica se é arquivo
            arquivoZip = zipfile.ZipFile(self.arquivo.path) #Carrega o arquivo zip
            if arquivoZip.testzip(): #Verifica se não há arquivos corrompidos
                raise Exception('O arquivo %s esta corrompido.' % bad_file)
            contador = 1
            for nomeArquivo in arquivoZip.namelist(): #Percorrer todos os arquivos do zip com base no nome
                arquivo = arquivoZip.read(nomeArquivo) #Ler o arquivo atual com base na iteração
                try:
                    testarImagem = Image.open(StringIO(arquivo)) #Abri o arquivo de imagem
                    testarImagem.load() #Aloca espaço na memoria para o arquivo de imagem
                    testarImagem = Image.open(StringIO(arquivo)) #Abre novamente o arquivo para poder se usar o modo verify
                    testarImagem.verify() #Verifica se o arquivo de imagem não esta quebrado
                except IOError:
                    continue
                if len(arquivo): #Verifica se o tamanho do arquivo em bytes é maior que zero
                    #O bloco try usado para verificar se o arquivo já existe, se não uma exception é lançadaa e criamos então o arquivo.
                    try:
                        if self.usar_nome:
                            nomeFoto = "%s - %s" % (self.nome, contador)
                            foto = Foto.objects.get(nome = nomeFoto)                            
                        else:    
                            foto = Foto.objects.get(nome = nomeArquivo)                   
                    except Foto.DoesNotExist:
                        if self.usar_nome:
                            nomeFoto = "%s - %s" % (self.nome, contador)
                        else:
                            nomeFoto = nomeArquivo
                        nomeFotoSlug = slugify(nomeFoto)
                        foto = Foto(nome = nomeFoto,
                                    nome_slug = nomeFotoSlug,
                                    descricao = "",
                                    upload = self,
                                    autor = usuario,
                                    publico = self.publico
                            )
                        foto.arquivo.save(nomeArquivo, ContentFile(arquivo))
                        foto.thumbnails = self.thumbnails.all()
                        foto.save()
                        foto.criar_miniaturas()
                    contador += 1    
            arquivoZip.close()

    def __str__(self):
        return "%s" % self.nome

    def __unicode__(self):
        return "%s" % self.nome