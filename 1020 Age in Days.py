idade = int(input()) # 30
ano = idade // 365  # 0
resto_ano = idade % 365 # 30

mes = resto_ano // 30 # 1
resto_mes = resto_ano % 30 # 0
dia = resto_mes # 0

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')

# print(f'{ano} ano(s)\n{mes} mês(es)\n{dia} dia(s)')


