soma = 1
termos= int(input("Quantos termos deseja imprimir? "))
print(1, end= "   +   ")
for ntermo in range(2,termos+1,1):
    H = 1
    soma= soma + H / ntermo
    print(H, "/", ntermo, end= "")
    if ntermo < termos:
        print("   +   ", end= "")
print("")
print("A soma dos termos é igual a:", soma)