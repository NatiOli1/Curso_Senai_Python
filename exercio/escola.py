from aluno import Aluno
from disciplina import Disciplina
from curso import Curso


curso_python = Curso("Programação em python")
gustavo = Aluno("Gustavo", 3892)
gustavo.atribuir_disciplina(Disciplina("Fundamentos", 10.0, 2.7))
gustavo.atribuir_disciplina(Disciplina("POO compython", 6.5, 7.6))

nadia = Aluno("Nadia", 1839)
nadia.atribuir_disciplina(Disciplina("Fundamentos", 9.6, 5.5))
nadia.atribuir_disciplina(Disciplina("POO compython", 7.0, 6.7))

curso_python.acionar_aluno(gustavo)
curso_python.acionar_aluno(nadia)


for aluno in curso_python.alunos:
    print(f"----Aluno nome: {aluno.nome}----")
    for disciplina in aluno.disciplinas:
        print(f"Disciplina: {disciplina.nome}")
        print(f"Notas: {disciplina.nota1}, {disciplina.nota2}")
        print(f"Média: {disciplina.media:.2f}")
        if disciplina.verificar_aprovado():
            print(f"Aluno {aluno.nome} aprovado")
        else:
            print(f"Aluno {aluno.nome} reprovado")

curso_eletrica = Curso("Elétrica")
aluno03 = Aluno("Aluno", 2832)
aluno03.atribuir_disciplina(Disciplina("CLP", 9.5, 5.5))
aluno03.atribuir_disciplina(Disciplina("Comandos", 3.5, 5.8))
curso_eletrica.acionar_aluno(aluno03)

curso_eletrica = Curso("Elétrica")
aluno04 = Aluno("Aluno", 5492)
aluno04.atribuir_disciplina(Disciplina("CLP", 8.5, 7.4))
aluno04.atribuir_disciplina(Disciplina("Comandos", 5.7, 7.6))
curso_eletrica.acionar_aluno(aluno04)


for aluno in curso_eletrica.alunos:
    print(f"----Aluno {aluno.nome}----")
    for disciplina in aluno.disciplinas:
        print(f"Notas: {disciplina.nota1}, {disciplina.nota2}")
        print(f"Média: {disciplina.media}")
        if disciplina.verificar_aprovado():
            print(f"Aluno aprovado com média: {disciplina.media}")
        else:
            print(f"Aluno reprovado com média: {disciplina.media}")