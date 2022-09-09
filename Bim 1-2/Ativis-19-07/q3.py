#3ª) A prefeitura de uma cidade fez uma pesquisa com 200 pessoas, coletando dados sobre o salário e o número de filhos. A prefeitura deseja saber:
# a) A média do salário dessas pessoas;
# b)  A média do número de filhos;
# c)  A quantidade de pessoas com salários igual ou superior a R$ 1200,00.

salario = 0
numerosf = 0
sal2 = 0

for p in range (200):
    salario = int(input('Insira Seu Salario:'))
    numerosf = int(input('Insira Numero de Filhos:'))
    if salario > 1200:
        sal2 = sal2 + 1


print (f'Media de Salario:{salario / 200}')
print (f'Media De Numeros de Filhos:{numerosf / 200} ')
print (f'A quantidade de pessoas com salários igual ou superior a R$ 1200,00:{sal2}')

