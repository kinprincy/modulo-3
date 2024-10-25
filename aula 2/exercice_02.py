nivel_do_professor = int(input("Digite seu nivel (1 / 2); "))
oras_tb = float(input("Digite o valor de oras trabalhadas nese mes: "))

def jaja(oras_tb):
    if nivel_do_professor == 1:
        salbase = 56 * oras_tb
    elif nivel_do_professor == 2:
        salbase = 66 * oras_tb
    else:
        print("Nivel inezistente")
        return 0

    drs =  salbase * 0.15
    salario = salbase + drs 
    return  salario 

    
print(f"O salario do professor e: R$ {jaja(oras_tb)}")