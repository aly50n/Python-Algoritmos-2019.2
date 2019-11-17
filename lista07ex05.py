def ler_matriz(ordem):
    matriz = []
    for i in range(ordem):
        matriz.append([0]*ordem)
    print("Digite os valores da Matriz:")
    for i in range(ordem):
        for j in range(ordem):
            matriz[i][j] = int(input("Matriz Linha[" + str(i+1) + "], Coluna[" + str(j+1) + "]: "))
    return matriz

def trocar_valores_matrizes(matriz1,matriz2,ordem):
    aux2 = "s"
    while aux2 == "s":
        aux1 = 0
        linha = int(input("De que linha deseja trocar o elemento? "))
        coluna = int(input("De qual coluna deseja trocar o elemento? "))
        aux1 = matriz1[linha-1][coluna-1]
        matriz1[linha-1][coluna-1] = matriz2[linha-1][coluna-1]
        matriz2[linha-1][coluna-1] = aux1
        aux2 = input("Deseja trocar mais algum elemento da sua matriz[s/n]? ")

def printar_matriz(matriz,ordem):
    for i in range(ordem):
        for j in range(ordem):
            print(matriz[i][j], end = " ")
        print()

ordem = int(input("Digite a ordem das suas matrizes: "))

print("1ª Matriz")
matriz1 = ler_matriz(ordem)

print("2ª Matriz")
matriz2 = ler_matriz(ordem)

print("=="*50)

print("Matriz 1 Antes da troca")
printar_matriz(matriz1,ordem)

print("Matriz 2 Antes da troca")
printar_matriz(matriz2,ordem)

print("=="*50)

trocar_valores_matrizes(matriz1,matriz2,ordem)

print("=="*50)

print("Matriz 1 Depois da troca")
printar_matriz(matriz1,ordem)

print("Matriz 2 Depois da troca")
printar_matriz(matriz2,ordem)