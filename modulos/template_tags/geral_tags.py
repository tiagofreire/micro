#-*- coding: utf-8 -*-
from django import template
from django.contrib import admin
from django.template import Context
from django.http import HttpRequest
from django.utils.text import capfirst
from django.utils.safestring import mark_safe
from micro.modulos.site_config.models import SiteConfig
from django.template import Template, Context, Node
from datetime import datetime
from micro.modulos.noticia.models import Noticia
from django.conf import settings
register = template.Library()

def menuApp(user) :
    request = HttpRequest()
    request.user = user
    app_list = admin.site._registry
    app_dict = {}
    for model, model_admin in app_list.items():
        app_label = model._meta.app_label
        has_module_perms = user.has_module_perms(app_label)

        if has_module_perms:
            perms = {
                'add': model_admin.has_add_permission(request),
                'change': model_admin.has_change_permission(request),
                'delete': model_admin.has_delete_permission(request),
            }

        if True in perms.values():
            model_dict = {
                'name': capfirst(model._meta.verbose_name_plural),
                'admin_url': mark_safe('/admin/%s/%s/' % (app_label, model.__name__.lower())),
                'perms': perms,
            }
            
        if app_label in app_dict:
            app_dict[app_label]['models'].append(model_dict)
        else:
            app_dict[app_label] = {
                'name': app_label.title(),
                'app_url': app_label + '/',
                'has_module_perms': has_module_perms,
                'models': [model_dict],
            }
    app_list = app_dict.values()
    app_list.sort(lambda x, y: cmp(x['name'], y['name']))

    for app in app_list:
        app['models'].sort(lambda x, y: cmp(x['name'], y['name']))

    context = {
        'title': 'Site administration',
        'app_list': app_list,
        'root_path': "/",
    }

    return context

register.inclusion_tag('menu.html')(menuApp)   
    
def google_analytics():
    site_config = SiteConfig.objects.get(id = 1)
    context = {
        'google_analytics_user': site_config.google_analytics_user,
        }
    return context
register.inclusion_tag('geral/google_analytics.html')(google_analytics)

# Classe e template tag para classificação de lista de itens com base em um campo do tipo data
class Ano(object):
    def __init__(self, meses, ano):
        self.meses = meses
        self.ano = ano
        
    def __str__(self):
        return "%s" % self.ano
    
    def __unicode__(self):
        return "%s" % self.ano

def filtrar_por_data(lista_de_objetos, campo):
    manager = lista_de_objetos[0]._default_manager
    datas = manager.order_by('-%s' % campo).dates('%s' % campo, 'year')
    anos = []
    for data in datas:
        kwargs = {str("%s__year" % campo): data.year}
        meses_ano = manager.filter(**kwargs).dates('%s' % campo, 'month')
        meses = {}        
        for data_mes in meses_ano:
            meses[data_mes.month] = None
            kwargs_ii = {str("%s__month" % campo): data_mes.month}
            objetos_mes = manager.filter(**kwargs).filter(**kwargs_ii).all()
            mes = []
            for objeto in objetos_mes:
                if objeto in lista_de_objetos:
                    mes.append(objeto)
            meses[data_mes.month] = mes    
        anos.append(Ano(meses = meses, ano = data.year))
    anos.reverse()    
    variaveis = Context({'MEDIA_URL': settings.MEDIA_URL, 'anos': anos})
    return variaveis
register.inclusion_tag('datas.html')(filtrar_por_data)

def ordinal_mes(valor):
    meses_nome = ["Valor Invalido", "Janeiro", "Fevereiro", "Abril", u"Mar\u00E7o", "Maio", "Julho", "Julho", "Agosto", "Setembro",
             "Outubro", "Novembro", "Dezembro"]
    return meses_nome[valor]
register.filter('ordinal_mes', ordinal_mes)

def potencia_minima(potencia, potencia_minima):
    if int(potencia) >= int(potencia_minima):
        return True
    else:
        return False
register.filter('potencia_minima', potencia_minima)

def converter_potencia(potencia, tipo_potencia):
    if tipo_potencia == "VA":
        potencia_convertida = potencia * 1.0
    elif tipo_potencia == "KVA":
        potencia_convertida = (potencia * 1.0)  * 1000
    elif tipo_potencia == "AH":
        potencia_convertida = potencia * 100000
    else:
        potencia_convertida = potencia
    return potencia_convertida
register.filter('converter_potencia', converter_potencia)