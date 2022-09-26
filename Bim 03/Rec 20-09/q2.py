media = 0
for n in range(4):
    nota = float(input("Sua Nota:"))
    media = media + nota

media = media /4

if media >= 7:
    print('Aprovado!!')
elif media >= 5 and media <= 7:
    print ("Rec!!")
elif media >=4 and media <= 5:
    print ('Conselho')
else:
    print ('Reprovado ')