<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<meta name="description" content="{{DESCRIPTION}}" />
	<meta name="keywords" content="{{TAGS}}" />
	<meta name="author" content="Index Comunicação Digital - www.indexvirtual.com" />
	<meta name="reply-to" content="index@indexvirtual.com" />
	<meta name="robots" content="index, follow" />
	<meta name="generator" content="Tibigo 0.5a" />
    <link rel="icon" href="img/favicon.ico" type="image/x-icon"/>


	<link rel="shortcut icon" href="favico.ico" >
	
	<title>Microsol &bull; Energia Inteligente</title>
	
	<!-- 960.gs -->
	<link rel="stylesheet" type="text/css" media="screen, projection" href="css/960/css/960.css" />
	<link rel="stylesheet" type="text/css" media="screen, projection" href="css/960/css/reset.css" />
	<link rel="stylesheet" type="text/css" media="screen, projection" href="css/960/css/text.css" />
	<link rel="stylesheet" type="text/css" media="screen, projection" href="css/geral.css" />
	<link rel="stylesheet" type="text/css" media="screen, projection" href="css/menu.css" />
    <!--[if IE 6]>
        <link rel="stylesheet" href="css/ie6.css" type="text/css" media="screen" />
    <![endif]-->

    
    <!-- jQuery -->
    <!--<script src="js/jquery-1.2.3.min.js" type="text/javascript"></script>
	<script src="js/jquery.dimensions.js" type="text/javascript"></script>
    <script src="js/ui.mouse.js" type="text/javascript"></script>
    <script src="js/ui.slider.js" type="text/javascript"></script>-->
    
	<script src="js/jquery-1.js" type="text/javascript"></script>
    <script src="js/jquery-ui-full-1.js" type="text/javascript"></script>
    
    <script type="text/javascript" charset="utf-8">
        window.onload = function () {
            
			var init = 0;
			var han = Array(16, 181, 376, 571,723);
			var sli = Array(-2, -68, -147, -201,-253);
		 	var valor = 0;
			var container = $('div.sliderGallery');
            var ul = $('ul', container);
            
            var itemsWidth = ul.innerWidth() - container.outerWidth();
            
            $('.slider', container).slider({
                min: 0,
                max: itemsWidth,
                handle: '.handle',
                stop: function (event, ui) {
                    ul.animate({'left' : ui.value * -1}, 500);
                },
                slide: function (event, ui) {
                    ul.css('left', ui.value * -1);
                }
            });
			$('.slider-lbl1').click(function(){
				$('.handle').css('left','16px');
				valor = 0;
			});
			$('.slider-lbl3').click(function(){
				$('.handle').css('left','181px');
				valor = 1;
			});
			$('.slider-lbl4').click(function(){
				$('.handle').css('left','376px');
				valor = 2;
			});
			$('.slider-lbl5').click(function(){
				$('.handle').css('left','571px');
				valor = 3;
			});
			$('.slider-lbl6').click(function(){
				$('.handle').css('left','723px');
				valor = 4;
			});
			$('.slider-right').click(function(){
				valor += 1;
				if(valor < 4 || valor >=0){
					$('.handle').animate({'left': han[valor]+'px'}, 'slow');
					$('.sliderGallery ul').animate({'left': sli[valor]+'px'}, 'slow');
				}
			});
			$('.slider-left').click(function(){
				valor -= 1;
				if(valor >=0 || valor<4){
					$('.handle').animate({'left': han[valor]+'px'}, 'slow');
					$('.sliderGallery ul').animate({'left': sli[valor]+'px'}, 'slow');
				}
			});
        };
    </script>
	
	<!--[if IE 6]>
	<script src="js/DD_belatedPNG_0.0.7a-min.js"></script>
	<script>
		DD_belatedPNG.fix('img, #geral, #topo, #busca, #rodape, #login_home, .bg, .microsol, .banner_tematico, .inicial, .index, .marca, .btn-login, .seta');
	</script>
	<![endif]-->

</head>

<body>
<a name="topo"></a>
<!-- TOPO -->
<div id="topo">
	<div class="container_12">
    	<div id="marcabanner" class="grid_12">
	        <div class="grid_3 alpha"><h1><a href="#" title="Voltar para a página inicial" class="microsol">Microsol &bull; Energia Inteligente</a></h1></div>
    	    <div class="grid_9 omega"><a href="#" class="banner_tematico">Conheça a nova linha de produtos Microsol.</a></div>
        </div>
        <div class="clear">&nbsp;</div>
        
        <div id="nav" class="grid_12">
            <div class="grid_9 alpha"><!-- MENU -->
                <ul class="menu">
                    <li><a href="index.php" title="Voltar para a página inicial" class="inicial">Voltar para a página inicial</a></li>
                    <li><a href="#" title="A Microsol">A Microsol</a></li>
                    <li><a href="../menu/index.html">Produtos<!--[if IE 7]><!--></a><!--<![endif]-->
                        <!--[if lte IE 6]><table><tr><td><![endif]-->
                        <ul>
                            <li><a href="#" title="">Nobreaks</a></li>
                            <li><a href="#" title="">Estabilizadores</a></li>
                            <li><a href="#" title="">Módulos Isoladores</a></li>
                            <li><a href="#" title="">Sob Encomenda</a></li>
                            <li><a href="#" title="">Estabilizadores e Condicionadores</a></li>
                            <li><a href="#" title="">Fontes para Notebook</a></li>
                            <li><a href="#" title="">Descontinuados</a></li>
                            <li><a href="#" title="">Acessórios</a></li>
                            <li><a href="#" title="">Softwares</a></li>
                        </ul>
                        <!--[if lte IE 6]></td></tr></table></a><![endif]-->
                    </li>
                    <li><a href="#" title="Catálogo">Catálogo</a></li>
                    <li><a href="#" title="Suporte">Suporte</a></li>
                    <li><a href="#" title="Onde encontrar">Onde encontrar</a></li>
                    <li><a href="#" title="Mídia">Mídia</a></li>
                    <li><a href="#" title="Fale Conosco">Fale Conosco</a></li>
                </ul>
            </div>
            <div class="grid_3 omega"><!-- BUSCA -->
                <form id="busca">
                    <fieldset>
                        <legend>Busca no site</legend>
                        <label>Buscar</label>
                        <input class="ipt_busca" type="text" value="Digite sua busca" />
                    </fieldset>
                </form>
            </div>
        </div>
        <div class="clear">&nbsp;</div>
    </div>
</div>

<!-- MEIO -->
<div id="meio">
	<div class="container_12">