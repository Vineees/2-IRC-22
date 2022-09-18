#3) Numa eleição existem três candidatos. Faça um programa que peça o número total de
#eleitores de um município. Em seguida, solicite para cada eleitor votar e ao final mostrar
#o número de votos de cada candidato.

#Input:
#Numero de Eleitores;
#Voto de Cada Eleitor;

#Saídas:
#Numero de Votos;

#Definição do Números de Eleitores;
num_eleitores = int(input('Numero de Eleitores: '))

#Definindo Variáveis;
cand_a = 0
cand_b = 0
cand_c = 0
total_v = 0

#Votação Acontece Aqui;
for x in range(num_eleitores):
    #Input Votos;
    voto = str(input('Eleição 2022. \n Utilize A - B - C Para Prosseguir com seu Voto: '))

    #Contador Votos;
    if voto == 'A' or voto == 'a':
        cand_a = cand_a + 1
    elif voto == 'B' or voto == 'b':
        cand_b = cand_b + 1
    elif voto == 'C' or voto == 'c':
        cand_c = cand_c + 1
    #Erro Caso User Erre o Candidato;
    else:
        print ('\n Erro No Voto!! \n Voto Anulado!! \n')
    total_v = total_v + 1

#Saida; 

print (f'Contagem de Votos: \n Candidato A: {cand_a} \n Candidato B: {cand_b} \n Candidato C: {cand_c} \n Total de Votos: {total_v}')

#By Vini - A Pedidos Da Fabi