num=int(input('Digite o tamanho da lista :'))
lista=[0]*num
cont1=cont2=cont3=cont4=0

for i in range(num):
    lista[i]=int(input('Digite números :'))
    if lista[i] % 2 == 0:
        cont1= cont1 + 1
    else:
        cont2 = cont2 + 1
pares= [0] * cont1
impares=[0] * cont2
for i in range(num):
    if lista[i] % 2 == 0:
        pares[cont3]=lista[i]
        cont3=cont3+1
    else :
        impares[cont4]=lista[i]
        cont4=cont4 +1
print('Valores pares', pares)
print('Valores ímpares', impares)