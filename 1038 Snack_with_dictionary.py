code,amount = input().split() # se code 5

productlist = [
    {
        "code": 1,
        "specification" : "cachorro quente",
        "price": 4.00
    },
    {
        "code": 2,
        "specification" : "X-salada",
        "price": 4.50
    },
    {
        "code": 3,
        "specification" : "X-bacon",
        "price": 5.00
    },
    {
        "code": 4,
        "specification" : "Torrada Simples",
        "price": 2.00
    },
    {
        "code": 5,
        "specification" : "Refrigerante",
        "price": 1.50
    }

]

index = int(code) -1  

product = productlist[index] 

final_price = product["price"] * int(amount) #

print(f'Total: R$ {final_price:.2f}')
