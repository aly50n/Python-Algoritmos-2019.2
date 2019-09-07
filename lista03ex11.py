impar = 0
par = 0
print("Vou te pedir 10 números inteiros para dizer quantos são pares e quantos são impares.")
cont= 0
for n in range (10):
    cont= cont+1
    contagem= print(cont, "º Número")
    num= int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
if par == 1:
    print("Tivemos",par, "Número par e", impar, "Números impares.")
elif impar == 1:
    print("Tivemos",par, "Números pares e", impar, "Número impar.")
elif par == 0:
    print("Não tivemos números pares mas tivemos", impar, "Números impares.")
elif impar == 0:
    print("Tivemos",par, "Números pares mas não tivemos números impares.")
else:
    print("Tivemos",par, "Números pares e", impar, "Números impares.")