a,b,c = input().split()

a = float(a)
b = float(b)
c = float(c)


delta = (b**2)-(4*a*c)

if delta <0 or a ==0:
    print("Impossível calcular")
    
elif delta >0:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print(f'R1 = {x1:.5f} \n R2 = {x2:.5f}')












