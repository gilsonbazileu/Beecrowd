code_product_1 = int(input())
number_of_units_produc_1 = int(input())
price_unit_produc_1 = float(input()) 

code_product_2 = int(input())
number_of_units_produc_2 = int(input())
price_unit_produc_2 = float(input())

VALOR_A_PAGAR_PRODUCT1 = number_of_units_produc_1 * price_unit_produc_1
VALOR_A_PAGAR_PRODUCT2 = number_of_units_produc_2 * price_unit_produc_2

VALOR_FINAL = VALOR_A_PAGAR_PRODUCT1 + VALOR_A_PAGAR_PRODUCT2

print(f'VALOR A PAGAR: R$ {VALOR_FINAL:.2f}')