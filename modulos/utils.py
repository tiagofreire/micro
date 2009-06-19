#-*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from xml.dom import minidom
from xml.parsers.expat import ExpatError
import urllib2
from micro.modulos.fale_conosco.models import PaginaFaleConosco, PaginaSAM, PaginaContato, PaginaDepartamento
from micro.modulos.a_microsol.models import PaginaAMicrosol
from micro.modulos.catalogo.models import PaginaCatalogo, ItemCatalogo
from micro.modulos.midia.models import PaginaMidia, PaginaPublicidade, PaginaManualDaMarca, PaginaInformativo, Publicidade, Noticia, Hotsite, ManualDaMarca
from micro.modulos.onde_encontrar.models import PaginaOndeEncontrar, PaginaRevendas, PaginaLojasOnline, PaginaAssistenciaTecnica
from micro.modulos.suporte.models import PaginaSuporte, PaginaManuais, PaginaCatalogos, PaginaAplicativos, Manuais, Pergunta
from micro.modulos.produtos.models import Produto, Software

try:
    import Image
except ImportError:
    try:
        from modulos.PIL import Image
    except ImportError:
        raise ImportError((u"Crop n\u00E3o conseguiu importar a biblioteca de imagem do Python (Python Imaging Library)."))

def busca_view(request):
    if request.methods == "POST":
        palavra_chave = request.post['palavra_chave']
        produtos = Produto.objects.filter(Q(nome__icontains = palavra_chave) | Q(descricao__icontains = palavra_chave) | Q(funcoes_e_beneficios__icontains = palavra_chave)).order_by('-data').all()
        softwares = Software.objects.filter(Q(nome__icontains = palavra_chave) | Q(descricao__icontains = palavra_chave) | Q(funcoes_e_beneficios__icontains = palavra_chave)).order_by('-data').all()
        fale_conosco = PaginaFaleConosco.objects.filter(texto__icontains = palavra_chave).all()
        a_microsol = PaginaAMicrosol.objects.filter(texto__icontains = palavra_chave).all()
        pagina_midia = PaginaMidia.objects.filter(texto__icontains = palavra_chave).all()
        pagina_informativo = PaginaInformativo.objects.filter(texto__icontains = palavra_chave).all()
        noticias = Noticia.objects.filter(Q(texto__icontains = palavra_chave) | Q(titulo__icontains = palavra_chave)).order_by('-data').all()
        publicidades = Publicidade.objects.filter(titulo__icontains = palavra_chave).order_by('-data').all()
        hotsites = Hotsite.objects.filter(texto__icontains = palavra_chave).order_by('-data').all()
        pagina_suporte = PaginaSuporte.objects.filter(texto__icontains = palavra_chave).all()
        pagina_onde_encontrar = PaginaOndeEncontrar.objects.filter(texto__icontains = palavra_chave).all()
        variaveis = RequestContext(request, {
            'produtos': produtos,
            'softwares': softwares,
            'fale_conosco': fale_conosco,
            'a_microsol': a_microsol,
            'pagina_midia': pagina_midia,
            'pagina_informativo': pagina_informativo,
            'noticias': noticias,
            'publicidades': publicidades,
            'hotsites': hotsites,
            'pagina_suporte': pagina_suporte,
            'pagina_onde_encontrar': pagina_onde_encontrar,
        })
        return render_to_response('busca.html', variaveis)
        
    
#CIDADES_DO_CEARA = (
    #("abaiara", "Abaiara"), 
    #("acarape", "Acarape"), 
    #("acarau", "Acarau"),
    #("acopiara", "Acopiara"),
    #("aiuaba", "Aiuaba"),
    #("alcantaras", "Alcantaras"),
    #("altaneira", "Altaneira"),
    #("alto_santo", "Alto Santo"),
    #("amontada", "Amontada"),
    #("antonina_do_norte", "Antonina do Norte"),
    #("apuiares", "Apuiares"),
    #("aquiraz", "Aquiraz"),
    #("aracati", "Aracati"),
    #("aracoiaba", "Aracoiaba"),
    #("ararenda", "Ararenda"),
    #("araripe", "Araripe"),
    #("aratuba", "Aratuba"),
    #("arneiroz", "Arneiroz"),
    #("assare", "Assare"),
    #("aurora", "Aurora"),
    #("baixio", "Baixio"),
    #("banabuiu", "Banabuiu"),
    #("barbalha", "Barbalha"),
    #("barreira", "Barreira"),
    #("barro", "Barro"),
    #("barroquinha", "Barroquinha"),
    #("baturite", "Baturite"),
    #("beberibe", "Beberibe"),
    #("bela_cruz", "Bela Cruz"),
    #("boa_viagem", "Boa Viagem"),
    #("brejo_santo", "Brejo Santo"),
    #("camocim", "Camocim"),
    #("campos_sales", "Campos Sales"),
    #("caninde", "Caninde"),
    #("capistrano", "Capistrano"), 
    #("caridade", "Caridade"),
    #("carire", "Carire"),
    #("caririacu", "Caririacu"),
    #("carius", "Carius"),
    #("carnaubal", "Carnaubal"),
    #("cascavel", "Cascavel"),
    #("catarina", "Catarina"),
    #("catunda", "Catunda"),
    #("caucaia", "Caucaia"),
    #("cedro", "Cedro"),
    #("chaval", "Chaval"),
    #("choro", "Choro"),
    #("Chorozinho", "Chorozinho")
