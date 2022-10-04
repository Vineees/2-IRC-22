qrep = 0
num = 1
som = 0
while num != 0:
    num = int(input('Seu Numero:'))
    qrep = qrep + 1
    som = som + num 


print (f'Media dos Nuemeros:{som / qrep} \nSoma dos Numeros {som}')