num1 = int(input('\nDigite o Numero1:'))
num2 = int(input('\nDigite o Numero2:'))
num3 = int(input('\nDigite o Numero3:'))

if num1 > num2:
    if num1 > num3:
        print ('O Maior Numero é:',num1)
    else:
        print ('O Maior Numero é:',num3)
elif num2 > num3:
    print ('O Maior Numero é:',num2)
else:
    print ('O Maior Numero é:',num3)
