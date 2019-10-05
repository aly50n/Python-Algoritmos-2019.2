vetor = [""] * 10
cont=0
for i in range(10):
    vetor[i]= int(input("Digite um valor inteiro: "))
    if vetor[i] % 2 == 0:
        cont= cont+1
print("Dos valores do seu vetor", cont, "são pares")