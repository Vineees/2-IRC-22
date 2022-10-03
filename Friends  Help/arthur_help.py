soma_pares = 0
mult_impares = 1

for n in range (10):
    num = int(input('INsira seu numero:'))
    if num % 2 == 0:
        soma_pares = soma_pares + num
    else:
        mult_impares = mult_impares * num

print ('Soma dos PAres:',soma_pares)
print ('Prosuto dos Imprares',mult_impares)

