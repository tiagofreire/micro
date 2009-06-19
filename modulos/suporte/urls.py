#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.suporte.views",   
    (r'^$', 'suporte_view'),
    (r'^catalogos/$', 'catalogos_view'),
    (r'^manuais/$', 'manuais_view'),
    (r'^perguntas_frequentes/$', 'perguntas_view'),
)    
