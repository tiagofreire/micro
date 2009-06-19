#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.a_microsol.views",   
    (r'^$', 'a_microsol_view'),
    (r'^aplicativo/$', 'aplicativo_view'),
    (r'^a_empresa/$', 'a_empresa_view'),
    (r'^conheca/$', 'conheca_view'),
    (r'^qualidade_e_premios/$', 'qualidade_e_premios_view'),
)    
