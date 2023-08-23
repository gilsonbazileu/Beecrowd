A = float(input("Insira Valor de A: "))
B = float(input("Insira Valor de B: "))


# Aqui é preciso calcular a média ponderada, já que cada valor tem pesos diferentes.
# Esse calculo é feito multiplicando cada valor por seu peso em seguida dividir pela soma os peso.
MEDIA = ((A*3.5) + (B*7.5)) / (3.5 + 7.5)

print("MEDIA = %.5f" % MEDIA)



 