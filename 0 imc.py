Peso = float (input ("Insira Seu Peso"))
Altura = float (input ("Insira Sua Altura"))

IMC = Peso /  (Altura**2)

print (IMC)

if IMC <= 18.5:
    print ("Você está a baixo o peso" + str(IMC))

elif IMC >= 18.6 and IMC <25:
    print (" Voce está no peso IDEAL" + str(IMC))

elif IMC >= 25 and IMC <30:  
    print (" Levemente acima do Peso" + str(IMC))

elif IMC >= 30 and IMC <35:
    print (" Você está com Obesidade grau 1" + str(IMC))   