from disciplina import Disciplina


class Aluno:
    def __init__(self, nome: str, matricula: int):
        self.nome = nome
        self.matricula = matricula
        self.disciplinas = []


    def atribuir_disciplina(self, disciplinas: Disciplina):
        self.disciplinas.append(disciplinas)