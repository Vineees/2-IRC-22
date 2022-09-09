#Elabore um programa em Python que receba a idade de 10 entrevistados e informe quantos possuem idade maior que 18 anos.
entr = 0
rest = 0
for i in range(10):
    entr = int(input('Insira Sua Idade'))
    if entr > 18:
        rest = rest + 1

print (f'Pessoas Com +18:{rest}')
