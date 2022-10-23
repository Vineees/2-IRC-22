#1) Crie um programa em que o usuário insira 5 números inteiros positivos e
# imprima a média
media = 0
for x in range(5):
    num = int(input('Insira seu Numero:'))
    media = media + num

print ('Media dos Numeros:', media /5)
