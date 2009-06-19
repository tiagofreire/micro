#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.conf import settings
from models import Foto, Galeria

#Importa a biblioteca grafica do Python (PIL - Python Imaging Library)
try:
    import Image
except ImportError:
    try:
        from micro.modulos.PIL import Image
    except ImportError:
        raise ImportError(u"Index Gallery n\u00E3o conseguiu importar a biblioteca de imagem do Pytho (Python Imaging Library).")


#View usada para visualizar a pagina de manipulação de fotos e para cropar uma foto.    
def manipular_foto(request, foto) :
    objFoto = Foto.objects.get(id = foto)
    thumbnails = objFoto.thumbnails.all()
    if request.method == "POST" :
        cropDimensao = (int(request.POST['x']), int(request.POST['y']), int(request.POST['x2']), int(request.POST['y2']))
        imagemCaminho = "%s/%s" % (settings.MEDIA_ROOT, objFoto.arquivo)
        imagem = Image.open(imagemCaminho)       
        imagemCrop = imagem.crop(cropDimensao)
        imagemCrop.save(imagemCaminho, imagem.format)
        objFoto.save()
        objFoto.criar_miniaturas()
        objFoto.criar_miniatura_admin()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    variaveis = RequestContext(request, {'foto': objFoto, 'thumbnails': thumbnails, "idObjeto":objFoto.id})
    return render_to_response('index_gallery/manipular_foto_padrao.html', variaveis)

#View usada para redimensionar uma foto    
def redimensionar_foto(request, foto):
    objFoto = Foto.objects.get(id = foto)
    thumbnails = objFoto.thumbnails.all()
    if request.method == "POST":
        altura = int(request.POST['alturaField'])
        largura = int(request.POST['larguraField'])
        imagemCaminho = "%s/%s" % (settings.MEDIA_ROOT, objFoto.arquivo)
        imagem = Image.open(imagemCaminho)
        imagemResize = imagem.resize((largura, altura))
        imagemResize.save(imagemCaminho, imagem.format)
        objFoto.save()
        objFoto.criar_miniaturas()
        objFoto.criar_miniatura_admin()
    variaveis = RequestContext(request, {'foto': objFoto, 'thumbnails': thumbnails, "idObjeto":objFoto.id})    
    return render_to_response('index_gallery/manipular_foto_padrao.html', variaveis) 

#Listar todas as galerias
def listar_galerias_view(request):
    galerias = Galeria.objects.all()
    variaveis = RequestContext(request, {'galerias': galerias})
    return render_to_response('index_gallery/listar_galerias.html', variaveis)

#Retorna uma pagina html usada para visualizar a galeria que possui o id passado na url
def visualizar_galeria_view(request, galeria_id):
    try:
        galeria = Galeria.objects.get(id = galeria_id)
        variaveis = RequestContext(request, {'galeria': galeria})
    except Galeria.DoesNotExist:
        variaveis = RequestContext(request, {'galeria': None})
    return render_to_response('index_gallery/visualizar_galeria.html', variaveis)

#Retorna uma pagina html contendo todas as galerias de determinado autor
def visualizar_galerias_por_autor_view(request, autor_username):
    galerias = Galeria.objects.filter(autor__username = autor_username).all()
    variaveis = RequestContext(request, {'galerias': galerias})
    return render_to_response('index_gallery/galerias_por_autor.html', variaveis)

#Retorna uma pagina html contendo todas as galerias de determinada categoria
def visualizar_galerias_por_categoria_view(request, categoria_slug):
    galerias = Galeria.objects.filter(categoria__nome_slug = categoria_slug).all()
    variaveis = RequestContext(request, {'galerias': galerias})
    return render_to_response('index_gallery/galerias_por_autor.html', variaveis)

#Retorna uma pagina html contendo todas as galerias de determinada autor em determinada categoria
def visualizar_galerias_por_categoria_autor_view(request, categoria_slug, autor_username):
    galerias = Galeria.objects.filter(categoria__nome_slug = categoria_slug).filter(autor__username = autor_username).all()
    variaveis = RequestContext(request, {'galerias': galerias})
    return render_to_response('index_gallery/galerias_por_autor.html', variaveis)
                
