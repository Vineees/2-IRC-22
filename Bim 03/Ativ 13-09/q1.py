stop = 0
maior = 0 

while stop == 0:
    num = int(input('Numero:'))
    if num > maior:
        maior = num
    print ('Deseja Continuar?')
    stop = int(input('Use -1 Para Parar:'))
print ('Maior Numero:', maior)