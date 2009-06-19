<?php include("_topo.php"); ?>
	<div id="categoria" class="grid_12">
        <h2>Fale conosco</h2>
        <ul>
            <li><a href="#" title="Serviço de Atendimento Microsol">Serviço de Atendimento Microsol</a></li>
            <li><a href="#" title="Departamentos">Departamentos</a></li>
            <li><a href="#" class="sub-ativo" title="Contato">Contato</a></li>
        </ul>
    </div>
    <div class="clr">&nbsp;</div>
    
    <div id="faleconosco" class="grid_12">
        <form>
        	<fieldset>
                <legend>Contato</legend>
                
                <div class="grid_6 alpha">
                	<label>Nome</label>
                    <input type="text" class="ipt_faleconosco" />
                    <br />
                    
                    <div class="grid_4 alpha">
                        <label>E-mail</label>
                        <input type="text" class="ipt_email" />
                    </div>
                    
                    <div class="grid_2 omega">
                    <label>DDD/Telefone</label>
                    <input type="text" class="ipt_ddd" />
                    <input type="text" class="ipt_fone" />
                    </div>
                    <div class="clear">&nbsp;</div>
                    
                    <div class="grid_2 alpha">
                        <label>Setor</label>
                        <select>
                            <option>Comercial</option>
                            <option>Marketing</option>
                        </select>
                    </div>
                    
                    <div class="grid_2">
                        <label>Estado</label>
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
                    
                    <div class="grid_2 omega">
                        <label>Cidade</label>
                        <select>
                            <option>Selecione</option>
                        </select>
                    </div>
                    <div class="clear">&nbsp;</div>
                </div>
                
                <div class="grid_6 omega">
                    <label>Mensagem</label>
                    <textarea></textarea>
                    <br />
                    
                    <input type="checkbox" class="cbx" /> <label class="lbl_cbx">Desejo receber novidades da Microsol</label>
                </div>
                <div class="clear">&nbsp;</div>
                
                <a href="#" class="btn btn-enviar fr" title="Enviar">Enviar</a>
            </label>
        </form>
    </div>
    <div class="clear">&nbsp;</div>
<?php include("_rodape.php"); ?>