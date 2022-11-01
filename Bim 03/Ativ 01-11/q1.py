#1ª)  Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = 0
nota = float(input('Insira Sua Nota:'))
while nota > 10 or nota < 0:
    print ('\nNota Invalida Digite Novamente!')
    nota = float(input('\nInsira Sua Nota:'))

print (f'Nota Inserida:{nota}')
