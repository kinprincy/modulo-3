#feça um programa para caucular a quantidade de  latas de tintas parapintar uma parede. O progrma
#deverá solicitar ao usuario, a altura(float) e o comprimento(float) da parede. Conside que a cobertura
#da tinta é de 1litro para cada 3 metros quadrados e que a tinta é vendida em latas de 3,6litos,que
#custam R$ 107,00. informe ao usuario a quantidades de latas de tinta a serem compradas e o preço total.
import math

altura = float(input("Digite a atura: "))
comprimento = float(input("Digite o comprimento: "))

area = altura * comprimento

litros_necessarios = area / 3

latas_necessarias = math.ceil(litros_necessarios / 3.6)
preco_total = latas_necessarias * 107

print(f"\nQantidade de latas de tinta a derem compradas: {latas_necessarias}")
print(f"Preço total: R$ {preco_total:.2f}")