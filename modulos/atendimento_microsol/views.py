#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail, EmailMessage
from models import PaginaAtendimentoMicrosol, Chamada
from forms import FormChamada
from micro.modulos.site_config.models import SiteConfig
from datetime import date

#Sombreamento do Admin
def sombreamento_pagina_atendimento_microsol(request):
    pagina, criado = PaginaAtendimentoMicrosol.objects.get_or_create(id = 1)
    return HttpResponseRedirect('/admin/atendimento_microsol/paginaatendimentomicrosol/1/')

#VIews do site
def atendimento_microsol_view(request):
    config = SiteConfig.objects.get(id = 1)
    pagina = PaginaAtendimentoMicrosol.objects.get(id = 1)
    cadastrado = False
    novo_cadastro = FormChamada()
    if request.method == "POST":
        novo_cadastro = FormChamada(request.POST)
        if novo_cadastro.is_valid():
            novo_objeto = novo_cadastro.save()
            novo_objeto.telefone = "(%s) %s %s" % (request.POST['ddd'], request.POST['fone'], request.POST['ramal'])
            novo_objeto.cep = "%s %s" % (request.POST['cep_1'], request.POST['cep_2'])
            novo_objeto.save()
            cadastrado = True
            mensagem_email = u"""
                <div align="center">
	<table width="545" cellspacing="3" cellpadding="0" border="0" style="font-family: Verdana,Arial,Helvetica,sans-serif; font-size: 11px;">
		<tbody><tr>
			<td width="220" style="font-size: 14px;" colspan="2">
				<div align="center">
					<strong>CONTATO ENVIADO ATRAVÉS DO ATENDIMENTO ON SITE MICROSOL <a onclick="onClickUnsafeLink(event);" target="_blank">www.microsol.com.br</a></strong>
				</div>
			</td>
		</tr>
		<tr>
			<td width="223"> </td>
			<td width="313"> </td>
		</tr>
		<tr>
			<td><strong>NÚMERO DA SOLICITAÇÃO:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td><strong>SETOR:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td><strong>ORGÃO SOLICITADOR:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td><strong>ORDEM CONSOFT:</strong></td>
			<td>%s<td/>
		</tr>
		<tr>
			<td><strong>NÚMERO D0 TOMBAMENTO:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td><strong>ENDEREÇO:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td><strong>COMPLEMENTO:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td><strong>NÚMERO:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td><strong>BAIRRO:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td><strong>CEP:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td><strong>CIDADE:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td><strong>ESTADO:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td><strong>EMAIL:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td><strong>TELEFONE:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td><strong>MODELO DO EQUIPAMENTO:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td><strong>NÚMERO DE SÉRIE EQUIPAMENTO:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td><strong>POTÊNCIA:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td><strong>NOTA FISCAL:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td><strong>PROBLEMA:</strong></td>
			<td>%s</td>
		</tr>
		<tr>
			<td/>
			<td/>
		</tr>
		<tr>
			<td width="220" colspan="2"><div align="center">
				<strong><i>Esta é uma mensagem automática, por favor não responda</i></strong></div></td>
		</tr>
	</tbody></table>
</div>

"""  % (novo_objeto.id, novo_objeto.setor, novo_objeto.orgao_solicitante, novo_objeto.ordem_consoft, novo_objeto.numero_de_tombamento,
        novo_objeto.endereco, novo_objeto.complemento, novo_objeto.numero, novo_objeto.bairro, novo_objeto.cep, novo_objeto.cidade, 
        novo_objeto.estado, novo_objeto.email, novo_objeto.telefone, novo_objeto.modelo_equipamento, novo_objeto.numero_de_serie, 
        novo_objeto.potencia, novo_objeto.numero_nota_fiscal, novo_objeto.descricao_problema)
            enviar_email = EmailMessage("Atendimento on site - www.microsol.com.br‏", mensagem_email, "microsol@microsol.com", (
            novo_objeto.email, "silvio@indexvirtual.com"))
            enviar_email.content_subtype = "html"
            enviar_email.send(fail_silently = False)
            return HttpResponse("sucesso")  
    variaveis = RequestContext(request, {'formulario': novo_cadastro, 'pagina': pagina, 'config': config, 'cadastrado': cadastrado})
    return render_to_response('atendimento_microsol.html', variaveis)


