#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.a_microsol.views",   
    (r'^paginaamicrosol/$', 'sombreamento_pagina_a_microsol'),
    (r'^paginaamicrosol/add/$', 'sombreamento_pagina_a_microsol'),
    (r'^paginaaempresa/$', 'sombreamento_pagina_a_empresa'),
    (r'^paginaaempresa/add/$', 'sombreamento_pagina_a_empresa'),
    (r'^paginaconheca/$', 'sombreamento_pagina_conheca'),
    (r'^paginaconheca/add/$', 'sombreamento_pagina_conheca'),
    (r'^paginaqualidadeepremios/$', 'sombreamento_pagina_qualidade_e_premios'),
    (r'^paginaqualidadeepremios/add/$', 'sombreamento_pagina_qualidade_e_premios'),
)    
