ordem= int(input("Qual a ordem da matriz? "))

matriz = []
for i in range(ordem):
    matriz.append([0]*ordem)

for i in range(ordem):
    for j in range(ordem):
        matriz[i][j] = int(input("Matriz Linha[" + str(i+1) + "], Coluna[" + str(j+1) + "]: "))

soma = 0

for n in range (ordem):
    for k in range (ordem):
        if k > n:
            soma = soma + matriz[n][k]

print("Matriz")
for i in range(ordem):
    for j in range(ordem):
        print(matriz[i][j], end= " ")
    print()

print("Soma dos elementos acima da diagonal principal:", soma)