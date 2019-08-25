print("Olá, em que turno você estuda?" )
turno= input("Digite M para Matutino, V para Vespertino ou N para Noturno: ")
print("="*100)
if turno=="M" or turno=="m":
    print('Bom dia!')
    print('"O homem não é nada além daquilo que a educação faz dele." -Immanuel Kant')
elif turno=="V" or turno=="v":
    print('Boa tarde!')
    print('"A educação tem raízes amargas, mas os seus frutos são doces." -Aristóteles')
elif turno=="N" or turno=="n":
    print('Boa noite!')
    print('"Educar é semear com sabedoria e colher com paciência." -Augusto Cury')
else:
    print('O turno escolhido é inválido.')
    print('Como dizia o sábio Raul Seixas: "Tente outra vez!" ')