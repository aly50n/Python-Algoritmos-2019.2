print("Calcule o tempo em anos para poupar 1 Milhão de Reais!")
n=input("Olá, qual o seu nome? -> ")
print(n, "digite qual é o seu sálario mensal:")
s=float(input())
print("Agora, me informe quantas são as suas dispesas mensais:")
d=float(input())
sa=(s-d)*12
m=1000000
a=m//sa
print(n, "Você irá demorar", a, "anos para poupar 1 Milhão de Reais.")
print("Obrigado por usar este aplicativo :D")