numero = 1
contador_unidades = 0

while numero <= 100:
    if (numero % 2) != 0:
        print(f"O número {numero} é impar")
        contador_unidades += 1

    if contador_unidades == 10:
        break

    numero += 1
