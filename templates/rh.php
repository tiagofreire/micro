<?php include("_topo.php"); ?>
	<div id="categoria" class="grid_12">
        <h2>Recursos Humanos</h2>
    </div>
    <div class="clr">&nbsp;</div>
    
    <div id="rh" class="grid_12">
    	<p>Para cadastrar seu currículo em nosso banco de dados por favor preencha todas as informações abaixo:</p>
        <form>
        	<fieldset>
                <legend>Contato</legend>
                
                <div class="grid_6 alpha">
                    <label>Nome</label>
                    <input type="text" class="ipt_nomerh" tabindex="1" />
                    <div class="clear">&nbsp;</div>
                    
                    <div class="grid_4 alpha">
                        <label>E-mail</label>
                        <input type="text" class="ipt_email" tabindex="2" />
                    </div>
                    
                    <div class="grid_2 omega">
                    	<label>Sexo</label>
                        <select tabindex="3">
                            <option>Selecione</option>
                            <option>Masculino</option>
                            <option>Feminino</option>
                        </select>
                    </div>
                    <div class="clear">&nbsp;</div>
                    
                    <div class="grid_2 alpha">
                        <label>Data de Nascimento</label>
                        <input type="text" class="ipt_dia" tabindex="4" />
                        <input type="text" class="ipt_mes" tabindex="5" />
                        <input type="text" class="ipt_ano" tabindex="6" />
                    </div>
                    
                    <div class="grid_2">
                        <label>DDD/Telefone</label>
                        <input type="text" class="ipt_ddd" tabindex="7" />
                        <input type="text" class="ipt_fone" tabindex="8" />
                    </div>
                    
                    <div class="grid_2 omega">
                        <label>DDD/Celular</label>
                        <input type="text" class="ipt_ddd" tabindex="9" />
                        <input type="text" class="ipt_fone" tabindex="10" />
                    </div>
                    <div class="clear">&nbsp;</div>
                    
                    <label>Endereço</label>
                    <input type="text" class="ipt_endereco" tabindex="11" />
                    <div class="clear">&nbsp;</div>
                    
                    <div class="grid_2 alpha">
                        <label>Bairro</label>
                        <input type="text" class="ipt_bairro" tabindex="13" />
                    </div>
                    
                    <div class="grid_2">
                        <label>Estado</label>
                        <select tabindex="14">
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
                    
                    <div class="grid_2 omega">
                        <label>Cidade</label>
                        <select tabindex="15">
                            <option>Selecione</option>
                        </select>
                    </div>
                    <div class="clear">&nbsp;</div>
                    
                    <div class="grid_2 alpha">
                        <label>Área de Formação</label>
                        <input type="text" class="ipt_area" tabindex="16" />
                    </div>
                    
                    <div class="grid_4 omega"><label>Instituição</label></div>
                    <div class="grid_2">
                    	<input type="text" class="ipt_area" tabindex="17" />
                    </div>
                    <div class="grid_2 omega">
                        <input type="radio" class="rdo" name="tipo" id="tipo_elo" tabindex="18" /> <label for="tipo_elo" class="lbl_rdo">Concluído</label><br clear="all" />
                        <input type="radio" class="rdo" name="tipo" id="tipo_rec" tabindex="19" /> <label for="tipo_rec" class="lbl_rdo">Em andamento</label><br clear="all" />
                    </div>
                    <div class="clear">&nbsp;</div>
                    
                    <label>Pós-Graduaçao</label>
                    <input type="text" class="ipt_endereco" tabindex="20" />
                    <div class="clear">&nbsp;</div>
                </div>
                
                <div class="grid_6 omega">
                    <label>Experiência Profissional</label>
                    <textarea tabindex="21"></textarea>
                    <br />
                    
                    <label>Conhecimentos em idiomas</label>
                    <textarea tabindex="22"></textarea>
                    <br />
                    
                    <label>Mini-currículo</label>
                    <textarea class="minicv" tabindex="23"></textarea>
                    <br />
                    
                    <input type="checkbox" class="cbx" tabindex="24" /> <label class="lbl_cbx">Desejo receber novidades da Microsol</label>

                    <a href="#" class="btn btn-enviar fr" title="Enviar" tabindex="25">Enviar</a>
                </div>
                <div class="clear">&nbsp;</div>
            </label>
        </form>
    </div>
    <div class="clear">&nbsp;</div>
<?php include("_rodape.php"); ?>