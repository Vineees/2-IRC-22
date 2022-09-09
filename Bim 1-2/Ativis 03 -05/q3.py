#3) Elabore um programa em Python que dado 6 números inteiros quaisquer, exiba a multiplicação dos pares e adição dos impares.
num1 = int(input('Primeiro Numero:'))
num2 = int(input('Segundo Numero:'))
num3 = int(input('Terceiro Numero:'))
num4 = int(input('Quarto Numero:'))
num5 = int(input('Quinto Numero:'))
num6 = int(input('Sexto Numero:'))

par = 0
impar = 1

if (num1 % 2) == 0:
    par = num1 + par
else:
    impar = num1 * impar


if (num2 % 2) == 0:
    par = num2 + par
else:
    imapar = num2 * impar


if (num3 % 2) == 0:
    par = num3 + par
else:
    impar = num3 * impar

if (num4 % 2) == 0:
    par = num4 + par
else:
    impar = num4 * impar

if (num5 % 2) == 0:
    par = num5 + par
else:
    impar = num5 * impar

if (num6 % 2) == 0:
    par = num6 + par
else:
    impar = num6 * impar



print ('\nPares:',par)
print ('Impares:',impar )
