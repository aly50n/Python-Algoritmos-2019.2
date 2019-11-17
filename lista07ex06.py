def ler_vetor(tamanho):
    vetor = [""] *tamanho
    for i in range(tamanho):
        vetor[i] = int(input("Digite um número inteiro: "))
    return vetor

def concatenar_vetores(vetor1,vetor2,tamanho):
    vetor = []
    for i in range(tamanho):
        vetor.append(vetor1[i]) 
    for i in range(tamanho):
        vetor.append(vetor2[i]) 
    return vetor

tamanho = int(input("Digite o tamanho dos seus vetores: "))
print("Primeiro Vetor: ")
vetor1 = ler_vetor(tamanho)
print("Segundo Vetor: ")
vetor2 = ler_vetor(tamanho)

print("="*50)

print("Vetor 1")
print(vetor1)

print("="*50)

print("Vetor 2")
print(vetor2)

print("="*50)

vetor3 = concatenar_vetores(vetor1,(vetor2),tamanho)
print("Vetor 3")
print(vetor3)