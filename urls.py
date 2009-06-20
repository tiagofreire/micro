#-*- coding: utf-8 -*-
##############################################
from django.conf.urls.defaults import *
from django.conf import settings
#############################################
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^generico/', include('generico.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #Sombreamentos de URL's no admin
    (r'^admin/midia/', include('micro.modulos.midia.admin_urls')),
    (r'^admin/suporte/', include('micro.modulos.suporte.admin_urls')),
    (r'^admin/rh/', include('micro.modulos.rh.admin_urls')),
    (r'^admin/atendimento_microsol/', include('micro.modulos.atendimento_microsol.admin_urls')),
    (r'^admin/onde_encontrar/', include('micro.modulos.onde_encontrar.admin_urls')),
    (r'^admin/catalogo/', include('micro.modulos.catalogo.admin_urls')),
    (r'^admin/a_microsol/', include('micro.modulos.a_microsol.admin_urls')),
    (r'^admin/fale_conosco/', include('micro.modulos.fale_conosco.admin_urls')),
    (r'^admin/site_config/siteconfig/$', 'micro.modulos.site_config.views.sombreamento_siteconfig'),
    (r'^admin/site_config/homepage/$', 'micro.modulos.site_config.views.sombreamento_homepage'),
    (r'^admin/(.*)', admin.site.root),
    
    (r'^$', 'micro.modulos.site_config.views.home_view'),
    (r'^microsol_e_voce/$', 'micro.modulos.site_config.views.microsol_e_voce_view'),
    (r'^teste_pdf/$', 'micro.modulos.site_config.views.teste_pdf_view'),
    (r'^cadastrar_newsletter_ajax/$', 'micro.modulos.newsletter.views.cadastrar_newsletter_ajax'),
    (r'^fale_conosco/', include('micro.modulos.fale_conosco.urls')),
    (r'^produtos/', include('micro.modulos.produtos.urls')),
    (r'^midia/', include('micro.modulos.midia.urls')),
    (r'^suporte/', include('micro.modulos.suporte.urls')),
    (r'^rh/', include('micro.modulos.rh.urls')),
    (r'^atendimentoonsite/', include('micro.modulos.atendimento_microsol.urls')),
    (r'^microsol_e_voce/aplicativo/(?P<potencia>.*)/(?P<delimitador>.*)/$', 'micro.modulos.produtos.views.aplicativo_microsol_e_voce'),
    (r'^a_microsol_indica/$', 'micro.modulos.a_microsol.views.aplicativo_view'),
    (r'^onde_encontrar/', include('micro.modulos.onde_encontrar.urls')),
    (r'^catalogos/', include('micro.modulos.catalogo.urls')),
    (r'^a_microsol/', include('micro.modulos.a_microsol.urls')),
    (r'^utils/', include('micro.modulos.urls')),
    (r'^__swf/(.*)', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + "/swf/"}),    
 #   (r'^__swf/banner1.swf', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + "/swf/banner1.swf"}),    
 #   (r'^__swf/banner2.swf', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + "/swf/banner2.swf"}),    
 #   (r'^__swf/banner3.swf', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + "/swf/banner3.swf"}),    
    (r'^site_media/(.*)', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),    

)
