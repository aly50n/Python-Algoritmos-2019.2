maior = 0
vetor = [""]*10
posiçao= 0
b=int(input("Digite um número inteiro: "))
vetor[0]= b
maior = vetor[0]
for i in range(1,10,1):
    b=int(input("Digite um número inteiro: "))
    vetor[i]= b
    if vetor[i] >= vetor[posiçao]:
        maior=vetor[i]
        posiçao = i
print("O vetor é:", vetor)
print("O maior elemento do vetor é:", maior, "e o seu indíce é:", posiçao)
