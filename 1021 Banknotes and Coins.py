ValorInserido = float(input())

notas = [100,50,20,10,5,2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")

for valor_nota in notas:
    Q_notas = int(round(ValorInserido,2)/valor_nota) #5
    ValorInserido = ValorInserido - Q_notas * valor_nota
    print(f"{Q_notas} nota(s) de R$ {valor_nota:.2f}")
    
print("MOEDAS:")
for valor_moeda in moedas:
    Q_moedas = int(round(ValorInserido,2)/valor_moeda)
    ValorInserido = ValorInserido - Q_moedas * valor_moeda
    print(f'{Q_moedas} moeda(s) de R$ {valor_moeda:.2f}')  
    
    


    
    
    