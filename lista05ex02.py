conjunto = [""]*10
quadrado = [""]*10
for i in range(10):
    conjunto[i] = int(input("Digite um número real: "))
for i in range(10):
    b = conjunto[i] ** 2
    quadrado[i] = b
print("Conjunto: ", conjunto, end="    ")
print("Quadrado: ", quadrado) 