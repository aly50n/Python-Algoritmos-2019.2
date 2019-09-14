#Gabarito
q1= 'A'
q2= 'B' 
q3= 'C' 
q4= 'D' 
q5= 'E' 
q6= 'E' 
q7= 'D' 
q8= 'C' 
q9= 'B' 
q10= 'A'
prof= input("Professor o(a) Srº(a) deseja alterar o gabarito original? Se Sim digite (S) se Não digite (N) em MAIÚSCULO: ")
if prof == 'S':
    q1= input("Digite a resposta da questão 1 em MAIÚSCULO: ")
    q2= input("Digite a resposta da questão 2 em MAIÚSCULO: ")
    q3= input("Digite a resposta da questão 3 em MAIÚSCULO: ") 
    q4= input("Digite a resposta da questão 4 em MAIÚSCULO: ") 
    q5= input("Digite a resposta da questão 5 em MAIÚSCULO: ")
    q6= input("Digite a resposta da questão 6 em MAIÚSCULO: ")
    q7= input("Digite a resposta da questão 7 em MAIÚSCULO: ")
    q8= input("Digite a resposta da questão 8 em MAIÚSCULO: ")
    q9= input("Digite a resposta da questão 9 em MAIÚSCULO: ")
    q10= input("Digite a resposta da questão 10 em MAIÚSCULO: ")

contaluno= pontos = aux = soma = 0
print("Vamos começar a prova!")
nome= input("Nome do aluno: ")
for i in range(1, 11,1):
    print("Questão", i, ":")
    RespostaDoAluno=input("Digite a sua resposta em MAIÚSCULO: ")
    if i == 1 and RespostaDoAluno == q1:
        pontos= pontos+1
    if i == 2 and RespostaDoAluno == q2:
        pontos= pontos+1
    if i == 3 and RespostaDoAluno == q3:
        pontos= pontos+1
    if i == 4 and RespostaDoAluno == q4:
        pontos= pontos+1
    if i == 5 and RespostaDoAluno == q5:
        pontos= pontos+1
    if i== 6 and RespostaDoAluno == q6:
        pontos= pontos+1
    if i == 7 and RespostaDoAluno == q7:
        pontos= pontos+1
    if i == 8 and RespostaDoAluno == q8:
        pontos= pontos+1
    if i == 9 and RespostaDoAluno == q9:
        pontos= pontos+1
    if i == 10 and RespostaDoAluno == q10:
        pontos= pontos+1
print (nome,"teve",pontos,"pontos de acerto!")
contaluno= contaluno + 1
soma= soma + pontos
aux=pontos
cont=input("Ainda há outro aluno?(Responda com 'S' pra Sim ou 'N' pra Não em MAIÚSCULO): ")
pontmaior = aux
pontmenor = aux

if cont == 'N':
    print("A maior quantidade de acertos foi:", pontmaior)
    print("A menor quantidade de acertos foi:", pontmenor)
    print(contaluno, "Utilizaram o sistema!")
    média= soma / 10
    print("A média das notas da turma é de:", média)

while cont != 'N':
    print("Vamos começar a prova!")
    nome= input("Nome do aluno: ")
    pontos=0
    for i in range(1, 11,1):
        print("Questão", i, ":")
        RespostaDoAluno=input("Digite a sua resposta em MAIÚSCULO: ")
        if i == 1 and RespostaDoAluno == q1:
            pontos= pontos+1
        elif i == 2 and RespostaDoAluno == q2:
            pontos= pontos+1
        elif i == 3 and RespostaDoAluno == q3:
            pontos= pontos+1
        elif i == 4 and RespostaDoAluno == q4:
            pontos= pontos+1
        elif i == 5 and RespostaDoAluno == q5:
            pontos= pontos+1
        elif i== 6 and RespostaDoAluno == q6:
            pontos= pontos+1
        elif i == 7 and RespostaDoAluno == q7:
            pontos= pontos+1
        elif i == 8 and RespostaDoAluno == q8:
            pontos= pontos+1
        elif i == 9 and RespostaDoAluno == q9:
            pontos= pontos+1
        elif i == 10 and RespostaDoAluno == q10:
            pontos= pontos+1
    
    aux= pontos
    print (nome,"teve",pontos,"pontos de acerto!")
    contaluno= contaluno + 1
    soma= soma + pontos
    if aux < pontmenor:
        pontmenor = aux
        nomemenor = nome
    if aux > pontmaior:
        pontmaior = aux
        nomemaior = nome
    cont=input("Ainda há outro aluno?(Responda com 'S' pra Sim ou 'N' pra Não em MAIÚSCULO): ")

if cont == 'N':
    print("A maior quantidade de acertos foi:", pontmaior)
    print("A menor quantidade de acertos foi:", pontmenor)
    print(contaluno, "Alunos utilizaram o sistema!")
    média= soma / 10
    print("A média das notas da turma é de:", média)