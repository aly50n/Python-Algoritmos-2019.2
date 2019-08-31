saque = int(input("Qual o valor do saque? (Min: 10 e Máx: 600): "))
if saque >= 10 and saque <= 600:
    cem= saque//100
    saque = saque - cem * 100

    cinquenta = saque//50
    saque = saque - cinquenta * 50

    dez = saque//10
    saque= saque - dez * 10

    cinco = saque//5
    saque = saque - cinco * 5

    um = saque
print(cem, "notas de R$ 100,00")
print(cinquenta, "notas de R$ 50,00")
print(dez, "notas de R$ 10,00")
print(cinco, "notas de R$ 5,00")
print(um, "notas de R$ 1,00")
        

