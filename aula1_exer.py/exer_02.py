numero1 = float(input("Digite um numero inteiro: " ))
numero2 = float(input("Digite outro numero inteiro: "))
real1 = (numero1*2) * (numero2/2)
real2 = (numero1 * 3) * (real1)
real3 = (real1**3)

print(f"O produto do dobro do primeiro com metade do segundo. {real1}")
print(f"A soma do triplo do primeiro com o terceiro. {real2}")
print(f"O terceiro elevado ao cubo. {real3}")