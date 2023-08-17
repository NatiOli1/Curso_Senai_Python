"""
Exemplo de criação de arquivo com python
MODO OPERAÇÃO
r   leitura
w   escrita
a   escrita, mas preserva o conteudo

"""

nome_arquivo = "numeros.txt"
arquivo = open(nome_arquivo, "w")

for numero in range(1, 181):
    arquivo.write(f"{numero}\n")
arquivo.close()