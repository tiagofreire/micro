#-*- coding: utf-8 -*-
from django.db import models

class Chamada(models.Model):
    nome = models.CharField(u"Nome", max_length = 196, blank = True, null = True)
    setor = models.CharField(u"Setor", max_length = 196, blank = True, null = True)
    orgao_solicitante = models.CharField(u"Orgão Solicitante", max_length = 196, blank = True, null = True)
    ordem_consoft = models.CharField(u"Ordem Consoft", max_length = 196, blank = True, null = True)
    endereco = models.CharField(u"Endereço", max_length = 196, blank = True, null = True)
    numero = models.CharField(u"Número", max_length = 196, blank = True, null = True)
    complemento = models.CharField(u"Complemento", max_length = 196, blank = True, null = True)
    cep = models.CharField(u"CEP", max_length = 196, blank = True, null = True)
    bairro = models.CharField(u"Bairro", max_length = 196, blank = True, null = True)
    estado = models.CharField(u"Estado", max_length = 196, blank = True, null = True)
    cidade = models.CharField(u"Cidade", max_length = 196, blank = True, null = True)
    telefone = models.CharField(u"Telefone", max_length = 196, blank = True, null = True)
    numero_de_tombamento = models.CharField(u"Número de Tombamento", max_length = 196, blank = True, null = True)     
    email = models.EmailField(u"Email", blank = True, null = True)
    modelo_equipamento = models.CharField(u"Modelo do Equipamento", max_length = 196, blank = True, null = True)
    numero_de_serie = models.CharField(u"Número de Série", max_length = 196, blank = True, null = True)
    potencia = models.CharField(u"Potência", max_length = 196, blank = True, null = True)
    numero_nota_fiscal = models.CharField(u"N de série da Nota Fiscal", max_length = 196, blank = True, null = True)
    descricao_problema = models.TextField(u"Descrição do Problema", blank = True, null = True)
    solucionado = models.BooleanField(u"Solucionado")
    data_solucao = models.DateTimeField(u"Data da solução", blank = True, null = True)
    data = models.DateTimeField(u"Cadastrado em", auto_now_add = True, blank = True, null = True)
    
    class Meta:
        verbose_name = u"Chamada"
        verbose_name_plural = u"Chamada"

    def __str__(self):
        return u"Chamada #%s" % self.id

    def __unicode__(self):
        return u"Chamada #%s" % self.id    
    
class PaginaAtendimentoMicrosol(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = True, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = True, null = True, help_text = "")
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina Atendimento Microsol"
        verbose_name_plural = "Pagina Atendimento Microsol"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""    
    
