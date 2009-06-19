#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.rh.views",   
    (r'^paginarecursoshumanos/$', 'sombreamento_pagina_rh'),
    (r'^paginarecursoshumanos/add/$', 'sombreamento_pagina_rh'),
)    
