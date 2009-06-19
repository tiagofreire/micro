#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("micro.modulos.midia.views",   
    (r'^paginahotsites/$', 'sombreamento_pagina_hotsites'),
    (r'^paginahotsites/add/$', 'sombreamento_pagina_hotsites'),
    (r'^paginamanualdamarca/$', 'sombreamento_pagina_manual_da_marca'),
    (r'^paginamanualdamarca/add/$', 'sombreamento_pagina_manual_da_marca'),
    (r'^paginamidia/$', 'sombreamento_pagina_midia'),
    (r'^paginamidia/add/$', 'sombreamento_pagina_midia'),
    (r'^paginapublicidade/$', 'sombreamento_pagina_publicidade'),
    (r'^paginapublicidade/add/$', 'sombreamento_pagina_publicidade'),
    (r'^paginainformativo/$', 'sombreamento_pagina_informativo'),
    (r'^paginainformativo/add/$', 'sombreamento_pagina_informativo'),
    
)    
