print("Vamos digitar 10 números de qualquer valor inteiro.")
a = int(input ("Digite um número: "))
b = int(input ("Digite mais um número: "))
cont = 0
while cont < 8:
    if a < b:
        a = b
        b = int(input ("Digite mais um número: "))
        cont = cont + 1
    if b < a:
        b = a
        a = int(input ("Digite mais um número: "))
        cont = cont + 1
if a < b:
    print("O maior número digitado foi:", b)
else:
    print("O maior número digitado foi:", a)