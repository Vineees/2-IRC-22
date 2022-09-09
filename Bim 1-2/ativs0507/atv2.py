#Faça um programa que leia 5 números e informe a soma e a média dos números.

num = 0
soma1 = 0
medi = 0


for i in range(5):
    sol = float(input('Insira um numero:'))
    soma1 = sol + soma1

print (f'Soma:{soma1}')
print (f'Media:{soma1 / 5}')
