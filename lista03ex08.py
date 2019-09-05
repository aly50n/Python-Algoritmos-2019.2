num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
aux1 = 1
aux2 = 1
if num1 < num2:
    print(num1, end= " ")
    aux1= num1
    while aux1 < num2:
        aux1= aux1 + 1
        print(aux1, end= " ")

if num1 > num2:
    print(num1, end= " ")
    aux2= num1
    while num2 < aux2:
        aux2 = aux2 - 1
        print(aux2, end= " ")