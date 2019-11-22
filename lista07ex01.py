def ler_vetor(tamanho,Vetor):
    for i in range(tamanho):
        Vetor[i] = int(input("Digite um número inteiro: "))

def separar_par(tamanho,Vetor):
    par = []
    for i in range(tamanho):
        if Vetor[i] % 2 == 0:
            par.append(Vetor[i])
    return par
    
def separar_impar(tamanho,Vetor):
    impar = []
    for i in range(tamanho):
        if Vetor[i] % 2 != 0:
            impar.append(Vetor[i])
    return impar

tamanho = int(input("Digite o tamanho do vetor: "))

vetor = [0] * tamanho
ler_vetor(tamanho,vetor)

par = separar_par(tamanho,vetor)
impar = separar_impar(tamanho,vetor)

print("="*50)
print("Vetor:", vetor)
print("="*50)
print("Números Pares do Vetor:", par)
print("="*50)
print("Números Impares do Vetor:", impar)