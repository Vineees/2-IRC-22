##2ª)  Faça um algoritmo para ler 10 números quaisquer 
#e some 5 caso o numero informado seja par ou some 10 caso seja ímpar, imprimir o resultado desta operação.

resultado = 0
for n in range (10):
    num = float(input('Digite Seu Numero'))

    if num % 2 == 0:
        resultado = num + 5
    else:
        resultado = num + 10
    
    print (f'Resultado:{resultado}')
