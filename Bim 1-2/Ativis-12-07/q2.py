#Escrever um programa em Python que lê o nome e o valor de 25 produtos, em seguida, calcula e apresenta o valor total a ser pago por eles.
nomep = 0
valorp = 0

for p in range (25):
    nomepi = str(input('Nome do Produto:'))
    valorpi = int(input('Preço Produto:'))
    valorp = valorp + valorpi

print ('Valor Total:R$',valorp)
