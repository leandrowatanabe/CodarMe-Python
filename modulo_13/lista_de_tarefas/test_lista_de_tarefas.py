import unittest
from datetime import datetime

from tarefa import Tarefa
from lista_de_tarefas import ListaDeTarefas


class TestAdicionarTarefa(unittest.TestCase):
    def test_adiciona_tarefa_a_lista_de_tarefas(self):
        tarefa = Tarefa("Tarefa Teste")
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa)

        # self.assertEqual(lista.get_tarefas()[0], tarefa)
        self.assertIn(tarefa, lista.get_tarefas())


class TestGetTarefas(unittest.TestCase):
    def test_retorna_lista_de_tarefas_adicionadas(self):
        tarefa_um = Tarefa("Tarefa Teste 1")
        tarefa_dois = Tarefa("Tarefa Teste 2")
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)

        self.assertEqual(lista.get_tarefas(), [
            tarefa_um,
            tarefa_dois,
        ])

    def test_retorna_lista_de_tarefas_nao_concluida(self):
        tarefa_um = Tarefa("Tarefa Teste 1")
        tarefa_dois = Tarefa("Tarefa Teste 2")
        lista = ListaDeTarefas()

        tarefa_um.concluir()

        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)

        self.assertEqual(lista.get_tarefas(), [
            tarefa_dois,
        ])

    def test_retorna_lista_de_tarefas_concluida(self):
        tarefa_um = Tarefa("Tarefa Teste 1")
        tarefa_dois = Tarefa("Tarefa Teste 2")
        lista = ListaDeTarefas()

        tarefa_um.concluir()

        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)

        self.assertEqual(lista.get_tarefas(incluir_concluidas=True), [
            tarefa_um,
            tarefa_dois,
        ])
    
    def test_retorna_lista_de_tarefas_atrasadas(self):
        dt_atrasada = datetime(2022, 2, 10)
        tarefa_um = Tarefa("Tarefa Teste 1", data=dt_atrasada)
        tarefa_dois = Tarefa("Tarefa Teste 2", data=dt_atrasada)
        tarefa_tres = Tarefa("Tarefa Teste 3", data=datetime.today())
        lista = ListaDeTarefas()
        
        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)
        lista.adicionar_tarefa(tarefa_tres)

        self.assertEqual(lista.get_tarefas_atrasadas(), [
            tarefa_um,
            tarefa_dois,
        ])

    def test_retorna_lista_de_tarefas_para_hoje(self):
        dt_atrasada = datetime(2022, 2, 10)
        tarefa_um = Tarefa("Tarefa Teste 1", data=dt_atrasada)
        tarefa_dois = Tarefa("Tarefa Teste 2", data=dt_atrasada)
        tarefa_tres = Tarefa("Tarefa Teste 3", data=datetime.today())
        lista = ListaDeTarefas()
        
        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)
        lista.adicionar_tarefa(tarefa_tres)

        self.assertEqual(lista.get_tarefas_para_hoje(), [
            tarefa_tres
        ])

unittest.main()