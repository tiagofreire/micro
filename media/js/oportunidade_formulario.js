        function enviar_curriculo(){
            if (validarNome($("#id_nome").val()) == false){
                $("#erros").html("Preencha o campo nome corretamente."); 
            }
            else if (validarEmail($("#id_email").val()) == false){
                $("#erros").html("Preencha o campo email corretamente.");
            }
            else if ($("#id_sexo").val() == "Selecione"){
                $("#erros").html("Selecione um sexo.");
            }
            else if ($("#id_estado_civil").val() == "Selecione"){
                $("#erros").html("Selecione seu estado civil.");
            }
            else if ($("#id_filhos").val() == "Selecione"){
                $("#erros").html("Selecione a quantidade de filhos que possui.");
            }   
            else if ($("#id_dia").val() == "" || $("#id_dia").val() == "__"){
                $("#erros").html("Informe o dia do seu nascimento.");
            } 
            else if ($("#id_mes").val() == "" || $("#id_dia").val() == "__"){
                $("#erros").html("Informe o mês do seu nascimento.");
            }
            else if ($("#id_ano").val() == "" || $("#id_dia").val() == "____"){
                $("#erros").html("Informe o ano do seu nascimento.");
            }     
            else if ($("#id_ddd_telefone").val() == "" || $("#id_ddd_telefone").val() == "(__)"){
                $("#erros").html("Informe o DDD do seu telefone.");
            }
            else if ($("#id_telefone").val() == "" || $("#id_telefone").val() == "____-____"){
                $("#erros").html("Informe o seu telefone.");
            }
            else if ($("#id_ddd_celular").val() == "" || $("#id_ddd_celular").val() == "(__)"){
                $("#erros").html("Informe o DDD do seu celular.");
            }
            else if ($("#id_celular").val() == "" || $("#id_celular").val() == "____-____"){
                $("#erros").html("Informe o seu celular.");
            }    
            else if ($("#id_endereco").val() == ""){
                $("#erros").html("Informe seu endereço.");
            }
            else if ($("#id_complemento").val() == ""){
                $("#erros").html("Informe o complemento do seu endereço.");
            }
            else if ($("#id_bairro").val() == ""){
                $("#erros").html("Informe seu bairro.");
            }
            else if ($("#id_estado").val() == ""){
                $("#erros").html("Informe seu estado.");
            }
            else if ($("#id_cidade").val() == ""){
                $("#erros").html("Informe sua cidade.");
            }
            else if (validarCPF($("#id_cpf").val()) == false){
                $("#erros").html("Informe um número de CPF valido.");
            } 
            else if ($("#id_salario").val() == ""){
                $("#erros").html("Informe sua pretensão salarial.");
            } 
            else if ($("#id_medio_instituicao").val() == ""){
                $("#erros").html("Informe sua instituição do Ensino Médio.");
            }
            else if ($("#id_medio_status").val() == "Selecione"){
                $("#erros").html("Informe seu Status no Ensino Médio.");
            }
            else if ($("#id_medio_status").val() == "0"){
                if ($("#id_medio_serie").val() == ""){
                    $("#erros").html("Informe sua série no Ensino Médio.");
                }
                else if ($("#id_medio_conclusao").val() == ""){
                    $("#erros").html("Informe a previsão de término do Ensino Médio.");
                }      
            }
            else if ($("#id_medio_status").val() == "1"){
                if ($("#id_medio_conclusao").val() == ""){
                    $("#erros").html("Informe a previsão de término do Ensino Médio.");
                }      
            }  
            else if ($("#id_graduacao_instituicao").val() == ""){
                $("#erros").html("Informe sua instituição de Graduação.");
            }
            else if ($("#id_graduacao_status").val() == "Selecione"){
                $("#erros").html("Informe seu Status na Graduação.");
            }
            else if ($("#id_graduacao_status").val() == "0"){
                if ($("#id_graduacao_semestre").val() == ""){
                    $("#erros").html("Informe seu semestre na Graduação.");
                }
                else if ($("#id_graduacao_conclusao").val() == ""){
                    $("#erros").html("Informe a previsão de término da Graduação.");
                }      
            }
            else if ($("#id_graduacao_status").val() == "1"){
                if ($("#id_graduacao_conclusao").val() == ""){
                    $("#erros").html("Informe o ano de término da Graduação.");
                }      
            }
            else if ($("#id_pos_graduacao_instituicao").val() == ""){
                $("#erros").html("Informe sua instituição de Pós-Graduação.");
            }
            else if ($("#id_posgraduacao_status").val() == "Selecione"){
                $("#erros").html("Informe seu Status na Pós-Graduação.");
            }
            else if ($("#id_posgraduacao_status").val() == "0"){
                if ($("#id_pos_graduacao_semestre").val() == ""){
                    $("#erros").html("Informe seu semestre na Pós-Graduação.");
                }
                else if ($("#id_pos_graduacao_conclusao").val() == ""){
                    $("#erros").html("Informe a previsão de término da Pós-Graduação.");
                }      
            }
            else if ($("#id_posgraduacao_status").val() == "1"){
                if ($("#id_pos_graduacao_conclusao").val() == ""){
                    $("#erros").html("Informe o ano de término da Pós-Graduação.");
                }      
            }
            else if ($("#id_curso_nome").val() == ""){
                $("#erros").html("Informe o nome do curso ou palestra.");
            }
            else if ($("#id_curso_instituicao").val() == ""){
                $("#erros").html("Informe a instituição do curso ou palestra.");
            }
            else if ($("#id_curso_periodo_de").val() == ""){
                $("#erros").html("Informe quando começou o curso.");
            }
            else if ($("#id_curso_periodo_a").val() == ""){
                $("#erros").html("Informe quando términou o curso.");
            }
            else if ($("#id_curso_complementar").val() == ""){
                $("#erros").html("Informe os dados complementares do curso.");
            } 
            else if ($("#id_ultima_empresa").val() == ""){
                $("#erros").html("Informe a última empresa em que trabalhou.");
            }
            else if ($("#id_ultima_salario").val() == ""){
                $("#erros").html("Informe o valor do seu salário na última empresa em que trabalhou.");
            }
            else if ($("#id_ultima_funcao").val() == ""){
                $("#erros").html("Informe a sua função na última empresa em que trabalhou.");
            }
            else if ($("#id_ultima_periodo_de").val() == ""){
                $("#erros").html("Informe quando entrou na última empresa em que trabalhou.");
            }
            else if ($("#id_ultima_periodo_a").val() == ""){
                $("#erros").html("Informe quando saiu da última empresa em que trabalhou.");
            }
            else if ($("#id_ultima_atividades_desenvolvidas").val() == ""){
                $("#erros").html("Informe as atividades desenvolvidas na última empresa em que trabalhou.");
            }
            else if ($("#id_ultima_motivo_saida").val() == ""){
                $("#erros").html("Informe o motivo da saída da última empresa em que trabalhou.");
            }
            else if ($("#id_penultima_empresa").val() == ""){
                $("#erros").html("Informe a penúltima empresa em que trabalhou.");
            }
            else if ($("#id_penultima_salario").val() == ""){
                $("#erros").html("Informe o valor do seu salário na penúltima empresa em que trabalhou.");
            }
            else if ($("#id_penultima_funcao").val() == ""){
                $("#erros").html("Informe a sua função na penúltima empresa em que trabalhou.");
            }
            else if ($("#id_penultima_periodo_de").val() == ""){
                $("#erros").html("Informe quando entrou na penúltima empresa em que trabalhou.");
            }
            else if ($("#id_penultima_periodo_a").val() == ""){
                $("#erros").html("Informe quando saiu da penúltima empresa em que trabalhou.");
            }
            else if ($("#id_penultima_atividades_desenvolvidas").val() == ""){
                $("#erros").html("Informe as atividades desenvolvidas na penúltima empresa em que trabalhou.");
            }
            else if ($("#id_penultima_motivo_saida").val() == ""){
                $("#erros").html("Informe o motivo da saída da penúltima empresa em que trabalhou.");
            }
            else if ($("#id_antepenultima_empresa").val() == ""){
                $("#erros").html("Informe a antepenúltima empresa em que trabalhou.");
            }
            else if ($("#id_antepenultima_salario").val() == ""){
                $("#erros").html("Informe o valor do seu salário na antepenúltima empresa em que trabalhou.");
            }
            else if ($("#id_antepenultima_funcao").val() == ""){
                $("#erros").html("Informe a sua função na antepenúltima empresa em que trabalhou.");
            }
            else if ($("#id_antepenultima_periodo_de").val() == ""){
                $("#erros").html("Informe quando entrou na antepenúltima empresa em que trabalhou.");
            }
            else if ($("#id_antepenultima_periodo_a").val() == ""){
                $("#erros").html("Informe quando saiu da antepenúltima empresa em que trabalhou.");
            }
            else if ($("#id_antepenultima_atividades_desenvolvidas").val() == ""){
                $("#erros").html("Informe as atividades desenvolvidas na antepenúltima empresa em que trabalhou.");
            }
            else if ($("#id_antepenultima_motivo_saida").val() == ""){
                $("#erros").html("Informe o motivo da saída da antepenúltima empresa em que trabalhou.");
            }     
            else if ($("#id_login").val() == ""){
                $("#erros").html("Informe seu login.");
            }
            else if ($("#id_senha").val() == ""){
                $("#erros").html("Informe sua senha.");
            }
            else if ($("#id_senha2").val() == ""){
                $("#erros").html("Repita a senha.");
            }
            else if ($("#id_senha").val() != $("#id_senha2").val()){
                $("#erros").html("As senhas não coincidem.");
            }
            else {
                $("#id_form_rh").submit();
            }
            window.location.href = "#ancora_erros";
        }

        function medio_conclusao_validar(){            
            if($("#id_medio_status").val() == "1"){
                $("#div_medio_serie").css("display", "none");  
                $("#label_medio_conclusao").html("Ano de conclusão"); 
            }
            else {
                $("#div_medio_serie").fadeIn("slow");  
                $("#label_medio_conclusao").html("Previsão de Término");   
            }  
        }

        function graduacao_conclusao_validar(){            
            if($("#id_graduacao_status").val() == "1"){
                $("#div_graduacao_semestre").css("display", "none");  
                $("#label_graduacao_conclusao").html("Ano de conclusão"); 
            }
            else {
                $("#div_graduacao_semestre").fadeIn("slow");  
                $("#label_graduacao_conclusao").html("Previsão de Término");   
            }  
        }

        function posgraduacao_conclusao_validar(){            
            if($("#id_posgraduacao_status").val() == "1"){
                $("#div_posgraduacao_semestre").css("display", "none");  
                $("#label_posgraduacao_conclusao").html("Ano de conclusão"); 
            }
            else {
                $("#div_posgraduacao_semestre").fadeIn("slow");  
                $("#label_posgraduacao_conclusao").html("Previsão de Término");   
            }  
        }

        function setar_nova_foto(caminho){
            $("#foto_curriculo").attr("src", caminho);
            $("#id_foto").val(caminho);
        } 
