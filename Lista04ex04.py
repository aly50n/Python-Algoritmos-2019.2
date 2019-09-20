ch = input("Caractere: ")
for linha in range(8):
    for coluna in range(8,0,-1):
        if (linha + coluna) % 8 == 0:
            print(ch, ch, sep = '', end = '')
        else:
            print('', sep = '', end = '   ')
    print()