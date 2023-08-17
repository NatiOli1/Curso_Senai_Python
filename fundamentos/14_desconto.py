nome_do_produto = input("Nome do produto: ")
preco = input("Preço do produto: ")
desconto = input("Valor de desconto, número inteiro: ")

valor_desconto = float(preco) * (int(desconto)/100)
valor_produto_com_desconto = float(preco) - valor_desconto

print(f"O valor do produto é: {valor_produto_com_desconto:.2f}")