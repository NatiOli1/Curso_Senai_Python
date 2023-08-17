def calcula_litros(km_percorrido, media_kms):
    qtde_litros_necessaria = (float(km_percorrido) / float(media_kms))
    return qtde_litros_necessaria


def calcula_custo_viagem(km_percorrido, media_km, valor_combustivel):
    qtde_litros_necessaria = (float(km_percorrido) / float(media_km))
    custo = (float(qtde_litros_necessaria) * float(valor_combustivel))
    return custo


def mensagem(cidade1, cidade2, combustivel, km_percorridos, valor_combustivel,
             qtde_litros_necessaria, custo):
    print("\n---Resumo da viagem---")
    print(f"Cidade saída {cidade1}")
    print(f"Cidade destino {cidade2}")
    print(f"distancia {km_percorridos}")
    print(f"combustivel {combustivel}")
    print(f"valor_combustivel {valor_combustivel}")
    print(f"litros necessario {qtde_litros_necessaria}")
    print(f"custo {custo}")


cidade_saida: str = input("digite a cidade saída: ")
cidade_destino: str = input("digite a cidade destino: ")
distancia: float = input("digite a distancia: ")
media_km_Litro: float = input("digite  média de km/por litro do veículo: ")
combustivels: str = input("digite o combustível utilizado: ")
preco_combustivel: float = input("digite o valor do combustível: ")

resultado_custo = calcula_custo_viagem(media_km=media_km_Litro, valor_combustivel=preco_combustivel,
                                       km_percorrido=distancia, )
resultado_litros = calcula_litros(km_percorrido=distancia, media_kms=media_km_Litro)

mensagem(cidade1=cidade_saida, cidade2=cidade_destino, km_percorridos=distancia,
         combustivel=combustivels, valor_combustivel=preco_combustivel,
         qtde_litros_necessaria=resultado_litros, custo=resultado_custo)
