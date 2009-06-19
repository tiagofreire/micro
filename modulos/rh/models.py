#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
    
class PaginaRecursosHumanos(models.Model):
    titulo = models.CharField(u"Título", max_length = 196, blank = True, null = True, help_text = "")
    texto = models.TextField(u"Texto", blank = True, null = True, help_text = "")
    imagem = models.ImageField(u"Imagem", upload_to = "img", blank = True, null = True, help_text = "")   
    texto_primeiro_acesso = models.TextField(u"Texto Primeiro Acesso", blank = True, null = True, help_text = "")
    seo_titulo = models.CharField(u"Título", max_length = 128, blank = True, null = True, help_text = "")
    seo_descricao = models.TextField(u"Descrição", blank = True, null = True, help_text = "")
    seo_tags = models.CharField(u"Tags", max_length = 255, blank = True, null = True, help_text = "")

    class Meta:
        verbose_name = "Pagina RH"
        verbose_name_plural = "Pagina RH"

    def __str__(self):
        return u""

    def __unicode__(self):
        return u""    
    
class Curriculo(models.Model):
    foto = models.ImageField("Foto", upload_to = "img/curriculos/", blank = True, null = True)
    nome = models.CharField(u"Nome", max_length = 128, blank = True, null = True)
    email = models.EmailField(u"Email", blank = True, null = True)
    sexo = models.CharField(u"Sexo", max_length = 32, blank = True, null = True)
    estado_civil = models.CharField(u"Estado Civil", max_length = 64, blank = True, null = True)
    filhos = models.CharField(u"Filhos", max_length = 64, blank = True, null = True)
    nascimento = models.DateField(u"Data de Nascimento", blank = True, null = True)
    telefone = models.CharField(u"Telefone", max_length = 32, blank = True, null = True)
    celular = models.CharField(u"Celular", max_length = 32, blank = True, null = True)
    endereco = models.CharField(u"Endereço", max_length = 128, blank = True, null = True)
    complemento = models.CharField(u"Complemento", max_length = 128, blank = True, null = True)
    bairro = models.CharField(u"Bairro", max_length = 128, blank = True, null = True)
    estado = models.CharField(u"Estado", max_length = 128, blank = True, null = True)
    cidade = models.CharField(u"Cidade", max_length = 128, blank = True, null = True)
    cpf = models.CharField(u"CPF", max_length = 128, blank = True, null = True)
    pretensao_salarial = models.CharField(u"Pretensão Salarial", max_length = 128, blank = True, null = True)
    medio_instituicao = models.CharField(u"Instituição Ensino Médio", max_length = 128, blank = True, null = True)
    medio_concluido = models.BooleanField(u"Concluido Ensino Médio", blank = True, null = True)    
    medio_serie = models.CharField(u"Serie Ensino Médio", max_length = 96, blank = True, null = True)    
    medio_conclusao = models.CharField(u"Ano Conclusão Ensino Médio", max_length = 4, blank = True, null = True)    
    graduacao_instituicao = models.CharField(u"Instituição Graduação", max_length = 128, blank = True, null = True)
    graduacao_concluido = models.BooleanField(u"Concluido Graduação", blank = True, null = True)    
    graduacao_curso = models.CharField(u"Curso Graduação", max_length = 96, blank = True, null = True)    
    graduacao_semestre = models.CharField(u"Semestre Graduação", max_length = 96, blank = True, null = True)    
    graduacao_conclusao = models.CharField(u"Ano Conclusão Graduação", max_length = 4, blank = True, null = True)    
    graduacao_complementar = models.TextField(u"Informação Complementar Graduação", blank = True, null = True)        
    pos_graduacao_instituicao = models.CharField(u"Instituição Posgraduação", max_length = 128, blank = True, null = True)
    pos_graduacao_concluido = models.BooleanField(u"Concluido Posgraduação", blank = True, null = True)    
    pos_graduacao_curso = models.CharField(u"Curso Posgraduação", max_length = 96, blank = True, null = True)    
    pos_graduacao_semestre = models.CharField(u"Semestre Posgraduação", max_length = 96, blank = True, null = True)    
    pos_graduacao_conclusao = models.CharField(u"Ano Conclusão Posgraduação", max_length = 4, blank = True, null = True)    
    pos_graduacao_complementar = models.TextField(u"Informação Complementar Posgraduação", blank = True, null = True)
    curso_nome = models.CharField(u"Instituição Curso/Palestra", max_length = 128, blank = True, null = True)    
    curso_instituicao = models.CharField(u"Instituição Curso/Palestra", max_length = 128, blank = True, null = True)
    curso_periodo_de = models.CharField(u"Concluido Curso/Palestra", max_length = 128, blank = True, null = True)    
    curso_periodo_a = models.CharField(u"Curso Curso/Palestra", max_length = 96, blank = True, null = True)    
    curso_complementar = models.TextField(u"Informação Complementar Curso/Palestra", blank = True, null = True)
    ultima_empresa = models.CharField(u"Última Empresa", max_length = 96, blank = True, null = True)    
    ultima_salario = models.CharField(u"Último Salário", max_length = 96, blank = True, null = True)    
    ultima_funcao = models.CharField(u"Última Função", max_length = 96, blank = True, null = True)    
    ultima_periodo_de = models.CharField(u"Último Período De", max_length = 96, blank = True, null = True)    
    ultima_periodo_a = models.CharField(u"Último Período A", max_length = 96, blank = True, null = True)    
    ultima_atividades_desenvolvidas = models.TextField(u"Últimas Atividades Desenvolvidas", blank = True, null = True)    
    ultima_motivo_saida = models.TextField(u"Último Motivo de Saída", blank = True, null = True)        
    penultima_empresa = models.CharField(u"Penúltima Empresa", max_length = 96, blank = True, null = True)    
    penultima_salario = models.CharField(u"Penúltima Salário", max_length = 96, blank = True, null = True)    
    penultima_funcao = models.CharField(u"Penúltima Função", max_length = 96, blank = True, null = True)    
    penultima_periodo_de = models.CharField(u"Penúltima Período De", max_length = 96, blank = True, null = True)    
    penultima_periodo_a = models.CharField(u"Penúltima Período A", max_length = 96, blank = True, null = True)    
    penultima_atividades_desenvolvidas = models.TextField(u"Penúltima Atividades Desenvolvidas", blank = True, null = True)    
    penultima_motivo_saida = models.TextField(u"Penúltima Motivo de Saída", blank = True, null = True)    
    antepenultima_empresa = models.CharField(u"Antipenúltima Empresa", max_length = 96, blank = True, null = True)    
    antepenultima_salario = models.CharField(u"Antipenúltima Salário", max_length = 96, blank = True, null = True)    
    antepenultima_funcao = models.CharField(u"Antipenúltima Função", max_length = 96, blank = True, null = True)    
    antepenultima_periodo_de = models.CharField(u"Antipenúltima Período De", max_length = 96, blank = True, null = True)    
    antepenultima_periodo_a = models.CharField(u"Antipenúltima Período A", max_length = 96, blank = True, null = True)    
    antepenultima_atividades_desenvolvidas = models.TextField(u"Antipenúltima Atividades Desenvolvidas", blank = True, null = True)    
    antepenultima_motivo_saida = models.TextField(u"Antipenúltima Motivo de Saída", blank = True, null = True)
    minicurriculo = models.TextField(u"Mini-Currículo", blank = True, null = True)
    codigo_cadastro = models.CharField(u"Codigo Cadastro", max_length = 96, blank = True, null = True)
    usuario = models.ForeignKey(User, verbose_name = u"Usuario", related_name = "curriculo_user", blank = True, null = True)
    data = models.DateTimeField(u"Cadastrado em", auto_now_add = True, blank = True, null = True)
    
    class Meta:
        verbose_name = u"Currículo Enviado"
        verbose_name_plural = u"Currículos Enviados"

    def __str__(self):
        return u"%s" % self.nome

    def __unicode__(self):
        return u"%s" % self.nome    
