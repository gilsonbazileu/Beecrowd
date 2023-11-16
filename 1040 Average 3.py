n1,n2,n3,n4 = input().split()

n1  = float(n1)
n2  = float(n2)
n3  = float(n3)
n4  = float(n4)


# Media pondera: multiplica os peso pelas notas e divide pela soma dos pesos.
media_ponderada = ((n1*2)+ (n2*3) + (n3*4) + (n4*1)) / 10



if media_ponderada >= 7.0:    
    print(f'Media: {media_ponderada:.1f}\nAluno aprovado.')


elif media_ponderada < 5:
    print(f'Media: {media_ponderada:.1f}\nAluno Reprovado ')


if media_ponderada > 5.0 and media_ponderada < 6.9:
    print(f'Media: {media_ponderada}')
    print('Aluno em exame')
    exam = float(input("insert exam score:\n"))
    print(f"Nota do Exame: {exam}")
    media_final = media_ponderada + exam /2

    print(f'Media Final: {media_final:.1f}')


#elif media_final <= 4.9 :
    

    


