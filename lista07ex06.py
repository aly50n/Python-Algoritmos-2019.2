def ler_vetor(tamanho,vetor):
    for i in range(tamanho):
        vetor[i] = int(input("Digite um número inteiro: "))

def concatenar_vetores(vetor1,vetor2,tamanho):
    vetor_resultante = []
    for i in range(tamanho):
        vetor_resultante.append(vetor1[i]) 
    for i in range(tamanho):
        vetor_resultante.append(vetor2[i]) 
    return vetor_resultante

tamanho = int(input("Digite o tamanho dos seus vetores: "))
print("Primeiro Vetor: ")
vetor1 = [0] *tamanho
ler_vetor(tamanho,vetor1)
print("Segundo Vetor: ")
vetor2 = [0] *tamanho
ler_vetor(tamanho,vetor2)

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