from classe import Pessoa


# A dicionado a herança na class 


class Aluno(Pessoa):
    def __init__(self, nome, data_nacimento, sexo,matricula):
        super().__init__(nome, data_nacimento, sexo)   #<--- A plicando a herança na class
        self.matricula = matricula

aluno1 = Aluno("Henrique Rafael", "06/05/1999", "masculino",224158)

print(" ********* Dados do Aluno **********")
print("Matricula: ", aluno1.matricula)
print("Nome: ", aluno1.nome)
print("Data de Nascimento: ", aluno1.data_nascimento)
print("Sexo: ", aluno1.sexo)