from enfermeiro import Enfermeiro
from medico import Medico

cadastro = []


while True:
    tipo = input("Digite qual seu cargo M = Medico(a), E = Enfermeiro(a) ou S para sair: ")

    if tipo.upper() == "S":
        break


    matricula = input("Digite a matricula do funcionario: ")
    nome = input("Digite o nome do funcionario: ")
    telefone = input("Digite o telefone do funcionario: ")
    email = input("Digite  o email do funcionario: ")
    cpf = input("Digite o CPF do funcionario: ")
    rg = input("Digite O RG do funcionario: ")

    if tipo.upper() == "M":
        crm = input("Digite o crm do funcionario: ")
        especialidade = input("Digite a especialidade do funcionario")
        horario = input("Digite o horario do funcionario")
        funcionario = Medico(matricula, nome, telefone, email, cpf, rg, crm, especialidade, horario)
    elif tipo.upper() == "E":
        coren = input("Digite o coren do funcionario: ")
        funcionario = Enfermeiro(matricula, nome, telefone, email, cpf, rg, coren)
    else:
        print("Tipo invalido. porfavor, digite M para Medico(a), E para Enfermeiro(a) ou S para sair.")
    
    cadastro.append(funcionario)

print("lista de funcionario:")

for funcionario in cadastro:
    if(funcionario.cargo == "Medico"):
        print(funcionario.nome, '-', funcionario.cargo, '-', funcionario.crm)
    
    if(funcionario.cargo == "Enfermeiro"):
        print(funcionario.nome, '-', funcionario.cargo, '-', funcionario.coren)


while True:
    resp = input("Deseja Visualizar o Horario dos Medicos? Digite S para sim ou N para não: ")

    if resp.upper() == "S":
        for funcionario in cadastro:
            if funcionario.cargo =='Medico':
                funcionario.informacao()
        break
    else:
        break