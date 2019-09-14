maior = menor = cont = somaveic = somaacidentes = soma2000 = 0
cidmaior = cidmenor = ''
for c in range(1,6):
    codigo      = int(input("Digite o código da cidade: "))
    veiculos    = int(input("Digite o número de veiculos de passeio: "))
    acidentes   = int(input("Número de acidentes de trânsito com vítimas: "))
    somaveiculos = somaveic + veiculos
    somaacidentes = somaacidentes + acidentes
    if acidentes > maior:
        maior = acidentes
        cidmaior = codigo

    if acidentes < menor or c == 1:
        menor = acidentes
        cidmenor = codigo

    if veiculos < 2000:
        soma2000 = soma2000 + acidentes
        cont = cont + 1
media5cidades = somaveic / c
media2000 = soma2000 / cont
print("O menor indice de acidentes de transito foi",menor, "acidente(s) na cidade de:", cidmenor)
print("O maior indice de acidentes de transito foi",maior, "acidente(s) na cidade de:", cidmaior)
print("Media de veiculos nas cincos cidades é de:", media5cidades)
print("Media de acidentes de trânsito nas cidades com menos de 2000 carros de passeio é de:", media2000) 