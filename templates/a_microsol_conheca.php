{% extends "base.html" %}
{% block "conteudo" %}
	<div id="categoria" class="grid_12">
        <h2>{{pagina.titulo}}</h2>
        <ul>
            <li><a href="/a_microsol/a_empresa/" title="A Empresa">A Empresa</a></li>
            <li><a href="/a_microsol/conheca/" class="sub-ativo" title="Conheça a Microsol">Conheça a Microsol</a></li>
            <li><a href="/a_microsol/qualidade_e_premios/" title="Qualidade e Prêmios">Qualidade e Prêmios</a></li>
        </ul>
    </div>
    <div class="clr">&nbsp;</div>
    
    <div class="grid_6"><img src="{{MEDIA_URL}}img/conheca_01.jpg" alt="Microsol - Conheça"  /></div>
    <div id="conheca" class="grid_6">
		<h3>A Microsol</h3>
		<p>Com 25 anos de história focados em tecnologia e inovação, a Microsol é uma das três maiores empresas brasileiras do setor de condicionadores de energia. Nossa missão é oferecer soluções tecnológicas para manter protegidos sonhos, dados e idéias, encantando clientes, acionista e colaboradores.</p>
    </div>
    <div class="clear">&nbsp;</div>
    
    <div id="outras-imagens" class="grid_12">
    	<h3>Outras imagens</h3>
        <ul>
        	<li><a href="#" title="MIE"><img src="{{MEDIA_URL}}img/outrosprodutos_mie.jpg" width="76" height="76" alt="MIE" /></a></li>
        	<li><a href="#" title="MI 1.0"><img src="{{MEDIA_URL}}img/outrosprodutos_mi10.jpg" width="76" height="76" alt="MI 10" /></a></li>
        </ul>
    </div>
    <div class="clear">&nbsp;</div>
    
    <div id="evolucao" class="grid_12">
        <h3>Nossa história</h3>
        <script type="text/javascript">
	    AC_FL_RunContent( 'codebase','http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=9,0,28,0','width','468','height','100','src','{{MEDIA_URL}}swf/banner','quality','high','pluginspage','http://www.adobe.com/shockwave/download/download.cgi?P1_Prod_Version=ShockwaveFlash','movie','{{MEDIA_URL}}swf/banner' ); //end AC code
	</script>
	<noscript>
            <object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=9,0,28,0" width="468" height="100">
            <param name="movie" value="{{MEDIA_URL}}swf/banner.swf" />
            <param name="quality" value="high" />
            <embed src="{{MEDIA_URL}}swf/banner.swf" quality="high" pluginspage="http://www.adobe.com/shockwave/download/download.cgi?P1_Prod_Version=ShockwaveFlash" type="application/x-shockwave-flash" width="468" height="100"></embed>
            </object>
        </noscript>
    </div>
    <div class="clear">&nbsp;</div>
{% endblock %}
