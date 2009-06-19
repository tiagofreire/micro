{% extends "base.html" %}
{% block "conteudo" %}
	<div id="categoria" class="grid_12">
        <h2>Mídia</h2>
        <ul>
            <li><a href="#" class="sub-ativo" title="Informativo">Informativo</a></li>
            <li><a href="#" title="Notícias">Notícias</a></li>
            <li><a href="#" title="Publicidade">Publicidade</a></li>
            <li><a href="#" title="Hotsites">Hotsites</a></li>
            <li><a href="#" title="Manual da Marca">Manual da Marca</a></li>
        </ul>
    </div>
    <div class="clr">&nbsp;</div>
    
    <div class="grid_5 alpha">
    	<img src="img/img_dtq_int_placeholder.jpg" alt="Mídia"  />
    </div>
    
    <div id="chamada" class="grid_7 omega">
        <p>Assine nosso Informativo para receber no seu email nossas notícias e novidades sobre as linhas de produtos Microsol.</p>
        <form id="informativo" class="informativo_int">
            <label>Seu nome</label> <input type="text" value="Seu nome" class="ipt_informativo" />
            <label>Seu e-mail</label> <input type="text" value="Seu e-mail" class="ipt_informativo" />
            <a href="#" title="Enviar" class="btn btn-enviar fr">Enviar</a>
        </form>
    </div>
    <div class="clear">&nbsp;</div>
    
    <div id="outros-links" class="grid_12">
    	<h2>Últimas Notícias</h2>
        <!-- LISTA COM AS 5 ULTIMAS NOTÍCIAS -->
        <div class="grid_6 alpha">
            <ul>
               {% for noticia in noticias|slice:":5" %}
                   <li><a href="#" title="">{{noticia.titulo}}</a></li>
               {% endfor %}
            </ul>
        </div>
        
        <!-- LISTA COM AS OUTRAS 5 ULTIMAS NOTÍCIAS COM OFFSET 5 -->
        <div class="grid_6 omega">
            <ul>
                {% for noticia in noticias|slice:"5:" %}
                   <li><a href="#" title="">{{noticia.titulo}}</a></li>
               {% endfor %}
            </ul>
        </div>
    </div>
{% endblock %}
