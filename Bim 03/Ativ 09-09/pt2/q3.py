n1 = int(input('Digite um numero para ver a sua tabuada: '))
for n2 in range(1, 11):
    resultado = n1 * n2
    print('{} x {:2} = {}'.format(n1, n2, resultado))
