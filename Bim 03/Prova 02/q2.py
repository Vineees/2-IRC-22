#2ª) Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final: 
# a) Quantos homens foram cadastrados; 
# b) Quantas mulheres foram cadastradas; 
# c) A média de idade do grupo; 
# d) A média de idade dos homens; 
# e) Quantas mulheres tem mais de 20 anos.  (2,0 pontos)

cas_homens = 1
cas_mulher = 0
idade20 = 0

med_homen = 0
med_total = 0

for x in range (1):
    idade = int(input('Insira sea idade:'))
    sexo = int(input('Insira Seu Sexo - 1 Para Masculino - 2 Para Feminino:'))

    med_total = med_total + idade

    if sexo == 1:
        cas_homens = cas_homens + 1
        med_homen = med_homen + idade
    elif sexo == 2:
        cas_mulher = cas_mulher + 1

        if idade >= 20:
            idade20 = idade20 + 1
print (f'\n Homens Cadastrados: {cas_homens} \n Mulheres Cadastradas: {cas_mulher}')
print (f' Media dos Homens: {med_homen/cas_homens} \n MEdia Total: {med_total/5}')
print (f' Mulheres Com Mais de 20 Anos:{idade20}')