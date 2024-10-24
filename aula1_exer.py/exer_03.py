#faça um programa que leia o salrio de uma pessoa em um determinado mês. Calcule e
#mostre o seu salario liquido no referido mês, sabendo-se que não descontados 11% para o inposto de
#renda,8% para o inss e %% para o sindicato. A saida do programa deve escrever o seguinte texto:

salarioB = float(input("digite seu salario: "))
ir = 11
inss = 8
sindicato = 5

valor_ir = (ir/100) * salarioB
valor_inss = (inss/100) * salarioB
valor_sindicato = (sindicato/100) * salarioB

tolal_discont = valor_ir + valor_inss + valor_sindicato

total = salarioB - tolal_discont

print(f"O salario bruto é.  R${salarioB}")
print(f"Valor a sobrar do imposto de renda.  R${valor_ir}")
print(f"Valor a sobrar do inss.  R${valor_inss}")
print(f"Valor a sobrar do sindicato. R${valor_sindicato}")
print(f"total de desconto,  R${tolal_discont}")
print(f"O salario liquido é.  R${total}")



