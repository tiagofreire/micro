#-*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.core.mail import EmailMessage, SMTPConnection, send_mail

class Email(models.Model) :
    nome = models.CharField(u"Nome", max_length = 96, blank = True, null = True)
    email = models.EmailField(u"Email", max_length = 76, unique = True, help_text = u"Endere\u00E7o de Email.", blank = True, null = True)
    data = models.DateTimeField(auto_now_add = True, blank = True, null = True)

    def __str__(self) :
        return u"%s" % self.email

    def __unicode__(self) :
        return u"%s" % self.email    

class Newsletter(models.Model) :
    emailsCadastrados = models.ManyToManyField(Email, related_name = "Newsletter-Email", verbose_name = "Emails", help_text = u"Emails que receber\u00E3o a mensagem.", blank = True, null = True)
    titulo = models.CharField(u"T\u00EDtulo", max_length = 76, help_text = u"T\u00EDtulo da mensagem.", blank = True, null = True)
    copia = models.EmailField(max_length = 76, help_text = u"Email a receber uma copia da mensagem", blank = True, null = True)
    texto = models.TextField("Mensagem", blank = True, null = True, help_text = "")
    arquivo = models.FileField(upload_to = "__arquivos/newsletter_uploads", help_text = u"Arquivo a ser anexado ao email", blank = True, null = True)
    data_envio = models.DateField("Data de envio", auto_now_add = True, blank = True, null = True)

    def __str__(self) :
        return "%s" % self.titulo

    def __unicode__(self) :
        return "%s" % self.titulo
    
    def enviar(self):
        toEmails = []
        mail = EmailMessage(subject = self.titulo.__str__(), body = self.texto.__str__(), from_email = "silvio@indexvirtual.com")
        mail.content_subtype = "html"
        if self.arquivo :
            mail.attach_file(self.arquivo.path)
        for email in self.emailsCadastrados.all() :
                toEmails.append(email.__str__())
        if toEmails.__len__() > 200 :
            connectionSMTP = SMTPConnection()
            mail.connection = connectionSMTP
            loops =  self.emailsCadastrados.all().__len__() / 200
            for loop in range(0, loops) :
                mail.to = toEmails[loop * 200: loop * 200 + 200]
                mail.send()
        else :
            mail.to = toEmails
            mail.send(fail_silently = False)

    class Meta:
        verbose_name = "Newslleter"
        verbose_name_plural = "Newslleters"
    
    
    
