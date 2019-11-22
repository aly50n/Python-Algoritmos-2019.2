def ler_vetorStr(tamanho,vetor):
    for i in range(tamanho):
        vetor[i] = input("Digite a resposta da questão "+ str(i+1) + ": ")

def acertos_erros(respostas,gabarito,tamanho):
    acertos = 0
    erros = 0
    for i in range(tamanho):
        if respostas[i] == gabarito[i]:
            acertos= float(acertos + 1)
        else:
            erros= float(erros + 1)
    acerto_erro = [acertos,erros]
    return acerto_erro

tamanho = int(input("Quantas questões teve na sua prova? "))
respostas = [""]*tamanho
gabarito = [""]*tamanho

print("="*50)
print("DIGITE AS SUAS RESPOSTAS")
print("="*50)
ler_vetorStr(tamanho,respostas)
print("="*50)
print("AGORA DIGITE O GABARITO DA PROVA")
print("="*50)
ler_vetorStr(tamanho,gabarito)
print("="*50)
acertos_e_erros = acertos_erros(respostas,gabarito,tamanho)
percentual = (acertos_e_erros[0] * 100) / tamanho
print("Seu percentual de acertos foi de:",percentual, "% !" )