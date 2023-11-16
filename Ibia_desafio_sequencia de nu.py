# Receba do usuário uma sequencia de números.
# Cada entrada precisa ser um número e a leitura 
# dos números deve ser interrompida quando o usuário digitar 'fim'.
# Exemplo de entrada:
# 1001
# 102
# 103
# 2000
# 1
# 99
# 100
# 30
# fim

# Após o fim da entrada imprima os números acima de 100 da seguinte forma:
# Esses são os números acima de 100:
# 1001, 102, 103, 2000

# Por fim imprima os números até 100:
# Esses são os números acima de 100:
# 1, 99, 100, 30

# AS LISTAS NECESSARIAS
lista_num = []
lista_maior100 = []
lista_menor100 = []


# CAPTURANDO DADOS DO USUARIO E O INSERINDO NA LISTA NUM
while True:
    numero = input("Insira o valor\n")
    if numero == 'fim':
        break
    numero = int(numero)
    lista_num.append(numero)


# FILTRANDO OS ITENS DA LISTA NUM QUE SAO MAIOR QUE 100
index = 0 
for item1 in lista_num:
    if item1 >100:
        itemMaior100 = item1
        lista_maior100.append(itemMaior100)


# FILTRANDO OS ITENS DA LISTA NUM QUE SAO MENOR QUE 100
index = 0 
for item2 in lista_num:
    if item2 <100:
        item_menor100 = item2
        lista_menor100.append(item_menor100)


index = 0
#chat gpt me ajudou nessa parte
print("Esses são os números acima de 100:")
if lista_maior100:
    for i, item in enumerate(lista_maior100):
        if i == len(lista_maior100) - 1:
            print(item, end='\n')
        else:
            print(item, end=', ')

## o que eu consegui chega!
# for item3 in lista_maior100:
    
#     print(item3, end=',')
#     index = index +1

print("\n")
#chat gpt me ajudou nessa parte
print("Esses são os números até 100:")
if lista_menor100:
    for i, item in enumerate(lista_menor100):
        if i == len(lista_menor100) - 1:
            print(item, end='\n')
        else:
            print(item, end=', ')
    





#     print(item4,end=',')
#     index = index +1
# print("\n")