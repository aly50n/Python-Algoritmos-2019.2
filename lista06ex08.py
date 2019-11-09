matriz = []
for i in range(3):
    matriz.append([0]*6)

for i in range(3):
    for j in range(6):
        matriz[i][j] = float(input("Digite um valor Real para a Matriz - Linha[" + str(i+1) + "], Coluna[" + str(j+1) + "]: "))

print("="*100)
print()

print("Matriz:")
for i in range(3):
    for j in range(6):
        print(matriz[i][j], end= " ")
    print()

print("="*100)

somaimpar = 0

for i in range(3):
    for j in range(6):
        if (j+1) % 2 != 0:
            somaimpar = somaimpar + matriz[i][j]
print("A soma dos elementos das colunas ímpares é igual a: ", somaimpar)

print("="*100)

media = 0
auxsoma1 = 0
auxsoma2 = 0
for i in range(3):
            auxsoma1 = auxsoma1 + matriz[i][1]
            auxsoma2 = auxsoma2 + matriz[i][3]

media = (auxsoma2 + auxsoma1) / 6

print("A média aritmética dos elementos da segunda e quarta coluna é:", media)

print("="*100)

for i in range(3):
        matriz[i][5] = matriz[i][0] + matriz [i][1]

print("Matriz Modificada:")
for i in range(3):
    for j in range(6):
        print(matriz[i][j], end= " ")
    print()