#4ª) Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
#a) Quantos homens foram cadastrados; -
#b) Quantas mulheres foram cadastradas; -
#c) A média de idade do grupo;
#d) A média de idade dos homens;
#e) Quantas mulheres tem mais de 20 anos.

sexo = 0
idade = 0
qmas = 0
medmas = 0
qmu = 0
sqmu = 0

for x in range(2):
    sexo = int(input('Responda 1-Homen 2-Mulheres:'))
    idade = idade + int(input('Insira Sua Idade:'))
    if sexo == 1:
        qmas = qmas + 1
        medmas = medmas + idade

    else:
        qmu = qmu + 1
        if idade > 20:
            sqmu = sqmu + 1


medmas = medmas / qmas
print ('Cadastro dos Homens:',qmas)
print ('Cadastro dos Mulhres:',qmu)
print (f'Media Idade Gerel:{idade / 5}')
print (f'Media Idade Homens:{medmas}')
print (f'Quantidade Mulheres Maior Que 20 Anos:{sqmu}')
