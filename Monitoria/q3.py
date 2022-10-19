n1 = float(input('INsira sua Nota:'))
n2 = float(input('INsira sua Nota:'))
n3 = float(input('INsira sua Nota:'))
n4 = float(input('INsira sua Nota:'))

media = ((n1 + n2 + n3 + n4)/4)

if media >= 7:
    print ('Aprovado!!')
elif media >= 5 and media <= 7:
    print ('Recuperação')
elif media >= 4 and media <=5:
    print ('Em Conselho')
else:
    print ('Reprovado')
