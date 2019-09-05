print("Bem Vindo ao Gerador de Tabuadas!")
num = int(input("Digite qualquer número inteiro para gerarmos sua tabuada do 1 ao 10: "))
aux = 1
while aux <= 10:
    calculo = num * aux
    print(num, "*", aux, "=", calculo)
    aux = aux + 1