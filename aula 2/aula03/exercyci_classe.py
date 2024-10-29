class Produto:
    def __init__(self,codproduto,nome,descriçao,tamanho,preço):
        self.codproduto = codproduto
        self.nome = nome
        self.descriçao = descriçao
        self.tamanho = tamanho
        self.preço = preço

    def desconto(self):
        desconto = self.preço * 0.10
        preço_desconto = self.preço - desconto
        print(f"O preço com desconto do Produto {self.nome} È R${preço_desconto:.2f}")


produto1 = Produto("0129", "Play 5","Eletronico", "1", 3513.90)
produto2 = Produto("0540", "Coeca Box","Roupa", "2", 54.99)
produto3 = Produto("2128", "Faca Tramontina","Item Domestico", "3", 219.52)


print("codproduto:", produto1.codproduto, ".nome:", produto1.nome,".descrição:", produto1.descriçao, ".tamanho:", produto1.tamanho, ".preço:", produto1.preço)

produto1.desconto()


print("codproduto:", produto2.codproduto, ".nome:", produto2.nome,".descrição:", produto1.descriçao, ".tamanho:", produto2.tamanho, ".preço:", produto2.preço)

produto2.desconto()


print("codproduto:", produto3.codproduto, ".nome:", produto3.nome,".descrição:", produto1.descriçao, ".tamanho:", produto3.tamanho, ".preço:", produto3.preço)

produto3.desconto()




