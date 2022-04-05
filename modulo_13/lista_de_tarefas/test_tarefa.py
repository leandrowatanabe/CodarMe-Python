import unittest
from datetime import datetime
from tarefa import Tarefa


class TestConcluir(unittest.TestCase):
    def test_concluir_tarefa_altera_concluido_para_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)

    def test_concluir_tarefa_concluida_mantem_concluida_como_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)


class TestAdiarNotificacao(unittest.TestCase):
    def test_adia_notificacao_em_N_minutos(self):
        dt_original = datetime(2022, 2, 10, 9, 10)  # year, month, day, hour, minute, second, millisecond
        tarefa = Tarefa("Estudar Python", data_notificacao=dt_original)
        tarefa.adiar_notificacao(15)

        dt_esperado = datetime(2022, 2, 10, 9, 25)
        self.assertEqual(tarefa.data_notificacao, dt_esperado)

class TestDescricao(unittest.TestCase):
    def test_inserir_descricao(self):
        descricao = "Descricao de teste"
        tarefa = Tarefa("Estudar Python", descricao=descricao)

        self.assertEqual(tarefa.descricao, descricao)

class TestAtrasado(unittest.TestCase):
    def test_tarefa_atrasada(self):
        dt_original = datetime(2022, 2, 10, 9, 10)
        tarefa = Tarefa("Estudar Python", data=dt_original)

        mensagem = tarefa.atrasada()

        self.assertEqual(mensagem, "Tarefa atrasada!")

    def test_tarefa_nao_atrasada(self):
        dt_original = datetime(2022, 5, 29, 9, 10)
        tarefa = Tarefa("Estudar Python", data=dt_original)

        mensagem = tarefa.atrasada()

        self.assertFalse(mensagem)

    def test_tarefa_sem_data(self):
        tarefa = Tarefa("Estudar Python")

        mensagem = tarefa.atrasada()

        self.assertFalse(mensagem)
        
unittest.main()