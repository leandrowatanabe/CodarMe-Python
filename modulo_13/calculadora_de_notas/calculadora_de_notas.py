"""
CALCULADORA DE NOTAS
====================
1. Recebe uma turma, composta por uma lista de Alunos(nome, nota) e média para aprovar um aluno.
2. Calcula a média das notas da turma (get_media).
3. Qual a maior e menor nota (get_maior_nota, get_menor_nota).
4. Retorna alunos aprovados e reprovados (get_aprovados, get_reprovados).
5. Retorna lista de notas em representação de "letra".
    - nota == 10       =>    "A+"
    - 9 <= nota < 10   =>    "A"
    - 7 <= nota < 9    =>    "B"
    - 5 <= nota < 7    =>    "C"
    - 3 <= nota < 5    =>    "D"
    - 1 <= nota < 3    =>    "E"
    - 0 <= nota <
"""

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adiciona_nota(self, nota):
        self.notas.append(nota)
    
class CalculadoraDeNotas:
    def __init__(self):
        self._alunos = []

    def adiciona_aluno(self, aluno):
        self._alunos.append(aluno)

    def get_media(self):
  
        total = 0
        numero_notas = 0
        for aluno in self._alunos:
            soma = 0
            for nota in aluno.notas:
                soma+=float(nota)
                numero_notas+=1
            total += soma
        
        return total/numero_notas

    def get_maior_nota(self):
        maior = 0
        for aluno in self._alunos:
            for nota in aluno.notas:
                if nota > maior:
                    maior = nota
        
        return maior

    def get_menor_nota(self):
        menor = 10
        for aluno in self._alunos:
            for nota in aluno.notas:
                if nota < menor:
                    menor = nota
        
        return menor

    def get_aprovados(self, media):

        lista_de_aprovados = []

        for aluno in self._alunos:
            soma = 0
            for nota in aluno.notas:
                soma+=float(nota)

            if soma/len(aluno.notas)>=media:
                lista_de_aprovados.append(aluno)
        
        return lista_de_aprovados

    def get_reprovados(self, media):
        
        lista_de_reprovados = []

        for aluno in self._alunos:
            soma = 0
            for nota in aluno.notas:
                soma+=float(nota)

            if soma/len(aluno.notas)<media:
                lista_de_reprovados.append(aluno)

        
        return lista_de_reprovados

