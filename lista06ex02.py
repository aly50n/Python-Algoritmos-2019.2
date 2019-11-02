matriz = []
for i in range(5):
    matriz.append([0]*5)

for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input("Digite o valor da matriz da Linha[" + str(i+1) + "], Coluna[" + str(j+1) + "]: "))
        
print("="*50)

for i in range(5):
    for j in range(5):
        print(matriz[i][j], end= " ")
    print()

print("="*50)

x = int(input("Qual o valor que deseja saber a localização na Matriz? "))
z = True

for i in range (5):
    for j in range (5):
        if x == matriz[i][j]:
            z = False
            print("O seu valor está localizado na Linha[", i+1, "] na Coluna[", j+1, "]")

if z:
    print("Valor não encontrado!")