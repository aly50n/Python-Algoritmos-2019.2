combustivel = input("Qual o tipo de combustível? Digite 'g' para Gasolina ou 'a' para Álcool:  ")
litros = float(input("Quantos litros de combustível foram vendidos? "))

if combustivel == "a":
    preço = 3.40
    if litros <= 20:
        desconto= (litros * preço) - (litros * preço * 3 / 100)
        print("O cliente pagará: ", desconto, "por", litros, "litro(s).")
    elif litros > 20:
        desconto= (litros*preço) - (litros * preço * 5 / 100)
        print("O cliente pagará: ", desconto, "por", litros, "litro(s).")
if combustivel == "g":
    preço = 4.50
    if litros <= 20:
        desconto= (litros * preço) - (litros * preço * 4 / 100)
        print("O cliente pagará: ", desconto, "por", litros, "litro(s).")
    elif litros > 20:
        desconto= (litros * preço) - (litros * preço * 6 / 100)
        print("O cliente pagará: ", desconto, "por", litros, "litro(s).")