#-*- coding: utf-8 -*-
from django.db import models

class OndeComprar(models.Model) :
    nome = models.CharField(u"Nome", max_length = 96, blank = True, null = True)
    telefone = models.CharField(u"Telefone", max_length = 76, help_text = u"Endere\u00E7o de Email.", blank = True, null = True)
    email = models.EmailField(u"Email", blank = True, null = True, help_text = "")
    lojaonline = models.BooleanField(u"Loja Online", blank = True, null = True)
    autor = models.IntegerField(u"Autor", blank = True, null = True)
    ativo = models.BooleanField(u"Ativo", blank = True, null = True)
    url = models.CharField(u"URL",  max_length = "196", blank = True, null = True)
    

    def __str__(self) :
        return u"%s" % self.nome

    def __unicode__(self) :
        return u"%s" % self.nome  
    
    class Meta:
        verbose_name = "Onde Comprar"
        verbose_name_plural = "Onde Comprar"
        
class Estado(models.Model):
    nome = models.CharField(u"Nome", max_length = "196", blank = True, null = True)
    uf = models.CharField(u"UF", max_length = "196", blank = True, null = True)
    
    def __str__(self) :
        return "%s" % self.nome

    def __unicode__(self) :
        return "%s" % self.nome
    
    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        
class Cidade(models.Model):
    estado =  models.ForeignKey(Estado, blank = True, null = True, verbose_name = u"Município")
    nome = models.CharField(u"Nome", max_length = "196", blank = True, null = True)
    
    def __str__(self) :
        return "%s" % self.nome

    def __unicode__(self) :
        return "%s" % self.nome
    
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        
class Franquia(models.Model) :
    ondecomprar = models.ForeignKey(OndeComprar, related_name = "Onde Comprar", verbose_name = "franquia_ondecomprar", help_text = u"", blank = True, null = True)
    cidade = models.ForeignKey(Cidade, related_name = "Cidade", verbose_name = "franquia_cidade", help_text = u"", blank = True, null = True)
    endereco = models.CharField(u"Endereço", max_length = 76, blank = True, null = True)
    telefone = models.CharField(u"Telefone", max_length = 76, blank = True, null = True)
    email = models.EmailField(u"Email", max_length = "196", blank = True, null = True)
    cordenadasLat = models.IntegerField(blank = True, null = True)
    cordenadasLong = models.IntegerField(blank = True, null = True)

    def __str__(self) :
        return "%s" % self.id

    def __unicode__(self) :
        return "%s" % self.id
    
    class Meta:
        verbose_name = "Franquia"
        verbose_name_plural = "Franquias"        
    
    
    
