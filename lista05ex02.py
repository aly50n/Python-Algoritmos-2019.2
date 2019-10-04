conjunto = [""]*10
quadrado = []
for i in range(10):
    conjunto[i] = int(input("Digite um número real: "))
for i in range(10):
    b = conjunto[i] ** 2
    quadrado.append(b)
print("Conjunto: ", conjunto, end="    ")
print("Quadrado: ", quadrado) 