nota = 0
aln = 0
for n in range (20):
    alni = str(input('Insira seu Nome:'))
    notai = int(input('Insira Sua Nota:'))
    if notai > nota:
        nota = notai
        aln = alni

print (f'Aluno:{aln}')
print (f'Maior Nota:{nota}')
