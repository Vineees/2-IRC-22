#ª) O restaurante a quilo ComaBem cobra R$26,00 por cada quilo de refeição. 
#Escreva um algoritmo que leia o peso da refeição do prato montado de 10 (dez) clientes (em quilos) e imprima o valor a pagar.


quilo = 0
resul = 0
for q in range(10):
    quilo = float(input('Peso Da Sua Comida:'))
    resul = quilo + resul

print (f'\n Total a Pagar: R${resul * 26}')

    