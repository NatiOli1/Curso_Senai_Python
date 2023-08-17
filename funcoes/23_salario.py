def calcula_salario(**kwargs):
    aumento = (float(kwargs.get("percentual")) + float(kwargs.get("salario"))) /100
    valor_final = float(kwargs.get("salario")) + aumento
    return valor_final

salario_atual = input("Digite salario: ")
percentual_de_aumento = input("Digite o percentual_de_aumento: ")

resultado_salario = calcula_salario(percentual=percentual_de_aumento,salario=salario_atual)

print(f"O aumento é de: {resultado_salario}")