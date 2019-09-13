print('Lojas Tabajara')
preço=float(input('Produto 1 : R$ '))
soma=0
dinheiro=0
troco=0
aux=preço
cont=1
while preço != 0 :
    cont=cont +1
    print('Produto', cont,end=' ')
    preço=float(input(': R$ '))
    soma= soma + preço
    if preço == 0 :
        print('Total:      R$', soma + aux)
        dinheiro=float(input('Dinheiro:   R$ '))
        troco=dinheiro - soma - aux
        print('Troco:      R$', troco)