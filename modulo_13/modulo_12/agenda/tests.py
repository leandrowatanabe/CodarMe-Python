from datetime import date
from django.test import TestCase, Client

from agenda.models import Evento, Categoria

# Create your tests here.

class TestPaginaInicial(TestCase):
    def test_lista_eventos(self):
        client = Client()
        response = client.get("/")
        self.assertTemplateUsed(response, "agenda/listar_eventos.html")

class TestListagemDeEventos(TestCase):
    def test_evento_com_data_de_hoje_e_exibido(self):
        categoria = Categoria.cria_categoria("Backend")

        evento = Evento.cria_evento(nome = "Aula de Python", categoria = categoria, local = "Sao Paulo", data = date.today())
    
        client = Client()
        response = client.get("/")
        self.assertContains(response, "Aula de Python")   
        self.assertEqual(list(response.context["eventos"]), [evento])
    
    def test_eventos_sem_data_sao_exibidos(self):
        categoria = Categoria.cria_categoria("Backend")

        evento = Evento.cria_evento(nome = "Aula de Python",categoria = categoria, local = "Sao Paulo")
    
        client = Client()
        response = client.get("/")
        self.assertContains(response, "Aula de Python")   
        self.assertContains(response, "A definir")   
        self.assertEqual(list(response.context["eventos"]), [evento])     

class TestMetodoDeCriarEvento(TestCase):
    def test_cria_evento(self):
        categoria = Categoria.cria_categoria("Backend")

        evento = Evento.cria_evento(nome="Aula de Python", categoria=categoria, link="https://")

        client = Client()
        response = client.get("/")

        self.assertContains(response, "Aula de Python")   
        self.assertEqual(list(response.context["eventos"]), [evento])

    def test_cria_evento_com_local_e_link(self):
        with self.assertRaises(ValueError, msg="Evento não pode possuir local e link."):
            Evento.cria_evento(nome="Aula de Python", categoria="Backend", link="https://", local="Sao Paulo")

class TestMetodoCriaCategoria(TestCase):
    def test_cria_categoria(self):
        nome = "Backend"
        categoria = Categoria.cria_categoria(nome)

        self.assertEqual(categoria.nome,nome)

    def test_cria_categoria_sem_nome(self):
        categoria = Categoria()

        with self.assertRaises(ValueError, msg="Categoria deve ter um nome"):
            categoria.cria_categoria("")