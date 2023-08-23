A = float(input())
B = float(input())
C = float(input())

# Aqui é preciso calcular a média ponderada, já que cada valor tem pesos diferentes.
# Esse calculo é feito multiplicando cada valor por seu peso em seguida dividir pela soma os peso.
MEDIA = ((A*2) + (B*3)+(C*5)) / (2 + 3 + 5)

print("MEDIA = %.1f" % MEDIA)