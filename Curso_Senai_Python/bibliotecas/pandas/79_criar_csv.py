import pandas as pd
from random import randrange

temperaturas = {}

for dia in range(1, 31):
    chave = "dia_" + str(dia)
    temperaturas[chave] = []
    for valor in range(1, 501):
        temp = randrange(5, 35)
        temperaturas[chave].append(temp)

dataframe = pd.DataFrame(temperaturas)
dataframe.to_csv("temperaturas.csv")

print(f"Informações basicas: \n{dataframe.head()}")
print(f"Informações com números de linhas definadas: \n{dataframe.tail(10)}")
print(f"Informações com estatíticas: \n{dataframe.describe()}")