import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv("chuvas_jan_2023.csv", sep=";")

# Define o tamanho da figura
plt.figure(figsize=[20, 10])

# Passa as informações dos eixos x e y
plt.plot(dataframe["DIA"], dataframe["VALOR"])

plt.title("Informações de Chuvas Janeiro de 2023")
plt.xlabel("Dias")
plt.ylabel("Valores")

# Exibe todos os valores do eixo
plt.xticks(dataframe["DIA"])
# Plt utiliza(dataframe["Valor"]

# Colocar linhas
plt.grid(True)

plt.savefig("chuvas_jan_2023.png")
plt.close("all")