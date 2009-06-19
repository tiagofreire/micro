//Possui funções utilitarias para validação de algums campos comuns em formularios, tais como email, cpf, etc...

//Faz a validação do email passado como argumento para a função e retorna true se for um email valido, caso contrario retorna false.
function validarEmail(email) {
   var expressaoRegular = new RegExp('^([a-zA-Z0-9._%+-])+@[a-zA-Z0-9.-]+\\.[a-z]{2,4}$');//Expressão regular para validar email.
	
   if (expressaoRegular.test(email)) {
	   return true;
   }
   else {
	   return false;
   }
}

//Faz a validação de um cep no formato 99999-999 passado como argumento para a função e retorna true caso seja um cep valido ou false em caso negativo.
function validarCEP(cep) {
	var expressaoRegular = new RegExp('^([0-9]{5})+-[0-9]{3}$'); //Expressão regular para validar cep.
	
	if (expressaoRegular.test(cep)) {
		return true;
	}
	else {
		return false;
	}
}

//Faz a validação de um numero de telefone no formato (99) 9999-9999 passado como argumento para a função e retorna true caso seja um telefone valido ou false em caso negativo.
function validarTelefone(telefone) {
	var expressaoRegular = new RegExp('^\\(\\d{2}\\)\\s\\d{4}-\\d{4}$'); //Expressão regular para validar o telefone.
	
	if (expressaoRegular.test(telefone)) {
		return true;
	}
	else {
		return false;
	}
}


//Faz a validação de um nome composto apenas de letras passado como argumento para a função e retorna true caso seja um nome valido e false em caso contrario.
function validarNome(nome) {
	var expressaoRegular = new RegExp('^[a-zA-ZÀ-Üà-ü]+( [a-zA-ZÀ-Üà-ü]+)+$'); //Expressão regular para validar nome.
	
	if (expressaoRegular.test(nome)) {
		return true;
	}
	else {
		return false;
	}
}

//Faz a validação de um CPF, verificando se ele está escrito de acordo com o padrão de formatação e verificando se é um número de CPF valido, em caso afirmativo retorna true, caso contrario retorna false.
function validarCPF(cpf) {
	var expressaoRegular =  new RegExp('^([0-9]){3}.([0-9]){3}.([0-9]){3}-([0-9]){2}$'); //Expressão regular para validar cpf
	
   if (expressaoRegular.test(cpf)) {
	   //Começa a verificação para saber se o cpf informado é um número de cpf valido ou não.
	   var numeroCPF = cpf.replace(".", "");
	   numeroCPF = numeroCPF.replace(".", "");
	   numeroCPF = numeroCPF.replace("-", "");
	   var numeroValidador = numeroCPF.substr(9, 2);
	   var soma = 0;
	   var fatorMultiplicador = 10;
	   var resto = 0;
	   var primeiroNumero = 0;
	   var segundoNumero = 0;
	   var i = 0;
	   
	  for (i = 0; i <= 8; i += 1) {
		   soma += parseInt(numeroCPF.substr(i, 1)) * fatorMultiplicador;
		   fatorMultiplicador -= 1;
	   }

	   resto = soma % 11;
	   
	   if (resto > 2) {
		   primeiroNumero = 11 - resto;
	   }
	   else {
		   primeiroNumero = 0;
	   }
	   
	   soma = 0;
	   resto = 0;
	   fatorMultiplicador = 11;
	   
	   for (i = 0; i <= 8; i += 1) {
		   soma += parseInt(numeroCPF.substr(i, 1)) * fatorMultiplicador;
		   fatorMultiplicador -= 1;
	   }
	   
	   soma += primeiroNumero * 2;
	   resto = soma % 11;
	   
	   if (resto > 2) {
		   segundoNumero = 11 - resto;
	   }
	   else {
		   segundoNumero = 0;
	   }
	   
	   var numeroValidadorObtido = primeiroNumero * 10 + segundoNumero;
	      
	   if (numeroValidadorObtido == numeroValidador) {
	      return true;
	   }
	   else {
	      return false;
	   }
	   	  
	}
	else {
		return false;
	}
}

//Faz a validação de um CNPJ, verificando se ele está escrito de acordo com o padrão de formatação e verificando se é um número de CNPJ valido, em caso afirmativo retorna true, caso contrario retorna false.
function validarCNPJ(cnpj) {
	var expressaoRegular =  new RegExp('^([0-9]){2}.([0-9]){3}.([0-9]){3}/([0-9]){4}-([0-9]){2}$'); //Expressão regular para validar cpf
	
   if (expressaoRegular.test(cnpj)) {
	   //Começa a verificação para saber se o cpf informado é um número de cpf valido ou não.
	   var numeroCNPJ = cnpj.replace(".", "");
	   numeroCNPJ = numeroCNPJ.replace(".", "");
	   numeroCNPJ = numeroCNPJ.replace("-", "");
	   numeroCNPJ = numeroCNPJ.replace("/", "");
	   var numeroValidador = numeroCNPJ.substr(12, 2);
	   var numerosMultiplicadores = new Array(5,4,3,2,9,8,7,6,5,4,3,2);
	   var soma = 0;
	   var resto = 0;
	   var primeiroNumero = 0;
	   var segundoNumero = 0;
	   var i = 0;
	   
	  for (i = 0; i < 12; i += 1) {
		   soma += parseInt(numeroCNPJ.substr(i, 1)) * numerosMultiplicadores[i];
	   }
          
	   resto = parseInt(soma) % 11;
	   
	   if (resto > 2) {
		   primeiroNumero = 11 - resto;
	   }
	   else {
		   primeiroNumero = 0;
	   }
	   
	   soma = 0;
	   resto = 0;
	   numerosMultiplicadores = new Array(6,5,4,3,2,9,8,7,6,5,4,3,2);
	   
	   for (i = 0; i < 12; i += 1) {
		   soma += parseInt(numeroCNPJ.substr(i, 1)) * numerosMultiplicadores[i];
	   }
	   
	   soma += primeiroNumero * 2;
	   resto = soma % 11;
	   
	   if (resto > 2) {
		   segundoNumero = 11 - resto;
	   }
	   else {
		   segundoNumero = 0;
	   }
	   
	   var numeroValidadorObtido = primeiroNumero * 10 + segundoNumero;
	      
	   if (numeroValidadorObtido == numeroValidador) {
	      return true;
	   }
	   else {
	      return false;
	   }
	   	  
	}
	else {
		return false;
	}
}
