num = 1
qpar = 0
qimpar = 0

while num != 0:
    num = int(input('Digite Seu Numero:'))
    if num % 2 == 0:
        qpar = qpar + 1
    else:
        qimpar = qimpar + 1

print(f'Impares:{qimpar}\nPares{qpar}')