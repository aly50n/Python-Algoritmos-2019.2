A = [1,0,5,-2,-5,7]
soma = A[0] + A[1] + A[5]
print("A soma dos índices das variáveis é:", soma)

A[4] = 100
for i in range(len(A)):
    print(A[i])