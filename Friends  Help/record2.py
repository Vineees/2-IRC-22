#input - 4
#Saida - 1


nota1 = float(input('Insira Nota1:'))
nota2 = float(input('Insira Nota2:'))
nota3 = float(input('Insira Nota3:'))
nota4 = float(input('Insira Nota4:'))

media = ((nota1 + nota2 + nota3 + nota4)/4)

if media >= 7:
    print('Aprovado!!')
elif media >=5 and media <=7:
    print ('Recuperação!!')
elif media >= 4 and media <= 5:
    print ('Conselho!!!')
else:
    print ('Reprovado')
