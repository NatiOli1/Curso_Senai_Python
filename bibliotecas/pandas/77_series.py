import pandas as pd

notas = [3.9, 2.0, 1.8, 7.8, 9.0]
serie = pd.Series(data=notas)
print(f"A informação contida na série é \n {serie}")
print(f"Estatísticas: {serie.describe()}")
print(f"Valor minimo: {serie.min()}")
print(f"Valor máximo: {serie.max()}")

notas_alunos = {
    "aluno01": 5.5,
    "aluno02": 7.5,
    "aluno03": 8.8,
    "aluno04": 3.5,
    "aluno05": 5.3,
}

serie_alunos = pd.Series(notas_alunos)
print(f"A informação contida na série é \n {serie_alunos}")
print(f"Estatísticas: {serie_alunos.describe()}")
print(f"Valor minimo: {serie_alunos.min()}")
print(f"Valor máximo: {serie_alunos.max()}")

estatistica_notas = serie_alunos.to_string(float_format="{:.6f}".format)
print(f"Saida formatada \n{estatistica_notas}")