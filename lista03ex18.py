cds=float(input("Quantos CD's você tem na sua coleção? "))
qntcds=0
soma=0
while qntcds < cds :
    valor=float(input('Digite o valor gasto em cada um deles: '))
    soma=soma+valor
    qntcds = qntcds + 1
media= soma / cds
print('O valor gasto foi de R$', soma,'reais')
print('A média do valor gasto em cada um deles foi de R$', media,'reais.')