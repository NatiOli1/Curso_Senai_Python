class Disciplina:
    def __init__(self, nome: str, nota1: float, nota2: float):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = (self.nota1 + self.nota2) / 2


    def verificar_aprovado(self):
        if self.media < 5.5:
            return False
        else:
            return True