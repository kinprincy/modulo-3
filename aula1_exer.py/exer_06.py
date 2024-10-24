paes = int(input("Digite a quantidade de pães fraceses vendidos: "))
broas = int(input("digite a quntidade de broas vendidas: "))
venda_total = (paes * 0.80) + (broas * 2.50)
fabricacao = venda_total * 0.43
restante = venda_total - fabricacao
poupança = restante * 0.15
converter_euros = restante *0.15
euros = converter_euros / 6.16

#Exibir os resultados
print(f"\nVenda total de pães e broas: R$ {venda_total:.2f}")
print(f"Custo de fabricação: R$ {fabricacao:.2f}")
print(f"Valor quardado na poupança: R$ {poupança:.2f}")
print(f"Quantidae de Euros que ira comprar: R$ {euros:.2f}")