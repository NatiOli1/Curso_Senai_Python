import os
import shutil

os.mkdir("escola")
alunos = ["Alfredo", "Silas", "Roberto", "Maria", "Helena", "Beatriz"]
nome_arquivo_txt = "escola/alunos.txt"

with open(nome_arquivo_txt, "w", encoding="UTF8") as file:
    for aluno in alunos:
        file.write(f"{aluno}\n")

nome_arquivo_zip = "escola/dados_para_download"

shutil.make_archive(nome_arquivo_zip, "zip", "escola")
