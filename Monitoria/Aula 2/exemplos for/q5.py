#Uma loja utiliza o código V para compras à vista e o código P para compras a prazo.
# Faça um programa em Python que receba o código da compra e o valor de 15 transações.
# Calcule e mostre:
# a) O valor total das compras à vista
# b) O valor total das compras a prazo;
# c) O valor total das compras efetuadas

#Entrada - P ou V
#Entrada - Valor das Compras

#Saida - Total Compras a Vista
#SAida - Total Compras a Prazo
#Saida - Valor Total

totalv = 0
totalp = 0

for c in range (2):
    veri = int(input('Utilize 1 ou 2 para comprar:'))

    if veri == 1:
        v = float(input('Valor da Sua compra:'))
        totalv = totalv + v
    else:
        p = float(input('Valor da Sua Compra:'))
        totalp = totalp + p

print ('Total Vista:',totalv)
print ('Total Prazo',p)
print ('Total Tudo:',totalv + totalp)
