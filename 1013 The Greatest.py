def compare(a,b):
    a = int(a)
    b = int(b)
    
    return (a+b+abs(a-b))/2

a,b,c = input().split()

maior = compare(a,b)

maior_final = compare(maior,c)

print(f'{int(maior_final)} eh o maior')

