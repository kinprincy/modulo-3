premio = float(input("Digite o valor total do premio: R$ "))

imposto = premio * 0.07

premio_descontado = premio - imposto

#Calcular a destribuição do premio
ganhador1 = premio_descontado * 0.46
ganhador2 = premio_descontado * 0.32
ganhador3 = premio_descontado - (ganhador1 + ganhador2)

print(f"\nValor total do premio: R$ {premio:.2f}")
print(f"Valor do premio apos desconto do imposto: R$ {premio_descontado:.2f}")
print(f"Primeiro ganhador recebera: R$ {ganhador1:.2f}")
print(f"Segundo ganhador recebera: R$ {ganhador2:.2f}")
print(f"Terceiro ganhador recebera: R$ {ganhador3:.2f}")