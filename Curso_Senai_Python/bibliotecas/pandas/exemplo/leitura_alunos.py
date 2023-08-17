import pandas as pd

dados = pd.read_csv("alunos.csv", skiprows=8, sep=";", encoding="latin-1", on_bad_lines="skip")

for index, row in dados.iterrows():
    Nota1 = (row.get('NOTA 1')).replace(";", ",", ".")
    Nota2 = str(row.get('NOTA 2')).replace(",", ".")