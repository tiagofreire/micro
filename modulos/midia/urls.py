#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.midia.views",   
    (r'^$', 'midia_view'),    
    (r'^informativo/$', 'informativo_view'),
    (r'^noticias/(?P<pagina>.*)/$', 'noticias_view'),
    (r'^noticia/(?P<titulo_slug>.*)/$', 'noticia_view'),
    (r'^hotsites/$', 'hotsites_view'),
    (r'^manual_da_marca/$', 'manual_da_marca_view'),
    (r'^publicidade/$', 'publicidade_view'),
    (r'^teste_aplicativo/$', 'teste_aplicativo'),
)    
