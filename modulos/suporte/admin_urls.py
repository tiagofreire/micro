#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.suporte.views",   
    (r'^paginaaplicativos/$', 'sombreamento_pagina_aplicativos'),
    (r'^paginaaplicativos/add/$', 'sombreamento_pagina_aplicativos'),
    (r'^paginacatalogos/$', 'sombreamento_pagina_catalogos'),
    (r'^paginacatalogos/add/$', 'sombreamento_pagina_catalogos'),
    (r'^paginamanuais/$', 'sombreamento_pagina_manuais'),
    (r'^paginamanuais/add/$', 'sombreamento_pagina_manuais'),
    (r'^paginasuporte/$', 'sombreamento_pagina_suporte'),
    (r'^paginasuporte/add/$', 'sombreamento_pagina_suporte'),    
)    
