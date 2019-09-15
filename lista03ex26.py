soma=0
num= int(input("Quantos termos deseja imprimir? "))
for denominador in range(1,num+1,1):
    numerador = 2*denominador-1
    soma= soma+numerador/denominador
    print(denominador, "/", numerador, end= "   +   ")
print("")
print("A soma dos termos é igual a:", soma)