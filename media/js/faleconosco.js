//Validações para o formulario Fale Conosco

function validar_faleconosco(){
    if(validarNome($("#id_nome").val()) == false){
        $("#info_faleconosco").html("O nome não está preenchido corretamente.");
        return false;
    }
    if(validarEmail($("#id_email").val()) == false){
        $("#info_faleconosco").html("O email não está preenchido corretamente.");
        return false;
    }
   return false;
}
