def ler_vetor(vetor,tamanho):
    for i in range(tamanho):
        vetor[i] = input("Digite os elementos do vetor: ")

tamanho = int(input("Qual o tamanho do seu vetor? "))
vetor = [0]*tamanho

ler_vetor(vetor,tamanho)
print("Vetor principal: ", vetor)

vetor.reverse()
print("Vetor invertido: ", vetor)