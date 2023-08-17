salario = input("Digite salario: ")
percentual_de_aumento = input("Digite o percentual_de_aumento: ")

aumento = (float(percentual_de_aumento)+float(salario))/100
valor_final = float(salario) + aumento

print(f"O aumento é de: {valor_final}")