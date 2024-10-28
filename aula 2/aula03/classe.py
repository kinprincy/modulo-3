#string ,date , void
class pessoa:
    def _init_(self,nome, data_nacimento, sexo):
        self.nome = nome
        self.data_nascimento = data_nacimento
        self.sexo =sexo

    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}")

    

pessoa1 = pessoa("José", "20/10/1995", "maculino")
pessoa2 = pessoa("Maria", "01/01/2001", "feminino")


print("nome:",pessoa1.nome,"data de nascimento:",pessoa1.data_nascimento, "sexo:",pessoa1.sexo)
print("nome:",pessoa2.nome,"data de nascimento:",pessoa2.data_nascimento, "sexo:",pessoa2.data_nascimento)