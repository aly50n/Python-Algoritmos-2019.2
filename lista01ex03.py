print("Seja Bem Vindo ao Calculador de dívida em atraso")
n=input("Por favor digite o nome do devedor-> ")
div=float(input("Digite o valor original da dívida-> R$ "))
dia=float(input("Digite a quantidade de dias de atraso no pagamento da dívida-> "))
mul=float(input("Defina o valor da multa por dia de atraso-> R$ "))
result=dia*mul+div
print(n, "está com uma dívida no valor total de R$", result)
print("Obrigado por usar este aplicativo ;)")