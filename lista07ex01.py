def criar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        aux = int(input("Digite um número inteiro: "))
        lista.append(aux)
    return lista

def separar_par(tamanho,lista):
    par = []
    for i in range(tamanho):
        if lista[i] % 2 == 0:
            par.append(lista[i])
    return par

def separar_impar(tamanho,lista):
    impar = []
    for i in range(tamanho):
        if lista[i] % 2 != 0:
            impar.append(lista[i])
    return impar

tamanho = int(input("Digite o tamanho do vetor: "))
vetor = [0] * tamanho

for i in range(tamanho):
    vetor[i] = int(input("Digite um número inteiro: "))

par = separar_par(tamanho,vetor)
impar = separar_impar(tamanho,vetor)
print("="*50)
print("Vetor:", vetor)
print("="*50)
print("Números Pares do Vetor:", par)
print("="*50)
print("Números Impares do Vetor:", impar)