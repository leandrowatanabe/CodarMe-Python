from ast import Sub
from calculadora import somar, dividir, subtrair, multiplicar
import unittest


class TestSomar(unittest.TestCase):
    def test_soma_de_dois_numeros_inteiros(self):
        soma = somar(2, 4)
        self.assertEqual(soma, 6)

    def test_soma_de_numero_com_zero(self):
        self.assertEqual(somar(2, 0), 2)


class TestDividir(unittest.TestCase):
    def test_divide_numero_por_1_retorna_o_numero(self):
        self.assertEqual(dividir(10, 1), 10)

    def test_divide_por_zero_(self):
        self.assertEqual(dividir(10, 0), "Não é um número")

class TestSubtrair(unittest.TestCase):
    def test_subtrair_dois_numeros_inteiros_iguais(self):
        self.assertEqual(subtrair(2,2),0)
    
    def test_subtrair_dois_numeros_inteiros_primeiro_maior(self):
        self.assertEqual(subtrair(4,2),2)

    def test_subtrair_dois_numeros_inteiros_segundo_maior(self):
        self.assertEqual(subtrair(2,4),-2)    

    def test_subtrair_zero(self):
        self.assertEqual(subtrair(2,0),2)

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar_dois_numeros_inteiros(self):
        self.assertEqual(multiplicar(2,2),4)
    
    def test_multiplicar_por_um_retorna_o_numero(self):
        self.assertEqual(multiplicar(2,1),2)

    def test_multiplicar_por_zero(self):
        self.assertEqual(multiplicar(0,2),0)

unittest.main()