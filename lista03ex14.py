num  = int(input("Digite quantos números deseja digitar: "))
valor = int(input("Agora digite um número: "))
maior = valor
menor = valor
soma = valor

for i in range(num-1):
    valor = int(input("Agora digite um número: "))
    soma = soma + valor
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print ("O maior número foi:", maior)
print ("O menor número foi:", menor)
print ("A soma de todos os números digitados foi:", soma)


                    
