# Exercício 3

# Receba do usuário uma sequencia de números.
# Cada entrada precisa ser um número e a leitura dos números deve ser interrompida quando o usuário digitar 'fim'.
# Exemplo de entrada:
# 102
# 103
# 2000
# 1
# 99
# 100
# 30
# fim

# Imprima o maior número:
# O maior número é 2000

# Por fim imprima o menor número:
# O menor número é 1

list_num = []
while True:
    seq_num = input("Insira os numeros: \n")
    if seq_num == 'fim':
        break
    list_num.append(seq_num)

list_maior = []
list_menor = []

try:
        num = int(seq_num)
        list_num.append(num)
except ValueError:
        print()

if list_num:
    maior_numero = menor_numero = list_num[0]
    
    for num in list_num:
        if num > maior_numero:
            maior_numero = num
        if num < menor_numero:
            menor_numero = num
    
    print(f"O maior número é: {maior_numero}")
    print(f"O menor número é: {menor_numero}")
    
    
    