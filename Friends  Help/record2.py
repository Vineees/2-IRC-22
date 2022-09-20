#input - 4
#Saida - 1

calc = 0
for n in range (4):
    nota = float(input('Digite Sua Nota:'))
    calc = calc + nota

media = calc /4
print (media)
if media >= 7:
    print('Aprovado!!')
elif media >=5 and media <=7:
    print ('Recuperação!!')
elif media >= 4 and media <= 5:
    print ('Conselho!!!')
else:
    print ('Reprovado')
