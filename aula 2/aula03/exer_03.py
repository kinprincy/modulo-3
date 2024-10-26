#dadas 

produtos =[
    {"produto": "tv 50 polegadas", "marca": "Sansung"},
    {"produto": "micro-ondas 10 litros", "marca": "Panasonic"},
    {"produto": "iphone 15 pro max", "marca": "Apple"},
    {"produto": "smartphone redmi note 13", "marca": "Xiaomi"},
    {"produto": "lavadora", "marca": "Brastemp"}
]



def imprimir(produtos):
    for produto in produtos:
        print(f"Produto: {produto['produto']}, Marca: {produto['marca']}")

imprimir(produtos)

