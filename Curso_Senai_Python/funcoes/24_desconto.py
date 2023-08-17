def calcula_desconto(valor, desconto):
    valor_desconto = float(valor) * (int(desconto) / 100)
    valor_produto_com_desconto = float(valor) - valor_desconto
    return valor_produto_com_desconto

def mensagem(nome, valor, desconto, total):
    print(f"\n---Calculo do Desconto---")
    print(f"Nome do produto: {nome}")
    print(f"Preço do produto: R${valor}")
    print(f"Desconto do produto: {desconto}%")
    print(f"O valor final é: R${total}")

nome_do_produto = input("Nome do produto: ")
preco = input("Preço do produto: ")
desconto_do_produto = input("Valor de desconto, número inteiro: ")

resultado_desconto = calcula_desconto(valor=preco, desconto=desconto_do_produto)
mensagem(nome=nome_do_produto, valor=preco, desconto=desconto_do_produto, total=resultado_desconto)