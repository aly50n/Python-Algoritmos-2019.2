def criar_matriz(linha,coluna):
    matrizaux = []
    for i in range(linha):
        matrizaux.append([0]*coluna)
    return matrizaux

def ler_matriz(matriz,linha,coluna):
    for i in range(linha):
        for j in range(coluna):
            matriz[i][j] = int(input("Matriz Linha[" + str(i+1) + "], Coluna[" + str(j+1) + "]: "))

def quant_multiplos(linha,coluna,matriz,numero):
    contador = 0
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] % numero == 0:
                contador += 1
    return contador

def printar_matriz(matriz,linha,coluna):
    for i in range(linha):
        for j in range(coluna):
            print(matriz[i][j], end = " ")
        print()

linhas = int(input("Digite a quantidade de linhas da matriz: "))
colunas = int(input("Digite a quantidade de colunas da matriz: "))

matriz = criar_matriz(linhas,colunas)
ler_matriz(matriz, linhas, colunas)

print("=="*50)

num = int(input("Digite um número inteiro para saber quantos múltiplos dele aparecem na matriz: "))

qntmultiplos = quant_multiplos(linhas,colunas, matriz, num)

print("=="*50)

print("Matriz:")
printar_matriz(matriz,linhas,colunas)

print("Tem", qntmultiplos, "múltiplos de", num, "na matriz!")