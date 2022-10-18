#3ª)  Escreva um programa em Python que receba a idade de 10 alunos. 
# Esse programa deve exibir a idade dos alunos, ler e imprimir o nome caso a idade seja igual ou superior a 18 anos.

for i in range(10):
    idade = int(input('Sua Idade:'))
    if idade > 18:
        nome = str(input('Seu Nome:'))
    print (f'Nome Informado:{nome} \n Idade Informada:{idade}')

        
