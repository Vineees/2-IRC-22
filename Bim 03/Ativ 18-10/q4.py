#4ª)  Faça um programa, que permita o usuário fazer três contas de subtração.

print ('OPERALÇAO - SUBTRAÇÂO \n=============================')

for x in range(1,4):
    print (f'Conta {x}! \n')
    num1 = int(input('Digite Seu Numero:'))
    num2 = int(input('Digite Seu Numero:'))

    print ( f'\n{num1} - {num2}: {num1 - num2}')
    print ('\n=============================')

