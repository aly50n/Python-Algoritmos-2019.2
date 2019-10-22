quantidade = int(input("Digite a quantidade de elementos que quer nas listas: "))
lista1 = [""]*quantidade
lista2 = [""]*quantidade
for i in range(quantidade):
    lista1[i] = int(input("Digite um número inteiro para a lista 01: "))
for i in range(quantidade):
    lista2[i] = int(input("Digite um numéro inteiro para a lista 02: "))

print("="*50)

cont = 0
dif = 1

for j in range(quantidade):
    for h in range(quantidade):
        if lista1[j] == lista2[h]:
            cont = cont + 1
    if cont == quantidade:
        dif = 0
    if cont != quantidade:
        dif = 1
cont2 = 0
dif2 = 1

for j in range(quantidade):
    for h in range(quantidade):
        if lista2[j] == lista1[h]:
            cont2 = cont2 + 1
    if cont2 == quantidade:
        dif2 = 0
    if cont2 != quantidade:
        dif2 = 1

if dif or dif2 != 0:
    print("As listas contêm o seu conteúdo DIFERENTE!")
else:
    print("As listas contêm o seu conteúdo IGUAIS!")


print('='*50)

print("Conteúdo da Lista 01:", lista1)
print("Conteúdo da lista 02:", lista2)