usuario = input("Digite seu nome de usuário: ")
senha = input ("Agora digite uma senha: ")
while usuario == senha:
    print("A sua senha deve ser diferente do seu nome de usuário, vamos tentar novamente!")
    usuario = input("Digite o seu nome de usuário: ")
    senha = input ("Agora digite uma senha: ")
print("Tudo certo! Registro completo!")