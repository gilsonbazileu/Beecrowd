# Monte um cardápio de restaurante usando um Dicionário.
# O dicionário deve ficar fixo no código.
# Receba do usuário a conta, com o código de cada produto e a quantidade.
# Quando o usuário digitar 'fim' significa que encerrou a conta.
# Ao final exiba a conta com uma linha para cada item com o nome do item,
# quantidade, valor unitário, valor total do produto.
# Por fim Exiba o total da conta.


# Criei uma lista com os dinossauros
cardapio =[
    {
        "cod_cardapio":1,
        "item_cardapio": "Feijoada",
        "preço":20,
    },

    {
        "cod_cardapio":2,
        "item_cardapio": "Arroz",
        "preço":5,
    },

    {
        "cod_cardapio":3,
        "item_cardapio": "Mão de vaca",
        "preço":24,
    },

    {
        "cod_cardapio":4,
        "item_cardapio": "Bode",
        "preço":22,
    },

    {
        "cod_cardapio":5,
        "item_cardapio": "Guizado",
        "preço":26,
    },

    {
        "cod_cardapio":6,
        "item_cardapio": "Cerveja",
        "preço":9,
    },

    {
        "cod_cardapio":7,
        "item_cardapio": "Suco limão",
        "preço":5,
    },

    {
        "cod_cardapio":8,
        "item_cardapio": "Suco laranja",
        "preço":7,
    },

    {
        "cod_cardapio":9,
        "item_cardapio": "Vinho",
        "preço":28,
    }
]

# # Receba do usuário a conta, com o código de cada produto e a quantidade.

# Lista que vai armazenar os dados codigo e quantidade de itens consumidos
lista_conta = []


while True:

    
    print("\n Quando terminar digite FIM \n")
    cod_item = input("Digite o codigo do item da sua conta:\n")
    
    # Condição de parada do looping
    if cod_item == 'fim':
        break

    cod_item = int(cod_item)

    # Condição para assegurar a escolha adequada dos codigos do cardápio
    if cod_item <=0 or cod_item >=10:
        print("Voce digitou número fora da lista de códigos")
        cod_item = input("Digite o codigo do item entre 1 e 9:\n")
        cod_item = int(cod_item)
    qtd_item = int(input("Digite a quantidade deste item:\n"))
    

    # Dicionario sendo alimentado pelos inputs do usuário do código a cima.
    dic_conta = {
        "Cod_dic_conta": cod_item,
        "qtd_iten_dic_conta" :qtd_item
    }
    # Adicionando o dicionario criando anteriormente a lista_conta = []
    lista_conta.append(dic_conta)


# Defini a variável e iniciei ela em zero 
# pra ser usada dentro do segundo for como um acumulador dos valores
subtotal = 0

# Percorrendo e comparando os codigos do cardápio e da conta do cliente.
# E imprime os itens consumidos 
for codigo_conta in lista_conta:
    for codigo_cardapio in cardapio:
        if codigo_conta["Cod_dic_conta"] == codigo_cardapio["cod_cardapio"]:

            print(f'{codigo_conta["qtd_iten_dic_conta"]} {codigo_cardapio["item_cardapio"]}\nCodigo do item: {codigo_cardapio["cod_cardapio"]} | Valor Unitário: R$ {codigo_cardapio["preço"]}\n')
        
            subtotal = subtotal + codigo_conta["qtd_iten_dic_conta"] * codigo_cardapio["preço"]

        
print(f'TOTAL A PAGAR: R$ {subtotal}')