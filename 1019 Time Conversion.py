valor_Tsec = int(input())
# Conversão para Minutos
valor_min = int(valor_Tsec / 60) #9min
valor_seg = valor_Tsec % 60 #16seg

#Conversão para Hora
valor_hora = int(valor_min /60) # 0, por o resultado deu uma fração!!
valor_min = valor_min % 60

print(f"{valor_hora}:{valor_min}:{valor_seg}") 


 