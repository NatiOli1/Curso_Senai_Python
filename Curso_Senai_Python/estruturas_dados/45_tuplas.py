nomes = ("Aluno 01", "Aluno02", "Aluno03")
print(f"A tupla tem {len(nomes)} itens")
print(f"O index 2 da tupla é {nomes[2]}")

# Adicionar item na tupla
nomes += ("Aluno 04",)
print(f"Tupla alterada {nomes}")

# Remover item da tupla (imútavel) erro esperado
del nomes[1]
print(f"Tupla alterada {nomes}")
