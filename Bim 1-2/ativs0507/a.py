cont = 0
num = int(input("Digite Um Numeo Qualquer:"))
num1 = int(input("Digite Um Numeo Qualquer:"))

if num1 > num:
    for i in range(num,num1):
       print (i)
       cont = cont + 1
else:
    for i in range(num1,num):
        print(i)
        cont = cont + i
print(f"A soma dos valores no intervalo:{cont}")
