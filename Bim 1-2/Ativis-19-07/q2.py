#Uma loja utiliza o código V para compras à vista e o código P para compras a prazo. Faça um programa em Python que receba o código da compra e o valor de 15 transações. Calcule e mostre:
# a) O valor total das compras à vista
# b);  O valor total das compras a prazo;
# c)  O valor total das compras efetuadas



v = 0
p = 0
totalv = 0
totalp = 0
veri = 0



for c in range(15):
    veri = int(input('Sua Compra Será a Praso ou a Vista? Use 1 ou 2.'))
    if veri == 2:
        v = int(input('Valor Da Sua Compra:'))
        totalv = v + totalv
    else:
        p = int(input('Valor Da Sua Commpra:'))
        totalp = p + totalp

print (f'Total Vista:{totalv}')
print (f'Total Praso:{totalp}')
print (f'Valor Total:{totalv + totalp}')
