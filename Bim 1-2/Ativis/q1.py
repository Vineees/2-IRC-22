num1 = int(input('\nDigite o um Numero:'))
num2 = int(input('\nDigite outro Numero:'))

calc = num1 + num2

if (calc % 2 ) == 0:
    print ('\nSeu Resultado é par\n Resultado:',calc)
else:
    print ('\nNumero Impar\n Resultado',calc)
