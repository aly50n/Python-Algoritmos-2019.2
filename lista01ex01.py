print("Olá! Seja Bem Vindo Ao Calculador de Combustível")
print("Qual o seu nome?")
n=(input())
print("Vamos começar", n, "!")
c=float(input("Por favor digite o valor do litro de combustível em dinheiro-> "))
d=float(input("Agora, me informe o valor em dinheiro que deseja abastecer-> "))
total= d//c
l= total
print(n, "com este valor você obterá ", total, "litro(s) de combustível.")
print("Obrigado por usar este aplicativo", n, "! ;)")