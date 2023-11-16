# Função para adicionar um contato à lista
def adicionar_contato(lista, nome, telefone, email):
    novo_contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }
    lista.append(novo_contato)


# # Função para Buscar contato

def busca_contato_por_nome(lista, nome):
    encontrado = False  #Inicializar encontrado como False é necessário para acompanhar se encontramos um contato com o nome que estamos procurando na lista. Antes de começar a procurar, assumimos que ainda não encontramos o contato.
    for contato in lista:
        if contato['nome'] == nome:
            print(f'Contato encontrado: Nome: {contato["nome"]}, Telefone: {contato["telefone"]}, Email: {contato["email"]}')
            encontrado = True
    if not encontrado:
        print(f'Contato {nome} não encontrado.')
    

# Função para remover um contato da lista por nome
def remover_contato_por_nome(lista, nome):
    for contato in lista:
        if contato['nome'] == nome:
            print(f'Contato {nome} removido com sucesso.')
            lista.remove(contato)
            return
    print(f'Contato {nome} não encontrado.')

# Função para exibir a lista de contatos
def lista_todos_contatos(lista):
    if not lista:
        print('A lista de contatos está vazia.')
    else:
        for contato in lista:
            print(f'Nome: {contato["nome"]}, Telefone: {contato["telefone"]}, Email: {contato["email"]}')


# Função para alterar um contato por nome
def alterar_contato_por_nome(lista, nome, novo_nome, novo_telefone, novo_email):
    for contato in lista:
        if contato['nome'] == nome:
            contato['nome'] = novo_nome
            contato['telefone'] = novo_telefone
            contato['email'] = novo_email
            print(f'Contato {nome} alterado com sucesso.')
            return
    print(f'Contato {nome} não encontrado.')
