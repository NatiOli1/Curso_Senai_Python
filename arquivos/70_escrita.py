import csv

nome_arquivo = "docs/temperaturas.csv"
cabecalho = ["DIA DE SEMANA", "TEMPERATURA"]
dados = [
    {"dia": "segunda-feira", "temperatura": "10.0"},
    {"dia": "terça-feira", "temperatura": "23.4"},
    {"dia": "quarta-feira", "temperatura": "31.0"},
    {"dia": "quinta-feira", "temperatura": "14.9"},
    {"dia": "sexta-feira", "temperatura": "25.5"},
    {"dia": "sábado", "temperatura": "23.8"},
    {"dia": "domingo", "temperatura": "12.4"},

]

with open(nome_arquivo, "a", encoding="UTF8", newline="") as file:
    escritor = csv.writer(file)
    escritor.writerow(cabecalho)

    for dado in dados:
        dia = dado.get("dia")
        valor = dado.get("temperatura")
        escritor.writerow([dia, valor])