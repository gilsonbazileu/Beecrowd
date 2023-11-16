#Exercicio  2

#Peça para o usuário digitar 10 números
#Depois crie um novo array com o quadrado de cada número
#Depois imprima uma linha para cada item dos arrays no seguinte formato:
#x ao quadrado é igual a y
#sendo x o número digitado e y o quadrado desse número
#imprima mais uma com o total da soma do array dos valores ao quadrado:
#A soma do array de numeros elevados ao quadrado é: z

#Peça para o usuário digitar 10 números e adiciono o dado ao array
array1 = []
while len(array1)<10:
    valor = int(input("Insira o valor:\n"))
    array1.append(valor)


#Depois crie um novo array com o quadrado de cada número
array_quadrado = []
for item in array1:
    item_new_array = item*item
    array_quadrado.append(item_new_array)

#imprima uma linha para cada item dos arrays
index = 0
for item2 in array1:
    print(f'{array1[index]} ao quadrado é igual a: {array_quadrado[index]}')
    index = index +1

soma = 0
for item3 in array_quadrado:
    
    soma = soma + item3
    
print(f'Soma array {soma}')

    
    #print(f'Soma Array{soma_array}')




# FAZENDO A MESMA COISA QUE ESTÁ NO FOR MAS COM WHILE
# indice = 0
# while indice < len(array_quadrado): 
#     item = array_quadrado[indice]
#     item_new_array = item*item
#     new_array.append(item_new_array)
#     indice = indice +1

