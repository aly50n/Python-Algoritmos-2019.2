quant = int(input("quantos elementos a lista vai ter? "))
lista = [[],[]]
valor = 0
cont1 = 0
cont2 = 0
for c in range(quant):
    valor = int(input("digite um numero: "))
    if valor % 2 == 0:
        lista[0] = valor
        cont1 = cont1 + 1
    else :
        lista[1] = valor
        cont2 = cont2 + 1
print(" total de pares: ", cont1)
print(" total de impares: ", cont2)