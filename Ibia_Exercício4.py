# Listas/Arrays - Exercício 4

# Receba um interiro N que vai ser a quantidade de números inteiros que o usuário irá digitar a seguir.
# Então receba cada um dos N Números linha a linha.
# Depois imprima um array com os números na ordem inversa das entradas do usuário.
# Ex:

# Entrada:
# 4 
# 10
# 1
# 5
# 11

# Saída
# [11, 5, 1, 10,4]

list_num = []


qtd_num = int(input("Quantos numeros vai inserir?\n"))

for item in range(qtd_num):
    valor_num = int(input("Insira o valor dos numeros: \n"))
    list_num.append(valor_num)


index1 = 0 
index2 = len(list_num) -1



for item in list_num:
    temp = list_num[index1] #10
    list_num[index1] = list_num[index2] #50
    list_num[index2] = temp #10
  
   

print(list_num)
    
