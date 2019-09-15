num = int(input("Digite um número inteiro para ser invertido: "))
aux = num
aux2 = num
print (num, end= " => ")
while aux2 > 0:
    aux = aux % 10
    print(aux, end= "" )
    aux2= aux2/10
