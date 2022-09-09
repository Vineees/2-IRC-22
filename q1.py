#1ª) Desenvolva um algoritmo em python que leia um conjunto de dados contendo a altura e o sexo (M ou F) de 50 pessoas 
# e que determine a maior e a menor altura do grupo, 
# a média das alturas das mulheres e o 
# número de homens com altura inferior a 1.73m. Imprima os resultados.


# Variaveis
quant_mulher = 0 
altmas = 0 #Menor que 1.73

altmaior = 0
altmenor = 2

medalt = 0

for i in range(50):
    alt = float(input("Qual Sua Altura?:"))
    sexo = str(input("Qual Seu Sexo?(M/F):"))

    if sexo == 'F' or sexo == 'f':
        quant_mulher = quant_mulher + 1
        medalt = medalt + quant_mulher
    
    if sexo == "M" or sexo == "m" and alt < 1.73:
        altmas = altmas + 1
    
    if alt > altmaior:
        altmaior = alt 
    if alt < altmenor:
        altmenor = alt


print ("Med Altura Mulher:",medalt/quant_mulher)
print ("Maior Altura:",altmaior)
print ("Menor Altura:",altmenor)
print ("Menor Que 1.73:",altmas)

