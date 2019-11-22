def ler_vetor(vetor,tamanho):
    for i in range(tamanho):
        vetor[i] = input("Digite os elementos do vetor: ")

def inverter_vetor(vetor,tamanho):
    vetorinvertido = [""]*tamanho
    aux2 = tamanho - 1
    for i in range(tamanho):
        vetorinvertido[i] = vetor[aux2]
        aux2 = aux2-1
    return vetorinvertido

tamanho = int(input("Qual o tamanho do seu vetor? "))
vetor = [0]*tamanho

ler_vetor(vetor,tamanho)
print("Vetor Principal: ", vetor)

vetorinverso = inverter_vetor(vetor,tamanho)
print("Vetor Invertido: ", vetorinverso)