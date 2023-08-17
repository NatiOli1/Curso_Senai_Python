def calcula_media_aluno(nome, disciplina, nota1, nota2, faltas):
    media_aritmetica = (nota1 + nota2) / 2
    print("\n---Informação do Aluno---")
    print(f"Aluno: {nome}")
    print(f"Disciplina: {disciplina}")
    print(f"Média: ")
    print(f"Faltas: {faltas}")
    return media_aritmetica

N1 = float(input("Digite a nota 1: "))
N2 = float(input("Digite a nota 2: "))
falta = int(input("Digite a quantidades de faltas: "))
aluno = str(input("Digite o nome do Aluno: "))
materia = str(input("Digite a disciplina: "))

resultado_media = calcula_media_aluno(nome=aluno, disciplina=materia, nota1=N1,
                                      nota2=N2, faltas=falta)

if resultado_media >= 6.5 and falta <= 3:
    print("Você está aprovado")
elif falta == 4:
    print("Está de recuperação")
else:
    print("Você está reprovado")