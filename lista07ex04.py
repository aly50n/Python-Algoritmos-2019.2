def verificar_ordem(tamanho,vetor):
    aux = vetor[0]
    for i in range(tamanho):
        if vetor[i] >= aux:
            aux = vetor[i]
        else:
            print("O vetor não está em ordem crescente!")
            return
    print("O vetor está em ordem crescente!")
    return

def ler_vetor(vetor,tamanho):
    for i in range(tamanho):
        vetor[i] = int(input("Digite números inteiros para o vetor: "))

tamanho = int(input("Qual o tamanho do seu vetor? "))

print("="*50)

vetor = [0]*tamanho
ler_vetor(vetor, tamanho)

print("="*50)

verificar_ordem(tamanho,vetor)
print(vetor)