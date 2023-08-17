combustivel = input("digite o combustível utilizado: ")
distancia = int(input("digite a distância: "))
media_km_Litro1 = int(input("digite km/por litro de gasolina ultizados: "))
media_km_Litro2 = int(input("digite km/por litro de etanol ultizados: "))

valor_g = 5.75
valor_e = 4.87

custo_g = (distancia/media_km_Litro1) * valor_g
custo_e = (distancia/media_km_Litro2) * valor_e

if custo_g < custo_e:
    print(f"A gasolina rendera mais que o Etanol")
else:
    print(f"O etanol rendera mais que a Gasolina")