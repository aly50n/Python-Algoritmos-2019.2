div = float(input("Digite o valor da divida: "))
parcela = 1
print("Valor da divida: ", end="  ")
print("Valor do juros: ", end="  ")
print("Quantidade de parcelas: ", end="  ")
print("Valor da parcela: ")
for i in range(5):
    if parcela == 1:
        juros = 1
        vjuros = 0
    elif parcela == 4:
        parcela = 3
        juros = 1.10
    elif parcela == 7 or parcela == 6:
        parcela = 6
        juros = 1.15
    elif parcela == 10 or parcela == 9:
        parcela = 9
        juros = 1.20
    elif parcela == 13 or parcela == 12:
        parcela = 12
        juros = 1.25
    vjuros = div * (juros - 1)
    divCjuros = div * juros
    valor_parcela = divCjuros / parcela
    print("R$",divCjuros, end="            ")
    print(vjuros, end="                  ")
    print(parcela, end="                        ")
    print("R$ ",valor_parcela)
    parcela = parcela + 3