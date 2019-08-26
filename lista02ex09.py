print("1 - Domingo, 2 - Segunda-Feira, 3 - Terça-Feira, 4 - Quarta=Feira, 5 - Quinta-Feira, 6 - Sexta-Feira, 7- Sábado.")
num= int(input("Digite um número de 1 a 7 que corresponde ao dia da semana: "))
if num==1:
    print("Você escolheu Domingo.")
elif num==2:
    print("Você escolheu Segunda-Feira.")
elif num==3:
    print("Você escolheu Terça-Feira.")
elif num==4:
    print("Você escolheu Quarta-Feira.")
elif num==5:
    print("Você escolheu Quinta-Feira.")
elif num==6:
    print("Você escolheu Sexta-Feira.")
elif num==7:
    print("Você escolheu Sábado.")
else:
    print("O número digitado é inválido.")