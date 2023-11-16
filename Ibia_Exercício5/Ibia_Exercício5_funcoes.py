def compara_lista(lista_conta,cardapio):
    for codigo_conta in lista_conta:
        for codigo_cardapio in cardapio:
            if codigo_conta["Cod_dic_conta"] == codigo_cardapio["cod_cardapio"]:
                print(f'{codigo_cardapio["item_cardapio"]}\nCodigo do item: {codigo_cardapio["cod_cardapio"]} | Valor Unitário: R$ {codigo_cardapio["preço"]}\n')
             
            