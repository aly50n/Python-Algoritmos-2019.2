num= int(input("Digite um número inteiro para saber os números primos entre 1 e ele: "))
for i in range (2, num+1 , 1):
    cont=0
    for n in range(2, num+1 , 1):
        if i % n == 0:
            cont= cont + 1
    if cont < 2:
        print (i, end= " ")