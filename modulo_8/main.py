from administrador import Administrador
from usuario import Usuario

u = Usuario("Gabriel", "gabriel@exemplo.com")
a = Administrador("Admin", "admin@exemplo.com")
u.imprime_usuario()
# => "Gabriel (gabriel@exemplo.com)
a.imprime_usuario()
# => "Admin (admin@exemplo.com) – Administrador"
print(Usuario.quantidade)
# => 2