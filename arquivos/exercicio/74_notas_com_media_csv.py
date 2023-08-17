import csv

cabecalho = []
dados_para_arquivo_alunos_com_media = []

with open("notas.csv", "r", encoding="UTF8", newline="") as file:
    leitor = csv.reader(file, delimiter=",")
    for indice, linha in enumerate(leitor):
        if indice == 0:
            cabecalho = linha
        else:
            aluno = linha[0]
            disciplina = linha[1]
            nota1 = int(linha[2])
            nota2 = int(linha[3])
            media = (nota1 + nota2) / 2
            nova_linha = [aluno, disciplina, nota1, nota2, media]
            dados_para_arquivo_alunos_com_media.append(nova_linha)


with open("74_notas_aprovados.csv", "w", encoding="UTF8", newline="") as file:
    escritor = csv.writer(file)
    cabecalho.append("Media")
    escritor.writerow(cabecalho)

    for linha in dados_para_arquivo_alunos_com_media:
        escritor.writerow(linha)

# 1) Criar o arquivo 74_notas_aprovados_csv
# 2) Verificar se a media é a maior ou igual a 5.5

with open("74_notas_aprovados_2.csv", "w", encoding="UTF8", newline="") as file:
    escritor = csv.writer(file)
    cabecalho.append("Aprovado")
    escritor.writerow(cabecalho)

    for conteudo in dados_para_arquivo_alunos_com_media:
        media = conteudo[4]
        if media > 5.5:
            conteudo.append("aprovado")
            escritor.writerow(conteudo)

with open("74_notas_aprovados_2.csv", "w", encoding="UTF8", newline="") as file:
    escritor = csv.writer(file)
    cabecalho[5] = "Reprovado"
    escritor.writerow(cabecalho)

    for linha in dados_para_arquivo_alunos_com_media:
        media = linha[4]
        if media < 5.5:
            linha.append("reprovado")
            escritor.writerow(linha)

with open("notas_poo.csv", "w", encoding="UTF8", newline="") as file:
    escritor = csv.writer(file)

    for linha in dados_para_arquivo_alunos_com_media:
        print(linha)
        disciplina = linha[1]
        if disciplina == "POO":
            escritor.writerow(linha)




