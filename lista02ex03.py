nota1= float(input("Qual foi a primeira nota? "))
nota2= float(input("Qual foi a segunda nota? "))
media= (nota1+nota2)/2
if media >= 7:
    print("Parabéns!! sua média foi:", media, ", você está aprovado!")
elif media >= 5:
    print("Por pouco em! sua média foi:", media, ", você vai para a final!")
else:
    print("Poxa... a sua média foi:", media, ", infelizmente você está reprovado!")