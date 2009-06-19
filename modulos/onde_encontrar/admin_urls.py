#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.onde_encontrar.views",   
    (r'^paginaondeencontrar/$', 'sombreamento_pagina_onde_encontrar'),
    (r'^paginaondeencontrar/add/$', 'sombreamento_pagina_onde_encontrar'),
    (r'^paginarevendas/$', 'sombreamento_pagina_revendas'),
    (r'^paginarevendas/add/$', 'sombreamento_pagina_revendas'),
    (r'^paginalojasonline/$', 'sombreamento_pagina_lojas_online'),
    (r'^paginalojasonline/add/$', 'sombreamento_pagina_lojas_online'),
    (r'^paginaassitenciatecnica/$', 'sombreamento_pagina_assistencia_tecnica'),
    (r'^paginaassitenciatecnica/add/$', 'sombreamento_pagina_assistencia_tecnica'),    
)    
