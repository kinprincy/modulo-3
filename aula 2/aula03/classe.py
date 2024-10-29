#string ,date , void
class Pessoa:
    def __init__(self,nome, data_nacimento, sexo):
        self.nome = nome
        self.data_nascimento = data_nacimento
        self.sexo =sexo

    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}")

    

pessoa1 = Pessoa("José", "20/10/1995", "maculino")
pessoa2 = Pessoa("Maria", "01/01/2001", "feminino")
pessoa3 = Pessoa("kinprincy,", "06/05/1999", "masculino")


print("nome:",pessoa1.nome,"data de nascimento:",pessoa1.data_nascimento, "sexo:",pessoa1.sexo)
print("nome:",pessoa2.nome,"data de nascimento:",pessoa2.data_nascimento, "sexo:",pessoa2.sexo)
print("nome:",pessoa3.nome,"data de nascimento:",pessoa3.data_nascimento, "sexo:",pessoa3.sexo)


pessoa1.falar("Ola!")
pessoa2.falar("Oi")
pessoa3.falar("Fala meu nobre")



# A dicionado a herança na class 


class Aluno(Pessoa):
    def __init__(self, nome, data_nacimento, sexo,matricula):
        super().__init__(nome, data_nacimento, sexo)
        self.matricula = matricula