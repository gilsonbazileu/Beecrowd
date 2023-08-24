code,amount = input().split()



pricelist = [4.00,4.50,5.0,2.0,1.50]

index = int(code) -1  #0

price = pricelist[index]

final_price = price * int(amount)

print(f'Valor a pagar {final_price}' )


