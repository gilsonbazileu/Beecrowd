def area_quadrilatero(base,altura):
    return base * altura

A,B,C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)


triangulo_retangulo = A * C / 2
area_circulo = C**2 * 3.14159
area_trapezio = (A + B)* C /2
area_quadrado = area_quadrilatero(B,B)
# area_quadrado = B*B
area_retangulo = area_quadrilatero(A,B)

# triangulo_retangulo = float(A) * float(C) / 2
# area_circulo = float(C)**2 * 3.14159
# area_trapezio = (float(A) + float(B))* float(C) /2
# area_quadrado = float(B)*float(B)
# area_retangulo = float(B)*float(A)

print(f'TRIANGULO: {triangulo_retangulo:.3f}')
print(f'CIRCULO: {area_circulo:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')

