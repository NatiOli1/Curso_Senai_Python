combustivel = input("digite o combustível utilizado: ")
distancia = int(input("digite a distância: "))
media_km_Litro = int(input("digite km/por litro de gasolina ultizados: "))
valor_c = 0.0

if combustivel == "gasolina":
    valor_c = 5.75
elif combustivel == "etanol":
    valor_c = 4.87
else:
    valor_c = float(input("Digite o valor do combustivel: "))
    
custo_viagem = (distancia/media_km_Litro) * valor_c

print(f"A viagem custou R$:{custo_viagem:.2f}")