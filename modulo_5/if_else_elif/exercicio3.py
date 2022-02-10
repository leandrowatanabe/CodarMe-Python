USUARIO = "admin"
SENHA = "123123"

nome_usuario = input("Digite o nome do usuário: \n")
senha_usuario = input("Digite a senha do usuário: \n")

if(USUARIO==nome_usuario):
    if(SENHA==senha_usuario):
        print("Autenticacao foi bem-sucedida")
    else:
        print("Senha incorreta")
else:
    print("Usuario invalido")