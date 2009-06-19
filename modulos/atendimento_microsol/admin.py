#-*- coding: utf-8 -*-
from django.contrib import admin
from models import Chamada, PaginaAtendimentoMicrosol

class ChamadaAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Dados do Contato", {'fields': ('nome', 'setor', 'orgao_solicitante', 'ordem_consoft', 'endereco',
                                         'numero', 'complemento', 'cep', 'bairro', 'estado', 'cidade', 'telefone',
                                         'numero_de_tombamento', 'email')}),
        ("Dados do Equipamento", {'fields': ('modelo_equipamento', 'numero_de_serie', 'potencia', 'numero_nota_fiscal', 'descricao_problema',
                                         'solucionado', 'data_solucao')}),
    )
    exclude = ['data', ]
    list_display = ['__unicode__', 'nome', 'email', 'cidade', 'estado', 'solucionado', 'data']
    search_fields = ['nome', 'cidade', 'estado']
    
class PaginaAtendimentoMicrosolAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'texto')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )

admin.site.register(Chamada, ChamadaAdmin)
admin.site.register(PaginaAtendimentoMicrosol, PaginaAtendimentoMicrosolAdmin)

