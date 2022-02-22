class Usuario:
    id = 0

    def __init__(self, nome="", email="", senha=""):
        self.id = Usuario.id
        Usuario.id += 1
        self.nome = nome
        self.email = email
        self.senha = senha
        
    def imprime_usuario(self):
        print(f"{self.nome} ({self.email})")