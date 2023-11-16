codigo,qtd = input().split() #Cod 1  e Qtd 5

lista = ['Feijoada - R$ 23', 'Bife a parmegiana - R$ 27','Filé de tilapia - R$ 30', 'Lasagna - R$ 25', 'Filé com fritas - R$ 20' ]
listaValor = [23,27,30,25,20]

index = int(codigo) -1

calc = int(qtd) * listaValor[index]

print(f'{qtd}x {lista[index]} = R$ {calc}')

#print(f'{lista[index]} {listaValor[index]}')