#Coreau
#Crateus
#Crato
#Croata
#Cruz
#Deputado Irapuan Pinheiro
#Erere
#Eusebio
#Farias Brito
#Forquilha
#Fortaleza
#Fortim
#Frecheirinha
#General Sampaio
#Graca
#Granja
#Granjeiro
#Groairas
#Guaiuba
#Guaraciaba do Norte
#Guaramiranga
#Hidrolandia
#Horizonte
#Ibaretama
#Ibiapina
#Ibicuitinga
#Icapui
#Ico
#Iguatu
#Independencia
#Ipaporanga
#Ipaumirim
#Ipu
#Ipueiras
#Iracema
#Iraucuba
#Itaicaba
#Itaitinga
#Itapage
#Itapipoca
#Itapiuna
#Itarema
#Itatira
#Jaguaretama
#Jaguaribara
#Jaguaribe
#Jaguaruana
#Jardim
#Jati
#Jijoca de Jericoacoara
#Juazeiro do Norte
#Jucas
#Lavras da Mangabeira
#Limoeiro do Norte
#Madalena
#Maracanau
#Maranguape
#Marco
#Martinopole
#Massape
#Mauriti
#Meruoca
#Milagres
#Milha
#Miraima
#Missao Velha
#Mombaca
#Monsenhor Tabosa
#Morada Nova
#Moraujo
#Morrinhos
#Mucambo
#Mulungu
#Nova Olinda
#Nova Russas
#Novo Oriente
#Ocara
#Oros
#Pacajus
#Pacatuba
#Pacoti
#Pacuja
#Palhano
#Palmacia
#Paracuru
#Paraipaba
#Parambu
#Paramoti
#Pedra Branca
#Penaforte
#Pentecoste
#Pereiro
#Pindoretama
#Piquet Carneiro
#Pires Ferreira
#Poranga
#Porteiras
#Potengi
#Potiretama
#Quiterianopolis
#Quixada
#Quixela
#Quixeramobim
#Quixere
#Redencao
#Reriutaba
#Russas
#Saboeiro
#Salitre
#Santa Quiteria
#Santana do Acarau
#Santana do Cariri
#Sao Benedito
#Sao Goncalo do Amarante
#Sao Joao do Jaguaribe
#Sao Luis do Curu
#Senador Pompeu
#Senador Sa
#Sobral
#Solonopole
#Tabuleiro do Norte
#Tamboril
#Tarrafas
#Taua
#Tejucuoca
#Tiangua
#Trairi
#Tururu
#Ubajara
#Umari
#Umirim
#Uruburetama
#Uruoca
#Varjota
#Varzea Alegre
#Vicosa do Ceara
#)    
    
#View normalmente usada no response_add e response_change do ModelAdmin para cropar imagem.
def cropar_imagem_view(request, imagem_name, post_redirect = "../"):
    if imagem_name:
        imagem_src = "%s/%s" % (settings.MEDIA_URL, imagem_name)
        imagem_root = "%s/%s" % (settings.MEDIA_ROOT, imagem_name)
        if request.method == "POST":
            try:
                dimensao_crop = (int(request.POST['x']), int(request.POST['y']), int(request.POST['x2']), int(request.POST['y2']))
                imagem = Image.open(imagem_root)       
                imagem_crop = imagem.crop(dimensao_crop)
                imagem_crop.save(imagem_root, imagem.format)
                request.session['obj_crop'].criar_miniaturas()
                request.session['obj_crop'] = None
            except Exception:
                pass
            redirecionar = request.POST['redirect']
            path_redirect = redirecionar[0:-5]    
            return HttpResponseRedirect(path_redirect)
        variaveis = RequestContext(request, {'imagem_name': imagem_name, 'imagem_src': imagem_src, 'post_redirect': request.path})
        return render_to_response('crop_padrao.html', variaveis)
    else:
        return HttpResponseRedirect("../")

#Faz uma requisição ao ceplivre para consutar um cep.    
def pesquisar_cep_view(request, cep):
    url = "http://ceplivre.pc2consultoria.com/index.php?module=cep&cep=%s&formato=xml" % cep
    pagina = urllib2.urlopen(url)
    dom = minidom.parse(pagina)
    xml = dom.firstChild
    ceplivre = xml.childNodes[1]
    tags = {}
    for tag in ceplivre.childNodes:
            if tag.nodeType == tag.ELEMENT_NODE:
                if tag.firstChild:
                    tags[tag.tagName] = tag.firstChild.data
    variaveis = RequestContext(request, tags)
    return render_to_response("detalhe_cep.html", variaveis)

#Consome o webservice dos correios para calculo de frete
#Codigo de serviços
#41106 - PAC
#40010 - SEDEX
#40215 - SEDEX 10
#40290 - SEDEX HOJE
#81019 - e-SEDEX
#44105 - MALOTE
def calcular_frete_view(request, servico, origem, destino, peso):
    url = "http://www.correios.com.br/encomendas/precos/calculo.cfm?resposta=xml&servico=%s&cepOrigem=%s&cepDestino=%s&peso=%s" % (
        servico, origem, destino, peso)
    pagina = urllib2.urlopen(url)
    tags = {}
    try:
        dom = minidom.parse(pagina)
        xml = dom.firstChild        
        dados_postais = xml.childNodes[3]
        for tag in dados_postais.childNodes:
            if tag.nodeType == tag.ELEMENT_NODE:
                if tag.firstChild:
                    tags[tag.tagName] = tag.firstChild.data
        erro = xml.childNodes[5]
        for tag in erro.childNodes:
            if tag.nodeType == tag.ELEMENT_NODE:
                if tag.firstChild:
                    tags[tag.tagName] = tag.firstChild.data
    except ExpatError:
        pass
    variaveis = RequestContext(request, tags)
    return render_to_response("calculo_frete.html", variaveis)

   
    