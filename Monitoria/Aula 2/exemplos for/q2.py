#2) Programe um script que peca 3 números e verifique qual deles é o
# maior e imprima

maior = 0

for x in range(3):
    num = float(input('Insira seu Numero:'))

    if num > maior:
        maior = num
        print ('Numero Substituido')
print ('Maior:', maior)

