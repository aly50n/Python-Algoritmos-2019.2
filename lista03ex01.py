n = float(input("Informe uma nota de 0 a 10 -> "))
while n < 0 or n > 10:
    print("A nota digitada é invalida, vamos tentar novamente!")
    n = float(input("Informe uma nota de 0 a 10 -> "))
print ("A sua nota foi:", n)