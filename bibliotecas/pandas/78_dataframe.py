from pandas import DataFrame, Series

notas_alunos = {
    "alunos": Series(data=["aluno01", "aluno02", "aluno03"]),
    "nota1": Series(data=[2.9, 3.3, 1.5]),
    "nota2": Series(data=[6.7, 8.8, 3.6])
}

dataframe = DataFrame(notas_alunos)
print(f"Dados dos alunos \n{dataframe}")

filtro_1 = DataFrame(notas_alunos, index=[1, 2])
print(f"Filtro 1 \n{filtro_1}")

filtro_2 = DataFrame(notas_alunos, columns=["alunos", "nota2"])
print(f"Filtro 2: \n{filtro_2}")