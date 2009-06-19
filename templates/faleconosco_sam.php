<?php include("_topo.php"); ?>
	<div id="categoria" class="grid_12">
        <h2>Fale conosco</h2>
        <ul>
            <li><a href="#" class="sub-ativo" title="Serviço de Atendimento Microsol">Serviço de Atendimento Microsol</a></li>
            <li><a href="#" title="Departamentos">Departamentos</a></li>
            <li><a href="#" title="Contato">Contato</a></li>
        </ul>
    </div>
    <div class="clr">&nbsp;</div>
    
    <div id="faleconosco" class="grid_12">
    	<p>A Microsol dispõe do serviço de atendimento ao cliente, visando identificar dúvidas, sugestões, críticas e elogios, oferecendo soluções adequadas a cada caso.<br />Para entrar em contato conosco, preencha o formulário abaixo.</p>
        <p><em>O prazo de retorno das solicitações será de até 48 horas úteis.</em></p>
        <form>
        	<fieldset>
                <legend>Contato</legend>
                
                <div class="grid_6 alpha">
                	<label>Nome *</label>
                    <input type="text" class="ipt_faleconosco" />
                    <br />
                    
                    <div class="grid_4 alpha">
                        <label>E-mail *</label>
                        <input type="text" class="ipt_email" />
                    </div>
                    
                    <div class="grid_2 omega">
                        <label>DDD/Telefone *</label>
                        <input type="text" class="ipt_ddd" />
                        <input type="text" class="ipt_fone" />
                    </div>
                    <div class="clear">&nbsp;</div>
                    
                    <div class="grid_2 alpha">
                        <label>Estado *</label>
                        <select>
                            <option value="Selecione">Selecione</option>
                            <option value="AC">AC</option>
                            <option value="AL">AL</option>
                            <option value="AM">AM</option>
                            <option value="AP">AP</option>
                            <option value="BA">BA</option>
                            <option value="CE">CE</option>
                            <option value="DF">DF</option>
                            <option value="ES">ES</option>
                            <option value="GO">GO</option>
                            <option value="MA">MA</option>
                            <option value="MG">MG</option>
                            <option value="MS">MS</option>
                            <option value="MT">MT</option>
                            <option value="PA">PA</option>
                            <option value="PB">PB</option>
                            <option value="PE">PE</option>
                            <option value="PI">PI</option>
                            <option value="PR">PR</option>
                            <option value="RJ">RJ</option>
                            <option value="RN">RN</option>
                            <option value="RO">RO</option>
                            <option value="RR">RR</option>
                            <option value="RS">RS</option>
                            <option value="SC">SC</option>
                            <option value="SE">SE</option>
                            <option value="SP">SP</option>
                            <option value="TO">TO</option>
                        </select>
                    </div>
                    
                    <div class="grid_2">
                        <label>Cidade *</label>
                        <select>
                            <option>Selecione</option>
                        </select>
                    </div>
                    <div class="clear">&nbsp;</div>
                    
                    <div class="grid_2 alpha">
                    	<label>Sexo</label>
                        <input type="radio" class="rdo" name="sexo" id="sexo_m" /> <label class="lbl_rdo" for="sexo_m">Masculino</label><br clear="all" />
                        <input type="radio" class="rdo" name="sexo" id="sexo_f" /> <label class="lbl_rdo" for="sexo_f">Feminino</label><br clear="all" />
                    </div>
                    
                    <div class="grid_4 omega">
                    	<label>Tipo de contato</label>
                    </div>
                    
                    <div class="grid_2">
                        <input type="radio" class="rdo" name="tipo" id="tipo_elo" /> <label for="tipo_elo" class="lbl_rdo">Elogio</label><br clear="all" />
                        <input type="radio" class="rdo" name="tipo" id="tipo_rec" /> <label for="tipo_rec" class="lbl_rdo">Reclamação</label><br clear="all" />
                    </div>
                    <div class="grid_2 omega">
                        <input type="radio" class="rdo" name="tipo" id="tipo_sug" /> <label for="tipo_sug" class="lbl_rdo">Sugestão</label><br clear="all" />
                        <input type="radio" class="rdo" name="tipo" id="tipo_inf" /> <label for="tipo_inf" class="lbl_rdo">Pedido de informação</label><br clear="all" />
                    </div>
                    <div class="clear">&nbsp;</div>
                </div>
                
                <div class="grid_6 omega">
                    <label>Descrição *</label>
                    <textarea class="sam"></textarea>
                    <br />
                    
                    <input type="checkbox" class="cbx" /> <label class="lbl_cbx">Desejo receber novidades da Microsol</label>

                    <a href="#" class="btn btn-enviar fr" title="Enviar">Enviar</a>
                </div>
                <div class="clear">&nbsp;</div><br />
                <p><em>* Campos obrigatórios</em></p>
            </label>
        </form>
    </div>
    <div class="clear">&nbsp;</div>
<?php include("_rodape.php"); ?>