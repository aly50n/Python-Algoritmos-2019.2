print("Lhe farei 5 perguntas sobre o crime, me responda apenas com sim ou não:")
p1 = input("Telefonou para a vítima? ")
if p1 == "sim":
    r1 = 1
elif p1 == "não":
    r1 = 0
p2 = input("Esteve no local do crime? ")
if p2 == "sim":
    r2 = 1
elif p2 == "não":
    r2 = 0
p3 = input("Mora perto da vítima? ")
if p3 == "sim":
    r3 = 1
elif p3 == "não":
    r3 = 0
p4 = input("Devia para a vítima? ")
if p4 == "sim":
    r4 = 1
elif p4 == "não":
    r4 = 0
p5 = input("Já trabalhou com a vítima? ")
if p5 == "sim":
    r5 = 1
elif p5 == "não":
    r5 = 0
somaR= r1+r2+r3+r4+r5
if somaR == 2:
    print("Você é Suspeito(a)!")
elif somaR >= 3 and somaR <= 4:
    print("Você é Cúmplice!")
elif somaR == 5:
    print("Você é o Assassino!")
else:
    print("Você é Inocente.")