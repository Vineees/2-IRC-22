
var1 = 0
var2 = 0
var3 = 0
var4 = 0


num = float(input('Digite Um Numero:'))

while num != -1:

    if num >= 0 and num <=25:
        var1 = var1 + 1
        print ('.')
    elif num >= 26 and num <= 50:
        var2 = var2 + 1
        print ('..')
    elif num >= 51 and num <= 75:
        var3 = var3 + 1
    elif num >= 76 and num <= 100:
        var4 = var4 + 1

    num = float(input('Digite Um Numero:'))

print (f'Valores [0-25]: {var1} \nValores [26-50]: {var2} \nValores [51-75]: {var3} \nValores [76-100]: {var4}') 
