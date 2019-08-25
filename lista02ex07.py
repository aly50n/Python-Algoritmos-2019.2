print("Olá, em que turno você estuda?" )
turno= input("Digite M para Matutino, V para Vespertino ou N para noturno: ")
if turno=="M" or turno=="m":
    print("Bom dia!")
elif turno=="V" or turno=="v":
    print("Boa tarde!")
elif turno=="N" or turno=="n":
    print("Boa noite!")
else:
    print("O turno escolhido é inválido.")
