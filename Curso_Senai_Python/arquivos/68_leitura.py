with open("docs/alunos.txt", "r") as file:
    for aluno in file.readlines():
        print(f"\nNome do aluno: {aluno}")