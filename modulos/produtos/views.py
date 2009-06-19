#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.html import strip_tags
from models import Produto, Categoria, Modelo, Software
from micro.modulos.site_config.models import SiteConfig

def produto_view(request, categoria, nome_slug = None):
    config = SiteConfig.objects.get(id = 1)
    categoria_obj = Categoria.objects.get(nome_slug = categoria)
    produtos = Produto.objects.filter(categoria = categoria_obj)
    if nome_slug:
        produto = Produto.objects.get(nome_slug = nome_slug)
    else:
        try:
            produto = produtos[0]
        except Exception:
            variaveis = RequestContext(request, {'config': config, 'categoria': categoria_obj}) 
            return render_to_response('produto_vazio.html', variaveis)    
        if categoria == "nobreak":
            return nobreak_view(request, categoria)
        elif categoria == "estabilizador":
            return estabilizador_view(request, categoria)
    produto_cor = False
    for modelo in produto.modelos.all():
        if modelo.cores.all():
            produto_cor = True
    sgm = Software.objects.get(nome = "SGM")        
    variaveis = RequestContext(request, {'sgm': sgm, 'produto_cor': produto_cor, 'config': config, 'produtos': produtos, 'produto': produto, 'categoria': categoria_obj})
    if categoria == "produtos_descontinuados":
        return render_to_response('produtos_descontinuados.html', variaveis)
    elif categoria == "nobreak":    
        return render_to_response('produto_nobreak.html', variaveis)
    else:    
        return render_to_response('produto_generico.html', variaveis)
    
def nobreak_view(request, categoria):
    config = SiteConfig.objects.get(id = 1)
    categoria_obj = Categoria.objects.get(nome_slug = categoria)
    produtos = Produto.objects.filter(categoria = categoria_obj)
    faixa_1 = produtos_por_potencia(0, 800, categoria_obj)
    faixa_2 = produtos_por_potencia(801, 1400, categoria_obj)
    faixa_3 = produtos_por_potencia(1401, 2000, categoria_obj)
    faixa_4 = produtos_por_potencia(2001, 10000, categoria_obj)
    variaveis = RequestContext(request, {'produtos': produtos, 'config': config, 'categoria': categoria_obj, 'faixa_1': faixa_1, 'faixa_2': faixa_2, 'faixa_3': faixa_3, 'faixa_4': faixa_4})
    return render_to_response('produto_nobreak_home.html', variaveis)

def estabilizador_view(request, categoria):
    config = SiteConfig.objects.get(id = 1)
    categoria_obj = Categoria.objects.get(nome_slug = categoria)
    produtos = Produto.objects.filter(categoria = categoria_obj)
    faixa_1 = produtos_por_potencia(0, 500, categoria_obj)
    faixa_2 = produtos_por_potencia(501, 1000, categoria_obj)
    faixa_3 = produtos_por_potencia(1001, 2000, categoria_obj)
    variaveis = RequestContext(request, {'produtos': produtos, 'config': config, 'categoria': categoria_obj, 'faixa_1': faixa_1, 'faixa_2': faixa_2, 'faixa_3': faixa_3})
    return render_to_response('produto_estabilizador_home.html', variaveis)

def software_view(request, nome_slug = None):
    config = SiteConfig.objects.get(id = 1)
    produtos = Software.objects.order_by('-data').all()
    if nome_slug:
        produto = Software.objects.get(nome_slug = nome_slug)
    else:
        produto = produtos[0]
    variaveis = RequestContext(request, {'config': config, 'produtos': produtos, 'produto': produto})
    return render_to_response('produto_software.html', variaveis)

def aplicativo_microsol_e_voce(request, potencia, delimitador):
    produtos = []
    potencia_convertida = 0
    for modelo in Modelo.objects.all():
        if modelo.tipo_potencia == "VA":
            potencia_convertida = modelo.potencia * 1.0
        elif modelo.tipo_potencia == "KVA":
            potencia_convertida = (modelo.potencia * 1.0)  * 1000
        elif modelo.tipo_potencia == "AH":
            potencia_convertida = modelo.potencia * 100000
        if modelo.tipo_potencia == "W":
            potencia_convertida = modelo.potencia
        if (potencia_convertida >= int(potencia) and potencia_convertida <= (int(potencia) + int(delimitador))):
            for produto in modelo.produto_modelo.all():
                if not produto in produtos:
                    produtos.append(produto)                
    variaveis = RequestContext(request, {'produtos': produtos, 'potencia': potencia})
    return render_to_response('aplicativos_produto.html', variaveis)

def produtos_por_potencia(potencia_minima, potencia_maxima, categoria):
    produtos = []
    potencia_convertida = 0
    for modelo in Modelo.objects.all():
        if modelo.tipo_potencia == "VA":
            potencia_convertida = modelo.potencia * 1.0
        elif modelo.tipo_potencia == "KVA":
            potencia_convertida = (modelo.potencia * 1.0)  * 1000
        elif modelo.tipo_potencia == "AH":
            potencia_convertida = modelo.potencia * 100000
        if modelo.tipo_potencia == "W":
            potencia_convertida = modelo.potencia
        if (potencia_convertida >= int(potencia_minima) and potencia_convertida <= int(potencia_maxima)):
            for produto in modelo.produto_modelo.filter(categoria = categoria).all():
                if not produto in produtos:
                    produtos.append(produto)                
    return produtos
    
    
