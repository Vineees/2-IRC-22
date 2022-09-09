num1 = int(input('Diga o Numero:'))
num2 = int(input('Diga o Numero:'))
num3 = int(input('Diga o Numero:'))

primeiro = 0
segundo = 0
terceiro = 0

if (num1 > num2):
    primeiro = num1
    if (num2 > num3):
        segundo = num2
        terceiro = num3
    if (num2 < num3):
        segundo = num3
        terceiro = num2
if (num2 > num 3):
    primeiro = num2
    if (num3 > num1):
        segundo = num3
        terceiro = num1
    else:
        segundo = num1
        terceiro = num2
