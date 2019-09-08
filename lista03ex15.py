num = int(input("Digite um número inteiro: "))
primo = True
for i in range(2, num, 1):
    if num % i == 0:
        primo = False
if primo:
    print ("O Número é primo!")
else:
    print ("O Número não é primo!")
