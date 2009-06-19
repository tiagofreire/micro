#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.atendimento_microsol.views",   
    (r'^paginaatendimentomicrosol/$', 'sombreamento_pagina_atendimento_microsol'),
    (r'^paginaatendimentomicrosol/add/$', 'sombreamento_pagina_atendimento_microsol'),
)    
