ch = input("Caractere: ")
pr= int(input("Proporção(Deve ser maior ou igual a 6): "))
while pr < 6:
    print("Erro! Preste atenção na proporção!")
    pr= int(input("Proporção(Deve ser maior ou igual a 6): "))
a1= a2 = pr - 2

for linha in range(pr//2):
    for coluna in range(pr//2):
        if linha == coluna:
            print(ch, ch, sep = "", end = "")
            print("  "*a1, ch, ch, sep = "", end = "")
        else:
            print("", sep = "", end = "  ")
    a1 = a1 - 2
    print()

for coluna in range(pr//2):
    for coluna in range (pr//2):
        if linha == coluna:
            print(" "*a2, ch, ch, sep = "", end = "")
            print("  "*(a1+2), ch, ch, sep = "", end = "")
            a2 = a2 - 2
    a1 = a1+2
    print()