def verificar_ordem(tamanho,vetor):
    aux = vetor[0]
    for i in range(tamanho):
        if vetor[i] >= aux:
            aux = vetor[i]
        else:
            return False
    return True

def ler_vetor(vetor,tamanho):
    for i in range(tamanho):
        vetor[i] = int(input("Digite números inteiros para o vetor: "))

tamanho = int(input("Qual o tamanho do seu vetor? "))

print("="*50)

vetor = [0]*tamanho
ler_vetor(vetor, tamanho)

print("="*50)

if verificar_ordem(tamanho,vetor):
    print("O vetor está em ordem crescente!")
else:
    print("O VETOR NÃO ESTÁ EM ORDEM CRESCENTE!")
print(vetor)