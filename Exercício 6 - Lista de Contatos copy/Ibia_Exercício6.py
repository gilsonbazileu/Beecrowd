
from Exercício6_funcoes import adicionar_contato
from Exercício6_funcoes import remover_contato_por_nome
from Exercício6_funcoes import lista_todos_contatos
from Exercício6_funcoes import busca_contato_por_nome
from Exercício6_funcoes import alterar_contato_por_nome

contatos = []

# Loop principal para interação com o usuário
while True:
    print("\n #################### Escolha um numero correspodente a opções:#################\n")
    print("(1) Adicionar Contato")
    print("(2) Buscar Contato")
    print("(3) Remover Contato")
    print("(4) Alterar Contatos")
    print("(5) Listar todos Contatos")
    print("(6) Sair")

    opcao = input("Escolha uma opção:\n")

################# Adicionar contato #####################

    if opcao == "1":
        nome = input("Nome do contato: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        adicionar_contato(contatos, nome, telefone, email)

################# Buscar contato #####################

    elif opcao == "2":
        nome = input("Digite nome do contato a buscar:")
        busca_contato_por_nome(contatos,nome)


################# Remover contato #####################

    elif opcao == "3":
        nome = input("Nome do contato a ser removido: ")
        remover_contato_por_nome(contatos, nome)

################# Alterar contato #####################

    elif opcao == "4":
        nome = input("Nome do contato a ser alterado: ")
        novo_nome = input("Novo nome: ")
        novo_telefone = input("Novo telefone: ")
        novo_email = input("Novo email: ")
        alterar_contato_por_nome(contatos, nome, novo_nome, novo_telefone, novo_email)

################# Listar todos contatos #####################

    elif opcao == "5":
        print("\nLista de contatos:")
        lista_todos_contatos(contatos)

################# Encerrar #####################

    elif opcao == "6":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")