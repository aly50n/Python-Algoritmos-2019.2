mora= float(input("Quantos Kg de morango você deseja comprar? "))
maça= float(input("E quantos Kg de maçã?"))

kgmo= 2.50
kgma= 1.80
if mora > 5:
    kgmo = 2.20
if maça > 5:
    kgma= 1.50
total = (kgmo * mora) + (kgma * maça)
if (mora+maça) > 8 or total > 25.00:
    desconto = (total * 10) / 100
    total = total - desconto
    print("O valor da sua compra é: R$", total)
else:
    print("O valor da sua compra é: R$", total)