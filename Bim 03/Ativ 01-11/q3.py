#3ª)   O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas. Para encerrar a leitura o usuário deve digitar 0 (zero).
temp = 0
maior = 0
menor = 0
media = 0

temp = float(input('Insira a Temperatuta:'))

while temp != 0:
    
    if temp > maior:
        maior = temp

    if temp < menor or menor == 0:
        menor = temp
    
    if temp != 0:
        media = media + temp/2

    temp = float(input('Insira a Temperatuta:'))

print (f'\nMaior Temperatura:{maior} \nMenor Temperatura:{menor} \nMedia das Temperaturas:{media}')
