#1ª) A prefeitura de uma cidade fez uma pesquisa com 200 pessoas, coletando dados sobre o salário e o número de filhos. A prefeitura deseja saber: 
#a) A média do salário dessas pessoas; 
#b)  A média do número de filhos; 
#c)  A quantidade de pessoas com salários igual ou superior a R$ 1.200,00. (2,0 pontos)


med_sal = 0
med_fl = 0
sal_sup = 0

for s in range(200):
    salario = float(input('Digite Seu Salario:'))
    filho = int(input('Digite o Numero de filhos:'))

    med_sal = med_sal + salario
    med_fl = med_fl + filho
    
    if salario >= 1.200:
        sal_sup = sal_sup + 1

print (f'\n Media de salário:{med_sal/200} \n Media de Filhos:{med_fl/200} \n Quantidade de Pessoas com Salario Maior que 1.200:{sal_sup/200}' )






