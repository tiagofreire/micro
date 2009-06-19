#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.fale_conosco.views",   
    (r'^paginafaleconosco/$', 'sombreamento_pagina_fale_conosco'),
    (r'^paginafaleconosco/add/$', 'sombreamento_pagina_fale_conosco'),
    (r'^paginacontato/$', 'sombreamento_pagina_contato'),
    (r'^paginacontato/add/$', 'sombreamento_pagina_contato'),
    (r'^paginasam/$', 'sombreamento_pagina_sam'),
    (r'^paginasam/add/$', 'sombreamento_pagina_sam'),
    (r'^paginadepartamentos/$', 'sombreamento_pagina_departamentos'),
    (r'^paginadepartamentos/add/$', 'sombreamento_pagina_departamentos'),
)    
