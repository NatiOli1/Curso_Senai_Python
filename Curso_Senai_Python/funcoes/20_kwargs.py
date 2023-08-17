def calcula_salario(**kwargs):
    desconto_inss = kwargs.get("inss") / 100
    desconto_plano_de_saude = kwargs.get("planos")
    total_descontos = desconto_inss + desconto_plano_de_saude
    salario_liquido = kwargs.get("salario_base") - total_descontos
    return salario_liquido

salario_atual = 5000
INSS = 8
plano_s = 129.90
salario_a_recebern = calcula_salario(salario_base=salario_atual, inss=INSS, planos=plano_s)