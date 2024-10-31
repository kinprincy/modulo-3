from funcionario import Funcionario

class Enfermeiro(Funcionario):
    def __init__(self, matricula, nome, telefone, email, cpf, rg, coren, ):
        super().__init__(matricula, nome, telefone, email, cpf, rg, 'Enfermeiro')
        self.coren = coren

  
     