#2) Para doar sangue é necessário ter entre 18 e 67 anos. Faça um aplicativo que pergunte a idade de uma pessoa e diga se ela pode doar sangue ou não.
print ('Cadastro Nacional de Doação de Sangue\n Insira Suas Informações')


idade = int(input('Sua Idade:'))

print ('\nIdade Informada:',idade)
if idade > 18:
    if idade < 65:
        print ('Você Pode Doar!!')
    else:
        print ('Você Não Pode Doar!!')
else:
    print ('Você Não pode Doar!!')

