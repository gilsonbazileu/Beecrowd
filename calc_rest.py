
print("                             CALCULADORA de DIVISÂO\n\n")

Dividendo = float(input("Insira o dividendo\n"))
divisor = float(input("Insira o divisor\n"))


calc_divisao = Dividendo / divisor
calc_resto =  Dividendo % divisor

print(f"{Dividendo} dividido por {divisor} é igual a: {int(calc_divisao)}\n e resta: {int(calc_resto)}")