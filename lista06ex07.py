ordem= int(input("Qual a ordem da matriz? "))

matriz = []
for i in range(ordem):
    matriz.append([0]*ordem)

for i in range(ordem):
    for j in range(ordem):
        matriz[i][j] = int(input("Matriz Linha[" + str(i+1) + "], Coluna[" + str(j+1) + "]: "))

soma = 0
aux = ordem
aux = aux - 1
for n in range (ordem):
    soma = soma + matriz[n][aux]
    aux = aux - 1

print("Matriz")
for i in range(ordem):
    for j in range(ordem):
        print(matriz[i][j], end= " ")
    print()

print("A soma dos elementos da diagonal secundária é =", soma)