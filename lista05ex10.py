vetor=[0]*10
for i in range(10):
    vetor[i]=int(input('Digite os valores do vetor: '))

print('Os valores repetidos no vetor são: ', end=' ')
cont= 0

for i in range(10):
    for j in range(i+1,10):
        if vetor[i] == vetor[j] :
            print( vetor[i], end= " ")
            cont = 1
if cont == 0:
    print('Não há valores repetidos!')