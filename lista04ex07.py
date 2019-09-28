ch = input("Caractere: ")
pr = int(input("Proporção: "))
aux = pr
for linha in range(pr):
    for coluna in range(pr):
        if linha == coluna:
            print(ch*aux, end = "")
    print()
    aux = aux - 1