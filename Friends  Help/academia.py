#Para resolver essa questão vamos separar em 2 topicos inicialmente, oque será dado de entrada e oque sairá

#Saidas 6:
# - Matricula + Cliente Mais Alto
# - Matricula + Cliente Mais Baixo
# - Matricula + Cliente Mais Gordo
# - Matricula + Cliente Mais Magro
# - Media das Alturas
# - Média dos Pesos

#Entradas 3 :
# - Matricula
# - Peso
# - Altura

#1) Definir as Variáveis de Base:

peso = 0
matricula = 1
altura = 0
clientes = 0

#2) Definir as Variáveis de Saida:

mr_alto = 0 # Maior Altura
mat_alto = 0 # Matricula

ms_baixo = 100
mat_baixo = 0 # Matricula

mr_gordo = 0
mat_gordo = 0 # Matricula

ms_magro = 100
mat_magro = 0 # Matricula

media_alt = 0
media_peso = 0 # Matricula

#3) Iniciando o Processo de Categorização:

while matricula != 0:

    #Iniciando com os Inputs
    matricula = int(input('Insira Sua Matricula:'))

    if matricula == 0: #Ordem de Parada Caso matricula = 0
        print ('Mais Alto:',mr_alto,"-",mat_alto)
        print ('Mais Baixo:',ms_baixo,"-", mat_baixo)
        print ('Mais Gordo:',mr_gordo,"-", mat_gordo)
        print ('Mais Magro:',ms_magro,"-",mat_magro)
        print ('Media de Peso', peso / clientes)
        print ('Media de Altura:',altura / clientes)
        exit() #Termina o Codigo
    peso_input = int(input('Insira Seu Peso:'))
    altura_input = float(input('Insira Sua Altura:'))

    #3.1) Definindo o Mais Gordo e o Mais Magro
    if peso_input > mr_gordo:
        mat_gordo = matricula
        mr_gordo = peso_input
    if peso_input < ms_magro:
        mat_magro = matricula
        mr_magro = peso_input

    #3.2) Definindo o Mais Alto e o mais Baixo
    if altura_input > mr_alto:
        mat_alto = matricula
        mr_alto = altura_input
    if altura_input < ms_baixo:
        mat_baixo = matricula
        ms_baixo = matricula

    #Para Calcular a Media no Futuro
    peso = peso + peso_input
    altura = altura + altura_input
    clientes = clientes + 1

    #Caso matricula != 0 Retorna Para o Inicio

