turma=int(input('Digite a quantidade de turmas :')) 
soma=0
for i in range(turma) :
    alunos=int(input('Digite os números de alunos nas turmas :'))
    while alunos > 40 :
        print(' A sua turma não pode ter mais de 40 alunos. Vamos tentar novamente!')
        alunos=int(input('Digite outro número de alunos para essa turma: '))
        
    if alunos <= 40 :
        soma = soma + alunos
media= soma / turma
print('A média de alunos por turma é de', media, 'aluno(s).')