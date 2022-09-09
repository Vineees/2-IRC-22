#1ª) Faça um programa que peça 10 notas, entre zero e dez. Mostre uma mensagem caso cada valor seja inválido.

nota = 0
soma1 = 0
for i in range(10):
    sol = float(input('Insira a sua nota:'))
    if sol > 10 or sol < 0:
        print ('Valor Invalido:')
    else:
       soma1 = sol + soma1
print (f'Soma:{soma1}')

