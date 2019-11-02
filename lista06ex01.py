matriz = []
for i in range(4):
    matriz.append([0]*4)
cont = 0
for i in range(4):
    for j in range(4):
        matriz[i][j] = int(input("Digite o valor da matriz da Linha[" + str(i+1) + "], Coluna[" + str(j+1) + "]: "))
        if 10 < matriz[i][j]:
            cont = cont + 1
print("="*50)
for i in range(4):
    for j in range(4):
        print(matriz[i][j], end= " ")
    print()
print("Na matriz existem ",cont, "números maiores que 10.")



