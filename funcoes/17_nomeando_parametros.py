def calcula_aumento_salario(salario, percentul_aumento):
    salario_com_aumento = salario + (salario + percentul_aumento / 100)
    return salario_com_aumento

salario_atual = 2500
percentual = 10

salario_novo = calcula_aumento_salario(percentul_aumento=percentual,
                                       salario=salario_atual)

print(f"O salario agora é: {salario_novo}")