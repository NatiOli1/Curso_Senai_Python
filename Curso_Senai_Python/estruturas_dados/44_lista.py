numeros = [20, 56, 19, 40, 31]
print(f"A lista tem {len(numeros)} itens")

print(f"O index 2 da lista é o numero {numeros[2]}")

"""
Alteração de itens da lista
"""
# Atualizar item da lista
numeros[4] = 230
print(f"A lista tem os numeros {numeros}")

# Adiciona itens na lista
numeros.append(678)
print(f"A lista tem os numeros {numeros}")

# Remover item da lista pelo seu indice
del numeros[3]
print(f"A lista tem os numeros {numeros}")

# Remover útimo item da lista
numeros.pop()
print(f"A lista tem os numeros {numeros}")