gabarito = [""]*10

for i in range(10):
    print("Professor digite a resposta da questão",i+1,"(Com A,B,C,D ou E):", end= " ")
    r = input()
    gabarito[i] = r

alunos = int(input("Digite a quantidade de alunos da turma: "))
acertos = [""]*alunos
acerto = 0
questao= 1

for i in range (alunos):
    print("Aluno Nº", i+1)
    for a in range(10):
        print("Questão",questao)
        resposta=input("Digite a sua resposta: ")
        if resposta == gabarito[a]:
            acerto = acerto + 1
        print("="*50)
        questao = questao + 1
    questao= 1
    acertos[i]= acerto
    acerto = 0

for i in range (alunos):
    print("Aluno nº", i+1,"acertou", acertos[i], "de 10 questões")