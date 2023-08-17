def calcula_gasto_combustivel(km_percorrido, valor_combustivel, media_km_veiculo=9.5):
    valor_total = (km_percorrido / media_km_veiculo) * valor_combustivel
    return valor_total

kms = 300
valor_gasolina = 5.99
media_veiculo = 12

resultado_com_media_padrao = calcula_gasto_combustivel(kms, valor_gasolina)

resultado_com_media = calcula_gasto_combustivel(kms, valor_gasolina, media_veiculo)

print(f"O gasto de combustível foi {resultado_com_media_padrao:.2f}")
print(f"\nO gasto do combustível foi {resultado_com_media}")
