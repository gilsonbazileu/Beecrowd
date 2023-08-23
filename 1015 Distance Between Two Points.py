x1,y1 = input().split()
x2,y2 = input().split()

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

distancia = (x2-x1)**2 + (y2-y1)**2
result_final = distancia **0.5  # Usei o **0.5 por que elevar a potencia em 0.5 se obtem a raiz  

print(f'{result_final:.4f}')

