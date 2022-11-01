#3 - Desenvolva um algoritmo em python que leia um conjunto de dados
# contendo a altura e o sexo (M ou F) de 50 pessoas
# e que determine a maior e a menor altura do grupo,
# a média das alturas das mulheres
# e o número de homens com altura inferior a 1.73m. Imprima os resultados.


#Entrada:
#Altura - Float x
#Sexo - str x

#Saida:
#Maior e Menor Altura x
#Media das Altura Mulheres x
#Num dos Homens com Altura  inferior a 1.73m x

altura = 0
sexo = 0
media_altmulher = 0
homens_alturamenor = 0
maior = 0
menor = 0
mulher = 0

for x in range(50):
    altura = float(input('Insira sua altura:'))
    sexo = str(input('Insira seu sexo'))

    if sexo == 'F':
        mulher = mulher + 1
        media_altmulher = media_altmulher + altura
    elif sexo == 'M' or sexo == 'm':
        if altura <= 1.73:
            homens_alturamenor = homens_alturamenor + 1

    if altura > maior:
        maior = altura

    if altura < menor:
        menor = altura

print ('Maior Altura:', maior)
print ('Menor Altura:',menor)
print ('Media Alt Mulheres:',media_altmulher)
print ('Homens com Altura  inferior a 1.73m:',homens_alturamenor)
