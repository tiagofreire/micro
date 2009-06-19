#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.produtos.views",   
    (r'^softwares/(?P<nome_slug>.*)/$', 'software_view'),
    (r'^softwares/$', 'software_view'),                   
    (r'^(?P<categoria>.*)/(?P<nome_slug>.*)/$', 'produto_view'),
    (r'^(?P<categoria>.*)/$', 'produto_view'),
    
)    
