# ADICIONAR CONTATO
def adicionar_contato(lista_contatos,contact_name,phone_number):
    
    contato = {

                "nome":contact_name,
                "numero":phone_number
            }

    lista_contatos.append(contato)




# REMOVER CONTATO

def remover_contato(nome, lista_contatos):
    # Crie uma lista vazia para armazenar os índices dos contatos a serem removidos
    indices_para_remover = []

    # Percorra a lista de contatos
    for i, contato in enumerate(lista_contatos):
        if nome == contato["nome"]:
            indices_para_remover.append(i)

    # Remova os contatos da lista com base nos índices
    for i in reversed(indices_para_remover):
        lista_contatos.pop(i)


nome_a_remover = input("Digite um contato a remover: ")
remover_contato(nome_a_remover, contatos)

# Imprima a lista atualizada de contatos
print("Contatos atualizados:")
print(contatos)









# def remover_contato(name, contato,lista_contatos):
    
#     name = input("Digite um contato a remover\n")
#     for contato in lista_contatos:
#         if name == contato["nome"]:
#             lista_contatos.remove(contato)