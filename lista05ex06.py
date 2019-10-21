vetor1 = [""]*10

for i in range (10):
    vetor1[i] = int(input("Digite um valor inteiro: "))
vetor2= [""]*10
aux= 0
for i in range (9,-1,-1):
    vetor2[aux] = vetor1[i]
    aux= aux + 1
print ("Vetor 1:", vetor1)
print ("Vetor 2:", vetor2)