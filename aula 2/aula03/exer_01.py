lista1 = []
lista1.append(1)

print(lista1)



lista1.append(2)
lista1.append(3)

print("Indice 0:" + str(lista1[0]))
print("Indice 1:" + str(lista1[1]))
print("Indice 2:" + str(lista1[2]))
print(lista1)




lista1 =[9,8,7,6,5,4,3,2,1]

print("(O comando Sorted ordena a listapara impreção)")
print(sorted(lista1))
print(lista1)



lista1 = [1,2,3,4,5,6,7,8,9]

print("(O comando soted ordena a lis para impreção em ordem decresente)")
print(sorted(lista1, reverse=True))



print("(Utilizando dicionario de dados em lista)")
pessoas =[
    {"nome":"joão","idade":25},
    {"nome":"Maria","idade":30},
    {"nome":"Pedro","idade":28},
    {"nome":"Ana","idade":22} 
]

#Acessando os elementos da lisata

for pessoa in pessoas:
    nome = pessoa['nome']
    idade = pessoa["idade"]
    print(f"Nome: {nome}, Idade: {idade}")



print("(outro exemplos )")
def caulcular_media_aluno(alunos):
    soma_notas = 0
    qtd_alunos = len(alunos)

    for aluno in alunos:
        nome = aluno["nome"]
        nota = aluno["nota"]
        soma_notas += nota
        print(f"Nome: {nome}, Nota: {nota}")
    
    media =soma_notas / qtd_alunos
    return media         #fim da função


alunos =[
    {"nome": "Alice", "nota": 8},
    {"nome": "Bob", "nota": 7},
    {"nome": "Carol", "nota": 9},
    {"nome": "David", "nota": 6}
]

#Chamando a  função para calcular a media das notas
media_notas = caulcular_media_aluno(alunos)
print(f"Media da turma: {media_notas}")




print("outra vertente do î ------------------------------------------")
alunos = []

qtd_alunos = int(input("Digite a quantidade de alunos: "))

for _ in range(qtd_alunos):
    nome = input("Digite seu nome: ")
    nota = float(input(f"Digite anota de {nome}: "))
    alunos.append({"nome": nome, "nota": nota})


media_notas = caulcular_media_aluno(alunos)
print(f"Media da turma : {media_notas:.2f}")