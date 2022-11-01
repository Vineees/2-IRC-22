#1- Crie um programa que calcule a media de cinco numeros inteiros e positivos e calcule a media

media = 0

for x in range(5):
    num = int(input('Insira seu Numero:'))
    media = media + num
print ('Valor Da Media:',media)
