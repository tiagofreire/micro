#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.rh.views",   
    (r'^$', 'rh_view'),    
    (r'^adicionar_foto/(?P<id_curriculo>.*)/$', 'editar_foto_view'),
    (r'^cropar/(?P<id_curriculo>.*)/$', 'cropar_foto_view'),
    (r'^curriculo/(?P<id_curriculo>.*)/$', 'rh_curriculo_editar_view'),
    (r'^curriculo/$', 'rh_curriculo_view'),
    (r'^logout/$', 'logout_view'), 
)    
