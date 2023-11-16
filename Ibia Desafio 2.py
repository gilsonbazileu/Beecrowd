lista_fruta = []

while len(lista_fruta) <3:
    fruta = input("Digite o nome de uma fruta\n\n")
    lista_fruta.append(fruta)

index = 0

for item in lista_fruta:
    
    print(f'{index} {item}')

    index = index +1
    

