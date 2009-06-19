#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.atendimento_microsol.views",   
    (r'^$', 'atendimento_microsol_view'),    
)    
