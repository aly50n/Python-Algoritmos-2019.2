a= float(input("Digite o valor de A: "))
if a == 0:
   print("A equação não é de segundo grau.")
if a != 0:
    b= float(input("Digite o valor de B: "))
    c= float(input("Digite o valor de C: "))
    delta= b ** 2 - 4 * a * c
    if delta < 0:
        print("Não há raizes reais.")
    elif delta == 0:
        x= (-b) / (2*a)
        print("Há uma raiz real:", x)
    else:
        x1 = ((-b) + (delta**(1/2))) / (2 * a) 
        x2 = ((-b) - (delta**(1/2))) / (2 * a) 
        print("Há duas raizes reais:", x1, "e", x2)
