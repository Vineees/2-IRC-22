#crie um programa que receba 20 idades e imprima:
# - Total de Idade maior que 18
# - Media das idades
# - Maior Idade
# - Menor Idade



maior = 0
menor = 0
media = 0
totalmaior18 = 0


for x in range(20):
    idade = int(input('Digite Sua Idade:'))

    if idade > 18:
        totalmaior18 = totalmaior18 + 1

    media = media + idade

    if idade > maior:
        maior = idade
    if idade < menor or menor == 0:
        menor = idade

print ('Maio:',maior)
print ('MEnor:',menor)
print ('Media:',media)
print ('Total Maior 18:',totalmaior18)
