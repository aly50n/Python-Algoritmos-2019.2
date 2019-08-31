ano = int(input("Digite um número que corresponda a um ano: "))
bissexto = ano/4
if bissexto == int(bissexto):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")