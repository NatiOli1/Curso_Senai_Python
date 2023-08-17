from aluno import Aluno


class Curso:
    def __init__(self, nome: str):
        self.nome = nome
        self.alunos = []


    def acionar_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)