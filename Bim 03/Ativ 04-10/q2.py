entr = 0
maior = 0

while entr != -1:
    entr = int(input('Digite Seu Numero:'))
    if entr > maior:
        maior = entr

print (f'Maior Numero:{maior}')