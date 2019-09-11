pessoas=int(input("Digite quantas pessoas tem na sua turma: "))
soma=0
for i in range(pessoas):
    idade= int(input("Agora digite a idade de todos um de cada vez: "))
    soma= soma + idade
media = soma / pessoas
if media <= 25:
    print("A turma é Jovem!")
elif media >= 26 and media <= 60:
    print("A turma é Adulta!")
else:
    print("A turma é Idosa!")