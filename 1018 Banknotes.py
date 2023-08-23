
ValorInserido = int(input())

notas = [100,50,20,10,5,2,1]
print(ValorInserido)
for valor_nota in notas:
    Q_notas = int(ValorInserido/valor_nota)
    
    print(f"{Q_notas} nota(s) de R$ {valor_nota},00")
    
    ValorInserido = ValorInserido - Q_notas * valor_nota  # calculo resto manual,
    #resto tbm pode ser calculado com o operador %
    
        
    #ValorInserido = ValorInserido % valor_nota
    
