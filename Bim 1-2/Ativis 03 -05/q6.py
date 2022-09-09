# 6) Desenvolva um programa para o salão de Beleza "BarbeiroPrime". Receba como dados de entrada as informações do serviço realizado: 1 - Barba (10 reais); 2- Corte (25 reais); 3- Barba e Corte (35 reais); a forma de pagamento
# (1 - Cartão; 2- Pix; 3 - Dinheiro). O programa deve exibir:
#a) O valor a ser pago pelo cliente;
#b) Caso o pagamento seja em PIX, informar a chave pix = 7912345678;
#c) Caso o pagamento no cartão perguntar (1-Crédito ou 2 - Débito);
#d) Caso o pagamento seja em dinheiro informar o troco.

print ('Bem Vindo ao BarbeiroPrime')

serv = int(input('1 - Barba (10 reais); 2- Corte (25 reais); 3- Barba e Corte (35 reais)\n Insira o Número:'))

pag = 0
ctroco = 0
troco = 0

if serv == 1:
    print ('R$:10.0')
    print ('1 - Cartão; 2- Pix; 3 - Dinheiro')
    pag = input('Metodo Pagamento:')
    if pag == 1:
        pagcred = input('1-Crédito ou 2 - Débito')
        print ('Pagamento Feito')
    if pag == 2:
        print ('7912345678')
        print ('Pagamento Feito')
    if pag == 3:
        input('Vc Tem quando ai?:')
