#5) Faça um programa que permita o usuário escolher entre três opções de bebidas (1 - Água (R$2,00), 2 - Refrigerante (R$3.50), 3 - Suco (R$ 2.50) e em seguida a quantidade desejada. O programa deve exibir na tela o total da compra da bebida escolhida.

print ('Prod: 1 - Água (R$2,00), 2 - Refrigerante (R$3.50), 3 - Suco (R$ 2.50)')
prods = int(input('Numero do Produto:'))


quant = 0
resto = 0

if (prods == 1):
    quant = int (input('Quantidade:'))
    resto = 2.00 * quant
    print ('Bebida Escolhida:',prods,'Quandtidade:',quant,'\nPreço: R$:',resto,)
if (prods == 2):
    quant = int (input('Quantidade:'))
    resto = 3.50 * quant
    print ('Bebida Escolhida:',prods,'Quandtidade:',quant,'\nPreço: R$:',resto,)
if (prods == 3):
    quant = int(input('Quantidade'))
    resto = 2.50 * quant
    print ('Bebida Escolhida:',prods,'Quandtidade:',quant,'\nPreço: R$:',resto,)
