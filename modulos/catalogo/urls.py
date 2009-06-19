#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.catalogo.views",   
    (r'^$', 'catalogo_view'),
    (r'^(?P<id_galeria>.*)/$', 'catalogo_view'),
)    
