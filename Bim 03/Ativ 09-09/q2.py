#Desenvolver um algoritmo em python que leia 15 números e calcule e escreva a média aritmética dos valores lidos, 
# a quantidade de valores positivos, 
# a quantidade de valores negativos. 
# Imprima os resultados.
positivos = 0
negativo = 0
mnum = 0
for n in range(15):
    num = float(input("Digite Um Numero:"))

    if num > 0:
        positivos = positivos + 1
    if num < 0:
        negativo = negativo + 1
    
    mnum = mnum + num


print ("Media dos Numeros:",mnum/15)
print ("Quant Positivos:",positivos)
print ("Quant Negativos:",negativo)
