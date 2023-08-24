code,amount = input().split() # se code 5

pricelist = [4.00,4.50,5.0,2.0,1.50]

index = int(code) -1  #4

price = pricelist[index] #  price vai ser 1.50 que está na posiçao 4

final_price = price * int(amount) #

print(f'Total: R$ {final_price:.2f}')
