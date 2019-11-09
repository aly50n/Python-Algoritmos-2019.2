matriz_1 = []

for i in range(4):
    matriz_1.append([0]*4)

for i in range(4):
    for j in range(4):
        matriz_1[i][j] = int(input("Digite o valor da Matriz 1 da Linha[" + str(i+1) + "], Coluna[" + str(j+1) + "]: "))

print("="*50)

matriz_2 = []

for i in range(4):
    matriz_2.append([0]*4)

for i in range(4):
    for j in range(4):
        matriz_2[i][j] = int(input("Digite o valor da Matriz 2 da Linha[" + str(i+1) + "], Coluna[" + str(j+1) + "]: "))

matriz_3 = []

for i in range(4):
    matriz_3.append([0]*4)

for i in range(4):
    for j in range(4):
        if matriz_1[i][j] >= matriz_2[i][j]:
            matriz_3[i][j] = matriz_1[i][j]
        else:
            matriz_3[i][j] = matriz_2[i][j]

print("="*50)
print("Matriz 1")
for i in range(4):
    for j in range(4):
        print(matriz_1[i][j], end= " ")
    print()

print()
print("Matriz 2")
for i in range(4):
    for j in range(4):
        print(matriz_2[i][j], end= " ")
    print()

print()
print("Matriz 3")  
for i in range(4):
    for j in range(4):
        print(matriz_3[i][j], end= " ")
    print()