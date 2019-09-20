ch = input("Caractere: ")
for linha in range(8):
    for coluna in range(8):
        if (linha + coluna) % 2 == 0:
            print(ch, ch, sep = ch, end = ch)
        else:
            print(ch, sep = ch, end = ch)
    print()