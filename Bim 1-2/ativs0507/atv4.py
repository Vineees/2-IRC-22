#Faça um programa que, dado um conjunto de 10 números, determine o menor valor, o maior valor e a soma dos valores.
maior = 0
menor = 1


for x in range(10):
    val = int(input('Seu Numero:'))
    if val > maior:
        maior = val
    if val < menor:
        menor = val

print ('Menor',menor)
print ('Maior',maior)
