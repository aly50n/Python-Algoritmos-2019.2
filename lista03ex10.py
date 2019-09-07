base= int(input("Digite uma Base: "))
expoente= int(input("Digite um expoente: "))
aux= base
for a in range (expoente-1):
    aux = base * aux
print (aux)