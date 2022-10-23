#3) Numa eleição existem três candidatos. Faça um programa que peça o número total de
#eleitores de um município. Em seguida, solicite para cada eleitor votar e ao final mostrar
#o número de votos de cada candidato.

bruno = 0
levy = 0
leonel = 0

eleitores = int(input('Numero de Eleitores:'))

for x in range (eleitores):
    votar = int(input('Numero do Seu Candidato:'))

    if votar == 1:
        bruno = bruno + 1
    elif votar == 2:
        levy = levy + 1
    elif votar == 3:
        leonel = leonel + 1
    else:
        print ('ERRO')

print ('Resultado: Bruno:',bruno,'Levy',levy,'Leonel',leonel)
