vetor = [""] * 10
par = []
for i in range(10):
    vetor[i]= int(input("Digite um valor inteiro: "))
    if vetor[i] % 2 == 0:
        par.append(vetor[i])
print("Dos valores que digitou", len(par), "são pares")