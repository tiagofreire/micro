#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.index_gallery.views",
    (r'^listar_galerias/$', 'listar_galerias_view'),
    (r'^visualizar_galeria/categoria/(?P<categoria_slug>.*)/(?P<autor_username>.*)/$', 'visualizar_galerias_por_categoria_autor_view'),
    (r'^visualizar_galeria/categoria/(?P<categoria_slug>.*)/$', 'visualizar_galerias_por_categoria_view'),
    (r'^visualizar_galeria/(?P<galeria_id>\d)/$', 'visualizar_galeria_view'),
    (r'^visualizar_galeria/(?P<autor_username>.*)/$', 'visualizar_galerias_por_autor_view'),
    (r'^manipular_foto/redimensionar/(?P<foto>.*)/$', 'redimensionar_foto'),
    (r'^manipular_foto/(?P<foto>.*)/$', 'manipular_foto'),
)    