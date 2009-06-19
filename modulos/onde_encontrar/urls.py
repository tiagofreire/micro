#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.onde_encontrar.views",   
    (r'^$', 'onde_encontrar_view'),    
    (r'^lojas_online/$', 'lojas_online_view'),
)    
