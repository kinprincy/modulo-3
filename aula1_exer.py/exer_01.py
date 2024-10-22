#def menu_inicial():
#    print('Programa para Conversão de Temperaturas')
#    print('1. Para Converter de Celsius para Fahrenheit')
#    print('2. Para Converter de Fahrenheit para Celsius')
#
#def cel_fahr():
#    C = float(input('Entre com a temperatura em graus Celsius: '))
#    F = C * (9 / 5) + 32
#    print('Valor em Fahrenheit: {0}°F'.format(F))
#
#def fahr_cel():
#    F = float(input('Entre com a temperatura em graus Fahrenheit: '))
#    C = (F - 32) * (5 / 9)
#    print('Valor em Celsius: {0}°C'.format(C))
#
#if __name__=='__main__':
#    menu_inicial()
#    escolha = input('Escolha o tipo de conversão que deseja realizar: ')
#
#    if escolha == '1':
#        cel_fahr()
#
#    if escolha == '2':
#        fahr_cel()

print("Digite uma temperatura")
print("1. Celsius")
print("2. fahrenhait")
print("3. kelvin")
TEMPERATURA = float(input())

K=C+273
F=32+(9/5)*K
C=(K - 32) * (5 / 9)


match TEMPERATURA:
    case 1:
        print("em celsius")
    case 2:
        print("em fahrenhait")
    case 3:
        print("em kelvin")