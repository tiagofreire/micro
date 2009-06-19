#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.fale_conosco.views",   
    (r'^$', 'fale_conosco_view'),    
    (r'^sam/$', 'sam_view'),    
    (r'^contato/$', 'contato_view'),
)    
