elei = int(input('Numero de Eleitores:'))
cand1 = 0
cand2 = 0
cand3 = 0

for x in range(elei):
    voto = str (input('Digite Seu Voto \n Escolha entre A - B - C:'))

    if voto == 'A' or voto == 'a':
        cand1 = cand1 + 1
    elif voto == 'B' or voto == 'b':
        cand2 = cand2 + 1
    elif voto == 'C' or voto == 'c':
        cand3 = cand3 + 1
    else:
        print('Invalid Voto')

print (f'Resultado: \n Candidato A:{cand1} \n Candidato B:{cand2} \n Candidato C:{cand3}')
