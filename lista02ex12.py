numero = int(input("Digite um número inteiro menor que 1000(mil): "))
unidade = numero // 1
if  numero < 10:
    if unidade < 2:
        print(unidade, "Unidade")
    else:
        print(unidade, "Unidades")
if numero >= 10 and numero < 100:
    unidade = unidade % 10
    dezena = numero // 10
    if dezena < 2 and unidade < 2:
        print(dezena, "Dezena e", unidade, "Unidade")
    elif dezena < 2 and unidade >= 2:
        print(dezena, "Dezena e", unidade, "Unidades")
    elif dezena >= 2 and unidade < 2:
        print(dezena, "Dezenas e", unidade, "Unidade")
    else:
        print(dezena, "Dezenas e", unidade, "Unidades")
if numero >= 100 and numero < 1000:
    centena = numero // 100
    numero = numero - (centena * 100)
    dezena = numero // 10
    numero = numero - (dezena * 10)
    unidade = numero
    if centena == 1 and dezena == 1 and unidade < 2:
        print(centena, "Centena,", dezena, "Dezena e", unidade, "Unidade")
    elif centena == 1 and dezena == 1 and unidade >= 2:
        print(centena, "Centena,", dezena, "Dezena e", unidade, "Unidades")
    elif centena >= 2 and dezena >= 2 and unidade == 1:
        print(centena, "Centenas,", dezena, "Dezenas e", unidade, "Unidade")
    elif centena >= 2 and dezena == 1 and unidade >= 2:
        print(centena, "Centenas,", dezena, "Dezena e", unidade, "Unidades")
    elif centena == 1 and dezena >= 2 and unidade == 1:
        print(centena, "Centena,", dezena, "Dezenas e", unidade, "Unidade")
    elif centena >= 2 and dezena == 1 and unidade == 1:
        print(centena, "Centenas,", dezena, "Dezena e", unidade, "Unidade")
    elif centena == 1 and dezena < 1 and unidade >= 2:
        print(centena, "Centena,", dezena, "Dezenas e", unidade, "Unidades")
    elif centena >= 2 and dezena >= 2 and unidade < 1:
        print(centena, "Centenas,", dezena, "Dezenas e", unidade, "Unidades")
    elif centena >= 2 and dezena < 1 and unidade >= 2:
        print(centena, "Centenas,", dezena, "Dezenas e", unidade, "Unidades")
    elif centena == 1 and dezena >= 2 and unidade < 1:
        print(centena, "Centena,", dezena, "Dezenas e", unidade, "Unidades")
    elif centena >= 2 and dezena < 1 and unidade < 1:
        print(centena, "Centenas,", dezena, "Dezenas e", unidade, "Unidades")
    elif centena == 1 and dezena == 1 and unidade < 1:
        print(centena, "Centena,", dezena, "Dezena e", unidade, "Unidades")
    elif centena == 1 and dezena < 1 and unidade == 1:
        print(centena, "Centena,", dezena, "Dezenas e", unidade, "Unidade")
    elif centena >= 2 and dezena < 1 and unidade == 1:
        print(centena, "Centenas,", dezena, "Dezenas e", unidade, "Unidade")
    elif centena >= 2 and dezena == 1 and unidade < 1:
        print(centena, "Centenas,", dezena, "Dezena e", unidade, "Unidades")
    else:
        print(centena, "Centenas,", dezena, "Dezenas e", unidade, "Unidades")