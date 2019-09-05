print("Digitaremos 10 números de qualquer valor, vamos lá!")
num = int(input("Digite um número: "))
soma = num
cont = 1
while cont < 10:
    num = int(input("Digite outro número: "))
    soma = soma + num
    cont= cont + 1
media = soma / 10
print ("A soma dos números digitado é:", soma)
print ("A média dos números digitados é:", media)