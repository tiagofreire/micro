#-*- coding: utf-8 -*-
from django.contrib import admin
from models import SiteConfig, HomePage

class HomePageAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Area I", {'fields': ('area_i_imagem', 'area_i_titulo', 'area_i_texto')}),
        ("Area II", {'fields': ('area_ii_imagem', 'area_ii_titulo', 'area_ii_texto')}),
        ("Area III", {'fields': ('area_iii_imagem', 'area_iii_titulo', 'area_iii_texto')}),
        ("Newsletter", {'fields': ('newslleter_imagem', 'newslleter_titulo', 'newslleter_texto')}),
        ("Blog", {'fields': ('blog_imagem', 'blog_titulo')}),
        ("Video", {'fields': ('video_imagem', 'video_titulo')}),
        (None, {'fields': ('banner', 'noticias_listadas')}),
        ("SEO", {'classes': ('collapse', ), 'fields': ('seo_titulo', 'seo_descricao', 'seo_tags')}),
    )

admin.site.register(SiteConfig)
admin.site.register(HomePage, HomePageAdmin)
