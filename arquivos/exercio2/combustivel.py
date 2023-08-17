import csv

distancia = 569
periodo_dias = 5
valor_gasolina = 5.19
valor_etanol = 3.39
cabecalho = []
dados_combustivel_calculado = []

with open("combustiveis.csv", "r", encoding="UTF8") as file:
    leitor = csv.reader(file, delimiter=",")
    for indice, linha in enumerate(leitor):
        if indice == 0:
            cabecalho = linha
            cabecalho.append("QTDE_LITROS_GASOLINA")
            cabecalho.append("QTDE_LITROS_ETANOL")
            cabecalho.append("TOTAL_GASOLINA")
            cabecalho.append("TOTAL_ETANOL")
            cabecalho.append("VALOR_TOTAL_GASOLINA")
            cabecalho.append("VALOR_TOTAL_ETANOL")
        else:
            # Calculando a qtde de litros por gasolina e etanol
            media_por_litro_gasolina = float(linha[4])
            media_por_litro_etanol = float(linha[5])
            qtde_litros_gasolina = int(distancia / media_por_litro_gasolina)
            qtde_litros_etanol = int(distancia / media_por_litro_etanol)

            linha_salvar = linha
            linha_salvar.append(qtde_litros_gasolina)
            linha_salvar.append(qtde_litros_etanol)

            # Calculando total de gasolina e etanol em reais
            total_gasolina = qtde_litros_gasolina * valor_gasolina
            total_etanol = qtde_litros_etanol * valor_etanol

            total_gasolina_formatado = f"R$ {total_gasolina:.2f}"
            total_etanol_formatado = f"R$ {total_etanol:.2f}"
            linha_salvar.append(total_gasolina_formatado)
            linha_salvar.append(total_etanol_formatado)

            # Calculando valor de dias por veiculo
            valor_diaria_veiculo = float(linha[2].replace("R$ ", ""))
            valor_dias_veiculo_total = periodo_dias * valor_diaria_veiculo

            # Calculando valor de km por veiculo
            valor_km_veiculo = float(linha[1].replace("R$ ", ""))
            valor_km_veiculo_total = distancia * valor_km_veiculo

            # Obtendo a informação do seguro
            valor_seguro_veiculo = float(linha[3].replace("R$ ", ""))

            # Calculando valor total para gasolina e veiculo
            # Considerando todas as variáveis, dias, km, seguro, total_gasolina
            valor_total_gasolina_veiculo = valor_dias_veiculo_total + \
                                           valor_km_veiculo_total + \
                                           valor_seguro_veiculo + \
                                           total_gasolina

            valor_total_gasolina_veiculo_formatada = f"R$ {valor_total_gasolina_veiculo:.2f}"
            linha_salvar.append(valor_total_gasolina_veiculo_formatada)

            # Considerando todas as variáveis, dias, km, seguro, total_etanol
            valor_total_etanol_veiculo = valor_dias_veiculo_total + \
                                           valor_km_veiculo_total + \
                                           valor_seguro_veiculo + \
                                           total_etanol

            valor_total_etanol_veiculo_formatada = f"R$ {valor_total_etanol_veiculo:.2f}"
            linha_salvar.append(valor_total_etanol_veiculo_formatada)

            dados_combustivel_calculado.append(linha_salvar)


# Criando o arquivo novo com a média
with open("combustiveis_calculado.csv", "w", encoding="UTF8", newline="") as arq:
    escritor = csv.writer(arq)
    escritor.writerow(cabecalho)

    for linha in dados_combustivel_calculado:
        escritor.writerow(linha)
