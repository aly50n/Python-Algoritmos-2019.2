print("Sequência de Fibonacci")
n_termo = (int(input("Digite quantos termos você deseja mostrar? ")))
a1= 1
a2= 1
print (a1, a2, end = " ")
for i in range (n_termo - 2):
    a3= a1 + a2
    a1 = a2
    a2 = a3
    print(a3, end = " ")