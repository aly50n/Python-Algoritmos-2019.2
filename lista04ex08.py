print("=" * 8, "Caixa Eletrônico", "=" * 8)
print()
soma = soma1 = 0
fim = "s"
fechar = "n"

while fechar == "n":
    while fim == "s":
        item = float(input("Digite o valor do item: R$ "))
        soma = soma + item
        fim = input("Há outro item para processar? [s/n]: ")
        print("_"*50)
    print("O valor da compra foi de: R$", soma)
    print("_"*50)
    fechar = input("Você deseja fechar o caixa? [s/n]: ")
    soma1 = soma + soma1
    if fechar == "n":
        print("="*50)
        fim = "s"
        soma = 0
print("")
print("Hoje foi apurado um total de: R$", soma1)