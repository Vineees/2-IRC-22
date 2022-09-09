#Elabore um programa em Python que o usuário forneça 10 números inteiros e positivos e imprima o produto dos números ímpares e a soma dos números pares.
restimpar = 1
restpar = 0

for n in range (10):
    numero = int(input('Insira o Numero:'))
    if numero % 2 != 0:
        restimpar = restimpar * numero
    else:
        restpar = restpar + numero


print (f'Produto Numeros Impares:{restimpar}')
print (f'Soma Numeros Pares:{restpar}')
