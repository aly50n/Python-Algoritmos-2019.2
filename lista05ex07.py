vetor1=[0] * 20
vetor2=[0] * 20

for i in range(20) :
    vetor1[i]=int(input('Digite os valores do primeiro vetor :'))

for i in range(20) :
    vetor2[i]=int(input('Digite valores do segundo vetor :'))

cont = 0
cont2 = 0
aux = [0]*40

for g in range(20) :
    for h in range(20):
        if vetor1[g] == vetor2[h]:
            cont = 1
    if cont == 0:
        cont2 = cont2 +1
        aux[cont2-1] = vetor1[g]
    if cont != 0:
        cont = 0

cont3= cont2

for i in range(20) :
    for j in range(20):
        if vetor2[i] == vetor1[j]:
            cont = 1
    if cont == 0:
        cont3 = cont3 +1
        aux[cont3-1] = vetor2[i]
    if cont != 0:
        cont = 0

vetor3 = [0]* (cont3)
for j in range (cont3):
    vetor3[j] = aux[j]

vetor4 = [0]*20
for k in range(20):
    vetor4[k] = vetor1[k] + vetor2[k]

vetor5 = [0]*20
for k in range(20):
    vetor5[k] = vetor1[k] * vetor2[k]

print("Vetor 01:", vetor1)
print("Vetor 02:", vetor2)
print("Vetor 03 (Diferença):", vetor3)
print("Vetor 04 (Soma):", vetor4 )
print("Vetor 05 (Multiplicação):", vetor5)