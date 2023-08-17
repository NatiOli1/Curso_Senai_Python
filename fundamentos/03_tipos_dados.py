nome = "Aldredo"
sobrenome = "Alves"
idade = 40
esta_empregado = True
salario_hora = 5.29
dados = [1,3,"A", False]
dicionario = {"estudar": True, "tempo": "calor"}
nada = None

cidade = "Piracicaba"

print("A cidade ", cidade, " tem", len(cidade), " letras")

indice_nove = cidade[9]
print("O indice nove da palavra ", cidade, " é a letra ", indice_nove)

estado = "São Paulo"
cidade_estado = "A cidade de " + cidade + " fica no estado de " + estado

print(cidade_estado)

"""
Fazendo composição de string de forma inteligente, argumento:
%d para numeros inteiros
%s para string
%f numeros decimais
%f5.2 onde os numeros antes e depois do ponto formatam casas decimais
"""

print("Senhor %s tem %d anos, trabalha e ganha %5.2f de sálario"
      % (nome,idade, salario_hora))

"""
Fazendo da formatação da saída de outras formas
"""
print(f"Senhor {nome} tem {idade} anos, trabalha e ganha R$ {salario_hora} por hora")

print("Senhor {0} tem {1} anos trabalha e ganha R$ {2}"
      .format(nome,idade,salario_hora))