class Produto:
    def __init__(self,codproduto,nome,descriçao,tamanho,preço):
        self.codproduto = codproduto
        self.nome = nome
        self.descricao = descricao
        self.tamanho = tamanho
        self.preço = preço

    def desconto(self):
        desconto = self.preço * 0.10
        preço_desconto = self.preço - desconto
        print(f"O preço com desconto do Produto {self.nome} È R${preço_desconto:.2f}")


produtos = []

while True:
    tipo = input("Para Casdastrar precione qualquer tecla ou Digite S para sair: ")

    if tipo.upper() == "S":
        break



    codproduto = input("Digite o codigo do produto: ")
    nome = input("Digite o nome: ")
    descricao = input("Digite a descrição: ")
    tamanho = input("Digite o tamanho: ")
    preço = input("Digite o preço: ")

    produto = Produto(codproduto, nome, descricao, tamanho, preço)

    produtos.append(produto)

print("Lista de Produtos")
for prod in produtos:
    print( prod.codproduto,"_", prod.nome, "-", prod.descricao, "-", prod.tamanho, "-", prod.preço)