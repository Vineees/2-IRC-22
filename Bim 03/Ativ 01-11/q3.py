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