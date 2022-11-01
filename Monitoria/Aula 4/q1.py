#Faça um programa que peça o salario e idade 20 funcionarios e imprima
#qual e o maior, o menor e divida todos os salarios por 2


#Entrada:
#Salario - float
#idade - int

#Saida:
#Maior Salario
#Menor Salario
#Divisão Salario

maior = 0
menor = 999999999999999999999999999999
idade = 0
salario = 0
divisão = 0

for x in range(2):
    salario = float(input('Insira Seu Salario:'))
    idade = int(input('Insira Sua IDade:'))

    if salario > maior:
        maior = salario

    if salario < menor:
        menor = salario

    divisão = divisão + salario / 2

print ('Maior Salario:',maior)
print ('Menor Salario:',menor)
print ('Divisão Salario:',divisão)

