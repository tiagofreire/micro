#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('micro.modulos.utils',
    (r'^verificar_cep/(?P<cep>.*)/$', 'pesquisar_cep_view'),
    (r'^calculo_frete/(?P<servico>.*)/(?P<origem>.*)/(?P<destino>.*)/(?P<peso>.*)/$', 'calcular_frete_view',),
    (r'^cropar_imagem/(?P<imagem_name>.*)/$', 'cropar_imagem_view'),
)