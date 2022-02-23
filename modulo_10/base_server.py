from http.server import HTTPServer, BaseHTTPRequestHandler
import hashlib
import json

from usuario import Usuario

def hash_string(texto):
    """
    Recebe um texto como string e retorna a representação hash desse texto.
    Exemplo:
        hash_string("123") -> "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"
    """
    return hashlib.sha256(texto.encode()).hexdigest() 

user1 = Usuario("Alice","alice@codar.me",hash_string("12345")[0:5])
user2 = Usuario("Luiza","luiza@codar.me",hash_string("246810")[0:5])
user3 = Usuario("Leandro","leandro@codar.me",hash_string("aisuhduisa")[0:5])
user4 = Usuario("Anderson","anderson@codar.me",hash_string("sdasddads")[0:5])

usuarios = [user1, user2, user3, user4]

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/usuarios":
            # Enviar o status code da resposta: self.send_reponse(status_code)
            # Enviar cabeçalhos: self.send_header(nome, valor)
            # Finalizar cabeçalhos: self.end_headers()
            # Escrever dados para o "socket" (wfile): self.wfile.write(data)
            self.send_response(200)
            self.send_header("Content-Type","text/html; charset=utf8")
            self.end_headers()

            lista_usuarios = []
            for user in usuarios:
                lista_usuarios.append({
                        "id": user.id,
                        "nome": user.nome,
                        "email":user.email,
                        "senha":user.senha
                    })
            data=json.dumps(lista_usuarios).encode()
            self.wfile.write(data)
            print("Implementar!")

 
server = HTTPServer(('localhost', 8000), SimpleHandler)
server.serve_forever()