import unittest
from calculadora_de_notas import Aluno, CalculadoraDeNotas

class TestAluno(unittest.TestCase):
    def test_criar_aluno(self):
        aluno = Aluno(nome="teste")
    
        self.assertEqual(aluno.nome, "teste")
    
    def test_adiciona_nota(self):
        aluno1 = Aluno(nome = "aluno1")
        aluno1.adiciona_nota(10)
        aluno1.adiciona_nota(10)

        aluno2 = Aluno(nome = "aluno2")
        aluno2.adiciona_nota(10)
        aluno2.adiciona_nota(10)

        self.assertEqual(aluno1.notas, [
            10,
            10,
        ])

        self.assertEqual(aluno2.notas, [
            10,
            10,
        ])
    
class TestCalculadoraDeNotas(unittest.TestCase):
    def test_get_media(self):
        aluno1 = Aluno("aluno1")
        aluno2 = Aluno("aluno2")

        aluno1.adiciona_nota(10)
        aluno1.adiciona_nota(10)
        aluno1.adiciona_nota(10)
        aluno2.adiciona_nota(10)
        aluno2.adiciona_nota(10)
        aluno2.adiciona_nota(10)

        turma = CalculadoraDeNotas()
        
        turma.adiciona_aluno(aluno1)
        turma.adiciona_aluno(aluno2)

        self.assertEqual(turma.get_media(), 10)
    
    def test_get_maior_nota(self):
        aluno1 = Aluno("aluno1")
        aluno2 = Aluno("aluno2")

        aluno1.adiciona_nota(1)
        aluno1.adiciona_nota(2)
        aluno1.adiciona_nota(3)
        aluno2.adiciona_nota(4)
        aluno2.adiciona_nota(5)
        aluno2.adiciona_nota(6)

        turma = CalculadoraDeNotas()
        
        turma.adiciona_aluno(aluno1)
        turma.adiciona_aluno(aluno2)

        self.assertEqual(turma.get_maior_nota(), 6)

    def test_get_menor_nota(self):
        aluno1 = Aluno("aluno1")
        aluno2 = Aluno("aluno2")

        aluno1.adiciona_nota(1)
        aluno1.adiciona_nota(2)
        aluno1.adiciona_nota(3)
        aluno2.adiciona_nota(4)
        aluno2.adiciona_nota(5)
        aluno2.adiciona_nota(6)

        turma = CalculadoraDeNotas()
        
        turma.adiciona_aluno(aluno1)
        turma.adiciona_aluno(aluno2)

        self.assertEqual(turma.get_menor_nota(), 1)

    def test_get_aprovados(self):
        aluno1 = Aluno("aluno1")
        aluno2 = Aluno("aluno2")
        aluno3 = Aluno("aluno3")

        aluno1.adiciona_nota(1)
        aluno1.adiciona_nota(2)
        aluno1.adiciona_nota(3)

        aluno2.adiciona_nota(4)
        aluno2.adiciona_nota(5)
        aluno2.adiciona_nota(6)

        aluno3.adiciona_nota(5)
        aluno3.adiciona_nota(6)

        turma = CalculadoraDeNotas()

        turma.adiciona_aluno(aluno1)
        turma.adiciona_aluno(aluno2)
        turma.adiciona_aluno(aluno3)

        self.assertEqual(turma.get_aprovados(5), [aluno2, aluno3])

    def test_get_reprovados(self):
        aluno1 = Aluno("aluno1")
        aluno2 = Aluno("aluno2")
        aluno3 = Aluno("aluno3")

        aluno1.adiciona_nota(1)
        aluno1.adiciona_nota(2)
        aluno1.adiciona_nota(3)

        aluno2.adiciona_nota(4)
        aluno2.adiciona_nota(5)
        aluno2.adiciona_nota(6)

        aluno3.adiciona_nota(5)
        aluno3.adiciona_nota(6)

        turma = CalculadoraDeNotas()

        turma.adiciona_aluno(aluno1)
        turma.adiciona_aluno(aluno2)
        turma.adiciona_aluno(aluno3)

        self.assertEqual(turma.get_reprovados(5), [aluno1])

unittest.main()