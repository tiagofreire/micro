#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.catalogo.views",   
    (r'^paginacatalogos/$', 'sombreamento_pagina_catalogos'),
    (r'^paginacatalogos/add/$', 'sombreamento_pagina_catalogos'), 
)    
