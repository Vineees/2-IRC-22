#Elabore um programa em Python que receba a idade de 10 entrevistados
#e informe quantos possuem idade maior que 18 anos e quantos são de menor.

qnt = 0
qnt1 = 0
for x in range (10):
    idade = int(input('Indorme Sua Idade:'))

    if idade >= 18:
        qnt = qnt + 1
    if idade < 18:
        qnt1 = qnt1 + 1


print ('Quantidade de pessoas com idade maior ou igual 18: ',qnt)
print ('Quantidade de pessoas com idade menor que 18:',qnt1)
