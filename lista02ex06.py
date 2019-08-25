num1= int(input("Digite um número inteiro: "))
num2= int(input("Digite outro número inteiro: "))
num3= int(input("Digite mais um número inteiro: "))
if num1 >= num2 >= num3:
    print("Os números em ordem decrescente ficam:", num1, num2, num3)
elif num2 >= num1 >= num3:
    print("Os números em ordem decrescente ficam:", num2,num1, num3)
else:
    print("Os números em ordem decrescente ficam:", num3, num2, num1)