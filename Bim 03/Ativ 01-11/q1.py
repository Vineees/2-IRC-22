nota = 0
nota = float(input('Insira Sua Nota:'))
while nota > 10 or nota < 0:
    print ('\nNota Invalida Digite Novamente!')
    nota = float(input('\nInsira Sua Nota:'))

print (f'Nota Inserida:{nota}')