valor = int(input("Digite um valor para calcular o fatorial: "))
aux = 1
for F in range (valor, 1, -1):
    aux = F * aux
print ("O fatorial de", valor, "é", aux)