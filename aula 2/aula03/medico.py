from funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, matricula, nome, telefone, email, cpf, rg, crm, especialidade, horario):
        super().__init__(matricula, nome, telefone, email, cpf, rg, 'Medico')   #<--- A plicando a herança na class
        self.crm = crm
        self.especialidade = especialidade
        self.horario = horario

    def informacao(self):
        print(f"{self.nome} horarios: {self.horario} / cargo: {self.especialidade}")
        

       



