#ª) Desenvolver um algoritmo em Python que leia 10 números, calcule e escreva a média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores negativos.  (2,0 pontos)
negativos = 0
positivos = 0
med = 0

for x in range(10):
    num = float(input('Insira Um Numero:'))

    med = med + num 

    if num < 0:
        negativos = negativos + 1
    else:
        positivos = positivos + 1

print (f'\nMedia dos Numeros:{med/10} \nValores Positivos:{positivos} \nValores Negativos{negativos}')
    