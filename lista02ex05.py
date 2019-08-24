p1= float(input("Qual o preço do primeiro produto? "))
p2= float(input("Qual o preço do segundo produto? "))
p3= float(input("Qual o preço do terceiro produto? "))
if p1 <= p2 and p1 <= p3:
    print("Compre o primeiro produto, ele custa apenas: R$", p1)
elif p2 <= p1 and p2 <= p3:
    print("Compre o segundo produto, ele custa apenas: R$", p2)
else:
    print("Compre o terceiro produto, ele custa apenas: R$", p3)