#ª) Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
#O resultado do atleta será determinado pela média dos cinco valores. 
#Faça um programa que receba o nome e as cinco distâncias alcançadas por um atleta em seus saltos e depois informe o nome, 
#os saltos e a média dos saltos. A saída do programa deve ser conforme o exemplo abaixo:  (2,0 pontos)




nome = str(input('Informe Seu Nome:'))
salto1 = float(input('Valor do Primeiro Salto: '))
salto2 = float(input('Valor do segundo Salto: '))
salto3 = float(input('Valor do Terceiro Salto: '))
salto4 = float(input('Valor do Quarto Salto: '))
salto5 = float(input('Valor do Quinto Salto: '))


print(f'\nAtleta: {nome}')
print(f'Primeiro Salto:{salto1}m \nSegundo Salto{salto2}m \nTerceiro Salto:{salto3}m \nQuarto Salto:{salto4}m \nQuinto Salto:{salto5}m')
print(f'\nResultado Final: \n Atleta:{nome} \n Saltos: {salto1} - {salto2} - {salto3} - {salto4} - {salto5}')
print(f' Media de Saltos:{(salto1 + salto2 + salto3 + salto4 + salto5)/5}m')
