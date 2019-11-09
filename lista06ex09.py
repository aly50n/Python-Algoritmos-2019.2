matriz = []
for i in range(5):
    matriz.append([0]*10)

for i in range(5):
    for j in range(10):
        matriz[i][j] = input("Resposta do Aluno: [" + str(i+1) + "], Questão: [" + str(j+1) + "]: ")
        while matriz[i][j] != "a" and matriz[i][j] != "b" and matriz[i][j] != "c" and matriz[i][j] != "d":
            print("A resposta não coincide com o gabarito, tente novamente!")
            matriz[i][j] = input("Resposta do Aluno: [" + str(i+1) + "], Questão: [" + str(j+1) + "]: ")
    print("="*50)
gabarito = [0]*10

for i in range (10):
    gabarito[i] = input("Professor, qual a resposta correta da questão ["+ str(i+1) + "] (a,b,c ou d)? ")
    while gabarito[i] != "a" and gabarito[i] != "b" and gabarito[i] != "c" and gabarito[i] != "d":
            print("A resposta certa só pode ser a ou b ou c ou d. Tente novamente!")
            gabarito[i] = input("Professor, qual a resposta correta da questão ["+ str(i+1) + "] (a,b,c ou d)? ")

print("="*100)
print("Gabarito dos alunos: ")
for i in range(5):
    print("Aluno", i+1,":", end= "  ")
    for j in range(10):
        print(matriz[i][j], end= " ")
    print()

print("Gabarito do professor: ", gabarito)

aux = 0
resultado = [0]*5

for i in range(5):
    for j in range(10):
        if matriz[i][j] == gabarito[j]:
            aux = aux + 1
    resultado[i] = aux
    aux = 0

print("="*100)
print("Resultado:")

for i in range(5):
    print("Aluno[", str(i+1), "]:", resultado[i])